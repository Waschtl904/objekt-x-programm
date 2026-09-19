# C1 readout obstruction: finite physical propagation cannot be repaired by finite rank

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `617ffe2a3bfe12bef768b536b9eeffbbfb21f1da`.
Six immutable analytic provenance files are bound by bytes, SHA-256 and Git
blob. The canonical C0 source system, all previous transport results and the
open moving 191D Low/Profile front are preserved.

## 1. Exact candidate classes and the result

Put B=log(5)/2. Work in PHYSICAL full-line coordinates with

    W_a = H1_0((-a,a)) intersect ker E_+ intersect ker E_-,
    E_+/- u = integral u(x) exp(+/-x/2) dx,
    B<=a<=1.

It suffices to work on these actual sources. Any proposed C1 readout on the
closed form space must restrict to them. A spatially local readout is a
different notion from a readout merely indexed by a finite window a.

Let a candidate target Hilbert space have a specified physical-position
direct-integral realization H=integral_R^direct H_x dmu(x), with arbitrary
fiber multiplicity. A complex-linear map L:W_a->H has physical propagation
at most R>=0 if

    support(Lu) subset {x:dist(x,support(u))<=R}              (1)

up to the target measure's null sets. In particular, separated input
supports at distance >2R have orthogonal L-images. The following theorem
also applies directly to maps satisfying this separated-support
orthogonality property, without choosing a direct-integral model.

**Theorem A (finite propagation plus finite rank is excluded).**
For any B<=a<=1 and any R<a, there is no exact positive Weil Gram readout

    T=L+K,  dim range K=m<infinity,
    q_a(u,v)=<Tu,Tv>_H for every u,v in W_a,                 (2)

where L has propagation at most R. K may be any finite-rank nonlocal map,
may depend on a, and need not have range orthogonal to L. No boundedness
assumption on these maps in the L2 norm is needed for this algebraic
obstruction. In particular an exact pure finite-propagation readout would
have to satisfy R>=a. A family with fixed R<1 cannot work on a cofinal
set a increasing to 1. A family with R_a<=theta*a, theta<1, fails already
at each individual endpoint.

The obstruction is an infinite-rank Gamma pairing between two separated
families of exact two-Mellin sources for which EVERY Prime pairing and
the L2 pairing vanish. A finite number of global features cannot reproduce
that pairing on top of a spatially local remainder.

**Theorem B (a quantitative witness for the pure local class).**
There are fixed actual sources u,v supported inside (-B,B), with u+v even
and u-v odd, such that for every linear T of propagation R<73/200,

    max_(f in {u+v,u-v}) |q[f]-||Tf||^2|/||f||^2 >10^-11.  (3)

This numerical error bound is for the PURE finite-propagation map T.
It is not asserted for a map with an additional nonlocal finite-rank K;
Theorem A excludes that larger class by exact rank, not by (3).

**Theorem C (individual channel Gram factors are excluded).**
For each strictly active prime power q, log(q)<2a, its signed arithmetic
form

    C_q[f]=-w_q<f,(tau_log(q)+tau_-log(q))f>,
    w_q=Lambda(q)/sqrt(q)>0,                                (4)

is indefinite on EACH parity sector of W_a. There are explicit sources
with C_q[f]/||f||^2=+w_q and -w_q, while all other arithmetic quadratic
terms vanish. Therefore neither sign of an individual Prime pairing can
be a positive Hilbert Gram component on all sources. At the exact entrance
log(q)=2a the channel is zero a.e.; indefiniteness is asserted only after
strict activation.

These results exclude concrete C1 architectures. They do not construct a
positive C1 readout, do not exclude arbitrary nonlocal or abstract-target
readouts, and do not exhibit a negative value of the FULL Weil quadratic
form. Indefinite self-adjoint Prime observables inside a common positive
mediator remain possible. All known 31D/191D decompositions retain their
full nonlocal hard forms and are unaffected.

## 2. A compact exact two-Mellin annihilator

For delta>0 define, with zero extension outside [-delta,delta],

    psi_delta(x)=(1-x^2/delta^2)^3 for |x|<=delta,
    phi_delta=(D^2-1/4)psi_delta.                            (5)

The bump and its first two derivatives vanish at both support endpoints.
Thus psi_delta is C2, its second derivative is piecewise smooth, and
phi_delta is continuous with zero boundary values and belongs to H1_0.
It is nonzero because phi_delta(0)=-6/delta^2-1/4. It is real and even.

Twice integrating by parts, with BOTH boundary terms zero, gives for every
real lambda

    integral phi_delta(x) exp(lambda*x) dx
        =(lambda^2-1/4) J_delta(lambda),
    J_delta(lambda)=integral psi_delta(x) exp(lambda*x) dx.  (6)

At lambda=+/-1/2 this is exactly zero. Every translate of phi_delta is
therefore an actual compactly supported two-Mellin source wherever its
support fits the window. Translation multiplies each zero moment by an
exponential; it does not require a new moment normalization. There is no
third constraint, no approximate moment ratio, and no use of A1.

The bump is nonnegative and even, so for lambda real

    J_delta(lambda)=integral psi_delta(x) cosh(lambda*x) dx
        >=integral psi_delta(x)dx=32delta/35>0.             (7)

The qualitative arguments below can instead use ANY nonzero, even,
nonnegative smooth compact bump psi and phi=(D^2-1/4)psi. Hence the
obstruction also holds already on a smooth dense source class, including
the natural domain of finite-order local differential readouts. Formula
(5) is chosen for the quantitative certificate because all its polynomial
norms and boundary data are rational.

These are auxiliary counterexample test sources for proposed operator
identities. They do not replace or rescale the previously inherited
physical near-null source.

## 3. The full Gamma mixed pairing survives the two moments

The bound physical nonpole identity is

    q(u,v)=G(u,v)-kappa<u,v>-sum_(q active) P_q(u,v),
    G(u,v)=integral_0^infinity k(r)<tau_r u-u,tau_r v-v>dr,
    k(r)=exp(-r/2)/(1-exp(-2r)),
    P_q(u,v)=w_q<u,(tau_log(q)+tau_-log(q))v>.               (8)

It agrees with the Weil form on W_a. The source embeddings of C0 are
physical zero extension, so these pairings do not change when the ambient
window is enlarged. All norms here use dx, with no reference-space scale.

Take two translates with centers -d/2 and d/2,

    u(x)=phi_delta(x+d/2), v(x)=phi_delta(x-d/2), d>2delta.

Suppose every active log(q) lies outside [d-2delta,d+2delta]. Then the
mass pairing and all mixed Prime pairings vanish by support separation.
The full Gamma polarization, with the left support preceding the right,
is exactly

    q(u,v)=-integral integral k(y-x)u(x)v(y) dx dy.           (9)

There is no extra factor two in (9): the quadratic cross term in
q[u+v] is 2q(u,v). In the r>0 jump integral only the translation which
brings the right support to the left contributes to this mixed pairing.

For t>0 the ENTIRE Gamma kernel has the geometric series

    k(t)=sum_(m=0)^infinity exp(-lambda_m t),
    lambda_m=2m+1/2.                                       (10)

On the separated supports t>=d-2delta>0, this series converges uniformly
and absolutely, so it can be integrated against the bounded compact
sources. Substituting (6) gives the exact identity

    -q(u,v)=sum_(m=1)^infinity
       [lambda_m^2-1/4]^2 exp(-lambda_m d) J_delta(lambda_m)^2
       >0.                                                (11)

The m=0 term is killed EXACTLY by the original Mellin constraints.
Every later summand is positive, since
lambda_m^2-1/4=2m(2m+1). The full sum is convergent: alternatively
bound J_delta(lambda)<=2delta exp(lambda*delta), giving a polynomial
in m times exp(-lambda_m(d-2delta)). No finite tail is substituted for
the Gamma operator. Keeping its first positive surviving term is a
rigorous lower bound, not an uncontrolled truncation.

In particular,

    -q(u,v)>=36 exp(-5d/2)(32delta/35)^2.                   (12)

This proves that the two Mellin constraints remove just the first mode
of this separated Gamma pairing; they do not make it local or finite rank.
A negative mixed value q(u,v) is entirely compatible with positive
diagonal energies q[u],q[v]. It is not a negative Weil source.

## 4. Arbitrary rank between separated source blocks

Fix any a in [B,1] and R<a. There are finitely many active prime powers.
Choose d in (2R,2a) which is not any active log(q). Since the excluded
set is finite, choose delta>0 and eta>0 sufficiently small that

    d/2+delta+eta<a,
    d-2delta-2eta>2R,
    [d-2delta-2eta,d+2delta+2eta] contains no active log(q).  (13)

For arbitrary N choose distinct increasing t_1,...,t_N in (-eta,eta),
and put

    u_i(x)=phi_delta(x+d/2-t_i),
    v_j(x)=phi_delta(x-d/2+t_j)=u_j(-x).                   (14)

The u_i supports all lie in the left block and the v_j supports all lie
in the right block. Each source has exactly the two required zero moments.
All cross-block mass and Prime pairings vanish, and the two support blocks
are at distance >2R. The same full series yields

    M_ij=-q(u_i,v_j)
        =sum_(m>=1) alpha_m exp(lambda_m t_i)exp(lambda_m t_j),
    alpha_m=[lambda_m^2-1/4]^2 exp(-lambda_m d)
                                      J_delta(lambda_m)^2>0. (15)

This real symmetric N by N matrix is strictly positive definite. To see
it, use only its FIRST N positive summands. With z_i=exp(2t_i), the matrix
of their feature vectors is

    V_im=exp(t_i/2) z_i^m, 1<=i,m<=N,
    det V=(product_i exp(t_i/2)z_i)
                              product_(i<j)(z_j-z_i) !=0.  (16)

This is the ordinary Vandermonde identity: after factoring the displayed
row factors, the remaining columns have powers 0,...,N-1. The nodes
are strictly increasing, so its determinant is nonzero. For every
nonzero coefficient vector c,

    c* M c >=sum_(m=1)^N alpha_m |sum_i c_i V_im|^2>0.

Thus the cross-block form has rank at least N for EVERY N. It has infinite
algebraic rank on the two separated admissible source subspaces. No
spectral approximation, sampled eigenvalue or finite-rank model is used
to infer this universal conclusion.

Now suppose (2) held with rank K<=m. Locality gives
<Lu_i,Lv_j>=0. Its proposed mixed Gram matrix is

    q(u_i,v_j)=<Tu_i,Kv_j>+<Ku_i,Lv_j>.                    (17)

The first matrix has rank at most m because all Kv_j lie in range K;
the second has rank at most m because all Ku_i lie there. Their sum
has rank at most 2m. Taking N=2m+1 contradicts (15)-(16). This proves
Theorem A. If L and K occupy orthogonal target summands, the mixed rank
bound improves to m, but no such orthogonality is assumed in the theorem.

The proof works for arbitrary finite m at EACH endpoint, so allowing
m to vary with a does not evade it. In particular, treating all nonlocality
as 31 or 191 global soft features and requiring the remaining infinite
readout to have R<a cannot be an exact C1 architecture. This says nothing
adverse about the inherited Low/Hard form decompositions: their complete
hard forms were never asserted to have spatially local Gram readouts.

For an explicit rank-three arithmetic instance, take delta=1/100,
d=3/4, eta=1/1000 and z=(1000/1001,1,1001/1000), with t_i=log(z_i)/2.
The checker proves |t_i|<eta, separation from every Prime length and
containment in the canonical B core. The enclosing left/right blocks
have gap d-2delta-2eta=91/125, so their locality condition holds whenever
R<91/250.
The first-three-mode matrix in (16) has determinant equal to the
rational determinant of z_i^m, since product z_i=1. It is strictly
positive. This exact instance illustrates the construction; the
arbitrary-N conclusion is proved by (16), not extrapolated from it.

## 5. A rational quantitative locality witness

Use delta=1/100 and d=3/4 without translations t_i. Then

    supports(u),supports(v) subset [-77/200,77/200],
    dist(support(u),support(v))=73/100,
    log(2)<73/100<77/100<log(3).

The checker proves these strict logarithmic inequalities. Thus the two
sources lie inside the known positive core B and every mixed arithmetic
term vanishes, even after adding any of the later channels. Their exact
rational bump mass and individual squared norm are

    J_delta(0)=8/875,
    N=||u||^2=||v||^2=||phi_delta||^2=2196489984032/75075
                                                   <40000000. (18)

The norm is obtained by integrating the degree-12 square polynomial.
An independent integration-by-parts identity checks the same value:

    ||psi''-psi/4||^2=||psi''||^2+(1/2)||psi'||^2
                                                   +(1/16)||psi||^2.

A rational Taylor series with an explicit positive geometric remainder
proves exp(15/8)<7. Consequently (12) gives

    q(u,v)<-L_0,
    L_0=(36/7)(8/875)^2=2304/5359375>1/2500,
    L_0/N=30888/2102109555030625>10^-11.                    (19)

For a pure readout T of propagation R<73/200 the images Tu,Tv are
orthogonal. Hence their even/odd combinations f_e=u+v, f_o=u-v satisfy

    ||f_e||^2=||f_o||^2=2N,
    ||Tf_e||^2=||Tf_o||^2,
    q[f_e]-q[f_o]=4q(u,v)<-4L_0.                            (20)

At least one of the two quadratic representation errors therefore has
absolute value >2L_0. Dividing by 2N proves (3). The actual lower error
bound L_0/N is >1.46938*10^-11; 10^-11 is a deliberate weakening.

Both f_e and f_o are actual original two-Mellin H1 sources. They lie
inside B, so the inherited All-Parity theorem already gives positive
FULL Weil energies for them. Their different positive energies cannot
both be represented by a local map assigning them the same squared norm.
This inherited positivity is contextual, not needed for the obstruction
or the rational bound (19); its prior matrix chain is not rerun here.

## 6. Isolating any active Prime channel in either parity

Let S={log(r):r is a strictly active prime power at a}. It is finite.
Fix ell=log(q) in S, so ell<2a. Choose c>0 small compared with
ell, min S, a-ell/2, and every |ell-log(r)| for r!=q. For example take

    c<min(ell/8, (min S)/8, (a-ell/2)/4,
                          min_(r!=q)|ell-log(r)|/8),
    0<delta<c/4,                                            (21)

omitting the last minimum if S has only one element. Let phi=phi_delta
and write phi_t(x)=phi(x-t). All the following supports fit strictly
inside (-a,a). For p=0,1 and epsilon=+/-1 define

    f_(p,epsilon)=phi_(c+ell/2)+epsilon phi_(c-ell/2)
          +(-1)^p phi_(-c-ell/2)+(-1)^p epsilon phi_(-c+ell/2). (22)

Reflection multiplies this source by (-1)^p, so it has parity p. Every
component already has both zero Mellin moments. The four supports are
disjoint, and ||f_(p,epsilon)||^2=4||phi||^2.

Their possible center distances are 2c, ell-2c, ell and ell+2c. Conditions
(21) make every non-ell distance miss every active prime length by more
than 2delta. The only q-overlaps are the two exact pairs at separation
ell. In the ordered four-bump basis the partial-shift compression is

             [0 0 1 0]
    A_ell =  [0 0 0 1],
             [1 0 0 0]
             [0 1 0 0]

and the source coefficient vector is

    ((-1)^p, epsilon, (-1)^p epsilon, 1).

Its norm square is 4 and its A_ell quadratic value is 4epsilon. Therefore

    C_q[f_(p,epsilon)]/||f_(p,epsilon)||^2=-epsilon w_q,
    C_r[f_(p,epsilon)]=0 for every other active r.            (23)

This proves Theorem C for every strict active channel, not just one
sampled endpoint. It concerns exact quadratic values of admissible
sources; it does not replace the full operator by this small compression
in a positivity proof. The other translated images may exist, but their
pairings with the source vanish by the stated support geometry.

For a concrete complete arithmetic ledger at a=1, use c=1/1000 and
delta=1/10000 for each q=2,3,4,5,7. Directed rational logarithms check
all supports and all missing overlaps. The checker verifies both choices
of p and epsilon, giving twenty exact isolated-channel cases. It uses
the correct von Mangoldt weights, including w_4=log(2)/2. Channel 8 is
excluded by log(8)>2. These sources establish individual-channel signs;
they do NOT establish a positive full endpoint at a=1 or at channel 7.

The q=2 cases lie already inside B. Thus even within a window where the
total form is known positive, its individual signed arithmetic channel
has both signs in each parity. A representation C_q(u,v)=<R_q u,R_q v>
would make C_q[f]>=0 for all f, contradicting epsilon=+1. Reversing the
channel sign fails on epsilon=-1. Unitary changes of feature coordinates
or positive orthogonal channel sums do not remove this obstruction.

## 7. What this closes at the C1 interface

The newly excluded classes are precise:

1. Physical-position readouts with propagation R_a<a, even after adding
   an arbitrary nonlocal correction of finite rank at each endpoint.
2. Positive Gram components identified individually with the original
   signed Prime contributions (or with their negatives), even within
   either parity and with other arithmetic channels isolated away.

The first obstruction requires genuinely infinite-dimensional nonlocal
interaction across separated admissible source blocks. The second
requires distinguishing signed channel observations from positive Gram
components. A common positive mediator could still carry Prime channels
as indefinite self-adjoint observations or through mixed terms. Neither
possibility is excluded, and neither is constructed here.

The conclusion is about the stated PHYSICAL support structure. A general
abstract Hilbert readout, a Fourier-indexed readout, or a nonlocal integral
readout need not satisfy (1). Relabeling an arbitrary Hilbert space by
physical coordinates is not a proof that its readout has finite propagation.
Likewise a readout defined on one local window may be spatially nonlocal.
This package does not claim that all possible intrinsic C1 readouts fail.

The obstruction occurs before choosing any mediator embedding I_(a,b).
An intertwining law cannot repair failure of the local Gram identity in
the excluded class. The already closed C0 embeddings remain physical
zero extension. They are not replaced or reconstructed by this result.
No shifted q+17 geometry is promoted to an unshifted Weil Gram geometry,
and no GNS space based on assumed positivity is used.

For the transport strand, all earlier positive bands and complete-tail
comparisons remain valid. Finite-dimensional Low spaces in a Schur proof
are not finite-dimensional positive C1 corrections to a spatially local
hard readout. Such a locality assumption was never part of the transport
proofs. Finite approximations with explicitly controlled nonzero errors
are also not ruled out by an exact-representation obstruction.

The strategic next C1 target is thus an intrinsically defined, genuinely
nonlocal common Prime/Gamma readout or a further precise obstruction to
a specified such candidate. Moving 191D Low/Profile renewal remains the
separate transport front. No additional microscopic width series is
claimed as the main result of this package.

## 8. Width-comparison clarification

The two comparison statements use different, explicit historical anchors:

| New outer width | Compared with | Exact factor |
| --- | --- | --- |
| 10^-10 in 617ffe2 | 5*10^-13 in immediately preceding b1c0186 | 200 |
| 10^-10 in 617ffe2 | 5*10^-19 in earlier ca3849a | 200000000 |

The proof and checker in 617ffe2 explicitly used b1c0186 as their anchor
and 5*10^-13 as the old outer width. Its factor 200 is therefore correct.
The factor 200 million is correct when comparing with ca3849a instead.
This is an append-only clarification of the baselines, with no correction
to any previously proved window, gap or byte of a historical package.

## 9. Reproduction and scope

`check_nonlocal.py --verify` is standalone Python standard-library code.
It uses only integers and Fractions, rational logarithmic/Taylor remainder
bounds and integer-square-root enclosures. It verifies the exact bump
identities and boundary data, source norms, Prime-free mixed geometry,
the first surviving Gamma coefficient, the error bound (19), an explicit
rank-three Vandermonde instance, all twenty isolated Prime/parity/sign
cases, the two width ratios, and all six analytic input bindings.

The new ledger has **84 exact checks**. JSON and log reproduce byte for
byte; all seven payload SHA-256 hashes must match. There is no quadrature,
numerical eigenvalue sign test, sampled infinite-rank inference or dropped
infinite Gamma remainder. No inherited numerical matrix is used as a new
arithmetic input, and the old expensive matrix chain is not rerun by this
checker. Its published results are preserved, not promoted to a fresh audit.

The universal rank theorem, the series/interchange argument, the continuum
choice in (13), the Hilbert support and rank obstruction, and the universal
Prime construction (21)-(23) are ANALYTIC proofs above. The finite checker
does not purport to independently prove them by sampling. Reproduction is
not independent analytic review. Status remains
**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

No negative full Weil source, new positive transport endpoint, non-summable
transport, positive C1 mediator, full C1-GEOM, Object X, global Weil
positivity or RH is certified here. The new result is a rigorous exclusion
of two concrete candidate classes at the named C1 interface.
