"""Replay the new finite response step against its sealed input ZIP."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
from audit import audit
HERE=Path(__file__).resolve().parent
INPUT_NAME='Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11'
INPUT_SHA='06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51'
REVIEW_NAME='Objekt-X-Common96-Pruefung-und-Residualanschluss-2026-10-11'
REVIEW_SHA='174f4f2410343643627ba3a38a12e0653e95615d7d6d2f702abd9bae43944bcf'
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
def manifest(root):
 data=json.loads((root/'MANIFEST.json').read_bytes())
 for name,want in data['files'].items():
  p=(root/name).resolve();assert p.is_relative_to(root.resolve());assert sha(p)==want,name
 return len(data['files'])
def extract(zpath,dest):
 with zipfile.ZipFile(zpath) as z:
  for e in z.infolist():
   assert (dest/e.filename).resolve().is_relative_to(dest.resolve())
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  z.extractall(dest)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--input-zip',type=Path,required=True);ap.add_argument('--full-input-replay',action='store_true');args=ap.parse_args()
 assert __debug__,'Do not run with -O'
 print('New manifest:',manifest(HERE),'files',flush=True)
 assert sha(args.input_zip)==INPUT_SHA
 reviewzip=HERE/(REVIEW_NAME+'.zip');assert sha(reviewzip)==REVIEW_SHA
 with tempfile.TemporaryDirectory(prefix='objekt-x-new-responses-') as tmp:
  target=Path(tmp);extract(args.input_zip,target);parent=target/INPUT_NAME
  print('Parent manifest:',manifest(parent),'files',flush=True)
  extract(reviewzip,target);review=target/REVIEW_NAME
  command=[sys.executable,'-B',str(review/'reproduce.py'),'--input-zip',str(args.input_zip.resolve())]
  if args.full_input_replay:command.append('--full-input-replay')
  subprocess.run(command,check=True)
  expected=json.loads((HERE/'AUDIT.json').read_bytes());assert audit(parent)==expected
  expected_precision=(HERE/'PRECISION_CHECK.json').read_bytes()
  subprocess.run([sys.executable,'-B',str(HERE/'compare_precision.py')],check=True)
  assert (HERE/'PRECISION_CHECK.json').read_bytes()==expected_precision
 print('PASS_NEW_RESPONSE_PACKAGE_REPLAY',flush=True)
 print('NEW_DIRECTIONAL_RESIDUAL_BUDGET_POSITIVE=true; SHARP_FULL_RESIDUAL_OPEN=true; FULL_REMAINDER_CERTIFIED=false')
if __name__=='__main__':main()
