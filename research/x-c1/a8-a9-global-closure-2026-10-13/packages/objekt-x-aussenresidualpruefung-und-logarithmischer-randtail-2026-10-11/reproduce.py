"""Portable rational replay of the new endpoint and complete log-tail step."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
HERE=Path(__file__).resolve().parent
NAMES={
 'responses':('Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11','5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3'),
 'common':('Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11','06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51'),
 'incoming':('Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11','70faaa1a9f8c2904320f69188624de225655ba3c6de5c2577c4e69d6706c6799')}
def read(p):return json.loads(p.read_bytes())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def manifest(root):
 m=read(root/'MANIFEST.json')
 for name,want in m['files'].items():
  p=(root/name).resolve();assert p.is_relative_to(root.resolve())
  assert sha(p)==want,name
 return len(m['files'])
def extract(p,dest):
 with zipfile.ZipFile(p) as z:
  for e in z.infolist():
   assert (dest/e.filename).resolve().is_relative_to(dest.resolve())
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  z.extractall(dest)
def run(*a):subprocess.run([sys.executable,'-B',*map(str,a)],check=True)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--responses-zip',type=Path,required=True)
 ap.add_argument('--common-zip',type=Path,required=True);ap.add_argument('--full-input-replay',action='store_true');args=ap.parse_args()
 assert __debug__;print('Review manifest:',manifest(HERE),flush=True)
 with tempfile.TemporaryDirectory(prefix='objekt-x-endpoint-review-') as tmp:
  tmp=Path(tmp);roots={}
  for key,(name,digest) in NAMES.items():
   archive=HERE/'inputs'/(name+'.zip') if key=='incoming' else getattr(args,key+'_zip')
   assert sha(archive)==digest,key
   extract(archive,tmp);roots[key]=tmp/name
   print(key,'manifest:',manifest(roots[key]),flush=True)
  incoming=roots['incoming']
  ref=read(HERE/'data/INDEPENDENT_COMPARISON.json')
  for row in ref['cases']:
   p=incoming/f"CROSS_{row['parity'].upper()}_3072.json";new=read(p);assert sha(p)==row['incoming_cross_file_sha256']
   count=0
   for key,matrix in row['reference_matrices'].items():
    for r,s in zip(matrix,new[key]):
     for x,y in zip(r,s):
      assert max(F(x[0]),F(y[0]))<=min(F(x[1]),F(y[1]));count+=1
   assert count==row['overlap_count']==1344
  if args.full_input_replay:
   run(incoming/'reproduce.py','--responses-zip',args.responses_zip.resolve(),'--common-zip',args.common_zip.resolve())
  target=tmp/'LOG_TAIL_104.json';run(HERE/'build_log_tail.py','--out',target)
  assert read(target)==read(HERE/'data/LOG_TAIL_104.json')
  result=tmp/'ENDPOINT_AUDIT.json'
  run(HERE/'audit_outer_endpoint.py','--responses',roots['responses'],'--data',HERE/'data','--out',result)
  assert read(result)==read(HERE/'data/ENDPOINT_AUDIT.json')
 print('PASS_COMPOSED_RESIDUAL_REVIEW_AND_COMPLETE_OUTER_LOG_TAIL',flush=True)
 print('COMPLETE_RESIDUAL_TAIL_CERTIFIED=false; FULL_REMAINDER_CERTIFIED=false',flush=True)
if __name__=='__main__':main()
