#!/usr/bin/env python3
"""Generate the human-readable current research state.

RESEARCH_STATE.yaml is deliberately JSON-compatible YAML so this script can
use only the Python standard library. The output is deterministic.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_PATH = ROOT / "00-uebersicht" / "RESEARCH_STATE.yaml"
OUTPUT_PATH = ROOT / "00-uebersicht" / "CURRENT_STATE.md"


def load_state(path: Path = STATE_PATH) -> dict:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def render_current_state(state: dict) -> str:
    baseline = state["published_baseline"]
    frontier = state["live_frontier"]
    transport = state["fronts"]["transport"]
    c1 = state["fronts"]["c1"]
    global_status = state["global_status"]

    lines = [
        "# Current Research State",
        "",
        "> **GENERATED FILE — DO NOT EDIT**",
        ">",
        "> Source: `00-uebersicht/RESEARCH_STATE.yaml`  ",
        f'> State date: {state["state_date"]}',
        "",
        "## Published baseline",
        "",
        f'`{baseline["branch"]}@{baseline["sha"]}`',
        "",
        "PR #137 is merged and frozen as the published baseline through \\(B=\\log(5)/2\\).  ",
        f'Mathematical status: **{baseline["mathematical_status"]}**. Review status: **{baseline["review_status"]}**.',
        "",
        "## Verified research frontier",
        "",
        f'Verified through `{frontier["verified_through"]}` on',
        f'`{frontier["branch"]}`.',
        "",
        "Branch head observed at generation:",
        f'`{frontier["branch_head_at_generation"]}`.',
        "",
        "**The observed branch head is not automatically promoted to the verified frontier.**",
        "Commits after `verified_through` remain outside the canonical mathematical state until explicitly audited and promoted.",
        "",
        "## Active fronts",
        "",
        f'### Transport — {transport["title"].upper()}',
        "",
        "Scope: \\(B\\le a\\le1\\).",
        "",
        "Open obligations:",
    ]
    for item in transport["obligations"]:
        lines.append(f"- {item};" if item != transport["obligations"][-1] else f"- {item}.")
    lines += [
        "",
        "### C1 — COMPACT DEFECT CONTRACTION",
        "",
        f'Candidate: **{c1["candidate"]}**.',
        "",
        "Open target:",
        "\\[",
        "\\|R_a\\|\\le1",
        "\\]",
        "proved independently of already-known Weil positivity on the fixed horizon \\(B\\le a\\le1\\).",
        "Where the nested restriction structure is used, terminal control at \\(a=1\\) may serve as the sufficient endpoint formulation.",
        "",
        "## Closed operative results",
        "",
    ]
    for result in state["closed_results"]:
        lines.append(f'- `{result["id"]}`')
    lines += [
        "",
        "## Active No-Go firewalls",
        "",
    ]
    for result in state["no_go_results"]:
        lines.append(f'- `{result["id"]}`')
    lines += [
        "",
        "These are candidate-class exclusions, not negative results for the full Weil form.",
        "",
        "## Global limits",
        "",
        f'- Connected Unit-Window Coercivity: **{global_status["connected_unit_window_coercivity"]}**',
        f'- Strong Terminal: **{global_status["strong_terminal"]}**',
        f'- Full C1-GEOM: **{global_status["full_c1_geom"]}**',
        f'- Objekt X: **{global_status["object_x"].replace("_", " ")}**',
        f'- Global Weil-Gram identity: **{global_status["global_weil_gram_identity"]}**',
        f'- Global Weil positivity: **{global_status["global_weil_positivity"]}**',
        f'- RH: **{global_status["rh"]}**',
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    rendered = render_current_state(load_state())
    if args.check:
        existing = OUTPUT_PATH.read_text(encoding="utf-8")
        if existing != rendered:
            raise SystemExit(
                "CURRENT_STATE.md is stale. Run scripts/generate_research_state.py "
                "and commit the generated output."
            )
        print("CURRENT_STATE.md matches RESEARCH_STATE.yaml")
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
