"""Directed A8 check using the explicit high Mellin graph metric.

Uses the previously built complete model Gram. This is a new sufficient
matrix check, not an independent reconstruction of the model or a review
of the analytic form-domain arguments. Requires python-flint 0.9.0.
"""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import gzip,hashlib,json,sys,time

HERE=Path(__file__).resolve().parent
BASE=HERE.parent/'o8-rechenstand'
sys.path.insert(0,str(BASE))
import flint
from flint import arb,arb_mat,fmpq,ctx
from generate_a8 import ldl,interval
from check_a8 import ball,af
from rational_bounds import gamma_bound


def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    ctx.prec=2048
    checks=[]
    def check(name,truth):
        if not truth:raise RuntimeError(name)
        checks.append(name)
    check('python-flint 0.9.0',flint.__version__=='0.9.0')
    old=json.loads((BASE/'reserve_refined.json').read_bytes())
    data=json.loads(gzip.decompress((BASE/'a8_model.json.gz').read_bytes()))
    tail=json.loads((BASE/'refined_tail.json').read_bytes())
    common=json.loads((BASE/'common_reserve.json').read_bytes())
    check('model bytes bound to previous positive check',digest(BASE/'a8_model.json.gz')==old['model_sha256'])
    check('model generator and rational bound sources',data['generator_sha256']==digest(BASE/'generate_a8.py') and data['bounds_source_sha256']==digest(BASE/'rational_bounds.py'))
    check('previous directed checker source',old['checker_sha256']==digest(BASE/'check_a8.py'))
    check('sharper high floor source and result',tail['high_physical_floor']=='2/3' and tail['source_sha256']==digest(BASE/'refine_tail.py') and old['refined_tail_binding_sha256']==digest(BASE/'refined_tail.json'))
    check('previous common reserve binding',common['reserve_results_sha256']==digest(BASE/'reserve_refined.json'))
    check('endpoint dimensions degree and both earlier passes',data['endpoint']=='3*log(2)/2' and data['cutoff']==383 and data['Gamma_degree']==160 and old['both_parities_strictly_certified'])
    epsilon=gamma_bound(160,F(21,20))
    gamma=F(21,10)*epsilon
    eL=4*gamma
    eC=2*gamma
    delta=F(2,3)
    graph_error=F(1,10**930)
    check('Gamma and low errors reproduced',epsilon==F(data['Gamma_kernel_error_exact']) and gamma==F(old['Gamma_operator_error_exact']) and eL==F(old['low_form_error_exact']))
    check('H383 below 7',sum((F(1,k) for k in range(1,384)),F(0))<7)
    check('QPhi below 400 using supplied majorants',14+272+8+2*(F(5,2)+F(21,40)+F(63,20))<400)
    check('Q carrier below 12 using supplied majorants',1+4+F(5,2)+F(21,40)+F(63,20)<12)
    check('delta-specific graph comparison coefficient',1/delta==F(3,2) and (1/delta)*F(1001,1000)==F(3003,2000))
    scale=10**data['scale_digits']
    matrix_output={'scale_digits':100,'parities':{}}
    report={
        'status':'LOCAL_GRAPH_SCHUR_CHECK_ANALYTIC_REVIEW_OPEN',
        'endpoint':'A8=log(8)/2','delta':'2/3','precision_bits':2048,'scale_digits':100,
        'model_sha256':digest(BASE/'a8_model.json.gz'),
        'previous_reserve_sha256':digest(BASE/'reserve_refined.json'),
        'checker_sha256':digest(Path(__file__)),
        'source_bindings':{name:digest(BASE/name) for name in ('generate_a8.py','check_a8.py','rational_bounds.py','refine_tail.py','refined_tail.json')},
        'new_error_split':{
            'low_form_error_exact':str(eL),
            'raw_high_model_coupling_error_exact':str(eC),
            'separate_graph_schur_error_exact':str(graph_error),
            'Gram_coefficient':'3003/2000',
            'error_diagonal':'eL + (3003/2)*eC^2 + 10^-930'
        },
        'parities':{},'checks':checks,
        'original_24_user_reported_tests_reproduced':False,
        'model_rebuilt_in_this_check':False,
        'repository_status_changed':False
    }
    z=F(21,40)
    for parity,label in enumerate(('even','odd')):
        start=time.time()
        n=384+parity
        em=z**n/factorial(n)/(1-z*z/((n+1)*(n+2)))
        if parity:em*=4
        check(label+' exact high moment bound matches existing certificate',em==F(old['parities'][label]['high_mellin_correction_exact']))
        display_bound=F(173,100*10**935) if parity==0 else F(939,100*10**938)
        check(label+' supplied decimal moment bound',em<display_bound)
        check(label+' raw low density below 272 squared',sum(2*k+1 for k in range(parity+2,384,2))<272**2)
        check(label+' complete coupling below 401',400+24*em<401)
        difference=19224*em+160801*em**2
        check(label+' graph error for original half floor',2*difference<graph_error)
        check(label+' graph error for sharper two-thirds floor',difference/delta<graph_error)
        full_error=eC+24*em
        check(label+' full coupling error matches executed original checker',full_error==F(old['parities'][label]['coupling_operator_error_exact']))

        sigma_previous=F(int(old['parities'][label]['schur_reserve'][0]),scale)
        check(label+' graph matrix retains positive certified floor by scalar transfer',sigma_previous-graph_error>sigma_previous/2)
        # F_graph - F_old = delta^-1*1001*(eB^2-eC^2) - graph_error.
        relative_shift=1001*(full_error**2-eC**2)/delta-graph_error
        check(label+' exact difference of error diagonals is at least minus graph error',relative_shift>=-graph_error)

        p=data['parities'][label]
        dim=p['dimension']
        check(label+' dimension 191',dim==191)
        L=arb_mat([[ball(v,scale) for v in row] for row in p['A']])
        G=arb_mat([[ball(v,scale) for v in row] for row in p['complete_model_raw_high_Gram']])
        Hraw=G*af(F(1001,1000))
        Hfull=arb_mat(Hraw)
        for i in range(dim):
            Hraw[i,i]+=1001*af(eC)**2
            Hfull[i,i]+=1001*af(full_error)**2
        lower=L-Hraw/af(delta)
        for i in range(dim):lower[i,i]-=af(eL+graph_error)
        matrix_output['parities'][label]={'dimension':dim,'lower_matrix':[[interval(lower[i,j]) for j in range(dim)] for i in range(dim)]}
        print(label+': directed LDL for explicit graph-budget lower matrix',flush=True)
        low,piv,fail=ldl(lower)
        check(label+' all 191 directed pivots positive',fail is None and len(piv)==191)
        inverse_trace=arb(0)
        for k in range(dim):
            col=[arb(0)]*dim
            for i in range(k,dim):
                col[i]=(arb(1) if i==k else arb(0))-sum((low[i][j]*col[j] for j in range(k,i)),arb(0))
                inverse_trace+=col[i]**2/piv[i]
        check(label+' inverse trace positive',inverse_trace>0)
        sigma=1/inverse_trace
        # B_hat=G_H^(-1/2) B, so ||B_hat|| <= ||B||.
        b2=Hfull.trace()
        check(label+' full coupling norm estimate positive',b2>0)
        denominator=(2+b2.sqrt()/af(delta))**2+1
        physical=min(sigma.lower(),af(delta))/denominator
        eta=physical/(physical+af(F(23,2)))
        check(label+' original common physical floor retained',physical>af(F(12,10**30)))
        check(label+' original common defect floor retained',eta>af(F(1,10**30)))
        report['parities'][label]={
            'dimension':dim,'positive_directed_pivots':len(piv),
            'high_moment_error_exact':str(em),
            'graph_Gram_difference_majorant_exact':str(difference),
            'graph_schur_error_majorant_exact':str(difference/delta),
            'sigma_previous_lower_endpoint_exact':str(sigma_previous),
            'sigma_transfer_floor_exact':str(sigma_previous-graph_error),
            'new_minus_old_diagonal_exact':str(relative_shift),
            'schur_reserve':interval(sigma),'schur_reserve_display':sigma.str(35),
            'complete_coupling_norm_squared_upper':interval(b2),
            'physical_conversion_denominator':interval(denominator),
            'physical_reserve':interval(physical),'physical_reserve_display':physical.str(35),
            'defect_reserve':interval(eta),'defect_reserve_display':eta.str(35),
            'all_positive_pivot_intervals':[interval(v) for v in piv],
            'elapsed_seconds':time.time()-start
        }
        print(label+': 191 positive pivots; physical '+physical.str(20)+'; defect '+eta.str(20),flush=True)
    report['check_count']=len(checks)
    report['both_parities_strictly_positive']=True
    report['retained_common_physical_floor']='1.2e-29'
    report['retained_common_defect_floor']='1e-30'
    matrices=HERE/'graph_lower_matrices.json.gz'
    matrices.write_bytes(gzip.compress((json.dumps(matrix_output,separators=(',',':'))+'\n').encode(),mtime=0))
    report['lower_matrices_sha256']=digest(matrices)
    (HERE/'graph_check_results.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(str(len(checks))+' targeted checks PASS; both graph-budget matrices strictly positive',flush=True)


if __name__=='__main__':main()
