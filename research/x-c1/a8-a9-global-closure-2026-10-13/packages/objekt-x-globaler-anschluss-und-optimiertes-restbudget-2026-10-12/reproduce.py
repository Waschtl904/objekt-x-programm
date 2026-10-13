from pathlib import Path
import argparse,hashlib,json,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def main():
 assert __debug__
 ap=argparse.ArgumentParser()
 for k in ['responses','log','review']:ap.add_argument('--'+k+'-zip',type=Path,required=True)
 args=ap.parse_args();manifest=read(HERE/'MANIFEST.json')
 for name,want in manifest['files'].items():
  q=(HERE/name).resolve();assert q.is_relative_to(HERE)
  assert hashlib.sha256(q.read_bytes()).hexdigest()==want,name
 print('MANIFEST_PASS',len(manifest['files']),flush=True)
 with tempfile.TemporaryDirectory(prefix='objekt-x-global-budget-') as tmp:
  out=Path(tmp)/'GLOBAL_BUDGET.json'
  cmd=[sys.executable,'-B',str(HERE/'audit_global_budget.py')]
  for k in ['responses','log','review']:cmd+=['--'+k+'-zip',str(getattr(args,k+'_zip').resolve())]
  cmd+=['--out',str(out)];subprocess.run(cmd,check=True)
  assert read(out)==read(HERE/'GLOBAL_BUDGET.json')
 print('PASS_CONDITIONAL_GLOBAL_CONNECTION_AND_OPTIMIZED_BUDGET',flush=True)
 print('GLOBAL_RESIDUAL_INTEGRAL_COMPUTED=false; FULL_REMAINDER_CERTIFIED=false',flush=True)
if __name__=='__main__':main()
