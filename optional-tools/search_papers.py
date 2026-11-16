import argparse, re
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description='Search paper titles, notes, abstracts and catalog entries by keywords.')
    ap.add_argument('root'); ap.add_argument('query', nargs='+'); ap.add_argument('--limit',type=int,default=20)
    a=ap.parse_args(); root=Path(a.root).resolve(); terms=[x.lower() for x in a.query]; hits=[]
    for p in root.rglob('*'):
        if not p.is_file() or '.git' in p.parts or p.suffix.lower() not in {'.md','.txt','.bib'}: continue
        try: text=p.read_text(encoding='utf-8',errors='ignore')
        except Exception: continue
        low=text.lower(); score=sum(low.count(t) for t in terms)
        if score: 
            lines=[x.strip() for x in text.splitlines() if any(t in x.lower() for t in terms)]
            hits.append((score,p,lines[:3]))
    for score,p,lines in sorted(hits,key=lambda x:(-x[0],str(x[1])))[:a.limit]:
        print(f'[{score}] {p.relative_to(root)}')
        for line in lines: print(f'  {line[:240]}')
    if not hits: print('No matching records found in the local knowledge-base copy.')
if __name__=='__main__': main()
