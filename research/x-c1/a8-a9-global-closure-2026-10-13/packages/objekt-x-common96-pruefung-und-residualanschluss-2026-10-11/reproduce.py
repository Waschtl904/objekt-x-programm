"""Check this review and its new scalar certificate against the bound input ZIP.

Optional --full-input-replay reruns the input's full rational matrix auditor.
This script does not rerun the four analytic matrix integrations.
"""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
from check_residual_setup import audit

HERE=Path(__file__).resolve().parent
INPUT_NAME='Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11'
INPUT_SHA='06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51'
def digest(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def manifest(root):
 data=json.loads((root/'MANIFEST.json').read_bytes())
 for name,want in data['files'].items():
  p=(root/name).resolve()
  assert p.is_relative_to(root.resolve()),name
  assert digest(p)==want,name
 return len(data['files'])
def extract(path,target):
 with zipfile.ZipFile(path) as z:
  for e in z.infolist():
   assert (target/e.filename).resolve().is_relative_to(target.resolve())
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  z.extractall(target)
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--input-zip',type=Path,required=True)
 ap.add_argument('--full-input-replay',action='store_true')
 args=ap.parse_args()
 assert sys.flags.optimize==0,'Run without Python -O: assertions are certificate checks.'
 print('Review manifest:',manifest(HERE),'files',flush=True)
 assert digest(args.input_zip)==INPUT_SHA,'Input ZIP SHA256 mismatch'
 with tempfile.TemporaryDirectory(prefix='objekt-x-common96-review-') as temp:
  extract(args.input_zip,Path(temp));root=Path(temp)/INPUT_NAME
  print('Input manifest:',manifest(root),'files',flush=True)
  assert json.loads((root/'AUDIT.json').read_bytes())==json.loads((HERE/'INPUT_AUDIT_COPY.json').read_bytes())
  assert audit(root)==json.loads((HERE/'RESIDUAL_SETUP.json').read_bytes())
  if args.full_input_replay:
   subprocess.run([sys.executable,'-B',str(root/'reproduce.py')],cwd=root,check=True)
 print('PASS_REVIEW_BINDINGS_AND_NEW_RESIDUAL_SCALAR_SETUP',flush=True)
 print('FULL_INPUT_REPLAY_EXECUTED='+str(args.full_input_replay).lower())
 print('NEW_FULL_FORMDUAL_RESIDUAL_CERTIFIED=false; FULL_REMAINDER_CERTIFIED=false')
if __name__=='__main__':main()
