"""Exact signed perturbation from correcting inner/outer regular kernel orientation.
This is an experiment on a separate model, never an edit of the frozen package.
"""
from pathlib import Path
import json,time,sys
TASK=Path(__file__).resolve().parent
BOOT=TASK.parent/'pairing-check/run_pairs.py'
g={'__file__':str(BOOT),'__name__':'orientation_bootstrap'}
exec(compile(BOOT.read_text(encoding='utf-8').split('# Coarse signed quadrature')[0],str(BOOT),'exec'),g)
arb,arb_mat,arb_poly,ns,c=(g[k]for k in ['arb','arb_mat','arb_poly','ns','c'])
q,enc,box=c.q,c.enc,c.box
a,b,hs,half,mid,J,Y,w,pv,delta,mu,fac,convker,gamma,leg=(ns[k]for k in ['a','b','hs','half','mid','J','Y','w','pv','delta','mu','fac','convker','gamma','leg'])
eta=q('1e-10');of=ns['of'];mc=arb_poly([(a/2)**k/fac[k]if k%2==0 else arb(0)for k in range(161)])
cuts=[]
for edge in ns['edges']:
 for sh,wt in ns['channels']:
  cuts.extend(xx for xx in [edge+sh,edge-sh,sh-edge,-edge-sh]if a<xx<b)
cuts.extend(xx for xx in ns['res'].cuts if a<xx<b);cuts.sort(key=float)
exact_edges=[a]
for xx in cuts:
 if not xx.overlaps(exact_edges[-1]):exact_edges.append(xx)
exact_edges.append(b);assert len(exact_edges)==4
def regular_out(moments):
 co=convker*arb_poly([2*moments[k]/fac[k]if k%2==0 else arb(0)for k in range(225)])
 return arb_poly([co[224-k]/fac[k]for k in range(225)])
def shellpoly(coeff):return sum((leg[k]*(coeff[k,0]*(arb(2*k+1)/(2*hs)).sqrt())for k in range(96)),arb_poly([]))(arb_poly([-mid/half,1/half]))
def correction(coeff):
 sp=shellpoly(coeff)
 moments=[c.pint(sp*arb_poly([0]*k+[1]),a,b)for k in range(225)]
 co=convker*arb_poly([moments[k]/fac[k]for k in range(225)])
 right=arb_poly([co[224-k]/fac[k]*(1+(-1)**k)for k in range(225)])
 wrong=regular_out(moments)
 return (wrong-right)(arb_poly([0,a]))
gcoeff=J*w-Y*arb_mat([[pv[i,0]]for i in range(4,12)])
dG=correction(gcoeff);dPsi=correction(ns['slocal'])
alpha=c.pint(dG)/c.mellin(0,a)
du=(dG-alpha*mc)*(1/delta)
print('CORE_CORRECTION_READY',round(time.monotonic()-g['start'],2),flush=True)
# Q8 m: original model, including every prime cell.
mls=[arb(0)]*161;mdh=arb_poly([])
for n in range(0,161,2):
 mls[n]=(2*n+1)*c.pint(mc*leg[n]);mdh+=leg[n]*(mls[n]*ns['harm'][n])
qm0=mdh+mc*(-(2*arb.pi()*a).log()-arb.const_euler())-of.kernel(mc,mls,a,gamma,0)
qmLog=mc*(-arb(1)/2)
def logint01(p,root):
 mm=[-arb(1)/(k+1)**2 for k in range(len(p))]if root==0 else of.log_moments(root,len(p))
 return sum((p[k]*mm[k]for k in range(len(p))),arb(0))
dR=a*c.pint(dPsi*mc)+a*(c.pint(du*qm0)+logint01(du*qmLog,arb(1))+logint01(du*qmLog,arb(-1)))
for lo,hi in zip(ns['edges'][:-1],ns['edges'][1:]):
 at=(lo+hi)/2;pp=arb_poly([])
 for sh,wt in ns['channels']:
  for sign in [-1,1]:
   if abs(at+sign*sh)<a:pp-=mc(arb_poly([sign*sh/a,1]))*wt
 dR+=a*c.pint(du*pp,lo/a,hi/a)
# Reconstruct the correction on the physical outer shell x=a+hs*z.
x=arb_poly([a,hs]);s=x*(1/a)
def quotient_moment(p):return arb_poly([sum((p[k]/(k-j)for k in range(j+1,len(p))),arb(0))for j in range(len(p)-1)])
corr=quotient_moment(du)
# -1/2 [C(s)-C(-s)], C(s)=P(s)log|s/(s-1)|-int quotient.
plain=(corr(s)-corr(-s))*(arb(1)/2)
logs=[(arb(0),du(s)*(arb(1)/2)), (-2*a/hs,du(-s)*(-arb(1)/2)), (-a/hs,(du(-s)-du(s))*(arb(1)/2))]
# All log(hs) constants cancel identically.
moment=[a**(k+1)*c.pint(du*arb_poly([0]*k+[1]))for k in range(225)]
plain-=regular_out(moment)(x)+mc(s)*(dR/mu)
polys=[sum((leg[k]*(J[k,i]*(arb(2*k+1)/(2*hs)).sqrt())for k in range(96)),arb_poly([]))(arb_poly([-1,2]))for i in range(84)]
outmom=[]
for i,jp in enumerate(polys):
 v=2*hs*c.pint(plain*jp)
 for root,pol in logs:v+=2*hs*logint01(pol*jp,root)
 outmom.append(v)
# Prime translations of du are polynomial on the known outer cells.
edges=exact_edges
for lo,hi in zip(edges[:-1],edges[1:]):
 at=(lo+hi)/2;pp=arb_poly([])
 for sh,wt in ns['channels']:
  for sign in [-1,1]:
   y=at+sign*sh
   if abs(y)<a:
    affine=(x+sign*sh)*(1/a)
    if y<0:affine=-affine
    pp-=du(affine)*wt
 for i,jp in enumerate(polys):outmom[i]+=2*hs*c.pint(pp*jp,(lo-a)/hs,(hi-a)/hs)
data=json.loads((TASK/('localized-81.json'if '--extra'in sys.argv else 'localized.json')).read_bytes());rows=[]
for r,change in zip(data['rows'],outmom):
 old=box(r['difference_expanded']);new=old+change
 rows.append({'coordinate':r['coordinate'],'old_difference':enc(old),'orientation_correction':enc(change),'corrected_difference':enc(new),'corrected_contains_zero':new.contains(0)})
out={'status':'EXPERIMENTAL_EXACT_KERNEL_ORIENTATION_CORRECTION','formula':'inner: factor 1+(-1)^output_degree; outer: keep even input moments','rows':rows,'alpha_correction':enc(alpha),'momentR_correction':enc(dR),'seconds':time.monotonic()-g['start']}
(TASK/('kernel-orientation-81.json'if '--extra'in sys.argv else 'kernel-orientation.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print('MAX_OLD',max(float(abs(box(r['old_difference'])).upper())for r in rows),flush=True)
print('MAX_CORRECTION',max(float(abs(box(r['orientation_correction'])).upper())for r in rows),flush=True)
print('MAX_REMAINING',max(float(abs(box(r['corrected_difference'])).upper())for r in rows),'ZERO',sum(r['corrected_contains_zero']for r in rows),flush=True)
print('SECONDS',out['seconds'],flush=True)
