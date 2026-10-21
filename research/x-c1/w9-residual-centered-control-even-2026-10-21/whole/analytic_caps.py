"""Whole-function analytic caps used only together with their written proof."""
import contextlib,io,json
from math import factorial
from pathlib import Path
from flint import arb,arb_poly,ctx
HERE=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile((HERE/'whole_model_integrate.py').read_text().split('cuts=[]')[0],str(HERE/'whole_model_integrate.py'),'exec'))
iv=json.loads((HERE/'endpoint-ingredients.json').read_bytes())['values']
get=lambda key:q(iv[key][1])
mc=arb_poly([(a/2)**k/factorial(k) if k%2==0 else arb(0) for k in range(161)])
mls=[arb(0)]*161;mdh=arb_poly([])
for n in range(0,161,2):
    mls[n]=(2*n+1)*c.pint(mc*leg[n]);mdh+=leg[n]*(mls[n]*harm[n])
qm0=mdh+mc*(-(2*arb.pi()*a).log()-arb.const_euler())-of.kernel(mc,mls,a,gamma,0)
absp=lambda pol,r:sum((abs(v).upper()*r**i for i,v in enumerate(pol)),arb(0))
qm_poly_complex=absp(qm0,q('6/5'));mcomplex=absp(mc,q('6/5'))
prime=2*sum((wt for _,wt in channels),arb(0))
assert qm_poly_complex<100 and mcomplex<3 and prime<7
# All radius-two rectangles of the core quadrature lie in |x/a|<1.2.
panels=list(zip(edges[:-2],edges[1:-1]));width=a-edges[-2]
panels +=[(a-width*arb(2)**(-k),a-width*arb(2)**(-k-1))for k in range(48)]
domains=[]
for lo,hi in panels:
    mid=(lo+hi)/2;half=(hi-lo)/2
    r=((mid+2*half)**2+(2*half)**2).sqrt()/a
    assert r<q('6/5')
    for sh,_ in channels:
        for sign in(-1,1):
            if abs(mid+sign*sh)<a:
                rp=((abs(mid+sign*sh).upper()+2*half)**2+(2*half)**2).sqrt()/a
                assert rp<q('6/5')
    domains.append(r)
# With Re(1 +/- x/a)>0, |log(1 +/- x/a)| is bounded by
# 10+|log(gap)| on these domains; this includes the imaginary part.
qm_contour=100+3*(10+1)+3*7
qm_real=100+3*(3+1)+3*7
assert qm_contour<1000000 and qm_real<1000
force=json.loads((HERE/'force-results/RESULT.json').read_bytes())['whole_force_transport']['values']
cross=q(force['cross_operator_upper'][1]);qmnorm=q(force['Q8_m_upper'][1])
lambdaop=((hs+b.sinh()-a.sinh())/4).sqrt()
graw=cross+lambdaop*qmnorm/mu
assert graw<100
# Restored integral estimates: no polynomial continuation is estimated
# outside its physical interval.  See ANALYTIC_CAPS.md for the inequalities.
assert get('Phi_ff_real_sup')<q('1e14')
assert get('finite_p_Euclidean_norm')<q('1e7')
assert get('shell_polynomial_real_sup')<q('1e5')
assert get('low_projection_real_sup')<1
assert get('physical_shell_coefficients_norm')<1
assert get('internal_w_norm')<2 and get('old_J_frozen_HS_norm')<10
assert get('shell_moment_lm')<1
assert get('core_measure_Cauchy_bound')<34 and get('core_measure_total_variation')<1
assert get('momentR')<1 and delta>1 and a>1 and b<q('11/10') and mu>1
assert get('ell_global_sup')<q('7e15') and get('quot_global_sup')<q('6e14')
assert get('gamma_global_sup')<18 and get('D_polynomial_cell_sup')<q('7e6')
assert get('Dv_sup')<q('4e6') and get('moment_multiplier')<1 and get('source_moment_coefficient')<1
assert harm[383]<7
assert 12/(2*res.h).sqrt()<100
assert 96/(2*hs).sqrt()*get('old_J_frozen_HS_norm')*get('internal_w_norm')<10000
# Q of the old Phi part: coefficients of 1+|log(a-y)|.
oldQ=(7+4+2*a*2+prime)*q('1e14')
assert oldQ<q('3e15')
# Four global degree <=8 polynomials and the shell part of Jw-Fp.
assert sum((abs(pv[i,0]).upper() for i in range(4)),arb(0))*8<q('2e8')
zcore=q('1e11');shellcore=q('1e10')
rawcore=oldQ+zcore+shellcore
assert rawcore<q('4e15')
# |int rawcore| < 3*rawcore, scale/me=1/a<1, |mc|<3.
ustatic=q('1e14')+rawcore+3*(3*rawcore+1)+1
assert ustatic<q('1e18')
# h on [0,b): reflected ell integral is <=1; only ell(x) uses
# continuation to the core.  All prime ell evaluations are physical.
hbound=q('7e15')*2+q('6e14')+18+1020+q('7e6')+q('4e6')*2+100
assert hbound<q('1e17')
assert 1+abs(hs.log()).upper()<4
u_H=(q('1e18')*4+q('4e17')*(2*a).sqrt())
assert u_H<q('1e20')
# On each outer endpoint tail t=-log(v)>100. The fixed prime images
# are either at a core endpoint with distance v or >=1e-6 away.
for endpoint in (a,b):
    for sh,_ in channels:
        for sign in (-1,1):
            dist=abs(a-abs(endpoint+sign*sh)).upper()
            assert dist<q('1e-100') or dist>q('1e-6')
# Cauchy integral <=1e18*(3+2t+t²/2); reflected/regular <=14e18;
# prime <=7*(1e18*(1+t)+4e17); base h<=1e17*(1+t).
# Remaining shell/global/moment terms <=1e12*(1+t).
const=q('1e18')*17+7*(q('1e18')+q('4e17'))+q('1e17')+q('1e12')
linear=2*q('1e18')+7*q('1e18')+q('1e17')+q('1e12')
quadratic=q('5e17')
endpoint_cap=const+linear/2+quadratic
assert endpoint_cap<q('1e20')
tail=(a/2).exp()*(a/2)**160/arb.fac_ui(160)
assert q('1e6')*tail<q('1e-200')
assert c.norm(ff)<q('1e20') and c.norm(pv)<q('1e20') and c.norm(w)<q('1e20')
out={'status':'ANALYTIC_CAP_INGREDIENTS_DIRECTED_PASS',
     'caps':{'qm_contour':1000000,'qm_real_endpoint':1000,'raw_g_X_operator':100,
             'modeled_u_H8_norm':'1e20','outer_endpoint_envelope':'1e20*(1+log(v)^2)'},
     'values':c.encode(dict(qm_poly_complex=qm_poly_complex,m_complex=mcomplex,
         raw_g_X_operator=graw,old_Q_Phi_envelope=oldQ,combined_raw_core_envelope=rawcore,
         static_u_envelope=ustatic,h_envelope=hbound,u_H8_bound=u_H,
         outer_endpoint_coefficient=endpoint_cap,moment_Taylor_tail=tail)),
     'requires_written_integral_lemma':True,'full_comparison_pass':False}
(HERE/'analytic-caps.json').write_bytes((json.dumps(out,indent=2)+'\n').encode())
print(json.dumps({k:float(c.box(v).mid())for k,v in out['values'].items()},indent=2),flush=True)
