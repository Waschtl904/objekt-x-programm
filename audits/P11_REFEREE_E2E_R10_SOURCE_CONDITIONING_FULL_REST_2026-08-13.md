# P11 End-to-End Referee Audit R10 — Source conditioning, Feshbach denominator and full-rest factorization

**Date:** 2026-08-13  
**Repository:** `Waschtl904/objekt-x-programm`  
**Branch:** `main`  
**Paper under review:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`

## Executive verdict

R10 audits the entry chain of P11 rather than the terminal/asymptotic output chain.

The current manuscript correctly defines the source-dependent martingale projection and its action on the residual marks, but it introduces an inconsistent hard prime-power cutoff in the residual operator.  The subsequent full-rest martingale factorization is written for the untruncated source-conditioned residual operator.  Hence the displayed identity

\[
\widetilde R_R^*\widetilde R_R=R_R^*R_R
\]

is false for the current paper definitions.

The defect is structural but locally repairable: restore the canonical C1z-B residual sum over all `k>=1`, whose effective support is finite on every fixed source window, while keeping the source-windowed neutral hub cutoff `p^k<=e^{2R}`.  Then the full-rest square factorization follows directly from the martingale coordinates.

Status:

\[
\boxed{
\begin{aligned}
[R10\text{-}A]&\quad \checkmark[M]_{\rm source\text{-}martingale\ projection},\\
[R10\text{-}B]&\quad \times[M]_{\rm residual\ cutoff\ mismatch},\\
[R10\text{-}C]&\quad \times[M]_{\widetilde R_R^*\widetilde R_R=R_R^*R_R\ \rm as\ currently\ written},\\
[R10\text{-}D]&\quad \checkmark[M]_{\rm canonical\ repair\ available},\\
[R10\text{-}E]&\quad ?[O]_{\rm downstream\ paper\ chain\ until\ repaired\ and\ rechecked}.
\end{aligned}
}
\]

**Overall R10 disposition:** **PAPER REPAIR REQUIRED — source-conditioning/Feshbach theorem core not refuted, but the current full-rest identity is false under the printed definition of `R_R`.**

---

## 1. What is correct at the source-conditioning level

The paper defines

\[
J_{p,R}(u)
=\max\left\{0,\left\lfloor\frac{2(R-|u|)_+}{\log p}\right\rfloor\right\}
\]

and the fiber projection

\[
\mathsf Q_R(u)\psi_{p,j}
=1_{\{j<J_{p,R}(u)\}}\psi_{p,j}.
\]

For

\[
\eta_{p,k}
=\sqrt{p-1}\sum_{j=0}^{k-1}p^{(j-k)/2}\psi_{p,j},
\]

this gives exactly

\[
\mathsf Q_R(u)\eta_{p,k}
=\sqrt{p-1}
\sum_{j=0}^{\min(k-1,J_{p,R}(u)-1)}p^{(j-k)/2}\psi_{p,j}.
\]

This part is algebraically correct.  In particular, the `a`-th martingale coordinate of the `p^k` residual mark survives exactly when

\[
a<J_{p,R}(u),\qquad a\le k-1.
\]

No R10 objection applies to this projection geometry.

---

## 2. The paper's residual cutoff differs from the canonical source-conditioned rest

The current paper prints

\[
(R_Rf)(u)
=\sum_{p^k\le e^{2R}}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Rf(u)\otimes\mathsf Q_R(u)\eta_{p,k}.
\tag{R10.1}
\]

The historical source-conditioning construction C1z-B instead defines the conditioned residual operator formally by

\[
\mathcal T_{R,{\rm res}}^{\bowtie}a(u)
=\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}a(u)\otimes\mathsf Q_R(u)\eta_{p,k}.
\tag{R10.2}
\]

Its fixed-`R` finiteness is proved from the geometry itself.  If a summand is nonzero, then `Q_R(u) eta_{p,k} != 0` forces `p<=e^{2R}`, while `D_{k log p}E_Rf(u) !=0` with `|u|<=R` forces

\[
\frac{k}{2}\log p\le R+|u|\le2R,
\]

hence

\[
\boxed{p^k\le e^{4R}.}
\tag{R10.3}
\]

Thus the canonical residual operator is still a finite sum at fixed `R`; it does not need the stronger artificial cutoff `p^k<=e^{2R}`.

C1z-B1 subsequently defines the neutral hub using the source-active label set

\[
\mathcal N_R=\{p^k:p^k\le e^{2R}\},
\]

but keeps the residual denominator abstractly equal to the full C1z-B conditioned rest.  The asymmetry is intentional: the neutral source-windowed hub and the source-conditioned residual denominator are not cut off in the same way.

Therefore (R10.1) is not the canonical C1z-B/B1 residual operator.

---

## 3. Why the printed full-rest factorization does not match (R10.1)

The paper defines

\[
K_s^{\rm tr}:=P_RD_sE_R
\]

and

\[
\Phi_{p,a,R}[f](u)
:=\sum_{k\ge a+1}p^{-3k/4}(K_{k\log p}^{\rm tr}f)(u),
\tag{R10.4}
\]

with no `p^k<=e^{2R}` restriction.  It then sets

\[
(\widetilde R_Rf)_{p,a}(u)
=\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,R}}(u)\Phi_{p,a,R}[f](u)
\]

and claims

\[
\widetilde R_R^*\widetilde R_R=R_R^*R_R.
\tag{R10.5}
\]

If `R_R` is the truncated operator (R10.1), its actual `a`-th martingale coefficient is instead

\[
\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,R}}(u)
\sum_{\substack{k\ge a+1\\ p^k\le e^{2R}}}
 p^{-3k/4}(K_{k\log p}^{\rm tr}f)(u).
\tag{R10.6}
\]

Thus (R10.4) and (R10.6) are different coefficient fields.  The identity (R10.5) cannot be obtained from the paper's own definition (R10.1).

---

## 4. Explicit counterexample to the current identity

The mismatch is not merely formal notation.  It produces different quadratic forms.

Choose

\[
\frac34\log2<R<\frac12\log3.
\tag{R10.7}
\]

For example, `R=0.53` works.  Then

\[
2<e^{2R}<3,
\]

so the paper's truncated residual operator (R10.1) contains only the label `(p,k)=(2,1)`.

Moreover

\[
1<\frac{2R}{\log2}<2,
\]

so the only nonempty `p=2` martingale target is `a=0`, with

\[
\Omega_{2,0,R}
=\left\{|u|\le R-\frac12\log2\right\}.
\]

Choose a small `epsilon>0` and set

\[
u_0=-R+\frac12\log2+\epsilon,
\qquad
x_0=u_0+\log2=-R+\frac32\log2+\epsilon.
\]

Because `R>3 log 2/4`, `epsilon` can be chosen so that `x_0<R`.  Let

\[
0\ne f\in C_c^\infty(-R,R)
\]

be supported in a sufficiently small neighborhood of `x_0`.

On a sufficiently small interval `I` around `u_0`, contained in `Omega_{2,0,R}`, one has

\[
K_{\log2}^{\rm tr}f=0,
\qquad
K_{2\log2}^{\rm tr}f\ne0.
\tag{R10.8}
\]

Indeed, the `k=2` positive translate maps `u_0` to `x_0`, while the `k=1` translate points are separated from the support of `f`.  For `k>=3` both translated points lie outside the support window after shrinking `I` if necessary.

Hence the actual truncated residual coefficient (R10.6) vanishes on `I`, whereas the printed full-rest coefficient (R10.4) contains the nonzero term

\[
2^{-3/2}K_{2\log2}^{\rm tr}f.
\]

The `k=1` and `k=2` source pieces can be chosen with disjoint `u`-supports, and there are no other prime or martingale channels under (R10.7).  Therefore

\[
\|\widetilde R_Rf\|^2
>
\|R_Rf\|^2.
\]

Consequently

\[
\boxed{
\widetilde R_R^*\widetilde R_R\ne R_R^*R_R
}
\]

for the current manuscript definitions.

This is a genuine `x[M]` result against the printed identity, not a missing-explanation issue.

---

## 5. Canonical repair and direct derivation of the full-rest squares

The clean repair is to restore the source-conditioned residual operator itself:

\[
\boxed{
(R_Rf)(u)
=\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
D_{k\log p}E_Rf(u)\otimes\mathsf Q_R(u)\eta_{p,k}.
}
\tag{R10.9}
\]

At fixed `R`, (R10.3) makes this sum effectively finite, so boundedness is unchanged.

Now expand the `p`-sector in the orthonormal martingale basis.  The coefficient of `psi_{p,a}` is

\[
\begin{aligned}
&\sum_{k\ge1}
\sqrt{\log p}\,p^{-k/4}
(K_{k\log p}^{\rm tr}f)(u)
\sqrt{p-1}\,p^{(a-k)/2}
1_{\{a<k\}}1_{\{a<J_{p,R}(u)\}}\\
&=\sqrt{(\log p)(p-1)p^a}\,
1_{\Omega_{p,a,R}}(u)
\sum_{k\ge a+1}p^{-3k/4}(K_{k\log p}^{\rm tr}f)(u).
\end{aligned}
\tag{R10.10}
\]

This is exactly the printed `\widetilde R_R` coefficient.

Orthogonality of the `psi_{p,a}` and of different prime sectors then gives

\[
\boxed{
\begin{aligned}
\langle R_Rf,R_Rg\rangle
&=
\sum_p(\log p)(p-1)
\sum_{a\ge0}p^a
\int_{\Omega_{p,a,R}}
\Phi_{p,a,R}[f](u)
\overline{\Phi_{p,a,R}[g](u)}\,du,
\end{aligned}
}
\tag{R10.11}
\]

and hence

\[
\boxed{
\widetilde R_R^*\widetilde R_R=R_R^*R_R.
}
\tag{R10.12}
\]

Thus the full-rest theorem core is recoverable by a local definition repair plus an explicit paper proof.

---

## 6. Downstream impact

The current proof of the sharp odd theorem invokes the full-rest identity in Step 1 and the `a=0` full-rest lift in Step 6.  Therefore, under the manuscript as presently printed, that end-to-end proof chain contains a false dependency.

This does **not** by itself refute the sharp odd asymptotic.  The canonical repair (R10.9) restores the full-rest operator used by the historical C6q/C6s/O3d-I1 chain, and the later paper estimates were already written with unrestricted geometric tails in the martingale-square representation.  Nevertheless the downstream paper chain must be rechecked after the definition repair before R10 can be promoted to `PASS`.

No conclusion about terminal transport follows from this defect.

---

## 7. Firewalls

R10 does not show that the Feshbach construction is impossible.  It does not show that the sharp odd theorem is false.  It does not prove or disprove

\[
K_{R,S}^{T,U}\to I,
\qquad
W_{R,S,-}^{[T]}\text{ strongly Cauchy},
\]

and it has no Object-X or RH consequence.

The finding is precise:

\[
\boxed{
\text{current printed }R_R
\quad\text{and current printed }\widetilde R_R
\quad\text{do not describe the same residual Gram geometry}.}
\]
