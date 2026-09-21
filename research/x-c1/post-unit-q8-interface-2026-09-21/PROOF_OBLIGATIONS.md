# PROOF_OBLIGATIONS - terminal-horizon C1 cocycle and q=8 wall

Status: **OPEN**.

Raw horizon compatibility comes first. Positivity may be attempted only after
the raw interface is proved.

## O0 - inherited firewall

May be used without reopening:
- C1a-COUPLED-SPECTRAL-MEDIATOR;
- C1b-ZERO-EXTENSION-INTERTWINING;
- C1-COMPACT-DEFECT-IDENTITY;
- C1d-COMPATIBLE-POSITIVE-COMPLETION;
- the terminal A=1 reserve and the single Delta_1.

Must not be imported beyond scope:
- positivity at A>1;
- 191 as a new critical dimension;
- local-square-root intertwining;
- P11 fixed-pair Strong Terminal as C1 horizon compatibility.

## O1 - first fixed-channel chamber

For every terminal
\[
1\le A\le A_8=\frac12\log8
\]
use the same family \mathcal Q_-={2,3,4,5,7}. For every source a\le A prove:

1. the full Gamma/Prime signed identity with no omitted active channel;
2. T^{[A]}(W_a)\subset L^2 and the closed H_a^{[A]};
3. bounded extension of the sourcewise defect map R_a^{[A]};
4. fixed-terminal zero-extension naturality
   \[
   T_b^{[A]}J_{a,b}=I_{a,b}^{[A]}T_a^{[A]},
   \qquad
   R_b^{[A]}I_{a,b}^{[A]}=R_a^{[A]};
   \]
5. the corresponding compression law for the signed defect form.

O1 carries no positivity conclusion.

## O2 - raw terminal transport

For 1\le A<B define
\[
V^0_{A,B}(T^{[A]}u)=I_{A,B}^{[B]}T^{[B]}u,\qquad u\in W_A.
\]

Prove:
- well-definedness;
- bounded extension V_{A,B}:H_A^{[A]}\to H_B^{[B]};
- a lower bound if needed to preserve closed range;
- old-source intertwining for all a\le A;
- V_{A,A}=I;
- V_{B,C}V_{A,B}=V_{A,C}.

Inside one channel chamber V must reduce to literal inclusion. Across a wall
it may be nontrivial.

For the multiplier-ratio candidate, prove the removable limit at xi=0 and
global boundedness. Sampling is not a proof.

## O3 - signed form congruence

After bounded defect maps exist, define
\[
C_A=(R_A^{[A]})^*R_A^{[A]},\qquad G_A=I-C_A.
\]
No sign is assumed for G_A.

Prove
\[
\boxed{V_{A,B}^*G_BV_{A,B}=G_A.}
\]

This must be a form congruence, not an operator commutation law and not a
square-root intertwining law. At the q=8 wall it must explicitly use that the
q=8 translation term vanishes on old sources a\le A_8, including endpoint
contact.

## O4 - first chamber terminal positivity

Only after O1-O3 are closed may terminal positivity be attacked for
1<A\le A_8.

Required output at a terminal A:
\[
G_A\succeq\eta_A I,\qquad \eta_A>0.
\]

Rules:
- do not import 191 without a fresh tail/codimension proof;
- do not replace a scalable horizon mechanism by a chain of tiny windows;
- CI, Arb, or a finite matrix is not a theorem without the analytic reduction
  to that matrix at the new horizon.

Failure to prove O4 is not by itself a no-go.

## O5 - terminal positive cocycle

If O3 and strict terminal reserves hold at A<B, define only terminal roots
\[
\Delta_A=G_A^{1/2},\qquad \Delta_B=G_B^{1/2}.
\]
For every source window a\le A define conditionally
\[
T_{X,a}^{[A]}=\Delta_A I_{a,A}^{[A]}T_a^{[A]},
\]
so in particular
\[
T_{X,A}^{[A]}=\Delta_A T_A^{[A]}.
\]
Then define
\[
K_{X,A}=\Delta_AH_A^{[A]},
\qquad
U^X_{A,B}(\Delta_Ah)=\Delta_BV_{A,B}h.
\]

Prove
\[
(U^X_{A,B})^*U^X_{A,B}=I,\qquad
U^X_{B,C}U^X_{A,B}=U^X_{A,C},
\]
and
\[
\boxed{U^X_{A,B}T_{X,A}^{[A]}
=T_{X,B}^{[B]}J_{A,B}.}
\]

Do not replace this by Delta_B V_{A,B}=V_{A,B} Delta_A.

## O6 - q=8 wall crossing

Use
\[
\mathcal Q_-=\{2,3,4,5,7\},\qquad
\mathcal Q_+=\{2,3,4,5,7,8\},\qquad
w_8=\frac{\log2}{\sqrt8}.
\]

Before any post-wall positivity claim:

1. construct the Q_+ raw mediator with the full Gamma term and all cross terms;
2. prove a bounded source-linked wall map from the old mediator to the new;
3. prove the cocycle-compatible signed form congruence on the old subspace;
4. prove the post-wall defect interface on genuinely new sources a>A_8;
5. only then seek a fresh terminal reserve;
6. only after that define Delta_A and U^X.

The q=8 contribution may not be an independent positive Gram channel.

## Success criterion

Success means: raw terminal maps V_{A,B} satisfy cocycle plus signed form
congruence, and independently proved terminal reserves then make
\[
U^X_{A,B}=\Delta_BV_{A,B}\Delta_A^{-1}
\]
a compatible isometric positive transport through the q=8 wall.

Positivity at one isolated larger horizon is insufficient.

## Abort / redirect criteria

Stop the current construction path and record the exact failure if:
- V^0_{A,B} is not well defined;
- no bounded V_{A,B} exists;
- the cocycle fails;
- signed form congruence fails;
- wall compatibility requires an independent positive q=8 block;
- local-square-root intertwining is required;
- only a non-scalable tiny-window chain remains;
- a finite-dimensional reduction imports 191 without a fresh proof.

A rigorously proved strict negative direction of G_A must be recorded as a
scoped candidate no-go, not as an inconclusive numerical failure.
