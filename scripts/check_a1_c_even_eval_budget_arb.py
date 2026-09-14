# -*- coding: utf-8 -*-
"""Global error-budget arithmetic for the frozen A1 C-even evaluation engine.

This checker is only valid together with success of all 32 shard jobs from
check_a1_c_even_eval_shard_arb.py.  Those jobs prove e_b<1e-43 at every Gauss
node and a total scalar-alpha contribution <1e-39 after summing shard budgets.

Using positive Gauss weights and |r|<12, the total midpoint-alpha mass is
bounded a priori by 12*1551.  Together with ||b||<=sqrt(2/pi) this yields the
uniform vector-error part of the node perturbation lemma and certifies

    epsilon_eval < 4e-39.
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

# Proposal norm is at most true norm plus e_b.
B0 = BMAX + E
vector = ALPHA_MASS * (2 * B0 * E + E * E)
if not (vector < VECTOR_TARGET):
    raise RuntimeError(f"global vector evaluation budget failed: {vector}")

total = vector + SCALAR_TOTAL
if not (total < EVAL_TARGET):
    raise RuntimeError(f"global evaluation budget failed: {total}")

print("A1 C-even global evaluation-error budget")
print(f"Bmax                  = {BMAX.str(40)}")
print(f"alpha mass upper      = {ALPHA_MASS.str(20, radius=False)}")
print(f"uniform e_b           = {E.str(20, radius=False)}")
print(f"vector-error upper    = {vector.str(50)}")
print(f"scalar-alpha budget   = {SCALAR_TOTAL.str(20, radius=False)}")
print(f"epsilon_eval upper    = {total.str(50)}")
print("CERTIFIED: uniform C-even vector-error contribution < 3e-39")
print("CERTIFIED: all-shard scalar-alpha budget plus vector part gives epsilon_eval < 4e-39")
print("FIREWALL: this is an evaluation-error certificate, not finite matrix positivity")
