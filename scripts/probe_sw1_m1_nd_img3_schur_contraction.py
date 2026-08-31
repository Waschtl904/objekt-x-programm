#!/usr/bin/env python3
"""Diagnostic Schur-bound probe for K = D_R^{-1} R_R on the IMG1 horizon block.

This script computes:
- exact row absolute-sum expressions on every active P0 output slot;
- a safe incoming-column overbound on every reference B96 atom/lift by mapping
  each output atom through every active FREE off-diagonal pullback.

The column bookkeeping deliberately overcovers: if an output atom image is a
proper subset of one input atom, its coefficient is charged to that entire
input atom.  Therefore the resulting column maximum is a safe upper bound,
not an underestimate.

If A*B < 1, the standard L2 Schur argument would give ||K|| <= sqrt(A B) < 1.
This file is diagnostic until the analytic transfer/audit is written.
"""

from fractions import Fraction as F
from collections import defaultdict
import bisect
import sympy as sp

import certify_sw1_a10_c2_m1_full_b96 as m1

print("SW1 M1-ND IMG3 SCHUR CONTRACTION PROBE")

L2, L3 = sp.log(2), sp.log(3)
c1 = L2 * 2**sp.Rational(-3, 2)
c2 = L2 * 2**sp.Rational(-9, 4)
c3 = L2 * 2**sp.Rational(-3)
c4 = c2
c5 = c3
c6 = L2 * 2**sp.Rational(-15, 4)
c7 = c3
c9 = L2 * 2**sp.Rational(-9, 2)
c10 = L2/4
c11 = 2*L3/(3*sp.sqrt(3))
alphaA = sp.simplify(c1+c5)
alphab = sp.simplify(c1+c5+c11)
kappa = sp.simplify(c1+c5+c9+c10+c11)
beta0 = sp.simplify(-c1+c3)
betam = sp.simplify(-c2-c4)
betap = sp.simplify(c2+c6)
betaT = sp.simplify(-c3-c5-c7-c10)
betab = sp.simplify(-c11)

C = {
    "1+2c1": 1+2*c1,
    "1+c1": 1+c1,
    "1+alphaA": 1+alphaA,
    "1+alphab": 1+alphab,
    "1+kappa": 1+kappa,
    "c1": c1,
    "-c1": -c1,
    "c2": c2,
    "beta0": beta0,
    "betam": betam,
    "betap": betap,
    "betaT": betaT,
    "betab": betab,
}

DIAG_NAME = {
    "R0":"1+2c1",
    "R1":"1+c1",
    "R2":"1+alphaA",
    "R3":"1+alphaA",
    "R4I":"1+alphaA",
    "R4II":"1+alphab",
    "R5":"1+alphab",
    "R6":"1+kappa",
    "R7":"1+kappa",
}

def abs_exact(x):
    x=sp.simplify(x)
    if x.is_positive is True:
        return x
    if x.is_negative is True:
        return -x
    raise AssertionError(("unknown sign",x))

def coeff_expr(name):
    if name in C:
        return sp.simplify(C[name])
    raise KeyError(name)

def effective_map(gname,j):
    _,s,eta,kappa0=m1.gdict[gname]
    return (s,F(eta,2),s*j+kappa0)

def apply_map(amap,theta):
    s,h,k=amap
    return (s*theta+h*m1.L+k*m1.D) % m1.L

def circ_dist(x,y):
    d=(x-y) % m1.L
    return min(d,m1.L-d)

def atom_index(vals,x):
    x=x % m1.L
    i=bisect.bisect_left(vals,x)
    if i<len(vals) and vals[i]==x:
        return None
    if i==0:
        return len(vals)-1
    return i-1

# Source-level identity uniqueness.
identity=(+1,F(0),0)
assert [br[0] for br in m1.FREE
        if effective_map(m1.free_sr[(br[0],"P0")][0],
                         m1.free_sr[(br[0],"P0")][1])==identity] == ["I"]

global_row_max = sp.Integer(0)
global_col_max = sp.Integer(0)
global_row_where = None
global_col_where = None
chamber_stats=[]

for ci,rep in enumerate(m1.reps):
    sigma,R,eps=rep
    vals=sorted(m1.bvalue(sig,rep) for sig in m1.B96)
    assert len(vals)==96 and len(set(vals))==96

    arcs=[]
    mids=[]
    for ai in range(96):
        lo=vals[ai]
        hi=vals[ai+1] if ai<95 else vals[0]+m1.L
        mid=(lo+hi)/2
        arcs.append((lo,hi))
        mids.append(mid % m1.L)

    incoming=defaultdict(lambda: sp.Integer(0))
    chamber_row_max=sp.Integer(0)

    for ai,theta in enumerate(mids):
        lo,hi=arcs[ai]
        half=(hi-lo)/2

        for lout in range(3):
            xout=theta+lout*m1.L
            T0=m1.T+eps
            if not (0<xout<T0):
                continue
            rows=m1.active_rows(xout,eps)
            assert len(rows)==1
            row=rows[0]
            drow=sp.simplify(coeff_expr(DIAG_NAME[row]))
            assert sp.simplify(drow-1).is_positive is True

            row_sum=sp.Integer(0)

            for affine, coeff_name in m1.row_terms_by_name[row]:
                gin,j,m,s=m1.free_sr[(affine,"P0")]
                amap=effective_map(gin,j)

                lin=(
                    s*(lout-m1.Nwrap("P0",theta))
                    +m1.Nwrap(gin,theta+j*m1.D)
                    -m
                )
                if not (0<=lin<3):
                    continue

                # Identity contribution belongs to D_R and is excluded from R_R.
                if affine=="I":
                    assert amap==identity and lin==lout
                    continue

                acoef=sp.simplify(abs_exact(coeff_expr(coeff_name))/drow)
                row_sum=sp.simplify(row_sum+acoef)

                # The image of this entire output atom under the affine isometry
                # must not contain an input B96 wall in its interior.  A midpoint
                # circular-distance test is exact because image half-length=half.
                imid=apply_map(amap,theta)
                mindist=min(circ_dist(imid,w) for w in vals)
                assert mindist >= half, (ci,ai,lout,row,affine,amap,mindist,half)

                target_ai=atom_index(vals,imid)
                assert target_ai is not None

                # Safe overcover: charge the whole coefficient to the target atom.
                incoming[(lin,target_ai)] = sp.simplify(
                    incoming[(lin,target_ai)] + acoef
                )

            if chamber_row_max==0 or sp.N(row_sum-chamber_row_max)>0:
                chamber_row_max=row_sum
            if global_row_max==0 or sp.N(row_sum-global_row_max)>0:
                global_row_max=row_sum
                global_row_where=(ci,ai,lout,row)

    chamber_col_max=sp.Integer(0)
    chamber_col_where=None
    for key,val in incoming.items():
        if chamber_col_max==0 or sp.N(val-chamber_col_max)>0:
            chamber_col_max=val
            chamber_col_where=key
        if global_col_max==0 or sp.N(val-global_col_max)>0:
            global_col_max=val
            global_col_where=(ci,key)

    chamber_stats.append((ci,chamber_row_max,chamber_col_max,chamber_col_where))

AB=sp.simplify(global_row_max*global_col_max)
schur=sp.sqrt(AB)

print("reference chambers:",len(m1.reps))
print("safe global row bound A =",sp.N(global_row_max,18))
print("row-bound location =",global_row_where)
print("safe global column overbound B =",sp.N(global_col_max,18))
print("column-bound location =",global_col_where)
print("A*B =",sp.N(AB,18))
print("sqrt(A*B) =",sp.N(schur,18))
print("A<1:", bool(sp.N(global_row_max)<1))
print("B<1:", bool(sp.N(global_col_max)<1))
print("A*B<1:", bool(sp.N(AB)<1))
print("top chamber column bounds:")
for ci,a,b,key in sorted(chamber_stats,key=lambda x:float(sp.N(x[2])),reverse=True)[:10]:
    print(ci,"A=",sp.N(a,12),"B=",sp.N(b,12),"at",key)
print("FIREWALL: diagnostic reference-r Schur overbound only; no promotion")
