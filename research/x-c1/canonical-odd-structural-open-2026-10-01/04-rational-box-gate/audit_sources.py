from pathlib import Path
import argparse,json,os,subprocess,sys,tempfile
from verify_box_gate import dependencies,SHA

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
 with tempfile.TemporaryDirectory(prefix='box-source-audit-') as name:
  temp=Path(name);folder,_,_,_,_,_=dependencies(temp);out=temp/'source.json'
  subprocess.run([sys.executable,'-B',str(folder/'audit_sources.py'),'--repo',str(args.repo),'--out',str(out)],
   check=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
  result={'status':'PASS','upstream_archive_sha256':SHA,'inherited_audit':json.loads(out.read_bytes()),'A13_inputs_used':False}
  assert result['inherited_audit']['status']=='PASS'
  args.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
 print('Canonical sources bound by the four-variable certifier: PASS')
if __name__=='__main__':main()
