"""Rational decision for two odd directions; run inside the repository checkout."""
import argparse
import json
from fractions import Fraction as Q
from pathlib import Path

from budget import COEFFICIENTS, PACKAGE, PAIR_SHA256, git_blob

HERE = Path(__file__).resolve().parent
ODD = Path("handoffs/a9-a11-ungerader-restvergleich-2026-11-24/feldrechnung/ZEUGE.json")
EVEN = Path("research/x-c1/w9-residual-centered-control-even-2026-10-21/whole/WHOLE_RESULT.json")

def read(p):
    return json.loads(p.read_bytes())

def verify(root, odd_path, budget_path, variation_path):
    budget, var = read(budget_path), read(variation_path)
    assert git_blob(odd_path) == "41c3cd0f6a1ff8d7b4e265932c7a829826bac596"
    assert git_blob(root/EVEN) == "da2d028e0e76953a63e7a37da9f3eff15b1aa386"
    odd, even = read(odd_path), read(root/EVEN)
    candidate = root/PACKAGE/"expected/CANDIDATE_odd.json"
    assert git_blob(candidate) == "4e21fad9f0569fe1738e328e620f4da4075b7e76"
    old = list(map(Q,read(candidate)["raw_coefficients"]))
    assert len(old) == len(COEFFICIENTS) == 12
    assert old[0]*COEFFICIENTS[1] != old[1]*COEFFICIENTS[0]
    assert list(map(int,budget["raw_coefficients"])) == var["raw"] == COEFFICIENTS
    assert budget["source_sha256"] == var["pairs_sha256"] == PAIR_SHA256
    assert len(var["test_w_rational"]) == 84 and len(var["test_y_rational"]) == 12
    assert Q(even["strict_margin_lower"]) > Q("0.166244453e-6")
    odd_margin = Q(odd["positive_margin_lower"])
    assert odd_margin >= Q("7.4034790876e-8")
    lo, hi = map(Q,budget["K_P_interval"])
    assert Q("3.7402002545037") < lo <= hi < Q("3.7402002545039")
    base, pair, b, bprice, sq, eta = [Q(var[k]) for k in
        ("base_lower","pair_lower","B_model_upper","B_price_upper","square_lower","eta_direct_lower")]
    finite_lower = min(Q(var["F_lower"]), base+2*pair-b-bprice+sq+eta)
    assert finite_lower > Q("3.7438933640601")
    gap = finite_lower-hi
    assert gap > Q("0.0036931095562")
    assert odd_margin*gap > Q("2.73418e-10")
    price, delta, eta_upper = [Q(var[k]) for k in
        ("physical_F_directional_price","physical_grouped_force_error","restore_eta_upper")]
    assert 0<=price<Q("0.000023727346") and 0<=delta<Q("0.000000125")
    assert 0<=eta_upper<Q("0.000003436102")
    restored_floor = finite_lower-price-delta**2-eta_upper
    assert restored_floor-hi > Q("0.00366594")
    return {"status":"AUTHOR_DERIVED_CONDITIONAL_EXCLUSION","parity":"odd",
            "budget_upper":"3.7402002545039","inverse_lower":"3.7438933640601",
            "odd_comparison_upper":"-0.0036931095562","two_by_two_determinant_upper":"-2.73418e-10",
            "restored_shell_comparison_upper":"-0.00366594","outer_response":"frozen P",
            "restored_shell_core":"frozen U8","external_review":"OPEN","point4_closed":False}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=HERE.parents[1])
    parser.add_argument("--odd", type=Path)
    parser.add_argument("--budget", type=Path, default=HERE/"BUDGET.json")
    parser.add_argument("--variation", type=Path, default=HERE/"VARIATION.json")
    options = parser.parse_args()
    result = verify(options.root, options.odd or options.root/ODD, options.budget, options.variation)
    print(json.dumps(result, indent=2))
