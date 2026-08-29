#!/usr/bin/env python3
"""SW1-A9-SEP-BYPASS(part): exact regular-phase KNF bypass certificate.

Result:
On the open lower-chamber subregion
    0 < R < epsilon < Delta/2,
    epsilon < s_* + R,
where s_* = L/2 - 2 Delta,
there exists a regular A8 phase
    epsilon < s < Delta-epsilon, s != Delta/2,
with u=s-s_* in (0,R), for which the certified free Gram graph has an
explicit path from local index -1 to local index 6.

This disproves universal transfer of the A8 separator to the KNF Gram graph
on that subregion. It does NOT prove absence of every possible separator or
infinite components.

No numerical gate or sign decision is used.
"""
import sympy as sp

# ----- Fixed exact constants -----
L2=sp.log(2)
L3=sp.log(3)
Delta=L3-sp.Rational(3,2)*L2
L=2*L2-L3
sstar=sp.simplify(L/2-2*Delta)

# L-4Delta = log(256/243)>0 -> s_*>0.
assert 256>243
assert sp.simplify(sstar-sp.Rational(1,2)*(L-4*Delta))==0

# 5Delta-L = 1/2 log(3^12/2^19)>0 -> s_*<Delta/2.
assert 3**12 > 2**19
assert sp.simplify(Delta/2-sstar-sp.Rational(1,2)*(5*Delta-L))==0

# ----- Abstract positive-slack parameterization -----
# A=s-epsilon>0
# B=Delta-epsilon-s>0
# U=s-s_*>0
# V=s_*+R-s>0
# E=epsilon-R>0
A,B,U,V,E=sp.symbols("A B U V E", positive=True)

# This parameterization exactly realizes those five strict inequalities.
G=A+V+E                      # s_*
R=U+V
eps=U+V+E
s=G+U
D=A+B+2*U+2*V+2*E           # Delta
LL=4*D+2*G                   # L, since G=L/2-2D

assert sp.simplify(s-eps-A)==0
assert sp.simplify(D-eps-s-B)==0
assert sp.simplify(s-G-U)==0
assert sp.simplify(G+R-s-V)==0
assert sp.simplify(eps-R-E)==0
assert sp.simplify(D-2*eps-(A+B))==0

a=LL+D
b=sp.Rational(3,2)*LL+2*D
T=2*LL+2*D
d=LL/2+D
e=LL/2
T0=T+eps

# ----- Explicit physical representatives -----
y_m1=s+LL/2-D
x1=sp.Rational(3,2)*LL+3*D-s
x2=sp.Rational(3,2)*LL+D+s
x3=sp.Rational(3,2)*LL+2*D-s
x4=sp.Rational(3,2)*LL+2*D+s
x5=sp.Rational(3,2)*LL+D-s
x6=sp.Rational(3,2)*LL+3*D+s
x7=sp.Rational(3,2)*LL-s
x8=sp.Rational(3,2)*LL+4*D+s
x9=LL+4*D+s
y_6=LL-2*D-s

# Exact affine path:
# P_{-1,1} --r_T--> Qbar_{1,1} --r_2b--> P_{1,1}
# --r_3a--> Qbar_{2,1} --r_2b--> P_{2,1}
# --r_3a--> Qbar_{3,1} --r_2b--> P_{3,1}
# --r_3a--> Qbar_{4,1} --r_2b--> P_{4,1}
# --tau_{-e} (KNF)--> P_{4,0} --r_T--> Qbar_{6,0}.
path_checks=[
    T-y_m1-x1,
    2*b-x1-x2,
    3*a-x2-x3,
    2*b-x3-x4,
    3*a-x4-x5,
    2*b-x5-x6,
    3*a-x6-x7,
    2*b-x7-x8,
    x8-e-x9,
    T-x9-y_6,
]
assert all(sp.simplify(z)==0 for z in path_checks)

# Sheet/index congruences modulo L; each displayed representative differs from
# the formal P/Qbar phase by an integer multiple of L.
P=lambda n,eta: s+n*D+eta*LL/2
Q=lambda n,eta: 4*D-s-n*D+eta*LL/2
labels=[
    (y_m1,P(-1,1),0),
    (x1,Q(1,1),1),
    (x2,P(1,1),1),
    (x3,Q(2,1),1),
    (x4,P(2,1),1),
    (x5,Q(3,1),1),
    (x6,P(3,1),1),
    (x7,Q(4,1),1),
    (x8,P(4,1),1),
    (x9,P(4,0),1),
    (y_6,Q(6,0),1),
]
for x,base,k in labels:
    assert sp.simplify(x-base-k*LL)==0

# ----- Gate verification -----
low_r2b=2*d-eps
low_r3a=a-eps

margins={
    # r_T at the two ends
    "y_m1>0":y_m1,
    "T-y_m1":T-y_m1,
    "x9>0":x9,
    "T-x9":T-x9,

    # r_2b sources x1,x3,x5,x7
    "x1-r2b_low":x1-low_r2b, "T0-x1":T0-x1,
    "x3-r2b_low":x3-low_r2b, "T0-x3":T0-x3,
    "x5-r2b_low":x5-low_r2b, "T0-x5":T0-x5,
    "x7-r2b_low":x7-low_r2b, "T0-x7":T0-x7,

    # r_3a sources x2,x4,x6
    "x2-r3a_low":x2-low_r3a, "T0-x2":T0-x2,
    "x4-r3a_low":x4-low_r3a, "T0-x4":T0-x4,
    "x6-r3a_low":x6-low_r3a, "T0-x6":T0-x6,

    # free-coordinate firewall: endpoints below reconstructed A_- window
    "a-R-y_m1":a-R-y_m1,
    "a-R-y_6":a-R-y_6,
}

# Every interior path point lies strictly above a, hence cannot be A_-.
for name,x in {
    "x1":x1,"x2":x2,"x3":x3,"x4":x4,"x5":x5,
    "x6":x6,"x7":x7,"x8":x8,"x9":x9,
}.items():
    margins[name+"-a"]=x-a

for name,m in margins.items():
    m=sp.factor(sp.expand(m))
    assert m.is_positive is True, (name,m)

# The unique KNF step is exactly T+u -> B+u with u in (0,R).
u=sp.simplify(s-G)
assert sp.simplify(u-U)==0
assert sp.simplify(x8-(T+u))==0
assert sp.simplify(x9-(b+u))==0
assert u.is_positive is True
assert sp.simplify(R-u).is_positive is True

# The J1(full) coefficient on B+ <-> T+ is strictly nonzero with exact margin.
K=8+L2-2*sp.sqrt(2)*L2
assert sp.simplify(K-6).is_positive is True

print("SW1-A9 REGULAR-PHASE KNF BYPASS CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("fixed constants: 0 < s_* < Delta/2 certified exactly")
print("parameter condition: epsilon < s_* + R")
print("regular phase interval is nonempty; choose s != Delta/2")
print("u=s-s_* lies strictly in (0,R)")
print("explicit certified path: index -1 -> 6")
print("all r_T, r_2b, r_3a gates certified by exact positive margins")
print("all path vertices are free; reconstructed A_- interval avoided")
print("unique KNF step is T+u <-> B+u = tau_{-e}, J1 coefficient nonzero")
print("FIREWALL: disproves universal A8-separator transfer only on this subregion")
print("           no claim that all separators fail or that components are infinite")
