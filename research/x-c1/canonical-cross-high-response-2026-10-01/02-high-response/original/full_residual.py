"""Complete L2 residual of a finite polynomial candidate, with no high truncation.

The raw model is D_H+V+q0-Gamma-S. Integrate its entire piecewise
polynomial/logarithmic response. Subtract a multiple of the exact odd
Mellin normal sinh(Ax/2); its Taylor remainder is explicitly paid.
"""
from math import factorial
from flint import arb,acb,arb_poly,acb_mat
from high_common import *

def polys(n):
 x=arb_poly([0,1]);out=[arb_poly([1])]
 if n:out.append(x)
 for k in range(2,n+1):out.append(((2*k-1)*x*out[-1]-(k-1)*out[-2])*(arb(1)/k))
 return out
def integrate(p,l,r):return sum((p[i]*(r**(i+1)-l**(i+1))/(i+1) for i in range(len(p))),arb(0))
def vmom(b,n):
 if b==1:return [arb(0)]*(n+1)
 lm=(1-b).log();lp=(1+b).log();hp=arb(0);ps=arb(0);ao=arb(0);az=arb(0);power=arb(1);out=[];log2=arb(2).log()
 for m in range(1,n+2):
  power*=b;hp+=arb(1)/m;ps+=power/m;ao=-ao+arb(1)/m;az=-az+power/m
  minus=(hp-ps-(1-power)*lm)/m
  plus=((1-(-1)**m)*log2-ao-(power-(-1)**m)*lp+az)/m
  out.append((minus-plus)/2)
 return out
def dotpoly(p,mom):return sum((p[i]*mom[i] for i in range(len(p))),arb(0))
def v2mom(n):
 out=[];odd=arb(0);odd2=arb(0);log2=arb(2).log();pi2=arb.pi()**2/12
 for r in range(n//2+1):
  odd+=arb(1)/(2*r+1);odd2+=arb(1)/(2*r+1)**2
  out.extend([((odd-log2)**2+odd2-pi2)/(2*r+1),arb(0)])
 return out

def local_vmom(l,r,n):
 """Integral_0^1 s^j V(l+(r-l)s) ds, stable backward recurrence."""
 h=r-l
 def logmom(A,c,endpoint=False):
  if endpoint:
   harmonic=arb(0);out=[]
   for j in range(n+1):harmonic+=arb(1)/(j+1);out.append((A.log()-harmonic)/(j+1))
   return out
  assert abs(c)<1
  power=arb(1);start=arb(0)
  for k in range(2048):start+=power/(n+k+2);power*=c
  tail=abs(power).upper()/(1-abs(c).upper())
  T=[arb(0)]*(n+2);T[n+1]=start+arb(0,tail.upper())
  for j in range(n+1,0,-1):T[j-1]=arb(1)/j+c*T[j]
  logarithm=A.log()+(1-c).log()
  return [(logarithm+c*T[j+1])/(j+1) for j in range(n+1)]
 minus=logmom(1-l,h/(1-l),r==1);plus=logmom(1+l,-h/(1+l))
 return [-(x+y)/2 for x,y in zip(minus,plus)]

def affine_expansion(coeff,l,h):
 """Expand several Legendre columns directly in a short cell coordinate."""
 out=[[arb_poly([]),arb_poly([])] for j in range(coeff.ncols())]
 previous=arb_poly([1]);current=arb_poly([l,h])
 for i in range(coeff.nrows()):
  poly=previous if i==0 else current
  if i>=2:
   nxt=((2*i-1)*arb_poly([l,h])*current-(i-1)*previous)*(arb(1)/i)
   previous,current=current,nxt;poly=current
  for j in range(coeff.ncols()):
   out[j][0]+=poly*coeff[i,j].real;out[j][1]+=poly*coeff[i,j].imag
 return out

def norm_certificates(w,u,poles,pg,a,name,progress=lambda s:None,subtract_normal=True):
 """q columns are ordinary Legendre coefficients, all inputs odd.

 Returns true raw-model full residual enclosures after a harmless normal
 subtraction; physical projection contracts. Gamma model error and source
 rounding are added by the caller. Every finite coefficient is a candidate.
 """
 N=w.nrows()-1;c=w.ncols();assert u.nrows()==w.nrows() and u.ncols()==c and len(poles)==c
 assert all(w[i,j]==0 and u[i,j]==0 for i in range(0,N+1,2) for j in range(c))
 ga=gamma_action(w,pg,a);D=ga.nrows()-1
 harm=[arb(0)]
 for n in range(1,N+1):harm.append(harm[-1]+arb(1)/n)
 q0=-(2*arb.pi()*a).log()-arb.const_euler()
 ch=channels(a,name);edges=[arb(0),arb(1)]
 for _,_,d in ch:
  for s in (-1,1):
   for edge in (-1,1):
    v=edge-s*d
    if 0<v<1 and not any(v.overlaps(x) for x in edges):edges.append(v)
 edges.sort(key=lambda x:float(x.mid()));assert all(l<r for l,r in zip(edges,edges[1:]))
 maxpower=2*max(D,81)+2;v2=v2mom(2*N)
 normal=arb_poly([((a/2)**i/factorial(i) if i%2 else arb(0)) for i in range(82)])
 normal*=1/(arb(3).sqrt()*moment(a,1))
 normal_tail=((a/2)**83/factorial(83)/(1-(a/2)**2/(84*85))/(arb(3).sqrt()*moment(a,1))).upper()
 wp=affine_expansion(w,arb(0),arb(1))
 b=acb_mat([[ga[i,j]+(u[i,j]+(poles[j]-q0-harm[i])*w[i,j] if i<=N else acb(0)) for j in range(c)] for i in range(D+1)])
 cells=[];r1r=[arb(0) for j in range(c)];r1i=[arb(0) for j in range(c)]
 for k,(l,r) in enumerate(zip(edges,edges[1:])):
  h=r-l;mid=(l+r)/2;bp=affine_expansion(b,l,h);vm=local_vmom(l,r,maxpower);lc=arb_poly([l,h]);xp=lc*arb(3).sqrt();rows=[]
  for j in range(c):
   wr,wi=[poly(lc) for poly in wp[j]];cr,ci=bp[j]
   for _,weight,d in ch:
    for sign in (-1,1):
     shift=sign*d
     if -1<mid+shift<1:
      sr,si=[poly(arb_poly([l+shift,h])) for poly in wp[j]];cr+=sr*weight;ci+=si*weight
   r1r[j]+=h*(integrate(xp*cr,arb(0),arb(1))-dotpoly(xp*wr,vm))
   r1i[j]+=h*(integrate(xp*ci,arb(0),arb(1))-dotpoly(xp*wi,vm))
   rows.append((wr,wi,cr,ci))
  cells.append((h,normal(lc),vm,rows))
  progress('complete integration cell '+str(k+1)+'/'+str(len(edges)-1))
 out=[]
 for j in range(c):
  wr,wi=wp[j];norm=dotpoly(wr*wr+wi*wi,v2);raw_norm=norm
  for h,normpoly,vm,rows in cells:
   wr,wi,cr,ci=rows[j]
   raw_norm+=h*(integrate(cr*cr+ci*ci,arb(0),arb(1))-2*dotpoly(wr*cr+wi*ci,vm))
   if subtract_normal:cr-=normpoly*r1r[j];ci-=normpoly*r1i[j]
   norm+=h*(integrate(cr*cr+ci*ci,arb(0),arb(1))-2*dotpoly(wr*cr+wi*ci,vm))
  assert raw_norm.lower()>=0 and norm.lower()>=0,(raw_norm,norm)
  assert raw_norm.rad()<rat('1e-20') and norm.rad()<rat('1e-20'), 'Full integral cancellation requires a valid directed enclosure'
  extra=((r1r[j]*r1r[j]+r1i[j]*r1i[j]).sqrt()*normal_tail).upper() if subtract_normal else arb(0)
  bound=(norm.upper().sqrt()+extra).upper()
  out.append({'raw_model_residual_norm_squared':iv(raw_norm),'normal_removed_model_residual_norm_squared':iv(norm),
   'raw_carrier_residual':[iv(r1r[j]),iv(r1i[j])],'Mellin_normal_Taylor_error_upper':exact(extra,False),
   'complete_model_residual_upper':exact(bound,False),'all_high_modes_included':True})
  progress('complete residual column '+str(j+1)+'/'+str(c)+': '+str(float(bound)))
 return out
