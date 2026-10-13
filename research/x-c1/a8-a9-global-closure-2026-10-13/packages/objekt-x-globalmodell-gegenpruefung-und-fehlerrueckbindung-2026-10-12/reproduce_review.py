"""Self-contained replay. It does not assert any unproved global bound."""
from pathlib import Path
import argparse,hashlib,json,os,subprocess,sys,tempfile,zipfile
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(cmd,env=None):subprocess.run(cmd,check=True,env=env)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rebuild-models',action='store_true');ap.add_argument('--diagnostic',action='store_true');ap.add_argument('--deps',type=Path);ap.add_argument('--receipt',type=Path);x=ap.parse_args();assert __debug__
    for fn,want in read(HERE/'MANIFEST.json')['files'].items():
        p=(HERE/fn).resolve();assert p.is_relative_to(HERE.resolve());assert sha(p)==want,fn
    print('MANIFEST_PASS',flush=True)
    env=os.environ.copy()
    if x.deps:env['PYTHONPATH']=str(x.deps.resolve())+os.pathsep+env.get('PYTHONPATH','')
    with tempfile.TemporaryDirectory(prefix='objekt-x-function-review-') as td:
        td=Path(td);z=next((HERE/'inputs').glob('Objekt-X-Globale-Funktionsdarstellung*.zip'))
        assert sha(z)=='86e510b6d68f5b70345f7ce710491fd09e7d8818cff3be6565fd8254d16581e3'
        with zipfile.ZipFile(z) as a:
            for n in a.namelist():assert not Path(n).is_absolute() and '..' not in Path(n).parts
            a.extractall(td)
        pkg=td/z.stem
        cmd=[sys.executable,'-B',str(pkg/'reproduce.py')]
        if x.rebuild_models:cmd+=['--rebuild']
        run(cmd,env)
        result=td/'BOOTSTRAP.json'
        run([sys.executable,'-B',str(HERE/'audit_bootstrap.py'),'--package',str(pkg),'--inputs',str(HERE/'data/BOOTSTRAP_INPUT.json'),'--out',str(result)],env)
        assert read(result)==read(HERE/'data/BOOTSTRAP_AUDIT.json')
        if x.diagnostic:
            result=td/'DIAGNOSTIC.json'
            run([sys.executable,'-B',str(HERE/'diagnose_quadrature.py'),'--package',str(pkg),'--inputs',str(HERE/'data/BOOTSTRAP_INPUT.json'),'--points',str(HERE/'data/quadrature'),'--out',str(result)],env)
            actual=read(result);stored=read(HERE/'data/DIAGNOSTIC_SUMMARY.json')
            assert len(actual['cases'])==len(stored['cases'])==2
            for a,b in zip(actual['cases'],stored['cases']):
                assert len(a['quadratures'])==len(b['quadratures'])==2
                for aa,bb in zip(a['quadratures'],b['quadratures']):
                    assert aa['order']==bb['order']
                    k='weighted_sample_matrix_largest_eigenvalue_relative_to_H'
                    assert abs(aa[k]-bb[k])<1e-10
                    assert not aa['whole_interval_upper_bound']
    receipt={'status':'PASS_RATIONAL_MODEL_REVIEW_AND_CONDITIONAL_ERROR_ABSORPTION',
       'fresh_global_models_rebuilt':x.rebuild_models,'numerical_diagnostic_replayed':x.diagnostic,
       'global_model_Gram_upper_certified':False,'remaining_independent_model_defect_certified':False,
       'full_remainder_certified':False,'tail_floor_1_over_20_certified':False}
    if x.receipt:x.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
