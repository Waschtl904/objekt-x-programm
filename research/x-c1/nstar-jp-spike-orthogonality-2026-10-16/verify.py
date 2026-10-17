#!/usr/bin/env python3
"""Replay-Wrapper zum Paket nstar-jp-spike-orthogonality-2026-10-16.

Nur Standardbibliothek. Prueft
  (B1) SHA-256 aller in SOURCE_BINDINGS.json gebundenen Dateien dieses Pakets und der
       repositoryinternen Abhaengigkeiten (N*Jp-Brueckenarchiv aus #226, #227-Archive),
  (B2) die sichtbaren Kopien in original/ gegen die Archivmitglieder (bytegenau),
  (R1) Replay des gerichteten Stufe-1-Pruefers certify.py (Paket 940cd40e...) aus dem frisch
       entpackten Archiv gegen das Brueckenarchiv; Ausgaben bytegleich mit expected/,
  (R2) Replay des gerichteten Stufe-3-Pruefers certify_stage3.py (Paket ab7116f7...) analog,
  (R3) Replay des gerichteten Stufe-4-Hochantwort-Pruefers certify.py (Paket 1ccb6be1...) mit den drei
       Vorgaengerarchiven (b48e3895 aus #226, ab7116f7 aus diesem Paket, b8677c0b aus #227),
  (R4) Replay des Rayleigh-Zeugen-Pruefers verify.py (Paket f0bdfe69...) mit Hochantwort- und Antwortarchiv.
Die mpmath-Diagnosen (stufe1/, stufe2/, stufe4/) werden nicht neu gerechnet; ihre Dateien sind
in (B1) hashgebunden. Es wird keine mathematische Aussage ueber den N12-Test, A9->A11 oder
Objekt X geprueft; der Wrapper zertifiziert Bindung und Reproduzierbarkeit der Pruefer.
"""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BINDINGS = HERE / "SOURCE_BINDINGS.json"
BRIDGE = ROOT / "research/x-c1/a9-inverse-spike-calibration-2026-10-15/archives/Objekt-X-Nstar-Jp-Funktionsanschluss-und-Koeffizienten-2026-10-16.zip"
BRIDGE_SHA = "b48e3895d57cc5cc2c11ca170e32d6af5fbdfcde9948b4db7c370d3376b6d57b"
STAGE1 = "archives/Objekt-X-Stufe1-Intervallzertifikat-Momentkorrektur-und-W9-Diagnose-2026-10-16.zip"
STAGE3 = "archives/Objekt-X-Stufe3-Endliche-U8-Antwort-und-Skalaranschluss-2026-10-16.zip"
STAGE4 = "archives/Objekt-X-Vollstaendige-Hochantwort-und-Spike-Skalarfehler-2026-10-16.zip"
RAYLEIGH = "archives/Objekt-X-Stufe4-Teil2-Gegenpruefung-und-Rayleigh-Zeugen-2026-10-17.zip"
RESPONSE = ROOT / "research/x-c1/a9-a11-whole-response-gram-2026-10-15/archives/Objekt-X-Vollstaendiger-Antwortgram-und-Scharfer-Modellfehler-2026-10-15.zip"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def check_bindings(b) -> int:
    n = 0
    for rel, d in b["files"].items():
        p = HERE / rel
        data = p.read_bytes()
        assert sha(data) == d["sha256"] and len(data) == d["bytes"], rel
        n += 1
    for rel, d in b["repository_dependencies"].items():
        data = (ROOT / rel).read_bytes()
        assert sha(data) == d["sha256"], rel
        n += 1
    for rel, d in b["archives"].items():
        data = (HERE / rel).read_bytes()
        assert sha(data) == d["sha256"] and len(data) == d["bytes"], rel
        z = zipfile.ZipFile(HERE / rel)
        for name, m in d["members"].items():
            raw = z.read(name)
            assert sha(raw) == m["sha256"] and len(raw) == m["bytes"], name
            n += 1
            vis = d.get("visible_copies", {}).get(name)
            if vis:
                assert (HERE / vis).read_bytes() == raw, "sichtbare Kopie weicht ab: " + vis
    return n


def replay(archive: Path, script: str, workdir: Path, label: str, extra=(), bridge=True) -> dict:
    z = zipfile.ZipFile(archive)
    root = z.namelist()[0].split("/")[0]
    z.extractall(workdir)
    pkg = workdir / root
    out = workdir / (label + "-out")
    cmd = [sys.executable, "-B", "-X", "utf8", str(pkg / script)] + (["--bridge-archive", str(BRIDGE)] if bridge else []) + [*extra, "--output", str(out)]
    p = subprocess.run(cmd, cwd=str(pkg), capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit(label + " Replay fehlgeschlagen:\n" + p.stdout[-2000:] + p.stderr[-2000:])
    compared = 0
    for exp in sorted((pkg / "expected").glob("*.json")):
        got = out / exp.name
        assert got.is_file(), "fehlende Ausgabe " + exp.name
        assert got.read_bytes() == exp.read_bytes(), "Ausgabe weicht ab: " + exp.name
        compared += 1
    receipt = json.loads((out / "RECEIPT.json").read_bytes())
    assert receipt.get("status") in ("PASS", "PASS_UNDER_BOUND_OPERATOR_DOMAIN_AND_COMPLETE_SOURCE_HYPOTHESES",
                                     "PASS_UNDER_BOUND_COMPLETE_SOURCE_GRAM_AND_OPERATOR_HYPOTHESES",
                                     "PASS_UNDER_BOUND_OPERATOR_DOMAIN_AND_FULL_MODEL_INTEGRATION_HYPOTHESES"), receipt
    return {"expected_files_bytewise_equal": compared, "receipt_status": receipt["status"]}


def main() -> int:
    b = json.loads(BINDINGS.read_text(encoding="utf-8"))
    assert sha(BINDINGS.read_bytes()) == (HERE / "SOURCE_BINDINGS.sha256").read_text().split()[0]
    assert sha(BRIDGE.read_bytes()) == BRIDGE_SHA
    report = {"package": HERE.name, "proof_sha256": sha((HERE / "PROOF.md").read_bytes()), "bound_items": check_bindings(b)}
    tmp = Path(tempfile.mkdtemp(prefix="nstar-spike-replay-"))
    try:
        report["stage1_certify_replay"] = replay(HERE / STAGE1, "certify.py", tmp / "s1", "stage1")
        report["stage3_certify_replay"] = replay(HERE / STAGE3, "certify_stage3.py", tmp / "s3", "stage3")
        report["stage4_high_certify_replay"] = replay(HERE / STAGE4, "certify.py", tmp / "s4", "stage4",
                                                      extra=("--stage3-archive", str(HERE / STAGE3), "--response-archive", str(RESPONSE)))
        report["rayleigh_witness_replay"] = replay(HERE / RAYLEIGH, "verify.py", tmp / "s5", "rayleigh", bridge=False,
                                                   extra=("--high-archive", str(HERE / STAGE4), "--response-archive", str(RESPONSE)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    report["scope"] = "binding and replay only; no mathematical claim about N12, A9->A11 or Object X"
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
