# P11 Audit — Archimedean ground as the strong h=0 cell limit

**Datum:** 15. September 2026

## 0. Result

For `h>0`, put `q=e^{-h/2}` and

```math
A_h:=B_h^*B_h
=\sum_{k\ge1}h e^{-kh/2}K_{kh}^*K_{kh}.
```

Then

```math
\boxed{
A_h\xrightarrow[h\downarrow0]{\rm strong}
A_0:=\int_0^\infty e^{-t/2}K_t^*K_tdt
=4D^2(D^2+1/4)^{-1}.
}
```

Thus `A_0` is exactly the Gamma ground mode.

However the convergence is maximally non-uniform:

```math
\boxed{\|A_h-A_0\|=4\quad\text{for every }h>0.}
```

So the archimedean ground is a genuine strong boundary point of the same Euler/AR(1) cell family, but never an operator-norm limit.

**Status:** `✓[M]`.

---

## 1. Multipliers

Let `z` denote Fourier frequency. Since

```math
A_h=\sum_{k\ge1}h q^kK_{kh}^*K_{kh},
```

its multiplier is

```math
\boxed{
a_h(z)
=h\left[
\frac{1+q}{1-q}-P_q(zh)
\right],
}
```

where

```math
P_q(\theta)=\frac{1-q^2}{1-2q\cos\theta+q^2}
```

is the disk Poisson kernel.

For fixed `z`, Taylor expansion at `h=0` gives

```math
P_{e^{-h/2}}(zh)
=\frac1{h(z^2+1/4)}+O(1),
```

and

```math
h\frac{1+q}{1-q}=4+O(h^2).
```

Hence

```math
\boxed{
a_h(z)\to
4-\frac1{z^2+1/4}
=\frac{4z^2}{z^2+1/4}
=:a_0(z).}
```

This is exactly the multiplier of the `mu_0=1/2` Gamma resolvent mode.

---

## 2. Uniform domination and strong convergence

The Poisson kernel satisfies

```math
\frac{1-q}{1+q}\le P_q(\theta)\le\frac{1+q}{1-q}.
```

Therefore

```math
0\le a_h(z)
\le h\left[
\frac{1+q}{1-q}-\frac{1-q}{1+q}
\right]
=\frac{4hq}{1-q^2}
=\frac{2h}{\sinh(h/2)}<4.
```

Also `0<=a_0(z)<4`. Pointwise convergence plus bounded dominated convergence yields

```math
\|(A_h-A_0)v\|_2\to0
```

for every `v in L^2(R)`.

---

## 3. Exact norm failure by aliasing

At every alias frequency

```math
z_n=\frac{2\pi n}{h},
```

one has `P_q(z_nh)=(1+q)/(1-q)`, hence

```math
a_h(z_n)=0.
```

But

```math
a_0(z_n)\to4
\qquad(n\to\infty).
```

Thus

```math
\|A_h-A_0\|\ge4.
```

The uniform bounds `0<=a_h,a_0<=4` give the reverse inequality, so

```math
\boxed{\|A_h-A_0\|=4.}
```

This is an exact sampling-aliasing obstruction, not a numerical effect.

---

## 4. Centered cells and the archimedean place

The centered cell uses

```math
c(h)=\frac{h e^{-h/2}}{1-e^{-h/2}}\to2,
```

so for every fixed source

```math
C_v(h)=\langle v,A_hv\rangle-2c(h)\|v\|^2
```

has the strong boundary value

```math
\boxed{
C_v(0)
=\langle v,A_0v\rangle-4\|v\|^2.
}
```

On NULLPOL the complete Weil form can therefore be written

```math
\boxed{
Q_W(v)
=C_v(0)+\sum_pC_v(\log p)
+E_{Gamma,>=1}(v)
-(\kappa_*-4)\|v\|^2.
}
```

The scale set `h=0` together with `h=log p` thus treats the Gamma ground and finite prime places as one strong cell family.

---

## 5. Interpretation firewall

This is not an adelic proof and not an Object-X completion. The lack of norm continuity is essential: high-frequency aliasing prevents any uniform cell-limit argument. Any global construction must therefore use a strong/source-local topology or an additional smoothing/storage mechanism.
