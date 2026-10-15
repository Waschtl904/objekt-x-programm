#!/usr/bin/env python3
"""Exakte rationale Kontrollen zum Paket renewal-reduction-and-obstructions-2026-10-15.

Geprueft werden nur endliche Modelle: Monotonie der eingeschraenkten Inversen
(Lemma 2), Form der fortgesetzten Majorante (Folgerung 2b), Gap-Monotonie
(Lemma 3), Traegheit bei endlichrangiger Stoerung (Lemma 5) und die
Propagation der Zertifikatsinvarianten in einer Spielzeugkette (Satz 4).
Keine Kontrolle beruehrt Prim-/Gamma-Daten oder unendliche Domaenen.
"""

from __future__ import annotations

import hashlib
import json
import sys
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROOF = HERE / "PROOF.md"

Matrix = list[list[F]]


# ----------------------------------------------------------------- Algebra

def mat(rows) -> Matrix:
    return [[F(x) for x in r] for r in rows]


def eye(n: int) -> Matrix:
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n: int, m: int) -> Matrix:
    return [[F(0)] * m for _ in range(n)]


def T(a: Matrix) -> Matrix:
    return [list(r) for r in zip(*a)]


def add(a: Matrix, b: Matrix) -> Matrix:
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[x - y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(c, a: Matrix) -> Matrix:
    return [[F(c) * x for x in r] for r in a]


def mul(a: Matrix, b: Matrix) -> Matrix:
    bt = T(b)
    return [[sum(x * y for x, y in zip(r, c)) for c in bt] for r in a]


def block(a: Matrix, b: Matrix, c: Matrix, d: Matrix) -> Matrix:
    return [ra + rb for ra, rb in zip(a, b)] + [rc + rd for rc, rd in zip(c, d)]


def inv(a: Matrix) -> Matrix:
    n = len(a)
    m = [row[:] + eye(n)[i] for i, row in enumerate(a)]
    for col in range(n):
        piv = next((r for r in range(col, n) if m[r][col] != 0), None)
        if piv is None:
            raise ZeroDivisionError("singular matrix")
        m[col], m[piv] = m[piv], m[col]
        p = m[col][col]
        m[col] = [x / p for x in m[col]]
        for r in range(n):
            if r != col and m[r][col] != 0:
                f = m[r][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[col])]
    return [row[n:] for row in m]


def is_symmetric(a: Matrix) -> bool:
    return all(a[i][j] == a[j][i] for i in range(len(a)) for j in range(len(a)))


def inertia(a: Matrix) -> tuple[int, int, int]:
    """Exakte Traegheit (neg, null, pos) einer symmetrischen rationalen Matrix.

    Symmetrische Gaussalgorithmus-Kongruenz; verschwindet ein Diagonalpivot,
    wird zuerst die Kongruenz x_k -> x_k +/- x_j angewandt, die den Pivot
    nicht-null macht. Kongruenzen erhalten die Traegheit (Sylvester).
    """
    assert is_symmetric(a)
    n = len(a)
    m = [row[:] for row in a]
    neg = pos = 0
    for k in range(n):
        if m[k][k] == 0:
            j = next((j for j in range(k + 1, n) if m[k][j] != 0), None)
            if j is None:
                continue  # Zeile/Spalte k ist bereits null
            for sgn in (F(1), F(-1)):
                cand = m[k][k] + 2 * sgn * m[k][j] + m[j][j]
                if cand != 0:
                    break
            # x_k -> x_k + sgn x_j : Zeile k += sgn*Zeile j, Spalte k += sgn*Spalte j
            for c in range(n):
                m[k][c] += sgn * m[j][c]
            for r in range(n):
                m[r][k] += sgn * m[r][j]
        p = m[k][k]
        if p == 0:
            continue
        if p > 0:
            pos += 1
        else:
            neg += 1
        for r in range(k + 1, n):
            if m[r][k] != 0:
                f = m[r][k] / p
                for c in range(n):
                    m[r][c] -= f * m[k][c]
        for c in range(k + 1, n):
            m[k][c] = F(0)
        for r in range(k + 1, n):
            m[r][k] = F(0)
    return neg, n - neg - pos, pos


def is_psd(a: Matrix) -> bool:
    return inertia(a)[0] == 0


def is_pd(a: Matrix) -> bool:
    neg, nul, _ = inertia(a)
    return neg == 0 and nul == 0


def compress(a: Matrix, idx: list[int]) -> Matrix:
    return [[a[i][j] for j in idx] for i in idx]


def quad(a: Matrix, v: list[F]) -> F:
    return sum(v[i] * a[i][j] * v[j] for i in range(len(v)) for j in range(len(v)))


# ----------------------------------------------------------------- Kontrollen

def check_lemma2() -> dict:
    """(Q^-1)_11 >= A^-1 fuer positive Blockmodelle; Gleichheit nur bei C=0."""
    cases = {
        "2+1": mat([[2, 1, F(1, 2)], [1, 3, 1], [F(1, 2), 1, 2]]),
        "2+2": mat([[4, 1, 1, 0], [1, 3, 0, 1], [1, 0, 2, F(1, 3)], [0, 1, F(1, 3), 5]]),
        "3+2": mat([
            [5, 1, 0, 1, F(1, 2)],
            [1, 4, 1, 0, 1],
            [0, 1, 3, 1, 0],
            [1, 0, 1, 2, F(1, 4)],
            [F(1, 2), 1, 0, F(1, 4), 3],
        ]),
        "C=0": mat([[2, 1, 0], [1, 3, 0], [0, 0, 5]]),
    }
    out = {}
    for name, q in cases.items():
        assert is_pd(q), name
        n0 = len(q) - (1 if name in ("2+1", "C=0") else 2)
        old = list(range(n0))
        a = compress(q, old)
        diff = sub(compress(inv(q), old), inv(a))
        psd = is_psd(diff)
        zero = all(x == 0 for r in diff for x in r)
        c_zero = all(q[i][j] == 0 for i in old for j in range(n0, len(q)))
        assert psd, name
        assert zero == c_zero, name
        out[name] = {"psd": psd, "equality": zero, "C_zero": c_zero}

    # dreistufige genestete Kette Q1 < Q2 < Q3 (Kompression)
    q3 = cases["3+2"]
    q2 = compress(q3, [0, 1, 2, 3])
    q1 = compress(q3, [0, 1, 2])
    i1, i2, i3 = inv(q1), inv(q2), inv(q3)
    chain_ok = is_psd(sub(compress(i2, [0, 1, 2]), i1)) and is_psd(sub(compress(i3, [0, 1, 2, 3]), i2))
    chain_ok = chain_ok and is_psd(sub(compress(i3, [0, 1, 2]), i1))
    assert chain_ok
    out["nested_chain_3_steps"] = chain_ok

    # Gegenkontrolle: indefinites Q, Monotonie gilt nicht
    q_ind = mat([[1, 2], [2, 1]])
    assert inertia(q_ind)[0] == 1
    diff = sub(compress(inv(q_ind), [0]), inv(compress(q_ind, [0])))
    out["indefinite_counter_control_fails_as_expected"] = not is_psd(diff)
    assert not is_psd(diff)
    return out


def check_unew() -> dict:
    """Unew - U(+)0 = [-H;I] V [-H;I]^T >= 0; Kompression auf neuen Raum = V."""
    out = {}
    for name, (u, h, v) in {
        "a": (mat([[2, F(1, 2)], [F(1, 2), 1]]), mat([[1], [-2]]), mat([[F(3, 2)]])),
        "b": (mat([[3, 1, 0], [1, 2, 1], [0, 1, 4]]), mat([[1, 0], [F(1, 2), -1], [0, 2]]), mat([[2, F(1, 3)], [F(1, 3), 1]])),
    }.items():
        assert is_pd(u) and is_pd(v)
        n0, n1 = len(u), len(v)
        hv = mul(h, v)
        unew = block(add(u, mul(hv, T(h))), scale(-1, hv), scale(-1, mul(v, T(h))), v)
        u0 = block(u, zeros(n0, n1), zeros(n1, n0), zeros(n1, n1))
        diff = sub(unew, u0)
        m = [[-x for x in r] for r in h] + eye(n1)  # [-H; I]
        congr = mul(mul(m, v), T(m))
        assert diff == congr
        assert is_psd(diff)
        assert compress(unew, list(range(n0, n0 + n1))) == v
        out[name] = {"difference_is_congruence_of_V": True, "psd": True, "compression_is_V": True}
    return out


def check_lemma3() -> dict:
    """Zeugentransfer: Rayleighquotient eines Zeugen in T_a schraenkt lambda*(T_b), T_a in T_b, nach oben ein."""
    w = mat([[3, 1, 0], [1, 2, 1], [0, 1, 4]])
    # T_a = span(e1), T_b = span(e1, e2): lambda*(T_a) = w11 = 3 exakt.
    lam_a = w[0][0]
    # Zeuge in T_b mit kleinerem Rayleighquotienten
    z = [F(1), F(-1), F(0)]
    rq_b = quad(w, z) / sum(x * x for x in z)  # (3 - 2 + 2)/2 = 3/2
    assert rq_b < lam_a
    # der alte Zeuge liegt weiterhin in T_b, also lambda*(T_b) <= lambda*(T_a) trivial
    # Gegenkontrolle: nicht genestete 1-dim Klassen span(e1) vs span(e3): 3 < 4
    lam_other = w[2][2]
    return {
        "lambda_star_T_a": str(lam_a),
        "witness_quotient_in_T_b": str(rq_b),
        "monotone_in_nested_pair": rq_b <= lam_a,
        "non_nested_counter_control_increases": lam_other > lam_a,
    }


def check_lemma5() -> dict:
    """Pi >= 0 plus Rang-2m-Stoerung mit Traegheit (m,m) hat hoechstens m negative Eigenwerte."""
    pi = mat([
        [2, 1, 0, 0, 0],
        [1, 2, 1, 0, 0],
        [0, 1, 2, 1, 0],
        [0, 0, 1, 2, 1],
        [0, 0, 0, 1, 2],
    ])
    assert is_psd(pi)
    out = {}
    # (1,1)-Stoerung: s = t * (x y^T + y x^T) hat Traegheit (1,1) fuer unabhaengige x,y
    x = [F(1), F(0), F(0), F(0), F(0)]
    y = [F(0), F(0), F(0), F(0), F(1)]
    s_unit = [[x[i] * y[j] + y[i] * x[j] for j in range(5)] for i in range(5)]
    assert inertia(s_unit) == (1, 3, 1)
    for t in (F(1, 2), F(1), F(3), F(10)):
        q = add(pi, scale(t, s_unit))
        neg = inertia(q)[0]
        assert neg <= 1, (t, neg)
        out[f"rank2_t={t}"] = {"negative_eigenvalues": neg}
    assert out["rank2_t=10"]["negative_eigenvalues"] == 1  # Gleichheit fuer grosse Stoerung
    # (2,2)-Stoerung: zwei negative Eigenwerte moeglich, Schranke m=2 scharf
    x2 = [F(0), F(1), F(0), F(0), F(0)]
    y2 = [F(0), F(0), F(0), F(1), F(0)]
    s2 = [[x2[i] * y2[j] + y2[i] * x2[j] for j in range(5)] for i in range(5)]
    s22 = add(s_unit, s2)
    assert inertia(s22) == (2, 1, 2)
    q = add(pi, scale(10, s22))
    neg = inertia(q)[0]
    assert neg == 2
    out["rank4_(2,2)_t=10"] = {"negative_eigenvalues": neg, "bound_m": 2}
    return out


def toy_step(q_new: Matrix, n0: int, u_old: Matrix, p: Matrix, margin: F):
    """Ein Schritt des Inversfortsetzungslemmas auf einem endlichen Modell.

    Liefert (ok, U_new, lower) oder (False, None, None), wenn (H1) scheitert.
    """
    n = len(q_new)
    old, new = list(range(n0)), list(range(n0, n))
    a = compress(q_new, old)
    c = [[q_new[i][j] for j in new] for i in old]
    d = compress(q_new, new)
    r = sub(c, mul(a, p))
    k = add(sub(sub(d, mul(T(c), p)), mul(T(p), c)), mul(mul(T(p), a), p))
    b = sub(sub(k, mul(mul(T(r), u_old), r)), scale(margin, eye(len(new))))
    if not is_pd(b):
        return False, None, None
    v = inv(b)
    h = add(p, mul(u_old, r))
    hv = mul(h, v)
    u_new = block(add(u_old, mul(hv, T(h))), scale(-1, hv), scale(-1, mul(v, T(h))), v)
    # lower = [I 0; -H^T I]^T-Kongruenz von U^-1 (+) B ; hier direkt: lower = inverse von U_new
    lower = inv(u_new)
    # Lemma-Konklusionen exakt pruefen
    assert is_psd(sub(u_new, inv(q_new))), "Q^-1 <= U_new verletzt"
    assert is_psd(sub(q_new, lower)), "q >= lower verletzt"
    return True, u_new, lower


def check_theorem4() -> dict:
    """Spielzeugkette: Invarianten (I1),(I2) propagieren bei gueltigem H_n und versagen in degenerierter Kette."""
    c_const, C_const = F(1, 2), F(3)
    # Kette A: gut konditionierte Erweiterungen
    q1 = mat([[2, F(1, 2)], [F(1, 2), 2]])
    q2 = mat([[2, F(1, 2), F(1, 4)], [F(1, 2), 2, 0], [F(1, 4), 0, 2]])
    q3 = mat([
        [2, F(1, 2), F(1, 4), 0],
        [F(1, 2), 2, 0, F(1, 4)],
        [F(1, 4), 0, 2, F(1, 2)],
        [0, F(1, 4), F(1, 2), 2],
    ])
    assert compress(q2, [0, 1]) == q1 and compress(q3, [0, 1, 2]) == q2  # Rueckzugsvertraeglichkeit
    u = inv(q1)
    log = []
    assert is_psd(sub(q1, scale(c_const, eye(2)))) and is_psd(sub(scale(C_const, eye(2)), u))
    for step, (q_new, n0) in enumerate(((q2, 2), (q3, 3)), start=1):
        # Antwortregel vor der Positivitaetsauswertung festgelegt: P = A^-1 C (Residuum 0)
        a = compress(q_new, list(range(n0)))
        c = [[q_new[i][j] for j in range(n0, len(q_new))] for i in range(n0)]
        p = mul(inv(a), c)
        ok, u_new, lower = toy_step(q_new, n0, u, p, F(1, 100))
        assert ok
        i1 = is_psd(sub(lower, scale(c_const, eye(len(q_new)))))
        i2 = is_psd(sub(scale(C_const, eye(len(q_new))), u_new))
        log.append({"step": step, "H1": True, "I1_same_c": i1, "I2_same_C": i2})
        assert i1 and i2
        u = u_new
    # Kette B: Reserve kollabiert (neuer Diagonalblock knapp ueber Schurrest)
    qb1 = q1
    qb2 = mat([[2, F(1, 2), 1], [F(1, 2), 2, 1], [1, 1, F(9, 10)]])  # Schurrest exakt 1/10
    assert compress(qb2, [0, 1]) == qb1 and is_pd(qb2)
    a = compress(qb2, [0, 1])
    c = [[qb2[i][2]] for i in range(2)]
    p = mul(inv(a), c)
    ok, u_new, lower = toy_step(qb2, 2, inv(qb1), p, F(1, 100))
    degenerate = {"H1": ok}
    if ok:
        degenerate["I1_same_c"] = is_psd(sub(lower, scale(c_const, eye(3))))
        degenerate["I2_same_C"] = is_psd(sub(scale(C_const, eye(3)), u_new))
        assert not (degenerate["I1_same_c"] and degenerate["I2_same_C"])
    return {"chain_A": log, "chain_B_degenerate": degenerate, "c": str(c_const), "C": str(C_const)}


def main() -> int:
    report = {
        "package": "renewal-reduction-and-obstructions-2026-10-15",
        "proof_sha256": hashlib.sha256(PROOF.read_bytes()).hexdigest(),
        "lemma2_restricted_inverse_monotone": check_lemma2(),
        "corollary2b_unew_structure": check_unew(),
        "lemma3_gap_monotone": check_lemma3(),
        "lemma5_inertia": check_lemma5(),
        "theorem4_toy_chain": check_theorem4(),
        "scope": "finite exact rational models only; no prime/gamma data; no infinite domains",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
