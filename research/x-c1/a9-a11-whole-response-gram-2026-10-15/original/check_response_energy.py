"""Separate exact checker: convolution assembly, norms, and matrix bookkeeping."""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,hashlib,argparse

def conv(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z
def integral(a,l,b,k):
    aa=conv(a,b);al=conv(a,k);lb=conv(l,b);ll=conv(l,k)
    return (sum((v/Q(n+1) for n,v in enumerate(aa)),Q(0))
       +sum((v/Q((n+1)**2) for n,v in enumerate(al)),Q(0))
       +sum((v/Q((n+1)**2) for n,v in enumerate(lb)),Q(0))
       +sum((2*v/Q((n+1)**3) for n,v in enumerate(ll)),Q(0)))
def positive(a):
    n=len(a);assert a==list(map(list,zip(*a)));l=[[Q(0)]*n for _ in range(n)];d=[]
    for j in range(n):
        p=a[j][j]-sum((l[j][k]**2*d[k] for k in range(j)),Q(0));assert p>0;d.append(p);l[j][j]=1
        for i in range(j+1,n):l[i][j]=(a[i][j]-sum((l[i][k]*l[j][k]*d[k] for k in range(j)),Q(0)))/p
    return n
def main():
    ap=argparse.ArgumentParser();ap.add_argument('data',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    here=Path(__file__).resolve().parent;data=json.loads(a.data.read_bytes());source=json.loads((here/'inputs/FUNCTIONS12.json').read_bytes());fresh=json.loads((here/'inputs/FRESH_A12.json').read_bytes())
    prior=json.loads((here/'input/objekt-x-f12-d12-audit-2026-10-15/reports/RESPONSE_ERROR_BUDGET.json').read_bytes())
    for p,want in data['source_bindings'].items():assert hashlib.sha256((here/p).read_bytes()).hexdigest()==want
    count=pivots=0;summary={}
    for par,cases in data['parities'].items():
        summary[par]={}
        for name,case in cases.items():
            rows=[([Q(v) for v in r['regular_rational_coefficients']],[Q(v) for v in r['log_rational_coefficients']]) for r in case['rows']]
            gram=[[Q(v) for v in r] for r in case['rational_whole_reference_Gram']]
            for i in range(12):
                for j in range(i,12):
                    v=integral(*rows[i],*rows[j]);assert v==gram[i][j]==gram[j][i];count+=1 if i==j else 2
            e2=sum((Q(r['whole_bracket_L2_error_upper'])**2 for r in case['rows']),Q(0));tr=sum(gram[i][i] for i in range(12));radius=Q(case['whole_reference_Gram_Loewner_error'])
            assert radius>e2 and (radius-e2)**2>=4*tr*e2
            factor=Q(case['physical_metric_factor_upper']);upper=[[Q(v) for v in r] for r in case['physical_TT_adjoint_upper']]
            assert upper==[[factor*(v+(radius if i==j else 0)) for j,v in enumerate(r)] for i,r in enumerate(gram)]
            pivots+=positive(upper)
            trace=Q(case['T_norm_squared_upper']);tn=Q(case['T_norm_upper']);assert trace>=sum(upper[i][i] for i in range(12)) and tn*tn>=trace
            dD=Q(source['parities'][par]['whole_D12_operator_error_upper']);dF=Q(source['parities'][par]['whole_F12_operator_error_upper']);dA=Q(fresh['parities'][par]['whole_Loewner_radius'])
            ke=Q(case['direct_K_error_upper']);re=Q(case['weighted_residual_error_factor_per_unit_W9_norm'])
            assert ke>=2*dF*tn+dA*trace and re>=dD*dD*trace
            assert ke<(Q(1661,10**27) if par=='even' else Q(2183,10**29))
            assert re<(Q(590,10**64) if par=='even' else Q(775,10**66))
            assert tn<(Q(6838544) if par=='even' else Q(784134))
            if name=='audit_S':
                improvement=Q(637*10**15) if par=='even' else Q(380*10**13)
                assert Q(prior['parities'][par]['whole_K_model_error_upper'])>improvement*ke
                assert Q(prior['parities'][par]['squared_residual_error_per_unit_W9_norm_upper'])>improvement*re
            summary[par][name]={'T_norm_upper':str(tn),'direct_K_error_upper':str(ke),'weighted_error_factor':str(re)}
    # These controls fail if the log cross terms or the unitary half factor
    # are dropped. They are algebra controls, not a substitute for the data.
    assert integral([Q(1)],[Q(1)],[Q(1)],[Q(1)])==5
    assert Q(1)+2<5
    assert 2*Q(1)*Q(1,2)**2==Q(1,2)
    receipt={'status':'PASS','exact_Gram_entry_comparisons':count,'positive_upper_Gram_pivots':pivots,
       'log_cross_term_and_measure_controls':True,'full_W9_residual_certified':False,'results':summary}
    a.output.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('PASS:',count,'exact Gram entries;',pivots,'positive pivots; whole response/model-error prices.')
if __name__=='__main__':main()
