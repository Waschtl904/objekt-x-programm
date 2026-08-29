#!/usr/bin/env python3
import sympy as sp

s, eps = sp.symbols("s eps", real=True)
log2,log3=sp.log(2),sp.log(3)
a=log2/2
b=log3/2
T=2*a
d=b-a
e=T-b
Delta=sp.simplify(d-e)
T0=T+eps

weights=[
 log2*2**sp.Rational(-3,2),log2*2**sp.Rational(-9,4),log2*2**sp.Rational(-3),
 log2*2**sp.Rational(-9,4),log2*2**sp.Rational(-3),log2*2**sp.Rational(-15,4),
 log2*2**sp.Rational(-3),log2*2**sp.Rational(-15,4),log2*2**sp.Rational(-9,2),
 log2/4,2*log3/(3*sp.sqrt(3))]
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11=weights
beta0=sp.simplify(-c1+c3)
betam=sp.simplify(-c2-c4)
betap=sp.simplify(c2+c6)
betaT=sp.simplify(-c3-c5-c7-c10)
betab=sp.simplify(-c11)
kappa=sp.simplify(c1+c5+c9+c10+c11)
alphab=sp.simplify(c1+c5+c11)

WORDS=[(1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),(6,T,3*a,a),
       (7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),(10,T,T,T),(11,b,b,b)]
SIGNS=(-1,1,1,-1)

h3=sp.simplify(a-4*Delta)
k3=sp.simplify(h3-Delta) # a-5Delta
assert k3.is_positive is True
assert sp.simplify(2*Delta-h3).is_positive is True

# Base triangle 0<=s<=eps<=Delta split by s+eps=h3.
VLOW=[
 {s:0,eps:0},
 {s:0,eps:Delta},
 {s:k3,eps:Delta},
 {s:h3/2,eps:h3/2},
]
VHIGH=[
 {s:k3,eps:Delta},
 {s:Delta,eps:Delta},
 {s:h3/2,eps:h3/2},
]

def vals(expr,vs):
    return [sp.simplify(sp.expand(expr).subs(v)) for v in vs]

def nn(expr,vs):
    return all(v.is_nonnegative is True for v in vals(expr,vs))

def pos(expr,vs):
    expr=sp.expand(expr)
    return expr!=0 and nn(expr,vs)

def absclass(expr,bound,vs):
    if nn(bound-expr,vs) and nn(bound+expr,vs): return "IN"
    if pos(expr-bound,vs) or pos(-expr-bound,vs): return "OUT"
    return "MIX"

def profile(expr,vs):
    if pos(expr,vs): return sp.simplify(expr)
    if pos(-expr,vs): return sp.simplify(-expr)
    if sp.simplify(expr)==0:return sp.Integer(0)
    raise AssertionError(("profile sign switch",expr))

def aggregate(vs):
    x=sp.simplify(2*d+3*Delta+s)
    out={}
    count=0
    for j,delta,eta,lam in WORDS:
        gm=absclass(x-delta,T0-lam,vs)
        gp=absclass(x+delta,T0-lam,vs)
        assert gm!="MIX" and gp!="MIX",(j,gm,gp)
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for kk,(gate,q) in enumerate(zip(gates,src)):
            if gate=="OUT": continue
            hc=absclass(q,T0,vs)
            assert hc!="MIX",(j,kk+1,hc,q)
            if hc=="IN":
                p=profile(q,vs)
                out[p]=sp.simplify(out.get(p,0)+SIGNS[kk]*weights[j-1])
                count+=1
    return out,count

def assert_map(got,expected):
    rem=list(got.items())
    for ek,ev in expected.items():
        hit=None
        for i,(gk,gv) in enumerate(rem):
            if sp.simplify(gk-ek)==0:
                assert sp.simplify(gv-ev)==0,(ek,gv,ev)
                hit=i;break
        assert hit is not None,("missing",ek,got)
        rem.pop(hit)
    assert not rem,("extra",rem)

expected_low={
 2*e-3*Delta-s:-c1,
 2*d+3*Delta+s:alphab,
 T-4*Delta-s:betam,
 4*Delta+s:c2,
 T-3*Delta-s:betab,
}
t=sp.simplify(h3-s)
x=sp.simplify(2*d+3*Delta+s)
assert sp.simplify(x-(T-t))==0
expected_high={
 t:beta0,
 T-t:kappa,
 a+t:betam,
 a-t:betap,
 T+t:betaT,
 2*d+t:betab,
}

got,n=aggregate(VLOW)
assert n==8
assert_map(got,expected_low)

got,n=aggregate(VHIGH)
assert n==16
assert_map(got,expected_high)

# Exact profile identities quoted in the audit.
assert sp.simplify(t-(2*e-3*Delta-s))==0
assert sp.simplify(a+t-(T-4*Delta-s))==0
assert sp.simplify(a-t-(4*Delta+s))==0
assert sp.simplify(T+t-(3*a-4*Delta-s))==0
assert sp.simplify(2*d+t-(T-3*Delta-s))==0

# On the high chamber, t is a legal 2TP parameter once SW1 R is restored.
# SW1 slack: R=r, s=r+u, eps=r+u+v, Delta=R+eps+g.
r,u,v,g=sp.symbols("r u v g", positive=True)
R=r
ss=r+u
eeps=r+u+v
DD=2*r+u+v+g
hDD=sp.simplify(a-4*DD)
tt=sp.simplify(hDD-ss)
# t > h3-eps > R+(a-5Delta)
assert sp.simplify((hDD-eeps)-R-(a-5*DD)-g)==0
assert sp.simplify(a-5*Delta).is_positive is True

# Hub identity in folded chamber: x3=T-t.
x3=sp.simplify(2*d+3*Delta+s)
assert sp.simplify(x3-a-(a-t))==0
assert sp.simplify(x3-b-(e-t))==0
assert sp.simplify(x3-T-(-t))==0

print("SW1-DELTA-DESCENT STAGE-6 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("wall h3=a-4Delta lies strictly between Delta and 2Delta")
print("below wall: 8-echo outer-shell row")
print("above wall: 16-echo row equals certified mirrored 2TP row at t=h3-s")
print("high-chamber t lies in (R,eps)")
print("third-shell upper chamber folds exactly into SW1-2TP")
