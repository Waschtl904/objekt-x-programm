# Same-engine B calibration for the terminal Schur assembly

2026-09-20. AUDIT CALIBRATION ONLY. No terminal sign promotion.

This package applies the same Arb/Legendre/active-set assembly primitives used
by the terminal 191D enclosure candidate to the independently known positive
endpoint

    B = log(5)/2.

It is a release gate for the pending terminal package, not a new theorem.

## Calibration geometry

The endpoint calibration uses the canonical endpoint resolution N=63 and
Gamma degree M=64. Thus the Low dimensions are 31 per parity and the raw High
starts at degree 64 (even) or 65 (odd), exactly as in the frozen PR-137 endpoint
certificate.

The implementation imports the terminal package's helper functions for:

- rational Legendre polynomials;
- directed Arb matrices;
- Gamma polynomial construction;
- translated Legendre polynomials;
- exact Gauss-Legendre prime integrals;
- directed LDL factorization.

The only mathematical endpoint changes are:

- a = log(5)/2;
- active prime-power channels q = 2,3,4 (q=5 has zero-measure overlap);
- the endpoint canonical cutoff N=63 and Gamma degree M=64.

## Full High response

The calibration reconstructs the same complete coupling Gram architecture:

    Cgram = P_Y (V-K^p-S)^* (V-K^p-S) P_Z,

with V^2, S^2, V-S cross terms, finite Gamma-polynomial support beyond the
cutoff, and explicit Gamma/moment remainder budgets. It is not a sampled
High-mode test.

For each parity the independent High floor is rebuilt as

    delta_p =
      H_tail + q0
      - 2a(1/4-g(2a)+eps)
      - ||S||_bound
      - 80 eps_moment,

with all quantities directed in Arb. This is the same endpoint-tail formula
used by the frozen segment proof.

## Directed Schur test

With moment-corrected Low matrices A and complete coupling Gram G, the same
lower enclosure is used:

    L = A - (1001/1000) G/delta
          - (e + 1001 e^2/delta) I.

The calibration then applies the same directed LDL routine, computes an
inverse-trace lower bound sigma, the complete inverse-shear factor, and the
physical moment-map norm conversion.

PASS requires, in both parities:

1. delta > 0;
2. all directed LDL pivots of L are strictly positive;
3. the complete inverse-trace/shear/norm conversion is directed;
4. the final physical gap is strictly larger than 1e-13.

A positive midpoint is irrelevant.

## Audit meaning

If this calibration passes, it materially strengthens the claim that the
terminal assembly code is constructing the intended physical Schur object.
It does not by itself promote the pending terminal a=1 result: independent
review of the terminal High-floor direction and a pinned full terminal
--recompute replay are still required.

If this calibration fails or is undecided, the terminal candidate remains
PENDING_STATUS_REVIEW and TERMINAL-191D-DEFECT-SCHUR-A1 remains OPEN.
