"""Norm discrepancy audit using only the already bound repository inputs.

The displayed mesh norm is reconstructed at 90 digits. Its disagreement with
the complete model Gram is compared with the fixed-k high-source error budget.
Selected stored source values are independently recalculated by stufe2/qnp_psi.py.
No mesh difference is promoted to a directed integration remainder.
"""
import json,sys,importlib.util
from pathlib import Path
from fractions import Fraction
import mpmath as mp
HERE=Path(__file__).resolve().parent
PACKAGE=HERE.parent
mp.mp.dps=90

def rat(s):
    q=Fraction(s);return mp.mpf(q.numerator)/q.denominator

def mid(v):return (rat(v[0])+rat(v[1]))/2

def run(par):
    sigma=0 if par=='even' else 1
    a=3*mp.log(2)/2
    m=lambda x:mp.cosh(x/2) if sigma==0 else mp.sinh(x/2)
    mu=(mp.sinh(a)+(-1)**sigma*a)/2
    me=mp.quad(lambda t:m(a*t)*mp.sqrt(2*sigma+1)*mp.legendre(sigma,t),[-1,1])/2
    gamma=mu/(a*me*me)
    nodes=json.loads((HERE/f'MESHH_{par}_upper_v.json').read_text())['nodes']
    x=[mp.mpf(n['x']) for n in nodes];w=[mp.mpf(n['w']) for n in nodes];raw=[mp.mpf(n['Q_raw']) for n in nodes]
    moment=mp.fsum(wi*m(xi)*v for xi,wi,v in zip(x,w,raw))
    f=[v-m(xi)*moment/mu for xi,v in zip(x,raw)]
    af=mp.sqrt(mp.mpf(2*(2*sigma+1))/a)*mp.fsum(wi*mp.legendre(sigma,xi/a)*v for xi,wi,v in zip(x,w,f))
    f2=2*mp.fsum(wi*v*v for wi,v in zip(w,f))
    low=json.loads((PACKAGE/'original/gpt2-stufe3-endliche-u8-antwort/expected/FINITE_ACTION.json').read_text())[par]['directions']['upper_v']
    high=json.loads((PACKAGE/'original/gpt2-stufe4-hochantwort/expected/COMPLETE_HIGH_RESPONSE.json').read_text())[par]['directions']['upper_v']
    phi2=mp.fsum(mid(v)**2 for v in low['Phi_star_f_model'])
    y2=f2+gamma*af*af-phi2;assert y2>0
    model2=mid(high['full_model_y_norm_squared'])
    ef=rat(high['y_fixed_k_error_upper'][1])
    n=lambda x:mp.nstr(x,60)
    out={'status':'NUMERICAL_MESH_DIAGNOSTIC_WITH_BOUND_GRAM_REFERENCE','parity':par,
         'norm_f_squared_mesh':n(f2),'gamma_m_a_f_squared_mesh':n(gamma*af*af),'Phi_star_f_model_squared_midpoint':n(phi2),
         'norm_y_squared_mesh':n(y2),'norm_y_mesh':n(mp.sqrt(y2)),
         'full_model_y_norm_squared_interval':high['full_model_y_norm_squared'],'model_y_norm_midpoint':n(mp.sqrt(model2)),
         'mesh_minus_model_y_squared':n(y2-model2),'mesh_minus_model_y_norm':n(mp.sqrt(y2)-mp.sqrt(model2)),
         'fixed_k_high_source_error_upper':high['y_fixed_k_error_upper'],
         'fixed_k_squared_norm_change_bound_display':n(2*mp.sqrt(model2)*ef+ef*ef),
         'cause_scope':'The displayed mesh norm is not an upper bound; cancellation in a coarse norm integral. Fixed-k source-model error is much too small to explain the discrepancy. Stored source evaluation and norm quadrature remain numerical, not directed.'}
    # Point checks use the existing public, slower Gamma integrator, not an external source implementation.
    spec=importlib.util.spec_from_file_location('qnp_public',PACKAGE/'stufe2/qnp_psi.py');qnp=importlib.util.module_from_spec(spec);spec.loader.exec_module(qnp)
    qnp.PSI_PATH=PACKAGE/'stufe1/PSI_DEFINITION.json'
    g=qnp.setup(55);psi=qnp.Psi(g,par,'upper_v')
    checks=[]
    for target in ('0.3','0.8'):
        k=min(range(len(x)),key=lambda i:abs(x[i]-mp.mpf(target)))
        value=qnp.q_raw(psi,x[k],g)
        checks.append({'x':n(x[k]),'stored_Q_raw':n(raw[k]),'recomputed_Q_raw':n(value),'absolute_difference':n(abs(value-raw[k]))})
        print(par,target,mp.nstr(abs(value-raw[k]),8),flush=True)
    out['public_integrator_point_checks']=checks
    (HERE/'recomputed_mu8'/f'YF_NORM_DIAGNOSTIC_{par}.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':
    for par in sys.argv[1:] or ('even','odd'):run(par)
