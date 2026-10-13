"""Exact rational follow-up checks; no source integrals or full tail proof.

Run after the supplied reproduce.py, which materializes its inherited inputs.
Only the standard library is required. Synthetic matrix checks are labelled.
"""
from fractions import Fraction as Q
from math import isqrt
from pathlib import Path
import argparse
import hashlib
import json


class I:
    def __init__(self, a, b=None):
        self.a, self.b = Q(a), Q(a if b is None else b)
        assert self.a <= self.b

    @staticmethod
    def box(x):
        return I(*x)

    def __add__(self, other):
        other = other if isinstance(other, I) else I(other)
        return I(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.b, -self.a)

    def __sub__(self, other):
        return self + -(other if isinstance(other, I) else I(other))

    def __mul__(self, other):
        other = other if isinstance(other, I) else I(other)
        v = [a*b for a in (self.a, self.b) for b in (other.a, other.b)]
        return I(min(v), max(v))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = other if isinstance(other, I) else I(other)
        assert other.a > 0
        return self * I(1/other.b, 1/other.a)

    def sqrt(self):
        assert self.a >= 0
        scale = 10**100
        def floorroot(x):
            n = isqrt(x.numerator*scale*scale//x.denominator)
            assert Q(n, scale)**2 <= x < Q(n+1, scale)**2
            return n
        return I(Q(floorroot(self.a), scale), Q(floorroot(self.b)+1, scale))

    def square(self):
        if self.a <= 0 <= self.b:
            return I(0, max(self.a**2, self.b**2))
        return I(min(self.a**2, self.b**2), max(self.a**2, self.b**2))

    def serial(self):
        return [str(self.a), str(self.b)]

    def overlaps(self, other):
        return max(self.a, other.a) <= min(self.b, other.b)


def read(p):
    return json.loads(p.read_bytes())


def trans(a):
    return [list(v) for v in zip(*a)]


def mm(a, b):
    return [[sum((x*y for x, y in zip(row, col)), Q(0))
             for col in zip(*b)] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(a, c):
    return [[c*x for x in row] for row in a]


def ident(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def inv(a):
    n = len(a)
    w = [list(map(Q, row))+e for row, e in zip(a, ident(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if w[i][j])
        w[j], w[pivot] = w[pivot], w[j]
        x = w[j][j]
        w[j] = [v/x for v in w[j]]
        for i in range(n):
            if i != j:
                x = w[i][j]
                w[i] = [v-x*z for v, z in zip(w[i], w[j])]
    return [row[n:] for row in w]


def psd2(a):
    assert len(a) == 2 and a[0][1] == a[1][0]
    return a[0][0] >= 0 and a[1][1] >= 0 and a[0][0]*a[1][1] >= a[0][1]**2


def synthetic_checks():
    eta = Q(1, 10**10)
    c = Q(11, 100)-eta
    b = [[Q(2, 5), Q(1, 10)], [Q(1, 10), Q(3, 5)]]
    f = [[Q(1, 3), Q(1, 4)], [Q(-1, 5), Q(2, 5)]]
    x = [[Q(1, 2), Q(-1, 4)], [Q(1, 3), Q(3, 4)]]
    e2 = ident(2)
    assert psd2(b) and psd2(add(scale(e2, Q(89, 100)), scale(b, -1)))
    s = add(scale(e2, 1-eta), scale(b, -1))
    g = mm(mm(f, inv(s)), trans(f))
    fx = mm(f, x)
    v = add(add(fx, trans(fx)), scale(mm(mm(trans(x), s), x), -1))
    residual = add(trans(f), scale(mm(s, x), -1))
    residual_gram = mm(trans(residual), residual)
    exact_error = mm(mm(trans(residual), inv(s)), residual)
    assert g == add(v, exact_error)
    assert psd2(add(g, scale(v, -1)))
    assert psd2(add(add(v, scale(residual_gram, 1/c)), scale(g, -1)))
    k = scale(b, 1/(1-eta))
    power, gn = ident(2), [[Q(0), Q(0)], [Q(0), Q(0)]]
    for _ in range(3):
        gn = add(gn, scale(mm(mm(f, power), trans(f)), 1/(1-eta)))
        power = mm(power, k)
    moment = mm(mm(f, power), trans(f))
    g0 = mm(f, trans(f))
    assert psd2(add(g, scale(gn, -1)))
    assert psd2(add(add(gn, scale(moment, 1/c)), scale(g, -1)))
    assert psd2(add(scale(g0, (Q(89, 100)/(1-eta))**3), scale(moment, -1)))
    return {"synthetic_residual_identity": True,
            "synthetic_full_residual_upper_bound": True,
            "synthetic_directional_neumann_bound": True,
            "actual_operator_certificate": False}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("package", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    root = args.package.resolve()
    task = root/"work/tail-probe-2026-10-10"
    finite = root/"work/inherited/Objekt-X-Endlicher-Schuranschluss-2026-10-09"
    bridge = read(root/"work/inherited/Objekt-X-Unendlicher-Rest-Vergleich-2026-10-09/work/infinite-tail-2026-10-09/FINITE_BRIDGE.json")
    delta, eta = Q(91, 50), Q(1, 10**10)
    eps, c = Q(3, 10**25), Q(11, 100)-eta
    assert 4*eps < (Q(2, 10**12)-eps)**2
    report_bounds = [
        (("0.3460219647", "0.3460219652"), ("0.5370508072", "0.5370508077")),
        (("0.4084886817", "0.4084886819"), ("0.5964190046", "0.5964190048"))]
    cases, checks = [], 0
    for p, label in enumerate(["EVEN", "ODD"]):
        pr = read(task/f"PROBE_{label}_12_3072.json")
        joint = read(task/f"JOINT_{label}_12_3072.json")
        getp = lambda k: I.box(pr[k])
        getj = lambda k: I.box(joint[k])
        rem = sum((getj(k) for k in ["old_low_model_energy", "four_coupling_model_energy",
                                    "eight_residualized_coupling_model_energy"]), I(0))
        ki = inv(bridge["cases"][2+p]["K12_lower"])
        trace_ki = sum(ki[i][i] for i in range(12))
        elow2, eh = getp("weighted_low_model_error_norm_squared"), getp("high_source_model_error_norm")
        err = elow2.sqrt() + (getj("source_feature_metric_trace")*(elow2+eh.square()/delta)).sqrt() + I(12*trace_ki).sqrt()*Q(1, 10**25)
        assert err.overlaps(getj("remaining_error_norm_bound"))
        rroot = rem.sqrt()
        assert rroot.a > err.b
        r0 = I((rroot.a-err.b)**2, (rroot.b+err.b)**2)/getp("L_form_value")
        hg = I.box(pr["complete_old_high_model_gram"][0][0]).sqrt()
        assert hg.a > eh.b
        high = I((hg.a-eh.b)**2, (hg.b+eh.b)**2)/delta
        old_hi = high.b+(getj("old_low_model_energy").sqrt().b+elow2.sqrt().b)**2
        allerr = err + (I(old_hi)*eps).sqrt()
        assert rroot.a > allerr.b
        loss = (high+I((rroot.a-allerr.b)**2, (rroot.b+allerr.b)**2))/getp("L_form_value")
        for interval, bound in zip([r0, loss], report_bounds[p]):
            assert Q(bound[0]) < interval.a <= interval.b < Q(bound[1])
        assert r0.a > Q(11, 100) and loss.b < 1
        high_ratio = high/getp("L_form_value")
        new_directional_quotient = r0/(I(1-eta)-high_ratio)
        assert new_directional_quotient.b < 1
        cases.append({"parity":label.lower(), "R0_over_L":r0.serial(),
                      "Loss_T_over_L":loss.serial(),
                      "R0_over_S_eta_on_probe":new_directional_quotient.serial(),
                      "display_only_approximate":[float(r0.a),float(loss.b),float(new_directional_quotient.b)],
                      "all_four_report_endpoints_enclose_reconstruction":True})
        cal = read(task/f"DIRECT_CALIBRATION_{label}_3072.json")
        schur = read(finite/"work/gamma-low-2026-10-09/SCHUR_SHELL_TIGHT_4096.json")["cases"][p]
        diag = I.box(cal["direct_cross"][4][0])
        assert Q(schur["D_Y_lower"][0][0]) < diag.a <= diag.b < Q(schur["D_Y_upper"][0][0])
        for rr in cal["physical_z_cross_residuals"]:
            xx=I.box(rr)
            assert -Q(1,10**20) < xx.a <= xx.b < Q(1,10**20)
        if p == 0:
            calold = read(task/"CALIBRATION_EVEN_3072.json")
            cert = read(finite/"work/gamma-low-2026-10-09/CERTIFICATE_EVEN_gamma224_tight_4096.json")
            for k in range(191):
                for lhs, rhs in [("old_low_c_model", "source_c_model"), ("old_low_Bh_model", "source_Bh_model")]:
                    assert I.box(calold[lhs][k][0]).overlaps(I.box(cert[rhs][k][4]))
                    checks += 1
            assert I.box(calold["complete_old_high_model_gram"][0][0]).overlaps(I.box(cert["source_h_gram_model"][4][4]))
            checks += 1
    stored_mixed = 0
    for fn in ["PROBE_EVEN_12_3072.json", "PROBE_ODD_12_3072.json", "PROBE_EVEN_12_4096.json", "CALIBRATION_EVEN_3072.json"]:
        for row in read(task/fn)["direct_mixed_checks"]:
            d = I.box(row["difference"])
            assert d.a <= 0 <= d.b and max(abs(d.a),abs(d.b)) < Q(1,10**35)
            stored_mixed += 1
    kappa = Q(89,100)/(1-eta)
    out = {"status":"PASS_RATIONAL_ENDPOINT_AND_SYNTHETIC_CHECKS",
           "cases":cases,"old_calibration_interval_overlaps_rechecked":checks,
           "stored_mixed_residual_enclosures_rechecked":stored_mixed,
           "source_error_price_verified":"2e-12 L",
           "conditional_remaining_L_reserve":str(eta-Q(2,10**12)),
           "S_eta_relative_L_floor":str(c),"dual_L_residual_multiplier":str(1/c),
           "neumann_tail_coefficients_display_only":{str(n):float(kappa**(n+1)/c) for n in [64,128,192,256]},
           "synthetic_checks":synthetic_checks(),
           "analytic_inputs_reproved":False,"source_integrals_recomputed_by_this_script":False,
           "full_203_tail_gram_computed":False,"full_remainder_certified":False}
    args.out.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({"status":out["status"],"cases":[c["display_only_approximate"] for c in cases],
                      "calibration_checks":checks,"mixed_residual_checks":stored_mixed,
                      "neumann":out["neumann_tail_coefficients_display_only"],
                      "full_remainder_certified":False},indent=2))


if __name__ == "__main__":
    main()
