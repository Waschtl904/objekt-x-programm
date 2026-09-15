# P11 Audit — Causal Volterra / passivity normal form

**Datum:** 15. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Operatorverdichtung des Critical-half-Finite-Part-Transfers.  
**Registry:** unveraendert.  
**Nonclaim:** kein Passivitaetsbeweis, kein Object-X-/RH-Abschluss, keine Publikationsneuheit.

---

## 0. Kurzurteil

Der pole-subtrahierte Prime-Diskrepanzoperator besitzt eine exakte **kausale Volterra-Faktorisierung** mit dem festen Critical-half-Port

```math
D_+=\partial_x+\frac12.
```

Definiere den kausalen Volterra-Operator

```math
\boxed{
(V_Jv)(x)
=\int_{-\infty}^{x}J_\Delta(x-y)v(y)dy,
}
```

wobei

```math
J_\Delta(L)
=e^{L/2}
\left(L-\gamma-\sum_{\log n<L}\frac{\Lambda(n)}{n}\right).
```

Mit

```math
D_-:=D_+^*=-\partial_x+\frac12
```

gilt auf glatten kompakt getragenen Funktionen exakt

```math
\boxed{
D_-V_J+V_J^*D_+
=2\gamma I+\mathcal C_\Delta,
}
```

wobei `C_Delta` der selbstadjungierte Faltungsoperator ist, dessen Quadratform

```math
\langle v,\mathcal C_\Delta v\rangle
=\int_0^\infty F_v(L)d\Delta(L)
```

ist.

Die verbleibende positive Gamma-Schicht `m>=1` besitzt zugleich eine kausale stabile Filterbankrealisierung. Fuer

```math
\mu_m=2m+\frac12,
\qquad
y_m=(\partial_x+\mu_m)^{-1}v,
```

gilt

```math
\boxed{
\int_0^\infty e^{-\mu_m t}\|K_tv\|_2^2dt
=\frac{2}{\mu_m}\|y_m'\|_2^2.
}
```

Damit wird die NULLPOL-Weilform zu

```math
\boxed{
Q_W(v)
=
\sum_{m=1}^\infty\frac{2}{\mu_m}\|y_m'\|_2^2
-c_*\|v\|_2^2
-2\operatorname{Re}\langle D_+v,V_Jv\rangle,
}
```

mit

```math
c_*
=\log(8\pi)+\frac\pi2-4-\gamma
=0.2177520894\ldots>0.
```

Dies ist eine radiusunabhaengige **Dissipation-minus-feedback**-Normalform. Der verbleibende Object-X-Gate kann daher als Passivitaets-/Storage-Problem eines kausalen Systems formuliert werden.

Status:

```text
Volterra factorization of C_Delta                       ✓[M]
fixed critical-half port D_+                            ✓[M]
causal higher-Gamma filter bank                         ✓[M]
causal dissipation-feedback normal form                 ✓[M]
positive storage / bounded-real certificate             ?[O]
RH / Object X                                           ?[O]
```

---

# 1. One-sided kernel as a distribution

Let

```math
j_+(t)=\mathbf1_{t\ge0}J_\Delta(t).
```

On `(0,infty)` the previous audit proved

```math
d\Delta
=\frac12J_\Delta(t)dt-dJ_\Delta(t).
```

As a distribution on the whole line, differentiating the Heaviside extension adds the root atom:

```math
dj_+
=\mathbf1_{t>0}dJ_\Delta+J_\Delta(0)\delta_0.
```

Since

```math
J_\Delta(0)=-\gamma,
```

we get

```math
\boxed{
\left(\frac12-\partial_t\right)j_+
=d\Delta+\gamma\delta_0.
}
```

Here `dDelta` is understood on the positive half-line and extended by zero to negative `t`.

---

# 2. Volterra operator factorization

Convolution by `j_+` is exactly

```math
(V_Jv)(x)
=\int_{-\infty}^xJ_\Delta(x-y)v(y)dy.
```

Applying

```math
D_-=-\partial_x+\frac12
```

to the output gives convolution by

```math
\left(\frac12-\partial_t\right)j_+
=d\Delta+\gamma\delta_0.
```

Hence `D_-V_J` has the positive-half discrepancy kernel plus `gamma I`. Its adjoint `V_J^*D_+` supplies the reflected negative-half kernel plus the second `gamma I`.

Therefore

```math
\boxed{
D_-V_J+V_J^*D_+
=\mathcal C_\Delta+2\gamma I.
}
```

In quadratic-form language,

```math
\boxed{
2\operatorname{Re}\langle D_+v,V_Jv\rangle
=2\gamma\|v\|_2^2
+\int_0^\infty F_v(t)d\Delta(t).
}
```

This is equivalent to the midpoint-coordinate transfer identity of the preceding audit but makes causality explicit.

---

# 3. Causal realization of one higher Gamma mode

For `mu>0` let

```math
y=(\partial_x+\mu)^{-1}v,
```

i.e. the stable causal first-order state satisfying

```math
y'+\mu y=v.
```

On the Fourier line,

```math
\widehat{y'}(z)
=\frac{iz}{\mu+iz}\widehat v(z).
```

Thus

```math
\frac{2}{\mu}\|y'\|_2^2
```

has multiplier

```math
\frac{2}{\mu}\frac{z^2}{z^2+\mu^2}.
```

But directly

```math
\int_0^\infty e^{-\mu t}\|K_tv\|_2^2dt
```

has the same multiplier because

```math
2\int_0^\infty e^{-\mu t}(1-\cos zt)dt
=\frac{2z^2}{\mu(z^2+\mu^2)}.
```

Therefore

```math
\boxed{
\int_0^\infty e^{-\mu t}\|K_tv\|_2^2dt
=\frac{2}{\mu}\|y'\|_2^2.
}
```

---

# 4. Higher-Gamma filter bank

The post-ground Gamma density is

```math
h_1(t)
=\sum_{m=1}^\infty e^{-\mu_m t},
\qquad
\mu_m=2m+\frac12.
```

By monotone convergence of the positive mode energies,

```math
\boxed{
\int_0^\infty h_1(t)\|K_tv\|_2^2dt
=\sum_{m=1}^\infty\frac{2}{\mu_m}\|y_m'\|_2^2,
}
```

where

```math
y_m=(\partial_x+\mu_m)^{-1}v.
```

Thus the entire positive remainder after removing the Gamma ground mode is a parallel bank of stable first-order causal dissipative channels.

---

# 5. Causal NULLPOL normal form

The Critical-half finite-part audit gave

```math
Q_W(v)
=
\int h_1(t)\|K_tv\|^2dt
-c_*\|v\|^2
-2\operatorname{Re}\langle D_+v,V_Jv\rangle.
```

Substituting the filter-bank realization gives

```math
\boxed{
Q_W(v)
=
\sum_{m=1}^\infty\frac{2}{\mu_m}\|y_m'\|_2^2
-c_*\|v\|_2^2
-2\operatorname{Re}\langle D_+v,V_Jv\rangle.
}
```

Every operator in this formula is now radius-independent. Compact support enters only through the input `v`; no prime cutoff or frequency truncation is present.

---

# 6. Passivity interpretation and firewall

The form has the schematic structure

```math
Q_W
=
\text{positive causal dissipation}
-
\text{fixed scalar leakage}
-
\text{Hermitian arithmetic feedback}.
```

This suggests a bounded-real/KYP-type question: can one construct a positive storage state `S(v)` from the stopped OU boundary-tail geometry so that

```text
positive Gamma dissipation + storage drop
>= arithmetic feedback + scalar leakage?
```

Such a theorem would be genuinely forward if the storage is fixed by the already-derived OU/overlap-cone system and not selected from the desired Weil inequality.

However no such storage certificate is currently known. Simply applying a generic realization theorem to a transfer function already defined from `Q_W` would be circular and is forbidden as an Object-X claim.

---

# 7. Why the route is different from fixed-window prolate

The prolate formulation encodes the arithmetic obstruction through a sign-changing Fourier multiplier whose dangerous frequency region grows doubly exponentially with the support radius under pointwise tail control.

The Volterra formulation instead uses one fixed causal kernel `J_Delta` on the half-line and restricts it automatically to the source support. There is no radius-dependent prime cutoff in the operator definition.

This does **not** prove that the Volterra route is easier; polynomial control of `J_Delta` is itself RH-scale. It does, however, remove the artificial pointwise-frequency-resolution barrier and exposes a different structural gate: causal passivity/storage rather than multiplier positivity.

---

# 8. Next gate

The next destructive task is to search for a **canonical storage functional** generated by the stopped OU boundary state

```math
Y(L)=\int_L^\infty e^{-(t-L)/2}X(t)dt
```

and the higher-Gamma filter states `y_m`, and test it first on the exact `R=1` Prime-2 mixed witness.

PASS criterion:

```text
a coefficient-free positive block/storage identity reproduces the exact
Volterra cross term and scalar c_*.
```

FAIL criterion:

```text
the natural OU storage class cannot reach the Prime-2 mixed calibration;
record the class no-go and do not fit free constants.
```
