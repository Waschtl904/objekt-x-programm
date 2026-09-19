# Scalar-gap restart summability barrier

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

This package proves a structural limitation of the two currently certified
restart laws.

1. The `ca3849a` restart halves the certified gap and allows width
   `h <= 2^(-ceil(1600/epsilon))`. Repeated use produces a summable
   super-geometric width sequence.
2. The `829019d` target-gap restart can preserve a positive limiting gap, but
   if `m_n=epsilon_n-epsilon_(n+1)` is summable then its sufficient width
   `h_n <= 2 exp(-16/m_n)` is also summable.

Therefore neither published scalar-global-gap mechanism can certify
non-summable transport by itself. This is a certificate-architecture
barrier, not a negative result for the Weil form.

Exact gap monotonicity also means that "reserve renewal" cannot mean making
the true optimal physical gap increase to the right. The preferred next
front is block-adaptive transport: isolate the finite soft block and pay the
hard tail/profile directions from their much larger internal reserves.
