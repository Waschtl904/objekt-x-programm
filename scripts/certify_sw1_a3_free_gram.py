#!/usr/bin/env python3
"""
SW1-A3 algebraic/mechanical certificate.

Scope:
- exact finite-dimensional realizations of the free Gram operator
  Gfr = J^* (I + R^*R) J;
- exact verification of Gram factorization, positivity skeleton,
  compressed-inverse identity, variational equation, and the
  support-disjoint z/h identity-term firewall;
- exact rational arithmetic via SymPy.

Firewall:
This script does NOT machine-prove the infinite-dimensional Hilbert-space
claims (bounded inverse theorem, coercivity constants in operator norm,
Lax-Milgram/variational functional analysis, or the full finite-cell
L2-operator statement). Those require the separate mathematical audit.
"""

import sympy as sp


def full_rank_J(n, m):
    assert m <= n
    J = sp.zeros(n, m)
    for i in range(n):
        for j in range(m):
            J[i, j] = sp.Rational((i + 1) ** j + (j + 1), i + j + 2)
    # Stabilize the top square block by adding identity.
    for j in range(m):
        J[j, j] += 2
    assert J.rank() == m
    return J


def rest_matrix(p, n):
    R = sp.zeros(p, n)
    for i in range(p):
        for j in range(n):
            R[i, j] = sp.Rational((i + 2) * (j + 1) + (-1) ** (i + j), i + j + 3)
    return R


def certify_case(n, m, p):
    J = full_rank_J(n, m)
    R = rest_matrix(p, n)
    T = sp.simplify(sp.eye(n) + R.T * R)
    Gfr = sp.simplify(J.T * T * J)

    assert Gfr == Gfr.T
    assert Gfr.det() != 0

    # Exact A3.9 Gram factorization.
    rhs = sp.simplify(J.T * J + (R * J).T * (R * J))
    assert sp.simplify(Gfr - rhs) == sp.zeros(m)

    # Positivity skeleton: Gfr - J^*J is an exact Gram matrix.
    rest_gram = sp.simplify(Gfr - J.T * J)
    assert sp.simplify(rest_gram - (R * J).T * (R * J)) == sp.zeros(m)

    # Orthogonal projection onto K=Ran(J).
    P = sp.simplify(J * (J.T * J).inv() * J.T)
    assert sp.simplify(P * P - P) == sp.zeros(n)
    assert sp.simplify(P.T - P) == sp.zeros(n)
    assert sp.simpl(P * J - J) == sp.zeros(n, m)

    # A3.13 candidate ambient operator:
    # R_K = J (J^* T J)^(-1) J^*.
    RK = sp.simplify(J * Gfr.inv() * J.T)

    # It maps into K and solves P T k = P z for every z.
    assert sp.simplify((sp.eye(n) - P) * RK) == sp.zeros(n)
    assert sp.simplify(P * T * RK - P) == sp.zeros(n)

    # Uniqueness on K: if k=J xi and P T k=0 then xi=0.
    assert Gfr.det() != 0

    # Variational equation for deterministic exact source vectors.
    for seed in range(1, 4):
        z = sp.Matrix([
            sp.Rational((seed + 1) * (i + 2) + (-1) ** i, i + seed + 2)
            for i in range(n)
        ])
        xi = sp.simplify(Gfr.inv() * J.T * z)
        assert sp.simplify(Gfr * xi - J.T * z) == sp.zeros(m, 1)

        k = sp.simplify(J * xi)
        assert sp.simplify(P * T * k - P * z) == sp.zeros(n, 1)
        assert sp.simplify(RK * z - k) == sp.zeros(n, 1)

    return {
        "n": n,
        "m": m,
        "p": p,
        "rank_J": J.rank(),
        "rank_Gfr": Gfr.rank(),
    }


def certify_support_firewall():
    # Coordinate model of KNF:
    # z occupies blind physical rows only.
    # h occupies free sampled rows, and reconstruction from h occupies
    # additional sampled rows. Therefore z and h physical supports are disjoint.
    zdim = 3
    hdim = 5
    recon = 2
    n = zdim + hdim + recon

    Jz = sp.zeros(n, zdim)
    Jz[:zdim, :] = sp.eye(zdim)

    Jh = sp.zeros(n, hdim)
    Jh[zdim:zdim + hdim, :] = sp.eye(hdim)

    # Two reconstructed sampled rows from h only.
    Jh[zdim + hdim, :] = sp.Matrix([[1, -2, 2, -3, 3]])
    Jh[zdim + hdim + 1, :] = sp.Matrix([[2, 1, -1, 1, -2]])

    J = sp.Matrix.hstack(Jz, Jh)
    identity_gram = sp.simplify(J.T * J)

    cross = identity_gram[:zdim, zdim:]
    assert cross == sp.zeros(zdim, hdim)
    assert identity_gram[zdim:, :zdim] == sp.zeros(hdim, zdim)

    return {"physical_rows": n, "zdim": zdim, "hdim": hdim}


def main():
    cases = [(5, 2, 3), (6, 3, 4), (7, 3, 5), (8, 4, 5)]
    results = [certify_case(*case) for case in cases]
    support = certify_support_firewall()

    print("SW1-A3 FREE GRAM ALGEBRAIC CERTIFICATE: PASS")
    print(f"sympy={sp.__version__}")
    for r in results:
        print(
            "case n={n}, m={m}, p={p}: rank(J)={rank_J}, rank(Gfr)={rank_Gfr}".format(**r)
        )
    print(
        "support firewall: physical_rows={physical_rows}, zdim={zdim}, hdim={hdim}, "
        "identity z/h cross-block=0".format(**support)
    )
    print("certified: Gram factorization, compressed-inverse identity skeleton,")
    print("           exact variational equations, support-disjoint identity block")
    print("scope firewall: finite algebraic/mechanical identities only;")
    print("                infinite-dimensional Hilbert-space steps require audit")


if __name__ == "__main__":
    main()
