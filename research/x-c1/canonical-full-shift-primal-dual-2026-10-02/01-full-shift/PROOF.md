# Full shift-image corrected resolvent: analytic certificate

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Source: `main@b27a18c32058a9a2a4e4c1611a18a67caa586c15`.
This text specifies the certificate used by the local computations. Numerical
acceptance, tested correction spaces, and output hashes belong to the result
receipt. It does not assert a positive outcome for the target gate.

## 1. Whole high functions

Work in the odd part of `L²((-1,1),dx/2)`, with
`e_n=sqrt(2n+1) P_n`. The inherited cutoffs are `N=593` at A9 and `N=571`
at A11. For the fixed low candidate `w_z`, each active channel is represented as

`psi_q = c_q [w_z(x+d_q) + w_z(x-d_q)] - P_(<=N) c_q [w_z(x+d_q)+w_z(x-d_q)]`,

where every shifted function is zero outside its original interval. Each
`psi_q` is a finitely described piecewise polynomial. Its complete Legendre
tail above N is retained. Oddness makes every even coefficient vanish.
The remaining low coefficients are exact polynomial integrals, enclosed by
Arb Gauss quadrature with N+1 nodes. Their integrands have degree at most 2N.

Cuts use exact rational labels `R`, with `x=-1+log(R)/A` and `exp(2A)=T`
(`T=9` or `11`). Translation by `log(q)/A` maps `R` to `R/q`.
Reflection maps `R` to `T/R`. This identifies coincident cuts algebraically;
overlapping numerical balls alone are not accepted as equal cuts.

Candidate arithmetic remains 1024 bits; the existing operator-integral
arithmetic remains 3072 bits. Point candidates and normalizing scales are
fixed dyadic numbers. Interval Galerkin matrices only select these candidates.
Their complete residuals supply the certificate.

An optional diagonal-response candidate uses exactly the earlier 128 capture
degrees I, without enlarging them. With a fixed nonzero dyadic approximation
`alpha` to `1/(H_max(I)+1+q0-z)`, form

`chi = alpha psi + sum_(n in I) b_n e_n`,

where b_n are fixed 1024-bit approximations to
`[(H_n+q0-z)^(-1)-alpha] <psi,e_n>`. Outside I the complete tail is exactly
`alpha P_(>max(I)) psi`. The candidate is the inherited low vector plus chi.
The extra constant 1 in alpha is a candidate choice, not a spectral theorem.
Both the diagonal approximation error and the feedback into the low block
remain in the complete residual. No assertion of an exact inverse is used.

## 2. Complete operator action and its domain

The inherited raw model is

`Q^P = D_H + q0 + V - Gamma^P - S`,

where `D_H P_n=H_n P_n`, `V=-log(1-x²)/2`, and S is the full sum of
zero-extended weighted shift pairs. On piecewise polynomials,

`D_H f(x) = (1/2) integral_-1^1 [f(x)-f(y)]/|x-y| dy`.

Polynomial division on each cell gives an exact polynomial part and finitely
many terms `p(x) log|x-c|`. Interior jumps must be included. They are not
discarded as a tail error. The implementation combines the endpoint terms
of D_H with V before evaluating the formula.

These expressions belong to L², since all singularities are logarithmic.
Pairing the symmetrized kernel with each P_n gives the coefficient
`H_n <f,P_n>`. Consequently the computed L² function represents the diagonal
operator D_H applied to f, and f lies in its operator domain. This argument
does not require a coefficient asymptotic law.

For the polynomial Gamma model of degree M<N, full high orthogonality
annihilates the even kernel powers. For odd j,

`integral |x-y|^j f(y) dy/2 = integral_-1^x (x-y)^j f(y) dy`.

The right side is evaluated by exact polynomial beta integrals and prefix
moments, with every cell retained. A separate antiderivative construction and
direct small kernel integrals provide checks. The inherited uniform Gamma
operator-model error is additionally paid in the final residual.

## 3. Stable complete norms at the same precision

Repeated translations can have very large global monomial coefficients even
when their norm on an active cell is modest. Ordinary products are therefore
formed after composing each factor with that cell's affine coordinate.

For logarithmic norms, map each cell to `s in [-1,1]`. Endpoint logarithms
are retained exactly as `log(1+s)` or `log(1-s)`, with the scale constant
absorbed into the polynomial part. Subdivide a cell until every other cut
has `rho=|h/(m-c)| <= 3/4`, where m is its midpoint and h its half-width.
For such a cut,

`log|m-c+h s| = log|m-c| + sum_(k=1)^L (-1)^(k+1) [h/(m-c)]^k s^k/k + E(s)`,

with the explicit uniform bound

`|E(s)| <= rho^(L+1)/((L+1)(1-rho))`.

For a local polynomial coefficient `q(s)=sum q_j s^j`, multiply this bound
by `sum |q_j|`. Choose L by a directed inequality, with a total local
uniform error budget of `2^-100`. This is an approximation of elementary
logarithms used in integration; it is not a Legendre cutoff or a change in
candidate precision.

Only a polynomial and at most two endpoint logarithms remain. Their squared
norm is evaluated analytically. Single-log moments use explicit primitives.
For a product of two logs, subtract the polynomial mean and integrate by
parts. The resulting primitive vanishes at both endpoints, so all boundary
limits are finite. The remaining scalar primitives involve real dilogarithms.

If the computed approximant has squared norm in I and the aggregate L²
remainder is at most e, the actual norm is enclosed by

`[max(0,sqrt(inf I)-e), sqrt(sup I)+e]`.

Every arithmetic ball and this analytic remainder are retained. The code
checks the final squared-norm enclosure before accepting it. Exact oddness
may halve the domain; it follows from the source and all applied operations,
and the implementation additionally guards every reflected polynomial and
log coefficient. The full-domain and halved small-case computations agree.

## 4. Physical compression and resolvent errors

Let `m(x)=sinh(Ax/2)` and `M=m^perp`. The finite physical source and low part
already satisfy the Mellin constraint. A raw high correction h is made physical
by subtracting `beta e_1`, where `beta=<m,h>/<m,e_1>`. Since h is orthogonal
through degree N,

`|beta| <= ||h|| (A/2)^(N+2) / [(N+2)! (1-(A/2)^2/((N+3)(N+4))) <m,e_1>]`.

The numerator is the uniform Taylor remainder of m after degree N.
The candidate solve may omit this tiny carrier term; the full certificate
pays both its operator residual and its distance from the raw candidate.

For a raw candidate W, form `r=u0-(Q^P-z)W`. Any multiple of m may be removed
before taking a norm because orthogonal compression to M annihilates m.
The implementation removes `<e_1,r> m/<e_1,m>` using an odd Taylor polynomial
through degree 81 and adds the full degree-83 remainder to the norm bound.

The accepted residual upper bound rho includes:

- the complete model residual and the normal's Taylor remainder;
- the inherited uniform Gamma model error times the candidate norm;
- the physical carrier correction times an upper bound for `||(Q-z)e_1||`;
- the inherited physical source-enclosure error.

For the physical coordinate map `M e_n=e_n-t_n e_1` (odd n>=3),
`||M||² <= 1+sum t_n² = ||m||²/|<m,e_1>|² < 4` in both chambers.
Here `||m||²=sinh(A)/(2A)-1/2`. Thus twice the Euclidean coefficient error
is a valid physical source error; this strict bound is checked separately.

The carrier operator bound uses `D_H e_1=e_1`, exact V² moments, the full
Gamma-model norm, `||S|| <= 2 sum c_q`, and the uniform model error.

The source certificates enclose the spectrum in `[0,theta] union [nu,infinity)`.
For the four upper filter poles `z_k=exp(i(2k+1)pi/8)/300`, the source bounds
give `Re(z_k)<nu`, and each real part is either negative or greater than theta.
Thus the stated directed distance d to these two spectral intervals is valid.
The physical resolvent error relative to the raw candidate is at most

`rho/d + |beta|`.

## 5. Only Y58 and Y68

Keep the inherited scalar filter `f(lambda)=1/(1+(300 lambda)^8)`.
Its partial fractions give the candidate projector column

`p_tilde = -(1/4) sum_(k=0)^3 Re(z_k W_k)`.

The projector error eta is the inherited scalar-filter error plus
`sum |z_k|/4 (rho_k/d_k+|beta_k|)`. All four poles are required.

A separate bound on the same error uses positivity and the inherited gap:
`||(I-P)u|| <= sqrt(S_ii/nu)`. Hence
`||Pu-p_tilde|| <= sqrt(S_ii/nu)+||u-p_tilde||`.
The second norm is integrated in full, using a point source polynomial plus
its separately paid source-enclosure error. The target calculation uses the
minimum of this bound and the resolvent-filter bound. The latter is retained
separately when reporting the improvement of the new resolvent construction.

For A9 and A11, the physical candidate overlap is integrated on the entire
A9 interval as

`K_tilde = sqrt(A/B) integral_-1^1 p_A(x) p_B((A/B)x) dx/2`.

Every transformed cut is included. Since the physical inclusion is a
contraction and the exact projected source columns have norm at most one,

`|K-K_tilde| <= min(eta_A ||p_B|| + eta_B, eta_A + eta_B ||p_A||)`.

The inherited energy conversion adds `sqrt(S_A(ii) S_B(88))/17` to obtain
the Y bound. Intersect only the two requested entries with their previous
certified enclosures. Exclusion is accepted only if

`upper(Y58) < lower(Y58_rotated)` or `lower(Y68) > upper(Y68_rotated)`.

The target script does not invoke the joint odd-angle evaluator. That step
requires a prior strict exclusion. No claim about A13, Renewal, a cofinal
positive family, a global Objekt X, or RH follows from these calculations.

## 6. Scope of a possible primal-dual follow-up

Write `e_A=P_A u_A-a` and `e_B=P_B u_B-b` for the two candidate errors. Then

`K-<a,J*b> = <e_A,J*b> + <a,J*e_B> + <e_A,J*e_B>`.

Only the last term is bounded directly by `eta_A eta_B`. The first two terms
require directed corrections; it would be incorrect to replace the entire
overlap error by this product. For a known target c and a resolvent equation
`Ax=b`, an approximate adjoint solution y_h gives the exact identity

`<c,x> - [<c,x_h>+<y_h,b-Ax_h>] = <c-A*y_h,A^(-1)(b-Ax_h)>`.

This can be applied to the two linear terms pole by pole, using the known
candidate from the other chamber as the target. It additionally requires
certified adjoint residuals, physical compression of the transported targets,
and the scalar-filter and carrier errors. A reported product bound by itself
does not certify these missing linear terms.
