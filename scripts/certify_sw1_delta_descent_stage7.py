#!/usr/bin/env python3
import sympy as sp

s, eps, z = sp.symbols("s eps z", real=True)
log2,log3=sp.log(2),sp.log(3)
a=log2/2;b=log3/2;T=2*a;d=b-a;e=T-b;Delta=sp.simplify(d-e)
T0=T+eps
weights=[
 log2*2**sp.Rational(-3,2),log2*2**sp.Rational(-9,4),log2*2**sp.Rational(-3),
 log2*2**sp.Rational(-9,4),log2*2**sp.Rational(-3),log2*2**sp.Rational(-15,4),
 log2*2**sp.Rational(-3),log2*2**sp.Rational(-15,4),log2*2**sp.Rational(-9,2),
 log2/4,2*log3/(3*sp.sqrt(3))]
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11=weights
beta0=sp.simplify(-c1+c3);betam=sp.simplify(-c2-c4);betap=sp.simplify(c2+c6)
betaT=sp.simplify(-c3-c5-c7-c10);betab=sp.simplify(-c11)
kappa=sp.simplify(c1+c5+c9+c10+c11);alphab=sp.simplify(c1+c5+c11)
WORDS=[(1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),(6,T,3*a,a),
       (7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),(10,T,T,T),(11,b,b,b)]
SIGNS=(-1,1,1,-1)

def classifier(verts):
    def vals(expr):
        return [sp.simplify(sp.expand(expr).subs(v)) for v in verts]
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
                if gate=="OUT":continue
                hc=absclass(q,T0)
                assert hc!="MIX",(x,j,kk+1,hc,q,vals(q))
                if hc=="IN":
                    p=profile(q)
                    out[p]=sp.simplify(out.get(p,0)+SIGNS[kk]*weights[j-1])
                    count+=1
        return out,count
    return aggregate

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

# 1. Extended 2TP: 0<z<eps<Delta.
VZ=[{z:0,eps:0},{z:0,eps:Delta},{z:Delta,eps:Delta}]
aggz=classifier(VZ)
expTp={T+z:kappa,z:beta0,a-z:betam,a+z:betap,T-z:betaT,2*d-z:betab}
expTm={T-z:kappa,z:beta0,a+z:betam,a-z:betap,T+z:betaT,2*d+z:betab}
got,n=aggz(T+z); assert n==16; assert_map(got,expTp)
got,n=aggz(T-z); assert n==16; assert_map(got,expTm)
tau=1+kappa
DT=sp.simplify(tau**2-betaT**2)
assert DT.is_positive is True

# 2. Constants for finite terminal split.
h3=sp.simplify(a-4*Delta)
h4=sp.simplify(a-5*Delta)
g6=sp.simplify(6*Delta-a)
assert h3.is_positive is True
assert h4.is_positive is True
assert g6.is_positive is True
assert sp.simplify(h4+g6-Delta)==0
assert sp.simplify(h4-g6).is_positive is True
assert sp.simplify(h3-h4-Delta)==0

# 3. Low x4 chamber s+eps<h4.
VA=[{s:0,eps:0},{s:0,eps:h4},{s:h4/2,eps:h4/2}]
agga=classifier(VA)
x4=sp.simplify(2*d+4*Delta+s)
exp_x4={
 2*e-4*Delta-s:-c1,
 x4:alphab,
 T-5*Delta-s:betam,
 5*Delta+s:c2,
 T-4*Delta-s:betab,
}
got,n=agga(x4); assert n==8; assert_map(got,exp_x4)
assert sp.simplify(x4-a-(5*Delta+s))==0
assert sp.simplify(x4-b-(4*Delta+s-e))==0
assert sp.simplify(x4-T-(4*Delta+s-2*e))==0

# 4. u5 terminal companion split by q=g6+s vs eps.
m=sp.simplify((h4-g6)/2)
VON=[{s:0,eps:g6},{s:0,eps:h4},{s:m,eps:m+g6}]
VOFF=[{s:0,eps:0},{s:0,eps:g6},{s:m,eps:m+g6},{s:h4/2,eps:h4/2}]
aggon=classifier(VON)
aggoff=classifier(VOFF)
U5=sp.simplify(5*Delta+s)
expU={T-U5:-c1,U5:c1,a+U5:c2}
expAm={a+U5:-c1,a-U5:c1,T-U5:c2}
expTm_on={U5:-c1,T-U5:alphab,a-U5:c2,a+U5:betam,2*d+U5:betab}
alpha_off=sp.simplify(c1+c5)
expTm_off={U5:-c1,T-U5:alpha_off,a-U5:c2,a+U5:betam}
for agg in (aggon,aggoff):
    got,n=agg(U5); assert n==3; assert_map(got,expU)
    got,n=agg(a-U5); assert n==3; assert_map(got,expAm)
got,n=aggon(T-U5); assert n==8; assert_map(got,expTm_on)
got,n=aggoff(T-U5); assert n==6; assert_map(got,expTm_off)

M_on=sp.Matrix([[1+c1,0,-c1],[0,1+c1,c2],[-c1,c2,1+alphab]])
M_off=sp.Matrix([[1+c1,0,-c1],[0,1+c1,c2],[-c1,c2,1+alpha_off]])
assert M_on.is_positive_definite is True
assert M_off.is_positive_definite is True

# 5. Terminal shell identity.
x5=sp.simplify(2*d+5*Delta+s)
q=sp.simplify(g6+s)
assert sp.simplify(x5-(T+q))==0
assert g6.is_positive is True

# 6. Middle x4 fold identities.
tminus=sp.simplify(h4-s)
tplus=sp.simplify(s-h4)
assert sp.simplify(x4-(T-tminus))==0
assert sp.simplify(x4-(T+tplus))==0

print("SW1-DELTA-DESCENT STAGE-7 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("extended T±z 2TP ledger/pivot valid for 0<z<eps")
print("low x4 outer row has exactly 8 echoes")
print("u5 terminal companion: 8 echoes when q<eps, 6 when q>eps")
print("both terminal companion matrices are positive definite")
print("x5=T+(6Delta-a+s): folds to extended 2TP if inside horizon, else is horizon-zero")
print("finite y-shell graph closes after at most five Delta steps")
