# C1d: terminal square-root positive completion on the fixed horizon

2026-09-20. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Scope: the already constructed coupled spectral C1 system on
\[
B=\frac12\log5\le a\le1.
\]
No horizon beyond \(1\) is treated.

## 1. Inherited fixed-horizon data

For each \(B\le a\le1\), let
\[
W_a=H^1_0((-a,a))\cap\ker E_+\cap\ker E_-,
\]
and let \(F_a\) be its inherited closed form completion. The coupled spectral
candidate supplies a closed subspace
\[
H_a=\overline{T(W_a)}\subset H=L^2(\mathbb R,d\xi),
\]
a bounded isomorphism \(T_a:F_a\to H_a\), literal isometric inclusions
\[
I_{a,b}:H_a\hookrightarrow H_b,\qquad B\le a\le b\le1,
\]
and bounded defect transfers
\[
R_a:H_a\to H,\qquad R_a(T_au)=Du.
\]

The previously proved identities are
\[
T_bJ_{a,b}=I_{a,b}T_a,\qquad
I_{b,c}I_{a,b}=I_{a,c},
\]
\[
R_bI_{a,b}=R_a,
\]
and, for all \(u,v\in F_a\),
\[
q_a(u,v)=\langle T_au,T_av\rangle_H
-\langle R_aT_au,R_aT_av\rangle_H.
\]
Inner products are conjugate-linear in the first argument.

Set
\[
C_a=R_a^*R_a.
\]
The compression identity
\[
I_{a,b}^*C_bI_{a,b}=C_a
\]
is available, but no local square-root intertwining is assumed or used.

The promoted terminal theorem gives a physical coercive bound
\[
q_1[u]\ge\varepsilon\|u\|_2^2,\qquad
\varepsilon=10^{-26},
\]
for every \(u\in F_1\), and the mediator construction gives
\[
\|Du\|_H^2\le s\|u\|_2^2,\qquad s<\frac{23}{2}.
\]

## 2. Strict terminal defect reserve on \(H_1\)

Define
\[
\eta:=\frac{\varepsilon}{23/2+\varepsilon}.
\]
Then
\[
\eta>10^{-28}.
\]

For \(u\in F_1\),
\[
\|T_1u\|^2=q_1[u]+\|Du\|^2
\le q_1[u]+\frac{s}{\varepsilon}q_1[u]
=\frac{s+\varepsilon}{\varepsilon}q_1[u].
\]
Since \(s<23/2\),
\[
q_1[u]\ge\eta\|T_1u\|^2.
\]
Using
\[
q_1[u]=
\langle T_1u,(I-C_1)T_1u\rangle,
\]
we obtain on \(H_1\), by density and continuity,
\[
\boxed{I-C_1\succeq\eta I_{H_1}.}
\]
Because \(C_1=R_1^*R_1\ge0\),
\[
\eta I\preceq I-C_1\preceq I.
\]
In particular,
\[
\|R_1\|^2\le1-\eta<1.
\]

This is an operator statement on the entire closed terminal space \(H_1\),
not only a diagonal source inequality.

## 3. The single terminal square root

By the continuous functional calculus for bounded positive self-adjoint
operators, define
\[
\boxed{\Delta_1=(I-C_1)^{1/2}\in\mathcal B(H_1).}
\]
Then
\[
\sqrt\eta\,I\preceq\Delta_1\preceq I,
\qquad
\Delta_1^2=I-C_1.
\]
Hence \(\Delta_1\) is boundedly invertible and
\[
\|\Delta_1^{-1}\|\le\eta^{-1/2}<10^{14}.
\]

Crucially, this is the **only** defect square root used. We do not define
local operators \((I-C_a)^{1/2}\) and we do not infer any false
square-root intertwining from the compression law.

## 4. Fixed-horizon positive readout

For \(B\le a\le1\), define the terminal-space readout
\[
\boxed{
T_{X,a}:F_a\longrightarrow H_1,\qquad
T_{X,a}:=\Delta_1 I_{a,1}T_a.
}
\]

Also define
\[
K_{X,a}:=\Delta_1 H_a\subset H_1.
\]
Since \(H_a\) is closed and \(\Delta_1\) is boundedly invertible,
\(K_{X,a}\) is closed. Since \(H_a\subset H_b\) for \(a\le b\),
\[
K_{X,a}\subset K_{X,b}\subset H_1.
\]
Thus the corrected targets form a literal nested Hilbert family inside the
single terminal space.

## 5. Exact positive Weil-Gram identity

Let \(u,v\in F_a\), and put
\[
h=I_{a,1}T_au,\qquad k=I_{a,1}T_av.
\]
Then
\[
\begin{aligned}
\langle T_{X,a}u,T_{X,a}v\rangle
&=\langle\Delta_1h,\Delta_1k\rangle\\
&=\langle h,(I-C_1)k\rangle\\
&=\langle h,k\rangle-\langle R_1h,R_1k\rangle.
\end{aligned}
\]
The inclusion is isometric, and defect naturality gives
\[
R_1I_{a,1}=R_a.
\]
Therefore
\[
\boxed{
\langle T_{X,a}u,T_{X,a}v\rangle_{H_1}
=q_a(u,v).
}
\]

This is sesquilinear and holds on the closed source space \(F_a\), not merely
for diagonal quadratic values.

Consequently \(q_a\) is a genuine positive Hilbert inner product on \(F_a\),
and
\[
T_{X,a}:(F_a,q_a)\longrightarrow K_{X,a}
\]
is unitary onto its closed range. No GNS completion is introduced: the
ambient terminal space, the maps \(T_a\), the defect transfers \(R_a\), and
the inclusions \(I_{a,b}\) were constructed before the sign of \(q_a\) was
settled.

## 6. Exact transition compatibility

For \(B\le a\le b\le1\),
\[
\begin{aligned}
T_{X,b}J_{a,b}
&=\Delta_1I_{b,1}T_bJ_{a,b}\\
&=\Delta_1I_{b,1}I_{a,b}T_a\\
&=\Delta_1I_{a,1}T_a\\
&=T_{X,a}.
\end{aligned}
\]
Hence
\[
\boxed{T_{X,b}J_{a,b}=T_{X,a}.}
\]

Because all corrected readouts land in the same terminal Hilbert space
\(H_1\), this is literal equality. Equivalently, with
\(\iota^X_{a,b}:K_{X,a}\hookrightarrow K_{X,b}\) the literal inclusion,
\[
\iota^X_{a,b}T_{X,a}=T_{X,b}J_{a,b},
\qquad
\iota^X_{b,c}\iota^X_{a,b}=\iota^X_{a,c}.
\]

Thus the corrected positive geometry is compatible on the entire declared
fixed C1 horizon.

## 7. Quantitative relation to the physical gap

The physical terminal coercivity and the mediator envelope give
\[
I-C_1\succeq\eta I,\qquad
\eta=\frac{10^{-26}}{23/2+10^{-26}}>10^{-28}.
\]
Therefore the square-root correction does not collapse any terminal
direction:
\[
\|\Delta_1h\|^2\ge\eta\|h\|^2.
\]

Independently, the exact Gram identity and physical theorem give
\[
\|T_{X,a}u\|^2=q_a[u]\ge10^{-26}\|u\|_2^2
\]
on the source class for which the promoted fixed-horizon coercivity theorem
applies. These are different norms and different quantitative statements:
\(\eta\) controls the correction inside \(H_1\), while \(10^{-26}\) is the
physical source-space gap.

## 8. C1d conclusion and scope firewall

The fixed-horizon C1d obligation is closed:

\[
\boxed{
(F_a,J_{a,b},q_a)
\xrightarrow{\;T_{X,a}\;}
(K_{X,a},\iota^X_{a,b},\langle\cdot,\cdot\rangle_{H_1})
}
\]
is a compatible positive Gram realization for every
\[
B\le a\le b\le1.
\]

This construction is intrinsic to the already fixed coupled Prime/Gamma
mediator and uses one terminal defect square root. It does not use local
square roots of compressed defect operators.

It does **not** establish:

- any compatible horizon larger than \(1\);
- a cofinal family \(a_n\to\infty\);
- compatibility of positive completions across different future terminal
  horizons;
- the full global Weil test class;
- a final global Object X;
- global Weil positivity;
- the Riemann hypothesis.
