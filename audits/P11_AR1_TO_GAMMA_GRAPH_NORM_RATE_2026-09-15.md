# P11 Audit — Graph-norm rate for the AR(1)-to-Gamma cell limit

**Datum:** 15. September 2026

## Result

For `mu>0`,

```math
A_{h,\mu}
=h\sum_{k\ge1}e^{-\mu kh}K_{kh}^*K_{kh},
```

and

```math
A_{0,\mu}
=\int_0^\infty e^{-\mu t}K_t^*K_tdt
=\frac2\mu D^2(D^2+\mu^2)^{-1}.
```

Although

```math
\|A_{h,\mu}-A_{0,\mu}\|=2/\mu
```

for every `h>0`, one has the quantitative graph-norm estimate

```math
\boxed{
\|(A_{h,\mu}-A_{0,\mu})(1+D^2)^{-1/2}\|
\le\left(4+\frac2\mu\right)h.
}
```

In particular, for the Critical-half ground mode `mu=1/2`,

```math
\boxed{
\|(A_{h,1/2}-A_{0,1/2})(1+D^2)^{-1/2}\|
\le8h.
}
```

Thus the failure of bare `L^2` norm convergence is purely a high-frequency aliasing obstruction; after paying one derivative, the discrete-to-archimedean cell transition is operator-norm continuous with linear rate.

**Status:** `✓[M]`.

---

## Proof

At Fourier frequency `z`, define

```math
f_z(t)=2e^{-\mu t}(1-\cos zt).
```

Then the multipliers are

```math
a_{h,\mu}(z)=h\sum_{k\ge1}f_z(kh),
\qquad
a_{0,\mu}(z)=\int_0^\infty f_z(t)dt.
```

For an absolutely continuous function with `f_z(0)=0`, the right-Riemann-sum error satisfies

```math
\left|h\sum_{k\ge1}f_z(kh)-\int_0^\infty f_z(t)dt\right|
\le h\int_0^\infty|f_z'(t)|dt.
```

Indeed, on each interval `((k-1)h,kh]`, integrate

```math
|f_z(kh)-f_z(t)|
\le\int_t^{kh}|f_z'(u)|du
```

and sum.

Now

```math
f_z'(t)
=-2\mu e^{-\mu t}(1-\cos zt)
+2z e^{-\mu t}\sin zt,
```

so

```math
\int_0^\infty|f_z'(t)|dt
\le4+\frac{2|z|}{\mu}.
```

Hence

```math
\frac{|a_{h,\mu}(z)-a_{0,\mu}(z)|}
{\sqrt{1+z^2}}
\le h\left(
\frac4{\sqrt{1+z^2}}
+\frac{2|z|}{\mu\sqrt{1+z^2}}
\right)
\le h\left(4+\frac2\mu\right).
```

Taking the essential supremum proves the claim.

---

## Interpretation

The strong-but-not-norm cell limit and the earlier Strong-Terminal behavior have the same geometry: raw `L^2` permits arbitrarily high-frequency vectors tuned to the lattice aliasing, whereas every fixed smooth source pays a derivative and sees a stable limit.

This estimate does not prove any Weil positivity. It only hardens the finite-place/archimedean gluing topology and shows that the archimedean boundary is quantitatively accessible in natural graph norms.
