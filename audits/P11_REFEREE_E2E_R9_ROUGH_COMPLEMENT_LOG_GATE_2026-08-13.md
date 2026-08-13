# P11 End-to-End Referee Audit R9 — Rough complement and logarithmic prime-cell gate

**Date:** 2026-08-13  
**Repository:** `Waschtl904/objekt-x-programm`  
**Branch:** `main`  
**Paper under review:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Relevant paper modules:** `P11_O3_Diagnostic_Proofs.tex`, `P11_O3j_Reconciliation.tex`

## Executive verdict

- **[R9-A] ✓[M]** — the explicit compact odd rough-complement vector `g_h=(I-Pi^raw)h` is valid and nonzero.
- **[R9-B] ✓[M]** — every such nonzero odd `g_h` has a finite first nonzero integral jet.
- **[R9-C] ✓[M]** — the logarithmic translation lemma
  \[
  F\in\mathscr H_{\log}^{\alpha}
  \Longrightarrow
  \|\tau_tF-F\|_2=o((\log(1/t))^{-\alpha})
  \]
  is correct.
- **[R9-D] ✓[M]** — the sufficient finite-log threshold `alpha >= m+3/2` for the robust prime-cell quadrature is correct.
- **[R9-E] ✓[M]_part** — the current paper states the prime-cell threshold but does not include the quantitative rough quadrature estimate from which it follows. Thus the manuscript is not end-to-end self-contained at this gate.

**Overall R9 status:** **PAPER REPAIR REQUIRED — mathematical claims retained; prime-cell derivation missing from the paper.**

---

## 1. Explicit rough complement

Fix `0<R<S<T_0`. Write

\[
G_R^0:=G_{R,T_0},\qquad G_S^0:=G_{S,T_0},\qquad J:=J_{R,S}.
\]

The paper defines

\[
\Pi^{\rm raw}:=J(G_R^0)^{-1}J^*G_S^0.
\]

By the exact pullback identity

\[
J^*G_S^0J=G_R^0,
\]

one has

\[
(\Pi^{\rm raw})^2=\Pi^{\rm raw}.
\]

Choose a nonzero smooth odd annulus vector `h` with support disjoint from `[-R,R]` and put

\[
g_h:=(I-\Pi^{\rm raw})h.
\]

Then

\[
\begin{aligned}
J^*G_S^0g_h
&=J^*G_S^0h
 -J^*G_S^0J(G_R^0)^{-1}J^*G_S^0h\\
&=J^*G_S^0h-G_R^0(G_R^0)^{-1}J^*G_S^0h\\
&=0.
\end{aligned}
\]

Parity is preserved by the finite-terminal metric architecture, so `g_h` is odd. Therefore

\[
\boxed{g_h\in\mathcal C^-_{S,T_0}(R).}
\]

Moreover `Pi^raw h` lies in `Ran J` and is therefore supported in `[-R,R]` as a raw source function, whereas `h` is nonzero on the annulus. On that annulus

\[
g_h=h,
\]

so

\[
\boxed{g_h\ne0.}
\]

Its support is contained in the compact union `[-R,R] union supp(h)`, hence is compactly contained in `(-S,S)`.

---

## 2. Finite first jet

The integral-jet completeness theorem states that on the odd sector

\[
\bigcap_{m\ge0}\ker\beta_S^{(m)}=\{0\}.
\]

Since `g_h` is odd and nonzero, not all jets can vanish. Because the index set is the nonnegative integers, there is a finite first index

\[
\boxed{
m_h:=\min\{m\ge0:\beta_S^{(m)}(g_h)\ne0\}<\infty.
}
\]

No smoothness of `g_h` is needed for this conclusion.

---

## 3. Logarithmic translation lemma

For `alpha>0`, define

\[
\mathscr H_{\log}^{\alpha}(\mathbb R)
:=\left\{F\in L^2:\int [\log(2+|\xi|)]^{2\alpha}|\widehat F(\xi)|^2d\xi<\infty\right\}.
\]

Let `0<t<1` and set `M=t^{-1/2}`. By Plancherel,

\[
\|\tau_tF-F\|_2^2
=\frac1{2\pi}\int |e^{it\xi}-1|^2|\widehat F(\xi)|^2d\xi.
\]

For `|xi|<=M`,

\[
|e^{it\xi}-1|^2\le t^2\xi^2\le t,
\]

so the low-frequency contribution is `O(t)=o((log(1/t))^{-2 alpha})`.

For `|xi|>M`, use `|e^{it xi}-1|^2<=4` and the weighted tail:

\[
\int_{|\xi|>M}|\widehat F(\xi)|^2d\xi
\le [\log(2+M)]^{-2\alpha}
\int_{|\xi|>M}[\log(2+|\xi|)]^{2\alpha}|\widehat F(\xi)|^2d\xi.
\]

The last weighted tail tends to zero and `log(2+M) asymp log(1/t)`. Therefore

\[
\boxed{
\|\tau_tF-F\|_2
=o((\log(1/t))^{-\alpha}).
}
\]

Thus the translation statement printed in the paper is correct.

---

## 4. Why the threshold is `m+3/2`

The robust future-prime cell analysis has cell width

\[
\delta_T\lesssim e^{-2T/5}
\]

and rough quadrature error of the form

\[
\boxed{
\|Z_T^{\rm quad,rough}\|_2
\le
Ce^{T/2}\sqrt T
\bigl[\delta_T\|f\|_2+\omega_f(2\delta_T)\bigr]
+Z_T^{\rm anchor},
}
\]

where

\[
\omega_f(t):=\|\tau_tE_Sf-E_Sf\|_2,
\qquad
\|Z_T^{\rm anchor}\|_2=o(\sqrt{M_T}),
\]

and for a fixed compact odd vector of first jet `m`,

\[
\sqrt{M_T}\asymp_f \frac{e^{T/2}}{T^{m+1}}.
\]

The cell-width term is automatically negligible because

\[
\frac{e^{T/2}\sqrt T\,\delta_T}{e^{T/2}T^{-m-1}}
\lesssim T^{m+3/2}e^{-2T/5}\to0.
\]

The translation term is negligible precisely under the sufficient condition

\[
\boxed{
\omega_f(2\delta_T)=o(T^{-m-3/2}).
}
\]

If

\[
E_Sf\in\mathscr H_{\log}^{\alpha},
\]

the translation lemma and `log(1/delta_T) >= (2/5)T-O(1)` give

\[
\omega_f(2\delta_T)=o(T^{-\alpha}).
\]

Hence every

\[
\boxed{\alpha\ge m+\frac32}
\]

closes this robust prime-cell quadrature argument. In particular

\[
E_Sf\in\mathscr H_{\log}^{m+3/2}
\]

is sufficient.

The exponent and the endpoint are therefore correct: the little-`o` in the translation lemma makes equality `alpha=m+3/2` sufficient.

---

## 5. Native Gamma baseline

The paper has

\[
m_\Gamma(\xi)\asymp\log(2+|\xi|).
\]

Therefore the Gamma form domain corresponds, up to equivalent fixed-window norms, to the logarithmic exponent

\[
2\alpha=1,
\qquad
\boxed{\alpha=\frac12.}
\]

For a first jet `m`, the sufficient prime-cell threshold is `m+3/2`, so the additional logarithmic order above the native Gamma form is

\[
\boxed{m+1.}
\]

This arithmetic in the paper is correct.

---

## 6. The actual end-to-end defect

The current main paper states, in prose, that the robust prime-cell quadrature closes under

\[
E_Sf\in\mathscr H_{\log}^{m+3/2},
\]

but the paper modules presently included do **not** derive the rough quadrature bound displayed in Section 4 above. The O3 diagnostic module stops at the second-moment/complement representation, while the O3j reconciliation proves a separate operator-domain gain and explicitly leaves the higher logarithmic complement regularity open.

The quantitative derivation exists in the historical O3i audit, but under end-to-end referee rules an audit file is not a substitute for a paper proof.

### Required paper repair

Insert a concise lemma/proposition before the logarithmic gate containing:

1. the future-prime cell-width bound `delta_T <= C e^{-2T/5}`;
2. the rough quadrature estimate
   \[
   \|Z_T^{\rm quad,rough}\|_2
   \le Ce^{T/2}\sqrt T[\delta_T\|f\|_2+\omega_f(2\delta_T)]
   +o(\sqrt{M_T});
   \]
3. the scale `sqrt(M_T) asymp e^{T/2}T^{-m-1}`;
4. the translation-modulus lemma or its short Fourier proof;
5. the deduction `alpha >= m+3/2`.

Until that is inserted, the paper's gate statement is mathematically correct but not internally proved.

---

## 7. Firewalls

The explicit `g_h` is only known at the native graph/domain regularity supplied by the finite-window construction. R9 does not prove

\[
E_Sg_h\in\mathscr H_{\log}^{m_h+3/2}.
\]

It therefore does not produce the desired polynomial second-moment witness.

Nor does it prove any failure of strong terminal transport. The following remain open:

\[
?[O]_{\rm logarithmic\ complement\ regularity},
\qquad
?[O]_{\nu_2\ \rm polynomial\ witness},
\qquad
?[O]_{\rm polar\ gauge},
\qquad
?[O]_{W_{R,S,-}^{[T]}\ \rm strong\ Cauchy}.
\]

---

## Final referee disposition

\[
\boxed{
[R9\text{-}A,B,C,D]\ \checkmark[M],
\qquad
[R9\text{-}E]\ \checkmark[M]_{\rm part}.
}
\]

**R9: PAPER REPAIR REQUIRED — mathematical gate retained; proof integration incomplete.**
