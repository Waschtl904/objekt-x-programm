#!/usr/bin/env python3
import sympy as sp

s, eps = sp.symbols("s eps", real=True)
log2, log3 = sp.log(2), sp.log(3)
a=log2/2
b=log3/2
T=2*a
d=b-a
e=T-b
Delta=sp.simplify(d-e)
T0=T+eps

weights=[
 log2*2**sp.Rational(-3,2),
 log2*2**sp.Rational(-9,4),
 log2*2**sp.Rational(-3),
 log2*2**sp.Rational(-9,4),
 log2*2**sp.Rational(-3),
 log2*2**sp.Rational(-15,4),
 log2*2**sp.Rational(-3),
 log2*2**sp.Rational(-15,4),
 log2*2**sp.Rational(-9,2),
 log2/4,
 2*log3/(3*sp.sqrt(3)),
]
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11=weights
betam=sp.simplify(-c2-c4)
betab=sp.simplify(-c11)
alphab=sp.simplify(c1+c5+c11)

WORDS=[
 (1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),
 (6,T,3*a,a),(7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),
 (10,T,T,T),(11,b,b,b)
]
SIGNS=(-1,1,1,-1)

VERTS={
 "L":[{s:0,eps:0},{s:0,eps:Delta},{s:Delta/2,eps:Delta/2}],
 "U":[{s:0,eps:Delta},{s:Delta/2,eps:Delta/2},{s:Delta,eps:Delta}],
}

def vals(expr,vs):
    return [sp.simplify(sp.expand(expr).subs(v)) for v in vs]

def nn(expr,vs):
    return all(v.is_nonnegative is True for v in vals(expr,vs))

def pos(expr,vs):
    expr=sp.expand(expr)
    return expr!=0 and nn(expr,vs)

def absclass(expr,bound,vs):
    if nn(bound-expr,vs) and nn(bound+expr,vs):
        return "IN"
    if pos(expr-bound,vs) or pos(-expr-bound,vs):
        return "OUT"
    return "MIX"

def profile(expr,vs):
    if pos(expr,vs): return sp.simplify(expr)
    if pos(-expr,vs): return sp.simplify(-expr)
    if sp.simplify(expr)==0: return sp.Integer(0)
    raise AssertionError(("profile sign switch",expr))

def aggregate(case):
    vs=VERTS[case]
    x=sp.simplify(2*d+Delta+s)
    out={}
    count=0
    for j,delta,eta,lam in WORDS:
        gm=absclass(x-delta,T0-lam,vs)
        gp=absclass(x+delta,T0-lam,vs)
        assert gm!="MIX" and gp!="MIX"
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for k,(gate,q) in enumerate(zip(gates,src)):
            if gate=="OUT": continue
            hc=absclass(q,T0,vs)
            assert hc!="MIX"
            if hc=="IN":
                p=profile(q,vs)
                out[p]=sp.simplify(out.get(p,0)+SIGNS[k]*weights[j-1])
                count+=1
    return out,count

def assert_map(got,expected):
    rem=list(got.items())
    for ek,ev in expected.items():
        hit=None
        for i,(gk,gv) in enumerate(rem):
            if sp.simplify(gk-ek)==0:
                assert sp.simplify(gv-ev)==0,(ek,gv,ev)
                hit=i; break
        assert hit is not None,("missing",ek,got)
        rem.pop(hit)
    assert not rem,("extra",rem)

expected={
 2*e-Delta-s:-c1,
 2*d+Delta+s:alphab,
 T-2*Delta-s:betam,
 2*Delta+s:c2,
 T-Delta-s:betab,
}

for case in ("L","U"):
    got,n=aggregate(case)
    assert n==8
    assert_map(got,expected)

# Hub affine identities.
x=sp.simplify(2*d+Delta+s)
assert sp.simplify(x-a-(2*Delta+s))==0
assert sp.simplify(x-b-(-e+Delta+s))==0
assert sp.simplify(x-T-(-2*e+Delta+s))==0

# Fixed inequalities needed for signs/support.
assert sp.simplify(e-2*Delta).is_positive is True
assert sp.simplify(T-3*Delta).is_positive is True

# SW1 slack parametrization: R=r, s=r+u, eps=r+u+v, Delta=R+eps+g.
r,u,v,g,sigma=sp.symbols("r u v g sigma", positive=True)
R=r
ss=r+u
eeps=r+u+v
DD=2*r+u+v+g
assert sp.simplify(DD-(R+eeps)-g)==0
# e-Delta-s > R:
assert sp.simplify((e-DD-ss-R)-((e-2*DD)+(v+g)))==0
# 2e-Delta-s > R:
assert sp.simplify((2*e-DD-ss-R)-((2*e-2*DD)+(v+g)))==0
# first left branch 2Delta+s > R trivially:
assert sp.simplify((2*DD+ss)-R-(2*DD+u))==0
# all left branches are below T; in particular 2Delta+s<T because s<Delta:
assert sp.simplify(T-(2*DD+ss) - ((T-3*DD)+(DD-ss)))==0
# right a-branch is above S=T+sigma whenever sigma<=R<s.
# x+a = T+2Delta+s, so excess over T+sigma is 2Delta+s-sigma >0.

print("SW1-DELTA-DESCENT STAGE-5 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("first outer shell 2d+Delta+s: 8 echoes in both AWI chambers")
print("aggregated A-row DD.98 certified")
print("Hub source identities/support DD.99 certified")
print("no new J-switch on first outer shell")
