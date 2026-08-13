# P11 End-to-End Referee Audit R10 — Reconciliation

**Date:** 2026-08-13  
**Original audit:** `audits/P11_REFEREE_E2E_R10_SOURCE_CONDITIONING_FULL_REST_2026-08-13.md`

## Repair

The structural defect found by R10 is repaired in paper commit

`cdca16d0119dca0b91f27f5dc2daee7e81c73dcb`.

Equation (2.6) now restores the canonical source-conditioned residual operator

\[
(R_Rf)(u)=\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}D_{k\log p}E_Rf(u)
\otimes\mathsf Q_R(u)\eta_{p,k}.
\]

The manuscript proves effective fixed-window finiteness: a nonzero summand forces

\[
p\le e^{2R},\qquad p^k\le e^{4R}.
\]

Thus the residual sum is untruncated in notation but finite and bounded at every fixed source level.

For

\[
\Phi_{p,a,R}[f](u)=\sum_{k\ge a+1}p^{-3k/4}K_{k\log p}^{\rm tr}f(u),
\]

the paper now computes the exact `psi_{p,a}` coordinate of `R_Rf` as

\[
\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,R}}(u)\Phi_{p,a,R}[f](u).
\]

Orthogonality of martingale coordinates and distinct prime sectors yields

\[
\langle\widetilde R_Rf,\widetilde R_Rg\rangle
=\langle R_Rf,R_Rg\rangle,
\]

hence

\[
\boxed{\widetilde R_R^*\widetilde R_R=R_R^*R_R.}
\]

Therefore the two original R10 `times[M]` findings are repaired.

## Build verification

Guarded GitHub Actions run `31707067633`:

- found each old target block exactly once;
- applied exactly two replacements;
- passed `git diff --check`;
- compiled P11 twice with `pdflatex`;
- passed the unresolved-reference/citation and multiply-defined-label rejection check;
- committed only the paper as `cdca16d0119dca0b91f27f5dc2daee7e81c73dcb`.

## Forced Theorem 6.1 downstream recheck

### Step 1

Step 1 uses

\[
A_T=I+R_T^*R_T=I+\widetilde R_T^*\widetilde R_T
\]

and explicitly estimates the full tail `k>J`. For `J=j<k`,

\[
\|\mathsf Q_T(u)\eta_{p,k}\|^2
=p^{j-k}-p^{-k}\le p^{j-k}.
\]

This gives

\[
\|F_{p,T}\|_2^2\lesssim\frac{(\log p)^2}{p^2},
\qquad
\sup_T\|R_T\mathbf1_T\|_2^2<\infty,
\]

and hence `d_T=2T+O(1)`. The argument is exactly compatible with the repaired full residual.

Status: `✓[M]`.

### Step 6

Step 6 uses the exact `a=0` full-rest channel

\[
(\widetilde R_Tf)_{q,0}
=P_{q,T}f+
\sqrt{(\log q)(q-1)}1_{\Omega_{q,0,T}}
\sum_{k\ge2}q^{-3k/4}K_{k\log q}^{\rm tr}f.
\]

Thus it already requires the same untruncated higher-prime-power tail restored by R10. The tail estimate

\[
\|E_T^{\rm fut}\|\le C\sqrt{T+1}e^{-T/2}
\]

and the full-rest lift remain valid.

Status: `✓[M]`.

## Reconciled verdict

\[
\boxed{
[R10\text{-}A]\ \checkmark[M],\quad
[R10\text{-}B]\ \checkmark[M]_{\rm repaired},\quad
[R10\text{-}C]\ \checkmark[M]_{\rm repaired},\quad
[R10\text{-}D]\ \checkmark[M],\quad
[R10\text{-}E]\ \checkmark[M].
}
\]

**R10: PASS AFTER STRUCTURAL PAPER REPAIR.**

The source-conditioning/Feshbach/full-rest theorem core is retained. This repair also closes the full-rest self-containment item previously recorded inside R1; the other local R1 issues are unchanged.

The following remain open and untouched:

\[
?[O]_{\rm uniform\ finite\text{-}jet\ Gram/square\text{-}root\ control},
\qquad
?[O]_{K_{R,S}^{T,U}\to I},
\qquad
?[O]_{W_{R,S,-}^{[T]}\ \mathrm{strong\ Cauchy}},
\]

together with the polar-gauge problem and the wider Object-X/global obligations.

No SYN, Seal, Object-X closure, or RH conclusion is added by R10.
