"""
P12 Round 19: scope and restricted-tail structural verifier.

This is not a proof of the remaining large-tail wedge.  It checks:
  * the four-way parameter partition,
  * the elementary inequalities used in the new restricted-tail reduction,
  * raw support patterns at the three new restricted-tail steps.
"""
import math
import random

a = math.log(2)/2
b = math.log(3)/2
T = 2*a
d = b-a
e = T-b
delta = d-e
epsmax = .5*math.log(5/4)
rho = epsmax-delta

assert 0 < rho < delta < e/2 < d/2 < epsmax < e < d < a < T

SHIFTS = (a,b,T)

def fold_arg(y):
    return abs(y)

def live(y,R,sigma):
    y=abs(y)
    return R < y < T+sigma

def raw_args(u):
    """Six positive folded h-arguments before support deletion."""
    out=[]
    for s in SHIFTS:
        out += [abs(u-s), u+s]
    return out

def classify(R,sigma):
    if R >= e/2:
        return "A"
    if sigma <= R:
        return "B"
    if sigma < e/2:
        return "C"
    return "D"

# Exhaustive random partition on the target chamber.
random.seed(20260823)
counts={k:0 for k in "ABCD"}
for _ in range(400000):
    R=random.uniform(rho, T-1e-8)
    eps=random.uniform(1e-8,epsmax-1e-8)
    sigma=random.uniform(1e-10,eps-1e-10)
    c=classify(R,sigma)
    counts[c]+=1
    if c=="A":
        assert R>=e/2
    elif c=="B":
        assert rho<=R<e/2 and 0<sigma<=R
    elif c=="C":
        assert rho<=R<sigma<e/2
    else:
        assert rho<=R<e/2<=sigma<epsmax
assert all(v>0 for v in counts.values())
print("FOUR_WAY_PARTITION = PASS", counts)

# Directed restricted-tail structural stress.
random.seed(190019)
n=0
for _ in range(200000):
    R=random.uniform(rho+1e-10,e/2-1e-10)
    eps=random.uniform(1e-8,epsmax-1e-10)
    sigmax=min(R,eps-1e-10)
    if sigmax<=1e-9:
        continue
    sigma=random.uniform(1e-10,sigmax)

    # Step B1: for every lower-support x>R the mixed T+x branch is dead.
    x=random.uniform(R+1e-10,a-1e-10)
    assert T+x >= T+R > T+sigma

    # Step B2: horizon source u=T+t.  Its only possibly relevant
    # backward arguments are t,e+t,a+t; all forward arguments are >S.
    t=random.uniform(1e-10,eps-1e-10)
    u=T+t
    args=raw_args(u)
    # order by shifts: |u-a|,u+a,|u-b|,u+b,|u-T|,u+T
    assert abs(args[0]-(a+t))<1e-12
    assert args[1] > T+sigma
    assert abs(args[2]-(e+t))<1e-12
    assert args[3] > T+sigma
    assert abs(args[4]-t)<1e-12
    assert args[5] > T+sigma
    assert t < eps < e
    assert e+t < e+epsmax < a

    # Step B3: high-reflection seed strip.
    z=random.uniform(a-eps+1e-10,a-1e-10)
    assert z > a-epsmax > d
    assert z > sigma
    assert z-e > d-epsmax > e/2 > R >= sigma

    # Raw source at u=z. After lower-half kill, the B3 null strip,
    # and support deletion, only T-z and a+z can carry the old
    # high-reflection relation.
    uz=z
    ar=raw_args(uz)
    # |z-a|=a-z lower; z+a=a+z is l(a-z)
    assert abs(ar[0]-(a-z))<1e-12
    assert abs(ar[1]-(a+z))<1e-12
    # |z-b|=b-z lower
    assert abs(ar[2]-(b-z))<1e-12
    # z+b = T+(z-e) is above mixed support
    assert abs(ar[3]-(T+(z-e)))<1e-12
    assert ar[3] > T+sigma
    # |z-T|=T-z = l(z), z+T is tail with offset z>sigma
    assert abs(ar[4]-(T-z))<1e-12
    assert ar[5] > T+sigma

    # Step B4: P1 tail partner is dead.
    tt=random.uniform(1e-10,sigma-1e-10)
    assert d-tt > d-sigma >= d-R > d-e/2 > e/2 > sigma
    n+=1

assert n>100000
print("RESTRICTED_TAIL_STRUCTURAL_STRESS = PASS", n)

# Region D is genuinely nonempty, with explicit interior witness.
R0=(rho+e/2)/2
sigma0=(e/2+epsmax)/2
eps0=(sigma0+epsmax)/2
assert rho<R0<e/2<sigma0<eps0<epsmax
assert classify(R0,sigma0)=="D"
print("REGION_D_INTERIOR_WITNESS = PASS",
      {"R":R0,"sigma":sigma0,"eps":eps0})

print("ROUND19_REASSEMBLY_SCOPE_VERIFY = PASS")
