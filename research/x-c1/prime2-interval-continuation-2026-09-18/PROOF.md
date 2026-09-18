# Prime-2 interval continuation on the complete connected NULLPOL class

2026-09-18. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.**

## 1. Statement and change of research unit

Let
\[
A=\tfrac12\log3,\qquad
\mathcal W_a=H^1_0((-a,a);\mathbb C)\cap\ker E_+\cap\ker E_-,
\quad E_\pm u=\int_{-a}^a u(x)e^{\pm x/2}\,dx.
\]
The result is the interval theorem
\[
\boxed{Q_W[u]>\frac1{100000}\|u\|_2^2
\quad(0<a\le A,\ 0\ne u\in\mathcal W_a).}                 \tag{1}
\]
The endpoint is the exact number log(3)/2, not a decimal substitute.
Prime 3 has zero overlap at this endpoint. No prime beyond Prime 2 has
nonzero overlap anywhere in this interval.

The new ingredients are an exact common-space recombination of the entire
Node and Gamma terms, direct elimination of the two actual Mellin moments,
complete infinite-tail Gram identities, and an exact window continuation
law. There is no optimization of the former scalar splits (s, theta, z),
no search for a local crossing, and no claim that a failed lower comparison
is a loss of coercivity of the actual form.

The checker proves a positive **actual infinite-dimensional** Schur
complement in each parity, a bound on its actual shear, and the final
source-norm division. Its 15 by 15 finite blocks are accompanied by the
entire infinite tails; a finite-section eigenvalue is not the proof.

## 2. The full operator family on a common reference space

Put dmu=dξ/2 on (-1,1), H=L2(dmu), and use the unitary map
\[
(U_a u)(\xi)=\sqrt{2a}\,u(a\xi).
\]
Write ell=log2, w=ell/sqrt2,
\[
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad g(t)=h(t)-\frac1{2t},
\quad H_\Gamma(s)=\int_s^\infty h(t)dt,
\quad \kappa=\log(8\pi)+\gamma+\pi/2.
\]
We use the connected-edge identity of the corrected anchor
`9aa5cb1edac72fc683c5c9aba5a1f0639fbbf8bb`:
\[
q_a[f]=2a\int_{\xi<\eta}h(a(\eta-\xi))|f(\eta)-f(\xi)|^2d\mu\,d\mu
+\int[H_\Gamma(a(1+\xi))+H_\Gamma(a(1-\xi))-\kappa]|f|^2d\mu
-w\langle f,T_af\rangle.                                  \tag{2}
\]
Here d_a=ell/a and
\[
(T_af)(\xi)=f(\xi+d_a)1_{\xi+d_a<1}
             +f(\xi-d_a)1_{\xi-d_a>-1},
\]
with all functions zero outside (-1,1). On our macroscopic interval
[3/8,A], 1<d_a<2. Thus T_a is self-adjoint, ||T_a||<=1, and
T_a squared is multiplication by the two active endpoint bands.
Formula (2) equals Q_W on the two-Mellin kernel. Its off-kernel use below
is the explicitly defined nonpole form, not an assertion that the pole
term vanishes off that kernel.

For comparison with the earlier notation, L=2a and c_a=g(L) give
\[
F_a=F_{\mathrm{diag},a}+R_{\mathrm{node},a}+R_{\Gamma,a}+R_{2,a},
\]
where the diagonal eigenvalues are -C_a on E_0 and
H_n+Lc_a-C_a on E_n, n>=1, with E_n=sqrt(2n+1)P_n. Here
\[
C_a=\max\{\kappa-2H_\Gamma(a),\
\kappa+w-H_\Gamma(2a-\ell)-H_\Gamma(\ell)\},
\]
R_node is multiplication by rho_a+C_a, R_Gamma is the entire difference
form with kernel g(t)-c_a, and R_2 is the entire Prime-2 difference form.
These three remainders are nonnegative. This definition is used only for
a in [3/8,A], where both candidate minima have their stated geometry.
Both the center and endpoint-band floor branches are included.

To see g'<0 for 0<t<=6/5, put z=t/2<=1. The positive Taylor series gives
sinh(z)/z <= 1+(10/57)z^2. Squaring yields
(sinh(z)/z)^2 <= 1+(1240/3249)z^2 < cosh(z). Consequently
\[
g'(t)=\tfrac18[z^{-2}-\operatorname{csch}z\operatorname{coth}z
                        -\operatorname{sech}z\tanh z]<0.
\]
In particular c_a<=g(t)<=1/4 on 0<=t<=L.

## 3. Exact recombination: the full logarithmic Node potential

Define
\[
V(\xi)=-\tfrac12\log(1-\xi^2),\qquad
(K_af)(\xi)=2a\int g(a|\xi-\eta|)f(\eta)d\mu(\eta).
\]
The singular difference operator is diagonal with eigenvalues
H_n=sum_{j=1}^n 1/j, H_0=0. Expanding only the **bounded regular**
difference kernel and combining its degree with the Node leakage gives
the exact identity
\[
\boxed{q_a=\operatorname{diag}(H_n)+V+q_0(a)I-K_a-wT_a,
\qquad q_0(a)=-\log(2\pi a)-\gamma.}                         \tag{3}
\]
Indeed the regular degree plus the regular leakage is the constant
B(a)=2H_Gamma(a)+2 integral_0^a g(t)dt. Its derivative is -1/a.
The limit 2H_Gamma(s)+log s -> log4+pi/2 as s decreases to zero gives
B(a)=log(4/a)+pi/2 and B(a)-kappa=q_0(a). The singular leakage is V.
Thus (3) retains the entire nonconstant Gamma remainder and the entire
Prime-2 difference energy together with the entire Node potential;
the apparently signed pieces in (3) are an exact regrouping of (2).

The common closed-form domain is the intersection of the harmonic
diagonal form domain with L2(V dmu). The remaining operators in (3) are
bounded and self-adjoint. Polynomials lie in this domain, and H1_0 lies
in it as well. The singular integral operator has the complete Legendre
eigenbasis: direct polynomial integration gives H_n P_n, and its
nonnegative closed form is the corresponding harmonic diagonal form.
Finite-rank projections onto Legendre polynomials preserve the domain.
All subsequent Schur arguments are form-domain arguments on this
infinite-dimensional space. Auxiliary polynomials need not vanish at
the endpoints; this does not enlarge the asserted source class in (1).

## 4. Continuity and the moving two-Mellin kernel

For a,b in [3/8,A], the checker and the estimates below give
\[
|q_a[f]-q_b[f]|\le8|a-b|\bigl(\|f\|_H^2+\|f'\|_H^2\bigr),
\qquad f\in H^1_0(-1,1).                                  \tag{4}
\]
The diagonal and V in (3) do not vary. The derivative of q_0 has
absolute value <=8/3. The derivative of the kernel 2a g(a|ξ-η|) is
2[g(t)+tg'(t)]. Twelve rational interval cells covering [0,6/5], with
analytic series remainder bounds, certify |g+tg'|<1. Schur's integral
bound therefore gives ||K_a-K_b||<=2|a-b|.

For the zero extension of f in H1_0, translation satisfies
||tau_d f-tau_e f||<=|d-e| ||f'||. Consequently the Prime-2 contribution
varies by at most
\[
\frac{w\ell}{(3/8)^2}|a-b|(\|f\|^2+\|f'\|^2)
<\frac{112}{45}|a-b|\|f\|_{H^1}^2.
\]
The sum 8/3+2+112/45 is less than 8. We do **not** claim operator-norm
continuity of translation on L2.

The two constraints on the reference space are exactly
\[
\langle f,\cosh(a\xi/2)\rangle=0,\qquad
\langle f,\sinh(a\xi/2)\rangle=0.                          \tag{5}
\]
If a literally fixed constrained coordinate space is wanted, take
X=H1_0 intersect ker<.,1> intersect ker<.,ξ>,
phi_e=1-ξ^2, phi_o=ξ(1-ξ^2), and set
\[
P_af=f-\frac{\langle f,\cosh(a\xi/2)\rangle}
                   {\langle\phi_e,\cosh(a\xi/2)\rangle}\phi_e
       -\frac{\langle f,\sinh(a\xi/2)\rangle}
                   {\langle\phi_o,\sinh(a\xi/2)\rangle}\phi_o.
\]
The denominators are at least 2/3 and a/15 respectively. Parity kills
the crossed moments. P_a:X -> ker(5) in H1_0 is an isomorphism, with
inverse the projection P_0 along span{phi_e,phi_o} using moments 1,ξ.
Its coefficients and their derivatives are uniformly bounded on
[3/8,A], so q_a[P_a f] is a Lipschitz family on the fixed space X by
(4) and boundedness of q_a on H1_0. These are coordinates for the two
physical constraints; they impose no third condition.

## 5. A uniform rational approximation to the regular Gamma kernel

All computations below occur at a=A, L=log3. Let x=t/2. The identity
\[
g(t)=\tfrac14[\operatorname{sech}x+(x/\sinh x-1)/x]
\]
defines the polynomial p(x) of degree 16 used by the checker: take the
formal inverse of cosh through degree 16 and of sinh(x)/x through
degree 17, subtract 1 from the second, divide by x, add, and divide
by 4. Every coefficient is rational.

This is accompanied by a uniform error, not a sampled approximation.
Multiply each inverse polynomial by its denominator series through
degree 62. The residual coefficients through the order of the inverse
polynomial vanish exactly. On 0<=x<=3/5, bound the remaining finite
coefficients by their absolute values times (3/5)^k. Bound the positive
denominator-series tail starting at degree 64 by
(3/5)^64/[63!(1-(3/5)^2)] for cosh and the still conservative 64!
version for sinh(x)/x. Multiply by the absolute coefficient norm of
the inverse polynomial. Divide the second residual by x, lowering
each exponent by one; its constant and lower coefficients vanish.
The exact denominator is at least one in both cases. The resulting
rational epsilon satisfies
\[
|g(t)-p(t/2)|\le\epsilon<10^{-8}\qquad(0\le t\le6/5).       \tag{6}
\]
It is about 9.867 times 10^-9, enclosed outwards in the saved log.

Let K^p have kernel L p(a|ξ-η|/2), and set
q^p=diag(H_n)+V+q_0 I-K^p-wT. Schur's integral bound gives
\[
\|q-q^p\|_{\mathrm{bounded\ difference}}\le L\epsilon.     \tag{7}
\]
No Gamma or spatial integral is evaluated by quadrature.

## 6. Exact finite integrals and the entire tail Gram

We use the unnormalized P_n basis, whose Gram matrix is
J_nn=1/(2n+1). No square roots of basis norms enter the matrix arithmetic.
Write V_ij=<P_i,V P_j>, W_ij=<P_i,V^2 P_j>,
K_ij=<P_i,K^p P_j>, T_ij=<P_i,T P_j>.

All V and W entries reduce to the two exact moments
\[
\int_0^1 x^{2r}V(x)dx=\frac{O_r-\log2}{2r+1},
\]
\[
\int_0^1 x^{2r}V(x)^2dx=
\frac{(O_r-\log2)^2+S_r-\pi^2/12}{2r+1},                 \tag{8}
\]
where O_r=sum_{j=0}^r 1/(2j+1), S_r=sum_{j=0}^r 1/(2j+1)^2.
For example, these follow by differentiating
integral_0^1 x^(2r)(1-x^2)^s dx = B(r+1/2,s+1)/2 twice at s=0;
the half-integer recurrence cancels to the displayed finite sums.
The logarithmic singularity is integrated analytically and retained.

For K entries, write v=(ξ+1)/2 and
P_n(2v-1)=sum_l b_nl v^l, where
b_nl=(-1)^(n+l)(n+l)!/[(l!)^2(n-l)!]. Then
\[
\int |\xi-\eta|^kP_n(\eta)d\mu(\eta)
=2^k\sum_l b_{nl}\left[
\frac{l!k!}{(l+k+1)!}v^{l+k+1}
+\sum_{h=0}^l\binom lh\frac{v^{l-h}(1-v)^{k+h+1}}{k+h+1}\right]. \tag{9}
\]
This is a polynomial of degree at most n+k+1. Integrate its product
with P_i(2v-1) exactly. Symmetry and orthogonality justify zero entries
when max(i,j)>min(i,j)+k+1; for even k the kernel is a polynomial in
both variables and the entry also vanishes when max(i,j)>k.

Put d=2ell/L, u=2-d, b=1-u. For i,j of the same parity,
\[
T_{ij}=(-1)^j\sum_{k=0}^i\sum_{l=0}^j
 a_{ik}a_{jl}\frac{k!l!}{(k+l+1)!}u^{k+l+1},
\quad a_{nk}=\frac{(-1)^{n+k}(n+k)!}{2^k(k!)^2(n-k)!}.       \tag{10}
\]
This is the exact integral over the left shift band; reflection supplies
the other band and cancels the factor 1/2 in dmu. Further,
\[
A_{ij}:=\langle P_i,T^2P_j\rangle
=\frac{\delta_{ij}}{2i+1}-\int_{-b}^bP_iP_j\,d\mu.        \tag{11}
\]
The last integral is polynomial integration at the interval endpoint b.

Fix N=31. In each parity, let Z be all modes of that parity through N,
including its low mode j=0 or 1. Let Y contain **every** same-parity
mode above N. For B_op=V-K^p, Parseval and (9) give the exact identities
\[
\begin{aligned}
\mathcal E^B_{il}&=\langle P_YB_{op}P_i,P_YB_{op}P_l\rangle\\
&=W_{il}-\sum_{k\in Z}(2k+1)V_{ik}V_{kl}\\
&\quad+\sum_{N<k\le N+17\atop k\text{ same parity}}(2k+1)
 [K_{ik}K_{kl}-V_{ik}K_{kl}-K_{ik}V_{kl}],\\
\mathcal E^T_{il}&=\langle P_YTP_i,P_YTP_l\rangle
=A_{il}-\sum_{k\in Z}(2k+1)T_{ik}T_{kl}.                  \tag{12}
\end{aligned}
\]
The apparent finite sum in the K correction is exact because (9)
is polynomial. The V and T tails have **not** been truncated: (8),
(11), and Parseval evaluate their full squared norms. These Gram
identities are the conservative tail certificate.

## 7. The moment congruence and its quantified infinite remainder

In each parity put j=0 (even) or j=1 (odd), and m=cosh(aξ/2) or
sinh(aξ/2). On X_j=E_j perpendicular in that parity define
\[
V_mx=x-\frac{\langle x,m\rangle}{\langle E_j,m\rangle}E_j.
\]
This is onto the actual Mellin kernel in the larger form domain.
For the finite low block n=2,4,...,30 or n=3,5,...,31 use exactly
\[
v_n=P_n-r_nP_j,\qquad r_n=\frac{\langle P_n,m\rangle}{\langle P_j,m\rangle}.
                                                                    \tag{13}
\]
The moments are enclosed by their integrated positive Taylor series
through degree 60 (even) or 61 (odd). The remainder is bounded by
(a/2)^(last+2)/(last+2)! divided by
1-(a/2)^2/[(last+3)(last+4)], using |P_n|<=1. Both signs are allowed
for the remainder after pairing with P_n.

The global norm loss is exactly the usual two-moment estimate
\[
\|V_mx\|^2\le(1+\beta_j)\|x\|^2,
\quad
\beta_0=\left[\frac{(a/2)^2}{2(1-(a/2)^2/12)}\right]^2,
\quad
\beta_1=\left[\frac{(a/2)^2}{6(1-(a/2)^2/20)}\right]^2.    \tag{14}
\]
For even parity subtract 1 from cosh and use <E_0,cosh>>=1.
For odd parity subtract (a/2)ξ from sinh and use
<E_1,sinh>>=a/(2sqrt3). The remainders give (14) by Cauchy-Schwarz.
There is only one condition per parity.

For the model V_m^0, use (13) on the finite block and the identity
on Y. Let n_*=32 or 33 be its first tail degree. Orthogonality to the
Taylor polynomial of degree n_*-2 bounds
\[
\|V_m-V_m^0\|\le\epsilon_m,
\quad
\epsilon_m=\frac{(a/2)^{n_*}}{n_*!\,[1-(a/2)^2/((n_*+1)(n_*+2))]}
\begin{cases}1,&j=0,\\4/a,&j=1.\end{cases}                \tag{15}
\]
The factor 4/a is larger than 2sqrt3/a. This controls every omitted
moment coefficient, not just the first one.

The checker verifies beta_j<1 and ||Q^p E_j||<8: in (3) the diagonal
contribution has absolute value <4, ||V E_j||<2 by (8), ||K^p||<1,
and w||T||<1. Expanding the rank-one difference between the two moment
maps yields a bound <40 epsilon_m, conservatively replaced by
64 epsilon_m. Combining this with (7) and ||V_m||^2<2 gives
\[
F:=V_m^*qV_m=F^0+E,\quad F^0=(V_m^0)^*q^pV_m^0,
\qquad \|E\|\le e:=2L\epsilon+64\epsilon_m.              \tag{16}
\]
This is a bounded form difference even though the full form is unbounded:
Q^p E_j belongs to H. The finite entries already contain the entire
constant/linear-mode moment cost, including its sign and cross terms.
There is no further scalar beta K subtraction to omit or to count twice.
The remaining moment-tail subtraction is explicitly in e.

## 8. Actual infinite-dimensional pivot and actual full shear

Split X_j into its 15 low modes and Y. On Y, the constant part 1/4 of
the integral kernel annihilates every vector. From monotonicity of g
and (6), ||P_Y K^p P_Y||<=L(1/4-g(L)+epsilon). Since V>=0,
the **actual** tail D of F satisfies
\[
D\succeq\delta I,
\quad\delta=H_{n_*}+q_0-L(1/4-g(L)+\epsilon)-w-e>1.        \tag{17}
\]

Apply the change (13) to both indices of each Gram in (12), denoting
the resulting matrices by a superscript m. The coupling C^0 of F^0
has the operator quadratic bound
\[
(C^0)^*C^0\preceq G:=2(\mathcal E^{B,m}+w^2\mathcal E^{T,m}).
\]
This uses ||v-w||^2<=2||v||^2+2||w||^2 and retains both complete tails.
The actual coupling C differs in norm by at most e, by (16). With
tau=1/1000 the stronger required bound is
\[
C^*C\preceq G^{\rm act}:=\tfrac{1001}{1000}G+1001e^2J.   \tag{18}
\]
Here J is the diagonal Gram matrix of the unnormalized low basis.

Let M^0_ik=q^p[v_i,v_k], computed by (3), (8)--(10), and (13).
The actual Schur complement satisfies
\[
S=A-C^*D^{-1}C\succeq M^0-eJ-G^{\rm act}/\delta.
\]
The checker performs outward rational interval LDL factorization on
\[
M^0-eJ-G^{\rm act}/\delta-\tfrac1{10000}J.                \tag{19}
\]
All 15 pivots in each parity are strictly positive. Thus the actual
infinite-dimensional Schur complement S is greater than I/10000.
This conclusion is not based on a numerical eigenvalue calculation.

For the actual full shear, (17)--(18) give
\[
\|D^{-1}C\|^2\le
\delta^{-2}\sum_{n\text{ low}}(2n+1)G^{\rm act}_{nn}<4.    \tag{20}
\]
Completing the full square and bounding the inverse shear by
1+||D^{-1}C||<3 gives
\[
F[x]>\frac1{90000}\|x\|^2.
\]
Finally, and only after this positive gap is established, (14) gives
\[
\boxed{q[V_mx]>\frac{1/90000}{1+\beta_j}\|V_mx\|^2
>\frac1{100000}\|V_mx\|^2.}                              \tag{21}
\]
The whole back-transformed gap is divided by 1+beta_j. Reflection
commutes with all operators, so adding the parity estimates proves
(1) at a=A. The saved JSON distinguishes lower-bound expressions from
actual eigenvalues or exact optimal gaps.

## 9. Exact interval continuation and source compatibility

For 0<a<=b<=A define on the fixed reference space
\[
(J_{a,b}f)(\xi)=\sqrt{b/a}\,f((b/a)\xi)1_{|\xi|<a/b}.
\]
This is an isometry, J_b,c J_a,b=J_a,c, and
\[
M_{b,\pm}(J_{a,b}f)=\sqrt{a/b}\,M_{a,\pm}(f).
\]
It maps the H1_0 source with its two moments into the corresponding
larger source. In physical coordinates it is ordinary zero extension.
The exact identity is
\[
q_b[J_{a,b}f]=q_a[f].                                    \tag{22}
\]
For the Gamma part in (2), the newly internal edges with one zero
endpoint replace exactly the removed leakage integral. The Prime
correlation is unchanged by zero extension; equivalently its new
difference edges cancel its changed degree term. All nonsingular
cross-region integrals are nonnegative and Tonelli applies. The
singular difference energy of an H1_0 zero extension is finite.
The two pole moments remain zero.

Taking b=A transfers (21), with the same L2 norm, to **every** a in
(0,A]. This is the continuum certificate: one rigorously enclosed
endpoint and the exact identity (22) cover the whole macroscopic
interval, without unresolved gaps between a-grid boxes. The requested
Lipschitz control is separately supplied by (4); it is not being used
to extrapolate beyond a finite sampled grid.

After positivity has been proved, one may complete the sources in
their q_a norms. Polarization of (22) extends these source maps to
isometric maps of those completions, with the same composition law.
This is source/form-level canonical window compatibility. It does not
construct the requested global arithmetic-archimedean output geometry,
its individual channel readouts, or the C0-to-C1 intertwiner.

## 10. Arithmetic, reproducibility, and scope

`check_interval.py` is self-contained Python standard-library code.
All inputs, interval endpoints, decisions, polynomial integrals, LDL
operations, and displayed bounds use integers and Fraction. Each
interval operation rounds outwards to 10^-70 Z. No binary float,
quadrature, numerical eigensolver, or imported decimal enclosure is used.

Exponentials use Taylor degree 64 and the positive next-term geometric
tail. atanh uses 64 positive terms and x^129/[129(1-x^2)]; logarithms
are reduced by exact powers of two. atan uses 64 alternating terms
plus the next positive term. Machin's identity encloses pi. Integer
square root encloses sqrt2, with its two rational squares checked.
Euler's constant is enclosed by
H_10000-log(10000)-1/20000 plus [0,1/(8*10000^2)]: the convex trapezoid
error kernel is at most 1/8 and integral_N^infinity (1/x)'' dx=1/N^2.
The cancellation-free regular-g series, including derivative tails,
certifies the twelve Lipschitz cells. These are enclosures of analytic
functions on intervals, not spatial quadrature.

Run `python check_interval.py --verify` from any directory. The run
recomputes the entire certificate, requires byte-identical saved JSON
and log, and checks all five payload SHA-256 hashes. `--write` explicitly
regenerates them and the manifest. A default run writes nothing.
The manifest deliberately does not hash itself.

The mathematical anchor remains the corrected connected identity at
`9aa5cb1...`. Earlier full-residual and Gamma-Node deposits are preserved.
The live branch advanced independently to
`f18f7e496d8537615a480ed225e692f32a0f8207`, adding a separate dyadic
Gamma-waxing package; this deposit preserves that tree and imports no
numeric bound from it. Exactly this package's six files are added.

No A1 is imported. No third Mellin condition is imposed. No C15
necessity or architectural no-go is asserted. The phase of shifting
local scalar-certificate crossings is ended by the interval theorem.
The remaining macroscopic obligation starts beyond A, where Prime 3
becomes active. The unit window a=1, full C1-GEOM, the canonical global
channel geometry, Object X, and RH remain open. This is an author
derivation with reproducible arithmetic, not independent external review.
