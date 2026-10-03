# Common Y-kernel / second-order odd line

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN; root UNRESOLVED.**
The package is registered as `PENDING_STATUS_REVIEW` in the operative
[registry](../../../00-uebersicht/RESEARCH_STATE.yaml).

## Result

On the same 19 cases and physical reference, the common Y-kernel model
improves the conditional total-angle upper bounds to **2.933357°** (central)
and **3.070163°** (quarter). The previously open **half** slice is newly
isolated on the maximal eigenvalue branch with width **3.642693°**. All five
known complete points remain contained and maximal. Root, the other two
slices and all eight diagnostic boxes remain unresolved. Those boxes are
not a cover of root, so no uniform localization or new adaptive tree follows.

The exact rational center solves Y_L X+Y_R=0. Common terms through degree
two propagate through N, moments and the scaled line equation. Componentwise
Neumann bounds pay the higher kernel remainder; all subsequent rounding and
truncation are paid. See [proof](PROOF.md), [19-case comparison](REPORT.md),
[exact summary](summary.json), [controls](controls.json) and [audit](audit.json).

## Reproduction and immutable source

The [sealed source archive](archives/Gemeinsamer-Y-Kernel-zweite-Ordnung-2026-10-03.zip)
contains 81 files, including all 59 unchanged Direct-Line original files.
[SOURCE_BINDINGS.json](SOURCE_BINDINGS.json) records every original hash;
[ACCEPTANCE.json](ACCEPTANCE.json) binds the completed local replay.

From the repository root with Python 3.13 and the package requirements:

```text
python -B research/x-c1/canonical-y-kernel-second-order-2026-10-03/replay.py --output <new-directory-outside-repository>
```

The wrapper verifies the closed publication manifest and original archive,
checks historical Git sources, runs all 19 cases, and requires byte-identical
comparison, controls, inherited controls, audit and summary receipts. It
preserves a receipt for the exact checked-out commit. The dedicated CI performs
the same full replay. No completed large operator integral or adaptive tree is
repeated by this new package.

The eight maximal-root certificates, 41 Newton steps, 19 exact center/tail
checks and eleven independent Arb angle checks are recorded in the audit.
The [acceptance plan](ACCEPTANCE_PLAN.json) fixes the required checks.
Uniform localization, renewal, A13 positivity, cofinal positivity, global
Object X and RH remain open. PR #187 remains separate. Existing proof anchors,
the global verification snapshot and external-review status are unchanged.
