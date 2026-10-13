from pathlib import Path
import argparse,json,hashlib,subprocess,sys,tempfile,zipfile
from audit_endpoint import audit
HERE=Path(__file__).resolve().parent
NEW='Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11'
PARENT='Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11'
REVIEW='Objekt-X-Antwortpruefung-und-Aussenresidual8-2026-10-11'
DUAL='Objekt-X-Unendlicher-Dualrest-und-Aussenrichtungen-2026-10-11'
HASHES={NEW:'5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3',
 PARENT:'06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51',
 REVIEW:'57b8731ee450b3d1c96701ba1fac341a8b50286f5953b1124c39d8d0b42bdc0b',
 DUAL:'2ac05dceb88e2b485c155f800840182e300f8899e2093f295400bc59fd530399'}
def sha(p):return hashlib.file_digest(p.open('rb'),'sha256').hexdigest()
def manifest(root):
 d=json.loads((root/'MANIFEST.json').read_bytes())
 for name,want in d['files'].items():
  p=(root/name).resolve();assert p.is_relative_to(root.resolve());assert sha(p)==want,name
 return len(d['files'])
def extract(path,target):
 with zipfile.ZipFile(path) as z:
  for e in z.infolist():
   assert (target/e.filename).resolve().is_relative_to(target.resolve())
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  z.extractall(target)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--responses-zip',type=Path,required=True);ap.add_argument('--parent-zip',type=Path,required=True);args=ap.parse_args()
 assert __debug__
 print('New manifest:',manifest(HERE),'files',flush=True)
 reviewzip=HERE/'inputs'/f'{REVIEW}.zip';dualzip=HERE/'inputs'/f'{DUAL}.zip'
 archives=[(args.responses_zip,NEW),(args.parent_zip,PARENT),(reviewzip,REVIEW),(dualzip,DUAL)]
 for path,name in archives:assert sha(path)==HASHES[name]
 with tempfile.TemporaryDirectory(prefix='objekt-x-endpoint-review-') as temp:
  target=Path(temp)
  for path,name in archives:extract(path,target);print(name,'manifest',manifest(target/name),flush=True)
  subprocess.run([sys.executable,'-B',str(target/REVIEW/'reproduce.py'),'--responses-zip',str(args.responses_zip.resolve()),'--parent-zip',str(args.parent_zip.resolve()),'--dual-zip',str(dualzip.resolve())],check=True)
  out=audit(target/NEW,target/PARENT)
  assert out==json.loads((HERE/'AUDIT_ENDPOINT.json').read_bytes())
 print('PASS_ENDPOINT_PACKAGE_FRESH_REPLAY',flush=True)
 print('RANK_ONE_LOWER_GRAM_VERIFIED=true; FULL_WEIGHTED_TAIL_UPPER_COMPUTED=false; FULL_REMAINDER_CERTIFIED=false')
if __name__=='__main__':main()
