# Block-adaptive profile transport: a millionfold larger actual window

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `ca3849ab2a5abf6268ee892109a293332c1030e9`.
Canonical endpoint-matrix origin: `6a16d90b551588572c87e622c21c2df7f7b1adc2`.
All 103 mathematical input files are bound by byte length, SHA-256 and
Git blob. The parallel positive-gap-floor schedule of `829019d` and the
conditional restart through b<=1 from `ca3849a` are preserved.
The later concurrent commit `6cbef9df4536a02121af25edc9f5e5afcfd05174`
is preserved too; Section 9 supplies an append-only correction to one
of its quantitative ceiling bounds. Its qualitative summability
conclusion remains valid and is not a mathematical input to this package.

## 1. Result and precise scope

Put B=log(5)/2. For EVERY nonzero complex actual source
u in H1_0((-b,b)) satisfying exactly the original conditions
E_+u=E_-u=0, E_+/-u=integral u(x)e^(+/-x/2)dx, we prove

| Range | Physical all-parity gap |
| --- | --- |
| 0<b<=B+10^-13 | Q_W[u]>4*10^-15 ||u||^2 |
| 0<b<=B+5*10^-13 | Q_W[u]>10^-15 ||u||^2 |

The odd gap alone is >10^-12 on both ranges. The outer added width is
10^6 times the previously certified 5*10^-19. All norms are physical
L2(dx), except explicitly named reference norms. The original physical
source is not selected or rescaled. No A1 or third Mellin condition is used.

The improvement is a block-adaptive estimate: the full finite low block
retains its energy geometry, while the full infinite tail is paid from
its own positive reserve. The low/profile coupling is a two-function
analytic model PLUS a rigorously bounded full low-space remainder.
The entire shell space remains infinite-dimensional. No numerical
eigenvalue, quadrature, or sampled shell grid is a sign certificate.

This is a stronger actual finite window, not a theorem of non-summable
transport. The adaptive blocks are certified at the fixed core B only.
Their endpoint-uniform renewal, transport to log7/2, Connected Unit-Window
Coercivity, historical Strong Terminal, full C1-GEOM, Object X, global
Weil positivity and RH remain open. The improved lower gap compared with
an earlier weaker certificate is not an increase of the true variational
gap; exact zero-extension monotonicity is unchanged.

## 2. Source coordinates and canonical complete core blocks

We use the same full core plus profile coordinates as the even, odd and
restart packages. In parity p=0,1 the exact positive-half moment weight
is H_0(x)=cosh(x/2), H_1(x)=sinh(x/2). On 0<=x<=B set

    rho_0(x)=1-x/B, rho_1(x)=(x/B)(1-x/B),
    M_p=integral_0^B rho_p H_p, chi_p=rho_p/M_p.

Reflect chi_p with its parity and extend it by zero. It has zero boundary
value at +/-B and positive-half moment exactly one. For a right-shell
profile s on (B,b), let S_s be its parity extension to the two shells,
m_s=integral_B^b s H_p, Y_s=S_s-m_s chi_p, and p_s=||s||.

Then Y_s satisfies precisely its component of the original two moments,
||Y_s||^2=2p_s^2+||m_s chi_p||^2<4p_s^2 for all widths used here. The full
physical source is Psi(v,s)=Jv+Y_s. The complete core carries the trace;
there is no extra independent trace coordinate.

The physical isometry is (U_B f)(t)=sqrt(2B) f(Bt), into
H_ref=L2((-1,1),dt/2). With P_n the ordinary Legendre polynomials, define

    I_0={2,4,...,62}, I_1={3,5,...,63}, J_nn=1/(2n+1),
    r_n=<P_n,H_p(Bt)>/<P_p,H_p(Bt)>, phi_n=P_n-r_n P_p.

The exact moment map M acts on P_p-perp by these corrections. Its norm
is <sqrt2. The low space L_p is spanned by P_n for n in I_p; the complete
tail Y_p begins at degree 64+p. Thus the physical low source associated
with coefficients l is f_l=U_B^(-1) M l. On the full tail,
||U_B^(-1) M y||^2<=(1+epsilon_m,p^2)||y||^2.

The pinned endpoint proof gives the actual inequalities

    a[U_B^(-1)M l] >=(A^0-e_c J)[l],
    a[U_B^(-1)M y] >=delta_c,p ||y||^2,
    C* C <=G_act=(1001/1000)G+1001 e_c^2 J,                  (1)

where C is the ACTUAL low/full-tail coupling, delta_c,p is a directed
lower bound for the full core tail, and e_c includes the uniform Gamma
model and the infinite moment reconstruction errors. The checker
reconstructs A^0, G_act, e_c and delta_c independently in each parity.
The complete tail floors, total errors and Gram traces are required to
equal the pinned rational intervals exactly.

The Gram G is not a finite tail truncation. It contains the exact full
V^2, shifted-square, V/shift and all channel/channel integrals, minus the
finite low projections, plus the exact finite support of the polynomial
Gamma image. The latter ends at degree at most 128 because the kernel
model has degree 64; no infinite V or shift image is cut off. Both
indices undergo the exact moment congruence. All signed shift actions
are summed on each exact support interval before multiplication.

## 3. A sharper full core/profile coupling by separating input supports

Write h=b-B and assume 0<h<=H_*=5*10^-13. Directed logarithms verify
b<1, 2b<log7, and the active channels are exactly 2,3,4,5. Their
weights are w_q=Lambda(q)/sqrt(q). In the positive core, their reflected
input intervals at the right shell are

    (B-log2,B-log2+h), (log3-B-h,log3-B),
    (log4-B-h,log4-B), (B-h,B).

Let d_0=1/20 and split the positive core into the near interval
(B-d_0,B) and its complement, with the matching parity reflection.
The q=5 samples lie entirely in the near interval; the other three lie
outside it and are pairwise disjoint. These assertions hold uniformly
at H_* and are checked with directed intervals.

The singular same-side Gamma kernel is 1/[2(z+r)], where z=B-x and
r is shell distance. On the near input its full physical operator norm
is at most pi/sqrt2 by the Carleman integral. The q=5 action there has
norm at most sqrt2*w_5. On the far input, the other prime actions have
joint norm at most sqrt(2(w_2^2+w_3^2+w_4^2)), by disjoint INPUT intervals.
Combining these two orthogonal input spaces, while allowing their shell
outputs to be perfectly aligned, gives the norm upper bound

    c_0=sqrt((pi/sqrt2+sqrt2*w_5)^2+2(w_2^2+w_3^2+w_4^2))
                                            <3.466789839.   (2)

This follows from alpha||f_near||+beta||f_far||
<=sqrt(alpha^2+beta^2)||f||; output orthogonality is not assumed.
The omitted far singular Gamma piece has Hilbert-Schmidt norm at most
sqrt(h/(2d_0)), since its squared physical kernel integral is bounded by
(h/2) integral_(d_0)^B z^(-2) dz <=h/(2d_0).
The regular same-side and opposite-core Gamma pieces are bounded by
(5sqrt2/4)sqrt(Bh), as in the pinned full-coupling proof. Finally the
exact moment correction costs at most 720sqrt(h) in either parity.
Thus the ENTIRE physical core/profile coupling satisfies

    |q_b(Jf,Y_s)|<=c(h)||f|| p_s,
    c(h)=c_0+sqrt(h/(2d_0))+(5sqrt2/4)sqrt(Bh)+720sqrt(h),
    c(H_*)<3.468.                                           (3)

The tiny full-tail moment norm cost is included explicitly by checking
c(H_*)^2(1+epsilon_m,p^2)<(347/100)^2. Consequently, in the reference
tail norm,

    |q_b(U_B^(-1)M y,Y_s)| <=c_H ||y||p_s, c_H=347/100.       (4)

No high direction is discarded. The improved constant is due to input
support geometry, not to an assumption that high Legendre modes vanish
near the endpoint.

The existing pure profile estimates also remain valid on this larger
range: their derivations only need the checked support geometry and b<1.
Since h(8L+450)<1 and h(12L+1140)<1 at H_* and are increasing below it,

    d_p[s]=q_b[Y_s] >(2L-17)p_s^2, L=log(2/h).               (5)

All same-side shell shifts vanish because h<log2. All cross-shell
distances exceed 2B=log5, so these four prime shell self-terms vanish
a.e.; the possible endpoint contact has zero measure.

## 4. Exact logarithmic and constant low-coupling vectors

Unlike a bound of ||f_l||_infinity by a single scalar times ||l||, the
following construction retains the signed action of every low direction.
Let g(t)=k(t)-1/(2t). The pinned directed kernel model is

    g_64(t)=sum_(k=0)^64 p_k (t/2)^k,
    |g(t)-g_64(t)|<=epsilon_G on 0<=t<=5/3,

where epsilon_G<2.3*10^-19 is proved by a rational remainder estimate.
Let K_64 f(t)=B integral_(-1)^1 g_64(B|t-v|)f(v)dv. Its exact Legendre
columns are the same columns used in (1). Let q_B^64 be the nonpole
core form with K replaced by K_64 and all other terms unchanged.

For each n in I_p set f_n=U_B^(-1)phi_n and define the REAL coefficients

    a_n=-(1-r_n)/sqrt(2B),
    qchi_n=q_B^64(f_n,chi_p),
    c_n=[2(H_n-r_n H_p)-2(K_64 phi_n)(1)
             -2 sum_(q=2,3,4,5) w_q phi_n(1-log(q)/B)]/sqrt(2B)
             -H_p(B) qchi_n.                                (6)

Here H_n denotes the harmonic number in the numerator; H_p(B) denotes
the cosh/sinh moment weight, as specified above. These different uses
are disambiguated by the argument B. The q=5 term in (6) is a genuine
core/shell term evaluated at -1, although its core/core action is zero.

For completeness, qchi is evaluated without quadrature. In reference
coordinates set rho(t)=1-t for p=0, rho(t)=t-t^2 for p=1 on (0,1), and

    T_64=D_harm+q0 I+V-K_64-sum_(q=2,3,4) w_q T_(log(q)/B),
    qchi_n=sqrt(2B)/M_p integral_0^1 rho(t)(T_64 phi_n)(t)dt.  (7)

All polynomial and shifted polynomial integrals are exact antiderivatives
on the exact support intervals. For V=-log(1-t^2)/2 the required moments
are explicitly

    integral_0^1 t^(2j) V(t)dt
      =[sum_(k=0)^j 1/(2k+1)-log2]/(2j+1),
    integral_0^1 t^(2j+1) V(t)dt=H_(j+1)/(4j+4).

These follow by elementary log integration/series. The exact corrector
moments are M_0=4(cosh(B/2)-1)/B and
M_1=4sinh(B/2)/B-16(cosh(B/2)-1)/B^2. Directed intervals enclose the
exact moments and all coefficients; no rounded normalization replaces
them. The checker stores every a_n, c_n and qchi_n.

The actual low/profile functional has the representation

    q_b(Jf_l,Y_s)=integral_0^h [a[l] log(2B/r)+c[l]+e_l(r)]
                                           conjugate(s(B+r)) dr,
    |e_l(r)|<=[300000 r(log(2/r)+10)+110epsilon_G]||l||_ref.  (8)

Here a[l]=sum a_n l_n and c[l]=sum c_n l_n. This is a rank-at-most-two
MODEL for a map from the low space to the full shell, plus a uniform
operator remainder. Neither e_l nor any shell direction is dropped.

## 5. Proof of the uniform low-coupling remainder

For a polynomial P_n the elementary identity
integral_(-1)^1 (P_n(t)-1)/(1-t)dt=-2H_n gives the constant term of
the singular Gamma coupling. For a general low f=f_l, subtract its
endpoint value inside that integral. The difference between the exact
singular integral at r and its logarithmic/constant expansion at zero
is bounded by

    ||f||_infinity r/(2B)
              +Lip(f) r log((2B+r)/r).                       (9)

Indeed the constant part contributes f(B)log(1+r/(2B)); the remainder
uses |f(x)-f(B)|<=Lip(f)(B-x) and the exact difference of reciprocal
kernels. On the present range 2B+r<2, so the logarithm in (9) is at
most log(2/r).

The pinned low bounds give ||f_l||_infinity<=110||l|| in both parities.
The derivative is bounded using |P_n'|<=n(n+1)/2, |r_n|<2 and B>4/5:

    Lip(f_l)^2/||l||^2
      <=sum_(n in I_p)(2n+1)[n(n+1)/2+2p]^2/(2B^3)<100000^2.

This covers the full low space, not a chosen source. For the regular
kernel, the model derivative satisfies

    D_g=(1/2)sum_(k=1)^64 k|p_k|(5/6)^(k-1)<10.

Thus replacing the regular outside-core kernel by its model value at
r=0 costs at most [4D_g r+4epsilon_G]||l||. The bound follows from
||f_l||<sqrt2||l|| and the physical core length 2B. The model remainder
estimate applies because 2B+H_*<5/3.

Each prime sample remains in its core interval. Replacing its argument
by r=0 costs at most 2 sum w_q Lip(f_l) r<8*100000 r||l||.
The moment weight has derivative <3/5 on [0,1]. The actual complete
corrector functionals are bounded by 215||f|| and 1200||f|| respectively;
therefore varying that weight costs <1100r||l||.

Finally the qchi model error is paid separately. The conservative model
operator bound 2(2B)epsilon_G, together with ||f_l||<sqrt2||l||,
||chi_p||<sqrt200 and H_p(B)<6/5, costs <96epsilon_G||l||.
Together with the outside model error it fits 110epsilon_G||l||.
The coefficient in (9) is <70r||l||. Summing all linear and logarithmic
terms gives

    100000 r log(2/r)+(70+800000+1100+40)r+110epsilon_G
      <=300000 r(log(2/r)+10)+110epsilon_G.

This proves (8). The right side increases on (0,H_*], since the
derivative of r(log(2/r)+10) is log(2/r)+9>0. It also proves the full
L2 shell operator bound ||E_h||<=sqrt(h) R_h with

    R_h=300000 h(log(2/h)+10)+110epsilon_G.                    (10)

Although the logarithmic model is singular at r=0, it is square
integrable. No value at that measure-zero endpoint is needed.

## 6. Energy-adaptive finite loss with all infinite blocks retained

Choose an endpoint width H and a positive tail/profile payment alpha.
Using (4), pay the entire high/profile mixed term by

    2c_H||y||p_s <=(c_H^2/alpha)||y||^2+alpha p_s^2.

Set the exact rational effective tail floor and remaining profile floor

    delta=delta_c,p-c_H^2/alpha,
    d=2 log(2/H)_lower-17-alpha.

The two cases used below have delta>0 and d>0. For every h<=H, the
original form dominates the NAMED comparison form

    Q[l,y,s]=(A^0-e_c J)[l]+2 Re<C l,y>+delta||y||^2
                           +2 Re<B_h l,s>+d||s||^2,          (11)

where C and B_h are the ACTUAL low/high and low/profile couplings.
Complete its high square and use C*C<=G_act. The remaining low matrix is

    S=A^0-e_c J-G_act/delta.                                 (12)

For both parities and both cases, directed rational LDL gives 31 positive
pivots and S>=sigma J via the upper inverse trace tr(J S^(-1)). This is
recomputed, not transported from a scalar gap. All 124 pivots are stored.

Use this S as the metric on the entire low space. Let ell=log(2B/H).
The exact integrated energy trace of the two-function model in (8) is

    mu_H=H[(ell^2+2ell+2) a^T S^(-1)a
              +2(ell+1) a^T S^(-1)c+c^T S^(-1)c].            (13)

All three dual products are computed by directed triangular solves with
the same LDL factors. The SIGNED mixed product is retained; replacing
it by unrelated scalar absolute values would lose important information.
Equation (13) is an exact analytic integral, since the three shell
moments are H, H(ell+1), H(ell^2+2ell+2). It bounds the squared operator
norm of B_model S^(-1/2) by its Hilbert-Schmidt norm.

For the remainder, S>=sigma J gives
||E_H S^(-1/2)||^2<=H R_H^2/sigma. Therefore define the proved upper bound

    zeta=(sqrt(mu_H,upper)+sqrt(H R_H^2/sigma_lower))^2/d.

Then on the FULL low space, uniformly for h<=H,

    B_h* B_h/d <=zeta S.                                    (14)

The uniformity uses the same fixed S: the actual nonnegative integral
of the model's squared energy norm increases with its integration
interval, and h R_h^2 also increases. The profile floor at smaller h
only improves. Monotonicity of a rounded expression with a signed cross
term is not assumed in place of this integral argument.

This zeta is a LOW/comparison energy loss, not the norm Theta of the
actual complete core/profile Schur operator from the restart theorem.
Neither that Theta nor the inverse of an actual infinite block is
identified with S^(-1). The two meanings remain separate in the JSON.

Now complete the remaining profile square in (11). By (12)-(14),

    Q >=(1-zeta) S[l]+delta||y+delta^(-1)C l||^2
                           +d||s+d^(-1)B_h l||^2.           (15)

Its comparison inverse shear has norm <=1+r, with

    r^2<=tr(J^(-1)G_act)/delta^2+b_H^2/d^2,
    b_H^2=H[c_p(log(2/H)_upper+11)+m_p]^2,
    (c_0,m_0)=(72,516), (c_1,m_1)=(110,1440).                (16)

The crude norm in (16) is sufficient for conditioning only; it is NOT
used as the low Schur subtraction. This distinction is the source of
the improvement. The full physical norm obeys
||U_B^(-1)M(l+y)+Y_s||^2<=6(||l||^2+||y||^2+||s||^2), as before.
Thus (15) yields the all-source physical lower bound

    gamma_phys>=min((1-zeta)sigma,delta,d)/(6(1+r)^2).         (17)

All physical norm, moment map and both shear costs are included. Failure
of any sufficient LDL/Schur test would mean UNDECIDED for the actual
form; it would not certify a negative physical source.

## 7. Certified numerical ledger and source-domain conclusion

The exact rational/interval calculations give:

| Width H | alpha | even zeta upper | even physical gap lower | odd physical gap lower |
| --- | --- | --- | --- | --- |
| 10^-13 | 44 | <5.061*10^-7 | >4.3636*10^-15 | >1.6061*10^-12 |
| 5*10^-13 | 41 | <1.267*10^-4 | >1.1085*10^-15 | >1.4290*10^-12 |

The exact outward rational endpoints, not these explanatory decimal
weakenings, decide all inequalities. Both parity zetas are <10^-3;
on the first range they are <10^-6. The odd gap is weakened to the
simple published 10^-12, and the smaller parity gap gives Section 1.

The form-domain assertion applies to all original sources. Define
F_b^p as the closure of the actual parity H1_0 two-Mellin sources in a
positive graph norm of the full nonpole form, and
F_profile^p={s:Y_s in F_b^p}. Its pullback form is closed and densely
defined in L2(B,b), by the bounded profile lift with closed image.
The complete core/profile map is a Hilbert bijection with inverse
s=u|_(B,b), v=u_core+m_s chi_p. It has
(||v||^2+||s||^2)/2<=||u||^2<=5(||v||^2+||s||^2).

The coupling (3) is <4, and (5) is positive even at H_*. Together with
the inherited positive core form, these give equivalence of the product
graph norm and q_b+20||.||^2, exactly as in the pinned odd proof. Hence
the image of F_B^p direct-sum F_profile^p is form-closed. It contains all
actual H1 sources: their inverse has internal core H1 and shell H1 with
the exact gluing v(B)=s(B), s(b)=0. Cutting off the core in endpoint
strips of size eta and restoring its O(eta) moment with a fixed bump
approximates it in form norm, even if v(B) is nonzero. The strip error
has squared translate difference O(min(r,eta)), and therefore Gamma
energy O(eta(1+|log eta|)); the bounded remainder tends to zero too.
Thus v belongs to F_B^p, and Y_s=u-Jv belongs to F_b^p. Closure proves
surjectivity on the full form domain. No separate core zero trace or
extra Mellin condition is imposed.

The finite moment-corrected polynomial images are also in this core form
space by the same cutoff argument. Their finite projections and the
complete reference tail preserve the form domain, as proved at the
endpoint. Thus (11)-(17) apply to every source in this full domain.
Reflection invariance gives q[e+o]=q[e]+q[o], and the original two zero
moments split exactly into the even cosh and odd sinh zero moments.
This proves the all-parity theorem. Exact physical zero extension
extends the bounds to every smaller b, with no normalization loss.

## 8. Relation to reserve renewal and reproducibility

The old uniform restart pays a worst-case full-core loss of order
1/log(2/h) against the smallest physical gap. Here the high/profile
loss is paid by the tail reserve, and the low/profile loss retains
the two dual energy vectors and their signed mixing. Its main budget
is an explicit H times quadratic polynomial in log(2B/H), plus the
controlled O(H^3 log^2(2/H)/sigma) and model-error terms from (10).
No exponentially small width in the global physical gap is used to
certify the two stated windows.

This is evidence and a proved finite-step implementation of the
block-adaptive approach. It does not yet make the two dual vectors,
the full tail bound, or their comparison matrix uniform at new core
endpoints. The next structural gate is to renew THESE quantities,
or control a combined multi-shell block, with enough total certified
progress to reach a prescribed larger endpoint. The remaining thin
profile reserve in the outer case shows why a low-only improvement
does not by itself close that gate. Neither the fixed width nor the
small value of zeta proves non-summable transport.

The ordinary standalone `check_adaptive.py --verify` uses only Python's
standard library and integer/Fraction directed intervals on the pinned
10^-200 grid. It rebuilds both complete core blocks, all low coupling
vectors, four 31-pivot comparisons, signed energy products and every
remainder/conditioning loss. It also replays ca3849a and its entire
88/51/41/38/40/31/28/43/9 chain plus 349 universal algebraic regressions.
It verifies all 103 input bindings, byte-identical result JSON/log and
all seven payload hashes. No exploratory cache is a certificate input.
The new ledger has 71 passing exact checks, in addition to the inherited
reproduction and the 124 explicitly stored positive comparison pivots.

These checks establish arithmetic reproducibility. They do not replace
independent analytic review of the kernel, domain and infinite-operator
arguments. Status remains **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Publication appends eight package files and a transport-ladder appendix
on the research branch, preserving main and all earlier work, with no
PR or merge.

## 9. Append-only ceiling correction to concurrent 6cbef9d

Section 2 of `scalar-gap-restart-summability-barrier-2026-09-19/PROOF.md`
sets c=1600/epsilon_0, N_n=ceil(2^n c), t=2^(-ceil(c)) and infers
h_n<=t^(2^n). The intermediate inequality needed for this inference,
ceil(2^n c)>=2^n ceil(c), is false in general. At the very gap
epsilon_0=3*10^-16 discussed there,

    N_0=5333333333333333334,
    N_1=10666666666666666667 <2N_0=10666666666666666668.

Thus the allowed upper width 2^(-N_1) is larger than t^2. This concerns
the stated sufficient-width bound; it is not a negative source or a
failure of the restart theorem.

A corrected exact dyadic bound is immediate. Under the actual restart
hypothesis 0<epsilon_0<=1, let K=floor(c)>=1600 and s=2^(-K)<1/2.
Then, for every n>=0,

    ceil(2^n c)>=2^n K,
    h_n<=s^(2^n)<=s^(n+1),
    sum_(n>=0) h_n<=s/(1-s)<2s<infinity.

Alternatively, without epsilon_0<=1, use the real bound s=2^(-c) in
(0,1) and retain s/(1-s), without asserting s<=1/2. The corrected
argument proves the same qualitative summability barrier. For a
nonintegral c, K=ceil(c)-1, so its dyadic s is twice the old t;
the old displayed estimate with that particular t should not be reused.

This correction does not affect the explicit ca3849a schedule, whose
exponents were DEFINED as N_n=2^n ceil(c). It also does not affect the
separate target-gap-law summability argument in Section 3 of 6cbef9d.
The new fixed-core adaptive proof above uses neither schedule nor this
barrier estimate. Historical files are preserved byte for byte.
