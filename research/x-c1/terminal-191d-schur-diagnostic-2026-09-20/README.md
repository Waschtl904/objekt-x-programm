# Terminal 191D Schur diagnostic preflight

Local-only diagnostic for `TERMINAL-191D-DEFECT-SCHUR-A1`.

Run:

```text
python diagnose_terminal_schur.py --nx 900 --nt 300 --high 32 --json terminal_schur_diag.json
```

Requires NumPy and SciPy. The mandatory calibration at `B=log(5)/2` fails,
so the raw `a=1` signs are not mathematical evidence. See `PROOF.md`.
