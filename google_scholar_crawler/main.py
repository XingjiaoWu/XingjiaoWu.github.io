import os, re, json, time
from datetime import datetime

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"


def parse_citations(html: str):
    # "Citations" 行的第一个 gsc_rsb_std 单元格为总被引
    cells = re.findall(r'<td class="gsc_rsb_std">([\d,]+)</td>', html)
    if not cells:
        raise RuntimeError('citation cells not found (captcha or layout change?)')
    return int(cells[0].replace(',', '')), cells


def fetch_light():
    import httpx
    url = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
    r = httpx.get(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"},
                  cookies={"CONSENT": "YES+cb"}, timeout=30, follow_redirects=True)
    print(f'light fetch: HTTP {r.status_code}, {len(r.text)} bytes', flush=True)
    cited, cells = parse_citations(r.text)
    hindex = int(cells[4].replace(',', '')) if len(cells) > 4 else None
    return cited, hindex


def fetch_scholarly():
    from scholarly import scholarly
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=['basics', 'indices', 'counts'])
    return int(author['citedby']), author.get('hindex')


cited, hindex, source = None, None, None
for attempt in range(1, 5):
    try:
        cited, hindex = fetch_light(); source = 'light'; break
    except Exception as e:
        print(f'light attempt {attempt} failed: {type(e).__name__}: {e}', flush=True)
        time.sleep(20)
    try:
        cited, hindex = fetch_scholarly(); source = 'scholarly'; break
    except Exception as e:
        print(f'scholarly attempt {attempt} failed: {type(e).__name__}: {e}', flush=True)
        time.sleep(30)

if cited is None:
    raise SystemExit('all fetch attempts failed')

print(f'OK source={source} citations={cited} hindex={hindex}', flush=True)
os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as f:
    json.dump({'citedby': cited, 'hindex': hindex, 'updated': str(datetime.now()), 'source': source}, f, ensure_ascii=False)
with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump({"schemaVersion": 1, "label": "citations", "message": str(cited)}, f, ensure_ascii=False)
