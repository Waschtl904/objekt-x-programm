# P11 End-to-End Referee R12 — logarithmic complement regularity

Date: 2026-08-14

Target: the firewall left open by `papers/P11_sections/P11_O3j_Reconciliation.tex` and `open:log` in `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex`.

## Referee question

For fixed
\[
0<R<S<T_0,
\]
let \(h\in C_c^\infty((-S,S))\) be the nonzero smooth odd annulus vector, supported away from \([-R,R]\), and put
\[
u_h=G_{R,T_0}^{-1}J_{R,S}^*G_{S,T_0}h,
\qquad
g_h=h-J_{R,S}u_h.
\]
If \(m_h\) is the first nonzero integral-jet order of \(g_h\), is
\[
E_Sg_h\in \mathscr H_{\log}^{m_h+3/2}?
\]

The answer is **yes**, and in fact a stronger positive Sobolev statement holds.

---

# Verdict

\[
\boxed{
\exists s_*>0:\qquad E_Ru_h\in H^{s_*}(\mathbb R),
\qquad E_Sg_h\in H^{s_*}(\mathbb R).
}
\]
Consequently
\[
\boxed{
E_Sg_h\in\bigcap_{\alpha<\infty}\mathscr H_{\log}^{\alpha}(\mathbb R),
}
\]
and therefore in particular
\[
\boxed{
E_Sg_h\in\mathscr H_{\log}^{m_h+3/2}(\mathbb R).
}
\]

Status:

- [R12-A] exact reduction from \(g_h\) to \(u_h\): **✓[M]**;
- [R12-B] positive Sobolev regularity of the Schur forcing: **✓[M]**;
- [R12-C] finite-window Gamma/Schur resolvent Sobolev bootstrap: **✓[M]**;
- [R12-D] logarithmic complement gate: **✓[M]**.

Hence
\[
\boxed{\text{R12 = ✓[M] PASS.}}
\]

This closes only the logarithmic complement gate. It does **not** prove strong terminal transport, \(K_{R,S}^{T,U}\to I\), polar-gauge convergence, or a global Object-X construction.

---

# 1. Exact reduction: the gate is a regularity question for \(u_h\)

On the underlying real line,
\[
E_Sg_h=E_Sh-E_Ru_h.
\]
Because \(h\in C_c^\infty((-S,S))\), its zero extension \(E_Sh\) is Schwartz. Therefore, for every finite \(\alpha\),
\[
\boxed{
E_Sg_h\in\mathscr H_{\log}^{\alpha}
\iff
E_Ru_h\in\mathscr H_{\log}^{\alpha}.
}
\tag{R12.1}
\]
Thus no cancellation with the smooth annulus vector is needed; it is enough to gain any positive Sobolev regularity for \(E_Ru_h\).

Indeed, if \(s>0\), then for every finite \(\alpha\)
\[
[\log(2+|\xi|)]^{2\alpha}
\le C_{s,\alpha}\langle\xi\rangle^{2s},
\]
so
\[
H^s(\mathbb R)\hookrightarrow\mathscr H_{\log}^{\alpha}(\mathbb R)
\qquad(\alpha<\infty).
\tag{R12.2}
\]

---

# 2. Cutoff lemma on the small Sobolev/logarithmic scale

For fixed finite \(a\ge0\) and \(|s|<1/2\), put
\[
\mathcal H^{s,a}
:=\left\{F:\int_{\mathbb R}
\langle\xi\rangle^{2s}[\log(2+|\xi|)]^{2a}
|\widehat F(\xi)|^2\,d\xi<\infty\right\}.
\]
The multiplier by the characteristic function of a bounded interval is bounded on every \(\mathcal H^{s,a}\) with \(|s|<1/2\).

For \(a=0\), this is the classical fractional-Sobolev cutoff range; see R. S. Strichartz, *Multipliers on Fractional Sobolev Spaces*, J. Math. Mech. 16 (1967), 1031–1060.

For the logarithmically refined spaces, one may argue directly on the Fourier side. The weight
\[
w_{s,a}(\xi)=\langle\xi\rangle^{2s}[\log(2+|\xi|)]^{2a}
\]
is an \(A_2\)-weight whenever \(|s|<1/2\): away from the origin it is a power weight with an arbitrary slowly varying logarithmic factor, and the \(A_2\) product of the average of \(w_{s,a}\) with that of \(w_{s,a}^{-1}\) is uniformly bounded precisely in the open power range \(-1<2s<1\). Multiplication by a half-line in physical space becomes, after Fourier transform, a linear combination of the identity and the Hilbert transform; the Hunt--Muckenhoupt--Wheeden weighted Hilbert-transform theorem therefore gives boundedness on \(L^2(w_{s,a})\). A bounded interval is a difference of two translated half-lines.

Reference: R. A. Hunt, B. Muckenhoupt, R. L. Wheeden, *Weighted norm inequalities for the conjugate function and Hilbert transform*, Trans. Amer. Math. Soc. 176 (1973), 227–251.

In particular, for \(|s|<1/2\), zero extension/restriction between fixed nested intervals is bounded on \(H^s\) and on the Gamma-refined scale used below.

---

# 3. Fixed-window prime/rest operators act on a small Sobolev scale

At fixed \(T_0\), the paper proves that the sum defining \(R_{T_0}\) is effectively finite. In each prime/martingale coordinate,
\[
\mathsf Q_{T_0}(u)\eta_{p,k}
=\sqrt{p-1}\sum_{j=0}^{\min(k-1,J_{p,T_0}(u)-1)}
 p^{(j-k)/2}\psi_{p,j}.
\]
For fixed \((p,j)\), the scalar coefficient
\[
1_{\{j<J_{p,T_0}(u)\}}
\]
is, up to endpoints, the characteristic function of the interval
\[
\left\{|u|<T_0-\frac{j+1}{2}\log p\right\}.
\]
Thus \(R_{T_0}\) is a finite sum of compositions of:

1. zero extension/restriction to fixed intervals;
2. translations \(U_t\), hence differences \(D_s=U_{s/2}-U_{-s/2}\);
3. multiplication by fixed interval indicators;
4. fixed finite-dimensional coefficient maps in the martingale fibers.

Consequently, for every \(|s|<1/2\),
\[
R_{T_0}:X_{T_0}^s\to Z_{T_0}^s
\]
is bounded on the support-restricted Sobolev scale
\[
X_{T_0}^s:=\{F\in H^s(\mathbb R):\operatorname{supp}F\subset[-T_0,T_0]\},
\]
with the analogous finite vector-valued target \(Z_{T_0}^s\).

Since the same statement holds for \(-s\), duality gives boundedness of the \(L^2\)-adjoint
\[
R_{T_0}^*:Z_{T_0}^s\to X_{T_0}^s.
\]
Therefore
\[
A_{T_0}^{\rm rest}:=I+R_{T_0}^*R_{T_0}
\tag{R12.3}
\]
is bounded on \(X_{T_0}^s\) for all \(|s|<1/2\).

At \(s=0\), \(A_{T_0}^{\rm rest}\ge I\), so it is an isomorphism of \(L^2(-T_0,T_0)\) onto itself.

The supported spaces are the ranges of the common interval-cutoff projection, which is bounded at the two endpoint Sobolev exponents. Hence they form the expected complex interpolation scale. By Šneǐberg local stability of invertibility, there exists
\[
\varepsilon_0=\varepsilon(T_0)>0
\]
such that
\[
\boxed{
B_{T_0}=(I+R_{T_0}^*R_{T_0})^{-1}
:X_{T_0}^s\to X_{T_0}^s
\quad\text{bounded for }|s|<\varepsilon_0.
}
\tag{R12.4}
\]

For the local stability theorem used here, see I. Asekritova, N. Kruglyak, M. Mastyło, *Stability of the inverses of interpolated operators with application to the Stokes system*, Rev. Mat. Complut. 36 (2023), 163–206, recalling Šneǐberg's theorem that the set of complex interpolation parameters at which a bounded interpolated operator is invertible is open.

---

# 4. The Schur forcing has positive Sobolev regularity

Write
\[
\phi:=E_{S,T_0}h\in C_c^\infty((-T_0,T_0)).
\]
The fixed-window hub
\[
H_{T_0}
=P_{T_0}\sum_{p^k\le e^{2T_0}}
\sqrt{\log p}\,p^{-3k/4}D_{k\log p}E_{T_0}
\]
is a finite sum of fixed translations together with interval extension/restriction. Therefore \(H_{T_0}\) is bounded on \(X_{T_0}^s\) for \(|s|<1/2\); using the corresponding negative exponents, the same is true for \(H_{T_0}^*\).

Choose
\[
0<s_1<\min\{\varepsilon_0,1/2\}.
\]
Since \(\phi\) is smooth and supported strictly inside the terminal interval,
\[
H_{T_0}^*\phi\in X_{T_0}^{s_1}.
\]
By (R12.4),
\[
B_{T_0}H_{T_0}^*\phi\in X_{T_0}^{s_1},
\]
and hence
\[
\Sigma_{T_0}\phi
=H_{T_0}B_{T_0}H_{T_0}^*\phi
\in X_{T_0}^{s_1}.
\]
Restriction to the smaller interval \(R\) and zero extension back to the line preserve \(H^{s_1}\), so
\[
\boxed{
E_Rr_{\sigma,h}\in H^{s_1}(\mathbb R).
}
\tag{R12.5}
\]

R11 already proved that
\[
r_{\Gamma,h}=P_R\mathcal G_\phi,
\qquad
\mathcal G_\phi\in H^N(\mathbb R)\quad\forall N<\infty.
\]
After restriction to \((-R,R)\), the zero extension is \(H^s\) for every \(s<1/2\) (endpoint jumps are allowed in precisely this range). Thus, after shrinking \(s_1\) if necessary,
\[
\boxed{
E_Rr_h=E_R(r_{\Gamma,h}+r_{\sigma,h})\in H^{s_1}(\mathbb R)
\quad\text{for some }s_1>0.
}
\tag{R12.6}
\]
This already defeats the proposed adversarial mechanism at the forcing level: the bounded Schur component does not destroy all positive Sobolev regularity.

---

# 5. Second Šneǐberg step: the finite-window Gamma/Schur resolvent

The remaining issue is not to identify the inverse with the full-line multiplier \(m_\Gamma^{-1}\). We instead work with the **form operator itself**.

Let
\[
m(\xi):=m_\Gamma(\xi)\asymp\log(2+|\xi|),
\]
and for \(|s|<1/2\) define the full-line Hilbert scale
\[
\mathcal V^s
:=\left\{F:\int_{\mathbb R}
\langle\xi\rangle^{2s}m(\xi)|\widehat F(\xi)|^2\,d\xi<\infty\right\}.
\tag{R12.7}
\]
Let
\[
V_R^s:=\{F\in\mathcal V^s:\operatorname{supp}F\subset[-R,R]\}.
\tag{R12.8}
\]
Because \(m\asymp\log(2+|\xi|)\), the cutoff lemma above applies to the weight
\[
\langle\xi\rangle^{2s}m(\xi),
\]
so the interval projection is bounded on \(\mathcal V^s\) for \(|s|<1/2\). Therefore the \(V_R^s\) are complemented subspaces of the full weighted Fourier scale and inherit its complex interpolation law. In particular, for fixed small \(\delta>0\),
\[
[V_R^{-\delta},V_R^{\delta}]_\theta
=V_R^{(2\theta-1)\delta}
\tag{R12.9}
\]
with equivalent Hilbert norms.

Put
\[
Y_R^s:=(V_R^{-s})^*.
\tag{R12.10}
\]
The dual Hilbert scale interpolates correspondingly.

Define the form operator
\[
\mathcal A_R:V_R^s\longrightarrow Y_R^s
\]
by
\[
\langle\mathcal A_Ru,v\rangle
:=\mathfrak c_{\Gamma,R}[u,v]
+\langle\Sigma_R^{[T_0]}u,v\rangle.
\tag{R12.11}
\]

## 5.1 Gamma part

For \(u\in V_R^s\), \(v\in V_R^{-s}\), Cauchy--Schwarz in Fourier space gives
\[
|\mathfrak c_{\Gamma,R}[u,v]|
\le \|u\|_{V_R^s}\|v\|_{V_R^{-s}}.
\tag{R12.12}
\]

## 5.2 Schur part

The first Šneǐberg step and the fixed finite translation/cutoff structure show, after reducing \(\delta>0\) if necessary, that
\[
\Sigma_R^{[T_0]}:H^s_R\to H^s_R
\]
is bounded for all \(|s|\le\delta\). Since \(m\ge1\),
\[
V_R^s\hookrightarrow H_R^s,
\qquad
V_R^{-s}\hookrightarrow H_R^{-s},
\]
and therefore by the \(H^s-H^{-s}\) dual pairing
\[
|\langle\Sigma_R^{[T_0]}u,v\rangle|
\le C_s\|u\|_{V_R^s}\|v\|_{V_R^{-s}}.
\tag{R12.13}
\]
Thus \(\mathcal A_R:V_R^s\to Y_R^s\) is bounded on a symmetric interval of exponents around zero.

## 5.3 Invertibility at the midpoint

At \(s=0\), \(V_R^0\) is exactly the Gamma form space under zero extension. The form
\[
a_R(u,v)
:=\mathfrak c_{\Gamma,R}[u,v]
+\langle\Sigma_R^{[T_0]}u,v\rangle
\]
is bounded and coercive, with
\[
a_R(u,u)\ge\mathfrak c_{\Gamma,R}[u]
=\|u\|_{V_R^0}^2.
\tag{R12.14}
\]
Hence Lax--Milgram gives an isomorphism
\[
\mathcal A_R:V_R^0\xrightarrow{\sim}Y_R^0.
\tag{R12.15}
\]

Applying Šneǐberg local stability a second time to the interpolation couples in (R12.9)--(R12.10), there exists
\[
\varepsilon_1=\varepsilon(R,S,T_0)>0
\]
such that
\[
\boxed{
\mathcal A_R:V_R^s\xrightarrow{\sim}Y_R^s
\qquad(|s|<\varepsilon_1).
}
\tag{R12.16}
\]

---

# 6. Apply the improved forcing to \(u_h\)

Take
\[
0<s_*<\min\{s_1,\varepsilon_1\}.
\]
By (R12.6), \(E_Rr_h\in H^{s_*}\). Hence \(r_h\) defines a bounded functional on \(V_R^{-s_*}\):
\[
|\langle r_h,v\rangle|
\le C\|E_Rr_h\|_{H^{s_*}}\|E_Rv\|_{H^{-s_*}}
\le C'\|v\|_{V_R^{-s_*}}.
\]
Therefore
\[
r_h\in Y_R^{s_*}.
\tag{R12.17}
\]
By (R12.16), there is a unique
\[
u_*:=\mathcal A_R^{-1}r_h\in V_R^{s_*}.
\]
Since \(s_*>0\), one has \(V_R^{s_*}\subset V_R^0\). Testing the \(s_*\)-equation against vectors in \(V_R^0\subset V_R^{-s_*}\) shows that \(u_*\) solves the original \(s=0\) variational equation from OJ.4. Uniqueness at \(s=0\) therefore gives
\[
u_*=u_h.
\]
Consequently
\[
\boxed{
E_Ru_h\in V_R^{s_*}\subset H^{s_*}(\mathbb R).
}
\tag{R12.18}
\]

Using (R12.1) and smoothness of \(E_Sh\),
\[
\boxed{
E_Sg_h\in H^{s_*}(\mathbb R).
}
\tag{R12.19}
\]
Together with (R12.2),
\[
\boxed{
E_Sg_h\in\mathscr H_{\log}^{\alpha}
\qquad\forall\alpha<\infty.
}
\tag{R12.20}
\]
In particular, since the paper has already proved that \(m_h<\infty\),
\[
\boxed{
E_Sg_h\in\mathscr H_{\log}^{m_h+3/2}.
}
\tag{R12.21}
\]

---

# 7. Adversarial checks

## 7.1 No illegal full-line Gamma inversion

Nowhere is
\[
(C_{\Gamma,R}+\Sigma_R^{[T_0]})^{-1}
\]
identified with the Fourier multiplier \(m_\Gamma^{-1}\). The second bootstrap is performed at the level of the finite-window coercive form operator and therefore respects the Dirichlet/Riesz boundary geometry emphasized in R11.

## 7.2 No false claim that bounded operators preserve regularity

The proof does not use
\[
\Sigma\in\mathcal B(L^2)\Rightarrow \Sigma:H^s\to H^s.
\]
Instead, \(H\), \(R\), and the martingale cutoffs are explicitly decomposed at fixed window into a finite family of translations and interval multipliers. Only then is \(H^s\)-boundedness obtained. The inverse \(B=(I+R^*R)^{-1}\) is promoted from \(L^2\) to a small Sobolev neighborhood by Šneǐberg stability.

## 7.3 Boundary jumps are harmless here

No \(H^{1/2}\) endpoint claim is made. All Sobolev exponents are chosen strictly in
\[
0<s_*<1/2.
\]
This is precisely the stable range for multiplication by interval indicators. Since the desired logarithmic spaces are much weaker than every positive \(H^{s_*}\), this small gain is sufficient.

## 7.4 No uniformity in terminal horizons

The exponents \(\varepsilon_0,\varepsilon_1,s_*\) may depend on the fixed triple \((R,S,T_0)\). No uniform lower bound as \(T_0\to\infty\) is asserted or needed for the fixed-complement logarithmic gate.

## 7.5 No promotion to actual terminal convergence

Closing `open:log` has only the consequence already stated in the paper: it feeds the O3 second-moment/complement diagnostic and can obstruct the auxiliary Jensen-product condition. By the R6 polar-gauge firewall, this is not a proof of failure (or success) of the actual strong terminal transport.

---

# 8. Referee conclusion

The R11 firewall was mathematically necessary, but it is not an obstruction. At fixed terminal horizon, the prime/rest Schur correction has enough hidden regularity because its apparently rough source cutoff is a **finite interval-step geometry**. The inverse \(B_{T_0}\) inherits a small positive Sobolev window from its \(L^2\)-invertibility by Šneǐberg stability. A second Šneǐberg argument on the Gamma form scale then transfers the positive Sobolev forcing through the genuine finite-window Dirichlet/Riesz resolvent.

Thus the proposed adversarial obstruction does not occur at this level:
\[
\boxed{
\text{bounded Schur coupling does not block the complement gate at fixed }T_0.
}
\]
Instead one gets the stronger regularity
\[
\boxed{
E_Sg_h\in H^{s_*}\subset\bigcap_{\alpha<\infty}\mathscr H_{\log}^{\alpha}
\quad\text{for some }s_*>0.
}
\]

This is a genuine positive advance beyond R11. The next paper repair should replace `open:log` by a proved theorem/corollary with an explicit firewall preserving the still-open strong-terminal and polar-gauge problems.
