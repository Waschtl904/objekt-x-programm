"""Rational audit of a conditional absorption of the low-F modelling error.

Neither the global integral nor the remaining physical-model defect is certified.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys,gzip
from math import factorial
def read(p):return json.loads(p.read_bytes())
def traceprod(a,b):return sum((a[i][j]*b[j][i] for i in range(len(a)) for j in range(len(a))),F(0))
def main(pkg,inputs,out):
    sys.path.insert(0,str(pkg));import interval_helpers as h
    data=read(inputs);direction=read(pkg/'data/DIRECTIONAL_DERIVATIVE_TARGET.json')
    G=h.rat(direction['full_log_tail_Gram_rational_upper_3x3'])
    inner=read(pkg/'snapshot/work/inner-log-2026-10-12/INNER_LOG_1536.json')
    old=read_gzip(next((pkg/'snapshot').rglob('a8_model.json.gz')))
    gamma=F(old['Gamma_kernel_error_exact'])
    gamma_abs=sum((abs(F(v))*F(11,10)**k for k,v in enumerate(old['Gamma_polynomial_coefficients'])),F(0))+gamma
    assert gamma_abs<1
    prime_sum=F(0)
    for power,prime,logcap,sqrtlow in [(2,2,F(7,10),F(14,10)),(3,3,F(11,10),F(17,10)),(4,2,F(7,10),F(2)),(5,5,F(17,10),F(22,10)),(7,7,F(2),F(26,10)),(8,2,F(7,10),F(28,10))]:
        assert sqrtlow**2<=power
        assert sum((logcap**k/factorial(k) for k in range(21)),F(0))>prime
        prime_sum+=logcap/sqrtlow
    assert prime_sum<4
    rows=[]
    for i,r in enumerate(data['cases']):
        d=direction['cases'][i];K=h.rat(r['K12_new_rational']);Ki=h.inv(K)
        rho=F(r['rho']);beta=F(r['beta']);delta=F(r['delta'])
        assert r['M_upper_diagonal_191']==[r['M_upper_rational'][j][j] for j in range(191)]
        assert r['M_upper_finite12']==[row[191:] for row in r['M_upper_rational'][191:]]
        traceM=sum(map(F,r['M_upper_diagonal_191']))/(1-rho)+traceprod(Ki,h.rat(r['M_upper_finite12']))
        traceT=beta*(203-traceM)
        C=h.rat(d['coefficient_midpoints_3x203'])
        CDiCt=[[sum((C[j][k]*C[l][k]/(1-rho) for k in range(191)),F(0))+sum((C[j][191+k]*Ki[k][m]*C[l][191+m] for k in range(12) for m in range(12)),F(0)) for l in range(3)] for j in range(3)]
        logtrace=traceprod(G,CDiCt)
        Htrace=(F(d['derivative_target_coefficient_T'])*traceT-F(d['derivative_target_subtracted_coefficient_D'])*203-F(d['derivative_target_subtracted_coefficient_CtGC'])*logtrace)/10920
        assert Htrace>0 and logtrace>=0
        m=h.sqrtup(F(999,1000)*Htrace)+h.sqrtup(logtrace)
        assert m<20
        # Additional freezing radii, in the same normalized feature metric.
        lf=inner['cases'][i]['new_low_F_model']
        rad=[[abs(F(v[1])-F(v[0]))/2 for v in row] for row in lf]
        mid2=sum((rad[k][j]*abs(Ki[j][l])*rad[k][l] for k in range(191) for j in range(12) for l in range(12)),F(0))/(1-rho)
        ee=h.sqrtup(F(r['finite_feature_error_metric_trace'][1]))+h.sqrtup(mid2)
        assert ee<1
        x=h.sqrtup(F(r['fixed_X_squared_HS_in_D_inverse_metric'][1]))
        # The exact high source has HS norm <13; inherited complete errors included.
        htrace=sum((F(v[1]) for v in r['H84_new_model_diagonal']),F(0))
        hJ=h.sqrtup(delta*htrace)+h.sqrtup(F(84))*F(r['high_source_error_norm'][1])
        assert hJ<13
        sJ=F(300)+10*hJ/delta
        assert sJ<400
        target=F(['0.000000676796364171','0.000001628860045447'][i])
        allowed_base=(1-ee)*(target-F(1,10**300))-ee*(20+400*x)
        assert allowed_base>0
        # Round down to a portable decimal for the remaining independent defect.
        den=10**18;floor=F((allowed_base*den).numerator//(allowed_base*den).denominator,den)
        checked=(floor+ee*(20+400*x))/(1-ee)+F(1,10**300)
        assert checked<=target
        qcap=F(2*10**14 if i==0 else 10**13)
        assert F(r['qmodel_HS_norm'][1])<qcap
        oldgamma=30*gamma*qcap/delta
        assert oldgamma < F(6 if i==0 else 3,10**14 if i==0 else 10**15)
        rows.append({'parity':r['parity'],'trace_H_in_D_metric':str(Htrace),
          'model_log_tail_Gram_trace_in_D_metric':str(logtrace),
          'raw_model_tail_norm_cap_conditional_on_Gram_gate':'20',
          'raw_model_tail_norm_computed_upper_conditional_on_Gram_gate':str(m),
          'additional_frozen_lowF_midpoint_error_norm_upper':str(h.sqrtup(mid2)),
          'normalized_lowF_error_norm_upper':str(ee),
          'actual_hJ_HS_norm_upper':str(hJ),'raw_SJ_operator_norm_upper':str(sJ),
          'raw_SJ_simplified_cap':'400','full_X_D_dual_HS_norm_upper':str(x),
          'sufficient_remaining_independent_defect_norm_upper':str(floor),
          'resulting_total_model_norm_error_upper_conditional':str(checked),
          'previous_sufficient_total_model_norm_error_cap':str(target),
          'old_Gamma160_component_norm_upper_with_same_raw_projection':str(oldgamma),
          'remaining_independent_defect_bound_proved':False,
          'global_model_Gram_upper_certified':False,'full_remainder_certified':False})
        print(r['parity'],'PASS absorption; factor',float(ee),'remaining defect budget',float(floor),'Gamma160 part',float(oldgamma),flush=True)
    result={'status':'PASS_CONDITIONAL_LOW_FEATURE_ERROR_ABSORPTION',
       'exact_kernel_regular_part_absolute_bound_on_radius_11_over_10':str(gamma_abs),
       'six_prime_shift_weights_sum_rational_upper':str(prime_sum),
       'core_shell_operator_norm_simplified_cap':'10','shell_Q_Lambda_J_operator_norm_cap':'300',
       'cases':rows,'global_model_Gram_upper_certified':False,'full_global_model_error_certified':False,'full_remainder_certified':False}
    out.write_text(json.dumps(result,indent=2)+'\n')
def read_gzip(p):return json.loads(gzip.decompress(p.read_bytes()))
if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for name in ['package','inputs','out']:ap.add_argument('--'+name,type=Path,required=True)
    x=ap.parse_args();main(x.package,x.inputs,x.out)
