# X-C1 connected crossing — a=387/1000

Append-only research package for PR #137.

Status: `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

Contents:
- `X_C1_CONNECTED_CROSSING_387_1000.md` — analytic proof note.
- `check_x_c1_connected_387_1000.py` — standard-library exact rational checker.
- `connected_387_1000_checks.log` — local checker stdout, 22 PASS.
- `connected_387_1000_results.json` — compact exact/rational result summary.
- `SHA256SUMS` — hashes of the five package files above including this README.

Scope: full connected source class
`H1_0((-387/1000,387/1000)) ∩ ker E_+ ∩ ker E_-`.

At this point the OLD `1/5` scalarized Gamma split has exact `lambda_2=-1/5000`.
The package proves that retaining the larger positive Gamma constant `43/200`
restores `lambda_2=1141/100000>0`, keeps the two-moment defect contractive,
and yields `Q_W >= (2687/250100)||u||^2 > (1/100)||u||^2`.

This is a controlled crossing/rescue of the selected lower form, not a statement
that the full Weil form ever became negative. Prime 2 is active; Prime 3 is not.
No A1 import, unit-window closure, all-window claim, Object X or RH claim.
