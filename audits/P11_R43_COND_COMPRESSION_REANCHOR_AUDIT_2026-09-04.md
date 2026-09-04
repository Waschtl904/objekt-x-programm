# P11 / R43 — COND compression and reanchor audit

**Date:** 2026-09-04  
**Status:** local exact hardening; `B-METINC-COND` remains OPEN

## 0. Scope and firewall

This note performs the binary definition check requested after the external multi-model reconciliation and records only exact operator-theoretic consequences.

It does **not** close `B-METINC-COND`, `B-METINC-NORMMIX`, `B-METINC`, `B-FLAGMOD`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, Object X, or RH. R43 remains OPEN; no freeze and no new formal independent-GREEN booking occur here.

The decisive frozen-definition fact is that the canonical old-conditioning term is **not** presently written on one unchanged terminal source window.

From the companion spectral-width audit, for `X<U<V`,

\[
v_U=H_U^*E_{X,U}f,
\qquad
\iota=E_{U,V}:L^2(-U,U)\to L^2(-V,V),
\qquad
v_0=\iota v_U,
\]

and the exact old-conditioning contribution is

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
=
\langle \iota v_U,B_V\iota v_U\rangle
-
\langle v_U,B_Uv_U\rangle
=
\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle.
}
\tag{C1}
\]

Thus the current canonical `COND` term **does carry the embedding** `\iota`. Replacing it by a same-space `\iota=I` increment would be a new refinement of the decomposition, not a reading of the already frozen definition.

---

## 1. Abstract resolvent antitonicity and fixed-vector telescope

Let `A_0,A_1` be bounded positive self-adjoint operators on one Hilbert space and

\[
A_0\preceq A_1,
\qquad
B_j=(I+A_j)^{-1}.
\]

Then inversion reverses Loewner order:

\[
\boxed{
A_0\preceq A_1
\Longrightarrow
B_0\succeq B_1.
}
\tag{C2}
\]

The same statement holds for positive closed forms via the associated resolvents; no commutation is required.

For a monotone chain `A_0\preceq A_1\preceq\cdots\preceq A_N`, put

\[
D_j:=B_j-B_{j+1}\succeq0.
\]

Then

\[
\sum_{j=0}^{N-1}D_j=B_0-B_N\preceq B_0\preceq I,
\tag{C3}
\]

and for every **fixed** vector `x`,

\[
\boxed{
\sum_{j=0}^{N-1}\langle x,D_jx\rangle
=
\langle x,(B_0-B_N)x\rangle
\le \|x\|^2.
}
\tag{C4}
\]

Book locally:

```text
R43-RESOLVENT-ANTITONE-TELESCOPE ✓[M]
R43-COND-PSD-INCREMENT-ABSTRACT ✓[M]
```

These are abstract theorems only. Equation (C1) is not yet known to satisfy the premise needed to make `B_U-\iota^*B_V\iota` positive.

---

## 2. Compression and inversion: exact Schur criterion

Let

\[
\mathcal K_V=\operatorname{Ran}\iota\oplus\mathcal N,
\]

where `\iota:\mathcal K_U\to\mathcal K_V` is an isometry. Let

\[
A_V\succeq0,
\qquad
B_V=(I+A_V)^{-1},
\qquad
A_U\succeq0,
\qquad
B_U=(I+A_U)^{-1}.
\]

Relative to `\operatorname{Ran}\iota\oplus\mathcal N`, write

\[
I+A_V=
\begin{pmatrix}
a&b\\ b^*&d\end{pmatrix},
\]

with

\[
a=I+\iota^*A_V\iota,
\qquad
b=\iota^*A_VP_{\mathcal N},
\qquad
d=I_{\mathcal N}+P_{\mathcal N}A_VP_{\mathcal N}\succeq I_{\mathcal N}.
\]

Since `d` is invertible, the block inverse formula gives

\[
\boxed{
\iota^*B_V\iota
=
\bigl(a-bd^{-1}b^*\bigr)^{-1}.
}
\tag{C5}
\]

Define

\[
\Delta A:=\iota^*A_V\iota-A_U,
\qquad
\Sigma:=bd^{-1}b^*\succeq0.
\tag{C6}
\]

Then

\[
a-bd^{-1}b^*=I+A_U+\Delta A-\Sigma.
\]

Because inversion reverses Loewner order on strictly positive operators,

\[
\boxed{
\iota^*B_V\iota\preceq B_U
\iff
\Delta A\succeq\Sigma.
}
\tag{C7}
\]

This is the exact canonical PSD criterion.

It also exposes the compression firewall:

\[
\Sigma\succeq0
\Longrightarrow
\iota^*B_V\iota
\succeq
(I+\iota^*A_V\iota)^{-1}.
\tag{C8}
\]

Thus compression of the inverse dominates inverse of the compression; they do not commute in general.

### Falsifiability

If `\Delta A=0` and `b\ne0`, then `\Sigma\ne0` and

\[
I+A_U-\Sigma\preceq I+A_U,
\]

so

\[
\iota^*B_V\iota\succeq B_U,
\tag{C9}
\]

with strict inequality on at least one vector. Hence the desired order can genuinely reverse.

### Rank obstruction

If `\Delta A` has rank one and `\Delta A\succeq\Sigma`, then necessarily

\[
\operatorname{Ran}\Sigma\subseteq\operatorname{Ran}\Delta A,
\qquad
\operatorname{rank}\Sigma\le1.
\tag{C10}
\]

Therefore any higher-rank or differently oriented Schur-coupling term `\Sigma` rules out (C7) for that isolated rank-one increment.

Book locally:

```text
R43-COND-COMPRESSION-SCHUR-CRITERION ✓[M]
```

The application remains:

```text
R43-COND-CANONICAL-PSD-REALIZATION [OPEN]
```

because the frozen R43 definitions do not currently prove `\Delta A\succeq\Sigma`.

---

## 3. Why the binary definition check does not close COND

The frozen SW14 decomposition defines old-conditioning through (C1), with `\iota=E_{U,V}` explicitly present. Therefore the cheap branch

```text
canonical COND already has iota = id
```

is false for the current definition.

A same-window refinement may still be useful. Algebraically one may insert

\[
\widehat B_{U;V}:=(I+\iota^*A_V\iota)^{-1}
\]

and split

\[
\boxed{
\iota^*B_V\iota-B_U
=
(\widehat B_{U;V}-B_U)
+
(\iota^*B_V\iota-\widehat B_{U;V}).
}
\tag{C11}
\]

The second term is always positive semidefinite by (C8). The first term has the desired nonpositive sign exactly when

\[
\iota^*A_V\iota\succeq A_U.
\tag{C12}
\]

However, assigning the second term to an existing `BMIX`/`BDRY` node would be a **new taxonomic theorem** and is not booked here. In particular, the already frozen BMIX target `Q_BB_VQ_I` should not be silently identified with the Schur-compression correction in (C11) without a type-correct proof.

---

## 4. Reanchoring: sharp sufficient condition in the telescoping PSD form

Assume now an abstract positive telescoping chain

\[
D_j:=B_j-B_{j+1}\succeq0,
\qquad
\sum_jD_j\preceq I.
\]

Let

\[
v_j=x+\delta_j
\]

for one fixed anchor `x`. For every `\varepsilon>0`, Cauchy-Schwarz in the seminorm induced by `D_j` gives

\[
2|\operatorname{Re}\langle x,D_j\delta_j\rangle|
\le
\varepsilon\langle x,D_jx\rangle
+\varepsilon^{-1}\langle\delta_j,D_j\delta_j\rangle.
\tag{C13}
\]

Hence

\[
\boxed{
\sum_j\langle v_j,D_jv_j\rangle
\le
(1+\varepsilon)\|x\|^2
+(1+\varepsilon^{-1})\sum_j\|\delta_j\|^2.
}
\tag{C14}
\]

Therefore

\[
\boxed{
\sum_j\|v_j-x\|^2<\infty
}
\tag{C15}
\]

is a sufficient fixed-anchor path condition for summability of the moving-vector energies. The cross term does **not** require ambient operator-norm variation; it is absorbed inside the positive increment form itself.

Book locally:

```text
R43-COND-REANCHOR-SUFFICIENT ✓[M]
```

This does not prove that the actual canonical path `v_U` satisfies (C15).

---

## 5. Boundedness alone cannot replace a path condition

There is no universal estimate of the form

\[
\sum_j\langle v_j,D_jv_j\rangle
\le C\sup_j\|v_j\|^2
\tag{C16?}
\]

for all positive telescoping chains.

Take `\ell^2(\mathbb N)` with standard basis `e_j`,

\[
B_j=P_{\overline{\operatorname{span}}\{e_j,e_{j+1},\dots\}},
\qquad
D_j=B_j-B_{j+1}=e_je_j^*,
\qquad
v_j=e_j.
\]

Then `0\preceq B_j\preceq I`, the chain decreases strongly to zero, and

\[
\sup_j\|v_j\|=1,
\qquad
\sum_j\langle v_j,D_jv_j\rangle
=\sum_j1=\infty.
\tag{C17}
\]

Thus boundedness of the moving source path is provably insufficient.

Book locally:

```text
R43-COND-REANCHOR-BOUNDEDNESS-NOGO ✓[M]_neg
```

The live application node remains

```text
R43-COND-FIXED-SOURCE-REANCHOR [OPEN]
```

with an actual quantitative path condition still required.

---

## 6. Exact discrete Abel decomposition for a moving normalization

Let `B_j` be arbitrary bounded self-adjoint operators, put

\[
D_j:=B_j-B_{j+1},
\]

and let `T_j` be bounded operators on one fixed source space. Define

\[
\Delta T_j:=T_{j+1}-T_j.
\]

Then the exact identity

\[
\boxed{
\begin{aligned}
\sum_{j=0}^{N-1}T_j^*D_jT_j
={}&T_0^*B_0T_0-T_N^*B_NT_N\\
&+\sum_{j=0}^{N-1}
\Bigl[(\Delta T_j)^*B_{j+1}T_{j+1}
+T_j^*B_{j+1}\Delta T_j\Bigr]
\end{aligned}
}
\tag{C18}
\]

holds by direct expansion. No positivity is required.

For a fixed source vector `\varepsilon`, (C18) separates the telescoping endpoint term from the entire moving-normalization defect. In the R43 taxonomy this is the natural algebraic bridge for exporting `\Delta T_j`-variation toward `NORMMIX`, but such an assignment is not itself a quantitative estimate.

Book locally:

```text
R43-COND-DISCRETE-ABEL-DECOMPOSITION ✓[M]
```

---

## 7. Sign convention

Whenever the canonical PSD criterion (C7) is available, define the **positive COND variation** by

\[
\boxed{
\Delta_{\rm COND}^+B(U,V)
:=B_U-\iota^*B_V\iota\succeq0.
}
\tag{C19}
\]

The actual SW14 contribution to the metric increment is the negative quadratic form

\[
\Delta s_{\rm cond}^{U,V}(f)
=-\langle v_U,\Delta_{\rm COND}^+B(U,V)v_U\rangle.
\tag{C20}
\]

This convention prevents the phrase “positive COND variation” from being confused with the sign of the METINC summand itself.

---

## 8. Current exact status after the definition check

```text
R43-RESOLVENT-ANTITONE-TELESCOPE          ✓[M]      (abstract)
R43-COND-PSD-INCREMENT-ABSTRACT           ✓[M]      (abstract)
R43-COND-COMPRESSION-SCHUR-CRITERION      ✓[M]      (abstract/local exact)
R43-COND-DISCRETE-ABEL-DECOMPOSITION      ✓[M]      (abstract)
R43-COND-REANCHOR-SUFFICIENT              ✓[M]      (abstract)
R43-COND-REANCHOR-BOUNDEDNESS-NOGO        ✓[M]_neg  (abstract counterexample)

R43-COND-CANONICAL-PSD-REALIZATION        [OPEN]
R43-COND-FIXED-SOURCE-REANCHOR            [OPEN]
B-METINC-COND                              [OPEN]
B-METINC-NORMMIX                           [OPEN]
```

### Decisive answer to the first live question

```text
Does the canonical COND term carry iota?
YES.
```

Therefore `CANONICAL-PSD-REALIZATION` does **not** close by the `iota=id` shortcut. Its exact criterion is (C7). The next canonical calculation is to identify `\Delta A` and `\Sigma` for the frozen residual operator `R_V` and test whether `\Delta A\succeq\Sigma` can hold, or whether the Schur-compression correction must be split into a separate boundary/mixing channel.

The reanchor problem comes second: once a positive COND chain is actually available, one must prove a path condition such as (C15), or an equivalent blockwise/energy-norm variant, for the canonical source path.

---

## 9. Governance

No promotion of any program-level gate occurs.

Still OPEN: `B-METINC-COND`, `B-METINC-NORMMIX`, `B-METINC-GEO-BMIX`, `B-METINC-GEO-BDRY`, `B-METINC-NEW`, `B-METINC-WIDTH`, `B-METINC`, `B-FLAGMOD`, `B-FLAGPHASE`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, R43, Object X, RH. R38–R42 remain frozen as before; R37/G4c remains separate and OPEN.
