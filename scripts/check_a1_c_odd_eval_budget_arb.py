# -*- coding: utf-8 -*-
"""Global evaluation-error budget for frozen A1 C-odd.

Valid together with success of all 32 odd evaluation shards.  Those shards
prove e_b<1e-43 at every Gauss node and total scalar-alpha contribution
<1e-39.  The a priori alpha midpoint mass is bounded by 12*1551 from the
already-certified ||r||_infty<12 gate.  The odd normalized Bessel vector has
norm <= sqrt(2/pi), so the same conservative vector budget as C-even applies.
"""

from flint import arb, ctx

ctx.prec = 256
PI = arb.pi()
E = arb("1e-43")
BMAX = (2 / PI).sqrt()
ALPHA_MASS = arb(12) * arb(1551)
SCALAR_TOTAL = arb("1e-39")
VECTOR_TARGET = arb("3e-39")
EVAL_TARGET = arb("4e-39")

B0 = BMAX + E
vector = ALPHA_MASS * (2 * B0 * E + E * E)
if not (vector < VECTOR_TARGET):
    raise RuntimeError(f"C-odd global vector evaluation budget failed: {vector}")

total = vector + SCALAR_TOTAL
if not (total < EVAL_TARGET):
    raise RuntimeError(f"C-odd global evaluation budget failed: {total}")

print("A1 C-odd global evaluation-error budget")
print(f"Bmax                  = {BMAX.str(40)}")
print(f"alpha mass upper      = {ALPHA_MASS.str(20, radius=False)}")
print(f"uniform e_b           = {E.str(20, radius=False)}")
print(f"vector-error upper    = {vector.str(50)}")
print(f"scalar-alpha budget   = {SCALAR_TOTAL.str(20, radius=False)}")
print(f"epsilon_eval upper    = {total.str(50)}")
print("CERTIFIED: uniform C-odd vector-error contribution < 3e-39")
print("CERTIFIED: all-shard C-odd scalar-alpha budget plus vector part gives epsilon_eval < 4e-39")
print("FIREWALL: this is a C-odd evaluation-error certificate, not finite matrix positivity")
