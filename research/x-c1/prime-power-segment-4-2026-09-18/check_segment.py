#!/usr/bin/env python3
"""Finite prime-power segment engine with complete mixed infinite tails.

All proof decisions and displayed enclosures use integer/Fraction arithmetic.
The analytic domain and the meaning of the interval covers are in PROOF.md.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

SCALE = 10**200


def down(x):
    x = F(x)
    return F((x.numerator * SCALE) // x.denominator, SCALE)


def up(x):
    return -down(-F(x))


class I:
    """Directed intervals stored as integer multiples of 1/SCALE."""
    def __init__(self,lo,hi=None):
        low=F(lo);high=low if hi is None else F(hi)
        self._lo=(low.numerator*SCALE)//low.denominator
        self._hi=-((-high.numerator*SCALE)//high.denominator)
        assert self._lo<=self._hi
    @classmethod
    def raw(cls,lo,hi):
        obj=cls.__new__(cls);obj._lo=lo;obj._hi=hi
        assert lo<=hi
        return obj
    @property
    def lo(self):return F(self._lo,SCALE)
    @property
    def hi(self):return F(self._hi,SCALE)
    @staticmethod
    def of(x):return x if isinstance(x,I) else I(x)
    def __add__(self,other):
        o=I.of(other);return I.raw(self._lo+o._lo,self._hi+o._hi)
    __radd__=__add__
    def __neg__(self):return I.raw(-self._hi,-self._lo)
    def __sub__(self,other):return self+(-I.of(other))
    def __rsub__(self,other):return I.of(other)+(-self)
    def __mul__(self,other):
        o=I.of(other)
        v=[self._lo*o._lo,self._lo*o._hi,self._hi*o._lo,self._hi*o._hi]
        return I.raw(min(v)//SCALE,-((-max(v))//SCALE))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=I.of(other);assert o._lo>0 or o._hi<0
        inv=I.raw(SCALE*SCALE//o._hi,-((-SCALE*SCALE)//o._lo))
        return self*inv
    def __rtruediv__(self,other):return I.of(other)/self
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        v=I(1)
        for _ in range(n):v=v*self
        return v


def exp_pos(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= 4
    term = total = I(1)
    for k in range(1, 257):
        term = term*x/k
        total = total+term
    following = term*x/257
    tail = following/(1-x/258)
    return total + I(0, tail.hi)


def atanh(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= F(1, 2)
    term = x
    total = I(0)
    for k in range(256):
        total = total + term/(2*k+1)
        term = term*x*x
    tail = term/(513*(1-x*x))
    return total + I(0, tail.hi)


LOG2 = 2*atanh(I(F(1, 3)))


def log_point(x):
    assert x > 0
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    return 2*atanh(I((x-1)/(x+1))) + k*LOG2


def log(x):
    x = I.of(x)
    return I(log_point(x.lo).lo, log_point(x.hi).hi)


def atan(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= F(1, 2)
    term = x
    total = I(0)
    for k in range(256):
        total = total + ((-1)**k)*term/(2*k+1)
        term = term*x*x
    # 256 terms end negative; the next positive term bounds the remainder.
    return total + I(0, (term/513).hi)


PI = 16*atan(I(F(1, 5))) - 4*atan(I(F(1, 239)))


def gamma():
    # Euler-Maclaurin through B16; bound the periodic polynomial by
    # its coefficient l1 norm on [0,1]. Integral remainder C/(16 N^16).
    from math import comb
    bs=[F(1)]
    for n in range(1,17):
        bs.append(-sum((F(comb(n+1,k))*bs[k] for k in range(n)),F(0))/(n+1))
    n=10000
    harmonic=sum((I(F(1,k)) for k in range(1,n+1)),I(0))
    center=harmonic-log(I(n))-F(1,2*n)
    for k in range(1,9):center+=bs[2*k]/(2*k*n**(2*k))
    radius=sum((abs(comb(16,k)*bs[k]) for k in range(17)),F(0))/(16*n**16)
    return center+I(-radius,radius)


def H(s):
    q = 1/exp_pos(I.of(s)/2)
    r = (1-q)/(1+q)
    return log((1+q)/(1-q))/2 + PI/4 - atan(r)


def h(t):
    t = I.of(t)
    return (1/exp_pos(t/2))/(1-1/exp_pos(2*t))


def g(t):
    return h(t)-1/(2*I.of(t))


from math import factorial, comb, isqrt
from functools import lru_cache

def polyadd(p,q):
    return [(p[k] if k<len(p) else F(0))+(q[k] if k<len(q) else F(0)) for k in range(max(len(p),len(q)))]

def polymul(p,q):
    r=[F(0)]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):r[i+j]+=x*y
    return r

def polyval(p,x):
    v=I(0)
    for c in reversed(p):v=v*x+c
    return v

def integral(p):return sum((p[k]/(k+1) for k in range(0,len(p),2)),F(0))

@lru_cache(None)
def leg(n):
    if n==0:return [F(1)]
    if n==1:return [F(0),F(1)]
    return polyadd([F(0)]+[(2*n-1)*x/n for x in leg(n-1)],[-(n-1)*x/n for x in leg(n-2)])

@lru_cache(None)
def prod(i,j):return polymul(leg(i),leg(j))

@lru_cache(None)
def shiftedleg(n):return [F((-1)**(n+l)*factorial(n+l),factorial(l)**2*factorial(n-l)) for l in range(n+1)]

@lru_cache(None)
def tpoly(i,j):
    r=[F(0)]*(i+j+2)
    for k in range(i+1):
        ai=F((-1)**(i+k)*factorial(i+k),2**k*factorial(k)**2*factorial(i-k))
        for l in range(j+1):
            aj=F((-1)**(j+l)*factorial(j+l),2**l*factorial(l)**2*factorial(j-l))
            r[k+l+1]+=(-1)**j*ai*aj*F(factorial(k)*factorial(l),factorial(k+l+1))
    return r

def inverse_series(p,n):
    r=[1/p[0]]
    for k in range(1,n+1):r.append(-sum((p[j]*r[k-j] for j in range(1,min(k,len(p)-1)+1)),F(0))/p[0])
    return r

def kernel_polynomial(M):
    degree=max(128,M+2)
    if degree%2:degree+=1
    cs=[F(1,factorial(k)) if k%2==0 else F(0) for k in range(degree+1)]
    sn=[F(1,factorial(k+1)) if k%2==0 else F(0) for k in range(degree+1)]
    ic=inverse_series(cs,M); ins=inverse_series(sn,M+1)
    pg=[(ic[k]+ins[k+1])/4 for k in range(M+1)]
    xmax=F(5,6); err=F(0)
    for polynomial,denom,shift,fac in [(ic,cs,0,degree+2),(ins,sn,1,degree+3)]:
        residual=polymul(polynomial,denom); residual[0]-=1
        assert all(v==0 for v in residual[:len(polynomial)])
        finite=sum((abs(v)*xmax**(k-shift) for k,v in enumerate(residual) if v),F(0))
        tail=xmax**(degree+2-shift)/factorial(fac)/(1-xmax*xmax)
        norm=sum((abs(v)*xmax**k for k,v in enumerate(polynomial)),F(0))
        err+=(finite+norm*tail)/4
    return pg,err

def leg_integrate(p):
    r=[F(0)]*(len(p)+1)
    for n,v in enumerate(p):
        r[n+1]+=v/F(2*n+1)
        if n:r[n-1]-=v/F(2*n+1)
    return r

def kernel_columns(j,M):
    # f_jk(x)=1/2 integral |x-y|^k P_j(y)dy, in Legendre coordinates.
    cols=[[F(int(j==0))]]
    for k in range(1,M+1):
        p=([F(0)]*j+[F(1)]) if k==1 else [k*(k-1)*v for v in cols[k-2]]
        r=leg_integrate(leg_integrate(p))
        value=F(2**k*(-1)**j*factorial(k)**2,factorial(k-j)*factorial(k+j+1)) if k>=j else F(0)
        deriv=F(k*2**(k-1)*(-1)**j*factorial(k-1)**2,factorial(k-1-j)*factorial(k+j)) if k-1>=j else F(0)
        alpha=deriv-sum((v*n*(n+1)/2 for n,v in enumerate(r)),F(0))
        beta=value-sum(r,F(0))-alpha
        r[1]+=alpha;r[0]+=beta
        assert all(v==0 for n,v in enumerate(r) if n%2!=j%2)
        cols.append(r)
    return cols

def show(x):
    x=I.of(x);digits=24
    def dec(v,upper=False):
        n=-((-v.numerator*10**digits)//v.denominator) if upper else (v.numerator*10**digits)//v.denominator
        return ('-' if n<0 else '')+str(abs(n)//10**digits)+'.'+str(abs(n)%10**digits).zfill(digits)
    return [dec(x.lo),dec(x.hi,True)]

REPORT={'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN','checks':[], 'values':{}}
LOG=[]
def record(name,value):
    value=I.of(value)
    REPORT['values'][name]={'lo':str(value.lo),'hi':str(value.hi),'outward_decimal':show(value)}
    LOG.append(name+' '+str(show(value)))
def check(name,condition):
    assert condition,name
    REPORT['checks'].append(name);LOG.append('PASS '+name)
def progress(s):print(s,flush=True)

def factor(m):
    n=len(m); low=[[I(0) for _ in range(n)] for _ in range(n)];piv=[]
    for i in range(n):
        low[i][i]=I(1)
        d=m[i][i]-sum((low[i][k]**2*piv[k] for k in range(i)),I(0))
        if d.lo<=0:return low,piv,{'index':i,'lo':str(d.lo),'hi':str(d.hi),'display':show(d)}
        piv.append(d)
        for j in range(i+1,n):low[j][i]=(m[j][i]-sum((low[j][k]*low[i][k]*piv[k] for k in range(i)),I(0)))/d
    return low,piv,None

def inverse_trace_bound(m,ix):
    low,piv,failure=factor(m)
    if failure:return None,low,piv,failure
    n=len(ix);trace=I(0)
    for k in range(n):
        col=[I(0)]*n
        for i in range(k,n):col[i]=int(i==k)-sum((low[i][j]*col[j] for j in range(k,i)),I(0))
        trace+=sum((col[i]**2/piv[i] for i in range(k,n)),I(0))/(2*ix[k]+1)
    return I(1/trace.hi),low,piv,None

def sqrt_enclosure(n):
    if isqrt(n)**2==n:return I(isqrt(n))
    k=isqrt(n*SCALE*SCALE);return I(F(k,SCALE),F(k+1,SCALE))

def channels(endpoint):
    out=[]
    for q in range(2,endpoint):
        p=next((d for d in range(2,isqrt(q)+1) if q%d==0),q)
        r=q;k=0
        while r%p==0:r//=p;k+=1
        if r!=1:continue
        lp=log(I(p));ell=k*lp;w=lp/sqrt_enclosure(q)
        m=1
        while q**m<endpoint:m+=1
        norm=I(0) if m==1 else I(1) if m==2 else sqrt_enclosure(2) if m==3 else I(2)
        out.append({'q':q,'prime':p,'exponent':k,'ell':ell,'weight':w,'norm':norm,'chain':m})
    return out

def v_moments(b,nmax):
    if b.lo==b.hi==1:return [I(0)]*(nmax+1)
    assert 0<=b.lo<=b.hi<1
    hp=F(0);ps=I(0);ao=F(0);az=I(0);power=I(1);out=[]
    lm=log(1-b);lp=log(1+b)
    for m in range(1,nmax+2):
        power*=b;hp+=F(1,m);ps+=power/m;ao=-ao+F(1,m);az=-az+power/m
        minus=(hp-ps-(1-power)*lm)/m
        plus=((1-(-1)**m)*LOG2-ao-(power-(-1)**m)*lp+az)/m
        out.append((minus-plus)/2)
    return out

def translated_legs(shift,N):
    out=[[I(1)],[shift,I(1)]]
    for n in range(2,N+1):
        p=out[-1];r=[I(0)]*(n+1)
        for k,v in enumerate(p):r[k]+=(2*n-1)*shift*v/n;r[k+1]+=(2*n-1)*v/n
        for k,v in enumerate(out[-2]):r[k]-=(n-1)*v/n
        out.append(r)
    return out[:N+1]

def source_trial(label,parity,N,Q,moment,L,eps):
    # A true H1_0, exact-Mellin trial source. Inverse iteration ONLY
    # selects rational coefficients; the concluding Rayleigh enclosure
    # is a direct interval evaluation, not an eigenvalue proof.
    def mulx(p):
        r={}
        for n,v in p.items():
            r[n+1]=r.get(n+1,F(0))+v*F(n+1,2*n+1)
            if n:r[n-1]=r.get(n-1,F(0))+v*F(n,2*n+1)
        return r
    def hn(n):
        r={k:-v for k,v in mulx(mulx({n:F(1)})).items()}
        r[n]=r.get(n,F(0))+1
        return r
    def mom(p):return sum((v*moment(n,parity) for n,v in p.items()),I(0))
    base=hn(parity);denom=mom(base);degrees=list(range(parity+2,N-1,2));basis=[]
    for n in degrees:
        p={k:I(v) for k,v in hn(n).items()};ratio=mom(hn(n))/denom
        for k,v in base.items():p[k]=p.get(k,I(0))-ratio*v
        basis.append(p)
    energy=[];norms=[]
    for p in basis:
        energy.append([sum((v*w*Q(i,j) for i,v in p.items() for j,w in q.items()),I(0)) for q in basis])
        norms.append([sum((v*q.get(i,I(0))/(2*i+1) for i,v in p.items()),I(0)) for q in basis])
    low,piv,failure=factor(energy)
    if failure:return
    n=len(degrees);v=[F(int(k==0)) for k in range(n)]
    for iteration in range(4):
        rhs=[sum((norms[i][j]*v[j] for j in range(n)),I(0)) for i in range(n)]
        f=[]
        for i in range(n):f.append(rhs[i]-sum((low[i][j]*f[j] for j in range(i)),I(0)))
        z=[I(0)]*n
        for i in range(n-1,-1,-1):z[i]=f[i]/piv[i]-sum((low[j][i]*z[j] for j in range(i+1,n)),I(0))
        mid=[(x.lo+x.hi)/2 for x in z];scale=max(abs(x) for x in mid)
        v=[F((x/scale*10**60).__floor__(),10**60) for x in mid]
    en=sum((v[i]*v[j]*energy[i][j] for i in range(n) for j in range(n)),I(0))
    no=sum((v[i]*v[j]*norms[i][j] for i in range(n) for j in range(n)),I(0))
    assert no.lo>0
    ray=en/no+I(-(L*eps).hi,(L*eps).hi)
    record(label+'_actual_H1_Mellin_trial_Rayleigh',ray)
    REPORT.setdefault('source_trials',{})[label]={'degrees':degrees,'coefficients':[str(x) for x in v],
        'basis':'h_n - <h_n,m>/<h_j,m> h_j; h_n=(1-x^2)P_n; exact endpoint moment m',
        'meaning':'Rayleigh enclosure for one actual H1_0 source; upper bound on optimal source coercivity, not a lower bound on it'}

def shift_grams(ch,a,N):
    # Partition the positive half interval at EVERY entry/exit of every
    # signed shift. Summing actions before squaring retains all cross terms.
    breaks=[I(0),I(1)];actions=[]
    for c in ch:
        d=c['ell']/a
        for sign in (-1,1):
            s=sign*d;actions.append((s,c['weight'],translated_legs(s,N)))
            for edge in (-1,1):
                b=edge-s
                if b.lo>0 and b.hi<1:breaks.append(b)
                else:assert b.hi<=0 or b.lo>=1
    breaks.sort(key=lambda b:b.lo+b.hi)
    for i in range(len(breaks)-1):assert breaks[i].hi<breaks[i+1].lo
    sq=[[I(0) for j in range(N+1)] for i in range(N+1)]
    vs=[[I(0) for j in range(N+1)] for i in range(N+1)]
    for cell,(l,hb) in enumerate(zip(breaks,breaks[1:])):
        progress('analytic shift band '+str(cell+1)+'/'+str(len(breaks)-1))
        mid=I((l.hi+hb.lo)/2);active=[]
        for s,w,p in actions:
            if -1<(mid+s).lo and (mid+s).hi<1:active.append((w,p))
            else:assert (mid+s).hi<-1 or (mid+s).lo>1
        act=[[sum((w*p[j][k] for w,p in active),I(0)) for k in range(j+1)] for j in range(N+1)]
        plain=[];lp=hp=I(1)
        for k in range(2*N+1):lp*=l;hp*=hb;plain.append((hp-lp)/(k+1))
        vl=v_moments(l,2*N);vh=v_moments(hb,2*N);v=[x-y for x,y in zip(vl,vh)]
        for j in range(N+1):
            pcol=[sum((x*plain[r+s] for s,x in enumerate(act[j])),I(0)) for r in range(N+1)]
            vcol=[sum((x*v[r+s] for s,x in enumerate(act[j])),I(0)) for r in range(N+1)]
            for i in range(j%2,N+1,2):
                sq[i][j]+=sum((x*pcol[r] for r,x in enumerate(act[i])),I(0))
                vs[i][j]+=sum((x*vcol[r] for r,x in enumerate(leg(i))),I(0))
    return sq,vs,breaks

def run(endpoint=5,N=63,M=64):
    progress('constants and exact Gamma model')
    a=log(I(endpoint))/2;L=2*a;ch=channels(endpoint)
    q0=-log(2*PI*a)-gamma();c=g(L);pg,eps=kernel_polynomial(M)
    check('endpoint range for uniform Gamma model',0<L.lo<L.hi<F(5,3))
    check('active prime powers 2,3,4 with von Mangoldt weights',[(v['q'],v['prime'],v['exponent']) for v in ch]==[(2,2,1),(3,3,1),(4,2,2)])
    check('positive decreasing regular Gamma floor',0<c.lo<c.hi<F(1,4))
    record('endpoint_a',a);record('q0',q0);record('uniform_Gamma_error',eps)
    snorm=sum((c['weight']*c['norm'] for c in ch),I(0))
    record('joint_shift_operator_norm_upper',snorm)
    check('kernel and shift norms used for moment reconstruction',(L*(F(1,4)+eps)).hi<1 and snorm.hi<2)
    kcols=[];powers=[L*(a/2)**k*pg[k] for k in range(M+1)]
    for j in range(N+1):
        cols=kernel_columns(j,M);out=[I(0)]*(N+M+2)
        for k,pol in enumerate(cols):
            if not pg[k]:continue
            for n,v in enumerate(pol):
                if v:out[n]+=powers[k]*v
        kcols.append(out)
    progress('full Gamma columns ready')
    @lru_cache(None)
    def G(i,j):
        if i>j:return G(j,i)
        return kcols[i][j]/(2*j+1) if j<len(kcols[i]) else I(0)
    @lru_cache(None)
    def lm(r):return (sum((F(1,2*k+1) for k in range(r+1)),F(0))-LOG2)/(2*r+1)
    @lru_cache(None)
    def lm2(r):
        odd=sum((F(1,2*k+1) for k in range(r+1)),F(0));odd2=sum((F(1,(2*k+1)**2) for k in range(r+1)),F(0))
        return ((odd-LOG2)**2+odd2-PI**2/12)/(2*r+1)
    @lru_cache(None)
    def P(i,j):
        if i>j:return P(j,i)
        if (i+j)%2:return I(0)
        if i!=j:return I(F(1,(j-i)*(j+i+1)))
        return sum((v*lm(k//2) for k,v in enumerate(prod(i,j)) if k%2==0),I(0))
    @lru_cache(None)
    def P2(i,j):
        if i>j:return P2(j,i)
        return sum((v*lm2(k//2) for k,v in enumerate(prod(i,j)) if k%2==0),I(0))
    @lru_cache(None)
    def S(i,j):
        if i>j:return S(j,i)
        return sum((c['weight']*polyval(tpoly(i,j),2-c['ell']/a) for c in ch),I(0))
    sq,vs,breaks=shift_grams(ch,a,N)
    REPORT['band_breakpoints']=[{'lo':str(b.lo),'hi':str(b.hi)} for b in breaks]
    @lru_cache(None)
    def moment(n,parity):
        last=100+parity
        val=sum(((a/2)**k/F(factorial(k))*integral([F(0)]*k+leg(n)) for k in range(parity,last+1,2)),I(0))
        tail=(a/2)**(last+2)/factorial(last+2)/(1-(a/2)**2/((last+3)*(last+4)))
        return val+I(-tail.hi,tail.hi)
    harm=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(N+3)]
    @lru_cache(None)
    def Q(i,j):return (harm[i]+q0)/(2*i+1)*(i==j)+P(i,j)-G(i,j)-S(i,j)
    for j in (0,1):check('low basis Qnorm ingredient '+str(j),max(abs((harm[j]+q0).lo),abs((harm[j]+q0).hi))<4 and ((2*j+1)*P2(j,j)).hi<4)
    gaps=[];REPORT['obligations']=[]
    for parity in (0,1):
        label='even' if parity==0 else 'odd';progress(label+' complete tail Gram and moment congruence')
        source_trial(label,parity,N,Q,moment,L,eps)
        ix=list(range(2+parity,N+1,2));allix=list(range(parity,N+1,2));tail=ix[-1]+2
        beta=((a/2)**2/((2 if parity==0 else 6)*(1-(a/2)**2/(12 if parity==0 else 20))))**2
        rem=(a/2)**tail/factorial(tail)/(1-(a/2)**2/((tail+1)*(tail+2)))
        epsmoment=rem*(1 if parity==0 else 4/a);err=2*L*eps+80*epsmoment
        delta=harm[tail]+q0-L*(F(1,4)-c+eps)-snorm-err
        check(label+' moment bounds',0<beta.lo<=beta.hi<1 and epsmoment.hi<1)
        record(label+'_beta',beta);record(label+'_Gamma_form_error',2*L*eps)
        record(label+'_infinite_moment_form_error',80*epsmoment);record(label+'_total_form_error',err)
        record(label+'_tail_floor',delta)
        if delta.lo<=0:
            REPORT['obligations'].append({'parity':label,'stage':'positive tail floor','enclosure':show(delta)});continue
        check(label+' positive infinite-dimensional tail',delta.lo>0)
        @lru_cache(None)
        def ratio(i):return moment(i,parity)/moment(parity,parity)
        @lru_cache(None)
        def gramC(i,j):
            # Exact Gram of P_Y(V-Kp-S)P_i. V and S tails are infinite.
            value=P2(i,j)+sq[i][j]-vs[i][j]-vs[j][i]
            for k in allix:value-=(2*k+1)*(P(i,k)-S(i,k))*(P(k,j)-S(k,j))
            for k in range(tail,N+M+2,2):
                value+=(2*k+1)*(G(i,k)*G(k,j)-(P(i,k)-S(i,k))*G(k,j)-G(i,k)*(P(k,j)-S(k,j)))
            return value
        def changed(fun,i,j):return fun(i,j)-ratio(i)*fun(parity,j)-ratio(j)*fun(i,parity)+ratio(i)*ratio(j)*fun(parity,parity)
        mat=[[I(0) for _ in ix] for _ in ix];amat=[[I(0) for _ in ix] for _ in ix];gmat=[[I(0) for _ in ix] for _ in ix]
        trace=I(0);moment_cost_sq=F(0)
        for ii,i in enumerate(ix):
            progress(label+' Gram row '+str(ii+1)+'/'+str(len(ix)))
            for jj,j in enumerate(ix[:ii+1]):
                ga=F(1001,1000)*changed(gramC,i,j)+1001*err**2/(2*i+1)*(i==j)
                av=changed(Q,i,j);entry=av-err/(2*i+1)*(i==j)-ga/delta
                mat[ii][jj]=mat[jj][ii]=entry;amat[ii][jj]=amat[jj][ii]=av;gmat[ii][jj]=gmat[jj][ii]=ga
                if i==j:trace+=(2*i+1)*ga
                cost=av-Q(i,j)
                moment_cost_sq+=(1 if i==j else 2)*(2*i+1)*(2*j+1)*max(abs(cost.lo),abs(cost.hi))**2
        record(label+'_finite_Mellin_correction_HS_squared_upper',moment_cost_sq)
        record(label+'_coupling_HS_squared',trace);record(label+'_Schur_deduction_operator_upper',trace/delta)
        record(label+'_shear_increment_squared_upper',trace/delta**2)
        abound,_,_,afail=inverse_trace_bound(amat,ix)
        if abound is not None:record(label+'_finite_Mellin_block_reserve_lower',abound)
        bound,low,piv,failure=inverse_trace_bound(mat,ix)
        for k,v in enumerate(piv):record(label+'_Schur_LDL_pivot_'+str(ix[k]),v)
        if failure:
            # A failed lower pivot alone is only undecided. Try a rational
            # test vector for the comparison matrix, never for q itself.
            f=len(piv);z=[I(0)]*(f+1);z[f]=I(1)
            for k in range(f-1,-1,-1):z[k]=-sum((low[r][k]*z[r] for r in range(k+1,f+1)),I(0))
            v=[(x.lo+x.hi)/2 for x in z]
            size=max(abs(x) for x in v);v=[F((x/size*10**80).__floor__(),10**80) for x in v]
            ray=sum((v[i]*v[j]*mat[i][j] for i in range(f+1) for j in range(f+1)),I(0))
            norm=sum((v[i]**2/F(2*ix[i]+1) for i in range(f+1)),F(0))
            record(label+'_failed_comparison_direction_Rayleigh',ray/norm)
            REPORT['obligations'].append({'parity':label,'stage':'finite comparison Schur positivity','failure':failure,
                'comparison_vector_coefficients':[str(x) for x in v],
                'comparison_vector_degrees':ix[:f+1],
                'negative_comparison_certified':ray.hi<0})
            progress(label+' comparison Schur UNDECIDED at '+str(failure['index']));continue
        check(label+' actual Schur positive via all rational LDL pivots',len(piv)==len(ix))
        record(label+'_Schur_inverse_trace_reserve_lower',bound)
        shear=trace/delta**2;k=isqrt((shear.hi.numerator*10**12)//shear.hi.denominator)+1;sqrtupper=F(k,10**6)
        assert sqrtupper**2>shear.hi
        inverse=(1+sqrtupper)**2;eta=I(min(bound.lo,delta.lo))/inverse;gap=eta/(1+beta)
        record(label+'_inverse_shear_norm_squared_upper',inverse);record(label+'_back_transformed_gap_lower',eta)
        record(label+'_final_normalized_gap_lower',gap);gaps.append(gap.lo)
        check(label+' entire numerator divided by 1+beta',gap.lo>0)
    verdict='CLOSED' if len(gaps)==2 else 'UNDECIDED'
    uniform=F(0)
    if verdict=='CLOSED':
        uniform=F(1)
        while uniform>=min(gaps):uniform/=10
        check('strict uniform source gap at full macro endpoint',uniform>0 and uniform<min(gaps))
    REPORT.update({'verdict':verdict,'cutoff':N,'kernel_polynomial_degree':M,'endpoint':'log(5)/2',
        'uniform_window':'0 < a <= log(5)/2' if verdict=='CLOSED' else None,'uniform_gap':str(uniform),
        'arithmetic_grid':'1/10^200','interval_extension':'exact isometric zero extension','mellin_constraints':2,
        'channels':[{'q':c['q'],'prime':c['prime'],'exponent':c['exponent'],'chain_vertices':c['chain']} for c in ch],
        'check_count':len(REPORT['checks'])})
    LOG.append('TOTAL '+str(len(REPORT['checks']))+' checks PASS; verdict '+verdict)
    LOG.append('UNIFORM GAP '+str(uniform))
    return REPORT,'\n'.join(LOG)+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__);mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--write',action='store_true');mode.add_argument('--verify',action='store_true')
    args=parser.parse_args();root=Path(__file__).resolve().parent
    result,logtext=run();jsontext=json.dumps(result,indent=2,sort_keys=True)+'\n'
    files={'segment_results.json':jsontext,'segment_checks.log':logtext}
    if args.write:
        for name,content in files.items():(root/name).write_text(content,encoding='utf-8',newline='\n')
        payload=['PROOF.md','README.md','check_segment.py','segment_checks.log','segment_results.json']
        manifest=''.join(hashlib.sha256((root/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in payload)
        (root/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')
    if args.verify:
        for name,content in files.items():assert (root/name).read_bytes()==content.encode('utf-8'),name+' replay mismatch'
        entries=(root/'SHA256SUMS').read_text(encoding='ascii').splitlines();assert len(entries)==5
        for entry in entries:
            digest,name=entry.split('  ',1);assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name+' hash mismatch'
        print('REPLAY and all five SHA256 payload hashes PASS')
    print(logtext,end='')

if __name__=='__main__':main()
