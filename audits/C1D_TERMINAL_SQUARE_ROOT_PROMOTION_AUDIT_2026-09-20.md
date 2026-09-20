# C1d terminal square-root completion — promotion audit

**Date:** 2026-09-20  
**Candidate theorem:** \`a0c57ddd5c4b7dd2cf18c17b19f5af4069915387\`  
**Status recommended:** AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN  
**Scope:** the already constructed coupled spectral C1 system on \(B\le a\le1\).

This audit checks the fixed-horizon C1d theorem after the terminal 191D
positivity result was promoted. It is not an external peer review and does not
extend the horizon.

## 1. Domain and operator statement

The inherited candidate gives bounded maps
\[
T_a:F_a\to H_a,\qquad
R_a:H_a\to H,
\]
literal isometric inclusions \(I_{a,b}:H_a\hookrightarrow H_b\), and
\[
R_bI_{a,b}=R_a.
\]
The terminal theorem gives
\[
q_1[u]\ge 10^{-26}\|u\|_2^2
\]
on \(F_1\), while the mediator gives
\[
\|Du\|^2\le s\|u\|_2^2,\qquad s<23/2.
\]

With
\[
\eta=\frac{10^{-26}}{23/2+10^{-26}},
\]
one has \(\eta>10^{-28}\) and
\[
q_1[u]\ge \eta\|T_1u\|^2.
\]
Since
\[
q_1[u]=\langle T_1u,(I-R_1^*R_1)T_1u\rangle,
\]
density and boundedness extend the quadratic inequality to all of \(H_1\):
\[
I-R_1^*R_1\succeq\eta I_{H_1}.
\]
Thus this is an operator inequality on the whole closed terminal space, not
only a source-level diagonal estimate.

## 2. Functional calculus

The operator
\[
A_1:=I-R_1^*R_1
\]
is bounded positive self-adjoint and satisfies
\[
\eta I\preceq A_1\preceq I.
\]
Therefore the continuous functional calculus defines the single terminal
operator
\[
\Delta_1=A_1^{1/2},
\]
with
\[
\sqrt\eta\,I\preceq\Delta_1\preceq I,
\qquad
\|\Delta_1^{-1}\|\le\eta^{-1/2}<10^{14}.
\]
No local square roots \((I-C_a)^{1/2}\) are needed or asserted to intertwine.

## 3. Exact Gram identity

For
\[
T_{X,a}=\Delta_1 I_{a,1}T_a
\]
and \(u,v\in F_a\),
\[
\begin{aligned}
\langle T_{X,a}u,T_{X,a}v\rangle
&=\langle I_{a,1}T_au,(I-R_1^*R_1)I_{a,1}T_av\rangle\\
&=\langle T_au,T_av\rangle
 -\langle R_aT_au,R_aT_av\rangle\\
&=q_a(u,v).
\end{aligned}
\]
The argument is fully sesquilinear. It uses only the previously proved
isometry of \(I_{a,1}\), defect naturality \(R_1I_{a,1}=R_a\), and the exact
difference-of-Grams identity.

## 4. Completeness and positive target

The tightened theorem records
\[
\eta\|T_au\|^2\le q_a[u]\le\|T_au\|^2.
\]
The inherited mediator theorem already makes \(T_a:F_a\to H_a\) a bounded
isomorphism for the original complete form norm. Hence the \(q_a\)-norm is
equivalent to that complete norm. Therefore \((F_a,q_a)\) is complete.

With
\[
K_{X,a}:=\Delta_1H_a,
\]
bounded invertibility of \(\Delta_1\) implies that \(K_{X,a}\) is closed and
\[
T_{X,a}:(F_a,q_a)\to K_{X,a}
\]
is unitary onto the full target.

This removes any hidden completion ambiguity and does not introduce a GNS
construction.

## 5. Transition compatibility

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
All corrected readouts land in the same \(H_1\), so this is literal equality.

Since \(H_a\subset H_b\), also
\[
K_{X,a}=\Delta_1H_a\subset\Delta_1H_b=K_{X,b}.
\]

## 6. Non-circularity

The following objects were constructed before the terminal positivity theorem:

- the common Prime/Gamma multiplier \(T\);
- the closed spaces \(H_a\);
- the defect output \(D\);
- the defect transfers \(R_a\);
- the inclusions \(I_{a,b}\);
- the exact signed identity \(q_a=\langle T_a\cdot,T_a\cdot\rangle-
  \langle R_aT_a\cdot,R_aT_a\cdot\rangle\).

The terminal positivity result is used only to prove that the already
constructed defect satisfies \(I-R_1^*R_1\succ0\), enabling an intrinsic
functional-calculus correction. Thus the theorem is not a tautological
definition of a Hilbert norm from \(q_a\).

## 7. Scope

The theorem is restricted to
\[
B\le a\le1.
\]
Although physical Weil coercivity is known on \(0<a\le1\), this audit does not
silently extend the registered C1 spaces, inclusions or defect transfers below
\(B\).

The theorem does not establish:

- any horizon \(>1\);
- a cofinal family of terminal positive completions;
- compatibility between different future terminal horizons;
- the full global Weil test class;
- full C1-GEOM on an unbounded horizon;
- global Object X;
- global Weil positivity;
- RH.

## 8. Audit conclusion

All candidate-specific fixed-horizon C1d obligations are satisfied:

1. terminal strict reserve on the whole \(H_1\): PASS;
2. continuous-functional-calculus square root: PASS;
3. bounded invertibility and quantitative reserve: PASS;
4. exact sesquilinear Weil-Gram identity: PASS;
5. completeness of \((F_a,q_a)\): PASS;
6. closed nested corrected targets: PASS;
7. literal zero-extension intertwining: PASS;
8. no local square-root compression inference: PASS;
9. no GNS circularity: PASS;
10. scope firewall \(B\le a\le1\): PASS.

The theorem is therefore suitable for registry promotion as
**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
