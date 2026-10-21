"""Candidate complete model-error ledger; needs the analytic bound audit."""
import contextlib,hashlib,io,json
from pathlib import Path
from flint import arb,arb_mat,ctx
import model_cache
HERE=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile((HERE/'probe.py').read_text().split('# Midpoint-only trade-off')[0],str(HERE/'probe.py'),'exec'))
ctx.prec=3072
values,bindings=model_cache.load(HERE/'whole-model-ed58da3caacd.json.gz',hashlib.sha256((HERE/'whole_function_probe.py').read_bytes()).hexdigest())
pv,ff,low,w=(values[k]for k in ('pv','ff','low','w'))
root=lambda x:x.upper().sqrt()
cc0=arb_mat([[v]for v in values['cc']])
coefficient_interval=c.norm(env['c']-cc0)
normalization_error=coefficient_interval*(c.trace(mat(e.data['H9_Gram'])).sqrt()+e.eResidual)
physical_error=e.eResidual+normalization_error
C=e.w['C'];delta=e.w['delta'];rho=e.w['rho'];gamma=e.w['gamma'];Ki=e.w['Ki']
hn=root(quad(e.H,env['c']));eh=abs((e.eh*env['c'])[0,0]).upper();en=c.norm(e.ell*env['c'])
eBy=e.eRawA*(hn+gamma*eh)+e.eLowA*en
eWh=c.norm(C)*eBy/(delta*(1-rho).sqrt())
eta0=C.solve(ff)*(1-rho).sqrt()
eta_model=e.wj*w-e.wh*env['c']-e.wf*pv
eta_round=c.norm(eta_model-eta0)
eta_source=root(EJ)*c.norm(w)+root(quad(EF,pv))+eWh
eta_physical=e.bounds['U8_norm_upper'].sqrt()*physical_error
etaerr=eta_round+eta_source+eta_physical
dpmodel=Ki*(e.w['a']*w-e.v*env['c'])-pv
K=Ki.inv();p_round=root(quad(K,dpmodel))
prior=json.loads(data['pilot_result'])
p_feature=c.box(prior['feature_error_norms']['K_inverse_v'])
p_physical=e.bounds['v_feature_operator_norm_upper']*physical_error
perror=ea_direction+p_feature+p_physical+p_round
wn,pn,fn=c.norm(w),c.norm(pv),c.norm(ff)
rawerror=gamma.sqrt()*(e.eRawJ*wn+e.eRawF*pn+e.eRawA*fn+physical_error)
lowerror=e.eLJ*wn+root(quad(e.ELF,pv))+e.eLowA*fn+gamma.sqrt()*physical_error
old=env['inp'].json('a8_model')
Am=arb_mat([[q(v[0]).union(q(v[1]))/10**100 for v in row]for row in old['parities']['even']['A']])
raw=env['inp'].json('old_sources')['cases'][0]
cs=mat(raw['galerkin']['old_low_c_model'])*w-e.ell*env['c']-mat(raw['old_certificate']['source_c_model'])*pv
low_round=c.norm(cs-Am*ff-low)
rawerror+=lowerror+low_round+q('1e-150')
# The two constants below must be proved as whole operators/functions; the
# incomplete finite coordinate norm may not stand in for either one.
forcecap=q('10');g_X_cap=q('100');u_model_norm_cap=q('1e20')
reg=e.bounds['old_FJ_regular_kernel_uniform_error']
g_error=100*reg*u_model_norm_cap
q_error=100*reg*(wn+16*pn)+100000*(e.eBareJ*wn+e.eBareF*pn)
X_raw_error=g_X_cap*rawerror/delta+g_error+q_error+2*physical_error
L_error=forcecap*(perror+etaerr)+q('5/21').sqrt()*X_raw_error
out={'status':'PROPOSED_WHOLE_MODEL_ERROR_LEDGER_PENDING_ANALYTIC_AUDIT',
     'values':c.encode(dict(witness_normalization_Hilbert_error=normalization_error,
        low_feature_interval_placement=eta_round,low_feature_sources=eta_source,
        low_feature_physical=eta_physical,low_feature_total=etaerr,
        p_model_interval_placement=p_round,p_feature=p_feature,p_physical=p_physical,p_total=perror,
        raw_source_and_low_leakage=rawerror,low_model_interval_placement=low_round,
        g_kernel_model_error=g_error,q_image_model_error=q_error,
        raw_X_error=X_raw_error,proposed_Ldual_error=L_error)),
     'unproved_caps':['whole g raw X norm <=100','modeled u H8 norm <=1e20'],
     'core_quadrature_paid':False,'full_comparison_pass':False}
(HERE/'whole-error-ledger.json').write_bytes((json.dumps(out,indent=2)+'\n').encode())
print(json.dumps({k:float(c.box(v).mid())for k,v in out['values'].items()},indent=2),flush=True)
