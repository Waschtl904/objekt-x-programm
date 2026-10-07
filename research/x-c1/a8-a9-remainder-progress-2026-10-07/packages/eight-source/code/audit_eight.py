"""Exact rational final checks, independent of the Arb LDL implementation."""
from pathlib import Path
from fractions import Fraction as F
import json, argparse, hashlib

def read(p): return json.loads(p.read_bytes())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def bound(a,sign):
    n=len(a);out=[[sum(map(F,a[i][j]))/2 for j in range(n)] for i in range(n)]
    assert all(a[i][j]==a[j][i] for i in range(n) for j in range(n))
    for i in range(n):out[i][i]+=sign*sum((F(a[i][j][1])-F(a[i][j][0]))/2 for j in range(n))
    return out
def add(a,b,c=F(1)):
    return [[x+c*y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def ldl(a):
    n=len(a);l=[[F(0)]*n for _ in range(n)];ds=[]
    for i in range(n):
        d=a[i][i]-sum(l[i][k]**2*ds[k] for k in range(i))
        ds.append(d)
        if d<=0:return False,ds
        l[i][i]=1
        for j in range(i+1,n):l[j][i]=(a[j][i]-sum(l[j][k]*l[i][k]*ds[k] for k in range(i)))/d
    return True,ds
def quadratic(a,v):return sum(v[i]*a[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))
def serialize(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [serialize(y) for y in x]
    if isinstance(x,dict):return {k:serialize(v) for k,v in x.items()}
    return x

BOUND_VARIATIONS=[]
def compare(a,b,path=''):
    if isinstance(a,dict):
        for k in a:
            if k not in ('seconds','bits','program_sha256'):compare(a[k],b[k],path+'/'+k)
    elif isinstance(a,list):
        assert len(a)==len(b),path
        if len(a)==2 and all(isinstance(x,str) for x in a):
            try:lo,hi=map(F,a);bl,bh=map(F,b)
            except ValueError:assert a==b,path
            else:
                assert lo<=hi and bl<=bh,path
                gap=max(lo,bl)-min(hi,bh)
                if gap>0:
                    # Independently rounded majorants need not enclose a common
                    # unique scalar. Genuine model integrals must still overlap.
                    allowed=['/Gamma_upper/','/S_lower/','/corrected_source_energy_upper/',
                             '/old_source_inverse_energy_upper/','/inverse_check/']
                    assert any(k in path for k in allowed) and gap<F('1e-32'),(path,gap)
                    BOUND_VARIATIONS.append({'path':path,'gap':gap})
        else:
            for i,(x,y) in enumerate(zip(a,b)):compare(x,y,path+'/'+str(i))
    else:assert a==b,(path,a,b)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--primary',type=Path,required=True);ap.add_argument('--higher',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();assert not args.out.exists()
    a=read(args.primary);b=read(args.higher);assert a['bits']==3072 and b['bits']==4096
    compare(a,b)
    records=[]
    for r in a['blocks']:
        # Reconstruct the final separate lower matrix from K and Gamma.
        km=bound(r['K_lower'],-1);gp=bound(r['Gamma_upper'],1)
        sl=add(km,gp,-1);wu=bound(r['reference_gram_upper'],1)
        wl=bound(r['reference_gram_lower'],-1)
        assert ldl(wl)[0]
        ok,piv=ldl(sl)
        assert ok==r['separate_positive']
        floors=[]
        for eta in r['certified_trial_relative_floors']:
            passed,ds=ldl(add(sl,wu,-F(eta)));assert passed,(r['parity'],eta)
            floors.append({'eta':eta,'positive_exact_pivots':ds})
        old=[[sl[i][j] for j in range(2)] for i in range(2)]
        assert ldl(old)[0] and r['two_source_subblock_positive']
        headline=F('4e-12' if r['parity']=='even' else '3e-11')
        exact_headline=[]
        for run in [a,b]:
            rr=next(x for x in run['blocks'] if x['parity']==r['parity'])
            ss=add(bound(rr['K_lower'],-1),bound(rr['Gamma_upper'],1),-1)
            passed,ds=ldl(add(ss,bound(rr['reference_gram_upper'],1),-headline))
            assert passed,(r['parity'],run['bits'],'headline floor')
            exact_headline.append({'bits':run['bits'],'positive_exact_pivots':ds})
        records.append({'parity':r['parity'],'reference_positive':True,'separate_positive':ok,'exact_pivots':piv,
                        'certified_relative_floors':floors,'headline_relative_floor':headline,
                        'headline_verified_independently_for_both_runs':exact_headline,'previous_subblock_positive':True})
    # Negative control: a deliberately negative diagonal must be rejected.
    assert not ldl([[F(-1),F(0)],[F(0),F(1)]])[0]
    out={'status':'PASS_EXACT_FINAL_CHECKS','primary_sha256':sha(args.primary),'higher_sha256':sha(args.higher),
         'precision_comparison':'All model-integral enclosures overlap; independently rounded derived majorants differ by less than 1e-32. Each run independently passes exact final floor checks.',
         'derived_majorant_differences':BOUND_VARIATIONS,
         'blocks':records,'negative_control_rejected':True,'external_review':'OPEN',
         'scope':'Independent rational final matrix checks, not an independent reconstruction of all integrals or inherited analytic assumptions.'}
    args.out.write_text(json.dumps(serialize(out),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':out['status'],'blocks':[{'parity':r['parity'],'positive':r['separate_positive'],'floors':[x['eta'] for x in r['certified_relative_floors']]} for r in records]}))
if __name__=='__main__':main()
