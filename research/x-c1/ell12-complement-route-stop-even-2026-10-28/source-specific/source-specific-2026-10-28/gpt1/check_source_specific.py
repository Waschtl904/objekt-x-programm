"""Exact feasibility test for ONE selected source-specific upper price.

This does not lower-bound the true inverse energy and performs no integration.
The form/domain implication X >= U8[g8] is proved in SOURCE_SPECIFIC_CONTRACT.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import sys
if sys.flags.optimize:
    raise SystemExit("OPTIMIZED_PYTHON_REJECTED")
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BINDINGS = {
    "full-energy-execution-2026-10-27/ENERGY_BRIDGE_RATIONAL.json": "d7642ab3b96fa10ff9aa75e784f934d81b62432c870c76da0567356bea4fb78e",
    "full-energy-execution-2026-10-27/inputs/INVERSE_DATA.json": "41afad50d284b8bf2e170449384c33bb256743abee8c720904c95f2f64f8b90f",
    "full-energy-execution-2026-10-27/inputs/DIRECT_FORM.json": "8f9f1baa83a18f4045f949622e583e6a7e7eeb77b11283ae210d5525b7899cfd",
    "joint-energy-2026-10-28/gpt1-metric/COUPLING_ONLY_DECISION_RATIONAL.json": "7ceed06fdfe377a9cf32457887a0b8d3acbdcd42fd7bcebeb3622d815e40caef",
    "full-energy-execution-2026-10-27/sources/ANSCHLUSSSATZ.txt": "debe5b5552291d83e1bfcff954b8cc581b4e544a50eb954234428e261f3caf61",
    "full-energy-execution-2026-10-27/sources/FULL_FORM_ORDER.txt": "a9d6dbd2d2403e4885bf6581243e5d0d75fd816046ce17589f3b171e79060a43",
    "full-energy-execution-2026-10-27/sources/HERLEITUNG.txt": "d221c870fccf8e8ab4298e53c7beff35b63bd704f5a6d0782864b51e93ce83d7",
}
def need(ok, why):
    if not ok:
        raise RuntimeError(why)
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def check_bindings(bindings=BINDINGS):
    for name,digest in bindings.items():
        need(sha(ROOT/name)==digest, "source byte binding: "+name)
def load(name): return json.loads((ROOT/name).read_bytes())

def verify_math(xlo,klo,theta,Dhi):
    xfloor=F(18,25)
    znorm=F(20738,10000)
    ecap=F(107,1000)
    cut=F(9,2)
    need(xlo>xfloor, "accepted core energy strictly exceeds 18/25")
    need(klo>=F(215033,50000), "accepted paid coupling energy")
    need(znorm**2<klo, "rational lower Q-norm witness")
    need(0<=theta<F(1,400), "whole formdual residual Gram constant")
    need(F(1,400)*cut<ecap**2, "upper residual norm witness when X<cut")
    need(znorm>ecap, "positive reverse triangle lower")
    small_case=xfloor+(znorm-ecap)**2
    need(small_case==F(28676889,6250000), "exact small-X case arithmetic")
    need(small_case>cut, "small-X price exceeds the split value")
    need(Dhi<cut, "selected upper price cannot give a positive reserve")
    return {
        "core_energy_lower_used":str(xfloor),
        "coupling_norm_lower_witness":str(znorm),
        "theta_upper_used":"1/400",
        "large_X_case_threshold":str(cut),
        "small_X_residual_norm_upper":str(ecap),
        "small_X_price_lower":str(small_case),
        "global_selected_upper_price_lower":str(cut),
        "direct_upper":str(Dhi),
        "price_lower_minus_direct_upper":str(cut-Dhi),
    }

def main():
    check_bindings()
    bridge=load("full-energy-execution-2026-10-27/ENERGY_BRIDGE_RATIONAL.json")
    need(bridge["status"]=="PASS_EXACT_ARITHMETIC_OF_NEW_BRIDGE_UNDER_INHERITED_OPERATOR_IDENTITIES","accepted U8 bridge")
    coupling=load("joint-energy-2026-10-28/gpt1-metric/COUPLING_ONLY_DECISION_RATIONAL.json")
    need(coupling["status"]=="INDEPENDENT_EXACT_RATIONAL_COUPLING_ONLY_ROUTE_EXCLUSION","accepted all12 recombination")
    inv=load("full-energy-execution-2026-10-27/inputs/INVERSE_DATA.json")
    direct=load("full-energy-execution-2026-10-27/inputs/DIRECT_FORM.json")
    Xlo=F(bridge["exact"]["U8_lower"])
    Klo=F(coupling["simplified_coupling_energy_lower"])
    theta=F(inv["theta_exact"])
    Dhi=F(437284983429949477,10**17)
    need(F(direct["D_hi"])<=Dhi,"direct endpoint outward rounding")
    proof=verify_math(Xlo,Klo,theta,Dhi)
    out={
        "status":"ONE_SELECTED_SOURCE_SPECIFIC_UPPER_PRICE_INFEASIBLE_FOR_POSITIVE_COMPARISON",
        "formula":"A_src = X + (r12-eB)^T Cg^-1 (r12-eB)/(1-theta)",
        "X_definition":"<g9,Qold(Knew)^-1 g9>",
        "eB_definition":"(R B)^* Qold(Knew)^-1 g9, R=h-Q1 V",
        "source":"Z ell12, unchanged",
        "proof":proof,
        "source_sha256":BINDINGS,
        "contract_sha256":sha(HERE/"SOURCE_SPECIFIC_CONTRACT.txt"),
        "checker_sha256":sha(Path(__file__)),
        "new_integration":False,
        "new_inverse_response":False,
        "claim_about_true_inverse_energy":"NO LOWER BOUND asserted; only an upper replacement price is bounded from below.",
        "inherited_assumptions":"H1-H4 and accepted v2 form/domain and joint rest Gram interfaces",
    }
    (HERE/"SOURCE_SPECIFIC_RATIONAL.json").write_text(json.dumps(out,indent=2)+"\n")
    print(out["status"])
    print("A_src >=",proof["global_selected_upper_price_lower"],"> D_hi; margin",proof["price_lower_minus_direct_upper"])
if __name__=="__main__":main()
