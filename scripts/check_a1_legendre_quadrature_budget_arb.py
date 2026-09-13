# -*- coding: utf-8 -*-
"""Rigorous Arb budget for the final A1 Legendre matrix quadrature.

This checker does NOT assemble or certify the final 1075x1075 parity blocks.
It certifies that a concrete panel/Gauss rule can make the *analytic quadrature
remainder* negligible compared with the predeclared Legendre head target 1e-35.

Setup inherited from A1-LEGENDRE (#117):

    Omega = 1551,
    c = 0.1,
    r(xi) = (m_1(xi)-c) 1_{|xi|<=Omega},
    normalized Legendre orders n=0,...,2149.

For same parity,

    K_nm = (4/pi) sqrt(nu_n nu_m) phase * integral_0^Omega r(xi) j_n(xi) j_m(xi) dxi.

We split [0,1551] into panels of width <= 0.4 and use 40-point
Gauss--Legendre on every panel.  On the Bernstein ellipse whose semiminor
reaches |Im xi|=0.4, rho=2+sqrt(5).  The analytic continuation is obtained by
replacing Re psi by the symmetric half-sum of the two digamma branches.

The numerical constants below certify:

    |r(z)| < 42 on the strip/ellipse,
    |full matrix integrand| < 260000,
    per-parity operator quadrature remainder < 4e-38.

No binary float enters an acceptance test.
"""

from flint import arb, ctx

ctx.prec = 256

PI = arb.pi()
C = arb(1) / 10
OMEGA = arb(1551)
STRIP = arb(2) / 5          # 0.4
PANEL = arb(2) / 5          # 0.4
HALF_PANEL = PANEL / 2      # 0.2
GAUSS_N = 40
PANELS = 3878               # ceil(1551 / 0.4)
PARITY_DIM = 1075           # orders 0..2148 or 1..2149
NMAX = 2149

R_BOUND_TARGET = arb(42)
INTEGRAND_BOUND_TARGET = arb(260000)
OP_ERROR_TARGET = arb("4e-38")
HEAD_TARGET = arb("1e-35")


def von_mangoldt_weight(n: int, p: int) -> arb:
    return arb(p).log() / arb(n).sqrt()


def strip_digamma_bound() -> arb:
    """Uniform bound for |psi(w)| when Re w>=0.05, |Im w|<=775.5.

    Shift w -> u=w+20.  Then Re u>=20.05.  Binet's formula gives

      |psi(u)| <= |log u| + 1/(2|u|) + 1/(12 Re(u)^2).

    We use |log u| <= log(776)+pi/2.  The recurrence

      psi(w) = psi(w+20) - sum_{k=0}^{19} 1/(w+k)

    is bounded by replacing |w+k| with k+0.05.
    """
    a = arb(20) + arb(1) / 20   # 20.05
    shifted = arb(776).log() + PI / 2
    shifted += 1 / (2 * a)
    shifted += 1 / (12 * a * a)

    rec = arb(0)
    for k in range(20):
        rec += 1 / (arb(k) + arb(1) / 20)
    return shifted + rec


def prime_comb_strip_bound() -> arb:
    # |cos(z log n)| <= cosh(0.4 log n) for |Im z|<=0.4.
    active = ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7))
    s = arb(0)
    for n, p in active:
        w = von_mangoldt_weight(n, p)
        s += 2 * w * (STRIP * arb(n).log()).cosh()
    return s


def main() -> None:
    psi_bound = strip_digamma_bound()
    prime_bound = prime_comb_strip_bound()

    # The analytic continuation of Re psi is a half-sum of two digamma terms;
    # each obeys the same psi_bound, so the half-sum also does.
    r_bound = psi_bound + PI.log() + C + prime_bound
    if not (r_bound < R_BOUND_TARGET):
        raise RuntimeError(f"strip multiplier bound failed: r_bound={r_bound}")

    # Poisson representation: |j_n(z)| <= exp(|Im z|).
    nu_max = arb(NMAX) + arb(1) / 2
    integrand_bound = (4 / PI) * nu_max * (2 * STRIP).exp() * r_bound
    if not (integrand_bound < INTEGRAND_BOUND_TARGET):
        raise RuntimeError(f"integrand bound failed: M={integrand_bound}")

    # For panel half-width 0.2 and strip height 0.4, normalized ellipse
    # semiminor is b=2, hence Bernstein rho=b+sqrt(1+b^2)=2+sqrt(5).
    rho = arb(2) + arb(5).sqrt()
    gauss_panel_error = (
        4 * INTEGRAND_BOUND_TARGET * rho
        / ((rho - 1) * (rho ** (2 * GAUSS_N) - 1))
    )
    entry_error = arb(PANELS) * gauss_panel_error
    op_error = arb(PARITY_DIM) * entry_error

    if not (op_error < OP_ERROR_TARGET):
        raise RuntimeError(f"operator quadrature budget failed: op_error={op_error}")
    if not (HEAD_TARGET > 100 * op_error):
        raise RuntimeError(
            f"quadrature budget has insufficient clearance: head={HEAD_TARGET}, op={op_error}"
        )

    print("A1 Legendre quadrature-budget Arb certificate")
    print(f"prec_bits              = {ctx.prec}")
    print(f"digamma strip bound    = {psi_bound.str(50)}")
    print(f"prime strip bound      = {prime_bound.str(50)}")
    print(f"r strip bound          = {r_bound.str(50)}")
    print(f"integrand bound        = {integrand_bound.str(50)}")
    print(f"rho                    = {rho.str(50)}")
    print(f"panels                 = {PANELS}")
    print(f"Gauss order            = {GAUSS_N}")
    print(f"per-panel error        = {gauss_panel_error.str(60)}")
    print(f"per-entry error        = {entry_error.str(60)}")
    print(f"parity operator error  = {op_error.str(60)}")
    print(f"finite head target     = {HEAD_TARGET.str(20, radius=False)}")
    print("CERTIFIED: |r(z)| < 42 on the A1 Legendre quadrature strip")
    print("CERTIFIED: Gauss-40 panel width 0.4 gives parity operator quadrature error < 4e-38")
    print("CERTIFIED: analytic quadrature error is >100 times below the 1e-35 head target")


if __name__ == "__main__":
    main()
