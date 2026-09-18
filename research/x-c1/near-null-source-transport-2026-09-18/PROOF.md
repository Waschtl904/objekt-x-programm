# The explicit even near-null source: reconstruction, full directional tail, and transport

2026-09-18. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.**

## 1. Scope and the source being audited

This is the GPT-2 source investigation following the endpoint package
at `6a16d90b551588572c87e622c21c2df7f7b1adc2`. It does not build a
new all-source endpoint Schur matrix at log(7)/2. It reconstructs
the specified near-null source by a separate integral calculation,
accounts for its entire infinite directional tail, and proves a
continuum statement about its transported family. The same author
performing a second calculation is not an independent external audit.

Let B=log(5)/2, C=log(7)/2, H=L2((-1,1),dx/2). Extract the 30
rational coefficients c_n, n=2,4,...,60, from `source_trials.even`
in the pinned `prime-power-segment-4-2026-09-18/segment_results.json`.
The source blob is `ec29897cd614fe1ee759aa97e791c40ac154c141`.
The checker embeds the complete coefficient list and the source JSON
SHA-256. It reads no external numeric data when run.

Write
\[
F(x)=\sum_{n=2,4,\ldots,60}c_n(1-x^2)P_n(x),\qquad\phi(x)=1-x^2,
\]
\[
\rho(a)=\frac{\langle F,\cosh(ax/2)\rangle}{\langle\phi,\cosh(ax/2)\rangle},
\qquad v_a=F-\rho(a)\phi.                                      (1)
\]
The denominator is at least <phi,1>=2/3. The original sum of
individually moment-corrected h_n is exactly (1), by linearity.
There is no new inverse iteration or reselection of the source here.
Its even degree is 62. F and phi vanish at both endpoints, so v_a
is a genuine H1_0 polynomial. Its cosh moment vanishes identically
by (1); its sinh moment vanishes by parity. Thus both original
Mellin conditions hold exactly, not just to a residual tolerance.

The physical source is u_a(t)=(2a)^(-1/2)v_a(t/a). The fixed-space
norm equals its physical L2 norm. JSON includes the rational
coefficients of F and the complete Legendre coefficient enclosures
of v_B, with the analytic definition (1) retaining exact moments.

Two different transports must be distinguished. Physical zero
extension of u_B to a larger window has identically constant norm
and energy by the exact family law. The nontrivial investigation
here instead uses (1): fixed reference polynomial F, with the
changing exact Mellin correction, then physical dilation by a.

## 2. Results and their quantifiers

The independent representation encloses the original Rayleigh
quotient, and the higher-precision run narrows it to
\[
3.296290826616004472\,10^{-12}
\le\frac{Q_W[u_B]}{\|u_B\|^2}
\le3.296290826616004499\,10^{-12}.                          (2)
\]
The outward displayed endpoints may be used with non-strict signs
without relying on decimal-rounding strictness.

The continuum transport certificate proves
\[
\boxed{\frac{Q_W[u_a]}{\|u_a\|^2}>10^{-12}
\quad(B\le a\le C),\quad u_a\text{ specifically defined by (1)}.} (3)
\]
It does **not** quantify over all sources in W_a at C. The certified
shape comparison on the same whole interval is
\[
\frac{|\langle v_a,v_B\rangle|^2}{\|v_a\|^2\|v_B\|^2}
>0.999984682052540116577737879770.                         (4)
\]
Channel 5 is exactly zero at B and makes a strictly negative
contribution to this family's energy at every B<a<=C. Therefore
it does not stabilize this particular transported direction.

Selected directed evaluations (not the continuum proof):

| a | Source Rayleigh quotient, approximately | Signed channel-5 contribution, approximately |
|---|---:|---:|
| log(5)/2 | 3.296290826616e-12 | 0 |
| 17/20 | 0.00233387156549029 | -2.350919300285e-8 |
| 9/10 | 0.00535258785475540 | -3.422631949351e-6 |
| 19/20 | 0.00562706797996733 | -7.310364684528e-5 |
| log(7)/2 | 0.00496577446096407 | -0.000209099519905866 |

The reference direction changes little while its energy changes
substantially. It ceases to be a near-null trial direction at the
larger windows. No monotonicity of its Rayleigh quotient is asserted.

## 3. The actual energy identity and the separate Schur estimate

Use the established nonpole family on the actual two-Mellin kernel:
\[
q_a=D_H+V+q_0(a)I-K_a-\sum_{q}w_qT_{\log(q)/a},
\quad V=-\tfrac12\log(1-x^2),\quad q_0=-\log(2\pi a)-\gamma.
\]
Here D_H P_n=H_n P_n, w_(p^k)=log(p)/sqrt(p^k), and K_a has
kernel 2a g(a|x-y|) against dy/2, with
g(t)=e^(-t/2)/(1-e^(-2t))-1/(2t).

The direct identity for the already admissible source is
\[
q_a[v_a]=\langle v_a,D_Hv_a\rangle+\langle v_a,Vv_a\rangle
+q_0\|v_a\|^2-\langle v_a,K_av_a\rangle
-\sum_qw_q\langle v_a,T_{\log(q)/a}v_a\rangle.             (5)
\]
There is no further Schur subtraction or moment-cost subtraction
in (5). The moment correction is already inside v_a. Schur
subtraction bounds a different quantity: the energy after allowing
an arbitrary tail to couple to the prescribed low coordinates.
Subtracting it again in (5) would double-count certificate losses.

At B the normalized pieces are approximately:

| Piece | Value |
|---|---:|
| Harmonic diagonal | +2.206390061987739229 |
| Logarithmic potential V | +0.055285747492470258 |
| Scalar q0 | -2.197830546078043656 |
| Regular Gamma kernel | -0.001437475893573129 |
| Channel 2 | -0.034635961662743115 |
| Channel 3 | -0.027752226688362499 |
| Channel 4 | -0.000019599154190799 |

The saved intervals, rather than these rounded display values,
certify the cancellation. The Gamma model remainder is paid as
an explicit interval of radius 2a epsilon in the final quotient.

## 4. Separate exact integration of the fixed source

The checker reconstructs monomial F and phi from the rational
coefficients. It evaluates the two-dimensional bilinear form on
span{F,phi} and substitutes (1); it imports no matrix, LDL factor,
source energy, or tail Gram from the old checker.

For r>=n with r-n even,
\[
\langle x^r,P_n\rangle=\frac{r!}{(r-n)!!(r+n+1)!!},        (6)
\]
and it is zero otherwise. This determines the harmonic energy and
the Legendre coordinates exactly. Ordinary polynomial products
are integrated as rational coefficients. With
O_j=sum_(k=0)^j1/(2k+1), Z_j=sum_(k=0)^j1/(2k+1)^2,
\[
\int_0^1x^{2j}Vdx=(O_j-\log2)/(2j+1),
\quad\int_0^1x^{2j}V^2dx=[(O_j-\log2)^2+Z_j-\pi^2/12]/(2j+1). (7)
\]

For p(2t-1)=sum b_r t^r, q(2t-1)=sum d_s t^s, direct integration
of both triangles of [0,1]^2 gives
\[
\langle p,\mathcal K_k q\rangle
=2^k\sum_{r,s}b_rd_s
\frac{r!k!/(r+k+1)!+s!k!/(s+k+1)!}{r+s+k+2},              (8)
\]
where Kcal_k has kernel |x-y|^k against dy/2. This is the direct
Gamma energy calculation; it does not use the old Legendre image
recurrence. For even p,q, write p(-1+t)=sum a_r t^r and
q(-1+t)=sum b_s t^s. The complete partial shift, including both
signed branches, has
\[
\langle p,T_dq\rangle
=\sum_{r,s}a_rb_s\frac{r!s!}{(r+s+1)!}(2-d)^{r+s+1}.      (9)
\]
This follows by x=-1+(2-d)t and parity, and works also for d<1.

For the independent tail calculation, polynomial images of Kcal_k
are also generated in monomial coordinates by f_p,1''=p and
f_p,k''=k(k-1)f_p,k-2, starting from f_p,0=<p,1>.
Their value and derivative at x=1 are beta integrals against
(1-y)^k and k(1-y)^(k-1). Two affine integration constants fix the
image. For both basis polynomials and all k=0,...,144, integration
of these images agrees exactly with (8): 435 rational identities.

## 5. Uniform Gamma remainder, moments, and precision

For x=t/2, g(t)=[sech x+(x/sinh x-1)/x]/4. Formal rational
inversion of cosh through M and sinh(x)/x through M+1 produces
p_M(x). Multiply each inverse polynomial by its denominator Taylor
polynomial through D=max(192,M+4), rounded up to an even degree.
The initial residual coefficients vanish exactly. On 0<=x<=1,
bound the remaining coefficients by their absolute sum. The omitted
denominator tail is at most
\[
\frac1{(D+2)!\,[1-1/((D+3)(D+4))]}
\]
for cosh, with (D+3)! for sinh(x)/x. Multiply by the inverse's
absolute coefficient sum. The division by x in the second residual
is removable; all remaining exponents are nonnegative. Both exact
denominators are >=1. Thus |g(t)-p_M(t/2)|<=epsilon_M on [0,2].
Schur's integral inequality gives ||K-Kp||<=2a epsilon_M.

The first run uses grid 10^-220 and M=112; the second uses grid
10^-300 and M=144. Both B and C enclosures strictly narrow in the
second run. Logarithms use respectively 384 and 512 atanh terms,
with geometric tails; pi uses the alternating Machin formula.
Gamma uses rational Euler-Maclaurin through B16 at N=10000,
with periodic Bernoulli polynomial bounded by its coefficient
absolute sum. These are reused arithmetic primitives, not an
independent implementation of transcendental interval arithmetic.

The cosh integrals in (1) are evaluated through degree 160. Each
coefficient integral is rational before evaluating a. The omitted
value and first two derivatives are bounded using the polynomial's
coefficient absolute sum and the factorial series tail. For
derivative order d<=2 and 0<a<=1 a valid tail bound is
\[
\|p\|_{\mathrm{coeff},1}\,2^{-d}
\frac{(1/2)^{162-d}}{(162-d)!\,[1-1/(4(163-d)(164-d))]}.    (10)
\]
The exact moment identity comes from (1); the tiny computed
residual interval is a consistency check, not its proof.

## 6. Entire infinite directional tail and every mixed shift term

At B fix v=v_B and O=V-Kp-S, S=w2T2+w3T3+w4T4. All these
images of v lie in H. Direct integration computes
\[
\|Ov\|^2=VV+KK+SS-2VK-2VS+2KS.                           (11)
\]
Here each symbol is the corresponding inner product. The shift
Gram is assembled separately from (9), by all signed support
intersections on the full interval:
\[
\langle T_dv,T_ev\rangle=\frac12\sum_{\sigma,\tau=\pm1}
\int_{I_\sigma(d)\cap I_\tau(e)}v(x+\sigma d)v(x+\tau e)dx,
\quad I_\sigma(d)=(-1,1)\cap(-1-\sigma d,1-\sigma d).      (12)
\]
All nine ordered q,r entries for q,r in {2,3,4} are saved. In
particular the two branches of T2 overlap; no T2²=I shortcut is
used. KK and KS are polynomial integrals. VV uses (7); VK and VS
use analytic logarithmic antiderivatives on every signed band.
For m=n+1, those antiderivatives are
\[
A_n^-=(x^m-1)\log(1-x)/m-\sum_{k=1}^m x^k/(mk),
\quad A_n^+=(x^m-(-1)^m)\log(1+x)/m
-\sum_{k=1}^m(-1)^{m-k}x^k/(mk).
\]
Their derivatives are x^n log(1-x) and x^n log(1+x).
Use -(A^-+A^+)/2, endpoint limits, and parity for negative arguments.
This differs from sampling a singular potential or truncating its
Legendre expansion.

For N=63,79,95, Parseval gives the complete mass
\[
g_N=\|P_{Y_N}Ov\|^2=\|Ov\|^2
-\sum_{0\le n\le N,\ n\ \mathrm{even}}(2n+1)|\langle P_n,Ov\rangle|^2. (13)
\]
Every omitted even mode is included by (13). Increasing N changes
only the low/tail split; it does not change the fixed source or
truncate it differently.

For comparison with the actual constrained Schur estimate, let
x=v-<v,1>1, so v is the exact Mellin reconstruction of x. Set
L=2B, n_*=N+1, and use the even moment-tail bound epsilon_m from
orthogonality to the cosh polynomial through degree n_*-2. With
e=2L epsilon_M+80 epsilon_m and tau=1/1000,
\[
\delta_N=H_{n_*}+q_0-L(1/4-g(L)+\epsilon_M)
-(\log2+\log3/\sqrt3+\log2/2)-e>0,                        (14)
\]
\[
g_N^{act}=(1001/1000)g_N+1001e^2\|x\|^2.
\]
The Gamma monotonicity on [0,2] and the chain-adjacency norm bound
are the same elementary inequalities used by the endpoint proof.
The checker verifies all scalar bounds for ||Qp E0||<9 and the
moment reconstruction. The directional actual Schur quadratic is
bounded below by qp[v]-e||x||²-g_N^act/delta_N.

| Cutoff N | Entire tail Gram / ||v||² | Schur deduction / ||v||² | Directional comparison lower / ||v||² |
|---|---:|---:|---:|
| 63 | 3.30936201036167144e-13 | 4.60445852750974530e-13 | >2.83584497386502992e-12 |
| 79 | 2.59367858318020181e-13 | 2.75894810893027178e-13 | >3.02039601572297728e-12 |
| 95 | 2.36756033733583720e-13 | 2.11163131343802077e-13 | >3.08512769527220238e-12 |

The first two columns are rounded displays; JSON has outward
enclosures. These are whole-tail directional calculations, not
an independent audit of every entry of the original Schur matrix.
They do not supply a new global inverse-shear bound. The exact
source norm is used in these quotients; the original all-source
certificate's final 1+beta division remains a separate norm bound.

## 7. Continuum transport and the sign of channel 5

Parameterize a=B+(C-B)t with rational t in [0,1]. On this segment
the active channels are 2,3,4,5, with channel 5 zero at t=0 and
channel 7 zero at t=1. Define
\[
F_*(a)=q_a^p[v_a]-(10^{-12}+2a\epsilon_{112})\|v_a\|^2.
\]
Directed second-order interval jets enclose its value and first
two derivatives, including the moment tails in (10). Shift
polynomials are translated exactly to rational centers before
evaluation. In a dyadic t-cell, let c be its a-midpoint and h an
upper bound on its a-radius. Taylor's theorem gives
\[
F_*(a)\ge F_*(c)_{lo}-|F_*'(c)|_{up}h
-\tfrac12\sup_{cell}|F_*''|h^2.                           (15)
\]
All 19 accepted cells have a strictly positive right side. Their
rational endpoints tile [0,1] exactly. This proves (3) on the
continuum; the five displayed points are not used for interpolation.

For channel 5 put u=2-log5/a. Both polynomials F and phi vanish
at -1, so each shift bilinear polynomial (9) is divisible by u³.
The checker factors this exactly and applies the same Taylor
certificate to
\[
P_5(a)=\langle v_a,T_{\log5/a}v_a\rangle/u^3,
\]
using its removable value at B. All 25 accepted cells are positive.
It follows that -w5 u³ P5(a) is strictly negative for B<a<=C,
and zero at B. This sign concerns this specified source family,
not the influence of channel 5 on every possible direction.

Finally, for the constant Gram matrix N of F,phi,
\[
1-\frac{|\langle v_a,v_B\rangle|^2}{\|v_a\|^2\|v_B\|^2}
=\frac{(\rho(a)-\rho(B))^2\det N}{\|v_a\|^2\|v_B\|^2}.    (16)
\]
A whole-interval enclosure of rho and positive norm bounds proves
(4), without sampling shapes or numerical eigenvectors.

## 8. Reproducibility, interpretation, and remaining obligation

The standard-library checker uses only integers and Fraction with
directed interval rounding. It stores rational interval endpoints,
the full source description, all energy pieces, every accepted
Taylor cell, all mixed shift entries, and the three full directional
tail calculations. `--verify` recomputes the report and log byte for
byte and verifies all five SHA-256 payload hashes. The manifest
does not hash itself. There is no quadrature, A1, third Mellin
condition, numerical eigenvalue proof, merge, or Registry change.

The near-null signal at B survives the separate representation,
higher precision, higher Gamma degree, and the full directional
tail calculation. Its transported version remains positive and
changes little in normalized reference shape, but its Rayleigh
quotient grows to order 10^-3. Channel 5 lowers its energy throughout
the new segment. These facts do not produce a nonpositive source
or evidence requiring a C15 freedom.

For a<=B, the preceding all-source theorem, if accepted, already
excludes a negative admissible source before channel 5 enters.
For B<a<=C this investigation proves positivity only for (1).
It neither excludes other negative directions nor proves a positive
minimum over the full two-Mellin class. The exact remaining endpoint
obligation is the positive actual constrained Schur complement on
all low directions with active set {2,3,4,5}, together with its
whole tail and final norm conversion, or another valid all-source
argument. Tracking a newly optimized near-null direction is also
distinct from following this fixed source family.

The historical endpoint bound 10^-13 remains AUTHOR-DERIVED /
EXTERNAL-REVIEW-OPEN. This source audit does not promote it to
external verification. The unit window, a prime-independent global
positive reserve, C1-GEOM, Object X and RH remain open.
