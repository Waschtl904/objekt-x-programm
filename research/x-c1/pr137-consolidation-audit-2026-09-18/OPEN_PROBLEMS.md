# Open problems and a correction to the proposed shell decomposition

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.** No new endpoint theorem.

## O1. The H1_0 shell split is not yet justified

The frozen `window-gap-monotonicity-2026-09-18/PROOF.md` Â§5 calls
E=J_(B,b) W_B^even a closed isometric copy and writes
W_b^even=E direct-sum Z with L2 orthogonality. Its use as an automatic
Hilbert-space decomposition needs correction. W_B is an H1_0 source
space, not an L2-complete Hilbert space. E is not closed in ambient L2.
Although it is relatively L2-closed among the H1_0 sources, that fact
does not give an orthogonal direct-sum decomposition of this incomplete
space. The concurrent `pr137-consolidated-milestone-2026-09-18/OPEN_PROBLEMS.md`
at `21fade97f35089617d07a111ab64082404084319` repeats the proposed split;
the same correction applies to that open-problem formulation. It does
not affect its stated positive milestone.

Here is a direct obstruction for every 0<B<b. Work in physical
coordinates, with h(x)=cosh(x/2). The L2 closure of E is
\[
\overline E^{L^2}=\{f\in L^2_{\rm even}(-b,b):
\operatorname{supp}f\subset[-B,B],\quad
\int_{-B}^B f h=0\}.
\]
Density follows by even compact smooth approximation inside (-B,B),
then subtracting a fixed even compact smooth bump with nonzero h-moment
to correct the vanishing approximation error in the moment.
Nonclosedness follows, for example, from the discontinuous function
1_(|x|<B/2)-c 1_(|x|<B), where c is chosen to make the h-moment zero.
It lies in this closure but not in H1.

The unique L2 projection onto this closure is
\[
P_{\overline E}u
=1_{|x|<B}\left(u(x)-
\frac{\int_{-B}^B u h}{\int_{-B}^B h^2}h(x)\right).
\]
Choose an even u in C_c^infinity(-b,b) with u(B)=1 and with h-moment
zero separately on the core and the shell. Such a u exists: start with
an even smooth bump crossing +/-B, subtract an even bump supported
strictly inside the core to cancel the core moment, and then an even
bump strictly inside the shell to cancel the shell moment. The two
corrections do not change u(B). Parity makes the sinh moment zero.
Thus u lies in W_b^even. For this u,
\[
P_{\overline E}u=1_{|x|<B}u,
\]
which jumps at +/-B and is not H1. If u=e+z with e in E and z in
W_b^even orthogonal to E, continuity of the L2 pairing makes z
orthogonal to the closure, forcing e=P_(closure E)u. This is impossible.
Consequently the stated orthogonal split does not hold for every H1_0
source as written.

This defect is confined to the *proposed next shell construction*.
The monotonicity theorem in Â§Â§1-4 uses only nested admissible sets and
exact zero extension; it does not use that split. The existing endpoint
certificates use Legendre low/tail decompositions in the explicitly
larger closed form domain, not this H1_0 core/shell projection.

A repair must either work in a suitable closed constrained form domain
and prove the required projections/domain properties and return to H1_0,
or construct admissible coordinates with explicit trace and moment
matching. A minimal L2 core correction proportional to h typically
fails the zero-trace condition. Pure shell bumps plus an arbitrary
moment correction are not automatically a complete decomposition.
This note does not claim to have supplied the repair.

## O2. Full-core shell positivity beyond B

After resolving O1, define meaningful form blocks, prove D_b>=delta I>0,
and control the coupling on the ENTIRE old core, including its
complement to any chosen near-null vector. The exact sufficient relative
condition, when its operators/forms are well defined, is
\[
C_b^*D_b^{-1}C_b\preceq(1-\varepsilon)A_B,\qquad\varepsilon>0.
\]
One must still control the inverse change of coordinates, source norms,
all unbounded-domain issues and any new moment remainders.

The number R_B~3.29629e-12 is an UPPER bound on the variational gap,
not an available uniform reserve. A coarse scalar subtraction may be
compared to the CERTIFIED lower bound 10^-13 as a sufficient criterion,
or a sharper relative bound may exploit direction-dependent reserves.
A subtraction merely less than 3.3e-12 is not sufficient for all sources.
For a unit near-null test vector, its own threshold is R_B, a separate
statement. A local right interval would not alone cover log(7)/2 or 1.

## O3. Separate three possible outcomes

1. A lower comparison bound is nonpositive: that comparison failed.
2. An interval computation cannot decide: that certificate is undecided.
3. An actual admissible source has a strictly negative upper energy bound:
   that disproves positivity of the specified form on that source class.

Case 3 cannot be repaired by giving the same form on the same source
class a new factorization or by invoking C15. Before drawing conclusions
about the classical Weil criterion or RH, independently verify the
imported form identity, normalization, domain and admissibility. This
package establishes none of these negative outcomes and makes no RH
claim. Case 1 is not Case 3.

## O4. Audit and broader construction

Independent review of the frozen imports and the three endpoint
certificates remains open. The five stale historical manifests are
explicitly recorded, not silently cured. The old anonymous/scoped
positive review is not an independent review of the new endpoints.

All-source positivity at log(7)/2 and a=1, a canonical full C1 readout,
the C0/C1 mediator, full C1-GEOM, global geometry, Object X and RH remain
outside the consolidated positive milestone. Nothing here shows that
no further structural idea is needed.

A later shell investigation may use a separately scoped PR after an
explicit decision. No such PR is created here. No merge or status
promotion is implied by this consolidation.
