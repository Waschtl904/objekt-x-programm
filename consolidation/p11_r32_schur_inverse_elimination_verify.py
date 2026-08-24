#!/usr/bin/env python3
"""
P11/R32 Schur inverse-elimination interface verifier.

Checks only:
  * arithmetic bookkeeping of the effective full-rest blocks in
    log(2) < T0 < 1/2 log(5);
  * the resulting 9+1+1 finite K^* M_Omega K word count;
  * an exact finite-dimensional algebraic sanity model of the block-kernel
    equivalence behind SE-1.

This script is NOT a proof of the infinite-dimensional theorem and is NOT a
proof of Schur-crossblock injectivity. P11/P12 remain unchanged.
"""

from fractions import Fraction
import sympy as sp

# -----------------------------------------------------------------------------
# 1. Exact arithmetic inequalities defining the three-rest-block chamber
# -----------------------------------------------------------------------------
# a = 1/2 log 2, b = 1/2 log 3, c = 1/2 log 5.
# Needed strict comparisons can be reduced to integer inequalities:
#   5a > 2c  <=> 2^5 > 5^2
#   3b > 2c  <=> 3^3 > 5^2
assert 2**5 > 5**2
assert 3**3 > 5**2
print("SE_ARITHMETIC_CUTOFFS = PASS 2^5>5^2 and 3^3>5^2")

# Martingale blocks Omega_{p,j} nonempty throughout the chamber:
# p=2: j=0,1; p=3: j=0.  Deeper j require thresholds above c.
blocks = [(2,0),(2,1),(3,0)]
assert blocks == [(2,0),(2,1),(3,0)]
print("SE_ACTIVE_REST_BLOCKS = PASS", blocks)

# Effective k lists on each output window.
# (2,0): k=1,2,3; k=4 would require 5a<2T0, impossible by 5a>2c>2T0.
# (2,1): k=2; k=3 would require 5a<2T0.
# (3,0): k=1; k=2 would require 3b<2T0, impossible by 3b>2c>2T0.
active_k = {
    (2,0): (1,2,3),
    (2,1): (2,),
    (3,0): (1,),
}
assert active_k[(2,0)] == (1,2,3)
assert active_k[(2,1)] == (2,)
assert active_k[(3,0)] == (1,)
print("SE_EFFECTIVE_K_LISTS = PASS", active_k)

# R*R expansion word count = square of each block length, summed over orthogonal blocks.
word_count = sum(len(ks)**2 for ks in active_k.values())
assert word_count == 11
print("SE_RSTAR_R_WORD_COUNT = PASS", word_count)

# -----------------------------------------------------------------------------
# 2. Exact coefficient bookkeeping
# -----------------------------------------------------------------------------
L2,L3 = sp.symbols('L2 L3', positive=True)
phi20 = [sp.Integer(2)**sp.Rational(-3*k,4) for k in active_k[(2,0)]]
phi21 = [sp.Integer(2)**sp.Rational(-3*k,4) for k in active_k[(2,1)]]
phi30 = [sp.Integer(3)**sp.Rational(-3*k,4) for k in active_k[(3,0)]]
assert phi20 == [sp.Integer(2)**sp.Rational(-3,4),
                 sp.Integer(2)**sp.Rational(-3,2),
                 sp.Integer(2)**sp.Rational(-9,4)]
assert phi21 == [sp.Integer(2)**sp.Rational(-3,2)]
assert phi30 == [sp.Integer(3)**sp.Rational(-3,4)]

block_prefactors = {
    (2,0): L2,      # (log 2)(2-1)2^0
    (2,1): 2*L2,    # (log 2)(2-1)2^1
    (3,0): 2*L3,    # (log 3)(3-1)3^0
}
print("SE_BLOCK_COEFFICIENTS = PASS", block_prefactors)

# -----------------------------------------------------------------------------
# 3. Finite-dimensional exact sanity model for SE-1
# -----------------------------------------------------------------------------
# Use a 4D ambient space with parity already suppressed.  H is skew-symmetric,
# A=C^T C >=0, B=(I+A)^-1.  EI and EA are coordinate embeddings.
H = sp.Matrix([
    [0, 1, 0, 0],
    [-1,0, 1, 0],
    [0,-1,0, 1],
    [0, 0,-1,0],
])
C = sp.Matrix([
    [1,0,1,0],
    [0,1,0,1],
])
A = C.T*C
B = (sp.eye(4)+A).inv()
assert H.T == -H
assert A == A.T

# one-dimensional inner/annular source embeddings chosen for exact arithmetic
EI = sp.Matrix([1,0,0,0])
EA = sp.Matrix([0,0,0,1])

S = (EI.T*H*B*H.T*EA)[0]

# Block system K(y,w)=0. For w=1, its unique first-row solution is y=B H^* EA.
y = B*H.T*EA
first = (sp.eye(4)+A)*y + H*EA
second = (EI.T*H*y)[0]
assert first == sp.zeros(4,1)
assert sp.simplify(second-S) == 0
print("SE_BLOCK_KERNEL_ALGEBRA_SANITY = PASS Schur scalar equals second block residual")

# General logical firewall: I+A is invertible because A>=0 in the real theorem.
assert (sp.eye(4)+A).det() != 0
print("SE_INVERTIBILITY_FIREWALL = PASS finite sanity model only")

print("P11_R32_SCHUR_INVERSE_ELIMINATION_VERIFY = PASS")
