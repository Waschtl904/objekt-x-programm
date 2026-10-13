"""Sealed-data replay, including an independent rational 96D rebuild."""
from pathlib import Path
import json,hashlib,zipfile,tempfile
from audit_full import audit
ROOT=Path(__file__).resolve().parent
def manifest(root):
 d=json.loads((root/'MANIFEST.json').read_bytes())
 for name,digest in d['files'].items():
  p=(root/name).resolve();assert p.is_relative_to(root.resolve())
  assert hashlib.sha256(p.read_bytes()).hexdigest()==digest,name
 return len(d['files'])
def extract(path,out):
 with zipfile.ZipFile(path) as z:
  for e in z.infolist():
   assert (out/e.filename).resolve().is_relative_to(out.resolve())
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  z.extractall(out)
def unpack_previous(temp):
 arc=ROOT/'inputs/Objekt-X-Richtungsbruecken-Pruefung-und-Konstantentest-2026-10-11.zip'
 assert hashlib.sha256(arc.read_bytes()).hexdigest()=='ec6b5398a8ac3ddb1038e7e4cb3ceaee5b2eebccf534137a3d7b14be0993e511'
 extract(arc,temp)
 review=temp/'Objekt-X-Richtungsbruecken-Pruefung-und-Konstantentest-2026-10-11';manifest(review)
 parentzip=review/'inputs/Objekt-X-Richtungsbruecke-und-Vergleichsgrenze-2026-10-11.zip'
 assert hashlib.sha256(parentzip.read_bytes()).hexdigest()=='4faa7004a0622b7434ad0baa35c15f53a165db8d758091bd1f1aa682bb20275d'
 extract(parentzip,temp);parent=temp/'Objekt-X-Richtungsbruecke-und-Vergleichsgrenze-2026-10-11';manifest(parent)
 return parent
if __name__=='__main__':
 count=manifest(ROOT)
 with tempfile.TemporaryDirectory(prefix='objekt-x-direct96-') as td:
  parent=unpack_previous(Path(td))
  sources=json.loads((ROOT/'REFINED_INPUT.json').read_bytes())['sources'];old=json.loads((parent/'AUDIT_INPUT.json').read_bytes())['sources']
  for label in ['EVEN','ODD']:
   for key in [f'inverse_{label}',f'galerkin_{label}']:assert sources[key]['sha256']==old[key]['sha256']
   d=json.loads((ROOT/f'DIRECT_REST_{label}_3072.json').read_bytes());assert d['bindings']['old']==sources['old']['sha256']
  assert hashlib.sha256((ROOT/'inherited_floor.py').read_bytes()).hexdigest()==sources['floor']['sha256']
  result=audit(parent);assert result==json.loads((ROOT/'AUDIT.json').read_bytes())
 print('PASS',count,'new manifest bindings, sealed predecessors and independent rational common96 rebuild')
 print('NEW_COMMON96_POSITIVE=true; FULL_REMAINDER_CERTIFIED=false')
