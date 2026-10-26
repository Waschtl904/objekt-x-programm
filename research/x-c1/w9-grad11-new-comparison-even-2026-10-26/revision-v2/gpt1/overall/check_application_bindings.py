"""GPT1: exact conditions for the new analytic applications; no quadrature."""
from pathlib import Path
from fractions import Fraction as Q
from math import factorial
import json,hashlib,sys
if sys.flags.optimize or not __debug__:raise SystemExit('OPTIMIZED_PYTHON_REJECTED')
P=Path(__file__).resolve().parent
H=P.parent/'new-comparison-review-2026-10-26/author/workspace/work/breakthrough-2026-10-25'
R=P.parent/'revision-v2-review-2026-10-26/merged/workspace/work/breakthrough-2026-10-25/revision_v2'
def need(x,msg):
    if not x:raise RuntimeError(msg)
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
rows=[]
for i in range(12):
    label=f'T{i:02d}';ef=H/f'ENDPOINT_INGREDIENTS_{label}.json';e=read(ef);v=e['values']
    hi=lambda k:Q(v[k][1])
    caps=read(H/f'CONTOUR_CAPS_{label}.json')
    need(caps['endpoint_ingredients_sha256']==sha(ef),'Real ingredient binding')
    for key in ['physical_shell_coefficients_norm','source_moment_coefficient','moment_multiplier']:
        need(0<=hi(key)<1,f'{label} small coefficient {key}')
    ph=hi('Phi_ff_real_sup');z=32*hi('finite_p_Euclidean_norm');s=hi('shell_polynomial_real_sup');lm=hi('shell_moment_lm')
    tail=sum(abs(Q(a))for a in e['signed_strip_constant']);width=Q(e['signed_strip_width'][1])
    g=40*ph+40*z+20*s+1000*lm
    F=ph+10*g+hi('low_projection_real_sup')+3*hi('core_measure_total_variation')+3*tail*width+3*lm
    hc=2*hi('ell_global_sup')+hi('quot_global_sup')+hi('gamma_global_sup')+1000+hi('D_polynomial_cell_sup')+2*hi('Dv_sup')+100
    E=100*(F+hc+z+s+hi('core_measure_Cauchy_bound')+hi('momentR')+tail+1)
    need(Q(caps['static_log_envelope'])==F and Q(caps['h_log_envelope'])==hc,'Real coefficient formula')
    need(Q(caps['whole_endpoint_log_squared_envelope'])==E and Q(caps['static_Cauchy_source_L1_upper'])==3*F,'Endpoint and Cauchy formula')
    small=read(H/f'SMALL_MODEL_CHANGES_{label}.json');need(small['input_sha256']==sha(ef),'Moment input binding')
    lam=2*lm;alpha=10*(F+hc+1);u=100*(F+hc+1);qpsi=100*(40*z+20*s+1000*lm+1);eps=Q(2,factorial(160))
    moment=eps*(100*(300*lam+2*alpha+2*lam)+2*qpsi+100*u+24*lam)
    lift=1000*eps*(u+ph+1)
    need(moment==Q(small['moment_X_error_upper']) and lift==Q(small['high_lift_X_error_upper']),'Moment/lift formula')
    need(moment+lift==Q(small['small_raw_upper'])<Q('1e-150'),'Moment/lift allowance')
    physical=read(R/f'WHOLE_PHYSICAL_ERROR_V2_{label}.json')['quantities']
    gamcap=Q(physical['outer_Gamma_norm_cap'][1])if i>=4 else Q(10**20)
    need(gamcap>=u,f'{label} Gamma cap does not cover whole continuous source')
    need(0<Q(physical['new_low_force_cap_expression'][0])<=Q(physical['new_low_force_cap_expression'][1])<Q('11.415'),'Fresh low force cap')
    rows.append({'label':label,'real_caps_exactly_recombined':True,'small_coefficient_conditions':True,
      'whole_core_norm_cap_upper':str(u),'outer_Gamma_cap_upper':str(gamcap),'moment_and_lift_upper':str(moment+lift),
      'CLOSED_or_DYNAMIC':'CLOSED'if i<4 else'DYNAMIC'})
plan=read(H/'K_MATRIX_PLAN.json');krows=[]
for i in range(12):
    for j in range(i,12):
        f=H/f'K_MATRIX_CELLS/{i:02d}-{j:02d}.json';a=read(f)
        coeff=[str(int(k==i)+(int(k==j)if j!=i else 0))for k in range(12)]
        need(a['coefficients']==coeff and a['plan']==plan,'Canonical K polarization')
        need(Q(a['certificate']['near_zero_bound'][0])>=0,'Nonnegative recorded Minkowski radius')
        krows.append({'pair':[i,j],'sha256':sha(f)})
need(len(krows)==78 and plan['near_zero_depth']==64,'All K polarization inputs')
direct=read(H/'DIRECT_D_TRANSPORT.json')
for key in ['lambda_zY','lambda_zJ']:
    lo,hi=map(Q,direct['details'][key]);need(0<lo<=hi,'Direct D Young factor')
out={'status':'GPT1_NEW_APPLICATION_BINDINGS_PASS','directions':rows,'canonical_K_records':krows,
     'physical_error_application_is_analytically_reviewed_separately':True,'new_integrations':0}
(P/'APPLICATION_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: 12 real/endpoint/moment/Gamma applications; 78 fixed K polarization records; positive direct-D Young parameters')
