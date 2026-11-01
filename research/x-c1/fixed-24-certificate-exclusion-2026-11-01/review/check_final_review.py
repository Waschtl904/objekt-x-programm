"""GPT1: independent rational close of the targeted physical-rest review.

No quadrature is executed. All arithmetic deciding inequalities is Fraction
arithmetic. The analytic audit and the correction proof are in BERICHT.txt.
The original GPT2 files, including their original result, are never changed.
"""
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
sys.set_int_max_str_digits(100000)
HERE = Path(__file__).resolve().parent
INP = HERE / "inputs"


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def read(name):
    return json.loads((INP / name).read_bytes())


def upper(x):
    need(isinstance(x, list) and len(x) == 2, "directed endpoints required")
    a, b = map(F, x)
    need(a <= b, "ordered endpoints")
    return b


def ceilq(x, digits=15):
    n = 10**digits
    return F(-((-x.numerator*n)//x.denominator), n)


def floorq(x, digits=18):
    n = 10**digits
    return F((x.numerator*n)//x.denominator, n)


def sqrt_upper(x, digits=24):
    need(x >= 0, "nonnegative radicand")
    scale = 10**digits
    n = math.isqrt((x.numerator*scale*scale)//x.denominator)
    if F(n*n, scale*scale) < x:
        n += 1
    out = F(n, scale)
    need(out*out >= x, "rational directed square root")
    return out


def encode(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


def calculate():
    original_manifest = read("ORIGINAL_MANIFEST.json")
    bound_files = []
    for p in sorted(INP.rglob("*")):
        if not p.is_file() or p.name == "ORIGINAL_MANIFEST.json":
            continue
        name = p.relative_to(INP).as_posix()
        raw = p.read_bytes()
        info = original_manifest[name]
        need(len(raw) == info["bytes"], "original byte count " + name)
        need(hashlib.sha256(raw).hexdigest() == info["sha256"], "original SHA " + name)
        bound_files.append(name)

    author = read("FINAL_REST_RESULT.json")
    tr = read("PHYSICAL_REST_TRANSPORT.json")
    values = tr["values"]
    geometry = read("BOUNDARY_INPUTS.json")["geometry"]
    budget = read("gpt1-review/GPT1_BUDGET.json")
    prior = read("gpt1-review/JOINT_REVIEW.json")
    data = read("gpt1-data/BANK_ERROR_RESULT.json")
    plan = read("NORM_PLAN.json")
    caps = read("STRUCTURED_GAUSS_CAPS.json")
    ends = read("ANALYTIC_ENDS.json")
    need(len(plan["panels"]) == len(caps["rows"]) == 135, "all fixed panels")
    need(plan["node_count"] == 17280, "fixed node count")
    need(F(plan["endstrip_exact"]) == F(1, 2**200), "positive endstrips")
    need(caps["plan_sha256"] == hashlib.sha256((INP/"NORM_PLAN.json").read_bytes()).hexdigest(), "bound plan")
    need(len(list((INP/"norm-panels").glob("*.json"))) == 135, "unique retained panels")
    estimates, errors, widths = [F(0), F(0)], [F(0), F(0)], [F(0), F(0)]
    left = list(map(F, plan["left_endpoint_symbolic"]))
    right = list(map(F, plan["right_endpoint_symbolic"]))
    left[-1] += F(1, 2**200)
    right[-1] -= F(1, 2**200)
    previous = left
    for i, panel in enumerate(plan["panels"]):
        need(list(map(F, panel["lo_symbolic"])) == previous, "exact consecutive coverage")
        previous = list(map(F, panel["hi_symbolic"]))
        row = read("norm-panels/%03d.json" % i)
        cap = caps["rows"][i]
        need(panel["index"] == row["index"] == cap["index"] == i, "panel indices")
        need(panel["order"] == row["order"] == 128 and panel["rho"] == row["rho"] == 2, "same fixed rule")
        need(row["lo_symbolic"] == panel["lo_symbolic"] and row["hi_symbolic"] == panel["hi_symbolic"], "same node interval")
        for name, digest in row["inputs_sha256"].items():
            need(original_manifest[name]["sha256"] == digest, "same numerical inputs " + name)
        w = upper(panel["hi"]) - F(panel["lo"][0])
        need(w > 0, "positive panel width")
        for k in range(2):
            e = upper(cap["gauss_error_upper"][k])
            c = upper(cap["complex_cap_HS"][k])
            need(e >= 16*w*c*c/F(2**256), "whole analytic Gauss error")
            estimates[k] += upper(row["squared_integral_estimate"][k])
            errors[k] += e
            widths[k] += upper(row["squared_integral_estimate"][k]) - F(row["squared_integral_estimate"][k][0])
    need(previous == right, "right complete coverage")
    tails = [upper(x) for x in ends["endstrip_square_norm_by_group"]]
    need(estimates == list(map(F, author["integral_square_estimates_upper"])), "independent estimator sum")
    need(errors == list(map(F, author["analytic_Gauss_square_errors_upper"])), "independent analytic error sum")
    need(tails == list(map(F, author["endstrip_square_prices"])), "same whole endstrip prices")
    need(ends["all_endpoints_included"], "whole ends")

    old_prices = {k: upper(v) for k, v in tr["fixed_prices"].items()}
    need(old_prices == {k: F(v) for k, v in author["fixed_physical_high_prices"].items()}, "same ten saved prices")
    need(len(old_prices) == 10 and all(x >= 0 for x in old_prices.values()), "complete positive fixed ledger")

    # Concrete correction: ||Theta*Theta|| <= gamma, not sqrt(gamma).
    # A conservative replacement is eV_new <= gamma_upper * eV_old,
    # since gamma >= sqrt(gamma) >= 1. This also covers the unchanged
    # positive Cpre coefficient price already in eV_old.
    gamma = upper(geometry["geometry"]["gamma"])
    need(F(geometry["geometry"]["gamma"][0]) > 1, "gamma greater than one")
    d12_old, d12_safe = F("1.573e-50"), F("2.632e-50")
    source_factor = d12_safe/d12_old
    need(source_factor > 1, "use the previously confirmed GPT1 D12 cap")
    w_lower = F(values["w_model_whole_upper"][0])
    need(w_lower > 1, "positive saved whole model guard")

    # W = 1 + A*v + (V+eV)*a + 2*gamma/delta*(q+graph+ecore).
    # Pcore = 30*gamma/delta*ecore. Thus W_new is at most
    # gamma_upper*W + (source_factor-1)*Pcore/15.
    # Multiplying the complete saved positive complex/end envelopes by
    # cap_factor transports the corrections without any new evaluation.
    cap_factor = gamma + (source_factor-1)*old_prices["core_source_model_and_new_Taylor"]/(15*w_lower)
    need(cap_factor >= gamma > 1, "positive entire-envelope inflation")
    squared = [estimates[k] + cap_factor**2*(errors[k]+tails[k]) for k in range(2)]
    model = [sqrt_upper(x) for x in squared]
    prices = dict(old_prices)
    prices["direct_source_D_C_and_T"] *= source_factor
    prices["core_source_model_and_new_Taylor"] *= source_factor
    prices["physical_V_synthesis_and_Cpre"] *= gamma
    prices["whole_cross_kernel_Gamma224_tail"] *= cap_factor
    ev = upper(values["e_v_total_Ki"])
    exi = gamma*upper(values["joint_v_response_physical_model_difference"])
    need(0 < ev < 1, "positive whole v error")
    small = {k: F(v) for k, v in author["small_positive_prices"].items()}
    need(len(small) == 4 and all(v == F("1e-200") for v in small.values()), "four positive small prices")
    factor = 1+F("1e-80")
    r_raw = factor*(model[0]+sum(prices.values(), F(0))+ev*(model[1]+exi))+sum(small.values(), F(0))
    r = ceilq(r_raw)

    # Original full gradient inequality; no additional old partial price.
    ed = F("0.004356223514")
    need(F(data["total_data_upper"]) < ed == F(author["complete_data_price_once"]), "closed complete data price exactly once")
    alpha = F(prior["reference_corrected_high_norm_upper"])
    need(alpha == F("0.04183918836"), "unchanged S0 price")
    C = F(prior["current_high_multiplier_with_positive_inherited_correction"])
    need(C == F(budget["kappa_exact"])*F(budget["mu_H_upper"])*F(budget["R_rho"])*(1+F(budget["relative_high_correction_upper"])), "original high multiplier")
    s = max(abs(F(x)) for x in budget["scalar_published_safe_enclosure"])
    mass = F(geometry["metric"]["x0_M_lower_x0"])
    q0 = F(budget["GPT1_perpendicular_box_norm_upper"])
    E = F(budget["E_star"])
    high = C*(alpha+r)
    used = ed+high
    energy = s*s/mass + (q0+used)**2
    need(energy < E, "original strict gradient threshold")
    target = F("0.0718188852")
    return encode({
        "status": "PASS_UNDER_H1_H4_AND_INHERITED_PHYSICAL_CONTRACTS_AFTER_EXPLICIT_CORRECTION",
        "scope": "fixed 24-component certificate class only; no positive complement claim",
        "external_review_open": True,
        "new_quadrature_evaluations": 0,
        "originals_changed": False,
        "original_archive_sha256": "0ae5879e0783a88d102def93c5cce3a768e42dbc3c09209bac703822a154515e",
        "original_author_r_upper_not_accepted_unchanged": F(author["r_upper"]),
        "correction_location": "physical_transport.py:21, eV=gamma.sqrt()*eQC/(delta*sqrt(1-rho))",
        "correct_eV_formula": "gamma*eQC/(delta*sqrt(1-rho)) + unchanged Cpre price",
        "gamma_upper": gamma,
        "D12_old": d12_old,
        "D12_GPT1_safe": d12_safe,
        "source_price_factor": source_factor,
        "whole_analytic_envelope_factor": cap_factor,
        "same_signed_estimator_upper": estimates,
        "evaluation_interval_width_sums": widths,
        "corrected_analytic_Gauss_square_errors": [cap_factor**2*x for x in errors],
        "corrected_endstrip_square_prices": [cap_factor**2*x for x in tails],
        "corrected_model_squared_norm_upper": squared,
        "corrected_model_norm_upper": model,
        "corrected_fixed_high_prices": prices,
        "whole_v_error_upper": ev,
        "corrected_v_response_physical_error": exi,
        "corrected_joint_v_price": ev*(model[1]+exi),
        "small_positive_prices": small,
        "positive_relative_high_factor": factor,
        "r_unrounded_rational_upper": r_raw,
        "r_upper": r,
        "sufficient_r_target": target,
        "r_target_margin": target-r,
        "complete_data_price_once": ed,
        "old_partial_price_added_again": False,
        "reference_high_norm_upper": alpha,
        "whole_high_source_energy_upper": (alpha+r)**2,
        "C_H_exact": C,
        "reference_gradient_price": C*alpha,
        "corrected_rest_gradient_price": C*r,
        "total_high_gradient_price": high,
        "total_additional_gradient_norm_price": used,
        "remaining_norm_budget_slack": F(budget["joint_remaining_norm_budget_lower"])-used,
        "scalar_absolute_upper": s,
        "scalar_mass_lower": mass,
        "perpendicular_model_norm_upper": q0,
        "original_rational_energy_upper": energy,
        "E_star": E,
        "strict_energy_slack": E-energy,
        "display_E_upper": ceilq(energy, 18),
        "display_E_star_lower": floorq(E, 18),
        "display_strict_slack_lower": floorq(E-energy, 18),
        "bound_original_input_count": len(bound_files),
    })


if __name__ == "__main__":
    result = calculate()
    output = HERE/"GPT1_FINAL_REVIEW.json"
    if "--write" in sys.argv:
        output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    else:
        need(result == json.loads(output.read_bytes()), "saved exact GPT1 conclusion")
    print(result["status"])
    for key in ["r_upper", "display_E_upper", "display_E_star_lower", "display_strict_slack_lower"]:
        print(key, "=", result[key])
