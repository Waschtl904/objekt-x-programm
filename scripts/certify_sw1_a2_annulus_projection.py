#!/usr/bin/env python3
"""
SW1-A2 algebraic/mechanical certificate.

Scope:
- exact finite-dimensional matrix realizations of the operator identities used in
  A2 (compression, oblique projection, kernel/range, reconstruction, and
  Cross-Gram reconciliation);
- exact rational arithmetic via SymPy.

Firewall:
This certificate does NOT by itself prove the infinite-dimensional Hilbert-space
claims (closedness, bounded inverse theorem, functional calculus, adjoint/range
closure identities). Those require the separate functional-analytic audit.
"""

import sympy as sp


def same_subspace(cols_a, cols_b, nrows):
    A = sp.Matrix.hstack(*cols_a) if cols_a else sp.zeros(nrows, 0)
    B = sp.Matrix.hstack(*cols_b) if cols_b else sp.zeros(nrows, 0)
    return A.rank() == B.rank() == sp.Matrix.hstack(A, B).rank()


def certify_case(n, k):
    assert 1 <= k < n

    # Symmetric strictly diagonally dominant positive-definite rational square root.
    S = sp.zeros(n)
    for i in range(n):
        S[i, i] = sp.Rational(4 + i, 1)
        if i + 1 < n:
            S[i, i + 1] = sp.Rational(1, 2)
            S[i + 1, i] = sp.Rational(1, 2)

    # Sylvester criterion, then T = S^2 with T^(1/2)=S.
    for j in range(1, n + 1):
        assert sp.factor(S[:j, :j].det()) > 0
    T = sp.simplify(S * S)

    Ek = sp.eye(n)[:, :k]
    Eperp = sp.eye(n)[:, k:]
    P = Ek * Ek.T

    G = sp.simplify(Ek.T * T * Ek)
    assert G == G.T
    assert G.det() != 0

    Ginv_ext = sp.simplify(Ek * G.inv() * Ek.T)
    Q = sp.simplify(sp.eye(n) - T * Ginv_ext)

    # A2.9-A2.16: range K^perp, idempotence, kernel T K.
    assert sp.simplify(P * Q) == sp.zeros(n)
    assert sp.simplify(Q * Eperp - Eperp) == sp.zeros(n, n - k)
    assert sp.simplify(Q * Q - Q) == sp.zeros(n)
    TK = sp.simplify(T * Ek)
    assert sp.simplify(Q * TK) == sp.zeros(n, k)
    assert Q.rank() == n - k
    assert TK.rank() == k
    assert sp.Matrix.hstack(TK, Eperp).rank() == n

    # Exact block form Q = [[0,0],[-C G^-1,I]].
    C = sp.simplify(Eperp.T * T * Ek)
    Qblock = sp.zeros(n)
    Qblock[k:, :k] = sp.simplify(-C * G.inv())
    Qblock[k:, k:] = sp.eye(n - k)
    assert sp.simplify(Q - Qblock) == sp.zeros(n)

    # A2.29g: square-root / Cross-Gram reconciliation.
    J = sp.simplify(S * Ek)
    PJperp = sp.simplify(
        sp.eye(n) - J * (J.T * J).inv() * J.T
    )
    Qhat = sp.simplify(S * PJperp * S.inv())
    assert sp.simplify(Qhat - Q) == sp.zeros(n)

    # Build F with ker(F)=K, so Ran(F^*)=K^perp in this exact model.
    F = Eperp.T
    MI = sp.simplify(S.inv() * F.T)

    # Annulus test map Z with a guaranteed nontrivial kernel direction:
    # k columns lie in T K, plus two generic columns.
    generic1 = sp.Matrix([sp.Rational(i + 1, i + 2) for i in range(n)])
    generic2 = sp.Matrix([sp.Rational((-1) ** i * (i + 2), i + 3) for i in range(n)])
    Z = sp.Matrix.hstack(TK, generic1, generic2)

    L = sp.simplify(Q * Z)
    MA = sp.simplify(-S.inv() * Z)

    # A2.29h-A2.29j.
    assert sp.simplify(L + S * PJperp * MA) == sp.zeros(n, Z.cols)
    CG = sp.simplify(MI.T * MA)
    assert same_subspace(L.nullspace(), CG.nullspace(), Z.cols)

    # A2.20-A2.26: every L-kernel vector reconstructs an augmented kernel pair.
    for w in L.nullspace():
        z = sp.simplify(Z * w)
        yk = sp.simplify(-G.inv() * Ek.T * z)
        y = sp.simplify(Ek * yk)
        assert sp.simplify(T * y + z) == sp.zeros(n, 1)
        assert sp.simplify(F * y) == sp.zeros(n - k, 1)

    # Conversely, the deliberately inserted T K source columns are killed by L.
    for j in range(k):
        ej = sp.eye(Z.cols)[:, j]
        assert sp.simplify(L * ej) == sp.zeros(n, 1)

    return {
        "n": n,
        "k": k,
        "rank_Q": Q.rank(),
        "dim_kernel_L": len(L.nullspace()),
    }


def main():
    cases = [(3, 1), (4, 2), (5, 2), (6, 3)]
    results = [certify_case(n, k) for n, k in cases]

    print("SW1-A2 ANNULUS PROJECTION ALGEBRAIC CERTIFICATE: PASS")
    print(f"sympy={sp.__version__}")
    for r in results:
        print(
            "case n={n}, k={k}: rank(Q)={rank_Q}, dim ker(L)={dim_kernel_L}".format(**r)
        )
    print("certified: oblique projection algebra, block form, reconstruction,")
    print("           square-root/Cross-Gram reconciliation in exact rational models")
    print("scope firewall: finite algebraic/mechanical identities only;")
    print("                infinite-dimensional Hilbert-space steps require audit")


if __name__ == "__main__":
    main()
