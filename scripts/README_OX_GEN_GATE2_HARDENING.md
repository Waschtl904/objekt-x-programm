# OX-GEN / Gate-2 hardening note

The external Gate-2 scripts supplied on 2026-09-12 are not committed verbatim as theorem certificates.

Before a repository certificate is accepted, the following changes are required:

1. include the omitted Bernoulli-series tail of `r_1''` in every Arb enclosure, or use the closed form
   `r_1''(u)=exp(u/2)/(2*sinh(u))-1/(2*u)` with removable value `r_1''(0)=1/4`;
2. decide the prime-power cutoff by Arb comparisons against `exp(2a)`, not by `float(exp(2a))`;
3. replace float-valued endpoint-error factors by proven Arb upper bounds;
4. use direct Arb positivity comparisons for Cholesky pivots;
5. rerun the full three-radius/two-parity Gate-2 matrix test before any `certificate` or `frozen` status is claimed.

For `|u|<=2` and `N=340`, the omitted Bernoulli tail is bounded by

```math
|R_N(u)|\le \frac{\zeta(2)}{2}\frac{(2/\pi)^{N+1}}{1-2/\pi},
```

which is about `3.1e-67` at `N=340`; the issue is formal enclosure, not expected numerical size.

This note is a hardening checklist, not a theorem, certificate, or Registry promotion.
