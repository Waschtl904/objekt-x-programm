# Quantitative gauge transition, exact block congruence and the complete complement gate

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anchor: `04bc2466053f1ba939158e6a9ecc023ba40bc756`.
Branch: `research/x-c1-inherited-resonance-shell-schur-2026-09-18`.

## 1. Current status and scope

The supplied review describes the earlier directional head d145ba88.
Since then, 4ab3341 has established the A-gauge conditioning theorem and
04bc246 has proved an entire-core gate on the much smaller interval
0<h<=2^(-10^16). Those results and all their files are preserved.

This package makes the transition T_A BETWEEN THE TWO REDUCED coordinate
spaces explicit, supplies quantitative forward and inverse norms, proves
its complete form-domain and H1 transport and its block/Schur congruence,
and records the A-gauge directional quotient already implied by the
published Riesz residual. No new Riesz solve or source selection occurs.

Throughout Sections 2-8, B=log(5)/2 and **0<h=b-B<=10^-20**. We prove

\[
 {1\over3}\|x\|_0^2\le\|T_Ax\|_A^2\le3111^2\|x\|_0^2,
 \qquad \|T_A^{-1}\|\le\sqrt3<2,
\tag{1}
\]

and for the prescribed A-orthogonal near-null coordinate f_A,

\[
 \boxed{\eta_{v,A}(b)<7.55\,10^{-6}},\qquad
 R_A[f_A]=R_0[w_v]>5.449\,10^{-13}.
\tag{2}
\]

The norms in (1) are physical-core L2 plus trace plus RIGHT-shell L2
product norms. They are not energy norms. The additional energy-norm
statements are given separately below.

The entire A-core gate on the FULL interval 0<h<=10^-20 is still
**UNDECIDED**. The exact remaining complement criterion in Section 8
does not certify its own missing hypothesis. The positive even all-source
result on 0<h<=2^(-10^16) remains valid; odd continuation remains open.

## 2. Spaces and certified constants

Use the physical product linear in its first argument. Write

\[
 K_0=K_B\cap\psi^{\perp_{L^2}},\quad
 L_\psi(v)=a(v,\psi),\quad
 a_\psi=a[\psi],\quad n=\|\psi\|^2,
\]
\[
 \ell(v)=L_\psi(v)/a_\psi,\quad K_A=\ker\ell,\quad
 X=\mathbb C\oplus L^2(B,b),\quad e=(1,0).
\]

For general v in K_B the symbol L_psi denotes the unique bounded L2
extension of the form functional, proved in the A-gauge package. The
form identity is asserted on F_B; we do not assume v is in the form
domain merely because v is L2. Its certified bounds, together with the
pinned directional intervals, imply

\[
 |L_\psi(v)|\le272\|v\|,\quad a_\psi>7/50,\quad
 \|\ell\|\le1943,\quad \ell(\psi)=1,
 \quad {1\over2}<n<{9\over16},\quad a_\psi<{3\over20}.
\tag{3}
\]

The old and new product spaces are H_0=K_0 plus X and H_A=K_A plus X.
Their form domains are F_0=F_B intersect K_0 and F_A=F_B intersect K_A,
each paired with the same full shell form domain F_D. The two compressed
core forms are a_0 and a_A; their associated operators are form
compressions, not unproved restrictions of operator domains. Both have
the physical gap epsilon=10^-13. The full shell form satisfies
d>=delta I, delta=epsilon/32, and e belongs to F_D with d[e]=a_psi.

The physical maps are Phi_0(w,z)=Jw+L_tilde z and
Phi_A(f,z)=Jf+L_tilde z, with L_tilde e=J psi. The coordinate theorems
prove both complete form-domain surjectivities and the forward physical
norm constant 65. Those domain results, and not finite algebra alone,
justify the whole-source conclusions below.

## 3. Explicit transition and its actual inverse

Define

\[
 T_A(w,z)=(w-\ell(w)\psi,\ z+\ell(w)e)\quad(w\in K_0),
\tag{4}
\]

and put k(f)=<f,psi>/n, P_0f=f-k(f)psi. Then the inverse is

\[
 \boxed{T_A^{-1}(f,\zeta)=(P_0f,\ \zeta+k(f)e)}\quad(f\in K_A).
\tag{5}
\]

The sign in (5) is PLUS. Since ell(f)=0, ell(P_0f)=-k(f).
Conversely, for w perpendicular to psi and lambda=ell(w),
k(w-lambda psi)=-lambda. These two identities prove both inverse
compositions exactly. Also ell(w-ell(w)psi)=0, and P_0f belongs to K_0.
Both maps preserve the shell profile s and hence m_s.

This is an isomorphism between the two REDUCED spaces. The same expression
on the unreduced K_B plus X would have the old kernel span{(-psi,e)};
it must not be declared invertible on that larger coordinate space.

On both Hilbert and form levels the physical identity is

\[
 \boxed{\Phi_A T_A=\Phi_0.}
\tag{6}
\]

Indeed the core subtraction and shell trace addition cancel physically.
In particular this coordinate change adds no Mellin condition and changes
no physical source. It is not the removal of a physical direction.

## 4. Explicit L2 conditioning of the transition

Let x=(w,(t,s)), lambda=ell(w), p=||s||. Since w is L2-orthogonal to psi,

\[
 \|T_Ax\|_A^2=\|w\|^2+n|\lambda|^2+|t+\lambda|^2+p^2
 \le[1+(n+2)1943^2]\|w\|^2+2|t|^2+p^2.
\]

Using (3),

\[
 1+{41\over16}1943^2={154785225\over16}<3111^2,
\tag{7}
\]

which gives the upper bound in (1).

For the inverse write f=v+k psi with v=P_0f perpendicular to psi.
Then ||f||^2=||v||^2+n|k|^2, while

\[
 \|T_A^{-1}(f,(t,s))\|_0^2=\|v\|^2+|t+k|^2+p^2.
\]

Weighted Cauchy-Schwarz gives
|t+k|^2<=(1+1/n)(|t|^2+n|k|^2). As 1+1/n<3, this yields

\[
 \|T_A^{-1}(f,(t,s))\|_0^2\le3(\|f\|^2+|t|^2+p^2).
\tag{8}
\]

Applying (8) to T_Ax proves the lower bound in (1). These constants
are uniform for the whole original interval; no smallness of h beyond
the inherited coordinate hypotheses enters this step.

The core map U=P_A|_(K_0), Uw=w-ell(w)psi, has inverse V=P_0|_(K_A).
In addition,

\[
 \|w\|\le\|Uw\|\le1458\|w\|,\qquad \|Vf\|\le\|f\|,
\tag{9}
\]

because 1+(9/16)1943^2=33977257/16<1458^2. These are core-map bounds,
not substitutes for the full product bounds in (1).

## 5. Closed form domains and the exact H1 trace transport

For w in F_0, subtracting ell(w)psi stays in F_B and lands in F_A;
for z in F_D, adding ell(w)e stays in F_D. The same argument using
(5) gives the reverse inclusion. Thus

\[
 T_A:F_0\oplus F_D\longrightarrow F_A\oplus F_D
\]

is a bijection. We give explicit continuity in the positive PRODUCT
energies G_0=a_0[w]+d[z] and G_A=a_A[f]+d[zeta], distinguished from
the possibly indefinite full block form on the original interval.

Since f=Uw is a-orthogonal to psi,

\[
 a_A[f]=a_0[w]-a_\psi|\ell(w)|^2.
\]

The shell form Cauchy-Schwarz bound d[z+lambda e]<=2d[z]+2a_psi|lambda|^2
then yields G_A[T_Ax]<=2G_0[x]. Conversely, for f in F_A,
a_0[P_0f]=a_A[f]+a_psi|k(f)|^2 and
|k(f)|^2<=||f||^2/n<=a_A[f]/(epsilon n). Therefore

\[
 G_0[T_A^{-1}y]\le
 \left(1+{3a_\psi\over\epsilon n}\right)a_A[f]+2d[\zeta]
 \le(1+9\,10^{12})G_A[y].
\tag{10}
\]

These product energy norms are complete and dominate their L2 norms,
by the inherited gaps. Equations (10) and its forward counterpart prove
the topological form-space isomorphism, without operator-domain
invariance or an unproved H1_0 restriction on the separate core.

For actual H1 sources psi is internally H1 and psi(B)=1. Formula (4)
takes w(B)+t=s(B) precisely to

\[
 (w(B)-\lambda)+(t+\lambda)=s(B),\qquad s(b)=0.
\tag{11}
\]

The inverse has the identical cancellation with k(f). The shell function
is unchanged, and both core transformations preserve internal H1. The
transition and its inverse are consequently bounded on the corresponding
H1 product subspaces as well: their scalar coefficients are L2-bounded
and multiply the fixed H1 function psi. This proves transport of the
EXACT source trace condition, not just of form closures.

## 6. Exact full block and Schur congruence

Write mathfrak F_0 and mathfrak F_A for the full block FORMS in the two
gauges, using a_0,C_0,d and a_A,C_A,d respectively. F_0 and F_A still
denote the core form domains. To avoid an operator-domain
claim, the notation below is explicitly equality of closed forms.
From (6), polarization and the proven form-domain identities,

\[
 \boxed{\mathfrak F_0(x,y)=\mathfrak F_A(T_Ax,T_Ay).}
\tag{12}
\]

One can also verify all blocks directly. With f=Uw and lambda=ell(w),

\[
 a_0[w]=a_A[f]+a_\psi|\lambda|^2,\quad
 c_0(w,z)=c_A(f,z)+\lambda d(e,z),\quad c_A(f,e)=0,
\]
\[
 d[z+\lambda e]=d[z]+2\Re(\lambda d(e,z))+a_\psi|\lambda|^2.
\tag{13}
\]

For general f in K_A, c_A(f,e)=0 holds for the bounded Hilbert coupling
extension; for form vectors it is exactly a(f,psi)=0. It removes the
trace FORCING, not the trace component of D^-1 C_A f. The entire D inverse
and all shell responses remain in the following Schur forms.

For fixed w, the map z -> z+ell(w)e is a bijection of F_D. Taking the
infimum in (12) and using the full positive shell Riesz realization gives

\[
 \boxed{R_0[w]=R_A[Uw]},\qquad
 R_A[f]=a_A[f]-\|D^{-1/2}C_Af\|^2.
\tag{14}
\]

This is the form congruence R_0=U^* R_A U, with the associated domains
understood as above. It does NOT assert that U preserves associated
operator domains. In particular Theta_0 and Theta_A are different
normalized operator norms and are not invariant under this change of gauge.

## 7. The fixed near-null coordinate: no new source or Riesz solver

Use exactly the pinned physical degree-62 source v_B. Put
c_v=<v_B,psi>/n, w_v=v_B-c_v psi, alpha=a(v_B,psi)/a_psi and
f_A=v_B-alpha psi. Then

\[
 \ell(w_v)=\alpha-c_v,\quad Uw_v=f_A,\quad
 T_A(w_v,c_ve)=(f_A,\alpha e).
\tag{15}
\]

Thus the original physical source is still reconstructed as
v_B=f_A+alpha psi. Neither it nor its coordinates have been rescaled to
unit physical norm. In particular f_A by itself need not be an H1_0
source: f_A(B)=-alpha, while its reconstructing trace coordinate is
alpha and its shell profile is zero. The joint trace condition is exact.

The inherited directed quantities are

\[
 E_A=a_A[f_A]=q_B[v_B]-{|q_B(v_B,\psi)|^2\over a_\psi}>0,
 \qquad \mathcal R=\|r_N\|_{d^*}^2\le\mathcal R_+.
\]

For the full shell, c_A(f_A,z)=r_N(z), since a(f_A,psi)=0. Consequently

\[
 \eta_{v,A}(b)={\mathcal R\over E_A}
 \le {\mathcal R_+\over(E_A)_-}
 <{151\over20000000}=7.55\,10^{-6}.
\tag{16}
\]

The numerator and denominator are taken from the pinned rational
interval endpoints, including every Gamma, cosh and normalization error,
not from the rounded diagnostic decimals. Equation (14) then gives the
same positive Schur remainder R_A[f_A]=R_0[w_v] as before. This extracts
a consequence of the existing FULL residual certificate; it does not
repeat a new one-dimensional solve or upgrade a scalar probe to an
operator bound.

## 8. A precise sufficient gate for the whole A-core complement

Normalize ONLY for the following energy-space decomposition:
v_A=f_A/sqrt(E_A), and let Z_A={z in F_A:a_A(z,v_A)=0}. This is the
complete energy-orthogonal complement, including every infinite coretail.
Let B_h f=D^-1/2 C_A f, as a bounded map from (F_A,a_A) to X, and put

\[
 \kappa(h)=\sup_{0\ne z\in Z_A}{\|B_hz\|^2\over a_A[z]}.
\]

The exact mixed functional is <B_h v_A,B_h z>. Positivity of this Gram
and (16) imply, for all z in Z_A,

\[
 |\langle B_hv_A,B_hz\rangle|^2
 \le\nu\,\kappa(h)a_A[z],\qquad \nu={151\over20000000}.
\]

Thus for any complex c and any z in Z_A,

\[
 \|B_h(cv_A+z)\|^2
 \le(\sqrt\nu|c|+\sqrt{\kappa(h)}\sqrt{a_A[z]})^2
 \le(\nu+\kappa(h))(|c|^2+a_A[z]).
\tag{17}
\]

No sign of a mixed contribution has been omitted and no finite core
or shell truncation appears. A uniform bound kappa(h)<=kappa_* with
kappa_*+nu<1 is therefore a sufficient full A-core gate. For example,

\[
 \kappa(h)\le{999\over1000}\quad\Longrightarrow\quad
 \Theta_A(h)\le{19980151\over20000000}<1.
\tag{18}
\]

Equation (18) is CONDITIONAL: **the hypothesis is not certified on the
whole interval 0<h<=10^-20**. A sharper independently certified mixed
bound mu could instead use (1-nu)(1-kappa_*)>mu^2 with both diagonal
terms below one. Neither version is an assertion that kappa is already
small. The inherited generic estimate is only
kappa(h)<=169/(epsilon log(2/h)); it is insufficient at h=10^-20.

On 0<h<=2^(-10^16), 04bc246 already proves the stronger global
Theta_A<=169/500, Theta_0<1-2*10^-13 and physical even-source gap
>10^-17. We do not weaken or replace that result with (18). For the
remaining widths a sharper complete complement or full operator bound
is still required. A failed comparison is UNDECIDED, never a negative
physical source certificate.

## 9. Factors, evidence and publication discipline

Every eventual relative operator bound theta<1 has Schur factor 1-theta
and full block factor 1-sqrt(theta). The inverse-free physical conversion
uses the forward coordinate constant 65 and min(epsilon,delta), not the
inverse transition constant 3 or 3111^2 from (1). These latter constants
certify the coordinate isomorphism, not an additional obligatory loss in
that different inequality. No previous endpoint normalization is undone
or charged again, and the two Mellin conditions remain exact.

The checker makes 38 new exact checks, binds 65 inherited files and replays the 40-check all-core
package, which itself replays 31 direction, 28 coordinate, 43 shell and
9 A-gauge checks. New rational checks verify the transition constants,
universal inverse/trace/source/complex-block identities, the directional
quotient and the explicitly conditional complement ledger. Saved JSON
and log are reproduced byte for byte, with seven payload SHA-256 hashes.
These finite checks do not replace the analytic closed-form, H1 or
infinite-dimensional arguments above and are not an external audit.

Only this new package is appended on the research branch. No main,
Registry, previous package, PR or merge is changed. No quadrature,
numerical eigenvalue proof, third Mellin condition or A1 is introduced.
