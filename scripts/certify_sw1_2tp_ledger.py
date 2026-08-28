#!/usr/bin/env python3
"""
Exact symbolic certificate for Objekt-X SW1-2TP stage 1 (11-word ledger).

Enumerates all 2 * 11 * 4 = 88 echo cases from HT.3 on
0 < s < eps < Delta (implied by SW1), certifies gate/source-horizon
status uniformly, and aggregates the surviving even-y profiles.

Requires: sympy
"""
import sympy as sp

s, eps = sp.symbols("s eps", real=True)
a = sp.log(2) / 2
b = sp.log(3) / 2
T = 2 * a
d = b - a
e = T - b
Delta = d - e
T0 = T + eps
c = sp.symbols("c1:12")

WORDS = [
    (1,a,a,a),(2,a,T,a),(3,a,3*a,a),(4,T,a,a),(5,T,T,a),
    (6,T,3*a,a),(7,3*a,a,a),(8,3*a,T,a),(9,3*a,3*a,a),
    (10,T,T,T),(11,b,b,b),
]
VERTICES = [{s:0,eps:0},{s:0,eps:Delta},{s:Delta,eps:Delta}]
SIGNS = (-1,+1,+1,-1)

def vertex_values(expr):
    return [sp.simplify(expr.subs(v)) for v in VERTICES]

def is_nonnegative_on_closure(expr):
    vals = vertex_values(sp.expand(expr))
    return all(v.is_nonnegative is True for v in vals), vals

def is_positive_on_open_triangle(expr):
    expr = sp.simplify(expr)
    ok, vals = is_nonnegative_on_closure(expr)
    return ok and expr != 0, vals

def abs_within(expr, bound):
    ok1,_ = is_nonnegative_on_closure(bound-expr)
    ok2,_ = is_nonnegative_on_closure(bound+expr)
    return ok1 and ok2

def abs_outside(expr, bound):
    ok1,_ = is_positive_on_open_triangle(expr-bound)
    ok2,_ = is_positive_on_open_triangle(-expr-bound)
    return ok1 or ok2

def profile_for_even_y(expr):
    expr = sp.simplify(expr)
    ok,_ = is_positive_on_open_triangle(expr)
    if ok:
        return expr
    ok,_ = is_positive_on_open_triangle(-expr)
    if ok:
        return sp.simplify(-expr)
    raise AssertionError(f"source changes sign in SW1 interior: {expr}")

def echo_data(x, delta, eta, lam):
    gm = sp.simplify(x-delta)
    gp = sp.simplify(x+delta)
    gate_bound = sp.simplify(T0-lam)
    assert abs_within(gm, gate_bound), ("left gate not uniformly open", x,delta,lam)
    assert abs_outside(gp, gate_bound), ("right gate not uniformly closed", x,delta,lam)
    sources = [
        sp.simplify(x-delta-eta), sp.simplify(x-delta+eta),
        sp.simplify(x+delta-eta), sp.simplify(x+delta+eta),
    ]
    out = []
    for k,src in enumerate(sources):
        if k >= 2:
            out.append(("GATE_CLOSED",src,None))
        elif abs_within(src,T0):
            out.append(("SURVIVES",src,profile_for_even_y(src)))
        elif abs_outside(src,T0):
            out.append(("HORIZON_DEAD",src,None))
        else:
            raise AssertionError(f"undecidable source horizon: {src}")
    return out

def aggregate(row_sign):
    x = sp.simplify(T + row_sign*s)
    agg = {}
    raw = []
    survivors = 0
    for j,delta,eta,lam in WORDS:
        data = echo_data(x,delta,eta,lam)
        for k,(status,src,profile) in enumerate(data):
            raw.append((j,k+1,status,sp.simplify(src),profile))
            if status == "SURVIVES":
                survivors += 1
                key = sp.simplify(profile)
                agg[key] = sp.simplify(agg.get(key,0) + SIGNS[k]*c[j-1])
    return raw,agg,survivors

def assert_maps_equal(got, expected):
    unmatched = list(got.items())
    for ekey,ecoeff in expected.items():
        hit = None
        for idx,(gkey,gcoeff) in enumerate(unmatched):
            if sp.simplify(gkey-ekey) == 0:
                assert sp.simplify(gcoeff-ecoeff) == 0, (ekey,gcoeff,ecoeff)
                hit = idx
                break
        assert hit is not None, ("missing profile",ekey,list(got.keys()))
        unmatched.pop(hit)
    assert not unmatched, ("unexpected profiles",unmatched)

rawp,aggp,np = aggregate(+1)
rawm,aggm,nm = aggregate(-1)

EXPECTED_PLUS = {
    sp.simplify(s): -c[0]+c[6],
    sp.simplify(a-s): -c[1]-c[3],
    sp.simplify(a+s): c[3]+c[7],
    sp.simplify(T-s): -c[2]-c[4]-c[6]-c[9],
    sp.simplify(T+s): c[0]+c[4]+c[8]+c[9]+c[10],
    sp.simplify(2*d-s): -c[10],
}
EXPECTED_MINUS = {
    sp.simplify(s): -c[0]+c[6],
    sp.simplify(a+s): -c[1]-c[3],
    sp.simplify(a-s): c[3]+c[7],
    sp.simplify(T+s): -c[2]-c[4]-c[6]-c[9],
    sp.simplify(T-s): c[0]+c[4]+c[8]+c[9]+c[10],
    sp.simplify(2*d+s): -c[10],
}

assert np == 16
assert nm == 16
assert_maps_equal(aggp,EXPECTED_PLUS)
assert_maps_equal(aggm,EXPECTED_MINUS)
assert sp.simplify(Delta).is_positive is True
assert sp.simplify(a-2*Delta).is_positive is True
assert sp.simplify(e-Delta).is_positive is True
assert sp.simplify(d-e-Delta) == 0

# ---- Stages 2-4: exact weights, Hub support, pivot and eigenchannels ----

WEIGHTS = [
    sp.log(2)*2**sp.Rational(-3,2),
    sp.log(2)*2**sp.Rational(-9,4),
    sp.log(2)*2**sp.Rational(-3,1),
    sp.log(2)*2**sp.Rational(-9,4),
    sp.log(2)*2**sp.Rational(-3,1),
    sp.log(2)*2**sp.Rational(-15,4),
    sp.log(2)*2**sp.Rational(-3,1),
    sp.log(2)*2**sp.Rational(-15,4),
    sp.log(2)*2**sp.Rational(-9,2),
    sp.log(2)/4,
    2*sp.log(3)/(3*sp.sqrt(3)),
]

kappa = sp.simplify(WEIGHTS[0]+WEIGHTS[4]+WEIGHTS[8]+WEIGHTS[9]+WEIGHTS[10])
beta0 = sp.simplify(-WEIGHTS[0]+WEIGHTS[6])
betam = sp.simplify(-WEIGHTS[1]-WEIGHTS[3])
betap = sp.simplify(WEIGHTS[3]+WEIGHTS[7])
betaT = sp.simplify(-WEIGHTS[2]-WEIGHTS[4]-WEIGHTS[6]-WEIGHTS[9])
betab = sp.simplify(-WEIGHTS[10])

assert sp.simplify(betaT + sp.Rational(5,8)*sp.log(2)) == 0
assert kappa.is_positive is True
assert sp.simplify(1-sp.log(2)).is_positive is True

lambda_sum = sp.simplify(1+kappa+betaT)
lambda_diff = sp.simplify(1+kappa-betaT)
det_MT = sp.simplify((1+kappa)**2-betaT**2)

assert lambda_sum.is_positive is True
assert lambda_diff.is_positive is True
assert det_MT.is_positive is True
assert sp.simplify(lambda_sum*lambda_diff-det_MT) == 0

# Full SW1 closure for Hub support:
# 0 <= sigma <= R <= s <= eps <= Delta.
R, sigma = sp.symbols("R sigma", real=True)
HUB_VERTICES = [
    {sigma:0,R:0,s:0,eps:0},
    {sigma:0,R:0,s:0,eps:Delta},
    {sigma:0,R:0,s:Delta,eps:Delta},
    {sigma:0,R:Delta,s:Delta,eps:Delta},
    {sigma:Delta,R:Delta,s:Delta,eps:Delta},
]

def hub_vertex_values(expr):
    return [sp.simplify(expr.subs(v)) for v in HUB_VERTICES]

def hub_nonnegative(expr):
    vals = hub_vertex_values(sp.expand(expr))
    return all(v.is_nonnegative is True for v in vals)

def hub_positive(expr):
    expr = sp.simplify(expr)
    return expr != 0 and hub_nonnegative(expr)

def hub_sign(expr):
    if hub_positive(expr):
        return +1
    if hub_positive(-expr):
        return -1
    raise AssertionError(f"Hub argument changes sign: {expr}")

def annulus_class(expr):
    sg = hub_sign(expr)
    mag = sp.simplify(sg*expr)
    if hub_positive(mag-R) and hub_positive(T+sigma-mag):
        return "ACTIVE", sg, mag
    if hub_positive(mag-(T+sigma)) or hub_positive(R-mag):
        return "DEAD", sg, mag
    raise AssertionError(f"Undecidable annulus support: {expr}")

p, r, q = sp.symbols("p r q", positive=True)

def hub_aggregate(row_sign):
    u = sp.simplify(T+row_sign*s)
    out = {}
    for tau, coeff in [(a,p),(b,r),(T,q)]:
        for branch_sign, op_sign in [(-1,+1),(+1,-1)]:
            arg = sp.simplify(u+branch_sign*tau)
            status, odd_sign, mag = annulus_class(arg)
            if status == "ACTIVE":
                key = sp.simplify(mag)
                out[key] = sp.simplify(out.get(key,0)+op_sign*odd_sign*coeff)
    return out

def assert_profile_map(got, expected):
    unmatched = list(got.items())
    for ekey, ecoeff in expected.items():
        hit = None
        for idx,(gkey,gcoeff) in enumerate(unmatched):
            if sp.simplify(gkey-ekey) == 0:
                assert sp.simplify(gcoeff-ecoeff) == 0
                hit = idx
                break
        assert hit is not None, ("missing hub profile",ekey,got)
        unmatched.pop(hit)
    assert not unmatched, ("unexpected hub profiles",unmatched)

hub_plus = hub_aggregate(+1)
hub_minus = hub_aggregate(-1)
assert_profile_map(hub_plus,{sp.simplify(a+s):p,sp.simplify(e+s):r,sp.simplify(s):q})
assert_profile_map(hub_minus,{sp.simplify(a-s):p,sp.simplify(e-s):r,sp.simplify(s):-q})

# Algebraic sum/difference certificate for the two augmented rows.
yp, ym, ys, yam, yap, ydm, ydp = sp.symbols("yp ym ys yam yap ydm ydp")
wap, wam, wep, wem, ws = sp.symbols("wap wam wep wem ws")

row_plus = (
    (1+kappa)*yp + betaT*ym + beta0*ys
    + betam*yam + betap*yap + betab*ydm
    + p*wap + r*wep + q*ws
)
row_minus = (
    betaT*yp + (1+kappa)*ym + beta0*ys
    + betam*yap + betap*yam + betab*ydp
    + p*wam + r*wem - q*ws
)

expected_sum = (
    lambda_sum*(yp+ym) + 2*beta0*ys
    + (betam+betap)*(yam+yap) + betab*(ydm+ydp)
    + p*(wap+wam) + r*(wep+wem)
)
expected_diff = (
    lambda_diff*(yp-ym)
    + (betap-betam)*(yap-yam) + betab*(ydm-ydp)
    + p*(wap-wam) + r*(wep-wem) + 2*q*ws
)

assert sp.simplify(row_plus+row_minus-expected_sum) == 0
assert sp.simplify(row_plus-row_minus-expected_diff) == 0

print("SW1-2TP CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("stage1: all 88 echo cases classified exactly")
print(f"x=T+s: survivors={np}")
print(f"x=T-s: survivors={nm}")
print("stage2: paired A-rows and both Hub support patterns certified")
print("stage3: beta_T=-5/8 log(2), both eigenvalues positive, det(M_T)>0")
print("stage4: q*w(s) cancels in sum and appears as 2*q*w(s) in difference")
print("word 11 at x=T-s: surviving profile 2*d+s")
