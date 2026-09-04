# P11 / R43 — post-merge strict referee reconciliation

**Date:** 2026-09-04  
**Status:** exact reconciliation of the strict cross-model audit received after merge `b4e0293fbace457838e3fe07abbafcaf4acca19b`; R43 and `B-METINC-COND` remain OPEN.

## 0. Scope

This note rechecks the four mathematical objections raised against

`audits/P11_R43_COND_COFINAL_PSD_KERNEL_WITNESS_NOGO_2026-09-04.md`

and separates true scope corrections from rejected objections. It does not promote Strong Terminal/C6, B-FLAGTIGHT, Object X, or RH.

The strict review is useful, but several of its mathematical objections conflate local finiteness with uniform separation or omit factors already present in the merged proof.

---

## 1. Resonance set: local finiteness is correct

The merged witness defines

\[
\Lambda=\{n a_p:\ p\text{ prime},\ n\ge2\},\qquad a_p=\tfrac12\log p.
\]

For every **fixed** compact interval `[0,L]`,

\[
na_p\le L\iff p^n\le e^{2L}.
\]

There are only finitely many prime powers below `e^{2L}`. Hence

\[
\boxed{\Lambda\text{ is locally finite}.}
\]

The referee observation that the number of points in a moving window near a large `U` can grow rapidly does **not** contradict local finiteness. Local finiteness is not a uniform lower-gap assertion as `U\to\infty`.

The proof needs only: for an arbitrarily large selected `U` with

\[
2U-a_2\notin\Lambda,
\]

the fixed-point distance

\[
\rho_U=\operatorname{dist}(2U-a_2,\Lambda)>0.
\]

This follows from local finiteness. No uniform lower bound on `\rho_U` is claimed or needed; `h` and `\ell` are chosen **after** `U`, proportional to that possibly tiny `\rho_U`.

Therefore no prime-counting estimate such as `\ell\lesssim Ue^{-U}` is required for existence of the witness. Such an estimate could describe a possible size scale of gaps, but the theorem is purely existential and adapts `h,\ell` to the actual positive gap.

Booking remains:

```text
R43-COND-WITNESS-RESONANCE-LOCAL-FINITENESS ✓[M]
```

---

## 2. Exact kernel statement `Cf=0`: no missing k=1 danger

The new layer index `j` always satisfies `j>=1`, and a newly exposed martingale layer sees only residual translation indices `k>=j` through

\[
\sum_{k\ge j}p^{-3k/4}D_{k\log p}E_Uf(u).
\]

For positive-side depth-increment rows, the support interval `I_P` sits a distance

\[
d=a_2-\varepsilon\in(3a_2/4,a_2)
\]

inside the right old boundary. Combining the depth-layer strip with `k>=j` makes a same-side hit impossible.

For negative-side rows, any hit of the positive `I_P` is an opposite-boundary translation and forces

\[
|2U-a_2+\varepsilon-(j+k)a_p|<h+\ell,
\]

with `j+k>=2`. This is exactly why `\Lambda` starts at `n>=2`: the dangerous resonance parameter is `n=j+k`, not a free residual index `k=1` by itself.

The gap choice excludes all such rows simultaneously. Thus the merged conclusion

\[
\boxed{Cf=0}
\]

is a full-operator support statement, not a `p=2`-sector statement.

Booking remains:

```text
R43-COND-C-KERNEL-WITNESS-REALIZED ✓[M]_neg
```

---

## 3. The coefficient `2^{-9/4}` is reproducible

For the isolated first `p=2`, adjacent-index overlap `(l,k)=(1,2)`, the two frozen residual coefficients are

\[
\sqrt{\log2}\,2^{-1/4},\qquad
\sqrt{\log2}\,2^{-1/2}.
\]

Their product is

\[
(\log2)2^{-3/4}.
\]

On the output interval the terminal depth is `J_{2,V}=2`, and the frozen mark Gram factor is

\[
\langle q_{2,1;V},q_{2,2;V}\rangle
=2^{-1/2}-2^{-3/2}=2^{-3/2}.
\]

Hence the full contribution is

\[
\boxed{
\ell(\log2)2^{-3/4}2^{-3/2}
=\ell(\log2)2^{-9/4}>0.
}
\]

The referee's proposed `2^{-3/4}` omitted the mark-Gram factor.

Booking:

```text
R43-COND-WITNESS-WEIGHT-DERIVATION ✓[M]
```

---

## 4. No noncancellation gap

Because `I_P=I_Q-a_2`, exact overlap of translated copies requires

\[
|k-l|a_p=a_2
\quad\text{or}\quad
(k+l)a_p=a_2.
\]

The second is impossible. The first forces

\[
p=2,\qquad |k-l|=1.
\]

At fixed terminal `V`, only finitely many translated copies of the compact witness supports can meet the target window. After shrinking `\ell`, every non-exact mismatch is disjoint. Therefore only exact `p=2` adjacent-index overlaps survive.

For every surviving adjacent-index overlap, the two translation signs agree, so their sign product is positive; the frozen mark-Gram coefficients are nonnegative. The `(1,2)` overlap is strictly positive. Hence the complete scalar product satisfies

\[
\boxed{\langle Mf,Sg\rangle>0}
\]

with no cancellation possibility.

Thus

\[
\boxed{S^*Mf\ne0.}
\]

Booking:

```text
R43-COND-WITNESS-NONCANCELLATION ✓[M]
```

---

## 5. No geometry contradiction with the earlier `F_K` witness

The earlier target-orthogonality witness used source intervals separated by

\[
\log2=2a_2
\]

and consequently selected a different exact overlap pattern, including `|k-l|=2` channels.

The kernel witness intentionally uses

\[
a_2=\tfrac12\log2
\]

so that adjacent-index `|k-l|=1` overlaps survive while the newly exposed layer can be killed by support engineering.

These are distinct constructions. The kernel witness derives its own overlap relation, its own depth values, and its own Gram factor; no `F_K` formula is imported.

Booking:

```text
R43-COND-WITNESS-GEOMETRY-CONSISTENCY ✓[M]
```

---

## 6. Resolvent immunity

For any bounded `S`, the positive operator

\[
I+S^*S\succeq I
\]

is invertible, hence `(I+S^*S)^{-1/2}` is injective. Therefore

\[
S^*y\ne0
\Longrightarrow
\|(I+S^*S)^{-1/2}S^*y\|^2>0.
\]

No quantitative lower bound, no uniform bound on `||S||`, and no `beta<1` hypothesis is needed for strict negativity of the witness. Thus the exact sign conclusion is immune to the earlier strip-norm growth issue.

Book:

```text
R43-COND-WITNESS-RESOLVENT-IMMUNITY ✓[M]
```

---

## 7. Genuine scope correction: uniform local PSD versus partition-selective PSD

The proved quantifier statement is

\[
\forall U_*,h_*>0\ \exists U\ge U_*\ \exists h\in(0,h_*):
K_{U,U+h}^{\rm Schur}\not\succeq0.
\]

This exactly falsifies the **uniform eventual fine-step** assertion

\[
\exists U_*,h_*>0\ \forall U\ge U_*\ \forall h\in(0,h_*):
K_{U,U+h}^{\rm Schur}\succeq0.
\]

It also falsifies pairwise canonical PSD for all pairs.

However it does **not** exclude the existence of a specially selected cofinal partition

\[
U_0<U_1<\cdots\to\infty
\]

whose used increments happen to satisfy PSD. Therefore the old label

```text
R43-COND-LOEWNER-ANTITONE-TELESCOPE-ROUTE ×[M]
```

was too broad. From now on it is scope-corrected to

```text
R43-COND-UNIFORM-LOCAL-LOEWNER-TELESCOPE-ROUTE ×[M]
```

and a separate node is opened:

```text
R43-COND-PARTITION-SELECTIVE-PSD ?[O]
```

No claim is made that such a partition exists; it is simply not excluded by the kernel witness.

---

## 8. Was canonical PSD necessary? No — it was an accelerator

The earlier terminal-metric definition audit already stated before the no-go that Loewner monotonicity is an **accelerator, not a prerequisite** for B-FLAGMOD. The unconditional bound

\[
\|\mathscr E_{U,V}\|\le\|\mathbf H_S^{U,V}\|
\]

requires no Loewner positivity.

Therefore the no-go should be described precisely as

> elimination of an overstrong uniform Loewner/PSD helper route,

not as a no-go for `B-METINC-COND`, B-FLAGDYN, or Strong Terminal.

The theorem is still strategically valuable because it prevents further work on a false universal helper claim, but it is not a necessary-gate failure.

---

## 9. Epsilon-relaxed telescope: promising OPEN route, but no `Ue^{-U}` theorem yet

A legitimate new target is

\[
K_{U,V}^{\rm Schur}\succeq-\delta(U,V)I
\]

or the corresponding vector-sensitive scalar inequality, with a chosen cofinal partition satisfying

\[
\sum_j\delta(U_j,U_{j+1})<\infty.
\]

Book only:

```text
R43-COND-EPSILON-RELAXED-TELESCOPE ?[O]
```

The strict review's suggested scale `\delta\sim Ue^{-U}` is **not proved** by the kernel witness. The witness provides a negative test direction; it does not furnish a lower bound on the whole operator `K`, and the injective resolvent factor supplies no quantitative lower singular-value bound when `||S||` grows. In particular, one witness Rayleigh quotient controls `\lambda_{\min}` in the wrong direction for the claimed global lower bound.

Thus the epsilon-relaxed route is genuinely promising but starts OPEN without a booked decay rate.

---

## 10. Provenance of the structured-vector target before any PR #54 calculation

The structured vector is not introduced after the no-go. It appears in the terminal metric increment definition audit created in commit

```text
ca370c6b95c0a454da82376bc82b9e2261113e0d
```

(`R43: audit terminal metric increments before shell reindexing`), before the COND kernel-witness work.

That audit defines, as equation `(MI12)`,

\[
\boxed{v_T(f):=H_T^*E_{X,T}f\in L^2(-T,T)}
\]

and equation `(MI15)` identifies the old-conditioning term as

\[
\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle.
\]

Thus PR #54's restriction to this structured path is a return to the original canonical scalar term, not an ad-hoc post-no-go narrowing.

Provenance of the older auxiliary comparator remains

```text
669cda8204228f25ea840ea81733fdeb30c39cc4
```

file `audits/P11_R43_COND_COMPRESSION_REANCHOR_AUDIT_2026-09-04.md`, equation `(C11)`, GitHub author/committer timestamp `2026-09-04T17:45:39Z`.

---

## 11. Post-merge governance note

PR #53 was merged before this stricter cross-model audit arrived. The present reconciliation finds:

- the mathematical kernel-witness theorem survives;
- the four alleged core proof gaps are closed/rejected by the merged derivation itself;
- one real taxonomy/scope issue exists: the telescope-route label was too broad;
- no rollback of `CANONICAL-PSD-REALIZATION ×[M]` or `COFINAL-LOCAL-PSD ×[M]` is mathematically justified;
- the telescope label must be narrowed, and partition-selective / epsilon-relaxed alternatives remain OPEN.

Future merge decisions on PR #54 should preserve this distinction and should not treat this cross-model audit as independent peer review or project-level GREEN.

---

## 12. Status after reconciliation

```text
R43-COND-C-KERNEL-WITNESS-REALIZED                 ✓[M]_neg
R43-COND-WITNESS-RESONANCE-LOCAL-FINITENESS       ✓[M]
R43-COND-WITNESS-WEIGHT-DERIVATION                 ✓[M]
R43-COND-WITNESS-NONCANCELLATION                   ✓[M]
R43-COND-WITNESS-GEOMETRY-CONSISTENCY              ✓[M]
R43-COND-WITNESS-RESOLVENT-IMMUNITY                ✓[M]
R43-COND-COFINAL-LOCAL-PSD                          ×[M]
R43-COND-CANONICAL-PSD-REALIZATION                  ×[M]
R43-COND-UNIFORM-LOCAL-LOEWNER-TELESCOPE-ROUTE      ×[M]
R43-COND-PARTITION-SELECTIVE-PSD                    ?[O]
R43-COND-EPSILON-RELAXED-TELESCOPE                  ?[O]
B-METINC-COND                                       OPEN
Strong Terminal/C6                                  OPEN
```

Standard no-go firewall: this result does **not** exclude positivity along the structured path `v_U`, partition-selective positivity, epsilon-relaxed antitonicity with summable error, COND-INNER positivity, another `B-METINC-COND` decomposition, B-FLAGTIGHT, Strong Terminal/C6, Object X, or RH.
