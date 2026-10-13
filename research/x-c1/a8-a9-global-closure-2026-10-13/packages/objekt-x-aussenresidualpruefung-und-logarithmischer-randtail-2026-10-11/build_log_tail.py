"""Full infinite tail Gram for log(u), log(u)^2, log(1-u), n>=104.

Pure rational series bounds. No finite tail is passed off as an infinite
sum. The result is an auxiliary singular-function Gram, not the full R Gram.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,math
ap=argparse.ArgumentParser();ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
N=104;terms=400
def add(x,y):return (x[0]+y[0],x[1]+y[1])
def neg(x):return (-x[1],-x[0])
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 vals=[a*b for a in x for b in y];return min(vals),max(vals)
def point(x):return F(x),F(x)
def sc(x,s):return mul(x,point(s))
def log_bound(q,k):
 z=F(q-1,q+1)
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(k)),F(0))
 err=2*z**(2*k+1)/F(2*k+1)/(1-z*z)
 return lo,lo+err
def zeta_bounds(s):
 H=F(0);H2=F(0);val=F(0)
 for n in range(1,terms+1):
  H+=F(1,n);H2+=F(1,n*n)
  difference=H/n if s==2 else (H*H+H2)/(2*n)
  val+=difference/F(2**n)
 factor=1/(1-F(1,2**(s-1)))
 return factor*val,factor*(val+F(1,2**terms))
z2=zeta_bounds(2);z3=zeta_bounds(3)
h=sub(log_bound(3,240),sc(log_bound(2,160),F(3,2)))
assert F(1,20)<h[0]<h[1]<F(1,16)
G=[[point(2),point(-6),sub(point(2),z2)],
   [point(-6),point(24),add(add(point(-6),sc(z2,2)),sc(z3,2))],
   [sub(point(2),z2),add(add(point(-6),sc(z2,2)),sc(z3,2)),point(2)]]
prefix=[[F(0) for j in range(3)] for i in range(3)]
H=[F(0)]
for n in range(1,N+1):H.append(H[-1]+F(1,n))
coeff=[]
polys=[[F(1)],[F(-1),F(2)]]
for k in range(1,N-1):
 pp=polys[-1];pm=polys[-2];pn=[F(0)]*(len(pp)+1)
 for j,v in enumerate(pp):pn[j]-=(2*k+1)*v;pn[j+1]+=2*(2*k+1)*v
 for j,v in enumerate(pm):pn[j]-=k*v
 polys.append([v/(k+1) for v in pn])
for n in range(N):
 if n==0:v=[F(-1),F(2),F(-1)]
 else:
  den=n*(n+1)
  v=[F((-1)**(n+1),den),F(2*(-1)**n,den)*(H[n-1]+H[n+1]),F(-1,den)]
 # Independent exact polynomial integration verifies all prefix moments.
 assert sum((-a/F((j+1)**2) for j,a in enumerate(polys[n])),F(0))==v[0]
 assert sum((2*a/F((j+1)**3) for j,a in enumerate(polys[n])),F(0))==v[1]
 assert v[2]==(-1)**n*v[0]
 coeff.append([str(x) for x in v])
 for i in range(3):
  for j in range(3):prefix[i][j]+=(2*n+1)*v[i]*v[j]
tail=[[mul(sc(h,2),sub(G[i][j],point(prefix[i][j]))) for j in range(3)] for i in range(3)]
assert sub(G[2][2],point(prefix[2][2]))==point(F(1,N*N))
# A fixed rational upper matrix pays every entry uncertainty by diagonal
# dominance. The interval table remains available for sharper contractions.
den=10**100
centre=[[F(round((x[0]+x[1])*den/2),den) for x in row] for row in tail]
upper=[row[:] for row in centre]
for i in range(3):
 radius=sum(max(abs(tail[i][j][0]-centre[i][j]),abs(tail[i][j][1]-centre[i][j])) for j in range(3))
 upper[i][i]+=F(math.ceil(radius*den),den)
out={'status':'FULL_INFINITE_LOG_TEMPLATE_TAIL_GRAM_ENCLOSED','N':N,
 'basis':['log(u)','log(u)^2','log(1-u)'],'physical_inner_product':'2h integral_0^1',
 'h_interval':[str(v) for v in h],'zeta2_interval':[str(v) for v in z2],
 'zeta3_interval':[str(v) for v in z3],'Euler_terms':terms,
 'Legendre_moments_through_103':coeff,
 'independent_exact_polynomial_log_moment_checks':2*N,
 'full_tail_Gram_intervals':[[[str(v) for v in x] for x in row] for row in tail],
 'full_tail_Gram_rational_upper':[[str(v) for v in row] for row in upper],
 'outer_log_tail_scalar_exact':'2h/104^2',
 'actual_residual_singular_coefficient_matrix_complete':False,
 'actual_regular_remainder_derivative_Gram_computed':False,'full_remainder_certified':False}
args.out.write_text(json.dumps(out,indent=2)+'\n')
print('Full infinite log-tail Gram upper, N=104:')
for row in upper:print([float(x) for x in row])
