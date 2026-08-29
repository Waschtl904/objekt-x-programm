#!/usr/bin/env python3
import sympy as sp

s, eps = sp.symbols("s eps", real=True)
a = sp.log(2)/2
b = sp.log(3)/2
T = 2*a
d = b-a
e = T-b
Delta = sp.simplify(d-e)
T0 = T+eps

c = sp.symbols("c1:12")
SIGNS = (-1,1,1,-1)
WORDS = [
 (1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),
 (6,T,3*a,a),(7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),
 (10,T,T,T),(11,b,b,b)
]

# Exact chamber closures in (s,eps).
# L interior: 0<s<eps<Delta and s+eps<Delta.
# U interior: 0<s<eps<Delta and s+eps>Delta.
VERTS = {
 "L":[{s:0,eps:0},{s:0,eps:Delta},{s:Delta/2,eps:Delta/2}],
 "U":[{s:0,eps:Delta},{s:Delta/2,eps:Delta/2},{s:Delta,eps:Delta}],
}

def vals(expr, verts):
    return [sp.simplify(expr.subs(v)) for v in verts]

def nonnegative(expr, verts):
    return all(v.is_nonnegative is True for v in vals(sp.expand(expr), verts))

def positive_interior(expr, verts):
    expr=sp.simplify(expr)
    return expr != 0 and nonnegative(expr, verts)

def abs_within(expr,bound,verts):
    return nonnegative(bound-expr,verts) and nonnegative(bound+expr,verts)

def even_profile(expr,verts):
    if positive_interior(expr,verts):
        return sp.simplify(expr)
    if positive_interior(-expr,verts):
        return sp.simplify(-expr)
    raise AssertionError(("sign switch",expr))

def aggregate(row_sign,chamber):
    verts=VERTS[chamber]
    x=sp.simplify(2*d+row_sign*s)
    out={}
    survivors=0
    gate_pattern=[]
    for j,delta,eta,lam in WORDS:
        gm=x-delta
        gp=x+delta
        gb=T0-lam
        left_open=abs_within(gm,gb,verts)
        right_open=abs_within(gp,gb,verts)
        gate_pattern.append((j,left_open,right_open))
        src=[x-delta-eta,x-delta+eta,x+delta-eta,x+delta+eta]
        gates=[left_open,left_open,right_open,right_open]
        for k,(g,q) in enumerate(zip(gates,src)):
            if not g:
                continue
            if abs_within(q,T0,verts):
                survivors+=1
                prof=even_profile(q,verts)
                out[prof]=sp.simplify(out.get(prof,0)+SIGNS[k]*c[j-1])
    return gate_pattern,out,survivors

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

expected_plus={
    2*e-s:-c[0],
    2*d+s:c[0]+c[4]+c[10],
    T-Delta-s:-c[1]-c[3],
    Delta+s:c[3],
    T-s:-c[10],
}
expected_minus_L={
    2*e+s:-c[0],
    2*d-s:c[0]+c[4]+c[10],
    T-Delta+s:-c[1]-c[3],
    Delta-s:c[3],
    T+s:-c[10],
}
expected_minus_U=dict(expected_minus_L)
expected_minus_U[T+Delta-s]=c[1]+c[5]

for chamber in ("L","U"):
    gp,mp,np=aggregate(+1,chamber)
    gm,mm,nm=aggregate(-1,chamber)
    for j,l,r in gp+gm:
        assert l == (j in {1,2,3,4,5,6,11})
        assert r is False
    assert np==8
    assert_map(mp,expected_plus)
    if chamber=="L":
        assert nm==8
        assert_map(mm,expected_minus_L)
    else:
        assert nm==10
        assert_map(mm,expected_minus_U)

weights=[
 sp.log(2)*2**sp.Rational(-3,2),
 sp.log(2)*2**sp.Rational(-9,4),
 sp.log(2)*2**sp.Rational(-3),
 sp.log(2)*2**sp.Rational(-9,4),
 sp.log(2)*2**sp.Rational(-3),
 sp.log(2)*2**sp.Rational(-15,4),
 sp.log(2)*2**sp.Rational(-3),
 sp.log(2)*2**sp.Rational(-15,4),
 sp.log(2)*2**sp.Rational(-9,2),
 sp.log(2)/4,
 2*sp.log(3)/(3*sp.sqrt(3))
]
alpha_b=sp.simplify(weights[0]+weights[4]+weights[10])
beta_m=sp.simplify(-weights[1]-weights[3])
beta_p=sp.simplify(weights[1]+weights[5])
beta_b=sp.simplify(-weights[10])
assert alpha_b.is_positive is True
assert sp.simplify(weights[3]-weights[1])==0
assert beta_p.is_positive is True
assert beta_b.is_negative is True

# Hub source identities and exact SW1 support inequalities.
r,u,v,g = sp.symbols("r u v g", positive=True)
R = r
ss = r+u
eeps = r+u+v
DD = 2*r+u+v+g
assert sp.simplify(DD-(R+eeps)-g)==0
assert sp.simplify(DD-ss-R-(v+g))==0
assert sp.simplify(ss-R-u)==0
assert sp.simplify(a-(2*e+Delta))==0
assert sp.simplify(d-(e+Delta))==0
assert sp.simplify(e-2*Delta).is_positive is True

xplus=2*d+s
xminus=2*d-s
assert sp.simplify(xplus-a-(Delta+s))==0
assert sp.simplify(xminus-a-(Delta-s))==0
assert sp.simplify(xplus-b-(-e+s))==0
assert sp.simplify(xminus-b-(-e-s))==0
assert sp.simplify(xplus-T-(-2*e+s))==0
assert sp.simplify(xminus-T-(-2*e-s))==0

print("SW1-DELTA-DESCENT STAGE-1/2 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("2d+s: 8 surviving echoes in both chambers")
print("2d-s: 8 echoes off J, 10 on J")
print("unique switch: beta_plus*y(T+Delta-s) on s>Delta-eps")
print("aggregated A-rows match DD.13-DD.14")
print("Hub source profiles match DD.16-DD.17")
print("direct diagonal coefficient 1+alpha_b > 1")
