"""Replay immutable archive contents against their historical source commit."""
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
def extract_package(pkg,out):
 archive=checked_path(HERE,pkg['archive']);assert sha(archive.read_bytes())==pkg['archive_sha256']
 root=out/pkg['original_folder'];assert not root.exists()
 with zipfile.ZipFile(archive) as z:
  prefix=pkg['original_folder']+'/'
  expected={prefix+n for n in pkg['original_sha256']}
  assert set(z.namelist())==expected and len(z.namelist())==len(expected) and z.testzip() is None
  for name in sorted(expected):
   raw=z.read(name);rel=name[len(prefix):];assert sha(raw)==pkg['original_sha256'][rel]
   target=checked_path(root,rel);target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(raw)
  m=json.loads((root/'manifest.json').read_bytes())['sha256']
  assert set(m)|{'manifest.json'}==set(pkg['original_sha256'])
  assert all(pkg['original_sha256'][name]==h for name,h in m.items())
 for original,visible in pkg['visible_copies'].items():
  assert (root/original).read_bytes()==checked_path(HERE,visible).read_bytes()
 return root
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--full',action='store_true');a=p.parse_args()
 out=a.output.resolve();assert not out.is_relative_to(REPO.resolve()) and not out.exists()
 family=manifest(HERE);data=json.loads((HERE/'SOURCE_BINDINGS.json').read_bytes());out.mkdir(parents=True)
 git=['git','-c','safe.directory='+REPO.as_posix(),'-c','core.longpaths=true','-C',str(REPO)]
 head=subprocess.check_output(git+['rev-parse','HEAD']).decode().strip();pin=data['publication_base'];source=out/'source'
 subprocess.run(['git','-c','safe.directory='+REPO.as_posix(),'clone','--shared','--no-checkout',str(REPO),str(source)],check=True,capture_output=True)
 sg=['git','-c','safe.directory='+source.as_posix(),'-c','core.longpaths=true','-c','core.autocrlf=false','-C',str(source)]
 subprocess.run(sg+['config','core.longpaths','true'],check=True,capture_output=True)
 subprocess.run(sg+['checkout','--detach',pin],check=True,capture_output=True)
 for name,h in data['source_sha256'].items():
  assert sha(checked_path(source,name).read_bytes())==h,name
  assert sha(checked_path(REPO,name).read_bytes())==h,name
 steps=[]
 def run(label,args):
  with (out/(label+'.log')).open('wb') as log:
   proc=subprocess.run([sys.executable,'-B',*map(str,args)],env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),stdout=log,stderr=subprocess.STDOUT)
  assert proc.returncode==0,label+' failed; see '+str(out/(label+'.log'))
  steps.append(label);print(label+': PASS',flush=True)
 roots=[extract_package(pkg,out) for pkg in data['packages']]
 extra=['--full'] if a.full else []
 run('full_shift',[roots[0]/'replay.py','--repo',source,'--work-dir',out/'full-shift',*extra])
 reuse=['--expanded-primal',out/'full-shift'] if a.full else []
 run('primal_dual',[roots[1]/'replay.py','--repo',source,'--primal-package',roots[0],'--work-dir',out/'primal-dual',*reuse,*extra])
 run('integration_controls',[HERE/'check_replay.py'])
 receipts=[]
 for name in ('gate.json','angle.json','counterfamily.json'):
  raw=(out/'primal-dual'/name).read_bytes();assert raw==(roots[1]/name).read_bytes()
  receipts.append({'file':'primal-dual/'+name,'sha256':sha(raw),'byte_identical':True})
 report={'status':'PASS','integration_commit':head,'publication_base':pin,'family_manifest_sha256':sha((HERE/'SHA256SUMS').read_bytes()),'family_files':len(family),'source_files':len(data['source_sha256']),'original_files':sum(len(pkg['original_sha256']) for pkg in data['packages']),'receipts':receipts,'steps':steps,'large_operator_integrals_replayed_in_this_run':a.full,'prior_full_spot_replays':2,'independent_large_operator_implementation':False,'Y68_status':'TARGET_EXCLUSION','odd_angle_status':'UNRESOLVED','bounded_counterfamily_status':'BOUNDED_SEARCH_UNRESOLVED','mathematical_review_changed':False,'A13_inputs_used':False}
 (out/'REPLAY.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
 print('ALL FULL-SHIFT / PRIMAL-DUAL REPLAYS PASS',flush=True)
if __name__=='__main__':main()
