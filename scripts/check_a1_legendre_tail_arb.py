# -*- coding: utf-8 -*-
"""Rigorous Arb certificate for an alternative Legendre-tail reduction at a=1.

This checker does NOT certify the final finite matrix.  It certifies that the
orthogonal complement of the first M=2150 normalized Legendre polynomials has
negligible frequency-band concentration for Omega=1551, and that the remaining
rank-two moment completion contributes a negligible resolved--tail cross term.

Together with the already certified bounded multiplier

    c = 0.1,
    r(xi) = (m_1(xi)-c) 1_{|xi|<=Omega},
    ||r||_infty < 12,

this gives a rigorous Schur penalty below 7e-39.  Therefore a lower bound
1e-35 on each finite Legendre parity block is sufficient for positivity of the
full lower operator L_1 = c I + K + E^*E.

No float conversion is used in any acceptance test.
"""

from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
OMEGA = arb(1551)
C = arb("0.1")
R = arb(12)
M = 2150  # first discarded Legendre degree
ETA_TARGET = arb("4.8e-42")
PENALTY_TARGET = arb("7e-39")
FINITE_TARGET = arb("1e-35")


def odd_double_factorial(n: int) -> int:
    """n!! for positive odd n, exactly as a Python integer."""
    assert n >= 1 and n % 2 == 1
    out = 1
    for k in range(1, n + 1, 2):
        out *= k
    return out


def legendre_band_tail_bound() -> arb:
    """Bound eta_M = sum_{n>=M} <phi_n, C_Omega phi_n>.

    For normalized phi_n=sqrt(n+1/2) P_n and the nonunitary Fourier transform,

        F_n(t) = 2 i^n sqrt(n+1/2) j_n(t).

    Using |j_n(t)| <= t^n/(2n+1)!! on 0<=t<=Omega gives

        d_n <= (2/pi) Omega^(2n+1) / ((2n+1)!!)^2.

    The ratio d_{n+1}/d_n is Omega^2/(2n+3)^2, decreasing in n,
    so the infinite tail is geometrically majorized from n=M onward.
    """
    df = arb(odd_double_factorial(2 * M + 1))
    dM = (2 / PI) * (OMEGA ** (2 * M + 1)) / (df * df)
    q = (OMEGA * OMEGA) / arb((2 * M + 3) ** 2)
    if not (q < 1):
        raise RuntimeError(f"Legendre geometric ratio is not <1: q={q}")
    return dM / (1 - q)


def moment_tail_bound_one_weight() -> arb:
    """Bound ||P_tail e^{x/2}||^2 in normalized Legendre coordinates.

    For phi_n=sqrt(n+1/2) P_n,

        a_n = <phi_n,e^{x/2}> = 2 sqrt(n+1/2) i_n(1/2).

    The positive series for modified spherical Bessel gives

        i_n(z) <= z^n/(2n+1)!! * exp(z^2/(2(2n+3))).

    We square this and majorize the n-tail by its first term times a
    geometric ratio upper bound.
    """
    z = arb(1) / 2
    df = arb(odd_double_factorial(2 * M + 1))
    nu = arb(M) + arb(1) / 2
    exponent = (z * z) / arb(2 * M + 3)
    sM = 4 * nu * (z ** (2 * M)) / (df * df) * exponent.exp()

    # Ratio bound for s_{n+1}/s_n; the exponential correction decreases.
    q = ((arb(M) + arb(3) / 2) / (arb(M) + arb(1) / 2))
    q *= (z * z) / arb((2 * M + 3) ** 2)
    if not (q < 1):
        raise RuntimeError(f"moment geometric ratio is not <1: q={q}")
    return sM / (1 - q)


def main() -> None:
    eta = legendre_band_tail_bound()
    if not (eta < ETA_TARGET):
        raise RuntimeError(f"Legendre band-tail bound too large: eta={eta}")

    sigma2 = moment_tail_bound_one_weight()
    # Two moment rows e^{+x/2}, e^{-x/2}; reflection gives the same tail norm.
    delta_E = (2 * sigma2).sqrt()

    # Frobenius bound on ||E||: ||e^{x/2}||^2+||e^{-x/2}||^2=4 sinh(1).
    e1 = arb(1).exp()
    em1 = (-arb(1)).exp()
    E_norm = (2 * (e1 - em1)).sqrt()  # sqrt(4*sinh(1))

    # K=P_I F^{-1} M_r F P_I has ||K_HT|| <= R sqrt(eta).
    # Completion cross satisfies ||(E^*E)_HT|| <= ||E|| ||E P_T||.
    cross = R * eta.sqrt() + E_norm * delta_E

    # On the tail, E^*E is positive and may be discarded in the lower bound.
    tau = C - R * eta
    if not (tau > arb("0.099")):
        raise RuntimeError(f"Legendre tail floor too small: tau={tau}")

    penalty = (cross * cross) / tau
    if not (penalty < PENALTY_TARGET):
        raise RuntimeError(f"Legendre Schur penalty too large: penalty={penalty}")
    if not (FINITE_TARGET > penalty):
        raise RuntimeError("predeclared finite target does not dominate penalty")

    print("A1 orthonormal-Legendre tail Arb certificate")
    print(f"prec_bits          = {ctx.prec}")
    print(f"Omega              = {OMEGA.str(20, radius=False)}")
    print(f"first discarded n  = {M}")
    print(f"even head dim       = {M//2}")
    print(f"odd head dim        = {M//2}")
    print(f"eta_M upper         = {eta.str(60)}")
    print(f"moment tail one row = {sigma2.str(30)}")
    print(f"total cross upper   = {cross.str(60)}")
    print(f"tail tau lower      = {tau.str(60)}")
    print(f"Schur penalty upper = {penalty.str(60)}")
    print(f"finite target       = {FINITE_TARGET.str(20, radius=False)}")
    print("CERTIFIED: Legendre band-tail eta_2150 < 4.8e-42")
    print("CERTIFIED: Legendre Schur penalty < 7e-39")
    print("CERTIFIED: finite parity-block lower bound 1e-35 is sufficient for A1 positivity")


if __name__ == "__main__":
    main()
