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
    raise AssertionError(("profile sign switch",expr))

def aggregate(x):
    out={}
    count=0
    for j,delta,eta,lam in WORDS:
        gm=absclass(x-delta,T0-lam)
        gp=absclass(x+delta,T0-lam)
        assert gm!="MIX" and gp!="MIX",(x,j,gm,gp)
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for kk,(gate,q) in enumerate(zip(gates,src)):
            if gate=="OUT": continue
            hc=absclass(q,T0)
            assert hc!="MIX",(x,j,kk+1,hc,q)
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
                hit=i;break
        assert hit is not None,("missing",ek,got)
        rem.pop(hit)
    assert not rem,("extra",rem)

# Fixed inequality ensuring m=2,3,4 companion parameters remain below a.
assert sp.simplify(a-5*Delta).is_positive is True

# Extended outer companion rows for u_m=m Delta+s, m=2,3,4.
for m in (2,3,4):
    U=sp.simplify(m*Delta+s)
    expU={T-U:-c1,U:c1,a+U:c2}
    expAm={a+U:-c1,a-U:c1,T-U:c2}
    expTm={
        U:-c1,
        T-U:alphab,
        a-U:c2,
        a+U:betam,
        2*d+U:betab,
    }
    got,n=aggregate(U); assert n==3; assert_map(got,expU)
    got,n=aggregate(a-U); assert n==3; assert_map(got,expAm)
    got,n=aggregate(T-U); assert n==8; assert_map(got,expTm)

# The same M_O and nonzero gamma_Q apply.
M3=sp.Matrix([
 [1+c1,0,-c1],
 [0,1+c1,c2],
 [-c1,c2,1+alphab],
])
assert M3.is_positive_definite is True
SO=sp.simplify(1+alphab-(c1**2+c2**2)/(1+c1))
assert SO.is_positive is True
rho=-2*c2/((1+c1)*SO)
assert rho.is_negative is True
gammaQ=sp.simplify(-betab*rho)
assert gammaQ.is_negative is True
assert gammaQ.is_zero is False

# Missing second outer shell x2=2d+2Delta+s.
x2=sp.simplify(2*d+2*Delta+s)
expected_x2={
 2*e-2*Delta-s:-c1,
 x2:alphab,
 T-3*Delta-s:betam,
 3*Delta+s:c2,
 T-2*Delta-s:betab,
}
got,n=aggregate(x2)
assert n==8
assert_map(got,expected_x2)

# Exact Hub affine identities for DD.102k.
assert sp.simplify(x2-a-(3*Delta+s))==0
assert sp.simplify(x2-b-(2*Delta+s-e))==0
assert sp.simplify(x2-T-(2*Delta+s-2*e))==0

# The chain labels are exact.
u2=sp.simplify(2*Delta+s)
u3=sp.simplify(3*Delta+s)
u4=sp.simplify(4*Delta+s)
assert sp.simplify((2*d+u2)-x2)==0
assert sp.simplify((2*d+u3)-(2*d+3*Delta+s))==0
assert sp.simplify((2*d+u4)-(2*d+4*Delta+s))==0

print("SW1-DELTA-DESCENT STAGE-5B CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("outer companion M_O rows certified for m=2,3,4")
print("same gamma_Q<0 is nonzero on all three bridge levels")
print("missing shell x2=2d+2Delta+s has exactly 8 echoes")
print("aggregated second-shell A-row and Hub affine identities certified")
print("chain to Stage 6 is now ledger-complete")
