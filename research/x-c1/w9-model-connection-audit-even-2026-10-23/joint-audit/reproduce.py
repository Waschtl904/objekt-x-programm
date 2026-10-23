"""Repeat this review from the two original archives and the pinned Git inputs."""
import sys
if not __debug__:raise SystemExit('Assertions required; do not use -O/-OO')
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,zipfile
H=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(description=__doc__)
src=ap.add_mutually_exclusive_group();src.add_argument('--repo',type=Path);src.add_argument('--snapshot',type=Path)
ap.add_argument('--run-dir',type=Path);ap.add_argument('--validate-only',action='store_true');args=ap.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
for n,h in json.loads((H/'MANIFEST.json').read_bytes()).items():assert sha(H/n)==h,n
if args.validate_only:
    for p in (H/'inputs').glob('*.zip'):
        with zipfile.ZipFile(p)as z:assert z.testzip()is None
    print('Delivery files and both original input ZIPs verified.');raise SystemExit(0)
if not args.run_dir or not(args.repo or args.snapshot):ap.error('--run-dir and --repo/--snapshot are required')
R=args.run_dir.resolve()
if R.exists():raise SystemExit('Run directory must not exist yet.')
R.mkdir(parents=True);work=R/'work';work.mkdir();outputs=R/'outputs';outputs.mkdir()
def unpack(p,d):
    d.mkdir(parents=True)
    with zipfile.ZipFile(p)as z:
        for i in z.infolist():
            target=(d/i.filename).resolve();assert target.is_relative_to(d)
            assert (i.external_attr>>16)&0o170000!=0o120000
            if i.is_dir():target.mkdir(exist_ok=True,parents=True);continue
            target.parent.mkdir(exist_ok=True,parents=True);target.write_bytes(z.read(i))
A=work/'binding-model-review-2026-10-23';O=outputs/'Objekt-X-Modellanschluss-2026-10-22'
unpack(H/'inputs/received-binding-model.zip',A);unpack(H/'inputs/previous-model-connection.zip',O)
S=work/'pr254-review';S.mkdir();W=work/'binding-reconciliation-2026-10-23';W.mkdir()
inputs=json.loads((A/'SOURCE_BINDINGS.json').read_bytes())['repository_files']
for n,item in inputs.items():
    p=(S/n).resolve();assert p.is_relative_to(S)
    if args.snapshot:raw=(args.snapshot/n).read_bytes()
    else:
        repo=args.repo.resolve()
        raw=subprocess.check_output(['git','-c','safe.directory='+repo.as_posix(),'-C',str(repo),'show',
            'beb38c9d1cba666bb3b7ddab9577873e59d854c4:'+n])
    assert hashlib.sha256(raw).hexdigest()==item['sha256'],n
    p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
for p in (H/'scripts').glob('*.py'):shutil.copy2(p,W/p.name)
import flint
assert flint.__version__=='0.9.0','Use the tested python-flint 0.9.0 runtime'
env=os.environ.copy();env['PYTHONUTF8']='1';env['PYTHONDONTWRITEBYTECODE']='1'
def run(p,*argv):subprocess.run([sys.executable,'-u','-B',str(p),*map(str,argv)],env=env,check=True)
run(A/'check_distribution.py','--repo',S)
run(W/'check_binding_patch.py')
for script,folder in [('fixed_combination_check.py','fresh-sources'),('model_identity_audit.py','fresh-identity'),('core_moment_diagnostic.py','fresh-moment')]:
    run(A/'Skripte'/script,'--repo',S,'--out',W/folder)
run(W/'raw_operator.py');run(W/'reconcile.py')
# Compare all deterministic mathematics from the fresh review, not wall time
# dependent result-file hashes. The source replay comparator already compares
# the complete mathematical fields with the received reference files.
for n in ('raw-operator-result.json','binding-patch-result.json'):
    assert json.loads((W/n).read_bytes())==json.loads((H/'evidence'/n).read_bytes()),n
x=json.loads((W/'reconciliation-result.json').read_bytes());y=json.loads((H/'evidence/reconciliation-result.json').read_bytes())
for record in (x,y):
    for item in record['fresh_replays'].values():item.pop('fresh_sha256',None)
assert x==y,'Reconciliation differs'
print('PASS: all deterministic review results reproduced. Full analytic acceptance remains open.')
