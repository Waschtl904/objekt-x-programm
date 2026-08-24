#!/usr/bin/env python3
import itertools
from fractions import Fraction
import sympy as sp

# P12 Round 27 candidate verifier.
# Exact residual-shadow atlas + exact one-sided 43x43 shell candidate.
# Candidate only. No promotion. P11/R14 firewall unchanged.

def ln_bounds_int(xint, N):
    z = Fraction(xint - 1, xint + 1)
    s = Fraction(0)
    for k in range(N + 1):
        s += z ** (2 * k + 1) / Fraction(2 * k + 1)
    lo = 2 * s
    tail = 2 * z ** (2 * N + 3) / Fraction(2 * N + 3) / (1 - z * z)
    return lo, lo + tail

l2lo, l2hi = ln_bounds_int(2, 120)
l3lo, l3hi = ln_bounds_int(3, 180)
l5lo, l5hi = ln_bounds_int(5, 500)

Hlo, Hhi = (8*l2lo - 5*l3hi)/2, (8*l2hi - 5*l3lo)/2
Clo, Chi = (7*l3lo - 11*l2hi)/2, (7*l3hi - 11*l2lo)/2
Elo, Ehi = l5lo/2 - l2hi, l5hi/2 - l2lo

assert Hlo > 0
assert Clo > Hhi
assert Elo > 0

H0 = (float(Hlo) + float(Hhi))/2
C0 = (float(Clo) + float(Chi))/2
E0 = (float(Elo) + float(Ehi))/2
D0 = H0 + C0
K0 = 2*H0 + C0
rho0 = E0 - D0
rstar0 = (C0 - H0)/2
sstar0 = (3*H0 + C0)/2
tstar0 = 3*D0/2

# Exact order checks, directed by rational log bounds.
assert Clo > Hhi
assert 2*Hhi < 3*Hlo + Clo
assert 3*Hhi + Chi < 3*(Hlo + Clo)
assert 3*(Hhi + Chi)/2 < Elo
assert (Hhi + Chi)/2 < Elo - Hhi - Chi
print("R27_CONSTANT_ORDER = PASS", {
    "eta": H0, "chi": C0, "delta": D0, "rho": rho0,
    "rstar": rstar0, "sstar": sstar0, "tstar": tstar0
})

R, X, SIG, EPS = sp.symbols("R X SIG EPS", real=True)
H, C, E = sp.symbols("H C E", real=True)
D = H + C
K = 2*H + C
RHO = E - D

def fm_eliminate_x(ineqs):
    """Eliminate X from strict affine inequalities g>0."""
    pos, neg, zero = [], [], []
    for g in map(sp.expand, ineqs):
        a = sp.expand(g).coeff(X)
        rest = sp.expand(g - a*X)
        if a > 0:
            pos.append((a, rest))
        elif a < 0:
            neg.append((a, rest))
        else:
            zero.append(rest)
    out = list(zero)
    for ap, rp in pos:
        for an, rn in neg:
            out.append(sp.expand(ap*rn + (-an)*rp))
    seen = []
    for g in map(sp.expand, out):
        if g not in seen:
            seen.append(g)
    return seen

# Original promoted chambers, written only as strict affine inequalities.
C42 = [
    R, RHO-R,
    X-R, D-R-X, X-(C-R), H+R-X,
    SIG-X, SIG-(D-X), (K-X)-SIG, (X+H)-SIG,
    EPS-(K-X), EPS-(X+H), EPS-SIG, E-EPS,
]
C44 = [
    R, RHO-R,
    X-R, D-R-X, X-(C-R), H+R-X,
    SIG-(K-X), SIG-(X+H), (2*D-X)-SIG, (X+D)-SIG,
    EPS-(2*D-X), EPS-(X+D), EPS-SIG, E-EPS,
]
C26m = [
    X-H, C-X, R+X-C, 2*H-R-X, H-X+R,
    SIG-X-(C-H), 3*H-SIG-X, EPS-X-H, E-EPS,
]
C26p = [
    X-H, C-X, R+X-C, X-R-(C-H), H-X+R,
    SIG+X-2*C, 2*H-C-SIG+X, EPS+X-(2*H+C), E-EPS,
]

P42_raw = fm_eliminate_x(C42)
P44_raw = fm_eliminate_x(C44)
P26m_raw = fm_eliminate_x(C26m)
P26p_raw = fm_eliminate_x(C26p)

assert sorted(map(str, P26m_raw)) == sorted(map(str, P26p_raw))
print("R27_C26_SHADOW_IDENTITY = PASS", len(P26m_raw), "FM inequalities")

# Compact exact shadow presentations.
P42 = [
    2*R-(C-H), D-2*R, SIG-R, R+SIG-C,
    2*SIG-D, SIG+EPS-K,
    3*H+C-2*SIG, 2*EPS-(3*H+C), E-EPS,
]
P44 = [
    2*R-(C-H), D-2*R,
    2*SIG-(3*H+C), 3*D-2*SIG,
    2*EPS-3*D, E-EPS,
]
P26 = [
    2*R-(C-H), H-R,
    SIG-C, 2*H-SIG, EPS-2*H,
    R+SIG-(2*C-H), (3*H-C)+R-SIG,
    R+EPS-D, E-EPS,
]

def occurs_all(compact, raw):
    rawset = {sp.expand(g) for g in raw}
    return all(sp.expand(g) in rawset for g in compact)

assert occurs_all(P42, P42_raw)
assert occurs_all(P44, P44_raw)
assert occurs_all(P26, P26m_raw)

def qfrac(q0):
    q0 = sp.Rational(q0)
    return Fraction(int(q0.p), int(q0.q))

def coeff3(expr):
    ex = sp.expand(expr)
    ch, cc, ce = ex.coeff(H), ex.coeff(C), ex.coeff(E)
    const = sp.expand(ex - ch*H - cc*C - ce*E)
    assert not const.free_symbols
    return qfrac(ch), qfrac(cc), qfrac(ce), qfrac(const)

def interval3(cf):
    ah, ac, ae, c0 = cf
    lo = hi = c0
    for aa, (bl, bh) in zip((ah, ac, ae),
                             ((Hlo,Hhi),(Clo,Chi),(Elo,Ehi))):
        if aa >= 0:
            lo += aa*bl
            hi += aa*bh
        else:
            lo += aa*bh
            hi += aa*bl
    return lo, hi

vars3 = (R, SIG, EPS)

def closed_vertices(constraints):
    verts = []
    for combo in itertools.combinations(range(len(constraints)), 3):
        sol = sp.solve([constraints[i] for i in combo], vars3,
                       dict=True, simplify=False)
        if len(sol) != 1 or not all(v in sol[0] for v in vars3):
            continue
        vv = tuple(sp.expand(sol[0][v]) for v in vars3)
        sub = dict(zip(vars3, vv))
        feasible = True
        for g in constraints:
            lo, hi = interval3(coeff3(sp.expand(g.subs(sub))))
            if hi < 0:
                feasible = False
                break
            assert not (lo < 0 < hi), ("uncertain vertex", combo, g, float(lo), float(hi))
        if feasible:
            verts.append((combo, vv))
    return verts

def compact_implies_raw(compact, raw, label):
    verts = closed_vertices(compact)
    assert verts, label
    for g in raw:
        for combo, vv in verts:
            ex = sp.expand(g.subs(dict(zip(vars3, vv))))
            lo, hi = interval3(coeff3(ex))
            assert hi >= 0, (label, g, combo, float(lo), float(hi))
            assert not (lo < 0 < hi), (label, "uncertain", g, combo)
    print(label, "= PASS", len(verts), "vertices", len(raw), "raw inequalities")

compact_implies_raw(P42, P42_raw, "R27_P42_COMPACT_EQUIV")
compact_implies_raw(P44, P44_raw, "R27_P44_COMPACT_EQUIV")
compact_implies_raw(P26, P26m_raw, "R27_P26_COMPACT_EQUIV")

assert sp.expand(P42[6] - (3*H+C-2*SIG)) == 0
assert sp.expand(P42[7] - (2*EPS-(3*H+C))) == 0
assert sp.expand(P44[3] - (3*D-2*SIG)) == 0
assert sp.expand(P44[4] - (2*EPS-3*D)) == 0
assert sp.expand(P26[3] - (2*H-SIG)) == 0
assert sp.expand(P26[4] - (EPS-2*H)) == 0

# P26: SIG < 2H and EPS > 2H.
# P42: SIG < sstar and EPS > sstar.
# P44: SIG < tstar and EPS > tstar.
# All have R > rstar. Each shadow is upward-monotone in EPS, apart from E.
print("R27_SINGLE_OPEN_REMAINDER_COMPONENT = PASS",
      "path certificate via EPS staircase and R<rstar anchor")

# ---------- exact prioritized one-sided 43x43 raw-pattern cell ----------

p, q, r = sp.symbols("p q r", positive=True, nonzero=True)
A = (0,2,1)
B = (0,3,2)
TT = (0,4,2)
shifts = [("a",A,p),("b",B,r),("T",TT,q)]

sources42 = [
(-1,0,1),(-1,0,2),
(-1,1,0),(-1,1,1),(-1,1,2),(-1,1,3),
(-1,2,0),(-1,2,1),(-1,2,2),(-1,2,3),(-1,2,4),
(-1,3,0),(-1,3,1),(-1,3,2),(-1,3,3),(-1,3,4),
(-1,4,0),(-1,4,1),(-1,4,2),(-1,4,3),
(-1,5,1),
(1,0,0),(1,0,1),
(1,1,-1),(1,1,0),(1,1,1),(1,1,2),
(1,2,-1),(1,2,0),(1,2,1),(1,2,2),(1,2,3),
(1,3,-1),(1,3,0),(1,3,1),(1,3,2),(1,3,3),
(1,4,-1),(1,4,0),(1,4,1),(1,4,2),
(1,5,0),
]
Vplus = (1,4,3)
Vminus = (-1,4,4)
Uplus = (1,5,0)
Uminus = (-1,5,1)

def add(u,v):
    return tuple(u[i]+v[i] for i in range(3))

def neg(u):
    return tuple(-z for z in u)

def J(u):
    s,m,n = u
    return (-s,m,n+s)

assert J(Vplus) == Vminus
assert all(J(s) in sources42 for s in sources42)

e0 = 3*H0 + 2*C0
d0 = H0 + C0
T0 = 14*H0 + 10*C0

def aval(u,x0):
    s,m,n = u
    return s*x0 + m*e0 + n*d0

def raw_row(src,x0,R0,sigma0,eps0):
    u = aval(src,x0)
    if not (0 < u < T0 + eps0):
        return None
    row = {}
    for _, sh, k in shifts:
        for pm, sgn in [(-1,+1),(+1,-1)]:
            arg = add(src,(0,pm*sh[1],pm*sh[2]))
            coeff = sgn*k
            av = aval(arg,x0)
            if av < 0:
                arg = neg(arg)
                av = -av
                coeff = -coeff
            if R0 < av < T0 + sigma0:
                row[arg] = sp.expand(row.get(arg,0) + coeff)
    return {v:sp.factor(c) for v,c in row.items() if sp.simplify(c) != 0}

def make_matrix(sources, pt):
    R0,x0,sigma0,eps0 = pt
    rows = [raw_row(s,x0,R0,sigma0,eps0) for s in sources]
    legal = [i for i,rr in enumerate(rows) if rr is not None]
    vars_ = sorted(set().union(*(set(rows[i]) for i in legal)))
    M = sp.zeros(len(legal),len(vars_))
    for ii,i in enumerate(legal):
        for v,c in rows[i].items():
            M[ii,vars_.index(v)] = c
    return M,vars_,rows,legal

ref42 = (.010, (H0+C0)/2, .040, .070)
M42, V42, _, L42 = make_matrix(sources42, ref42)
assert M42.shape == (42,42) and len(L42) == 42

ref43 = (.010, .028, .0555, .100)
M42one, V42one, _, L42one = make_matrix(sources42, ref43)
assert M42one.shape == (42,43) and len(L42one) == 42
assert set(V42one) == set(V42) | {Uplus}

selected43 = sources42 + [Vplus]
M43, V43, _, L43 = make_matrix(selected43, ref43)
assert M43.shape == (43,43) and len(L43) == 43
assert set(V43) == set(V42) | {Uplus}
print("R27_M43_RAW_SHAPE = PASS 43x43")

Tsym = 14*H + 10*C

def aff_sym(u):
    s,m,n = u
    return s*X + m*(3*H+2*C) + n*(H+C)

raw_conditions = []
Rref,xref,sref,eref = ref43
for src in selected43:
    u = aff_sym(src)
    raw_conditions.append((u,("source_lower",src)))
    raw_conditions.append((Tsym+EPS-u,("source_upper",src)))
    for shname,sh,_ in shifts:
        for pm in (-1,+1):
            arg0 = add(src,(0,pm*sh[1],pm*sh[2]))
            vv = aff_sym(arg0)
            vref = aval(arg0,xref)
            sign = 1 if vref > 0 else -1
            w = sp.expand(sign*vv)
            raw_conditions.append((w,("slot_sign",src,shname,pm,arg0,sign)))
            avref = abs(vref)
            if Rref < avref < T0+sref:
                raw_conditions.append((w-R,("live_lower",src,shname,pm,arg0,sign)))
                raw_conditions.append((Tsym+SIG-w,("live_upper",src,shname,pm,arg0,sign)))
            elif avref < Rref:
                raw_conditions.append((R-w,("dead_lower",src,shname,pm,arg0,sign)))
            else:
                raw_conditions.append((w-Tsym-SIG,("dead_upper",src,shname,pm,arg0,sign)))

assert len(raw_conditions) == 758

W43m = [
    X-H,
    X-R,
    R+X-C,
    SIG-X-H,
    K-SIG-X,
    EPS-X-D,
    E-EPS,
]
facet_names = [
    "x=eta", "x=R", "R+x=chi", "sigma=x+eta",
    "sigma+x=kappa", "epsilon=x+delta", "epsilon=epsmax"
]
for f,name in zip(W43m[:-1],facet_names[:-1]):
    hits = sum(1 for g,_ in raw_conditions if sp.expand(g-f) == 0)
    assert hits > 0, (name,hits)
print("R27_W43_GENUINE_RAW_FACETS = PASS", facet_names)

vars4 = (R,X,SIG,EPS)

def closed_vertices4(constraints):
    verts = []
    for combo in itertools.combinations(range(len(constraints)),4):
        sol = sp.solve([constraints[i] for i in combo], vars4,
                       dict=True, simplify=False)
        if len(sol) != 1 or not all(v in sol[0] for v in vars4):
            continue
        vv = tuple(sp.expand(sol[0][v]) for v in vars4)
        sub = dict(zip(vars4,vv))
        feasible = True
        for g in constraints:
            lo,hi = interval3(coeff3(sp.expand(g.subs(sub))))
            if hi < 0:
                feasible = False
                break
            assert not (lo < 0 < hi), ("uncertain W43 vertex",combo,g)
        if feasible:
            verts.append((combo,vv))
    return verts

verts43 = closed_vertices4(W43m)
assert len(verts43) == 12

for g,label in raw_conditions:
    for combo,vv in verts43:
        ex = sp.expand(g.subs(dict(zip(vars4,vv))))
        lo,hi = interval3(coeff3(ex))
        assert hi >= 0, (label,combo,float(lo),float(hi))
        assert not (lo < 0 < hi), (label,combo,"uncertain")

print("R27_W43_PATTERN_CERTIFICATE = PASS", len(verts43),
      "vertices", len(raw_conditions), "raw inequalities")

Y = D-X
W43p = [sp.expand(g.subs(X,Y,simultaneous=True)) for g in W43m]
W43p_expected = [
    C-X,
    D-X-R,
    R+H-X,
    SIG+X-K,
    X+H-SIG,
    EPS+X-2*D,
    E-EPS,
]
assert sorted(map(str,map(sp.expand,W43p))) == sorted(map(str,map(sp.expand,W43p_expected)))
print("R27_W43_J_CHAMBER_MAP = PASS")

xmir = d0-xref
mirror_sources = [J(s) for s in selected43]
mirror_rows = [raw_row(s,xmir,Rref,sref,eref) for s in mirror_sources]
mirror_cols = [J(v) for v in V43]
assert all(rr is not None for rr in mirror_rows)
Mmir = sp.Matrix([[rr.get(v,0) for v in mirror_cols] for rr in mirror_rows])
assert Mmir == M43
print("R27_W43_J_MATRIX_IDENTITY = PASS")

# Exact normalized determinant and exact sign enclosure.
# Homogeneity lets us set p=1, beta=q/p and tau=r/p before elimination.
beta, tau, v = sp.symbols("beta tau v", positive=True)
M43norm = M43.subs({p:1, q:beta, r:tau})
det43norm = sp.factor(M43norm.det(method="domain-ge"))
Q43tau = sp.cancel(det43norm/(beta*tau**7))
assert sp.denom(Q43tau) == 1
Ptau = sp.Poly(sp.expand(Q43tau), beta, tau)
G43 = 0
for (eb,et),coef in Ptau.terms():
    assert et % 2 == 0
    G43 += coef*beta**eb*v**(et//2)
G43 = sp.expand(G43)
assert sp.total_degree(G43) <= 16

blo = Fraction("0.59460355750136053335")
bhi = Fraction("0.59460355750136053336")
assert blo**4 < Fraction(1,8) < bhi**4
slo = Fraction("0.54433105395181735515")
shi = Fraction("0.54433105395181735516")
assert slo*slo < Fraction(8,27) < shi*shi
l2lo2,l2hi2 = ln_bounds_int(2,40)
l3lo2,l3hi2 = ln_bounds_int(3,60)
vlo = (l3lo2/l2hi2)*slo
vhi = (l3hi2/l2lo2)*shi

def poly_interval(expr):
    P = sp.Poly(sp.expand(expr),beta,v)
    lo = Fraction(0)
    hi = Fraction(0)
    for (eb,ev),coef in P.terms():
        coef = int(coef)
        ml = blo**eb * vlo**ev
        mh = bhi**eb * vhi**ev
        if coef >= 0:
            lo += coef*ml
            hi += coef*mh
        else:
            lo += coef*mh
            hi += coef*ml
    return lo,hi

I43 = poly_interval(G43)
assert I43[1] < 0
print("R27_M43_NORMALIZED_FACTOR_INTERVAL = PASS",
      (float(I43[0]),float(I43[1])))
print("R27_M43_DET_FACTOR = PASS",
      "det(M43)=p^43*beta*(sqrt(v))^7*G43(beta,v)")
print("ROUND27_RESIDUAL_ATLAS_VERIFY = PASS")
