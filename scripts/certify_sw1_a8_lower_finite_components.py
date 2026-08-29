#!/usr/bin/env python3
import sympy as sp

# Exact SW1 constants.
L2, L3 = sp.log(2), sp.log(3)
a = L2/2
b = L3/2
T = 2*a
d = b-a
Delta = sp.simplify(2*d-a)
L = sp.simplify(a-Delta)
eps, s = sp.symbols("eps s", real=True)
T0 = T + eps

# Fixed exact identities.
assert sp.simplify(Delta - (L3 - sp.Rational(3,2)*L2)) == 0
assert sp.simplify(L - (2*L2-L3)) == 0
assert sp.simplify(T - (2*L + 2*Delta)) == 0
assert sp.simplify(2*b - (3*a + Delta)) == 0
assert sp.simplify(a-5*Delta).is_positive is True
assert sp.simplify(L-4*Delta).is_positive is True
assert sp.simplify(a-Delta).is_positive is True

# Lower-chamber separator cell:
# 0 < eps < Delta/2 and eps < s < Delta-eps.
u = s-eps
v = Delta-eps-s
assert sp.simplify(Delta - (2*eps + u + v)) == 0

# Four middle P/Qbar residues (no modulo wrap because 4 Delta < L).
p = {j: sp.simplify(s+j*Delta) for j in range(4)}
q = {j: sp.simplify((4-j)*Delta-s) for j in range(4)}

# Exact endpoint checks reduced to positive fixed/slack pieces.
assert sp.simplify(p[0]) == s
assert sp.simplify(q[3]) == eps+v
assert sp.simplify(L-p[3] - ((a-5*Delta)+(Delta-s))) == 0
assert sp.simplify(L-q[0] - ((a-5*Delta)+s)) == 0

# Third lift criterion: r+2L<T0 iff r<2Delta+eps.
threshold = 2*Delta + eps
assert sp.simplify(T0-2*L-threshold) == 0

# Existence signs for the third lifts.
third_diff = {
    ("P",0): sp.simplify(threshold-p[0]),
    ("P",1): sp.simplify(threshold-p[1]),
    ("P",2): sp.simplify(p[2]-threshold),
    ("P",3): sp.simplify(p[3]-threshold),
    ("Q",0): sp.simplify(q[0]-threshold),
    ("Q",1): sp.simplify(q[1]-threshold),
    ("Q",2): sp.simplify(threshold-q[2]),
    ("Q",3): sp.simplify(threshold-q[3]),
}
expected_identities = {
    ("P",0): 2*Delta+eps-s,
    ("P",1): v+2*eps,
    ("P",2): u,
    ("P",3): Delta+u,
    ("Q",0): Delta+v,
    ("Q",1): v,
    ("Q",2): eps+s,
    ("Q",3): Delta+eps+s,
}
for key, expr in third_diff.items():
    assert sp.simplify(expr-expected_identities[key]) == 0

# Physical middle states: exactly five in each layer.
states = {
    0: [("P",0),("P",1),("P",2),("Q",0),("Q",1)],
    1: [("P",0),("P",1),("P",2),("Q",0),("Q",1)],
    2: [("P",0),("P",1),("Q",0),("Q",1),("Q",2)],
    3: [("P",0),("P",1),("Q",0),("Q",1),("Q",2)],
}
assert sum(len(vs) for vs in states.values()) == 20

left = {
    0:{("P",1),("P",2),("Q",0),("Q",1)},
    1:{("P",2),("Q",0),("Q",1)},
    2:{("Q",0),("Q",1)},
    3:{("Q",0)},
}
right = {
    0:{("P",0)},
    1:{("P",0),("P",1)},
    2:{("P",0),("P",1),("Q",2)},
    3:{("P",0),("P",1),("Q",1),("Q",2)},
}
for j in range(4):
    assert left[j].isdisjoint(right[j])
    assert left[j] | right[j] == set(states[j])

# A7 local index shifts and sheet changes.
shift = {
    ("P","+a"):("P",+1), ("P","-a"):("P",-1),
    ("P","+T"):("P",+2), ("P","-T"):("P",-2),
    ("Q","+a"):("Q",-1), ("Q","-a"):("Q",+1),
    ("Q","+T"):("Q",-2), ("Q","-T"):("Q",+2),
    ("P","r_a"):("Q",+3), ("Q","r_a"):("P",-3),
    ("P","r_T"):("Q",+2), ("Q","r_T"):("P",-2),
    ("P","r_3a"):("Q",+1), ("Q","r_3a"):("P",-1),
    ("P","r_4a"):("Q",0), ("Q","r_4a"):("P",0),
    ("P","r_2b"):("Q",0), ("Q","r_2b"):("P",0),
}
maps = {
    "+a": lambda x: x+a,
    "-a": lambda x: x-a,
    "+T": lambda x: x+T,
    "-T": lambda x: x-T,
    "r_a": lambda x: a-x,
    "r_T": lambda x: T-x,
    "r_3a": lambda x: 3*a-x,
    "r_4a": lambda x: 4*a-x,
    "r_2b": lambda x: 2*b-x,
}
assert max(abs(jump) for (_,jump) in shift.values()) == 3

def value(j, sheet, k):
    return sp.simplify((p[j] if sheet=="P" else q[j]) + k*L)

def side(j, sheet, k):
    if j <= -1:
        return "L"
    if j >= 4:
        return "R"
    pair=(sheet,k)
    if pair in left[j]:
        return "L"
    if pair in right[j]:
        return "R"
    return None

# Exhaustively enumerate the 20*9 formal source-map possibilities.
cross = []
middle_unmatched = []
for j in range(4):
    for sheet,k in states[j]:
        src_side = side(j,sheet,k)
        x = value(j,sheet,k)
        for name, f in maps.items():
            target_sheet, jump = shift[(sheet,name)]
            jj = j+jump
            y = sp.simplify(f(x))
            if jj <= -1 or jj >= 4:
                tgt_side = "L" if jj <= -1 else "R"
                if tgt_side != src_side:
                    cross.append((j,sheet,k,name))
            else:
                matches=[]
                for tsh,tk in states[jj]:
                    if tsh == target_sheet and sp.simplify(y-value(jj,tsh,tk)) == 0:
                        matches.append((tsh,tk))
                if len(matches) == 1:
                    tsh,tk=matches[0]
                    assert side(jj,tsh,tk) == src_side
                else:
                    assert len(matches) == 0
                    middle_unmatched.append((j,sheet,k,name,jj,target_sheet))

expected_cross = [
    (0,"P",0,"-a"),
    (0,"P",0,"-T"),
    (1,"P",0,"-T"),
    (1,"P",1,"-T"),
    (2,"Q",2,"r_a"),
    (1,"P",2,"r_a"),
    (2,"Q",0,"-T"),
    (2,"Q",1,"-T"),
    (3,"Q",0,"-a"),
    (3,"Q",0,"-T"),
]
assert sorted(cross) == sorted(expected_cross)
assert len(cross) == 10

# Universal exact positivity on the closed parameter triangle
# 0<=eps<=Delta/2, eps<=s<=Delta-eps.
vertices = [
    {eps:0, s:0},
    {eps:0, s:Delta},
    {eps:Delta/2, s:Delta/2},
]
def positive_on_triangle(expr):
    vals=[sp.simplify(expr.subs(vtx)) for vtx in vertices]
    return all(v.is_positive is True for v in vals), vals

src = {(j,sh,k):value(j,sh,k) for j in range(4) for sh,k in states[j]}

# The exact source-gate inequalities killing all ten cross candidates.
checks = [
    ("P0^0 -a inactive", a-src[(0,"P",0)]),
    ("P0^0 -T inactive", T-src[(0,"P",0)]),
    ("P1^0 -T inactive", T-src[(1,"P",0)]),
    ("P1^1 -T inactive", T-src[(1,"P",1)]),
    ("Q2^2 r_a above a", src[(2,"Q",2)]-a),
    ("P1^2 r_a above a", src[(1,"P",2)]-a),
    ("Q2^0 -T inactive", T-src[(2,"Q",0)]),
    ("Q2^1 -T inactive", T-src[(2,"Q",1)]),
    ("Q3^0 -a inactive", a-src[(3,"Q",0)]),
    ("Q3^0 -T inactive", T-src[(3,"Q",0)]),
]
for label, expr in checks:
    ok, vals = positive_on_triangle(sp.simplify(expr))
    assert ok, (label, vals)

# Cross-source formulas advertised in A8.
assert sp.simplify(src[(0,"P",0)]-s)==0
assert sp.simplify(src[(1,"P",0)]-(s+Delta))==0
assert sp.simplify(src[(1,"P",1)]-(a+s))==0
assert sp.simplify(src[(2,"Q",2)]-(T-s))==0
assert sp.simplify(src[(1,"P",2)]-(T-Delta+s))==0
assert sp.simplify(src[(2,"Q",0)]-(2*Delta-s))==0
assert sp.simplify(src[(2,"Q",1)]-(a+Delta-s))==0
assert sp.simplify(src[(3,"Q",0)]-(Delta-s))==0

# Undirected-edge sanity: inverse translation domains match and reflection domains are invariant.
assert sp.simplify((a+eps+a)-T0) == 0
assert sp.simplify((eps+T)-T0) == 0
assert sp.simplify((3*a-T0)-(a-eps)) == 0
assert sp.simplify((4*a-T0)-(T-eps)) == 0
assert sp.simplify((2*b-T0)-(2*d-eps)) == 0

# Exact irrationality reduction:
# Delta/L=m/n implies (2n+2m)log3=(3n+4m)log2.
# Unique prime factorization forces both coefficients to vanish.
M = sp.Matrix([[2,2],[3,4]])
assert M.det() == 2

print("SW1-A8 LOWER FINITE RAW COMPONENTS CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("20 middle physical states exhaustively certified")
print("A8 left/right partition certified in all four middle layers")
print("180 source-map cases exhaustively scanned from the A7 jump table")
print("exactly 10 formal cross candidates found; all 10 universally gate-inactive")
print("A7 edge range <=3 and inverse/reflection symmetry checks certified")
print("irrationality reduces to a nondegenerate integer 2x2 system (plus unique factorization)")
print("scope: raw A1 separator ledger; KNF J_R edges, Schur injectivity, HT-RED, Objekt X, RH excluded")
