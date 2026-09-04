# P11 / R43 — GEO strip, BMIX, NORMMIX and FD23 compactness audit

**Date:** 2026-09-04  
**Status:** R43 research hardening; project gates remain OPEN

## 0. Scope and firewall

This note reconciles the external GEO/FD23 review with the frozen P11 definitions.  It does **not** promote `B-METINC-GEO`, `B-METINC-WIDTH`, `FD23-UNIF`, `B-FLAGMOD`, `B-FLAGTIGHT`, `B-SIGN`, Strong Terminal/C6, Object X, or RH.

The exact high-level Schur split remains

```text
old-conditioning + old-geometry + new-shell.
```

The purpose here is to locate more precisely where the old-geometry obstruction survives.

---

## 1. Frozen common-ambient definitions

The canonical P11 source geometry fixes

\[
\mathscr H_T=L^2(-T,T),
\qquad
D_s=U_{s/2}-U_{-s/2},
\]

with `U_t` translation on `L^2(R)`, zero extension

\[
E_T:\mathscr H_T\longrightarrow L^2(\mathbb R),
\]

and restriction

\[
P_T=E_T^*.
\]

For `0<U<V`, zero extension `\iota_{U\to V}` satisfies

\[
E_V\iota_{U\to V}=E_U.
\]

Writing

\[
M_T:=E_TP_T=1_{(-T,T)}
\]

on the common ambient `L^2(R)`, we have

\[
M_U\le M_V.
\]

Endpoints are irrelevant in `L^2`.

For a shift `s`, set

\[
K_{s,T}:=P_TD_sE_T.
\]

Since `U_t^*=U_{-t}`,

\[
D_s^*=-D_s,
\]

and hence

\[
K_{s,T}^*=-P_TD_sE_T.
\]

These are exact frozen identities.

---

## 2. R43-GEO-RAW-STRIP — exact symmetric strip identity ✓[M]

Fix a source `X<U<V`, `f\in\mathscr H_X`, and a shift `s`.  Define the ambient field

\[
\psi_s(f):=-D_sE_Xf\in L^2(\mathbb R).
\]

Using `E_TE_{X,T}=E_X`,

\[
K_{s,T}^*E_{X,T}f
=-P_TD_sE_Xf
=P_T\psi_s(f).
\]

Therefore

\[
\boxed{
K_{s,V}^*E_{X,V}f
-\iota_{U\to V}K_{s,U}^*E_{X,U}f
=P_V(M_V-M_U)\psi_s(f).
}
\]

Equivalently, after the canonical common-ambient identification, the increment is supported on the **symmetric strip**

\[
\boxed{
\mathcal S_{U,V}:=\{x\in\mathbb R:U<|x|<V\}.
}
\]

Thus for arbitrary ambient fields `\psi_a,\psi_b`,

\[
\boxed{
\langle P_V\psi_a,P_V\psi_b\rangle_{V}
-\langle P_U\psi_a,P_U\psi_b\rangle_{U}
=
\int_{\mathcal S_{U,V}}
\psi_a(x)\overline{\psi_b(x)}\,dx.
}
\]

This corrects the one-sided schematic `\int_U^V` form: the frozen P11 windows are `(-T,T)`, so the exact new region is `U<|x|<V`.

### Raw row/column annihilation

If one factor vanishes on `\mathcal S_{U,V}`, then the whole corresponding raw Gram row and column increment vanish.  Hence on the **unweighted raw window-Gram layer** an interior-support hypothesis closes raw `II` and raw `IB` simultaneously.

This is a local exact theorem, booked as

```text
R43-GEO-RAW-STRIP ✓[M]
```

only.  It is not a closure of the Schur or normalized `B-METINC-GEO` gate.

---

## 3. The whole old-hub geometry increment is strip supported

For the old index set `\Lambda_U`, frozen primitive coefficients are terminal independent.  Define

\[
H_{V,\mathrm{old}}
:=\sum_{(p,k)\in\Lambda_U}a_{p,k}K_{p,k;V}.
\]

For fixed `f`, write

\[
v_0:=\iota_{U\to V}H_U^*E_{X,U}f,
\qquad
v_1:=H_{V,\mathrm{old}}^*E_{X,V}f,
\qquad
d:=v_1-v_0.
\]

By linearity of the raw-strip identity, there is one ambient old-hub field `\Psi_U(f)` such that

\[
v_0=M_U\Psi_U(f),
\qquad
v_1=M_V\Psi_U(f),
\qquad
d=(M_V-M_U)\Psi_U(f).
\]

Consequently

\[
M_Uv_0=v_0,
\qquad
(M_V-M_U)d=d,
\qquad
\langle d,v_0\rangle_{L^2(-V,V)}=0.
\]

Thus the **raw** old geometry is a pure boundary strip phenomenon.

---

## 4. Why Schur-GEO does not collapse: B-METINC-GEO-BMIX

The frozen Schur factor is

\[
B_T=(I+R_T^*R_T)^{-1},
\qquad 0<B_T\le I,
\]

and the exact old-geometry term at terminal `V` keeps `B_V` fixed:

\[
\Delta s_{\rm geo}
=
2\operatorname{Re}\langle d,B_Vv_0\rangle
+\langle d,B_Vd\rangle.
\]

Let on `L^2(-V,V)`

\[
Q_I:=1_{(-U,U)},
\qquad Q_B:=I-Q_I.
\]

Since `v_0=Q_Iv_0` and `d=Q_Bd`,

\[
\boxed{
\Delta s_{\rm geo}
=
2\operatorname{Re}\langle d,Q_BB_VQ_Iv_0\rangle
+\langle d,Q_BB_VQ_Bd\rangle.
}
\]

The second term is nonnegative because `B_V\ge0`.  The only old/new-strip cross contamination is therefore the fixed-terminal offblock

\[
\boxed{Q_BB_VQ_I.}
\]

This motivates the primitive live node

```text
B-METINC-GEO-BMIX [OPEN]
    control ||Q_B B_V Q_I||
```

(or the corresponding condition-weighted/projected version actually required downstream).

### BMIX is not COND

`BMIX` is present with **one fixed operator `B_V`**.  By contrast,

```text
B-METINC-COND
```

controls the separate horizon change `B_U -> B_V`.  The two mechanisms must not be merged.

If `[B_V,Q_I]=0`, then `Q_BB_VQ_I=0`; Schur-GEO reduces to the positive boundary quadratic term.  No such commutation theorem is presently booked.

Because `B_V=(I+R_V^*R_V)^{-1}`,

\[
[B_V,Q_I]
=-B_V[R_V^*R_V,Q_I]B_V,
\]

hence, using `\|B_V\|\le1`,

\[
\boxed{
\|Q_BB_VQ_I\|
\le
\|[R_V^*R_V,Q_I]\|.
}
\]

This is an exact reduction, not yet a smallness estimate.

---

## 5. A second mixing layer after pullback: B-METINC-NORMMIX

Even if a raw or Schur-level source block has a vanishing `II` component, the operator entering the spectral-width route is normalized by the old source metric:

\[
\mathbf H_{\rm geo}
=G_{S,U}^{-1/2}\,\Delta G_{\rm geo}\,G_{S,U}^{-1/2}.
\]

For any chosen source decomposition `I\oplus B`, write

\[
G_{S,U}^{-1/2}
=\begin{pmatrix}A&C\\ C^*&F\end{pmatrix},
\qquad
\Delta G_{\rm geo}
=\begin{pmatrix}0&X\\X^*&D\end{pmatrix}.
\]

Direct multiplication gives

\[
\boxed{
(\mathbf H_{\rm geo})_{II}
=AXC^*+CX^*A+CDC^*.
}
\]

Therefore

\[
\boxed{
\|(\mathbf H_{\rm geo})_{II}\|
\le
2\|A\|\,\|C\|\,\|X\|
+\|C\|^2\,\|D\|.
}
\]

Exact normalized cancellation therefore requires an additional reducing/commutation statement, or quantitative control of the offblock

\[
P_I G_{S,U}^{-1/2}P_B.
\]

Book this independently as

```text
B-METINC-NORMMIX [OPEN].
```

`NORMMIX` is distinct from both:

- `GEO-BMIX`: fixed-`B_V` spatial strip mixing inside Schur-GEO;
- `COND`: the actual horizon change `B_U -> B_V`.

---

## 6. Spectral-width block sharpening

For a bounded self-adjoint block

\[
H=\begin{pmatrix}0&C\\C^*&D\end{pmatrix},
\]

write `H=H_{off}+0\oplus D`.  The offdiagonal part has spectrum symmetric about zero and norm `\|C\|`, hence width `2\|C\|`.  Spectral-width subadditivity gives

\[
\boxed{
\operatorname{width}\sigma(H)
\le
2\|C\|
+
\operatorname{width}(\sigma(D)\cup\{0\}).
}
\]

In particular,

\[
\operatorname{width}\sigma(H)
\le2\|C\|+2\|D\|.
\]

If separately `D\ge0`, then

\[
\operatorname{width}\sigma(H)
\le2\|C\|+\|D\|.
\]

No positivity of the full normalized GEO boundary block is silently booked here.

---

## 7. Canonical jet tails: compactness equivalence ✓[M]

The frozen jet-tail space is

\[
\mathcal H_S^{[m]}
=
\overline{\operatorname{span}}\{e_{S,n}:n\ge m\},
\]

with orthogonal tail projection `P_S^{[m]}`.  The tail is generally infinite dimensional; its complement

\[
Q_m:=I-P_S^{[m]}
\]

has finite-dimensional range `\operatorname{span}\{e_{S,1},\ldots,e_{S,m-1}\}`.

### Theorem

For every bounded set `K\subset\mathcal H_S^0`,

\[
\boxed{
K\text{ is relatively norm compact}
\iff
\sup_{x\in K}\|P_S^{[m]}x\|\longrightarrow0.
}
\]

**Proof, forward direction.** `P_S^{[m]}\to0` strongly and `\|P_S^{[m]}\|\le1`; the standard finite-net argument makes this convergence uniform on the compact closure of `K`.

**Proof, reverse direction.** Given `\varepsilon>0`, choose `m` with
`\sup_{x\in K}\|P_S^{[m]}x\|<\varepsilon`.  Since `K` is bounded and `Q_mK` lies in a finite-dimensional space, `Q_mK` is totally bounded.  A finite `\varepsilon`-net for `Q_mK` lifts to a finite `2\varepsilon`-net for `K`.  Thus `K` is totally bounded, hence relatively compact in the Hilbert space.

Book this only as the abstract/canonical-tail fact

```text
FD23-TAIL-COMPACTNESS-EQUIV ✓[M].
```

The phrase “finite-dimensional jet stages” is misleading: the **heads**, not the tails `\mathcal H_S^{[m]}`, are finite dimensional.

### Uniform boundedness remark

In the more general lemma `T_m\to0` strongly implies uniform convergence on compact sets, a separately stated hypothesis `\sup_m\|T_m\|<\infty` is redundant by Banach–Steinhaus.  Keeping it is harmless for an elementary epsilon-net proof; for the actual orthogonal tail projections it is trivial because `\|P_S^{[m]}\|\le1`.

### R43 application remains OPEN

For the actual fixed-interval modulus-vector family `K_k`, `FD23-UNIF` becomes equivalent to relative compactness **once boundedness of that concrete family is established**.  Norm-continuity in `V` on `[U_k,U_{k+1}]` is still a sufficient compactness mechanism.  Neither concrete boundedness/continuity nor compactness is promoted here.

---

## 8. Revised live theorem tree

```text
B-METINC-WIDTH [OPEN]
├─ summable width/conditioning majorants [OPEN]
│  ├─ B-METINC-NEW [OPEN]
│  ├─ B-METINC-GEO [OPEN]
│  │  ├─ R43-GEO-RAW-STRIP ✓[M]      (local raw theorem)
│  │  ├─ B-METINC-GEO-BMIX [OPEN]    (Q_B B_V Q_I)
│  │  └─ B-METINC-GEO-BDRY [OPEN]    (strip quadratic / boundary size)
│  ├─ B-METINC-NORMMIX [OPEN]        (G_{S,U}^{-1/2} offblock)
│  └─ B-METINC-COND [OPEN]           (B_U -> B_V; elevated priority)
└─ FD23-UNIF [OPEN]
   └─ FD23-TAIL-COMPACTNESS-EQUIV ✓[M] (abstract/canonical-tail fact)
```

Legacy labels `GEO-II` and `GEO-IB` remain OPEN at the actual normalized/source-metric level.  On the raw unweighted window-Gram layer, their support analogue collapses jointly by `R43-GEO-RAW-STRIP`; `BMIX` and `NORMMIX` are exactly why that raw fact is not promoted downstream.

---

## 9. Immediate proof order

1. Attack `B-METINC-GEO-BMIX` through `Q_BB_VQ_I`, equivalently the spatial offblock/commutator of `B_V`.
2. In parallel, derive a quantitative `B-METINC-COND` resolvent estimate for `B_U -> B_V` without conflating it with BMIX.
3. Audit `P_I G_{S,U}^{-1/2}P_B` for `B-METINC-NORMMIX`.
4. Prove fixed-interval boundedness/norm-continuity or relative compactness of the actual FD23 modulus-vector family.
5. Only after these structural reductions, return to condition-weighted prime-power summability.

---

## 10. Governance

- `R43-GEO-RAW-STRIP`: ✓[M] as a local exact frozen-definition lemma only.
- `FD23-TAIL-COMPACTNESS-EQUIV`: ✓[M] as an abstract/canonical-tail functional-analytic lemma only.
- no new project-level `✓[M]`.
- `B-METINC-GEO`: OPEN.
- `B-METINC-GEO-BMIX`: OPEN.
- `B-METINC-GEO-BDRY`: OPEN.
- legacy normalized `GEO-II`: OPEN.
- legacy normalized `GEO-IB`: OPEN.
- `B-METINC-NORMMIX`: OPEN.
- `B-METINC-COND`: OPEN, elevated priority.
- `B-METINC-NEW`: OPEN.
- `FD23-UNIF`: OPEN.
- `B-METINC-WIDTH`: OPEN.
- B-METINC: OPEN.
- B-FLAGMOD: OPEN.
- B-FLAGPHASE: OPEN.
- B-FLAGTIGHT: OPEN.
- B-SIGN: OPEN.
- Strong Terminal/C6: OPEN.
- R43: OPEN.
- no freeze.
- no new formal independent GREEN.
- R38–R42 unchanged/frozen.
- R37/G4c separate and OPEN.
- no Object-X/RH promotion.
