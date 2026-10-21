"""One exact rational eta*q[Jw] evaluation; no new solve or integration."""
import argparse
import gzip
import hashlib
import io
import json
import subprocess
import sys
from fractions import Fraction as Q
from pathlib import Path, PurePosixPath, PureWindowsPath
from types import MappingProxyType
from zipfile import ZipFile

HERE = Path(__file__).resolve().parent
BASE = "4e292a178bc3034049eb7abfa0c915a3c2bf815f"
ETA = Q(1, 10**10)
VECTOR = "70e8f72ab0cb8ca1ac0d254392384a2040a9d76d04ebf82587c48771e9f34628"
KNEW = "89ded551059d1279c646bc17e3b5ab3e2a7f7a261d1c239ac752b7f0d35467a8"


def need(ok, message):
    if not ok:
        raise RuntimeError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def bound_path(root, name):
    """Read repository-relative bindings identically on Windows and POSIX."""
    need(isinstance(name, str) and bool(name) and "\x00" not in name,
         "Invalid input path")
    relative = PurePosixPath(name.replace("\\", "/"))
    need(not relative.is_absolute() and not PureWindowsPath(name).drive,
         "Absolute input path")
    need(".." not in relative.parts, "Escaping input")
    root = root.resolve()
    path = root.joinpath(*relative.parts).resolve()
    need(path.is_relative_to(root), "Escaping input")
    return path


def snapshot(root, bindings):
    need(__debug__, "Do not use python -O")
    spec = json.loads(bindings)
    need(spec["source_commit"] == BASE, "Frozen base")
    data = {}
    for alias, entry in spec["files"].items():
        path = bound_path(root, entry["path"])
        raw = path.read_bytes()
        need(sha(raw) == entry["sha256"], "Input hash: " + alias)
        data[alias] = raw
    old = json.loads(data["source_bindings"])
    need(old["files"]["stage3_archive"]["sha256"] == sha(data["stage3_archive"]),
         "Archive provenance")
    member = old["members"]["common"]
    need(member["archive"] == "stage3_archive", "Common source")
    with ZipFile(io.BytesIO(data["stage3_archive"])) as archive:
        raw = archive.read(member["member"])
    need(sha(raw) == member["sha256"], "Nested common hash")
    data["common"] = raw
    return MappingProxyType(data)


def interval_quad(rows, w):
    """Ordered sum including both off-diagonal entries, with exact endpoints."""
    need(len(rows) == 96 and all(len(row) == 96 for row in rows), "D96 shape")
    lo = hi = Q(0)
    for i, wi in enumerate(w):
        for j, wj in enumerate(w):
            a, b = map(Q, rows[i + 12][j + 12])
            need(a <= b, "Reversed matrix interval")
            t = wi * wj
            lo += t * (a if t >= 0 else b)
            hi += t * (b if t >= 0 else a)
    return lo, hi


def run(data):
    prior = json.loads(data["previous_result"])
    frozen = json.loads(data["frozen_vector"])
    need(sha(data["frozen_vector"]) == VECTOR == prior["test_vector_sha256"],
         "Frozen test vector")
    need(frozen["K_new_sha256"] == prior["K_new_sha256"] == KNEW, "Fixed K_new")
    need(frozen["physical_candidate_sha256"] == prior["physical_candidate_sha256"],
         "Fixed physical witness")
    need(frozen["parity"] == prior["parity"] == "even", "Parity")
    need(prior["positive_eta_q_term_unused"] is True, "Do not count eta twice")
    old_lower = Q(prior["inverse_energy_lower"])
    need(old_lower == Q(prior["base_actual_energy_interval"][0])
         + 2 * Q(prior["pairing_actual_interval"][0]) - Q(prior["H_new_form_upper"]),
         "Inherited endpoint algebra")
    need(prior["full_inverse_energy_upper_claimed"] is False
         and prior["partial_pass"] is False and prior["dual_reserve"] is None,
         "Inherited one-sided scope")
    w = [Q(x) for x in frozen["raw_coefficients"]]
    need(len(w) == 84 and any(w), "Nonzero fixed 84-vector")
    source = json.loads(gzip.decompress(data["common"]))["cases"][0]
    need(source["parity"] == "even", "Common parity")
    dl = interval_quad(source["D96_lower_model"], w)
    du = interval_quad(source["D96_upper_model"], w)
    qlo, qhi = dl[0], du[1]
    need(0 < qlo <= qhi, "Positive directed q interval")
    eta_lo, eta_hi = ETA*qlo, ETA*qhi
    lower = old_lower + eta_lo
    budget = Q(prior["budget_interval"][1])
    outcome = ("SCHUR_UNDERFORM_COMPARISON_EXCLUDED"
               if lower > budget else "SCHUR_LOWER_TEST_OPEN")
    return {
        "status": "AUTHOR_DERIVED", "review_status": "EXTERNAL_REVIEW_OPEN",
        "source_commit": BASE, "outcome": outcome, "parity": "even",
        "eta": str(ETA), "test_vector_sha256": VECTOR, "K_new_sha256": KNEW,
        "physical_candidate_sha256": prior["physical_candidate_sha256"],
        "K_P_certificate_sha256": prior["K_P_certificate_sha256"],
        "previous_result_sha256": sha(data["previous_result"]),
        "common_source_sha256": sha(data["common"]),
        "D_lower_quadratic_interval": list(map(str, dl)),
        "D_upper_quadratic_interval": list(map(str, du)),
        "q_interval": [str(qlo), str(qhi)],
        "eta_q_interval": [str(eta_lo), str(eta_hi)],
        "inherited_inverse_energy_lower": str(old_lower),
        "inherited_H_new_form_upper": prior["H_new_form_upper"],
        "updated_H_new_form_upper": str(Q(prior["H_new_form_upper"])-eta_lo),
        "inverse_energy_lower": str(lower),
        "budget_interval": prior["budget_interval"],
        "lower_minus_budget_upper": str(lower-budget),
        "original_gap_to_budget_upper": str(budget-old_lower),
        "remaining_gap_to_budget_upper": str(budget-lower),
        "eta_upper_insufficient_to_close_inherited_gap": eta_hi < budget-old_lower,
        "remaining_gain": "<nu_new-H_new Jw, H_new^-1 (nu_new-H_new Jw)>",
        "full_inverse_energy_upper_claimed": False, "partial_pass": False,
        "dual_reserve": None, "previous_bounds_changed": False,
        "test_vector_changed": False, "physical_witness_changed": False,
        "frozen_response_changed": False, "K_new_changed": False,
        "new_integrations": False, "new_solves": False, "adaptive_search": False,
        "N12_closed": False, "milestone_4_closed": False,
    }


def checked_package(directory):
    manifest = json.loads((directory / "MANIFEST.json").read_bytes())
    checked = {}
    for name, expected in manifest.items():
        path = bound_path(directory, name)
        raw = path.read_bytes()
        need(sha(raw) == expected, "Package hash: " + name)
        checked[name] = raw
    return checked


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repository", type=Path, default=HERE.parents[2])
    ap.add_argument("--output", type=Path)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    args = ap.parse_args()
    need(__debug__, "Do not use python -O")
    if not args.worker:
        subprocess.run([sys.executable, "-B", str(HERE / "verify.py"),
                        *sys.argv[1:], "--worker"], check=True, timeout=120)
        return
    if args.check:
        package = checked_package(HERE)
        raw_bindings = package["INPUT_BINDINGS.json"]
    else:
        raw_bindings = (HERE / "INPUT_BINDINGS.json").read_bytes()
    data = snapshot(args.repository.resolve(), raw_bindings)
    result = run(data)
    raw = (json.dumps(result, indent=2) + "\n").encode()
    if args.check:
        need(raw == package["RESULT.json"], "Byte-identical result")
    if args.output:
        args.output.write_bytes(raw)
    print("PASS: " + result["outcome"])
    print("eta*q interval: " + str([float(Q(x)) for x in result["eta_q_interval"]]))
    print("updated lower: " + str(float(Q(result["inverse_energy_lower"]))))


if __name__ == "__main__":
    main()
