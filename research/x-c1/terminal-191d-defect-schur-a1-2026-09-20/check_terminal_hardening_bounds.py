#!/usr/bin/env python3
"""Exact rational propagation for the terminal a=1 source hardening.

This checker propagates already proved finite-Legendre and tail bounds through
the exact moment-neutral source chart. It proves only the comparison budget.
The separate exact-integer LDL must certify the dyadic source floor.
"""
from fractions import Fraction as F
from math import factorial


def req(cond, label):
    if not cond:
        raise RuntimeError("FAIL: " + label)
    print("PASS " + label)


def e_upper():
    partial = sum((F(1, factorial(k)) for k in range(7)), F(0))
    first = F(1, factorial(7))
    tail = first / (1 - F(1, 8))
    return partial + tail


def main():
    # Elementary analytic constants used in the source chart.
    eu = e_upper()
    req(eu < F(11, 4), "Taylor majorant e < 11/4")
    sinh1_upper = (F(11, 4) - F(4, 11)) / 2
    req(sinh1_upper < F(6, 5), "sinh(1) < 6/5")

    # Exact parity moment identities:
    # ||a_even||^2 = 1+sinh(1), ||a_odd||^2=sinh(1)-1.
    req(1 + F(6, 5) < F(3, 2) ** 2,
        "even exact moment-vector norm < 3/2")
    req(F(6, 5) - 1 < F(1, 2) ** 2,
        "odd exact moment-vector norm < 1/2")

    # Carrier lower bounds:
    # even a0 = 2 sqrt(2) sinh(1/2) > sqrt(2) > 7/5.
    req(F(2) > F(7, 5) ** 2, "even carrier a0 > 7/5")
    # odd a1 > sqrt(3/2)/3 > 2/5 from sinh(x/2)>x/2.
    req(F(1, 6) > F(2, 5) ** 2, "odd carrier a1 > 2/5")

    q = F(1, 2 ** 161)
    req(33 * q < F(1, 100), "dyadic moment-vector l2 error < 1/100")

    # Exact source chart Z and dyadic chart Zd. Uniform parity bounds.
    z2 = F(169, 64)           # ||Z||^2 < (13/8)^2
    z = F(13, 8)
    zd = F(5, 3)
    req(F(421, 196) < z2, "even exact source chart norm < 13/8")
    req(F(41, 16) < z2, "odd exact source chart norm < 13/8")
    req(1 + F(151, 139) ** 2 < zd ** 2,
        "even dyadic source chart norm < 5/3")
    req(1 + F(17, 13) ** 2 < zd ** 2,
        "odd dyadic source chart norm < 5/3")

    # Ratio perturbation for the carrier correction.
    dz = 93 * q
    exact_ratio_bound = (
        33 * q / F(2, 5)
        + F(151, 100) * q / (F(2, 5) * F(39, 100))
    )
    req(exact_ratio_bound < dz, "source-chart perturbation ||Z-Zd|| < 93*2^-161")

    # Imported finite-head operator ledger:
    # ||A_head-A_head^dyad|| < 4.5e-38.
    eps_head = F(45, 10 ** 39)
    # Exact completed head norm < 33/2; dyadic head norm <17.
    req(F(1, 10) + 12 + 2 * F(11, 5) == F(33, 2),
        "exact completed finite-head norm majorant = 33/2")
    ad_norm = F(17)
    finite_source_error = z2 * eps_head + dz * ad_norm * (z + zd)
    req(finite_source_error < F(12, 10 ** 38),
        "finite-head source-chart comparison < 1.2e-37")

    # Imported complete Legendre tail inputs:
    # tau>0.099, b^2/tau<7e-39, sigma^2<1e-15054.
    # Since tau<0.1, b<3e-20. The source carrier correction from the
    # omitted moment tail is vastly below 1e-1000.
    b = F(3, 10 ** 20)
    rho = F(1, 10 ** 1000)
    tail_floor = F(98, 1000)
    req(F(99, 1000) - 2 * b * rho - 17 * rho * rho > tail_floor,
        "source-corrected omitted-tail floor > 0.098")
    tail_penalty = z2 * (b + 17 * rho) ** 2 / tail_floor
    req(tail_penalty < F(3, 10 ** 38),
        "source-corrected omitted-tail Schur penalty < 3e-38")

    total = finite_source_error + tail_penalty
    req(total < F(15, 10 ** 38),
        "total terminal hardening loss < 1.5e-37")

    dyad_floor = F(1, 10 ** 34)
    reserve = dyad_floor - total
    req(reserve > F(99, 10 ** 36),
        "1e-34 dyadic source floor leaves exact reserve > 9.9e-35")

    print("FINITE_SOURCE_ERROR_UPPER =", float(finite_source_error))
    print("TAIL_PENALTY_UPPER       =", float(tail_penalty))
    print("TOTAL_HARDENING_UPPER    =", float(total))
    print("CONDITIONAL_EXACT_RESERVE=", float(reserve))
    print("CONDITIONAL: if the exact-integer dyadic source LDL certifies M_d>1e-34 I,")
    print("then the exact terminal two-Mellin source form is strictly positive.")
    print("FIREWALL: this scalar propagation does not itself certify the dyadic LDL.")


if __name__ == "__main__":
    main()
