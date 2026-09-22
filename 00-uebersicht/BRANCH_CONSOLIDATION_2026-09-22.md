# Branch consolidation inventory — 2026-09-22

This is a **read-only inventory**. It deletes no branches and changes no
mathematical status.

## Snapshot

- Baseline: `main@5dcf96e2d3fe977051d7d65febb1ed7b7ef03901`
- Legacy non-main branches inventoried: **195**
- Pull requests inspected: **152**
- The temporary inventory branch itself is excluded from the count.
- Canonical navigation scanned literally for branch references:
  - `00-uebersicht/RESEARCH_STATE.yaml`
  - `00-uebersicht/CURRENT_STATE.md`
  - `00-uebersicht/NEXT_GATES.md`
  - `00-uebersicht/RESEARCH_STATE_MAINTENANCE.md`

## Conservative recommendations

- `DELETE_CANDIDATE_AFTER_APPROVAL`: **81**
- `KEEP`: **1**
- `KEEP_PROVENANCE`: **2**
- `REVIEW_UNIQUE`: **111**

## Categories

- `ACTIVE_PR`: **1**
- `AUDIT_MERGED_HISTORY`: **11**
- `AUDIT_UNIQUE`: **7**
- `MERGED_HISTORY`: **61**
- `RESEARCH_MERGED_HISTORY`: **11**
- `RESEARCH_UNIQUE`: **63**
- `UNIQUE_HISTORY`: **41**

## Current-navigation references

- `docs/post-pr144-research-state-sync-2026-09-21`
- `research/x-c1-inherited-resonance-shell-schur-2026-09-18`

## Rules used

A branch is marked `DELETE_CANDIDATE_AFTER_APPROVAL` only when its compared
head contributes **zero commits ahead of the baseline main** and its branch
name is not literally referenced by the current canonical navigation files
listed above. This is a candidate classification, **not deletion authority**.

Any branch with commits ahead of main is `REVIEW_UNIQUE` unless current
canonical navigation requires it, in which case it is `KEEP_PROVENANCE`.
Unique research/audit history is therefore preserved for a second,
branch-specific provenance/supersession review.

## What this first pass does not prove

This is not yet a repository-wide textual reference scan of every historical
proof file. Before deletion of any provenance-sensitive branch, its exact
head SHA, PR history, successor relation, and any proof/hash references must
be reconciled. Where long-term reachability of an otherwise deletable unique
historical tip matters, an immutable archive tag should be created first.

## Files

- [BRANCH_INVENTORY_2026-09-22.csv](BRANCH_INVENTORY_2026-09-22.csv) — flat manifest.
- [BRANCH_INVENTORY_DATA_2026-09-22.json](BRANCH_INVENTORY_DATA_2026-09-22.json) — full machine-readable API snapshot.
