"""Compare current optimized targets with the certified directional target.

Also give a complete conditional L2-error certificate for rounded log subtraction.
No global residual integral is evaluated by this script.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,sys

def read(p):return json.loads(p.read_bytes())
def floorq(x,digits):
    v=x*10**digits;return F(v.numerator//v.denominator,10**digits)

def main(current,prior,responses,out):
    sys.path.insert(0,str(current));import interval_helpers as h
    ld=h.ld;new=read(current/'GLOBAL_BUDGET.json')
    previous=read(prior/'data/YOUNG_BUDGET_AUDIT.json')
    direction=read(prior/'data/DIRECTIONAL_DERIVATIVE_TARGET.json')
    G=h.rat(direction['full_log_tail_Gram_rational_upper_3x3']);Gi=h.inv(G)
    rows=[]
    for p,label in enumerate(['EVEN','ODD']):
        a=new['cases'][p];old=previous['cases'][p];d=direction['cases'][p]
        r=read(responses/f'RESPONSES_{label}.json');rho=F(r['rho']);beta=F(r['beta'])
        K=h.rat(r['K12_new_rational']);M=h.rat(r['M_upper_rational'])
        D=[[1-rho if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
        T=[[beta*(D[i][j]-M[i][j]) for j in range(203)] for i in range(203)]
        d104=F(a['d104']);newT=10920*d104*F(a['remaining_Ug_target_T_coefficient_before_d104']);newD=10920*d104*F(a['remaining_Ug_target_D_subtraction_before_d104'])
        oldT=F(d['derivative_target_coefficient_T']);oldD=F(d['derivative_target_subtracted_coefficient_D']);cg=F(d['derivative_target_subtracted_coefficient_CtGC'])
        C=h.rat(d['coefficient_midpoints_3x203'])
        # E_dir(old)-E_theta(new)>0, with every full matrix entry retained.
        top=[[(oldT-newT)*T[i][j]-(oldD-newD)*D[i][j] for j in range(203)] for i in range(203)]
        block=[[ld.point(top[i][j]/cg) if i<203 and j<203 else ld.point(C[j-203][i]) if i<203 else ld.point(C[i-203][j]) if j<203 else ld.point(Gi[i-203][j-203]) for j in range(206)] for i in range(206)]
        proof=ld.positive(block)
        # All inherited coefficient errors plus rounding radii are present.
        ec=[F(v) for v in d['total_coefficient_errors_D_dual']]
        dc=sum((h.sqrtup(G[i][i])*ec[i] for i in range(3)),F(0))
        assert dc<F(1,10**10)
        u=F(a['sufficient_global_Ug_upper_relative_to_D'])
        eps=F(1,1000)
        lowerroot=h.sqrtup(u)-F(1,10**100);assert lowerroot*lowerroot<=u
        deltaR=floorq(eps*lowerroot/2-dc,18)
        assert deltaR>0 and 4*(deltaR+dc)**2<=eps**2*u
        # Stronger mathematical optimality check than merely testing an
        # interval LOWER endpoint: certify the reported UPPER gap <1e-7.
        gap=F(a['scalar_normalized_target_optimality_gap_upper']);assert 0<=gap<F(1,10**7)
        newe=F(a['sufficient_global_Eg_tail_upper_relative_to_D']);olde=F(old['new_scalar_target_floor'])
        increase=100*(newe/olde-1)
        rows.append({'parity':label.lower(),'optimized_scalar_derivative_target':str(newe),
          'previous_review_scalar_derivative_target':str(olde),
          'increase_percent_over_previous_review':str(increase),
          'previous_directional_target_strictly_dominates_new_optimized_target':proof,
          'normalized_optimality_gap_upper_checked':str(gap),
          'rounded_log_subtraction_tail_D_dual_error_upper':str(dc),
          'simplified_log_subtraction_error_cap':'1/10000000000',
          'L2_target_lower_relative_to_D':str(u),
          'model_Gram_target_fraction':'999/1000',
          'sufficient_additional_FULL_residual_model_D_dual_error_upper':str(deltaR),
          'additional_model_error_bound_proved_for_actual_model':False,
          'global_model_Gram_computed':False,'full_remainder_certified':False})
        print(label,'PASS E_dir(previous)>E_theta(new); 206 pivots; rounded-log error <1e-10; conditional full model error <=',float(deltaR),flush=True)
    out.write_text(json.dumps({'status':'PASS_TARGET_CONSOLIDATION_AND_CONDITIONAL_L2_MODEL_BUDGET',
      'cases':rows,'new_global_residual_integral_computed':False,'full_remainder_certified':False},indent=2)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for k in ['current','prior','responses','out']:ap.add_argument('--'+k,type=Path,required=True)
    x=ap.parse_args();assert __debug__;main(x.current,x.prior,x.responses,x.out)
