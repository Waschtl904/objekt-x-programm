#!/usr/bin/env python3
import math, random

a=.5*math.log(2)
b=.5*math.log(3)
T=2*a
d=b-a
e=T-b
delta=d-e
epsmax=.5*math.log(5/4)
rho=epsmax-delta

assert epsmax < e
assert a-epsmax > d
assert d-epsmax > e/2
assert d-e/2 > e/2

# The key point: none of these comparisons uses rho as a lower bound for R.
random.seed(220022)
n=0
for _ in range(500000):
    R=random.uniform(1e-10,e/2-1e-10)
    sigma=random.uniform(1e-12,R)
    eps=random.uniform(sigma+1e-12,epsmax-1e-12)

    # high-reflection seed strip: z in (a-eps,a)
    z=a-eps + random.random()*eps
    assert z>d
    assert z>sigma
    assert z-e > d-epsmax > e/2 > R >= sigma

    # P1 tail-kill geometry, any t in (0,sigma)
    t=random.random()*sigma
    assert d-t > d-sigma
    assert d-sigma >= d-R > d-e/2 > e/2 > sigma
    n+=1

print("ROUND22_RESTRICTED_TAIL_ALL_R_STRUCTURAL_STRESS = PASS",n)
print("rho is not used as an R lower bound; rho =",rho)
