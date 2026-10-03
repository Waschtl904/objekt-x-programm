# Common Y-kernel and second-order odd eigenline

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. This certificate concerns
the existing A9→A11 odd family after the Y68 intersection. Its scope is exactly
the 19 cases in `comparison.json`. The full root family remains UNRESOLVED.

## 1. Unchanged inputs and acceptance

The 59 files of the sealed direct-line package are retained byte for byte in
`inputs/canonical-direct-odd-line-2026-10-02/`, including its 41 inherited
adaptive files. `SOURCE_BINDINGS.json` binds these files and the canonical
source archive at `main@b8924422effe809d8ba51590cf50ca23f3c117b1`.
The five complete points are the existing certified completions; this work
does not construct new feasible points. Each point's full corrected Y and
common spectral measures are checked for inclusion in the inherited family.
Its four-Y slice fixes only Y57, Y58, Y67 and Y68, retaining every other
interval. The eight diagnostic boxes retain their original bounds and are
not a cover of the root family. All cases use the identical physical reference.

The acceptance plan was recorded before the first acceptance run. New
operator integrals, Y58 dual information, L_B data, and adaptive subdivision
are outside this attempt. PR #187 and A13 are separate.

## 2. Exact center and common kernel

On each case write Y_L=A0+ΔA and Y_R=B0+ΔB. A0 and B0 are the exact rational
entrywise midpoints. Rational Gaussian elimination computes A0 inverse.
Multiplication checks A0 A0⁻¹=I and A0 X0+B0=0 exactly, where X0=−A0⁻¹B0.
There is no unaccounted center residual or floating point inverse.

Set H=A0⁻¹ΔA and q=−A0⁻¹(ΔB+ΔA X0). The exact kernel equation is

```math
(I+H)\Delta X=q,\qquad
\Delta X=q-Hq+H^2(I+H)^{-1}q.
```

Each of the 48 Y entries has one shared symbol ε_ij in [−1,1], reused in H,
q, q−Hq and every subsequent operation. Inverse entries are rational constants,
not new independent uncertain inputs. All common terms of degrees one and
two are retained. Rounding discrepancies are included in uniform error radii.

## 3. A componentwise Neumann remainder

Let M_ij be an upper bound for |H_ij| on the entire case box, and let b_ij
bound |q_ij|. Both come from directed enclosures. Define

```math
h=\max_i\sum_j M_{ij}<1,\qquad Q_j=\max_i b_{ij}.
```

The induced infinity norm is submultiplicative, so I+H is invertible on the
whole case. The ordinary columnwise remainder bound is h² Q_j/(1−h).
That bound is valid but wastes the very different row scales: the first
kernel components are much smaller than the last ones, while Z_B amplifies
their errors strongly.

Instead use the nonnegative comparison matrix M. The signed Neumann series
gives, componentwise,

```math
|H^2(I+H)^{-1}q_{:j}|
\le \sum_{k=2}^6 M^k b_{:j}
   + M^7\mathbf 1\,\frac{Q_j}{1-h}=:t_{:j}.
```

Indeed |H^k q|≤M^k b and M^r b≤1 h^r Q_j. Applying M⁷ to the geometric
tail proves the displayed formula. Its finite sums and remaining geometric
factor are computed as exact rational numbers. All t_ij are also checked
against the ordinary columnwise bound. These powers refine the **bound on
the remainder**; no additional polynomial degree or input data is introduced.
The largest certified h over the 19 cases is below 0.007720.

Add t_ij to the model error of X0+q−Hq, then append the two identity rows to
obtain N=[X;I₂]. The resulting enclosure contains the common exact kernel for
every admissible input in the case, not merely for sampled points.

## 4. Rigorous arithmetic of degree two

Each scalar is represented by

```math
x=c+\sum_i l_i\epsilon_i+\sum_{i\le j}q_{ij}\epsilon_i\epsilon_j+r,
\qquad |r|\le e.
```

Stored coefficients and e are integers in units of 10⁻⁷⁰. Addition and
negation are exact integer operations. Multiplication first accumulates all
constant, linear and quadratic coefficients as exact integers, including
both contributions to each shared mixed term. It retains

```math
c_xc_y,\quad c_xL_y+c_yL_x,\quad c_xQ_y+c_yQ_x+L_xL_y.
```

Write l_x=Σ|l_xi| and q_x=Σ|q_xij|, and similarly for y. A uniform radius
for every omitted term is

```math
|c_x|e_y+|c_y|e_x+l_xq_y+q_xl_y+q_xq_y
+(l_x+q_x)e_y+(l_y+q_y)e_x+e_xe_y.
```

This accounts for every degree ≥3 product and every product with an inherited
error. Exact division with remainder rounds stored coefficients downward.
The absolute discarded coefficient fraction is added to e; the resulting e
is rounded upward. Scalar rational multiplication follows the same rule.
Thus negative coefficients, coefficient underflow and accumulated rounding
cannot silently remove an admissible value.

For range evaluation, linear and off-diagonal quadratic monomials lie in
[−1,1]; a shared square ε_i² lies in [0,1]. Its coefficient contributes
[min(0,q_ii),max(0,q_ii)]. This range rule retains signs of shared squares.
All ranges are rational. Python floating point values occur only in progress
printing; no acceptance decision uses them.

## 5. Moments and scaled pencil

The same N models propagate through G=NᵀG_BN, L=NᵀL_BN and Z=NᵀZ_BN.
Each symmetric input entry uses the same symbol in both matrix positions,
with disjoint symbol ranges for G_B, L_B and Z_B. No midpoint replaces a
free input interval. There are 156 possible shared input variables.

The previous centered interval enclosures and their Stage-A/Y68, energy
Loewner, resolvent-factor and inherited moment intersections are retained.
The new model ranges are intersected with them. Each side encloses the same
quantity; an intersection therefore preserves every admissible datum.
Some joint moment constraints remain unused by the polynomial models, which
only enlarges the outer family. Failure on that enlargement is inconclusive.

As in the bound direct-line proof, put

```math
R=L+34G+289Z,\qquad
\widetilde M=\det(L)(L+34G)+289G\operatorname{adj}(L)G.
```

The retained positive Loewner bound proves det(L)>0, and
M~=det(L)(L+17G)L⁻¹(L+17G)>0 for admissible data. Positive scaling preserves
the generalized eigenlines and their ordering. Neither L⁻¹ nor M⁻¹ is
introduced as an independent interval in this calculation.

For R=[[a,b],[b,d]], M~=[[p,q],[q,r]] and v=(s,1), the shared polynomial
models propagate through the coefficients of

```math
F(s)=(bp-aq)s^2+(dp-ar)s+(dq-br).
```

Every product uses the same degree-two arithmetic and pays its higher terms.
The receipt stores all three coefficient models, their errors and ranges.
Endpoint evaluation combines their shared coefficients before bounding.
For derivative evaluation at s=m+δ, |δ|≤ρ, a valid enclosure is the range of
2ma+b enlarged by 2ρ sup|a|, intersected with the ordinary interval result.

## 6. Maximal branch and physical angle

The unchanged rational search grid supplies candidate brackets. Acceptance
requires uniform F(l)<0<F(h) and inf F′([l,h])>0. For every admissible datum
there is exactly one root in that bracket. The generalized Rayleigh quotient
Q(s)=vᵀRv/(vᵀM~v) satisfies

```math
Q'(s)=-2F(s)/(ps^2+2qs+r)^2.
```

At the root Q″<0. For a real symmetric definite two-dimensional pencil,
this is the unique maximal eigenline, not the minimal branch. A possible
other line at infinity does not affect this conclusion. Interval Newton
intersections preserve the root; existence comes from the uniform signs,
not from a nonempty Newton image. Up to twelve steps are recorded.

The physical vector is u=N(s,1), and c is the unchanged fixed reference.
The interval of s is treated as an additional independent variable; this
can enlarge the enclosure but cannot remove the actual root. Its products
with N and G_B retain degree-two dependence and bounded higher errors.
The positive G_B Gershgorin bound and the old interval estimates provide
positive lower bounds for ||u||² and ||c||². Their intersections with the new
model ranges are used in

```math
\cos^2\theta=\frac{(u^TG_Bc)^2}{(u^TG_Bu)(c^TG_Bc)},\qquad
\sin^2\theta\le\frac{\|u-c\|_{G_B}^2}{\|u\|_{G_B}^2}.
```

The second inequality follows by orthogonal projection onto c's complement.
The smaller of the two valid sine bounds is used. The reported physical
width is **twice** the upper angle to c. It is not an eigenline coordinate
width and does not follow from isolation alone. A full uniform certificate
requires root width strictly below ten degrees.

## 7. Verification and boundaries

`check_controls.py` checks exact polynomial values, deliberate coarse
rounding, nonzero inherited errors, cubic and quartic truncation, shared
squares, cancellation, explicit kernel solutions, invalid centers, failed
Neumann conditions and maximal/minimal/degenerate branch examples. These
finite controls supplement the derivation; they do not prove uniformity by
sampling.

`audit_receipts.py` uses separate rational arithmetic to check all 19 center
identities and componentwise tail calculations, trial signs, Newton images
and physical sine arithmetic. Arb at 768 bits independently encloses every
reported angular conversion. The deterministic replay rebuilds all 19 cases,
controls, audit and summary, requiring byte equality with the sealed files.
The inherited small algebra controls are also replayed; the completed large
operator integrations and adaptive tree are not repeated.

Root and all eight diagnostic boxes remain UNRESOLVED. A failed bracket is
not an exclusion, feasible counterexample, structural openness proof, or
failure of every higher model. The conditional improvements and newly
isolated half slice do not imply uniform localization. A new adaptive tree
is not justified by the stated all-eight-isolated criterion. General renewal,
A13 positivity, cofinal positive compatibility, global Object X and RH remain
open. No external review or global verification snapshot is promoted.
