# Terminal 191D Schur diagnostic

This package is a diagnostic precursor to the canonical gate
`TERMINAL-191D-DEFECT-SCHUR-A1`.

It reconstructs a moment-neutral 191/883 finite-head Schur model from the
hash-fixed Even/Odd Legendre integer artifacts and evaluates the Schur matrix
with Arb ball arithmetic.

It is deliberately **not** a positivity theorem for the exact terminal
matrices. The exact-moment comparison, finite-model error ledger and infinite
Legendre-tail/omitted-frequency comparison remain to be hardened.

Run via the dedicated GitHub Actions workflow
`terminal-191d-schur-diagnostic.yml`.
