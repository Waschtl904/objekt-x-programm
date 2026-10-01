"""Independent finite tests for the planned rational residual enclosure.
No A9/A11 input is loaded. Tests include a nonorthogonal physical mass.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent/'publication-deps'))
from flint import arb, arb_mat, acb, acb_mat, ctx
ctx.prec=256
def trc(a):return acb_mat([[a[j,i].conjugate() for j in range(a.nrows())] for i in range(a.ncols())])
def e(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def norm2(a,g):return (trc(a)*acb_mat(g)*a)[0,0].real
def rm(a):return arb_mat([[a[i,j].real for j in range(a.ncols())] for i in range(a.nrows())])
for tl,th,b in [(arb(0),arb(0),arb('0.003')),(arb('0.3'),arb('0.2'),arb('0.02'))]:
 g=e(2)+arb_mat([[tl],[th]])*arb_mat([[tl,th]])
 h=arb_mat([['0.0001',b],[b,10]])
 assert h.det()>0
 op=g.inv()*h
 lo=(op.trace()-(op.trace()**2-4*op.det()).sqrt())/2
 hi=(op.trace()+(op.trace()**2-4*op.det()).sqrt())/2
 u=arb_mat([[1/g[0,0].sqrt()],[0]])
 projector=(hi*e(2)-op)/(hi-lo)
 target=projector*u
 scale=arb('0.1');m=8
 scalar=max(((lo/scale)**m/(1+(lo/scale)**m)).upper(),(1/(1+(hi/scale)**m)).upper())
 total=arb_mat(2,1);err=scalar
 for k in range(4):
  angle=arb.pi()*(2*k+1)/m;z=acb(scale*angle.cos(),scale*angle.sin())
  # One-dimensional Galerkin solve, checked in the complete two-dimensional system.
  xx=acb(g[0,0]*u[0,0])/(h[0,0]-z*g[0,0]);x=acb_mat([[xx],[0]])
  residual=acb_mat(g*u)-(acb_mat(h)-acb_mat(g)*z)*x
  raw=norm2(residual,e(2)).sqrt().upper()
  dual=norm2(residual,g.inv()).sqrt().upper()
  assert dual<=raw or (raw-dual).contains(0)
  distance=min(abs(z-acb(lo)).lower(),abs(z-acb(hi)).lower())
  actual=(acb_mat(op)-acb_mat(e(2))*z).solve(acb_mat(u))-x
  assert norm2(actual,g).sqrt().upper() < raw/distance
  total+=rm(x*(-z/m))*2
  err+=2*abs(z).upper()/m*raw/distance
 difference=target-total
 actual_error=(difference.transpose()*g*difference)[0,0].sqrt().upper()
 assert actual_error<err
 # Check the complete rational partial-fraction sum against the matrix rational function.
 full=arb_mat(2,1)
 for k in range(4):
  angle=arb.pi()*(2*k+1)/m;z=acb(scale*angle.cos(),scale*angle.sin())
  full+=rm((acb_mat(op)-acb_mat(e(2))*z).solve(acb_mat(u))*(-z/m))*2
 power=e(2)
 for k in range(m):power=power*(op/scale)
 direct=(e(2)+power).solve(u)
 assert all(v.contains(0) for v in (full-direct).entries())
 # Omitting the high residual would incorrectly certify zero error for this Galerkin solve.
 assert actual_error>scalar
print('Rational filter identity, complete residual bound, nonorthogonal mass and omitted-high negative control: PASS')

# A separate exact rational check of joint signed residual identities and
# the two direct product perturbation bounds used for K.
from fractions import Fraction as F
def dot(x,y):return sum(a*b for a,b in zip(x,y))
def plus(x,y):return [a+b for a,b in zip(x,y)]
def minus(x,y):return [a-b for a,b in zip(x,y)]
ua=[F(3,5),F(4,5),F(0)];ub=[F(0),F(3,5),F(4,5)]
pa=[F(3,5),F(0),F(0)];pb=[F(0),F(0),F(4,5)]
ra=minus(ua,pa);rb=minus(ub,pb)
assert dot(pa,pb)==dot(ua,ub)-dot(ra,ub)-dot(ua,rb)+dot(ra,rb)
ea=[F(1,100),F(-1,200),F(1,300)];eb=[F(-1,80),F(1,150),F(1,250)]
aa=minus(pa,ea);bb=minus(pb,eb)
error=abs(dot(pa,pb)-dot(aa,bb))
ena=arb(str(dot(ea,ea).numerator))/dot(ea,ea).denominator;ena=ena.sqrt()
enb=arb(str(dot(eb,eb).numerator))/dot(eb,eb).denominator;enb=enb.sqrt()
na=arb(str(dot(aa,aa).numerator))/dot(aa,aa).denominator;na=na.sqrt()
nb=arb(str(dot(bb,bb).numerator))/dot(bb,bb).denominator;nb=nb.sqrt()
exact_error=arb(error.numerator)/error.denominator
assert exact_error<ena*nb+enb and exact_error<ena+enb*na
assert dot(ra,rb)!=0  # Dropping the shared cross residual changes the exact identity.
print('Signed residual identity, shared cross term and direct K perturbation bounds: PASS')
ga=dot(ua,pa);gb=dot(ub,pb)
ea_trial=minus(pa,[ga*x for x in ua]);eb_trial=minus(pb,[gb*x for x in ub])
assert dot(ua,ea_trial)==dot(ub,eb_trial)==0
assert dot(ea_trial,ea_trial)==ga-ga*ga and dot(eb_trial,eb_trial)==gb-gb*gb
joint=ga*dot(ua,ub)*gb+ga*dot(ua,eb_trial)+gb*dot(ea_trial,ub)+dot(ea_trial,eb_trial)
assert joint==dot(pa,pb)
print('Common projected Gram covariance and signed product decomposition: PASS')
