"""Fresh inherited source audit with no repository changes."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile
from verify_projector_transport import load_input,SHA

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
 with tempfile.TemporaryDirectory(prefix='projector-source-audit-') as name:
  temp=Path(name);folder,_,_=load_input(temp);out=temp/'source.json'
  subprocess.run([sys.executable,'-B',str(folder/'audit_sources.py'),'--repo',str(args.repo),'--out',str(out)],
   check=True,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
  data=json.loads(out.read_bytes());assert data['status']=='PASS'
  result={'status':'PASS','upstream_archive_sha256':SHA,'inherited_audit':data,
   'A13_inputs_used':False,'large_operator_solves_rerun':False}
  args.out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
 print('Inherited canonical source bindings: PASS')
if __name__=='__main__':main()
