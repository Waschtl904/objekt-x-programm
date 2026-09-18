# Reproduction and checker inventory

## Frozen inputs and environment

Mathematical/byte target: fc597f6129db57787c85ec20627ed608233187ba.
The consolidation commit adds only this directory. All historical inputs
are bound in frozen_inputs.json. Use an exact-byte checkout (disable Git
line-ending conversion) or the accompanying archive. Do not regenerate
old manifests before verification: doing so would erase the evidence of
mismatches. No network access is needed to run the checkers.

Fresh central replay used CPython 3.13 on Windows and the standard
library. All seven processes exited zero with empty stderr and left
historical input bytes unchanged. replay_results.json and replays/
record that execution, including stdout hashes and elapsed times. No
GitHub CI or independent external execution is claimed.

From the repository root:

```text
python research/x-c1/pr137-consolidation-audit-2026-09-18/check_consolidation.py
python research/x-c1/pr137-consolidation-audit-2026-09-18/check_consolidation.py --replay-scope
```

The first command rechecks all 134 byte bindings, all 19 historical
manifests, claim/source bindings, archived replay evidence and the new
payload manifest. It succeeds only if the documented five discrepant
manifests are reproduced exactly; it does NOT report them as repaired.
The second additionally reruns the seven central checkers. It may take
several minutes. Five use their native --verify mode; the two legacy
scripts run in temporary output directories. For those two, JSON is
compared semantically and stdout after CRLF/LF normalization; no
cross-platform raw-byte identity is claimed for generated legacy JSON.
The native --verify modes require exact committed JSON/log bytes.

Use --root PATH when the frozen repository files live elsewhere.
The supplied archive has a repository/ directory containing the bound
inputs and this package; it is a scoped snapshot, not a complete clone.
Python assert checks must be enabled: do not run with -O or -OO.

## Seven fresh central replays

| Package | Checker | Native mode | What its successful arithmetic supports |
|---|---|---|---|
| prime2-interval-continuation-2026-09-18 | check_interval.py | --verify | 22 endpoint/continuation groups; gap 10^-5 |
| prime3-transition-unified-shifts-2026-09-18 | check_prime3.py | --verify | 23 groups; gap 10^-11 |
| active-set-segment-schur-2026-09-18 | check_active_set_gram.py | no flags, isolated cwd | 381 exact finite algebra regressions |
| universal-prime-power-family-2026-09-18 | check_universal_family.py | --verify | 349 exact finite algebra regressions |
| prime-power-segment-4-2026-09-18 | check_segment.py | --verify | 15 endpoint groups; gap 10^-13 |
| near-null-source-transport-2026-09-18 | check_near.py | --verify | 27 groups, 435 Gamma identities, covers and directional tails |
| window-gap-monotonicity-2026-09-18 | check_window_gap_monotonicity.py | no flags, isolated cwd | 5 rational inequalities on imported source bounds; not an executable proof of the analytic monotonicity theorem |

All seven package manifests match. Different counts describe different
kinds of checks; adding them does not measure independent mathematical
verification. The shared code ancestry also prevents calling their
agreement an independent external audit.

## All 23 frozen C1 checkers

The full inventory includes 16 additional historical checkers. They were
byte-audited, not all rerun or promoted in this consolidation. List them:

```text
python research/x-c1/pr137-consolidation-audit-2026-09-18/check_consolidation.py --list-checkers
```

Run any one exactly identified inventory path with:

```text
python research/x-c1/pr137-consolidation-audit-2026-09-18/check_consolidation.py --run-checker research/x-c1/connected-3_8-2026-09-17/check_connected_constants.py
```

The wrapper selects --verify when present, otherwise uses an isolated
working directory, reports legacy JSON comparisons when available and
checks that inputs did not change. For archive-only scripts, successful
execution does not independently validate supplied decimal enclosures,
repair stale manifests, or certify their analytic claims. It does not
rerun their input generators automatically.

The additional frozen checkers are listed below. Paths are relative to
the repository root and can be passed directly to --run-checker.

- `research/x-c1/analytic-waxing-function-2026-09-17/check_x_c1_analytic_waxing_function.py`

- `research/x-c1/connected-193_500-2026-09-17/check_x_c1_connected_193_500.py`

- `research/x-c1/connected-19_50-2026-09-17/check_x_c1_connected_19_50.py`

- `research/x-c1/connected-387_1000-2026-09-17/check_x_c1_connected_387_1000.py`

- `research/x-c1/connected-3_8-2026-09-17/check_connected_constants.py`

- `research/x-c1/connected-49_125-rest-schur-2026-09-17/check_x_c1_rest_schur_49_125.py`

- `research/x-c1/full-residual-schur-19651_50000-2026-09-17/check_full_residual.py`

- `research/x-c1/full-residual-schur-3930110-2026-09-17/check_x_c1_full_residual_3930110.py`

- `research/x-c1/gamma-node-waxing-2026-09-18/check_gamma_node_waxing.py`

- `research/x-c1/gamma-residual-waxing-4096-2026-09-18/check_x_c1_gamma_residual_waxing_4096.py`

- `research/x-c1/node-schur-waxing-2026-09-17/check_x_c1_node_schur_waxing.py`

- `research/x-c1/node-schur-waxing-function-2026-09-17/check_x_c1_node_schur_function.py`

- `scripts/check_x_c1_endpoint_green_bridge.py`

- `scripts/check_x_c1_sparse_graph.py`

- `scripts/check_x_c1_storage_prefix.py`

- `scripts/check_x_c1_three_cell_constants.py`

The separate archival generator
`research/x-c1/gamma-residual-waxing-4096-2026-09-18/generate_gamma_residual_waxing_4096_intervals.py`
requires mpmath and is not one of the 23 checkers. It was not rerun and
is not an input dependency of the consolidated endpoint at log(5)/2.
Its old README describes its interval-generation role. If inspecting
it, run a disposable copy; do not replace committed enclosure inputs
or equate generator execution with proof validation.

Analytic obligations, especially the original form identity, closed
form domain, infinite Parseval identities and final norm argument,
still require mathematical review. See DEPENDENCIES.md.
