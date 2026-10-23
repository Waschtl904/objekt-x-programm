"""Reproduce the new finite audit; outputs must be outside this package."""
import sys
if not __debug__:raise SystemExit('Python -O/-OO is rejected')
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json,os,subprocess
H=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);ap.add_argument('--validate-only',action='store_true');args=ap.parse_args()
subprocess.run([sys.executable,'-B',str(H/'check_results.py')],check=True)
R=args.repo.resolve();O=args.out.resolve()
if O.exists()or O.is_relative_to(H)or O.is_relative_to(R):raise SystemExit('Use a fresh output directory outside package and checkout')
bindings=json.loads((H/'SOURCE_BINDINGS.json').read_bytes())['repository_files']
for name,v in bindings.items():
 p=(R/name).resolve();assert p.is_relative_to(R)
 assert hashlib.sha256(p.read_bytes()).hexdigest()==v['sha256'],name
import flint
assert flint.__version__=='0.9.0'
if args.validate_only:print('PASS: package, 668 source bindings and runtime');raise SystemExit(0)
O.mkdir(parents=True)
env=os.environ.copy();env['PYTHONUTF8']='1';env['PYTHONDONTWRITEBYTECODE']='1'
def run(script,*tail):subprocess.run([sys.executable,'-u','-B',str(H/'scripts'/script),*map(str,tail)],check=True,env=env)
run('source_cap_audit.py','--repo',R,'--out',O/'source')
run('cache_binding_audit.py','--repo',R,'--out',O/'atoms')
run('cache_rebuild_128.py','--repo',R,'--out',O/'cache-rebuild.json')
run('cache_price.py','--audit',O/'atoms/cache-atom-audit.json','--rebuild',O/'cache-rebuild.json','--joint',H/'evidence/reconciliation-result.json','--out',O/'cache-price.json')
for fresh,old in [('source/source-caps.json','source-caps.json'),('atoms/cache-atom-audit.json','cache-atom-audit.json'),('cache-rebuild.json','cache-rebuild.json'),('cache-price.json','cache-price.json')]:
 a=json.loads((O/fresh).read_bytes());b=json.loads((H/'evidence'/old).read_bytes())
 a.pop('seconds',None);b.pop('seconds',None)
 assert a==b,fresh
print('PASS: new deterministic fields reproduced; analytic prerequisites remain as listed.')
