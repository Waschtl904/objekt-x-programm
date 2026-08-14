# P11 End-to-End Referee R13 — polynomial second-moment witness

Date: 2026-08-14

Target chain:
\[
E_Sg_h\in\mathscr H_{\log}^{m_h+3/2}
\stackrel{?}{\Longrightarrow}
\nu_2(U)\gtrsim U^{-M}
\stackrel{?}{\Longrightarrow}
\chi_{T_0,U}^{R,-}\|\Theta_{T_0,U}^-\|\not\to0.
\]

The second arrow must be read with the correct sign: a polynomial lower witness for
\(\nu_2\) contradicts the auxiliary condition \(\chi\|\Theta\|\to0\); it does not imply
that condition.  In the actual P11 family the product in fact diverges.

## Verdict

Fix \(0<R<S<T_0\).  Let \(g_h\) be the explicit nonzero odd complement and let \(m_h\)
be its first nonzero integral-jet order.  Then
\[
\boxed{\nu_2(U)\ge cU^{-2m_h-2}}
\]
for all sufficiently large \(U\), and therefore
\[
\boxed{\|\Theta_{T_0,U}^-\|\ge c' U^{-2m_h-2}}.
\]
Since R7 gives superpolynomial growth of
\(\chi_{T_0,U}^{R,-}\),
\[
\boxed{\chi_{T_0,U}^{R,-}\|\Theta_{T_0,U}^-\|\to\infty.}
\]

Statuses:

- [R13-A] rough/smooth mixed future Schur asymptotic: **✓[M]**;
- [R13-B] exact complement pairing for \(\mathscr B\): **✓[M]**;
- [R13-C] crude relative-metric norm upper bound: **✓[M]**;
- [R13-D] polynomial \(\nu_2\) witness: **✓[M]**;
- [R13-E] obstruction of the auxiliary Jensen-product condition: **✓[M]**;
- [R13-F] implication to strong terminal nonconvergence: **not claimed / ?[O]** because the R6 polar-gauge firewall remains.

Hence
\[
\boxed{\text{R13 = ✓[M] PASS for the auxiliary O3/Jensen diagnostic.}}
\]

---

## 1. Rough complement now lies in the sharp-asymptotic class

R12 proves more than the logarithmic threshold:
\[
E_Sg_h\in H^{s_*}(\mathbb R)
\]
for some \(s_*>0\).  Hence
\[
E_Sg_h\in\mathscr H_{\log}^{m_h+3/2}.
\]
By the R9 logarithmic threshold corollary, the rough prime-cell modulus gate holds for
\(g_h\), and its diagonal future Schur form therefore has the sharp asymptotic
\[
\sigma_U(J_{S,U}g_h)
=c_{m_h}^2|\beta_S^{(m_h)}(g_h)|^2
\frac{e^U}{U^{2m_h+2}}(1+o(1)).
\tag{R13.1}
\]

Choose a fixed smooth odd \(f_0\in C_c^\infty((-R,R))\) with
\(\beta_R^{(0)}(f_0)\ne0\), and set \(F_0=J_{R,S}f_0\).  Exact jet pullback gives
\(\beta_S^{(0)}(F_0)=\beta_R^{(0)}(f_0)\ne0\).

---

## 2. Mixed asymptotic extends to the rough complement

The TC1 proof does not require smoothness in its algebraic part.  For fixed compactly
supported odd vectors define
\[
D_U(f,g)=\sigma_U(Jf,Jg)-\frac{\ell_U(f)\overline{\ell_U(g)}}{d_U}.
\]
The exact Gram identity gives
\[
|D_U(f,g)|^2\le D_U(f,f)D_U(g,g).
\tag{R13.2}
\]

For \(F_0\), Theorem 6.1 gives the diagonal sharp asymptotic.  For \(g_h\), (R13.1)
does.  The R9 rough boundary expansion gives the corresponding rank-one term for both
vectors, while \(d_U=2U+O(1)\).  Therefore
\[
D_U(F_0,F_0)=o(e^U/U^2),
\]
\[
D_U(g_h,g_h)=o(e^U/U^{2m_h+2}),
\]
and (R13.2) yields
\[
D_U(F_0,g_h)=o(e^U/U^{m_h+2}).
\]
Thus
\[
\boxed{
\sigma_U(J_{S,U}F_0,J_{S,U}g_h)
=c_{m_h}\beta_R^{(0)}(f_0)
\overline{\beta_S^{(m_h)}(g_h)}
\frac{e^U}{U^{m_h+2}}(1+o(1)).
}
\tag{R13.3}
\]
The leading coefficient is nonzero by construction.

---

## 3. Exact complement pairing for the second-moment defect

Work in the fixed graph Hilbert spaces, not with naive \(L^2\)-adjoints.  Put
\[
A_R=A_{T_0,U}^{R,-},\qquad
A_S=A_{T_0,U}^{S,-},\qquad
W=W_{R,S,-}^{[T_0]},
\]
\[
\mathscr B=(I-WW^*)A_SW.
\]
Set
\[
x=G_{R,T_0}^{1/2}f_0,
\qquad
y=G_{S,T_0}^{1/2}g_h.
\]
Because
\[
g_h\in\ker(J_{R,S}^*G_{S,T_0}),
\]
one has \(y\perp\operatorname{Ran}W\).  Hence
\[
\langle\mathscr Bx,y\rangle
=\langle A_SWx,y\rangle.
\]
Substituting the definitions of \(A_S\) and \(W\) gives
\[
\langle A_SWx,y\rangle
=\langle G_{S,U}F_0,g_h\rangle.
\]
The base-terminal pairing vanishes by the complement condition, so
\[
\boxed{
\langle\mathscr Bx,y\rangle
=\langle(G_{S,U}-G_{S,T_0})F_0,g_h\rangle.
}
\tag{R13.4}
\]

Exact Gamma compatibility under zero extension cancels the Gamma contribution in the
difference.  Therefore
\[
\langle(G_{S,U}-G_{S,T_0})F_0,g_h\rangle
=\sigma_U(J_{S,U}F_0,J_{S,U}g_h)
-\sigma_{T_0}(J_{S,T_0}F_0,J_{S,T_0}g_h).
\]
The second term is fixed, while (R13.3) grows exponentially.  Consequently
\[
\boxed{\|\mathscr B\|\ge c_1e^U/U^{m_h+2}.}
\tag{R13.5}
\]
Since \(\Delta_2=\mathscr B^*\mathscr B\),
\[
\boxed{
\|\Delta_2\|\ge c_2e^{2U}/U^{2m_h+4}.
}
\tag{R13.6}
\]

---

## 4. Relative metric norms grow at most on the hub scale

For \(X=R,S\), the Rayleigh quotient of the relative metric satisfies
\[
\frac{q_U^X(E_{X,U}z)}{q_{T_0}^X(E_{X,T_0}z)}
\le1+\|H_U\|^2.
\]
Indeed, the numerator is at most
\((1+\|H_U\|^2)\mathfrak c_{\Gamma,X}[z]\), while the denominator is at least
\(\mathfrak c_{\Gamma,X}[z]\).  Hence
\[
\|A_{T_0,U}^{X,-}\|\le1+\|H_U\|^2.
\tag{R13.7}
\]

From the explicit hub formula and \(\|D_s\|\le2\),
\[
\|H_U\|
\le2\sum_{p^k\le e^{2U}}\sqrt{\log p}\,p^{-3k/4}
\le C\sum_{p\le e^{2U}}\sqrt{\log p}\,p^{-3/4}.
\]
The same Chebyshev/partial-summation estimate used in R9 gives
\[
\boxed{\|H_U\|\ll e^{U/2}/\sqrt U.}
\tag{R13.8}
\]
Thus
\[
\boxed{
\|A_R\|\|A_S\|\ll e^{2U}/U^2.
}
\tag{R13.9}
\]

---

## 5. Polynomial witness and product obstruction

Combining (R13.6) and (R13.9),
\[
\boxed{
\nu_2(U)
=\frac{\|\Delta_2\|}{\|A_R\|\|A_S\|}
\ge cU^{-2m_h-2}.
}
\tag{R13.10}
\]
The second-moment/Jensen inequality gives
\[
\|\Theta_{T_0,U}^-\|\ge\nu_2(U)/8,
\]
so
\[
\boxed{
\|\Theta_{T_0,U}^-\|\ge c'U^{-2m_h-2}.
}
\tag{R13.11}
\]

R7 proves
\[
U^{-N}\chi_{T_0,U}^{R,-}\to\infty
\qquad\forall N>0.
\]
Take \(N=2m_h+2\).  Then (R13.11) implies
\[
\boxed{
\chi_{T_0,U}^{R,-}\|\Theta_{T_0,U}^-\|\to\infty.
}
\tag{R13.12}
\]
Thus the auxiliary Jensen-product condition is impossible for this explicit P11
complement diagnostic.

---

## Firewall

R13 does **not** prove failure of strong terminal transport.  The R6 polar-gauge identity
\[
W_{R,S,-}^{[U]}=U_SQU_R^*
\]
remains the governing firewall.  Obstruction of \(\chi\|\Theta\|\to0\) obstructs the
auxiliary sufficient modulus route only.  No control of the unitary polar gauges
\(U_R,U_S\) is obtained, and no conclusion
\(K_{R,S}^{T,U}\not\to I\) is drawn.
