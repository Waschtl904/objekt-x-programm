# Reduced shell coordinates: Hilbert isomorphism, exact form domains and H1 traces

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Mathematical anchor: `6f24422ee8e074d387e9656e5307b607edb6c809`.
Publication parent: `309f7be2c4d3033ce15e49c497c3698879d61185`.
Branch: `research/x-c1-inherited-resonance-shell-schur-2026-09-18`.

This note isolates the coordinate theorem needed before estimating the reduced
Schur operator. It sharpens the domain statement in Section 8 of the anchor.
There is no new numerical positivity gate, no additional Mellin condition,
and no claim of continuation of all-source positivity beyond B.

## 1. Spaces, scalar products and fixed functions

Let B=log(5)/2, b=B+h, 0<h<=h0=10^-20. Throughout, the CORE scalar product
is the physical L2((-B,B),dx) product, linear in the first argument.
Orthogonality to psi refers to THIS product, not to the core-energy form.

Put H(x)=cosh(x/2), H_B=H(B),
A_mass=(B+sinh B)/2, A_T=A_mass/H_B, M_B=4(H_B-1)/B, and on 0<x<B set

\[
 \chi(x)={1-x/B\over M_B},\qquad
 \psi(x)={H(x)\over H_B}-A_T\chi(x).
\tag{1}
\]

Reflect them evenly on the core. They satisfy

\[
 \int_0^B\chi H=1,\quad\int_0^B\psi H=0,\quad
 \chi(B)=0,\quad\psi(B)=1.
\tag{2}
\]

Zero extensions are used when these core functions enter the physical form.
Let

\[
 \mathcal K_a=\{u\in L^2_{\rm even}(-a,a):\int_{-a}^a uH=0\},
 \quad\mathcal W_a^{\rm e}=\mathcal K_a\cap H^1_0(-a,a),
\]
\[
 \mathcal K_B^0=\mathcal K_B\cap\psi^{\perp_{L^2(dx)}},\qquad
 X=\mathbb C\oplus L^2((B,b),dx),\quad\|(t,s)\|_X^2=|t|^2+\|s\|_2^2.
\tag{3}
\]

The shell norm is on the RIGHT shell only; the reflected physical shell S has
||S||^2=2||s||^2. Define m_s=integral_B^b sH, J=core zero extension and

\[
 \widetilde L(t,s)=t\psi-m_s\chi+S.
\tag{4}
\]

For general (t,s) in X there is no trace s(B). The original H1 lift is the
restriction to V={(s(B),s):s in H1(B,b), s(b)=0}.

The inherited rational estimates used below are

\[
 \|\psi\|^2\ge1/16,\quad\|\psi\|^2\le32,\quad\|\chi\|^2\le18,
 \quad |m_s|^2\le(36/25)h\|s\|^2,\quad\|\widetilde L\|\le8,
\tag{5}
\]

and the completed core and shell forms have respective lower bounds

\[
 \epsilon=10^{-13},\qquad\delta={1\over32\,10^{13}}.
\tag{6}
\]

All norms in (5) of core functions are physical full-core norms.

## 2. The Hilbert-space coordinate theorem

### Theorem 2.1

The map

\[
 \boxed{\Phi_0:\mathcal K_B^0\oplus X\longrightarrow\mathcal K_b,
 \qquad \Phi_0(w,(t,s))=Jw+\widetilde L(t,s)}
\tag{7}
\]

is a bounded linear bijection. Its kernel is ZERO. Its inverse is

\[
 s=u|_{(B,b)},\qquad v=u|_{(-B,B)}+m_s\chi,\qquad
 t={\langle v,\psi\rangle_{L^2(dx)}\over\|\psi\|^2},\qquad w=v-t\psi.
\tag{8}
\]

For N^2=||w||^2+|t|^2+||s||^2, uniformly in the stated h interval,

\[
 \boxed{N^2/32\le\|\Phi_0(w,(t,s))\|^2\le65N^2.}
\tag{9}
\]

### Proof

All displayed maps are bounded in L2 by (5). The core positive-half H moment
of t psi-m_s chi is -m_s, exactly cancelling the shell moment. Hence (7)
lands in K_b. Given u in K_b, the full core moment of u is -2m_s; adding
m_s chi makes it zero. Thus v in K_B, and the PHYSICAL L2 projection (8)
gives w in K_B^0. Substitution proves Phi_0(w,(t,s))=u.
Conversely restriction of (7) to the shell recovers s, hence m_s; then
v=w+t psi and orthogonality recovers exactly t and w. This proves both
inverse identities, uniqueness and the zero kernel.

The upper norm estimate follows from ||J||=1 and ||L_tilde||<=8:
||Jw+L_tilde z||^2<=(1+64)(||w||^2+||z||^2).
For the lower estimate, orthogonality in (8) gives
||v||^2=||w||^2+|t|^2||psi||^2, so

\[
 \|w\|^2+|t|^2\le16\|v\|^2
 \le32\|u_{\rm core}\|^2+576|m_s|^2.
\]

As 1+(20736/25)h<=64, adding ||s||^2 gives
N^2<=32||u_core||^2+64||s||^2=32||u||^2. This proves (9).

For comparison the UNREDUCED map on K_B direct-sum X has kernel
span{(-psi,(1,0))}. That direction has already been removed in (7);
it is not a residual kernel of the reduced map. No physical source was
removed, since (8) represents every u in K_b. QED.

## 3. The closed form spaces being identified

Let q_a be the closed common-jump nonpole form on supported even L2 functions.
On its two-Mellin kernel it equals the physical Weil form. In this small
interval only channels 2,3,4,5 occur and q_a>=-14||.||^2; q_a+15||.||^2 is
an equivalent positive graph norm to the full Gamma energy plus L2 norm.

To avoid an unproved density identification with any larger form domain,
define F_a precisely as the FORM-NORM CLOSURE of W_a^e in this closed physical
form domain. F_a is a closed form space densely embedded in K_a. L2 density
follows from even compact smooth approximation with correction along one
fixed compact smooth bump of nonzero H moment. Taking the form closure does
not add a Mellin condition. The physical source class W_a^e is still the
H1 class defined in (3).

Let a be q_B restricted to F_B. The inherited endpoint inequality and
form-norm passage to limits imply a>=epsilon I on F_B. The cutoff proof in
the anchor gives psi in F_B. Consequently the rank-one L2 projection
P_psi f=<f,psi> psi/||psi||^2 is bounded also in the core FORM norm:
its coefficient is L2-bounded and psi has finite form norm. Thus

\[
 F_B^0=F_B\cap\mathcal K_B^0
\tag{10}
\]

is a closed densely defined form domain on K_B^0. Define a_0 as the
restriction of a to (10), and A_0 as its associated self-adjoint operator.
This is a FORM COMPRESSION. No assertion that an arbitrary operator-domain
projection is automatically invariant is required. In particular a_0>=epsilon I.

Let d be the shell form defined by closing q_b[L s] on V in X as in the
anchor; write F_D for its form domain and D for its associated operator.
Then d>=delta I, and e=(1,0) belongs to F_D, with L_tilde e=psi.
The separate endpoint-cutoff and trace-ramp arguments proving these inclusions
are essential: the original core H1 zero-trace and shell trace restrictions
are not silently extended to all L2 functions.

The cross form c(w,z)=q_b(Jw,L_tilde z) extends to a bounded operator
C:K_B -> X, via c(w,z)=<Cw,z>_X. Briefly, the core actions on fixed psi and
chi have at most L2 logarithmic boundary singularities; the disjoint
core-shell Gamma singularity is the bounded Carleman kernel 1/(r+z),
with weighted Schur integral pi; the remaining kernel is bounded on the
compact distance interval and the finite translations are bounded.
For the kernel remainder one may use |k(r)-1/(2r)|<=1/2 for 0<r<=2:
use the bounds 1/(2r)-1/4<=k(r)<=1/(2r)+1/4 for r<=1, and
k(r)>=0 and the same upper bound for 1<=r<=2.
The anchor supplies the same bounded-extension proof. This is boundedness,
not an estimate small enough to close a Schur gate.

Define C_0=C restricted to K_B^0. Its adjoint is taken with the physical
L2 core product and the trace-plus-right-shell product of X in (3).
Put M=||C_0||<infinity; no small numerical value for M is asserted.

## 4. Exact equality of the form domains

### Theorem 4.1

The restriction of Phi_0 is a topological isomorphism of form spaces

\[
 \boxed{\Phi_0:F_B^0\oplus F_D\ \xrightarrow{\ \cong\ }\ F_b.}
\tag{11}
\]

On this entire product, by sesquilinearity and passage to form limits,

\[
 q_b[\Phi_0(w,z)]=a_0[w]+2\operatorname{Re}\langle C_0w,z\rangle_X+d[z].
\tag{12}
\]

For nu=32(M+1), put E_0=a_0[w]+d[z]. The graph norms satisfy

\[
 E_0+N^2\le q_b[\Phi_0(w,z)]+\nu\|\Phi_0(w,z)\|^2
 \le E_0+(M+65\nu)N^2.
\tag{13}
\]

### Proof

J maps F_B into F_b by the exact window identity and closure of zero-extended
H1 core approximants. L_tilde maps F_D into F_b by the definition of d as
the closure of actual lifted shell sources, using the norm equivalence
between X and the physical lifted L2 norm from the anchor. Thus every
product vector in (11) has image in F_b, and (12) holds by continuity.

The product is complete for E_0+N^2. Its mixed term is bounded in absolute
value by M N^2. Applying (9) gives (13), since nu/32-M=1. Also nu>=32>15,
so q_b+nu||.||^2 is an equivalent positive norm on F_b. It follows from
(13) that the image of (11) is a CLOSED subspace of F_b in its form norm.

It contains every original H1 source u in W_b^e. Indeed the parent H1 lift
supplies w_old in W_B^e and z_old=(s(B),s) in V with u=Jw_old+L z_old.
Set c=<w_old,psi>/||psi||^2, w=w_old-c psi and z=z_old+c e. Then w in F_B^0,
z in F_D, and Phi_0(w,z)=u. Hence the image contains a form-dense set in F_b.
Its closedness proves surjectivity onto F_b. Injectivity and the graph norm
bounds were already established. QED.

This argument identifies precisely the form closure of the ACTUAL sources.
It does not rely on treating H1 as L2-complete, on point evaluation for L2,
or on assuming arbitrary separate pieces retain the original H1 traces.

## 5. The exact preimage of actual H1 sources

The product in Theorem 4.1 is a FORM-domain product. It must not be confused
with a product of the original H1 zero-trace core and arbitrary X.
The following statement gives exactly the actual source subspace.

### Theorem 5.1

Let T_b be the coordinate space of all (w,(t,s)) satisfying

\[
 w\in H^1_{\rm even}(-B,B)\cap\mathcal K_B^0,
 \quad s\in H^1(B,b),\quad s(b)=0,
 \quad\boxed{w(B)+t=s(B)}.
\tag{14}
\]

The core w is NOT required to have zero trace at B. Then

\[
 T_b\subset F_B^0\oplus F_D,\qquad
 \boxed{\Phi_0(T_b)=\mathcal W_b^{\rm e}},
\tag{15}
\]

and the restriction is a bijection with inverse (8). It is a topological
isomorphism for the inherited H1 product topology on T_b and the H1 source
topology on W_b^e, for every fixed b in the stated interval. The L2 norm
bounds (9) still hold on this subspace.

### Proof of the domain inclusions

Every core f in H1_even(-B,B) with zero H moment, even with nonzero boundary
trace, belongs to F_B. Here are details beyond the fixed-function statement
for psi. An H1 function in one dimension is bounded and of bounded variation
on the compact interval. Multiplying by boundary ramps and zero extending
gives approximants with zero endpoint traces. Their difference r_eta is
supported in strips of total length O(eta), with bounded supremum and total
variation uniformly in eta. The latter follows from the product rule:
the ramp derivative has uniformly bounded L1 mass and ||f'||_1 is finite.
Thus ||tau_r r_eta-r_eta||_2^2<=C min(r,eta), proving Gamma-form convergence
with error O(eta(1+|log eta|)). Subtract the small positive-half H moment
of each cutoff times chi to restore the core moment. The correction tends
to zero in form norm, and each corrected cutoff is in W_B^e. This proves
f in F_B and, with the stipulated orthogonality, w in F_B^0.

For s in H1(B,b) with s(b)=0, (s(B),s) belongs to V. Since e=(1,0) belongs
to F_D, the arbitrary independent coordinate
(t,s)=(s(B),s)+(t-s(B))e belongs to F_D as well.

### Proof of the source statement

The positive-half physical core in (7) is w+t psi-m_s chi. Its trace at B
is w(B)+t, using (2). Its shell trace is s(B). Therefore (14) is EXACTLY
the one-dimensional H1 gluing condition across B. Even reflection gives
the identical condition at -B. The outer shell trace vanishes at b and -b.
The piecewise H1 function is consequently in H1_0(-b,b); its global H moment
is zero by (2), and its odd Mellin component vanishes by parity.

Conversely take u in W_b^e and use (8). Its restrictions are H1 and s(b)=0.
Adding the fixed smooth/Lipschitz core correctors preserves core H1, so w is
H1_even. Also w in K_B^0 by Theorem 2.1. At B,
w(B)=u(B)-t=s(B)-t, proving (14). This proves equality in (15).

All operations in (7)-(8) are bounded between these H1 spaces for fixed b:
restrictions, multiplication by fixed H1 functions, and the displayed L2
moment and projection functionals. The condition (14) defines a closed
subspace in the H1 product topology by trace continuity. The explicit inverse
therefore proves the claimed H1 topological isomorphism. QED.

### Why the schematic H1 product in the review is not the theorem

The map (psi-perp intersect W_B^e) direct-sum X -> W_b^e is not even a map
into H1 for all its inputs: (0,e) is mapped to the zero extension of psi,
which jumps at +/-B. Restricting its outputs to H1 would still lose sources.
Choose w_old in W_B^e with <w_old,psi> != 0; such a vector exists by L2 density
of W_B^e in K_B and psi != 0. Then u=Jw_old is an actual admissible source.
Its unique reduced coordinates have s=0,

\[
 t=\langle w_{\rm old},\psi\rangle/\|\psi\|^2\ne0,
 \qquad w=w_{\rm old}-t\psi,\qquad w(B)=-t\ne0.
\tag{16}
\]

Thus the correct reduced w is excluded by an H1_0 core requirement. It is
included in (14), where w(B)+t=0=s(B). This is why both the form-domain
statement and the coupled trace condition matter. Orthogonality removes
one coordinate redundancy; it does not impose an extra physical constraint.

## 6. Precisely defined blocks and the next Schur obligation

The blocks use the Hilbert products specified in (3):

- a_0 is the CLOSED FORM compression of a to F_B^0, with associated A_0;
- d and D are the complete shell form/operator on X, unchanged by reduction;
- C_0:K_B^0 -> X is the bounded cross operator, restricted from C.

These definitions determine all adjoints. An energy-orthogonal core would
be a different coordinate choice with different projection, blocks and
normalization proofs. The constants of this note belong to the L2 choice.

Since D>=delta I, the reduced Schur form is well defined on ALL of F_B^0:

\[
 r_0[w]=a_0[w]-\|D^{-1/2}C_0w\|_X^2.
\tag{17}
\]

It is closed and lower bounded, being a bounded subtraction from a_0.
Its operator is R_0=A_0-C_0^*D^-1 C_0 on Dom(A_0). The open problem is
r_0[w]>=sigma||w||^2 for all w in F_B^0, with sigma>0 on a right interval.
The physical near-null branch and every other reduced-core direction must
be included. This note supplies no such estimate.

For clarity both valid conditional completion routes are recorded:

1. If (17)>=sigma||w||^2 and r>=||D^-1 C_0|| is certified, actual inverse
   shear and (9) yield
   q_b[u]>=min(sigma,delta)||u||^2/[65(1+r)^2].
2. If for all w in F_B^0, z in F_D one proves
   |<C_0w,z>|^2<=theta a_0[w]d[z], with 0<=theta<1, then

\[
 \boxed{q_b[u]\ge{1-\sqrt\theta\over65}\min(\epsilon,\delta)\|u\|^2.}
\tag{18}
\]

For the second statement, bound the mixed term by
2 sqrt(theta) sqrt(a_0[w]d[z])<=sqrt(theta)(a_0[w]+d[z]), then use the
coordinate gaps and the upper norm bound (9). This is the inverse-free
criterion on the CORRECT complete reduced spaces. Its strict hypothesis
remains open; it is not imported from the impossible unreduced hypothesis.

The exact moment identities (2) hold throughout the completions by L2
continuity. There is no omitted moment tail in this coordinate theorem.
The inherited epsilon already contains the prior endpoint's 1+beta division.
The new physical conditioning factor is 65, paid in both routes above.
No inherited norm loss is silently undone or counted twice.

Even a successful even estimate would leave the odd sector beyond B to be
certified separately. No new all-parity endpoint or merge is asserted.

## 7. Evidence and scope

The checker hash-binds the input chain, reruns the inherited 43-check pivot
certificate, verifies the universal coordinate/projection/trace algebra
as coefficient identities in an exact rational Laurent-polynomial ring,
and verifies the rational norm ledger. It does not infer the form closure,
trace theorem, bounded cross operator or infinite-dimensional surjectivity
from finite algebra tests. Those are the analytic proofs above.

Only a new append-only theorem package is published on the research branch.
main remains the PR #137 milestone. Status remains
AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.


## 8. Relationship to the concurrent quotient package

The publication parent `309f7be2c4d3033ce15e49c497c3698879d61185` adds
`reduced-trace-quotient-2026-09-19/`; those six files are preserved.
Its quotient map G, physical L2 projection and conditional reduced
inverse-free constant agree with this note. There is no conflicting choice
of scalar product or removed direction.

The additional statements isolated here are the explicit inverse of Phi_0,
the exact identity of its image with the form-norm closure F_b (Theorem 4.1,
including two-sided graph estimates), and the precise coupled H1 source
preimage (Theorem 5.1). The distinction between the kernel of G and the zero
kernel of Phi_0 resolves the ambiguous schematic statement in the supplied
review. The formal counterexample in (16) concerns that schematic H1_0-product
statement; it is not an objection to the concurrent package's completed
Hilbert-space quotient theorem.

The next coupling estimate remains open in both packages. The concurrent
near-null diagnostic is compatible with (16): projection can give a nonzero
reduced core trace, compensated exactly by the independent shell trace
coordinate. No numerical value of the relative coupling is certified here.
