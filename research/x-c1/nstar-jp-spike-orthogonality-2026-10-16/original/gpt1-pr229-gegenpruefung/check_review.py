"""Independent downstream rational checks; not a full source-integral replay."""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import json,hashlib

ROOT=Path(__file__).resolve().parent
SRC=ROOT/'source'
CERT=SRC/'original/gpt2-stufe4-hochantwort/expected'
SCALE=10**100

def read(p): return json.loads(p.read_text())
def interval(x):
    a,b=map(F,x)
    if a>b: raise ValueError('Reversed interval')
    return a,b
def sqrthi(x):
    if x<0: raise ValueError('Negative square')
    k=isqrt(x.numerator*SCALE*SCALE//x.denominator)
    return F(k+1,SCALE)
def show(x): return format(float(x),'.14g')

def main():
    bindings=read(SRC/'SOURCE_BINDINGS.json')['files']
    matched=[]
    for name,record in bindings.items():
        p=SRC/name
        if p.exists():
            if hashlib.sha256(p.read_bytes()).hexdigest()!=record['sha256']:
                raise ValueError('Hash mismatch: '+name)
            matched.append(name)
    high=read(CERT/'COMPLETE_HIGH_RESPONSE.json')
    prices=read(CERT/'SPIKE_SCALAR_D_MODEL_ERROR.json')
    budget=read(SRC/'stufe4/D12_ERROR_BUDGET.json')
    result={'scope':'Downstream rational check conditional on saved input enclosures; no full replay.',
            'verified_selected_source_bindings':matched,'parities':{}}
    limits={'even':{'upper_v':F('.016'),'lower_Pv':F(902),'orthogonal_difference':F('4.43e-10')},
            'odd':{'upper_v':F('.00245'),'lower_Pv':F(23),'orthogonal_difference':F('5.61e-11')}}
    delta=F(18219,10000)
    for parity,case in high.items():
        gamma=interval(case['full_M_norm_squared'])[1]
        out={}
        for name,d in case['directions'].items():
            yy=interval(d['full_model_y_norm_squared'])
            cb=interval(d['model_c_Bh_cross'])
            bb=interval(d['full_model_Bstar_c_norm_squared'])
            lo=yy[0]-2*cb[1]+bb[0]
            hi=yy[1]-2*cb[0]+bb[1]
            if lo<=0: raise ValueError('Model residual positivity unresolved')
            r_bound=sqrthi(hi)+interval(d['high_difference_error_upper'])[1]
            h_bound=sqrthi(gamma)*r_bound/delta
            if not h_bound<limits[parity][name]: raise ValueError('High bound failed')
            chi=interval(d['whole_physical_chi_norm_upper'])[1]
            priceD=chi*F(prices[parity]['delta_D_upper'])
            priceR=chi*F(prices[parity]['whole_Hilbert_residual_model_error_upper'])
            if name=='lower_Pv':
                if not priceR<F('1.86e-13' if parity=='even' else '2.668e-16'):
                    raise ValueError('Residual scalar error bound failed')
            out[name]={'model_r_squared_recomputed':[show(lo),show(hi)],
                       'high_norm_recomputed_upper':show(h_bound),
                       'safe_rational_high_bound':str(limits[parity][name]),
                       'D_scalar_model_error_upper':show(priceD),
                       'residual_scalar_model_error_upper':show(priceR)}
        pairs=read(SRC/f'stufe4/HIGH_PAIRINGS_{parity}.json')
        rows=pairs['rows']
        gram_diff=F(pairs['check_||B*c||^2_from_function'])-F(pairs['check_cT_G0_c'])
        cross_diff=F(pairs['check_<B*c,y_f>_from_function'])-F(pairs['archive_<c,B_Th_f>'])
        model_r2_upper=interval(case['directions']['upper_v']['full_model_high_difference_norm_squared'])[1]
        out['diagnostics']={
            'pair_count':len(rows),
            'max_abs_r':show(max(abs(F(x['r_vj'])) for x in rows)),
            'max_abs_ell_mid':show(max(abs(F(x['ell_v(D_j) Mittelpunkt'])) for x in rows)),
            'Gram_check_difference':show(gram_diff),
            'cross_check_difference':show(cross_diff),
            'whole_residual_squared_using_quadrature_checks':show(model_r2_upper+gram_diff-2*cross_diff),
            'budget_note':budget[parity]['note'],
            'D12_pairings_certified':False}
        result['parities'][parity]=out
    (ROOT/'REVIEW_CHECKS.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({'matched_bindings':len(matched),'parities':result['parities']},indent=2,ensure_ascii=False))

if __name__=='__main__': main()
