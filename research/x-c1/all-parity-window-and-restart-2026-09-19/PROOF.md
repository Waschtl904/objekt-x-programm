# Fiftyfold all-parity window and a quantitative conditional restart

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Anchor: `a659047e00d024c0daa3991ea59fd21afd9f8793`.
Matrix origin: `6a16d90b551588572c87e622c21c2df7f7b1adc2`.
The 95 input files, including the complete even and odd certificates and
the universal prime-power family, are bound in `input_bindings.json`.
All norms below are physical L2(dx), unless reference coordinates are named.
Forms are Hermitian and linear in their first argument. Complex sources
are allowed throughout.

Publication context: the concurrent commit
`829019d7e62f936ab4db903bb9c7758edf427609` adds a different shrinking-step
iteration on B<=a<=B+10^-2 with an author-derived positive uniform gap
floor. It is preserved in full and is not an input to this proof or a
claimed external audit. The halving-gap example below does not supersede
or weaken that stronger gap-floor schedule. Our distinct additions are
the fiftyfold actual window and conditional restart estimates on the
larger endpoint range b<=1, including channel 7. For both contributions,
non-summable/macroscopic certified progress remains the common open gate.

## 1. Two distinct results

Put B=log(5)/2. For every nonzero u in H1_0((-b,b);C) satisfying exactly
the ORIGINAL conditions E_+u=E_-u=0, where E_+/-u=integral u(x)e^(+/-x/2)dx,
the following nested all-parity bounds hold:

| Range | Certified physical inequality |
| --- | --- |
| 0<b<=B+10^-19 | Q_W[u]>3*10^-15 ||u||^2 |
| 0<b<=B+4*10^-19 | Q_W[u]>10^-15 ||u||^2 |
| 0<b<=B+5*10^-19 | Q_W[u]>3*10^-16 ||u||^2 |

The last width is fifty times the inherited 10^-20 width. In all three
ranges the odd gap alone is >10^-12. Stronger previously proved bounds
on smaller ranges remain valid. This is finite window amplification.

Independently, this package proves the following conditional restart
theorem with constants uniform in the core endpoint:

**Restart theorem.** Suppose B<=a<1, 0<epsilon<=1, and q_a>=epsilon I on
the closed form space of all actual two-Mellin sources. If

    0<h=b-a<=min(1-a, 2^(-ceil(1600/epsilon))),

then q_b>=(epsilon/2)I on the corresponding complete source form space.
In the full core plus profile coordinates defined below, the actual
Schur subtraction obeys

    Theta=||D^(-1/2) C A^(-1/2)||^2 <49/200<1/4,
    R=A-C*D^(-1)C >=(151/200) A.

This is a uniform analytic one-step mechanism with an explicit gap cost.
It does NOT supply a uniform positive gap over an infinite iteration or
nonaccumulating progress to a distant endpoint. Section 8 exhibits an
actual infinite chain whose guaranteed widths are summable and proves
every finite step only. Connected Unit-Window Coercivity, historical
P11/R43 Strong Terminal, full C1-GEOM, Object X, global Weil positivity
and RH remain open.

No A1, third Mellin condition, source selection, physical source
renormalization, quadrature, or numerical eigenvalue proof is used.

## 2. Exact reserve transport for the larger fixed-core window

Use the complete even and odd core/profile decompositions of the pinned
width and odd packages. The reference low spaces have degrees 2,...,62
and 3,...,63 respectively; their full tails begin at 64 and 65.
J is the low reference norm matrix, J_ii=1/(2i+1). All moment corrections
act on both matrix indices. The matrix A^0, its form error e_c, and
G_act=(1001/1000)G+1001 e_c^2 J are unchanged at the fixed core B.
The full infinite coupling Gram G includes all Gamma, shift, channel and
mixed images by exact analytic integration, as in the pinned proofs.

First recheck the enlarged interval hypotheses, rather than extending
the scope of an old conclusion by assertion. Set H=5*10^-19 and
L(h)=log(2/h). For 0<h<=H, b<1 and 2b<log7; the only channels are
2,3,4,5. The four reflected core input intervals

    (B-log2, B-log2+h), (log3-B-h, log3-B),
    (log4-B-h, log4-B), (B-h,B)

remain disjoint inside (0,B), as checked by directed logarithms. All
same-shell prime shifts vanish since h<log2. Cross-shell distances are
>2B=log5, so shell/shell shifts by these four channels vanish a.e. too.
The complete core/profile couplings from the pinned proofs satisfy

    C_e(h) <= pi/sqrt2 +(5sqrt2/4)sqrt(Bh)
                       +sqrt(2 sum_(q=2,3,4,5) w_q^2)+258sqrt(h) <4,
    C_o(h) <= pi/sqrt2 +(5sqrt2/4)sqrt(Bh)
                       +sqrt(2 sum_(q=2,3,4,5) w_q^2)+720sqrt(h) <4.

The inequalities are checked at H; their right sides increase with h.
They act on the entire physical core, not just the finite low space.
The unchanged moment tail norm estimates then give the high/profile
bound 41/10 in the reference norm. Pay its entire mixed term with
60 p^2, where p=||s|| on the right shell. The effective tail floor is

    delta_p = (original tail floor)_p,lower -1681/6000 >0.

This is EXACTLY the rational denominator used in the parent matrix,
not a rounded decimal or a second rounded lower endpoint. The pure
profile estimates remain

    d_e[s] >=[2(L-8)-h(8L+450)]p^2 >(2L-17)p^2,
    d_o[s] >=[2(L-8)-h(12L+1140)]p^2 >(2L-17)p^2.

Both subtracted losses are <1 at H and are increasing with h. The
profile norm satisfies ||Y_s||^2<4p^2, so the complete physical norm
conversion constant 6 from the parent reference coordinates still holds.
The form-domain proof is unchanged: all its bounded-kernel estimates
hold on this checked range and retain positive profile floors. In
particular the full core carries the boundary trace, with no duplicate
independent trace variable.

For an endpoint width H_j and directed rational L_j^-<L(H_j)<L_j^+,
put d_j=2L_j^- -77, the profile floor left after the payment of sixty.
The low/profile squared bounds, uniform on 0<h<=H_j, are

    b_e,j^2 = H_j[72(L_j^+ +11)+516]^2,
    b_o,j^2 = H_j[110(L_j^+ +11)+1440]^2.

Monotonicity follows by differentiating h[c(L+11)+m]^2: its derivative
is [c(L+11)+m][c(L+11)+m-2c]>0 on the checked interval. Thus the upper
logarithm bound at H_j controls the entire interval, including h->0.
The remaining profile floor only increases as h decreases.

Let S_p,old be the EXACT comparison matrix already verified in the
parent package, with S_p,old>=sigma_p,old J. Its scalar profile deduction
is b_p,old^2/15, where b_e,old=4692*10^-10 and b_o,old=7820*10^-10.
The new comparison matrix is the exact identity

    S_p,j = S_p,old - Delta_p,j J,
    Delta_p,j = b_p,j^2/d_j - b_p,old^2/15,
    S_p,j >= (sigma_p,old-Delta_p,j) J = sigma_p,j J.

No numerical eigenvalue update or unproved approximate inverse is used.
This subtracts a scalar multiple of the norm matrix from an already
certified Hermitian matrix. The checker replays both parent computations,
including their 31-pivot full-tail comparisons, then evaluates this
identity with exact Fractions. It does not claim a separate fresh LDL
factorization for each new scalar shift.

The same NAMED comparison square completion as in the pinned proofs gives

    r_p,j^2 <= tr(J^(-1)G_act)/delta_p^2 + b_p,j^2/d_j^2,
    gamma_p,j >= min(sigma_p,j,delta_p,d_j)/(6(1+r_p,j)^2).

Both shear entries and all norm conversions are paid. The comparison
inverse is not identified with an actual infinite-block inverse.

| H_j | L_j^- | L_j^+ | d_j | even amplitude | odd amplitude |
| --- | --- | --- | --- | --- | --- |
| 10^-19 | 44 | 45 | 11 | 4548 | 7600 |
| 4*10^-19 | 43 | 44 | 9 | 4476 | 7490 |
| 5*10^-19 | 214/5 | 43 | 43/5 | 4404 | 7380 |

The directed physical lower bounds are respectively >3.1737*10^-15,
>1.0792*10^-15, >3.7197*10^-16 for even sources, and >10^-12 in every
odd case. These decimals are explanatory weakenings; the JSON stores
exact outward rational bounds used for every decision. Reflection
invariance eliminates the even/odd mixed form, and the two original
moments split exactly into cosh and sinh moments. Taking the smaller
gap proves Section 1. Exact isometric zero extension covers smaller b.

## 3. Uniform physical identity, moments and new channels

For the restart let B<=a<b<=1, h=b-a<=h_cap=10^-18, L=log(2/h).
The pinned universal family gives the common full-line nonpole form

    q[f]=Gamma[f]-kappa||f||^2
         -sum_(q=2,3,4,5,7) w_q <f,(tau_(log q)+tau_(-log q))f>,
    Gamma[f]=integral_0^infinity k(r)||tau_r f-f||^2 dr,
    k(r)=e^(-r/2)/(1-e^(-2r)),
    kappa=log(8pi)+EulerGamma+pi/2 <6.

For a prime power q=p^j, w_q=log(p)/sqrt(q). Every listed weight is <1.
Because log7<2<log8, this is the entire possible active set for b<=1.
An inactive shift is zero by disjoint support, including equality at the
diameter cutoff, and may be included in the sum. In particular channel
7 is retained through its entrance. Its operator norm is NOT assumed
small at entrance. The non-Gamma remainder has norm <6+2*5=16, so
q>=-16 I. Exact zero extension preserves q and both moments.

Use the proved kernel bounds k(r)<=1/(2r)+1/4,
integral_0^infinity r k(r)dr<5, k(a)<1 for a>=B, and
integral_d^infinity k(r)dr<=log(1/d)/2+21/4 for 0<d<1.
These are inherited analytic estimates, not numerical quadrature.

For p=e,o set H_e(x)=cosh(x/2), H_o(x)=sinh(x/2) on the positive half.
Define boundary-vanishing correctors on 0<=x<=a by

    rho_e=1-x/a,              M_e=integral_0^a rho_e H_e,
    rho_o=(x/a)(1-x/a),       M_o=integral_0^a rho_o H_o,
    chi_p=rho_p/M_p.

Reflect with parity p and extend by zero. Both are H1_0(-a,a).
Their normalizations and moments are exact:

    M_e=4(cosh(a/2)-1)/a >=a/2>2/5,
    M_o=4sinh(a/2)/a-16(cosh(a/2)-1)/a^2 >=a^2/24>2/75.

The inequalities use positive-series or elementary integral lower
bounds, so no cancellation-sensitive evaluation is needed. Uniformly,

| Corrector | supremum | Lipschitz constant | squared physical norm |
| --- | --- | --- | --- |
| even | <3 | <4 | <18 |
| odd | <10 | <47 | <200 |

For s in L2(a,b), let S_s be its parity extension on the two shells,
zero on the core; put p_s=||s||, m_s=integral_a^b s H_p and

    Y_s=-m_s chi_p+S_s,       Psi(v,s)=Jv+Y_s.

Then ||S_s||^2=2p_s^2 and the H_p moment of Y_s is exactly zero.
cosh(1/2)<6/5 and sinh(1/2)<3/5 give

    |m_e|<=(6/5)sqrt(h)p_s,   |m_o|<=(3/5)sqrt(h)p_s,
    ||m_s chi_p||^2<=72h p_s^2.

Thus the original two Mellin conditions are preserved at every endpoint.
Correcting coordinates with chi_p does not change the physical source.

## 4. Uniform complete mixed operator

For any physical L2 core f with parity p, the same Carleman bound as in
the pinned proofs, applied before taking parity signs, yields

    |Gamma(Jf,S_s)|
       <=sqrt2[pi/2+(5/4)sqrt(ah)] ||f|| p_s <3||f||p_s.

The singular same-side kernel is bounded by the Carleman operator
1/[2(r+z)] of norm pi/2; the regular part and opposite half contribute
(5/4)sqrt(ah). For a prime channel, at a right-shell point x>a only
the sample f(x-log q) can lie in the core. The two reflections therefore
give an absolute pairing <=2w_q||f||p_s, even if this sample interval
crosses zero. Summing five channels gives <10||f||p_s. This argument
does not require disjoint input intervals at a variable endpoint.

For d=a-|x| the full Gamma action of a corrector on the core obeys

    |G_chi(x)| <= 2 Lip(chi) integral_0^d r k(r)dr
                  +4||chi||_infinity integral_d^infinity k(r)dr.

Consequently |G_chi_e|<=103+6log(1/d),
|G_chi_o|<=680+20log(1/d). Since a<=1, integration against dx gives

    ||G_chi_e||^2 <=2(103^2+2*103*6+2*6^2)=23834<155^2,
    ||G_chi_o||^2 <=2(680^2+2*680*20+2*20^2)=980800<1000^2.

The non-Gamma part adds <16sqrt18<70 and <16sqrt200<230. Thus the
complete core functionals satisfy

    |q_a(f,chi_e)|<=225||f||,   |q_a(f,chi_o)|<=1230||f||.

These are nonpole pairings; chi_p is not itself claimed to have zero
Mellin moment. Initially test smooth functions, then use these explicit
L2 bounds to extend the functionals. Combining all terms proves

    |q_b(Jf,Y_s)| <=[sqrt2(pi/2+(5/4)sqrt(h))
                           +10+738sqrt(h)]||f||p_s <14||f||p_s.  (1)

The bound holds at h_cap and is monotone below it. It covers the full
core, including every tail and every mixed image. No finite tail
cutoff, orthogonality of shell outputs, or retained endpoint basis is
needed for this restart estimate.

## 5. Uniform profile pivot, including shell self-interactions

Write T(t)=integral_t^infinity k(r)dr. The positive Gamma leakage out
of each interval and the opposite-shell cross estimate give

    Gamma[S_s] >=2[2T(h/2)-h k(2a)]p_s^2.

This follows by keeping the exterior leakage on each shell, whose
minimum is attained at its midpoint (k is decreasing), and bounding the
opposite-shell kernel by k(2a). The inherited elementary estimate is
2T(h/2)>=L-1/2, and k(2a)<1. Pay kappa||S_s||^2<12p_s^2.
Crucially, at a variable endpoint shell/shell prime overlap may be
nonzero. Pay ALL five such terms by the operator norm:

    |sum w_q <S_s,(tau_(log q)+tau_(-log q))S_s>|
                             <=2 sum w_q ||S_s||^2 <20p_s^2.

It follows that q_b[S_s]>[2L-33-2h]p_s^2>2(L-18)p_s^2.
This estimate remains valid exactly at and on both sides of channel 7's
entrance; no continuity of the shift operator in norm is assumed.

For bounded core f, integration of the Gamma kernel from a shell point
x=a+r over the core gives <=log(2/r)+1 after both reflections: indeed
2a+r<=a+b<=2. The five prime terms add at most 10. Cauchy-Schwarz and

    integral_0^h [log(2/r)+11]^2 dr
            =h[(L+11)^2+2(L+11)+2] <h(L+13)^2

therefore imply

    |q_b(Jf,S_s)|<=||f||_infinity sqrt(h)(L+13)p_s.

Expand Y_s=S_s-m_s chi_p and use q_a[chi_p]>=-16||chi_p||^2.
The additional losses are at most

    even: h[(36/5)(L+13)+(36/25)*16*18]
                  =h[(36/5)L+12708/25],
    odd:  h[12(L+13)+(9/25)*16*200]=h(12L+1308).

Both are bounded by h(12L+1400). At h_cap, 42<L<43 and this loss is
<1916*10^-18<1. Its derivative is 12L+1388>0, so uniformly

    d_p[s]=q_b[Y_s] >[2(L-18)-1]p_s^2
                          =(2L-37)p_s^2 >L p_s^2.              (2)

The positive profile pivot is logarithmic in the actual width. No
profile direction or boundary value is excluded from this inequality.

## 6. Actual source domains and conditioning at a moving endpoint

Let K_a^p be the physical L2 parity subspace with zero H_p moment, and
W_a^p=K_a^p intersect H1_0(-a,a). Let F_a^p be its closure in the
closed nonpole form norm q+17||.||^2. This is a closed form space, dense
in K_a^p by smooth approximation with an exact compact moment correction.
Assume the restart hypothesis a_p=q_a|F_a^p>=epsilon I.

Define the full profile form domain by

    F_profile^p={s in L2(a,b):Y_s in F_b^p},  d_p[s]=q_b[Y_s].

The profile map has 2p_s^2<=||Y_s||^2<4p_s^2, hence a closed Hilbert
image; pulling back the closed form gives a closed form domain. Interior
smooth shell functions have actual H1 corrected lifts, so this domain
is dense in L2(a,b). Inequality (2) holds throughout it: S_s=Y_s+m_s chi_p
has finite Gamma energy, so the leakage inequalities apply directly to
the full finite-energy domain. No unproved graph-density of compact
shell profiles is used to restrict that estimate. The associated actual
operator D_p therefore obeys D_p>=L I.

At Hilbert level Psi:K_a^p direct-sum L2(a,b)->K_b^p is a bounded
bijection, with the exact inverse

    s=u|_(a,b),                v=u_core+m_s chi_p.

For N^2=||v||^2+p_s^2, the uniform estimates give

    N^2/2 <=||Psi(v,s)||^2<=5N^2.                              (3)

For the inverse, ||v||^2<=2||u_core||^2+144h p_s^2 and
1+144h<4, while ||u||^2=||u_core||^2+2p_s^2. The forward estimate uses
||Y_s||<2p_s. A sharper anisotropic upper bound needed below is

    ||Psi(v,s)||^2
       =||v-m_s chi_p||^2+2p_s^2
       <=(3/2)||v||^2+(2+216h)p_s^2
       <(3/2)||v||^2+3p_s^2.                                 (4)

We now identify the entire form domain. Zero extension maps F_a^p into
F_b^p by passing from actual source approximants. On F_a^p direct-sum
F_profile^p, (1) gives the exact closed-block form

    q_b[Psi(v,s)]=a_p[v]+2 Re <C_p v,s>+d_p[s], ||C_p||<=14.

With E=a_p[v]+d_p[s], the mixed term is bounded by 14N^2. Thus (3) gives

    E+N^2 <=q_b[Psi(v,s)]+32||Psi(v,s)||^2 <=E+174N^2.          (5)

The product is complete and (5) makes its image form-closed in F_b^p.
It contains every actual H1 source, as follows. Its inverse has internal
H1 core v with zero H_p moment, shell s in H1(a,b), and trace conditions
v(a)=s(a), s(b)=0; the other traces follow by parity. The core is NOT
required to have v(a)=0. Its zero extension has only endpoint jumps,
which are allowed in this logarithmic-energy form closure.

For completeness, cut off v near +/-a in a layer of size eta. The error
g_eta is bounded, supported on a set of size O(eta), and has uniformly
bounded total variation, because one-dimensional H1 embeds in bounded
continuous functions. Hence ||tau_r g_eta-g_eta||_2^2 is bounded by
O(min(eta,r)) for 0<r<1, and by O(eta) for r>=1. Using k(r)<=O(1/r)
near zero and its integrable tail gives Gamma[g_eta]=O(eta log(1/eta)).
The bounded remainder tends to zero as well. The cutoff creates a
moment error O(eta), which is removed exactly with a fixed interior H1
bump of nonzero H_p moment. Thus the internal v belongs to F_a^p.
Then Y_s=u-Jv belongs to F_b^p and s belongs to F_profile^p. This proves
that every W_b^p source lies in the image. By form closure and (5),

    Psi:F_a^p direct-sum F_profile^p -> F_b^p

is an isomorphism of complete form spaces. Conversely the internal H1
conditions v(a)=s(a), s(b)=0 give exactly an actual H1_0 source under
Psi. This pays the quotient/domain conditioning uniformly. There is
one full core and one shell profile, with no independent trace variable.

## 7. Uniform restart Schur bound and retained physical gap

Let N_epsilon=ceil(1600/epsilon) and 0<h<=2^(-N_epsilon). Since
epsilon<=1, N_epsilon>=1600, hence h<h_cap (even 2^80>10^20).
The exact logarithm lower bound log2>1/2 gives

    L=log(2/h)>N_epsilon/2>=800/epsilon.

All preceding uniform estimates apply. On each parity's ACTUAL closed
operators, A_p>=epsilon I, D_p>=L I and ||C_p||<=14. Therefore

    K_p=C_p* D_p^(-1) C_p <=196/L I
                            <(49/200)epsilon I <=(49/200)A_p,
    R_p=A_p-K_p >=(151/200)A_p.

This establishes the full relative Theta bound stated in Section 1.
D_p^(-1) is the true Riesz inverse of the complete closed profile form,
not a finite surrogate. Because the norm estimate is on the entire
physical core, it pays low, high and every mixed block simultaneously;
separate transported endpoint Legendre tail constants are unnecessary
here. Their role is replaced by the assumed full-core coercivity and
the full-core L2 coupling estimate (1), not silently omitted.

For the physical gap, retaining the anisotropic norm (4) avoids an
unnecessary fivefold loss. Young's inequality gives

    28||v||p_s <=(epsilon/4)||v||^2+(784/epsilon)p_s^2,
    q_b[Psi(v,s)]
       >=(3epsilon/4)||v||^2+(L-784/epsilon)p_s^2
       >=(3epsilon/4)||v||^2+(16/epsilon)p_s^2
       >=(epsilon/2)[(3/2)||v||^2+3p_s^2]
       >=(epsilon/2)||Psi(v,s)||^2,

where 0<epsilon<=1 is used in the penultimate line. The domain identity
in Section 6 includes every actual H1 source and the full form closure.
Reflection commutes with the complete form, including every prime
channel. For u=e+o, the two original zero moments imply separately the
zero cosh moment of e and zero sinh moment of o, and q_b[e+o]=q_b[e]+q_b[o].
This proves the all-parity restart theorem without an extra condition.

## 8. An actual iteration, its exact scope and the remaining gate

Start from the enlarged endpoint and certified gap

    a_0=B+5*10^-19, epsilon_0=3*10^-16,
    N_0=ceil(1600/epsilon_0)=5333333333333333334.

Define, for n>=0,

    epsilon_n=epsilon_0/2^n, N_n=2^n N_0,
    h_n=2^(-N_n), a_(n+1)=a_n+h_n.

Then N_n epsilon_n=N_0 epsilon_0>=1600, so h_n is no larger than
the width allowed by the restart theorem. Also h_(n+1)=h_n^2,
h_0<1/2, and 2^n>=n+1 by induction. Consequently

    sum_(n>=0) h_n <=sum_(n>=0) h_0^(n+1)
                     =h_0/(1-h_0)<2h_0=2^(1-N_0).

Since a_0<0.82 and 2h_0<0.01, every a_n<0.83<1 and the right-endpoint
condition is preserved. Induction proves q_(a_n)>=epsilon_n I for
EVERY FINITE n, on the full all-parity source space. No astronomically
large dyadic integer is materialized: the exact exponent and elementary
integer inequalities suffice for this quantified construction.

The constants of this one-step analytic argument are uniform up to 1,
including the entrance of 7, but this particular guaranteed chain stays
below 0.83. It does NOT actually cross that entrance. Its reserve tends
to zero, its endpoint sequence accumulates, and no positive coercivity
constant at the limit follows. These are limitations of the proved
guarantees; they do not show failure of the true form beyond that limit.

The next structural gate is a quantitative reserve renewal or other
width control that supplies non-summable certified progress while
preserving positive core bounds, complete mixed control and the two
moments. The present one-step lemma makes the dependency explicit but
does not close that gate. A failed sufficient scalar/Schur comparison
would be UNDECIDED, never a negative physical source certificate.

The loss of a uniform gap is a limitation of THIS chosen halving
schedule. It is not asserted to be unavoidable for summable schedules;
the concurrent 829019d contribution specifically retains a positive
gap floor on its different accumulating chain.

## 9. Reproduction and epistemic status

`check_restart.py --verify` checks all 95 byte/hash bindings, reproduces
the odd 51 and even 41 checks, including their complete matrix and
infinite-tail computations, and the inherited 38/40/31/28/43/9 chain.
It also runs the universal family's 349 exact algebraic regression
checks and its five payload hashes. The older 381-check parent mentioned
inside that historical JSON is not newly replayed here.

The 88 new exact checks cover enlarged-range hypotheses, exact
scalar reserve transport, both shear entries, all physical conversion
costs, the uniform five-channel estimates, and the integer restart
threshold. Every proof decision uses integers/Fractions and the pinned
directed 10^-200 interval grid. JSON/log reproduce byte for byte; all
seven payload SHA-256 hashes are checked. The manifest binds this proof
and the status documents too.

The checker validates arithmetic and reproducibility, not an independent
formal verification of the analytic domain, kernel or infinite-operator
arguments. Those arguments are stated above for external review. Status
remains **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

This package appends eight files and an append-only transport-ladder
update on the named research branch. No main, Registry, historical
package, PR or merge is part of this publication.
