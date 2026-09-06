#!/usr/bin/env python3
"""Validate the volatile active-front ledger.

Governance-only check. It does not validate mathematical theorem status.

Checks:
- current main is declared as live-tracked rather than self-recorded by SHA;
- stack_root_base_sha is a 40-character lowercase hex commit id;
- every stored stack SHA is 40-character lowercase hex;
- every stacked parent_pr resolves to an earlier stack entry;
- parent_head_sha equals the recorded parent head exactly;
- the stack root parent_head_sha equals stack_root_base_sha;
- volatile stack/base SHA values are not manually duplicated in operative navigation files.

Why no current main SHA is stored here:
a versioned file cannot permanently contain the SHA of the commit that contains that
same file. Updating the value creates a new commit SHA and immediately makes the stored
value stale. The current main head must therefore be read live from GitHub.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FRONT = ROOT / "00-uebersicht" / "ACTIVE_FRONT.yaml"
NAV_FILES = [
    ROOT / "CURRENT-FRONT.md",
    ROOT / "00-uebersicht" / "AKTUELLER_STAND.md",
    ROOT / "00-uebersicht" / "DAG.md",
    ROOT / "00-uebersicht" / "FORSCHUNGS_ROADMAP_AKTUELL.md",
]

SHA_RE = re.compile(r"^[0-9a-f]{40}$")
STACK_START_RE = re.compile(r"^  - pr: ([0-9]+)$")
FIELD_RE = re.compile(r"^    ([a-z_]+): (.*)$")
STACK_ROOT_BASE_RE = re.compile(r"(?m)^stack_root_base_sha: ([0-9a-f]+)$")
MAIN_TRACKING_RE = re.compile(r"(?m)^  tracking: live$")
MAIN_SOURCE_RE = re.compile(r"(?m)^  source: github:refs/heads/main$")
SELF_RECORDED_MAIN_SHA_RE = re.compile(r"(?m)^  sha: [0-9a-f]{7,40}$")


def fail(message: str) -> None:
    print(f"ACTIVE_FRONT validation FAILED: {message}", file=sys.stderr)
    raise SystemExit(1)


def clean_value(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1]
    return value


def parse_stack(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    current: dict[str, str] | None = None

    for line in text.splitlines():
        start = STACK_START_RE.match(line)
        if start:
            if current is not None:
                entries.append(current)
            current = {"pr": start.group(1)}
            continue

        if current is not None:
            field = FIELD_RE.match(line)
            if field:
                current[field.group(1)] = clean_value(field.group(2))

    if current is not None:
        entries.append(current)

    return entries


def main() -> None:
    text = FRONT.read_text(encoding="utf-8")

    if SELF_RECORDED_MAIN_SHA_RE.search(text):
        fail(
            "current main SHA must not be self-recorded in ACTIVE_FRONT.yaml; "
            "read refs/heads/main live from GitHub"
        )
    if not MAIN_TRACKING_RE.search(text):
        fail("main.tracking must be 'live'")
    if not MAIN_SOURCE_RE.search(text):
        fail("main.source must be github:refs/heads/main")

    root_match = STACK_ROOT_BASE_RE.search(text)
    if not root_match:
        fail("stack_root_base_sha is missing")
    stack_root_base_sha = root_match.group(1)
    if not SHA_RE.fullmatch(stack_root_base_sha):
        fail(f"stack_root_base_sha is not 40-hex: {stack_root_base_sha!r}")

    entries = parse_stack(text)
    if not entries:
        fail("stack is empty")

    by_pr: dict[str, dict[str, str]] = {}
    seen_heads: set[str] = set()

    for index, entry in enumerate(entries):
        pr = entry.get("pr", "?")
        for key in ("branch", "head_sha", "base", "parent_head_sha"):
            if not entry.get(key):
                fail(f"PR #{pr}: missing {key}")

        head_sha = entry["head_sha"]
        parent_head_sha = entry["parent_head_sha"]
        if not SHA_RE.fullmatch(head_sha):
            fail(f"PR #{pr}: head_sha is not 40-hex: {head_sha!r}")
        if not SHA_RE.fullmatch(parent_head_sha):
            fail(f"PR #{pr}: parent_head_sha is not 40-hex: {parent_head_sha!r}")
        if head_sha in seen_heads:
            fail(f"PR #{pr}: duplicate head_sha {head_sha}")
        seen_heads.add(head_sha)

        if index == 0:
            if entry["base"] != "main":
                fail(f"stack root PR #{pr}: base must be main")
            if parent_head_sha != stack_root_base_sha:
                fail(
                    f"stack root PR #{pr}: parent_head_sha {parent_head_sha} "
                    f"!= stack_root_base_sha {stack_root_base_sha}"
                )
            if "parent_pr" in entry:
                fail(f"stack root PR #{pr}: parent_pr must be absent")
        else:
            parent_pr = entry.get("parent_pr")
            if not parent_pr:
                fail(f"PR #{pr}: missing parent_pr")
            parent = by_pr.get(parent_pr)
            if parent is None:
                fail(f"PR #{pr}: parent_pr #{parent_pr} is not an earlier stack entry")
            if parent_head_sha != parent["head_sha"]:
                fail(
                    f"PR #{pr}: parent_head_sha {parent_head_sha} "
                    f"!= PR #{parent_pr} head_sha {parent['head_sha']}"
                )
            if entry["base"] != parent["branch"]:
                fail(
                    f"PR #{pr}: base {entry['base']!r} "
                    f"!= parent PR #{parent_pr} branch {parent['branch']!r}"
                )

        by_pr[pr] = entry

    volatile_values = {stack_root_base_sha}
    volatile_values.update(entry["head_sha"] for entry in entries)
    volatile_values.update(entry["parent_head_sha"] for entry in entries)

    for path in NAV_FILES:
        nav_text = path.read_text(encoding="utf-8")
        for sha in volatile_values:
            if sha in nav_text:
                fail(f"volatile stack/base SHA {sha} duplicated in {path.relative_to(ROOT)}")

    print(
        "ACTIVE_FRONT validation PASS: live main tracking; "
        f"historical stack root + {len(entries)} stacked PRs consistent; "
        "no volatile stack/base SHA duplication in operative navigation files."
    )


if __name__ == "__main__":
    main()
