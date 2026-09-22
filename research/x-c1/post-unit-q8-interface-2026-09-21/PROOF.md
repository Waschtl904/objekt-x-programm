# POST-UNIT-Q8-HORIZON-INTERFACE - proof-obligation anchor

2026-09-21. OPEN / EXTERNAL_REVIEW_OPEN.

This package fixes the type-correct interface for the next C1 phase. It is not
a theorem and does not promote positivity beyond the already proved terminal
horizon 1.

## 1. Inherited input and firewall

May be used without reopening on the proved fixed terminal horizon:
- the coupled Prime/Gamma mediator;
- zero-extension source maps;
- the compact defect identity;
- terminal positivity at 1;
- the single terminal correction Delta_1.

Not imported beyond scope:
- positivity for A>1;
- the number 191 as a new finite critical dimension;
- any square-root intertwining;
- P11 fixed-pair Strong Terminal as C1 terminal-horizon compatibility.

## 2. Source and terminal notation

Let
\[
0<A<B<C
\]
denote terminal horizons and let
\[
J_{A,B}:\mathcal F_A\to\mathcal F_B
\]
be the source zero-extension map when this map is defined for the chosen
closed source spaces.

At terminal A the raw coupled mediator has two outputs
\[
T_A:\mathcal F_A\to\mathcal H_A^T,\qquad
D_A:\mathcal F_A\to\mathcal H_A^D.
\]
The spaces \mathcal H_A^T and \mathcal H_A^D are the corresponding closed
range carriers. They are not assumed equal across horizons and no positive
correction is built into them.

For a terminal channel set
\[
\mathcal Q_A=\{q=p^k:\log q<2A\},\qquad
w_q=\frac{\Lambda(q)}{\sqrt q}.
\]
The inequality is strict.

## 3. TERMINAL-HORIZON-C1-COCYCLE: raw theorem interface

The first theorem must construct two transport families
\[
M^T_{A,B}:\mathcal H_A^T\to\mathcal H_B^T,\qquad
M^D_{A,B}:\mathcal H_A^D\to\mathcal H_B^D
\]
such that on the source-linked ranges
\[
\boxed{M^T_{A,B}T_A=T_BJ_{A,B},}
\]
\[
\boxed{M^D_{A,B}D_A=D_BJ_{A,B}.}
\]

These equations are not definitions by fiat. Before they are valid, the
following must be proved.

### 3.1 Well-definedness on quotient ranges

The source prescriptions descend to the images only if
\[
\ker T_A\subseteq\ker(T_BJ_{A,B}),
\]
\[
\ker D_A\subseteq\ker(D_BJ_{A,B}).
\]
If the carriers are presented as quotient completions, the corresponding
quotient maps and null spaces must be identified explicitly.

No injectivity at a new horizon may be inherited from the terminal-1 theorem
without proof.

### 3.2 Boundedness and extension

The maps first defined on
\[
T_A(\mathcal F_A),\qquad D_A(\mathcal F_A)
\]
must admit bounded extensions to the declared closed carriers. Any lower
bound or closed-range statement later needed for a positive completion is a
separate obligation.

### 3.3 Identity and cocycle laws

For every admissible A<B<C,
\[
M^T_{A,A}=I,\qquad
\boxed{M^T_{B,C}M^T_{A,B}=M^T_{A,C},}
\]
and independently
\[
M^D_{A,A}=I,\qquad
\boxed{M^D_{B,C}M^D_{A,B}=M^D_{A,C}.}
\]

The T- and D-transports must not be silently identified.

## 4. Defect compatibility is a further theorem

If bounded defect transfers
\[
R_A:\mathcal H_A^T\to\mathcal H_A^D,\qquad D_A=R_AT_A
\]
are proved, then the source equations suggest the dense-range identity
\[
R_BM^T_{A,B}T_A=M^D_{A,B}R_AT_A.
\]
Promoting this to
\[
\boxed{R_BM^T_{A,B}=M^D_{A,B}R_A}
\]
requires its own domain, density, and bounded-extension proof.

It does not follow merely from the two source identities.

Likewise the source-form equality
\[
q_B(J_{A,B}u,J_{A,B}v)=q_A(u,v)
\]
must be proved on the declared source class. Across a prime-power wall this
requires checking that newly activated translations vanish on the old
source range exactly where claimed.

No operator congruence, isometry, or positive completion is asserted here.

## 5. FIRST-GLOBAL-CHAMBER-1-TO-LOG8/2

Set
\[
A_8=\frac12\log8.
\]
Because activation is strict,
\[
1\le A\le A_8
\]
has the unchanged terminal channel family
\[
\boxed{\mathcal Q_-=\{2,3,4,5,7\}.}
\]
At A=A_8 the q=8 channel is still absent.

Within this closed chamber the raw spectral formulas have the same finite
Prime family. This makes literal-inclusion candidates for M^T and M^D
plausible, but nesting, quotient compatibility, boundedness, and the two
cocycle laws still have to be proved. No terminal positivity for A>1 is
included in the chamber theorem interface.

## 6. X4-Q8-WALL-CROSSING

Only for
\[
A>A_8
\]
does
\[
q=8=2^3,\qquad
w_8=\frac{\log2}{\sqrt8}
\]
enter.

The post-wall raw mediator must use
\[
\mathcal Q_+=\{2,3,4,5,7,8\}
\]
inside one coupled Prime/Gamma construction, including all resulting cross
terms. No independent positive q=8 Gram block is permitted.

The wall theorem must first construct and prove both
\[
M^T_{-,+},\qquad M^D_{-,+},
\]
including their kernel/quotient descent, boundedness, source intertwining,
and compatibility with the adjacent chamber cocycles.

At the endpoint A_8 itself the old family is still the correct family; q=8
belongs to the theorem strictly to the right of the wall.

## 7. Positive corrections come later

Even a successful raw T/D cocycle does not produce compatible positive
corrected spaces.

At a new terminal A one would separately need, at minimum:
1. a bounded defect map R_A on the correct closed carrier;
2. positivity and a strict reserve for
   \[
   G_A=I-R_A^*R_A;
   \]
3. a justified terminal square root
   \[
   \Delta_A=G_A^{1/2};
   \]
4. kernel/quotient compatibility for the corrected readout;
5. a separately proved transition
   \[
   U^X_{A,B}
   \]
   satisfying
   \[
   U^X_{A,B}T_{X,A}=T_{X,B}J_{A,B};
   \]
6. the U^X cocycle.

No formula such as
\[
\Delta_BM^T_{A,B}=M^T_{A,B}\Delta_A
\]
is assumed. No formula for U^X is promoted before the required square-root,
kernel/quotient, and intertwining proofs are supplied.

## 8. Abort criteria

The present route must stop or be reformulated if any of the following is
proved:
- either source prescription fails to descend to the stated quotient/image;
- no bounded M^T or M^D extension exists;
- either cocycle law fails;
- q=8 compatibility requires an independent positive single-channel block;
- the route requires local square-root intertwining without proof;
- the only continuation mechanism is a non-scalable chain of tiny windows;
- a finite-dimensional step imports 191 without a fresh tail/codimension
  theorem.

A numerical failure is not a no-go. Any negative theorem must receive its own
explicit candidate class and proof.

## 9. Scope firewall

This package establishes types and proof obligations only. It does not prove:
- terminal-horizon C1 compatibility;
- positivity for any A>1;
- the first chamber theorem;
- q=8 wall crossing;
- compatible positive corrections across terminals;
- a cofinal C1 system;
- the full global Weil test class;
- global Object X;
- global Weil positivity;
- RH.
