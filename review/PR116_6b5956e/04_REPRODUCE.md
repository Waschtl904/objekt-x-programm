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

## Review PR / CI trigger audit

Review PR #125 is stacked directly on

```text
research/critical-half-green-tree-bridge-2026-09-13
```

whose base SHA is the frozen source

```text
6b5956e69dfcb8124e8e31083613fd89c5f35fb3.
```

The review branch itself was created exactly from that SHA and changes only the five documents under `review/PR116_6b5956e/`.

Two trigger attempts were checked:

1. PR #125 was initially opened while its head still equaled exact source SHA `6b5956e…`;
2. after stacking it on the PR #116 research branch, a neutral synchronize commit was created and then removed.

Neither produced a recorded pull-request workflow run. The neutral trigger file is not present in the final diff.

The relevant infrastructure fact is that `np-prolate-1-arb.yml` is introduced by the unmerged PR #116 research branch and is not registered on current default branch `main`. We do **not** modify `main` merely to force CI.

Therefore GitHub Actions currently supplies no exact-head certificate evidence.

## Local execution status in the review environment

A second independent execution route was tested in the review runtime. It cannot currently execute the frozen checker because:

```text
python-flint is not installed
```

and the runtime has no external network resolution from which to install `python-flint==0.9.0` or clone the repository.

This is an infrastructure limitation, **not** a mathematical failure and not a certificate PASS.

## Required evidence for promotion

To change either sector from `?[O]` to theorem-level PASS, record and audit all of:

1. an immutable execution of frozen theorem/checker source `6b5956e…` (or a documentation-only descendant whose checker/workflow blobs are independently shown identical);
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

A reviewer with the repository checked out and network/package access can run:

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

The strings are evidence only if they arise from a successful immutable-source execution of the rigorous code path.

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

Until the immutable-source execution and logs are present and reviewed:

```text
NP-PROLATE-1 / a=1/2 remains ?[O].
```

A green run on a later source-modifying commit is not automatically a certificate for the frozen PR #116 snapshot.