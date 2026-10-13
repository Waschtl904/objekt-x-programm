"""Replay complete smooth correction and the global-function implementation.

--rebuild needs python-flint; the default rational replay is stdlib-only.
Neither mode certifies the still missing global Gram or total model error.
"""
from pathlib import Path
from fractions import Fraction as F
from concurrent.futures import ThreadPoolExecutor
import argparse,hashlib,json,os,subprocess,sys,tempfile
HERE=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def without_source_hashes(d):
    d=json.loads(json.dumps(d))
    for c in d['cases']:c.pop('response_sha256',None)
    return d
def compare(a,b):
    assert a['parity']==b['parity']
    assert not a['global_model_Gram_computed'] and not b['global_model_Gram_computed']
    assert not a['global_model_error_certified'] and not b['global_model_error_certified']
    for d in [a,b]:
        for key in ['endpoint_A_log_difference_norm','endpoint_A_fin_difference_norm','three_log_rows_difference_norm']:
            assert F(d[key][1])<F(1,10**45),(key,d[key])
    count=0
    for pa,pb in zip(a['points'],b['points']):
        assert pa['u']==pb['u']
        assert len(pa['raw_residual_model_1x203'])==len(pb['raw_residual_model_1x203'])==1
        aa=pa['raw_residual_model_1x203'][0];bb=pb['raw_residual_model_1x203'][0]
        assert len(aa)==len(bb)==203
        for va,vb in zip(aa,bb):
            la,ua=map(F,va);lb,ub=map(F,vb)
            assert la<=ua and lb<=ub
            assert max(la,lb)<=min(ua,ub),'model intervals do not overlap'
            assert max(ua-la,ub-lb)<F(1,10**60)
            count+=1
    assert count==609
    return count
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--rebuild',action='store_true');ap.add_argument('--python',default=sys.executable);ap.add_argument('--deps',type=Path);ap.add_argument('--receipt',type=Path);x=ap.parse_args();assert __debug__
    for fn,want in read(HERE/'MANIFEST.json')['files'].items():
        path=(HERE/fn).resolve();assert path.is_relative_to(HERE.resolve());assert sha(path)==want,fn
    print('MANIFEST_PASS',flush=True)
    checks=sum(compare(read(HERE/f'data/MODEL_{label}_3072.json'),read(HERE/f'data/MODEL_{label}_4096.json')) for label in ['EVEN','ODD'])
    with tempfile.TemporaryDirectory(prefix='objekt-x-global-function-') as td:
        td=Path(td);audit=td/'SMOOTH.json'
        subprocess.run([sys.executable,'-B',str(HERE/'audit_smooth_correction.py'),'--root',str(HERE/'snapshot'),'--out',str(audit)],check=True)
        assert without_source_hashes(read(audit))==without_source_hashes(read(HERE/'data/SMOOTH_CORRECTION.json'))
        if x.rebuild:
            env=os.environ.copy()
            if x.deps:env['PYTHONPATH']=str(x.deps.resolve())+os.pathsep+env.get('PYTHONPATH','')
            ca=td/'CAUCHY.json'
            subprocess.run([x.python,'-B',str(HERE/'check_cauchy.py'),'--root',str(HERE/'snapshot'),'--out',str(ca)],env=env,check=True)
            assert read(ca)==read(HERE/'data/CAUCHY_CHECK.json')
            def run(label):
                out=td/f'{label}.json'
                subprocess.run([x.python,'-B',str(HERE/'compute_global_model.py'),'--root',str(HERE/'snapshot'),'--bits','4096','--parity',label.lower(),'--out',str(out)],env=env,check=True)
                return compare(read(out),read(HERE/f'data/MODEL_{label}_3072.json'))
            with ThreadPoolExecutor(max_workers=2) as pool:assert sum(pool.map(run,['EVEN','ODD']))==1218
    receipt={'status':'PASS_GLOBAL_FUNCTION_IMPLEMENTATION_AND_COMPLETE_SMOOTH_CORRECTION',
      'stored_cross_precision_value_checks':checks,'fresh_function_rebuild':x.rebuild,
      'kernel_controls':read(HERE/'data/CAUCHY_CHECK.json')['total_checks'],
      'global_model_Gram_computed':False,'full_global_model_error_certified':False,'full_remainder_certified':False}
    if x.receipt:x.receipt.write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt),flush=True)
if __name__=='__main__':main()
