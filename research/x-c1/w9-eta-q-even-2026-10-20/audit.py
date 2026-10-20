"""Independent exact midpoint/radius audit of the scalar, not the old proofs."""
import gzip
import json
from fractions import Fraction as Q
from pathlib import Path
import verify


def check(result, data):
    verify.need(__debug__, "Do not use python -O")
    need = verify.need
    prior = json.loads(data["previous_result"])
    w = [Q(v) for v in json.loads(data["frozen_vector"])["raw_coefficients"]]
    case = json.loads(gzip.decompress(data["common"]))["cases"][0]
    values = []
    for name in ("D96_lower_model", "D96_upper_model"):
        centre = radius = Q(0)
        rows = case[name]
        # Pair transposed entries first, independently of the certifier's
        # ordered endpoint sum. No symmetry of rounded intervals is assumed.
        for i in range(84):
            lo, hi = map(Q, rows[i+12][i+12])
            need(lo <= hi, "Diagonal interval")
            centre += w[i]**2*(lo+hi)/2
            radius += w[i]**2*(hi-lo)/2
            for j in range(i):
                a, b = map(Q, rows[i+12][j+12])
                c, d = map(Q, rows[j+12][i+12])
                need(a <= b and c <= d, "Cross interval")
                centre += w[i]*w[j]*(a+b+c+d)/2
                radius += abs(w[i]*w[j])*(b-a+d-c)/2
        values.append([centre-radius, centre+radius])
    need(list(map(Q, result["D_lower_quadratic_interval"])) == values[0], "Lower quadratic")
    need(list(map(Q, result["D_upper_quadratic_interval"])) == values[1], "Upper quadratic")
    q = [values[0][0], values[1][1]]
    need(0 < q[0] <= q[1], "Positive form interval")
    need(list(map(Q, result["q_interval"])) == q, "Form interval")
    eta = Q(1, 10**10)
    need(Q(result["eta"]) == eta, "Fixed eta")
    interval = [eta*x for x in q]
    need(list(map(Q, result["eta_q_interval"])) == interval, "eta multiplication")
    old = Q(prior["inverse_energy_lower"])
    lower = old+interval[0]
    budget = Q(prior["budget_interval"][1])
    need(Q(result["inherited_inverse_energy_lower"]) == old, "Inherited lower")
    need(Q(result["inverse_energy_lower"]) == lower, "Positive gain sign")
    need(result["budget_interval"] == prior["budget_interval"], "Inherited budget")
    need(Q(result["updated_H_new_form_upper"]) == Q(prior["H_new_form_upper"])-interval[0],
         "Form upper sign")
    need(Q(result["lower_minus_budget_upper"]) == lower-budget, "Decision gap")
    need(Q(result["original_gap_to_budget_upper"]) == budget-old, "Original gap")
    need(Q(result["remaining_gap_to_budget_upper"]) == budget-lower, "Remaining gap")
    need(result["eta_upper_insufficient_to_close_inherited_gap"] == (interval[1] < budget-old),
         "Upper bound significance")
    expected = "SCHUR_UNDERFORM_COMPARISON_EXCLUDED" if lower > budget else "SCHUR_LOWER_TEST_OPEN"
    need(result["outcome"] == expected, "One-sided decision")
    for key in ("full_inverse_energy_upper_claimed", "partial_pass", "previous_bounds_changed",
                "test_vector_changed", "physical_witness_changed", "frozen_response_changed",
                "K_new_changed", "new_integrations", "new_solves", "adaptive_search",
                "N12_closed", "milestone_4_closed"):
        need(result[key] is False, "Scope: "+key)
    need(result["dual_reserve"] is None, "No reserve")
    need(result["status"] == "AUTHOR_DERIVED"
         and result["review_status"] == "EXTERNAL_REVIEW_OPEN", "Review status")
    for key in ("test_vector_sha256", "K_new_sha256", "physical_candidate_sha256",
                "K_P_certificate_sha256"):
        need(result[key] == prior[key], "Inherited identity: "+key)
    need(result["previous_result_sha256"] == verify.sha(data["previous_result"]), "Result binding")
    need(result["common_source_sha256"] == verify.sha(data["common"]), "Common binding")
    return expected


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    package = verify.checked_package(here)
    data = verify.snapshot(here.parents[2], package["INPUT_BINDINGS.json"])
    print("PASS: independent rational midpoint/radius audit: "
          + check(json.loads(package["RESULT.json"]), data))
