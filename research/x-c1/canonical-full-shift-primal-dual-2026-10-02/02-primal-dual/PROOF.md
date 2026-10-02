# Primal-dual cross-projector gate: Y68

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Source: `main@b27a18c32058a9a2a4e4c1611a18a67caa586c15`.
The fixed primal functions are the four-pole aggregate candidates a6 at A9
and b8 at A11 from the sealed full-shift package. This gate evaluates only
the two dual source families `c_A=J* b8` and `c_B=J a6`, four poles each.

## 1. Transport and exact cuts

Work with the conjugate-first inner product on `L²((-1,1),dx/2)`.
For chamber lengths A<B, `(Jf)(y)=sqrt(B/A) f(By/A)` for `|y|<A/B`,
and zero elsewhere. Its adjoint is `(J*g)(x)=sqrt(A/B) g(Ax/B)`.
Thus J is isometric and J* is contractive. Neither the raw primal candidates
nor the raw transported functions are silently assumed to satisfy a Mellin
constraint.

Use the exact rational cut key K with `x=log(K/T)/(2A)`, `T=exp(2A)`.
Native keys R from the preceding package become K=R². Transport from a
chamber U to T sends K to `(T/U)K`. A shift by `log(q)/A` sends K to K/q²;
reflection sends K to T²/K. All identities are exact rational identities.
The engine rejects overlapping cuts unless their equality has been bound
to the same exact key. This includes every transported and shifted cell.

## 2. The eight fixed dual candidates

The low source moments are exact polynomial integrals over all transported
cells. Solve the existing low physical model at `Q-conj(z_j)` to obtain one
1024-bit point seed per pole. Apply the same complete aggregate shift-image
construction as in the primal package:

`h=(I-P_(<=N)) S(seed)`.

All low odd coefficients through N are integrated using the preceding stable
Gauss rule with N+1 nodes (degree at most 2N), and exact oddness removes
the even coefficients. The whole piecewise-polynomial h is retained. A fixed
1024-bit scale normalizes it, and a coupled low-plus-one-high solve selects
the point coefficients. The high right-hand side `<h,c>` is included.
The Galerkin model selects candidates only; all acceptance comes from the
complete physical residual. There is no new correction-space search.

All integral arithmetic uses the inherited 3072 bits. Products are composed
on their actual cell before multiplication. The preceding full-shift
logarithm norm proof and its explicit Taylor remainders apply without change.
The dual residual contains all transported source cells and every logarithmic
jump produced by the complete candidate.

## 3. Complete Gamma action on arbitrary piecewise polynomials

The signed primal residual is reconstructed from the frozen whole candidate.
For this purpose a general polynomial-kernel action avoids assuming that
the input itself is high-orthogonal. Define

`T_j(x)=integral_-1^1 (x-y)^j f(y)dy`,
`L_j(x)=integral_-1^x (x-y)^j f(y)dy`.

Then the kernel moment with measure dy/2 is `T_j/2` for even j and
`L_j-T_j/2` for odd j. Prefix polynomial moments evaluate L_j on each cell;
the complete global moments evaluate T_j. These identities include both
low and high components. Small tests compare this construction with direct
piecewise kernel integrals and the preceding separate Legendre engine.
The inherited uniform Gamma model error is paid separately below.

## 4. Physical residuals and the signed correction

Let `m=sinh(Ax/2)`, `M=m^perp`, and let P_M denote orthogonal compression.
For a raw primal candidate w and dual candidate y, their physical versions
are `w_p=w-beta_w e1`, `y_p=y-beta_y e1`. The low parts already lie in M.
Full high orthogonality bounds beta by the inherited entire sinh tail after N.
The saved nonnegative bounds are denoted b_w and b_y.

The exact primal and dual residuals are

`r_p=u-(Q-z)w_p`,
`s_p=P_M c-(Q-conj(z))y_p`.

The primal norm bound rho is inherited unchanged from the sealed package.
The new dual bound sigma is the complete normal-removed model residual norm
plus the normal Taylor remainder, carrier operator error, and uniform Gamma
model error. The source c is represented by the full interval-enclosed fixed
piecewise expression, so its integration uncertainty is retained directly.
P_M c need not be expanded as a separate function: compression is supplied
by the residual argument itself.

For any multiple alpha m, `<y_p,alpha m>=0`. Let r_tilde be the computable
primal model residual after subtracting its chosen normal through degree 81.
Let epsilon_w be the sum of its paid normal-tail, carrier-operator, Gamma-model
and primal-source-enclosure errors. Then

`||r_p-P_M r_tilde|| <= epsilon_w`.

Consequently the directed correction is enclosed by the computed complex
number `S=<y,r_tilde>` with error

`|( <y_p,r_p> - S )| <= (||y||+b_y) epsilon_w + b_y ||r_tilde||`.

The last norm bound is inherited from the same primal model expression;
the new general Gamma formula is algebraically identical to its prior split
low/high evaluation. The source point and its enclosure error are regenerated
using the identical 1024-bit rule. Single-log integrals in S retain all cells.
They use either the local-cell formula or the inherited global polynomial
log moments. A receipt with `signed_integral_method=global` specifies the
latter; absence of that field denotes the original local formula. Both
formulas are checked against each other on small inputs. The entire interval
width, including any cancellation loss, is carried into the final gate.

## 5. Adjoint identity and product remainder

Self-adjointness of Q on M gives exactly

`<P_M c,(Q-z)^(-1)u-w_p>
 = <y_p,r_p> + <s_p,(Q-z)^(-1)r_p>`.

The latter term has absolute value at most `rho sigma/d`, where d is the
inherited certified distance of z to `[0,theta] union [nu,infinity)`.
The distance is the same for the conjugate pole. Returning from w_p to the
fixed raw w adds at most `b_w ||c||`.

The four-pole filter is unchanged:

`f(Q)u=-(1/4) sum_j Re(z_j (Q-z_j)^(-1)u)`.

For a real target c, each linear contribution has the interval-valued center
`Re(-z_j S_j/4)` and the additional error radius

`|z_j|/4 [rho_j sigma_j/d_j + correction_error_j + b_w,j ||c||]`.

The center's entire arithmetic interval is retained in addition to this
radius. In particular, an integral enclosure wider than 1e-15 is not replaced
by its midpoint or rejected solely for missing that optional accuracy target.
Only the final strict directed inequality determines the target outcome.

The scalar filter error is added once per family, as `delta ||c||`, using
the inherited source norm bound one. This accounts for `P u-f(Q)u`.
The saved weighted correction and corrected complex functional include an
additional reporting radius 1e-40, making the independent rational replay
insensitive to serialization of already outward-rounded interval endpoints.
The result encloses the two real linear terms

`L_A=<P_Au_A-a6,J*b8>`,
`L_B=<J a6,P_Bu_B-b8>`.

The thresholds sigma_A<=0.05 and sigma_B<=0.04 bound the product remainder
by approximately 0.01799910. **They do not bound the signed correction.**
Therefore those thresholds alone are not an unconditional GREEN criterion.
A separate small exact counterexample tests this distinction even when the
dual residual vanishes. The actual acceptance test uses the full signed sum.

## 6. Y68 and the conditional next step

With `e_A=P_Au_A-a6`, `e_B=P_Bu_B-b8`,

`K=<a6,J*b8>+L_A+L_B+<J e_A,e_B>`.

The last term is bounded by the already certified geometric product
`eta_A eta_B = 0.0027048135341885444...`. The inherited energy conversion
adds `0.0000093411260...`. Their exact rational bounds and the old center
are taken byte-for-byte from the sealed target receipt.

The strict gate is `lower(L_A+L_B)>-B68`, with
`B68=0.019980144720918858...`. The independent Fraction-only verifier
checks all residue and correction budgets, pole weights, filter errors and
the complete signed Y68 interval. It intersects only Y68 with its existing
certified interval and checks strict separation from the rotated witness.

The directed test passes. With outward decimal rounding,

`L_A+L_B in [-0.0130180923, 0.0130174044]`,
`signed gate margin > 0.0069620524`,
`Y68 in [0.0410706614, 0.0725344674]`.

The exact rational endpoints in gate.json strictly exclude the old rotated
witness. This excludes that completion, not every other completion.

## 7. Conditional angle evaluation and bounded family search

After this strict exclusion, the inherited joint BoxModel is evaluated with
all the Stage-A cross-projector entry enclosures and the new Y68 intersection.
All nuisance-entry uncertainties are retained. This is one evaluation of
the root box; no new subdivision or exhaustive branch-and-bound is claimed.
The squared-sine enclosure is [0,1], so only a trivial total corridor upper
bound of 180 degrees is returned. This is an uninformative outer enclosure,
not a claim that the physical maximizers actually span 180 degrees.
The uniform corridor strictly narrower than 10 degrees remains UNRESOLVED.

Only then is the inherited rational Cayley family probed at seven fixed
fractions of its previous root parameter: 0, 1/2, 3/4, 2/3, 5/8, 7/10, 1/4.
Each accepted completion is checked against both inherited primary and
crosscheck moment data, all Stage-A plus new Y68 entries, corrected transport
positive matrices, the shared exact kernel, and the inherited eigenvalue
and gap enclosures. The samples at 3/4 and 7/10 fail Y68. The five remaining
samples pass these finite common-relaxation checks. They do not assert a full
physical realization of all trial data.

For each noncentral accepted sample u and central reference v, the common
physical Gram matrix G gives

`cos²(angle)=|v*G u|² / ((v*G v)(u*G u))`.

Rational outward square roots and the inherited atan bounds enclose the acute
line angle. When the tangent exceeds one, the reciprocal chart
`angle=90 degrees-atan(cot(angle))` is used with reversed endpoints. Every
accepted noncentral sample has a certified upper separation from the central
sample below 0.822 degrees. The full rational intervals are in counterfamily.json.
These samples provide neither a uniform angle bound nor a new pair separated
by more than 10 degrees. The bounded search is therefore UNRESOLVED.

In particular, the old nearly perpendicular pair no longer proves STRUCTURAL
OPEN for this strengthened relaxation. No general impossibility or global
localization follows from this change. Y58 has not been computed by the new
dual method. A13, Renewal, a cofinal positive family, a global Objekt X and RH
remain outside the claim.
