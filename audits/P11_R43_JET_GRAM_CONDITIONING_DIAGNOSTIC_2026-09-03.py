#!/usr/bin/env python3
"""
R43 diagnostic: normalized constrained-Gamma higher-jet Gram conditioning.

This is a numerical diagnostic, not a proof and not an independent certificate.

It Galerkin-approximates the odd finite-window Gamma Hilbert space on (-S,S)
using the L2-orthonormal sine basis

    e_j(x) = S^{-1/2} sin(j*pi*x/S),  j >= 1.

The exact R33 multiplier is

    m_Gamma(xi)
      = 1 + Re psi(1/4 + i xi/2) - psi(1/4).

For jet functionals beta_m with odd L2 kernels
    phi_m(x) = sgn(x) I_m(|x|),
    I_m(r) = int_0^r s^m exp(-s/2) ds,

the Galerkin unconstrained Riesz Gram is B A^{-1} B^T.
The beta_0 constraint is imposed by orthogonally projecting each whitened
Riesz vector off the whitened beta_0 vector.  Every remaining vector is then
normalized before the singular-value test, so raw jet scaling is removed.

For an m-vector normalized family Y_m, the normalized Gram is Y_m^T Y_m and

    lambda_min(Gram_m) = sigma_min(Y_m)^2.

Run:
    python audits/P11_R43_JET_GRAM_CONDITIONING_DIAGNOSTIC_2026-09-03.py
"""

from __future__ import annotations

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy import special
from scipy.linalg import cholesky, solve_triangular, svdvals


def m_gamma(xi: np.ndarray) -> np.ndarray:
    return (
        1.0
        + np.real(special.digamma(0.25 + 0.5j * xi))
        - special.digamma(0.25)
    )


def fourier_sine_basis_amplitude(xi: np.ndarray, S: float, P: int) -> np.ndarray:
    """
    Real amplitude F with \hat e_j(xi) = -i F_j(xi).
    np.sinc(t)=sin(pi t)/(pi t), so removable resonances are stable.
    """
    xi = np.asarray(xi)
    j = np.arange(1, P + 1)[:, None]
    z = xi[None, :] * S / np.pi
    return np.sqrt(S) * (np.sinc(j - z) - np.sinc(j + z))


def gamma_form_matrix(
    S: float,
    P: int,
    nq: int = 300,
    segments=(0.0, 20.0, 60.0, 180.0, 540.0, 1620.0),
) -> np.ndarray:
    """
    A_ij = (1/2pi) int_R m_Gamma \hat e_i overline{\hat e_j}.
    Evenness reduces this to (1/pi) int_0^infty.
    """
    A = np.zeros((P, P), dtype=float)
    nodes, weights = leggauss(nq)
    for a, b in zip(segments[:-1], segments[1:]):
        xi = 0.5 * (b - a) * nodes + 0.5 * (a + b)
        w = 0.5 * (b - a) * weights
        F = fourier_sine_basis_amplitude(xi, S, P)
        wm = w * m_gamma(xi) / np.pi
        A += (F * wm[None, :]) @ F.T
    return A


def jet_values(x: np.ndarray, M: int) -> np.ndarray:
    """
    I_m(x) = 2^(m+1) Gamma(m+1) P(m+1,x/2).
    """
    x = np.asarray(x)
    out = np.empty((M + 1, len(x)), dtype=float)
    for m in range(M + 1):
        out[m] = (
            2.0 ** (m + 1)
            * special.gamma(m + 1)
            * special.gammainc(m + 1, x / 2.0)
        )
    return out


def jet_matrix(S: float, P: int, M: int, nq: int = 600) -> np.ndarray:
    """
    B_mj = beta_m(e_j) = 2 int_0^S I_m(x) e_j(x) dx.
    """
    nodes, weights = leggauss(nq)
    x = 0.5 * S * (nodes + 1.0)
    w = 0.5 * S * weights
    I = jet_values(x, M)
    j = np.arange(1, P + 1)[:, None]
    E = np.sin(j * np.pi * x[None, :] / S) / np.sqrt(S)
    return 2.0 * (I * w[None, :]) @ E.T


def normalized_constrained_riesz_columns(
    S: float,
    P: int,
    M: int,
    nq_A: int = 300,
    nq_B: int = 600,
) -> tuple[np.ndarray, np.ndarray]:
    A = gamma_form_matrix(S, P, nq_A)
    B = jet_matrix(S, P, M, nq_B)

    # If A=L L^T and A g_m=B_m^T, then z_m=L^T g_m=L^{-1}B_m^T.
    # Euclidean inner products of z_m are exactly Gamma inner products.
    L = cholesky(A, lower=True, check_finite=False)
    Z = solve_triangular(L, B.T, lower=True, check_finite=False)

    z0 = Z[:, 0]
    Y = Z[:, 1:].copy()
    Y -= z0[:, None] * (z0 @ Y)[None, :] / (z0 @ z0)

    norms = np.linalg.norm(Y, axis=0)
    Y /= norms[None, :]
    return Y, A


def table_for_radius(S: float, P: int = 120, M: int = 16) -> list[tuple]:
    Y, A = normalized_constrained_riesz_columns(S, P, M)
    rows = []
    for m in (4, 8, 12, 16):
        s = svdvals(Y[:, :m])
        sigma_min = float(s[-1])
        lambda_min = sigma_min * sigma_min
        cond_gram = float((s[0] / s[-1]) ** 2)
        rows.append((S, P, m, sigma_min, lambda_min, cond_gram, np.linalg.cond(A)))
    return rows


def resolution_check(S: float = 1.0, M: int = 16) -> None:
    print("\nResolution check at S=1 (sigma_min):")
    print("P      m=4             m=8             m=12            m=16")
    for P in (40, 60, 80, 100, 120):
        Y, _ = normalized_constrained_riesz_columns(
            S, P, M, nq_A=260, nq_B=500
        )
        vals = [svdvals(Y[:, :m])[-1] for m in (4, 8, 12, 16)]
        print(
            f"{P:<6d}"
            + " ".join(f"{v: .6e}" for v in vals)
        )


def cutoff_check(S: float = 1.0, P: int = 100, M: int = 16) -> None:
    print("\nFourier-cutoff check at S=1, P=100 (sigma_min):")
    print("Xi_max   m=4             m=8             m=12            m=16")
    for segments in (
        (0.0, 20.0, 60.0, 180.0, 540.0),
        (0.0, 20.0, 60.0, 180.0, 540.0, 1620.0),
        (0.0, 20.0, 60.0, 180.0, 540.0, 1620.0, 4860.0),
    ):
        A = gamma_form_matrix(S, P, nq=260, segments=segments)
        B = jet_matrix(S, P, M, nq=500)
        L = cholesky(A, lower=True, check_finite=False)
        Z = solve_triangular(L, B.T, lower=True, check_finite=False)
        z0 = Z[:, 0]
        Y = Z[:, 1:].copy()
        Y -= z0[:, None] * (z0 @ Y)[None, :] / (z0 @ z0)
        Y /= np.linalg.norm(Y, axis=0)[None, :]
        vals = [svdvals(Y[:, :m])[-1] for m in (4, 8, 12, 16)]
        print(
            f"{segments[-1]:<9.0f}"
            + " ".join(f"{v: .6e}" for v in vals)
        )


def main() -> None:
    print("Normalized constrained-Gamma higher-jet Gram diagnostic")
    print("S    P   m   sigma_min        lambda_min(Gram)  cond(Gram)")
    for S in (0.5, 1.0, 2.0, 4.0):
        for row in table_for_radius(S):
            S0, P, m, sigma_min, lambda_min, cond_gram, _ = row
            print(
                f"{S0:<4.1f} {P:<3d} {m:<3d} "
                f"{sigma_min: .6e}   {lambda_min: .6e}   {cond_gram: .6e}"
            )

    resolution_check()
    cutoff_check()

    # Log-linear diagnostic at S=1.
    Y, _ = normalized_constrained_riesz_columns(1.0, 120, 16)
    ms = np.arange(2, 17)
    sig = np.array([svdvals(Y[:, :m])[-1] for m in ms])
    slope, intercept = np.polyfit(ms, np.log10(sig), 1)
    print("\nS=1 log10(sigma_min) least-squares fit for m=2..16:")
    print(f"log10 sigma_min ~= {slope:.6f} m + {intercept:.6f}")
    print(
        "Diagnostic only: a stable negative linear slope is evidence of "
        "geometric/exponential conditioning loss, not a proof."
    )


if __name__ == "__main__":
    main()
