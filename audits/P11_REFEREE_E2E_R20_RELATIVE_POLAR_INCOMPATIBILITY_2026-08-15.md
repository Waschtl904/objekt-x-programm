# P11 End-to-End Referee R20 — individual noncommutativity versus relative polar incompatibility

Date: 2026-08-15

## Target

Audit the proposed R20 route: use quantitative noncommutativity of the concrete metric pairs
\[
[G_{R,T_0},G_{R,U}],\qquad [G_{S,T_0},G_{S,U}]
\]
together with the R19 modulus leakage to force a genuine polar-level lower bound, e.g.
\[
\|(I-WW^*)U_SW\|\ge c>0
\]
or at least a lower bound on
\[
\|U_SW-WU_R\|.
\]

## Verdict

The proposal is **too weak as stated**.  Individual metric-pair noncommutativity does control whether each polar factor is nontrivial, but it does not control whether the source and target polar rotations are incompatible under the canonical inclusion.

There is a valid scale-invariant one-pair estimate:
\[
\boxed{
\|U-I\|
\ge
\frac{
\|B^{-1/2}[B^{1/2},C^{1/2}]B^{-1/2}\|
}{
2\|(B^{-1/2}CB^{-1/2})^{1/2}\|
}.
}
\]
Thus a normalized square-root commutator measures **individual polar activity**.

However, a canonical nested model with exact base/future pullback can have arbitrarily large source and target commutators and nontrivial polar factors while
\[
\boxed{(I-P)U_SW=0,\qquad U_SW-WU_R=0}
\]
identically.  A stronger direct-sum model can simultaneously carry genuine R19-type modulus leakage, arbitrarily large square-root off-block, and arbitrarily large individual metric commutators, while the same two polar quantities remain exactly zero.

Therefore the missing P11 object is not individual noncommutativity but **relative polar incompatibility** between the two nested metric pairs.

## Canonical statuses

- [R20-A] normalized square-root commutator lower-bounds individual `||U_X-I||`: **✓[M]**;
- [R20-B] exact decomposition of the relative polar defect into target leakage plus internal gauge compression: **✓[M]**;
- [R20-C] individual quantitative noncommutativity implies polar leakage: **✓[M]_neg**;
- [R20-D] individual quantitative noncommutativity implies relative gauge defect: **✓[M]_neg**;
- [R20-E] R19 modulus leakage + arbitrarily large individual metric commutators imply polar leakage: **✓[M]_neg**;
- [R20-F] concrete P11 relative polar incompatibility / `Gamma_U -> I` / cross-terminal convergence: **?[O]**.

---

## 1. Scale-correct individual commutator estimate

Let `B,C` be boundedly invertible positive operators and put
\[
X=C^{1/2}B^{-1/2}=UH,
\qquad
H=(B^{-1/2}CB^{-1/2})^{1/2}.
\]
Then
\[
X-X^*
=B^{-1/2}[B^{1/2},C^{1/2}]B^{-1/2}.
\]
Also
\[
X-X^*=(U-I)H+H(I-U^*).
\]
Hence
\[
\|X-X^*\|
\le2\|H\|\,\|U-I\|,
\]
which yields
\[
\boxed{
\|U-I\|
\ge
\frac{
\|B^{-1/2}[B^{1/2},C^{1/2}]B^{-1/2}\|
}{2\|H\|}.
}
\]

This is the quantitative refinement of O3N.8.  It is invariant under common scalar rescaling `(B,C) -> (tB,tC)`.  In contrast, the raw commutator `||[B,C]||` scales like `t^2` while the polar factor is unchanged.  Therefore a raw commutator lower bound by itself has no scale-correct polar meaning.

---

## 2. Exact relative polar decomposition

Define
\[
\mathfrak P_U:=U_SW-WU_R,
\qquad
P=WW^*,
\qquad
\Lambda_U:=(I-P)U_SW,
\]
and recall
\[
\Gamma_U=W^*U_SWU_R^*.
\]
Then exactly
\[
\boxed{
\mathfrak P_U
=\Lambda_U+W(\Gamma_U-I)U_R.
}
\]
The two summands lie in orthogonal subspaces `(Ran W)^perp` and `Ran W`.  Therefore for each source vector `f`,
\[
\boxed{
\|\mathfrak P_Uf\|^2
=\|\Lambda_Uf\|^2
+\|(\Gamma_U-I)U_Rf\|^2.
}
\]
Thus a lower bound on target polar leakage would indeed give a true gauge lower bound.  But individual `||U_X-I||` does not appear in this decomposition.

---

## 3. Canonical nested countermodel: large noncommutativity, zero relative polar defect

Take
\[
B=\begin{pmatrix}1&0\\0&2\end{pmatrix},
\qquad
C=\begin{pmatrix}2&1\\1&2\end{pmatrix}>0,
\]
so
\[
[B,C]=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\ne0.
\]
Let source be `C^2`, target `C^3`, and let
\[
Wz=(z,0)
\]
be the canonical inclusion.  For `t>0`, set
\[
G_{R,T_0}=tB,
\qquad
G_{R,U}=tC,
\]
\[
G_{S,T_0}=tB\oplus1,
\qquad
G_{S,U}=tC\oplus1.
\]
Both base and future pullback identities hold exactly.  The normalized base transition is the same canonical inclusion.  Moreover
\[
X_S=X_R\oplus1,
\]
so uniqueness of polar decomposition gives
\[
U_S=U_R\oplus1.
\]
Since `[B,C] != 0`, O3N.8 gives `U_R != I` and `U_S != I`.  Nevertheless
\[
\boxed{U_SW=WU_R}
\]
and therefore
\[
\boxed{(I-P)U_SW=0.}
\]
At the same time
\[
\|[G_{R,T_0},G_{R,U}]\|
=t^2\|[B,C]\|
\]
and similarly on the target block.  These commutators can be made arbitrarily large.

Hence even arbitrarily large individual metric noncommutativity, occurring directly on the canonically embedded source block, does not force either polar leakage or relative gauge mismatch.

---

## 4. Stronger direct-sum model: R19 modulus leakage plus large commutators, still zero polar leakage

Use two orthogonal summands.

### Modulus-leakage summand

Take the R19 inclusion
\[
W_1:\mathbb C\hookrightarrow\mathbb C^2,
\qquad W_1z=(z,0),
\]
with base metrics `1` and `I_2` and future metrics
\[
2s^2,
\qquad
s^2A_0,
\qquad
A_0=\begin{pmatrix}2&1\\1&2\end{pmatrix}.
\]
The polar factors are `1` and `I_2`, hence zero polar leakage.  But
\[
Q_1=A_0^{1/2}W_1/\sqrt2
\]
has nonzero off-range component because `e_1` is not an eigenvector of `A_0`, and the square-root off-block grows like `s`.

### Noncommuting matched summand

Take identical source and target copies of `C^2` with identity transition, base metric `tB`, future metric `tC`.  The source and target polar factors are the same nontrivial unitary `U_0`, while the raw commutator norm is `t^2||[B,C]||`.

### Direct sum

The total transition is a canonical coordinate inclusion.  The total polar factors are
\[
U_R=1\oplus U_0,
\qquad
U_S=I_2\oplus U_0,
\]
so
\[
\boxed{
(I-P)U_SW=0,
\qquad
U_SW-WU_R=0.
}
\]
Yet the total system has nonzero modulus leakage, square-root off-block as large as desired by increasing `s`, and individual commutators as large as desired by increasing `t`.

This is an abstract non-promotion theorem.  It is not a counterexample to the concrete P11 family.

---

## 5. Corrected R20 frontier

The proposed condition
\[
[G_{R,T_0},G_{R,U}]\ne0,
\qquad
[G_{S,T_0},G_{S,U}]\ne0
\]
— even quantitatively and even together with R19 modulus leakage — is not enough.

The remaining P11 gate is intrinsically relative:
\[
\boxed{
\mathfrak P_U=U_SW-WU_R.
}
\]
Equivalently, by O3N.4, it is the convergence of
\[
\Gamma_U=W^*U_SWU_R^*
\]
to the identity.

Any successful commutator-based criterion must compare the source and target metric pairs **across the canonical inclusion**, so that matched polar rotations such as the countermodel are excluded.  Two separate commutator lower bounds cannot do this.

No conclusion about `Gamma_U -> I`, `K_{R,S}^{T_0,U} -> I`, strong terminal transport, a global Object X, Seal, or RH follows from R20.
