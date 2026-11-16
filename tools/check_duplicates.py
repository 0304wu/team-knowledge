import argparse, hashlib, re
from pathlib import Path

def sha256(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser(description='Find duplicate files and DOI collisions without deleting anything.')
 ap.add_argument('root'); a=ap.parse_args(); root=Path(a.root).resolve(); by_hash={}; by_doi={}
 for p in root.rglob('*'):
  if not p.is_file() or '.git' in p.parts or p.name.startswith('.'): continue
  by_hash.setdefault(sha256(p),[]).append(p)
  try: txt=p.read_text(encoding='utf-8',errors='ignore') if p.suffix.lower() in {'.md','.txt','.bib'} else p.name
  except Exception: txt=p.name
  for doi in re.findall(r'10\.\d{4,9}/[-._;()/:A-Z0-9]+',txt,re.I): by_doi.setdefault(doi.rstrip('.,);'),[]).append(p)
 print('Exact duplicate files:')
 for ps in by_hash.values():
  if len(ps)>1: print('  ' + ' | '.join(str(p.relative_to(root)) for p in ps))
 print('DOI collisions:')
 for doi,ps in by_doi.items():
  if len(ps)>1: print(f'  {doi}: ' + ' | '.join(str(p.relative_to(root)) for p in ps))
if __name__=='__main__': main()
