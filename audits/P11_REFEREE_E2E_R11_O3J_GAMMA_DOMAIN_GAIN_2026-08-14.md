# P11 End-to-End Referee Audit R11 — O3j Gamma action and operator-domain gain

**Date:** 2026-08-14  
**Paper:** `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`  
**Module:** `papers/P11_sections/P11_O3j_Reconciliation.tex`  
**Audit mode:** end-to-end referee; historical audits are destructive counterchecks only and are not used as missing proof steps.

## 0. Scope and retargeting

The initially suggested R11 candidate `thm:schatten` is not a new node: it is exactly the theorem already audited end-to-end as R2, including the localized Fourier family, the isolated primitive `p=2` translate, and the implication from Schatten membership of the Schur operator to Schatten membership of the preconditioned hub. R11 is therefore not double-counted.

The next genuinely unaudited high-risk paper step is the O3j reconciliation:

\[
\text{graph normal equation}
\longrightarrow
\text{Gamma/Schur }L^2\text{ forcing}
\longrightarrow
u_h\in D(C_{\Gamma,R})
\longrightarrow
\text{finite logarithmic regularity of the Gamma forcing}.
\]

The danger is a false upgrade from form domain to operator domain or an illicit replacement of the finite-window Dirichlet/Riesz inverse by the global Fourier multiplier.

## 1. Graph normal equation

Fix `0<R<S<T_0` and the smooth odd annulus vector

\[
h\in C_c^\infty((-S,S)),\qquad \operatorname{supp}h\cap[-R,R]=\varnothing.
\]

The paper defines

\[
u_h:=G_{R,T_0}^{-1}J_{R,S}^*G_{S,T_0}h,
\qquad
g_h:=h-J_{R,S}u_h.
\tag{R11.1}
\]

All adjoints here are graph-Hilbert adjoints. Since

\[
G_{R,T_0}=J_{R,T_0}^*J_{R,T_0}
\]

and `G_{R,T_0}` is boundedly invertible, for every `v\in\mathcal K_{X,R}` one has

\[
\begin{aligned}
\langle J_{R,T_0}u_h,J_{R,T_0}v\rangle_{X,T_0}
&=\langle G_{R,T_0}u_h,v\rangle_{X,R}\\
&=\langle G_{S,T_0}h,J_{R,S}v\rangle_{X,S}\\
&=\langle J_{S,T_0}h,J_{S,T_0}J_{R,S}v\rangle_{X,T_0}\\
&=\langle J_{S,T_0}h,J_{R,T_0}v\rangle_{X,T_0},
\end{aligned}
\]

where the last step is the transition cocycle. Because the graph inner product is `q^X`, this is exactly OJ.2:

\[
q_{T_0}^X(E_{R,T_0}u_h,E_{R,T_0}v)
=
q_{T_0}^X(E_{S,T_0}h,E_{R,T_0}v).
\]

No naive `L^2` adjoint is substituted for `J^*`.

**Status:**

\[
\boxed{[R11\text{-}A]\;\checkmark[M].}
\]

## 2. Expansion as a weak Gamma/Schur equation

At fixed terminal horizon,

\[
q_{T_0}^X(f,v)
=\mathfrak c_{\Gamma,T_0}[f,v]
+\langle\Sigma_{T_0}f,v\rangle,
\qquad
\Sigma_{T_0}=H_{T_0}(I+R_{T_0}^*R_{T_0})^{-1}H_{T_0}^*.
\]

The left Gamma form is exactly compatible with ordinary zero extension:

\[
\mathfrak c_{\Gamma,T_0}[E_{R,T_0}u,E_{R,T_0}v]
=\mathfrak c_{\Gamma,R}[u,v].
\]

The left bounded part compresses to

\[
\Sigma_R^{[T_0]}:=E_{R,T_0}^*\Sigma_{T_0}E_{R,T_0}.
\]

Thus OJ.2 becomes, in form sense,

\[
\mathfrak c_{\Gamma,R}[u_h,v]
+\langle\Sigma_R^{[T_0]}u_h,v\rangle
=\langle r_{\Gamma,h}+r_{\sigma,h},v\rangle,
\tag{R11.2}
\]

provided the two right-hand terms are genuine `L^2` vectors. The finite Schur term is immediate because `\Sigma_{T_0}` is bounded:

\[
r_{\sigma,h}=E_{R,T_0}^*\Sigma_{T_0}E_{S,T_0}h\in L^2(-R,R).
\]

The Gamma term is the only nontrivial domain issue and is checked next.

**Status:**

\[
\boxed{[R11\text{-}B]\;\checkmark[M].}
\]

## 3. Gamma action on the smooth interior core

For `\phi\in C_c^\infty((-T,T))` define

\[
\mathcal G_\phi
:=\mathcal F^{-1}\!\left(m_\Gamma\widehat{E_T\phi}\right).
\]

Because `E_T\phi` is smooth and compactly supported, its Fourier transform is Schwartz. The paper has

\[
m_\Gamma(\xi)\asymp\log(2+|\xi|),
\]

so for every finite `N`,

\[
(1+|\xi|^2)^{N/2}m_\Gamma(\xi)\widehat{E_T\phi}(\xi)\in L^2(\mathbb R).
\]

Hence

\[
\mathcal G_\phi\in H^N(\mathbb R)
\qquad\text{for every finite }N.
\]

For every `v` in the Gamma form domain, Plancherel gives

\[
\mathfrak c_{\Gamma,T}[\phi,v]
=\langle P_T\mathcal G_\phi,v\rangle_{L^2(-T,T)}.
\]

This is precisely the criterion from the representation theorem for

\[
\phi\in D(C_{\Gamma,T}),
\qquad
C_{\Gamma,T}\phi=P_T\mathcal G_\phi.
\tag{R11.3}
\]

Now `\phi=E_{S,T_0}h` is in `C_c^\infty((-T_0,T_0))` because the support of `h` is compactly contained in `(-S,S)`. Therefore

\[
r_{\Gamma,h}
=E_{R,T_0}^*C_{\Gamma,T_0}E_{S,T_0}h
=P_R\mathcal G_\phi
\in L^2(-R,R).
\]

This is a concrete multiplier calculation for this smooth interior vector; it is not the false general principle “smooth implies operator domain for every form-defined operator.”

**Status:**

\[
\boxed{[R11\text{-}C]\;\checkmark[M].}
\]

## 4. Genuine operator-domain gain

Equation (R11.2) now has a forcing

\[
r_h=r_{\Gamma,h}+r_{\sigma,h}\in L^2(-R,R).
\]

The paper already proves

\[
C_{\Gamma,R}\ge I,
\qquad
\Sigma_R^{[T_0]}\ge0,
\]

and `\Sigma_R^{[T_0]}` is bounded selfadjoint. Hence

\[
A_R:=C_{\Gamma,R}+\Sigma_R^{[T_0]}
\]

is positive selfadjoint on

\[
D(A_R)=D(C_{\Gamma,R}),
\qquad A_R\ge I,
\]

so `A_R^{-1}` is bounded on all of `L^2(-R,R)`.

Applying the first representation theorem to the weak identity (R11.2) gives

\[
u_h\in D(A_R)=D(C_{\Gamma,R}),
\qquad
A_Ru_h=r_h,
\]

therefore

\[
\boxed{
u_h=(C_{\Gamma,R}+\Sigma_R^{[T_0]})^{-1}r_h
\in D(C_{\Gamma,R}).}
\tag{R11.4}
\]

There is no circular use of operator-domain membership: `u_h` starts only as a graph/form vector, the right side is first shown to be `L^2`, and the domain gain is then deduced.

**Status:**

\[
\boxed{[R11\text{-}D]\;\checkmark[M].}
\]

## 5. Finite logarithmic regularity of the Gamma forcing

The global function `\mathcal G_\phi` belongs to every finite Sobolev space, so its restriction

\[
r_{\Gamma,h}=P_R\mathcal G_\phi
\]

is smooth on the closed finite interval. Its zero extension may have jumps at `\pm R`, so one must not claim arbitrary positive Sobolev regularity after zero extension.

For a smooth interval function `r`, one integration by parts gives, for `|\xi|\ge1`,

\[
\widehat{E_Rr}(\xi)
=
\frac{r(-R)e^{iR\xi}-r(R)e^{-iR\xi}}{i\xi}
+\frac{1}{i\xi}\int_{-R}^{R}r'(x)e^{-ix\xi}\,dx.
\]

Consequently

\[
|\widehat{E_Rr}(\xi)|\le \frac{C_r}{|\xi|}.
\]

Therefore, for every finite `\alpha`,

\[
\int_{|\xi|\ge1}
[\log(2+|\xi|)]^{2\alpha}
|\widehat{E_Rr_{\Gamma,h}}(\xi)|^2\,d\xi
<\infty,
\]

because `\int_1^\infty (\log x)^{2\alpha}x^{-2}\,dx<\infty`. Thus OJ.10 is correct:

\[
\boxed{E_Rr_{\Gamma,h}\in\bigcap_{\alpha<\infty}\mathscr H_{\log}^{\alpha}.}
\tag{R11.5}
\]

**Status:**

\[
\boxed{[R11\text{-}E]\;\checkmark[M].}
\]

## 6. Firewall and what R11 does not prove

The paper correctly does **not** promote (R11.5) to the Schur forcing, the solution, or the rough complement. In particular R11 proves neither

\[
E_Ru_h\in\mathscr H_{\log}^{m_h+3/2}
\]

nor

\[
E_Sg_h\in\mathscr H_{\log}^{m_h+3/2}.
\]

The finite-window inverse

\[
(C_{\Gamma,R}+\Sigma_R^{[T_0]})^{-1}
\]

is also not replaced by the global Fourier multiplier `m_\Gamma^{-1}`.

The exact complement gate therefore remains

\[
\boxed{?[O]_{E_Sg_h\in\mathscr H_{\log}^{m_h+3/2}}.}
\]

The terminal gates are untouched:

\[
?[O]_{\rm uniform\ finite\text{-}jet\ Gram/square\text{-}root\ control},
\qquad
?[O]_{K_{R,S}^{T,U}\to I},
\qquad
?[O]_{W_{R,S,-}^{[T]}\ \mathrm{strong\ Cauchy}},
\]

as is the polar-gauge problem.

## 7. Referee verdict

No counterexample, domain mismatch, adjoint-typing error, or illicit form-to-operator upgrade was found in the current paper module. The critical chain is paper-internal:

\[
\text{graph projection}
\to
\text{weak Gamma/Schur equation}
\to
L^2\text{ forcing}
\to
D(C_{\Gamma,R})\text{ gain}
\to
\text{finite log regularity of }r_{\Gamma,h}.
\]

Hence

\[
\boxed{
[R11\text{-}A]=[R11\text{-}B]=[R11\text{-}C]=[R11\text{-}D]=[R11\text{-}E]
=\checkmark[M].
}
\]

**R11: `✓[M] PASS`.**

No SYN, Seal, Object-X closure, or RH conclusion follows from R11.