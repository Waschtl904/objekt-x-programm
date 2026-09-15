# P11 / Object X — Bulk–Trace gate after Euler-cell hard audit

**Datum:** 15. September 2026  
**Registry:** unveraendert.  
**Nonclaim:** kein RH-/Object-X-Beweis, keine Publikationsneuheit.

## 0. Current front

The surviving local geometry is now fixed.

Define

```math
X_v(t)=e^{-t/4}K_tv,
\qquad
\rho(h)=R'(e^h)e^h
=\sum_{j\ge1}\frac{h^{j-1}}{j!\zeta(j+1)}.
```

For `m>=0`, `k>=1`, define the bulk field

```math
\boxed{
(\mathcal G_m v)(h,k)
=e^{-mkh}\sqrt{\frac{h}{e^{kh}-1}}X_v(kh).
}
```

Then the Gamma mode `mu_m=2m+1/2` is exactly

```math
\boxed{
\|\mathcal G_m v\|^2_{L^2(\rho(h)dh;\ell^2_k;L^2_x)}
=\int_0^\infty e^{-\mu_m t}\|K_tv\|^2dt.
}
```

At a prime scale `h=log p`, the ground bulk satisfies

```math
\boxed{
(p^k-1)\|\mathcal G_0v(\log p,k)\|^2
=\frac{\log p}{p^{k/2}}\|K_{k\log p}v\|^2.
}
```

Hence:

```text
Gamma positive layer = continuum bulk norm;
Prime positive layer = weighted atomic trace of the same ground bulk field.
```

The P11 multiplicity `p^k-1` is exactly the trace multiplicity.

This is the current exact common geometry.

---

## 1. Equivalent OU interpretation

For each prime, the P11 Hub+Rest form is the covariance/state norm of the AR(1) tail state, while the positive p-power Weil tower is the inverse-covariance/precision norm of that same state.

At `h->0`, the discrete precision cells converge strongly to the archimedean Gamma resolvent modes. For mode `mu`,

```math
A_{h,\mu}=h\sum_{k\ge1}e^{-\mu kh}K_{kh}^*K_{kh}
\to
\frac2\mu D^2(D^2+\mu^2)^{-1}.
```

The convergence is never `L^2` operator-norm convergence because of aliasing, but after one source derivative it has the explicit graph-norm rate

```math
\|(A_{h,\mu}-A_{0,\mu})(1+D^2)^{-1/2}\|
\le(4+2/\mu)h.
```

Thus the correct gluing topology is strong/source-local, with quantitative graph-norm stability on smooth sources.

---

## 2. What the Riemann-R continuum supplies

The cell base density is the derivative of the classical Riemann R function. It satisfies

```math
\int_0^\infty\rho(h)\sum_{k\ge1}h\delta_{kh}(dt)dh
=(e^t-1)dt.
```

Disintegrating the left side over `t=kh` gives the probability weights

```math
\boxed{
\lambda_k(t)
=\frac{t\rho(t/k)}{k^2(e^t-1)},
\qquad \sum_{k\ge1}\lambda_k(t)=1.
}
```

Thus the smooth archimedean background has a canonical exponent-fibre decomposition; a genuine prime power `p^r` selects one specific exponent coordinate `r`.

However ordinary orthogonal shorting against this continuum is not the answer:
- collapsing `(h,k)` to depth `t` makes the continuum total and kills the arithmetic;
- pointwise exponent-fibre shorting reduces the exact Prime-2 mixed calibration and therefore fails if the Gamma baseline is left unchanged.

---

## 3. Exact local cell and archimedean boundary

For every `h>0`,

```math
B_h
=\sqrt{\frac{h q(1+q)}{1-q}}
(T_h-I)(I-qT_h)^{-1},
\qquad q=e^{-h/2},
```

compresses the complete logarithmic tower:

```math
B_h^*B_h
=\sum_{k\ge1}h e^{-kh/2}K_{kh}^*K_{kh}.
```

At `h=log p` this is the full p-power positive Weil tower. At `h=0` its strong boundary is the Gamma ground operator

```math
4D^2(D^2+1/4)^{-1}.
```

The actual prime scales do not approach zero (`log p>=log2`); the `h->0` statement is a boundary theorem for the continuous generalized cell family, not a limit of actual finite places.

---

## 4. Closed natural couplings

The following coefficient-free classes have now failed:

```text
root-only Prime/continuum coupling                     FAIL
ordinary common-depth OU Gram shorting                 FAIL (continuum totality)
pointwise exponent-fibre shorting with fixed Gamma     FAIL (Prime-2 calibration)
orthogonal sum of local passive cells                  insufficient
ordinary passive cascade of normalized Euler cells    FAIL (limit collapses to zero)
ordinary positive Sobolev regularity in scale h        not supplied by current energy;
                                                      high-frequency cell oscillation is too expensive
```

The last line is an architectural warning rather than a closed theorem class: any future scale-space norm must be derived explicitly and tested against high-frequency modulation before it is accepted.

---

## 5. Single remaining gate

The missing object is now a **relative scale-storage structure** which:

1. lives before the quotient `(h,k)->t=kh` so the base/factorization label is not lost;
2. couples atomic scales `h=log p` to the Riemann-R bulk `rho(h)dh`;
3. preserves the full exact Prime-2 mixed correction;
4. uses the already fixed local OU covariance/precision metrics, not fitted coefficients;
5. provides only the amount of scale regularity supported by the existing Gamma/P11 energy;
6. remains compatible with the strong, non-norm-continuous `h->0` archimedean boundary.

A successful construction would turn the prime layer into a genuine boundary/trace term of the positive Gamma/P11 bulk. Failure of every natural relative-storage kernel derived from the overlap cone would close this branch as an Object-X architecture while preserving the local identities as independent mathematics.
