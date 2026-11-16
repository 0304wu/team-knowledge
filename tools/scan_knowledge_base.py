import argparse, hashlib, re
from pathlib import Path
from datetime import date

EXTS = {'.pdf','.docx','.doc','.md','.txt','.pptx','.xlsx','.csv','.py','.r','.ipynb'}

def sha256(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser(description='Scan a team knowledge base and update a catalog report.')
    ap.add_argument('root'); ap.add_argument('--catalog',default='00_index/catalog.md'); ap.add_argument('--report',default='00_index/new-files-report.md')
    a=ap.parse_args(); root=Path(a.root).resolve(); catalog=root/a.catalog; report=root/a.report
    rows=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file() or '.git' in p.parts or p.name.startswith('.'): continue
        if p.suffix.lower() not in EXTS: continue
        rel=p.relative_to(root).as_posix(); rows.append((rel,p.stat().st_size,sha256(p)))
    lines=['# New Files Scan', '', f'Scanned: {date.today().isoformat()}', '', '| File | Size (bytes) | SHA-256 |', '|---|---:|---|']
    lines += [f'| `{r}` | {s} | `{h}` |' for r,s,h in rows]
    report.parent.mkdir(parents=True,exist_ok=True); report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    if not catalog.exists(): catalog.write_text('# Catalog\n\n| Title | Category | Date | Owner | Status | Source |\n|---|---|---|---|---|---|\n',encoding='utf-8')
    print(f'Scanned {len(rows)} files; wrote {report}')
if __name__=='__main__': main()
