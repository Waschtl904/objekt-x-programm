"""Audit immutable packages and replay their small Arb controls at pinned sources."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,os,subprocess,sys,zipfile
HERE=Path(__file__).resolve().parent;REPO=HERE.parents[2]
def sha(raw):return hashlib.sha256(raw).hexdigest()
def checked_path(root,name):
 p=PurePosixPath(name);assert name and '\\' not in name and ':' not in name and not p.is_absolute()
 assert all(x not in ('','.','..') for x in name.split('/'))
 target=root.joinpath(*p.parts);assert target.resolve().is_relative_to(root.resolve()) and not target.is_symlink();return target
def manifest(root):
 rows={}
 for line in (root/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
  digest,name=line.split('  ',1);assert name not in rows and len(digest)==64
  assert sha(checked_path(root,name).read_bytes())==digest,name;rows[name]=digest
 actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
 assert actual==set(rows)|{'SHA256SUMS'},(actual-set(rows),set(rows)-actual);return rows
def bindings():
 family=manifest(HERE);data=json.loads((HERE/'SOURCE_BINDINGS.json').read_bytes())
 for item in data['original_files']:assert sha(checked_path(HERE,item['path']).read_bytes())==item['sha256']
 for pkg in data['packages']:
  parent=checked_path(HERE,pkg['folder']);root=parent/'original';files=manifest(root)
  assert (parent/'PROOF.md').read_bytes()==(root/pkg['original_proof']).read_bytes()
  archive=checked_path(HERE,pkg['archive']);assert sha(archive.read_bytes())==pkg['archive_sha256']
  with zipfile.ZipFile(archive) as z:
   prefix=pkg['original_folder']+'/';expected={prefix+n for n in set(files)|{'SHA256SUMS'}}
   assert set(z.namelist())==expected and len(z.namelist())==len(expected) and z.testzip() is None
   for name in expected:assert z.read(name)==(root/name[len(prefix):]).read_bytes()
 return data,family
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--full',action='store_true');a=p.parse_args()
 out=a.output.resolve();assert not out.is_relative_to(REPO.resolve()) and not out.exists()
 data,family=bindings();out.mkdir(parents=True)
 git=['git','-c','safe.directory='+REPO.as_posix(),'-c','core.longpaths=true','-C',str(REPO)]
 head=subprocess.check_output(git+['rev-parse','HEAD']).decode().strip();pin=data['publication_base']
 # Isolate the historical HEAD required by the immutable verifiers. A shared
 # clone avoids writes to the live checkout or its worktree registrations.
 source=out/'source'
 subprocess.run(['git','-c','safe.directory='+REPO.as_posix(),'clone','--shared','--no-checkout',str(REPO),str(source)],check=True,capture_output=True)
 sg=['git','-c','safe.directory='+source.as_posix(),'-c','core.longpaths=true','-c','core.autocrlf=false','-C',str(source)]
 subprocess.run(sg+['checkout','--detach',pin],check=True,capture_output=True)
 receipts=[];steps=[]
 def run(name,root,argv):
  with (out/(name+'.log')).open('wb') as log:
   result=subprocess.run([sys.executable,'-B']+argv,cwd=root,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),stdout=log,stderr=subprocess.STDOUT)
  assert result.returncode==0,name+' failed: '+str(out/(name+'.log'))
  steps.append(name);print(name+': PASS',flush=True)
 for pkg in data['packages']:
  root=HERE/pkg['folder']/'original';stem=pkg['stem']
  # Bind both pinned and current source bytes; historical evidence cannot
  # silently survive changes to the canonical operator inputs.
  binding=json.loads((root/'SOURCE_BINDINGS.json').read_bytes())
  for name,digest in binding['source_sha256'].items():
   current=checked_path(REPO,name).read_bytes();assert sha(current)==digest
   assert current==checked_path(source,name).read_bytes()
  modes=[('',[],'verification.json')]
  if stem=='high_response':modes.append(('_arb',['--arb'],'verification_arb.json'))
  for suffix,flags,expected in modes:
   output=out/(stem+suffix+'.json')
   run('verify_'+stem+suffix,root,['verify_'+stem+'.py','--repo',str(source),'--out',str(output)]+flags)
   assert output.read_bytes()==(root/expected).read_bytes(),stem+suffix+' receipt differs'
   receipts.append({'package':pkg['id'],'file':output.name,'sha256':sha(output.read_bytes()),'byte_identical':True})
  if a.full:
   output=out/(stem+'_full.json')
   run('verify_'+stem+'_full',root,['verify_'+stem+'.py','--repo',str(source),'--out',str(output),'--full'])
 run('replay_controls',HERE,['check_replay.py'])
 report={'status':'PASS','integration_commit':head,'publication_base':pin,'family_manifest_sha256':sha((HERE/'SHA256SUMS').read_bytes()),
  'family_files':len(family),'original_files':len(data['original_files']),'receipts':receipts,'steps':steps,
  'large_operator_integrals_replayed':a.full,'independent_large_operator_implementation':False,'mathematical_review_changed':False,'A13_inputs_used':False}
 (out/'REPLAY.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
 print('ALL CROSS/HIGH RESPONSE REPLAYS PASS',flush=True)
if __name__=='__main__':main()
