# Vor-iota' 7D finite-window cross-bridge firewall -- Draft package

**Status:** local Draft-PR package only; no repository write, no Registry promotion, no Object-X claim, no RH claim.

**Publication base to re-check before any push:** `main@5280471a550f2ce2b8a0e55d8a07646d82baff34` (PR #96 merge).

This package records a new post-PR-#96 negative result in a class that PR #96 explicitly left open: a canonical, positive, parameter-free pre-Schur/Mediator cross bridge at `R=1`.

Files:

- `audit.md` -- mathematical statement, bridge construction, Chebyshev/Arb certificate and exact scope;
- `provenienz.md` -- error/reconciliation chronology from the first unverified CG value to the Arb-hardened certificate;
- `../../scripts/check_vor_iota_prime_7D_harden.py` -- `python-flint` Arb-ball certificate, degree `N=13`, precision `200` bits.

Run from repository root after the package is placed in the repository tree:

```bash
python scripts/check_vor_iota_prime_7D_harden.py
```

Required Python dependency:

```text
python-flint
```

The checker deliberately performs **no small-amplitude pruning**.  It certifies every finite-window cutoff decision with Arb balls and verifies that all distinct final lobe centres are separated by more than `2*epsilon` before replacing the final `L^2` pairings by tuplewise coefficient pairings.

Expected mathematical conclusion:

```text
X_7D(a,b) lies in a certified interval approximately
[-0.0911347959, -0.0520968085],
whereas X_req = -(4+sqrt(2))*log(2)/32 approximately -0.1172764646.
Therefore X_req < X_lo and 7D d-exact FAILS.
```

The exact printed Arb balls, not the rounded decimal display above, carry the finite numerical certificate.

## Pre-push execution firewall

The package-preparation runtime used for this local assembly does not have `python-flint` installed, so the Arb checker could not be re-executed in that runtime.  The tuple/Chebyshev logic was independently shadow-reproduced there and gives the expected degree-13 central value and analytic tail.  **Before any push**, run the included Arb checker in the available `python-flint` environment and preserve its exact stdout (or an equivalent result file) for the pre-push audit.

## Governance

Intended sequence:

`local package -> pre-push package audit -> explicit push authorization -> Draft PR -> remote exact-head verification -> independent exact-head review -> merge decision`

Nothing in this package is a universal no-go for mediators, pre-Schur cross terms, Object X, or RH.
