# P11 Audit — Common-depth OU shorting totality no-go

**Datum:** 15. September 2026

## Result

For `h>0`, `k>=1`, define the normalized OU innovation cell

```math
\eta_{h,k}(t)
=\frac{\mathbf 1_{((k-1)h,kh]}(t)e^{-(kh-t)/2}}
{\sqrt{1-e^{-h}}}.
```

For fixed `h`, the family in `k` is orthonormal in `L^2(R_+,dt)`. Hence the most direct nonorthogonal discrete/continuum coupling is to place all prime cells and all Riemann-R continuum cells in this common depth space and use their ordinary Gram overlaps.

This architecture collapses: the continuum family is already total in the common depth space.

Indeed its `k=1` vectors are

```math
\eta_{h,1}(t)=c(h)e^{t/2}\mathbf 1_{(0,h]}(t),
\qquad c(h)\ne0.
```

Because the Riemann-R density `rho(h)` is strictly positive for every `h>0`, all these vectors occur in the continuum support. Their linear span is dense in `L^2(R_+)`: differences of the weighted initial-interval indicators generate weighted compactly supported step functions, and those are dense.

Therefore every discrete prime cell `eta_(log p,k)` lies in the closed span of the continuum cells. Orthogonal shorting of the joint Gram against the full continuum block removes the discrete side completely.

In geometric Schur-complement notation,

```math
\boxed{A_P-B A_C^{-1}B^*=0}
```

where this is understood as the shorted operator / projection onto the orthogonal complement of the closed continuum feature span (not as a claim that an unbounded literal matrix inverse exists).

## Consequence

```text
common depth embedding + ordinary Gram overlap + orthogonal shorting   ×[M]
```

The common OU depth geometry is too complete to retain arithmetic information. A nontrivial relative storage mechanism must preserve additional structure not visible in the depth vector alone, for example:

```text
- the scale/base variable h itself,
- the physical overlap-cone x-incidence,
- or a relative/renormalized boundary form.
```

This does not invalidate the exact discrete/continuous precision identities. It only excludes the simplest canonical Schur complement on the shared `L^2(dt)` innovation space.

No RH/Object-X claim.
