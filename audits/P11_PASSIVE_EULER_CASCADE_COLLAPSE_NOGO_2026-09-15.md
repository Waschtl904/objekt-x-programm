# P11 Audit — Passive Euler cascade collapse no-go

**Datum:** 15. September 2026

## Result

For a prime `p` put

```math
F_p(s)=\frac{1-p^{-1/2}}{1-p^{-(s+1/2)}}.
```

For `Re s>0`, `F_p` is Schur; on the positive real axis `0<F_p(s)<1` and `F_p(0)=1`.

The inverse continuous Euler background is the Critical-half allpass

```math
b(s)=\frac{s-1/2}{s+1/2}.
```

Hence for every finite prime cutoff `P`,

```math
\Theta_P(s)=b(s)\prod_{p\le P}F_p(s)
```

is Schur. Its standard de-Branges/KYP cascade storage is positive and nonorthogonal across the cells.

However, for every fixed real `s>0`,

```math
\boxed{\Theta_P(s)\to0\qquad(P\to\infty).}
```

Indeed

```math
-\log F_p(s)
=\log\frac{1-p^{-(s+1/2)}}{1-p^{-1/2}}
=p^{-1/2}(1-p^{-s})+O(p^{-1}),
```

and the prime sum of the leading positive term diverges because `sum_p p^-1/2 = infinity`, while `p^-s -> 0`. Therefore the product tends to zero.

Consequently the Cayley positive-real transfer

```math
(1+Theta_P)/(1-Theta_P)
```

tends to the trivial constant `1` on the positive real axis (and any locally uniform analytic limit of the Schur products is the zero function).

## Meaning

The most direct nonorthogonal passive cross-prime architecture — ordinary cascade of the canonical local Schur cells, together with the Critical-half allpass — loses all arithmetic information in the infinite-prime limit.

A nontrivial global transfer therefore requires a **relative renormalization against the positive Riemann-R continuum background**. Such a renormalization is not automatically passivity preserving and cannot be inserted as a free scalar normalization.

```text
orthogonal local-cell sum                 insufficient
ordinary passive local-cell cascade       ×[M] in the direct-limit sense
relative discrete/continuum storage        ?[O]
```

No RH/Object-X conclusion is claimed.
