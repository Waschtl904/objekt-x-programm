# Three-parameter Gamma-plus-Node envelope: a certified local crossing

Date: 2026-09-18. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.**
Continuation on PR #137 after `5de865932827d45aa119fa0e1b74eaab635624c8`.
This is a new method-class certificate, not a correction of an accepted
point certificate. Existing research files remain unchanged.

## 1. Result

For the Gamma-plus-Node lower estimate specified below, optimizing all
three variables \(s,\theta,z\), there is exactly one zero on
\[
I=[a_-,a_+],\qquad
a_-=\frac{3931224}{10^7},\qquad a_+=\frac{3931226}{10^7}.
\]
In particular
\[
\boxed{0.3931224<a_{\Gamma\text{-node}}<0.3931226.}
\tag{1}
\]
For every \(a\in I\), the global maximizer over the method's entire
admissible parameter domain is unique and belongs to the compact box
\[
\boxed{
\begin{aligned}
0.328025&\le s_*\le0.328825,\\
0.759267&\le\theta_*\le0.759667,\\
\frac{93547}{163840}&\le z_*\le\frac{187097}{327680}.
\end{aligned}}
\tag{2}
\]
The last interval lies inside \((0.570965576171,0.570974731446)\).
Every point of (2) is admissible, with a positive infinite-dimensional
tail. The optimized envelope is differentiable throughout \(I\), with
\[
-5.216461935993<G_{\Gamma\text{-node}}'(a)<-5.212359791482<-5.
\tag{3}
\]
The endpoint evidence is
\[
G_{\Gamma\text{-node}}(a_-)>0.000000481959>0,
\]
\[
G_{\Gamma\text{-node}}(a_+)<-0.000000560219<0.
\tag{4}
\]
The upper statement is a **global upper bound on the parameter
supremum**, not just a negative value at a tested triple. The odd gap
is greater than \(1/4\) throughout \(I\).

This is a unique crossing on the displayed interval. We do not claim
global monotonicity in \(a\), or the first zero on the entire
Prime-2-only domain. Prime-2 difference energy is not used in this
method-class envelope. The stronger joint-residual point certificate
at \(a=19651/50000\) is preserved and is not contradicted by (1).

## 2. Functions on the Prime-2-only domain

Let \(\ell=\log2\), \(w=\ell/\sqrt2\), \(L=2a\), and
\[
\ell/2<a<\log3/2,\quad
h(t)=\frac{e^{-t/2}}{1-e^{-2t}},\quad
g(t)=h(t)-\frac1{2t},\quad H(v)=\int_v^\infty h(t)\,dt,
\]
\[
\kappa=\log(8\pi)+\gamma+\pi/2.
\]
All exponentials and logarithms below have positive, nonsingular real
arguments on their stated open domains. At zero, \(g\) is understood
by its analytic continuation, with \(g(0)=1/4\).

A domain detail matters when extending the formulas beyond the accepted
point: the global Node floor must account for both the center and the
inner edge of an active endpoint band. Define
\[
C_0(a)=\kappa-2H(a),\qquad
C_2(a)=\kappa+w-H(L-\ell)-H(\ell),
\]
\[
C(a)=\max\{C_0(a),C_2(a)\},\qquad
m(a)=H(a+\ell/2)+H(a-\ell/2)-\kappa-w+C(a).
\tag{5}
\]
These formulas give the true global scalar floor and its outer-slab
surplus on the entire Prime-2-only domain. They are explicit and
piecewise analytic. No globally analytic claim is made at a possible
change of the maximizing branch in (5).

Indeed \(a<\ell\), the Prime-2 endpoint bands are disjoint, and
\(W(x)=H(a+x)+H(a-x)\) increases for \(x>0\). Hence the minimum of
\(\rho=W-\kappa-d_P\) is the smaller of those two levels. Thus
\(V=\rho+C\ge0\), and \(V\ge m1_J\), where
\(J=\{|x|\ge\ell/2\}\). In particular \(m>0\).

On our whole crossing interval the checker proves
\[
C_2-C_0=2H(a)-H(L-\ell)-H(\ell)+w>0.049482078967>0.
\tag{6}
\]
Therefore the active branch is exactly the one in the user's proposed
method, with
\(m=H(a+\ell/2)+H(a-\ell/2)-H(L-\ell)-H(\ell)\).
The checker evaluates this analytic branch and independently verifies
(6). It does not extrapolate that branch as a valid global floor where
(6) fails.

Put
\[
p(a)=1-\frac94(\ell/L)^5+\frac52(\ell/L)^3-\frac54(\ell/L),
\]
\[
\lambda_2(a)=1+Lh(L)-C(a),\qquad
\delta(a)=\lambda_2(a)+7/12,
\]
\[
\beta_e(a)=\left[\frac{(a/2)^2}{2(1-(a/2)^2/12)}\right]^2,
\quad
\beta_o(a)=\left[\frac{(a/2)^2}{6(1-(a/2)^2/20)}\right]^2.
\tag{7}
\]
For \(0<z<1\), define
\[
\Phi(z)=20z^3-45z^4+36z^5-10z^6,
\]
\[
q(a,z)=L\Phi(z)[g(zL)-g(L)],\qquad
M(a)=2L[1/4-g(L)].
\tag{8}
\]
Here \(q\) is a lower estimate for the Gamma diagonal, not its exact
value. For \(0<s,\theta<1\), set
\[
d(a,s)=\delta(a)-\frac{s}{1-s}M(a),\qquad
\mu(a,\theta)=\theta m(a),
\]
\[
\sigma(a;s,\theta,z)=\lambda_2+s q+\mu p(1-\mu/d),
\quad \eta=\frac{\min(\sigma,d)}{(1+\mu/d)^2},
\]
\[
K(a,\theta)=C(a)+\frac{\theta}{1-\theta}m(a),\qquad
G(a;s,\theta,z)=\frac{\eta-\beta_e K}{1+\beta_e}.
\tag{9}
\]
The admissible parameter domain is \(0<s,\theta,z<1\), \(d>0\).
When \(\delta>0\), this is equivalent to
\(0<s<\delta/(\delta+M)\). When \(\delta\le0\), it is empty and the
supremum is assigned \(-\infty\). Define
\[
G_{\Gamma\text{-node}}(a)=\sup_{d>0,\ 0<s,\theta,z<1}G(a;s,\theta,z).
\tag{10}
\]
Formula (9) is an algebraic method indicator even where \(\sigma\le0\).
Its interpretation as a positive source-norm lower bound requires
\(\sigma>0\) and \(\eta-\beta_eK>0\). We never infer a negative Weil
vector from a negative value of this indicator. Every maximizing
parameter in (1)--(4) has \(\sigma>0\), as proved below.

## 3. Infinite-dimensional provenance of (9)

The accepted connected identity and Legendre normalization are retained:
\(e_n(x)=\sqrt{(2n+1)/L}P_n(x/a)\). On the even sector write
\(u=u_0e_0+\alpha e_2+y\),
\(y\in Y=\overline{\operatorname{span}}\{e_4,e_6,\ldots\}\).
The singular Gamma kernel has eigenvalues \(\mathsf H_n\); after the
constant Gamma floor, all even tail eigenvalues are at least \(\delta\).
The positive residual is
\[
R_\Gamma[u]=\int_{x<y\in I_a}[g(y-x)-g(L)]|u(y)-u(x)|^2\,dx\,dy.
\]
The accepted local monotonicity \(g'<0\) on \((0,2]\), which covers
this whole Prime-2-only domain, gives
\[
R_\Gamma[e_2]\ge q(a,z),\qquad 0\preceq R_\Gamma\preceq M(a)I.
\tag{11}
\]
The first inequality follows by integrating the exact polynomial
\(60t^2(L-t)^3/L^5\) from zero to \(zL\). Its primitive is
\(L\Phi(z)\). In particular \(\Phi(1/2)=21/32\) and \(\Phi(1)=1\).
The second inequality is the degree bound for the entire Gamma graph
Laplacian. There is no high-mode truncation.

The positive-form inequality
\[
R_\Gamma[\alpha e_2+y]\ge s q|\alpha|^2
-\frac{s}{1-s}M\|y\|^2
\]
leaves the positive tail floor \(d\). The Node split yields
\(\mu P_J\) on the high-mode block and costs
\(\theta m/(1-\theta)|u_0|^2\). Its tail block and coupling satisfy
\[
D=dI+\mu P_YP_JP_Y\succeq dI,\qquad
b=\mu P_YP_Je_2,\quad \|P_YP_Je_2\|^2\le p.
\]
Thus the actual comparison-block Schur pivot is at least \(\sigma\)
in (9). Also \(\|D^{-1}b\|\le\mu/d\), giving the inverse-shear norm
bound \(1+\mu/d\). For positive \(\sigma\), this proves the
back-transformed lower bound \(\eta\).

The Gamma difference form annihilates \(e_0\) including cross terms.
The even Mellin condition gives \(|u_0|^2\le\beta_e\|\alpha e_2+y\|^2\).
Subtracting \(\beta_e K\) and then dividing the **whole** numerator by
\(1+\beta_e\) proves the positive-gap interpretation of (9).
The odd condition gives the bound
\[
G_o(a)\ge\frac{\lambda_2+1/3-(1/2-\lambda_2)\beta_o}{1+\beta_o}.
\tag{12}
\]
These are exactly two global Mellin conditions. The closed form domains
and parity decomposition are those of the accepted connected packages;
the bounded Gamma and Node residuals introduce no finite-dimensional
substitute for the tail. A1 and Prime-2 difference energy do not enter
this argument.

## 4. Analytic reduction of the z optimization

For fixed admissible \(s,\theta\), (9) is nondecreasing in \(q\).
On the compact region eventually containing all maximizers, its min
branch is inactive and its derivative with respect to \(q\) is
\[
\frac{s}{(1+\beta_e)(1+\mu/d)^2}>0.
\tag{13}
\]
Thus the optimal Gamma cut can be found independently of both splits.

Here is a uniform global uniqueness proof for that cut on \(a\in I\).
The checker certifies \(g''(t)<0\) on \([0,4/5]\) using eight enclosing
derivative intervals, including their analytic series remainders.
Since \(g'(0)=-1/24\), also \(g'<0\) there. All our distances satisfy
\(L<4/5\). Write \(r=g(Lz)-g(L)>0\). Then
\[
\Phi'=60z^2(1-z)^3,\qquad \Phi''=60z(1-z)^2(2-5z),
\]
\[
q_z=L[\Phi' r+L\Phi g'(Lz)],
\quad
q_{zz}=L[\Phi''r+2L\Phi'g'(Lz)+L^2\Phi g''(Lz)].
\tag{14}
\]
For \(0<z\le2/5\), the increase of \(-g'\) implies
\(r\ge L(1-z)(-g'(Lz))\), while the increase of \(\Phi'\) on this
interval implies \(\Phi\le z\Phi'\). Therefore
\[
q_z\ge L^2(-g'(Lz))(1-2z)\Phi'>0.
\]
For \(2/5\le z\le1\), (14) gives \(q_{zz}<0\). Finally
\(q_z(1)=L^2g'(L)<0\). There is exactly one critical point, which is
the global maximum over \(0\le z\le1\) and lies in \((2/5,1)\).

Derivative-sign bisection, with all operations outward rounded, gives
the rational z interval in (2), uniformly over \(I\). At its endpoints,
\[
q_z(z_-) > 0.000000839393,\qquad
q_z(z_+) < -0.000000838143.
\]
At the rational midpoint \(z_c\), concavity supplies the bound
\[
q(a,z_*)\le q(a,z_c)+|q_z(a,z_c)|\,(z_+-z_-)/2.
\tag{15}
\]
Together with the lower bound \(q(a,z_*)\ge q(a,z_c)\), this gives
\[
0.011486486426<q_*(a)<0.011486514946\quad(a\in I).
\tag{16}
\]
All subsequent interval calculations contain the exact \(q_*(a)\).

## 5. Compactness: exclude the entire open-domain boundary

Set \(\tau=-1/10000\) and substitute \(q=q_*(a)\). The checker proves
\(C,m,p,\delta,\beta_e,M>0\), \(\lambda_2+q_*<0\), and
\[
-\frac{\beta_e C}{1+\beta_e}<-0.000646939413<\tau.
\tag{17}
\]
Whenever \(\sigma\le0\), (17) bounds \(G\) above by \(\tau\).
Thus a maximizer exceeding \(\tau\) must have a positive pivot.

For any \(d>0\), the quadratic Node expression satisfies
\(\mu(1-\mu/d)\le d/4\). Hence, over all admissible triples:

* If \(\theta\le3/10\), then
  \(\sigma\le\lambda_2+q_*+(3/10)mp<0\).
* If \(s\ge3/4\), then \(d\le\delta-3M\) and
  \(\sigma\le\lambda_2+q_*+p(\delta-3M)/4<0\).
* Always \(\eta\le\max\{0,\lambda_2+q_*+p\delta/4\}\). If
  \(\theta\ge199/200\), the cost is at least \(C+199m\). The resulting
  upper bound for \(G\) is less than \(-0.011436858475<\tau\).

Thus every candidate exceeding \(\tau\) lies inside the closed search
rectangle
\[
K=[0,3/4]\times[3/10,199/200].
\tag{18}
\]
This is an auxiliary continuous extension to \(s=0\), not a claim that
\(s=0\) belongs to the original open admissible domain. On all of \(K\),
\[
d>0.368423515841>0,\qquad
\sigma\le\lambda_2+q_*+mp<\delta-3M\le d.
\tag{19}
\]
Hence the min in (9) selects \(\sigma\) throughout the search rectangle;
the formula is smooth there.

The fixed rational split pair
\[
(s_c,\theta_c)=(328425/10^6,759467/10^6)
\tag{20}
\]
with the certified Gamma optimizer has \(G>\tau\) uniformly over
\(a\in I\). The entire remaining boundary \(s=0\) is excluded by a
complete adaptive interval cover of its theta interval: 24 leaves all
have upper value below \(\tau\). The other three faces are already
covered by the strict analytic bounds above.

Consequently the original supremum is attained in the interior of
\(K\), with \(s>0\). Its cut is the unique \(z_*\), and its two split
derivatives vanish. Once (2) is proved, that box itself is a compact
subset of the original strictly admissible domain containing every
maximizer. No limiting sequence at \(s=0\), \(\theta=1\), \(d=0\), or
\(z\in\{0,1\}\) is left unaccounted for.

## 6. Exhaustive derivative boxes and unique maximizer

The checker differentiates the rational expression (9), with inactive
min branch and \(q=q_*\), using exact second-order interval automatic
differentiation. Starting with \(K\), it bisects the longer side of any
box that has not yet been classified. A box is discarded only when:

1. its entire G interval is below \(\tau\); or
2. its entire \(G_s\) interval is strictly positive or negative; or
3. its entire \(G_\theta\) interval is strictly positive or negative.

A box entirely inside
\[
B=[328025/10^6,328825/10^6]\times
  [759267/10^6,759667/10^6]
\tag{21}
\]
is retained. The process exhausts its queue, with no undecided box:

| Classification | Number of leaves |
|---|---:|
| value below tau | 4 |
| nonzero s derivative | 79 |
| nonzero theta derivative | 60 |
| entirely inside B | 6 |

There are 149 leaves and 297 total visited boxes. The exact summed leaf
area equals the area of K, and the binary-tree count is also checked.
The s=0 boundary cover likewise checks its entire interval length.
This is an exhaustive interval proof over boxes, not a point grid or a
search declaring an observed best sample optimal.

All global maximizers are interior stationary points, so they must be
inside B. Throughout \(I\times B\), with the exact q maximum enclosed
by (16), the Hessian satisfies
\[
G_{ss}<-0.018151607647<0,\qquad
\det\nabla^2_{s,\theta}G>0.001536279462>0.
\tag{22}
\]
It is therefore negative definite. Strict concavity on the convex box B
allows at most one stationary point there. Existence was established by
compactness and the boundary exclusions. This proves uniqueness and
the full three-parameter enclosure (2) for every \(a\in I\).

## 7. Endpoint signs and a unique local crossing

At each rational endpoint, the checker repeats derivative-sign bisection
for z, giving a much narrower pointwise z enclosure. The rational
midpoint of that enclosure, combined with (20), gives a genuine lower
witness. At \(a_-\) its gap is enclosed by
\[
[0.000000481959,\ 0.000000482589]
\]
with the displayed endpoints rounded outwards.

For the upper bound at \(a_+\), use the tangent plane of the concave
function on B, centered at (20). If \(r_i\) is the maximum coordinate
distance from this center to B, then
\[
\sup_B G\le G(s_c,\theta_c)+
\sum_{i\in\{s,\theta\}}|G_i(s_c,\theta_c)|r_i.
\tag{23}
\]
All terms are interval-enclosed with the exact q maximum contained in
the q interval. The resulting upper bound is less than
\(-0.000000560219\). By Section 6 this is an upper bound over the entire
original admissible domain. This proves both signs in (4).

For uniqueness of the crossing, the optimizer is interior and its split
Hessian is nonsingular; the z second derivative is also strictly
negative. The implicit-function theorem yields smooth optimizers on I.
The envelope derivative equals \(G_a\) at the optimizer. The checker
encloses this derivative on the entire box (2). For reproducibility the
nontrivial first derivatives, on the verified active branch, are
\[
C'=2h(L-\ell),\quad
m'=-h(a+\ell/2)-h(a-\ell/2)+2h(L-\ell),
\]
\[
p'=\tfrac54(3z_0^2-1)^2z_0/a,\qquad z_0=\ell/L,
\]
\[
\lambda_2'=2h(L)+2Lh'(L)-C',\quad
M'=4[1/4-g(L)]-4Lg'(L),
\]
\[
q_a=2\Phi(z)[g(Lz)-g(L)]
+2L\Phi(z)[zg'(Lz)-g'(L)],
\]
\[
h'(t)=h(t)\left[-\tfrac12-\frac{2e^{-2t}}{1-e^{-2t}}\right].
\tag{24}
\]
The rational moment expression is differentiated directly. The computed
derivative interval is precisely (3); no finite-difference derivative
is used. Continuity, the two endpoint signs, and strict decrease on I
prove exactly one crossing there. Formula (12) gives
\(G_o>0.279902209513>1/4\) throughout I.

## 8. Arithmetic, analytic tails, and reproduction

The checker is self-contained Python standard library code. All
arithmetic, derivative propagation, predicates, and decimal displays use
integers and `fractions.Fraction`, rounded outwards on a \(10^{-25}\)
grid. Decimal outputs are floor/ceiling displays, not binary floats.

Exponential intervals use terms through degree 64 and tail at most the
degree-65 term divided by \(1-x/66\), for \(0\le x\le4\). Logarithms
use exact power-of-two range reduction and 64 atanh terms with remainder
\(x^{129}/[129(1-x^2)]\). Arctangent uses 64 alternating terms and the
next-term bound. Machin's identity encloses pi. The square-root-of-two
endpoints are checked by squaring. With \(q=e^{-v/2}\), H is evaluated as
\[
H(v)=\tfrac12\log\frac{1+q}{1-q}+\frac\pi4
-\arctan\frac{1-q}{1+q}.
\]

Euler's constant is bounded without an imported decimal or an unchecked
high-precision evaluation. For \(f(x)=1/x\), the positive trapezoid
error on each unit interval equals
\(\frac12\int_0^1t(1-t)f''(k+t)dt\), which is at most
\(\frac18\int_k^{k+1}f''(x)dx\). Summing to infinity gives
\[
\mathsf H_N-\log N-\frac1{2N}
<\gamma<
\mathsf H_N-\log N-\frac1{2N}+\frac1{8N^2},\quad N=10000.
\tag{25}
\]
The interval width is at most \(1.25\cdot10^{-9}\), apart from the much
smaller accumulated outward rounding, and is propagated everywhere.

To differentiate g near zero without singular cancellation, the checker
uses the identity
\[
g(t)=\tfrac14\left[\frac1{\cosh x}
-\frac{xB(x)}{1+x^2B(x)}\right],\quad x=t/2,
\quad B(x)=\sum_{k\ge0}\frac{x^{2k}}{(2k+3)!}.
\tag{26}
\]
Both cosh and B are expanded through k=16. For each derivative order
0, 1, 2, the remaining positive series is bounded by its first omitted
term divided by \(1-x_{\rm hi}^2\), with \(0\le x\le3/5\). The
successive derivative-term coefficient ratios are at most one. These
tails are inserted before interval differentiation of (26). Thus the
g'' proof and all first derivatives include analytic remainders.

`--write` produces deterministic JSON and log; `--verify` recomputes the
entire certificate, compares their exact bytes, and verifies all five
payload hashes. Nineteen named checks pass. The interval covers and
their statistics are reproduced, not imported. No quadrature, external
numerical optimizer, finite-difference derivative, or floating-point
decision appears in the certificate.

JSON fields containing an `upper` or `lower` in their names describe
enclosures of the bound expression itself. For example an interval
around a tangent upper bound is not an interval enclosure of the exact
optimal gap. The analytic arguments in Sections 2--7 remain part of the
proof; the checker alone does not replace them or the accepted
connected-form identities.

## 9. Meaning of the method boundary and next mechanism

The theorem optimizes exactly the proposed Gamma-plus-Node estimate:
the Gamma cut z, the Gamma split s, the Node split theta, its conservative
Node coupling bound p, the shear loss, and the full moment normalization.
It retains the entire infinite-dimensional tail through its positive
floor and operator bound. The negative upper-endpoint value proves
failure of this particular optimized estimate there. It says nothing
negative about the exact residual operator or Q_W.

The Node projection bound could still be sharpened, and the positive
Prime-2 difference energy remains outside this envelope. The previous
joint certificate at 19651/50000 already demonstrates one way to use
both improvements. Those results are preserved; they are not silently
folded into (10), whose method class would then change. C15 is not
inferred necessary. There is no all-window theorem, Prime-3 result,
registry promotion, merge, or claim of independent external approval.
