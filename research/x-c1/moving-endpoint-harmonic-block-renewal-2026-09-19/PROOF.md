# Moving-endpoint harmonic block renewal on a certified finite band

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `b1c01860fef2a960cae57634041f75b29d37f836`.
Canonical endpoint-matrix origin: `6a16d90b551588572c87e622c21c2df7f7b1adc2`.
The 111 mathematical input files, including all eight files of the anchor
package, are bound by bytes, SHA-256 and Git blob. Earlier results and the
append-only ceiling correction in b1c0186 remain unchanged.
The concurrent commit `a0ea6f80f317e4ef1132fc02c86be5bd2064e738`
is preserved as well. Its uniform moving high-tail theorem on B<=a<=1
is complementary context, not an input to the proof below.

## 1. The finite-band result and its limits

Put B=log(5)/2 and H=10^-10. Every nonzero complex actual source
u in H1_0((-b,b)) satisfying exactly the original two conditions

    integral u(x) exp(x/2) dx = integral u(x) exp(-x/2) dx = 0

obeys, for 0<b<=B+H,

    Q_W[u] > 2*10^-15 ||u||_L2(dx)^2.                         (1)

The odd-sector bound is >10^-12. The added width is 200 times the outer
width of b1c0186. This is an actual all-source theorem with the complete
infinite tail, the complete profile and their mixed terms.

For EVERY a in the finite band [B,B+H], we also construct an actual
form-domain decomposition

    F_a = N_a direct-sum L_a direct-sum H_a.                  (2)

Here N_a has dimension one and follows the fixed inherited even source
by form projection; L_a has dimension 61 across the two parities; H_a
contains both complete core tails and ALL accumulated profiles. In each
parity the soft dimension is 31. The hard block has coordinate floor
>2/5 and physical floor >1/15 throughout the band. Actual harmonic
lifts have norm <15/2 in the named coordinates. Their full physical
coordinate maps have squared norm bounds 1/162 and 486. The two soft
Schur floors are >8*10^-13 and >4*10^-10 in the reference low norm.

Nested actual form projections give an exact transport cocycle and a
finite energy budget for the moving near-null direction. These bounds
do not deteriorate with the number of subdivisions of this band. In
particular two equal steps of width 5*10^-11 fill it without halving a
global gap at either step. Every a in [B,B+5*10^-13], the formerly
reached new band, permits the actual further step 5*10^-11.

This closes a FINITE-BAND version of moving-endpoint block reserve
renewal. It uses an accumulated profile anchored at B. It does not
reset that profile to empty or provide new comparison data beyond
B+H. Renewal over an unbounded sequence of new bands, non-summable
transport, reaching log(7)/2 or 1, Connected Unit-Window Coercivity,
full C1-GEOM, Object X, global Weil positivity and RH remain open.
The sum of any increasing subdivision's widths inside this band is
at most H. No contrary non-summability conclusion is inferred.

## 2. A sharp profile floor from the exact Gamma primitive

Use the inherited physical nonpole form

    q[f] = Gamma[f] - kappa ||f||^2
                 - sum_q w_q <f,(tau_log(q)+tau_-log(q))f>,
    Gamma[f] = integral_0^infinity k(r)||tau_r f-f||^2 dr,
    k(r)=exp(-r/2)/(1-exp(-2r)),
    kappa=log(8*pi)+EulerGamma+pi/2.

It equals Q_W on the two original Mellin constraints and is exactly
preserved by physical zero extension. On this band the active channels
are 2,3,4,5, with w_q=Lambda(q)/sqrt(q). Directed logarithms verify
2(B+H)<log(7). The q=5 core/profile channel is included throughout.

Let h=a-B>0, L=log(2/h), and let S_s be the parity extension of a
right profile s on (B,a), zero on the core. Write p=||s||_L2(B,a), so
||S_s||^2=2p^2. Since h<log(2) and opposite shells are separated by
more than 2B=log(5), all prime self-correlations of S_s vanish a.e.

The same full Gamma leakage argument as in the odd package, Section 4,
gives, in either parity,

    q[S_s] >= [4T(h/2)-2*kappa-2h*k(2B)] p^2,
    T(t)=integral_t^infinity k(r)dr.                          (3)

Indeed exterior leakage for a component of length h is at least
2T(h/2) pointwise by convexity of T (T''=-k'>0). The absolute
interaction between the two components is at most 2h*k(2B)*p^2.
Thus (3) does not drop their interaction or assume its sign.

The exact primitive already underlying the pinned Gamma model is

    T(t)=atanh(exp(-t/2))+atan(exp(-t/2)),
    T(t)+(1/2)log(t)=log(2)+pi/4-integral_0^t g(r)dr,
    g(r)=k(r)-1/(2r).                                        (4)

The first identity follows by substituting y=exp(-r/2); the primitive
of 2/(1-y^4) is atanh(y)+atan(y). Its t->0 constant is log(2)+pi/4.
The second follows by differentiation and that limit. On the required
range the pinned regular-kernel bound gives 0<g<=1/4. Also
k(2B)=25/(24sqrt(5))<1/2. Substituting (4) into (3) cancels pi and
the appropriate log constants BEFORE estimating:

    q[S_s] >= [2L-c_Gamma-(3/2)h]p^2,
    c_Gamma=2log(2*pi)+2EulerGamma <4.831.                    (5)

The error (3/2)h consists of 4 integral_0^(h/2) g <=h/2 and
2h*k(2B)<h. In particular no numerical evaluation of atanh or atan
is needed for the certificate.

The fixed physical correctors on 0<=x<=B are

    rho_e=1-x/B, rho_o=(x/B)(1-x/B),
    M_p=integral_0^B rho_p(x) H_p(x)dx,
    chi_p=rho_p/M_p, H_e=cosh(x/2), H_o=sinh(x/2).

They are reflected by parity and extended by zero. Set
m_s=integral_B^a s H_p and Y_s=S_s-m_s chi_p. The exact moments
of Y_s vanish, and the inherited bounds hold uniformly for a<1:

    |m_e|<=(6/5)sqrt(h)p,  |m_o|<=(3/5)sqrt(h)p,
    ||chi_e||_infinity<3, ||chi_o||_infinity<10,
    ||chi_e||^2<18,        ||chi_o||^2<200.

The inherited bounded-core/profile estimate
|q(Jf,S_s)|<=||f||_infinity sqrt(h)(L+11)p and q[chi_p]>=-14||chi_p||^2
give the complete correction losses <=h(8L+450)p^2 and
<=h(12L+1140)p^2, respectively. The first is a conservative rounding
of (36/5)(L+11)+(36/25)*252. The second equals
12(L+11)+(9/25)*2800. This uses the full form expansion of Y_s.

Both h(12L+1140) and h(8L+450) increase for 0<h<=H. The checker proves

    c_Gamma+(3/2)H+H(12log(2/H)+1140)<5,
    c_Gamma+(3/2)H+H(8log(2/H)+450)<5.

Consequently the FULL corrected profile has the uniform floor

    q[Y_s] > [2log(2/h)-5]p^2.                               (6)

This sharper constant replaces 17 in the old sufficient bound. The
logarithmic profile reserve is still consumed by the TOTAL accumulated
width h, not just the width of the most recent added shell.

## 3. Full core/profile coordinates and all coupling bounds

All core objects in this section are those of b1c0186, Sections 2-5.
We specify them to distinguish actual operators from comparisons.
Let U_B f(t)=sqrt(2B)f(Bt), with reference space L2((-1,1),dt/2).
In parity p=0,1 remove P_p and let M be the exact Mellin moment map

    M P_n=P_n-r_n P_p,
    r_n=<P_n,H_p(Bt)>/<P_p,H_p(Bt)>.

Let K_p be the 31-dimensional reference low space, degrees
2,4,...,62 for even and 3,5,...,63 for odd, and let Y_p be its
complete reference tail, beginning at degree 64+p. Write J_nn=1/(2n+1)
for the low Gram matrix. The moment map satisfies ||M||<sqrt(2),
and deleting its P_p component is an inverse of norm <=1.

For each a define the raw hard coordinates and physical maps

    E_a^p = Y_p direct-sum L2(B,a),
    Z_p l = zero extension of U_B^-1 M l,
    V_a^p(y,s)=zero extension of U_B^-1 M y+Y_s,
    P_a^p(l,y,s)=Z_p l+V_a^p(y,s).                            (7)

At a=B the profile space is {0}. Norms in K_p,Y_p are reference norms;
profile norms use dx on the positive shell. For N^2=||l||^2+||y||^2+||s||^2,

    N^2/2 <= ||P_a^p(l,y,s)||_physical^2 <= 6N^2.              (8)

For the upper bound use ||U_B^-1 M(l+y)||^2<2(||l||^2+||y||^2),
||Y_s||^2<4||s||^2 and Cauchy-Schwarz on their sum. For the lower
bound the inverse is s=u|_(B,a), v=u_core+m_s chi_p, l+y=M^-1 U_B v.
Thus N^2<=2||u_core||^2+(1+144h)||s||^2<=2||u||^2, since
||u||^2=||u_core||^2+2||s||^2 and 1+144H<4. No trace is added.

The pinned actual core inequalities are

    q[Z_p l]>=(A^0-e_c J)[l],
    q[U_B^-1 M y]>=delta_c,p ||y||^2,
    C_p^* C_p<=G_act=(1001/1000)G+1001 e_c^2 J.               (9)

C_p is the ACTUAL low/full-tail coupling. The Gram retains the complete
infinite V and shift images, all signed mixed channel actions, and the
exact finite support of the degree-64 Gamma model. The latter is not
a cutoff of an infinite tail. e_c pays both Gamma and infinite moment
errors. Both complete tail floors exceed .719. The checker reconstructs
these two 31 by 31 matrices and complete Grams with pinned analytic
integrals; no exploratory cache is used.

The near/far INPUT-support argument of b1c0186, Section 3, applies
on the entire larger band. The q=5 input lies in the near strip
(B-1/20,B); the q=2,3,4 input intervals lie in its complement and
are disjoint there. The full physical core/profile norm is at most

    c(h)=c_0+sqrt(h/(2d_0))+(5sqrt(2)/4)sqrt(Bh)+720sqrt(h),
    d_0=1/20,
    c_0=sqrt((pi/sqrt(2)+sqrt(2)w_5)^2
                         +2(w_2^2+w_3^2+w_4^2)).            (10)

Output orthogonality is not assumed. Directed bounds give c(H)<3.475,
and, after including the exact full-tail moment norm cost,

    |q(U_B^-1 M y,Y_s)| <= c_H ||y|| ||s||, c_H=87/25.       (11)

All model distances remain below 5/3. The actual low/profile operator
B_h still has the representation from b1c0186, Sections 4-5,

    (B_h l)(r)=a[l]log(2B/r)+c[l]+e_l(r), 0<r<h,
    |e_l(r)| <=[300000 r(log(2/r)+10)+110epsilon_G]||l||.     (12)

The exact analytic coefficients are

    a_n=-(1-r_n)/sqrt(2B),
    c_n=[2(Harm_n-r_n Harm_p)-2(K_64(P_n-r_nP_p))(1)
        -2 sum_(q=2,3,4,5) w_q(P_n-r_nP_p)(1-log(q)/B)]/sqrt(2B)
        -H_p(B) q_B^64(U_B^-1(P_n-r_nP_p),chi_p).

The checker recomputes and exactly matches all 93 intervals per parity
(a,c and corrector functional). It verifies the enlarged support range,
low derivative bound 100000, regular-model derivative bound 10 and all
remainder budgets. Thus (12) retains the operator remainder on the
ENTIRE low space. The full profile remains infinite-dimensional.
The uniform bounds also include

    ||B_h||^2 <= b_H^2=H[c_p(log(2/H)+11)+m_p]^2,
    (c_e,m_e)=(72,516), (c_o,m_o)=(110,1440).                 (13)

This coarse bound is used for conditioning; the Schur loss below uses
the signed two-function energy, not (13).

## 4. The new all-source comparison and soft reserve

For each parity choose alpha=42 and form the rational lower constants

    delta=lower(delta_c,p)-c_H^2/42,
    d=2 lower(log(2/H))-5-42>0,
    S=A^0-e_c J-G_act/delta.                                 (14)

Pay the complete high/profile mixed term using
2c_H||y||||s|| <=c_H^2||y||^2/42+42||s||^2. The actual form then
dominates the comparison with the ACTUAL off-diagonal C_p and B_h,
tail floor delta and profile floor d. Completing those two squares
reduces to the same full-tail argument as b1c0186, Section 6.

Directed rational LDL has 31 strictly positive pivots in each parity.
The inverse trace bound gives S>=sigma J. With ell=log(2B/H), compute

    mu=H[(ell^2+2ell+2)a^T S^-1 a
                     +2(ell+1)a^T S^-1 c+c^T S^-1 c],
    R_H=300000 H(log(2/H)+10)+110epsilon_G,
    zeta=(sqrt(upper(mu))+sqrt(H R_H^2/lower(sigma)))^2/d.    (15)

This retains the signed logarithmic/constant mixed term. It uses exact
analytic shell integrals and pays the entire remainder. For every h<=H,
B_h^*B_h/d<=zeta S: nonnegative integrated energy increases with the
integration interval, and h R_h^2 increases. This is not a monotonicity
assertion for a rounded signed polynomial. Consequently

    inf_(y,s) q[P_a(l,y,s)] >= (1-zeta)S[l].                 (16)

The infimum is over the full form domain. It will be identified with an
ACTUAL harmonic Schur form in Section 6; S^-1 is only a comparison
inverse, and zeta is not the actual full-core/profile Theta.

The physical all-source bound follows from the comparison inverse
shear and (8): with t_p=tr(J^-1 G_act),

    r^2<=t_p/delta^2+b_H^2/d^2,
    gamma_physical>=min((1-zeta)sigma,delta,d)/(6(1+r)^2).    (17)

The exact outward endpoints in moving_results.json imply

| Quantity | Even | Odd |
| --- | --- | --- |
| sigma | >8.8209*10^-13 | >4.7943*10^-10 |
| zeta | <.001294 | <.00006929 |
| (1-zeta)sigma | >8*10^-13 | >4*10^-10 |
| physical gap (17) | >2.5424*10^-15 | >1.4781*10^-12 |

The theorem weakens the last row to 2*10^-15 and 10^-12. Reflection
splits both the form and original moments into the even and odd
components. Zero extension then supplies (1) for every smaller b.
Failure of an LDL or sufficient comparison inequality would be
UNDECIDED for the actual form, never a negative-source certificate.

## 5. Form domains and the growing hard space

F_a^p denotes the completion of actual parity H1_0 two-Mellin sources
in a positive graph norm of the nonpole form. The full physical kernel
is closed in L2 because its moment functionals are bounded on the compact
support. The profile form domain consists of s for which Y_s is in F_a^p.
The core moment map and finite low projection preserve the core form
domain, as in the pinned endpoint proof. The source coordinates (7)
extend to a Hilbert bijection on the full physical moment kernel.

They also identify the full form domain with the product core/profile
domain. Here are the relevant points from b1c0186, Section 7, with the
range verified again: both diagonal forms are closed and semibounded,
and the entire core/profile coupling (10) is L2-bounded. Hence the
product graph norm is equivalent to the full graph norm. An actual
H1 source has inverse v=u_core+m_s chi_p and s=u|_(B,a), with the
actual gluing v(B)=s(B), s(a)=0. A core with nonzero internal endpoint
trace lies in F_B^p: cut it off in strips of width eta and restore
its O(eta) moment with a fixed interior bump. Squared translate
differences are O(min(r,eta)), giving Gamma energy
O(eta(1+|log eta|)); the bounded remainder tends to zero. This also
puts all finite moment-corrected low polynomials in the core form
domain. Thus no extra zero trace or third moment is imposed. Conversely
finite sums of admissible core and lifted profile approximations lie
in F_a^p, and closure gives the entire product domain.

Define the actual physical hard form space

    H_a^p=V_a^p(E_a^p intersect the product form domain).     (18)

It is the kernel of the bounded low-coordinate map l on F_a^p, hence
closed in the form norm. Its form D_a is the restriction of q through
V_a. For hard coercivity use a SEPARATE Young payment alpha_hard=40:

    D_a[y,s] >=(delta_c,p-c_H^2/40)||y||^2
                   +(2log(2/H)-5-40)||s||^2
              > (2/5)(||y||^2+||s||^2).                    (19)

Both scalar inequalities are checked independently in both parities.
The comparison payment 42 in Section 4 is not substituted into (19).
By (8), every nonzero v in H_a^p has

    q[v] > (1/15)||v||_physical^2.                           (20)

This is a floor for the FULL growing hard space, including every
accumulated shell direction and its interaction with the core tail.
It is not just a statement about a finite tail matrix.

The hard spaces are nested under exact zero extension: if a<=b in
the band, (y,s) embeds as (y,zero-extended s). The moment m_s and the
fixed corrector chi_p do not change. Thus V_b i_(b,a)=J_(b,a)V_a
and H_a^p is a form-closed subspace of H_b^p. The forms agree exactly
on the smaller support. More explicitly, zero extension is an isometry
for the shared graph norm q+20||.||^2. The image of the complete F_a^p
is therefore closed in F_b^p, and the already closed H_a^p remains
closed there. This argument needs no additional assertion equating a
restricted support domain with a form closure. These facts justify
the nested projections used below.

## 6. Actual harmonic lifts and uniform conditioning

Let A_p=q[Z_p .] be the ACTUAL finite low form and let K_a denote
the actual low-to-hard map, so

    q[Z_p l+V_a eta]=A_p[l]+2 Re<K_a l,eta>+D_a[eta].        (21)

It is L2-bounded with

    ||K_a||^2 <= tr(J^-1 G_act)+b_H^2 <9.                    (22)

The two output coordinates in E_a are orthogonal by definition; this
use of a product norm does not assume physical shell output
orthogonality in the near/far proof. The operator associated with
closed D_a is positive and has inverse norm <=5/2 by (19).
Consequently define actual Riesz lifts and actual Schur forms

    T_a=D_a^-1 K_a,          ||T_a||<15/2,
    W_a l=Z_p l-V_a T_a l,
    R_a=A_p-K_a^*D_a^-1K_a.                                 (23)

T_a takes values in the operator domain, hence the hard form domain.
The defining variational equation is D_a(T_a l,eta)=<K_a l,eta>.
It follows EXACTLY, for every form-domain hard eta, that

    q[W_a l+V_a eta]=R_a[l]+D_a[eta],
    q(W_a l,V_a eta)=0.                                     (24)

No numerical inverse of an infinite block is being claimed. Its
existence and these identities follow from the proved actual coercivity
and bounded coupling. Equation (16) supplies the lower bounds for
R_a in Section 1. Also R_a<=A_p, while A_p is positive by the inherited
core theorem. The same two-sided uniform model error e_c used in (9)
also bounds its diagonal from above by A^0_nn+e_c J_nn. Its trace is bounded by
sum_n(2n+1)A^0_nn+31e_c<200, explicitly checked. Hence

    8*10^-13 I < R_a^e <=200 I,
    4*10^-10 I < R_a^o <=200 I                              (25)

in reference norms. All low/low mixed directions remain in R_a.

The triangular coordinate shear (l,eta)->(l,eta-T_a l) and its inverse
have norm <=1+||T_a||<9. Combining this with (8) gives

    (||l||^2+||eta||^2)/162
       <=||W_a l+V_a eta||_physical^2
       <=486(||l||^2+||eta||^2).                             (26)

These constants are independent of a and of any subdivision count.
For a single soft vector the stronger lower bound
||W_a l||^2>=||l||^2/2 follows directly from (8), since its raw low
coordinate is still l.

## 7. Exact moving-endpoint cocycle and near-null variation

Work first in either parity, identifying smaller supports with their
exact zero extensions. Since q is positive on F_(B+H), it is a Hilbert
inner product there (equivalent to its graph norm by (1)). Let Pi_a
be its q-orthogonal projection onto H_a. Nesting gives

    Pi_a Pi_b=Pi_b Pi_a=Pi_a, a<=b,
    W_a l=(I-Pi_a)Z_p l,
    W_b l=(I-Pi_b)W_a l.                                    (27)

Thus the change of a soft lift is the actual hard increment

    W_a l-W_b l=(Pi_b-Pi_a)Z_p l in H_b intersect H_a^(perp_q),
    (R_a-R_b)[l]=q[(Pi_b-Pi_a)Z_p l]>=0.                     (28)

In particular the soft Schur matrices decrease, consistently with
zero-extension variational monotonicity. The result does not assert
that a true physical gap increases when a better lower bound is found.

For a partition B<=a_0<...<a_m<=B+H, the increments in (28) are mutually
q-orthogonal, and

    sum_j q[W_(a_j)l-W_(a_(j+1))l]
       =R_(a_0)[l]-R_(a_m)[l] <=A_p[l],
    sum_j ||W_(a_j)l-W_(a_(j+1))l||_physical^2 <=15 A_p[l].  (29)

The second inequality uses the physical hard floor (20) at the larger
endpoint for each increment. It controls total squared variation; no
Lipschitz rate or non-summable extension is asserted.

In coordinates there is an equally explicit transport law. With i the
isometric raw hard embedding, zero extension from a to b sends

    (l,eta)_a -> (l, i eta+Delta_(b,a)l)_b,
    Delta_(b,a)=T_b-i T_a,
    Delta_(c,a)=Delta_(c,b)+i_(c,b)Delta_(b,a).               (30)

The norm of Delta is <15. The transition map and inverse on its image
are bounded by 16. Because of the exact cocycle, a sequence of
transitions has the same endpoint bound 16; a product of per-step
worst-case losses is not accumulated. This is a concrete finite-band
reserve transport law, in the actual form, alongside the energy law
(28). The checker checks the scalar shear constants; the infinite
projection identities (27)-(30) are the analytic proof, not a finite
numerical projection test.

For the distinguished near-null direction keep exactly the inherited
physical degree-62 even source v_B of the near-null source and direction
packages. Its moment is exact and its nonconstant degree makes it
nonzero. As a degree-62 even Mellin-null polynomial it has the unique
representation v_B=Z_e l_v, with l_v in K_e. The polynomial itself and
its physical normalization are not changed. Its pinned bounds are

    E_v=q[v_B] <5.45324*10^-13,
    N_v=||v_B||^2 >.16543536.

Define n_a=W_a^e l_v. This is the soft coordinate projection of the
SAME embedded physical source:

    Jv_B=n_a+Pi_a Jv_B,    q[n_a]<=E_v.

Since ||M||^2<2, ||l_v||^2>=N_v/2, and (8) gives
||n_a||^2>=||l_v||^2/2>=N_v/4. Therefore

    0<q[n_a]/||n_a||^2 <=4E_v/N_v <14*10^-12,
    sum_j ||n_(a_j)-n_(a_(j+1))||^2 <=15E_v<8.2*10^-12.     (31)

These are uniform analytic bounds for the moving coordinate direction,
not a selection of a new physical witness at each endpoint.

Finally, on the all-parity low coordinate space K_e direct-sum K_o,
take the reference-orthogonal decomposition

    K_N=span(l_v,0), K_L=K_N^(perp_ref),
    N_a=W_a K_N, L_a=W_a K_L, H_a=H_a^e direct-sum H_a^o.    (32)

This proves (2) and the dimensions 1,61,infinity. The reference
orthogonality preserves the conditioning bounds (26); there is no
small-energy normalization of l_v. Only the combined soft space is
q-orthogonal to H_a. N_a and L_a need not be q-orthogonal: their
entire mixed term is retained in R_a, bounded by (25) and by
|R_a(x,y)|^2<=R_a[x]R_a[y]. Thus (32) does not silently discard a
near-null/low interaction.

## 8. What has been renewed, and what remains open

Within the named band the construction controls the quantities asked
for at the moving-endpoint front:

| Quantity | Uniform finite-band control |
| --- | --- |
| Soft dimension | 31 per parity; distinguished inherited line plus 61 other coordinates |
| Full coordinate conditioning | squared bounds 1/162 and 486 |
| Complete growing hard block | reference floor >2/5; physical floor >1/15 |
| Complete corrected profile | >2log(2/(a-B))-5 |
| Low/full-hard coupling | operator norm <3 |
| Core/profile coupling | full moment-corrected tail norm cap 87/25 |
| Low/profile remainder | (12), retained uniformly through H=10^-10 |
| Two moment correctors | fixed exact chi_e,chi_o; accumulated moments unchanged by extension |
| New active channel | q=5 included in all mixed terms; q=7 excluded by directed geometry |
| Near-null change | actual nested projection identities and the budget (31) |
| Successive endpoint maps | exact cocycle; norm bounds 16 independent of subdivision count |

The construction absorbs new shells into an existing infinite hard
space. It proves a uniform decomposition at each endpoint in the band,
without rebuilding Legendre coordinates at the new physical length.
The old endpoint data still anchor the quantitative comparison. This
distinction is essential: after B+H one must certify a new band or a
stronger joint profile bound. Equation (30) alone supplies no such
extension, no uniform absolute positive step for arbitrarily many
steps, and no divergent sum of certified step widths.

The next open gate is quantitative renewal beyond this finite band:
control an accumulating or re-anchored hard/profile system and its
soft comparison so that total certified progress reaches a prescribed
larger endpoint. No spectral transport to the 7-channel threshold,
Connected Unit-Window Coercivity or Object X is claimed here.

The parallel a0ea6f8 package has already supplied a different useful
ingredient: a physical moving high-tail floor >1/41 on the entire
interval B<=a<=1, with tail starts 384/385 and 191 remaining low
coordinates in each parity. Its larger moving low block and its
couplings are still open. Our 31-coordinate accumulated-profile
construction proves all block bounds on a much smaller actual band;
it does not promote that separate 191-coordinate theorem to all-source
positivity up to one. Both results remain available without identifying
their different hard spaces or combining incompatible constants.

## 9. Reproduction and epistemic status

`check_moving.py --verify` uses only Python standard-library integers,
Fractions and the pinned directed grid 10^-200. It checks all 111 input
bindings, replays b1c0186 and the complete earlier chain, rebuilds both
full core Grams, recomputes both coupling-vector triples, verifies the
62 new positive comparison pivots, all profile/remainder losses,
physical gaps, hard floors, coupling/conditioning constants, and the
inherited-source scalar variation bounds. JSON and log must reproduce
byte for byte, and all seven payload SHA-256 hashes must match.
The new ledger contains 80 passing exact checks in addition to the
inherited chain and the explicitly stored positive pivots.

The numerical ledger does not independently prove the analytic
primitive, complete form-domain, comparison or infinite Riesz-projection
arguments. Those are supplied above and in the bound input proofs.
Successful exact replay is arithmetic reproduction, not independent
analytic audit. Status remains **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Publication adds eight package files and an append-only ladder update
on the research branch, preserving all historical and concurrent work.

## 10. Append-only reproduction note for parallel a0ea6f8

The parallel `moving-endpoint-uniform-high-tail-2026-09-19` package
publishes a 25-check JSON/log pair. At its pinned a0ea6f8 bytes these
are the outputs of `--math-only`: that mode omits the additional
successful input-binding check from the serialized check list. The
ordinary `check_tail.py --verify` instead computes 26 checks, including
the binding check, and therefore fails its byte comparison with that
published 25-check JSON before reaching its hash loop.

Both parts can nevertheless be reproduced without changing any old file.
From the repository root run these TWO commands:

```text
python -B research/x-c1/moving-endpoint-uniform-high-tail-2026-09-19/check_tail.py --math-only --verify
python -B research/x-c1/moving-endpoint-uniform-high-tail-2026-09-19/check_tail.py
```

The first reproduces the published 25-check JSON/log and all seven
package hashes. The second passes all 26 checks, including bytes,
SHA-256 and Git blobs for all four bound inputs, without overwriting
anything. Both were run successfully for this addendum. Thus the
ordinary combined verify command has a mode-dependent serialization
mismatch, not an observed arithmetic or input-binding failure. This
qualification is append-only; the parallel theorem and its files are
preserved. These separate reproduction observations are not included
in our 80-check ledger or its 111 mathematical input bindings, and the
parallel theorem is not needed for (1)-(32).
