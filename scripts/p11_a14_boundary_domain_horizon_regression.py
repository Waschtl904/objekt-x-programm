#!/usr/bin/env python3
"""Independent regression checks for A14.2i domain / horizon hardening.

Checks:
1. exact old-shift boundary-horizon chart relations at T0=2a;
2. the A14.2i four-chart constructor is cut off by the newly visible source
   u=a+x when the source horizon reaches 2a;
3. the newly active tau=2a fold is a one-to-one reflected copy of h.

This script is a regression firewall, not a substitute for the analytic proof.
"""

from __future__ import annotations

from math import log, sqrt

EPS = 1.0e-10
A = 0.5 * log(2.0)
B = 0.5 * log(3.0)
D = B - A
T = 2.0 * A
C = A + B
M = A - 0.5 * D
C2 = sqrt(log(2.0)) * 2.0 ** (-0.75)
C3 = sqrt(log(3.0)) * 3.0 ** (-0.75)
C22 = sqrt(log(2.0)) * 2.0 ** (-1.5)
RHO = C3 / C2


def close(x, y, tol=EPS):
    return abs(x - y) <= tol


def active_terms(u, R, S, T0, include_2a=False):
    shifts = [("a", A, C2), ("b", B, C3)]
    if include_2a:
        shifts.append(("2a", T, C22))

    out = []
    for label, tau, weight in shifts:
        folded = abs(u - tau)
        if R < folded < S:
            sign = -1.0 if u < tau else 1.0
            out.append((sign * weight, folded, f"{label}-fold"))

        forward = u + tau
        if R < forward < S:
            out.append((-weight, forward, f"{label}-forward"))
    return out


def combine(terms):
    data = []
    for coeff, arg, _ in terms:
        for item in data:
            if close(item[1], arg):
                item[0] += coeff
                break
        else:
            data.append([coeff, arg])
    data = [x for x in data if abs(x[0]) > EPS]
    data.sort(key=lambda x: x[1])
    return data


def same_terms(left, right):
    left = combine(left)
    right = combine(right)
    assert len(left) == len(right), (left, right)
    for (cl, xl), (cr, xr) in zip(left, right):
        assert close(cl, cr), (left, right)
        assert close(xl, xr), (left, right)


def expected_low(y, R, S):
    # Source u=a+y, valid for y<a at T0=2a.
    out = [(C2, y, "self")]
    pred = abs(y - D)
    if R < pred < S:
        sign = 1.0 if y > D else -1.0
        out.append((C3 * sign, pred, "b-fold predecessor"))
    return out


def expected_high(y, R, S):
    # Source u=y-a, valid for y>a at T0=2a, after no simplification.
    out = [(-C2, y, "a-forward self")]

    afold = T - y
    if R < afold < S:
        out.append((-C2, afold, "a-fold"))

    bfold = C - y
    if R < bfold < S:
        out.append((-C3, bfold, "b-fold"))

    bforward = y + D
    if R < bforward < S:
        out.append((-C3, bforward, "b-forward"))
    return out


def assert_boundary_relations(R, S):
    assert 0.0 < R < S < T

    # Low chart: sample every indicator cell induced by d and its R/S shifts.
    low_hi = min(S, A)
    if R < low_hi:
        pts = {R, low_hi}
        for x in (D, D - R, D + R, D - S, D + S):
            if R < x < low_hi:
                pts.add(x)
        pts = sorted(pts)
        for lo, hi in zip(pts, pts[1:]):
            if hi - lo <= EPS:
                continue
            y = 0.5 * (lo + hi)
            same_terms(active_terms(A + y, R, S, T), expected_low(y, R, S))

    # High chart: source u=y-a for all y>a.
    high_lo = max(R, A)
    if high_lo < S:
        pts = {high_lo, S}
        for x in (B, C - R, C - S, S - D, R - D):
            if high_lo < x < S:
                pts.add(x)
        pts = sorted(pts)
        for lo, hi in zip(pts, pts[1:]):
            if hi - lo <= EPS:
                continue
            y = 0.5 * (lo + hi)
            same_terms(active_terms(y - A, R, S, T), expected_high(y, R, S))


def old_lambda(R, S, T0):
    return max(R, T0 - A, C - S, M)


def f_base(x):
    return 1.0 + 0.41 * x


def old_four_chart_h(y, R, S, T0):
    lam = old_lambda(R, S, T0)
    if not lam < A:
        return 0.0

    if lam < y < A:
        return f_base(y)
    if A < y < 2.0 * A - lam:
        return -f_base(2.0 * A - y)
    if lam + D < y < B:
        return RHO * f_base(y - D)
    if B < y < C - lam:
        return -RHO * f_base(C - y)
    return 0.0


def eval_old_operator(u, R, S, source_horizon, constructor_horizon):
    value = 0.0
    for coeff, arg, _ in active_terms(u, R, S, source_horizon):
        value += coeff * old_four_chart_h(arg, R, S, constructor_horizon)
    return value


def assert_four_chart_horizon_obstruction(R, S, T_old):
    assert 0.0 < R < A < B < S < T_old < T
    lam = old_lambda(R, S, T_old)
    assert lam < A

    # Old construction is designed so a+x > T_old.
    for theta in (0.2, 0.5, 0.8):
        x = lam + theta * (A - lam)
        u = A + x
        assert u > T_old
        assert u < T

        # At the boundary source horizon the newly visible old a-fold sees x.
        val = eval_old_operator(u, R, S, T, T_old)
        assert abs(val - C2 * f_base(x)) <= 5.0e-10, (x, u, val)
        assert abs(val) > 1.0e-6

    # If one tries to impose the old lambda rule with T0=2a, I is empty.
    assert old_lambda(R, S, T) >= A - EPS


def assert_new_2a_fold(R, S):
    assert 0.0 < R < S < T
    for theta in (0.1, 0.3, 0.5, 0.7, 0.9):
        y = R + theta * (S - R)
        u = T - y
        terms = [term for term in active_terms(u, R, S, T, include_2a=True) if term[2] == "2a-fold"]
        assert len(terms) == 1
        coeff, arg, _ = terms[0]
        assert close(coeff, -C22)
        assert close(arg, y)


if __name__ == "__main__":
    # Boundary old-shift relations throughout qualitatively different regions.
    boundary_cases = (
        (0.02, 0.10),
        (0.05, 0.30),
        (0.10, 0.50),
        (0.10, 0.60),
        (0.30, 0.65),
        (0.40, 0.65),
        (0.60, 0.68),
    )
    for R, S in boundary_cases:
        assert_boundary_relations(R, S)
        assert_new_2a_fold(R, S)

    # Deterministic sweep across 0<R<S<2a.
    for i in range(1, 9):
        S = 0.04 + i * (T - 0.05) / 9.0
        if not (0.02 < S < T):
            continue
        for j in range(1, 6):
            R = 0.01 + j * (S - 0.02) / 6.0
            if 0.0 < R < S:
                assert_boundary_relations(R, S)
                assert_new_2a_fold(R, S)

    # Old four-chart kernel channel: valid below 2a, broken by source-horizon opening.
    for case in (
        (0.10, 0.60, 0.68),
        (0.30, 0.65, 0.68),
        (A - 0.01, 0.60, 0.68),
    ):
        assert_four_chart_horizon_obstruction(*case)

    assert abs((C2 / C3) ** 2 - 1.0) > 1.0e-6
    assert C22 > 0.0
    print("PASS: A14.2i domain/horizon hardening and boundary diagnostics")
