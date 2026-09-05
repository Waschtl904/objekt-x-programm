# P11 / R43 — one-sided step-floor epsilon reserve criterion

**Date:** 2026-09-05  
**Scope:** sufficient summability criterion for an epsilon-defect majorant along any chosen cofinal chain satisfying the one-sided `e^{-4U}` lower step floor.  
**Status:** theorem-level conditional summability accelerator only. It does not prove the required epsilon defect estimate and does not imply PSD existence.

## 1. One-sided floor implies a step-count bound

Assume a chosen terminal chain satisfies eventually

\[
\boxed{
h_j:=U_{j+1}-U_j\ge c e^{-4U_j}}
\tag{OS1}
\]

for some `c>0`. Put

\[
x_j:=e^{4U_j}.
\]

Then, using `e^t-1>=t`,

\[
\begin{aligned}
x_{j+1}-x_j
&=x_j(e^{4h_j}-1)\\
&\ge4x_jh_j\\
&\ge4c.
\end{aligned}
\tag{OS2}
\]

Therefore

\[
\boxed{x_j\ge x_{j_0}+4c(j-j_0)}
\tag{OS3}
\]

for all sufficiently large `j`. Equivalently,

\[
\boxed{e^{-4U_j}=O(1/j).}
\tag{OS4}
\]

This is an **upper** density bound on the number of steps: the one-sided floor prevents a chain from being denser than order `e^{4U}`. It does not force floor saturation.

## 2. Exponential reserve greater than four is sufficient

Let `delta_j>=0` be a defect majorant on this chain. If for some `eta>0`

\[
\boxed{\delta_j\le C e^{-(4+\eta)U_j},}
\tag{OS5}
\]

then, since `x_j=e^{4U_j}`,

\[
\delta_j
\le C x_j^{-1-\eta/4}
=O(j^{-1-\eta/4}).
\tag{OS6}
\]

Hence

\[
\boxed{\sum_j\delta_j<\infty.}
\tag{OS7}
\]

Thus on **any chosen chain satisfying the one-sided floor (OS1)**, an epsilon upper bound with any fixed exponential reserve beyond exponent `4` is automatically summable.

Book:

```text
R43-COND-EPSILON-ONE-SIDED-FLOOR-RESERVE-SUFFICIENT ✓[M]
```

## 3. Relation to the harmonic firewall

The companion floor-dynamics audits prove:

- exact floor saturation gives `e^{-4U_j}~const/j`;
- two-sided floor comparability gives `e^{-4U_j}=Theta(1/j)`;
- therefore a defect bounded **below** by a positive multiple of `e^{-4U_j}` diverges on those dense chains.

The present result is complementary: it needs only the **one-sided** lower step floor, but it assumes an **upper** defect estimate with exponent strictly larger than `4`.

No claim is made that exponent `4` can never be summable on a sparser admissible chain. No unconditional `delta_j=o(1/j)` condition is booked.

## 4. Live research implication

For the epsilon-relaxed COND front, one concrete sufficient theorem shape is now:

\[
\sup_{\|x\|=1}(-\langle x,K_{U,U+h}^{\rm Schur}x\rangle)_+
\le C_X e^{-(4+\eta)U}
\tag{OS8}
\]

uniformly on a deliberately chosen cofinal terminal chain whose steps satisfy `h_j>=c e^{-4U_j}`. If such an operator or structured-range estimate were proved, the epsilon telescope would be summable by (OS7).

`R43-COND-EPSILON-RELAXED-TELESCOPE` remains `?[O]`: (OS8) itself is not proved.