#!/usr/bin/env python3
import sympy as sp

u, eps = sp.symbols("u eps", real=True)
log2, log3 = sp.log(2), sp.log(3)
a = log2/2
b = log3/2
T = 2*a
d = b-a
e = T-b
Delta = sp.simplify(d-e)
T0 = T+eps

weights = [
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
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11 = weights
beta0 = sp.simplify(-c1+c3)
betam = sp.simplify(-c2-c4)
betap = sp.simplify(c2+c6)
betaT = sp.simplify(-c3-c5-c7-c10)
betab = sp.simplify(-c11)
kappa = sp.simplify(c1+c5+c9+c10+c11)
alphab = sp.simplify(c1+c5+c11)

WORDS = [
    (1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),
    (6,T,3*a,a),(7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),
    (10,T,T,T),(11,b,b,b),
]
SIGNS=(-1,1,1,-1)

VERTS = {
    "L":[{u:0,eps:0},{u:0,eps:Delta},{u:Delta/2,eps:Delta/2}],
    "U":[{u:0,eps:Delta},{u:Delta/2,eps:Delta/2},{u:Delta,eps:Delta}],
    "O":[{u:0,eps:0},{u:2*Delta,eps:0},{u:2*Delta,eps:Delta},{u:Delta,eps:Delta}],
}

def vals(expr,vs):
    return [sp.simplify(sp.expand(expr).subs(v)) for v in vs]

def nonnegative(expr,vs):
    return all(v.is_nonnegative is True for v in vals(expr,vs))

def positive_affine(expr,vs):
    expr=sp.expand(expr)
    return expr != 0 and nonnegative(expr,vs)

def classify_abs(expr,bound,vs):
    if nonnegative(bound-expr,vs) and nonnegative(bound+expr,vs):
        return "IN"
    if positive_affine(expr-bound,vs) or positive_affine(-expr-bound,vs):
        return "OUT"
    return "MIX"

def even_profile(expr,vs):
    if positive_affine(expr,vs):
        return sp.simplify(expr)
    if positive_affine(-expr,vs):
        return sp.simplify(-expr)
    if sp.simplify(expr)==0:
        return sp.Integer(0)
    raise AssertionError(("profile sign changes",expr))

def aggregate(x,case):
    vs=VERTS[case]
    out={}
    count=0
    for j,delta,eta,lam in WORDS:
        gm=classify_abs(x-delta,T0-lam,vs)
        gp=classify_abs(x+delta,T0-lam,vs)
        assert gm!="MIX" and gp!="MIX", ("mixed gate",case,x,j)
        gates=[gm,gm,gp,gp]
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        for k,(gate,sr) in enumerate(zip(gates,src)):
            if gate=="OUT":
                continue
            hs=classify_abs(sr,T0,vs)
            assert hs!="MIX", ("mixed source horizon",case,x,j,k+1,sr)
            if hs=="IN":
                prof=even_profile(sr,vs)
                out[prof]=sp.simplify(out.get(prof,0)+SIGNS[k]*weights[j-1])
                count+=1
    return out,count

def assert_map(got,expected):
    rem=list(got.items())
    for ek,ev in expected.items():
        hit=None
        for i,(gk,gv) in enumerate(rem):
            if sp.simplify(gk-ek)==0:
                assert sp.simplify(gv-ev)==0,(ek,gv,ev)
                hit=i
                break
        assert hit is not None,("missing",ek,got)
        rem.pop(hit)
    assert not rem,("extra",rem)

# Inner rows, off J (L) and on J (U)
exp_u={
    u:2*c1,
    a-u:c2,
    a+u:c2,
    T-u:beta0,
    T+u:beta0,
}
exp_am={
    u:c2,
    a-u:c1+c5,
    a+u:-c1,
    T-u:betap,
    T+u:betam,
}
exp_ap_L={
    u:c2,
    a-u:-c1,
    a+u:c1+c5,
    T-u:betam,
    T+u:betap,
}
exp_ap_U=dict(exp_ap_L)
exp_ap_U[a+u]=sp.simplify(c1+c5+c11)
exp_ap_U[T+Delta-u]=betab

for case in ("L","U"):
    got,n=aggregate(u,case); assert n==8; assert_map(got,exp_u)
    got,n=aggregate(a-u,case); assert n==8; assert_map(got,exp_am)
    got,n=aggregate(a+u,case)
    if case=="L":
        assert n==8; assert_map(got,exp_ap_L)
    else:
        assert n==10; assert_map(got,exp_ap_U)

# Outer companion rows
exp_O_u={T-u:-c1,u:c1,a+u:c2}
exp_O_am={a+u:-c1,a-u:c1,T-u:c2}
exp_O_Tm={
    u:-c1,
    T-u:alphab,
    a-u:c2,
    a+u:betam,
    2*d+u:betab,
}
got,n=aggregate(u,"O"); assert n==3; assert_map(got,exp_O_u)
got,n=aggregate(a-u,"O"); assert n==3; assert_map(got,exp_O_am)
got,n=aggregate(T-u,"O"); assert n==8; assert_map(got,exp_O_Tm)

# Exact companion matrices
M3=sp.Matrix([
    [1+c1,0,-c1],
    [0,1+c1,c2],
    [-c1,c2,1+alphab],
])
assert M3.is_positive_definite is True
det3=sp.factor(M3.det())
assert det3.is_positive is True

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

E33=sp.zeros(5); E33[2,2]=c11
CJ=sp.zeros(5); CJ[2,4]=betab; CJ[4,2]=betab
Mloc=M5+E33
Mref_plus=Mloc+CJ
Mref_minus=Mloc-CJ
assert Mref_plus.is_positive_definite is True
assert Mref_minus.is_positive_definite is True

# Nonzero next-shell coefficient gamma_Q.
# Avoid a full symbolic M3 inverse: solve M3*x=e3 explicitly.
rO=sp.Matrix([c2,-c1,betam])
e3=sp.Matrix([0,0,1])
SO=sp.simplify(1+alphab-(c1**2+c2**2)/(1+c1))
assert SO.is_positive is True
x3=1/SO
x1=c1*x3/(1+c1)
x2=-c2*x3/(1+c1)
xvec=sp.Matrix([x1,x2,x3])
for entry in (M3*xvec-e3):
    assert sp.cancel(sp.together(entry)) == 0
rho3_expected=-2*c2/((1+c1)*SO)
rho3=sp.expand((rO.T*xvec)[0])
assert sp.cancel(sp.together(rho3-rho3_expected)) == 0
assert rho3_expected.is_negative is True
gammaQ=sp.simplify(-betab*rho3_expected)
assert gammaQ.is_negative is True
assert gammaQ.is_zero is False

# Fixed support inequalities used by Hub formulas.
assert sp.simplify(e-2*Delta).is_positive is True
assert sp.simplify(a-2*Delta).is_positive is True
assert sp.simplify((d-2*Delta)).is_positive is True

print("SW1-DELTA-DESCENT STAGE-4 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("inner off-J rows u,a-u,a+u: exact")
print("inner on-J: unique word-11 correction exact")
print("outer rows u,a-u,T-u: exact")
print("M3, M5, and both reflected J 5x5 blocks positive definite")
print("gamma_Q < 0 and nonzero: next D_+(u) shell genuinely couples")
