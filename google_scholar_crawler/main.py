import os, re, json
from datetime import datetime
import httpx

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
ORCID = os.environ.get('ORCID', '0000-0001-9146-051X')
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


def fetch_scholar():
    """直接抓取 Google Scholar 个人页（数据中心 IP 常被 403，快速失败）"""
    url = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
    for _ in range(2):
        r = httpx.get(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"},
                      cookies={"CONSENT": "YES+cb"}, timeout=15, follow_redirects=True)
        cells = re.findall(r'<td class="gsc_rsb_std">([\d,]+)</td>', r.text)
        if cells:
            cited = int(cells[0].replace(',', ''))
            h = int(cells[4].replace(',', '')) if len(cells) > 4 else None
            return cited, h, 'google-scholar'
    raise RuntimeError('scholar blocked')


def fetch_openalex():
    """OpenAlex 兜底：免费、无密钥、稳定（口径与 Scholar 略有差异）"""
    r = httpx.get(f"https://api.openalex.org/authors/orcid:{ORCID}",
                  headers={"User-Agent": "homepage-stats/1.0 (mailto:xjwu@pharm.ecnu.edu.cn)"}, timeout=30)
    r.raise_for_status()
    d = r.json()
    return int(d['cited_by_count']), d.get('summary_stats', {}).get('h_index'), 'openalex'


cited = hindex = source = None
err = None
try:
    cited, hindex, source = fetch_scholar()
except Exception as e:
    err = f'scholar: {type(e).__name__}: {e}'
    print(err, flush=True)
try:
    if cited is None:
        cited, hindex, source = fetch_openalex()
except Exception as e:
    print(f'openalex: {type(e).__name__}: {e}', flush=True)

if cited is None:
    raise SystemExit(f'all sources failed; last error: {err}')

label = "citations" if source == 'google-scholar' else "citations (OpenAlex)"
print(f'OK source={source} cited={cited} h={hindex}', flush=True)

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as f:
    json.dump({'citedby': cited, 'hindex': hindex, 'source': source,
               'updated': str(datetime.now()), 'last_scholar_error': err}, f, ensure_ascii=False)
with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump({"schemaVersion": 1, "label": label, "message": str(cited)}, f, ensure_ascii=False)
