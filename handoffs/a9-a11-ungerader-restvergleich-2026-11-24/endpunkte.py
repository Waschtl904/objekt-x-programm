"""Check the published comparison endpoints using only the Python standard library."""
import json
from fractions import Fraction as Q
from pathlib import Path


def verify(condition, message):
    if not condition:
        raise ValueError(message)


base = Path(__file__).resolve().parent
result = json.loads((base / "ERGEBNIS.json").read_bytes())
lo, hi = map(Q, result["F"])
budget = Q(result["K_P"][0])
z = Q(result["residual_P_norm_upper"])
c, beta, d = map(Q, (result["c"], result["beta"], result["sufficient_d"]))
upper = Q(result["conditional_full_upper"])
verify(0 < lo <= hi < budget and budget-hi > Q("7.40397e-8"), "F interval")
verify(0 <= z < Q("8.558e-8") and 0 < c < 1 and beta > 0, "finite feature")
verify(d == Q("8.1e-9"), "whole residual target")
x = d/beta
# Square only after checking the two sides are nonnegative.
room = (upper-hi)*(1-c) - x - z*z
verify(room >= 0 and room*room >= 4*c*x*z*z, "conditional energy inequality")
verify(upper < Q("5.280273126e-6") and budget-upper > Q("5.03309e-10"), "headroom")
verify(result["actual_whole_residual_certified"] is False, "open whole residual")
old = json.loads((base / "vorpruefung/ERGEBNIS.json").read_bytes())
verify(Q(old["full_RL_energy_lower"]) > Q("1.8952384e-8"), "old dual lower")
verify(Q(old["family_margin_lower"]) > Q("5.07762e-8"), "old family exclusion")
print("PASS: finite endpoints, previous obstruction and conditional comparison.")
print("OPEN: the actual whole odd residual energy.")
