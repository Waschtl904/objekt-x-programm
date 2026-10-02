# Direct joint odd eigenline: certificate and scope

Status: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`. This is a local research
package. Its numerical conclusion is limited to the comparisons recorded in
the three comparison receipts. No new operator integral or input enclosure is
computed. The full family remains `UNRESOLVED`.

## 1. Unchanged family

The baseline is the sealed adaptive package after the primal-dual Y68
exclusion. Its original files are included byte for byte under
`inputs/baseline/`. The baseline loader checks the eight source bindings and
uses the same Stage-A and Y68 intersections, energy Loewner bounds,
resolvent-factor bounds and physical reference. The physical inner product is
the inherited positive Gram matrix G_B. Its Gershgorin lower bound is checked
strictly positive when an angle is accepted.

The full root box retains every nuisance interval. The five inherited
certified completions are conditional restrictions to their full corrected Y
and the already certified common spectral measures. They are not new
existence constructions. Their five four-coordinate slices retain all other
Y and moment intervals. The eight terminal boxes are exactly the diagnostic
leaves of the earlier adaptive tree. There are 19 cases; the central model is
one of the five completions and is not counted twice.

Dropping some common moment constraints enlarges an outer family and is safe
for a successful enclosure. Failure on that larger family proves no failure
of the actual common family. No failed enclosure is used as an exclusion or
as evidence for a new feasible counterexample.

## 2. Exact scaled pencil

Write L=L_0, G=G_0 and Z=Z_0. For the inherited admissible data, L and G are
positive definite. Set B=L+17G. Then

    M = B L^{-1} B = L+34G+289 G L^{-1} G > 0,
    R = L+34G+289Z.

For D=det(L)>0,

    M_tilde = D(L+34G)+289 G adj(L) G = D M > 0.

The energy determinant enclosure is intersected with the inherited positive
Loewner determinant interval. Scaling by the positive scalar D preserves
both eigenlines and their ordering; the generalized eigenvalues are divided
by D. No inverse of L or M is used in the new directional calculation. The
inverse of the left Y block remains an inherited enclosure in constructing N.

## 3. Maximal eigenline, not an arbitrary root

Let R=[[a,b],[b,d]] and M_tilde=[[p,q],[q,r]]. For v=(s,1)^T, put

    F(s) = (bp-aq)s^2+(dp-ar)s+(dq-br).

This is (Rv)_2(M_tilde v)_1-(Rv)_1(M_tilde v)_2. Its vanishing is
equivalent to the generalized eigenvector equation because M_tilde is
invertible. With Q(s)=(v^T R v)/(v^T M_tilde v), exact differentiation gives

    Q'(s) = -2 F(s)/(p s^2+2 q s+r)^2.

Every accepted starting interval [l,h] has *uniform* certificates

    F(l)<0, F(h)>0, inf_{s in [l,h]} F'(s)>0.

For each admissible datum, continuity gives a root, positive derivative makes
it unique in the interval, and Q'' at that root is strictly negative. For a
symmetric two-dimensional definite pencil, its two stationary projective
lines are the maximum and minimum (or every line if degenerate). A strict
local maximum is therefore its global maximal eigenline. This proves the
branch without relying on a numerically chosen eigenvector or merely on
continuation from the central point. A possible second line at infinity
causes no problem.

Brackets are sought on a fixed rational grid k/1024, -128<=k<=128, followed by
five fixed symmetric intervals. Grid values are enclosures of the entire
data family at a fixed chart coordinate; they are not samples of input data.
The initial endpoint and derivative conditions, not the search heuristic,
are the certificate.

For each fixed admissible datum, interval Newton gives

    s_root in m - F(m)/F'([l,h]).

Intersecting this image with the current interval preserves that root. The
receipt records up to twelve steps and strict inclusion where obtained.
Existence comes from the uniform endpoint signs; it is not inferred from a
nonempty Newton intersection. All arithmetic is rational with outward
rounding. If the initial conditions fail, this implementation returns
UNRESOLVED. That is not a proof that no better bracket or representation exists.

## 4. Direct physical angle

Set u=N(s,1)^T and let c be the same fixed physical reference as before. Then

    cos^2(theta) = (u^T G_B c)^2 / ((u^T G_B u)(c^T G_B c)).

Positive lower norm bounds follow from the checked Gershgorin floor of G_B.
The alternative residual enclosure uses e=u-c and the orthogonal projection
onto the G_B-orthogonal complement of c:

    P_c^perp u = P_c^perp e,
    sin^2(theta) <= ||e||_G_B^2 / ||u||_G_B^2.

Both estimates are recorded and their smaller upper bound is used. The
reported width is **twice** the upper angle to this one common reference.
Consequently it bounds the total common projective corridor. The gate is
strict width<10 degrees, not sin^2(theta)<=0.01. Rational angular bounds are
independently checked with Arb at 768 bits.

## 5. Centered compression and common affine calculation

The second comparison writes N=N_0+E, with N_0 the rational midpoint, and
evaluates

    N^T A N = N_0^T A N_0 + E^T A N_0 + N_0^T A E + E^T A E.

Every interval in A is retained. Symmetric entries are collected once and
identical scalar factors use interval square. The result is intersected with
the original enclosure. Gram-factor diagonals likewise use sums of squares.
There is no replacement of an unknown input by its midpoint.

The third comparison additionally uses affine forms

    x = c + sum_i t_i epsilon_i + error, |epsilon_i|<=1, |error|<=e.

The same symbol is retained for each Y-right entry, each entry of the inverse
Y-left enclosure, and each symmetric full-moment entry. The 156 shared symbols
are propagated through N, G, L, Z and the scaled pencil. Using independent
symbols for the inverse-Y-left enclosure only enlarges the allowed family;
it does not claim to preserve the exact inverse relation to Y-left.

Addition collects shared coefficients. In a product x*y the linear part is
c_x t_y+c_y t_x. Each shared diagonal t_xi t_yi epsilon_i^2 contributes half
its coefficient to the center. A valid remainder radius is

    |c_x|e_y + |c_y|e_x
      + (sum|t_xi|+e_x)(sum|t_yi|+e_y)
      - (1/2)sum|t_xi t_yi|.

Indeed epsilon_i^2-1/2 is bounded by 1/2 and all remaining products use the
triangle inequality. All center and linear coefficients are rounded to 100
decimal places, with the exact rounding error added to the remainder and
that radius rounded upward. Thus finite coefficient storage cannot lose an
admissible value. These are first-order affine forms with rigorous nonlinear
remainders, not a complete higher-order Taylor model.

The three polynomial coefficients retain the same symbols in endpoint and
derivative evaluation. Their common affine enclosures are intersected with
the ordinary interval results. Dependency is therefore preserved across the
coefficients as well as within each coefficient. Some correlations still
reside in bounded remainders; this implementation does not resolve them all.

## 6. Acceptance and boundaries

`check_controls.py` checks exact pencil and Rayleigh identities, positive,
negative and degenerate branch controls, affine rounding, and centered
quadratic evaluation. `audit_receipts.py` independently checks accepted
endpoint signs and Newton images with a separate rational implementation,
and checks the angular bounds using Arb. `replay.py` rebuilds all three
19-case comparisons and compares their bytes with the sealed receipts.

The central conditional improvement is evidence of lost enclosure precision
in the earlier method. Root and terminal failures do not establish structural
openness, a no-go theorem, the necessity of new Y58 or L_B data, or the failure
of every finer subdivision or higher-order model. No new adaptive tree is
run because the tested root and all eight terminal boxes remain unresolved.
No random sampling is used for acceptance. General renewal, A13 positivity,
a cofinal positive family, global Object X and RH remain open.
