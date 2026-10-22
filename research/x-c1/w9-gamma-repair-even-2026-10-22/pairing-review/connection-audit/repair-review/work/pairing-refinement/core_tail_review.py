"""Signed contribution of the omitted smooth core h tail; already paid in #252."""
from pathlib import Path
import json,time
TASK=Path(__file__).resolve().parent;src=TASK/'kernel_orientation.py'
code=src.read_text(encoding='utf-8')
exec(compile(code.split('# Reconstruct the correction')[0],str(src),'exec'),globals())
import taylor_model as tm
from flint import acb,arb_series,ctx
d=(a-ns['edges'][-2])*arb(2)**(-48);center=a-d/2;radius=d/2
tm.Jet.N=8;ctx.cap=8;R=q('0.001')/radius
xx=tm.Jet(arb_series([center,radius],prec=8),acb(arb(center,q('0.001')),arb(0,q('0.001'))))
# Independent audit amendment: polynomial bounds must use the same Cauchy
# radius as the tail estimate. Original peval is hard-coded to radius 2.
original_hh=tm.hjet(ns,xx)
original_remainder=abs(original_hh.b).upper()*R**(-8)/(1-1/R)
def peval_radius(p,x):
 x=tm.jet(x);assert x.s.length()<=2
 co=p(arb_poly([x.s[0],x.s[1]]))
 bound=arb_poly([abs(v).upper() for v in co])(R).upper()
 return tm.Jet(arb_series(list(co)[:tm.Jet.N],prec=tm.Jet.N),acb(arb(0,bound),arb(0,bound)))
tm.peval=peval_radius
hh=tm.hjet(ns,xx);h0=hh.s[0]
contour_review={'normalized_radius':enc(R),'original_contour_bound':enc(abs(original_hh.b).upper()),'corrected_contour_bound':enc(abs(hh.b).upper()),'original_cauchy_remainder':enc(original_remainder),'corrected_cauchy_remainder':enc(abs(hh.b).upper()*R**(-8)/(1-1/R))}
(TASK/'contour-review.json').write_text(json.dumps(contour_review,indent=2)+'\n')
print('CONTOUR_REVIEW', {k:float(box(v).upper()) for k,v in contour_review.items()},flush=True)
variation=sum((abs(hh.s[k]).upper()for k in range(1,8)),arb(0))+abs(hh.b).upper()*R**(-8)/(1-1/R)
assert variation<q('1e-10')
print('CORE_TAIL_SETUP','h',float(h0.mid()),'width',float(d),'variation',float(variation.upper()),flush=True)
aff=arb_poly([1,-d/a]);mnear=mc(aff);Hmass=h0*d
Hm=h0*d*c.pint(mnear)
qp=arb_poly([]);at=a-d/2
for sh,wt in ns['channels']:
 for sign in [-1,1]:
  if abs(at+sign*sh)<a:qp-=mc(arb_poly([sign*sh/a,1]))*wt
# Near t=1: log(1-t)=log(d/a)+log(z), log(1+t)=log(2)+log(1-d*z/(2*a)).
eps=d/(2*a);logsmall=arb_poly([0]+[-eps**k/k for k in range(1,9)])
near_plain=(qm0+qp)(aff)+qmLog(aff)*((d/a).log()+arb(2).log()+logsmall)
HQm=h0*d*(c.pint(near_plain)+logint01(qmLog(aff),arb(0)))
logsmall_error=eps**9/(9*(1-eps))
HQm_error=abs(h0).upper()*d*sum((abs(v).upper()for v in qmLog(aff)),arb(0))*logsmall_error
du=mc*(Hmass/(a*c.mellin(0,a)*delta))
dR=Hm-HQm/delta+a*(c.pint(du*qm0)+logint01(du*qmLog,arb(1))+logint01(du*qmLog,arb(-1)))
for lo,hi in zip(ns['edges'][:-1],ns['edges'][1:]):
 at=(lo+hi)/2;pp=arb_poly([])
 for sh,wt in ns['channels']:
  for sign in [-1,1]:
   if abs(at+sign*sh)<a:pp-=mc(arb_poly([sign*sh/a,1]))*wt
 dR+=a*c.pint(du*pp,lo/a,hi/a)
Hmom=[h0*(a**(k+1)-(a-d)**(k+1))/(k+1)for k in range(225)]
body=code[code.index('# Reconstruct the correction'):code.index('data=json.loads')]
needle='plain-=regular_out(moment)(x)+mc(s)*(dR/mu)'
assert body.count(needle)==1
body=body.replace(needle,needle+'''
plain+=regular_out(Hmom)(x)*(1/delta)
logs.extend([(-d/hs,arb_poly([h0/(2*delta)])),(arb(0),arb_poly([-h0/(2*delta)])),(-2*a/hs,arb_poly([h0/(2*delta)])),(-(2*a-d)/hs,arb_poly([-h0/(2*delta)]))])
''')
exec(compile(body,'signed_core_tail_pairings','exec'),globals())
# Residual from replacing h on this tiny cell by h(center), plus certified
# retained-cell quadrature errors and the existing 64-to-128 model bridge.
core=json.loads((g['WHOLE']/'core-quadrature-control-128.json').read_bytes())
E=arb(0);Ec=arb(0);Eq=arb(0)
for row in core['cells']:
 err=q(row['integral_error'][1]);gap=q(row['gap'][0]);E+=err;Ec+=err*(2/gap).sqrt();Eq+=err*1000000*(1+abs(gap.log()).upper())
selected=((Ec+4*E*(2*hs).sqrt()+14*(2*mu).sqrt()*E/a)/delta+(2*hs).sqrt()*2/mu*(2*E+Eq/delta)).upper()
# Original tail norm estimate is linear in the h supremum, so replace that
# supremum by the rigorously bounded variation of h about its constant value.
tailX=variation*(arb.pi()/2*(2*d).sqrt()+d/a*(2*hs).sqrt()/2+4*d*(2*hs).sqrt()+14*(2*mu).sqrt()*d/a)/delta
tailX+=(2*hs).sqrt()*2/mu*(2*variation*d+1000*variation*d*(2-d.log())/delta)
wr=json.loads((g['WHOLE']/'WHOLE_RESULT.json').read_bytes());remain=(selected+tailX+q(wr['core_bridge_X_error_upper'])+HQm_error*(hs+b.sinh()-a.sinh()).sqrt()/(mu*delta)+q('1e-150')).upper()
data=json.loads((TASK/'kernel-orientation-81.json').read_bytes());rows=[]
for r,change in zip(data['rows'],outmom):
 i=r['coordinate']-1;testnorm=sum((J[k,i]**2 for k in range(96)),arb(0)).upper().sqrt()
 error=remain*testnorm;v=c.pad(box(r['corrected_difference'])+change,error)
 rows.append({'coordinate':i+1,'after_orientation_difference':r['corrected_difference'],'signed_core_tail_correction':enc(change),'remaining_core_error':enc(error),'final_difference':enc(v),'contains_zero':v.contains(0)})
out={'status':'SIGNED_CORE_TAIL_CORRECTION_ALREADY_PAID_BY_EXISTING_CORE_QUADRATURE_PRICE','rows':rows,'h_constant':enc(h0),'h_variation_bound':enc(variation),'core_tail_width':enc(d),'remaining_core_X_error':enc(remain),'selected_core_X_error':enc(selected),'tail_variation_X_error':enc(tailX),'additional_budget_charge':False,'seconds':time.monotonic()-g['start']}
(TASK/'core-tail.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('AFTER_BOTH_MAX',max(float(abs(box(r['final_difference'])).upper())for r in rows),'ZERO',sum(r['contains_zero']for r in rows),'CORE_REMAINDER',float(remain),flush=True)
