"""Portable rational replay; pass the two sealed predecessor ZIP archives."""
from pathlib import Path
import argparse,json,hashlib,subprocess,sys,tempfile,zipfile
from audit_exterior import audit
HERE=Path(__file__).resolve().parent
NEW='Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11'
COMMON='Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11'
INCOMING='Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11'
HASHES={NEW:'5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3',
 COMMON:'06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51',
 INCOMING:'2ac05dceb88e2b485c155f800840182e300f8899e2093f295400bc59fd530399'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def manifest(root):
 d=json.loads((root/'MANIFEST.json').read_bytes())
 for name,want in d['files'].items():
  p=(root/name).resolve();assert p.is_relative_to(root.resolve());assert sha(p)==want,name
 return len(d['files'])
def extract(archive,target):
 with zipfile.ZipFile(archive) as z:
  for e in z.infolist():
   assert (target/e.filename).resolve().is_relative_to(target.resolve())
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  z.extractall(target)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--responses-zip',type=Path,required=True);ap.add_argument('--common-zip',type=Path,required=True);ap.add_argument('--full-input-replay',action='store_true');args=ap.parse_args()
 assert __debug__,'Run without -O'
 count=manifest(HERE);print('New manifest:',count,'files',flush=True)
 izip=HERE/'inputs'/f'{INCOMING}.zip'
 for p,name in [(args.responses_zip,NEW),(args.common_zip,COMMON),(izip,INCOMING)]:assert sha(p)==HASHES[name]
 with tempfile.TemporaryDirectory(prefix='objekt-x-composed-residual-') as temp:
  target=Path(temp)
  for path in [args.responses_zip,args.common_zip,izip]:extract(path,target)
  new=target/NEW;common=target/COMMON;inc=target/INCOMING
  print('Predecessor manifests:',manifest(new),manifest(common),manifest(inc),flush=True)
  subprocess.run([sys.executable,'-B',str(inc/'reproduce.py')],check=True)
  if args.full_input_replay:
   subprocess.run([sys.executable,'-B',str(new/'reproduce.py'),'--input-zip',str(args.common_zip.resolve())],check=True)
  result=audit(new,common,inc)
  assert result==json.loads((HERE/'AUDIT_EXTERIOR.json').read_bytes())
 print('PASS_COMPOSED_RESIDUAL_PACKAGE_FRESH_REPLAY',flush=True)
 print('MOMENT_GATES_PASSED=true; FIRST_EIGHT_COMPOSED_ROWS_VERIFIED=true; FULL_REMAINDER_CERTIFIED=false')
if __name__=='__main__':main()
