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

print("SW1-2TP STAGE-1 CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("domain: 0 < s < eps < Delta (implied by SW1)")
print("all 88 echo cases classified exactly")
print(f"x=T+s: survivors={np}")
print(f"x=T-s: survivors={nm}")
print("right gates E3/E4: uniformly closed for all 11 words in both rows")
print("word 6: both left-gate sources horizon-dead in both rows")
print("word 11 at x=T-s: surviving off-diagonal blind profile = 2*d+s")
print("aggregated profile maps match the audit ledger")
