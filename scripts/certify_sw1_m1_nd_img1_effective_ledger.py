#!/usr/bin/env python3
"""SW1 M1-ND IMG1 exact effective 3x6 function-channel ledger certificate.

This certificate is intentionally downstream of the canonical M1-FULL B96
certificate. Importing that module first reruns and revalidates the exact
12x24 seven-shift physical-vs-ledger identity at r0=7/2.

IMG1 then performs the valid-image reduction:
  - restrict output species to P0 (three horizon output lifts);
  - replace each valid input species slot by its IMG0 base-lift pullback;
  - collapse 12_H+12_W ambient slots to 3_H+3_W function channels;
  - retain the exact effective affine pullback type, coefficient, lift,
    source family, gate/row, input species, and original M1 shift as provenance;
  - compare the reduced ledger with a direct physical P0 assembly on every
    one of the 64*96 open B96 atoms.

Scope firewall:
  * exact finite/algebraic reference-r assembly only;
  * f is still required analytically to lie in B_K and g in B_W;
  * no kernel-triviality, recurrence, transfer-invertibility, or RH claim.
"""

from fractions import Fraction as F
from collections import Counter, defaultdict
import hashlib

import certify_sw1_a10_c2_m1_full_b96 as m1

print("SW1 M1-ND IMG1 EFFECTIVE 3x6 LEDGER CERTIFICATE")

assert m1.r0 == F(7, 2)
assert m1.gdict["P0"] == ("P0", +1, 0, 0)

# Effective pullback alpha=(s,lambda,d) means
#   theta |-> s*theta + lambda*L + d*Delta (mod L).
EXPECTED_TYPES = {
    (+1, F(0), -2),
    (+1, F(0), -1),
    (+1, F(0), 0),
    (+1, F(0), 1),
    (+1, F(0), 2),
    (-1, F(0), 1),
    (-1, F(0), 2),
    (-1, F(0), 3),
    (-1, F(0), 4),
    (-1, F(1, 2), 2),
    (+1, F(1, 2), -2),
    (+1, F(1, 2), 2),
}


def effective_map(gname, j):
    _, s, eta, kappa = m1.gdict[gname]
    return (s, F(eta, 2), s * j + kappa)


# Re-derive the P0 effective alphabet directly from the M1 species/shift rules.
free_types = set()
for br in m1.FREE:
    gin, j, _, _ = m1.free_sr[(br[0], "P0")]
    free_types.add(effective_map(gin, j))

hub_types = set()
half_hub_names = set()
for ch in m1.HUB:
    gin, j, _, _ = m1.hub_sr[(ch[0], "P0")]
    a = effective_map(gin, j)
    hub_types.add(a)
    if a[1] == F(1, 2):
        half_hub_names.add(ch[0])

assert len(free_types) == 9
assert len(hub_types) == 9
assert free_types | hub_types == EXPECTED_TYPES
assert all(a[1] == 0 for a in free_types)
assert half_hub_names == {"B_L", "B_R", "B_O"}


def reduced_term(lout, block, lin, amap, coeff, gate, source, gin, j):
    assert block in {"H", "W"}
    assert 0 <= lout < 3
    assert 0 <= lin < 3
    col = lin if block == "H" else 3 + lin
    assert 0 <= col < 6
    assert amap in EXPECTED_TYPES
    return (lout, col, block, lin, amap, coeff, gate, source, gin, j)


def aggregate_signature(terms):
    """Exact unsimplified coefficient/provenance aggregation by 3x6 cell+map."""
    groups = defaultdict(list)
    for t in terms:
        lout, col, block, lin, amap, coeff, gate, source, gin, j = t
        key = (lout, col, amap)
        groups[key].append((coeff, block, lin, gate, source, gin, j))
    return tuple(
        (key, tuple(sorted(vals, key=str)))
        for key, vals in sorted(groups.items(), key=lambda kv: str(kv[0]))
    )


atom_count = 0
total_reduced_terms = 0
nonzero_pullback_hist = Counter()
nonzero_channel_hist = Counter()
aggregation_mult_hist = Counter()
map_term_hist = Counter()
max_aggregation = 0
all_active_types = set()
state_hasher = hashlib.sha256()
unique_state_digests = set()

for ci, rep in enumerate(m1.reps):
    sigma, R, eps = rep
    assert eps < m1.Emax < m1.D / 2

    vals = [m1.bvalue(sig, rep) for sig in m1.B96]
    assert len(set(vals)) == 96
    vals = sorted(vals)
    thetas = [(vals[i] + vals[i + 1]) / 2 for i in range(95)]
    thetas.append(((vals[-1] + vals[0] + m1.L) / 2) % m1.L)
    assert len(thetas) == 96

    for ai, theta in enumerate(thetas):
        atom_count += 1
        physical = []
        ledger = []

        # R_P0^out: only the three P0 horizon output lifts survive.
        for lout in range(3):
            xout = theta + lout * m1.L
            T0 = m1.T + eps
            if not (0 < xout < T0):
                continue

            rows = m1.active_rows(xout, eps)
            assert len(rows) == 1
            row = rows[0]

            # -------------------------
            # Direct physical FREE row.
            # -------------------------
            for affine, coeff in m1.row_terms_by_name[row]:
                _, s, lam, k = m1.Fdict[affine]
                xsrc = s * xout + lam * m1.L + k * m1.D
                assert 0 < xsrc < T0

                gin, j, _, s2 = m1.free_sr[(affine, "P0")]
                assert s2 == s
                rin = m1.rho(gin, theta + j * m1.D)
                q = (xsrc - rin) / m1.L
                assert q.denominator == 1
                lin = int(q)
                assert 0 <= lin < 3

                physical.append(
                    reduced_term(
                        lout, "H", lin, effective_map(gin, j),
                        coeff, row, affine, gin, j
                    )
                )

            # ------------------------
            # Direct physical HUB row.
            # ------------------------
            for name, s, lam, k, coeff in m1.HUB:
                if not m1.hub_active(name, xout, sigma, R, eps):
                    continue

                t = s * xout - s * lam * m1.L - s * k * m1.D
                assert R < t < m1.T + sigma

                gin, j, _, s2 = m1.hub_sr[(name, "P0")]
                assert s2 == s
                rin = m1.rho(gin, theta + j * m1.D)
                q = (t - rin) / m1.L
                assert q.denominator == 1
                lin = int(q)
                assert 0 <= lin < 3

                physical.append(
                    reduced_term(
                        lout, "W", lin, effective_map(gin, j),
                        coeff, name, name, gin, j
                    )
                )

            # -------------------------------------------------------------
            # M1-ledger FREE row, then exact IMG0 species/lift elimination.
            # -------------------------------------------------------------
            for affine, coeff in m1.row_terms_by_name[row]:
                gin, j, m, s = m1.free_sr[(affine, "P0")]
                lin = (
                    s * (lout - m1.Nwrap("P0", theta))
                    + m1.Nwrap(gin, theta + j * m1.D)
                    - m
                )
                if 0 <= lin < 3:
                    xsrc = (
                        s * xout
                        + m1.Fdict[affine][2] * m1.L
                        + m1.Fdict[affine][3] * m1.D
                    )
                    assert xsrc == m1.rho(gin, theta + j * m1.D) + lin * m1.L

                    ledger.append(
                        reduced_term(
                            lout, "H", lin, effective_map(gin, j),
                            coeff, row, affine, gin, j
                        )
                    )

            # ------------------------------------------------------------
            # M1-ledger HUB row, then exact IMG0 species/lift elimination.
            # ------------------------------------------------------------
            for name, s, lam, k, coeff in m1.HUB:
                if not m1.hub_active(name, xout, sigma, R, eps):
                    continue

                gin, j, m, s2 = m1.hub_sr[(name, "P0")]
                assert s2 == s
                lin = (
                    s * (lout - m1.Nwrap("P0", theta))
                    + m1.Nwrap(gin, theta + j * m1.D)
                    - m
                )
                if 0 <= lin < 3:
                    t = s * xout - s * lam * m1.L - s * k * m1.D
                    assert t == m1.rho(gin, theta + j * m1.D) + lin * m1.L

                    ledger.append(
                        reduced_term(
                            lout, "W", lin, effective_map(gin, j),
                            coeff, name, name, gin, j
                        )
                    )

        physical = sorted(physical, key=str)
        ledger = sorted(ledger, key=str)

        # Strong reduced equality: same coefficients and complete provenance,
        # not merely the same numerical/symbolic sum.
        assert physical == ledger

        physical_sig = aggregate_signature(physical)
        ledger_sig = aggregate_signature(ledger)
        assert physical_sig == ledger_sig

        groups = {key: vals for key, vals in ledger_sig}
        assert all(0 <= key[0] < 3 for key in groups)
        assert all(0 <= key[1] < 6 for key in groups)

        active_types = {key[2] for key in groups}
        assert active_types <= EXPECTED_TYPES
        all_active_types |= active_types

        nonzero_pullback_hist[len(groups)] += 1
        nonzero_channel_hist[len({(key[0], key[1]) for key in groups})] += 1

        for key, vals in groups.items():
            mult = len(vals)
            aggregation_mult_hist[mult] += 1
            max_aggregation = max(max_aggregation, mult)
            map_term_hist[key[2]] += mult

        total_reduced_terms += len(ledger)
        payload = (
            str(ci) + "|" + str(ai) + "|" + str(theta) + "|"
            + repr(ledger_sig)
        ).encode()
        state_hasher.update(payload + b"\n")
        unique_state_digests.add(hashlib.sha256(repr(ledger_sig).encode()).hexdigest())

assert atom_count == 64 * 96 == 6144
assert all_active_types == EXPECTED_TYPES

EXPECTED_TOTAL_REDUCED_TERMS = 117546
EXPECTED_PULLBACK_HIST = Counter({
    14: 314,
    15: 2615,
    16: 276,
    23: 1690,
    24: 669,
    25: 497,
    26: 83,
})
EXPECTED_CHANNEL_HIST = Counter({
    8: 1754,
    9: 1213,
    10: 238,
    14: 1344,
    15: 251,
    16: 1260,
    17: 84,
})
EXPECTED_AGGREGATION_HIST = Counter({1: 117546})
EXPECTED_MAP_TERM_HIST = Counter({
    (-1, F(0), 1): 7884,
    (-1, F(0), 2): 29796,
    (-1, F(0), 3): 7990,
    (-1, F(0), 4): 7140,
    (-1, F(1, 2), 2): 11684,
    (+1, F(0), -2): 344,
    (+1, F(0), -1): 15284,
    (+1, F(0), 0): 15227,
    (+1, F(0), 1): 15367,
    (+1, F(0), 2): 386,
    (+1, F(1, 2), -2): 3229,
    (+1, F(1, 2), 2): 3215,
})
EXPECTED_DISTINCT_STATES = 22
EXPECTED_STATE_DIGEST = "1cffd33529534a15c941b67086217f8f8c47b0cc302cb2cf740b0e08c2ff4474"

assert total_reduced_terms == EXPECTED_TOTAL_REDUCED_TERMS
assert nonzero_pullback_hist == EXPECTED_PULLBACK_HIST
assert nonzero_channel_hist == EXPECTED_CHANNEL_HIST
assert aggregation_mult_hist == EXPECTED_AGGREGATION_HIST
assert max_aggregation == 1
assert map_term_hist == EXPECTED_MAP_TERM_HIST
assert len(unique_state_digests) == EXPECTED_DISTINCT_STATES

state_digest = state_hasher.hexdigest()
assert state_digest == EXPECTED_STATE_DIGEST

print("reference ratio r0=7/2; exact open atoms checked: 64*96=6144")
print("P0 reduced physical assembly == reduced M1 ledger on every atom: PASS")
print("output channels: 3; input function channels: 3_H + 3_W = 6")
print("effective affine alphabet used:", len(all_active_types))
print("total reduced active terms:", total_reduced_terms)
print("nonzero (output,input,map) histogram:", sorted(nonzero_pullback_hist.items()))
print("nonzero 3x6 channel histogram:", sorted(nonzero_channel_hist.items()))
print("aggregation multiplicity histogram:", sorted(aggregation_mult_hist.items()))
print("maximum contributions aggregated into one (output,input,map) cell:", max_aggregation)
print("distinct reduced operator states:", len(unique_state_digests))
print("reduced state ledger SHA256:", state_digest)
print("effective map term histogram:", sorted((str(k), v) for k, v in map_term_hist.items()))
print("FIREWALL: domain remains B_K direct-sum B_W; no ambient species freedoms reintroduced")
print("FIREWALL: no injectivity/recurrence/actual-r/RH claim")
print("SW1 M1-ND IMG1 EFFECTIVE 3x6 LEDGER CERTIFICATE: PASS")
