# A complete infinite-shell Schur enclosure for the inherited near-null direction

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `1f7628b20e4bd7b3588ae36cfdf66c3f1656d1ca` on
`research/x-c1-inherited-resonance-shell-schur-2026-09-18`.
This is an append-only continuation of the reduced coordinate theorem.
The main branch and merged PR #137 are not changed.

## 1. Statement, normalization and scope

Let B=log(5)/2, b=B+h, and 0<h<=10^-20. Use the physical L2(dx)
inner product, linear in its first argument. All quantities below are real
on the specified source, but the shell estimates allow complex functions.
The core source is exactly the source in
`near-null-source-transport-2026-09-18/`, with its pinned rational
degree-62 polynomial F and exact moment ratio:

\[
 v_B(t)=(2B)^{-1/2}\bigl(F(t/B)-\rho(B)(1-(t/B)^2)\bigr),\qquad
 \rho(B)={\langle F,\cosh(Bx/2)\rangle_{dx/2}
                 \over\langle1-x^2,\cosh(Bx/2)\rangle_{dx/2}}.
\tag{1}
\]

The factor (2B)^(-1/2) is the isometric change of variables. The source
has NOT subsequently been rescaled to unit norm: ||v_B||^2 is about
0.16543536. Its endpoint traces vanish and its two Mellin moments vanish
exactly. This is physical zero extension of the fixed source at B, not
the changing polynomial family v_b of the earlier transport calculation.

Retain the parent's exact functions chi and psi, with psi(B)=1, chi(B)=0,
integral_0^B chi H=1 and integral_0^B psi H=0, H(t)=cosh(t/2). Write

\[
 c_v={\langle v_B,\psi\rangle\over\|\psi\|^2},\qquad
 w_v=v_B-c_v\psi\in\mathcal F_B^0,\qquad e=(1,0)\in\mathcal F_D.
\tag{2}
\]

The quotient and form domains are exactly those of the anchor. In particular
the reduced core form a_0 is a form compression, and physical H1 sources
satisfy the joint trace condition w(B)+t=s(B), s(b)=0. No separate H1_0
condition is imposed on w_v. It has trace -c_v at B.

The new result concerns the FULL shell response to this ONE core direction:

\[
 \eta_v(b)={\|D_b^{-1/2}C_0w_v\|_X^2\over a_0[w_v]},\qquad
 r_v(b)=a_0[w_v]-\|D_b^{-1/2}C_0w_v\|_X^2.
\]

Uniformly on the stated right interval, directed rational enclosures prove

\[
 \boxed{\eta_v(b)<1-4\,10^{-11},\qquad
 r_v(b)>{5449\over10^{16}}=5.449\,10^{-13}.}
\tag{3}
\]

The latter is the energy remainder for the fixed normalization (1), not
a Rayleigh quotient. A narrower enclosure is

\[
 5.44902716834069532\,10^{-13}\le r_v(b)
 \le5.44906829720240261\,10^{-13}.
\tag{4}
\]

There is no finite shell replacement in (3). The entire trace-plus-L2 shell
space and its closed form domain enter the proof. The full reduced-core
operator norm, even all-source continuation, and odd continuation remain
OPEN. No negative physical source has been found or asserted.

## 2. Trace diagnostics in physical units

Put E=q_B[v_B], a=q_B[psi], u=q_B(v_B,psi), and g=u-c_v a. Exact algebra gives

\[
 a_0[w_v]=E-2c_vu+c_v^2a,\quad d[c_ve]=c_v^2a,\quad
 c_0(w_v,c_ve)=c_vg.
\tag{5}
\]

The nonpole core form may be used because v_B and psi have zero moments.
All pieces of a pairing with chi or a separate shell below use the nonpole
form explicitly; they are not individually declared admissible Weil sources.

Selected rational outward decimal enclosures (not nearest rounding) are:

| Quantity | Lower bound | Upper bound |
|---|---:|---:|
| c_v | 0.298651520175487245474490692893 | 0.298651520175487245474490692894 |
| ||w_v||^2 | 0.117512910754871149291668703970 | 0.117512910754871149291668703971 |
| a | 0.145813467002544157907084146746 | 0.145813467002544157907084146761 |
| u | -0.000000007790555201770212265899 | -0.000000007790555201770212265890 |
| a_0[w_v] | 0.013005505919952513170909362278 | 0.013005505919952513170909362290 |
| d[c_ve] | 0.013005501266084882066180035310 | 0.013005501266084882066180035312 |
| c_0(w_v,c_ve) | -0.013005503592746036085903692321 | -0.013005503592746036085903692316 |

In particular c_v, a, and a_0[w_v] are separated from zero before any
quotient is formed. The checker verifies the exact Laurent polynomial
identity, as well as the interval reconstruction,

\[
 a_0[w_v]+2c_0(w_v,c_ve)+d[c_ve]=E.
\tag{6}
\]

Here E lies between 0.000000000000545323065282012955 and
0.000000000000545323065282012961. Cancellation of terms of size 10^-2
is therefore substantial. Identities are simplified exactly before computing
the Schur remainder; they are not inferred from a small floating residual.

The scalar probe is

\[
 \rho_e={|c_0(w_v,c_ve)|^2\over a_0[w_v]d[c_ve]}
 ={g^2\over a\,a_0[w_v]}
 \in[0.999999999958101835247772515802,
       0.999999999958101835247772517238].
\tag{7}
\]

It is only a LOWER bound on eta_v. The near-unit value is a real diagnostic:
in this L2 gauge most of the coupling is the trace response. It is not an
upper bound on the full reduced-core coupling.

## 3. An exact trace Riesz approximant and the remaining functional

Use the full shell form from the parent, which satisfies

\[
 d[(t,s)]\ge\delta|t|^2+70\|s\|_{L^2(B,b)}^2,
 \qquad\delta={1\over32\,10^{13}}>0.
\tag{8}
\]

This holds on the completed form domain, not merely on a finite span. Define

\[
 y_N={g\over a}e,\qquad
 \alpha={u\over a},\qquad f=v_B-\alpha\psi=w_v-{g\over a}\psi.
\tag{9}
\]

The coefficients in (9) are exact analytic ratios, enclosed by intervals in
the checker. No rounded coefficient is silently treated as exact. In particular
q_B(f,psi)=0: this is an auxiliary A-orthogonal residual direction, while
the tested reduced direction remains the requested L2 projection w_v.

For z=(t,s), write Y_s=-m_s chi+S_s, m_s=integral_B^b sH, and
L_tilde z=t psi+Y_s. Because e lies in the shell form domain,

\[
 r_N(z):=c_0(w_v,z)-d(y_N,z)=q_b(f,Y_s),\qquad r_N(e)=0.
\tag{10}
\]

These identities hold on the entire form domain by the parent's continuity
and density results. If y=D_b^(-1)C_0w_v and r_N=d(y-y_N, .), Riesz
representation in the d inner product yields

\[
 \boxed{\|D_b^{-1/2}C_0w_v\|^2
       ={g^2\over a}+\|r_N\|_{d^*}^2.}
\tag{11}
\]

Indeed d[y_N]=g^2/a and d(y-y_N,y_N)=r_N(y_N)=0. Thus (11) is an
exact orthogonal splitting in the SHELL ENERGY, not a truncation or an
L2-orthogonal splitting of the physical source.

The whole dual norm is

\[
 \|r_N\|_{d^*}^2=\sup_{0\ne z\in\mathcal F_D}{|r_N(z)|^2\over d[z]}.
\tag{12}
\]

This includes any trace component generated by the exact inverse response
to a shell functional. Setting the trace functional to zero does not amount
to discarding that response.

## 4. Conservative control of the complete shell residual

The full-shell pivot package proves, for any bounded even core f, with
L=log(2/h) and p=||s||_{L2(B,b)},

\[
 |q_b(f,S_s)|\le\|f\|_\infty\sqrt h(L+11)p,
 \qquad |m_s|\le{6\over5}\sqrt h\,p.
\tag{13}
\]

All active arithmetic shifts 2,3,4,5 and the complete Gamma kernel are
included in (13). Channel 5 has zero core-core overlap at B, but is NOT
omitted from the core-shell estimate immediately to its right.

Let M_f>=||f||_infinity and J_f>=|q_B(f,chi)|. Then (10)-(13) imply

\[
 0\le\|r_N\|_{d^*}^2\le
 {h\over70}\left[M_f(L+11)+{6\over5}J_f\right]^2.
\tag{14}
\]

This uses the anisotropic 70 p^2 part of (8). Applying the much smaller
isotropic delta indiscriminately would lose unnecessary powers of the trace
reserve. When p=0 the numerator vanishes; hence division introduces no gap.

The constants are computed without new quadrature. If v_ref=sum l_n P_n,
then |P_n(x)|<=1 on [-1,1] gives

\[
 M_v={\sum|l_n|\over\sqrt{2B}},\qquad M_f=M_v+4|\alpha|.
\]

The parent's full nonpole form is E_Gamma minus an operator of norm at most
14. With N_v=||v_B||^2, therefore E_Gamma[v_B]<=E+14N_v. The same package
has E_Gamma[chi]<=106, ||chi||^2<=18, and |q_B(psi,chi)|<500. Consequently

\[
 J_f\le\sqrt{106(E+14N_v)}+14\sqrt{18N_v}+500|\alpha|.
\tag{15}
\]

Every square root is enclosed by integer square roots and outward rounding.
The checker proves M_f<2111/1000 and J_f<40. More precise directed values
give a coefficient in brackets at h0=10^-20 below 169.676760916352.
For fixed positive constants M,J, the function
h[M(log(2/h)+11)+(6/5)J]^2 is increasing on this interval: its derivative
is F(F-2M)>0, with F=M(L+11)+(6/5)J and L>46. Thus evaluating (14) at
h0 provides the uniform bound

\[
 \boxed{0\le\|r_N\|_{d^*}^2
 \le4.112886170724\,10^{-18}<5\,10^{-18}.}
\tag{16}
\]

No shell polynomial degree, quadrature mesh, or tail cutoff occurs here.

Combining (5), (11), and the exact cancellation gives

\[
 r_v(b)=E-{u^2\over a}-\|r_N\|_{d^*}^2,\qquad
 \rho_e\le\eta_v(b)\le\rho_e+{\text{bound in (14)}\over a_0[w_v]}.
\tag{17}
\]

The complete directed enclosure for eta_v is

\[
 [0.999999999958101835247772515802,
  0.999999999958102151489693134390].
\tag{18}
\]

Equations (16)-(18) prove (3)-(4). The full Riesz equation has thus been
enclosed, although its shell profile has not been explicitly tabulated.

## 5. Exact integration of the core diagnostics

The checker imports only the rational arithmetic primitives, rational source
coefficients, and certified analytic Gamma polynomial construction from the
pinned near-null checker. It evaluates the required forms anew using even
reflection of half-interval polynomials. No stored finite operator matrix or
numerical eigenpair is used as a proof input.

On the reference space L2((-1,1),dx/2), the nonpole form is

\[
 q_B=D_H+V+q_0I-K_B-\sum_{q=2,3,4}w_qT_{\log(q)/B},\quad
 V=-\tfrac12\log(1-x^2),\quad q_0=-\log(2\pi B)-\gamma.
\tag{19}
\]

This representation also applies to the individually non-admissible
approximating pieces when interpreted as the NONPOLE form. Let p(|x|) and
q(|x|) be polynomials on the positive half. Their norm pairing is
sum p_r q_s/(r+s+1). Put H_j=sum_(k=1)^j 1/k and
J_j=integral_0^1 t^j/(1+t)dt, so J_0=log2 and J_j=1/j-J_(j-1).
Splitting the two same-sign and two opposite-sign squares gives

\[
 \langle|x|^r,D_H|x|^s\rangle
 ={H_r+H_s-H_{r+s}+J_0-J_r-J_s+J_{r+s}\over2(r+s+1)}.
\tag{20}
\]

For derivation use
<p,D_Hq>=(1/8)integral integral (p(x)-p(y))(q(x)-q(y))/|x-y| dxdy,
then y=tx in each positive triangle. This is the familiar Legendre
harmonic form on polynomials; the BV cutoff/form closure from the parent
extends it to these even piecewise smooth functions. In particular the cusp
term for r=s=1 is (2log2-1)/3, not zero.

The potential moments are

\[
 \int_0^1x^{2j}V(x)dx={\sum_{k=0}^j(2k+1)^{-1}-\log2\over2j+1},\quad
 \int_0^1x^{2j+1}V(x)dx={H_{j+1}\over4(j+1)}.
\tag{21}
\]

For the regular Gamma polynomial, define
beta(r,k)=r!k!/(r+k+1)! and U(r,k)=sum_(j=0)^k binom(k,j)/(r+j+1).
The complete reflected kernel moment is

\[
 \langle|x|^r,\mathcal K_k|x|^s\rangle
 ={\beta(r,k)+\beta(s,k)+U(r,k)+U(s,k)\over2(r+s+k+2)},
\tag{22}
\]

where Kcal_k has kernel |x-y|^k against dy/2. Same-sign triangles give
the beta terms and opposite-sign triangles give the U terms. With the
rational polynomial g(t)=p_M(t/2)+error, M=144, multiply (22) by
2B p_(M,k)(B/2)^k and sum. The pinned construction proves a uniform
error epsilon_M on [0,2], so the omitted operator satisfies
||K_B-K_(B,M)||<=2B epsilon_M. Every bilinear pairing pays
2B epsilon_M ||p|| ||q|| with directed upper bounds.

For a shift 0<d<2,

\[
 \langle p,T_dq\rangle=\int_{d-1}^1p(|x|)q(|x-d|)dx.
\tag{23}
\]

This already includes both signed branches and the factor dx/2. Divide the
integration interval at 0 and d when present, translate each polynomial,
and integrate every monomial exactly. The checker compares low-degree
instances of (20), (22), (23) with the independent Legendre, full-square,
and beta-polynomial formulas from the older checker.

Conversion back to physical units is essential. If p approximates psi(Bx)
and v is the reference polynomial in (1), then

\[
 q_B[v_B]=q_{\rm ref}[v],\quad q_B(v_B,\psi)=\sqrt{2B}\,q_{\rm ref}(v,p),
 \quad q_B[\psi]=2B\,q_{\rm ref}[p],
\tag{24}
\]

and the analogous factors apply to norm pairings. These factors are present
in the checker, including the L2 projection coefficient c_v.

## 6. The cosh approximation, exact moments, and reproducibility

The reference psi is cosh(Bx/2)/H_B-(A_T/M_B)(1-|x|), where
H_B=cosh(B/2), A_T=(B+sinh B)/(2H_B), M_B=4(H_B-1)/B.
Only its cosh factor is Taylor truncated, through degree 40. All constants
are themselves directed enclosures of their exact definitions.

For x0=41/100>B/2, the error e=psi-p satisfies in physical coordinates

\[
 \|e\|_\infty\le R_0={x_0^{42}\over42![1-x_0^2/(43\cdot44)]},\quad
 \operatorname{Lip}(e|_{[-B,B]})\le
 R_1={x_0^{41}\over2\,41![1-x_0^2/(42\cdot43)]}.
\tag{25}
\]

The zero extension can jump at the endpoints; that leakage is included.
The complete Gamma estimate of the parent gives E_Gamma[e]<=R_1^2+10R_0^2
and ||e||^2<=2R_0^2. Cauchy-Schwarz in Gamma energy and the bounded
14-norm remainder therefore give explicit errors for q(v_B,e), q(psi,e),
q[e], and all norm pairings. For example

\[
 |q(v_B,e)|\le\sqrt{(E+14N_v)(R_1^2+10R_0^2)}
                 +14\sqrt{2N_vR_0^2}.
\tag{26}
\]

To enclose q[psi] from q[p] use q[psi]-q[p]=2q(psi,e)-q[e],
E_Gamma[psi]<=176, ||psi||^2<=32, and |q[e]|<=E_Gamma[e]+14||e||^2.
Every resulting physical approximation radius is below 10^-60 and is
actually added to its computed interval, not merely declared negligible.

The exact source moment ratio in (1) uses the inherited Taylor enclosure
with its full factorial tail. Moment cancellation is an algebraic identity
of exact definitions. Neither the cosh approximation to psi nor a rounded
moment residual is substituted for that identity. There are exactly the
original two Mellin conditions, one automatic by even parity. No third
condition or A1 is introduced.

All computational decisions use integers and Fractions on a directed
10^-160 grid. Logs, pi and gamma use the pinned rational series and
remainder bounds. This reuses arithmetic primitives; it is not an
independently implemented external audit. The checker has 31 new exact
checks, replays the 28 coordinate checks and their 43 full-shell checks,
and binds 41 input files by SHA-256 and Git blob SHA-1. The saved JSON,
log and seven payload hashes are reproduced byte for byte by --verify.

## 7. A correction concerning absolute and relative gates

The assertion that Theta_0<1 is strictly stronger than absolute coercivity
because A_0 is unbounded overlooks a hypothesis already established here:
C_0 is a bounded Hilbert-space operator and D>=delta I. Consequently

\[
 K=C_0^*D^{-1}C_0\quad\hbox{is bounded and nonnegative},\qquad
 K\le M I,\quad M=\|C_0\|^2/\delta<\infty.
\]

For EACH fixed b, R_0=A_0-K>=sigma I with sigma>0 implies

\[
 K\le{M\over\sigma}R_0,\quad
 A_0=R_0+K\le(1+M/\sigma)R_0,\quad
 \boxed{\Theta_0\le {M\over M+\sigma}<1.}
\tag{27}
\]

Conversely Theta_0<1 gives R_0>=(1-Theta_0)A_0>=10^-13(1-Theta_0)I.
Thus the gates ARE equivalent under the present bounded-coupling
hypotheses. A uniform-in-b version of the reverse implication additionally
requires uniform sigma>0 and a uniform finite M; a merely pointwise
assertion must not be substituted. No value of sigma or Theta_0 on the
ENTIRE reduced core is supplied by (3).

For a block-form bound the factor remains 1-sqrt(theta) in front of
a_0[w]+d[z]. The factor 1-theta instead applies to the Schur remainder
relative to a_0. Confusing those two assertions is incorrect.

## 8. What remains open

The trace diagnostics, full Riesz residual, and directed Schur remainder
for w_v are now positive. The proof does NOT control
sup_(w!=0) ||D^(-1/2)C_0w||^2/a_0[w]. An a_0-orthogonal split into w_v
and its full complement still needs low-complement mixed bounds, all core
and shell tails, and a strict operator bound below one. Positivity on one
direction, even with its complete shell response, cannot supply these.

The parent's physical coordinate norm bound 65 and its joint H1 trace
condition remain required in any eventual all-source conclusion. The old
endpoint epsilon already includes its final division by 1+beta; no new
all-source gap or altered normalization is claimed here. A failed future
comparison bound would be undecided, not a negative source certificate.
The research status remains AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.
