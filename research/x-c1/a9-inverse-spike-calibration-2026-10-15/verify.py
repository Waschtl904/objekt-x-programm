#!/usr/bin/env python3
"""Exakte Kontrollen zum Paket a9-inverse-spike-calibration-2026-10-15.

Nur Standardbibliothek und exakte Bruchrechnung. Eingaben sind die im
Repository gebundenen Originaldateien INVERSE_EVEN.json / INVERSE_ODD.json
aus dem A9-Inversarchiv (SHA-256 gebunden) und die rationalen Zeugen in
WITNESSES.json. Zertifiziert werden:

  (Z1) P_upper <= mu * v v^T + eps * I            (exakte LDL, 84 positive Pivots)
  (Z2) v^T P v / |v|^2 >= mu_lower                 (mu ist nicht wesentlich senkbar)
  (Z3) w ⊥ v exakt und w^T P w / |w|^2 >= eps_lower (eps ist nicht wesentlich senkbar)
  (Z4) u^T E u / |u|^2 <= E_min_cap                (gerichtete Budgetluecke fast null)
  (Z5) abgeleitete skalare Konstanten aus (2.4), (1.1), R_L <= 5/21, beta des A9-Pakets

Alle Aussagen betreffen endliche rationale Matrizen des Archivs. Sie beweisen
keine neue A9-Eigenschaft und keine A11-Aussage.
"""

from __future__ import annotations

import hashlib
import io
import json
import sys
import time
import zipfile
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PROOF = HERE / "PROOF.md"
WITNESSES = HERE / "WITNESSES.json"
ARCHIVE = ROOT / "research/x-c1/a9-inverse-renewal-2026-10-13/archives/Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13.zip"
ARCHIVE_SHA = "a1fa41958d79ab16a7c42b12375c3373f5a86a99993ae2d23c984ff6b3b2e8ae"
MEMBER = "Objekt-X-A9-Inverserneuerung-und-Hoher-Schurrest-2026-10-13/INVERSE_{}.json"

# Konstanten des A9-Pakets (HERLEITUNG.txt (1.1), (2.4), (3.3)); hier nur uebernommen.
ELEVEN_TENTHS = F(11, 10)
R_L_BOUND = F(5, 21)
J_NORM_SQ = F(1000502, 1000000)


def inertia(a):
    """Exakte Traegheit (neg, null, pos) einer symmetrischen rationalen Matrix via Kongruenz."""
    n = len(a)
    m = [row[:] for row in a]
    neg = pos = 0
    for k in range(n):
        if m[k][k] == 0:
            j = next((j for j in range(k + 1, n) if m[k][j] != 0), None)
            if j is None:
                continue
            for sgn in (F(1), F(-1)):
                if m[k][k] + 2 * sgn * m[k][j] + m[j][j] != 0:
                    break
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
                for c in range(k, n):
                    m[r][c] -= f * m[k][c]
        for c in range(k + 1, n):
            m[k][c] = F(0)
        for r in range(k + 1, n):
            m[r][k] = F(0)
    return neg, n - neg - pos, pos


def quad(a, v):
    n = len(v)
    return sum(v[i] * sum(a[i][j] * v[j] for j in range(n)) for i in range(n))


def load_archive():
    data = ARCHIVE.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    if sha != ARCHIVE_SHA:
        raise SystemExit("Archiv-SHA weicht ab: " + sha)
    z = zipfile.ZipFile(io.BytesIO(data))
    return {p: json.loads(z.read(MEMBER.format(p.upper()))) for p in ("even", "odd")}


def check_parity(par, d, wit):
    P = [[F(x) for x in r] for r in d["P_upper_rational"]]
    E = [[F(x) for x in r] for r in d["E_rational"]]
    n, m = len(P), len(E)
    assert n == 84 and m == 203
    assert all(P[i][j] == P[j][i] for i in range(n) for j in range(n)), "P nicht symmetrisch"
    assert all(E[i][j] == E[j][i] for i in range(m) for j in range(m)), "E nicht symmetrisch"
    assert sum(P[i][i] for i in range(n)) == F(d["candidate_P_upper_trace"]), "Spur weicht ab"
    beta = F(d["beta"])
    mu, eps = F(wit["mu"]), F(wit["eps"])
    v = [F(x) for x in wit["v_hat"]]
    w = [F(x) for x in wit["w_orth"]]
    u = [F(x) for x in wit["u_E_min"]]
    u2 = [F(x) for x in wit["u_E_second"]]
    out = {"beta": str(beta), "mu": str(mu), "eps": str(eps)}

    # (Z1) mu v v^T + eps I - P >= 0, exakt
    t = time.time()
    D = [[mu * v[i] * v[j] + (eps if i == j else F(0)) - P[i][j] for j in range(n)] for i in range(n)]
    ine = inertia(D)
    assert ine == (0, 0, 84), ine
    out["Z1_inertia_mu_vv_plus_eps_minus_P"] = ine
    out["Z1_seconds"] = round(time.time() - t, 1)

    # (Z2) Rayleigh von v
    rv = quad(P, v) / sum(x * x for x in v)
    assert rv >= F(wit["mu_lower_witness"]), float(rv)
    out["Z2_rayleigh_v"] = float(rv)

    # (Z3) w exakt orthogonal zu v und Rayleigh >= eps_lower
    assert sum(a * b for a, b in zip(w, v)) == 0
    rw = quad(P, w) / sum(x * x for x in w)
    assert rw >= F(wit["eps_lower_witness"]), float(rw)
    out["Z3_rayleigh_w_orthogonal"] = float(rw)

    # (Z4) Budgetluecke E in Richtung u fast null (obere Schranke fuer lambda_min(E))
    ru = quad(E, u) / sum(x * x for x in u)
    assert 0 < ru <= F(wit["E_min_rayleigh_cap"]), float(ru)
    ru2 = quad(E, u2) / sum(x * x for x in u2)
    assert 0 < ru2 <= F(wit["E_second_rayleigh_cap"]), float(ru2)
    out["Z4_lambda_min_E_upper_bound"] = "%.3e" % float(ru)
    out["Z4_second_direction_upper_bound"] = "%.3e" % float(ru2)
    out["Z4_E_max_diagonal"] = float(max(E[i][i] for i in range(m)))

    # (Z5) abgeleitete skalare Konstanten; Herleitung in PROOF.md Abschnitt 4
    global_const = ELEVEN_TENTHS * (R_L_BOUND / beta + J_NORM_SQ * sum(P[i][i] for i in range(n)))
    offspike_const = ELEVEN_TENTHS * (R_L_BOUND / beta + J_NORM_SQ * eps)
    spike_weight = ELEVEN_TENTHS * mu
    out["Z5_global_constant_source_3_3"] = float(global_const)
    out["Z5_offspike_constant"] = float(offspike_const)
    out["Z5_spike_weight_on_Jv"] = float(spike_weight)
    out["Z5_ratio_global_over_offspike"] = float(global_const / offspike_const)
    cap = 65000 if par == "even" else 11000
    assert global_const < cap, float(global_const)
    assert offspike_const < (F(47, 10) if par == "even" else F(28, 10))
    return out


def main() -> int:
    arch = load_archive()
    wit = json.loads(WITNESSES.read_text(encoding="utf-8"))
    assert wit["source_archive_sha256"] == ARCHIVE_SHA
    report = {
        "package": "a9-inverse-spike-calibration-2026-10-15",
        "proof_sha256": hashlib.sha256(PROOF.read_bytes()).hexdigest(),
        "archive_sha256": ARCHIVE_SHA,
        "scope": "exact rational certificates on the stored 84x84 P_upper and 203x203 E per parity; no new A9 claim, no A11 data",
    }
    for par in ("even", "odd"):
        report[par] = check_parity(par, arch[par], wit["parities"][par])
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
