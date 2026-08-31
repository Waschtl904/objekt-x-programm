#!/usr/bin/env python3
"""SW1 M1-ND IMG4 small-R FREE-separator coverage / measure certificate.

This certificate supplies the exact finite/arithmetic premises for a proposed
negative M1-ND construction at one explicit SW1 parameter point:

    epsilon0 = Delta/4,
    R0       = T/100000,
    sigma0   = R0/2.

It proves exactly:

1. For epsilon0=Delta/4, the A8 regular separator interval is, up to the
   single degenerate midpoint,
       (Delta/4, 3 Delta/4).
   Rotates with indices n=-14,...,14 cover the full L-circle a.e.

2. Hence every block of 29 consecutive rotation indices contains a regular
   separator a.e.  Combining this arithmetic premise with the already audited
   A8 separator theorem gives the analytic component bound:
       <=65 rotation layers, <=390 physical FREE states per component.
   The graph-theoretic implication itself is recorded in the audit, not
   machine-proved here.

3. A8.10B shows that the physical sheet-collision quotient glues at most two
   formal components.  Hence the universal physical component envelope is
       2 * 390 = 780 states.
   The crude measure envelope for the annulus visibility set is therefore
       6 KNF branches * 780 FREE states * 6 HUB branches * R0
       = 28080 R0
       = (351/1250) T,
   which is strictly smaller than the positive annulus length
       S0-R0 = T-R0/2.

The script does NOT construct an L2 function or prove that the component
saturation is a reducing set.  Those are the separate analytic steps in the
IMG4 audit.
"""

from fractions import Fraction as F
from math import gcd, lcm
import math

print("SW1 M1-ND IMG4 SMALL-R SEPARATOR/VISIBILITY CERTIFICATE")

# Linear forms a*log(2)+b*log(3), represented exactly by rational pairs.
LOG2=(F(1),F(0))
LOG3=(F(0),F(1))
DELTA=(F(-3,2),F(1))   # log3 - 3/2 log2
L=(F(2),F(-1))         # 2 log2 - log3
T=LOG2                 # log2

def add(x,y):
    return (x[0]+y[0],x[1]+y[1])

def sub(x,y):
    return (x[0]-y[0],x[1]-y[1])

def scale(q,x):
    q=F(q)
    return (q*x[0],q*x[1])

def sign_form(x):
    """Exact sign of a log2+b log3 by integer prime-power comparison."""
    a,b=x
    if a==0 and b==0:
        return 0
    if a>=0 and b>=0:
        return 1
    if a<=0 and b<=0:
        return -1
    den=lcm(a.denominator,b.denominator)
    A=a.numerator*(den//a.denominator)
    B=b.numerator*(den//b.denominator)
    if A>0 and B<0:
        lhs=2**A
        rhs=3**(-B)
        return (lhs>rhs)-(lhs<rhs)
    if A<0 and B>0:
        lhs=3**B
        rhs=2**(-A)
        return (lhs>rhs)-(lhs<rhs)
    raise AssertionError((x,A,B))

def cmp_form(x,y):
    return sign_form(sub(x,y))

def numeric(x):
    return float(x[0])*math.log(2)+float(x[1])*math.log(3)

assert sign_form(DELTA)>0
assert sign_form(L)>0
assert sign_form(sub(L,DELTA))>0

def mod_L(x):
    # Numerical quotient only proposes the integer; exact inequalities certify it.
    k=math.floor(numeric(x)/numeric(L))
    y=sub(x,scale(k,L))
    while sign_form(y)<0:
        k-=1
        y=add(y,L)
    while cmp_form(y,L)>=0:
        k+=1
        y=sub(y,L)
    assert sign_form(y)>=0
    assert cmp_form(y,L)<0
    return y,k

# A8 regular separator for epsilon0=Delta/4:
# (Delta/4,Delta/2) U (Delta/2,3Delta/4).
# For a.e. covering we may use the joined open interval and later remove the
# finitely many rotated midpoint/endpoints.
Jlo=scale(F(1,4),DELTA)
Jhi=scale(F(3,4),DELTA)
width=sub(Jhi,Jlo)
assert width==scale(F(1,2),DELTA)

# Compute exact modulo-L arcs for t such that t+n Delta belongs to J.
arcs=[]
for n in range(-14,15):
    raw_lo=sub(Jlo,scale(n,DELTA))
    lo,_=mod_L(raw_lo)
    end=add(lo,width)
    if cmp_form(end,L)<=0:
        arcs.append((lo,end,n))
    else:
        arcs.append((lo,L,n))
        arcs.append(((F(0),F(0)),sub(end,L),n))

# Sort only by a high-precision proxy; every ordering relation is then checked
# exactly with sign_form before being accepted.
arcs.sort(key=lambda z:numeric(z[0]))
for i in range(len(arcs)-1):
    assert cmp_form(arcs[i][0],arcs[i+1][0])<=0

# Exact interval merge. Touching endpoints are allowed because the desired
# separator cover is an a.e. statement; the finitely many endpoints and the
# degenerate midpoint are null.
merged=[]
for lo,hi,n in arcs:
    if not merged or cmp_form(lo,merged[-1][1])>0:
        merged.append([lo,hi,[n]])
    else:
        if cmp_form(hi,merged[-1][1])>0:
            merged[-1][1]=hi
        merged[-1][2].append(n)

assert len(merged)==1
assert merged[0][0]==(F(0),F(0))
assert merged[0][1]==L

# A.e. every phase therefore has a regular separator within +/-14 indices.
# Any 29 consecutive indices contain one separator.
HIT_RADIUS=14
MAX_NONSEP_RUN=28
assert 2*HIT_RADIUS+1==29

# A8 requires n_- <= m0-4 and n_+ >= m0+1.
# Search intervals [m0-32,m0-4] and [m0+1,m0+29], both 29 indices.
LEFT_OFFSET=32
RIGHT_OFFSET=29
assert (LEFT_OFFSET-4+1)==29
assert RIGHT_OFFSET==29

# A8.14 support [n_-, n_++3], hence at most
# (m0+29+3) - (m0-32) + 1 = 65 layers.
MAX_LAYERS=RIGHT_OFFSET+3+LEFT_OFFSET+1
assert MAX_LAYERS==65
MAX_FORMAL_STATES=6*MAX_LAYERS
assert MAX_FORMAL_STATES==390
# A8.10B: the physical quotient saturates a formal component by C U J_K(C),
# hence at most two formal components are glued.
MAX_PHYSICAL_STATES=2*MAX_FORMAL_STATES
assert MAX_PHYSICAL_STATES==780

# Explicit physical parameter point.
# epsilon0=Delta/4, R0=T/100000, sigma0=R0/2.
eps0=scale(F(1,4),DELTA)
R0=scale(F(1,100000),T)
sigma0=scale(F(1,2),R0)

# Exact SW1 inequalities 0<sigma<R<epsilon<Delta/2 and R+epsilon<Delta.
assert sign_form(sigma0)>0
assert sign_form(sub(R0,sigma0))>0
assert sign_form(sub(eps0,R0))>0
assert sign_form(sub(scale(F(1,2),DELTA),eps0))>0
assert sign_form(sub(DELTA,add(R0,eps0)))>0

# Crude positive-half measure envelope.
KNF_BRANCHES=6
HUB_BRANCHES=6
VISIBLE_FACTOR=KNF_BRANCHES*MAX_PHYSICAL_STATES*HUB_BRANCHES
assert VISIBLE_FACTOR==28080

# visible <= 28080 R0 = 28080/100000 T = 351/1250 T.
visible_T_factor=F(VISIBLE_FACTOR,100000)
assert visible_T_factor==F(351,1250)

# S=T+sigma, so positive annulus length S-R=T-R/2
# = (1-1/200000)T.
annulus_T_factor=F(1)-F(1,200000)
assert visible_T_factor<annulus_T_factor
blind_T_factor=annulus_T_factor-visible_T_factor
assert blind_T_factor>F(7,10)  # still a huge safety margin

print("epsilon0 = Delta/4")
print("rotation indices used for separator cover: -14..14")
print("a.e. separator cover of the full L-circle: PASS")
print("max consecutive nonseparator run:",MAX_NONSEP_RUN)
print("A8-derived layer envelope (analytic handoff):",MAX_LAYERS)
print("A8-derived formal FREE-state envelope (analytic handoff):",MAX_FORMAL_STATES)
print("A8.10B universal physical quotient envelope:",MAX_PHYSICAL_STATES)
print("explicit R0 = T/100000, sigma0 = R0/2")
print("SW1 inequalities at explicit point: PASS")
print("visibility factor:",VISIBLE_FACTOR)
print("visible positive-annulus measure <=",visible_T_factor,"* T")
print("positive annulus length =",annulus_T_factor,"* T")
print("blind-measure lower envelope >",blind_T_factor,"* T")
print("FIREWALL: arithmetic/measure premises only; reducing-subspace/kernel step is analytic")
print("SW1 M1-ND IMG4 SMALL-R SEPARATOR/VISIBILITY CERTIFICATE: PASS")
