"""Launch fresh complete integrations after reproduce.py has unpacked inputs."""
from pathlib import Path
import argparse,subprocess,sys,os,json
ROOT=Path(__file__).resolve().parent
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out',type=Path,required=True,help='New output directory for a fresh run.')
    ap.add_argument('--parity',choices=['even','odd'],required=True)
    ap.add_argument('--deps',type=Path,help='Optional Python dependency directory.')
    args=ap.parse_args();out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
    task=ROOT/'work/galerkin84-2026-10-10';env=os.environ.copy()
    if args.deps:env['PYTHONPATH']=str(args.deps.resolve())+os.pathsep+env.get('PYTHONPATH','')
    target=out/f'GALERKIN_{args.parity.upper()}_3072.json'
    assert not target.exists(),'Select a fresh output directory.'
    launch="import runpy,sys;from pathlib import Path;p=sys.argv[1];sys.argv=sys.argv[1:];sys.path.insert(0,str(Path(p).parent));runpy.run_path(p,run_name='__main__')"
    subprocess.run([sys.executable,'-B','-c',launch,str(task/'compute_galerkin84.py'),'--bits','3072','--parity',args.parity,'--out',str(target)],cwd=ROOT,env=env,check=True)
    from fractions import Fraction as F
    expected=json.loads((task/target.name).read_bytes());actual=json.loads(target.read_bytes());n=0
    for key in ['H84_model','C84_model','R84_model','direct_cross_model','complete_source_high_cross_model']:
        for ra,rb in zip(expected[key],actual[key]):
            assert len(ra)==len(rb)
            for va,vb in zip(ra,rb):
                a,b=map(F,va);c,d=map(F,vb);assert max(a,c)<=min(b,d),(key,va,vb);n+=1
    receipt={'status':'PASS_FRESH_COMPLETE_INTEGRATION_COMPARISON','parity':args.parity,'matrix_entry_comparisons':n,'full_remainder_certified':False}
    (out/'COMPARISON.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8');print(json.dumps(receipt,indent=2))
if __name__=='__main__':main()
