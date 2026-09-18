#!/usr/bin/env python3
"""Prime-2/Prime-3 interval continuation with exact mixed shift tails.

All proof decisions and displayed enclosures use integer/Fraction arithmetic.
The analytic domain and the meaning of the interval covers are in PROOF.md.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

SCALE = 10**100


def down(x):
    x = F(x)
    return F((x.numerator * SCALE) // x.denominator, SCALE)


def up(x):
    return -down(-F(x))


class I:
    def __init__(self, lo, hi=None):
        self.lo = down(lo)
        self.hi = up(lo if hi is None else hi)
        assert self.lo <= self.hi

    @staticmethod
    def of(x):
        return x if isinstance(x, I) else I(x)

    def __add__(self, other):
        o = I.of(other)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-I.of(other))

    def __rsub__(self, other):
        return I.of(other) + (-self)

    def __mul__(self, other):
        o = I.of(other)
        v = [self.lo*o.lo, self.lo*o.hi, self.hi*o.lo, self.hi*o.hi]
        return I(min(v), max(v))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = I.of(other)
        assert o.lo > 0 or o.hi < 0
        return self * I(1/o.hi, 1/o.lo)

    def __rtruediv__(self, other):
        return I.of(other) / self

    def __pow__(self, n):
        assert isinstance(n, int) and n >= 0
        v = I(1)
        for _ in range(n):
            v = v*self
        return v


def exp_pos(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= 4
    term = total = I(1)
    for k in range(1, 129):
        term = term*x/k
        total = total+term
    following = term*x/129
    tail = following/(1-x/130)
    return total + I(0, tail.hi)


def atanh(x):
    x = I.of(x)
    assert 0 <= x.lo <= x.hi <= F(1, 2)
    term = x
    total = I(0)
    for k in range(128):
        total = total + term/(2*k+1)
        term = term*x*x
    tail = term/(257*(1-x*x))
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
    for k in range(128):
        total = total + ((-1)**k)*term/(2*k+1)
        term = term*x*x
    # 128 terms end negative; the next positive term bounds the remainder.
    return total + I(0, (term/257).hi)


PI = 16*atan(I(F(1, 5))) - 4*atan(I(F(1, 239)))


def gamma():
    # Euler-Maclaurin through B4, |periodic B4| <= 1/30.
    # Remainder radius <= integral_N^infinity |f^(4)(x)|/(30*24) dx
    # = 1/(120 N^4), for f(x)=1/x.
    n=10000
    harmonic=sum((I(F(1,k)) for k in range(1,n+1)),I(0))
    center=harmonic-log(I(n))-F(1,2*n)+F(1,12*n*n)-F(1,120*n**4)
    return center+I(-F(1,120*n**4),F(1,120*n**4))


def H(s):
    q = 1/exp_pos(I.of(s)/2)
    r = (1-q)/(1+q)
    return log((1+q)/(1-q))/2 + PI/4 - atan(r)


def h(t):
    t = I.of(t)
    return (1/exp_pos(t/2))/(1-1/exp_pos(2*t))


def g(t):
    return h(t)-1/(2*I.of(t))


class J:
    """Second-order interval jets in two real variables."""
    def __init__(self, v, d=None, hess=None):
        self.v = I.of(v)
        self.d = [I(0), I(0)] if d is None else d
        self.hess = [[I(0), I(0)], [I(0), I(0)]] if hess is None else hess

    @staticmethod
    def of(x):
        return x if isinstance(x, J) else J(x)

    @staticmethod
    def var(v, index):
        r = J(v)
        r.d[index] = I(1)
        return r

    def __add__(self, other):
        o = J.of(other)
        return J(self.v+o.v, [self.d[i]+o.d[i] for i in range(2)],
                 [[self.hess[i][j]+o.hess[i][j] for j in range(2)] for i in range(2)])

    __radd__ = __add__

    def __neg__(self):
        return J(-self.v, [-v for v in self.d], [[-v for v in row] for row in self.hess])

    def __sub__(self, other):
        return self+-J.of(other)

    def __rsub__(self, other):
        return J.of(other)+-self

    def __mul__(self, other):
        o = J.of(other)
        return J(self.v*o.v, [self.d[i]*o.v+self.v*o.d[i] for i in range(2)],
                 [[self.hess[i][j]*o.v+self.d[i]*o.d[j]+self.d[j]*o.d[i]+self.v*o.hess[i][j]
                   for j in range(2)] for i in range(2)])

    __rmul__ = __mul__

    def compose(self, val, first, second):
        return J(val, [first*v for v in self.d],
                 [[first*self.hess[i][j]+second*self.d[i]*self.d[j] for j in range(2)] for i in range(2)])

    def reciprocal(self):
        return self.compose(1/self.v, -1/(self.v**2), 2/(self.v**3))

    def __truediv__(self, other):
        return self*J.of(other).reciprocal()

    def __rtruediv__(self, other):
        return J.of(other)*self.reciprocal()

    def __pow__(self, n):
        r = J(1)
        for _ in range(n):
            r = r*self
        return r


def regular_g(t):
    # Cancellation-free g(t)=1/4[1/cosh(x)-x B(x)/(1+x^2 B(x))], x=t/2.
    # B(x)=sum_{k>=0} x^(2k)/(2k+3)!, including all derivative tails.
    from math import factorial
    x = I.of(t)/2
    assert 0 <= x.lo <= x.hi <= F(3, 4)
    jets = []
    for shift in (0, 3):
        vals = []
        for derivative in range(3):
            total = I(0)
            for k in range(17):
                power = 2*k
                if power < derivative:
                    continue
                coeff = F(factorial(power), factorial(power-derivative)*factorial(power+shift))
                total += coeff*x**(power-derivative)
            power = 34
            coeff = F(factorial(power), factorial(power-derivative)*factorial(power+shift))
            tail = coeff*I(x.hi)**(power-derivative)/(1-I(x.hi)**2)
            vals.append(total+I(0, tail.hi))
        jets.append(J(vals[0], [vals[1], I(0)], [[vals[2], I(0)], [I(0), I(0)]]))
    coshx, B = jets
    X = J.var(x, 0)
    result = (1/coshx-X*B/(1+X*X*B))/4
    return result.v, result.d[0]/2, result.hess[0][0]/4


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
    cs=[F(1,factorial(k)) if k%2==0 else F(0) for k in range(63)]
    sn=[F(1,factorial(k+1)) if k%2==0 else F(0) for k in range(63)]
    ic=inverse_series(cs,M); ins=inverse_series(sn,M+1)
    pg=[(ic[k]+ins[k+1])/4 for k in range(M+1)]
    xmax=F(3,4); err=F(0)
    for polynomial,denom,shift,fac in [(ic,cs,0,63),(ins,sn,1,64)]:
        residual=polymul(polynomial,denom); residual[0]-=1
        assert all(v==0 for v in residual[:len(polynomial)])
        finite=sum((abs(v)*xmax**(k-shift) for k,v in enumerate(residual) if v),F(0))
        # The denominator series was kept through power 62. Its next even
        # power is 64; bounding its factorial by 63! or 64! is conservative.
        tail=xmax**(64-shift)/factorial(fac)/(1-xmax*xmax)
        norm=sum((abs(v)*xmax**k for k,v in enumerate(polynomial)),F(0))
        err+=(finite+norm*tail)/4
    return pg,err

@lru_cache(None)
def kernel_on_poly(n,k):
    r=[F(0)]*(n+k+2)
    for l,bl in enumerate(shiftedleg(n)):
        r[k+l+1]+=bl*F(factorial(l)*factorial(k),factorial(k+l+1))
        for h in range(l+1):
            fac=bl*F(comb(l,h),k+h+1)
            for z in range(k+h+2):r[l-h+z]+=fac*comb(k+h+1,z)*(-1)**z
    return [v*2**k for v in r]

@lru_cache(None)
def kernel_entry(i,j,k):
    if i>j:return kernel_entry(j,i,k)
    if (k%2==0 and j>k) or j>i+k+1:return F(0)
    # Integrate each triangle by the beta integral before summing the
    # exact shifted-Legendre coefficients. No sampled kernel integrals.
    fac=[F(factorial(r)*factorial(k),factorial(r+k+1)) for r in range(j+1)]
    return 2**k*sum((x*y*(fac[r]+fac[s])/F(r+s+k+2)
                    for r,x in enumerate(shiftedleg(i))
                    for s,y in enumerate(shiftedleg(j))),F(0))


def show(x):
    x=I.of(x)
    def dec(v,upper=False):
        n=-((-v.numerator*10**12)//v.denominator) if upper else (v.numerator*10**12)//v.denominator
        return ('-' if n<0 else '')+str(abs(n)//10**12)+'.'+str(abs(n)%10**12).zfill(12)
    return [dec(x.lo),dec(x.hi,True)]

REPORT={'status':'AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN','checks':[], 'values':{}}
LOG=[]

def record(name,value):
    value=I.of(value)
    REPORT['values'][name]={'lo':str(value.lo),'hi':str(value.hi),'outward_decimal':show(value)}
    LOG.append(name+' '+str(show(value)))

def check(name,condition):
    assert condition,name
    REPORT['checks'].append(name)
    LOG.append('PASS '+name)

def ldlt(m):
    n=len(m); low=[[I(0) for _ in range(n)] for _ in range(n)]; piv=[]
    for i in range(n):
        low[i][i]=I(1)
        d=m[i][i]-sum((low[i][k]**2*piv[k] for k in range(i)),I(0))
        assert d.lo>0, ('finite Schur LDL pivot not positive',i,show(d))
        piv.append(d)
        for j in range(i+1,n):
            low[j][i]=(m[j][i]-sum((low[j][k]*low[i][k]*piv[k] for k in range(i)),I(0)))/d
    return piv

@lru_cache(None)
def cross_shift_poly(i,j):
    # <T_2 P_i,T_3 P_j> at a=log(2): d_2=1, u_3=2-d_3.
    r=[F(0)]*(i+j+2)
    for k,pik in enumerate(leg(i)):
        for l in range(j+1):
            aj=F((-1)**l*factorial(j+l),2**l*factorial(l)**2*factorial(j-l))
            r[k+l+1]+=pik*aj*F(factorial(k)*factorial(l),factorial(k+l+1))
    return r

def run():
    a=LOG2; L=2*a; ell=LOG2; ell3=log(I(3))
    def sq(n):
        k=isqrt(n*10**200);v=I(F(k,10**100),F(k+1,10**100))
        check('rational sqrt enclosure '+str(n),v.lo**2<n<v.hi**2)
        return v
    w=ell/sq(2); w3=ell3/sq(3); q0=-log(2*PI*a)-gamma(); c=g(L)
    pg,eps=kernel_polynomial(32); M=len(pg)-1; N=31
    u=2-ell3/a; b=1-u
    check('endpoint log2: shifts 2 and 3 active; shift 4 has zero overlap',1<L.lo<L.hi<F(3,2) and 0<u.lo<u.hi<1 and ell3.lo>a.hi)
    check('positive regular Gamma floor',0<c.lo<c.hi<F(1,4))
    check('uniform polynomial Gamma error < 1/10000000000',eps<F(1,10**10))
    record('endpoint_a_log2',a);record('log3',ell3);record('q0',q0);record('kernel_uniform_error_upper',eps)
    bounds=[]
    for cell in range(15):
        t=I(F(cell,10),F(cell+1,10));gv,gp,gpp=regular_g(t);v=gv+t*gp
        bounds.append(max(abs(v.lo),abs(v.hi)))
    check('15-cell bound sup |g+t gprime| < 1',max(bounds)<1)
    record('regular_kernel_derivative_absolute_upper',max(bounds))
    check('joint H1 form Lipschitz constant 13',F(8,3)+2+(F(1,2)*F(7,10)+F(2,3)*F(11,10))/F(3,8)**2<13 and ell.hi<F(7,10) and w.hi<F(1,2) and ell3.hi<F(11,10) and w3.hi<F(2,3))
    @lru_cache(None)
    def lm(r):return (sum((F(1,2*k+1) for k in range(r+1)),F(0))-ell)/(2*r+1)
    @lru_cache(None)
    def lm2(r):
        odd=sum((F(1,2*k+1) for k in range(r+1)),F(0));odd2=sum((F(1,(2*k+1)**2) for k in range(r+1)),F(0))
        return ((odd-ell)**2+odd2-PI**2/12)/(2*r+1)
    @lru_cache(None)
    def P(i,j):
        if i>j:return P(j,i)
        return sum((v*lm(k//2) for k,v in enumerate(prod(i,j)) if k%2==0),I(0))
    @lru_cache(None)
    def P2(i,j):
        if i>j:return P2(j,i)
        return sum((v*lm2(k//2) for k,v in enumerate(prod(i,j)) if k%2==0),I(0))
    @lru_cache(None)
    def G(i,j):
        if i>j:return G(j,i)
        return L*sum((pg[k]*(a/2)**k*kernel_entry(i,j,k) for k in range(M+1)),I(0))
    @lru_cache(None)
    def S(i,j):
        if i>j:return S(j,i)
        return w*polyval(tpoly(i,j),I(1))+w3*polyval(tpoly(i,j),u)
    @lru_cache(None)
    def Act3(i,j):
        p=prod(i,j);coeff=[F(0)]+[p[k]/(k+1) if k%2==0 else F(0) for k in range(len(p))]
        return F(1,2*i+1)*(i==j)-polyval(coeff,b)
    @lru_cache(None)
    def S2(i,j):
        return w*w*F(1,2*i+1)*(i==j)+w3*w3*Act3(i,j)+w*w3*(polyval(cross_shift_poly(i,j),u)+polyval(cross_shift_poly(j,i),u))
    @lru_cache(None)
    def v_band_moment(n,channel):
        z=I(0) if channel==2 else b
        degree=n+1;sgn=(-1)**degree
        hp=sum((F(1,k) for k in range(1,degree+1)),F(0))
        power_sum=sum((z**k/k for k in range(1,degree+1)),I(0))
        alt_one=sum((F((-1)**(degree-k),k) for k in range(1,degree+1)),F(0))
        alt_z=sum(((-1)**(degree-k)*z**k/k for k in range(1,degree+1)),I(0))
        minus=(hp-power_sum-(1-z**degree)*log(1-z))/degree
        plus=((1-sgn)*ell-alt_one-(z**degree-sgn)*log(1+z)+alt_z)/degree
        return (minus-plus)/2
    @lru_cache(None)
    def reflected_shift_poly(j,channel):
        d=I(1) if channel==2 else 2-u
        return [sum((pk*comb(l,k)*d**(l-k)*(-1)**k for l,pk in enumerate(leg(j)) if l>=k),I(0)) for k in range(j+1)]
    @lru_cache(None)
    def VS(i,j):
        total=I(0)
        for channel,weight in [(2,w),(3,w3)]:
            product=polymul(leg(i),reflected_shift_poly(j,channel))
            total+=weight*(-1)**i*sum((v*v_band_moment(k,channel) for k,v in enumerate(product)),I(0))
        return total
    @lru_cache(None)
    def moment(n,parity):
        last=80+parity
        val=sum(((a/2)**k/F(factorial(k))*integral([F(0)]*k+leg(n)) for k in range(parity,last+1,2)),I(0))
        tail=(a/2)**(last+2)/factorial(last+2)/(1-(a/2)**2/((last+3)*(last+4)))
        return val+I(-tail.hi,tail.hi)
    harm=[sum((F(1,k) for k in range(1,n+1)),F(0)) for n in range(N+3)]
    @lru_cache(None)
    def Q(i,j):return (harm[i]+q0)/(2*i+1)*(i==j)+P(i,j)-G(i,j)-S(i,j)
    check('entire polynomial Gamma kernel norm < 1',(L*(F(1,4)+eps)).hi<1)
    check('joint weighted adjacency norm < 2',(w+w3).hi<2)
    for j in (0,1):check('low basis Qnorm ingredient '+str(j),max(abs((harm[j]+q0).lo),abs((harm[j]+q0).hi))<4 and ((2*j+1)*P2(j,j)).hi<4)
    for parity in (0,1):
        ix=list(range(2+parity,N+1,2));allix=list(range(parity,N+1,2));tail=ix[-1]+2
        beta=((a/2)**2/((2 if parity==0 else 6)*(1-(a/2)**2/(12 if parity==0 else 20))))**2
        rem=(a/2)**tail/factorial(tail)/(1-(a/2)**2/((tail+1)*(tail+2)))
        epsmoment=rem*(1 if parity==0 else 4/a)
        err=2*L*eps+80*epsmoment # ||Q^p E_j|| < 9; conservative rank-one loss
        delta=harm[tail]+q0-L*(F(1,4)-c+eps)-w-w3-err
        label='even' if parity==0 else 'odd'
        check(label+' moment beta < 1',0<beta.lo<=beta.hi<1 and epsmoment.hi<1)
        check(label+' positive infinite-dimensional tail',delta.lo>F(1,2))
        record(label+'_moment_beta_upper',beta);record(label+'_moment_tail_norm_upper',epsmoment)
        record(label+'_total_bounded_form_error_upper',err);record(label+'_actual_tail_lower_bound',delta)
        @lru_cache(None)
        def ratio(i):return moment(i,parity)/moment(parity,parity)
        @lru_cache(None)
        def gramB(i,j):
            ep=P2(i,j)-sum(((2*k+1)*P(i,k)*P(k,j) for k in allix),I(0))
            for k in range(tail,N+M+2,2):ep+=(2*k+1)*(G(i,k)*G(k,j)-P(i,k)*G(k,j)-G(i,k)*P(k,j))
            return ep
        @lru_cache(None)
        def gramS(i,j):return S2(i,j)-sum(((2*k+1)*S(i,k)*S(k,j) for k in allix),I(0))
        @lru_cache(None)
        def gramBS(i,j):
            return VS(i,j)-sum(((2*k+1)*P(i,k)*S(k,j) for k in allix),I(0))-sum(((2*k+1)*G(i,k)*S(k,j) for k in range(tail,N+M+2,2)),I(0))
        @lru_cache(None)
        def gramC(i,j):return gramB(i,j)+gramS(i,j)-gramBS(i,j)-gramBS(j,i)
        def changed(fun,i,j):return fun(i,j)-ratio(i)*fun(parity,j)-ratio(j)*fun(i,parity)+ratio(i)*ratio(j)*fun(parity,parity)
        mat=[[I(0) for _ in ix] for _ in ix];trace=I(0);target=F(1,10**9)
        for ii,i in enumerate(ix):
            for jj,j in enumerate(ix[:ii+1]):
                gram=changed(gramC,i,j)
                gramactual=F(1001,1000)*gram+1001*err**2/(2*i+1)*(i==j)
                entry=changed(Q,i,j)-(err+target)/(2*i+1)*(i==j)-gramactual/delta
                mat[ii][jj]=mat[jj][ii]=entry
                if i==j:trace+=(2*i+1)*gramactual
        piv=ldlt(mat)
        check(label+' finite Schur LDL pivots positive',len(piv)==len(ix) and min(v.lo for v in piv)>0)
        for k,v in enumerate(piv):record(label+'_ldl_pivot_'+str(ix[k]),v)
        check(label+' actual Schur complement > 1/1000000000',target==F(1,10**9) and min(v.lo for v in piv)>0)
        check(label+' actual full shear increment squared < 16',trace.hi<16*delta.lo**2)
        record(label+'_actual_coupling_HS_squared_upper',trace);record(label+'_actual_shear_increment_squared_upper',trace/delta**2)
        eta=I(target)/25;gap=eta/(1+beta)
        check(label+' final division gives gap > 1/100000000000',gap.lo>F(1,10**11))
        record(label+'_back_transformed_gap_lower_bound',eta);record(label+'_normalized_source_gap_lower_bound',gap)
    REPORT.update({'cutoff':N,'kernel_polynomial_degree':M,'endpoint':'log(2)',
                   'uniform_window':'0 < a <= log(2)','uniform_gap':'1/100000000000',
                   'arithmetic_grid':'1/10^100','lipschitz_interval':'3/8 <= a,b <= log(2)',
                   'lipschitz_H1_form_constant':'13','interval_extension':'exact isometric zero extension',
                   'mellin_constraints':2,'check_count':len(REPORT['checks'])})
    LOG.append('TOTAL '+str(len(REPORT['checks']))+' checks PASS')
    LOG.append('UNIFORM Q_W[u] > ||u||_2^2 / 100000000000 for 0<a<=log(2)')
    return REPORT,'\n'.join(LOG)+'\n'

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group()
    mode.add_argument('--write',action='store_true'); mode.add_argument('--verify',action='store_true')
    args=parser.parse_args(); root=Path(__file__).resolve().parent
    result,logtext=run(); jsontext=json.dumps(result,indent=2,sort_keys=True)+'\n'
    files={'prime3_results.json':jsontext,'prime3_checks.log':logtext}
    if args.write:
        for name,content in files.items():(root/name).write_text(content,encoding='utf-8',newline='\n')
        payload=['PROOF.md','README.md','check_prime3.py','prime3_checks.log','prime3_results.json']
        manifest=''.join(hashlib.sha256((root/name).read_bytes()).hexdigest()+'  '+name+'\n' for name in payload)
        (root/'SHA256SUMS').write_text(manifest,encoding='ascii',newline='\n')
    if args.verify:
        for name,content in files.items():assert (root/name).read_bytes()==content.encode('utf-8'),name+' replay mismatch'
        entries=(root/'SHA256SUMS').read_text(encoding='ascii').splitlines()
        assert len(entries)==5
        for entry in entries:
            digest,name=entry.split('  ',1)
            assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name+' hash mismatch'
        print('REPLAY and all five SHA256 payload hashes PASS')
    print(logtext,end='')

if __name__=='__main__':main()
