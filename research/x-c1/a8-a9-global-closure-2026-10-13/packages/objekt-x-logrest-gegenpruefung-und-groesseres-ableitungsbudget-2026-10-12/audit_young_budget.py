"""Exact rational improvement of the unchanged regularized-tail target.

This computes allowed budgets, not the actual regularized derivative Gram.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, json, zipfile

RESP='Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11'
LOG='Objekt-X-Aussenresidualpruefung-und-Logarithmischer-Randtail-2026-10-11'
GATE='Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11'

def sha(p):
    with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def floor12(x):return F((x*10**12).numerator//(x*10**12).denominator,10**12)
def read(p):return json.loads(p.read_bytes())

def run(root,responses,review):
    d104=F(11,10)+sum((F(1,n) for n in range(1,105)),F(0))
    derivative_factor=104*105*d104
    with zipfile.ZipFile(review/'inputs'/(GATE+'.zip')) as z:
        gates=json.loads(z.read(GATE+'/ATTACHMENT_GATES.json'))['cases']
    original=read(root/'AUDIT.json')['cases']
    rows=[]
    for p,label in enumerate(['EVEN','ODD']):
        rp=responses/f'RESPONSES_{label}.json';r=read(rp)
        sigma=F(r['sufficient_complete_QR_normalized_budget'])
        assert sigma==F(r['beta'])*(1-F(r['M_actual_normalized_upper_scalar']))>0
        c8=F(1,5000) if p==0 else F(13,20000)
        clog=F(original[p]['three_log_full_weighted_tail_relative_to_T_upper'])
        assert clog==(F(1,500) if p==0 else F(1,250))
        e=F(gates[p]['basis84_dual_contribution_relative_to_D_upper'])+F(1,10**300)
        theta=F(21 if p==0 else 15)
        def target(t):
            # E_target = a*T_budget - b*D, entirely rational.
            assert t>0
            return derivative_factor*t/(1+t)*(1-c8-(1+t)*clog), derivative_factor*t/(1+t)*e
        a0,b0=target(F(1));a1,b1=target(theta)
        oldscalar=a0*sigma-b0;newscalar=a1*sigma-b1
        assert floor12(oldscalar)==F(original[p]['sufficient_E_g_tail_scalar_relative_to_D'])
        assert newscalar>oldscalar>0
        # Matrix enlargement, not just a scalar numerical observation:
        # T>=sigma*D implies a*T-b*D >= (a-b/sigma)*T for b>=0.
        gain=F(183,100) if p==0 else F(1769,1000)
        da=a1-gain*a0;db=b1-gain*b0
        assert db>0
        relative_T_margin=da-db/sigma
        assert relative_T_margin>0
        # A rational scalar target really fits the complete Young budget.
        newfloor=floor12(newscalar)
        spent=c8+(1+theta)*clog+(1+1/theta)*newfloor/(derivative_factor*sigma)+e/sigma
        assert spent<=1
        assert a1>0 and a1*sigma-b1>0
        # Independent algebraic identity: optimize the scalar Young bound.
        # With B=1-c8-e/sigma and l=clog, the budget function is
        # K*sigma*(B*t/(1+t)-l*t). At t=sqrt(B/l)-1 its
        # supremum is K*sigma*(sqrt(B)-sqrt(l))^2. No irrational
        # optimizer is used in any certificate.
        B=1-c8-e/sigma
        assert newscalar==derivative_factor*sigma*(B*theta/(1+theta)-clog*theta)
        assert B>clog
        rows.append({'parity':label.lower(),'response_file_sha256':sha(rp),
          'directional_budget_definition':'T=beta*(D-M_upper); D and M_upper are unchanged response data',
          'D_lower_coefficient_of_T':str(sigma),'c8':str(c8),'c_log':str(clog),
          'basis_and_moment_price_relative_to_D':str(e),'young_parameter':str(theta),
          'old_target_coefficient_T':str(a0),'old_target_subtracted_coefficient_D':str(b0),
          'new_target_coefficient_T':str(a1),'new_target_subtracted_coefficient_D':str(b1),
          'old_scalar_target_floor':str(floor12(oldscalar)),
          'new_scalar_target_floor':str(newfloor),
          'uniform_Loewner_improvement_factor':str(gain),
          'positive_target_difference_margin_relative_to_T':str(relative_T_margin),
          'total_budget_fraction_at_scalar_target_upper':str(spent),
          'actual_regularized_derivative_Gram_computed':False,'full_remainder_certified':False})
        print(label,'theta',theta,'old target',float(floor12(oldscalar)),
              'new target',float(newfloor),'uniform matrix factor >',float(gain),flush=True)
    return {'status':'PASS_EXACT_RATIONAL_ENLARGED_DERIVATIVE_TARGETS',
            'derivative_factor_10920_d104':str(derivative_factor),'cases':rows,
            'inherited_operator_hypotheses':True,'actual_regularized_derivative_Gram_computed':False,
            'full_remainder_certified':False,'tail_floor_1_over_20_certified':False}

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for k in ['input','responses','review','out']:ap.add_argument('--'+k,type=Path,required=True)
    x=ap.parse_args();assert __debug__
    out=run(x.input,x.responses,x.review)
    x.out.write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
