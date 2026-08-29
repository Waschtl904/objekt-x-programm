#!/usr/bin/env python3
import sympy as sp

u, eps = sp.symbols("u eps", real=True)
L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b
Delta=sp.simplify(d-e); T0=T+eps
C=sp.simplify(a+e)
hB=sp.simplify(e-Delta)

c1=L2*2**sp.Rational(-3,2)
c2=L2*2**sp.Rational(-9,4)
c3=L2*2**sp.Rational(-3)
c4=c2
c5=L2*2**sp.Rational(-3)
c6=L2*2**sp.Rational(-15,4)
c7=c3
c8=c6
c9=L2*2**sp.Rational(-9,2)
c10=L2/4
c11=2*L3/(3*sp.sqrt(3))
weights=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11]
beta0=sp.simplify(-c1+c3)
betam=sp.simplify(-c2-c4)
betap=sp.simplify(c2+c6)
betaT=sp.simplify(-c3-c5-c7-c10)
betab=-c11
kappa=sp.simplify(c1+c5+c9+c10+c11)
alphab=sp.simplify(c1+c5+c11)

WORDS=[(1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),(6,T,3*a,a),
       (7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),(10,T,T,T),(11,b,b,b)]
SIGNS=(-1,1,1,-1)

# Closure of the exact inner chamber:
# 0 <= u <= eps and u+eps <= Delta.
V=[{u:0,eps:0},{u:0,eps:Delta},{u:Delta/2,eps:Delta/2}]

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
    if sp.simplify(expr)==0: return sp.Integer(0)
    raise AssertionError(("profile sign switch",expr,vals(expr)))
def aggregate(x):
    out={}; count=0
    for j,delta,eta,lam in WORDS:
        gm=absclass(x-delta,T0-lam)
        gp=absclass(x+delta,T0-lam)
        assert gm!="MIX" and gp!="MIX",(x,j,gm,gp)
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for k,(gate,q) in enumerate(zip(gates,src)):
            if gate=="OUT": continue
            hc=absclass(q,T0)
            assert hc!="MIX",(x,j,k+1,q)
            if hc=="IN":
                p=profile(q)
                out[p]=sp.simplify(out.get(p,0)+SIGNS[k]*weights[j-1])
                count+=1
    return {k:sp.simplify(v) for k,v in out.items() if sp.simplify(v)!=0},count
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

# Inner a/T block: direct rows u,a-u,a+u,T-u,T+u.
expected_inner={
 u:{u:2*c1,a-u:c2,a+u:c2,T-u:beta0,T+u:beta0},
 a-u:{u:c2,a-u:c1+c5,a+u:-c1,T-u:betap,T+u:betam},
 a+u:{u:c2,a-u:-c1,a+u:c1+c5,T-u:betam,T+u:betap},
 T+u:{T+u:kappa,u:beta0,a-u:betam,a+u:betap,T-u:betaT,2*d-u:betab},
 T-u:{T-u:kappa,u:beta0,a+u:betam,a-u:betap,T+u:betaT,2*d+u:betab},
}
for x,exp in expected_inner.items():
    got,_=aggregate(x)
    assert_map(got,exp)

alpha0=1+2*c1
alphaA=1+c1+c5
alphaT=1+kappa
M5=sp.Matrix([
 [alpha0,c2,c2,beta0,beta0],
 [c2,alphaA,-c1,betap,betam],
 [c2,-c1,alphaA,betam,betap],
 [beta0,betap,betam,alphaT,betaT],
 [beta0,betam,betap,betaT,alphaT],
])
assert M5.is_positive_definite is True

# Inner pointwise B block: all eight direct rows.
expected_B={
 e+u:{b-u:-c1,e+u:c1,C+u:c2},
 e-u:{b+u:-c1,e-u:c1,C-u:c2},
 d+u:{C-u:-c1,d+u:c1,b+u:c2},
 d-u:{C+u:-c1,d-u:c1,b-u:c2},
 b+u:{e-u:-c1,b+u:alphab,C-u:betam,d+u:c2,b-u:betab},
 b-u:{e+u:-c1,b-u:alphab,C+u:betam,d-u:c2,b+u:betab},
 C+u:{d-u:-c1,C+u:alphab,b-u:betam,e+u:c2,b+Delta-u:betab},
 C-u:{d+u:-c1,C-u:alphab,b+u:betam,e-u:c2,b+Delta+u:betab},
}
for x,exp in expected_B.items():
    got,_=aggregate(x)
    assert_map(got,exp)

MB=sp.Matrix([
 [1+c1,0,c1,c2],
 [0,1+c1,c2,c1],
 [c1,c2,1+c1+c5+2*c11,2*c2],
 [c2,c1,2*c2,1+c1+c5+c11],
])
assert MB.is_positive_definite is True

# Direct 2d±u rows in the same off-J chamber.
expected_2d_plus={
 2*e-u:-c1,
 2*d+u:alphab,
 T-Delta-u:betam,
 Delta+u:c2,
 T-u:betab,
}
expected_2d_minus={
 2*e+u:-c1,
 2*d-u:alphab,
 T-Delta+u:betam,
 Delta-u:c2,
 T+u:betab,
}
got,_=aggregate(2*d+u); assert_map(got,expected_2d_plus)
got,_=aggregate(2*d-u); assert_map(got,expected_2d_minus)

# Exact SW1 slack parametrization for 0<u<R<eps and R+eps<Delta.
x,y,z,g=sp.symbols("x y z g", positive=True)
U=x
R=x+y
EPS=x+y+z
DD=sp.simplify(R+EPS+g)
assert sp.simplify(DD-(U+EPS)-(y+g))==0
assert sp.simplify(DD-2*U-(2*y+z+g))==0
assert sp.simplify((DD-U)-EPS-(y+g))==0
assert sp.simplify(2*DD-(DD+U)-(DD-U))==0

# Descendants are immediately outer:
# eps < Delta-u < Delta+u < 2Delta.
assert sp.simplify((DD-U)-EPS-(y+g))==0
assert sp.simplify((DD+U)-(DD-U)-2*U)==0
assert sp.simplify(2*DD-(DD+U)-(DD-U))==0

# Inner B sample is strictly below the Stage-10A wall.
assert sp.simplify(hB-Delta).is_positive is True
# hB-(u+eps) = (hB-Delta) + (Delta-u-eps), both positive.
assert sp.simplify((hB-(U+EPS))-((hB-DD)+(DD-U-EPS)))==0

# KNF reconstruction is algebraically exact.
p,r,q=sp.symbols("p r q", nonzero=True)
yaP,ybM,ybP,yTM,yTP=sp.symbols("yaP ybM ybP yTM yTP")
yaM=sp.simplify(yaP-r/p*(ybM-ybP)-q/p*(yTM-yTP))
inner=sp.simplify(p*(yaM-yaP)+r*(ybM-ybP)+q*(yTM-yTP))
assert inner==0

print("SW1-DELTA-DESCENT STAGE-12-INNER CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("inner chamber u+eps<Delta and u<Delta/2 certified")
print("direct a/T five-row M5 ledger certified; M5 positive definite")
print("direct e/d/b/C eight-row B ledger certified; M_B positive definite")
print("direct 2d±u off-J rows certified")
print("Delta±u descendants lie in (eps,2Delta)")
print("inner B step is strictly below h_B wall")
print("KNF left a-branch reconstruction satisfies the inner kernel row exactly")
print("downstream finite closure relies only on previously certified Stages 5-11")
print("A0 / blind-summand coverage intentionally not certified")
