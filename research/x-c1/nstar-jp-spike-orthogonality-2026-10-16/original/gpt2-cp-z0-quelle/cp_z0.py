"""Directed elementary representative of C_sigma z0 modulo the Mellin carrier.

All interval decisions use integers/rationals. No quadrature is used here.
The representative is NOT the moment-projected C_sigma z0 pointwise.
"""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent/'vendor'))
import source_core as sc
sc.DIGITS=120;sc.S=10**120
I=sc.I
CHANNELS=[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
def need(ok,label):
    if not ok:raise AssertionError(label)
@lru_cache(None)
def exp_point(q):
    q=F(q)
    if q<0:return 1/exp_point(-q)
    need(q<=6,'exponential range at most 6')
    t=s=I(1)
    for n in range(1,257):
        t=t*q/n;s+=t
    nxt=t*q/257
    tail=nxt/(1-q/F(258))
    return s+I.raw(0,tail.hi)
def exp(x):
    x=I(x);a=exp_point(F(x.lo,sc.S));b=exp_point(F(x.hi,sc.S))
    return I.raw(a.lo,b.hi)
def moment(x,sigma):
    e=exp(I(x)/2);return (e+(-1)**sigma/e)/2
def atan_v(v):
    """atan(v) for 1/4<v<=1, via pi/4+atan((v-1)/(v+1))."""
    v=I(v);need(v.lo>I(F(1,4)).hi and v.hi<=I(1).hi,'atan reduction range')
    t=(v-1)/(v+1);t2=t*t;power=t;value=I(0)
    for j in range(512):
        value+=((-1)**j)*power/(2*j+1);power*=t2
    rho=t.absolute();tail=rho**1025/(1025*(1-rho*rho))
    return sc.pi()/4+value.inflate(F(tail.hi,sc.S))
def theta(r):
    """Exact tail integral int_r^infinity k(t)dt, r>0."""
    r=I(r);need(r.lo>0,'positive tail lower endpoint')
    v=exp(-r/2)
    return (sc.log(1+v)-sc.log(1-v))/2+atan_v(v)
def j_plus(r):
    r=I(r);need(r.lo>0,'positive J+ argument')
    return 3*sc.log2()/2+sc.pi()/4-r-sc.log(1-exp(-2*r))/2
def j_minus(r):
    r=I(r);need(r.lo>0,'positive J- argument')
    v=exp(-r)
    return sc.log2()/2+sc.pi()/4-(sc.log(1-v)-sc.log(1+v))/2
@lru_cache(None)
def geometry(sigma):
    need(sigma in (0,1),'parity')
    a=sc.log_point(3);b=sc.log_point(11)/2;h=b-a
    mu=(I(F(4,3))+(-1)**sigma*a)/2
    ea=I(3).sqrt();eb=I(11).sqrt().sqrt()
    # Integral of cosh or sinh(x/2) on the new shell.
    ell=(eb-(-1)**sigma/eb)-(ea-(-1)**sigma/ea)
    amp=1/(2*(h+ell*ell/mu)).sqrt()
    core=-amp*ell/mu
    shifts=[(q,sc.log_point(pr)/I(q).sqrt(),sc.log_point(q)) for q,pr in CHANNELS]
    norm=2*amp*amp*(h+ell*ell/mu)
    moment_total=core*mu+amp*ell
    need(norm.lo<=sc.S<=norm.hi and moment_total.contains_zero(),'normalization identities')
    return {'a':a,'b':b,'h':h,'mu':mu,'shell_moment_integral':ell,
            'shell_amplitude':amp,'core_amplitude':core,'shifts':shifts,
            'physical_norm_square_check':norm,'half_interval_moment_check':moment_total}
def lift_at(y,sigma):
    """Piecewise lift on a box wholly inside one support piece.

    Boxes crossing a discontinuity are rejected, never assigned one value.
    Values at the cuts themselves are immaterial in L2.
    """
    y=I(y);g=geometry(sigma);a,b=g['a'],g['b']
    if y.lo>-a.lo and y.hi<a.lo:return g['core_amplitude']*moment(y,sigma)
    if y.lo>a.hi and y.hi<b.lo:return g['shell_amplitude']
    if y.hi<-a.hi and y.lo>-b.lo:return (-1)**sigma*g['shell_amplitude']
    if y.lo>b.hi or y.hi<-b.hi:return I(0)
    raise ValueError('split the evaluation interval at a support/shift discontinuity')
def gamma_m_core(x,sigma):
    x=I(x);a=geometry(sigma)['a'];ep=exp(x/2)
    return (ep*(j_plus(a-x)+j_minus(a+x))
            +(-1)**sigma/ep*(j_minus(a-x)+j_plus(a+x)))/2
def raw_source(x,sigma):
    """Representative c_tilde with Pi_a c_tilde=C_sigma z0."""
    x=I(x);g=geometry(sigma);a,b=g['a'],g['b']
    need(x.lo>0 and x.hi<a.lo,'0<x<a; endpoints have separate one-sided conventions')
    eps=(-1)**sigma
    shell_kernel=theta(a-x)-theta(b-x)+eps*(theta(a+x)-theta(b+x))
    shifts=sum((w*(lift_at(x+d,sigma)+lift_at(x-d,sigma)) for q,w,d in g['shifts']),I(0))
    return g['core_amplitude']*gamma_m_core(x,sigma)-g['shell_amplitude']*shell_kernel-shifts
def log_coefficient(x,sigma):
    g=geometry(sigma)
    return (g['shell_amplitude']-g['core_amplitude']*moment(x,sigma))/2
def regular_part(x,sigma):
    g=geometry(sigma);x=I(x)
    return raw_source(x,sigma)-log_coefficient(x,sigma)*sc.log(g['a']-x)
def regular_left_limit(sigma):
    """Limit at a from below after subtracting g(x) log(a-x)."""
    g=geometry(sigma);a,b=g['a'],g['b'];eps=(-1)**sigma
    c0=sc.log2()+sc.pi()/4;ea=I(3).sqrt()
    gm=moment(a,sigma)*c0+(ea*j_minus(2*a)+eps/ea*j_plus(2*a))/2
    sk=c0-theta(b-a)+eps*(theta(2*a)-theta(a+b))
    # q=9 reaches the negative shell at x=a-; its endpoint convention matters.
    sp=sum((w*(g['core_amplitude']*moment(a-d,sigma) if q<9 else eps*g['shell_amplitude'])
            for q,w,d in g['shifts']),I(0))
    return g['core_amplitude']*gm-g['shell_amplitude']*sk-sp
def interior_cuts():
    """The twelve distinct prime discontinuities in (0,a), in exact log form."""
    g=geometry(0);a,b=g['a'],g['b'];cuts=[]
    # These explicit labels avoid identifying overlapping interval boxes as equal.
    for q in [2]:
        d=sc.log_point(q);cuts.extend([(f'a-log({q})',a-d),(f'b-log({q})',b-d)])
    cuts.append(('b-a',b-a))
    for q in [4,5,7,8]:
        d=sc.log_point(q);cuts.extend([(f'log({q})-a',d-a),(f'log({q})-b',d-b)])
    cuts.append(('2*a-b',2*a-b))
    cuts.sort(key=lambda item:item[1].lo)
    need(len(cuts)==12 and cuts[0][1].lo>0 and cuts[-1][1].hi<a.lo,'twelve interior cuts')
    need(all(cuts[i][1].hi<cuts[i+1][1].lo for i in range(11)),'strictly separated cuts')
    return cuts
