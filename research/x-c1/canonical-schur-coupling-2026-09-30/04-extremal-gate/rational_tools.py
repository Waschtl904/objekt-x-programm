from fractions import Fraction as F
from math import isqrt

def pt(x):return F(x),F(x)
def iv(x):
 a,b=map(F,x);assert a<=b;return a,b
def add(x,y):return x[0]+y[0],x[1]+y[1]
def neg(x):return -x[1],-x[0]
def sub(x,y):return add(x,neg(y))
def mul(x,y):
 a=[u*v for u in x for v in y];return min(a),max(a)
def div(x,y):
 assert y[0]*y[1]>0;return mul(x,(1/y[1],1/y[0]))
def sq(x):return (F(0) if x[0]<=0<=x[1] else min(abs(x[0]),abs(x[1]))**2,max(abs(x[0]),abs(x[1]))**2)
def ab(x):return max(abs(x[0]),abs(x[1]))
def total(xs):
 a=pt(0)
 for x in xs:a=add(a,x)
 return a
def root(x,up=False):
 assert x>=0;s=10**100;n=isqrt(x.numerator*s*s//x.denominator)
 if up and F(n*n,s*s)<x:n+=1
 r=F(n,s);assert r*r>=x if up else r*r<=x
 return r
def sqrtiv(x):
 assert x[0]>0;return root(x[0]),root(x[1],True)
def matrix(m):return [[iv(x) for x in row] for row in m]
def tr(a):return list(map(list,zip(*a)))
def mm(a,b):return [[total(mul(x,y) for x,y in zip(u,v)) for v in tr(b)] for u in a]
def plus(a,b):return [[add(x,y) for x,y in zip(u,v)] for u,v in zip(a,b)]
def minus(a,b):return [[sub(x,y) for x,y in zip(u,v)] for u,v in zip(a,b)]
def scale(a,c):return [[mul(x,pt(c)) for x in row] for row in a]
def inv2(a):
 d=sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]));assert d[0]>0
 return [[div(a[1][1],d),div(neg(a[0][1]),d)],[div(neg(a[1][0]),d),div(a[0][0],d)]]
def det2(a):return sub(mul(a[0][0],a[1][1]),mul(a[0][1],a[1][0]))
def positive2(a):
 assert a[0][0][0]>0 and sub(a[1][1],div(mul(a[0][1],a[1][0]),a[0][0]))[0]>0
def pmat(a):return [[pt(x) for x in row] for row in a]
def pmm(a,b):return [[sum(x*y for x,y in zip(u,v)) for v in tr(b)] for u in a]
def pa(a,b):return [[x+y for x,y in zip(u,v)] for u,v in zip(a,b)]
def ps(a,b):return [[x-y for x,y in zip(u,v)] for u,v in zip(a,b)]
def pc(a,c):return [[c*x for x in row] for row in a]
def pinv(a):
 n=len(a);m=[r[:]+[F(i==j) for j in range(n)] for i,r in enumerate(a)]
 for j in range(n):
  i=next(i for i in range(j,n) if m[i][j]);m[i],m[j]=m[j],m[i]
  m[j]=[x/m[j][j] for x in m[j]]
  for i in range(n):
   if i!=j:
    c=m[i][j];m[i]=[x-c*y for x,y in zip(m[i],m[j])]
 return [r[n:] for r in m]
def ppositive(a):
 assert a==tr(a)
 n=len(a);l=[[F(i==j) for j in range(n)] for i in range(n)];d=[]
 for j in range(n):
  p=a[j][j]-sum(l[j][k]**2*d[k] for k in range(j));assert p>0,('nonpositive pivot',j)
  d.append(p)
  for i in range(j+1,n):l[i][j]=(a[i][j]-sum(l[i][k]*l[j][k]*d[k] for k in range(j)))/p
 return d
def midpoint(m):return [[(F(x[0])+F(x[1]))/2 for x in row] for row in m]
def symmetric_midpoint(m):
 n=len(m);a=[[F(0)]*n for _ in range(n)]
 for i in range(n):
  for j in range(i,n):
   lo=max(F(m[i][j][0]),F(m[j][i][0]));hi=min(F(m[i][j][1]),F(m[j][i][1]));assert lo<=hi
   a[i][j]=a[j][i]=(lo+hi)/2
 return a
def inside(a,m,label=''):
 for i,row in enumerate(a):
  for j,x in enumerate(row):assert F(m[i][j][0])<=x<=F(m[i][j][1]),(label,i,j)
def interval_inside(a,m,label=''):
 for i,row in enumerate(a):
  for j,x in enumerate(row):assert F(m[i][j][0])<=x[0]<=x[1]<=F(m[i][j][1]),(label,i,j)
def chol2(a,det=None):
 first=sqrtiv(a[0][0]);off=div(a[1][0],first)
 last=sqrtiv(div(det,a[0][0]) if det is not None else sub(a[1][1],sq(off)))
 return [[first,pt(0)],[off,last]]
def linv(c):return [[div(pt(1),c[0][0]),pt(0)],[neg(div(c[1][0],mul(c[0][0],c[1][1]))),div(pt(1),c[1][1])]]
def rounded(x,up=False,digits=6):
 if not x:return '0'
 if x<0:return '-'+rounded(-x,not up,digits)
 e=0;y=x
 while y<1:y*=10;e-=1
 while y>=10:y/=10;e+=1
 s=10**(digits-1);z=y*s;k=z.numerator//z.denominator
 if up and F(k)<z:k+=1
 val=F(k,s)*F(10)**e;assert val>=x if up else val<=x
 return f'{k//s}.{k%s:0{digits-1}d}e{e:+d}'
def display(x):return [rounded(x[0]),rounded(x[1],True)]

def chop(x,digits=500):
 s=10**digits
 a=x[0]*s;b=x[1]*s
 lo=a.numerator//a.denominator;hi=-((-b.numerator)//b.denominator)
 return F(lo,s),F(hi,s)
def fine_sqrt(x):
 assert x[0]>0
 s=10**500
 lo=isqrt(x[0].numerator*s*s//x[0].denominator)
 hi=isqrt(x[1].numerator*s*s//x[1].denominator)
 if F(hi*hi,s*s)<x[1]:hi+=1
 return F(lo,s),F(hi,s)
def fine_chol(a):
 n=len(a);c=[[pt(0) for _ in range(n)] for _ in range(n)]
 for j in range(n):
  pivot=chop(sub(pt(a[j][j]),total(sq(c[j][k]) for k in range(j))))
  c[j][j]=fine_sqrt(pivot)
  for i in range(j+1,n):
   residual=chop(sub(pt(a[i][j]),total(mul(c[i][k],c[j][k]) for k in range(j))))
   c[i][j]=chop(div(residual,c[j][j]))
 return c
