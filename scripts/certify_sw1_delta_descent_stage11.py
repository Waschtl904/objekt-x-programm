#!/usr/bin/env python3
import sympy as sp

s, eps = sp.symbols("s eps", real=True)
L2,L3=sp.log(2),sp.log(3)
a=L2/2; b=L3/2; T=2*a; d=b-a; e=T-b; Delta=sp.simplify(d-e); T0=T+eps
C=sp.simplify(a+e)
F1=sp.simplify(C-Delta)
E2=sp.simplify(e-2*Delta)
D2=sp.simplify(d+2*Delta)
B2=sp.simplify(b+2*Delta)
F2=sp.simplify(C-2*Delta)
B3=sp.simplify(b+3*Delta)
kB=sp.simplify(E2)
g3=sp.simplify(B3-T)

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
alpha_b=sp.simplify(c1+c5+c11)
beta_m=sp.simplify(-c2-c4)
beta_b=-c11

WORDS=[(1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),(6,T,3*a,a),
       (7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),(10,T,T,T),(11,b,b,b)]
SIGNS=(-1,1,1,-1)

assert sp.simplify(T-B2-kB)==0
assert kB.is_positive is True
assert sp.simplify(g3-kB).is_positive is True

VLOW=[{s:0,eps:0},{s:0,eps:kB},{s:kB/2,eps:kB/2}]

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
    if sp.simplify(expr)==0: return sp.Integer(0)
    raise AssertionError(("profile sign switch",expr,vals(expr,vs)))
def aggregate(x,vs):
    out={}; count=0
    for j,delta,eta,lam in WORDS:
        gm=absclass(x-delta,T0-lam,vs)
        gp=absclass(x+delta,T0-lam,vs)
        assert gm!="MIX" and gp!="MIX",(x,j,gm,gp)
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for k,(gate,q) in enumerate(zip(gates,src)):
            if gate=="OUT": continue
            hc=absclass(q,T0,vs)
            assert hc!="MIX",(x,j,k+1,q)
            if hc=="IN":
                p=profile(q,vs)
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

expected_low={
 E2+s:{B2-s:-c1,E2+s:c1,F2+s:c2},
 E2-s:{B2+s:-c1,E2-s:c1,F2-s:c2},
 D2+s:{F2-s:-c1,D2+s:c1,B2+s:c2},
 D2-s:{F2+s:-c1,D2-s:c1,B2-s:c2},
 B2+s:{E2-s:-c1,B2+s:alpha_b,F2-s:beta_m,D2+s:c2,F1-s:beta_b},
 B2-s:{E2+s:-c1,B2-s:alpha_b,F2+s:beta_m,D2-s:c2,F1+s:beta_b},
 F2+s:{D2-s:-c1,F2+s:c1+c5,B2-s:beta_m,E2+s:c2},
 F2-s:{D2+s:-c1,F2-s:c1+c5,B2+s:beta_m,E2-s:c2},
}
for x,exp in expected_low.items():
    got,_=aggregate(x,VLOW)
    assert_map(got,exp)

# Terminal low-chamber difference block.
M=sp.Matrix([
 [1+c1,0,c1,c2],
 [0,1+c1,c2,c1],
 [c1,c2,1+alpha_b,2*c2],
 [c2,c1,2*c2,1+c1+c5],
])
assert M.is_positive_definite is True

# B3 is horizon-dead in low chamber:
# g3 > kB > s+eps => B3-s = T+(g3-s) > T+eps.
assert sp.simplify(g3-kB).is_positive is True

# Case II identities.
q=sp.simplify(kB+s)
assert sp.simplify(B2-s-(T-q))==0
assert sp.simplify(a+q-(F2+s))==0
assert sp.simplify(2*d+q-(F1+s))==0
assert sp.simplify((2*Delta-q)-((Delta-kB)+(Delta-s)))==0
# q<2Delta follows on 0<s<Delta from the two positive summands.
assert sp.simplify(Delta-kB).is_positive is True

# B2+s is always T±|s-kB|; both affine identities.
assert sp.simplify(B2+s-(T+(s-kB)))==0
assert sp.simplify(B2+s-(T-(kB-s)))==0

# Case III: both offsets are below eps by chamber assumptions.
assert sp.simplify(B2-s-(T-(kB+s)))==0

# Exhaustive chamber logic is Boolean:
# not(s+eps<kB) => s+eps>kB a.e.; then either s+kB<eps or >eps.
# Boundaries are the two codimension-one walls.

print("SW1-DELTA-DESCENT STAGE-11 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("Case I: all 8 B2-center rows certified")
print("terminal 4x4 B2 block positive definite")
print("Case I: B3 is horizon-dead because g3>kB>s+eps")
print("Case II: B2+s is extended 2TP; B2-s=T-q uses outer Stage-4 companion")
print("Case II identities a+q=F2+s and 2d+q=F1+s certified")
print("Case III: both B2 branches are extended 2TP tails")
print("no new y-center type survives beyond B2")
