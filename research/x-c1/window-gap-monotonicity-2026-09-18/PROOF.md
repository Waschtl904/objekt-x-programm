# X-C1 WINDOW-GAP MONOTONICITY — exact zero-extension branch and shell-Schur reformulation

**Date:** 2026-09-18  
**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`  
**Parent:** PR #137 head `9d9c48de2d6e4d56556f38f45489d133c17bd181` (including the separate GPT-2 near-null transported-family package).  
**Scope:** connected two-Mellin NULLPOL family. No new endpoint positivity claim.

## 1. Exact variational monotonicity

For `0<a<=b`, let `J_{a,b}` be the already proved physical zero-extension isometry, written in fixed reference coordinates as

\[
(J_{a,b}f)(\xi)=\sqrt{b/a}\,f((b/a)\xi)1_{|\xi|<a/b}.
\]

The parent packages prove

\[
\|J_{a,b}f\|_2=\|f\|_2,
\qquad
M_{b,\pm}(J_{a,b}f)=\sqrt{a/b}\,M_{a,\pm}(f),
\]

and the exact connected-form identity

\[
q_b[J_{a,b}f]=q_a[f]. \tag{1}
\]

Reflection commutes with zero extension. Hence `J_{a,b}` maps the even and odd NULLPOL source spaces isometrically into their counterparts at `b`.

Define

\[
\lambda_{\rm e}(a)=
\inf_{0\ne u\in\mathcal W_a^{\rm even}}
\frac{Q_W[u]}{\|u\|_2^2},
\qquad
\lambda_{\rm o}(a)=
\inf_{0\ne u\in\mathcal W_a^{\rm odd}}
\frac{Q_W[u]}{\|u\|_2^2},
\]

and similarly `lambda(a)` on the whole two-Mellin class. From (1), every admissible Rayleigh quotient at `a` occurs unchanged at `b`. Therefore

\[
\boxed{
\lambda_{\rm e}(b)\le\lambda_{\rm e}(a),\qquad
\lambda_{\rm o}(b)\le\lambda_{\rm o}(a),\qquad
\lambda(b)\le\lambda(a).
} \tag{2}
\]

This is exact. No Lipschitz estimate, eigenvalue perturbation theorem, finite cutoff, or positivity assumption beyond the definition of the infimum is used.

## 2. Consequence for the log(5)/2 near-null source

Let

\[
B=\frac{\log5}{2}.
\]

The parent endpoint package constructs an explicit even physical source `v_B` in `H^1_0` satisfying both Mellin conditions and rigorously encloses its direct Rayleigh quotient by

\[
3.2962904568\times10^{-12}
<
\frac{Q_W[v_B]}{\|v_B\|_2^2}
<
3.2962911964\times10^{-12}. \tag{3}
\]

For every `b>=B`, define only the physical zero-extension branch

\[
v_b^{\rm ext}=J_{B,b}v_B.
\]

Then exactly

\[
\boxed{
\frac{Q_W[v_b^{\rm ext}]}{\|v_b^{\rm ext}\|_2^2}
=
\frac{Q_W[v_B]}{\|v_B\|_2^2}.
} \tag{4}
\]

Consequently

\[
\boxed{
\lambda_{\rm e}(b)<3.3\times10^{-12}
\qquad(b\ge B).
} \tag{5}
\]

In particular, any future uniform positive constant proved on all windows up to any endpoint `b>=B`, including `b=1`, cannot exceed this explicit source-level upper bound.

## 3. New prime-power channels vanish exactly on the extension branch

The physical support of `v_B` is contained in `[-B,B]`, whose diameter is

\[
2B=\log5.
\]

For every prime power `q>=5`, one has `log q>=log5`. Therefore the support of `v_B` and its translate by `log q` are disjoint up to a null endpoint contact. Hence

\[
\langle v_B,T_{\log q}v_B\rangle=0
\qquad(q\ge5). \tag{6}
\]

The same is true after placing the source in any larger ambient window by zero extension. Thus the newly active channel `5`, and every later channel, contributes **exactly zero prime correlation** to the extension branch. Formula (4) is the full statement: changes in the ambient Gamma/leakage bookkeeping cancel exactly so that the total form stays fixed.

This must be distinguished from a different full-window continuation obtained by rescaling the shape to fill the larger window and reprojecting the Mellin moment. For such a branch the channel-5 term can start cubically. That is a legitimate diagnostic branch, but it is not the variational competitor supplied by exact window functoriality.

## 4. Firewall against the wrong Kato expectation

Because (2) makes the true optimal even gap nonincreasing, the global variational quantity cannot have a strict local minimum at `B` followed by an increase.

If `lambda_e` admits a right derivative, then

\[
\lambda_{\rm e}'(B+)\le0. \tag{7}
\]

If it is twice right-differentiable and `lambda_e'(B+)=0`, then monotonicity implies

\[
\lambda_{\rm e}''(B+)\le0. \tag{8}
\]

Therefore a calculation producing `lambda'(B)≈0` and `lambda''(B)>0` can only describe a selected non-minimizing branch, a finite comparison eigenvalue, or a coordinate-dependent full-window continuation; it cannot describe the global lowest-even Rayleigh infimum.

## 5. Correct next local problem: new-direction shell Schur

For `b>B`, put

\[
E_{B,b}=J_{B,b}\mathcal W_B^{\rm even}
\subset\mathcal W_b^{\rm even}.
\]

This is a closed isometric copy of the old admissible space and the restriction of `Q_W` to it is exactly the old form. Let

\[
\mathcal W_b^{\rm even}=E_{B,b}\oplus Z_b
\]

be the `L^2` orthogonal decomposition inside the already constrained even NULLPOL space. Relative to it, write the actual form as

\[
F_b=
\begin{pmatrix}
A_B&C_b^*\\
C_b&D_b
\end{pmatrix}. \tag{9}
\]

Here `A_B` is not an approximation: by (1) it is exactly the old endpoint form transported to the larger window.

If `D_b` is strictly positive, eliminating the genuinely new directions gives

\[
A_{\rm eff}(b)=A_B-C_b^*D_b^{-1}C_b\preceq A_B. \tag{10}
\]

Thus shell coupling can leave the inherited resonance unchanged or push a low branch **down**, but can never make the variational minimum rise above the inherited old-space value. This is the operator version of (2).

The correct threshold-resonance gate is therefore:

1. obtain a positive lower bound on the new-direction block `D_b` on a right interval;
2. bound the actual coupling `C_b` to the inherited near-null sector;
3. prove that `A_B-C_b^*D_b^{-1}C_b` stays positive;
4. determine whether its lowest branch is flat to leading order or decreases.

If one chooses explicit unconstrained core/shell coordinates instead of the already constrained decomposition, the previously available constrained Schur/C15 algebra is a natural bookkeeping device for the two global moments. Its use would be a coordinate mechanism, not evidence that C15 is forced by a negative direction.

## 6. Research consequences

The full-window test branch that rises to the right of `B` remains useful for diagnosing one geometric family of shapes. It does **not** show that the optimal coercivity improves. The exact zero-extension branch supplies a permanent ceiling (5) for every later window.

Accordingly:

- no `log(7)/2` endpoint push should be interpreted as evidence that the near-null resonance disappeared;
- a future `a=1` positive theorem, if achieved, must coexist with the inherited source (4), so its optimal uniform constant is at most the upper endpoint in (3);
- the next qualitative question is whether new shell directions lower the gap below the inherited resonance, not whether channel 5 raises the old minimum.

This theorem adds no new RH, Object-X, or full-C1 claim. It sharpens the variational meaning of the already proved window functoriality.
