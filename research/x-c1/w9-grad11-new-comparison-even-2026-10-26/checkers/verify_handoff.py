"""Verify the complete publication-free handoff, without native libraries.

Examples: python -B verify_handoff.py --zip package.zip
          python -B verify_handoff.py --directory extracted_package
Directory mode additionally recombines all saved rational residual bounds.
This does not rerun native integration or verify analytic hypotheses.
"""
from pathlib import Path,PurePosixPath
from fractions import Fraction
import argparse,hashlib,json,subprocess,sys,tempfile,zipfile
sys.set_int_max_str_digits(50000)
ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True)
g.add_argument('--zip',type=Path);g.add_argument('--directory',type=Path);args=ap.parse_args()
def safe(name):
    p=PurePosixPath(name)
    assert not p.is_absolute() and '..' not in p.parts and '\\' not in name and ':' not in name,name
    return p
def digest(stream):
    h=hashlib.sha256();n=0
    while data:=stream.read(1024*1024):h.update(data);n+=len(data)
    return n,h.hexdigest()
if args.zip:
    with zipfile.ZipFile(args.zip)as z:
        names=z.namelist();assert len(names)==len(set(names)), 'Duplicate archive names'
        for name in names:safe(name)
        manifest=json.loads(z.read('MANIFEST.json'))
        expected={r['path']for r in manifest['files']}|{'MANIFEST.json'}
        assert set(names)==expected,'Unexpected or absent archive member'
        for row in manifest['files']:
            with z.open(row['path'])as f:n,h=digest(f)
            assert n==row['bytes']and h==row['sha256'],row['path']
        result=json.loads(z.read('workspace/work/breakthrough-2026-10-25/JOINT_REST_BUDGET.json'))
else:
    root=args.directory.resolve();manifest=json.loads((root/'MANIFEST.json').read_bytes())
    for row in manifest['files']:
        p=root.joinpath(*safe(row['path']).parts)
        assert p.resolve().is_relative_to(root)and not p.is_symlink(),row['path']
        with p.open('rb')as f:n,h=digest(f)
        assert n==row['bytes']and h==row['sha256'],row['path']
    research=root/'workspace/work/breakthrough-2026-10-25'
    result=json.loads((research/'JOINT_REST_BUDGET.json').read_bytes())
    with tempfile.TemporaryDirectory(prefix='objekt-x-rational-audit-')as tmp:
        target=Path(tmp)/'recombined.json'
        subprocess.run([sys.executable,'-B',str(research/'joint_rest_budget.py'),'--output',str(target)],check=True)
        fresh=json.loads(target.read_bytes())
    for key in ('relative_rest_upper','resulting_GW_floor','whole_joint_pass','directions','common_frame_sha256'):
        assert fresh[key]==result[key], 'Rational replay mismatch: '+key
assert result['whole_joint_pass']and len(result['directions'])==12
assert Fraction(result['relative_rest_upper'])<1 and Fraction(result['resulting_GW_floor'])>0
print(json.dumps({'status':'HANDOFF_BYTES_AND_STORED_RESULT_PASS','files':len(manifest['files']),
 'bytes':sum(r['bytes']for r in manifest['files']),
 'rational_recombination_replayed':bool(args.directory),
 'fresh_native_integrations_replayed':False,'independent_analytic_review_complete':False},indent=2))
