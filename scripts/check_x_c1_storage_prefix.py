#!/usr/bin/env python3
"""Exact scalar checks for X-C1-STORAGE, not a finite positivity certificate.

Standard library only. Analytic hypotheses and the smooth NULLPOL extension
are proved in X_C1_STORAGE.md. This script checks rational constants, the
polynomial prefix integrals, Green coefficients and the normalized Prime-2
mixed matrix. No numerical quadrature, A1 data, C0 replay, matrix builds or CI.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import factorial

CHECKS = 0


def require(ok: bool, label: str) -> None:
    global CHECKS
    if not ok:
        raise AssertionError("FAIL: " + label)
    CHECKS += 1
    print("PASS: " + label)


def poly_integral(coefficients: dict[int, F], endpoint: F) -> F:
    if any(power < 0 for power in coefficients):
        raise ValueError("polynomial powers must be nonnegative")
    return sum((c * endpoint ** (n + 1) / (n + 1)
                for n, c in coefficients.items()), F(0))


def main() -> None:
    # e < sum_{k=0}^3 1/k! + (1/4!)/(1-1/5) < 11/4.
    # Combined in the proof with pi>3 and gamma>=0, this gives kappa_*>9/2.
    e_cap = sum((F(1, factorial(k)) for k in range(4)), F(0))
    e_cap += F(1, factorial(4)) / (1 - F(1, 5))
    require(e_cap == F(87, 32) < F(11, 4), "factorial-series upper bound e<11/4")
    require(F(11, 4) ** 3 < 24, "e^3<24, hence log(24)>3")
    require(F(11, 4) < 4, "e^(1/2)<2, hence log(2)>1/2")
    require(F(3) + F(3, 2) == F(9, 2), "lower threshold from log(8pi) and pi/2")

    length = F(1, 2)
    energy = length / 3
    require(energy == F(1, 6), "ramp prefix L2 energy is 1/6")
    # Integrated causal squared difference / energy for t<=length.
    shape = {2: 3 / length ** 2, 3: -2 / length ** 3}
    require(sum((c * length ** n for n, c in shape.items()), F(0)) == 1,
            "prefix shape equals one at t=length")
    derivative = {n - 1: n * c for n, c in shape.items()}
    require(derivative == {1: 6 / length ** 2, 2: -6 / length ** 3},
            "prefix shape derivative is (6t/L^2)(1-t/L)")
    small = poly_integral(shape, length)
    small += poly_integral({n - 1: c / 2 for n, c in shape.items()}, length)
    require(small == length / 2 + F(5, 12) == F(2, 3),
            "small-delay bound is L/2+5/12=2/3")
    # Analytically: integral_L^inf h < 2 + (1/2)log 2 + e^(-1/2) <7/2.
    tail_cap = F(2) + F(1, 2) + F(1)
    require(tail_cap == F(7, 2), "large-delay bound is below 7/2")
    ratio_cap = small + tail_cap
    require(ratio_cap == F(25, 6), "archimedean prefix ratio below 25/6")
    arch_cap = ratio_cap * energy
    require(arch_cap == F(25, 36) < 1, "ramp archimedean energy below 25/36<1")
    raw_supply_cap = arch_cap - F(9, 2) * energy
    require(raw_supply_cap == -F(1, 18), "unsmoothed prefix supply below -1/18")

    # Fixed one-sided mollifier width, chosen before any numerical test.
    eps = F(1, 10**6)
    delta_arch_cap = F(7, 3) * eps + 24 * eps * eps
    require(delta_arch_cap < 3 * eps, "mollification archimedean error energy below 3eps")
    root_cap = F(2, 1000)
    require(3 * eps < root_cap * root_cap, "sqrt(error energy)<2/1000")
    require(energy - eps > 0, "smoothed prefix energy lower bound is positive")
    smooth_supply_cap = arch_cap + 2 * root_cap + 3 * eps
    smooth_supply_cap -= F(9, 2) * (energy - eps)
    require(smooth_supply_cap == -F(1, 18) + F(4, 1000) + F(15, 2) * eps,
            "complete smoothing budget includes the changed L2 term")
    require(smooth_supply_cap < -F(1, 20), "explicit smooth prefix supply is below -1/20")
    require(F(1, 2) + F(1, 4) + F(1, 100) < 1,
            "future moment-correction bumps fit strictly inside I_1")

    # Coefficient vectors use (|u(x-t)|^2, Re[u(x-t)conj(u(x))], |u(x)|^2).
    # Delay memory derivative is w*(|u(x)|^2-|u(x-t)|^2).
    memory_derivative = (-1, 0, 1)
    prime_supply = (1, -2, -1)
    gamma_supply = (1, -2, 1)
    require(tuple(a + b for a, b in zip(prime_supply, memory_derivative)) == (0, -2, 0),
            "centered prime supply plus memory derivative is the negative mixed port")
    require(tuple(a + b for a, b in zip(gamma_supply, memory_derivative)) == (0, -2, 2),
            "Gamma supply plus memory derivative is its causal boundary pairing")
    require((prime_supply[0], prime_supply[2]) ==
            (-memory_derivative[0], -memory_derivative[2]),
            "exterior-channel supply equals MINUS the positive-memory derivative")
    # For P_mu=exp(-(mu-1/4)(r+s)), bulk Green coefficient is -2mu.
    require(-2 * (-F(1, 4)) - F(1, 2) == 0,
            "Hankel Green coefficient has no constant remainder: -2(mu-1/4)-1/2=-2mu")

    jump_gram = ((2, -1), (-1, 2))
    prime_gram = tuple(tuple(jump_gram[i][j] - (2 if i == j else 0)
                             for j in range(2)) for i in range(2))
    require(prime_gram == ((0, -1), (-1, 0)), "Prime-2 normalized mixed coefficient is -1")
    require(prime_gram[0][0] * prime_gram[1][1] - prime_gram[0][1] * prime_gram[1][0] == -1,
            "centered isolated Prime-2 block is indefinite, not a proposed positive residual")
    require(sum(sum(row) for row in prime_gram) == -2,
            "normalized Prime-2 value on f+g is -2")
    require(sum(prime_gram[i][j] * (1, -1)[i] * (1, -1)[j]
                for i in range(2) for j in range(2)) == 2,
            "normalized Prime-2 value on f-g is +2")

    print(f"TOTAL: {CHECKS} exact rational/algebraic checks PASS")
    print("The smooth-prefix bound follows from the analytic estimates in X_C1_STORAGE.md.")
    print("The no-go concerns s=nonnegative residual + derivative of nonnegative causal storage.")
    print("No claim of negative full Weil energy, failed C0 geometry, or an A1/RH conclusion.")


if __name__ == "__main__":
    main()
