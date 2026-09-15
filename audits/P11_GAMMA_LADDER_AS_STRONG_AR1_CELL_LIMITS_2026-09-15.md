# P11 Audit — Gamma ladder as strong AR(1) cell limits

**Datum:** 15. September 2026

## Result

For `mu>0` and `h>0` define

```math
A_{h,\mu}
:=\sum_{k\ge1}h e^{-\mu kh}K_{kh}^*K_{kh}.
```

This is the positive logarithmic-grid jump cell with AR(1) transition

```math
r=e^{-\mu h}.
```

Then

```math
\boxed{
A_{h,\mu}\xrightarrow[h\downarrow0]{\rm strong}
A_{0,\mu}
:=\frac2\mu D^2(D^2+\mu^2)^{-1}.
}
```

Moreover

```math
\boxed{\|A_{h,\mu}-A_{0,\mu}\|=\frac2\mu}
```

for every `h>0`. Thus every mode has the same strong-but-never-norm-continuous sampling boundary behavior.

For the Gamma ladder

```math
\mu_m=2m+1/2,
```

and the Critical-half P11 parameter `q=e^{-h/2}`,

```math
\boxed{e^{-\mu_m h}=q^{4m+1}.}
```

Hence the complete Gamma resolvent ladder is the family of strong `h=0` limits of logarithmic AR(1) cells with transition powers

```text
q, q^5, q^9, q^13, ...
```

The ground mode is exactly the P11 transition itself.

**Status:** `✓[M]`; no RH/Object-X conclusion.

---

## Multiplier proof

Let `r=e^{-mu h}`. The multiplier of `A_(h,mu)` is

```math
a_{h,\mu}(z)
=h\left[
\frac{1+r}{1-r}-P_r(zh)
\right].
```

For fixed `z`, as `h->0`,

```math
h\frac{1+r}{1-r}\to\frac2\mu,
```

and

```math
hP_r(zh)\to\frac{2\mu}{z^2+\mu^2}.
```

Therefore

```math
\boxed{
a_{h,\mu}(z)\to
\frac{2z^2}{\mu(z^2+\mu^2)}.}
```

This is exactly the Gamma-mode multiplier.

The Poisson bounds give

```math
0\le a_{h,\mu}(z)
\le\frac{4hr}{1-r^2}
=\frac{2h}{\sinh(\mu h)}
<\frac2\mu.
```

Thus dominated convergence proves strong convergence.

At the alias frequencies `z_n=2 pi n/h`, one has `a_(h,mu)(z_n)=0`, while the limiting multiplier tends to `2/mu` as `n->infinity`. Since both multipliers lie in `[0,2/mu]`, the operator-norm difference is exactly `2/mu`.

---

## Interpretation firewall

This is a structural discretization theorem, not an RH mechanism. The higher Gamma masses are already known from the digamma expansion; expressing them as AR(1) cell limits does not create a new positivity theorem. Its use is architectural: finite-prime P11 cells and archimedean Gamma cells belong to one semigroup family, while the unavoidable aliasing explains why the gluing must be strong/source-local rather than norm-uniform.
