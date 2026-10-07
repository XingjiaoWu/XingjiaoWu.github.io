import os
import time
import json
from datetime import datetime
from scholarly import scholarly
from scholarly.proxy import ProxyGenerator

SCHOLAR_ID = os.environ['GOOGLE_SCHOLAR_ID']


def crawl_direct():
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
    return author


def crawl_via_proxy():
    pg = ProxyGenerator()
    if pg.FreeProxies():
        scholarly.use_proxy(pg)
    return crawl_direct()


author = None
for attempt in range(1, 7):
    for label, fn in (('direct', crawl_direct), ('proxy', crawl_via_proxy)):
        try:
            print(f'attempt {attempt} ({label})...', flush=True)
            author = fn()
            break
        except Exception as e:
            print(f'attempt {attempt} ({label}) failed: {type(e).__name__}: {e}', flush=True)
            time.sleep(30)
    if author is not None:
        break

if author is None:
    raise SystemExit('All crawl attempts failed')

author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']: v for v in author['publications']}
print(json.dumps(author, indent=2, ensure_ascii=False))

os.makedirs('results', exist_ok=True)
with open('results/gs_data.json', 'w') as f:
    json.dump(author, f, ensure_ascii=False)

shields = {
    "schemaVersion": 1,
    "label": "citations",
    "message": f"{author['citedby']}",
}
with open('results/gs_data_shieldsio.json', 'w') as f:
    json.dump(shields, f, ensure_ascii=False)

print(f"OK: citations={author['citedby']} hindex={author.get('hindex')}")
