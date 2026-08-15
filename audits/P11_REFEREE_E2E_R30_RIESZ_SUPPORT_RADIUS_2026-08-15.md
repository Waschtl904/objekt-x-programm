# P11 End-to-End Referee R30 — baseline Riesz support radius and fixed support classification

Date: 2026-08-15

## Target

Continue the R28/R29 constraint-normal branch at fixed
\[
0<R<S<T_0.
\]
The R29 small-source theorem proves \(s_{R,S,T_0}\neq0\) on a concrete region.  R30 asks whether the entire family of normal mismatches for fixed \(S,T_0\) can be encoded by one fixed baseline object, and whether the remaining problem can be stated without a terminal parameter.

No polar-gauge promotion is permitted.

## Verdict

Yes.  For each fixed source level \(X<T_0\), let \(r_X\) be the whitened Riesz normal from R28 and put
\[
\boxed{
\rho_{X,T_0}:=B_X^{-1/2}r_X,
\qquad B_X:=G_{X,T_0}^-.
}
\]
Then \(\rho_{X,T_0}\) is the unwhitened \(T_0\)-baseline Riesz representative of the first boundary functional:
\[
\boxed{
\beta_X^{(0)}(f)
=q_{T_0}^X(J_{X,T_0}f,J_{X,T_0}\rho_{X,T_0}).
}
\]
For every strict inclusion \(0<R<S<T_0\),
\[
\boxed{
s_{R,S,T_0}=0
\iff
\rho_{S,T_0}=J_{R,S}\rho_{R,T_0}
\iff
\operatorname{ess\,supp}\rho_{S,T_0}\subset[-R,R].
}
\]
Thus, for fixed \(S,T_0\), a single vector \(\rho_{S,T_0}\) simultaneously decides the normal mismatch for every old radius \(R<S\).

Define
\[
\boxed{
R_*(S,T_0)
:=\operatorname*{ess\,sup}
\{|u|:\rho_{S,T_0}(u)\neq0\}
\in(0,S].
}
\]
Then the classification is exact:
\[
\boxed{
s_{R,S,T_0}\neq0\iff0<R<R_*(S,T_0),
}
\]
\[
\boxed{
s_{R,S,T_0}=0\iff R_*(S,T_0)\le R<S.
}
\]
Hence R29-F is reduced to the single fixed question
\[
\boxed{R_*(S,T_0)=S\ ?}
\]
for each fixed \(S<T_0\).

The representative solves the fixed Dirichlet/Riesz equation
\[
\boxed{
(C_{\Gamma,S}+\Sigma_S^{[T_0]})\rho_{S,T_0}=\phi_S,
\qquad
\phi_S(u)=\operatorname{sgn}(u)I_0(|u|).
}
\]
Moreover the O3k interpolation machinery applies to this forcing and gives some \(s_*>0\) with
\[
E_S\rho_{S,T_0}\in H^{s_*}(\mathbb R),
\]
hence \(E_S\rho_{S,T_0}\in\mathcal H_\Gamma^\alpha\) for every finite \(\alpha\).

This regularity does **not** by itself prove \(R_*(S,T_0)=S\).  In particular, the current paper has not established a unique-continuation theorem for the finite-window Dirichlet/Riesz operator \(C_{\Gamma,S}+\Sigma_S^{[T_0]}\).  The Feshbach term is a fixed nonlocal translation/cutoff operator, so classical local elliptic UCP cannot simply be invoked.

## Canonical statuses

- [R30-A] unwhitened baseline Riesz representative and fixed Riesz identity: **✓[M]**.
- [R30-B] exact equivalence \(s=0\iff\rho_S=J_{R,S}\rho_R\): **✓[M]**.
- [R30-C] exact support criterion \(s=0\iff\operatorname{ess\,supp}\rho_S\subset[-R,R]\): **✓[M]**.
- [R30-D] critical support-radius classification for all \(R<S\) simultaneously: **✓[M]**.
- [R30-E] fixed Riesz equation and positive Sobolev/all-log regularity of \(\rho_{S,T_0}\): **✓[M]**.
- [R30-F] prove or disprove \(R_*(S,T_0)=S\) for every fixed \(S<T_0\): **?[O]**.
- [R30-UCP] direct applicability of a classical unique-continuation theorem to \(C_{\Gamma,S}+\Sigma_S^{[T_0]}\): **?[O]**, not an established input.

No conclusion about the R22 polar angle, strong terminal transport, or a global Object X follows.

---

## 1. Baseline Riesz representative

For \(X<T_0\), let
\[
B_X:=G_{X,T_0}^->0
\]
be the fixed terminal metric on the odd source graph space.  R28 transports the first boundary functional to whitened coordinates:
\[
\widehat\beta_X(x)=\beta_X^{(0)}(B_X^{-1/2}x)
=\langle x,r_X\rangle_{X,X}.
\]
Define
\[
\rho_{X,T_0}:=B_X^{-1/2}r_X.
\tag{R30.1}
\]
For \(f\in\mathcal K_{X,X}^-\),
\[
\begin{aligned}
\beta_X^{(0)}(f)
&=\langle B_X^{1/2}f,r_X\rangle_{X,X}\\
&=\langle B_X^{1/2}f,B_X^{1/2}\rho_{X,T_0}\rangle_{X,X}\\
&=\langle B_Xf,\rho_{X,T_0}\rangle_{X,X}\\
&=q_{T_0}^X(J_{X,T_0}f,J_{X,T_0}\rho_{X,T_0}).
\end{aligned}
\tag{R30.2}
\]
Thus \(\rho_{X,T_0}\) is exactly the \(T_0\)-baseline Riesz representative of \(\beta_X^{(0)}\).  This proves [R30-A].

---

## 2. Normal mismatch versus source compatibility

For \(0<R<S<T_0\), R28 gives
\[
s_{R,S,T_0}=0
\iff
r_S=Wr_R,
\]
where
\[
W=B_S^{1/2}J_{R,S}B_R^{-1/2}.
\]
Using \(r_X=B_X^{1/2}\rho_{X,T_0}\),
\[
\begin{aligned}
r_S=Wr_R
&\iff
B_S^{1/2}\rho_{S,T_0}
=B_S^{1/2}J_{R,S}B_R^{-1/2}B_R^{1/2}\rho_{R,T_0}\\
&\iff
\boxed{
\rho_{S,T_0}=J_{R,S}\rho_{R,T_0}.
}
\end{aligned}
\tag{R30.3}
\]
This proves [R30-B].

---

## 3. Exact support criterion

The canonical source map \(J_{R,S}\) is the graph-space realization of zero extension from \((-R,R)\) to \((-S,S)\).  Hence (R30.3) immediately implies
\[
s_{R,S,T_0}=0
\Longrightarrow
\operatorname{ess\,supp}\rho_{S,T_0}\subset[-R,R].
\tag{R30.4}
\]

Conversely suppose
\[
\operatorname{ess\,supp}\rho_{S,T_0}\subset[-R,R].
\]
Let \(\widetilde\rho_R\) be its restriction to \((-R,R)\), so
\[
\rho_{S,T_0}=J_{R,S}\widetilde\rho_R.
\]
For every \(f\in\mathcal K_{R,R}^-\), jet pullback and terminal-form compatibility give
\[
\begin{aligned}
\beta_R^{(0)}(f)
&=\beta_S^{(0)}(J_{R,S}f)\\
&=q_{T_0}^X(J_{S,T_0}J_{R,S}f,
             J_{S,T_0}\rho_{S,T_0})\\
&=q_{T_0}^X(J_{R,T_0}f,
             J_{R,T_0}\widetilde\rho_R).
\end{aligned}
\]
By uniqueness of the baseline Riesz representative,
\[
\widetilde\rho_R=\rho_{R,T_0}.
\]
Therefore \(\rho_{S,T_0}=J_{R,S}\rho_{R,T_0}\), and R30-B gives \(s=0\).  Thus
\[
\boxed{
s_{R,S,T_0}=0
\iff
\operatorname{ess\,supp}\rho_{S,T_0}\subset[-R,R].
}
\tag{R30.5}
\]
This proves [R30-C].

---

## 4. One critical radius classifies all old sources

Fix \(S<T_0\).  Since \(\beta_S^{(0)}\neq0\), the Riesz representative \(\rho_{S,T_0}\neq0\).  Define
\[
R_*(S,T_0)
:=\operatorname*{ess\,sup}
\{|u|:\rho_{S,T_0}(u)\neq0\}.
\tag{R30.6}
\]
A nonzero \(L^2\) function cannot be supported at the single point \(0\), so
\[
0<R_*(S,T_0)\le S.
\]
By (R30.5), for every \(0<R<S\),
\[
\boxed{
s_{R,S,T_0}=0
\iff R\ge R_*(S,T_0),
}
\tag{R30.7}
\]
and therefore
\[
\boxed{
s_{R,S,T_0}\neq0
\iff0<R<R_*(S,T_0).
}
\tag{R30.8}
\]
Thus the normal mismatch can change status at most once as the old source radius grows.  Equivalently, the dual normal norm
\[
R\longmapsto\|r_R\|
\]
is nondecreasing by R28 and reaches the final value \(\|r_S\|\) exactly at and above \(R_*\).  This proves [R30-D].

The universal strict-inclusion statement
\[
s_{R,S,T_0}\neq0\qquad(0<R<S)
\]
is now exactly equivalent to
\[
\boxed{R_*(S,T_0)=S.}
\tag{R30.9}
\]

---

## 5. Quantitative lower bounds for the support radius

R29 used the coarse kernel estimate
\[
\|r_R\|^2\le\frac23R^3.
\]
Together with R28 this gives
\[
R_*(S,T_0)
\ge
\min\left\{S,
\left(\frac32\|r_S\|^2\right)^{1/3}\right\}.
\tag{R30.10}
\]

The exact kernel norm from R29 gives a sharper fixed-window bound.  Put
\[
F(R):=\|\phi_R\|_2^2
=8\left[R-4(1-e^{-R/2})+(1-e^{-R})\right].
\tag{R30.11}
\]
Then
\[
F'(R)=8(1-e^{-R/2})^2>0
\qquad(R>0),
\]
so \(F\) is strictly increasing.  Since \(\|r_R\|^2\le F(R)\), every radius satisfying
\[
F(R)<\|r_S\|^2
\]
has \(s_{R,S,T_0}\neq0\).  Hence, writing \(F^{-1}\) on its range,
\[
\boxed{
R_*(S,T_0)
\ge F^{-1}(\|r_S\|^2)
}
\tag{R30.12}
\]
whenever the right side is defined below \(S\).  More concretely, any fixed test-vector lower bound \(c_h\le\|r_S\|\) gives the computable sufficient condition
\[
F(R)<c_h^2
\Longrightarrow s_{R,S,T_0}\neq0.
\tag{R30.13}
\]
This sharpens the cubic threshold while remaining entirely fixed-window.

---

## 6. Fixed Riesz equation

Let
\[
\phi_S(u):=\operatorname{sgn}(u)I_0(|u|).
\]
With the convention that the Hilbert product is linear in the first slot,
\[
\beta_S^{(0)}(f)=\langle f,\phi_S\rangle_{L^2(-S,S)}.
\]
The baseline form is
\[
q_{T_0}^X(J_{S,T_0}f,J_{S,T_0}g)
=\mathfrak c_{\Gamma,S}[f,g]
+\langle\Sigma_S^{[T_0]}f,g\rangle,
\]
where
\[
\Sigma_S^{[T_0]}:=E_{S,T_0}^*\Sigma_{T_0}E_{S,T_0}.
\]
Equation (R30.2) therefore says that \(\rho_{S,T_0}\) is the unique weak solution of
\[
\boxed{
(C_{\Gamma,S}+\Sigma_S^{[T_0]})\rho_{S,T_0}=\phi_S.
}
\tag{R30.14}
\]
Since the operator is coercive and \(\phi_S\in L^2\), the representation theorem also puts
\[
\rho_{S,T_0}\in\mathcal D(C_{\Gamma,S}).
\]
Thus the support radius is the support radius of one fixed Dirichlet/Riesz solution.

---

## 7. Positive Sobolev and all-log regularity of the baseline normal

The O3k proof applies to (R30.14) with a simpler forcing.  After zero extension,
\[
E_S\phi_S\in H^s(\mathbb R)
\qquad\text{for every }0<s<1/2,
\tag{R30.15}
\]
because \(\phi_S\) is piecewise smooth on the fixed interval and only the endpoint cutoff limits the Sobolev exponent.

Use the O3k form operator
\[
\mathcal A_S:V_S^s\to Y_S^s,
\]
now with the fixed pullback Schur term \(\Sigma_S^{[T_0]}\).  By the same \v Sne\u\i berg argument as in O3k, there exists \(\varepsilon>0\) such that
\[
\mathcal A_S:V_S^s\xrightarrow{\sim}Y_S^s
\qquad(|s|<\varepsilon).
\]
Choose
\[
0<s_*<\min\{\varepsilon,1/2\}.
\]
Then \(\phi_S\in Y_S^{s_*}\), and uniqueness of the weak solution gives
\[
\boxed{
E_S\rho_{S,T_0}\in V_S^{s_*}\subset H^{s_*}(\mathbb R).
}
\tag{R30.16}
\]
Consequently, for every finite \(\alpha\),
\[
\boxed{
E_S\rho_{S,T_0}\in\mathcal H_\Gamma^\alpha(\mathbb R).
}
\tag{R30.17}
\]
This proves the regularity part of [R30-E].

---

## 8. Unique-continuation firewall

It is tempting to argue from the full support of \(\phi_S\) to the full support of \(\rho_{S,T_0}\).  No such implication is currently proved.

The Gamma form comes from a logarithmically growing full-line Fourier multiplier restricted to a finite interval, but the associated finite-window operator is a genuine Dirichlet/Riesz operator rather than an already-established classical local pseudodifferential boundary problem.  Moreover
\[
\Sigma_S^{[T_0]}
=E_{S,T_0}^*H_{T_0}B_{T_0}H_{T_0}^*E_{S,T_0}
\]
is a fixed nonlocal Feshbach term built from translations, interval cutoffs and the rest inverse.  O3k proves boundedness on a small Sobolev scale; it does not prove locality, analyticity preservation, or a unique-continuation theorem for the sum.

Therefore the assertion
\[
R_*(S,T_0)=S
\]
remains open.  A valid R31 route would need either

1. a genuine UCP/support theorem tailored to the concrete operator in (R30.14), or
2. a direct P11 argument showing that no solution of (R30.14) can vanish on a nonempty boundary annulus.

Invoking generic ``elliptic/log-elliptic UCP'' without verifying the Feshbach perturbation hypotheses is forbidden.

---

## 9. Remaining gate

For fixed \(S<T_0\), determine
\[
\boxed{R_*(S,T_0)=S\ ?}
\]
Equivalently: does the baseline Riesz representative of the first boundary jet have essential mass arbitrarily close to \(\pm S\)?

A positive answer would upgrade R29 from a small-source region to
\[
s_{R,S,T_0}\neq0
\qquad\forall\,0<R<S<T_0,
\]
and therefore exclude full asymptotic inverse-root intertwining for every strict source enlargement.  By the R14 firewall this would still not decide the relative polar gauge or strong terminal transport.