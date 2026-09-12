# -*- coding: utf-8 -*-
"""Hardened normalization gate for the finite Suzuki OX-GRAM identity.

Compared with the external reviewer checker, this closes the interval gaps used
as merge firewalls in PR #98:

1. the Bernoulli truncation for r1'' gets an explicit uniform tail ball;
2. the prime-power cutoff n<exp(2a) is decided only by Arb comparisons;
3. the logarithmic endpoint bound contains no float conversion.

The positive singular block is referred to as the logarithmic form / log|D|
geometry, not the classical H^{1/2}/Douglas seminorm.

Scope: a in {1/2,4/5,1}, Arb precision 256, Fourier cutoff Z=2000 by default.
No Registry promotion and no RH/Object-X claim.
"""
import sys, time
from flint import ctx, arb, acb
from fractions import Fraction
import sympy as sp

ctx.prec = 256
PI, C0, LOG2 = arb.pi(), arb.const_euler(), arb(2).log()
TWOAP1 = (2*arb.pi()).log() + C0

KC   = [Fraction(1,2), Fraction(1,1), Fraction(3,2)]
TYPE = ['c','s','c']
def kk(i,a): return PI*arb(KC[i].numerator)/arb(KC[i].denominator)/a


def vm_upto(X):
    """Prime powers n<X, with every inclusion/exclusion certified by Arb."""
    if not (X < arb(8)):
        raise RuntimeError("vm_upto hardening scope requires X<8 (a<=1)")
    primes=[]
    for p in range(2,17):
        if all(p % q for q in primes if q*q <= p):
            primes.append(p)
    out={}
    for p in primes:
        t=p
        while t<=16:
            tb=arb(t)
            if tb < X:
                out[t]=arb(p).log()
            elif tb > X:
                break
            else:
                raise RuntimeError(f"uncertified prime-power cutoff at n={t}, X={X}")
            t*=p
    return out


def _ic(m,c,lo,hi,mzero):
    if mzero: return (hi-lo)*c.cos()
    return ((m*hi+c).sin()-(m*lo+c).sin())/m

def _is(m,c,lo,hi,mzero):
    if mzero: return (hi-lo)*c.sin()
    return ((m*lo+c).cos()-(m*hi+c).cos())/m

def prodint(ti,ki,ci,tj,kj,cj,lo,hi,same):
    md,cd,ms,cs = ki-kj, ci-cj, ki+kj, ci+cj
    if ti=='c' and tj=='c': return (_ic(md,cd,lo,hi,same)+_ic(ms,cs,lo,hi,False))/2
    if ti=='s' and tj=='s': return (_ic(md,cd,lo,hi,same)-_ic(ms,cs,lo,hi,False))/2
    if ti=='s' and tj=='c': return (_is(ms,cs,lo,hi,False)+_is(md,cd,lo,hi,same))/2
    return (_is(ms,cs,lo,hi,False)-_is(md,cd,lo,hi,same))/2


def SHp(i,j,tau,a):
    ki,kj=acb(kk(i,a)),acb(kk(j,a))
    return prodint(TYPE[i],ki,acb(0),TYPE[j],kj,kj*tau,acb(-a),acb(a)-tau,i==j)

def SHm(i,j,tau,a):
    ki,kj=acb(kk(i,a)),acb(kk(j,a))
    return prodint(TYPE[i],ki,acb(0),TYPE[j],kj,-kj*tau,acb(-a)+tau,acb(a),i==j)

def IP(i,j,a): return SHp(i,j,acb(0),a).real


def log_form(i,j,a):
    ki,kj=acb(kk(i,a)),acb(kk(j,a)); ti,tj=TYPE[i],TYPE[j]; same=(i==j); Z=acb(0)
    def f(u,_):
        lo,hi=acb(-a)+u, acb(a)
        t  = prodint(ti,ki,Z,    tj,kj,Z,    lo,hi,same)
        t -= prodint(ti,ki,Z,    tj,kj,-kj*u,lo,hi,same)
        t -= prodint(ti,ki,-ki*u,tj,kj,Z,    lo,hi,same)
        t += prodint(ti,ki,-ki*u,tj,kj,-kj*u,lo,hi,same)
        return t/u
    d=arb(2)**(-45)
    v=acb.integral(f,acb(d),acb(2*a)).real
    err=(kk(i,a)*kk(j,a)*2*a)*d*d/2
    return (v+arb(0,err))/2


def Mterm(i,j,a):
    ki,kj=kk(i,a),kk(j,a); ti,tj=TYPE[i],TYPE[j]; e=arb(2)**(-34)
    def f(z,_):
        vi=(acb(ki)*z).cos() if ti=='c' else (acb(ki)*z).sin()
        vj=(acb(kj)*z).cos() if tj=='c' else (acb(kj)*z).sin()
        return (acb(a*a)-z*z).log()*vi*vj
    v=acb.integral(f,acb(-a+e),acb(a-e)).real
    B=2*ki*kj*e*e*(-(2*a*e).log()+1)
    return -(v+arb(0,B))/2

def L_real(i,j,a): return log_form(i,j,a)+Mterm(i,j,a)


def prime_blocks(i,j,a,W):
    Tr=arb(0); Aa=arb(0); P=arb(0); ip=IP(i,j,a)
    for n,lp in W.items():
        w=lp/arb(n).sqrt(); Aa+=2*w
        s=SHp(i,j,acb(arb(n).log()),a).real + SHm(i,j,acb(arb(n).log()),a).real
        Tr+=w*s; P+=w*(2*ip-s)
    return Tr,Aa,P


def R0(i,j,a):
    def mom(kind,t,k):
        f=lambda z,_:((z/2).cosh() if kind=='ch' else (z/2).sinh())*((acb(k)*z).cos() if t=='c' else (acb(k)*z).sin())
        return acb.integral(f,acb(-a),acb(a)).real
    Ci,Si=mom('ch',TYPE[i],kk(i,a)),mom('sh',TYPE[i],kk(i,a))
    Cj,Sj=mom('ch',TYPE[j],kk(j,a)),mom('sh',TYPE[j],kk(j,a))
    return -2*(Ci*Cj-Si*Sj)


NB=300; _B=[arb(0)]*(NB+1)
for n in range(1,NB+1):
    q=sp.Rational(sp.bernoulli(n,sp.Rational(1,4))); _B[n]=arb(int(q.p))/arb(int(q.q))
_RTAIL=(PI*PI/12)*(arb(2)/PI)**(NB+1)/(1-arb(2)/PI)


def r1pp_partial(u):
    tot=u*0; p=u**0; fact=arb(1); pw=arb(1)
    for n in range(1,NB+1):
        fact=fact*n; pw=pw*(-2); tot=tot+acb(_B[n]*pw/(2*fact))*p; p=p*u
    return tot


def R1(i,j,a):
    f=lambda u,_: r1pp_partial(u)*(SHp(i,j,u,a)+SHm(i,j,u,a))
    v=acb.integral(f,acb(0),acb(2*a)).real
    return v + arb(0,4*a*a*_RTAIL)


def SINC(w):
    # Either branch is a valid enclosure; the threshold only selects the numerically stable formula.
    if float(w.abs_upper())<0.35:
        t=w*w; s=acb(1); term=acb(1)
        for m in range(1,45): term=term*(-t)/((2*m)*(2*m+1)); s=s+term
        return s
    return w.sin()/w

def S(w,a): return acb(a)*SINC(w*acb(a))
def vhat(i,z,a):
    k=acb(kk(i,a))
    if TYPE[i]=='c': return S(k-z,a)+S(k+z,a)
    return acb(0,1)*(S(k-z,a)-S(k+z,a))
def Pij(i,j,z,a): return vhat(i,z,a)*vhat(j,-z,a)


def fint(W,i,j,a,Z,tailfun,logw=False):
    if (TYPE[i]=='c')!=(TYPE[j]=='c'): return arb(0)
    e=arb(2)**(-40)
    f=lambda z,_: W(z)*Pij(i,j,z,a)
    v=acb.integral(f,acb(e),acb(Z)).real/PI
    ki,kj=kk(i,a),kk(j,a)
    Wn = arb(3) if not logw else (abs(e.log())+3)
    near = arb(0, 4*a*a*e*Wn/PI)
    return v+arb(0,tailfun(Z,ki,kj))+near


def mk_tail(kind,extra=None):
    def t(Z,ki,kj):
        Z=arb(Z); kmax=ki if ki>kj else kj; B=4*ki*kj/PI/(1-kmax*kmax/(Z*Z))**2
        if kind=='one':  return B/(3*Z**3)
        if kind=='log':  return B*((Z.log())/3+arb(1)/9+C0/3)/Z**3
        if kind=='bnd':  return B*extra/(3*Z**3)
        if kind=='loglike': return B*(2*(Z.log())/3+arb(2)/9+arb(2)/3)/Z**3
        raise ValueError
    return t


def W_one(z): return acb(1)
def W_log(z): return z.log()+acb(C0)
def mk_Wprime(Wv):
    items=[(lp/arb(n).sqrt(), arb(n).log()) for n,lp in Wv.items()]
    def W(z):
        s=acb(0)
        for w,ln in items: s=s+acb(2*w)*(z*acb(ln)).cos()
        return s
    return W

def W_r0(z,a):
    T=acb(2*a); num=(T/2).sinh()*(z*T).cos()+2*(T/2).cosh()*z*(z*T).sin()
    return acb(-2)*num/(acb(0.25)+z*z)
def W_psi(z):
    return ((acb(0.25)+acb(0,1)*z/2).digamma()+(acb(0.25)-acb(0,1)*z/2).digamma())/2 - acb(PI.log())
def W_r1(z):
    rp=((acb(0.25)+acb(0,1)*z/2).digamma()+(acb(0.25)-acb(0,1)*z/2).digamma())/2
    return -rp+z.log()-acb(LOG2)


def fmt(x):
    try: return arb(x).str(14,radius=True)
    except Exception: return str(x)
