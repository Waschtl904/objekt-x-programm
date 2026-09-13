# P11 Audit — Trace-minus-Ritz certificate for the shorted NP prolate defect

**Datum:** 13. September 2026  
**Branch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level certification lemma plus unc ertified `a=1/2` diagnostics.  
**Registry:** unveraendert.  
**Nonclaim:** the numerical margins below are not yet Arb-certified and therefore are not yet a theorem-level NP-GAP PASS.

---

## 0. Purpose

The previous prolate audit reduces the finite-window NULLPOL Weil form to a compact weighted prolate defect.

For a fixed `a>0`, let

```math
\mathcal N_a
=\{F\in PW_a:F(i/2)=F(-i/2)=0\},
```

and let `tau_a` be the canonical centered finite-window multiplier.

For any `c>0` define

```math
\boxed{
D_{a,c}
:=
P_{\mathcal N_a}
M_{(c-\tau_a)_+}
P_{\mathcal N_a}.
}
```

Since `(c-tau_a)_+` has compact support, `D_{a,c}` is positive trace class.

Pointwise

```math
\tau_a(z)
\ge
c-(c-\tau_a(z))_+,
```

hence for `F in N_a`

```math
\boxed{
Q_W(F)
\ge
c\|F\|^2
-\langle F,D_{a,c}F\rangle.
}
```

Therefore

```math
\boxed{
\|D_{a,c}\|<c
\quad\Longrightarrow\quad
Q_W(F)>0
\ \text{for all }0\ne F\in\mathcal N_a.
}
```

The point of this audit is to make `||D||<c` rigorously certifiable without an infinite-dimensional Galerkin error analysis.

---

# 1. Exact trace formula

The rank-2-shorted NULLPOL reproducing kernel is

```math
K_{NP,a}(z,w)
=
K_a(z,w)-k(z)^*G^{-1}k(w),
```

with

```math
K_a(z,w)
=\frac{\sin(a(z-\overline w))}
{\pi(z-\overline w)}.
```

Hence

```math
\boxed{
\operatorname{tr}D_{a,c}
=
\int_{\mathbb R}
(c-\tau_a(z))_+
K_{NP,a}(z,z)\,dz.
}
```

This is a one-dimensional compact-support integral.

---

# 2. Trace-minus-Ritz upper certificate for the top eigenvalue

Let the eigenvalues of `D=D_{a,c}` be

```math
\lambda_1\ge\lambda_2\ge\cdots\ge0.
```

Choose any `m`-dimensional subspace `V_m` of the Hilbert space and let

```math
\theta_1\ge\theta_2\ge\cdots\ge\theta_m\ge0
```

be the Ritz eigenvalues of the compression `P_{V_m}DP_{V_m}`.

By the min-max principle,

```math
\boxed{
\theta_j\le\lambda_j
\qquad(1\le j\le m).
}
```

Because `D` is positive trace class,

```math
\operatorname{tr}D
=\sum_{j\ge1}\lambda_j.
```

Therefore

```math
\begin{aligned}
\lambda_1
&=\operatorname{tr}D-\sum_{j\ge2}\lambda_j\\
&\le
\operatorname{tr}D-\sum_{j=2}^{m}\lambda_j\\
&\le
\operatorname{tr}D-\sum_{j=2}^{m}\theta_j.
\end{aligned}
```

Thus the exact certification lemma is

```math
\boxed{
\operatorname{tr}D_{a,c}
-
\sum_{j=2}^{m}\theta_j
<c
\quad\Longrightarrow\quad
\|D_{a,c}\|<c.
}
```

Combining with §0:

```math
\boxed{
\operatorname{tr}D_{a,c}
-
\sum_{j=2}^{m}\theta_j
<c
\quad\Longrightarrow\quad
Q_W>0\text{ on }\mathcal N_a\setminus\{0\}.
}
```

This is useful because a rigorous certificate needs only:

1. an **upper interval bound** for the scalar trace integral;
2. rigorous **lower interval bounds** for finitely many Ritz eigenvalues `theta_2,...,theta_m`.

No upper eigenvalue bound, no full-space Galerkin convergence theorem, and no estimate of the unresolved infinite Ritz tail are required.

---

# 3. Parity splitting reduces NULLPOL to one shorting condition per sector

The multiplier `tau_a` is even. Hence `D_{a,c}` commutes with parity and decomposes as

```math
D_{a,c}=D_{a,c}^{even}\oplus D_{a,c}^{odd}.
```

For an even Paley--Wiener function,

```math
F(-i/2)=F(i/2),
```

so the two NULLPOL conditions reduce to the single condition

```math
F(i/2)=0.
```

For an odd function,

```math
F(-i/2)=-F(i/2),
```

and again NULLPOL is one scalar condition.

Thus the global rank-2 shorting is exactly

```text
one rank-1 shorting in the even sector
+
one rank-1 shorting in the odd sector.
```

The trace-minus-Ritz certificate can and should therefore be applied separately in the two parity sectors.

---

# 4. `a=1/2` diagnostics

For

```math
a=1/2
```

the canonical finite-window multiplier is

```math
\tau_{1/2}(z)
=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)
-\log\pi
-\sqrt2\log2\cos(z\log2).
```

Numerical Nyström diagnostics using the **exact shorted reproducing kernel** give for the pure negative block `D_{1/2,0}` approximately

```text
even leading eigenvalue  0.2258375288...
odd  leading eigenvalue  0.2059078829...
```

and rapid spectral falloff after the first mode in each parity.

A more useful shifted defect is `D_{a,c}`.

### Even sector

Near

```text
c = 1.675
```

the diagnostic top eigenvalue is

```text
||D_even|| ≈ 1.665877817
```

so

```text
||D_even||/c ≈ 0.994553921.
```

The direct margin is only about `9.1e-3`, so a rigorous upper norm enclosure must be reasonably sharp.

However the trace-minus-Ritz certificate is favorable: diagnostic Ritz data indicate that using approximately

```text
m = 12
```

already gives

```text
tr(D_even) - sum_{j=2}^{12} theta_j
≈ 1.66903
< 1.675,
```

with margin about

```text
5.9e-3.
```

### Odd sector

Near

```text
c = 1.25
```

the diagnostic top eigenvalue is

```text
||D_odd|| ≈ 1.115100777,
```

so the margin is large.

Already roughly

```text
m = 5
```

Ritz dimensions are diagnostically enough for the trace-minus-Ritz upper certificate.

### Firewall

All numbers in this section are floating/Nyström diagnostics only. They motivate the finite certificate dimensions; they are not accepted as proof inputs.

---

# 5. Why this is stronger than a standard Ritz PASS

A conventional finite Ritz calculation can only show that some finite-dimensional restriction is positive; it does not control the missing infinite-dimensional directions.

The present certificate reverses the useful inequality:

- Ritz eigenvalues of a positive compact operator are **lower bounds** for the corresponding exact eigenvalues;
- subtracting those lower bounds from an exact trace gives an **upper bound** for the dangerous top eigenvalue.

Thus the uncomputed infinite tail helps rather than hurts: it is positive and is already included in the trace.

This is the crucial certification advantage.

---

# 6. Recommended rigorous implementation

For each parity separately:

1. choose a rational/interval value of `c` near the diagnostic optimum;
2. enclose all roots of `tau_{1/2}(z)=c` that delimit the compact support of `(c-tau)_+`;
3. certify the trace integral with Arb;
4. freeze an explicit finite Ritz family (e.g. shorted kernel sections or low-order orthogonalized polynomial/prolate trial functions);
5. interval-certify its Gram and weighted-operator matrices;
6. obtain rigorous lower bounds for `theta_2,...,theta_m` by interval Cholesky/Sturm/generalized-eigenvalue bracketing;
7. verify

```math
tr(D)-\sum_{j=2}^{m}\theta_j<c.
```

Suggested initial dimensions from diagnostics:

```text
odd:  m=5 or modestly larger for safety
even: m=12, preferably 14--16 for interval margin
```

No statement should be promoted until the interval margins are strictly separated from zero.

---

# 7. Strategic status

If the certificate closes, `a=1/2` becomes the first sharp NULLPOL NP-GAP theorem proved directly from the new Critical-half/prolate architecture.

That would not be a new RH result by itself, and fixed-`a` positivity is not claimed to be RH-equivalent. Its importance would be architectural: it would demonstrate that the same rank-2-shortened Paley--Wiener geometry that arose from `L_{1/2}` is quantitatively strong enough to dominate the sign-changing Euler/Gamma scattering multiplier.

If the certificate fails after rigorous optimization, the failure will identify the exact parity/eigenmode that obstructs the current prolate route.

---

# 8. Nonclaims

Do not claim yet:

- `a=1/2` has been interval-certified by this audit;
- the floating margins are theorem data;
- the all-window NP-GAP follows from one fixed radius;
- the trace-minus-Ritz lemma alone proves RH;
- publication novelty is established.
