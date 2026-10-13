"""Portable rational replay; original ZIPs are never changed.

The upstream byte-only precision comparison is replaced explicitly by a
JSON-value comparison, because its archive uses Windows line endings.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
HERE=Path(__file__).resolve().parent
INPUTS={
 'responses':('Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11','5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3'),
 'parent':('Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11','06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51'),
 'dual':('Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11','2ac05dceb88e2b485c155f800840182e300f8899e2093f295400bc59fd530399')}
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
def manifest(root):
 data=read(root/'MANIFEST.json')
 for name,want in data['files'].items():
  p=(root/name).resolve();assert p.is_relative_to(root.resolve())
  assert sha(p)==want,name
 return len(data['files'])
def extract(path,dest):
 with zipfile.ZipFile(path) as z:
  for e in z.infolist():
   assert (dest/e.filename).resolve().is_relative_to(dest.resolve())
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  z.extractall(dest)
def run(*args):subprocess.run([sys.executable,'-B',*map(str,args)],check=True)
def precision():
 for label in ['EVEN','ODD']:
  a=read(HERE/'data'/f'CROSS_{label}_3072.json');b=read(HERE/'data'/f'CROSS_{label}_4096.json');count=0
  for key in ['Hgram','source_c_model','direct_probe_model','exact_local_coefficient_intervals']:
   assert len(a[key])==len(b[key])
   for r,s in zip(a[key],b[key]):
    assert len(r)==len(s)
    for x,y in zip(r,s):
     assert max(F(x[0]),F(y[0]))<=min(F(x[1]),F(y[1]))
     count+=1
  assert count==44068
  print(label,count,'new cross-integration interval comparisons PASS',flush=True)
def main():
 ap=argparse.ArgumentParser()
 for key in INPUTS:ap.add_argument('--'+key+'-zip',type=Path,required=True)
 args=ap.parse_args();assert __debug__,'Do not run with -O'
 print('Review manifest:',manifest(HERE),'files',flush=True)
 t=F(1,10**352)
 price=(50*t*(1+5*t)+625*t*t)/6+1000*t*t*(1+30*t)**2/36
 assert price<F(1,10**350)
 precision()
 with tempfile.TemporaryDirectory(prefix='objekt-x-residual8-review-') as tmp:
  target=Path(tmp);roots={}
  for key,(name,digest) in INPUTS.items():
   path=getattr(args,key+'_zip');assert sha(path)==digest,key
   extract(path,target);roots[key]=target/name
   print(key,'manifest:',manifest(roots[key]),'files',flush=True)
  r=roots['responses'];p=roots['parent'];old=roots['dual']
  # Both original rational calculations are replayed. Their analytic
  # premises remain inherited, as in the mathematical report.
  run(old/'reproduce.py')
  expected=read(r/'AUDIT.json')
  run(r/'audit.py','--parent',p)
  assert read(r/'AUDIT.json')==expected
  expected=read(r/'PRECISION_CHECK.json')
  run(r/'compare_precision.py')
  assert read(r/'PRECISION_CHECK.json')==expected
  print('Upstream precision check: JSON equality PASS; CRLF/LF difference only',flush=True)
  connection=target/'CONNECTION.json'
  run(HERE/'check_connection.py','--responses',r,'--parent',p,'--out',connection)
  assert read(connection)==read(HERE/'data/CONNECTION.json')
  result=target/'EXTERIOR_AUDIT.json'
  run(HERE/'audit_exterior.py','--responses',r,'--parent',p,'--data',HERE/'data',
      '--prior-data',old/'data','--connection',connection,'--out',result)
  assert read(result)==read(HERE/'data/EXTERIOR_AUDIT.json')
 print('PASS_NEW_RESPONSES_GLOBAL_DUAL_CONNECTION_AND_EIGHT_EXTERIOR_TERMS',flush=True)
 print('FULL_WEIGHTED_RESIDUAL_TAIL_FROM_104_OPEN=true; FULL_REMAINDER_CERTIFIED=false',flush=True)
if __name__=='__main__':main()
