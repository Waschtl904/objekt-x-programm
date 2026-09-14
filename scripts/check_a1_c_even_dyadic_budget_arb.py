# -*- coding: utf-8 -*-
"""Rigorous dyadic-quantization budget for the frozen A1 C-even gate.

This checker does NOT prove the 1075x1075 finite positivity theorem.  It fixes
160 fractional bits for the Gauss scalar proposals, Legendre-Fourier vector
proposals, and the even moment vector.  It proves that replacing the already
certified midpoint proposal by these exact dyadic points costs <4e-43 in
operator norm, and that the total frozen finite-model ledger is <4.5e-38.

Consequently, positivity of the exact dyadic block above the stronger shift
1.005e-35 is sufficient to prove the original C-even target 1e-35.
"""

from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
DIM = 1075
NODES = 155120
DYAD_BITS = 160
EVAL_B = arb("1e-43")
ALPHA_MID_MASS = arb(18613)  # conservative: 12*1551 plus >1 unit slack
EPS_Q = arb("4e-38")
EPS_EVAL = arb("4e-39")
EPS_DYAD_TARGET = arb("4e-43")
EPS_LEDGER_TARGET = arb("4.5e-38")
FINITE_TARGET = arb("1e-35")
DYAD_PROOF_SHIFT = arb("1.005e-35")

# Nearest-dyadic rounding with D fractional bits changes one scalar by <=2^(-D-1).
q = arb(2) ** (-(DYAD_BITS + 1))
q_vec = arb(DIM).sqrt() * q
B_TRUE = (2 / PI).sqrt()                    # exact even infinite-vector norm upper bound
B_MID = B_TRUE + EVAL_B                     # certified midpoint proposal norm upper bound

# Quantize alpha and b independently.  Apply the same rank-one perturbation lemma
# already proved in the C-even engine audit.
eps_alpha_quant = arb(NODES) * q * (B_MID + q_vec) ** 2
eps_b_quant = ALPHA_MID_MASS * (2 * B_MID * q_vec + q_vec * q_vec)
eps_K_quant = eps_alpha_quant + eps_b_quant

# Even Legendre coefficients of exp(x/2) are the coefficients of cosh(x/2), so
# sum_{n even} a_n^2 = ||cosh(x/2)||^2_{L2(-1,1)} = 1+sinh(1).
A_NORM = (1 + arb(1).sinh()).sqrt()
eps_moment_quant = 2 * (2 * A_NORM * q_vec + q_vec * q_vec)

eps_dyad = eps_K_quant + eps_moment_quant
if not (eps_dyad < EPS_DYAD_TARGET):
    raise RuntimeError(f"dyadic quantization budget failed: {eps_dyad}")

ledger = EPS_Q + EPS_EVAL + EPS_DYAD_TARGET
if not (ledger < EPS_LEDGER_TARGET):
    raise RuntimeError(f"finite model ledger failed: {ledger}")

# The stronger exact-dyadic shift must dominate the original target plus the
# complete predeclared finite-model ledger.
required = FINITE_TARGET + EPS_LEDGER_TARGET
if not (DYAD_PROOF_SHIFT > required):
    raise RuntimeError(
        f"dyadic proof shift does not dominate target+ledger: shift={DYAD_PROOF_SHIFT}, required={required}"
    )

# Exact common-denominator identity for the later integer matrix.
# alpha_q = A_s/2^160, b_q = B_s/2^160, moment a_q = M/2^160.
# Then K_q has denominator 2^480 and 2 a_q a_q^T has numerator 2^161 M M^T
# over the same denominator.  With common positive scale 10^38*2^480,
# positivity of A_q - 1.005e-35 I is equivalent to positivity of
#
#   10^38 K_int
# + 10^38 2^161 M M^T
# + (10^37 - 1005) 2^480 I.
#
# This is an integer symmetric matrix: no BLAS or storage rounding is needed.
scale_diag = arb(10) ** 37 - 1005
if not (scale_diag > 0):
    raise RuntimeError("exact integer diagonal scale is not positive")

print("A1 C-even exact-dyadic budget certificate")
print(f"prec_bits                 = {ctx.prec}")
print(f"dyadic fractional bits    = {DYAD_BITS}")
print(f"scalar half-ulp            = {q.str(50)}")
print(f"vector l2 quant radius     = {q_vec.str(50)}")
print(f"B_true upper               = {B_TRUE.str(40)}")
print(f"alpha midpoint mass upper  = {ALPHA_MID_MASS.str(20, radius=False)}")
print(f"alpha quant error upper    = {eps_alpha_quant.str(50)}")
print(f"b quant error upper        = {eps_b_quant.str(50)}")
print(f"K quant error upper        = {eps_K_quant.str(50)}")
print(f"moment norm upper          = {A_NORM.str(40)}")
print(f"moment quant error upper   = {eps_moment_quant.str(50)}")
print(f"total dyadic error upper   = {eps_dyad.str(50)}")
print(f"finite ledger upper        = {ledger.str(50)}")
print(f"target + ledger            = {required.str(50)}")
print(f"exact dyadic proof shift   = {DYAD_PROOF_SHIFT.str(30, radius=False)}")
print("CERTIFIED: 160-bit dyadic Gauss/moment quantization error < 4e-43")
print("CERTIFIED: frozen finite model ledger < 4.5e-38")
print("CERTIFIED: exact dyadic shift 1.005e-35 dominates target 1e-35 plus ledger")
print("CERTIFIED: later dyadic Gauss/moment matrix can be represented by one exact integer symmetric matrix")
print("FIREWALL: this is not the 1075x1075 finite positivity certificate")
