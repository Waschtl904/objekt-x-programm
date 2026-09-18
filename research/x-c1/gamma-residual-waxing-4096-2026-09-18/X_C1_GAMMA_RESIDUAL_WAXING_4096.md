# X-C1 GAMMA-RESIDUAL WAXING — dyadic 4096-cell certificate

**Date:** 2026-09-18  
**Status:** `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`  
**Parent / live base:** PR #137 head `c87dbcb37c250bd6f420d1688f275ae2a4e7f5ab`, including `gamma-node-waxing-2026-09-18` and `full-residual-schur-19651_50000-2026-09-17`.  
**Scope:** connected NULLPOL class
\[
\mathcal W_a=H^1_0((-a,a);\mathbb C)\cap\ker E_+\cap\ker E_-
\]
in the Prime-2-only regime. No A1 import, no third Mellin condition, no finite-dimensional operator replacement, no numerical quadrature proof.

## 0. Result

The nonconstant positive Gamma residual can be promoted to a sharper analytic waxing certificate. This is a continuation beyond the current-head three-parameter Gamma-Node envelope, whose separately certified local crossing is near `0.3931225`; no earlier package is rewritten or invalidated.

At the rational lower endpoint
\[
a_- = \frac{3934355}{10^7}=0.3934355
\]
the exact checker proves, with the explicit split
\[
s=\frac{63597}{125000},\qquad
\theta=\frac{1459223}{2000000},
\]
that
\[
\boxed{
Q_W[u] > \frac1{1500000}\,\|u\|_2^2
}
\qquad(0\ne u\in\mathcal W_{a_-}).
\]
The odd gap remains greater than \(1/4\).

At
\[
a_+ = \frac{3934360}{10^7}=0.3934360
\]
the checker proves a global negative upper bound for **every admissible split pair** \((s,\theta)\) in the concrete certificate defined below, even when the exact Gamma \(e_2\)-energy is replaced by its 4096-cell *upper* Riemann enclosure.

Consequently the optimized degree-bound / split-Schur certificate has a rigorously bracketed local sign change
\[
\boxed{0.3934355<a_{\Gamma,4096}^{\rm cert}<0.3934360.}
\]
This is **not** a negative Weil vector, not a no-go for the full Gamma residual, not a no-go for the Prime-2 residual, and not evidence that C15 is forced. It is only the local boundary of the explicitly named certificate class below.

## 1. Current-head Node-floor branch on the new bracket

The live parent contains the global-floor correction
\[
C(a)=\max\{C_0(a),C_2(a)\},
\]
with
\[
C_0(a)=\kappa-2H(a),\qquad
C_2(a)=\kappa+w-H(2a-\ell)-H(\ell).
\]
Our formulas use the \(C_2\) branch. This is legitimate on the whole present bracket: the interval generator and exact checker certify
\[
C_2-C_0
=2H(a)-H(2a-\ell)-H(\ell)+w
>0.052043622165
\]
for every
\[
0.3934355\le a\le0.3934360.
\]
Thus the live-head global-floor correction causes no branch change here. The definitions of \(C,m,p,\lambda_2,\delta\) used below agree with the active current-head branch.

## 2. Exact Gamma \(e_2\)-energy as a one-dimensional waxing function


Put
\[
L=2a,\qquad r_a(t)=g(t)-g(L),\qquad
 g(t)=h(t)-\frac1{2t}.
\]
For the normalized Legendre mode \(e_2\), the already established exact identity is
\[
\int_{-a}^{a-t}|e_2(x+t)-e_2(x)|^2\,dx
=\frac{60t^2(L-t)^3}{L^5}.
\]
Hence, with \(x=t/L\),
\[
R_{\Gamma,a}[e_2]
=L\int_0^1 \phi(x)\,r_a(Lx)\,dx,
\qquad
\phi(x)=60x^2(1-x)^3.
\tag{G1}
\]
An antiderivative of \(\phi\) is
\[
W(x)=20x^3-45x^4+36x^5-10x^6,
\qquad W(0)=0,\quad W(1)=1.
\tag{G2}
\]

Because \(g'(t)<0\) on \((0,2]\), \(r_a\) is decreasing on the whole relevant interval. For
\[
x_j=\frac jN,\qquad \Delta W_j=W(x_j)-W(x_{j-1}),
\]
define
\[
q_N^-(a)
=L\sum_{j=1}^N \Delta W_j\,r_a(Lx_j),
\tag{G3-}
\]
\[
q_N^+(a)
=L\sum_{j=1}^N \Delta W_j\,r_a(Lx_{j-1}),
\qquad r_a(0)=\frac14-g(L).
\tag{G3+}
\]
Then exactly
\[
\boxed{
q_N^-(a)\le R_{\Gamma,a}[e_2]\le q_N^+(a).
}
\tag{G4}
\]
For nested dyadic refinement, \(q_N^-\) increases and \(q_N^+\) decreases. At \(N=2\), (G3-) reduces to the former coarse bound
\[
\frac{21L}{32}\bigl(g(L/2)-g(L)\bigr).
\]
Thus (G3) is an analytic residual-waxing hierarchy, not numerical quadrature used as a proof.

The present gate fixes
\[
N=4096=2^{12}.
\]
All Riemann weights are exact rationals; transcendental values are enclosed before the exact gate decisions.

## 3. Improved infinite-dimensional Gamma norm bound

Let
\[
d_a(x)=\int_{-a}^{a}r_a(|x-y|)\,dy.
\]
The graph-Laplacian estimate gives
\[
R_{\Gamma,a}[u]
\le 2\sup_{|x|\le a}d_a(x)\,\|u\|_2^2.
\tag{G5}
\]
Writing \(F(s)=\int_0^s r_a(t)\,dt\),
\[
d_a(x)=F(a+x)+F(a-x).
\]
Since \(r_a\) is decreasing, \(d_a\) is maximized at \(x=0\). Therefore
\[
\|R_{\Gamma,a}\|
\le M_\Gamma(a)
:=4\int_0^a r_a(t)\,dt.
\tag{G6}
\]

A useful exact primitive is
\[
J(t)=\int_0^t g(u)\,du
=\frac12\left[
\log\!\left(\frac{4\tanh(t/4)}{t}\right)
+\arctan(\sinh(t/2))
\right],
\qquad J(0)=0.
\tag{G7}
\]
Consequently
\[
\boxed{
M_\Gamma(a)=4\bigl(J(a)-a\,g(2a)\bigr).
}
\tag{G8}
\]
This strictly improves the earlier bound \(2L(1/4-g(L))\) near the current gate while remaining an infinite-dimensional operator-norm majorant.

## 4. The analytic split-Schur certificate

Keep the established Node data
\[
C(a),\ m(a),\ p(a),\lambda_2(a),\delta(a),\beta_e(a).
\]
Use a fraction \(0<s<1\) of the Gamma residual to rescue \(e_2\). From
\[
\|A+B\|^2\ge s\|A\|^2-\frac{s}{1-s}\|B\|^2
\]
and (G6), the even-tail floor is
\[
D(a;s)=\delta(a)-\frac{s}{1-s}M_\Gamma(a).
\tag{G9}
\]
Only pairs with \(D(a;s)>0\) are admissible.

For the Node split \(0<\theta<1\), put
\[
\mu(a;\theta)=\theta m(a),
\qquad
K(a;\theta)=C(a)+\frac{\theta}{1-\theta}m(a).
\tag{G10}
\]
Given a Gamma low-mode energy input \(q\), the operator-Schur pivot is bounded by
\[
\Sigma(a;s,\theta;q)
=\lambda_2(a)+s q
+\mu p\left(1-\frac{\mu}{D(a;s)}\right).
\tag{G11}
\]
The square-completion transport gives
\[
\eta(a;s,\theta;q)
=
\frac{\min\{\Sigma(a;s,\theta;q),D(a;s)\}}
     {(1+\mu/D(a;s))^2}.
\tag{G12}
\]
After the **separate** NULLPOL moment loss and norm division,
\[
\boxed{
G_{\Gamma}^{\rm cert}(a;s,\theta;q)
=
\frac{\eta(a;s,\theta;q)-\beta_e(a)K(a;\theta)}
     {1+\beta_e(a)}.
}
\tag{G13}
\]
No new Mellin condition appears: the Gamma difference form annihilates \(e_0\) exactly.

For a positive certificate one may insert \(q=q_{4096}^-\). For an upper test of the same certificate class one may insert \(q=q_{4096}^+\), since (G13) is nondecreasing in \(q\).

## 5. Positive lower endpoint

At \(a_-\), the exact Fraction checker uses the directed enclosures of
\[
C,m,p,\lambda_2,\delta,\beta_e,\beta_o,q_{4096}^-,M_\Gamma
\]
and the rational split stated in Section 0.

It proves in particular
\[
D>0,
\qquad
0<\Sigma<D,
\]
\[
G_{\Gamma}^{\rm cert}(a_-;s,\theta;q_{4096}^-)
>7.6580\times10^{-7}
>\frac1{1500000},
\]
and
\[
G_{\rm odd}(a_-) > 0.2765 > \frac14.
\]
Because \(q_{4096}^-\le R_{\Gamma,a_-}[e_2]\) and \(M_\Gamma\) is an operator-norm upper bound, this is a genuine lower bound for the full connected Weil form at this endpoint, not merely a value of an exploratory optimizer.

## 6. Global upper test at the upper endpoint

The upper endpoint uses \(q=q_{4096}^+\), i.e. an *optimistic* replacement of the exact \(e_2\)-Gamma energy. The checker then proves negativity for all admissible \((s,\theta)\) in this certificate class.

### 6.1 Excluding outer \(s\)-ranges

For \(D>0\), the quadratic Node term satisfies
\[
\mu p\left(1-\frac\mu D\right)\le \frac{pD}{4}.
\]
Hence
\[
\Sigma\le F(s)
:=\lambda_2+s q+\frac{pD(s)}4,
\]
with
\[
F'(s)=q-\frac{pM_\Gamma}{4(1-s)^2}.
\]
Exact rational interval decisions give
\[
F'(0.15)>0,\qquad F(0.15)<0,
\]
\[
F'(0.70)<0,\qquad F(0.70)<0.
\]
Thus \(\Sigma<0\) for all admissible \(s\le0.15\) and \(s\ge0.70\).

### 6.2 Low \(\theta\) on the central \(s\)-strip

For \(0.15\le s\le0.70\), the checker proves
\[
D(s)>1.1\,m.
\]
Therefore for \(\theta\le0.55\), \(\mu\le D/2\) and \(\Sigma\) is increasing in \(\theta\). Exact parameter-interval cells prove
\[
\sup_{0.15\le s\le0.70}\Sigma(s,0.55)<0.
\]
Hence this whole low-\(\theta\) strip is negative.

### 6.3 Central rectangle: strict joint concavity

On
\[
\mathcal R=[0.15,0.70]\times[0.55,0.95]
\]
the checker first proves \(\Sigma<D\), so the active branch in (G12) is smooth. It differentiates (G13) symbolically and evaluates its Hessian with exact rational interval arithmetic on a \(40\times40\) partition of the **two scalar split parameters only**.

The resulting global bounds include
\[
G_{ss}< -0.00454,
\]
\[
\det D^2G > 3.74\times10^{-4}.
\]
Thus the Hessian is negative definite everywhere on \(\mathcal R\), and \(G\) is strictly jointly concave there.

At the rational tangent point
\[
(s_0,\theta_0)
=\left(\frac{5088559}{10^7},\frac{7295959}{10^7}\right)
\]
the exact interval tangent-plane upper bound over all of \(\mathcal R\) is
\[
G(s,\theta)<-3.78\times10^{-7}< -\frac1{4000000}.
\]
Therefore no point in the central rectangle can certify positivity.

This finite subdivision is only an interval proof over two real optimization parameters. It does **not** replace the infinite-dimensional tail operator by a finite matrix.

### 6.4 High \(\theta\)

For fixed \(s\), write
\[
q_0=\frac{m}{D},\qquad A=mp,\qquad L_0=\lambda_2+s q.
\]
On the active \(\Sigma<D\) branch,
\[
\eta''(\theta)
=
\frac{6q_0\bigl(Aq_0\theta-A+L_0q_0\bigr)}
     {(1+q_0\theta)^4}.
\]
The numerator is increasing in \(\theta\). The checker proves its value at \(\theta=1\) is already negative throughout the central \(s\)-strip. Hence \(\eta''<0\) there for \(\theta\ge0.95\). The moment penalty makes \(G_{\theta\theta}\) even smaller.

It also proves
\[
G_\theta(s,0.95)<0
\]
throughout the strip. Thus \(G\) is strictly decreasing for \(\theta\ge0.95\).

Together with Sections 6.1--6.3 this exhausts every admissible split pair.

## 7. Why the upper endpoint is only a certificate-class boundary

The negative upper endpoint is deliberately scoped narrowly.

It proves that the particular analytic lower-bound architecture (G9)--(G13), using

- the degree majorant \(M_\Gamma(a)\) from (G8),
- the split inequality with parameter \(s\),
- the conservative Node Schur bound \(D^{-1}\preceq D(a;s)^{-1}I\), and
- no Prime-2 difference residual,

cannot produce a positive even certificate at \(a_+\), even when its low-mode Gamma input is replaced by the Riemann **upper** enclosure \(q_{4096}^+\).

It does **not** prove that the actual Gamma residual operator cannot do better. In particular, the true operator norm may be smaller than the degree bound and the full Schur geometry retains information discarded by (G11). The positive Prime-2 difference residual also remains completely unused.

Accordingly:

- positive endpoint \(a_-\): genuine connected Weil positivity certificate;
- negative endpoint \(a_+\): only a local boundary of this named certificate class;
- full Gamma-residual mechanism: not exhausted;
- Gamma + Prime-2 full residual: still open;
- C15: not forced;
- full C1-GEOM, unit window, Object X and RH: open.

## 8. Certificate implementation and provenance

`generate_gamma_residual_waxing_4096_intervals.py` evaluates the displayed analytic formulas with 70-decimal `mpmath.iv` interval arithmetic and emits outward enclosures. It is an input-enclosure generator, not the gate decision engine.

`check_x_c1_gamma_residual_waxing_4096.py` hardcodes those outer decimal intervals as exact `fractions.Fraction` endpoints. Every one of its final 20 PASS decisions is therefore exact rational arithmetic. The checker writes the committed result JSON; its stdout is captured verbatim in the committed log.

`SHA256SUMS` is generated only after the final bytes of the proof, checker, generator, log, result JSON and README are fixed.
