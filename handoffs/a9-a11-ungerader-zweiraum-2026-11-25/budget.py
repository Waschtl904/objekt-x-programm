"""Gerichteter Budgetprüfer für die festgelegte ungerade Richtung."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

COEFFICIENTS = [-960, -1786, -1111, 735, 2564, 1686, -2634, -3352, 6471, -4543, 1858, -485]
PACKAGE = Path("research/x-c1/w9-partial-energy-2026-10-18")
PAIR_SHA256 = "85a6e0309caa2272ea2f763653d4382b21d9041f754158401563e5c5a41c9bd4"
PINS = {
    "INPUT_BINDINGS.json": "a57030f51a827598cc41b923b8cfd23410cfd0b2",
    "common.py": "1a88b1d72daa3fe6aeccee0449ecc6998c466a6f",
    "assemble.py": "aeadc048c4928bf739c70a1cbf49b8651cf73544",
    "certify_k.py": "460b011613c683c43b3625c71dbf0fa116cf81b5",
    "weights.py": "adc250e1a3cf0d842fea94806fdb6bfa5e3a6f95",
}

def git_blob(path):
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    pkg = args.root.resolve() / PACKAGE
    check_package(pkg)
    sys.path.insert(0, str(pkg))
    from flint import ctx
    from common import Inputs, encode
    from assemble import load_pairs
    from certify_k import certify
    ctx.prec = 1536
    pairs = load_pairs(pkg / "expected/PAIRS_odd.json.gz")
    assert pairs["parity"] == "odd" and pairs["_source_sha256"] == PAIR_SHA256
    result = certify(Inputs(), pairs, [str(v) for v in COEFFICIENTS])
    result = encode(result)
    result.update(bits=ctx.prec, nodes_per_panel=128, source_sha256=pairs["_source_sha256"],
                  certify_k_blob=git_blob(pkg / "certify_k.py"))
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("K_P", result["K_P_interval"], flush=True)

def check_package(pkg):
    for name, expected in PINS.items():
        if git_blob(pkg / name) != expected:
            raise ValueError(f"Source blob mismatch in {name}")

if __name__ == "__main__":
    run()
