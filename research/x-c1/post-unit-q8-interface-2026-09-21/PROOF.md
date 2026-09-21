# POST-UNIT-Q8-HORIZON-INTERFACE - proof-obligation anchor

2026-09-21. OPEN / EXTERNAL_REVIEW_OPEN.

This file is the lifecycle anchor for an interface package. It is not a new
theorem and does not promote positivity beyond the already merged terminal
horizon 1.

## Inherited proved input

The package may use the merged fixed-horizon C1 results on
\[
B=\frac12\log5\le a\le1:
\]
the coupled Prime/Gamma mediator, zero-extension intertwining, compact defect
identity, the strict terminal reserve at 1, and the single terminal correction
\[
\Delta_1=(I-R_1^*R_1)^{1/2}.
\]
Those proofs are not reopened here.

## Two horizon variables

Use a for a source-window horizon and A for a terminal horizon, with
0<a\le A. The unchanged source core is
\[
W_a=H^1_0((-a,a))\cap\ker E_+\cap\ker E_-,
\qquad E_\pm u=\int u(x)e^{\pm x/2}\,dx.
\]
Let J_{a,b} denote zero extension.

For a terminal horizon A define
\[
\mathcal Q_A=\{q=p^k:\log q<2A\},
\qquad w_q=\frac{\Lambda(q)}{\sqrt q}.
\]
The inequality is strict. At
\[
A_8=\frac12\log8
\]
the q=8 channel is still absent and appears only for A>A_8.

## Raw terminal mediator interface

For fixed A the same terminal family \mathcal Q_A is used for every source
window a\le A. Set
\[
\omega_A=\sum_{q\in\mathcal Q_A}w_q,\quad
c_A(\xi)=\sum_{q\in\mathcal Q_A}w_q\cos(\xi\log q),
\]
\[
s_A=\kappa+2\omega_A,\quad
\mathscr A_A=g+s_A,\quad
m_A=g+\omega_A-c_A,\quad
n_A=\kappa+\omega_A+c_A.
\]
The raw candidates are
\[
T^{[A]}u=\frac{m_A}{\sqrt{\mathscr A_A}}\widehat u,\qquad
D^{[A]}u=\frac{n_A}{\sqrt{\mathscr A_A}}\widehat u.
\]
For a\le A put
\[
H_a^{[A]}=\overline{T^{[A]}(W_a)}^{L^2(\mathbb R,d\xi)}.
\]
Beyond the proved terminal A=1, bounded extension of the sourcewise defect
prescription
\[
R_{a,0}^{[A]}(T^{[A]}u)=D^{[A]}u
\]
and the signed identity
\[
q_a(u,v)=\langle T^{[A]}u,T^{[A]}v\rangle
-\langle D^{[A]}u,D^{[A]}v\rangle
\]
are proof obligations, not claims of this package.

For fixed A the target intertwining is
\[
T_b^{[A]}J_{a,b}=I_{a,b}^{[A]}T_a^{[A]},
\qquad
I_{b,c}^{[A]}I_{a,b}^{[A]}=I_{a,c}^{[A]}.
\]

## Terminal-horizon cocycle

For A<B define first on source-linked vectors
\[
V^0_{A,B}(T^{[A]}u)=I_{A,B}^{[B]}T^{[B]}u,\qquad u\in W_A.
\]
The raw obligation is to prove a bounded extension
\[
V_{A,B}:H_A^{[A]}\to H_B^{[B]}
\]
with
\[
V_{A,A}=I,\qquad V_{B,C}V_{A,B}=V_{A,C},
\]
and old-source intertwining for every a\le A.

When \mathcal Q_A=\mathcal Q_B the map must reduce to literal inclusion.
Across a wall a nontrivial map is allowed. A concrete candidate is the
multiplier ratio
\[
\rho_{A,B}(\xi)=
\frac{m_B(\xi)/\sqrt{\mathscr A_B(\xi)}}
     {m_A(\xi)/\sqrt{\mathscr A_A(\xi)}}.
\]
Its behavior at \xi=0 requires a proved removable-limit argument.

If the bounded defect maps exist, set
\[
C_A=(R_A^{[A]})^*R_A^{[A]},\qquad G_A=I-C_A.
\]
No sign of G_A is assumed. The decisive cross-terminal law is the proof
obligation
\[
\boxed{V_{A,B}^*G_BV_{A,B}=G_A.}
\]
This is signed form congruence, not square-root intertwining.

## Conditional positive mechanism

Only after an independent estimate
\[
G_A\succeq\eta_A I,\qquad \eta_A>0,
\]
has been proved may the single terminal square root
\[
\Delta_A=G_A^{1/2}
\]
be defined. No local source-window square roots are introduced.

If strict reserves and the raw congruence are proved at A<B, the intended
positive transport is
\[
U^X_{A,B}(\Delta_Ah)=\Delta_BV_{A,B}h,
\]
equivalently
\[
U^X_{A,B}=\Delta_BV_{A,B}\Delta_A^{-1}.
\]
The required cocycle and terminal-source law would be
\[
U^X_{B,C}U^X_{A,B}=U^X_{A,C},
\qquad
U^X_{A,B}T_{X,A}^{[A]}=T_{X,B}^{[B]}J_{A,B}.
\]
No equation \Delta_BV_{A,B}=V_{A,B}\Delta_A is asserted.

## q=8 wall

Let
\[
\mathcal Q_-=\{2,3,4,5,7\},\qquad
\mathcal Q_+=\mathcal Q_-\cup\{8\},
\qquad
w_8=\frac{\log2}{\sqrt8}.
\]
The q=8 wall task is to construct the source-linked map from the
\mathcal Q_- mediator to the \mathcal Q_+ mediator and prove the raw cocycle
and signed form congruence on the old source space. The new q=8 contribution
must remain inside the common coupled Prime/Gamma mediator. No independent
positive q=8 Gram block is allowed.

## Firewall

This package establishes notation, candidate maps, and obligations only.
It does not establish positivity for A>1, reuse 191 beyond its proved scope,
prove q=8 wall crossing, or construct a cofinal C1 system. It does not claim
global Object X, global Weil positivity, the full global Weil test class, or
the Riemann hypothesis.
