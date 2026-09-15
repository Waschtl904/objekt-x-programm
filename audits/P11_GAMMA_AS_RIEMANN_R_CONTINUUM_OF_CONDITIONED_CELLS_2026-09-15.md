# P11 Audit — Gamma ladder as a Riemann-R continuum of conditioned P11 cells

**Datum:** 15. September 2026

## 0. Result

Let `h>0`, `k>=1`, `t=kh`, and define the P11-type primitive squared amplitude

```math
\alpha_{h,k}^2:=h e^{-3t/2}.
```

For the Gamma ladder

```math
\mu_m=2m+1/2,
\qquad m>=0,
```

define

```math
\boxed{
\beta_{h,k,m}^2
:=\frac{h e^{-\mu_m t}}{e^t-1}
=\frac{\alpha_{h,k}^2}{1-e^{-t}}e^{-2mt}.
}
```

With the positive Riemann-R density

```math
\rho(h)=\frac{d}{dh}R(e^h),
```

one has for every suitable source `v`

```math
\boxed{
\int_0^\infty\rho(h)
\sum_{k>=1}\beta_{h,k,m}^2\|K_{kh}v\|^2dh
=
\int_0^\infty e^{-\mu_m t}\|K_tv\|^2dt.
}
```

Thus every positive Gamma resolvent mode is a positive continuum average of the same root-conditioned logarithmic lattice cell family.

**Status:** exact positive identity `✓[M]`; no RH/Object-X conclusion.

---

## 1. Proof

The continuum-cell audit gives the unweighted pushforward identity

```math
\boxed{
\int_0^\infty\rho(h)
\sum_{k>=1}h\,\delta_{kh}(dt)dh
=(e^t-1)dt.
}
```

Multiply the test integrand at `t` by

```math
\frac{e^{-\mu_m t}}{e^t-1}\|K_tv\|^2.
```

The factor `e^t-1` cancels and yields exactly

```math
\int_0^\infty e^{-\mu_m t}\|K_tv\|^2dt.
```

The second expression for `beta` follows from

```math
e^t-1=e^t(1-e^{-t})
```

and `mu_m=2m+1/2`.

---

## 2. Ground mode and P11 root-conditioning

For `m=0`,

```math
\boxed{
\beta_{h,k,0}^2
=\frac{\alpha_{h,k}^2}{1-e^{-kh}}.
}
```

For a genuine prime spacing `h=log p`, put `q=p^-1/2`. The normalized stationary OU node at depth `k` has root correlation `q^k`; after conditioning out the common root, its residual variance is

```math
\boxed{1-q^{2k}=1-p^{-k}.}
```

Hence `beta_(p,k,0)^2` is precisely the primitive P11 squared amplitude divided by the root-conditioned residual variance.

---

## 3. Martingale multiplicity produces the Weil weight

The P11 rest multiplicity at channel depth `k` is exactly

```math
m_{p,k}=p^k-1.
```

Therefore

```math
\begin{aligned}
(p^k-1)\beta_{p,k,0}^2
&=(p^k-1)
\frac{(\log p)p^{-3k/2}}{1-p^{-k}}\\
&=(\log p)p^{-k/2}\\
&=\frac{\Lambda(p^k)}{\sqrt{p^k}}.
\end{aligned}
```

Thus

```math
\boxed{
\text{P11 rest multiplicity}
\times
\text{root-conditioned primitive precision cell}
=
\text{Weil p-power weight}.
}
```

This is an exact local identity, not a fitted exponent or asymptotic.

---

## 4. Higher Gamma modes

For fixed `(h,k)`,

```math
\beta_{h,k,m}^2
=\beta_{h,k,0}^2 e^{-2mkh}.
```

So the entire Gamma ladder is generated from the ground conditioned cell by a universal geometric round-trip damping in the separation `t=kh`.

Summing `m>=0` gives

```math
\sum_{m>=0}\beta_{h,k,m}^2
=\frac{h e^{-3kh/2}}
{(1-e^{-kh})(1-e^{-2kh})}.
```

Consequently the complete archimedean positive layer is a positive Riemann-R continuum of this two-stage conditioned/round-trip cell family.

---

## 5. Firewall

The identity explains local weights and multiplicities but does not compare the discrete prime sampling of the cells with their continuous Riemann-R average. That discrete-versus-continuum storage/sampling comparison remains the global RH-hard gate.

In particular, no claim is made that multiplying or averaging these positive cells makes the centered Weil form positive. The earlier no-gos for diagonal and ordinary cascade coupling remain in force.
