# -*- coding: utf-8 -*-
"""Rigorous Arb certificate for high-frequency positivity and a Prolate tail at a=1.

For a=1, the centered COMMON-JUMP/null-pole form has exact Fourier multiplier

    m_1(xi) = Re psi(1/4 + i xi/2) - log(pi)
              - 2 * sum_{n in {2,3,4,5,7}} Lambda(n)/sqrt(n) * cos(xi log n).

This script certifies:

    m_1(xi) > 0.04    for |xi| >= 2300,

and combines this with the non-asymptotic continuous-PSWF eigenvalue bound of
Karnik--Romberg--Davenport, Corollary 3 (arXiv:2006.00427v2), to certify that
the Prolate concentration eigenvalue lambda_1490(c=2300) is < 0.0035.
Consequently the orthogonal Prolate tail after the first 1490 timelimited PSWFs
has a strictly positive q_1 reserve.

The digamma proof uses DLMF 5.7.6.  For x>0 and y real,

    Re psi(x+iy) - psi(x)
      = sum_{k>=0} y^2 / ((k+x)((k+x)^2+y^2)).

The summand is positive and decreasing in u=k+x.  Therefore, after N terms,
its tail is bounded below by the corresponding integral:

    sum_{k>=N} f_y(k+x)
      >= 1/2 * log(1 + y^2/(N+x)^2).

Every acceptance test below is interval-rigorous; no float conversion is used.
"""

from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
GAMMA = arb.const_euler()
LOG2 = arb(2).log()
X = arb(1) / 4
PSI_QUARTER = -GAMMA - PI / 2 - 3 * LOG2


def weight(n: int, p: int) -> arb:
    """Lambda(p^k)/sqrt(p^k) for the explicitly supplied prime base p."""
    return arb(p).log() / arb(n).sqrt()


# Active prime powers for a=1: log n <= 2 iff n <= e^2, hence {2,3,4,5,7}.
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
TARGET = arb("0.04")
RHO = arb("0.0035")
TAIL_TARGET = arb("0.01")
N = 64

# Continuous time interval is [-1,1], so T=2 and the PSWF parameter c=Omega*T/2=Omega.
PROLATE_C = OMEGA
PROLATE_K = 1490
SHANNON_CEIL = 1465  # certified below as ceil(2*c/pi)


def digamma_increment_lower(y: arb, n_terms: int = N) -> arb:
    """Lower enclosure of Re psi(1/4+iy)-psi(1/4)."""
    s = arb(0)
    yy = y * y
    for k in range(n_terms):
        u = arb(k) + X
        s += yy / (u * (u * u + yy))

    u0 = arb(n_terms) + X
    tail_integral = (1 + yy / (u0 * u0)).log() / 2
    return s + tail_integral


def multiplier_lower_at_omega() -> arb:
    y = OMEGA / 2
    # cos(theta) <= 1 for every prime-power phase, hence the worst prime term is -2W.
    return PSI_QUARTER + digamma_increment_lower(y) - PI.log() - 2 * W


def krd_pswf_upper() -> arb:
    """Karnik--Romberg--Davenport Corollary 3 upper bound for lambda_k(c)."""
    denom = (2 / (PI * PI)) * (100 * PROLATE_C / PI + 25).log()
    exponent = -(arb(PROLATE_K - SHANNON_CEIL - 6)) / denom
    return 10 * exponent.exp()


def main() -> None:
    # Certify the active cutoff boundary itself.
    if not (arb(7).log() < 2):
        raise RuntimeError("failed to certify log(7) < 2")
    if not (arb(8).log() > 2):
        raise RuntimeError("failed to certify log(8) > 2")

    lb = multiplier_lower_at_omega()
    if not (lb > TARGET):
        raise RuntimeError(f"high-frequency lower bound failed: lb={lb}, target={TARGET}")

    # Global form lower bound q_1 >= -Gamma_1 ||v||^2.
    rho_star = TARGET / (TARGET + GAMMA1)
    if not (rho_star > RHO):
        raise RuntimeError(f"Prolate concentration threshold too small: rho*={rho_star}")

    # Certify ceil(2c/pi)=1465, then apply the explicit KRD bound at k=1490.
    shannon = 2 * PROLATE_C / PI
    if not (arb(1464) < shannon and shannon < arb(1465)):
        raise RuntimeError(f"failed to certify 1464 < 2c/pi < 1465: {shannon}")

    prolate_upper = krd_pswf_upper()
    if not (prolate_upper < RHO):
        raise RuntimeError(f"KRD Prolate upper bound failed: lambda_1490 <= {prolate_upper}")

    # If band concentration <= prolate_upper, then
    # q_1(v) >= TARGET*(1-rho)||v||^2 - GAMMA1*rho||v||^2.
    tail_margin = TARGET - (TARGET + GAMMA1) * prolate_upper
    if not (tail_margin > TAIL_TARGET):
        raise RuntimeError(f"certified Prolate-tail margin too small: margin={tail_margin}")

    print("A1 high-frequency / Prolate-tail Arb certificate")
    print(f"prec_bits       = {ctx.prec}")
    print(f"W               = {W.str(40)}")
    print(f"Gamma_1         = {GAMMA1.str(40)}")
    print(f"Omega           = {OMEGA.str(20, radius=False)}")
    print(f"N_series        = {N}")
    print(f"m1 lower        = {lb.str(50)}")
    print(f"target c        = {TARGET.str(20, radius=False)}")
    print(f"rho_*           = {rho_star.str(50)}")
    print(f"2c/pi           = {shannon.str(50)}")
    print(f"PSWF index k    = {PROLATE_K}")
    print(f"KRD lambda_k ub = {prolate_upper.str(50)}")
    print(f"tail margin     = {tail_margin.str(50)}")
    print("CERTIFIED: m_1(xi) > 0.04 for every |xi| >= 2300")
    print("CERTIFIED: PSWF lambda_1490(c=2300) < 0.0035")
    print("CERTIFIED: Prolate tail k>=1490 has q_1 margin > 0.01")


if __name__ == "__main__":
    main()
