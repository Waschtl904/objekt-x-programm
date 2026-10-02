"""Replay immutable archive contents against their historical source commit."""
from pathlib import Path,PurePosixPath
import argparse,hashlib,json,os,re,subprocess,sys,zipfile
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
 root=checked_path(out,pkg['original_folder']);assert not root.exists()
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
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);p.add_argument('--quick',action='store_true');a=p.parse_args()
 out=a.output.resolve();assert not out.is_relative_to(REPO.resolve()) and not out.exists()
 family=manifest(HERE);data=json.loads((HERE/'SOURCE_BINDINGS.json').read_bytes());out.mkdir(parents=True)
 head=subprocess.check_output(['git','-c','safe.directory='+REPO.as_posix(),'-C',str(REPO),'rev-parse','HEAD'],shell=False).decode().strip()
 for name,h in data['source_sha256'].items():assert sha(checked_path(REPO,name).read_bytes())==h,name
 assert len(data['packages'])==1;pkg=data['packages'][0];root=extract_package(pkg,out)
 allowed_scripts={(root/'replay.py').resolve(),(root/'check_sources.py').resolve(),(HERE/'check_replay.py').resolve()}
 steps=[]
 def run(label,script,arguments):
  script=script.resolve();assert script in allowed_scripts
  with (out/(label+'.log')).open('wb') as log:
   result=subprocess.run(['python','-B',str(script),*map(str,arguments)],executable=sys.executable,shell=False,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'),stdout=log,stderr=subprocess.STDOUT)
  assert result.returncode==0,label+' failed';steps.append(label);print(label+': PASS',flush=True)
 run('integration_controls',HERE/'check_replay.py',[])
 run('source_check',root/'check_sources.py',['--repo',REPO,'--out',out/'source_check.json'])
 run('package_replay',root/'replay.py',['--work-dir',out/'numerical',*(['--quick'] if a.quick else [])])
 inner=json.loads((out/'numerical/REPLAY.json').read_bytes());assert inner['status']=='PASS'
 assert inner['all_box_receipts_recomputed']==(not a.quick)
 assert inner['unique_box_evaluations_replayed']==(0 if a.quick else 1121)
 receipts=[]
 names=['known_point_slices.json','uncertainty_groups.json','angle_controls.json']+([] if a.quick else ['audit.json'])
 for name in names:
  raw=(out/'numerical'/name).read_bytes();assert raw==(root/name).read_bytes()
  receipts.append({'file':'numerical/'+name,'sha256':sha(raw),'byte_identical':True})
 assert (out/'source_check.json').read_bytes()==(root/'source_check.json').read_bytes()
 report={'status':'PASS','integration_commit':head,'publication_base':data['publication_base'],'family_manifest_sha256':sha((HERE/'SHA256SUMS').read_bytes()),'family_files':len(family),'original_files':len(pkg['original_sha256']),'source_files':len(data['source_sha256']),'receipts':receipts,'steps':steps,'full_numerical_replay':not a.quick,'unique_box_evaluations_replayed':inner['unique_box_evaluations_replayed'],'outcome':'UNRESOLVED','mathematical_review_changed':False,'large_operator_integrals_repeated':False,'A13_inputs_used':False}
 (out/'REPLAY.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
 print('ADAPTIVE ODD ANGLE INTEGRATION REPLAY PASS',flush=True)
if __name__=='__main__':main()
