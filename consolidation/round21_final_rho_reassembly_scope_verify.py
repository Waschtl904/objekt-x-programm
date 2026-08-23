#!/usr/bin/env python3
import math, random

# P12 Round 21 -- final rho-reassembly SCOPE verifier.
# This script does NOT re-prove R14/R17/R18/R19/R20.
# It checks exact constants, exhaustive/disjoint case composition,
# boundary assignment, and the logical scope predicates used by the final audit.

a = .5*math.log(2)
T = 2*a
c = .5*math.log(5)
b = .5*math.log(3)
d = b-a
e = T-b
delta = d-e
epsmax = c-T
rho = epsmax-delta

assert abs(epsmax-.5*math.log(5/4)) < 1e-15
assert abs(rho-.5*math.log(10/9)) < 1e-15
assert 0 < rho < e/2 < T
print("CONSTANTS = PASS", {
    "rho": rho, "e/2": e/2, "epsmax": epsmax
})

def classify(R,sigma):
    if R >= e/2:
        return "A"
    if sigma <= R:
        return "B"
    if sigma < e/2:
        return "C"
    return "D"

def A_scope(R,sigma,eps):
    return e/2 <= R < T and 0 < sigma < eps < epsmax

def B_scope(R,sigma,eps):
    return rho <= R < e/2 and 0 < sigma <= R and sigma < eps < epsmax

def C_scope(R,sigma,eps):
    return rho <= R < sigma < e/2 and sigma < eps < epsmax

def D_scope(R,sigma,eps):
    return rho <= R < e/2 <= sigma < eps < epsmax

# Exact boundary assignments.
assert classify(e/2, e/4) == "A"
R0=(rho+e/2)/2
assert classify(R0,R0) == "B"
assert classify(R0,e/2) == "D"
assert classify(R0,(R0+e/2)/2) == "C"
print("BOUNDARY_ASSIGNMENT = PASS")

# Exhaustive randomized composition.
random.seed(210021)
counts={k:0 for k in "ABCD"}
for _ in range(1000000):
    R=random.uniform(rho,T-1e-12)
    eps=random.uniform(1e-10,epsmax-1e-12)
    sigma=random.uniform(1e-12,eps-1e-12)
    case=classify(R,sigma)
    counts[case]+=1

    vals=[
        A_scope(R,sigma,eps),
        B_scope(R,sigma,eps),
        C_scope(R,sigma,eps),
        D_scope(R,sigma,eps),
    ]
    assert sum(bool(v) for v in vals)==1, (R,sigma,eps,case,vals)
    assert vals["ABCD".index(case)]

assert min(counts.values())>0
print("FOUR_WAY_EXACT_PARTITION = PASS 1000000", counts)

# Directed near-boundary checks.
for k in range(1,10000):
    tiny=10**(-3 - 9*k/9999)
    # R=e/2 wall: low side is B/C/D depending sigma; exact/high side A.
    Rhi=e/2
    eps=min(epsmax-1e-10, e/2+0.02)
    sigma=min(e/4,eps/2)
    assert classify(Rhi,sigma)=="A"

    # sigma=R wall belongs to B for low R.
    Rb=rho+(e/2-rho)*k/10000
    assert classify(Rb,Rb)=="B"

    # sigma=e/2 wall belongs to D for low R.
    assert classify(Rb,e/2)=="D"

print("DIRECTED_BOUNDARIES = PASS")

# Region-C composition preconditions for b1 after the committed kills.
random.seed(210022)
n=0
for _ in range(200000):
    R=random.uniform(rho+1e-12,e/2-1e-12)
    sigma=random.uniform(R+1e-12,e/2-1e-12)
    eps=random.uniform(sigma+1e-12,epsmax-1e-12)

    # R18/R17 chamber.
    assert rho <= R < sigma < e/2
    assert sigma < eps < epsmax

    # After R18 lower kill and R17 tail kill, b1 uses R_eff=sigma, S_eff=T.
    R_eff=sigma
    assert 0 < R_eff < T
    T0=T+eps
    assert T < T0 < c
    n+=1

print("REGION_C_TO_B1_SCOPE = PASS",n)

# Region-D scope equivalence:
# low R + sigma>=e/2 automatically implies sigma>R.
random.seed(210023)
for _ in range(200000):
    R=random.uniform(rho,e/2-1e-12)
    sigma=random.uniform(e/2,epsmax-1e-10)
    eps=random.uniform(sigma+1e-12,epsmax-1e-12)
    assert R < sigma
    assert D_scope(R,sigma,eps)
print("REGION_D_SCOPE_EQUIVALENCE = PASS 200000")

print("ROUND21_FINAL_RHO_REASSEMBLY_SCOPE_VERIFY = PASS")
