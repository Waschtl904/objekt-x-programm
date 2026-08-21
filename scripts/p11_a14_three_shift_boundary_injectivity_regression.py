#!/usr/bin/env python3
"""Independent regression certificate for P11 R36-A14.3a.

Checks the canonical T0=2a three-shift boundary theorem at the mechanical level:
- original branch formula against the E/U split;
- lower reflection/translation matrices, determinants and commutation;
- upper delta/eta transfer matrices, determinants and commutation;
- explicit firewall for the old sign-indefinite convergent wrap-count bug;
- one-sided positive near-return mechanics with actual floor wrap counts;
- rank-two return-exponent differences and numerical line-moving witnesses.

The theorem itself is analytic.  This script is a domain/sign/algebra firewall
for the repaired A14.3a-UC2 proof.
"""

from __future__ import annotations

from math import floor, log, sqrt

EPS = 2.0e-10

A = 0.5 * log(2.0)
B = 0.5 * log(3.0)
T = 2.0 * A
D = B - A
E = T - B
DELTA = D - E
ETA = E - DELTA

P = sqrt(log(2.0)) * 2.0 ** (-0.75)      # c_{2,1}
R = sqrt(log(3.0)) * 3.0 ** (-0.75)      # c_{3,1}
Q = sqrt(log(2.0)) * 2.0 ** (-1.5)       # c_{2,2}


def mm(A0, B0):
    return [
        [A0[0][0] * B0[0][0] + A0[0][1] * B0[1][0],
         A0[0][0] * B0[0][1] + A0[0][1] * B0[1][1]],
        [A0[1][0] * B0[0][0] + A0[1][1] * B0[1][0],
         A0[1][0] * B0[0][1] + A0[1][1] * B0[1][1]],
    ]


def det(A0):
    return A0[0][0] * A0[1][1] - A0[0][1] * A0[1][0]


def inv(A0):
    d0 = det(A0)
    return [[A0[1][1] / d0, -A0[0][1] / d0],
            [-A0[1][0] / d0, A0[0][0] / d0]]


def eye():
    return [[1.0, 0.0], [0.0, 1.0]]


def maxerr(A0, B0):
    return max(abs(A0[i][j] - B0[i][j]) for i in range(2) for j in range(2))


def mpow(A0, n):
    if n < 0:
        return mpow(inv(A0), -n)
    out = eye()
    base = A0
    while n:
        if n & 1:
            out = mm(out, base)
        base = mm(base, base)
        n //= 2
    return out


def combine_terms(terms):
    out = []
    for coeff, arg in terms:
        found = False
        for item in out:
            if abs(item[1] - arg) < 1.0e-11:
                item[0] += coeff
                found = True
                break
        if not found:
            out.append([coeff, arg])
    out = [item for item in out if abs(item[0]) > 1.0e-10]
    out.sort(key=lambda item: item[1])
    return out


def same_terms(left, right):
    left = combine_terms(left)
    right = combine_terms(right)
    assert len(left) == len(right), (left, right)
    for (cl, xl), (cr, xr) in zip(left, right):
        assert abs(cl - cr) < 2.0e-10, (left, right)
        assert abs(xl - xr) < 2.0e-10, (left, right)


def original_terms(u, lo, hi):
    out = []
    for tau, coeff in ((A, P), (B, R), (T, Q)):
        y = abs(u - tau)
        if lo < y < hi:
            sgn = -1.0 if u < tau else 1.0
            out.append((sgn * coeff, y))
        y = u + tau
        if lo < y < hi:
            out.append((-coeff, y))
    return out


def expected_E_terms(x, lo, hi):
    out = []
    candidates = (
        (P, x),
        (R * (-1.0 if x < D else 1.0), abs(x - D)),
        (-Q, A - x),
    )
    for coeff, y in candidates:
        if lo < y < hi:
            out.append((coeff, y))
    return out


def expected_U_raw_terms(x, lo, hi):
    # Raw L at u=a-x equals minus the displayed positive U relation.
    out = []
    for coeff, y in (
        (-P, x),
        (-P, T - x),
        (-R, D + x),
        (-R, A + B - x),
        (-Q, A + x),
    ):
        if lo < y < hi:
            out.append((coeff, y))
    return out


def assert_branch_split():
    parameter_cases = (
        (0.02, 0.20),
        (0.02, 0.50),
        (0.10, 0.68),
        (0.30, 0.65),
        (A, 0.65),
        (0.55, 0.68),
    )
    xcuts = sorted({0.0, DELTA, E, D, A})
    probes = []
    for lo0, hi0 in zip(xcuts, xcuts[1:]):
        if hi0 - lo0 > 1.0e-12:
            probes.extend(lo0 + t * (hi0 - lo0) for t in (0.17, 0.41, 0.73))

    for lo, hi in parameter_cases:
        assert 0.0 < lo < hi < T
        for x in probes:
            same_terms(original_terms(A + x, lo, hi), expected_E_terms(x, lo, hi))
            same_terms(original_terms(A - x, lo, hi), expected_U_raw_terms(x, lo, hi))


def assert_lower_matrices():
    Rd = [
        [P / R, -Q / R],
        [(P * P - R * R) / (Q * R), -P / R],
    ]
    Re = [
        [Q / R, -P / R],
        [(Q * Q - R * R) / (P * R), -Q / R],
    ]
    Swap = [[0.0, 1.0], [1.0, 0.0]]
    Mdelta = mm(Rd, Re)
    E0 = mm(Swap, Rd)

    assert maxerr(mm(Rd, Rd), eye()) < EPS
    assert maxerr(mm(Re, Re), eye()) < EPS
    assert abs(det(Mdelta) - 1.0) < EPS
    assert abs(det(E0) - 1.0) < EPS
    assert maxerr(mm(E0, Mdelta), mm(Mdelta, E0)) < EPS
    assert abs(E0[0][1]) > 1.0e-6
    tr = E0[0][0] + E0[1][1]
    assert tr * tr - 4.0 < -1.0e-6
    return E0, Mdelta


def assert_upper_matrices():
    mu = P / Q
    kappa = (P * P - Q * Q) / (Q * R)
    Au = [
        [1.0 / mu, -kappa / mu],
        [kappa / mu, mu - kappa * kappa / mu],
    ]
    Qm = [
        [1.0, 0.0],
        [(kappa * kappa - mu * mu) / kappa, mu / kappa],
    ]
    Swap = [[0.0, 1.0], [1.0, 0.0]]
    Neta = mm(mm(mm(Swap, Qm), Swap), inv(Qm))

    assert abs(det(Au) - 1.0) < EPS
    assert abs(det(Neta) - 1.0) < EPS
    assert maxerr(mm(Au, Neta), mm(Neta, Au)) < EPS
    assert abs(Au[0][1]) > 1.0e-6
    tr = Au[0][0] + Au[1][1]
    assert tr * tr - 4.0 < -1.0e-6
    return Au, Neta


def convergents(x, count=24):
    # Return (numerator, denominator) continued-fraction convergents.
    aseq = []
    y = x
    for _ in range(count):
        ai = floor(y)
        aseq.append(ai)
        frac = y - ai
        if frac < 1.0e-15:
            break
        y = 1.0 / frac

    p_nm2, p_nm1 = 0, 1
    q_nm2, q_nm1 = 1, 0
    out = []
    for ai in aseq:
        pn = ai * p_nm1 + p_nm2
        qn = ai * q_nm1 + q_nm2
        out.append((pn, qn))
        p_nm2, p_nm1 = p_nm1, pn
        q_nm2, q_nm1 = q_nm1, qn
    return out


def assert_old_convergent_bug(alpha, ell):
    """Demonstrate the off-by-one defect repaired by A14.3a-UC2."""
    for k, n in convergents(alpha / ell, 24)[2:]:
        eps = n * alpha - k * ell
        if eps < -1.0e-10:
            actual_wraps = floor(n * alpha / ell)
            assert actual_wraps == k - 1
            assert actual_wraps != k
            return
    raise AssertionError("failed to find a negative-error convergent")


def positive_returns(alpha, ell, *, tol=1.0e-4, max_n=200000, min_count=8):
    """One-sided returns with k=floor(n*alpha/ell), hence exact wrap count."""
    out = []
    for n in range(1, max_n + 1):
        k = floor(n * alpha / ell)
        eps = n * alpha - k * ell
        if 0.0 < eps < tol:
            out.append((n, k, eps, (n - k, k)))
            if len(out) >= min_count:
                return out
    return out


def assert_positive_return_mechanics(alpha, ell, A0, B0):
    returns = positive_returns(alpha, ell)
    assert len(returns) >= 4

    # Pick a lift safely away from the circle endpoint.  Since eps<tol<<ell,
    # the actual number of wraps from this start point is exactly k.
    x = 0.25 * ell
    for n, k, eps, _ in returns:
        assert x + eps < ell
        actual_wraps = floor((x + n * alpha) / ell) - floor(x / ell)
        assert actual_wraps == k

    # The repaired analytic proof uses that the difference subgroup generated
    # by the actual exponent vectors has rank two.  Certify a concrete witness.
    base = returns[0][3]
    diffs = [
        (v[0] - base[0], v[1] - base[1])
        for _, _, _, v in returns[1:]
    ]
    rank_two = False
    for i in range(len(diffs)):
        for j in range(i + 1, len(diffs)):
            d0 = diffs[i][0] * diffs[j][1] - diffs[j][0] * diffs[i][1]
            if d0 != 0:
                rank_two = True
                break
        if rank_two:
            break
    assert rank_two

    # Numerical witness only: at least one actual one-sided return matrix moves
    # the vertical line.  The proof itself obtains existence analytically from
    # rank two plus the no-finite-power property of A0.
    moves = []
    for _, _, _, (n_no_wrap, n_wrap) in returns:
        G = mm(mpow(A0, n_no_wrap), mpow(B0, n_wrap))
        moves.append(abs(G[0][1]))
    assert max(moves) > 1.0e-7


def main():
    assert 0.0 < DELTA < E < D < A < T
    assert abs(A - (D + E)) < EPS
    assert abs(D - (E + DELTA)) < EPS
    assert abs(A - (2.0 * E + DELTA)) < EPS
    assert 0.0 < Q < P

    assert_branch_split()
    E0, Mdelta = assert_lower_matrices()
    Au, Neta = assert_upper_matrices()

    # Explicitly reject the old sign-indefinite convergent convention.
    assert_old_convergent_bug(E, D)
    assert_old_convergent_bug(DELTA, E)

    # Repaired one-sided return mechanics, with actual floor wrap counts.
    # Lower circle: length d, rotation e; wrap matrix Mdelta^{-1}.
    assert_positive_return_mechanics(E, D, E0, inv(Mdelta))
    # Upper circle: length e, rotation delta; wrap matrix Neta^{-1}.
    assert_positive_return_mechanics(DELTA, E, Au, inv(Neta))

    print("PASS: repaired A14.3a canonical three-shift boundary regressions")


if __name__ == "__main__":
    main()
