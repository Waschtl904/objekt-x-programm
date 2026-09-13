# -*- coding: utf-8 -*-
"""Rigorous Arb certificate for the bounded-band A1 Schur reduction.

Starting from the certified a=1 multiplier bound m_1(xi) >= c=0.04 for
|xi|>=Omega=2300, write

    m_1(xi) = c + r(xi) + s(xi),

where r=(m_1-c)1_{|xi|<=Omega} and s=(m_1-c)1_{|xi|>Omega} >= 0.
Then q_1 >= c I + K with K=P r(D) P.

This script certifies:
  * ||r||_infty < 12;
  * KRD lambda_1680(c=2300) < 1.1e-39;
  * tail lower bound tau > 0.039;
  * ||K_RT||^2 / tau < 4.1e-36.

Thus a resolved lower bound mu_R >= 5e-36 is sufficient for the full Schur
complement, provided the resolved space contains the two moment Riesz vectors so
that the completion term has no resolved-tail crossblock.
"""

from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
GAMMA = arb.const_euler()
LOG2 = arb(2).log()
X = arb(1) / 4
PSI_QUARTER = -GAMMA - PI / 2 - 3 * LOG2


def weight(n: int, p: int) -> arb:
    return arb(p).log() / arb(n).sqrt()


W = (
    weight(2, 2)
    + weight(3, 3)
    + weight(4, 2)
    + weight(5, 5)
    + weight(7, 7)
)
KAPPA = PI.log() - PSI_QUARTER
GAMMA1 = KAPPA + 2 * W

OMEGA = arb(2300)
C = arb("0.04")
M = arb(12)
SERIES_N = 64
PROLATE_K = 1680
SHANNON_CEIL = 1465
LAMBDA_TARGET = arb("1.1e-39")
TAIL_FLOOR = arb("0.039")
SCHUR_PENALTY_TARGET = arb("4.1e-36")
RESOLVED_TARGET = arb("5e-36")


def f_term(u: arb, yy: arb) -> arb:
    return yy / (u * (u * u + yy))


def digamma_increment_upper(y: arb) -> arb:
    """Upper bound for Re psi(1/4+iy)-psi(1/4), y>=0."""
    yy = y * y
    s = arb(0)
    for k in range(SERIES_N):
        u = arb(k) + X
        s += f_term(u, yy)
    u0 = arb(SERIES_N) + X
    # For decreasing f: sum_{k=N}^inf f(k+x) <= f(N+x)+int_N^inf f(t+x)dt.
    tail = f_term(u0, yy) + (1 + yy / (u0 * u0)).log() / 2
    return s + tail


def krd_upper(k: int) -> arb:
    denom = (2 / (PI * PI)) * (100 * OMEGA / PI + 25).log()
    exponent = -(arb(k - SHANNON_CEIL - 6)) / denom
    return 10 * exponent.exp()


def main() -> None:
    # Check active set boundary.
    if not (arb(7).log() < 2 and arb(8).log() > 2):
        raise RuntimeError("active prime-power set at a=1 not certified")

    # Upper bound for m_1 on the compact band.  Each digamma summand increases
    # with |y|, and the prime cosine contribution is <= +2W.
    y_max = OMEGA / 2
    m_upper = PSI_QUARTER + digamma_increment_upper(y_max) - PI.log() + 2 * W

    # Lower bound m_1 >= -Gamma_1 comes from m_1+Gamma_1 = positive feature symbol.
    if not (GAMMA1 + C < M):
        raise RuntimeError(f"lower-side r bound failed: Gamma1+c={GAMMA1+C}")
    if not (m_upper - C < M):
        raise RuntimeError(f"upper-side r bound failed: m_upper-c={m_upper-C}")

    shannon = 2 * OMEGA / PI
    if not (arb(1464) < shannon and shannon < arb(1465)):
        raise RuntimeError(f"failed Shannon-number enclosure: {shannon}")

    lam = krd_upper(PROLATE_K)
    if not (lam < LAMBDA_TARGET):
        raise RuntimeError(f"lambda_1680 KRD bound failed: {lam}")

    # On the augmented Prolate tail, E vanishes and band concentration <= lam.
    # r >= -(Gamma1+C), so cI+K has tail reserve tau.
    tau = C - (GAMMA1 + C) * lam
    if not (tau > TAIL_FLOOR):
        raise RuntimeError(f"tail floor failed: tau={tau}")

    # Crossblock K_RT norm <= ||r||_inf sqrt(lam); use M=12.
    cross_sq = M * M * lam
    schur_penalty = cross_sq / tau
    if not (schur_penalty < SCHUR_PENALTY_TARGET):
        raise RuntimeError(f"Schur penalty too large: {schur_penalty}")
    if not (RESOLVED_TARGET > SCHUR_PENALTY_TARGET):
        raise RuntimeError("resolved target does not dominate certified Schur penalty")

    print("A1 bounded-band Schur-cross Arb certificate")
    print(f"prec_bits            = {ctx.prec}")
    print(f"Gamma_1              = {GAMMA1.str(50)}")
    print(f"band m_1 upper       = {m_upper.str(50)}")
    print(f"certified ||r||      < {M.str(20, radius=False)}")
    print(f"2c/pi                = {shannon.str(50)}")
    print(f"PSWF index           = {PROLATE_K}")
    print(f"KRD lambda_1680 ub   = {lam.str(60)}")
    print(f"tail tau             = {tau.str(60)}")
    print(f"cross^2 ub           = {cross_sq.str(60)}")
    print(f"Schur penalty ub     = {schur_penalty.str(60)}")
    print(f"resolved target      = {RESOLVED_TARGET.str(20, radius=False)}")
    print("CERTIFIED: ||r||_infty < 12 on |xi|<=2300")
    print("CERTIFIED: PSWF lambda_1680(c=2300) < 1.1e-39")
    print("CERTIFIED: augmented tail lower bound tau > 0.039")
    print("CERTIFIED: Schur cross penalty < 4.1e-36")
    print("CERTIFIED: resolved lower bound 5e-36 is sufficient for A1 positivity")


if __name__ == "__main__":
    main()
