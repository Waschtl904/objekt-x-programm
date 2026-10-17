"""Refine only the high pairing budget using the bound Low/High coordinates.

M is not an isometry. Subtraction takes place in the orthogonal Legendre
coordinates of M*U h8, not in a purported orthogonal physical Phi basis.
"""
import hashlib
import json
import os
from fractions import Fraction
from pathlib import Path
from flint import arb, ctx

ctx.prec = 800
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = Path(os.environ.get("OBJEKT_X_SHARP_K_OUTPUT", str(HERE / "expected")))

def q(value):
    value = Fraction(value)
    return arb(value.numerator) / value.denominator

def box(pair):
    return q(pair[0]).union(q(pair[1]))

def enc(value):
    return [str(value.lower().fmpq()), str(value.upper().fmpq())]

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    bindings = json.loads((HERE / "INPUT_BINDINGS.json").read_text())["repository_files"]
    for name, digest in bindings.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    def load(name):
        assert name in bindings, name
        return json.loads((ROOT / name).read_text())
    previous_root = "research/x-c1/frozen-shell-direction-certificates-2026-10-17/"
    high_path = "research/x-c1/nstar-jp-spike-orthogonality-2026-10-16/original/gpt2-stufe4-hochantwort/expected/COMPLETE_HIGH_RESPONSE.json"
    inherited_bindings = load(previous_root + "INPUT_BINDINGS.json")
    assert inherited_bindings["repository_files"][high_path] == bindings[high_path]
    high_data = load(high_path)
    own_manifest = json.loads((HERE / "MANIFEST.json").read_text())
    for parity in ("even", "odd"):
        name = f"expected/SHARP_K_{parity}.json"
        raw = (HERE / name).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == own_manifest[name], name
        sharp = json.loads(raw)
        previous_path = previous_root + f"expected/FROZEN_CERTIFICATE_{parity}.json"
        old = load(previous_path)
        assert sharp["inherited_scalar_sha256"] == bindings[previous_path]
        assert sharp["candidate_sha256"] == old["candidate_sha256"]
        assert old["parity"] == sharp["parity"] == parity
        coordinates = list(map(box, old["Phi_star_h8"]))
        assert len(coordinates) == 191
        gamma_upper = q(high_data[parity]["full_M_norm_squared"][1])
        r_upper = q(high_data[parity]["directions"]["lower_Pv"]["actual_high_difference_norm_upper"][1])
        nh8 = box(old["norm_h8"])
        assert gamma_upper > 1 and r_upper > 0 and nh8 > 0
        low_square = sum((v ** 2 for v in coordinates), arb(0))
        # ||P_Y M* U h8||² = ||M* U h8||² - ||Phi* h8||²
        #                    <= gamma ||h8||² - ||Phi* h8||².
        high_square_majorant = gamma_upper * nh8 ** 2 - low_square
        assert high_square_majorant > 0, high_square_majorant
        new_high = r_upper / q("18219/10000") * high_square_majorant.sqrt()
        old_high = box(old["high_remainder_bound_using_h8"])
        assert new_high.upper() < old_high.lower()
        retained = {key: box(old[key]) for key in (
            "psi_k_coherent_error", "finite_response_feature_error", "source_model_scalar_error")}
        assert all(v >= 0 for v in retained.values())
        radius = new_high.upper() + sum((abs(v).upper() for v in retained.values()), arb(0))
        I0 = box(old["I0"])
        L = I0 + arb(0, radius.upper())
        threshold = box(sharp["threshold"])
        if L > threshold or L < -threshold:
            outcome = "EXCLUDES_FOR_DIRECTION"
        elif abs(L).upper() <= threshold.lower():
            outcome = "DOES_NOT_EXCLUDE_FOR_DIRECTION"
        else:
            outcome = "INCONCLUSIVE_FOR_DIRECTION"
        # The new interval must also fit inside the inherited, coarser interval.
        assert box(old["L00"]).contains(L)
        result = {
            "status": "AUTHOR_DERIVED_CONDITIONAL_DIRECTED_HIGH_PROJECTION_EXTERNAL_REVIEW_OPEN",
            "parity": parity,
            "candidate_sha256": old["candidate_sha256"],
            "inherited_scalar_sha256": bindings[previous_path],
            "sharp_K_certificate_sha256": hashlib.sha256(raw).hexdigest(),
            "whole_high_response_sha256": bindings[high_path],
            "gamma_M_norm_squared_upper": enc(gamma_upper),
            "high_coordinate_r_norm_upper": enc(r_upper),
            "norm_h8": enc(nh8),
            "Phi_star_h8_norm_squared": enc(low_square),
            "T_h_h8_norm_squared_majorant": enc(high_square_majorant),
            "old_high_pairing_bound": enc(old_high),
            "new_high_pairing_bound": enc(new_high),
            "retained_error_terms": {key: enc(value) for key, value in retained.items()},
            "I0": enc(I0),
            "radius_without_I0_width": enc(radius),
            "L_interval": enc(L),
            "threshold": enc(threshold),
            "threshold_minus_sup_abs_L": enc(threshold - abs(L).upper()),
            "outcome": outcome,
            "precision_bits": ctx.prec,
            "new_pairing_integrations": False,
            "physical_Phi_orthogonality_assumed": False,
        }
        (OUT / f"PROJECTED_HIGH_{parity}.json").write_text(json.dumps(result, indent=2) + "\n")
        print(parity, "new high bound", new_high, "L", L.lower(), L.upper(), outcome, flush=True)

if __name__ == "__main__":
    main()
