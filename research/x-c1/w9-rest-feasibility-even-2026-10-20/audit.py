"""Exact endpoint and minimum-cost dual-witness audit without Arb arithmetic."""
import json
from fractions import Fraction as Q
from pathlib import Path
import verify


def check(r, finite, data):
    need=verify.need
    need(__debug__,"Do not use python -O")
    old,eta=verify.js(data["previous_result"]),verify.js(data["eta_result"])
    base_hi=Q(old["base_actual_energy_interval"][1])
    pair_hi=Q(old["pairing_actual_interval"][1])
    B_lo=Q(old["form_B_model"][0])
    du=Q(old["form_common_D_U_error"][1])
    a_hi=Q(old["form_a_Ki_model_norm_squared"][1])
    p=Q(old["form_refinement"]["square_loss_upper"])
    e=Q(old["form_a_Ki_error_norm"][1])
    eq_hi=Q(eta["eta_q_interval"][1])
    upper=base_hi+2*pair_hi-B_lo+du+a_hi+p+e*e+eq_hi
    lower=Q(eta["inverse_energy_lower"])
    need(list(map(Q,r["F_interval"]))==[lower,upper],"Whole F endpoints")
    need(Q(r["positive_quadratic_error"])==e*e,"Positive square retained")
    need(Q(r["H_form_lower"])==B_lo-du-a_hi-p-e*e-eq_hi,"H lower sign")
    budget_lo,budget_hi=map(Q,old["budget_interval"])
    margin=budget_lo-upper
    need(r["budget_interval"]==old["budget_interval"],"Same budget")
    need(Q(r["budget_lower_minus_F_upper"])==margin,"Correct upper-comparison gap")
    need(r["positive_rest_upper_affordable"]==(margin>0),"No false rest reserve")
    need(r["lower_excludes"]==(lower>budget_hi),"No inference from large upper")
    need(sum(map(Q,r["width_components"].values()))==upper-lower,"Whole width accounting")
    E,D,X,w=verify.matrices(data)
    P=[[Q(v)for v in row]for row in finite["P_lower_rational"]]
    diag=list(map(Q,finite["P_lower_to_upper_diagonal"]))
    z=list(map(Q,finite["cost_lower_dual_test"]))
    need(len(P)==84 and len(diag)==len(z)==84 and all(v>=0 for v in diag),"Cost certificate shape")
    quadratic=sum(P[i][i]*z[i]**2+diag[i]*z[i]**2 for i in range(84))
    quadratic+=sum((P[i][j]+P[j][i])*z[i]*z[j] for i in range(84) for j in range(i))
    low=2*sum(wi*zi for wi,zi in zip(w,z))-quadratic
    high=Q(finite["minimum_E_cost_upper"])
    need(0<low<=high,"Positive minimum cost")
    need(list(map(Q,r["minimum_E_cost_interval"]))==[low,high],"Independent cost lower")
    need(r["minimum_E_cost_interval"]==finite["minimum_E_cost_interval"],"Cost source")
    need(finite["rank_and_cost_positive_block"]["positive_pivots"]==85,"Rank/cost pivots")
    need(finite["form_floor_positive_block"]["positive_pivots"]==203,"Whole floor pivots")
    eps=Q(finite["epsilon"]);c=Q(r["c"]);beta=Q(r["beta"])
    need(0<eps<1 and c==Q(1977,500000),"Positive floor constants")
    need(beta==Q(verify.js(data["inverse_even"])["beta"])
         ==Q(verify.js(data["pilot_result"])["beta"]),"Inherited beta")
    kappa=(1-c)*eps
    need(Q(r["epsilon"])==eps and Q(r["kappa"])==kappa,"Kappa")
    need(Q(r["full_Ru_Ldual_energy_upper"])==c*beta*high,"Whole R transport upper")
    need(Q(r["minimum_E_transport_bound_expression_lower"])==c*beta*low,"Minimum bound expression")
    need(Q(r["required_full_residual_Ldual_energy_upper"])==kappa*beta*margin,"Signed target")
    need(Q(r["transport_only_inverse_energy_price_upper"])==c*high/kappa,"Inverse residual price")
    need(r["response_rank"]==84 and r["representation_is_E_minimal"] is True,"Response interpretation")
    need(r["test_vector_sha256"]==verify.VECTOR==verify.sha(data["frozen_vector"])
         and r["K_new_sha256"]==verify.KNEW,"Frozen source identities")
    for key in ("full_residual_energy_computed","full_inverse_upper_computed","underform_excluded",
                "actual_Ru_lower_claimed","partial_pass","new_integration","new_physical_direction",
                "N12_closed","milestone_4_closed"):
        need(r[key] is False,"Scope: "+key)
    need(r["dual_reserve"] is None,"No reserve")
    expected="UPPER_CONTROL_ROUTE_TOO_COARSE" if margin<=0 else "REST_DATA_REQUIRED"
    need(r["outcome"]==expected,"Route decision")
    need(r["status"]=="AUTHOR_DERIVED" and r["review_status"]=="EXTERNAL_REVIEW_OPEN","Review status")
    return expected


if __name__=="__main__":
    here=Path(__file__).resolve().parent
    checked=verify.package()
    data=verify.snapshot(here.parents[2],checked["INPUT_BINDINGS.json"])
    print("PASS: independent rational endpoints and minimum-cost witness:",
          check(json.loads(checked["RESULT.json"]),json.loads(checked["FINITE.json"]),data))
