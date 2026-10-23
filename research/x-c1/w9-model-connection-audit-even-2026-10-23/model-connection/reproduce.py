"""Stage hash-bound inputs into a fresh run directory, then repeat the checks.

Usage: python reproduce.py --repo PATH_TO_GIT_CHECKOUT --run-dir NEW_DIRECTORY
Or:    python reproduce.py --snapshot PATH_TO_EXPORTED_ROOT --run-dir NEW_DIRECTORY
Python 3.13 and python-flint 0.9.0 are the tested runtime. No network, push,
merge or changes to the provided checkout. Do not use python -O.
"""
import argparse,hashlib,json,os,shutil,subprocess,sys
from pathlib import Path
if not __debug__:raise SystemExit('Assertions required; no -O/-OO.')
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ap=argparse.ArgumentParser(description=__doc__)
origin=ap.add_mutually_exclusive_group(required=True)
origin.add_argument('--repo',type=Path);origin.add_argument('--snapshot',type=Path)
ap.add_argument('--run-dir',type=Path,required=True)
ap.add_argument('--stage-only',action='store_true')
args=ap.parse_args()
sha=lambda x:hashlib.sha256(x).hexdigest()
manifest=json.loads((HERE/'MANIFEST.json').read_bytes())
for name,digest in manifest.items():
    assert sha((HERE/name).read_bytes())==digest,('Delivery hash',name)
target=args.run_dir.resolve()
if target.exists():raise SystemExit('The run directory must not exist yet.')
target.mkdir(parents=True)
snapshot=target/'pr254-review';scripts=target/'model-identification'
snapshot.mkdir();scripts.mkdir()
binding=json.loads((HERE/'SOURCE_FILES.json').read_bytes())
commit=binding['commit']
for name,digest in binding['files'].items():
    dest=(snapshot/name).resolve()
    if not dest.is_relative_to(snapshot):raise ValueError('Source path escapes snapshot')
    if args.snapshot:
        raw=(args.snapshot/name).read_bytes()
    else:
        repo=args.repo.resolve()
        raw=subprocess.check_output(['git','-c','safe.directory='+repo.as_posix(),
            '-C',str(repo),'show',commit+':'+name])
    if sha(raw)!=digest:raise ValueError('Bound input differs: '+name)
    dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw)
for name in ('rebuild.py','exact_cache.py','audit.py','rounding.py'):
    shutil.copy2(HERE/'scripts'/name,scripts/name)
print('Staged',len(binding['files']),'verified source files. Checkout unchanged.',flush=True)
if args.stage_only:raise SystemExit(0)
import flint
if flint.__version__!='0.9.0':raise SystemExit('Use the tested python-flint version 0.9.0.')
env=os.environ.copy();env['PYTHONUTF8']='1';env['PYTHONDONTWRITEBYTECODE']='1'
for name in ('rebuild.py','rounding.py','audit.py'):
    subprocess.run([sys.executable,'-u','-B',str(scripts/name)],env=env,check=True)
for name in ('component-rebuild.json','rounding-result.json','audit-result.json'):
    actual=json.loads((scripts/name).read_bytes());expected=json.loads((HERE/'evidence'/name).read_bytes())
    # Runtime is not a mathematical output. The audit also binds the fresh
    # component file hash, which changes when that file records a new runtime.
    for record in (actual,expected):
        record.pop('seconds',None)
        record.pop('component_rebuild_sha256',None)
    assert actual==expected,('Replay fields differ',name)
print('PASS: all deterministic result fields match the delivered evidence.',flush=True)
