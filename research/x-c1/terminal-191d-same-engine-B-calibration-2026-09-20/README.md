# Same-engine B calibration

Release-gate audit for the pending terminal 191D Schur candidate.

The GitHub workflow installs the pinned python-flint version and runs:

```text
python calibrate_B.py --output calibration_results.json
```

PASS requires a directed physical gap greater than `1e-13` in both parities.
No floating-point eigenvalue is used.
