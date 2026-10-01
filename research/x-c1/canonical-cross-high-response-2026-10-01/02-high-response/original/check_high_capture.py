"""Small independent assembly checks before actual capture calculations."""
from pathlib import Path
import argparse,sys,importlib.util
from flint import arb,acb,acb_mat,arb_poly,ctx
from high_common import *
p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);args=p.parse_args()
ctx.prec=512
engine=args.repo/'research/x-c1/chambers-through-a11-2026-09-28/a11'
sys.path.insert(0,str(engine));import generate_a11 as reference
a=arb(11).log()/2;pg,_=reference.gamma_polynomial(16)
q=acb_mat(8,2)
for i in (1,3,5,7):
 q[i,0]=acb(F(i,17).numerator,F(i,17).denominator) # arbitrary exact complex data
 q[i,1]=acb(rat(F(i,23)),rat(F(-i,31)))
got=gamma_action(q,[str(v) for v in pg],a)
from high_common_capture import gamma_action as frozen_gamma_action
frozen=frozen_gamma_action(q,[str(v) for v in pg],a)
cols=reference.gamma_columns(7,16,pg,a)
for n in range(got.nrows()):
 for j in range(2):
  want=sum((q[i,j]*cols[i].get(n,arb(0)) for i in range(8)),acb(0))
  assert (got[n,j]-want).contains(0)
  assert (frozen[n,j]-want).contains(0)
h,parts=high_coefficients(q,[str(v) for v in pg],a,'A11',[9,11,13])
# Independent exact antiderivatives of translated monomial polynomials.
pol=[arb_poly(v) for v in reference.leg_polynomials(13)]
def integral(poly,l,r):return sum((poly[i]*(r**(i+1)-l**(i+1))/(i+1) for i in range(len(poly))),arb(0))
for ii,k in enumerate((9,11,13)):
 for j in range(2):
  s=acb(0)
  for _,w,d in channels(a,'A11'):
   for i in (1,3,5,7):
    s+=q[i,j]*w*arb(2*k+1).sqrt()*integral(pol[i]*pol[k](arb_poly([d,1])),arb(-1),1-d)
  assert (s-parts['shift'][ii,j]).contains(0)
  pot=sum((q[i,j]*arb(2*k+1).sqrt()/((k-i)*(k+i+1)) for i in (1,3,5,7)),acb(0))
  gam=got[k,j]/arb(2*k+1).sqrt()
  assert (h[ii,j]-(pot-gam-s)).contains(0)
print('PASS: directional Gamma recurrence, signed shifts, parity and normalized high coefficients')
ctx.prec=1024
seq=values(rat('2/3'),849)
for k in (63,64,127,255,593,721,849):
 assert seq[k].overlaps(rat('2/3').legendre_p(k)) and seq[k].rad()<rat('1e-270')
print('PASS: restarted long Legendre recurrence at fixed 1024-bit precision')
