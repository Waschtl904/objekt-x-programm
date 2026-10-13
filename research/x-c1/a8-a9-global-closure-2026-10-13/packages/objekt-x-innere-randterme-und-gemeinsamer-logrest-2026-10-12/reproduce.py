"""Fresh archive replay; no Arb installation needed for the rational checks."""
from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
HERE=Path(__file__).resolve().parent
NAMES={
 'responses':('Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11','5b41695ea53cd620210654af0a0389219631484e5f2584404fddd0f5af206fd3'),
 'common':('Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11','06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51'),
 'review':('Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11','d4394c74d224cda1fcab44bc7e945a608f2228ff3cc91fcbe75da59de3572e3e')}
def read(p):return json.loads(p.read_bytes())
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def manifest(root):
 m=read(root/'MANIFEST.json')
 for name,want in m['files'].items():
  q=(root/name).resolve();assert q.is_relative_to(root.resolve()) and sha(q)==want,name
 return len(m['files'])
def extract(p,where):
 with zipfile.ZipFile(p) as z:
  for e in z.infolist():
   assert (where/e.filename).resolve().is_relative_to(where.resolve())
   assert ((e.external_attr>>16)&0o170000)!=0o120000
  z.extractall(where)
def run(*args):subprocess.run([sys.executable,'-B',*map(str,args)],check=True)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--responses-zip',type=Path,required=True);ap.add_argument('--common-zip',type=Path,required=True);args=ap.parse_args()
 assert __debug__;print('New package manifest:',manifest(HERE),flush=True)
 with tempfile.TemporaryDirectory(prefix='objekt-x-three-log-') as td:
  td=Path(td);roots={}
  for key,(name,digest) in NAMES.items():
   archive=HERE/'inputs'/(name+'.zip') if key=='review' else getattr(args,key+'_zip').resolve()
   assert sha(archive)==digest,key;extract(archive,td);roots[key]=td/name
   print(key,'manifest:',manifest(roots[key]),flush=True)
  run(roots['review']/'reproduce.py','--responses-zip',args.responses_zip.resolve(),'--common-zip',args.common_zip.resolve())
  out=td/'AUDIT.json'
  run(HERE/'audit.py','--responses',roots['responses'],'--common',roots['common'],'--review',roots['review'],'--old',HERE/'inputs/a8_model.json.gz','--out',out)
  assert read(out)==read(HERE/'AUDIT.json')
 print('PASS_FRESH_COMPLETE_THREE_LOG_COMPONENT_TAIL',flush=True)
 print('COMPLETE_RESIDUAL_TAIL_CERTIFIED=false; TAIL_FLOOR_CERTIFIED=false',flush=True)
if __name__=='__main__':main()
