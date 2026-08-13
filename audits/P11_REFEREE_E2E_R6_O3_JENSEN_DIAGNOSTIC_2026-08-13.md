# P11 End-to-End Referee Audit R6 — O3 Jensen diagnostic and the polar-gauge gap

**Date:** 2026-08-13  
**Repository:** `Waschtl904/objekt-x-programm`  
**Branch:** `main`  
**Paper under review:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Proof module checked:** `papers/P11_sections/P11_O3_Diagnostic_Proofs.tex`

## Referee mode

This is an end-to-end paper audit. Earlier O3 audit nodes are not used as missing proof pieces; they are only destructive cross-checks. The paper must justify its stated implication from its own definitions and proofs.

## Executive verdict

- **[R6-A] ✓[M]** — the O3 Jensen/second-moment algebra controlling the auxiliary operator `Q` is retained.
- **[R6-B] ×[M]** — the phrase **“sufficient route to terminal convergence”** is too strong as presently written. The proved estimate controls `Q`, not the actual future transport `W^{[U]}`.
- **[R6-C] ?[O]** — control of the polar unitary gauges, hence strong Cauchy/terminal convergence of `W_{R,S,-}^{[T]}`, remains open.

**Overall R6 status:** **PAPER REPAIR REQUIRED — theorem core (Jensen algebra) retained.**

This finding does **not** refute terminal convergence and does **not** invalidate the Jensen inequality itself. It is a reach/implication error.

---

## 1. What the paper proves

For fixed base terminal `T_0` and future terminal `U`, the O3 proof module introduces relative positive metrics

\[
A_R=A_{T_0,U}^{R,-},\qquad A_S=A_{T_0,U}^{S,-},
\]

and the auxiliary comparison operator

\[
Q:=A_S^{1/2}W_{R,S,-}^{[T_0]}A_R^{-1/2}.
\]

The Jensen/second-moment argument yields an estimate of the form

\[
\|Q-W_{R,S,-}^{[T_0]}\|
\le
\frac{\sqrt{2d(A_R)}}{\sqrt{\lambda_{\min}(A_R)}},
\]

with the scalar Jensen defect bounded by the O3 product diagnostic,

\[
d(A_R)\le \chi_-(T_0,U)^2\,\|\Theta_-(T_0,U)\|^2.
\]

Consequently, under the hypotheses used in the O3 reduction,

\[
\chi_-(T_0,U)\,\|\Theta_-(T_0,U)\|\to0
\]

implies

\[
\boxed{
\|Q-W_{R,S,-}^{[T_0]}\|\to0.
}
\]

This implication is mathematically retained:

\[
\boxed{[R6\text{-}A]\ \checkmark[M].}
\]

---

## 2. The missing promotion from `Q` to the actual future transport

The actual finite-terminal transport is

\[
W_{R,S,-}^{[T]}
=(G_{S,T}^{-})^{1/2}J_{R,S}^{-}(G_{R,T}^{-})^{-1/2}.
\]

The relative metrics are

\[
A_R=(G_{R,T_0}^{-})^{-1/2}G_{R,U}^{-}(G_{R,T_0}^{-})^{-1/2},
\]

\[
A_S=(G_{S,T_0}^{-})^{-1/2}G_{S,U}^{-}(G_{S,T_0}^{-})^{-1/2}.
\]

Define

\[
X_R:=(G_{R,U}^{-})^{1/2}(G_{R,T_0}^{-})^{-1/2},
\qquad
X_S:=(G_{S,U}^{-})^{1/2}(G_{S,T_0}^{-})^{-1/2}.
\]

Then

\[
X_R^*X_R=A_R,
\qquad
X_S^*X_S=A_S.
\]

Because these operators are boundedly invertible, their polar decompositions have unitary polar factors:

\[
X_R=U_R A_R^{1/2},
\qquad
X_S=U_S A_S^{1/2}.
\]

Thus

\[
X_R^{-1}=A_R^{-1/2}U_R^*.
\]

Using

\[
W_{R,S,-}^{[U]}
=X_S\,W_{R,S,-}^{[T_0]}\,X_R^{-1},
\]

we obtain the exact identity

\[
\boxed{
W_{R,S,-}^{[U]}
=U_S\,Q\,U_R^*.
}
\]

This is the decisive referee point.

The O3 Jensen estimate controls `Q`; it does **not** control the unitary factors `U_S,U_R`.

Therefore

\[
Q\to W_{R,S,-}^{[T_0]}
\]

does not by itself imply

\[
W_{R,S,-}^{[U]}\to W_{R,S,-}^{[T_0]}.
\]

A separate polar-gauge theorem would be required, for example sufficient control forcing the two unitary factors to converge compatibly to the identity (or another condition showing that their combined conjugation becomes asymptotically harmless on the relevant vectors).

No such control is proved in the current P11 paper or in the checked O3 proof module. A repository search for an additional polar/unitary bridge did not reveal a theorem closing this gap.

Hence

\[
\boxed{[R6\text{-}B]\ \times[M].}
\]

---

## 3. Why the logical implication genuinely fails without gauge control

The failure is structural, not a matter of constants.

In a toy finite-dimensional model let

\[
Q_n=W_0=I,
\]

so that `Q_n -> W_0` even identically. Let

\[
U_{R,n}=I,
\qquad
U_{S,n}=e^{i\theta_n}I,
\]

where `e^{i\theta_n}` does not converge to `1`. Then

\[
W_n=U_{S,n}Q_nU_{R,n}^*=e^{i\theta_n}I
\]

need not converge to `W_0`.

This toy model is only a logical counterexample to the implication

\[
Q_n\to W_0
\Longrightarrow
U_{S,n}Q_nU_{R,n}^*\to W_0
\]

without unitary control. It is **not** evidence that the actual P11 polar factors diverge.

---

## 4. Exact paper-level repair required

The current paper contains formulations asserting or suggesting that

\[
\chi_-\|\Theta_-\|\to0
\]

is a **sufficient route to terminal convergence**. That wording exceeds what the proved estimate establishes.

The safe replacement is:

> The O3 Jensen diagnostic shows that if
> \(\chi_-(T_0,U)\|\Theta_-(T_0,U)\|\to0\), then the auxiliary operator
> \(Q=A_S^{1/2}W_{R,S,-}^{[T_0]}A_R^{-1/2}\) converges to
> \(W_{R,S,-}^{[T_0]}\). Promoting this to convergence of the full future
> transport \(W_{R,S,-}^{[U]}\) requires separate control of the polar
> unitary gauges in \(W_{R,S,-}^{[U]}=U_SQU_R^*\), and remains open.

At minimum this correction is required in:

1. the executive-summary item describing the “conditional second-moment route”;
2. the main O3 remark calling the Jensen product a sufficient route to terminal convergence;
3. any abstract wording that can be read as closing the full transport from the Jensen product alone.

The open-problem section should continue to state the genuine unresolved target.

---

## 5. Firewalls

This R6 finding proves **none** of the following:

- that the actual polar factors `U_R,U_S` diverge;
- that `W_{R,S,-}^{[T]}` fails to be strongly Cauchy;
- that the cross-terminal kernel fails to converge to the identity;
- that the Jensen/second-moment estimates are false;
- that the finite-terminal isometry/cocycle algebra audited in R4 is false.

The correct status remains

\[
\boxed{
?[O]_{\text{polar-gauge control}},\qquad
?[O]_{K_{R,S}^{T,U}\to I},\qquad
?[O]_{W_{R,S,-}^{[T]}\ \mathrm{strong\ Cauchy}}.
}
\]

---

## Final referee disposition

\[
\boxed{
\begin{array}{ll}
\checkmark[M] & \text{O3 Jensen algebra / control of }Q,\\[1mm]
\times[M] & \text{“sufficient route to terminal convergence” as stated},\\[1mm]
?[O] & \text{polar-gauge control and full strong terminal transport}.
\end{array}
}
\]

**R6: PAPER REPAIR REQUIRED — theorem core (Jensen algebra) retained.**
