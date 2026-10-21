"""Independent stdlib audit of the published endpoint decision and reserve."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def check(result, schur_raw):
    need(__debug__, "Do not use python -O")
    schur = json.loads(schur_raw)
    need(hashlib.sha256(schur_raw).hexdigest() == result["SCHUR_sha256"], "Schur binding")
    rows = schur["K_new_rational"]
    need(hashlib.sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()
         == result["K_new_canonical_sha256"]
         == "89ded551059d1279c646bc17e3b5ab3e2a7f7a261d1c239ac752b7f0d35467a8",
         "Frozen candidate")
    need(schur["complete_287_block"] == result["complete_287_block"], "Full block reporting")
    need(result["complete_287_block"]["positive_pivots"] == 287, "287 positive pivots")
    need(Q(result["complete_287_block"]["smallest_pivot_lower"]) > 0, "Strict pivot bound")
    elo, ehi = map(Q, result["partial_actual_energy_interval"])
    klo, khi = map(Q, result["budget_interval"])
    need(0 <= elo <= ehi and 0 < klo <= khi, "Positive ordered endpoints")
    a, b, c, beta = map(Q, (result["a_weight"], result["P_weight"],
                            result["residual_cap"], result["beta"]))
    need((a, b, c) == (Q(500000, 399173), Q(51, 50), Q(1977, 500000)),
         "Frozen weights")
    need(beta > 0 and a*(1-c) > 1 and b*(1-c) > 1, "Weight domains")
    need((a*(1-c)-1)*(b*(1-c)-1) == c, "Exact Young identity")
    need(Q(result["dual_weight"]) == a/beta, "Dual coefficient")
    expected = ("PILOT_COMPARISON_EXCLUDED" if elo > khi else
                "PILOT_PARTIAL_PASS" if ehi < klo else "PILOT_INCONCLUSIVE")
    need(result["outcome"] == expected, "Endpoint classification")
    need(list(map(Q, result["energy_minus_budget_interval"])) == [elo-khi, ehi-klo],
         "Exact energy-budget difference")
    if expected == "PILOT_PARTIAL_PASS":
        need(Q(result["partial_pass_reserve"]) == klo-ehi > 0, "Positive partial reserve")
        need(Q(result["sufficient_actual_dual_energy_upper"]) == beta*(klo-ehi)/a > 0,
             "Actual dual-energy sufficient threshold")
    else:
        need(result["partial_pass_reserve"] is None and
             result["sufficient_actual_dual_energy_upper"] is None, "No reserve without pass")
    for key in ("RL_computed", "full_energy_upper_claimed", "N12_closed", "milestone_4_closed",
                "new_integrations", "frozen_response_changed", "frozen_direction_changed",
                "K_P_changed"):
        need(result[key] is False, "Scope: "+key)
    for key in ("a_fin_error_paid_once", "common_FJ_errors_retained", "new_partial_norm_recomputed"):
        need(result[key] is True, "Complete error handling: "+key)
    need(result["status"] == "AUTHOR_DERIVED" and result["review_status"] == "EXTERNAL_REVIEW_OPEN",
         "No external-review promotion")
    return expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, default=HERE)
    args = parser.parse_args()
    outcome = check(json.loads((args.directory/"RESULT.json").read_bytes()),
                    (args.directory/"SCHUR.json").read_bytes())
    print("PASS: independent rational endpoints, weights, reserve and scope; "+outcome)
