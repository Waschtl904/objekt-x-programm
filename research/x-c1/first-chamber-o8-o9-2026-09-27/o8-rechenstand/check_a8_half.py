"""Directed check of the full physical sufficient lower matrix at A8.

This is conditional on the analytic domain/tail/error argument in PROOF.md.
It never updates a repository status. No sampled eigenvalue is a certificate.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import argparse,gzip,hashlib,json,time
import flint
from flint import arb,arb_mat,fmpq,ctx
from generate_a8 import ldl,interval
from rational_bounds import gamma_bound,cosh_upper


def ball(pair,scale):
    lo,hi=map(int,pair)
    if lo>hi:raise ValueError('Reversed interval')
    return arb(fmpq(lo+hi,2*scale))+arb(0,arb(fmpq(hi-lo,2*scale)))


def af(q):
    return arb(fmpq(q.numerator,q.denominator))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--model',type=Path,default=Path(__file__).parent/'a8_model.json.gz')
    ap.add_argument('--output',type=Path,default=Path(__file__).parent/'reserve_results.json')
    args=ap.parse_args()
    ctx.prec=2048
    checks=[]
    def check(name,condition):
        if not condition:raise RuntimeError(name)
        checks.append(name)
    check('python-flint pinned to 0.9.0',flint.__version__=='0.9.0')
    raw=args.model.read_bytes()
    data=json.loads(gzip.decompress(raw))
    check('new endpoint and exact prime-2/prime-4 relations',data['endpoint']=='3*log(2)/2' and data['exact_shift_relations']=={'d2':'2/3','d4':'4/3'})
    check('raw cutoff 383 and both parity dimensions 191',data['cutoff']==383 and all(data['parities'][p]['dimension']==191 for p in ('even','odd')))
    check('new five-cell endpoint geometry',len(data['positive_half_cells'])==5)
    check('active family excludes q8',data['active_prime_powers']==[2,3,4,5,7])
    check('polynomial support includes all model Gamma response',data['model_high_support_last_degree']==383+data['Gamma_degree']+1)
    check('generator identity',hashlib.sha256((Path(__file__).parent/'generate_a8.py').read_bytes()).hexdigest()==data['generator_sha256'])
    check('rational bound source identity',hashlib.sha256((Path(__file__).parent/'rational_bounds.py').read_bytes()).hexdigest()==data['bounds_source_sha256'])
    eps=gamma_bound(data['Gamma_degree'],F(21,20))
    check('exact new Gamma residual reproduced',F(data['Gamma_kernel_error_exact'])==eps)
    # Bound M on the entire carrier-orthogonal parity space, not just low.
    z=F(21,40)
    even_ratio=cosh_upper(z)-1
    odd_ratio=z*z/(3*(1-z*z/20)) # sqrt(3) < 2, A >= 1 not needed here.
    check('full Mellin map norm <= 2 in both parities',1+even_ratio**2<4 and 1+odd_ratio**2<4)
    kernel_operator=F(21,10)*eps
    low_error=4*kernel_operator
    scale=10**data['scale_digits']
    check('stored Gamma interval contains exact rational bound',ball(data['Gamma_kernel_error'],scale).contains(af(eps)))
    matrices={}
    report={
        'status':'LOCAL_COMPUTATIONAL_RESULT_ANALYTIC_REVIEW_OPEN',
        'endpoint':'A8=log(8)/2','model_sha256':hashlib.sha256(raw).hexdigest(),
        'model_generator_sha256':data['generator_sha256'],
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'Gamma_degree':data['Gamma_degree'],'full_high_physical_floor':'1/2',
        'full_mellin_map_norm_upper':'2','tau':'1/1000',
        'Gamma_kernel_error_exact':str(eps),'Gamma_operator_error_exact':str(kernel_operator),
        'low_form_error_exact':str(low_error),
        'analytical_status':'LOCAL_DERIVATION_EXTERNAL_REVIEW_OPEN',
        'repository_O8_status_changed':False,'parities':{},'checks':checks,
    }
    for parity,label in enumerate(('even','odd')):
        start=time.time();p=data['parities'][label];n=p['dimension']
        first=384+parity
        em=z**first/factorial(first)/(1-z*z/((first+1)*(first+2)))
        if parity:em*=4
        coupling_error=2*kernel_operator+24*em
        L=arb_mat([[ball(v,scale) for v in row] for row in p['A']])
        G=arb_mat([[ball(v,scale) for v in row] for row in p['complete_model_raw_high_Gram']])
        check(label+' model matrices symmetric',all(L[i,j].overlaps(L[j,i]) and G[i,j].overlaps(G[j,i]) for i in range(n) for j in range(i)))
        H=G*arb(fmpq(1001,1000))
        for i in range(n):H[i,i]+=1001*af(coupling_error)**2
        lower=L-2*H
        for i in range(n):lower[i,i]-=af(low_error)
        matrices[label]={'dimension':n,'lower_matrix':[[interval(lower[i,j]) for j in range(n)] for i in range(n)]}
        print(label+': checking complete sufficient lower matrix',flush=True)
        low,piv,fail=ldl(lower)
        row={'dimension':n,'high_mellin_correction_exact':str(em),
             'coupling_operator_error_exact':str(coupling_error),
             'positive_directed_pivots':len(piv),
             'lower_matrix_is_full_form_bound':True,
             'coupling_Gram_includes_infinite_raw_high_response':True,
             'two_sided_mellin_correction_paid':True}
        if fail is not None:
            row.update(verdict='SUFFICIENT_LOWER_MATRIX_NOT_CERTIFIED',
                       first_unproved_pivot=interval(fail),
                       first_unproved_pivot_display=fail.str(30),
                       pivot_strictly_negative=bool(fail<0),
                       meaning='No negative source for the actual terminal form follows.')
        else:
            trace_inv=arb(0)
            for k in range(n):
                col=[arb(0)]*n
                for i in range(k,n):
                    col[i]=(arb(1) if i==k else arb(0))-sum((low[i][j]*col[j] for j in range(k,i)),arb(0))
                    trace_inv+=col[i]**2/piv[i]
            check(label+' finite inverse trace strictly positive',trace_inv>0)
            sigma=1/trace_inv
            coupling_sq=H.trace()
            check(label+' complete coupling norm upper positive',coupling_sq>0)
            inv_shear=(1+2*coupling_sq.sqrt())**2
            gap=min(sigma.lower(),arb(fmpq(1,2)))/(4*inv_shear)
            eta=gap/(gap+arb(fmpq(23,2)))
            check(label+' strict full physical and defect reserves',gap>0 and eta>0)
            row.update(verdict='STRICT_POSITIVE_SUFFICIENT_LOWER_MATRIX',
                       min_pivot_display=min(piv).str(30),
                       schur_reserve=interval(sigma),schur_reserve_display=sigma.str(40),
                       coupling_norm_squared_upper=interval(coupling_sq),
                       inverse_shear_squared_upper=interval(inv_shear),
                       full_physical_reserve=interval(gap),full_physical_reserve_display=gap.str(40),
                       full_defect_reserve=interval(eta),full_defect_reserve_display=eta.str(40),
                       all_positive_pivot_intervals=[interval(v) for v in piv])
        row['check_seconds']=time.time()-start
        report['parities'][label]=row
        print(label+': '+row['verdict']+'; positive pivots '+str(len(piv)),flush=True)
        if 'full_physical_reserve_display' in row:print('physical '+row['full_physical_reserve_display']+'; defect '+row['full_defect_reserve_display'],flush=True)
    report['both_parities_strictly_certified']=all(r['verdict']=='STRICT_POSITIVE_SUFFICIENT_LOWER_MATRIX' for r in report['parities'].values())
    report['check_count']=len(checks)
    report['scale_digits']=100
    args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    matrix_path=args.output.with_name(args.output.stem+'_lower_matrices.json.gz')
    matrix_path.write_bytes(gzip.compress((json.dumps({'scale_digits':100,'parities':matrices},separators=(',',':'))+'\n').encode(),mtime=0))
    print('RESULT '+str(args.output),flush=True)


if __name__=='__main__':main()
