# P11 End-to-End Referee R15 — gauge intertwining and square-root information gate

Date: 2026-08-14

Target: the actual-family polar-gauge frontier left by R14, especially the proposed coherence condition between
\[
X_R=(G_{R,U}^-)^{1/2}(G_{R,T_0}^-)^{-1/2},
\qquad
X_S=(G_{S,U}^-)^{1/2}(G_{S,T_0}^-)^{-1/2},
\]
and the fixed normalized inclusion
\[
W=W_{R,S,-}^{[T_0]}.
\]

## Referee questions

1. Is `Gamma_U -> I` exactly an intertwining condition between the unique polar factors `U_R,U_S`?
2. Is the raw condition `X_S W approximately W X_R` the right new gate, or does it merely repackage the original transport problem?
3. Can the present fixed-pair mixed-jet asymptotics already determine the inverse square roots and hence the gauges?

# Verdict

The gauge condition admits an exact intertwining formulation, but the correctly normalized `X_S`--`X_R` condition is exactly the original norm transport defect.  More importantly, the current fixed-pair mixed-jet asymptotics are mathematically insufficient to determine the inverse-square-root geometry: their leading finite-jet Gram matrix is rank one, so unquantified subleading remainders determine the smallest eigenvalues.

Canonical statuses:

- [R15-A] `Gamma_U` versus transported gauge isometry: **✓[M]**;
- [R15-B] exact normalized `X_S`--`X_R` coherence identity: **✓[M]**;
- [R15-C] individual polar gauge equals noncommutativity of the base/future metric pair: **✓[M]**;
- [R15-D] claim that the present fixed-pair `1+o(1)` mixed-jet data suffice for inverse-square-root/gauge control: **✓[M]_neg**;
- [R15-E] actual P11 convergence `Gamma_U -> I`, `K_{R,S}^{T_0,U} -> I`, or strong terminal Cauchy: **?[O]**.

Thus R15 does not decide the actual gauge.  It identifies exactly why the present asymptotic package cannot decide it and reduces the next genuine step to the finite-jet Gram/square-root gate already isolated in R8.

---

## 1. Exact gauge intertwining

Define
\[
V_U:=U_SWU_R^*,
\qquad
\Gamma_U=W^*V_U.
\]
Both `V_U` and `W` are isometries. Therefore
\[
(V_U-W)^*(V_U-W)=2I-\Gamma_U-\Gamma_U^*.
\]
For every fixed source vector `f`,
\[
\|(V_U-W)f\|^2
=2\|f\|^2-2\operatorname{Re}\langle\Gamma_Uf,f\rangle.
\]
Hence
\[
\Gamma_U\xrightarrow[s]{}I
\iff
V_U\xrightarrow[s]{}W.
\]
In operator norm,
\[
\|\Gamma_U-I\|\le\|V_U-W\|
\le\sqrt{2\|\Gamma_U-I\|}.
\]
Moreover
\[
V_U-W=(U_SW-WU_R)U_R^*,
\]
so in operator norm
\[
\Gamma_U\to I
\iff
\|U_SW-WU_R\|\to0.
\]

Scope warning: because `U_R` itself depends on `U`, one should not silently replace the strong convergence statement by a strong statement for `U_S W-W U_R` acting on fixed vectors.  The norm equivalence is exact; the strong criterion is best stated with `V_U=U_S W U_R^*`.

---

## 2. The raw `X` intertwining is not a new independent gate

Using
\[
X_R=U_RA_R^{1/2},
\qquad
X_S=U_SA_S^{1/2},
\qquad
A_S^{1/2}W=QA_R^{1/2},
\]
one gets exactly
\[
X_SW-WX_R
=\bigl[U_S(Q-W)+(U_SW-WU_R)\bigr]A_R^{1/2}.
\]
Thus with the canonical right normalization
\[
\mathcal E_U:=(X_SW-WX_R)A_R^{-1/2},
\]
\[
\mathcal E_U=U_SQ-WU_R.
\]
Since the true future transport is
\[
W_U=U_SQU_R^*,
\]
we have
\[
\boxed{\mathcal E_UU_R^*=W_U-W.}
\]
Consequently
\[
\boxed{\|\mathcal E_U\|=\|W_U-W\|.}
\]

Therefore the normalized `X` coherence problem is literally the original norm terminal-transport problem.  The unnormalized condition `X_S W-W X_R -> 0` is stronger and is distorted by the growing factor `A_R^{1/2}`.

This corrects the tempting interpretation that studying the products `X_R,X_S` automatically produces a simpler intermediary problem.

---

## 3. Individual gauge and noncommutativity

For either level `X=R,S`, put
\[
B=G_{X,T_0}^-,\qquad C=G_{X,U}^-.
\]
The corresponding product is
\[
C^{1/2}B^{-1/2}
=U_X(B^{-1/2}CB^{-1/2})^{1/2}.
\]
Then
\[
\boxed{U_X=I\iff [B,C]=0.}
\]
Indeed, commutation makes the product positive. Conversely `U_X=I` makes
`C^{1/2}B^{-1/2}` selfadjoint, hence
\[
C^{1/2}B^{-1/2}=B^{-1/2}C^{1/2},
\]
which is equivalent to commutation of `B` and `C`.

Thus the polar factor measures genuine noncommutativity of the base and future metric pair.  Nevertheless `Gamma_U -> I` does not require `U_R -> I` and `U_S -> I` separately; nontrivial rotations may coherently intertwine through `W`.

---

## 4. Adversarial finite-jet information test

The current mixed-jet theorem gives fixed-pair leading asymptotics.  On a two-dimensional jet-adapted block with first jet orders `0` and `m>0`, after removing the common exponential scalar and fixed nonzero coefficient normalizations, the leading Gram scale is
\[
\begin{pmatrix}
1&\varepsilon\\
\varepsilon&\varepsilon^2
\end{pmatrix},
\qquad \varepsilon=U^{-m},
\]
with entrywise relative `o(1)` errors.  The leading matrix has rank one.

Consider therefore, for any fixed `a>2`,
\[
v_\varepsilon=(1,\varepsilon)^T,
\]
\[
M_\varepsilon^{(a)}
=v_\varepsilon v_\varepsilon^*
+\varepsilon^a e_2e_2^*
=
\begin{pmatrix}
1&\varepsilon\\
\varepsilon&\varepsilon^2+\varepsilon^a
\end{pmatrix}.
\]
Every `a>2` gives the same leading entry asymptotics
\[
1,\qquad \varepsilon,\qquad \varepsilon^2(1+o(1)).
\]
But
\[
\det M_\varepsilon^{(a)}=\varepsilon^a,
\qquad
\operatorname{tr}M_\varepsilon^{(a)}=1+o(1),
\]
so
\[
\lambda_{\min}(M_\varepsilon^{(a)})\sim\varepsilon^a,
\]
and therefore
\[
\|(M_\varepsilon^{(a)})^{-1/2}\|
\sim\varepsilon^{-a/2}.
\]
Taking, for example, `a=4` and `a=8` gives identical leading fixed-pair Gram data but inverse-square-root norms of orders `epsilon^{-2}` and `epsilon^{-4}`.

Hence the present entrywise `1+o(1)` mixed-jet asymptotics do not determine even the polynomial order of the inverse square root in the near-null direction.

This is exactly the failure mode warned about in the R8 fixed-pair firewall: a leading rank-one Gram law is insufficient for inverse-square-root control.

---

## 5. Consequence for the actual P11 frontier

R15 does **not** show that the actual P11 gauges fail to converge.  It shows:

1. `Gamma_U -> I` is precisely a transported polar-unitary coherence condition;
2. normalized `X_S W-W X_R` coherence is just the original transport defect;
3. the polar factors arise from noncommutation of `(G_{X,U},G_{X,T_0})`;
4. current fixed-pair mixed-jet asymptotics do not contain enough subleading information to calculate the inverse square roots on near-null jet directions.

Therefore the next positive target is not another Jensen estimate and not merely a new prime-counting exponent.  One needs a **quantitative finite-jet Gram expansion with controlled remainder**, deep enough that after rank-one cancellation the smallest eigenvalues, positive square roots and inverse square roots are determined, and the resulting expansions must be compatible between the `R` and `S` levels.

That is precisely Open Problem `open:finite-jet-sqrt`.

No conclusion about `Gamma_U -> I`, `K_{R,S}^{T_0,U} -> I`, strong terminal transport, Object X, Seal, or RH follows from R15.
