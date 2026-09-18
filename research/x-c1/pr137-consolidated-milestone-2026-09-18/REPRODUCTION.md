# Reproduction index

All theorem packages below are `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

## Required endpoint and structural packages

### Prime-2 interval to `log(3)/2`

Path: `research/x-c1/prime2-interval-continuation-2026-09-18/`

```text
python check_interval.py --verify
```

Expected saved result: uniform `Q_W[u] > ||u||^2 / 100000` on `0<a<=log(3)/2`.

### Prime-2/3 interval to `log(2)`

Path: `research/x-c1/prime3-transition-unified-shifts-2026-09-18/`

```text
python check_prime3.py --verify
```

Expected: 23 check groups PASS and uniform `Q_W[u] > ||u||^2 / 100000000000` on `0<a<=log(2)`.

### Universal prime-power family

Path: `research/x-c1/universal-prime-power-family-2026-09-18/`

```text
python check_universal_family.py --verify
```

Expected: 349 exact structural regressions and five payload hashes PASS.

### Active-set segment Schur

Path: `research/x-c1/active-set-segment-schur-2026-09-18/`

The checker is an algebra-regression checker rather than a full package replay harness. Run it in a temporary directory if byte-preservation of the committed result file is desired:

```text
python /path/to/repo/research/x-c1/active-set-segment-schur-2026-09-18/check_active_set_gram.py
```

Expected: 381 exact Fraction checks PASS across both overlapping `d<1` and disjoint `d>1` regimes.

### Prime-power 4 endpoint `log(5)/2`

Path: `research/x-c1/prime-power-segment-4-2026-09-18/`

```text
python check_segment.py --verify
```

Expected: verdict CLOSED at author level and uniform gap `1/10000000000000` on `0<a<=log(5)/2`.

## Diagnostic packages

### Near-null source transport

Path: `research/x-c1/near-null-source-transport-2026-09-18/`

```text
python check_near.py --verify
```

Expected: direct reconstruction of the near-null source, continuum positivity for that selected transported family through `log(7)/2`, complete directional-tail checks, and no all-source theorem at `log(7)/2`.

### Window-gap monotonicity

Path: `research/x-c1/window-gap-monotonicity-2026-09-18/`

```text
python check_window_gap_monotonicity.py
```

Expected: exact quantitative consistency checks for the inherited source ceiling. The monotonicity theorem itself is analytic and follows from exact zero-extension functoriality.

## Hash discipline

Where a package contains `SHA256SUMS`, verify the committed payload hashes in addition to rerunning the checker. A successful checker run is not an external mathematical review.

Historical packages remain preserved. Known historical manifest/provenance corrections are not silently rewritten; the corrected green chain above should be used for the consolidated milestone.
