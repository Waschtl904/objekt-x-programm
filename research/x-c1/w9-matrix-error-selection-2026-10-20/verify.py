"""One matrix-error K candidate: admissibility and model selection, not energy certification."""
import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import ModuleType

from flint import arb_mat, ctx

HERE = Path(__file__).resolve().parent
EPSILON = Q(14401070947262324376501, 10**40)
B_WEIGHT = Q(51, 50)
RESIDUAL_CAP = Q(1977, 500000)
A_WEIGHT = (B_WEIGHT - 1) / (B_WEIGHT * (1 - RESIDUAL_CAP) - 1)
BASE = "2e8e86770c0fde6ef5ea69b0178775eab34d5de4"


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def module(name, raw, path):
    value = ModuleType(name)
    value.__file__ = str(path)
    sys.modules[name] = value
    exec(compile(raw, str(path), "exec"), value.__dict__)
    return value


def rational_lower(matrix):
    """Enclose each symmetric entry on 10^-80, subtract row radii and 10^-60 I."""
    n = matrix.nrows()
    scale = 10**80
    bounds = []
    for i in range(n):
        row = []
        for j in range(n):
            x = (matrix[i, j] + matrix[j, i]) / 2
            need(x.is_finite(), "Nonfinite candidate entry")
            lo, hi = Q(str(x.lower().fmpq()))*scale, Q(str(x.upper().fmpq()))*scale
            row.append((Q(lo.numerator // lo.denominator, scale),
                        Q(-((-hi.numerator) // hi.denominator), scale)))
        bounds.append(row)
    center = [[(lo+hi)/2 for lo, hi in row] for row in bounds]
    radii = [sum((hi-lo)/2 for lo, hi in row) for row in bounds]
    need(all(center[i][j] == center[j][i] for i in range(n) for j in range(n)), "Symmetry")
    lower = [row[:] for row in center]
    for i in range(n):
        lower[i][i] -= radii[i] + Q(1, 10**60)
    return [[str(x) for x in row] for row in lower], [
        [[str(lo), str(hi)] for lo, hi in row] for row in bounds]


def run(root, binding_bytes, audit):
    need(__debug__, "Do not use python -O")
    spec = json.loads(binding_bytes)
    need(spec["source_commit"] == BASE, "Wrong integration base")
    data = {}
    for name, item in spec["files"].items():
        path = (root / item["path"]).resolve()
        need(path.is_relative_to(root), "Escaping bound input")
        raw = path.read_bytes()
        need(sha(raw) == item["sha256"], "Input binding: " + name)
        data[name] = raw
    previous = module("bound_variational_selection", data["engine"],
                      root / spec["files"]["engine"]["path"])
    env = previous.load(root, data["bindings"])
    c, inp = env["common"], env["inp"]
    ctx.prec = 1024
    source = inp.json("common")["cases"][0]
    need(source["parity"] == "even", "Only fixed even witness")
    co = inp.json("coherent")["parities"]["even"]

    def block(A):
        return arb_mat([[A[i,j] for j in range(12)] for i in range(12)])

    U = block(c.mat(source["U96_model"]))
    EF = c.mat(source["finite_feature_error_gram"])
    DL = block(c.mat(source["D96_lower_model"]))
    GF = c.ratmat([row[:12] for row in source["G96_rational"][:12]])
    K = c.ratmat(co["K_rational"])
    ks_rows = [[str(Q(co["K_rational"][i][j]) + Q(13,10**8)*Q(source["G96_rational"][i][j]))
                for j in range(12)] for i in range(12)]
    Ks = c.ratmat(ks_rows)
    need(all(Ks[i,j].overlaps(env["energy"].w["K"][i,j]) for i in range(12) for j in range(12)),
         "Inherited K-star mismatch")
    # E_F bounds all F-source feature errors; no F-J error is changed.
    ceiling = DL - (1+c.q(EPSILON))*U - c.q(1+1/EPSILON)*EF
    rows, enclosure = rational_lower(ceiling)
    Kn = c.ratmat(rows)
    # Exact rational checks independent of all floating point operations.
    audit.admissibility(rows, ks_rows, enclosure)
    audit.controls()
    e2, tau = c.trace(GF.inv()*EF), c.trace(GF.inv()*U)
    need(e2 > 0 and tau > 0, "Feature trace positivity")
    trace_price = c.q(EPSILON)*tau + c.q(1+1/EPSILON)*e2
    need(trace_price < c.q(Q(38072933,125000000000000)), "Old scalar envelope comparison")

    # Only a model diagnostic: common physical F-J/model errors NOT paid here.
    energy, coeff = env["energy"], env["c"]
    a, Ki = energy.w["a"], Kn.inv()
    v = energy.v * coeff
    nu = env["nu"] + a.transpose()*(energy.w["Ki"]-Ki)*v
    base = previous.quad(energy.components["high_U8"]+energy.components["finite_U8"], coeff) + previous.quad(Ki, v)
    H = env["BJJ"] - a.transpose()*Ki*a
    Hmid = previous.midpoint_matrix((H+H.transpose())/2)
    nmid = previous.midpoint_matrix(nu)
    t = Hmid.solve(nmid)
    restricted = base + 2*(t.transpose()*nu)[0,0] - previous.quad(H,t)
    inv = inp.json("inverse_even")
    receipt = json.loads(data["closure_acceptance"])["reserve_review"]["independent_rational_review"]
    need(receipt["source_zip_sha256"] == "65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba",
         "Full residual source binding")
    cap = next(row for row in receipt["cases"] if row["parity"] == "even")
    need(Q(cap["new_simple_cap"]) == RESIDUAL_CAP and
         Q(cap["new_complete_QR_upper"]) < RESIDUAL_CAP < Q(inv["residual_cap"]),
         "Inherited full residual cap")
    need(Q(cap["beta"]) == Q(inv["beta"]), "Inherited beta")
    E = c.ratmat(inv["E_rational"])
    for i in range(12):
        for j in range(12):
            E[191+i,191+j] += Kn[i,j] - K[i,j]
    X = c.ratmat(inv["X84x203_rational"])
    P = X * E.solve(X.transpose())
    pterm = previous.quad(P, nu)
    partial_old_weight = base + c.q(Q(1,1)/(1-11*RESIDUAL_CAP))*pterm
    partial = base + c.q(B_WEIGHT)*pterm
    budget = c.box(env["kp"]["K_P_interval"])
    model_margin = budget-partial
    need(model_margin > 0, "Chosen model candidate has no positive model margin")
    return c.encode({
        "status": "AUTHOR_DERIVED", "review_status": "EXTERNAL_REVIEW_OPEN",
        "outcome": "MATRIX_ERROR_K_CANDIDATE_SELECTED_ENERGY_CERTIFICATION_OPEN",
        "source_commit": BASE, "parity": "even",
        "changed_exclusion_premise": "K_new > K_star; new lower form, same outer answer and witness",
        "epsilon": str(EPSILON), "K_new_rational": rows, "K_star_rational": ks_rows,
        "K_ceiling_enclosure": enclosure,
        "K_new_canonical_sha256": sha(json.dumps(rows,separators=(",",":")).encode()),
        "rational_positive_pivots": {"K_new_minus_K_star": 12, "rounding_margin": 12},
        "feature_trace_price": trace_price, "finite_error_metric_trace": e2,
        "finite_model_metric_trace": tau, "relative_increment_trace": c.trace(Ks.inv()*(Kn-Ks)),
        "weights": {"a": str(A_WEIGHT), "b": str(B_WEIGHT), "c": str(RESIDUAL_CAP),
                    "beta": inv["beta"], "dual_coefficient": str(A_WEIGHT/Q(inv["beta"]))},
        "model_only": {"base": base, "P_energy_unweighted": pterm,
                       "partial_old_weight": partial_old_weight, "partial_selected_weight": partial,
                       "restricted_variational_expression": restricted, "budget": budget,
                       "margin_before_additional_errors_and_dual": model_margin,
                       "dual_ceiling_if_all_other_errors_were_zero": model_margin*c.q(Q(inv["beta"])/A_WEIGHT)},
        "physical_candidate_sha256": sha(env["data"]["candidate_even"]),
        "budget_sha256": sha(env["data"]["kp_even"]),
        "P_model_computed": True, "P_upper_certified": False,
        "new_directed_partial_energy_computed": False, "new_integrations": False,
        "RL_computed": False, "frozen_outer_response_changed": False, "F_J_errors_reduced": False,
        "partial_pass": False, "certified_dual_reserve": None,
        "milestone_4_closed": False, "N12_closed": False,
        "warning": "Model interval arithmetic only; physical model/feature/whole-residual errors and the full dualterm are not included in model_only."
    })


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repository", type=Path, default=HERE.parents[2])
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    need(__debug__, "Do not use python -O")
    need(args.check or args.output, "Use --check or --output")
    checked = {}
    if args.check:
        for name, digest in json.loads((HERE/"MANIFEST.json").read_bytes()).items():
            path = (HERE/name).resolve()
            need(path.is_relative_to(HERE), "Escaping manifest path")
            raw = path.read_bytes()
            need(sha(raw) == digest, "Package binding: "+name)
            checked[name] = raw
    else:
        for name in ("audit.py", "INPUT_BINDINGS.json"):
            checked[name] = (HERE/name).read_bytes()
    audit = module("bound_matrix_error_audit", checked["audit.py"], HERE/"audit.py")
    result = run(args.repository.resolve(), checked["INPUT_BINDINGS.json"], audit)
    audit.check(result)
    raw = (json.dumps(result, indent=2)+"\n").encode()
    if args.check:
        need(raw == checked["EXPECTED.json"], "Selection replay differs")
        print("PASS: selected candidate byte-equal; 24 rational pivots; no new energy certificate")
    if args.output:
        args.output.write_bytes(raw)


if __name__ == "__main__":
    main()
