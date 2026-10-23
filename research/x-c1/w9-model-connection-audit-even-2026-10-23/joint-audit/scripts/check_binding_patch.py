"""Independent four-file patch and declared-input reconstruction check."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json,shutil,subprocess
W=Path(__file__).resolve().parent;ROOT=W.parent/'pr254-review'
A=W.parent/'binding-model-review-2026-10-23';ISO=W/'isolated-lf'
PREFIX='research/x-c1/w9-gamma-repair-even-2026-10-22'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_bytes())
if ISO.exists():raise SystemExit('Fresh isolated directory required')
ISO.mkdir()
bindings=read(A/'SOURCE_BINDINGS.json')['repository_files']
for name,info in bindings.items():
    p=ROOT/name;assert sha(p)==info['sha256'],name
    dest=(ISO/name).resolve();assert dest.is_relative_to(ISO)
    dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,dest)
patch=A/'manifest-binding-fix.patch'
subprocess.run(['git','-c','core.autocrlf=false','apply','--check',str(patch)],cwd=ISO,check=True)
subprocess.run(['git','-c','core.autocrlf=false','apply',str(patch)],cwd=ISO,check=True)
expected={p.relative_to(A/'Korrekturdateien').as_posix():sha(p)for p in (A/'Korrekturdateien').rglob('*')if p.is_file()}
assert len(expected)==4
changed={p.relative_to(ISO).as_posix()for p in ISO.rglob('*')if p.is_file()and (not(ROOT/p.relative_to(ISO)).exists()or sha(p)!=sha(ROOT/p.relative_to(ISO)))}
assert changed==set(expected),(changed,set(expected))
for name,h in expected.items():assert sha(ISO/name)==h,name
P=ISO/PREFIX
manifest=read(P/'MANIFEST.json');inputs=read(P/'INPUT_BINDINGS.json')['repository_files']
actual={p.relative_to(ISO).as_posix()for p in ISO.rglob('*')if p.is_file()}
declared={PREFIX+'/'+n for n in manifest}|{PREFIX+'/MANIFEST.json'}|set(inputs)
assert actual==declared,(actual-declared,declared-actual)
assert len(manifest)==100 and len(inputs)==568
assert sha(P/'ACCEPTANCE.json')==sha(ROOT/PREFIX/'ACCEPTANCE.json')
def run(*args):return subprocess.run([sys.executable,'-B',str(P/'verify.py'),*args],cwd=ISO,capture_output=True,text=True)
r=run('--bindings-only');assert r.returncode==0,(r.stdout,r.stderr)
report=json.loads(r.stdout)
extra='research/x-c1/w9-residual-centered-control-even-2026-10-21/MANIFEST.json'
target=ISO/extra;original=target.read_bytes();negative=[]
try:
    for mode in ('missing','changed'):
        if mode=='missing':target.unlink()
        else:target.write_bytes(original+b' ')
        r=run('--bindings-only');assert r.returncode!=0
        assert ('No such file'in r.stderr)if mode=='missing'else('Inherited input hash'in r.stderr)
        negative.append({'case':mode,'exit_code':r.returncode,'rejected_before_numerics':True})
        target.write_bytes(original)
finally:target.write_bytes(original)
r=subprocess.run([sys.executable,'-B',str(P/'test_controls.py')],cwd=ISO,capture_output=True,text=True)
assert r.returncode==0,(r.stdout,r.stderr)
(W/'binding-existing-controls.log').write_text(r.stdout+r.stderr,encoding='utf-8')
result={'status':'PATCH_AND_ISOLATED_BINDINGS_PASS','base':'beb38c9d1cba666bb3b7ddab9577873e59d854c4',
 'archive_sha256':'a2976b68b8693cf3bb5cda068eae16b8b8d34b3f87d4125d89dd9349a7f599e6',
 'exact_changed_files':expected,'isolated_files':len(actual),'package_files':len(manifest),'inherited_files':len(inputs),
 'original_acceptance_unchanged':True,'all_other_original_files_unchanged':True,
 'binding_check':report,'new_negative_controls':negative,'existing_controls_passed':6,
 'new_16_panel_integration_performed_here':False,
 'reason':'Mathematical files unchanged; earlier independent 16-panel replay retained at original head.',
 'git_apply_core_autocrlf':False,
 'portability_note':'An isolated patch application with the ambient Windows autocrlf setting wrote the new revision JSON as CRLF; its JSON content was identical but its manifest hash differed. Apply with core.autocrlf=false or copy the supplied exact bytes.',
 'remote_changes':False}
(W/'binding-patch-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k]for k in ['status','isolated_files','package_files','inherited_files','new_negative_controls','existing_controls_passed']},indent=2))
