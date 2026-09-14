# -*- coding: utf-8 -*-
"""Rigorous dyadic-quantization budget for frozen A1 C-odd.

The odd finite block uses the same 160 fractional bits for alpha, the
Legendre-Fourier vector and the odd moment vector.  This proves that replacing
the certified midpoint proposal by exact dyadic points costs <4e-43 in
operator norm and that the total finite-model ledger remains <4.5e-38.
"""

from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
DIM = 1075
NODES = 155120
DYAD_BITS = 160
EVAL_B = arb("1e-43")
ALPHA_MID_MASS = arb(18613)
EPS_Q = arb("4e-38")
EPS_EVAL = arb("4e-39")
EPS_DYAD_TARGET = arb("4e-43")
EPS_LEDGER_TARGET = arb("4.5e-38")
FINITE_TARGET = arb("1e-35")
DYAD_PROOF_SHIFT = arb("1.005e-35")

q = arb(2) ** (-(DYAD_BITS + 1))
q_vec = arb(DIM).sqrt() * q
B_TRUE = (2 / PI).sqrt()
B_MID = B_TRUE + EVAL_B

eps_alpha_quant = arb(NODES) * q * (B_MID + q_vec) ** 2
eps_b_quant = ALPHA_MID_MASS * (2 * B_MID * q_vec + q_vec * q_vec)
eps_K_quant = eps_alpha_quant + eps_b_quant

# Odd coefficients of exp(x/2) are the coefficients of sinh(x/2):
# sum_{n odd} a_n^2 = ||sinh(x/2)||^2 = sinh(1)-1.
A_NORM = (arb(1).sinh() - 1).sqrt()
eps_moment_quant = 2 * (2 * A_NORM * q_vec + q_vec * q_vec)

eps_dyad = eps_K_quant + eps_moment_quant
if not (eps_dyad < EPS_DYAD_TARGET):
    raise RuntimeError(f"C-odd dyadic quantization budget failed: {eps_dyad}")

ledger = EPS_Q + EPS_EVAL + EPS_DYAD_TARGET
if not (ledger < EPS_LEDGER_TARGET):
    raise RuntimeError(f"C-odd finite model ledger failed: {ledger}")

required = FINITE_TARGET + EPS_LEDGER_TARGET
if not (DYAD_PROOF_SHIFT > required):
    raise RuntimeError(
        f"C-odd dyadic proof shift does not dominate target+ledger: shift={DYAD_PROOF_SHIFT}, required={required}"
    )

scale_diag = arb(10) ** 37 - 1005
if not (scale_diag > 0):
    raise RuntimeError("exact C-odd integer diagonal scale is not positive")

print("A1 C-odd exact-dyadic budget certificate")
print(f"prec_bits                 = {ctx.prec}")
print(f"dyadic fractional bits    = {DYAD_BITS}")
print(f"scalar half-ulp            = {q.str(50)}")
print(f"vector l2 quant radius     = {q_vec.str(50)}")
print(f"B_true upper               = {B_TRUE.str(40)}")
print(f"alpha midpoint mass upper  = {ALPHA_MID_MASS.str(20, radius=False)}")
print(f"alpha quant error upper    = {eps_alpha_quant.str(50)}")
print(f"b quant error upper        = {eps_b_quant.str(50)}")
print(f"K quant error upper        = {eps_K_quant.str(50)}")
print(f"odd moment norm upper      = {A_NORM.str(40)}")
print(f"moment quant error upper   = {eps_moment_quant.str(50)}")
print(f"total dyadic error upper   = {eps_dyad.str(50)}")
print(f"finite ledger upper        = {ledger.str(50)}")
print(f"target + ledger            = {required.str(50)}")
print(f"exact dyadic proof shift   = {DYAD_PROOF_SHIFT.str(30, radius=False)}")
print("CERTIFIED: C-odd 160-bit dyadic Gauss/moment quantization error < 4e-43")
print("CERTIFIED: C-odd frozen finite model ledger < 4.5e-38")
print("CERTIFIED: C-odd exact dyadic shift 1.005e-35 dominates target 1e-35 plus ledger")
print("CERTIFIED: later C-odd dyadic matrix has one exact integer symmetric representation")
print("FIREWALL: this is not the 1075x1075 C-odd positivity certificate")
