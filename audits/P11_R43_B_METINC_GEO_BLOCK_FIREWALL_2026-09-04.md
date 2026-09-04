# P11 / R43 — B-METINC GEO block firewall and FD23 uniformity audit

**Date:** 2026-09-04  
**Branch:** `research/r43-gcac-hardening`  
**Scope:** refinement of the already exact `NEW / GEO / COND` split inside the `GEO` channel, plus the fixed-interval FD23 uniformity firewall.

---

## 0. Status firewall

This note does **not** close `B-METINC-GEO`, `B-METINC-WIDTH`, `B-FLAGMOD`, `B-FLAGTIGHT`, `B-SIGN`, or Strong Terminal/C6.

The only theorem-level item proved here is an abstract compactness lemma for strong operator convergence on norm-compact sets. Its application to the frozen R43 modulus-vector family remains OPEN.

In particular:

- `GEO-II = 0` is a theorem **candidate**, not a booked R43 theorem;
- the interior/boundary split has a genuine cross block `GEO-IB`;
- boundary localization alone is not an operator-norm-smallness theorem;
- no weighted prime-power summability is imported without an exact coefficient/frame estimate;
- no new project-level `✓[M]` and no Strong-Terminal promotion occur here.

---

## 1. Inherited exact structure

The companion definition audit fixes, for an active prime-power shift

\[
s=k\log p,
\qquad
K_{p,k;T}=P_TD_sE_T,
\]

and the frozen Schur channel

\[
H_T
=
P_T\sum_{p^k\le e^{2T}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_T,
\qquad
B_T=(I+R_T^*R_T)^{-1}.
\]

The companion spectral-width audit already gives the exact Schur-energy telescoping split

\[
\Delta G_X^{U,V}
=
\Delta G_{X,\mathrm{cond}}^{U,V}
+
\Delta G_{X,\mathrm{geo}}^{U,V}
+
\Delta G_{X,\mathrm{new}}^{U,V},
\tag{GB1}
\]

and, after normalization by the old metric,

\[
\mathbf H_X^{U,V}
=
\mathbf H_{X,\mathrm{cond}}^{U,V}
+
\mathbf H_{X,\mathrm{geo}}^{U,V}
+
\mathbf H_{X,\mathrm{new}}^{U,V}.
\tag{GB2}
\]

Thus the refinement below lives **inside** `old-geometry`; it does not replace the exact `NEW / GEO / COND` decomposition.

The positivity-free spectral-width chain remains

\[
\|\mathscr E_{U,V}\|
\le
\frac12\operatorname{width}\sigma(\mathbf H_S^{U,V}),
\tag{GB3}
\]

and the actual modulus gate retains both pairwise coercivity factors:

\[
\mathfrak d_{m,\mathrm{mod}}(U,V)
\le
\frac{\operatorname{width}\sigma(\mathbf H_S^{U,V})}
{2\alpha_R(U,V)\bigl(\alpha_S(U,V)+\alpha_R(U,V)\bigr)}.
\tag{GB4}
\]

No cofinal uniform spectral lower bound is booked.

---

## 2. Common-ambient algebra: exact conditional identity

To isolate the geometric movement, place the finite windows in a common ambient space and write, **provided the frozen realization actually supplies these identities**,

\[
M_T:=E_TP_T,
\qquad
M_U\le M_V,
\qquad
Q_{U,V}:=M_V-M_U.
\tag{GB5}
\]

For one shift `D_s`, pure algebra gives

\[
\boxed{
M_VD_sM_V-M_UD_sM_U
=
Q_{U,V}D_sM_U
+
M_UD_sQ_{U,V}
+
Q_{U,V}D_sQ_{U,V}.
}
\tag{GB6}
\]

Indeed `M_V=M_U+Q_{U,V}` and expansion is exact.

This identity is ✓[M] **as an abstract algebraic statement under (GB5)**. It is **not yet** a project-level theorem about the frozen `P_TD_sE_T`, because the required common-ambient compatibility and normalization hypotheses are not yet discharged.

For an old ambient vector `x` with `M_Ux=x`, the one-vector difference satisfies schematically

\[
(M_VD_sM_V-M_UD_sM_U)x
=
Q_{U,V}D_sx
\tag{GB7}
\]

whenever the additional right-compression terms reduce as intended. Hence the natural interior criterion is not `s\le 2U`, but

\[
\operatorname{supp}(D_sx)\subseteq\Omega_U,
\tag{GB8}
\]

or, in a compact-support parametrization with support length `\ell_a`, a sufficient schematic condition

\[
s_a+\ell_a\le U.
\tag{GB9}
\]

Under exact zero-extension compatibility and no additional terminal normalization, (GB8) forces the geometric one-vector defect to vanish.

**Project status:** this is the candidate mechanism behind `B-METINC-GEO-INT`; it is not yet booked because (GB5), boundary conventions, and normalization must be checked against the frozen realization.

---

## 3. The hidden Gram cross block

An interior/boundary split is a split of the **old channel index space**, whereas `\Delta G_{\rm geo}` is a Gram-form difference with pair entries.

Let

\[
\Lambda_U=I_U\sqcup B_U
\tag{GB10}
\]

be an eventual split into interior and boundary old channels. In the corresponding block coordinates,

\[
\boxed{
\Delta G_{\rm geo}^{U,V}
=
\begin{pmatrix}
\Delta_{II}&\Delta_{IB}\\
\Delta_{IB}^*&\Delta_{BB}
\end{pmatrix}.
}
\tag{GB11}
\]

Even if a future support theorem proves

\[
\Delta_{II}=0,
\tag{GB12}
\]

it does **not** imply that old geometry is purely a `BB` problem. A typical cross entry has the form

\[
\Delta_{ab}
=
\langle \phi_a,\,\phi_b(V)-\phi_b(U)\rangle,
\qquad a\in I_U,\quad b\in B_U,
\tag{GB13}
\]

so a full interior vector is tested against a moving boundary vector.

After old-metric normalization, this cross block can import conditioning from the interior sector. Therefore `GEO-IB` must remain a separate proof node.

For a self-adjoint normalized block operator of the schematic form

\[
H_{\rm geo}
=
\begin{pmatrix}
0&C\\
C^*&D
\end{pmatrix},
\tag{GB14}
\]

one has the conservative norm estimate

\[
\|H_{\rm geo}\|
\le \|D\|+\|C\|,
\tag{GB15}
\]

because the off-diagonal block operator has norm `\|C\|`. Consequently

\[
\operatorname{width}\sigma(H_{\rm geo})
\le 2\|D\|+2\|C\|.
\tag{GB16}
\]

In particular the looser estimate

\[
\operatorname{width}\sigma(H_{\rm geo})
\le 2\|H_{BB}\|+4\|H_{IB}\|
\tag{GB17}
\]

is safe but not sharp whenever the normalized block identification is exact. Constants are not the present bottleneck; the structural point is that `IB` survives even when `II` vanishes.

This corrects any reading of `GEO` as merely “old boundary channels”.

---

## 4. Normalization and support firewall

Before `GEO-II=0` can be promoted, the following exact frozen-definition checks are required.

### 4.1 Common-ambient compatibility

Verify the precise versions of

\[
E_TP_T=M_T,
\tag{GB18}
\]

\[
E_V\circ\iota_{U\to V}=E_U,
\tag{GB19}
\]

and

\[
M_U\le M_V.
\tag{GB20}
\]

Endpoint conventions matter: half-open versus closed windows, discrete index versus physical coordinate, and the treatment of a shift landing exactly at the boundary must be fixed from the frozen definitions.

### 4.2 Terminal-dependent normalization

Check whether the relevant inner product, measure, basis, extension, or channel normalization introduces a scalar or operator factor depending on `T`.

If such a factor exists, an interior channel may be geometrically unchanged as a function yet still change as a normalized Gram vector. In that case the correct theorem is not `GEO-II=0`; it is an exact known rescaling plus a residual tail term, with the rescaling allocated consistently between `GEO` and `COND`.

### 4.3 Robust tail formulation

The safe one-vector target is

\[
\boxed{
\|\phi_a(V)-\phi_a(U)\|
\le
\|(I-P_U)D_{s_a}E_U\phi_a^0\|
+
\mathrm{NormDrift}_a(U,V).
}
\tag{GB21}
\]

The first term is:

- exactly zero when the shifted support is contained in the old window;
- merely small when the frozen vectors have tails rather than compact support.

Any exponential tail estimate must be derived from the actual frozen vectors; it is not assumed here.

Thus the robust project target is `tail + normalization`, not an unconditional exact-zero slogan.

---

## 5. Boundary localization is not norm smallness

Even if `Q_{U,V}` projects onto a thin new boundary strip, the raw operator

\[
Q_{U,V}D_sM_U
\tag{GB22}
\]

can have norm `1`: an input unit vector may concentrate exactly where the shift crosses the old boundary.

Therefore neither

```text
boundary localized
```

nor

```text
pointwise stabilizes for every fixed old atom
```

implies

```text
operator norm -> 0.
```

This firewall blocks a premature proof of `B-METINC-GEO` from support geometry alone.

A weighted prime-power atomic estimate may still succeed because the coefficients

\[
a_{p,k}=\sqrt{\log p}\,p^{-3k/4}
\tag{GB23}
\]

decay, but such a route must first justify the precise synthesis/frame inequality, the old/new block interactions, and the old-metric conditioning. No bare scalar-series computation is booked as a Gram-operator estimate.

Hence boundary summability remains OPEN.

---

## 6. FD23 uniformity: abstract compactness lemma

The companion spectral-width audit correctly separates the summable majorant from the fixed-interval projected-tail limit.

For a fixed terminal interval `k`, set

\[
x_k(V)
:=
\mathcal U_S\mathscr M(U_k,V)
A_R(U_k,V)^{-1/2}\mathcal U_R^*\varepsilon_R,
\qquad
V\in[U_k,U_{k+1}].
\tag{GB24}
\]

Then the required fixed-interval term is

\[
\Delta_{m,k}^{\rm mod}
=
\sup_{V\in[U_k,U_{k+1}]}
\|P_mx_k(V)\|,
\tag{GB25}
\]

with the frozen FD23 convention `P_m\to0` strongly.

### Lemma GB-L1 — strong convergence is uniform on norm-compact sets ✓[M]

Let `T_m` be bounded operators on a Banach space with

\[
T_mx\to0\quad\text{for every }x,
\qquad
\sup_m\|T_m\|\le C<\infty.
\tag{GB26}
\]

Then for every norm-compact set `K`,

\[
\boxed{
\sup_{x\in K}\|T_mx\|\to0.
}
\tag{GB27}
\]

**Proof.** Fix `\varepsilon>0`. Choose a finite `\varepsilon/(2C)`-net `x_1,\ldots,x_N` of `K` (with the trivial modification if `C=0`). Strong convergence gives `m_0` such that

\[
\max_{1\le j\le N}\|T_mx_j\|<\varepsilon/2
\]

for all `m\ge m_0`. For `x\in K`, choose `x_j` in the net. Then

\[
\|T_mx\|
\le
\|T_m(x-x_j)\|+\|T_mx_j\|
<
C\frac{\varepsilon}{2C}+\frac\varepsilon2
=\varepsilon.
\]

This proves (GB27). `\square`

### Conditional FD23 corollary

If

\[
V\longmapsto x_k(V)
\tag{GB28}
\]

is norm-continuous on the compact interval `[U_k,U_{k+1}]`, then its image is norm compact. Taking `T_m=P_m` in GB-L1 yields

\[
\boxed{
\Delta_{m,k}^{\rm mod}\to0.
}
\tag{GB29}
\]

Thus norm-continuity is a sufficient route to the SW28 firewall.

**Important logical correction:** relative compactness of the vector family is a sufficient mechanism for (GB29); it is not asserted to be equivalent to (GB29) in general.

### What remains OPEN

For the actual R43 family (GB24), one still has to prove norm-continuity in `V` (or another compactness mechanism). A plausible derivative-free route is:

1. norm-continuity of the exact terminal metric increments `V\mapsto G_{X,V}` on the fixed compact interval;
2. pairwise spectral separation from zero on that interval;
3. continuity of inverse square roots and the Sylvester solution under those bounds.

None of these application-level continuity statements is silently promoted here.

Therefore:

- abstract lemma GB-L1: ✓[M];
- project node `FD23-UNIF`: OPEN.

This route uses no `dW_U/dU` generator and is compatible with the existing derivative firewall.

---

## 7. Refined B-METINC theorem tree

The previous exact high-level split remains:

```text
B-METINC
├─ B-METINC-NEW
├─ B-METINC-GEO
└─ B-METINC-COND
```

The `GEO` branch is now refined as

```text
B-METINC-GEO [OPEN]
├─ B-METINC-GEO-INT   / GEO-II [OPEN]
├─ B-METINC-GEO-CROSS / GEO-IB [OPEN]
└─ B-METINC-GEO-BDRY  / GEO-BB [OPEN]
```

and the dominated-convergence firewall is promoted to its own visible node:

```text
FD23-UNIF [OPEN]
```

The complete sufficient modulus route should therefore be read schematically as

```text
B-METINC-WIDTH [OPEN]
├─ summable width/conditioning majorants [OPEN]
│  ├─ B-METINC-NEW [OPEN]
│  ├─ B-METINC-GEO [OPEN]
│  │  ├─ GEO-INT / II [OPEN]
│  │  ├─ GEO-CROSS / IB [OPEN]
│  │  └─ GEO-BDRY / BB [OPEN]
│  └─ B-METINC-COND [OPEN]
└─ FD23-UNIF [OPEN]

B-METINC-WIDTH + FD23 machinery
  -> B-FLAGMOD contribution
  -> [with B-FLAGPHASE] B-FLAGTIGHT ?
  -> B-SIGN ?
  -> Strong Terminal ?
```

The arrows remain sufficient only where already established; no converse is asserted.

---

## 8. Next proof order

The next audit sequence is:

1. extract the exact frozen definitions of `P_T`, `E_T`, `D_s`, including endpoint and measure conventions;
2. verify or reject (GB18)–(GB20);
3. decide the terminal-normalization question;
4. prove the robust tail estimate (GB21), with exact zero only where justified;
5. define the actual interior/boundary channel split and estimate `GEO-BB` and `GEO-IB` separately;
6. independently prove a norm-continuity/compactness mechanism for the exact family (GB24), thereby closing `FD23-UNIF`;
7. only then attempt condition-weighted summability along a cofinal terminal partition.

A separate possible reduction of `COND` through a resolvent identity for

\[
B_T=(I+R_T^*R_T)^{-1}
\]

may later make `COND` dependent on `NEW+GEO`, but no such reduction is booked until the exact `R_T` increment structure is audited.

---

## 9. Governance / booking

- R43: OPEN.
- `R43-MI-LOEWNER`: OPEN, optional.
- `B-METINC-WIDTH`: OPEN.
- `B-METINC-NEW`: OPEN.
- `B-METINC-GEO`: OPEN.
- `B-METINC-GEO-INT` / `GEO-II`: OPEN.
- `B-METINC-GEO-CROSS` / `GEO-IB`: OPEN.
- `B-METINC-GEO-BDRY` / `GEO-BB`: OPEN.
- `B-METINC-COND`: OPEN.
- `FD23-UNIF`: OPEN.
- B-METINC: OPEN.
- B-FLAGMOD: OPEN.
- B-FLAGPHASE: OPEN.
- B-FLAGTIGHT: OPEN.
- B-SIGN: OPEN.
- Strong Terminal/C6: OPEN.
- abstract compactness lemma GB-L1: ✓[M] only as a general functional-analytic lemma.
- no new project-level `✓[M]`.
- no freeze.
- R38–R42 unchanged/frozen.
- R37/G4c separate and OPEN.
- no Object-X/RH promotion.
