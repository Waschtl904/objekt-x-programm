"""Bounded whole-rest feasibility: F_up, exact response formula and form floor."""
import argparse
import gzip
import hashlib
import io
import json
import subprocess
import sys
from fractions import Fraction as Q
from pathlib import Path
from types import MappingProxyType, ModuleType
from zipfile import ZipFile
from flint import arb, arb_mat, ctx

HERE = Path(__file__).resolve().parent
BASE = "34aad090a5a05037cae3e783e07c8382fa47f4b6"
VECTOR = "70e8f72ab0cb8ca1ac0d254392384a2040a9d76d04ebf82587c48771e9f34628"
KNEW = "89ded551059d1279c646bc17e3b5ab3e2a7f7a261d1c239ac752b7f0d35467a8"


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def dump(x):
    return (json.dumps(x, indent=2)+"\n").encode()


def snapshot(root, raw):
    need(__debug__, "Do not use python -O")
    spec = json.loads(raw)
    need(spec["source_commit"] == BASE, "Base")
    data = {}
    for alias, entry in spec["files"].items():
        path = (root/entry["path"]).resolve()
        need(path.is_relative_to(root), "Escaping input")
        buf = path.read_bytes()
        need(sha(buf) == entry["sha256"], "Input hash: "+alias)
        data[alias] = buf
    inherited = json.loads(data["source_bindings"])
    for alias in ("common", "inverse_even"):
        e = inherited["members"][alias]
        need(sha(data[e["archive"]]) == inherited["files"][e["archive"]]["sha256"],
             "Archive provenance")
        with ZipFile(io.BytesIO(data[e["archive"]])) as z:
            buf = z.read(e["member"])
        need(sha(buf) == e["sha256"], "Nested input: "+alias)
        data[alias] = buf
    need(sha(data["coherent"]) == inherited["files"]["coherent"]["sha256"], "Old K provenance")
    return MappingProxyType(data)


def js(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def q(v):
    v = Q(v)
    return arb(v.numerator)/v.denominator


def mat(rows):
    return arb_mat([[q(v) for v in row] for row in rows])


def enc(x, digits=80):
    need(x.is_finite(), "Nonfinite interval")
    grid = 10**digits
    lo, hi = Q(str(x.lower().fmpq()))*grid, Q(str(x.upper().fmpq()))*grid
    return [str(Q(lo.numerator//lo.denominator, grid)),
            str(Q(-((-hi.numerator)//hi.denominator), grid))]


def upper_grid(x, digits=24):
    x = Q(x)*10**digits
    return Q(-((-x.numerator)//x.denominator), 10**digits)


def f_upper(data):
    old, eta = js(data["previous_result"]), js(data["eta_result"])
    need(old["test_vector_sha256"] == eta["test_vector_sha256"]
         == sha(data["frozen_vector"]) == VECTOR, "Same frozen vector")
    for key in ("physical_candidate_sha256", "K_P_certificate_sha256", "K_new_sha256"):
        need(old[key] == eta[key], "Inherited identity: "+key)
    need(old["K_new_sha256"] == KNEW and old["budget_interval"] == eta["budget_interval"], "Fixed K/budget")
    need(eta["previous_result_sha256"] == sha(data["previous_result"]), "Eta provenance")
    # If d=(a-a0)w, the previous proof supplies |2<d,Ki a0w>|<=p,
    # ||Ki^(1/2)d||<=e. The upper square needs the positive e^2 term.
    a2 = Q(old["form_a_Ki_model_norm_squared"][1])
    cross = Q(old["form_refinement"]["square_loss_upper"])
    error = Q(old["form_a_Ki_error_norm"][1])
    a_square_up = a2+cross+error**2
    Hlo = Q(old["form_B_model"][0])-Q(old["form_common_D_U_error"][1])-a_square_up-Q(eta["eta_q_interval"][1])
    Fup = Q(old["base_actual_energy_interval"][1])+2*Q(old["pairing_actual_interval"][1])-Hlo
    Flo = Q(eta["inverse_energy_lower"])
    budget_lo = Q(old["budget_interval"][0])
    need(Flo <= Fup, "Ordered full test interval")
    components = {
        "base_interval_width": Q(old["base_actual_energy_interval"][1])-Q(old["base_actual_energy_interval"][0]),
        "twice_pairing_width": 2*(Q(old["pairing_actual_interval"][1])-Q(old["pairing_actual_interval"][0])),
        "B_model_width": Q(old["form_B_model"][1])-Q(old["form_B_model"][0]),
        "twice_common_D_U_form_price": 2*Q(old["form_common_D_U_error"][1]),
        "a_square_enclosure_width": a_square_up-Q(old["actual_a_square_lower"]),
        "eta_q_width": Q(eta["eta_q_interval"][1])-Q(eta["eta_q_interval"][0]),
    }
    need(sum(components.values()) == Fup-Flo, "Complete width accounting")
    return {
        "F_interval": [str(Flo), str(Fup)], "H_form_lower": str(Hlo),
        "a_square_upper": str(a_square_up), "positive_quadratic_error": str(error**2),
        "cross_price": str(cross), "width_components": {k:str(v) for k,v in components.items()},
        "budget_interval": old["budget_interval"],
        "budget_lower_minus_F_upper": str(budget_lo-Fup),
        "positive_rest_upper_affordable": Fup < budget_lo,
        "lower_excludes": Flo > Q(old["budget_interval"][1]),
    }


def matrices(data):
    inv, co, schur, case = js(data["inverse_even"]), js(data["coherent"]), js(data["pilot_schur"]), js(data["common"])["cases"][0]
    need(inv["parity"] == case["parity"] == "even", "Parity")
    knew = schur["K_new_rational"]
    need(sha(json.dumps(knew,separators=(",",":")).encode()) == KNEW, "Frozen K")
    E = [[Q(v) for v in row] for row in inv["E_rational"]]
    D = [[Q(0) for _ in range(203)] for _ in range(203)]
    rho = Q(case["rho"])
    for i in range(191):
        D[i][i] = 1-rho
    for i in range(12):
        for j in range(12):
            D[191+i][191+j] = Q(knew[i][j])
            E[191+i][191+j] += Q(knew[i][j])-Q(co["parities"]["even"]["K_rational"][i][j])
    need(sha(json.dumps([[str(v) for v in row] for row in E],separators=(",",":")).encode())
         == schur["E_new_canonical_rows_sha256"], "Exact E_new identity")
    X = [[Q(v) for v in row] for row in inv["X84x203_rational"]]
    w = [Q(v) for v in js(data["frozen_vector"])["raw_coefficients"]]
    need(len(E)==203 and all(len(r)==203 for r in E), "E dimensions")
    need(len(X)==84 and all(len(r)==203 for r in X) and len(w)==84, "X/w dimensions")
    need(all(E[i][j]==E[j][i] and D[i][j]==D[j][i] for i in range(203) for j in range(203)), "Symmetry")
    return E,D,X,w


def rational_lower(A):
    n = A.nrows()
    # The response Gram has very small positive pivots. Keep 200 digits
    # here; the 80-digit scalar output grid is not a safe matrix grid.
    boxes = [[list(map(Q,enc(A[i,j],200))) for j in range(n)] for i in range(n)]
    need(all(boxes[i][j]==boxes[j][i] for i in range(n) for j in range(n)), "Symmetric enclosure")
    centre = [[(v[0]+v[1])/2 for v in row] for row in boxes]
    diagonal = []
    for i in range(n):
        radius = sum((hi-lo)/2 for lo,hi in boxes[i])
        centre[i][i] -= radius
        diagonal.append(2*radius)
    return centre, diagonal


def auditor(data):
    m = ModuleType("bound_rest_rational_auditor")
    m.__file__ = str(HERE/"bound_rest_rational_auditor.py")
    exec(compile(data["rational_auditor"], "bound_rest_rational_auditor.py", "exec"),
         m.__dict__)
    m.SCALE = 10**300
    return m


def positive(audit, A):
    return audit.positive([[audit.point(v) for v in row] for row in A], True)


def run(data):
    ctx.prec = 1024
    endpoint = f_upper(data)
    print("F_up =", float(Q(endpoint["F_interval"][1])),
          "; budget margin =", float(Q(endpoint["budget_lower_minus_F_upper"])), flush=True)
    E,D,X,w = matrices(data)
    Ea,Da,Xa,wa = mat(E),mat(D),mat(X),mat([[v] for v in w])
    print("Finite E_new solve and response Gram", flush=True)
    # One solve with both right hand sides; no physical operator evaluation.
    rhs = arb_mat([[Xa[j,i] if j<84 else Da[i,j-84] for j in range(287)] for i in range(203)])
    solved = Ea.solve(rhs)
    Y = arb_mat([[solved[i,j] for j in range(84)] for i in range(203)])
    P = Xa*Y
    P = (P+P.transpose())/2
    Plo, Pdelta = rational_lower(P)
    action = P.solve(wa)
    cost = (wa.transpose()*action)[0,0]
    cost_box = enc(cost)
    cost_upper = upper_grid(cost_box[1])+Q(1,10**24)
    z = [Q(str(action[i,0].mid().fmpq())) for i in range(84)]
    # A fixed rational variational witness for the MINIMUM coefficient cost.
    # This certifies that choosing another exact representation cannot rescue
    # the same E-based transport price. It is not a physical test direction.
    cost_lower = 2*sum(w[i]*z[i] for i in range(84))
    cost_lower -= sum(z[i]*Plo[i][j]*z[j] for i in range(84) for j in range(84))
    cost_lower -= sum(Pdelta[i]*z[i]**2 for i in range(84))
    need(0 < cost_lower <= Q(cost_box[1]) <= cost_upper, "Minimum-cost lower/upper")
    trace = sum((solved[i,84+i] for i in range(203)),arb(0))
    trace_box = enc(trace)
    need(Q(trace_box[0])>0, "Positive trace")
    # Rounded upward trace gives a simple conservative epsilon. Its final
    # positivity is checked directly over rationals, independently of Arb.
    trace_ceiling = upper_grid(trace_box[1],0)
    eps = 1/trace_ceiling
    inv = js(data["inverse_even"])
    prior = js(data["pilot_result"])
    beta,c = Q(inv["beta"]),Q(prior["residual_cap"])
    need(c==Q(1977,500000) and beta==Q(prior["beta"])>0, "Inherited full residual constants")
    kappa = (1-c)*eps
    residual_price = c*beta*cost_upper
    residual_target = kappa*beta*Q(endpoint["budget_lower_minus_F_upper"])
    print("Minimum E cost interval:", [float(Q(v)) for v in cost_box],
          "; epsilon:", float(eps), "; Ru price:", float(residual_price), flush=True)
    audit = auditor(data)
    rank_block = [row+[w[i]] for i,row in enumerate(Plo)]+[w+[cost_upper]]
    print("Independent rational response-rank/transport and floor audits", flush=True)
    rank = positive(audit,rank_block)
    floor = positive(audit,[[E[i][j]-eps*D[i][j] for j in range(203)] for i in range(203)])
    finite = {
        "P_lower_rational": [[str(v) for v in row] for row in Plo],
        "P_lower_to_upper_diagonal": list(map(str,Pdelta)),
        "cost_lower_dual_test": list(map(str,z)),
        "arb_minimum_E_cost_interval": cost_box,
        "minimum_E_cost_interval": [str(cost_lower),str(cost_upper)],
        "minimum_E_cost_upper": str(cost_upper),
        "trace_Einv_D_interval": trace_box,
        "epsilon": str(eps), "kappa": str(kappa),
        "rank_and_cost_positive_block": rank, "form_floor_positive_block": floor,
    }
    result = {
        "status":"AUTHOR_DERIVED", "review_status":"EXTERNAL_REVIEW_OPEN",
        "source_commit":BASE, "outcome":("UPPER_CONTROL_ROUTE_TOO_COARSE"
            if not endpoint["positive_rest_upper_affordable"] else "REST_DATA_REQUIRED"),
        "test_vector_sha256":VECTOR, "K_new_sha256":KNEW, **endpoint,
        "response_rank":84, "exact_response_formula":"u = E_new^-1 X_ans* (X_ans E_new^-1 X_ans*)^-1 w",
        "exact_identity":"X_ans u = w", "representation_is_E_minimal":True,
        "minimum_E_cost_interval":[str(cost_lower),str(cost_upper)], "minimum_E_cost_upper":str(cost_upper),
        "full_Ru_Ldual_energy_upper":str(residual_price),
        "minimum_E_transport_bound_expression_lower":str(c*beta*cost_lower),
        "actual_Ru_lower_claimed":False,
        "epsilon":str(eps), "kappa":str(kappa), "beta":str(beta), "c":str(c),
        "required_full_residual_Ldual_energy_upper":str(residual_target),
        "transport_only_inverse_energy_price_upper":str(residual_price/(kappa*beta)),
        "complete_residual":"nu_new + A*(D_new^-1 A Jw-u) + R u",
        "missing_joint_data":["complete L-dual Gram of nu_new, A* and R at the fixed transported coefficients",
                              "mixed L-dual pairings preserving cancellation among all three terms",
                              "common source/model-error transport for the whole residual; 84 coordinates alone do not suffice"],
        "full_residual_energy_computed":False, "full_inverse_upper_computed":False,
        "underform_excluded":False, "partial_pass":False, "dual_reserve":None,
        "new_integration":False, "new_physical_direction":False,
        "N12_closed":False, "milestone_4_closed":False,
    }
    return result,finite


def package():
    m = js((HERE/"MANIFEST.json").read_bytes())
    out = {}
    for name, expected in m.items():
        path = (HERE/name).resolve()
        need(path.is_relative_to(HERE),"Escaping package")
        raw = path.read_bytes()
        need(sha(raw)==expected,"Package hash: "+name)
        out[name]=raw
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repository",type=Path,default=HERE.parents[2])
    ap.add_argument("--output-dir",type=Path)
    ap.add_argument("--check",action="store_true")
    ap.add_argument("--worker",action="store_true",help=argparse.SUPPRESS)
    args=ap.parse_args()
    need(__debug__,"Do not use python -O")
    if not args.worker:
        subprocess.run([sys.executable,"-B",str(HERE/"verify.py"),*sys.argv[1:],"--worker"],
                       check=True,timeout=600)
        return
    checked=package() if args.check else {}
    data=snapshot(args.repository.resolve(),checked.get("INPUT_BINDINGS.json") or (HERE/"INPUT_BINDINGS.json").read_bytes())
    result,finite=run(data)
    for name,value in (("RESULT.json",result),("FINITE.json",finite)):
        raw=dump(value)
        if args.check:need(raw==checked[name],"Byte replay: "+name)
        if args.output_dir:
            args.output_dir.mkdir(parents=True,exist_ok=True)
            (args.output_dir/name).write_bytes(raw)
    print("PASS:",result["outcome"])


if __name__=="__main__":
    main()
