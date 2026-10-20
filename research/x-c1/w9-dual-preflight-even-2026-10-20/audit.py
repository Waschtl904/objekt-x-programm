"""Independent rational endpoint logic; no upper-bound-to-exclusion shortcut."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

HERE=Path(__file__).resolve().parent


def need(ok,message):
    if not ok:
        raise RuntimeError(message)


def check(r,matrix_raw):
    need(__debug__,"Do not use python -O")
    need(hashlib.sha256(matrix_raw).hexdigest()==r["L_UPPER_sha256"],"L matrix binding")
    matrix=json.loads(matrix_raw)
    need(matrix["full_L_lower_minus_21_over_5_WJ_audit"]==r["L_floor_audit"],"Floor audit binding")
    need(r["L_floor_audit"]["positive_pivots"]==84 and
         Q(r["L_floor_audit"]["smallest_pivot_lower"])>0,"Positive L floor")
    need(r["exact_null_equations"]==672,"Exact constraints")
    elo,ehi=map(Q,r["inherited_partial_energy_interval"])
    klo,khi=map(Q,r["budget_interval"])
    dlo,dhi=map(Q,r["auxiliary_finite_energy_interval"])
    weight=Q(r["dual_weight"])
    need(weight==Q(91095000000000000000,8067286322727467113),"Frozen dual coefficient")
    need(0<=elo<=ehi<klo<=khi and 0<=dlo<=dhi and weight>0,"Ordered inherited pass")
    need(Q(r["full_dual_energy_lower"])==dlo,"Dual lower provenance")
    total=elo+weight*dlo
    need(Q(r["full_comparison_energy_lower"])==total,"Entire comparison lower")
    need(Q(r["full_lower_minus_budget_upper"])==total-khi,"Actual exclusion gap")
    need(Q(r["dual_lower_sufficient_for_exclusion"])==(khi-elo)/weight,"Exclusion threshold")
    need(Q(r["inherited_dual_upper_sufficient_for_pass"])==(klo-ehi)/weight,"Distinct pass threshold")
    expected="FULL_FIXED_COMPARISON_EXCLUDED_BY_DUAL_LOWER" if total>khi else "DUAL_PREFLIGHT_OPEN"
    need(r["outcome"]==expected,"No exclusion without full lower > budget upper")
    need(r["full_dual_energy_upper"] is None and r["full_comparison_energy_upper"] is None,
         "No complete upper enclosure")
    for key in ("partial_certificate_changed","physical_witness_changed","answer_matrix_changed",
                "comparison_weights_changed","new_integrations","infinite_tail_computed",
                "full_dual_enclosure_claimed","actual_A9_inverse_excluded",
                "all_majorants_of_new_lower_form_excluded","milestone_4_closed","N12_closed"):
        need(r[key] is False,"Scope: "+key)
    need(r["common_FJ_errors_retained"] and r["whole_residual_error_included"],"Complete lower-bound errors")
    need(r["status"]=="AUTHOR_DERIVED" and r["review_status"]=="EXTERNAL_REVIEW_OPEN","Review status")
    # A too-large upper bound alone never licenses an exclusion.
    def classify(partial_lo,dual_lo,weight,budget_hi):
        return partial_lo+weight*dual_lo>budget_hi
    need(not classify(Q(1),Q(0),Q(2),Q(3)),"Upper-only control")
    need(not classify(Q(1),Q(1),Q(2),Q(3)),"Strict boundary control")
    need(classify(Q(1),Q(2),Q(2),Q(3)),"Strict lower control")
    return expected


if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--directory",type=Path,default=HERE)
    a=p.parse_args()
    print("PASS: independent rational full-energy lower decision; "+
          check(json.loads((a.directory/"EXPECTED.json").read_bytes()),(a.directory/"L_UPPER.json").read_bytes()))
