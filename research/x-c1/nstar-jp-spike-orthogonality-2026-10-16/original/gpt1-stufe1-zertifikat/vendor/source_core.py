"""Source-derived arithmetic for the 764-entry A8/A9 mixed-form expansion.
Adaptation: 800 decimal fixed-point digits, 1000 logarithm-series terms.
No target positivity, spectral projectors, stored target inverses or new tails.
All numerical decisions use rational endpoints. Decimal is display only.
"""
from fractions import Fraction as F
from math import comb, factorial, isqrt
from functools import lru_cache
from decimal import Decimal, localcontext
import json, argparse
DIGITS=800
S=10**DIGITS

def ceildiv(a,b): return -((-a)//b)
class I:
    __slots__=('lo','hi')
    def __init__(self,x=0):
        if isinstance(x,I): self.lo,self.hi=x.lo,x.hi; return
        q=F(x); self.lo=q.numerator*S//q.denominator; self.hi=ceildiv(q.numerator*S,q.denominator)
    @classmethod
    def raw(cls,a,b):
        if a>b: raise ValueError('reversed interval')
        t=cls.__new__(cls);t.lo,t.hi=int(a),int(b);return t
    @classmethod
    def hull(cls,a,b): return cls.raw(min(I(a).lo,I(b).lo),max(I(a).hi,I(b).hi))
    def __add__(self,b): b=I(b);return I.raw(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I.raw(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I(b)
    def __rsub__(self,b):return I(b)+-self
    def __mul__(self,b):
        if isinstance(b,int):
            return I.raw(self.lo*b,self.hi*b) if b>=0 else I.raw(self.hi*b,self.lo*b)
        b=I(b);p=[self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi]
        return I.raw(min(p)//S,ceildiv(max(p),S))
    __rmul__=__mul__
    def __truediv__(self,b):
        if isinstance(b,int):
            if b==0:raise ZeroDivisionError()
            if b<0:return (-self)/(-b)
            return I.raw(self.lo//b,ceildiv(self.hi,b))
        b=I(b)
        if b.lo<=0<=b.hi:raise ZeroDivisionError('uncertified denominator')
        if b.hi<0:return (-self)/(-b)
        p=[F(self.lo*S,b.lo),F(self.lo*S,b.hi),F(self.hi*S,b.lo),F(self.hi*S,b.hi)]
        a,c=min(p),max(p)
        return I.raw(a.numerator//a.denominator,ceildiv(c.numerator,c.denominator))
    def __rtruediv__(self,b):return I(b)/self
    def __pow__(self,n):
        if n<0:return I(1)/(self**(-n))
        if n==0:return I(1)
        if n%2==0:
            v=self**(n//2);lo=0 if v.lo<=0<=v.hi else min(v.lo*v.lo,v.hi*v.hi)
            return I.raw(lo//S,ceildiv(max(v.lo*v.lo,v.hi*v.hi),S))
        return self*(self**(n-1))
    def sqrt(self):
        if self.lo<0:raise ValueError('negative sqrt lower endpoint')
        a=isqrt(self.lo*S);b=isqrt(self.hi*S)
        if b*b<self.hi*S:b+=1
        return I.raw(a,b)
    def absolute(self):return I.raw(0 if self.lo<=0<=self.hi else min(abs(self.lo),abs(self.hi)),max(abs(self.lo),abs(self.hi)))
    def intersects(self,b):b=I(b);return self.lo<=b.hi and b.lo<=self.hi
    def intersect(self,b):
        b=I(b)
        if not self.intersects(b):raise AssertionError('disjoint certified intervals')
        return I.raw(max(self.lo,b.lo),min(self.hi,b.hi))
    def inflate(self,e):e=I(e);return I.raw(self.lo-max(abs(e.lo),abs(e.hi)),self.hi+max(abs(e.lo),abs(e.hi)))
    def contains_zero(self):return self.lo<=0<=self.hi
    def frac(self):return [str(F(self.lo,S)),str(F(self.hi,S))]
    def display(self):
        with localcontext() as c:
            c.prec=25
            return [str(Decimal(self.lo)/Decimal(S)),str(Decimal(self.hi)/Decimal(S))]
    def __repr__(self):return repr(self.display())

def log_reduced(x):
    z=(x-1)/(x+1);z2=z*z;t=z;v=I(0)
    for k in range(1000):v+=t/(2*k+1);t*=z2
    tail=2*t/(2001*(1-z2));return (2*v)+I.raw(0,tail.hi)
@lru_cache(None)
def log2():return log_reduced(I(2))
def log_point(q):
    q=F(q)
    if q<=0:raise ValueError('log domain')
    k=0
    while q<1:q*=2;k-=1
    while q>2:q/=2;k+=1
    return log_reduced(I(q))+k*log2()
def log(x):
    x=I(x);a=log_point(F(x.lo,S));b=log_point(F(x.hi,S));return I.raw(a.lo,b.hi)
@lru_cache(None)
def pi():
    def atan(q):
        v=sum(((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(700)),F(0))
        nxt=q**1401/F(1401)
        return I.hull(v,v+nxt)
    return 16*atan(F(1,5))-4*atan(F(1,239))
@lru_cache(None)
def _bernoulli_table():
    a=[]; table=[]
    for m in range(385):
        a.append(F(1,m+1))
        for j in range(m,0,-1):a[j-1]=j*(a[j-1]-a[j])
        table.append(a[0])
    return table
def bernoulli(n):return _bernoulli_table()[n]
@lru_cache(None)
def euler():
    # DLMF 5.11.2 and 5.11(ii): positive-real remainder <= first omitted term.
    N=8192;m=192
    c=sum((F(1,k) for k in range(1,N+1)),F(0))-F(1,2*N)
    c+=sum((bernoulli(2*k)/F(2*k*N**(2*k)) for k in range(1,m)),F(0))
    err=abs(bernoulli(2*m))/F(2*m*N**(2*m))
    return (I(c)-log_point(N)).inflate(err)

def padd(a,b):return [(a[i] if i<len(a) else I(0))+(b[i] if i<len(b) else I(0)) for i in range(max(len(a),len(b)))]
def pscale(a,c):return [x*c for x in a]
def pmul(a,b):
    r=[I(0) for _ in range(len(a)+len(b)-1)]
    for i,x in enumerate(a):
        if x.lo==x.hi==0:continue
        for j,y in enumerate(b):
            if y.lo==y.hi==0:continue
            r[i+j]+=x*y
    return r

def pcompose(a,shift,scale):
    r=[I(0)];power=[I(1)]
    for v in a:r=padd(r,pscale(power,v));power=pmul(power,[I(shift),I(scale)])
    return r

def pint(a,l,r):return sum((v*(r**(k+1)-l**(k+1))/(k+1) for k,v in enumerate(a)),I(0))
def psymint(a,r):return sum((a[k]*r**(k+1)/(k+1) for k in range(0,len(a),2)),I(0))
_leg_table=[[F(1)],[F(0),F(1)]]
@lru_cache(None)
def leg(n):
    if n<0:raise ValueError('nonnegative Legendre degree required')
    while len(_leg_table)<=n:
        k=len(_leg_table)
        v=[F(0)]+[(2*k-1)*c/F(k) for c in _leg_table[-1]]
        for j,c in enumerate(_leg_table[-2]):v[j]-=F(k-1,k)*c
        _leg_table.append(v)
    return _leg_table[n]
def H(n):return sum((F(1,k) for k in range(1,n+1)),F(0))
def mellin(n,t):
    z=t/2;lead=I(1)
    for j in range(1,n+1):lead*=z/(2*j+1)
    v=term=I(1)
    for k in range(256):term*=z*z/(2*(k+1)*(2*n+2*k+3));v+=term
    nxt=term*z*z/(2*257*(2*n+515));ratio=z*z/(2*258*(2*n+517))
    return lead*(v+I.raw(0,(nxt/(1-ratio)).hi))

def profile(n,t):
    p=n%2;ratio=mellin(n,t)/mellin(p,t)
    lead=I(2*n+1).sqrt();normc=lead/I(2*p+1).sqrt()*ratio
    f=padd(pscale([I(x) for x in leg(n)],lead),pscale([I(x) for x in leg(p)],-lead*ratio))
    dh=padd(pscale([I(x) for x in leg(n)],lead*H(n)),pscale([I(x) for x in leg(p)],-lead*ratio*H(p)))
    return {'n':n,'f':f,'dh':dh,'norm':(1+normc**2).sqrt(),'ratio':ratio}

def potential_moment(n,r):
    if n%2:return I(0)
    if r.lo==r.hi==S:return (sum((F(1,2*k+1) for k in range(n//2+1)),F(0))-log2())/(n+1)
    atanh=(log(1+r)-log(1-r))/2
    t=sum((r**(2*k+1)/(2*k+1) for k in range(n//2+1)),I(0))
    return -(r**(n+1)*log(1-r*r)+2*(atanh-t))/(2*(n+1))
def potential_moment_series(n,r):
    if n%2:return I(0)
    K=768;r2=r*r;t=r**(n+3);v=I(0)
    for k in range(1,K+1):v+=t/(2*k*(n+2*k+1));t*=r2
    tail=t/(2*(K+1)*(n+2*K+3)*(1-r2))
    return v+I.raw(0,tail.hi)

def inverse_series(a,n):
    v=[F(1)]
    for k in range(1,n+1):v.append(-sum((a[j]*v[k-j] for j in range(1,k+1)),F(0)))
    return v

def convolution_q(a,b):
    v=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        if not x:continue
        for j,y in enumerate(b):
            if y:v[i+j]+=x*y
    return v
@lru_cache(None)
def gamma_polynomial(M):
    D=max(256,M+20);D+=D%2;r=F(11,10)
    c=[F(1,factorial(k)) if k%2==0 else F(0) for k in range(D+1)]
    s=[F(1,factorial(k+1)) if k%2==0 else F(0) for k in range(D+1)]
    pc=inverse_series(c,M);ps=inverse_series(s,M+1)
    rc=convolution_q(pc,c);rs=convolution_q(ps,s);rc[0]-=1;rs[0]-=1
    assert not any(rc[:M+1]) and not any(rs[:M+2])
    fc=sum((abs(v)*r**k for k,v in enumerate(rc)),F(0))
    fs=sum((abs(v)*r**(k-1) for k,v in enumerate(rs) if k),F(0))
    tc=r**(D+2)/F(factorial(D+2))/(1-r*r/F((D+3)*(D+4)))
    ts=r**(D+1)/F(factorial(D+3))/(1-r*r/F((D+4)*(D+5)))
    nc=sum((abs(v)*r**k for k,v in enumerate(pc)),F(0));ns=sum((abs(v)*r**k for k,v in enumerate(ps)),F(0))
    eps=(fc+fs+nc*tc+ns*ts)/4
    pg=[(pc[k]+ps[k+1])/4 for k in range(M+1)]
    return pg,eps

@lru_cache(None)
def abs_kernel_monomial(k,j):
    out=[F(0)]*(k+j+2)
    for m in range(j+1):
        t=k+m+1;factor=F(comb(j,m),t)
        for l in range(t+1):out[j-m+l]+=factor*comb(t,l)*((-1)**m+(-1)**l)
    return out

def gamma_direct(f,g,r,b,M):
    pg,eps=gamma_polynomial(M);value=I(0);power=I(1)
    for k,weight in enumerate(pg):
        if weight:
            v=[I(0)]
            for j,c in enumerate(g):
                if c.lo==c.hi==0:continue
                v=padd(v,pscale([I(x) for x in abs_kernel_monomial(k,j)],c))
            value+=b*I(weight)*power*psymint(pmul(f,v),r)
        power*=b/2
    return value

def corr_polynomial(f,g,r,edge):
    res=[I(0)]
    for i,fi in enumerate(f):
        if fi.lo==fi.hi==0:continue
        for j,gj in enumerate(g):
            if gj.lo==gj.hi==0:continue
            for m in range(j+1):
                h=i+m+1;factor=fi*gj*comb(j,m)/h
                upper=[r**h] if not edge else [I(comb(h,l)*(-1)**l) for l in range(h+1)]
                upper[0]-=(-r)**h
                pol=[I(0)]*(j-m)+pscale(upper,factor)
                res=padd(res,pol)
    return res

def gamma_correlation(f,g,r,b,M):
    pg,_=gamma_polynomial(M);part0=corr_polynomial(f,g,r,False);part1=corr_polynomial(f,g,r,True)
    mid=1-r;end=1+r;value=I(0);power=I(1)
    for k,w in enumerate(pg):
        if w:
            p0=[I(0)]*k+part0;p1=[I(0)]*k+part1
            value+=b*I(w)*power*(pint(p0,I(0),mid)+pint(p1,mid,end))
        power*=b/2
    return value

def endpoint_max(a,b):
    a,b=I(a),I(b)
    if a.lo>=b.hi:return a
    if b.lo>=a.hi:return b
    if a.lo==b.lo and a.hi==b.hi:return a
    raise AssertionError('uncertain shift cell order')
def endpoint_min(a,b):return -endpoint_max(-I(a),-I(b))

def shift_pair(f,g,r,d,reverse=False):
    result=I(0)
    for sign in (-1,1):
        t=sign*d;l=endpoint_max(-r,-1-t);h=endpoint_min(r,1-t)
        if h.hi<=l.lo:continue
        if l.hi>h.lo:raise AssertionError('uncertain empty overlap')
        if not reverse:part=pint(pmul(f,pcompose(g,t,1)),l,h)/2
        else:part=pint(pmul(pcompose(f,-t,1),g),l+t,h+t)/2
        result+=part
    return result

CHANNELS=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)]
def cross(n,m,a,b,M=128,alternate=False,same_horizon=False,channels=None):
    assert n%2==m%2
    r=I(1) if same_horizon else a/b
    ratio=I(1) if same_horizon else b/a
    pa=profile(n,a);pb=profile(m,b)
    f=pscale(pcompose(pa['f'],0,ratio),ratio.sqrt());g=pb['f']
    mass=psymint(pmul(f,g),r);dh=psymint(pmul(f,pb['dh']),r)
    potential=I(0)
    for k,v in enumerate(pmul(f,g)):
        mom=potential_moment_series(k,r) if alternate and r.hi<S else potential_moment(k,r)
        potential+=v*mom
    constant=(-(log(2*pi()*b))-euler())*mass
    gamma=(gamma_correlation if alternate else gamma_direct)(f,g,r,b,M)
    pg,eps=gamma_polynomial(M);error=2*b*I(eps)*pa['norm']*pb['norm'];gamma=gamma.inflate(error)
    channel_spec=CHANNELS if channels is None else channels
    channels={}
    for q,p in channel_spec:
        d=log_point(q)/b;w=log_point(p)/I(q).sqrt()
        channels[str(q)]=shift_pair(f,g,r,d,alternate)*w
    total=dh+potential+constant-gamma-sum(channels.values(),I(0))
    return {'n':n,'m':m,'mass':mass,'harmonic':dh,'potential':potential,'constant':constant,'regular_gamma':gamma,'gamma_error':error,'prime_channels':channels,'q':total}

def packed(row):
    def cv(x):
        if isinstance(x,I):return {'interval':x.frac(),'decimal':x.display()}
        if isinstance(x,dict):return {k:cv(v) for k,v in x.items()}
        return x
    return cv(row)

def run():
    a=3*log2()/2;b=log_point(3)
    assert a.hi<b.lo and b.hi<I(F(11,10)).lo
    assert gamma_polynomial(128)[1] < F(2738,10**24)
    rows=[];checks=[]
    for p in (0,1):
        for n in (2+p,4+p):
            for m in (2+p,4+p):
                one=cross(n,m,a,b);two=cross(n,m,a,b,alternate=True)
                for key in ['mass','harmonic','potential','constant','regular_gamma','q']:
                    assert one[key].intersects(two[key]),(n,m,key,one[key],two[key])
                for q in one['prime_channels']:assert one['prime_channels'][q].intersects(two['prime_channels'][q])
                assert F(one['q'].hi-one['q'].lo,S) < F(121,10**22)
                row=packed(one);row['alternate']=packed(two);row['certified_intersection']=packed(one['q'].intersect(two['q']))
                rows.append(row);checks.append(f'A8_A9_{n}_{m}: polynomial/correlation and shift reciprocity')
                print(n,m,one['q'], 'width',F(one['q'].hi-one['q'].lo,S),flush=True)
    return {'status':'PASS','scope':'Eight mixed form entries on first two corrected Legendre profiles in each parity; no full residual Gram, no new positivity.','scale_digits':DIGITS,'gamma_degree':128,'gamma_radius':'11/10','a':packed(a),'b':packed(b),'gamma_kernel_error':str(gamma_polynomial(128)[1]),'entries':rows,'checks':checks,'target_positivity_used':False,'full_cross_matrix_computed':False,'full_old_residual_computed':False,'forward_reserve_proved':False,'github_changed':False}
if __name__=='__main__':
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    p=argparse.ArgumentParser();p.add_argument('--out',required=True);args=p.parse_args()
    from pathlib import Path
    out=Path(args.out)
    if out.exists():raise FileExistsError(out)
    out.write_text(json.dumps(run(),indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
