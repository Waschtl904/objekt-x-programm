# A finite-channel segment theorem and the prime-power 4 endpoint

2026-09-18. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.**

## 1. Scope and source space

The fixed new endpoint is B=log(5)/2. Its active arithmetic channels
are q=2,3,4, with weights log(2)/sqrt(2), log(3)/sqrt(3), and
log(2)/2. Channel 5 has zero-measure overlap at B. We address the
whole segment [log(2),B], not a succession of points near log(2).

The physical source class remains
\[
\mathcal W_a=H^1_0((-a,a);\mathbb C)\cap\ker E_+\cap\ker E_-,
\qquad E_\pm u=\int_{-a}^a u(x)e^{\pm x/2}\,dx.
\]
There are exactly two global Mellin conditions. There is no A1,
additional moment, promotion to AUTHOR-VERIFIED, or claim of an
external audit. The imported connected nonpole identity is the same
corrected identity used in the preceding packages. This package
independently recomputes its endpoint matrices; it does not use the
previous endpoint's numerical gap as an assumption.

The endpoint certificate is CLOSED at author level and gives
\[
\boxed{Q_W[u]>10^{-13}\|u\|_2^2\quad(0<a\le\log(5)/2,\ 0\ne u\in\mathcal W_a).}
\]
The full reserve ledger is in Section 10.
The abstract result in Section 2 is conditional on its explicitly
listed bounds. Its architecture is independent of the labels of the
active prime powers; positivity of those bounds is not asserted for
all later segments.

## 2. A reusable finite-channel segment theorem

The concurrently deposited `active-set-segment-schur-2026-09-18`
package at `a18f90a867bfba2798068d5566a4e38a09013c01` states the
general active-set theorem but does not certify the log(5)/2
endpoint. The self-contained statement below specializes that
architecture and makes its hypotheses concrete at this endpoint.
The new numerical result does not change that package's review status.

Let b>0 and include every prime power q<exp(2b), with
w_q=Lambda(q)/sqrt(q), Lambda(p^k)=log(p). Put H=L2((-1,1),dmu),
dmu=dξ/2, U_a u(ξ)=sqrt(2a)u(aξ), E_n=sqrt(2n+1)P_n and
H_n=sum_(k=1)^n 1/k. The exact reference nonpole family is
\[
q_a=\operatorname{diag}(H_n)+V+q_0(a)I-K_a-S_a,
\quad V=-\tfrac12\log(1-\xi^2),\quad q_0=-\log(2\pi a)-\gamma,
\]
\[
K_af(\xi)=2a\int g(a|\xi-\eta|)f(\eta)d\mu(\eta),\quad
g(t)=\frac{e^{-t/2}}{1-e^{-2t}}-\frac1{2t},
\quad S_a=\sum_q w_qT_{\log(q)/a},
\]
where T_d f(ξ)=f(ξ+d)+f(ξ-d), with zero extension outside (-1,1).
Terms with d>=2 vanish. On the actual Mellin kernel this is Q_W.
The form domain is the harmonic diagonal form domain intersected
with L2(V dmu). It contains H1_0 and every polynomial. Finite
Legendre projections preserve it.

For each parity j=0,1, let X=E_j perpendicular, L0 the modes
j+2,...,N of that parity, and Y all higher modes. Define the actual
moment map M from X onto the corresponding Mellin kernel. Suppose
a bounded comparison error e>=0, a tail floor delta>0, a complete
model coupling Gram G, a finite moment matrix A0, and beta>=0 obey
\[
F=M^*q_bM=F^0+E,\quad\|E\|\le e,\quad D\succeq\delta I,
\quad (C^0)^*C^0=G,\quad\|Mx\|^2\le(1+\beta)\|x\|^2.
\]
Use unnormalized P_n coordinates and J_nn=1/(2n+1). For any tau>0,
\[
G_{\rm act}=(1+\tau)G+(1+1/\tau)e^2J\succeq C^*C.
\]
If a rational certificate proves
\[
R=A^0-eJ-G_{\rm act}/\delta\succeq\sigma J,\qquad\sigma>0,
\quad s^2\ge\delta^{-2}\operatorname{tr}(J^{-1}G_{\rm act}),
\]
then the actual infinite-dimensional Schur complement is >=sigma I.
Completing its square gives
\[
q_b[Mx]\ge\frac{\min(\sigma,\delta)}{(1+s)^2}\|x\|^2
\ge\frac{\min(\sigma,\delta)}{(1+s)^2(1+\beta)}\|Mx\|^2.       (1)
\]
The shear here is the actual D^-1 C: its norm is <=s, and the
inverse triangular change of variables has norm <=1+s. Thus no
comparison-operator shear is substituted for the actual shear.

If both parities satisfy these hypotheses with a common positive
epsilon strictly below their bounds in (1), then
\[
Q_W[u]>\epsilon\|u\|_2^2\quad(0<a\le b,\ 0\ne u\in\mathcal W_a). (2)
\]
The endpoint-to-interval implication is exact, as proved in Section 9.
This is the segment theorem: every active channel enters the same
Gram and the same sufficient criterion. It is not a claim that a
finite matrix alone represents the infinite operator, nor that
continuity alone preserves an L2 gap.

## 3. New channel geometry and a conservative infinite tail

Here L=2B=log(5), d_q=2log(q)/log(5). On the positive half interval
the breakpoints, in strictly certified order, are
\[
0<1-d_2<d_3-1<d_4-1<1.
\]
For 0<ξ<1-d2 BOTH signs of the Prime-2 shift are active. For the
next band only its negative shift is active; the negative shifts
of channels 3 and 4 enter successively at d3-1 and d4-1.
This accounts for the new central overlap, including two-step
Prime-2 edges of physical length log(4). In particular T2^2=I is
not used at this endpoint.

Disintegrate the interval into chains modulo log(q). If m is the
smallest integer such that q^m>=5, there are at most m vertices
almost everywhere in each chain. Its shift is path adjacency.
For m=1,2,3, bounds are 0,1,sqrt(2); for larger m, 2 suffices.
Consequently
\[
\|S\|\le\sqrt2w_2+w_3+w_4
=\log2+\log3/\sqrt3+\log2/2.                              (3)
\]
Weights use the base prime, not log(q), so w4 is log2/2.

For 0<t<=2, write z=t/2. The elementary Taylor bound
sinh(z)/z<=1+(10/57)z² for z<=1 implies
(sinh(z)/z)²<cosh(z). Hence
g'(t)=[z^-2-csch(z)coth(z)-sech(z)tanh(z)]/8<0.
The checker also verifies g(L)>0. Thus g(L)<=g(t)<=1/4 on [0,L].

If |g(t)-p(t/2)|<=epsilon and Kp has kernel Lp(B|ξ-η|/2),
the constant kernel 1/4 annihilates Y, and V>=0. The actual tail
after the complete moment reconstruction therefore has the floor
\[
\delta=H_{n_*}+q_0-L(1/4-g(L)+\epsilon)-\|S\|_{\rm bound}-e, (4)
\]
where n_* is the first omitted degree. This bound is conservative
on the entire infinite tail, including every arithmetic channel.

## 4. Uniform Gamma model and exact polynomial integration

For x=t/2,
\[
g(t)=\tfrac14[\operatorname{sech}x+(x/\sinh x-1)/x].
\]
Formal inversion of cosh through degree M and sinh(x)/x through
degree M+1 gives a rational polynomial p of degree M=64. Multiply
the inverse polynomials by the corresponding denominator Taylor
polynomials through degree 128. The initial residual coefficients
vanish exactly. Bound all remaining coefficients absolutely at
xmax=5/6. The denominator tails start at power 130 and are bounded
by x^130/[130!(1-x²)] and x^130/[131!(1-x²)]. Multiply by the
inverse polynomial's absolute coefficient norm; in the second
residual lower powers by one for division by x. Both exact
denominators are >=1. This proves a rational uniform epsilon
on 0<=t<=5/3, covering L=log5. It follows that ||q-qp||<=L epsilon
as a bounded form difference. No sampled integrals are used.

The polynomial Gamma image is computed directly in Legendre
coordinates. Let f_jk(x)=(1/2) integral_-1^1 |x-y|^k P_j(y)dy.
For k=0 it is delta_j0 P0; f_j1''=Pj; for k>=2,
f_jk''=k(k-1)f_j,k-2. Legendre antiderivatives use
integral P0=P1 and integral Pn=(P_(n+1)-P_(n-1))/(2n+1).
The two integration constants are fixed by the exact beta values
\[
f_{jk}(1)=\frac{2^k(-1)^j(k!)^2}{(k-j)!(k+j+1)!},\quad
f'_{jk}(1)=\frac{k2^{k-1}(-1)^j((k-1)!)^2}{(k-1-j)!(k+j)!}, (5)
\]
each zero when its factorial index is negative. The resulting
degree is at most j+k+1. Thus the Kp image of Pj has no coefficient
above j+M+1; the resulting finite support is exact, not a tail cut.
The checker uses these rational recurrences before any interval
evaluation of the endpoint. Its matrix normalization is
<Pi,Kcal_k Pj>=coefficient_i(f_jk)/(2i+1).

## 5. Analytic shift bands and all mixed signs

Write V_ij=<Pi,V Pj>, W_ij=<Pi,V²Pj>, K_ij=<Pi,Kp Pj>,
S_ij=<Pi,S Pj>, A^S_ij=<S Pi,S Pj>, and B^S_ij=<V Pi,S Pj>.
For O_r=sum_(k=0)^r1/(2k+1), Z_r=sum_(k=0)^r1/(2k+1)²,
\[
\int_0^1x^{2r}Vdx=(O_r-\log2)/(2r+1),
\quad\int_0^1x^{2r}V^2dx=[(O_r-\log2)^2+Z_r-\pi^2/12]/(2r+1). (6)
\]
Expansion of PiPj gives the entries. The exact off-diagonal
identity V_ij=1/[|j-i|(i+j+1)] for distinct same-parity i,j is
used to avoid high-degree cancellation; opposite-parity entries
vanish. This identity also follows by expanding the Legendre
polynomials in the first formula of (6), where the log2 term
cancels by orthogonality.

For a direct derivation, take j>i of the same parity and apply the
Legendre Sturm-Liouville equation to the integral with log(1-x).
Integration by parts gives
(j(j+1)-i(i+1)) integral_-1^1 log(1-x) Pi Pj dx
= -integral_-1^1 (1+x)(Pi Pj'-Pj Pi') dx = -2.
The logarithmic boundary term vanishes since (1-x²)log(1-x)
tends to zero. Orthogonality kills the lower-degree terms in the
last integral, leaving the endpoint term 2. Parity then converts
this identity to the stated V_ij formula with measure dx/2.

For a shift 0<d<2 and same parity,
\[
T_{d,ij}=(-1)^j\sum_{r,s}a_{ir}a_{js}
\frac{r!s!}{(r+s+1)!}(2-d)^{r+s+1},\qquad
a_{nr}=\frac{(-1)^{n+r}(n+r)!}{2^r(r!)^2(n-r)!}.           (7)
\]
This beta-integral formula remains valid when d<1.

The band engine collects every endpoint of every signed shift
on [0,1] and certifies their order and the active shifts on each
open cell. On a cell it forms the FULL polynomial
A_j(x)=sum_(active signed shifts s) w_q Pj(x+s), then integrates
A_i A_j and Pi A_j V. Same-parity products are even, so integration
over [0,1] equals integration against dmu on [-1,1]. Summation
BEFORE multiplication includes every ordered pair of channels,
both signs of each shift, their overlapping supports, and their
weights. There is no orthogonality assumption between channels.

Ordinary moments are (h^(n+1)-l^(n+1))/(n+1). For the V moments,
set m=n+1 and, for 0<=b<1,
\[
F_n^-=[H_m-\sum_{k=1}^m b^k/k-(1-b^m)\log(1-b)]/m,
\]
\[
F_n^+=[(1-(-1)^m)\log2-\sum_{k=1}^m(-1)^{m-k}/k
-(b^m-(-1)^m)\log(1+b)+\sum_{k=1}^m(-1)^{m-k}b^k/k]/m.
\]
Then M_n(b)=integral_b^1 x^n V dx=(F_n^- -F_n^+)/2,
and M_n(1)=0 exactly. A band uses M_n(l)-M_n(h).
Integration by parts proves these expressions, including the
integrable singular endpoint. Quadrature plays no role.

Let Z contain all same-parity modes <=N, including j=0 or 1,
and Y EVERY higher mode. Parseval yields the compact full Gram
\[
\begin{aligned}
E^C_{il}={}&W_{il}+A^S_{il}-B^S_{il}-B^S_{li}\\
&-\sum_{k\in Z}(2k+1)(V_{ik}-S_{ik})(V_{kl}-S_{kl})\\
&+\sum_{N<k\le N+M+1}(2k+1)
[K_{ik}K_{kl}-(V_{ik}-S_{ik})K_{kl}-K_{ik}(V_{kl}-S_{kl})]. (8)
\end{aligned}
\]
It is EXACTLY <P_Y(V-Kp-S)Pi,P_Y(V-Kp-S)Pl>.
The K upper limit is exact by (5); V and S have full infinite
tails in W, A^S, and B^S. Expanding (8) gives the signs
VV+KK+SS-VK-KV-VS-SV+KS+SK. Thus every mixed sign required by
the combined operator V-Kp-S is included before estimating it.

## 6. Actual Mellin reconstruction, including the omitted infinite part

Use m=cosh(Bξ/2), j=0, or m=sinh(Bξ/2), j=1. On X=E_j perp,
M x=x-<x,m>/<E_j,m> E_j. Its exact finite images are
v_n=Pn-r_nPj with r_n=<Pn,m>/<Pj,m>. The Taylor series through
degree 100 or 101, plus the next-term geometric remainder and
|Pn|<=1, rigorously encloses these exact ratios.

The global norm bounds are
\[
\beta_0=[(B/2)^2/(2(1-(B/2)^2/12))]^2,
\qquad\beta_1=[(B/2)^2/(6(1-(B/2)^2/20))]^2.              (9)
\]
Subtract 1 from cosh for the even estimate, and (B/2)ξ from sinh
for the odd one; the denominators are >=1 and B/(2sqrt3).
Thus ||Mx||²<= (1+beta_j)||x||². This applies to the whole X,
not only the finite coordinates.

Let M0 equal M on L0 and the identity on Y. Orthogonality to
the Taylor polynomial of degree n_*-2 gives
\[
\|M-M^0\|\le\epsilon_m=
\frac{(B/2)^{n_*}}{n_*!\,[1-(B/2)^2/((n_*+1)(n_*+2))]}
\begin{cases}1&j=0,\\4/B&j=1.\end{cases}                 (10)
\]
The checker verifies beta<1, epsilon_m<1, and ||Qp E_j||<9:
the diagonal scalar is <4, ||VEj||<2 by (6), ||Kp||<1,
and ||S||<2 by (3). The rank-one change M-M0 costs less than
45 epsilon_m; use 80 epsilon_m conservatively. Together with
||M||²<2 and the Gamma error this proves
\[
\|M^*qM-(M^0)^*q^pM^0\|\le e=2L\epsilon+80\epsilon_m.    (11)
\]
The finite A0 is q^p[v_i,v_j]. Applying the same congruence to
BOTH indices of (8) gives the entire model coupling Gram G.
The finite moment correction is paid exactly in A0 and G; the
omitted infinite moment contribution is paid in (11).
No additional beta K subtraction is missing. The entire final
coercive numerator in (1) is divided by 1+beta.

## 7. Directed Schur bounds and the reserve ledger

The certificate sets tau=1/1000. Every matrix entry and LDL
pivot is a directed rational interval. If R=LDL* has strictly
positive interval pivots, it is positive definite. Rather than
hard-code a tiny target floor, compute
\[
T=\operatorname{tr}(J R^{-1}),\qquad\sigma=1/T_{\rm upper}. (12)
\]
For the normalized positive matrix J^-1/2 R J^-1/2, the largest
inverse eigenvalue is at most the trace of the inverse; (12)
therefore gives a certified lower bound, without a numerical
eigensolver. The inverse trace is evaluated via triangular
solves using the interval factors. The same procedure on A0
records its finite moment-block reserve.

The ledger records delta; tr(J^-1 Gact), hence an operator upper
bound tr(J^-1 Gact)/delta on the entire Schur deduction; sigma;
the actual shear bound; both terms in (11); beta; and the final
bound in (1). It also records the squared Hilbert-Schmidt norm
upper bound of the ENTIRE finite moment correction A0-Q|L0,
with normalized basis factors (2i+1)(2j+1). This is a norm bound
on a signed correction, not an assertion that all of it is lost.

An upper bound on a deduction cannot simply be subtracted from
a separately reported inverse-trace lower bound to reproduce
sigma: the matrix computation retains the directional information.
Likewise, none of these lower bounds is an estimate of the optimal
source gap. Failure of a comparison LDL would be UNDECIDED for
the actual Weil form, not a negative Weil vector.

For an additional source-level upper diagnostic, put h_n=(1-ξ²)Pn
and psi_n=h_n-<h_n,m>/<h_j,m> h_j. These are genuine H1_0 sources
and obey the actual endpoint Mellin condition exactly. Their other
parity moment vanishes automatically. The checker selects rational
coefficients in this basis by four inverse iterations of the model
finite energy and norm matrices. This iteration is only a way to
choose a test function. The concluding evaluation is the directed
interval of qp[u]/||u||² plus [-L epsilon,L epsilon]. It encloses
the actual source Rayleigh quotient. The rational coefficients and
exact basis definition are stored in JSON. In particular its upper
endpoint is an upper bound on the optimal source coercivity; it
is not used as a positivity proof or a numerical eigenvalue claim.

## 8. Arithmetic and reproducibility

All proof decisions use Python integers/Fraction; interval endpoints
round outward to the grid 10^-200 Z. Exponential uses Taylor degree
256 and its positive geometric tail. atanh uses 256 terms with
x^513/[513(1-x²)] remainder after exact power-of-two log reduction.
atan uses 256 alternating terms and the next positive term. Machin's
identity encloses pi. Integer square root gives directed rational
radical enclosures. Displayed decimals round outward to 24 places;
smaller quantities retain exact rational endpoints in JSON.

Euler-Maclaurin for gamma uses N=10000 and Bernoulli numbers
through B16, generated by their rational recursion. The center is
H_N-log N-1/(2N)+sum_(k=1)^8 B_(2k)/(2k N^(2k)). The periodic
B16 polynomial on [0,1] is bounded by its coefficient l1 norm
C16=sum_(k=0)^16 |binom(16,k)Bk|. The integral remainder is
at most C16/(16 N^16). No digits of gamma are imported.

The checker is self-contained and has no nonstandard dependency.
`--write` generates JSON, log, and five SHA-256 payload hashes.
`--verify` recomputes the whole certificate, requires byte-identical
JSON/log, and checks every payload hash. SHA256SUMS does not hash
itself. Scratch algebra comparisons of (5) with direct beta sums
are implementation checks, not an external audit.

## 9. Exact continuation across every entrance

For 0<a<=b let
\[
J_{a,b}f(\xi)=\sqrt{b/a}\,f((b/a)\xi)1_{|\xi|<a/b}.
\]
This is an isometry and J_bc J_ab=J_ac. In physical coordinates
it is ordinary zero extension. An H1_0 source has zero endpoint
trace, so this extension is still H1_0. Direct substitution gives
M_(b,plus/minus)(J_ab f)=sqrt(a/b) M_(a,plus/minus)(f).
Thus the two actual moment conditions are preserved exactly.

For every shift log(q), physical correlation of the zero-extended
source is unchanged. If log(q)>=2a, it vanishes by disjoint support,
including equality. The Gamma difference energy added outside the
smaller interval exactly replaces its removed leakage. Equivalently
both expressions are the same full-line connected nonpole form.
Consequently q_b[J_ab f]=q_a[f] exactly. Applying the endpoint bound
and the isometry proves (2) for every smaller window at once.

No dense parameter grid, local crossing, or small-L2-norm assumption
at a channel entrance is used. Shrinking overlap does not make a
partial translation small in L2 operator norm. The moment and shear
costs are paid at the endpoint, then the exact source identity
transfers the result.

## 10. Outcome, provenance, and remaining obligations

The calculation began from `213edfd33d77b57c7ca272696be41339bf703f67`.
The publication base is `28351975097ed024ffa6a65145bc4a4d9b63d827`
on PR #137, preserving both intervening structural packages unchanged:
the active-set theorem at `a18f90a8...` and the universal prime-power
family at `28351975...`. Neither supplied this new endpoint reserve.
The package is append-only: proof, checker, log, JSON,
README, SHA256SUMS. Historical packages are not edited. The PR
remains open, draft, and unmerged. Main and Registry are unchanged.

The preceding gaps 10^-5 and 10^-11 arose from imposed Schur
floors 10^-4 and 10^-9, respective inverse-shear bounds 3 and 5,
the final beta division, and conservative decimal rounding.
Their ratio therefore does NOT measure a six-order loss of the
optimal geometry. The present ledger replaces those chosen floors
by (12). No conclusion about the actual change in the optimal
coercivity is inferred without comparable sharp bounds.

Even a successful endpoint here would not close a=1, the later
Prime-5/Prime-7 segments, a canonical reserve uniform over all
prime-power segments, C1-GEOM, Object X, or RH. The reusable
conditional segment theorem does not supply that missing global
positive reserve by itself. External review of this package and
its imported nonpole identity remains open.


### Certified endpoint result

The run uses N=63, 31 low modes per parity, tails starting at 64
and 65, and the degree-64 Gamma model. Both actual Schur complements
close. The published strict interval gap is **1/10^13**.

All entries below are outward decimal enclosures of certified
bounds, not interval enclosures of unknown optimal eigenvalues.
The trial row alone encloses the Rayleigh quotient of a particular
actual H1_0, two-Mellin source.

| Quantity | Even | Odd |
|---|---:|---:|
| Infinite-tail floor | 0.719448628450052179181039 to 0.719448628450052179181040 | 0.734833243834667563796423 to 0.734833243834667563796424 |
| Finite exact-Mellin block lower bound | 0.000000000003210487628048 to 0.000000000003210487628049 | 0.000000000638329082611597 to 0.000000000638329082611598 |
| Entire coupling squared HS bound | 8.093223555830155071955095 to 8.093223555830155071955096 | 8.040847556496107838762262 to 8.040847556496107838762263 |
| Schur deduction operator upper bound | 11.249202841995588347783244 to 11.249202841995588347783245 | 10.942411253110431336419555 to 10.942411253110431336419556 |
| Actual Schur inverse-trace lower bound | 0.000000000002575698126263 to 0.000000000002575698126264 | 0.000000000563052798223254 to 0.000000000563052798223255 |
| Inverse shear norm squared upper bound | 24.544315625284000000000000 to 24.544315625284000000000000 | 23.608792596544000000000000 to 23.608792596544000000000000 |
| Finite Mellin correction squared HS upper bound | 0.000155343703236469224539 to 0.000155343703236469224540 | 0.000018303837147917943675 to 0.000018303837147917943676 |
| Gamma form-error upper bound | 0.000000000000000000739601 to 0.000000000000000000739602 | 0.000000000000000000739601 to 0.000000000000000000739602 |
| Infinite Mellin form-error upper bound | 0.000000000000000000000000 to 0.000000000000000000000001 | 0.000000000000000000000000 to 0.000000000000000000000001 |
| Global Mellin beta | 0.006732787914843592696178 to 0.006732787914843592696179 | 0.000739969782224899503368 to 0.000739969782224899503369 |
| Back-transformed lower bound | 0.000000000000104940718885 to 0.000000000000104940718886 | 0.000000000023849283944562 to 0.000000000023849283944563 |
| Final source lower bound, after division | 0.000000000000104238900475 to 0.000000000000104238900476 | 0.000000000023831649244260 to 0.000000000023831649244261 |
| Actual source trial Rayleigh quotient | 0.000000000003296290456815 to 0.000000000003296291196417 | 0.000000000665105252693155 to 0.000000000665105253432757 |

The sub-10^-24 moment remainder displays as a zero lower decimal
and a 10^-24 upper decimal; JSON retains the exact nonzero rational
enclosure. It is included in every affected bound.

This ledger locates the small scale already in the endpoint source
geometry: the explicit even source trial has the displayed tiny
positive Rayleigh quotient, so arbitrarily large improvements to
the final gap are impossible at this endpoint. The Schur comparison
reduces the reported finite reserve, the inverse shear costs a factor
below 25, and the final beta division costs less than one percent.
The finite Mellin correction is signed and incorporated jointly;
its coarse norm must not be subtracted again from the tiny reserve.
These observations do not quantify the change from the preceding
endpoint's *optimal* gap, which that package did not determine.

The exploratory cutoff N=47 had positive tail floors above 0.434
and 0.454 but did not close the comparison Schur test. Increasing
the modal resolution to 63 at the same fixed endpoint closes it.
No intermediate a-value, local crossing search, or weakening of
the source class was used to obtain the result.

The deterministic certificate contains 15 check groups and 62 strictly positive Schur LDL pivots.
