# Analytic details checked in the critical author review

Target: `8074d14508873e09068222b9703b1f34e8607fc6`.
These arguments supplement the scoped review. They do not change the
historical source files or the external-review status.

## 1. Original normalization, pole block and connected form

The displayed additive explicit formula in Suzuki, *Weil's quadratic
form via the screw function*, arXiv:2606.09096v2, §1.1, was read directly:
https://arxiv.org/html/2606.09096v2 . Its normalization agrees with the
project's imported COMMON-JUMP formula. This source comparison concerns
the displayed formula only; it is not a reliance on global positivity.

Here is the subsequent algebra checked in this review. For
K_t=tau_(t/2)-tau_(-t/2), K_t^*K_t=2I-tau_t-tau_(-t).
The pole pairing of v*tilde(w) is
E_+(v) conjugate(E_-(w))+E_-(v) conjugate(E_+(w)); it vanishes with
exactly the two prescribed moments. The centered arithmetic term for
q=p^k is w_q(<K_log(q)v,K_log(q)w>-2<v,w>), with
w_q=log(p)/p^(k/2), and hence equals the negative sum of the two
translation correlations. The sign and the factor of two agree with
the S operator in the endpoint code.

For h(t)=exp(-t/2)/(1-exp(-2t)), put x=exp(-t/2). The additional
archimedean scalar is
\[
2\int_0^\infty h(t)(1-e^{-t/2})dt
=4\int_0^1\frac{dx}{(1+x)(1+x^2)}=\log2+\pi/2.
\]
Partial fractions give the last equality without quadrature. Thus
kappa=log(8*pi)+gamma+pi/2. On H1_0 zero-extended sources the small-t
energy is integrable because ||K_tu||<=t||u'||. The large-t part is
integrable because h decays and ||K_tu||<=2||u||. Smooth H1 approximation
therefore extends the quadratic identity to the stated sources; the
moments are continuous in L2 on a bounded interval.

With g(t)=h(t)-1/(2t), H_gamma(s)=integral_s^infinity h(t)dt,
\[
H_\gamma(s)=\operatorname{atanh}(e^{-s/2})+
\arctan(e^{-s/2}),
\quad
H_\gamma(s)+\int_0^s g(t)dt=\log2+\pi/4-\tfrac12\log s.
\]
Differentiation and the limit at zero establish the second identity.
Unitary scaling U_a u(x)=sqrt(2a)u(ax) then gives exactly
\[
q_a=D_H-\tfrac12\log(1-x^2)-\log(2\pi a)-\gamma-K_a-S_a,
\quad K_af=2a\int g(a|x-y|)f(y)\,dy/2.
\]
There is no missing a-dependent norm factor after this unitary change.

## 2. Harmonic diagonal and closed form domain

Let dmu=dx/2 and
\[
\mathcal E[f]=\int_{x<y}\frac{|f(x)-f(y)|^2}{y-x}\,d\mu(x)d\mu(y).
\]
It is a densely defined nonnegative closed form. One proof views its
square root as the difference map into the weighted pair-space L2.
If f_n converges in source L2 and its differences converge in that
pair-space, subsequences converge almost everywhere in both spaces;
the pair-space limit is the difference of the source limit. This is
the graph-closedness required for the form.

For a polynomial p, its associated operator on all form-domain test
vectors is
\[
(Ap)(x)=\int_{-1}^1\frac{p(x)-p(y)}{|x-y|}\,d\mu(y).
\]
The bilinear identity follows by symmetrization. Absolute integrability
is justified by boundedness of (p(x)-p(y))/(x-y) and source L2 on a
finite measure space. On a monomial,
\[
Ax^n=H_nx^n-\sum_{\substack{1\le r<n\\r\ {\rm odd}}}
\frac{x^{n-1-r}}{r+1}.
\]
Thus A preserves polynomial degree, has leading coefficient H_n, and
is symmetric. Orthogonality of P_n against lower-degree polynomials
implies AP_n=H_nP_n. These form an entire orthogonal L2 basis, so the
nonnegative self-adjoint operator associated to E is precisely the
harmonic diagonal and its form domain is sum H_n|f_n|^2<infinity.
This establishes the infinite-dimensional statement; the 129 exact
polynomial checks are supplementary implementation regressions.

Multiplication by V=-log(1-x^2)/2 defines a nonnegative closed form.
The sum E+<Vf,f> is closed on the intersection of their domains.
Every polynomial has finite V^2 integral. Consequently every
polynomial is in the associated operator domain, not merely in its
form domain. K_a and the finite sum S_a are bounded self-adjoint
perturbations. The full q_a is closed and lower bounded on that
intersection. H1_0 sources are contained in it.

Removing or adding finitely many polynomial components preserves the
form domain. For the low/tail split the finite-dimensional coupling
therefore maps into actual L2. The tail is a densely defined closed
restricted form and defines the self-adjoint operator used in the
Schur step. This is the appropriate setting for the endpoint proof.
It is distinct from the invalid H1_0 core/shell projection discussed
in the earlier consolidation audit.

## 3. Exact moments and a bounded error for an unbounded form

In one parity let E_j be the normalized carrier, j=0 or 1, and m the
cosh or sinh moment. On E_j-perp set Mx=x-<x,m>/<E_j,m> E_j.
Its inverse on the moment kernel is removal of the E_j coefficient.
Both directions preserve the form domain. No source is required to
obey an additional moment. The polynomial carrier is allowed in the
larger proof domain; the concluding estimate is restricted back to H1_0.

Put theta=a/2. For even parity,
|cosh(theta*x)-1|<=theta^2*x^2/[2(1-theta^2/12)] and the carrier
moment is at least one. For odd parity,
|sinh(theta*x)-theta*x|<=theta^3*|x|^3/[6(1-theta^2/20)].
Here ||x^3||=1/sqrt(7)<=1/sqrt(3) and
<E_1,sinh(theta*x)> >= theta/sqrt(3). These give both recorded beta
bounds, including the odd bound without a missing factor of three.
Orthogonality to E_j gives ||Mx||^2<= (1+beta)||x||^2.

For the omitted tail, subtract the entire Taylor polynomial below the
first tail degree n_*. Its uniform next-term geometric remainder
bounds the L2 tail norm and hence ||M-M0|| by epsilon_m. The odd
factor 4/a exceeds the required 2*sqrt(3)/a.

The difference Delta=M-M0 is rank one with range E_j. Since
Qp E_j belongs to L2, ||Qp E_j||<9, ||M0||<sqrt(2) and epsilon_m<1,
\[
|q^p[Mx]-q^p[M^0x]|
\le(18\sqrt2+9)\epsilon_m\|x\|^2
<35\epsilon_m\|x\|^2.
\]
This justifies the more conservative 80*epsilon_m used in the final
endpoint. Uniform Gamma error contributes at most 2L*epsilon after
M. Thus e=2L*epsilon+80*epsilon_m really is a bounded form error;
it does not assume that Q itself is bounded.

## 4. Gamma model and the entire coupling tail

The identity
\[
g(t)=\tfrac14[\operatorname{sech}(t/2)+((t/2)/\sinh(t/2)-1)/(t/2)]
\]
explains the rational inverse-series polynomial. The residual after
multiplication by the denominator Taylor polynomial is bounded
coefficientwise on 0<=t/2<=5/6. The denominator tails begin at degree
130; 130! and 131! with geometric ratio (5/6)^2 are conservative.
The denominators are >=1. The code therefore bounds a uniform kernel
error, not a discrete set of points. The endpoint L=log5<5/3 is inside
that interval.

For Gamma images, k=0 is the constant projection, the k=1 image has
second derivative P_j, and subsequent images satisfy
f_jk''=k(k-1)f_j,k-2. The two beta boundary values determine the
integration constants uniquely. Degree <=j+k+1 proves the exact
finite support of the polynomial model images. The review separately
integrates both unit-square triangles and compares 84 COMPLETE image
polynomials, including j=62,63 and k=64.

For each low vector p define O=V-Kp-S. Its complete coupling mass is
||P_Y O p||^2, not a finite sum of high-mode samples. Expand
\[
O^*O=V^2+(Kp)^2+S^2-VKp-KpV-VS-SV+KpS+SKp.
\]
Subtract all low-mode projections by Parseval. Only the Kp terms may
be cut at degree N+M+1, because their higher coefficients vanish
identically. V and S retain their entire infinite tails through their
full squared norms. The code's gramC is precisely this expansion.
Applying the exact finite moment congruence to BOTH indices then
produces G=(C0)^*C0. Complex sources are covered by the Hermitian form;
real symmetric coefficient computations apply to real and imaginary
parts and preserve the same bound.

At B, chain lengths give ||T_2||<=sqrt(2), ||T_3||,||T_4||<=1.
The constant kernel 1/4 annihilates Y. Monotonicity of g on [0,L],
V>=0 and the model/moment errors give the stated entire-tail floor.
The floors >0.7194 and >0.7348 are actual lower comparison bounds on
all high modes. They do not by themselves control the low even sector.

## 5. Interval LDL, actual shear and final source norm

For a fixed true endpoint, all exact matrix entries lie inside the
computed intervals. Interval LDL recursively encloses its true LDL
factorization; strictly positive lower pivot endpoints prove positive
definiteness. Entrywise intervals are not being mistaken for a
Loewner lower matrix. Symmetrizing one computed triangle retains the
same exact symmetric matrix.

With J_nn=1/(2n+1), the normalized low matrix is
J^-1/2 R J^-1/2, so
\[
\lambda_{\min}(J^{-1/2}RJ^{-1/2})
\ge[\operatorname{tr}(J R^{-1})]^{-1}.
\]
The triangular solves in inverse_trace_bound compute that weighted
trace. For the coupling, the different normalization is
tr(J^-1 Gact). Both weights in the code have the correct direction.
Young's inequality gives Gact=(1+tau)G+(1+1/tau)e^2J >= C^*C.
Since D>=delta I>0, the matrix R=A0-eJ-Gact/delta is a lower bound
on the actual infinite-dimensional Schur complement.

For s>=||D^-1 C||, completing the square uses
z=y+D^-1 C l. Its inverse satisfies ||(l,y)||<=(1+s)||(l,z)||.
Hence the actual lower bound is min(sigma,delta)/(1+s)^2.
The final comparison ||Mx||^2<=(1+beta)||x||^2 divides this ENTIRE
bound by 1+beta. This validates the final norm conversion and avoids
both the old missing-division error and double counting of moment loss.

## 6. Interval transfer and near-null interpretation

Physical zero extension of H1_0 functions preserves zero traces, both
moments, L2 norm and the same real-line form. It therefore transfers
the endpoint lower bound to every smaller window, including all shift
entrances. The reverse inclusion of admissible trial sets gives the
nonincreasing variational infimum. No minimizer, operator-norm
continuity of shifts, or proposed shell decomposition is needed.

The explicit source is a rational combination of (1-x^2)P_n corrected
along (1-x^2) by the EXACT cosh moment. It lies in H1_0, has zero cosh
moment by definition and zero sinh moment by parity. Its inverse
iteration only chooses rational coefficients; the final directed
Rayleigh evaluation supplies the bound. Thus its upper enclosure is
an admissible upper bound on the infimum, never a uniform lower reserve.
The already admissible direct energy must not pay Schur or moment
certificate losses a second time.
