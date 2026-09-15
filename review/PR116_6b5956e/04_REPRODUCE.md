# PR #116 — Reproduce the exact-head certificate

## Frozen source

The theorem/checker snapshot under review is exactly

```text
6b5956e69dfcb8124e8e31083613fd89c5f35fb3
```

Source PR #116 was a Draft and unmerged at this SHA.

**Do not substitute current `main` and do not silently rebase.**

## Pre-existing certificate implementation at the frozen head

Workflow:

```text
.github/workflows/np-prolate-1-arb.yml
```

Checker:

```text
scripts/check_np_prolate_1_arb.py
```

The workflow installs

```text
python-flint==0.9.0
```

and runs both sectors independently:

```text
python scripts/check_np_prolate_1_arb.py even
python scripts/check_np_prolate_1_arb.py odd
```

The job itself prints:

```text
git rev-parse HEAD
git hash-object scripts/check_np_prolate_1_arb.py
python --version
```

before using the checker output as the PASS gate.

## Exact-head GitHub status before this review package

Direct query of workflow runs associated with

```text
6b5956e69dfcb8124e8e31083613fd89c5f35fb3
```

returned **no run** for PR #116 before this review branch was opened.

Therefore the correct pre-review status is:

```text
Trace-minus-Ritz lemma                  ✓[M]
Arb certificate implementation         ✓[M]_part
NP-PROLATE-1 even at a=1/2              ?[O]
NP-PROLATE-1 odd at a=1/2               ?[O]
```

No PASS may be backfilled from floating/Nyström diagnostics.

## Review PR trigger

Review PR #125 was opened from

```text
review/critical-half-116-6b5956e-2026-09-15
```

**before any review-package file was committed.** At PR creation its head SHA was exactly

```text
6b5956e69dfcb8124e8e31083613fd89c5f35fb3.
```

This was done specifically so the pre-existing `pull_request` workflow could, if enabled by GitHub, create an execution tied to the frozen source SHA.

Subsequent commits on PR #125 add only the five review documents. They are not proof inputs for the frozen theorem/checker snapshot.

## Required evidence for promotion

To change either sector from `?[O]` to theorem-level PASS, record and audit all of:

1. workflow run attached to exact source SHA `6b5956e…`, or an equivalently immutable execution that explicitly checks out that SHA;
2. successful even job;
3. successful odd job;
4. full retained logs for both jobs;
5. printed checked-out SHA;
6. printed checker blob hash;
7. Python version and `python-flint==0.9.0` installation;
8. certified sign partition and tail lower bound;
9. certified shorted Gram positivity;
10. certified Cholesky/generalized Ritz inequalities;
11. final strict interval inequality before the PASS string.

## Local reproduction

A reviewer with the repository checked out can run:

```bash
git fetch origin
git checkout --detach 6b5956e69dfcb8124e8e31083613fd89c5f35fb3

git rev-parse HEAD
git hash-object scripts/check_np_prolate_1_arb.py

python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install python-flint==0.9.0

python scripts/check_np_prolate_1_arb.py even | tee np_prolate_1_even.log
python scripts/check_np_prolate_1_arb.py odd  | tee np_prolate_1_odd.log
```

Expected workflow gate strings are:

```text
NP-PROLATE-1 EVEN PASS ZERTIFIZIERT
NP-PROLATE-1 ODD PASS ZERTIFIZIERT
ALL REQUESTED NP-PROLATE-1 SECTORS PASS ZERTIFIZIERT
```

The strings are evidence only if they arise from a successful exact-source execution of the rigorous code path.

## Independent checker review before trusting a PASS

Even if both jobs are green, independently inspect these proof-critical points in `scripts/check_np_prolate_1_arb.py`:

- `verify_partition`: no uncovered frequency interval;
- root brackets: all uncertainty charged into `root_edge_trace_upper`;
- tail firewall: rigorous lower bound exceeds the sector `c`;
- parity normalization: no missing factor two;
- shorted kernel denominator: interval-certified positive;
- Ritz Gram: interval-certified SPD;
- `D_inner ≤ D`: follows from the certified positive inner subweight/subregions;
- `U G-A_inner`: interval-certified SPD;
- final bound uses upper trace/error data in the correct direction.

## Current promotion rule

Until the exact-head execution and logs are present and reviewed:

```text
NP-PROLATE-1 / a=1/2 remains ?[O].
```

A green run on a later source-modifying commit is not automatically a certificate for the frozen PR #116 snapshot.