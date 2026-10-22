"""Exact rational budget and coordinate-hull audit; Python standard library only."""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import json,hashlib
if not __debug__:
 raise SystemExit('Verification requires assertions enabled; Python -O/-OO is rejected.')
HERE=Path(__file__).resolve().parent
def sqrtup(x):
 x=Q(x);assert x>=0;s=10**120;scaled=x*s*s;n=isqrt(scaled.numerator//scaled.denominator)
 if Q(n*n)<scaled:n+=1
 out=Q(n,s);assert out*out>=x;return out
def upper(v):
 assert len(v)==2 and Q(v[0])<=Q(v[1]);return Q(v[1])
def read(name):return json.loads((HERE/name).read_bytes())
validation=read('orientation-validation.json');b=validation['bounds']
assert validation['scalar_checks_pass']
assert all(max(abs(Q(v))for v in r['identity_defect'])<Q('1e-25')for r in validation['scalar_checks'])
# Exported intervals are rounded outward to an 80-decimal grid. The live
# calculation checked 1e-100; the portable receipt supports the weaker 1e-70.
assert all(max(abs(Q(v))for v in r['defining_integral_identity_defect'])<Q('1e-70')for r in validation['kernel_checks'])
assert upper(b['whole_raw_g_bound_recomputed'])<14
change=(14+upper(b['Gamma_operator_allowance']))*sqrtup(upper(b['du_X_norm_squared']))
change+=upper(b['direct_moment_X_error'])+upper(b['moment_truncation_X_allowance'])
wr=read('budget-inputs/WHOLE_RESULT.json');finite=read('budget-inputs/FINITE_RESULT.json')
oldnorm=sqrtup(Q(5,21))*(sqrtup(Q(wr['model_X_norm_squared_upper']))+Q(wr['core_bridge_X_error_upper'])+Q(wr['core_quadrature_X_error_upper']))+Q(wr['whole_operator_model_Ldual_error_upper'])
newnorm=oldnorm+sqrtup(Q(5,21))*change;d=newnorm**2;dcap=Q('1e-9');assert d<dcap
beta=Q(finite['beta']);cc=Q(finite['c']);f=Q(finite['F_upper_cap']);z=Q(finite['residual_P_norm_cap'])
assert upper(finite['F_interval'])<f and upper(finite['finite_bounds']['residual_P_norm'])<z
full=f+(dcap/beta+z*z+2*z*sqrtup(cc*dcap/beta))/(1-cc);budget=Q(finite['budget_interval'][0]);assert full<budget
coords=read('core-tail.json')['rows'];orientation=read('kernel-orientation-81.json')['rows'];local=read('localized-81.json')['rows'];assert len(coords)==len(local)==len(orientation)==84
strong=[]
for r,o,l in zip(coords,orientation,local):
 p0,p1=map(Q,l['partial_pairing']);n0,n1=map(Q,l['expanded_model'])
 d0,d1=map(Q,o['orientation_correction']);h0,h1=map(Q,r['signed_core_tail_correction'])
 lo=p0-n1+d0+h0;hi=p1-n0+d1+h1
 envelope=upper(l['integration_error'])+upper(r['remaining_core_error'])
 magnitude=max(abs(lo),abs(hi));assert magnitude<=envelope
 strong.append({'coordinate':r['coordinate'],'raw_arithmetic_difference':[str(lo),str(hi)],'justified_error_envelope':str(envelope),'full_arithmetic_hull_contained':True,'margin':str(envelope-magnitude)})
for r in coords:
 lo,hi=map(Q,r['final_difference']);assert lo<=0<=hi
 a0,a1=map(Q,r['after_orientation_difference']);d0,d1=map(Q,r['signed_core_tail_correction'])
 error=upper(r['remaining_core_error']);assert lo<=a0+d0-error and a1+d1+error<=hi
for r in orientation:
 lo,hi=map(Q,r['corrected_difference']);a0,a1=map(Q,r['old_difference']);d0,d1=map(Q,r['orientation_correction'])
 assert lo<=a0+d0 and a1+d1<=hi
out={'status':'EXACT_RATIONAL_ARITHMETIC_PASS_CONDITIONAL_ON_BOUND_ANALYTIC_INPUTS','defect_confirmed':True,
 'kernel_identity_checks':len(validation['kernel_checks']),'scalar_controls':len(validation['scalar_checks']),
 'coordinate_hulls_cover_zero_after_correction':len(coords),'signed_panels':81,
 'full_arithmetic_hulls_within_justified_errors':len(strong),'minimum_hull_coverage_margin':str(min(Q(r['margin'])for r in strong)),
 'coordinate_checks':strong,
 'max_integration_error':str(max(upper(r['integration_error'])for r in local)),
 'max_corrected_difference_absolute_upper':str(max(max(abs(Q(v))for v in r['final_difference'])for r in coords)),
 'correction_X_upper':str(change),'repaired_residual_Ldual_norm_upper':str(newnorm),'repaired_residual_Ldual_energy_upper':str(d),
 'energy_cap':str(dcap),'full_comparison_energy_upper':str(full),'budget_lower':str(budget),'strict_margin_lower':str(budget-full),
 'p_error_recharged':False,'external_review':'OPEN','full_degree_11_space_closed':False,'odd_parity_closed':False,'point_4_closed':False,
 'inputs':{p:hashlib.sha256((HERE/p).read_bytes()).hexdigest()for p in ['orientation-validation.json','kernel-orientation-81.json','core-tail.json','localized-81.json','budget-inputs/WHOLE_RESULT.json','budget-inputs/FINITE_RESULT.json']}}
(HERE/'rational-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for k,v in out.items():
 if k not in ['inputs','coordinate_checks']:print(k,float(Q(v))if isinstance(v,str)and('/'in v or v.replace('.','',1).isdigit())else v)
