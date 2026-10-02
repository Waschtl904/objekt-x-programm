# Dependency-preserving direct odd eigenline

Publication of the sealed **DEPENDENCY-PRESERVING 2x2 ODD-LINE GATE**.
Status: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`; the full family is **UNRESOLVED**.

## Result and scope

The same 19 comparison cases are evaluated with direct, centered and shared
affine arithmetic. On the conditional four-Y slices, the certified total-angle
upper bounds improve from 163.162463 to **3.405363 degrees** (central) and from
165.457773 to **3.765366 degrees** (quarter). These are bounds on restricted
slices, not a uniform result for the full family. All five inherited feasible
points stay on the maximal eigenvalue branch. Root and all eight diagnostic
leaves remain unresolved; no new adaptive tree or operator input is used.

See the unchanged [proof](PROOF.md), [report](REPORT.md), [summary](summary.json),
[audit](audit.json), [controls](controls.json) and [original acceptance](ACCEPTANCE.json).
The word “local” in these original files describes their sealed source state;
the canonical integration status is recorded in the [registry](../../../00-uebersicht/RESEARCH_STATE.yaml).

## Immutable source and reproduction

The [original ZIP](archives/Direkte-gemeinsame-Odd-Eigenlinie-2026-10-02.zip) is byte-identical to the local sealed
archive, SHA-256 `b7a37a9d6cb8ef49233b77af5c536759cf208ced362f7cdb608f97c3f5847019`. All 59 original files and 58 manifest
bindings are retained, including 41 unchanged baseline files. The three
comparison receipts and all mathematical scripts are inside that archive.
Visible original copies are also checked byte for byte.

From the repository root, after installing `requirements.txt` for this package:

```text
python -B research/x-c1/canonical-direct-odd-line-2026-10-02/replay.py --output <new-directory-outside-repository>
```

The wrapper checks the closed publication manifest, archive paths and hashes,
the eight inherited source files and the integrated adaptive baseline archive.
It runs corruption/path/CI-routing controls and the inherited Git-source check,
then replays all **57 cases** with no abbreviated acceptance path. All three
comparison receipts, controls and the independent rational/Arb audit must
match the sealed bytes. CI uses Python 3.13 and python-flint 0.9.0, preserves
the exact source bytes and publishes commit-bound receipts and logs.

## Next open test

Preserve the common equation `Y_L X + Y_R = 0` and quadratic dependence before
bounding higher remainders, on the same 19 cases. The existing inverse-Y-left
enclosure and first-order affine remainders still lose correlations. The
forthcoming gate must prove any remainder bounds, maximal branch and physical
angle. A uniform root corridor below ten degrees would close localization;
no such result is claimed here. The registry defines its acceptance criteria.
General renewal, A13 positivity, cofinal positivity, global Object X and RH
remain open. PR #187 is separate.
