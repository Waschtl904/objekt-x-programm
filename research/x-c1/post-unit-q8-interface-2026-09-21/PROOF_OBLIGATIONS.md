# PROOF_OBLIGATIONS - post-unit terminal cocycle

Status: **OPEN**.

## O1 - Type the two raw carriers

For every new terminal A, define the closed carriers
\[
\mathcal H_A^T,\qquad \mathcal H_A^D
\]
and the raw maps
\[
T_A:\mathcal F_A\to\mathcal H_A^T,\qquad
D_A:\mathcal F_A\to\mathcal H_A^D.
\]
Prove all domain and completion statements used later.

## O2 - T-transport

On the source-linked image prove that
\[
T_Au\mapsto T_BJ_{A,B}u
\]
is well defined. In particular prove the required kernel inclusion or the
equivalent quotient statement.

Then prove a bounded extension
\[
M^T_{A,B}:\mathcal H_A^T\to\mathcal H_B^T
\]
with
\[
\boxed{M^T_{A,B}T_A=T_BJ_{A,B}.}
\]

## O3 - D-transport

Independently prove that
\[
D_Au\mapsto D_BJ_{A,B}u
\]
descends to the D-image/quotient and extends boundedly to
\[
M^D_{A,B}:\mathcal H_A^D\to\mathcal H_B^D
\]
with
\[
\boxed{M^D_{A,B}D_A=D_BJ_{A,B}.}
\]

Do not identify M^D with M^T without a theorem.

## O4 - Raw cocycles

For all admissible A<B<C prove
\[
M^T_{B,C}M^T_{A,B}=M^T_{A,C},
\qquad M^T_{A,A}=I,
\]
and
\[
M^D_{B,C}M^D_{A,B}=M^D_{A,C},
\qquad M^D_{A,A}=I.
\]

These are the minimum closure conditions for
TERMINAL-HORIZON-C1-COCYCLE.

## O5 - Defect intertwining

If D_A=R_AT_A and D_B=R_BT_B are established with bounded defect maps,
prove on the correct carriers
\[
\boxed{R_BM^T_{A,B}=M^D_{A,B}R_A.}
\]

A source-core equality is not enough; density/domain and extension must be
checked.

## O6 - Source-form naturality

Prove
\[
q_B(J_{A,B}u,J_{A,B}v)=q_A(u,v)
\]
on the declared source spaces, including all active Prime-power channels and
the Gamma term.

At a wall, explicitly prove why a newly activated translation contributes
zero on the old source range where that assertion is used.

## O7 - First closed chamber

For
\[
1\le A\le A_8=\frac12\log8
\]
use exactly
\[
\mathcal Q_-=\{2,3,4,5,7\}.
\]

Prove O1-O6 uniformly/scalably over this chamber. The endpoint A_8 still uses
the old family. No positivity for A>1 is part of O7.

## O8 - New terminal positivity, separately

Only after the raw chamber cocycle is proved may one seek, for a new terminal,
\[
G_A=I-R_A^*R_A\succeq\eta_A I,\qquad \eta_A>0.
\]

Do not import 191 without a fresh analytic tail/codimension reduction.
CI, Arb, or a finite matrix does not replace that reduction.

## O9 - Positive corrected transport, separately

After strict terminal reserves exist, separately prove:
- the correct terminal square roots;
- kernel/quotient compatibility of corrected readouts;
- existence and bounded/isometric properties of U^X_{A,B};
- the intertwining
  \[
  U^X_{A,B}T_{X,A}=T_{X,B}J_{A,B};
  \]
- the U^X cocycle.

No local-square-root intertwining is assumed.

## O10 - X4-Q8-WALL-CROSSING

For the first wall use
\[
\mathcal Q_-=\{2,3,4,5,7\},
\quad
\mathcal Q_+=\{2,3,4,5,7,8\},
\quad
w_8=\frac{\log2}{\sqrt8}.
\]

q=8 is absent at A=A_8 and enters only strictly to the right.

Construct the post-wall coupled mediator and prove both raw wall transports
M^T and M^D, their quotient descent, boundedness, source identities, and
compatibility with the chamber cocycles before any post-wall positivity claim.

## Success criterion

The raw success criterion is not q_A>0 at one larger terminal. It is a
type-correct scalable pair of T/D transport functors with the source
intertwinings and both cocycle laws.

The positive success criterion is later and requires independent terminal
positivity plus separately proved corrected-space transports.

## Abort / redirect

Stop the candidate path if a rigorous argument shows failure of quotient
descent, boundedness, either raw cocycle, or coupled q=8 wall compatibility.
Do not relabel an inconclusive estimate as a no-go.
