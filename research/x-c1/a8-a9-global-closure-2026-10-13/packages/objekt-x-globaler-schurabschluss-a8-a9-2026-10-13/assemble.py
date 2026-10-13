"""Exact final residual assembly. Analytic enclosures remain bound inputs.

No eigensolver, numerical inverse, tail cutoff, or assumed 1/20 floor.
Run after the bound input replays; see reproduce.py.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, sys

def read(p): return json.loads(p.read_bytes())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def subset(a, b, path=''):
    if isinstance(a, dict):
        assert isinstance(b, dict), path
        for k, v in a.items():
            assert k in b, (path, k)
            subset(v, b[k], path+'/'+k)
    elif isinstance(a, list):
        assert isinstance(b, list) and len(a)==len(b), path
        for i, (v,w) in enumerate(zip(a,b)): subset(v,w,path+'/'+str(i))
    else: assert a==b, path

def assemble(gram, responses, logreview, innerlogs, exterior, common, out):
    sys.path.insert(0,str(gram/'snapshot/work/global-model-2026-10-12'))
    import interval_helpers as h
    target=read(gram/'snapshot/work/global-model-2026-10-12/DIRECTIONAL_DERIVATIVE_TARGET.json')
    assert target==read(logreview/'data/DIRECTIONAL_DERIVATIVE_TARGET.json')
    origins=read(gram/'SNAPSHOT_ORIGINS.json')
    bindings=[]
    # Bind every response field used by the new integral to its full predecessor.
    for label in ['EVEN','ODD']:
        for rel, original in [
            (f'work/new-responses84-2026-10-11/RESPONSES_{label}.json',responses/f'RESPONSES_{label}.json'),
            (f'work/inner-log-2026-10-12/COMPOSED_{label}_3072.json',innerlogs/f'COMPOSED_{label}_3072.json'),
            (f'work/inner-log-2026-10-12/TRACES_{label}_3072.json',innerlogs/f'TRACES_{label}_3072.json')]:
            subset(read(gram/'snapshot'/rel),read(original))
            assert sha(original)==origins[rel]['original_sha256']
            bindings.append({'snapshot':rel,'original_sha256':sha(original),'exact_field_subset':True})
    for name in ['REFINED_INPUT.json','REFINED_COMMON96.json']:
        rel='work/direct-rest84-2026-10-11/'+name
        subset(read(gram/'snapshot'/rel),read(common/name))
        assert sha(common/name)==origins[rel]['original_sha256']
        bindings.append({'snapshot':rel,'original_sha256':sha(common/name),'exact_field_subset':True})
    gates=read(exterior/'ATTACHMENT_GATES.json')['cases']
    extaudit=read(exterior/'AUDIT_EXTERIOR.json')['cases']
    d104=F(11,10)+sum((F(1,k) for k in range(1,105)),F(0))
    G=h.pts(h.rat(target['full_log_tail_Gram_rational_upper_3x3']))
    cases=[]
    for p,label in enumerate(['EVEN','ODD']):
        r=read(responses/f'RESPONSES_{label}.json'); t=target['cases'][p]
        gr=read(gram/f'data/AUDIT_{label}_3072.json')
        assert t['parity']==gr['parity']==gates[p]['parity']==extaudit[p]['parity']==label.lower()
        assert gr['review_conditions_C5_closed']
        q=F(3,10000)
        assert F(gr['actual_regularized_Gram_relative_H_upper'])<q
        eta=F(r['eta']); beta=F(r['beta']); rho=F(r['rho'])
        assert eta==F(1,10**10) and beta==1-eta-F(16198,18219)>0
        K=h.rat(r['K12_new_rational']); MU=h.pts(h.rat(r['M_upper_rational']))
        D=h.pts([[1-rho if i==j and i<191 else K[i-191][j-191]
                  if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)])
        T=h.sc(h.add(D,MU,-1),beta)
        upper=F(r['M_actual_normalized_upper_scalar'])
        sigma=F(r['sufficient_complete_QR_normalized_budget'])
        assert sigma==beta*(1-upper)>0
        print(label,'checking inherited scalar gap directly in full matrices',flush=True)
        gapcert=h.ld.positive(h.add(h.sc(D,upper),MU,-1))
        j=F(gates[p]['basis84_dual_contribution_relative_to_D_upper'])
        assert j==F(extaudit[p]['basis84_dual_price_relative_to_D'])
        e=j+F(1,10**300)
        assert F(gates[p]['geometric_correction_computed_upper'])<F(1,10**300)
        c8=F(extaudit[p]['actual_first_eight_weighted_gram_relative_to_directional_budget_upper'])
        assert c8==[F(1,5000),F(13,20000)][p]
        clog=F(t['joint_log_upper_relative_to_T'])
        assert clog==[F(1,500),F(1,250)][p]
        theta=F(t['young_parameter'])
        qC=F(t['weighted_joint_log_upper_coefficient_CtGC'])
        qD=F(t['weighted_joint_log_upper_coefficient_D'])
        a=F(t['derivative_target_coefficient_T'])/10920
        b=F(t['derivative_target_subtracted_coefficient_D'])/10920
        c=F(t['derivative_target_subtracted_coefficient_CtGC'])/10920
        # Independently establish the complete target identity, including all prices.
        k=d104*theta/(1+theta)
        assert a==k*(1-c8)
        assert b==k*e+d104*theta*qD
        assert c==d104*theta*qC
        C=h.pts(h.rat(t['coefficient_midpoints_3x203']))
        CGC=h.mmI(h.T(C),h.mmI(G,C))
        Qlog=h.add(h.sc(CGC,qC),h.sc(D,qD))
        H=h.add(h.add(h.sc(T,a),h.sc(D,b),-1),h.sc(CGC,c),-1)
        # Complete Q_g <= U_g/d104 <= q H/d104. No derivative is assumed.
        young=[F(3,8),F(4,15)][p]
        QR=h.add(h.add(h.sc(D,e),h.sc(T,c8)),
                 h.add(h.sc(Qlog,1+young),h.sc(H,(1+1/young)*q/d104)))
        cap=[F(1,250),F(71,10000)][p]
        uniform_g=q*theta/(1+theta)*(1-c8)
        uniform=e/sigma+c8+(1+young)*clog+(1+1/young)*uniform_g
        assert uniform<cap<1
        print(label,'checking complete directional residual majorant',flush=True)
        finalcert=h.ld.positive(h.add(h.sc(T,cap),QR,-1))
        # R* S^-1 R <= beta^-1 QR, so A S^-1 A* <= (1-kappa)D.
        kappa=(1-cap)*(1-upper)
        form_L=eta+kappa*beta
        form_W=F(21,5)*form_L
        easy_W=[F(1328,10**9),F(7978,10**9)][p]
        assert form_W>easy_W>0 and form_W<F(1,20)
        cases.append({'parity':label.lower(),'d104':str(d104),'beta':str(beta),
          'actual_regularized_Gram_relative_H_cap':str(q),
          'basis84_price_relative_D':str(j),'full_moment_price_relative_D':'1e-300',
          'eight_exterior_rows_relative_T':str(c8),'joint_log_relative_T':str(clog),
          'new_log_rest_Young_parameter':str(young),
          'complete_QR_definition':'(j+1e-300)D+c8*T+(1+s)*Qlog_bar+(1+1/s)*(3/10000)*H/d104',
          'complete_QR_relative_T_scalar_upper':str(uniform),
          'complete_QR_relative_T_simple_upper':str(cap),
          'final_203x203_directional_LDL':finalcert,'M_upper_scalar_gap_LDL':gapcert,
          'finite_M_upper_relative_D':str(upper),'ASinvAstar_gap_relative_D':str(kappa),
          'reduced_comparison_form_lower_relative_L':str(form_L),
          'reduced_comparison_form_lower_relative_WX':str(form_W),
          'simple_lower_relative_WX':str(easy_W),
          'interpretation':'Lower bound on T after eliminating the twelve physical sources in D-U_new; the actual old-eliminated Schur form dominates this comparison.',
          'tail_floor_1_over_20_in_its_separate_target_metric_certified':False})
        print(label,'PASS full QR <',str(cap),'T; reduced WX floor >',str(easy_W),flush=True)
    # Countercontrol: log/rest cross terms cannot be dropped even in dimension one.
    log, reg=F(1,10),F(3,10)
    assert (log+reg)**2>log**2+reg**2
    # A positive Schur complement follows by congruence, without assuming a tail 1/20.
    K, cr, rest=F(2),F(1),F(3)
    for z,r in [(F(-1),F(2)),(F(2),F(-3))]:
        assert K*z*z+2*cr*z*r+rest*r*r==K*(z+cr*r/K)**2+(rest-cr*cr/K)*r*r
    result={'status':'PASS_COMPLETE_FORMDUAL_RESIDUAL_AND_CONDITIONAL_A8_A9_POSITIVITY',
      'cases':cases,'snapshot_field_bindings':bindings,
      'full_203_force_dual_residual_comparison_closed':True,
      'A8_to_A9_positivity_under_bound_operator_domain_and_decomposition_hypotheses':True,
      'tail_floor_1_over_20_certified':False,'all_horizons_certified':False,
      'object_X_constructed':False,'RH_proved':False,'external_mathematical_review_open':True,
      'new_full_global_integrations_repeated_in_this_review':False,
      'countercontrols':{'missing_log_rest_cross_terms_rejected':True,'Schur_congruence_exact':True}}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for name in ['gram','responses','logreview','innerlogs','exterior','common','out']:
        ap.add_argument('--'+name,type=Path,required=True)
    x=ap.parse_args(); assert __debug__
    assemble(**vars(x))
