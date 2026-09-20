#!/usr/bin/env python3
"""Fail-closed consistency checks for the canonical research-state registry."""
from __future__ import annotations

import json
import re
from pathlib import Path

from generate_research_state import load_state, render_current_state

ROOT = Path(__file__).resolve().parents[1]
SHA40 = re.compile(r"^[0-9a-f]{40}$")


def fail(message: str) -> None:
    raise SystemExit("research-state validation failed: " + message)


def assert_sha(value: str, label: str) -> None:
    if not SHA40.fullmatch(value):
        fail(f"{label} is not a 40-character lowercase commit SHA: {value!r}")


def load_json_yaml(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"{path.relative_to(ROOT)} is not valid JSON-compatible YAML: {exc}")


def validate_state(state: dict) -> None:
    if state.get("schema_version") != 1:
        fail("unsupported RESEARCH_STATE schema_version")

    baseline = state["published_baseline"]
    frontier = state["live_frontier"]
    assert_sha(baseline["sha"], "published_baseline.sha")
    assert_sha(frontier["verified_through"], "live_frontier.verified_through")
    assert_sha(frontier["branch_head_at_generation"], "live_frontier.branch_head_at_generation")

    ids = set()
    for collection_name in ("closed_results", "no_go_results"):
        for result in state[collection_name]:
            rid = result["id"]
            if rid in ids:
                fail(f"duplicate result id {rid}")
            ids.add(rid)
            if not result.get("scope"):
                fail(f"{rid} lacks scope")
            proof = ROOT / result["canonical_proof"]
            if not proof.is_file():
                fail(f"{rid} canonical proof does not exist: {result['canonical_proof']}")
            for key in ("origin_commit", "canonical_snapshot_commit"):
                if key in result:
                    assert_sha(result[key], f"{rid}.{key}")

    for result in state["no_go_results"]:
        if result.get("claim_polarity") != "NEGATIVE_FOR_CANDIDATE_CLASS":
            fail(f"{result['id']} lacks candidate-class negative polarity")
        if not result.get("negative_claim_boundary"):
            fail(f"{result['id']} lacks negative_claim_boundary")

    for name, front in state["fronts"].items():
        if front.get("mathematical_status") != "OPEN":
            fail(f"active front {name} is not OPEN")
        if not front.get("obligations"):
            fail(f"active front {name} has no open obligations")

    g = state["global_status"]
    if g["object_x"] == "NOT_CONSTRUCTED" and g["global_weil_gram_identity"] == "CLOSED":
        fail("Objekt X NOT_CONSTRUCTED conflicts with a CLOSED global Weil-Gram identity")

    if not frontier.get("head_policy"):
        fail("verified_through/head policy is missing")


def validate_generated(state: dict) -> None:
    expected = render_current_state(state)
    path = ROOT / state["canonical_files"]["generated_current_state"]
    if not path.is_file():
        fail("generated CURRENT_STATE.md is missing")
    if path.read_text(encoding="utf-8") != expected:
        fail("CURRENT_STATE.md is not the deterministic generator output")


def validate_survivors(state: dict) -> None:
    path = ROOT / state["canonical_files"]["survivor_registry"]
    text = path.read_text(encoding="utf-8")
    sections = re.split(r"(?m)^## ", text)[1:]
    if not sections:
        fail("SURVIVOR_REGISTRY.md has no entries")
    for section in sections:
        heading, _, body = section.partition("\n")
        for marker in ("- Scope:", "- Canonical proof:", "- Does not claim:"):
            if marker not in body:
                fail(f"survivor {heading!r} lacks {marker}")
        match = re.search(r"- Canonical proof: `([^`]+)`", body)
        if not match:
            fail(f"survivor {heading!r} has no parseable canonical proof path")
        if not (ROOT / match.group(1)).is_file():
            fail(f"survivor {heading!r} proof path does not exist: {match.group(1)}")
        if "NOGO" in heading and "- Negative claim boundary:" not in body:
            fail(f"No-Go survivor {heading!r} lacks negative claim boundary")


def validate_historical_banners(state: dict) -> None:
    for rel in state["historical_navigation_files"]:
        path = ROOT / rel
        if not path.is_file():
            fail(f"historical navigation file missing: {rel}")
        prefix = path.read_text(encoding="utf-8")[:1200]
        if "HISTORICAL SNAPSHOT" not in prefix:
            fail(f"historical navigation file lacks banner: {rel}")


def validate_package_meta(state: dict) -> None:
    for package in state.get("strategic_packages", []):
        meta_path = ROOT / package["meta"]
        if not meta_path.is_file():
            fail(f"strategic package lacks META.yaml: {package['id']}")
        meta = load_json_yaml(meta_path)
        if meta.get("strategic") is not True:
            fail(f"{package['id']} META.yaml is not marked strategic")
        if not any(meta.get(key) for key in ("closes", "opens", "supersedes")) and not meta.get("local_only"):
            fail(f"{package['id']} META.yaml has no closes/opens/supersedes/local_only classification")
        proof = meta.get("canonical_proof", {})
        if not (ROOT / proof.get("path", "")).is_file():
            fail(f"{package['id']} META canonical proof is missing")
        assert_sha(proof.get("commit", ""), f"{package['id']}.META.canonical_proof.commit")


def main() -> int:
    found = list(ROOT.rglob("RESEARCH_STATE.yaml"))
    if found != [ROOT / "00-uebersicht" / "RESEARCH_STATE.yaml"]:
        fail(f"expected exactly one canonical RESEARCH_STATE.yaml, found {len(found)}")

    state = load_state()
    validate_state(state)
    validate_generated(state)
    validate_survivors(state)
    validate_historical_banners(state)
    validate_package_meta(state)
    print("research-state registry validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
