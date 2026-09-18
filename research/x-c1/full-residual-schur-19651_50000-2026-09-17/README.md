# FULL-RESIDUAL-SCHUR: 19651/50000

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.** Append-only continuation of
corrected mathematical anchor `9aa5cb1edac72fc683c5c9aba5a1f0639fbbf8bb`
on `research/x-c0-common-memory-2026-09-16`, PR #137. No merge.

At **a = 19651/50000 = 0.39302**, the joint retained block contains the
outer Node reserve, the entire nonconstant Gamma residual, and the entire
Prime-2 difference energy. Its actual infinite-dimensional Schur pivot
is **> 1/50**. The actual inverse shear has norm **< 3/2**. After the
global moment penalty and division of the whole numerator by
**1 + beta_even**, the full connected NULLPOL class has **Q_W[u] >
||u||^2 / 150** for nonzero u. The odd sector has gap > 1/4.

Read [PROOF.md](PROOF.md) for the exact form comparison, domains, tail
bounds, normalization, and scope. No third moment, A1, quadrature, or
floating-point evidence is used. All constants are recomputed by the
self-contained rational checker; no decimal intervals are imported.

From this directory (or supply the checker's full path):

```text
python check_full_residual.py --verify
```

This reruns **16 arithmetic checks**, compares the computed JSON/log
against the saved bytes, and checks the five SHA-256 manifest entries.
`--write` regenerates only JSON and log. A read-only run is the default.
The complete payload is `PROOF.md`, the checker, JSON, log, and this
README; `SHA256SUMS` covers these five files, excluding itself.

Use repository LF bytes (disable checkout line-ending conversion) when
checking hashes. Existing historical artifacts are untouched. This is
a point certificate, not a maximal-window theorem or external approval.
