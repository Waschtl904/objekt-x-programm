"""Independent Fraction endpoint audit, with no Arb or numerical engine import."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path

HERE=Path(__file__).resolve().parent

def need(ok,message):
    if not ok: raise RuntimeError(message)

def sqrt_upper(x):
    need(x>=0,"Negative square")
    scale=10**90;a=x*scale**2
    k=isqrt(a.numerator//a.denominator)
    if Q(k*k)<a: k+=1
    need(Q(k*k,scale**2)>=x,"Integer square-root enclosure")
    return Q(k,scale)

def classify(lower,budget):
    return "SCHUR_UNDERFORM_COMPARISON_EXCLUDED" if lower>budget else "SCHUR_LOWER_TEST_OPEN"

def check_weights(w,p,d):
    need(__debug__,"Do not use python -O")
    c,b0,beta=map(Q,(w["c"],w["b0"],w["beta"]))
    need(c==Q(1977,500000) and b0==Q(51,50) and beta==Q(p["beta"])>0,"Family constants")
    t=1/(1-c)
    need(1<t<=b0 and Q(w["minimum_weight"])==t,"Nonnegative C coefficient")
    need(p["partial_actual_energy_interval"]==d["inherited_partial_energy_interval"],"Common partial interval")
    need(p["candidate_sha256"]==d["candidate_sha256"]==w["physical_candidate_sha256"],"Physical witness")
    need(p["K_P_certificate_sha256"]==d["K_P_sha256"]==w["K_P_certificate_sha256"],"Budget provenance")
    need(p["K_new_canonical_sha256"]==d["K_new_canonical_sha256"]==w["K_new_canonical_sha256"],"Fixed K")
    part=Q(p["partial_actual_energy_interval"][0]);dual=Q(d["full_dual_energy_lower"])
    budget=Q(d["budget_interval"][1]);lower=t*(part/b0+dual/beta)
    need(Q(w["partial_lower"])==part and Q(w["full_dual_lower"])==dual,"Energy inputs")
    need(Q(w["budget_upper"])==budget and Q(w["family_energy_lower"])==lower,"Family lower endpoint")
    need(Q(w["lower_minus_budget_upper"])==lower-budget,"Family gap")
    expected="YOUNG_WEIGHT_FAMILY_EXCLUDED" if lower>budget else "WEIGHT_FAMILY_OPEN"
    need(w["outcome"]==expected,"Family decision")
    need(w["weight_search"] is False and w["new_integrations"] is False,"No weight search")
    need(w["all_majorants_of_Q_new_excluded"] is False,"Family scope")
    # Exact coefficient identity for arbitrary nonnegative C,B,D.
    a=Q(p["a_weight"]);b=b0
    coefficients=(1-t/b0,b-t,(a-t)/beta)
    need(all(x>=0 for x in coefficients),"Coefficient proof")
    C,B,D=Q(7,11),Q(2,3),Q(3,5)
    need(C+b*B+a*D/beta-t*((C+b0*B)/b0+D/beta)
         ==coefficients[0]*C+coefficients[1]*B+coefficients[2]*D,"Algebra control")
    return expected

def check_result(r,w,frozen):
    need(__debug__,"Do not use python -O")
    need(r["K_new_sha256"]==w["K_new_canonical_sha256"]==frozen["K_new_sha256"],"New K identity")
    need(r["physical_candidate_sha256"]==w["physical_candidate_sha256"]==frozen["physical_candidate_sha256"],"Same physical witness")
    need(r["K_P_certificate_sha256"]==w["K_P_certificate_sha256"],"Same budget")
    need(r["test_vector_sha256"]==hashlib.sha256((json.dumps(frozen,indent=2)+"\n").encode()).hexdigest(),"Frozen vector bytes")
    f=r["form_refinement"]
    g={k:Q(v[1]) for k,v in f["directional_Grams"].items()}
    direct=Q(f["direct_relative_error"][1])*sqrt_upper(g["GF_r"]*g["GJ_w"])
    feature=sum(sqrt_upper(g[a]*g[b]) for a,b in
                [("model_F","error_J"),("error_F","model_J"),("error_F","error_J")])
    price=Q(f["square_loss_upper"])
    need(price>=2*(direct+feature),"Independent directional form loss")
    square=max(Q(0),Q(r["form_a_Ki_model_norm_squared"][0])-price)
    need(Q(r["actual_a_square_lower"])==square,"Actual square lower")
    H=Q(r["form_B_model"][1])+Q(r["form_common_D_U_error"][1])-square
    lower=Q(r["base_actual_energy_interval"][0])+2*Q(r["pairing_actual_interval"][0])-H
    budget=Q(r["budget_interval"][1])
    need(budget==Q(w["budget_upper"]),"Same budget endpoint")
    need(Q(r["H_new_form_upper"])==H,"Upper form sign")
    need(Q(r["inverse_energy_lower"])==lower,"Variational lower endpoint")
    need(Q(r["lower_minus_budget_upper"])==lower-budget,"One-sided gap")
    need(r["outcome"]==classify(lower,budget),"One-sided outcome")
    for key in ("full_inverse_energy_upper_claimed","partial_pass","RL_computed",
                "new_integrations","adaptive_search","K_new_changed","frozen_response_changed",
                "physical_witness_changed","N12_closed","milestone_4_closed"):
        need(r[key] is False,"Scope: "+key)
    need(r["dual_reserve"] is None and r["positive_eta_q_term_unused"],"No claimed upper or reserve")
    need(r["status"]=="AUTHOR_DERIVED" and r["review_status"]=="EXTERNAL_REVIEW_OPEN","Review status")
    need(classify(Q(2),Q(2))=="SCHUR_LOWER_TEST_OPEN","Strict boundary")
    need(classify(Q(1),Q(2))=="SCHUR_LOWER_TEST_OPEN","Lower below budget is open")
    need(classify(Q(3),Q(2))=="SCHUR_UNDERFORM_COMPARISON_EXCLUDED","Strict exclusion")
    return r["outcome"]

if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--directory",type=Path,default=HERE)
    args=ap.parse_args();directory=args.directory;root=HERE.parents[2]
    bindings=json.loads((directory/"INPUT_BINDINGS.json").read_bytes())
    def bound(name):
        item=bindings["files"][name];raw=(root/item["path"]).read_bytes()
        need(hashlib.sha256(raw).hexdigest()==item["sha256"],"Input hash: "+name)
        return json.loads(raw)
    w=json.loads((directory/"WEIGHTS.json").read_bytes())
    print("PASS: "+check_weights(w,bound("pilot_result"),bound("dual_result")))
    print("PASS: "+check_result(json.loads((directory/"RESULT.json").read_bytes()),w,
                                json.loads((directory/"CANDIDATE.json").read_bytes())))
