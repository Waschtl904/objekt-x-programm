"""Finite variational lower bound for the full dualterm, same #246 witness."""
import argparse
import gzip
import hashlib
import json
import subprocess
import sys
import time
from fractions import Fraction as Q
from pathlib import Path
from types import ModuleType
from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
BASE = "93cf629d5efdbf93d6a3cfef8cb849134f1f72ff"
OUTPUTS = ("L_UPPER.json", "EXPECTED.json")


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


def run(root, binding_bytes):
    need(__debug__, "Do not use python -O")
    spec = json.loads(binding_bytes)
    need(spec["source_commit"] == BASE, "Frozen #246 head")
    data = {}
    for key, item in spec["files"].items():
        path = (root/item["path"]).resolve()
        need(path.is_relative_to(root), "Escaping input")
        raw = path.read_bytes()
        need(sha(raw) == item["sha256"], "Input binding: "+key)
        data[key] = raw
    pilot = module("bound_pilot", data["pilot_verify"], root/spec["files"]["pilot_verify"]["path"])
    c, inp, old, oldspec = pilot.snapshot(root, data["pilot_inputs"])
    prior = json.loads(data["pilot_result"])
    schur = json.loads(data["pilot_schur"])
    pilot_audit = module("bound_pilot_audit", data["pilot_audit"], root/spec["files"]["pilot_audit"]["path"])
    pilot_audit.check(prior, data["pilot_schur"])
    need(prior["outcome"] == "PILOT_PARTIAL_PASS", "Inherited partial pass")
    ctx.prec = 1024
    half = inp.json("half")["blocks"][0]
    D = [[Q(x) for x in row] for row in inp.json("basis_even")["D_rational"]]
    S = [[Q(x) for x in row] for row in half["half_inverse_centre_rational_Q_coefficients"]]
    need(len(D) == 8 and all(len(row) == 84 for row in D), "Basis dimensions")
    need(len(S) == 92 and all(len(row) == 8 for row in S), "Constraint dimensions")
    for i in range(8):
        for j in range(84):
            need(sum(S[k][i]*D[k][j] for k in range(8))+S[8+j][i] == 0,
                 "Exact T constraint")
    Z = D+[[Q(int(i == j)) for j in range(84)] for i in range(84)]
    zr = c.ratmat(Z)
    J = c.mat(half["basis_Q_local_coefficients"])*zr
    need(J.nrows() == 96 and J.ncols() == 84, "Local J basis")
    gram = [[sum(Z[k][i]*Z[k][j] for k in range(92)) for j in range(84)] for i in range(84)]
    need(1+sum(x*x for row in D for x in row) < Q(1000502,10**6), "Bound J Hilbert norm")
    harmonic = Q(0)
    d = []
    for n in range(96):
        if n:
            harmonic += Q(1,n)
        d.append(harmonic+Q(11,10))
    EL = J.transpose()*arb_mat([[c.q(d[i])*J[i,j] for j in range(84)] for i in range(96)])
    EL = (EL+EL.transpose())/2
    upper = pilot.rational_upper(EL)
    lower = [[-Q(x) for x in row] for row in pilot.rational_upper(-EL)]
    auditor = module("bound_integer_auditor", old["rational_auditor"],
                     root/oldspec["files"]["rational_auditor"]["path"])
    floor = [[auditor.point(lower[i][j]-Q(21,5)*gram[i][j]) for j in range(84)] for i in range(84)]
    pivots = auditor.positive(floor, False)
    need(pivots["positive_pivots"] == 84, "Complete L floor audit")
    metric = c.ratmat(upper).inv()
    need(all(metric[i,j].is_finite() for i in range(84) for j in range(84)), "L upper inverse")
    module("pilot_weights", old["pilot_weights"], root/oldspec["files"]["pilot_weights"]["path"])
    assembler = module("pilot_energy", old["pilot_energy"], root/oldspec["files"]["pilot_energy"]["path"])
    pairs = json.loads(gzip.decompress(old["pairs_even"]))
    pairs["_source_sha256"] = sha(old["pairs_even"])
    # Only positive-matrix feature/error formulas are reused. This metric is
    # NOT claimed to majorize X_ans E_new^-1 X_ans*.
    energy = assembler.Energy(inp, pairs, c.ratmat(schur["K_new_rational"]), metric, c.q(1))
    candidate = json.loads(old["candidate_even"])
    kp = json.loads(old["kp_even"])
    need(sha(old["candidate_even"]) == prior["candidate_sha256"], "Physical witness changed")
    need(sha(old["kp_even"]) == prior["K_P_certificate_sha256"], "Budget changed")
    cert = energy.certificate(candidate["raw_coefficients"], kp["K_P_interval"], "fixed_finite_dual_feature")
    coeff = arb_mat([[c.q(x)] for x in candidate["raw_coefficients"]])/cert["normalization"]
    nu = energy.nu*coeff
    previous_nu = c.mat(prior["nu_new_direction"])
    need(all(nu[i,0].overlaps(previous_nu[i,0]) for i in range(84)), "Same composed nu")
    model = cert["component_model_energies"]["P_upper_J_star_nu"]
    ef = cert["feature_error_norms"]["P_upper_J_star_nu"]
    er = cert["residual_model_error_norm"]
    need(model.lower() > 0 and ef >= 0 and er >= 0, "Feature and error positivity")
    lo = max(arb(0), model.lower().sqrt()-ef.upper()-er.upper())**2
    hi = (model.upper().sqrt()+ef.upper()+er.upper())**2
    auxiliary_interval = [c.enc(lo)[0], c.enc(hi)[1]]
    dual_lower = Q(auxiliary_interval[0])
    e_partial = Q(prior["partial_actual_energy_interval"][0])
    b_hi = Q(kp["K_P_interval"][1])
    a, beta = Q(prior["a_weight"]), Q(prior["beta"])
    weight = a/beta
    full_lower = e_partial+weight*dual_lower
    excluded = full_lower > b_hi
    matrix = {
        "L_upper_rational":upper,
        "definition":"L[J,J] <= L_upper; M = L_upper^-1 <= (L[J,J])^-1",
        "basis":"J = Q (D; I_84), exact T constraints in W_X",
        "exact_null_equations":672,"full_L_lower_minus_21_over_5_WJ_audit":pivots,
        "L_lower_canonical_sha256":sha(json.dumps([[str(x) for x in row] for row in lower],separators=(",",":")).encode()),
        "strict_rounding_pad":"1e-40","precision_bits":1024
    }
    matrix_bytes = (json.dumps(matrix,indent=2)+"\n").encode()
    result = c.encode({
        "status":"AUTHOR_DERIVED","review_status":"EXTERNAL_REVIEW_OPEN",
        "source_commit":BASE,"parity":"even",
        "outcome":"FULL_FIXED_COMPARISON_EXCLUDED_BY_DUAL_LOWER" if excluded else "DUAL_PREFLIGHT_OPEN",
        "scope":"The full selected W_new comparison with fixed #246 weights, response, witness and budget",
        "finite_auxiliary_model_energy":model,"finite_feature_norm_error":ef,
        "whole_residual_norm_error_in_auxiliary_bound":er,
        "a_fin_common_feature_error":cert["a_fin_common_error_contribution"],
        "auxiliary_finite_energy_interval":auxiliary_interval,
        "full_dual_energy_lower":str(dual_lower),"full_dual_energy_upper":None,
        "inherited_partial_energy_interval":prior["partial_actual_energy_interval"],
        "budget_interval":kp["K_P_interval"],"dual_weight":str(weight),
        "full_comparison_energy_lower":str(full_lower),"full_comparison_energy_upper":None,
        "full_lower_minus_budget_upper":str(full_lower-b_hi),
        "dual_lower_sufficient_for_exclusion":str((b_hi-e_partial)/weight),
        "inherited_dual_upper_sufficient_for_pass":prior["sufficient_actual_dual_energy_upper"],
        "L_UPPER_sha256":sha(matrix_bytes),"L_floor_audit":pivots,
        "candidate_sha256":sha(old["candidate_even"]),"K_P_sha256":sha(old["kp_even"]),
        "K_new_canonical_sha256":prior["K_new_canonical_sha256"],
        "auxiliary_positive_weight_bounds":energy.bounds,
        "common_residual_Hilbert_errors":energy.residual_errors,
        "controls":energy.controls,"exact_null_equations":672,
        "common_FJ_errors_retained":True,"whole_residual_error_included":True,
        "partial_certificate_changed":False,"physical_witness_changed":False,
        "answer_matrix_changed":False,"comparison_weights_changed":False,
        "new_integrations":False,"infinite_tail_computed":False,
        "full_dual_enclosure_claimed":False,"actual_A9_inverse_excluded":False,
        "all_majorants_of_new_lower_form_excluded":False,
        "milestone_4_closed":False,"N12_closed":False
    })
    print(result["outcome"],flush=True)
    return {"L_UPPER.json":matrix_bytes,"EXPECTED.json":(json.dumps(result,indent=2)+"\n").encode()}


def worker(args):
    checked = {}
    if args.check:
        for name, digest in json.loads((HERE/"MANIFEST.json").read_bytes()).items():
            path=(HERE/name).resolve()
            need(path.is_relative_to(HERE),"Escaping manifest")
            raw=path.read_bytes();need(sha(raw)==digest,"Package binding: "+name)
            checked[name]=raw
    else:
        checked["INPUT_BINDINGS.json"]=(HERE/"INPUT_BINDINGS.json").read_bytes()
    out=run((args.repository or HERE.parents[2]).resolve(),checked["INPUT_BINDINGS.json"])
    if args.check:
        for name,raw in out.items():need(raw==checked[name],"Replay differs: "+name)
        print("PASS: both dual-preflight result files byte-equal",flush=True)
    if args.output_dir:
        args.output_dir.mkdir(parents=True,exist_ok=True)
        for name,raw in out.items():(args.output_dir/name).write_bytes(raw)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--check",action="store_true")
    ap.add_argument("--output-dir",type=Path)
    ap.add_argument("--repository",type=Path)
    ap.add_argument("--worker",action="store_true",help=argparse.SUPPRESS)
    args=ap.parse_args()
    need(__debug__,"Do not use python -O")
    need(args.check or args.output_dir,"Choose check or output")
    if args.worker:
        worker(args)
        return
    start=time.monotonic()
    try:
        done=subprocess.run([sys.executable,"-u","-B",str(HERE/"verify.py"),*sys.argv[1:],"--worker"],timeout=300)
    except subprocess.TimeoutExpired:
        print("DUAL_PREFLIGHT_TECHNICAL_TIMEOUT: no mathematical decision",flush=True)
        raise SystemExit(124)
    print("Complete elapsed seconds:",round(time.monotonic()-start,3),flush=True)
    raise SystemExit(done.returncode)


if __name__=="__main__":
    main()
