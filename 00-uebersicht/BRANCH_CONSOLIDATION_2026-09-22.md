# Branch consolidation inventory — 2026-09-22

This is a **read-only inventory**. It deletes no branches and changes no
mathematical status.

## Snapshot

- Baseline: `main@5dcf96e2d3fe977051d7d65febb1ed7b7ef03901` (post-PR #152 snapshot; subsequent #153 is proof-text reconciliation and does not invalidate the conservative ancestry test below)
- Legacy non-main branches inventoried: **195**
- Pull requests inspected: **152**
- The temporary inventory branch itself is excluded from the count.
- PR #151 was subsequently closed as duplicate/superseded by merged #152/#153; its branch remains preserved as unique provenance.

## Conservative recommendations

- `DELETE_CANDIDATE_AFTER_APPROVAL`: **81**
- `KEEP_PROVENANCE`: **2**
- `REVIEW_UNIQUE`: **112**

## Categories

- `AUDIT_MERGED_HISTORY`: **11**
- `AUDIT_UNIQUE`: **7**
- `MERGED_HISTORY`: **61**
- `RESEARCH_MERGED_HISTORY`: **11**
- `RESEARCH_UNIQUE`: **64**
- `UNIQUE_HISTORY`: **41**

## Canonical navigation scanned

- `00-uebersicht/RESEARCH_STATE.yaml`
- `00-uebersicht/CURRENT_STATE.md`
- `00-uebersicht/NEXT_GATES.md`
- `00-uebersicht/RESEARCH_STATE_MAINTENANCE.md`

Literal branch-name references found:
- `docs/post-pr144-research-state-sync-2026-09-21`
- `research/x-c1-inherited-resonance-shell-schur-2026-09-18`

## Rules used

`DELETE_CANDIDATE_AFTER_APPROVAL` requires zero commits ahead of the recorded
main baseline and no literal reference in the current canonical navigation
files above. This is **not deletion authority**.

Every branch with unique commits is preserved for a second provenance and
supersession pass. Audit/research history is therefore never deleted merely
because its PR is closed.

## Important limitation

This first pass is not a repository-wide textual reference scan of every
historical proof. Before deletion of any provenance-sensitive branch, its
exact head SHA, successor relation, PR history and proof/hash references must
be checked. If a unique historical tip must remain reachable, create an
immutable archive tag before deleting the branch.

## Files

- [BRANCH_INVENTORY_2026-09-22.csv](BRANCH_INVENTORY_2026-09-22.csv)
- [BRANCH_INVENTORY_DATA_2026-09-22.json](BRANCH_INVENTORY_DATA_2026-09-22.json)
