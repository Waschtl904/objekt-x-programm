#!/usr/bin/env python3
import sympy as sp

s, eps = sp.symbols("s eps", real=True)
log2,log3=sp.log(2),sp.log(3)
a=log2/2;b=log3/2;T=2*a;d=b-a;e=T-b;Delta=sp.simplify(d-e)
T0=T+eps
weights=[
 log2*2**sp.Rational(-3,2),log2*2**sp.Rational(-9,4),log2*2**sp.Rational(-3),
 log2*2**sp.Rational(-9,4),log2*2**sp.Rational(-3),log2*2**sp.Rational(-15,4),
 log2*2**sp.Rational(-3),log2*2**sp.Rational(-15,4),log2*2**sp.Rational(-9,2),
 log2/4,2*log3/(3*sp.sqrt(3))]
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11=weights
betam=sp.simplify(-c2-c4)
betab=sp.simplify(-c11)
alphab=sp.simplify(c1+c5+c11)

WORDS=[(1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),(6,T,3*a,a),
       (7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),(10,T,T,T),(11,b,b,b)]
SIGNS=(-1,1,1,-1)
V=[{s:0,eps:0},{s:0,eps:Delta},{s:Delta,eps:Delta}]

def vals(expr):
    return [sp.simplify(sp.expand(expr).subs(v)) for v in V]
def nn(expr):
    return all(v.is_nonnegative is True for v in vals(expr))
def pos(expr):
    expr=sp.expand(expr)
    return expr!=0 and nn(expr)
def absclass(expr,bound):
    if nn(bound-expr) and nn(bound+expr): return "IN"
    if pos(expr-bound) or pos(-expr-bound): return "OUT"
    return "MIX"
def profile(expr):
    if pos(expr): return sp.simplify(expr)
    if pos(-expr): return sp.simplify(-expr)
    if sp.simplify(expr)==0:return sp.Integer(0)
    raise AssertionError(("profile sign switch",expr,vals(expr)))
def aggregate(x):
    out={};count=0
    for j,delta,eta,lam in WORDS:
        gm=absclass(x-delta,T0-lam);gp=absclass(x+delta,T0-lam)
        assert gm!="MIX" and gp!="MIX",(x,j,gm,gp)
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for kk,(gate,q) in enumerate(zip(gates,src)):
            if gate=="OUT": continue
            hc=absclass(q,T0)
            assert hc!="MIX",(x,j,kk+1,hc,q,vals(q))
            if hc=="IN":
                p=profile(q)
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
                hit=i; break
        assert hit is not None,("missing",ek,got)
        rem.pop(hit)
    assert not rem,("extra",rem)

expected={
 e+s:{b-s:-c1,e+s:c1,a+e+s:c2},
 e-s:{b+s:-c1,e-s:c1,a+e-s:c2},
 d+s:{a+e-s:-c1,d+s:c1,b+s:c2},
 d-s:{a+e+s:-c1,d-s:c1,b-s:c2},
 b+s:{e-s:-c1,b+s:alphab,a+e-s:betam,d+s:c2,b-s:betab},
 b-s:{e+s:-c1,b-s:alphab,a+e+s:betam,d-s:c2,b+s:betab},
 a+e+s:{d-s:-c1,a+e+s:alphab,b-s:betam,e+s:c2,b+Delta-s:betab},
 a+e-s:{d+s:-c1,a+e-s:alphab,b+s:betam,e-s:c2,b+Delta+s:betab},
}
for x,exp in expected.items():
    got,n=aggregate(x)
    assert n in (3,8)
    assert_map(got,exp)

MB=sp.Matrix([
 [1+c1,0,c1,c2],
 [0,1+c1,c2,c1],
 [c1,c2,1+c1+c5+2*c11,2*c2],
 [c2,c1,2*c2,1+c1+c5+c11],
])
assert MB.is_positive_definite is True

A0=1+c1
p0=sp.simplify((c1**2+c2**2)/A0)
B0=sp.simplify(1+c1+c5+2*c11-p0)
C0=sp.simplify(1+c1+c5+c11-p0)
eta=sp.simplify(2*c2/A0)
S=sp.Matrix([[B0,eta],[eta,C0]])
assert S.is_positive_definite is True
detS=sp.simplify(S.det())
assert detS.is_positive is True
inv_off=sp.simplify(-eta/detS)
assert inv_off.is_negative is True
gammaB=sp.simplify(-c11*inv_off)
assert gammaB.is_positive is True
assert gammaB.is_zero is False

t=sp.simplify(Delta-s)
assert sp.simplify((e+s)-(d-t))==0
assert sp.simplify((a+e+s)-(b-t))==0

print("SW1-DELTA-DESCENT STAGE-8 POINTWISE CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("rows at e±s,d±s,b±s,(a+e)±s certified")
print("pointwise 4x4 B-difference block positive definite")
print("gamma_B>0 and nonzero")
print("J-reflection identities e+s=d-(Delta-s), a+e+s=b-(Delta-s) certified")
print("global L2 elimination remains open pending reflected-block audit")
