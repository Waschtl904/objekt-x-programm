# Entire reduced-core Schur gate on an explicit logarithmically small shell

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anchor: `d145ba88c86d4d0de665355bf3bff15844dbf414`.
Publication parent: `4ab3341f0e2190cc967affd460c1f370f7918ebc`.
Branch: `research/x-c1-inherited-resonance-shell-schur-2026-09-18`.

## 1. Statement and the substantial width restriction

Let B=log(5)/2, epsilon=10^-13, delta=epsilon/32 and

\[
 N_*=10^{16},\qquad h_*=2^{-N_*},\qquad b=B+h.
\]

The following bounds hold uniformly for **0<h<=h_*** on the ENTIRE
reduced closed core form domain from the coordinate theorem:

\[
 \boxed{\Theta_0(b)<1-2\,10^{-13}},\qquad
 \boxed{R_0\ge {331\over500}\,10^{-13}I}.
\tag{1}
\]

Consequently every nonzero actual even H1_0 two-Mellin source satisfies

\[
 \boxed{Q_W[u]>{1\over5200\,10^{13}}\|u\|_{L^2(dx)}^2
                  >10^{-17}\|u\|_{L^2(dx)}^2.}
\tag{2}
\]

The same constant applies to every smaller positive physical window by
exact zero extension. This is an even all-source continuation, not a
single-direction test. It is a VERY MUCH SMALLER right interval than
0<h<=10^-20. The latter entire-core gate remains **UNDECIDED**. Odd
continuation, larger windows, Object X and RH remain open.

The number h_* is an exact positive rational given in compressed power
notation. It is not zero, an underflowed floating-point value, or a claimed
practical width. No integer with 10^16 bits is constructed by the checker.
The proof below uses exact monotonicity and small rational inequalities
to verify this width. No decimal expansion of h_* is required.

The sharper physical bound (2) also uses the concurrently published
A-gauge conditioning theorem at the publication parent (Section 10).
The original physical-L2 reduced operator in (1) is unchanged. Sections
2-8 independently give the weaker physical bound >10^-30 from that gauge.

## 2. Imported spaces and normalization

All core products are physical L2((-B,B),dx), linear in the first argument.
The shell space is X=C plus L2((B,b),dx), with RIGHT-shell norm
|t|^2+||s||^2; its even physical extension S_s has norm squared 2||s||^2.
Use the parent's fixed chi, psi and H(x)=cosh(x/2), with

\[
 \widetilde L(t,s)=t\psi+Y_s,\quad Y_s=-m_s\chi+S_s,
 \quad m_s=\int_B^b sH.
\]

Let a be the inherited closed core form on F_B, a>=epsilon I, and
F_B^0=F_B intersect psi-perp in PHYSICAL L2. The form a_0 is its
compression to F_B^0, not an unproved restriction of an operator domain.
Let d,D,F_D be the parent's full closed shell form, operator and domain.
The parent proves e=(1,0) belongs to F_D, psi belongs to F_B, and

\[
 \Phi_0:F_B^0\oplus F_D\longrightarrow F_b
\]

is a topological form-space isomorphism. Its physical upper norm bound is
||Phi_0(w,z)||^2<=65(||w||^2+||z||_X^2). The coupling C_0 is bounded
between the specified Hilbert spaces. Actual H1 sources have the joint
trace condition w(B)+t=s(B), s(b)=0; no separate zero trace is imposed on w.

The common-jump nonpole form used on all separate pieces is

\[
 q_b[f]=\mathcal E[f]-\kappa\|f\|^2-
  \sum_{q=2,3,4,5}w_q\langle f,(\tau_{\log q}+\tau_{-\log q})f\rangle,
\quad \mathcal E[f]=\int_0^\infty k(r)\|\tau_rf-f\|^2dr,
\]

where k(r)=exp(-r/2)/(1-exp(-2r)). It agrees with Q_W on the two-Mellin
kernel. The bounded non-Gamma remainder has norm at most 14. Imported
bounds include 4/5<B<81/100, |m_s|<=(6/5)sqrt(h)||s||,
E[chi]<=106 and ||chi||^2<=18. Core-core pairings at b equal those at B.

The reproduced direction package encloses, with all its approximation
errors included, n=||psi||^2 and a_psi=a[psi], and in particular proves

\[
 n>1/2,\qquad 0<a_\psi<3/20.
\tag{3}
\]

No new source is selected or rescaled. The fixed degree-62 source is used
only for the optional decomposition diagnostic in Section 7.

## 3. A strict trace-only bound on the complete reduced core

The form a-epsilon<.,.> is nonnegative. For w in F_B^0, L2 orthogonality
gives a(w,psi)=(a-epsilon<.,.>)(w,psi). Cauchy-Schwarz in this nonnegative
form, valid also when it has a kernel, yields

\[
 |a(w,\psi)|^2\le(a_0[w]-\epsilon\|w\|^2)(a_\psi-\epsilon n)
                    \le a_0[w](a_\psi-\epsilon n).
\]

Define exact quantities

\[
 \lambda_w={a(w,\psi)\over a_\psi},\quad
 f_w=w-\lambda_w\psi,\quad
 \ell[w]={|a(w,\psi)|^2\over a_\psi},\quad
 E[w]=a[f_w]=a_0[w]-\ell[w],\quad
 \tau={\epsilon n\over a_\psi}.
\]

They satisfy, on the full domain,

\[
 0\le\ell[w]\le(1-\tau)a_0[w],\quad
 E[w]\ge\tau a_0[w],\quad
 E[w]\ge\epsilon\|f_w\|^2\ge\epsilon\|w\|^2,
 \quad \tau>{10\over3}\epsilon.
\tag{4}
\]

The last norm inequality uses w perpendicular to psi, so
||f_w||^2=||w||^2+|lambda_w|^2 n. The auxiliary f_w is a-orthogonal
to psi; this is an exact elimination step for EVERY w, not an additional
condition on the physical source. The domain is preserved because psi is
in F_B. Formula (4) also proves the trace-only contraction on the whole
original interval 0<h<=10^-20.

## 4. Retaining logarithmic growth of the full shell pivot

Write L=log(2/h), h0=10^-20. Section 5 of the full-shell pivot proof gives
on the dense original shell domain, and hence its closure,

\[
 d[(t,s)]\ge\delta|t|^2+
 \left[2(L-8)-h(8L+450)-32\,10^{13}h(4L+644)^2\right]\|s\|^2.
\tag{5}
\]

This follows from its full trace/shell expansion and Young inequality;
it does not replace the actual shell operator. Since h(8L+450) and
h(4L+644)^2 increase with h on (0,h0], and 46<log(2/h0)<47,

\[
 h(8L+450)+32\,10^{13}h(4L+644)^2
 \le h_0(826+32\,10^{13}\,832^2)<3.
\]

The derivatives of the two functions are 8L+442 and
(4L+644)(4L+636), respectively, both positive. As L>46,

\[
 \boxed{d[(t,s)]\ge\delta|t|^2+L\|s\|^2}\quad(0<h\le h_0).
\tag{6}
\]

Indeed the bracket in (5) is >2L-19>L. Thus the anisotropic floor used
here grows without bound as h tends to zero, while keeping the trace
coordinate and all its interactions.

## 5. A quantitative coupling bound for arbitrary L2 core functions

For any even L2 core f and p=||s|| on the right shell, the complete
disjoint-support pairing obeys

\[
 \boxed{|q_b(f,S_s)|\le12\|f\|p}\quad(0<h\le h_0).
\tag{7}
\]

Here is a physical-normalization proof. For smooth separated pieces the
Gamma cross pairing is minus the integral with kernel k(|x-y|); its two
reflected shell integrals equal twice the positive-shell integral. Write
x=B+r, y=B-z on the positive core. The same-side kernel is bounded by
1/[2(r+z)]+1/4, since k(t)<=1/(2t)+1/4 for all t>0. The Carleman
operator 1/(r+z) between the positive half-lines has norm at most pi:
the weighted Schur integral with weight z^-1/2 equals pi r^-1/2
by z=r v^2. Restricting its input and output intervals does not enlarge
this bound. On the opposite core half, |x-y|>=B and k(|x-y|)<1.
The two bounded-kernel pieces have total norm at most (5/4)sqrt(Bh).
Since ||f||=sqrt(2)||f|_(0,B)||, the entire reflected Gamma pairing is
bounded by

\[
 \sqrt2\left({\pi\over2}+{5\over4}\sqrt{Bh}\right)\|f\|p
 <\left(3+{15\over8}\,10^{-10}\right)\|f\|p<4\|f\|p.
\tag{8}
\]

Only sqrt2<3/2, pi<4, B<1 and sqrt(h)<=10^-10 were used. The scalar
term has disjoint supports. At x in (B,b), x+log(q) lies outside the
core. Thus each arithmetic channel contributes
-2w_q integral_B^b f(x-log(q)) conjugate(s(x)) dx, of modulus at most
2w_q||f||p. There are exactly four channels, each w_q<1, including q=5.
Their total is at most 8||f||p. This proves (7). No false small operator
norm for shrinking translations, or orthogonality between channels, is used.

The integral bounds extend from separated smooth data to all supported
L2 data by boundedness. On the closed form domains they agree with the
nonpole cross form by the parent's density and continuity argument. In
particular (7) contains arbitrary high core frequencies and the full
shell; there is no finite polynomial cutoff or supremum-norm assumption.

If f is additionally in F_B, put E=a[f]>=epsilon||f||^2. Gamma
Cauchy-Schwarz and the bounded 14-norm remainder give

\[
 |q_B(f,\chi)|\le\sqrt{106(E+14\|f\|^2)}+14\sqrt{18}\|f\|
                       <100\sqrt{E/\epsilon}.
\tag{9}
\]

In fact epsilon<=1, sqrt(106*15)<40 and 14sqrt(18)<60. Combining
(7)-(9) with the exact moment correction gives

\[
 |q_b(f,Y_s)|\le(12+120\sqrt h)\sqrt{E/\epsilon}\,p
                         \le13\sqrt{E/\epsilon}\,p.
\tag{10}
\]

All separate pieces in (9)-(10) use the nonpole form, including chi and S_s.
They are not declared individually admissible Weil sources.

## 6. Complete Riesz elimination and the all-core gate

For arbitrary w in F_B^0 set y_N=lambda_w e. The exact full-shell Riesz
residual, using a(f_w,psi)=0, is

\[
 r_w(z)=c_0(w,z)-d(y_N,z)=q_b(f_w,Y_s),\qquad r_w(e)=0.
\]

Let y be its original exact response, d(y,z)=c_0(w,z). Existence follows
from d>=delta I and bounded C_0. Orthogonality in the d inner product gives

\[
 \|D^{-1/2}C_0w\|^2=\ell[w]+\|r_w\|_{d^*}^2.
\tag{11}
\]

In particular the inverse response to r_w may itself have a trace
component; that response is included in the entire dual norm. From
(6) and (10), including p=0 where r_w vanishes,

\[
 0\le\|r_w\|_{d^*}^2\le\beta(h)E[w],\qquad
 \beta(h)={169\over\epsilon\log(2/h)}.
\tag{12}
\]

This is a simultaneous operator/form inequality on ALL reduced-core
directions. If beta(h)<=beta_*<1, then (4), (11) and (12) imply

\[
 R_0[w]\ge(1-\beta_*)E[w]\ge(1-\beta_*)\epsilon\|w\|^2,
\quad
 \Theta_0\le1-(1-\beta_*)\tau.
\tag{13}
\]

For h<=2^(-N_*), L>= (N_*+1)log2>N_*/2, since log2>1/2.
Also h_*<=2^-80<10^-20, verified by the small integer inequality
2^80>10^20. Hence every imported small-shell hypothesis applies and

\[
 \beta(h)\le {169\over\epsilon(N_*/2)}={169\over500},\qquad
 (1-\beta_*)\tau>{331\over150}\,10^{-13}>2\,10^{-13}.
\]

This proves (1). It also gives a general sufficient threshold
log(2/h)>169/epsilon; the dyadic width is simply a convenient explicit
choice with comfortable rational slack. No optimization of this threshold
or of the coupling constant 12 is claimed.

## 7. The fixed near-null direction and its full complement

The global argument above already includes all mixed contributions.
Its relation to the proposed a_0-orthogonal split can be made precise.
Give F_B^0 its complete energy inner product a_0, put
v_0=w_v/sqrt(a_0[w_v]), and let Z=v_0-perp in THIS energy product.
Let T and P be the bounded nonnegative operators represented by ell[w]
and ||r_w||_(d*)^2 in this energy space. Equations (4) and (12) say

\[
 0\le T\le(1-\tau)I,\quad \operatorname{rank}T=1,\qquad
 0\le P\le\beta_*(I-T).
\tag{14}
\]

The parent fixes <Tv_0,v_0>=rho_e. For a rank-one positive operator
the squared norm of its representing vector splits into its component
along v_0 and its component in Z. Therefore

\[
 \|P_ZT|_Z\|\le1-\tau-\rho_e<4.2\,10^{-11},\qquad
 |\langle Tv_0,z\rangle|^2
 \le\rho_e(1-\tau-\rho_e)a_0[z]\quad(z\in Z).
\tag{15}
\]

The checker verifies the first numerical bound with outward rational
endpoints from the pinned rho_e enclosure. It is a TRACE diagnostic for
the complete complement, not its full Schur bound. For every c in C
and z in Z, (14) controls the WHOLE residual at c v_0+z, including its
mixed term. Thus

\[
 T+P\le\beta_*I+(1-\beta_*)T
          \le[1-(1-\beta_*)\tau]I.
\tag{16}
\]

No coretail, mixed direction, or shelltail is discarded. The inequality
P<=beta_*(I-T) retains correlation with the trace elimination; independent
entrywise losses are unnecessary. For example residual mixed terms obey
|P(x,z)|^2<=P[x]P[z]<=beta_*^2 E[x]E[z]. These statements concern arbitrary
elements of the complete form domain, not only finite matrices.

## 8. Return to actual sources, with every norm factor

Set theta=1-2*10^-13. The parent block identity and (1) give

\[
 q_b[\Phi_0(w,z)]\ge(1-\sqrt\theta)(a_0[w]+d[z])
 \ge{(1-\sqrt\theta)\delta\over65}\|\Phi_0(w,z)\|^2.
\]

Here the block factor is **1-sqrt(theta)**; 1-theta is a relative
Schur-rest factor only. Since
1-sqrt(1-x)=x/(1+sqrt(1-x))>x/2 for 0<x<1, the physical constant is
strictly greater than epsilon^2/(32*65)=1/(2080*10^26)>10^-30.
Section 10 improves this physical bound to (2).
This uses the actual coordinate map and its complete form-domain
surjectivity. In particular it applies to all actual H1 sources with
w(B)+t=s(B), s(b)=0. No extra boundary or Mellin condition is imposed.

The old endpoint epsilon already paid its previous 1+beta normalization.
It is imported as a physical gap; it is neither undone nor paid a second
time. The new factor 65 and the trace-plus-right-shell normalization
are paid explicitly above. No approximate inverse shear is substituted
for the actual one: this conclusion uses the relative block criterion.

## 9. What is still undecided, and what the checker establishes

At h0=10^-20 the available comparison coefficient is bounded above by
169/(46 epsilon), which is greater than 10^13. Even the exact coefficient
169/(epsilon log(2/h0)) is greater than 10^13 because log(2/h0)<47.
Thus criterion beta<1 fails badly there. This is a failed SUFFICIENT
bound, not a lower bound on an actual coupling, and gives no negative
source. The whole interval h_*<h<=10^-20 remains uncertified here.

A precise sufficient remaining obligation on that interval is

\[
 \sup_{0\ne w\in F_B^0}
 {\|q_b(f_w,Y_{(\cdot)})\|_{d^*}^2\over a[f_w]}<1
\]

uniformly, or a direct strict bound on T+P that can succeed even when
this stronger sufficient residual comparison fails. A refined low/coretail
estimate exploiting the inherited near-null geometry may improve (12).
The trace-complement number (15) alone does not do so.

The new checker binds 57 input files, replays the complete parent
direction checker (31 checks), and its coordinate (28) and shell (43)
replays, as well as the 9 concurrent A-gauge checks. It verifies the rational reserve ledger, exact polynomial
identities for trace elimination and the operator majorant, the dyadic
width implications without underflow, and the physical norm conversion.
It reproduces its JSON and log byte for byte and verifies seven payload
SHA-256 hashes. Analytic form closure, Carleman boundedness and
infinite-dimensional inequalities are proved above, not inferred from
finite tests. The endpoint theorem is imported, not independently audited
or rerun in full by this checker. Reuse of the parent's arithmetic and
proof chain remains AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.

Only this new package is appended. No existing package, main, Registry,
PR or merge is changed by this result.

## 10. Preserved concurrent A-gauge theorem and stronger physical gap

During this calculation commit 4ab3341f0e2190cc967affd460c1f370f7918ebc
appended `a-gauge-conditioning-2026-09-19/`. Its eight files are preserved,
hash-bound and reproduced. That theorem establishes complete Hilbert and
form coordinates on the core F_(B,A)^0={f in F_B:a(f,psi)=0}, with the
same full shell D and physical forward norm bound 65. It also proves
the exact joint H1 gluing statement and c_A(f,(t,s))=q_b(f,Y_s).

Our equation (10), now applied directly to EVERY f in that A-gauge core,
together with (6) gives on the stated dyadic interval

\[
 |c_A(f,z)|^2\le {169\over\epsilon L}a_A[f]d[z]
                       \le{169\over500}a_A[f]d[z].
\tag{17}
\]

Thus the FULL A-gauge operator satisfies Theta_A<=169/500. This is a
different operator from the original L2-gauge Theta_0 of (1); the two
constants must not be identified. The new A-gauge theorem alone left
this gate open; (17) supplies it on the much smaller dyadic interval.

Since 169/500<9/25=(3/5)^2, its block factor obeys
1-sqrt(169/500)>2/5. Its complete coordinate and source theorem then gives

\[
 q_b[u]>{(2/5)\delta\over65}\|u\|^2
       ={1\over5200\,10^{13}}\|u\|^2>10^{-17}\|u\|^2,
\]

proving (2). Only the FORWARD norm bound 65 enters this relative block
conversion. The proved inverse coordinate constant 140000000 is needed
for the domain isomorphism, but is not an additional loss in this
inequality. No unverified inverse or change of physical normalization
is used. This corollary preserves the original source class, both Mellin
conditions, the fixed source, and all eight concurrent package files.
