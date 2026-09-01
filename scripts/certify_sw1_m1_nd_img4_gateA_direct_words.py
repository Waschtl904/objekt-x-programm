#!/usr/bin/env python3
"""Independent IMG4 Gate-A cross-check from the eleven raw A1 words.

Unlike certify_sw1_m1_nd_img4_gate1_gate9_graph_p12.py, this script does NOT
hard-code the A1 row coefficients/archetypes.  It imports the original A1
raw-word evaluator and reconstructs the off-diagonal source maps directly from
the eleven four-echo WORDS, SIGNS, weights, source gates and horizon gates.

At epsilon0=Delta/4 it:
  1. evaluates every lower-chamber A1 row from the raw words;
  2. classifies every surviving nonidentity folded source into one of the nine
     A7/A8 affine maps;
  3. proves no tenth source map survives;
  4. unions the exact row intervals mapwise;
  5. compares those unions with A7.1--A7.9;
  6. explicitly checks R6/R7 have exactly the five expected nonidentity maps.

This is a finite/algebraic graph-support certificate only.  It does not prove
the analytic unitary transport or reducing-subspace argument.
"""

import sympy as sp
from fractions import Fraction as F
import certify_sw1_a1_raw_archetypes as a1

print("SW1 M1-ND IMG4 GATE-A DIRECT-WORD GRAPH CROSS-CHECK")

X=a1.X
a,b,T,d,Delta=a1.a,a1.b,a1.T,a1.d,a1.Delta
eps=sp.expand(Delta/4)
T0=sp.expand(T+eps)

# Independent exact sign evaluator for linear forms A*log(2)+B*log(3).
# Every gate/source factor at the fixed rational-log parameter point is of
# this form. Clear denominators and compare integer prime powers.
L2,L3=sp.log(2),sp.log(3)
def lin_coeffs(expr):
    z=sp.expand(expr)
    A=sp.simplify(z.coeff(L2))
    B=sp.simplify(z.coeff(L3))
    rest=sp.simplify(z-A*L2-B*L3)
    assert rest==0, ("not-linear-log-form",expr,rest)
    assert A.is_Rational and B.is_Rational,(expr,A,B)
    return F(int(A.p),int(A.q)),F(int(B.p),int(B.q))

def exact_sign(expr):
    A,B=lin_coeffs(expr)
    if A==0 and B==0: return 0
    if A>=0 and B>=0: return 1
    if A<=0 and B<=0: return -1
    from math import lcm
    den=lcm(A.denominator,B.denominator)
    ai=A.numerator*(den//A.denominator)
    bi=B.numerator*(den//B.denominator)
    if ai>0 and bi<0:
        return (2**ai>3**(-bi))-(2**ai<3**(-bi))
    if ai<0 and bi>0:
        return (3**bi>2**(-ai))-(3**bi<2**(-ai))
    raise AssertionError((expr,A,B))

def inside_abs_exact(q,bound):
    # bound^2-q^2=(bound-q)(bound+q); each factor is a linear log form.
    s1=exact_sign(sp.expand(bound-q))
    s2=exact_sign(sp.expand(bound+q))
    return s1*s2>=0

def folded_exact(src_sym,src_at_mid):
    s=exact_sign(src_at_mid)
    assert s!=0
    return sp.expand(src_sym if s>0 else -src_sym)

def aggregate_direct(mid,eps):
    out={}
    bound0=T+eps
    for j,(delta,eta,lam) in enumerate(a1.WORDS):
        shifts=[-delta-eta,-delta+eta,delta-eta,delta+eta]
        gates=[X-delta,X-delta,X+delta,X+delta]
        for k,(gexpr,sh) in enumerate(zip(gates,shifts)):
            gmid=sp.expand(gexpr.subs(X,mid))
            if not inside_abs_exact(gmid,bound0-lam):
                continue
            src=X+sh
            smid=sp.expand(src.subs(X,mid))
            if not inside_abs_exact(smid,bound0):
                continue
            prof=folded_exact(src,smid)
            out[prof]=sp.simplify(out.get(prof,0)+a1.SIGNS[k]*a1.weights[j])
    return {sp.expand(k):sp.simplify(v) for k,v in out.items()
            if sp.simplify(v)!=0}

# Exact lower-chamber row intervals at epsilon0.
regions=[
    ("R0", sp.Integer(0), eps),
    ("R1", eps, a-eps),
    ("R2", a-eps, a),
    ("R3", a, a+eps),
    ("R4I", a+eps, 2*d-eps),
    ("R5", 2*d-eps, T-eps),
    ("R6", T-eps, T),
    ("R7", T, T+eps),
]
for _,lo,hi in regions:
    assert exact_sign(sp.expand(hi-lo))>0

# Canonical source expressions -> A7 names.
map_exprs={
    "+a": X+a,
    "-a": X-a,
    "+T": X+T,
    "-T": X-T,
    "r_a": a-X,
    "r_T": T-X,
    "r_3a": 3*a-X,
    "r_4a": 4*a-X,
    "r_2b": 2*b-X,
}

def classify(expr):
    if sp.simplify(expr-X)==0:
        return "I"
    hits=[name for name,ref in map_exprs.items() if sp.simplify(expr-ref)==0]
    assert len(hits)==1, ("unclassified-or-ambiguous-source", expr, hits)
    return hits[0]

row_maps={}
row_coeffs={}
by_map={}
for row,lo,hi in regions:
    mid=sp.expand((lo+hi)/2)
    got=aggregate_direct(mid,eps)  # independent direct eleven-word evaluation
    names=[]
    coeffs={}
    for expr,coeff in got.items():
        name=classify(expr)
        assert sp.simplify(coeff)!=0
        if name=="I":
            continue
        names.append(name)
        coeffs[name]=sp.simplify(coeff)
        by_map.setdefault(name,[]).append((sp.expand(lo),sp.expand(hi)))
    row_maps[row]=names
    row_coeffs[row]=coeffs

# Strong tail check: derived from WORDS, not copied row formulas.
assert set(row_maps["R6"])=={"r_T","r_3a","r_4a","-a","r_2b"}, row_maps["R6"]
assert set(row_maps["R7"])=={"-T","r_3a","r_4a","-a","r_2b"}, row_maps["R7"]
assert len(row_maps["R6"])==5
assert len(row_maps["R7"])==5

# No extra source map survives anywhere.
assert set(by_map)==set(map_exprs), (set(by_map),set(map_exprs))

def merge(intervals):
    # regions are canonically ordered; exact gap sign controls merging
    ints=sorted(intervals,key=lambda q:float(sp.N(q[0],80)))
    out=[]
    for lo,hi in ints:
        if not out:
            out.append([lo,hi]); continue
        gap=sp.expand(lo-out[-1][1])
        assert exact_sign(gap)>=0
        if gap==0:
            out[-1][1]=hi
        else:
            out.append([lo,hi])
    return [(sp.expand(lo),sp.expand(hi)) for lo,hi in out]

got_domains={name:merge(iv) for name,iv in by_map.items()}
expected={
    "+a":[(sp.Integer(0),a+eps)],
    "-a":[(a,T0)],
    "+T":[(sp.Integer(0),eps)],
    "-T":[(T,T0)],
    "r_a":[(sp.Integer(0),eps),(a-eps,a)],
    "r_T":[(sp.Integer(0),T)],
    "r_3a":[(a-eps,T0)],
    "r_4a":[(T-eps,T0)],
    "r_2b":[(2*d-eps,T0)],
}

assert set(got_domains)==set(expected)
for name in expected:
    assert len(got_domains[name])==len(expected[name]), (name,got_domains[name],expected[name])
    for (glo,ghi),(elo,ehi) in zip(got_domains[name],expected[name]):
        assert sp.simplify(glo-elo)==0,(name,"lo",glo,elo)
        assert sp.simplify(ghi-ehi)==0,(name,"hi",ghi,ehi)

# Cross-check the actually derived tail coefficients are the canonical A1
# aggregates from the raw-word script.  This deliberately uses the A1 module's
# own canonical coefficient definitions, not the later Gate1 helper constants.
assert sp.simplify(row_coeffs["R6"]["r_T"]-a1.beta0)==0
assert sp.simplify(row_coeffs["R6"]["r_3a"]-a1.betam)==0
assert sp.simplify(row_coeffs["R6"]["r_4a"]-a1.betaT)==0
assert sp.simplify(row_coeffs["R6"]["-a"]-a1.betap)==0
assert sp.simplify(row_coeffs["R6"]["r_2b"]-a1.betab)==0
assert sp.simplify(row_coeffs["R7"]["-T"]-a1.beta0)==0
assert sp.simplify(row_coeffs["R7"]["r_3a"]-a1.betam)==0
assert sp.simplify(row_coeffs["R7"]["r_4a"]-a1.betaT)==0
assert sp.simplify(row_coeffs["R7"]["-a"]-a1.betap)==0
assert sp.simplify(row_coeffs["R7"]["r_2b"]-a1.betab)==0

print("raw WORDS evaluated directly with independent exact gates:",len(a1.WORDS))
print("derived off-diagonal map alphabet:",sorted(by_map))
print("no tenth nonidentity source map survives: PASS")
print("derived A1 map-domain unions == A7.1--A7.9: PASS")
print("R6 derived five-arm support:",sorted(row_maps["R6"]))
print("R7 derived five-arm support:",sorted(row_maps["R7"]))
print("R6/R7 raw-word coefficients == canonical A1 aggregates: PASS")
print("FIREWALL: graph support only; no reducing-subspace or kernel verdict")
print("SW1 M1-ND IMG4 GATE-A DIRECT-WORD GRAPH CROSS-CHECK: PASS")
