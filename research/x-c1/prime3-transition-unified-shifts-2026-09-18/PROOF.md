# Prime-3 transition, joint shift Gram, and continuation to log(2)

2026-09-18. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.**

## 1. The macroscopic endpoint and the statement

Let B=log(2) and
\[
\mathcal W_a=H^1_0((-a,a);\mathbb C)\cap\ker E_+\cap\ker E_-,
\qquad E_\pm u=\int_{-a}^a u(x)e^{\pm x/2}\,dx.
\]
This certificate proves the author-derived interval theorem
\[
\boxed{Q_W[u]>10^{-11}\|u\|_2^2
\quad(0<a\le B,\ 0\ne u\in\mathcal W_a).}                 \tag{1}
\]
At B the shifts log(2) and log(3) are active. The shift log(4)=2B
has zero-measure overlap; its later weight would be log(2)/2, not
log(4)/2. No prime power beyond 3 contributes at this endpoint.

The endpoint is fixed by the next geometric transition. No local
crossing, scalar-split optimization, or intermediate positive-point
package is used. The new structural ingredient is the exact **joint
infinite-tail Gram**, including mixed Prime-2/Prime-3 terms and the
cross terms between the logarithmic potential, regular Gamma kernel,
and the full weighted shift operator. This avoids replacing those
cross terms by separate norm losses.

The preceding package at `eea8ff64e63bfca3c536427dd27fb0fc355edaa4`
remains AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN. This calculation is an
independent endpoint recomputation, not an external audit or a status
promotion of that package. It uses the same imported connected
nonpole-form identity and the two actual Mellin conditions. It does
not assume the preceding package's numerical gap in order to prove (1).

## 2. One reference family, including the new Node geometry

Use H=L2((-1,1),dmu), dmu=dξ/2, and U_a u(ξ)=sqrt(2a)u(aξ).
Let E_n=sqrt(2n+1)P_n, H_n=sum_(k=1)^n 1/k, H_0=0, and
\[
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
g(t)=h(t)-\frac1{2t},\quad H_\Gamma(s)=\int_s^\infty h(t)dt,
\quad\kappa=\log(8\pi)+\gamma+\pi/2.
\]
For p=2,3 put ell_p=log(p), w_p=ell_p/sqrt(p), d_p=ell_p/a,
and define zero-extended shifts
\[
(T_{p,a}f)(\xi)=f(\xi+d_p)1_{\xi+d_p<1}
               +f(\xi-d_p)1_{\xi-d_p>-1}.
\]
On the interval [log(3)/2,log(2)], one has 1<=d_2<d_3<=2.
At equality d_3=2 its operator is zero; at d_2=1 the bands meet only
at a null point. Otherwise each channel pairs disjoint endpoint bands.
In particular ||T_p||<=1 and T_p^2=P_active,p; at B, T_2^2=I.

The exact nonpole form is
\[
\begin{aligned}
q_a[f]={}&2a\int_{\xi<\eta}h(a(\eta-\xi))|f(\eta)-f(\xi)|^2d\mu d\mu\\
&+\int[H_\Gamma(a(1+\xi))+H_\Gamma(a(1-\xi))-\kappa]|f|^2d\mu
-\sum_{p=2,3}w_p\langle f,T_{p,a}f\rangle .               \tag{2}
\end{aligned}
\]
On the actual two-Mellin kernel it equals Q_W under U_a. Off that
kernel, q_a is the displayed nonpole form; no pole cancellation is
asserted there.

In the original positive-residual decomposition the Node degree is now
\[
\nu_a(\xi)=w_2 1_{|\xi|>d_2-1}+w_3 1_{|\xi|>d_3-1}
\quad\text{almost everywhere}.
\]
The outer Prime-3 bands are nested in the Prime-2 bands. Thus the three
candidate negative Node floors are
\[
\begin{aligned}
C_0&=\kappa-2H_\Gamma(a),\\
C_2&=\kappa+w_2-H_\Gamma(\ell_2)-H_\Gamma(2a-\ell_2),\\
C_3&=\kappa+w_2+w_3-H_\Gamma(\ell_3)-H_\Gamma(2a-\ell_3).
\end{aligned}                                            \tag{3}
\]
Set C=max(C_0,C_2,C_3), with C_3=-infinity at its entrance. These are
the minima on the three radial degree regions, since the archimedean
leakage increases with |ξ|. In particular, no Prime-2-only floor or
band mass is extrapolated unchanged into the new regime.

With L=2a and c=g(L), the diagonal part has eigenvalues -C on E_0,
and H_n+Lc-C on E_n for n>=1. The three positive remainders are the
full variable Node reserve, the entire Gamma difference kernel g(t)-c,
and the two full prime difference forms. Their exact sum recombines to
\[
\boxed{q_a=\operatorname{diag}(H_n)+V+q_0(a)I-K_a-S_a,}
\quad V(\xi)=-\tfrac12\log(1-\xi^2),                     \tag{4}
\]
\[
q_0(a)=-\log(2\pi a)-\gamma,\quad
(K_af)(\xi)=2a\int g(a|\xi-\eta|)f(\eta)d\mu(\eta),
\quad S_a=w_2T_{2,a}+w_3T_{3,a}.
\]
Indeed the regular Gamma degree plus regular leakage equals
2H_Gamma(a)+2 integral_0^a g(t)dt=log(4/a)+pi/2. The singular
difference operator has eigenvalues H_n; its leakage is V. Expanding
each prime difference energy cancels its full degree against the Node
degree, leaving exactly the signed correlations in (4).

The common closed-form domain is the intersection of the harmonic
diagonal domain with L2(V dmu). The remaining terms in (4) are bounded
self-adjoint perturbations. Polynomials belong to this domain, as
does H1_0. Auxiliary Legendre modes need not themselves have zero
endpoint traces. Finite-rank Legendre projections preserve this form
domain, which is the domain used in the infinite-dimensional Schur step.

## 3. The Prime-3 entrance and what continuity does and does not imply

For a immediately above A=log(3)/2, let u=2-log(3)/a>0. Zero endpoint
traces and Cauchy-Schwarz give, for f in H1_0(-1,1),
\[
|\langle f,T_{3,a}f\rangle|
\le\int_0^u|f(-1+s)f(1-u+s)|ds
\le\|f'\|_H^2\int_0^u2\sqrt{s(u-s)}ds
\le u^2\|f'\|_H^2.                                     \tag{5}
\]
Thus the new signed prime term vanishes quadratically in overlap width
in H1 form norm. Its Node degree is at most w_3 u^2||f'||^2; its
positive difference form is at most 2w_3 u^2||f'||^2. This proves a
continuous entrance of the actual combined channel, including its
changed Node degree.

By contrast, ||T_3||=1 for every positive overlap with d_3>=1: put a
function on one band and its translated copy on the other. At u=0,
T_3=0. Vanishing support is therefore **not** a small-L2-operator-norm
argument. In particular, (5) alone does not transfer a positive L2
gap to all sources. The endpoint Schur proof below supplies that step.

On the entire common-domain interval [3/8,B], for the same f in H1_0
before restriction to the moving moment kernel, the checker certifies
\[
|q_a[f]-q_b[f]|\le13|a-b|\|f\|_{H^1}^2.                 \tag{6}
\]
The scalar derivative is |q_0'|<=8/3. The derivative of the Gamma
integral kernel is 2[g(t)+tg'(t)]; fifteen rational interval cells
cover [0,3/2] and certify |g+tg'|<1. Its operator variation is at most
2|a-b|. Zero-extended H1 translations satisfy
||tau_d f-tau_e f||<=|d-e| ||f'||, so both prime terms together cost
at most
\[
\frac{w_2\ell_2+w_3\ell_3}{(3/8)^2}|a-b|\|f\|_{H^1}^2.
\]
The rational bounds w_2<1/2, ell_2<7/10, w_3<2/3, ell_3<11/10
make the sum of the three constants less than 13. This argument also
applies below the Prime-3 entrance, where its shift is zero.

The constraints remain exactly <f,cosh(aξ/2)>=<f,sinh(aξ/2)>=0.
As in the preceding package, projections along 1-ξ^2 and ξ(1-ξ^2)
give a smooth isomorphism from the fixed space H1_0 intersect ker<.,1>
intersect ker<.,ξ> to that moving kernel. The denominators are at
least 2/3 and a/15. This is a coordinate description, not extra moments.

Neither the previous interval theorem nor the present one propagates
an L2 gap by multiplying (6) by an a-box width. The continuation uses
the exact source isometry in Section 9. The variation of auxiliary
Node floors, split masses, or beta bounds is therefore not an omitted
parameter-grid loss. The moment normalization is paid at the endpoint.

## 4. Rational model for the full regular Gamma kernel

From here on a=B, L=2log2, and q_0 is evaluated at this exact endpoint.
For x=t/2,
\[
g(t)=\tfrac14[\operatorname{sech}x+(x/\sinh x-1)/x].
\]
The checker constructs the rational polynomial p(x) of degree 32 by
formal inversion: invert cosh through degree 32 and sinh(x)/x through
degree 33, subtract 1 from the latter, divide it by x, add, and divide
by 4. The value at zero is the removable-limit value 1/4.

For a rigorous uniform remainder, multiply these inverse polynomials
by their denominator Taylor polynomials through degree 62. All
residual coefficients through the appropriate inversion order vanish
exactly. Bound the remaining coefficients absolutely at x=3/4. The
positive omitted denominator tail begins at degree 64 and is bounded
by x^64/[63!(1-x^2)] for cosh and the conservative 64! version for
sinh(x)/x. Multiply by the absolute coefficient norm of the inverse
polynomial; lower all exponents by one for the division by x in the
second residual. Both exact denominators are at least 1. This yields
a rational epsilon with
\[
|g(t)-p(t/2)|\le\epsilon<10^{-10}\quad(0\le t\le3/2).    \tag{7}
\]
The actual saved enclosure is between 4 and 5 times 10^-12. This is
a uniform analytic bound, not a sampled approximation.

Let K^p have kernel L p(a|ξ-η|/2), and let
q^p=diag(H_n)+V+q_0 I-K^p-S. Then
\[
\|q-q^p\|_{\rm bounded\ difference}\le L\epsilon.        \tag{8}
\]
The bound follows from Schur's integral inequality on the probability
measure dmu. The entire Gamma operator, not merely a mode-2 energy,
is enclosed by (8).

The elementary monotonicity needed for the tail also holds on this
larger range. For z=t/2<=1, sinh(z)/z<=1+(10/57)z^2 implies
(sinh(z)/z)^2<cosh(z). Hence
g'(t)=[z^-2-csch(z)coth(z)-sech(z)tanh(z)]/8<0.
The checker verifies g(L)>0, so g(L)<=g(t)<=1/4 on [0,L].

## 5. Exact matrices and all mixed infinite-tail terms

Use P_n rather than E_n; the basis Gram matrix is J_nn=1/(2n+1).
Write V_ij=<P_i,V P_j>, W_ij=<P_i,V^2 P_j>, and
K_ij=<P_i,K^p P_j>. The exact logarithmic moments are
\[
\int_0^1 x^{2r}V(x)dx=\frac{O_r-\log2}{2r+1},\qquad
\int_0^1x^{2r}V(x)^2dx=
\frac{(O_r-\log2)^2+Z_r-\pi^2/12}{2r+1},                 \tag{9}
\]
where O_r=sum_(j=0)^r 1/(2j+1), Z_r=sum_(j=0)^r 1/(2j+1)^2.
These follow by differentiating the beta integral twice. Expanding
P_iP_j reduces V and W to (9), with no singular-endpoint quadrature.

For K, let P_i(2v-1)=sum_r b_ir v^r, where
b_ir=(-1)^(i+r)(i+r)!/[(r!)^2(i-r)!]. Integrating the two triangles
in [0,1]^2 by the beta integral gives, for every integer k>=0,
\[
\langle P_i,\mathcal K_kP_j\rangle
=2^k\sum_{r,s} b_{ir}b_{js}
\frac{r!k!/(r+k+1)!+s!k!/(s+k+1)!}{r+s+k+2},             \tag{10}
\]
where Kcal_k has kernel |ξ-η|^k. Thus
K_ij=L sum_k p_k(a/2)^k <P_i,Kcal_k P_j>.
The image Kcal_k P_j is a polynomial of degree at most j+k+1.
This proves exact finite support of its Legendre coefficients beyond
that degree. Symmetry gives the corresponding lower band bound;
for even k the kernel is a polynomial and entries with max(i,j)>k
vanish as well. These are exact identities used for efficiency.

Set u=2-log3/log2, b=1-u. In the same-parity sectors,
\[
T_{d,ij}=(-1)^j\sum_{k,l}a_{ik}a_{jl}
\frac{k!l!}{(k+l+1)!}(2-d)^{k+l+1},\quad
a_{nk}=\frac{(-1)^{n+k}(n+k)!}{2^k(k!)^2(n-k)!}.           \tag{11}
\]
This evaluates T_2 at d=1 and T_3 at d=2-u exactly. Put
S_ij=w_2 T_(1),ij+w_3 T_(2-u),ij. For the squared operator,
\[
\begin{aligned}
(S^2)_{ij}={}&w_2^2\frac{\delta_{ij}}{2i+1}
+w_3^2\left[\frac{\delta_{ij}}{2i+1}-\int_{-b}^{b}P_iP_jd\mu\right]\\
&+w_2w_3(C_{ij}+C_{ji}),                                \tag{12}\\
C_{ij}={}&\langle T_2P_i,T_3P_j\rangle
=u\int_0^1P_i(uv)P_j(1-u+uv)dv.
\end{aligned}
\]
If P_i(x)=sum_k c_ik x^k, the last integral is the rational polynomial
\[
C_{ij}=\sum_{k,l}c_{ik}
\frac{(-1)^l(j+l)!}{2^l(l!)^2(j-l)!}
\frac{k!l!}{(k+l+1)!}u^{k+l+1}.                          \tag{13}
\]
Thus mixed-prime interference is retained in S^2 before projection.

We also evaluate <V P_i,S P_j> analytically. For n>=0, m=n+1, define
\[
\begin{aligned}
F_n^-(b)&=\frac{H_m-\sum_{k=1}^m b^k/k-(1-b^m)\log(1-b)}m,\\
F_n^+(b)&=\frac{(1-(-1)^m)\log2-\sum_{k=1}^m(-1)^{m-k}/k
-(b^m-(-1)^m)\log(1+b)+\sum_{k=1}^m(-1)^{m-k}b^k/k}{m}.
\end{aligned}                                            \tag{14}
\]
Integration by parts gives F_n^- = integral_b^1 x^n[-log(1-x)]dx
and F_n^+ = integral_b^1 x^n log(1+x)dx. Therefore
integral_b^1 x^n V(x)dx=(F_n^--F_n^+)/2. For 1<=d<2,
\[
\langle VP_i,T_dP_j\rangle
=(-1)^i\int_{d-1}^1 V(x)P_i(x)P_j(d-x)dx.                \tag{15}
\]
Polynomial expansion and (14) compute the weighted sum VS_ij of (15),
using b=0 for Prime 2 and b=1-u for Prime 3. The logarithmic endpoint
and all band endpoints are included exactly.

Now fix N=31. Let Z contain all same-parity modes through N, including
j=0 or 1, and let Y contain **every** mode of that parity above N.
Let B_op=V-K^p. Parseval gives
\[
\begin{aligned}
E^B_{il}&=W_{il}-\sum_{k\in Z}(2k+1)V_{ik}V_{kl}
+\sum_{N<k\le N+33}(2k+1)(K_{ik}K_{kl}-V_{ik}K_{kl}-K_{ik}V_{kl}),\\
E^S_{il}&=(S^2)_{il}-\sum_{k\in Z}(2k+1)S_{ik}S_{kl},\\
E^{BS}_{il}&=VS_{il}-\sum_{k\in Z}(2k+1)V_{ik}S_{kl}
-\sum_{N<k\le N+33}(2k+1)K_{ik}S_{kl},\\
\boxed{E^C}&=E^B+E^S-E^{BS}-(E^{BS})^*.                  \tag{16}
\end{aligned}
\]
All sums use the same parity. The finite upper limit in the K terms
is exact polynomiality from (10). In particular E^C is exactly the
Gram matrix of P_Y(B_op-S)P_i. The V and shift tails are not truncated.
This includes all Node/Gamma/Prime cross terms in the coupling itself.
No replacement by twice the sum of separate Gram masses occurs here.

## 6. Two actual moments, including the entire omitted moment tail

For each parity use j=0, m=cosh(aξ/2), or j=1, m=sinh(aξ/2).
On X_j=E_j perpendicular in that parity define
\[
\mathcal Mx=x-\frac{\langle x,m\rangle}{\langle E_j,m\rangle}E_j.
\]
It is onto the actual Mellin kernel in the common form domain. The
15 low modes are 2,4,...,30 or 3,5,...,31. Their exact images are
\[
v_n=P_n-r_nP_j,\qquad r_n=\frac{\langle P_n,m\rangle}{\langle P_j,m\rangle}.
                                                               \tag{17}
\]
The checker integrates the Taylor series through degree 80 or 81 and
bounds the full remainder using |P_n|<=1 and the next-term geometric
ratio. Thus every finite moment correction is an interval enclosure
of the exact moment, not a polynomial replacement of the condition.

Cauchy-Schwarz and the positive Taylor remainders give
\[
\|\mathcal Mx\|^2\le(1+\beta_j)\|x\|^2,
\quad\beta_0=\left[\frac{(a/2)^2}{2(1-(a/2)^2/12)}\right]^2,
\quad\beta_1=\left[\frac{(a/2)^2}{6(1-(a/2)^2/20)}\right]^2. \tag{18}
\]
For even parity subtract 1 from cosh and use <E_0,cosh>>=1.
For odd parity subtract (a/2)ξ from sinh and use
<E_1,sinh>>=a/(2sqrt3). The checker verifies beta_j<1.

Let Mcal^0 be (17) on the low block and the identity on Y. The first
tail degree n_* is 32 or 33. Orthogonality to the moment's Taylor
polynomial of degree n_*-2 yields
\[
\|\mathcal M-\mathcal M^0\|\le\epsilon_m=
\frac{(a/2)^{n_*}}{n_*!\,[1-(a/2)^2/((n_*+1)(n_*+2))]}
\begin{cases}1,&j=0,\\4/a,&j=1.\end{cases}                \tag{19}
\]
The odd factor exceeds 2sqrt3/a. This bounds the whole infinite
moment tail. Also ||Q^p E_j||<9: the diagonal scalar costs <4,
||V E_j||<2 by (9), ||K^p||<1, and ||S||<2.
Expanding the rank-one change of moment map, with ||Mcal^0||<sqrt2
and epsilon_m<1, costs less than 45 epsilon_m; we use 80 epsilon_m.
Together with (8),
\[
F:=\mathcal M^*q\mathcal M=F^0+E,\quad
F^0=(\mathcal M^0)^*q^p\mathcal M^0,
\qquad\|E\|\le e:=2L\epsilon+80\epsilon_m.               \tag{20}
\]
This is a bounded form difference since Q^p E_j belongs to H. The
finite matrix already contains the full low-mode moment cost and
its mixed terms. The only omitted moment correction is bounded in e.
There is no missing additional beta K subtraction and no third moment.

## 7. The actual infinite-dimensional Schur certificate

On Y the constant part 1/4 of the integral kernel annihilates every
vector. Using (7), monotonicity of g, V>=0, and ||S||<=w_2+w_3,
the actual tail D of F satisfies
\[
D\succeq\delta I,\qquad
\delta=H_{n_*}+q_0-L(1/4-g(L)+\epsilon)-w_2-w_3-e>\tfrac12.
                                                               \tag{21}
\]
Apply the moment change (17) to both indices of E^C in (16). Call
the resulting matrix G. It is the exact entire-tail Gram of the
model coupling C^0, so (C^0)^*C^0=G. The actual coupling C differs
in norm by at most e. With tau=1/1000,
\[
C^*C\preceq G^{\rm act}:=\frac{1001}{1000}G+1001e^2J.    \tag{22}
\]
Let A^0_ik=q^p[v_i,v_k]. Then the actual Schur complement obeys
\[
S_{\rm Schur}=A-C^*D^{-1}C
\succeq A^0-eJ-G^{\rm act}/\delta.
\]
Outward rational interval LDL factorization certifies that
\[
A^0-eJ-G^{\rm act}/\delta-10^{-9}J                       \tag{23}
\]
has all 15 pivots strictly positive in each parity. Thus the actual
infinite-dimensional Schur complement is strictly greater than
10^-9 times the identity. The finite matrix has not replaced the
infinite-dimensional operator; (16), (20)--(22) control its full tail.

The actual shear is also bounded, not just that of a comparison form:
\[
\|D^{-1}C\|^2\le
\delta^{-2}\sum_{n\text{ low}}(2n+1)G^{\rm act}_{nn}<16.  \tag{24}
\]
Its inverse has norm <5. Completing the full square and using
delta>1/2 therefore gives F[x]>(10^-9/25)||x||^2.
Finally (18) yields the required entire-numerator division
\[
\boxed{q[\mathcal Mx]>
\frac{10^{-9}/25}{1+\beta_j}\|\mathcal Mx\|^2
>10^{-11}\|\mathcal Mx\|^2.}                             \tag{25}
\]
All operators commute with reflection, so adding the parity estimates
proves (1) at B. The reported constant is a conservative lower bound;
it is not an estimate of the optimal coercivity constant.

## 8. Directed arithmetic and endpoint results

`check_prime3.py` uses only Python's standard library, integers, and
Fraction. Every interval operation rounds outwards to 10^-100 Z.
Polynomial integrals, logarithmic band integrals, matrix operations,
sign decisions, and displayed enclosures use no binary floats.

The exponential uses Taylor degree 128 with the next-term geometric
tail. atanh uses 128 positive terms and x^257/[257(1-x^2)]; logs are
reduced by exact powers of two. atan uses 128 alternating terms plus
the next positive term. Machin's identity encloses pi. Integer square
root supplies rational enclosures of sqrt2 and sqrt3; their squares
are checked. No decimal transcendental enclosure is imported.

For gamma, Euler-Maclaurin through B4 gives a center
H_N-log N-1/(2N)+1/(12N^2)-1/(120N^4), N=10000, and remainder
radius at most 1/(120N^4). Indeed B4(t)=t^2(1-t)^2-1/30 on [0,1],
so |periodic B4|<=1/30, and
integral_N^infinity |(1/x)^(4)|dx=6/N^4; division by 4! gives
the stated radius. This replaces the much wider trapezoid enclosure
without assuming unproved digits. The cancellation-free regular-g
series, including its first two derivative tails, certifies (6).

Directed output from the endpoint certificate:

| Certified quantity | Even | Odd |
|---|---:|---:|
| actual tail lower bound | >0.778285614675 | >0.808588644978 |
| actual Schur complement | >10^-9 I | >10^-9 I |
| actual shear increment squared | <5.721119324403 | <5.557938959288 |
| inverse shear norm used | <5 | <5 |
| moment beta upper bound | <0.003680101199 | <0.000405612696 |
| normalized source gap | >10^-11 | >10^-11 |

The bound e in (20) is less than 1.2 times 10^-11. JSON stores exact
rational endpoints as well as outward decimal displays. Values named
lower bounds are not upper estimates of the actual pivot or gap.

The saved certificate has 23 check groups, including 30 positive LDL
pivots and a 15-cell analytic derivative cover. `--verify` recomputes
it, requires byte-identical saved JSON and log, and verifies the five
payload SHA-256 hashes. `--write` explicitly regenerates the certificate
and manifest. The default run writes nothing. The manifest does not
hash itself. No quadrature or numerical eigenvalue calculation is used.

## 9. Exact continuation and a representation independent of prime labels

For 0<a<=b define
\[
(J_{a,b}f)(\xi)=\sqrt{b/a}\,f((b/a)\xi)1_{|\xi|<a/b}.
\]
This is unitary onto its supported subspace, preserves zero traces,
satisfies J_b,c J_a,b=J_a,c, and scales the two moments by
M_(b,plus/minus)(J_ab f)=sqrt(a/b) M_(a,plus/minus)(f).
In physical coordinates it is ordinary zero extension. Newly internal
Gamma edges replace exactly the corresponding removed leakage, and
prime correlations are unchanged. Hence
\[
q_b[J_{a,b}f]=q_a[f].                                    \tag{26}
\]
Taking b=B transfers (25) to every smaller window, including those
where Prime 3 or both prime channels are inactive. No intermediate
grid of a-values is needed. Both Mellin conditions are preserved
exactly, without a further moment. This proves (1) on the continuum.

More generally, all prime powers can be expressed in the same family:
\[
q_a=\operatorname{diag}(H_n)+V+q_0(a)I-K_a
-\sum_{n<e^{2a}}\frac{\Lambda(n)}{\sqrt n}T_{\log(n)/a}.   \tag{27}
\]
The sum is finite on every bounded window, and equality at the cutoff
has zero overlap. Prime-power weights are Lambda(p^k)=log(p).
Formula (26) and its composition law hold for this whole locally
finite family, not merely for the first two primes. On any compact
parameter interval [a_min,B_max], one valid H1 Lipschitz constant is
\[
\frac1{a_{\min}}+2\sup_{0\le t\le2B_{\max}}|g(t)+tg'(t)|
+\frac1{a_{\min}^2}\sum_{n<e^{2B_{\max}}}
\frac{\Lambda(n)\log n}{\sqrt n}.                        \tag{28}
\]
The same partial-translation Gram construction can be formed for any
finite active set by integrating polynomial products over intersections
of shift bands. Thus the representation, the fixed positive core
diag(H_n)+V, the moment coordinates, and window law do not require
a separate architecture for each new prime.

This does **not** yet provide a prime-independent positive reserve
for unbounded windows. For example, the crude all-channel tail bound
\[
H_{N+1}+q_0(a)-2a\sup_{[0,2a]}|g(t)-g(0)|
-2\sum_{n<e^{2a}}\Lambda(n)/\sqrt n                       \tag{29}
\]
cannot stay positive for a fixed N as a grows: already q_0(a) tends
to minus infinity. Failure of (29) is only failure of that norm bound,
not a negative Weil vector, a C15 necessity, or a no-go for the full
coupled operator. A uniform positive reserve or an alternative
channel readout remains a distinct research obligation. Form-norm
completions and source isometries after positivity are not identified
with the desired global arithmetic-archimedean output geometry.

## 10. Provenance and remaining obligations

The publication base is PR #137 head
`eea8ff64e63bfca3c536427dd27fb0fc355edaa4`. This package adds six files
and preserves every historical file. The connected nonpole identity
is the imported corrected identity anchored at `9aa5cb1...`; this
work does not replace its external audit. All endpoint numbers here
are recomputed by the self-contained checker.

No A1, third Mellin condition, local crossing claim, merge, main
change, or Registry promotion is made. External acceptance of the
preceding and present interval theorems remains open. The new closed
author-level gate is the complete two-prime interval through log(2).
Beyond it, Prime-Power 4 becomes active. The unit window a=1,
full C1-GEOM, a prime-independent positive reserve/readout, Object X,
and RH remain open.
