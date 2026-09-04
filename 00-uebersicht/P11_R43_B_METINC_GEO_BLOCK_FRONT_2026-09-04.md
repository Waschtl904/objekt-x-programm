# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front  
**Companion audit:** `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`

## One-line update

The exact high-level metric split remains `NEW + GEO + COND`, but `GEO` must now be refined into an interior block, an interior-boundary cross block, and a boundary block. Exact interior cancellation is only a candidate until common-ambient and normalization compatibility are verified.

## Live tree

```text
B-METINC-WIDTH [OPEN]
├─ summable width/conditioning majorants [OPEN]
│  ├─ B-METINC-NEW [OPEN]
│  ├─ B-METINC-GEO [OPEN]
│  │  ├─ B-METINC-GEO-INT   / GEO-II [OPEN]
│  │  ├─ B-METINC-GEO-CROSS / GEO-IB [OPEN]
│  │  └─ B-METINC-GEO-BDRY  / GEO-BB [OPEN]
│  └─ B-METINC-COND [OPEN]
└─ FD23-UNIF [OPEN]
```

Downstream:

```text
B-METINC-WIDTH + FD23 machinery
  -> B-FLAGMOD contribution
  -> [with B-FLAGPHASE] B-FLAGTIGHT ?
  -> B-SIGN ?
  -> Strong Terminal ?
```

All arrows remain only as strong as the existing companion audits state; no converse is added here.

## Fixed facts retained

For fixed source and one terminal step `U<V`,

\[
\|\mathscr E_{U,V}\|
\le
\frac12\operatorname{width}\sigma(\mathbf H_S^{U,V})
\]

without any Loewner assumption, and

\[
\mathfrak d_{m,\rm mod}(U,V)
\le
\frac{\operatorname{width}\sigma(\mathbf H_S^{U,V})}
{2\alpha_R(U,V)(\alpha_S(U,V)+\alpha_R(U,V))}.
\]

The pairwise `\alpha_R^{-1}` factor must not be dropped.

The exact Schur-energy split remains

```text
old-conditioning + old-geometry + new-shell.
```

The present refinement is entirely inside `old-geometry`.

## New firewall

An index split `old = interior ⊔ boundary` gives a Gram block

\[
\Delta G_{\rm geo}
=
\begin{pmatrix}
\Delta_{II}&\Delta_{IB}\\
\Delta_{IB}^*&\Delta_{BB}
\end{pmatrix}.
\]

Therefore even a future theorem `\Delta_{II}=0` leaves `\Delta_{IB}`. The cross block must be estimated separately and may import interior conditioning after old-metric normalization.

`GEO-II=0` itself remains OPEN until all of the following are checked from the frozen definitions:

1. `E_TP_T=M_T` in one common ambient space;
2. zero-extension compatibility `E_V∘iota_{U->V}=E_U`;
3. nested window projections `M_U<=M_V`;
4. exact endpoint conventions;
5. absence, or exact accounting, of `T`-dependent normalization;
6. compact-support versus tail behavior of the relevant channel vectors.

The robust target is

\[
\|\phi_a(V)-\phi_a(U)\|
\le
\|(I-P_U)D_{s_a}E_U\phi_a^0\|
+
\mathrm{NormDrift}_a(U,V).
\]

Boundary localization alone does not imply operator-norm smallness: the raw boundary crossing operator may retain norm `1`.

## FD23-UNIF

The fixed-interval projected-tail condition is now a visible separate node.

Abstractly, if `T_m->0` strongly, `sup_m ||T_m||<∞`, and `K` is norm compact, then

\[
\sup_{x\in K}\|T_mx\|\to0.
\]

This compactness lemma is ✓[M] as a general functional-analytic fact.

For the R43 modulus vector family, norm-continuity in `V` on each compact terminal interval would make its image compact and hence imply the required fixed-interval FD23 convergence. That application remains OPEN.

Relative compactness is used only as a **sufficient** route, not stated as a general equivalence.

## Immediate proof order

1. frozen `P_T,E_T,D_s` definition extraction and boundary audit;
2. common-ambient compatibility and nesting;
3. terminal-normalization audit;
4. robust tail/interior lemma;
5. separate `GEO-BB` and `GEO-IB` estimates;
6. derivative-free norm-continuity/compactness proof for `FD23-UNIF`;
7. only then condition-weighted summability.

## Governance

- `B-METINC-GEO-INT`: OPEN.
- `B-METINC-GEO-CROSS`: OPEN.
- `B-METINC-GEO-BDRY`: OPEN.
- `FD23-UNIF`: OPEN.
- `B-METINC-NEW`: OPEN.
- `B-METINC-COND`: OPEN.
- `B-METINC-WIDTH`: OPEN.
- B-FLAGMOD: OPEN.
- B-FLAGTIGHT: OPEN.
- B-SIGN: OPEN.
- Strong Terminal/C6: OPEN.
- no new project-level `✓[M]`.
- no freeze.
- no Object-X/RH promotion.
