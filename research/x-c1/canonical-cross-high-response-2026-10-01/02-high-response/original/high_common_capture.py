"""Directed high-response utilities; all polynomial coordinates are Legendre."""
from fractions import Fraction as F
from math import factorial
from flint import arb, acb, arb_mat, acb_mat, fmpq

def rat(x):
 f=F(x);return arb(fmpq(f.numerator,f.denominator))
def ball(x,den=1):
 l,h=map(F,x);l/=den;h/=den
 assert l<=h
 return rat((l+h)/2)+arb(0,rat((h-l)/2))
def mat(x,den=1):return arb_mat([[ball(v,den) for v in row] for row in x])
def eye(n):return arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
def exact(x,lower=True):
 v=x.lower() if lower else x.upper();m,e=map(int,v.man_exp())
 return str(F(m*2**e) if e>=0 else F(m,2**(-e)))
def iv(x):return [exact(x),exact(x,False)]
def ci(x):return [iv(x.real),iv(x.imag)]
def cmat(x):return acb_mat([[acb(ball(v[0]),ball(v[1])) for v in row] for row in x])
def cmi(x):return [[ci(x[i,j]) for j in range(x.ncols())] for i in range(x.nrows())]
def real(x):return arb_mat([[x[i,j].real for j in range(x.ncols())] for i in range(x.nrows())])
def imag(x):return arb_mat([[x[i,j].imag for j in range(x.ncols())] for i in range(x.nrows())])
def point(x):return acb_mat([[acb(x[i,j].real.mid(),x[i,j].imag.mid()) for j in range(x.ncols())] for i in range(x.nrows())])
def normcol(x,j):return sum((abs(x[i,j]).upper()**2 for i in range(x.nrows())),arb(0)).sqrt().upper()
def normsq(x,j):return sum((x[i,j].real*x[i,j].real+x[i,j].imag*x[i,j].imag for i in range(x.nrows())),arb(0))
def values(x,n):
 out=[arb(1)]
 if n:out.append(x)
 for k in range(2,n+1):
  if k%64==0:
   # Restart from independent Arb special-function enclosures. A single
   # long interval recurrence otherwise amplifies rounding exponentially.
   previous=x.legendre_p(k-1);current=x.legendre_p(k)
   assert previous.overlaps(out[-1])
   out[-1]=previous;out.append(current)
  else:out.append(((2*k-1)*x*out[-1]-(k-1)*out[-2])/k)
 return out
def moment(a,n):
 z=a/2;lead=arb(1)
 for j in range(1,n+1):lead*=z/(2*j+1)
 term=total=arb(1)
 for k in range(128):term*=z*z/(2*(k+1)*(2*n+2*k+3));total+=term
 nxt=term*z*z/(2*129*(2*n+259));tail=nxt/(1-z*z/(2*130*(2*n+261)))
 return lead*(total+arb(0,tail.upper()))
def channels(a,name):
 pairs=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]+([(9,3)] if name=='A11' else [])
 return [(q,arb(p).log()/arb(q).sqrt(),arb(q).log()/a) for q,p in pairs]

def gamma_action(q,pg,a):
 """Exact polynomial kernel action by directional double integration.

 q stores ordinary P_n coefficients. F_k(x)=integral |x-y|^k q(y) dy/2.
 F_1''=q, F_k''=k(k-1)F_{k-2}; boundary values are beta integrals.
 """
 n=q.nrows()-1;c=q.ncols();m=len(pg)-1;D=n+m+2
 out=acb_mat(D,c)
 for col in range(c):
  source=[q[j,col] for j in range(n+1)]
  previous=[[source[0]]];acc=[acb(0) for _ in range(D)]
  acc[0]=2*a*rat(pg[0])*source[0]
  for k in range(1,m+1):
   p=source if k==1 else [k*(k-1)*v for v in previous[k-2]]
   def integral(seq):
    z=[acb(0) for _ in range(len(seq)+1)]
    for j,v in enumerate(seq):
     t=v/(2*j+1);z[j+1]+=t
     if j:z[j-1]-=t
    return z
   r=integral(integral(p))
   val=sum((source[j]*rat(F(2**k*(-1)**j*factorial(k)**2,factorial(k-j)*factorial(k+j+1))) for j in range(min(k,n)+1)),acb(0))
   der=sum((source[j]*rat(F(k*2**(k-1)*(-1)**j*factorial(k-1)**2,factorial(k-1-j)*factorial(k+j))) for j in range(min(k-1,n)+1)),acb(0))
   alpha=der-sum((v*(j*(j+1)//2) for j,v in enumerate(r)),acb(0))
   beta=val-sum(r,acb(0))-alpha
   r[1]+=alpha;r[0]+=beta
   # Exact input oddness is used as an analytic identity, with an overlap guard.
   if all(source[j]==0 for j in range(0,n+1,2)):
    assert all(r[j].contains(0) for j in range(0,len(r),2))
    for j in range(0,len(r),2):r[j]=acb(0)
   previous.append(r)
   w=2*a*(a/2)**k*rat(pg[k])
   if w!=0:
    for j,v in enumerate(r):acc[j]+=w*v
  for j,v in enumerate(acc):out[j,col]=v
 return out

def high_coefficients(q,pg,a,name,indices,progress=lambda s:None):
 """Raw high coefficients of (V-Gamma-S)q in normalized e_k."""
 n=q.nrows()-1;c=q.ncols();K=max(indices);rows=[]
 for k in indices:
  rows.append([arb(2*k+1).sqrt()/(abs(i-k)*(i+k+1)) if (i+k)%2==0 and i!=k else arb(0) for i in range(n+1)])
 assert min(indices)>n
 pot=acb_mat(arb_mat(rows))*q
 ga=gamma_action(q,pg,a)
 gam=acb_mat([[ga[k,j]/arb(2*k+1).sqrt() if k<ga.nrows() else acb(0) for j in range(c)] for k in indices])
 progress('directional Gamma response ready')
 count=(n+K+2)//2
 nodes=[arb.legendre_p_root(count,k,weight=True) for k in range(count)]
 shift=acb_mat(len(indices),c)
 for channel,w,d in channels(a,name):
  length=2-d;left=[];right=[]
  for node,weight in nodes:
   x=-1+length*(node+1)/2
   left.append(values(x,n))
   seq=values(x+d,K)
   right.append([seq[k]*arb(2*k+1).sqrt()*weight*length/2*w for k in indices])
  shift+=acb_mat(arb_mat(right).transpose())*(acb_mat(arb_mat(left))*q)
  progress('signed high shift channel '+str(channel))
 return pot-gam-shift,{'potential':pot,'gamma':gam,'shift':shift,'quadrature_nodes':count}

def finite_action(q,pg,a,name,indices,progress=lambda s:None):
 """Normalized finite coefficients of the full raw model Q^P q.

 No omitted coefficient is asserted zero: this is only a Galerkin assembly.
 """
 n=q.nrows()-1;c=q.ncols();K=max(indices);harm=[arb(0)]
 for k in range(1,2*max(n,K)+1):harm.append(harm[-1]+arb(1)/k)
 log2=arb(2).log();rows=[]
 for k in indices:
  row=[]
  for i in range(n+1):
   if (i+k)%2:v=arb(0)
   elif i!=k:v=arb(1)/(abs(i-k)*(i+k+1))
   else:v=(arb(1)/(2*i+1)+2*(harm[2*i]-harm[i])-log2)/(2*i+1)
   row.append(v*arb(2*k+1).sqrt())
  rows.append(row)
 out=acb_mat(arb_mat(rows))*q
 ga=gamma_action(q,pg,a)
 for ii,k in enumerate(indices):
  for j in range(c):
   if k<ga.nrows():out[ii,j]-=ga[k,j]/arb(2*k+1).sqrt()
   if k<=n:out[ii,j]+=(harm[k]-(2*arb.pi()*a).log()-arb.const_euler())*q[k,j]/arb(2*k+1).sqrt()
 progress('finite model: potential, harmonic and Gamma ready')
 count=(n+K+2)//2;nodes=[arb.legendre_p_root(count,k,weight=True) for k in range(count)]
 for channel,w,d in channels(a,name):
  length=2-d;left=[];right=[]
  for node,weight in nodes:
   x=-1+length*(node+1)/2
   left.append(values(x,n));seq=values(x+d,K)
   right.append([seq[k]*arb(2*k+1).sqrt()*weight*length/2*w for k in indices])
  out-=acb_mat(arb_mat(right).transpose())*(acb_mat(arb_mat(left))*q)
  progress('finite model: signed shift '+str(channel))
 return out
