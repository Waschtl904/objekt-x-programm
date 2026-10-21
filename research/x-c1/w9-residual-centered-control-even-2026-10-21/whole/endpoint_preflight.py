"""Quantitative endpoint-envelope ingredients, not a completed tail proof."""
import contextlib,io,json,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
code=(HERE/'whole_model_integrate.py').read_text()
with contextlib.redirect_stdout(io.StringIO()):exec(compile(code.split('cuts=[]')[0],str(HERE/'whole_model_integrate.py'),'exec'))
import fast_evaluation
_fast=fast_evaluation.install(globals());model=_scalar_model
def sup(p,lo,hi):
    d=max(0,len(p)-1)
    s=p(arb_poly([(lo+hi)/2,(hi-lo)/2]))
    v=c.pint(s*s,arb(-1),arb(1))/2
    assert v.upper()>=0
    return (d+1)*v.upper().sqrt()
vals={}
for k in ('ell','quot','gamma'):
    vals[k+'_global_sup']=sup(model[k],arb(0),res.b)
vals['Dv_sup']=sup(model['dv'],arb(0),arb(1))
vals['moment_multiplier']=abs(model['dm']).upper()
vals['source_moment_coefficient']=abs(model['ac']).upper()
vals['physical_shell_coefficients_norm']=sum((v*v for v in cc),arb(0)).sqrt()
vals['internal_w_norm']=c.norm(w)
vals['old_J_frozen_HS_norm']=c.norm(J)
vals['shell_moment_lm']=abs(lm).upper()
vals['old_half_width']=hs
vals['new_half_width']=res.h
cuts=[arb(0),res.a,res.b]
for n,p in res.channels:
    sh=res.logs[n]
    for e0 in(-res.a,-res.b,res.a,res.b):
        for v in(e0-sh,e0+sh):
            if 0<v<res.a:cuts.append(v)
cuts.sort(key=float);unique=[cuts[0]]
for v in cuts[1:]:
    if not v.overlaps(unique[-1]):unique.append(v)
dp=arb(0)
for lo,hi in zip(unique[:-1],unique[1:]):
    if hi>res.a:continue
    fun=res.cell(lo,hi);record=model['records'][fun]
    dp=max(dp,sup(record['dp'],lo/res.a,hi/res.a))
vals['D_polynomial_cell_sup']=dp
phin=arb(0)
for i,n in enumerate(range(2,384,2)):
    beta=arb(2*n+1).sqrt()*c.mellin(n,a)/c.mellin(0,a)
    phin+=abs(ff[i,0]).upper()*((arb(2*n+1)/(2*a)).sqrt()+abs(beta).upper()/(2*a).sqrt())
vals['Phi_ff_real_sup']=phin
vals['finite_p_Euclidean_norm']=c.norm(pv)
vals['shell_polynomial_real_sup']=sup(sp,arb(-1),arb(1))
vals['low_projection_real_sup']=c.norm(low)*384/(2*a).sqrt()
vals['core_measure_Cauchy_bound']=sum((abs(v).upper()/(a-y)for y,v in hpoints),arb(0))
vals['core_measure_total_variation']=sum((abs(v).upper()for y,v in hpoints),arb(0))
vals['momentR']=abs(momentR).upper()
out={'status':'ENDPOINT_INGREDIENTS_ONLY','values':c.encode(vals),'endpoint_envelope_proved':False}
(HERE/'endpoint-ingredients.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:float(v.mid())for k,v in vals.items()},indent=2),flush=True)
