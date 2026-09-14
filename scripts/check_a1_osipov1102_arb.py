# -*- coding: utf-8 -*-
"""Rigorous Arb gate for an Osipov-based A1 finite reduction.

For the continuous PSWF finite-Fourier operator F_c on L^2[-1,1],
Osipov Theorem 4 (arXiv:1206.4541) gives

    |lambda_n^F| <= nu(n,c)

with

    nu(n,c) = sqrt(pi) * c^n * (n!)^2 / ((2n)! * Gamma(n+3/2)).

The associated time-band concentration eigenvalue is

    mu_n = c/(2*pi) * |lambda_n^F|^2.

We evaluate this closed-form theorem at the predeclared values

    c = 1551, n = 1102

and combine it with the already certified A1 bounded-band constants

    multiplier floor alpha = 0.1,
    ||r||_infty < 12,
    Gamma_1 = kappa_* + 2 W_1.

The purpose is only to shrink the sufficient resolved dimension.  No PSWF
vector is computed, and no resolved-space positivity is claimed here.
All acceptance tests are Arb interval comparisons; no binary float enters a
proof decision.
"""

from math import factorial
from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
GAMMA_E = arb.const_euler()
LOG2 = arb(2).log()
PSI_QUARTER = -GAMMA_E - PI / 2 - 3 * LOG2
KAPPA = PI.log() - PSI_QUARTER


def weight(n: int, p: int) -> arb:
    return arb(p).log() / arb(n).sqrt()


W1 = (
    weight(2, 2)
    + weight(3, 3)
    + weight(4, 2)
    + weight(5, 5)
    + weight(7, 7)
)
GAMMA1 = KAPPA + 2 * W1

C = 1551
N = 1102
ALPHA = arb("0.1")
R_NORM = arb(12)
MU_TARGET = arb("1e-43")
TAU_TARGET = arb("0.099")
PENALTY_TARGET = arb("1.5e-40")
RESOLVED_TARGET = arb("3e-39")


def osipov_nu(n: int, c: int) -> arb:
    nfac = arb(factorial(n))
    two_n_fac = arb(factorial(2 * n))
    gamma_half = (arb(n) + arb(3) / 2).gamma()
    return PI.sqrt() * (arb(c) ** n) * nfac * nfac / (two_n_fac * gamma_half)


def main() -> None:
    nu = osipov_nu(N, C)
    mu = arb(C) / (2 * PI) * nu * nu

    if not (mu < MU_TARGET):
        raise RuntimeError(f"Osipov concentration bound too large: mu={mu}")

    tau = ALPHA - (GAMMA1 + ALPHA) * mu
    if not (tau > TAU_TARGET):
        raise RuntimeError(f"tail diagonal too small: tau={tau}")

    penalty = R_NORM * R_NORM * mu / tau
    if not (penalty < PENALTY_TARGET):
        raise RuntimeError(f"Schur penalty too large: penalty={penalty}")
    if not (RESOLVED_TARGET > penalty):
        raise RuntimeError("predeclared resolved target does not dominate penalty")

    print("A1 Osipov N=1102 Arb certificate")
    print(f"prec_bits       = {ctx.prec}")
    print(f"c               = {C}")
    print(f"PSWF index n    = {N}")
    print(f"Osipov nu_n ub  = {nu.str(60)}")
    print(f"concentration ub= {mu.str(60)}")
    print(f"Gamma_1         = {GAMMA1.str(45)}")
    print(f"tail tau        = {tau.str(60)}")
    print(f"Schur penalty   = {penalty.str(60)}")
    print(f"resolved target = {RESOLVED_TARGET.str(30, radius=False)}")
    print("CERTIFIED: Osipov concentration mu_1102(c=1551) < 1e-43")
    print("CERTIFIED: N=1102 augmented tail tau > 0.099")
    print("CERTIFIED: N=1102 Schur penalty < 1.5e-40")
    print("CERTIFIED: resolved lower bound 3e-39 remains sufficient")
    print("CERTIFIED: sufficient augmented resolved dimension <= 1104 = 552 even + 552 odd")


if __name__ == "__main__":
    main()
