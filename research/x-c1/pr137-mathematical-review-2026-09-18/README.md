# PR #137: scoped critical mathematical author review

Target: `8074d14508873e09068222b9703b1f34e8607fc6`.
Mathematical inputs anchored at `fc597f6129db57787c85ec20627ed608233187ba`.
Status remains **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Reviewer GPT 2 authored parts of the chain; this is not independent external review.

[REVIEW.md](REVIEW.md) gives the German decision, findings, scope and evidence.
[ANALYTIC_DETAILS.md](ANALYTIC_DETAILS.md) supplies the analytic arguments checked.
The positive scoped finding concerns all-source coercivity with gap 10^-13
for 0<a<=log(5)/2. No larger-window theorem or merge is asserted.

From repository root, with Python 3.10 or later, standard library only:

```text
python research/x-c1/pr137-mathematical-review-2026-09-18/check_review.py --verify
```

The checker verifies 44 input SHA-256 bindings, runs 678 exact/directed
interval regressions, compares its JSON/log byte for byte, and verifies
this package's SHA256SUMS. Allow several minutes. Run without Python -O
because assertions are certificate checks. `--write` deliberately regenerates
only the new JSON/log; it does not certify or repair historical packages.
An alternate repository root can be supplied with `--root PATH`.

The seven full endpoint/structural replays and historical manifest audit
are retained in `../pr137-consolidation-audit-2026-09-18/` unchanged.
The new checks supplement that evidence with alternate exact formulas.
The 678 checks include one EXPECTED rejection for coincident band limits;
its PASS documents an implementation limitation, not support for that case.

The original formula was compared with Suzuki arXiv:2606.09096v2 section 1.1:
https://arxiv.org/html/2606.09096v2 . See the review for the narrow source scope.

Append-only package. No historical proof, checker, result or manifest is edited.
The historical shell split remains invalid as described in finding R1;
this review does not supply its repair. The actual endpoint decomposition
has a separate valid closed-form-domain justification.
