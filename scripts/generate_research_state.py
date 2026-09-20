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
    unified = state["fronts"]["unified_terminal"]
    follow_on = state["fronts"]["global_continuation"]
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
        "At registry generation the observed research-branch head was the same commit.",
        "",
        "## Unified fixed-horizon front",
        "",
        f'### {unified["id"]}',
        "",
        f'**{unified["title"]}.**',
        "",
        "Equivalent fixed-horizon targets:",
    ]
    lines.extend(f"- {item}" for item in unified["equivalent_targets"])
    lines.extend(["", "Open certification obligations:"])
    lines.extend(f"- {item}" for item in unified["obligations"])
    lines.extend([
        "",
        "This terminal gate now represents both the fixed-horizon Moving-191D core positivity problem and C1 defect contraction.",
        "",
        "## Follow-on global continuation",
        "",
        f'### {follow_on["id"]}',
        "",
        f'**{follow_on["title"]}.**',
        "",
    ])
    lines.extend(f"- {item}" for item in follow_on["obligations"])
    lines.extend([
        "",
        "The bridge does not remove these profile/global-horizon obligations.",
        "",
        "## Closed operative results",
        "",
    ])
    lines.extend(f'- `{result["id"]}`' for result in state["closed_results"])
    lines.extend([
        "",
        "## Active No-Go firewalls",
        "",
    ])
    lines.extend(f'- `{result["id"]}`' for result in state["no_go_results"])
    lines.extend([
        "",
        "These are candidate-class exclusions, not negative results for the full Weil form.",
        "",
        "## Global limits",
        "",
        f'- C1a: **{global_status["c1a"]}**',
        f'- C1b: **{global_status["c1b"]}**',
        f'- C1 High: **{global_status["c1_high"]}**',
        f'- C1 Bridge: **{global_status["c1_bridge"]}**',
        f'- C1c: **{global_status["c1c"]}**',
        f'- C1d: **{global_status["c1d"]}**',
        f'- Connected Unit-Window Coercivity: **{global_status["connected_unit_window_coercivity"]}**',
        f'- Strong Terminal: **{global_status["strong_terminal"]}**',
        f'- Objekt X: **{global_status["object_x"].replace("_", " ")}**',
        f'- Global Weil-Gram identity: **{global_status["global_weil_gram_identity"]}**',
        f'- Global Weil positivity: **{global_status["global_weil_positivity"]}**',
        f'- RH: **{global_status["rh"]}**',
        "",
    ])
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
