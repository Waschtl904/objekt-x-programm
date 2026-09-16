# X-C0 — Critical asymptotic of the unresolved P11 Boundary tail

**Datum:** 16. September 2026  
**Basis:** exact `J_Delta = transport defect + P11 boundary tails` decomposition on this stacked audit.  
**Registry:** unverändert.  
**External input:** classical unconditional Prime Number Theorem / Chebyshev bound only.  
**Nonclaim:** kein RH-/Object-X-/NP-GAP-Beweis, kein Neuheitsclaim fuer die verwendeten Primzahlsummen.

---

## 0. Result

Recall

```math
h_p=\log p,
\qquad
J_p(L)=\left\lfloor\frac{L}{h_p}\right\rfloor,
```

and the unresolved safe P11 Root-tail mass

```math
U_p(L)
=\frac{h_p p^{-J_p(L)}}{p-1}
=h_p\sum_{k>J_p(L)}p^{-k}.
```

Set

```math
\boxed{
T(L):=\sum_{h_p<L}U_p(L).
}
```

Then

```math
\boxed{
e^{L/2}T(L)\longrightarrow1
\qquad(L\to\infty),
}
```

at non-jump `L` (and equivalently for either one-sided convention away from a vanishing set of thresholds).

Combining this with the exact identity

```math
 e^{-L/2}J_\Delta(L)
 =d_{tr}(L)+T(L),
```

where

```math
 d_{tr}(L)
 =L-\gamma-
  \sum_{p<e^L}\frac{\log p}{p-1},
```

gives

```math
\boxed{
J_\Delta(L)
=1+e^{L/2}d_{tr}(L)+o(1).
}
```

Thus the higher-p-power unresolved P11 Boundary tails contribute a positive, asymptotically universal critical channel. All nontrivial critical growth/oscillation left in `J_Delta` is carried by the **prime-base transport discrepancy** `d_tr`.

Status:

```text
critical boundary-tail limit e^(L/2)T(L)->1       ✓[K/M] (classical PNT input)
exact J_Delta decomposition                         ✓[M]
critical difficulty isolated in e^(L/2)d_tr         ✓[K/M]
RH-scale bound for d_tr                              ?[O]
```

---

# 1. Rewrite with `x=e^L`

Put

```math
x=e^L.
```

Then

```math
J_p(L)=\lfloor\log_p x\rfloor.
```

Hence

```math
\sqrt{x}\,T(\log x)
=
\sum_{j\ge1}
\sqrt{x}
\sum_{x^{1/(j+1)}<p<x^{1/j}}
\frac{\log p}{(p-1)p^j}.
```

Only finitely many `j` occur, namely `j<=log_2 x`.

Call the j-th contribution `T_j(x)`.

---

# 2. The `j=1` layer gives the limit one

For

```math
\sqrt{x}<p<x
```

we have `J_p=1`, so

```math
\sqrt{x}\,T_1(x)
=\sqrt{x}
\sum_{\sqrt{x}<p<x}
\frac{\log p}{p(p-1)}.
```

Since

```math
\frac1{p(p-1)}
=\frac1{p^2}+O(p^{-3}),
```

the difference between this and

```math
\sqrt{x}
\sum_{\sqrt{x}<p<x}
\frac{\log p}{p^2}
```

tends to zero.

By partial summation from the Prime Number Theorem,

```math
\boxed{
\sum_{p>y}\frac{\log p}{p^2}
\sim\frac1y.
}
```

Therefore

```math
\begin{aligned}
\sqrt{x}
\sum_{\sqrt{x}<p<x}
\frac{\log p}{p^2}
&=\sqrt{x}
\left[
\frac1{\sqrt{x}}-\frac1x+o(x^{-1/2})
\right]\\
&\longrightarrow1.
\end{aligned}
```

Thus

```math
\boxed{\sqrt{x}\,T_1(x)\to1.}
```

---

# 3. All `j>=2` layers vanish

Use `p-1>=p/2`. Then

```math
\sqrt{x}\sum_{j\ge2}T_j(x)
\le
2\sqrt{x}
\sum_{j=2}^{\lfloor\log_2x\rfloor}
\sum_{p>x^{1/(j+1)}}
\frac{\log p}{p^{j+1}}.
```

A classical Chebyshev bound

```math
\vartheta(t)=\sum_{p\le t}\log p\le Ct
```

and Stieltjes partial summation imply, uniformly for `j>=2`,

```math
\sum_{p>y}
\frac{\log p}{p^{j+1}}
\le C_1 y^{-j}
```

with an absolute `C_1`.

Take

```math
y=x^{1/(j+1)}.
```

Then the j-th majorant is

```math
C_2
x^{1/2-j/(j+1)}
=
C_2
x^{-(j-1)/(2(j+1))}.
```

For every `j>=2`,

```math
\frac{j-1}{2(j+1)}\ge\frac16.
```

There are at most `O(log x)` nonempty layers, hence

```math
\boxed{
\sqrt{x}\sum_{j\ge2}T_j(x)
=O(x^{-1/6}\log x)
\to0.
}
```

Together with Section 2 this proves the main limit.

---

# 4. Meaning for the C1 architecture

The exact scalar coefficient was

```math
 e^{-L/2}J_\Delta(L)
 =d_{tr}(L)+T(L).
```

The present theorem says

```math
 e^{L/2}T(L)=1+o(1).
```

Therefore the unresolved p-power Boundary tail itself is **not** the RH-hard growth channel. After the Critical-half scaling it asymptotically stabilizes.

The entire nontrivial critical problem is pushed into

```math
\boxed{e^{L/2}d_{tr}(L).}
```

This agrees with the analytic decomposition of the Euler product: higher prime powers form an absolutely better-convergent correction, while the first-prime layer carries the critical continuation difficulty.

The result also gives a useful review firewall:

```text
Do not spend further effort trying to regularize the higher p-power P11 tail.
Its critical normalization is already asymptotically benign.
The hard gate is the signed prime-base transport coordinate.
```

---

# 5. Relation to the lossless supply parent

In the lossless auxiliary pair

```math
R_L=r_L\oplus b_L,
\qquad
S_L=q_L\oplus b_L,
```

the common positive tail component satisfies

```math
\|b_L\|^2=T(L).
```

Thus its Critical-half energy scale obeys

```math
\boxed{e^{L/2}\|b_L\|^2\to1.}
```

The asymptotically difficult piece of the positive completion is therefore not the P11 tail state but the oriented transport strip representing `d_tr`.

No positivity statement about the full IN/OUT supply follows; this is a localization of the remaining difficulty, not its solution.
