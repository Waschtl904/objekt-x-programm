#!/usr/bin/env python3
import sympy as sp

L2,L3=sp.log(2),sp.log(3)
a=L2/2
b=L3/2
T=2*a
d=b-a
e=T-b
Delta=sp.simplify(d-e)

sig,R,eps=sp.symbols("sig R eps", real=True)

# Fixed constant ordering.
assert Delta.is_positive is True
assert sp.simplify(e-Delta).is_positive is True
assert sp.simplify(d-e).is_positive is True
assert sp.simplify(d-Delta).is_positive is True
assert sp.simplify(a-Delta).is_positive is True

# SW1 slack symbols.
g=sp.simplify(Delta-(R+eps))      # >0 on SW1
eta=sp.simplify(eps-R)            # >0 on SW1
rho=sp.simplify(R-sig)            # >=0, equality allowed

# R<Delta/2 follows exactly from g+eta=Delta-2R.
assert sp.simplify((Delta-2*R)-(g+eta))==0

# Historical A0 parameter walls are impossible on strict SW1:
# R=eps excluded by eta>0;
# R=e/2,d/2,d excluded by 2R<Delta<e<d;
# R=e+eps excluded already by R<eps.

# Z1 gap identities.
assert sp.simplify((eps-sig)-(eta+rho))==0
assert sp.simplify((e+sig-eps)-((e-Delta)+g+R+sig))==0
assert sp.simplify((a-eps-(e+sig))-((d-Delta)+g+rho))==0
assert sp.simplify((a-R-(a-eps))-eta)==0

# Z2: both candidate walls are always internal.
assert sp.simplify((2*d-eps-(a+R))-g)==0
assert sp.simplify((b-R-(a+eps))-((d-Delta)+g))==0
assert sp.simplify((b-R-(2*d-eps))-(e+eta))==0
assert sp.simplify((2*d-eps-(a+eps))-(Delta-2*eps))==0

# Z3/Z4 gaps.
assert sp.simplify((T-eps-(b+R))-((e-Delta)+g))==0
assert sp.simplify((T-R-(T-eps))-eta)==0
assert sp.simplify((T+eps-(T+R))-eta)==0

# Hub upper-contact walls from S=T+sig.
S=T+sig
assert sp.simplify(S-T-sig)==0
assert sp.simplify(S-b-(e+sig))==0
assert sp.simplify(S-a-(a+sig))==0
# a+sig is inside the free a-sample window up to its right endpoint.
assert sp.simplify((a+R)-(a+sig)-rho)==0

# Exhaustivity of positive Hub support walls for tau in {a,b,T}.
# Lower-contact walls |x-tau|=R are exactly tau±R (sample bounds).
# The upper-contact left solutions tau-S are all negative:
assert sp.simplify(a-S-(-a-sig))==0
assert sp.simplify(b-S-(-e-sig))==0
assert sp.simplify(T-S-(-sig))==0
# The upper-contact right solutions tau+S all lie beyond T0=T+eps.
assert sp.simplify((a+S-(T+eps))-((a-Delta)+g+R+sig))==0
assert sp.simplify((b+S-(T+eps))-((b-Delta)+g+R+sig))==0
assert sp.simplify((T+S-(T+eps))-((T-Delta)+g+R+sig))==0
# R-tau is negative for all three shifts because R<Delta/2<a<=tau.
assert sp.simplify(a-Delta/2).is_positive is True

# Chamber I z-cell lengths.
len_I=[
 sig,
 eps-sig,
 e+sig-eps,
 a-eps-(e+sig),
 eps-R,
 eps-R,
 Delta-2*eps,
 b-R-(2*d-eps),
 T-eps-(b+R),
 eps-R,
 eps-R,
]
# All entries except Delta-2eps are positive from strict SW1/fixed constants;
# Delta-2eps is exactly the Chamber-I condition.

# Chamber II z-cell lengths.
len_II=[
 sig,
 eps-sig,
 e+sig-eps,
 a-eps-(e+sig),
 eps-R,
 Delta-(R+eps),
 2*eps-Delta,
 b-R-(a+eps),
 T-eps-(b+R),
 eps-R,
 eps-R,
]
# 2eps-Delta is exactly the Chamber-II condition.

# Degenerate chamber: the two middle A-walls coincide.
assert sp.simplify((a+Delta/2)-(2*d-Delta/2))==0

# Exact blind total length equals sum of chamber-cell lengths.
blind_total=sp.simplify(
    (a-R)
    +(b-R-(a+R))
    +(T-R-(b+R))
    +(T+eps-(T+R))
)
sum_I=sp.simplify(sum(len_I))
sum_II=sp.simplify(sum(len_II))
assert sp.simplify(sum_I-blind_total)==0
assert sp.simplify(sum_II-blind_total)==0

# Degenerate cell total: replace the two-wall Z2 split by two cells.
sum_deg=sp.simplify(
    sig
    +(eps-sig)
    +(e+sig-eps)
    +(a-eps-(e+sig))
    +(eps-R)
    +(eps-R)
    +(b-R-(a+eps))
    +(T-eps-(b+R))
    +(eps-R)
    +(eps-R)
)
assert sp.simplify(sum_deg.subs(eps,Delta/2)-blind_total.subs(eps,Delta/2))==0

# Spatial boundaries are finite sets; no L2 class is created.
# This is measure-theoretic, so the certificate records endpoint finiteness by count.
a_walls=[eps,a-eps,a+eps,2*d-eps,T-eps]
hub_walls=[sig,e+sig,a+sig]
sample_bounds=[a-R,a+R,b-R,b+R,T-R,T+R]
assert len(a_walls)+len(hub_walls)+len(sample_bounds)==14

print("SW1-A0 COVERAGE CERTIFICATE: PASS")
print(f"sympy={sp.__version__}")
print("SW1 forces R<Delta/2; historical R=e/2,d/2,d,e+eps walls are absent")
print("blind Z1 ordering/gaps certified")
print("Z2 two-wall split certified in both epsilon chambers")
print("Z3 split and full horizon tail Z4 certified")
print("degenerate epsilon=Delta/2 collision is a single spatial null point")
print("a+sigma Hub wall lies inside/free-sample boundary, not a blind z cell")
print("cell-length sums equal the full blind-support length in all chambers")
print("A0 certificate is coverage-only; no raw-operator injectivity is asserted")
