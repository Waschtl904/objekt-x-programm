#!/usr/bin/env python3
"""SW1 M1-ND IMG3 linear orbit-growth visibility bound.

Strengthens the crude raw-path bound for finite Neumann truncations.

In unfolded affine phase coordinates write a horizon phase as
    sign*t + m*Delta + parity*L/2.
The FREE IMG1 alphabet has:
- sign-preserving maps m -> m+k, k in {-2,-1,0,1,2};
- sign-flipping maps m -> -m+k, k in {1,2,3,4};
and never flips half-period parity.

The six KNF starting samples have m in {1,2}.  Hence after at most N FREE
steps every reachable phase satisfies
    1-2N <= m <= 2+2N.
There are at most
    2 signs * 2 parities * 3 lifts * (4N+2)
horizon states, and after one of 6 HUB source branches at most
    Mlin_N = 72(4N+2) = 288N+144
distinct annulus affine sample maps.

Thus any finite truncation through order N sees annulus measure at most
Mlin_N*R.  Consequently full support visibility requires
    (288N+144)R >= S-R > T-R,
so necessarily
    N > (T/R - 145)/288
(up to the integer ceiling convention).

This is a support/visibility necessary condition only, not an injectivity
criterion.
"""

from fractions import Fraction as F
import sympy as sp
import certify_sw1_a10_c2_m1_full_b96 as m1

print("SW1 M1-ND IMG3 LINEAR ORBIT-GROWTH VISIBILITY CERTIFICATE")

# Derive the nine FREE effective maps from the canonical M1 source relations.
def effective_map(gname,j):
    _,s,eta,kappa=m1.gdict[gname]
    return (s,F(eta,2),s*j+kappa)

free_types=set()
for br in m1.FREE:
    gin,j,_,_=m1.free_sr[(br[0],"P0")]
    free_types.add(effective_map(gin,j))

expected={
    (+1,F(0),-2),(+1,F(0),-1),(+1,F(0),0),
    (+1,F(0),1),(+1,F(0),2),
    (-1,F(0),1),(-1,F(0),2),(-1,F(0),3),(-1,F(0),4),
}
assert free_types==expected
assert all(h==0 for _,h,_ in free_types)

# Six KNF starting orbit labels relative to u.
# Convert P_n -> (sign=+1,m=n), Q_n -> (sign=-1,m=4-n).
starts=[
    ("Q",3,0), # a-u
    ("P",1,0), # a+u
    ("Q",2,1), # b-u
    ("P",2,1), # b+u
    ("Q",2,0), # T-u
    ("P",2,0), # T+u
]

def to_sm(state):
    sheet,n,parity=state
    return (+1,n,parity) if sheet=="P" else (-1,4-n,parity)

sm_starts={to_sm(s) for s in starts}
assert {m for _,m,_ in sm_starts}=={1,2}

def step(alpha,state):
    s,h,k=alpha
    sg,m,par=state
    assert h==0
    return (s*sg, s*m+k, par)

# Exact finite checks of the inductive interval and the linear state bound.
seen=set(sm_starts)
front=set(sm_starts)
for N in range(0,21):
    lo=1-2*N
    hi=2+2*N
    assert all(lo<=m<=hi for _,m,_ in seen)
    assert len(seen)<=4*(4*N+2) # sign * parity * integer m
    if N<20:
        nxt={step(a,z) for a in free_types for z in front}
        seen |= nxt
        front=nxt

# Analytic induction margins:
# If m in [1-2N,2+2N], sign-preserving k in [-2,2] gives the N+1 interval.
# sign-flipping k in [1,4] gives an even smaller interval.
N=sp.symbols("N", integer=True, nonnegative=True)
lo=1-2*N
hi=2+2*N
next_lo=1-2*(N+1)
next_hi=2+2*(N+1)
assert sp.simplify((lo-2)-next_lo)==0
assert sp.simplify(next_hi-(hi+2))==0
assert sp.simplify((-hi+1)-next_lo)==0
assert sp.simplify(next_hi-(-lo+4))==1

mcount=sp.simplify(next_hi-next_lo+1)
assert mcount==4*N+6 # N+1 interval count

Mlin=72*(4*N+2)
assert sp.expand(Mlin)==288*N+144

# Physical constants and exact necessary support condition.
L2=sp.log(2)
T=L2
R=sp.symbols("R", positive=True)
S=sp.symbols("S", positive=True)

# If full annulus visibility occurs, Mlin*R must cover at least S-R.
# Since S=T+sigma with sigma>0, S-R > T-R.
# Rearrangement of Mlin*R >= T-R:
necessary_N=sp.simplify((T/R-145)/288)

print("FREE effective types:",len(free_types))
print("FREE half-period flips: 0")
print("starting unfolded m-set: {1,2}")
print("reachable m interval through order N: [1-2N, 2+2N]")
print("horizon-state upper bound: 12*(4N+2)")
print("annulus sample-map upper bound: Mlin_N = 288N+144")
print("necessary full-visibility inequality: (288N+144)R >= S-R > T-R")
print("therefore necessarily N > (T/R-145)/288 before integer rounding")
print("FIREWALL: support visibility is necessary, not sufficient, for injectivity")
print("SW1 M1-ND IMG3 LINEAR ORBIT-GROWTH VISIBILITY CERTIFICATE: PASS")
