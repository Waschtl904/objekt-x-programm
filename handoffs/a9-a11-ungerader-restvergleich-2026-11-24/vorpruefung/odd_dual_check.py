"""Odd frozen #238 witness. Usage: python odd_dual_check.py PATH_TO_REPOSITORY.

Requires python-flint 0.9.0. No new quadrature. The four-feature assembler is
used with a positive auxiliary metric only to price errors in J*nu. The actual
comparison uses the directed #238 partial energies and the exact old K.
"""
import hashlib
import json
import sys
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

from flint import arb, arb_mat, ctx

ROOT = Path(sys.argv[1]).resolve()
PACKAGE = ROOT / "research/x-c1/w9-partial-energy-2026-10-18"
BLOBS = {
    "common.py": "1a88b1d72daa3fe6aeccee0449ecc6998c466a6f",
    "weights.py": "adc250e1a3cf0d842fea94806fdb6bfa5e3a6f95",
    "assemble.py": "aeadc048c4928bf739c70a1cbf49b8651cf73544",
    "INPUT_BINDINGS.json": "a57030f51a827598cc41b923b8cfd23410cfd0b2",
    "expected/CANDIDATE_odd.json": "4e21fad9f0569fe1738e328e620f4da4075b7e76",
    "expected/K_P_odd.json": "76783a37e42c933701c2118dbb3d88a3de10b922",
    "expected/COMPARISON_odd.json": "f1b97ac47f4be56f527d90b64e41836b45a25c71",
    "../w9-majorant-preflight-2026-10-18/EXPECTED.json": "f33aa356795b9280387aa00a80dacacefdaff29a"
}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def read(name):
    return (PACKAGE / name).read_bytes()

for name, sha in BLOBS.items():
    raw = read(name)
    git_header = b"blob " + str(len(raw)).encode() + b"\0"
    require(hashlib.sha1(git_header + raw).hexdigest() == sha, "Git object: " + name)

sys.path.insert(0, str(PACKAGE))
from common import Inputs, enc, mat, q, ratmat
from assemble import Energy, load_pairs

ctx.prec = 1024
inputs = Inputs()
half = inputs.json("half")["blocks"][1]
D = [[Fraction(x) for x in row] for row in inputs.json("basis_odd")["D_rational"]]
S = [[Fraction(x) for x in row] for row in half["half_inverse_centre_rational_Q_coefficients"]]
require(len(D) == 8 and all(len(row) == 84 for row in D), "odd D dimensions")
require(len(S) == 92 and all(len(row) == 8 for row in S), "odd T dimensions")
for j in range(84):
    for i in range(8):
        require(sum(S[k][i]*D[k][j] for k in range(8)) + S[8+j][i] == 0, "odd T constraint")
Z = D + [[Fraction(i == j) for j in range(84)] for i in range(84)]
J = mat(half["basis_Q_local_coefficients"]) * ratmat(Z)
require((J.nrows(), J.ncols()) == (96, 84), "odd J dimensions")

weights = []
harmonic = Fraction(0)
for n in range(96):
    if n:
        harmonic += Fraction(1, n)
    weights.append(q(harmonic + Fraction(11, 10)))
LJ = J.transpose() * arb_mat([[weights[i]*J[i,j] for j in range(84)] for i in range(96)])
row_bounds = [sum(abs(LJ[i,j]).upper() for j in range(84)) for i in range(84)]
row_cap = max(row_bounds)
upper = 1
while not all(bound < upper for bound in row_bounds):
    upper *= 2
# L[J,J] <= upper I. Use M=I/upper to obtain a valid finite variational lower bound.
# The #238 assembler includes 11/10 in its fourth component, so set P=10/(11*upper) I.
aux_weight = Fraction(10, 11*upper)
class AuxiliaryInputs:
    def json(self, alias):
        original = inputs.json(alias)
        if alias == "inverse_odd":
            original["P_upper_rational"] = [[str(aux_weight) if i == j else "0"
                                              for j in range(84)] for i in range(84)]
        return original

candidate = json.loads(read("expected/CANDIDATE_odd.json"))
kp = json.loads(read("expected/K_P_odd.json"))
original = json.loads(read("expected/COMPARISON_odd.json"))
pilot = json.loads(read("../w9-majorant-preflight-2026-10-18/EXPECTED.json"))["parities"]["odd"]
pairs = load_pairs(PACKAGE / "expected/PAIRS_odd.json.gz")
require(candidate["pairs_sha256"] == original["pairs_sha256"] == pairs["_source_sha256"], "odd pairings")
require(pairs["parity"] == candidate["parity"] == kp["parity"] == "odd", "parity")
require(digest(read("expected/CANDIDATE_odd.json")) == kp["candidate_sha256"] ==
        original["candidate_sha256"] == pilot["candidate_sha256"], "witness")
require(digest(read("expected/K_P_odd.json")) == original["K_P_certificate_sha256"], "budget")
require(kp["raw_coefficients"] == candidate["raw_coefficients"], "fixed coefficients")

energy = Energy(AuxiliaryInputs(), pairs)
cert = energy.certificate(candidate["raw_coefficients"], kp["K_P_interval"], "odd_auxiliary_84")
key = "P_upper_J_star_nu"
model = cert["component_model_energies"][key]
feature_error = cert["feature_error_norms"][key]
whole_error = cert["residual_model_error_norm"]
require(model.lower() > 0 and feature_error >= 0 and whole_error >= 0, "feature intervals")
low_norm = max(arb(0), model.lower().sqrt() - feature_error.upper() - whole_error.upper())
dual_lo = Fraction(enc(low_norm**2)[0])
coeff = arb_mat([[q(value)] for value in candidate["raw_coefficients"]]) / cert["normalization"]
n_model = energy.nu * coeff
model_check = sum(n_model[i, 0]**2 for i in range(84)) / upper
require(model.overlaps(model_check), "independent matrix-vector contraction")
v = pilot["variants"]["P_51_50_dual_trade"]
partial_lo = Fraction(v["partial_actual_energy_interval"][0])
budget_hi = Fraction(v["K_P_interval_unchanged"][1])
weight = Fraction(v["coefficient_before_RL"])
full_lo = partial_lo + weight*dual_lo
# Wider claim: every admissible scalar Young pair for the original odd K has a,b >= 1/(1-c).
# Use the known partial energy at b0=51/50; C+b B+(a/beta)D >= t*(E_partial(b0)/b0+D/beta).
t = 1/(1-Fraction(pilot["full_residual_cap"]))
b0 = Fraction(v["P_weight"])
require(1 <= t <= b0, "family estimate")
family_lo = t*(partial_lo/b0 + dual_lo/Fraction(pilot["beta"]))
# Even allowing the simpler necessary bounds a,b >= 1 gives a useful margin.
unit_lo = partial_lo/b0 + dual_lo/Fraction(pilot["beta"])
require(full_lo-budget_hi > Fraction("2.10267e-7"), "fixed trade margin")
require(family_lo-budget_hi > Fraction("5.07762e-8"), "documented family margin")
require(unit_lo > budget_hi, "lower envelope at a=b=1")
def number(x):
    with localcontext() as context:
        context.prec = 18
        return str(Decimal(x.numerator)/Decimal(x.denominator))
for name, value in [("bound for L[J,J]", str(upper)), ("max interval row sum", str(row_cap)),
                    ("model auxiliary energy", str(model)), ("aux feature norm error", str(feature_error)),
                    ("aux residual norm error", str(whole_error)), ("full dual lower", number(dual_lo)),
                    ("trade energy lower", number(full_lo)), ("budget upper", number(budget_hi)),
                    ("trade lower minus budget", number(full_lo-budget_hi)),
                    ("family lower minus budget", number(family_lo-budget_hi)),
                    ("unit lower minus budget", number(unit_lo-budget_hi))]:
    print(name, value)
print("trade excluded:", full_lo > budget_hi, "scalar family excluded:", family_lo > budget_hi)
if len(sys.argv) == 3:
    # Directed rational endpoints are authoritative. Decimal console text is for reading.
    result = {
        "source_commit": "18dd92f89f889c1f506673fefee33e4544b22038",
        "parity": "odd", "precision_bits": ctx.prec,
        "candidate_sha256": original["candidate_sha256"], "pairings_sha256": original["pairs_sha256"],
        "K_P_certificate_sha256": original["K_P_certificate_sha256"],
        "verified_T_constraints": 8*84, "auxiliary_denominator": upper,
        "LJ_max_row_upper": enc(max(bound.upper() for bound in row_bounds))[1],
        "LJ_upper_verified_for_every_row": all(bound < upper for bound in row_bounds),
        "auxiliary_model_energy": enc(model), "aux_feature_norm_error_upper": enc(feature_error)[1],
        "aux_residual_norm_error_upper": enc(whole_error)[1],
        "full_RL_energy_lower": str(dual_lo), "partial_lower_at_b0": str(partial_lo),
        "beta": pilot["beta"], "a_trade": v["dual_weight"], "b0": str(b0),
        "t_family": str(t), "K_P_upper": str(budget_hi), "trade_energy_lower": str(full_lo),
        "trade_margin_lower": str(full_lo-budget_hi), "family_energy_lower": str(family_lo),
        "family_margin_lower": str(family_lo-budget_hi), "unit_energy_lower": str(unit_lo),
        "unit_margin_lower": str(unit_lo-budget_hi),
    }
    Path(sys.argv[2]).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
