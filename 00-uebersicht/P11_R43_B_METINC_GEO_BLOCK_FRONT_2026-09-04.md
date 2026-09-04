# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front  
**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`

## One-line update

The frozen `P_T,E_T,D_s` definitions now give an exact **raw symmetric-strip theorem**.  Raw unweighted interior/interior and interior/boundary increments collapse together, but the actual Schur/normalized GEO channel still has two separate mixing firewalls: fixed-terminal Feshbach mixing (`BMIX`) and old-metric square-root mixing (`NORMMIX`).

## Live tree

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
   └─ FD23-TAIL-COMPACTNESS-EQUIV ✓[M]
```

Legacy labels `GEO-II` and `GEO-IB` remain OPEN at the actual normalized/source-metric level.  Their **raw unweighted** support analogues are closed jointly by `R43-GEO-RAW-STRIP`.

Downstream remains

```text
B-METINC-WIDTH + FD23 machinery
  -> B-FLAGMOD contribution
  -> [with B-FLAGPHASE] B-FLAGTIGHT ?
  -> B-SIGN ?
  -> Strong Terminal ?
```

No converse is added.

## Frozen raw strip theorem

Canonical P11 has

\[
D_s=U_{s/2}-U_{-s/2},
\qquad
E_T:\mathscr H_T\to L^2(\mathbb R)\text{ zero extension},
\qquad
P_T=E_T^*.
\]

For `X<U<V` and

\[
\psi_s(f):=-D_sE_Xf,
\]

one has exactly

\[
K_{s,T}^*E_{X,T}f=P_T\psi_s(f),
\qquad K_{s,T}=P_TD_sE_T,
\]

and therefore

\[
K_{s,V}^*E_{X,V}f-
\iota_{U\to V}K_{s,U}^*E_{X,U}f
\]

is supported on

\[
\mathcal S_{U,V}=\{x:U<|x|<V\}.
\]

Equivalently,

\[
\langle P_V\psi_a,P_V\psi_b\rangle-
\langle P_U\psi_a,P_U\psi_b\rangle
=
\int_{U<|x|<V}\psi_a\overline{\psi_b}.
\]

The strip is symmetric because the frozen windows are `(-T,T)`.

For the entire old hub, if

\[
v_0=\iota H_U^*E_{X,U}f,
\qquad
v_1=H_{V,\rm old}^*E_{X,V}f,
\qquad
d=v_1-v_0,
\]

then `v_0` is supported in `(-U,U)` and `d` in the strip, so

\[
\langle d,v_0\rangle=0.
\]

This is `R43-GEO-RAW-STRIP ✓[M]`, a local exact frozen-definition result only.

## GEO-BMIX: the surviving Schur cross term

Frozen Schur geometry uses

\[
B_V=(I+R_V^*R_V)^{-1}
\]

inside the old-geometry term.  Let

\[
Q_I=1_{(-U,U)},
\qquad Q_B=I-Q_I.
\]

Then exactly

\[
\Delta s_{\rm geo}
=
2\operatorname{Re}\langle d,Q_BB_VQ_Iv_0\rangle
+
\langle d,Q_BB_VQ_Bd\rangle.
\]

Thus the primitive cross obstruction is

\[
\boxed{Q_BB_VQ_I.}
\]

It is **not** `COND`: `B_V` is fixed here.  `COND` is separately the horizon change `B_U\to B_V`.

A useful exact reduction is

\[
[B_V,Q_I]=-B_V[R_V^*R_V,Q_I]B_V,
\]

so

\[
\|Q_BB_VQ_I\|
\le
\|[R_V^*R_V,Q_I]\|.
\]

No smallness is yet booked.

## NORMMIX: a second, later mixing layer

The spectral-width operator is normalized by

\[
\mathbf H_{\rm geo}
=G_{S,U}^{-1/2}\Delta G_{\rm geo}G_{S,U}^{-1/2}.
\]

Therefore even a Schur/source block cancellation need not survive unless the old metric square root respects the relevant split.  The live quantitative node is

```text
B-METINC-NORMMIX [OPEN]
    control P_I G_{S,U}^{-1/2} P_B
```

(or the corresponding commutator/reducing-subspace formulation).

`BMIX`, `NORMMIX`, and `COND` are three distinct mechanisms:

1. `BMIX`: fixed `B_V` mixes old interior with the new strip;
2. `NORMMIX`: `G_{S,U}^{-1/2}` mixes source blocks after pullback;
3. `COND`: `B_U` changes to `B_V` with terminal horizon.

## Spectral-width sharpening

For

\[
H=\begin{pmatrix}0&C\\ C^*&D\end{pmatrix}=H^*,
\]

\[
\operatorname{width}\sigma(H)
\le
2\|C\|+
\operatorname{width}(\sigma(D)\cup\{0\})
\le
2\|C\|+2\|D\|.
\]

If separately `D\ge0`, the last term improves to `\|D\|`.  No such positivity is silently promoted for the full normalized GEO block.

## FD23 tail compactness

The canonical tail is

\[
\mathcal H_S^{[m]}
=
\overline{\operatorname{span}}\{e_{S,n}:n\ge m\},
\]

which is generally infinite dimensional.  Its complement/head is finite dimensional.  Therefore for every bounded `K\subset\mathcal H_S^0`,

\[
\boxed{
K\text{ relatively norm compact}
\iff
\sup_{x\in K}\|P_S^{[m]}x\|\to0.
}
\]

This abstract/canonical-tail equivalence is `✓[M]`.  The actual R43 family still has to be shown bounded/compact (for example by fixed-interval norm continuity), so `FD23-UNIF` remains OPEN.

In the more general strong-convergence lemma, `\sup_m\|T_m\|<\infty` is automatic from Banach–Steinhaus.  For the orthogonal tails it is trivial since `\|P_S^{[m]}\|\le1`.

## Immediate proof order

1. `B-METINC-GEO-BMIX`: estimate `Q_BB_VQ_I` or `[R_V^*R_V,Q_I]`.
2. `B-METINC-COND`: derive a quantitative resolvent increment for `B_U\to B_V` without conflating it with BMIX.
3. `B-METINC-NORMMIX`: control the old-metric square-root offblock.
4. `FD23-UNIF`: prove fixed-interval boundedness plus relative compactness/norm continuity of the concrete modulus-vector family.
5. Only then return to condition-weighted prime-power summability.

## Governance

- `R43-GEO-RAW-STRIP`: ✓[M] local exact theorem only.
- `FD23-TAIL-COMPACTNESS-EQUIV`: ✓[M] abstract/canonical-tail theorem only.
- no new project-level `✓[M]`.
- `B-METINC-GEO`: OPEN.
- `B-METINC-GEO-BMIX`: OPEN.
- `B-METINC-GEO-BDRY`: OPEN.
- legacy normalized `GEO-II`: OPEN.
- legacy normalized `GEO-IB`: OPEN.
- `B-METINC-NORMMIX`: OPEN.
- `B-METINC-COND`: OPEN, elevated priority.
- `FD23-UNIF`: OPEN.
- `B-METINC-NEW`: OPEN.
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
