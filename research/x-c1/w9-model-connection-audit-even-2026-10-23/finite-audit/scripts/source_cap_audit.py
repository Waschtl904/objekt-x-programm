"""Recompute real source envelopes and bound the continuous corrected core."""
import sys
if not __debug__:raise SystemExit('Optimized Python is rejected')
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,time
from math import factorial
from flint import arb,arb_poly,arb_mat,ctx
ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
R=args.repo.resolve();O=args.out.resolve();O.mkdir(parents=True,exist_ok=True);start=time.monotonic()
def mod(n,p):
 s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
S=R/'research/x-c1/w9-new-k-schur-underform-even-2026-10-20';eng=mod('source_cap_schur',S/'engine.py');ctx.prec=1024
spec,data=eng.snapshot(R,(S/'INPUT_BINDINGS.json').read_bytes());env=eng.load(R,spec,data);c=env['common'];q=c.q
ctx.prec=3072
W=R/'research/x-c1/w9-residual-centered-control-even-2026-10-21/whole';cache=mod('source_cap_cache',W/'model_cache.py')
v,ib=cache.load(W/'whole-model-ed58da3caacd.json.gz',hashlib.sha256((W/'whole_function_probe.py').read_bytes()).hexdigest());assert ib=={n:hashlib.sha256(d).hexdigest()for n,d in env['inp'].data.items()}
resmod=mod('source_cap_res',R/'research/x-c1/w9-partial-energy-2026-10-18/residuals.py');res=resmod.Residuals(env['inp'],'even')
cc=v['cc'];a,b,hs,mu,delta=(v[k]for k in('a','b','hs','mu','delta'))
def sup(p,lo,hi):
 d=max(0,len(p)-1);s=p(arb_poly([(lo+hi)/2,(hi-lo)/2]));normsq=c.pint(s*s,arb(-1),arb(1))/2
 assert normsq.upper()>=0
 return (d+1)*normsq.upper().sqrt()
vals={}
for field in ('ell','quot','gamma','Dv'):
 pol=sum((getattr(res,field)[j].p*cc[j]for j in range(12)),arb_poly([]))
 vals[field+'_sup']=sup(pol,arb(0),arb(1) if field=='Dv' else b)
for field in('Dm','Ac'):vals[field+'_abs']=abs(sum((getattr(res,field)[j]*cc[j]for j in range(12)),arb(0))).upper()
tc=[sum((res.T[i,j]*cc[j]for j in range(12)),arb(0))for i in range(12)]
dp0=sum((res.Dpoly[j]*cc[j]for j in range(12)),arb_poly([]))
cuts=[arb(0),res.a,res.b]
for n,_ in res.channels:
 for e in(-res.a,-res.b,res.a,res.b):
  for x in(e-res.logs[n],e+res.logs[n]):
   if 0<x<res.a:cuts.append(x)
cuts.sort(key=float);unique=[cuts[0]]
for x in cuts[1:]:
 if not x.overlaps(unique[-1]):unique.append(x)
dpbound=arb(0)
for lo,hi in zip(unique[:-1],unique[1:]):
 if hi>res.a:continue
 at=(lo+hi)/(2*res.a);dp=arb_poly(dp0)
 for i,f in enumerate(res.funcs):
  for term in f['D']['shift_terms']:
   sh=res.logs[int(term['channel'])]/res.a
   dl,dh=(arb(0),1-sh)if int(term['translation_sign'])==1 else(max(arb(0),sh-1),arb(1))
   if dl<at<dh:dp+=arb_poly(list(map(q,term['polynomial'])))*tc[i]
 dpbound=max(dpbound,sup(dp,lo/res.a,hi/res.a))
vals['D_polynomial_cell_sup']=dpbound
phin=arb(0)
for i,n in enumerate(range(2,384,2)):
 beta=arb(2*n+1).sqrt()*c.mellin(n,a)/c.mellin(0,a)
 phin+=abs(v['ff'][i,0]).upper()*((arb(2*n+1)/(2*a)).sqrt()+abs(beta).upper()/(2*a).sqrt())
vals['Phi_sup']=phin;vals['p_norm']=c.norm(v['pv']);vals['shell_sup']=sup(v['sp'],arb(-1),arb(1));vals['low_sup']=c.norm(v['low'])*384/(2*a).sqrt()
vals['coefficient_norm']=sum((z*z for z in cc),arb(0)).sqrt()
assert vals['ell_sup']<q('7e15') and vals['quot_sup']<q('6e14') and vals['gamma_sup']<18
assert vals['Dv_sup']<q('4e6') and dpbound<q('7e6') and vals['Dm_abs']<1 and vals['Ac_abs']<1
assert phin<q('1e14') and vals['p_norm']<q('1e7') and vals['shell_sup']<q('1e5') and vals['low_sup']<1 and vals['coefficient_norm']<1
prime=2*sum((wt for _,wt in v['channels']),arb(0));assert prime<7
H383=sum((arb(1)/n for n in range(1,384)),arb(0));assert H383<7
phi_Q=(7+4+4*a+prime)*q('1e14');assert phi_Q<q('3e15')
# The deliberately coarse physical-interval estimates are proved in SOURCE-CAPS.txt.
raw_envelope=phi_Q+q('1e11')+q('1e10');assert raw_envelope<q('4e15')
lognorm=(2*(4+a*(1+a.log()**2))).sqrt();assert lognorm<4
Mnorm=((2*mu)*(2*a)).sqrt()/(4*(a/2).sinh());assert Mnorm<q('1.01')
mc=arb_poly([(a/2)**k/factorial(k)if k%2==0 else arb(0)for k in range(161)])
intmc=a*c.pint(mc,arb(0),arb(1));normmc2=2*a*c.pint(mc*mc,arb(0),arb(1))
Mmodel=(normmc2*(2*a)).sqrt()/(2*intmc);assert Mmodel<q('1.01') and intmc>a
Mcommon=max(Mnorm.upper(),Mmodel.upper())
of=mod('source_cap_oldfields',R/'research/x-c1/w9-partial-energy-2026-10-18/old_fields.py')
absp=lambda p,r:sum((abs(z).upper()*r**k for k,z in enumerate(p)),arb(0))
gamma=v['gamma'];gpoly=arb_poly(gamma)
gamma_old=arb_poly(list(map(q,env['inp'].json('a8_model')['Gamma_polynomial_coefficients'])))
vals['Gamma224_abs_1_1']=absp(gpoly,q('1.1'));vals['Gamma160_abs_1_05']=absp(gamma_old,q('1.05'))
vals['Gamma224_derivative_abs_1_1']=absp(gpoly.derivative(),q('1.1'))
assert vals['Gamma224_abs_1_1']<2 and vals['Gamma160_abs_1_05']<2 and vals['Gamma224_derivative_abs_1_1']<q('1e6')
mls=[arb(0)]*161;mdh=arb_poly([])
for n in range(0,161,2):
 mls[n]=(2*n+1)*c.pint(mc*res.legs[n]);mdh+=res.legs[n]*(mls[n]*v['harm'][n])
qm0=mdh+mc*(-(2*arb.pi()*a).log()-arb.const_euler())-of.kernel(mc,mls,a,gamma,0)
vals['qm_polynomial_abs_1_2']=absp(qm0,q('1.2'));vals['m160_abs_1_2']=absp(mc,q('1.2'))
assert vals['qm_polynomial_abs_1_2']<100 and vals['m160_abs_1_2']<3
n128,_=cache.load(W/'whole-model-36d3f3fcb6cb-n128.json.gz',hashlib.sha256((W/'whole_function_probe_v2.py').read_bytes()).hexdigest())
vals['n128_atom_total_variation']=sum((abs(wh).upper()for x,wh in n128['hpoints']),arb(0));assert vals['n128_atom_total_variation']<1
assert (2*hs).sqrt()<1 and (2*mu).sqrt()<2 and a>1 and mu>1 and delta>1
g_local=-v['slocal']+q('1e-10')*(v['J']*v['w'])
g_shell=sum((res.legs[k]*(g_local[k,0]*(arb(2*k+1)/(2*hs)).sqrt())for k in range(96)),arb_poly([]))
vals['corrected_inner_shell_sup']=sup(g_shell,arb(-1),arb(1));assert vals['corrected_inner_shell_sup']<q('1e5')
assert c.norm(v['J'])*c.norm(v['w'])<20
assert abs(v['lm']).upper()+q('1e-10')*((hs+b.sinh()-a.sinh())/4).sqrt()*20<2
assert 1+abs(hs.log()).upper()<4
h_env=2*q('7e15')+q('6e14')+18+1020+q('7e6')+2*q('4e6')+100
assert h_env<q('1e17')
g_norm=q('4e15')*lognorm;h_norm=q('4e17')*(2*a).sqrt()
u_norm=q('1e14')*(2*a).sqrt()+(Mcommon*(g_norm+h_norm)+(2*a).sqrt())/delta
# Continuous source mean, not the total variation of a discrete Gauss measure.
alpha=(3*q('4e15')+4*a*q('1e17'))/a
assert u_norm<q('1e18')<q('1e20') and alpha<q('1e18')
E=arb(2*10**6)/arb(factorial(160))
amp=100*(2*100+4*2*100+2*q('1e18'))+2*2*100+2*q('1e20')*100+4*q('1e15')
moment=amp*E
assert amp<q('2.021e22') and moment<q('8.570e-257')
vals.update(raw_source_envelope=raw_envelope,h_envelope=h_env,log_weight_L2=lognorm,oblique_projection_norm=Mnorm,model_oblique_projection_norm=Mmodel,continuous_g_norm=g_norm,continuous_h_model_norm=h_norm,continuous_corrected_u_norm=u_norm,continuous_alpha_cap=alpha,explicit_moment_chain_factor=amp,explicit_moment_chain_X=moment)
enc=lambda z:[str(z.lower().fmpq()),str(z.upper().fmpq())]
out={'status':'CONTINUOUS_CORRECTED_CORE_CAP_DERIVED_CONDITIONAL_ON_BOUND_SOURCE_FORMULAS','values':{k:enc(z)for k,z in vals.items()},'uses_Gauss_measure_as_L2_function':False,'uses_cached_h_total_variation_to_bound_continuous_h':False,'historical_full_h_error_reproved':False,'all_moment_stages_catalogue_complete':False,'seconds':time.monotonic()-start}
(O/'source-caps.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:vals[k].str(15)for k in ['continuous_corrected_u_norm','continuous_alpha_cap','explicit_moment_chain_factor','explicit_moment_chain_X']},indent=2),flush=True)
