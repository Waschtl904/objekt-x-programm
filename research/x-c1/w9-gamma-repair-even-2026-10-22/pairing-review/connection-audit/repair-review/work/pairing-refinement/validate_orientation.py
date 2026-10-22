"""Independent polynomial-kernel checks, scalar model checks, whole-error price."""
from pathlib import Path
import json,time
TASK=Path(__file__).resolve().parent
source=TASK/'kernel_orientation.py'
exec(compile(source.read_text(encoding='utf-8').split('outmom=[]')[0],str(source),'exec'),globals())
import model_cache,hashlib
# A second route evaluates the defining polynomial kernel inside its integral.
sp=shellpoly(gcoeff)
sp_local=sp(arb_poly([mid,half]));gamma_poly=arb_poly(gamma)
moments=[c.pint(sp*arb_poly([0]*k+[1]),a,b)for k in range(225)]
wrong=regular_out(moments);checks=[]
for xx in [arb(0),a/4,a/2,3*a/4,a]:
 yy=arb_poly([mid,half])
 integrand=sp_local*(gamma_poly((yy-xx)*(arb(1)/2))+gamma_poly((yy+xx)*(arb(1)/2)))
 direct=half*c.pint(integrand,arb(-1),arb(1))
 defect=dG(xx/a)-(wrong(xx)-direct)
 assert abs(defect).upper()<q('1e-100')
 checks.append({'x':enc(xx),'defining_integral_identity_defect':enc(defect),'wrong_minus_right':enc(wrong(xx)-direct)})
print('DEFINING_KERNEL_CHECKS',len(checks),flush=True)
# Check the derived whole-function correction against changing only the frozen
# model's polynomial coefficients, with a freshly installed scalar evaluator.
edges=exact_edges
points=[lo+(hi-lo)*q(f'{k}/4')for lo,hi in zip(edges[:-1],edges[1:])for k in [1,2,3]]
points += [a+(edges[1]-a)*arb(2)**(-36),b-(b-edges[2])*arb(2)**(-36)]
oldvalues=[ns['outer_value'](xx)for xx in points]
def closed_change(xx):
 zz=(xx-a)/hs;v=plain(zz)
 for rt,pp in logs:v+=pp(zz)*abs(zz-rt).log()
 for sh,wt in ns['channels']:
  for sign in [-1,1]:
   y=xx+sign*sh
   if abs(y)<a:v-=wt*du(abs(y)/a)
 return v
predicted=[closed_change(xx)for xx in points]
ns['ustatic']=dict(ns['ustatic']);ns['outerstatic']=dict(ns['outerstatic'])
ns['ustatic'][None]+=du;ns['outerstatic'][None]+=du
ns['outerreg']+=regular_out(moment);ns['momentR']+=dR
g['fast_evaluation'].install(ns)
scalar=[]
for xx,oldv,pred in zip(points,oldvalues,predicted):
 newv=ns['outer_value'](xx);defect=newv-oldv-pred
 print('SCALAR_DEFECT',len(scalar),float(defect.mid()),float(defect.rad()),float(pred.mid()),flush=True)
 scalar.append({'x':enc(xx),'old_value':enc(oldv),'corrected_value':enc(newv),'closed_correction':enc(pred),'identity_defect':enc(defect)})
print('SCALAR_CHECKS',len(scalar),flush=True)
# du is not assumed to belong to the high subspace. Re-evaluate the published
# whole-X raw g estimate (13.066), including moment lift, then round up to 14.
du2=(2*a*c.pint(du*du)).upper();assert du2>=0
du_norm=du2.sqrt();dRpsi=a*c.pint(dPsi*mc)
mshell=(hs+b.sinh()-a.sinh()).sqrt()
manifest=json.loads((g['ORIGINAL']/'MANIFEST.json').read_bytes())
force_raw=(g['WHOLE']/'force-results/RESULT.json').read_bytes()
assert hashlib.sha256(force_raw).hexdigest()==manifest['whole/force-results/RESULT.json']
force=json.loads(force_raw)['whole_force_transport']['values']
raw_g=q(force['cross_operator_upper'][1])+((hs+b.sinh()-a.sinh())/4).sqrt()*q(force['Q8_m_upper'][1])/mu
assert raw_g<14
reg=ns['e'].bounds['old_FJ_regular_kernel_uniform_error']
g_price=(14+100*reg)*du_norm;moment_price=abs(dRpsi).upper()*mshell/mu
round_price=q('1e-150')
change_X=(g_price+moment_price+round_price).upper()
wr=json.loads((g['WHOLE']/'WHOLE_RESULT.json').read_bytes())
oldnorm=q(wr['actual_whole_residual_Ldual_norm_upper'])
newnorm=(oldnorm+q('5/21').sqrt()*change_X).upper();newenergy=newnorm**2
out={'status':'LOCAL_MODEL_DEFECT_CONFIRMED_REPAIR_PRICE_CONDITIONAL_ON_INHERITED_WHOLE_G_CAP',
 'kernel_checks':checks,'scalar_checks':scalar,
 'scalar_control_tolerance':'1e-25',
 'scalar_checks_pass':all(box(r['identity_defect']).contains(0)and abs(box(r['identity_defect'])).upper()<q('1e-25')for r in scalar),
 'bounds':{k:enc(v)for k,v in {'du_X_norm_squared':du2,'du_X_norm':du_norm,'whole_raw_g_bound_recomputed':raw_g,'whole_raw_g_cap_used':arb(14),'Gamma_operator_allowance':100*reg,'g_du_X_error':g_price,'direct_moment_X_error':moment_price,'moment_truncation_X_allowance':round_price,'kernel_orientation_X_error':change_X,'old_residual_Ldual_norm_upper':oldnorm,'repaired_residual_Ldual_norm_upper':newnorm,'repaired_residual_Ldual_energy_upper':newenergy}.items()},
 'below_existing_energy_cap':bool(newenergy.upper()<q('1e-9')),
 'no_p_error_recharged':True,'source_model_was_not_modified':True,'seconds':time.monotonic()-g['start']}
(TASK/'orientation-validation.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
cache=TASK/('orientation-correction-'+hashlib.sha256(source.read_bytes()).hexdigest()[:12]+'.json.gz')
if not cache.exists():model_cache.save(cache,{'du':du,'dG':dG,'dPsi':dPsi,'dR':dR,'dRpsi':dRpsi,'outerreg_change':regular_out(moment),'plain':plain,'log_terms':logs},hashlib.sha256(source.read_bytes()).hexdigest(),g['bindings'])
for k,v in out['bounds'].items():print(k,float(box(v).upper()),flush=True)
print('BELOW_EXISTING_CAP',out['below_existing_energy_cap'],'SECONDS',out['seconds'],flush=True)
