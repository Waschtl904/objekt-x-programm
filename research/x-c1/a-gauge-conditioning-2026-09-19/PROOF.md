# A-orthogonal reduced shell coordinates with explicit L2 conditioning

2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Branch: `research/x-c1-inherited-resonance-shell-schur-2026-09-18`.
Anchor: `d145ba88c86d4d0de665355bf3bff15844dbf414`.
This note is append-only and does not change `main` or merged PR #137.

Let
\[
B={\log 5\over2},\qquad 0<h=b-B\le 10^{-20},
\]
and use the spaces and fixed functions of the reduced shell coordinate theorem:
\(\mathcal K_B\), \(\mathcal K_b\), \(X=\mathbb C\oplus L^2(B,b)\),
\(\chi\), \(\psi\), and
\[
\widetilde L(t,s)=t\psi-m_s\chi+S,
\qquad m_s=\int_B^b s(x)\cosh(x/2)\,dx.
\]
All core scalar products below are physical \(L^2((-B,B),dx)\), linear in the first argument.
The closed core form is denoted by \(a=q_B\) on \(F_B\).

The point of this note is to replace the physical-L2 gauge by an **energy-orthogonal gauge** without changing the physical source class. The pure trace coupling then vanishes identically.

## 1. The fixed trace functional is L2-bounded

The full-shell pivot proof writes the nonpole form as
\[
q_B[f,g]=\mathcal E(f,g)+R_B(f,g),
\]
where
\[
\mathcal E[f]=\int_0^\infty k(r)\|\tau_r f-f\|_2^2\,dr,
\qquad
k(r)={e^{-r/2}\over1-e^{-2r}},
\]
and the non-Gamma part satisfies
\[
\|R_B\|_{L^2\to L^2}\le 14.
\tag{1}
\]
The same proof gives
\[
\|\psi\|_\infty\le4,
\qquad \operatorname{Lip}(\psi|_{[-B,B]})\le4,
\qquad \|\psi\|_2^2\le32,
\tag{2}
\]
\[
k(r)\le {1\over2r}+{1\over4}\quad(0<r\le1),
\qquad
\int_0^\infty r k(r)\,dr<5.
\tag{3}
\]

For smooth compactly supported core tests first, translation invariance gives
\[
\mathcal E(w,\psi)=\langle w,G_\psi\rangle,
\qquad
G_\psi(x)=\int_0^\infty k(r)
\bigl(2\psi(x)-\psi(x+r)-\psi(x-r)\bigr)\,dr,
\tag{4}
\]
with zero extension of \(\psi\).
Put \(d(x)=B-|x|\). For \(|x|<B\), if \(0<r\le d(x)\), (2) gives
\[
|2\psi(x)-\psi(x+r)-\psi(x-r)|\le8r.
\]
For \(r>d(x)\), the crude bound is \(16\). Hence
\[
|G_\psi(x)|
\le8\int_0^{d(x)}rk(r)\,dr
+16\int_{d(x)}^\infty k(r)\,dr.
\tag{5}
\]
Because \(0<d(x)<B<1\), (3) implies
\[
\int_d^\infty k(r)\,dr
\le {1\over2}\log {1\over d}+{1\over4}+5
={1\over2}\log {1\over d}+{21\over4}.
\]
Therefore
\[
|G_\psi(x)|<124+8\log {1\over d(x)}.
\tag{6}
\]
Using
\[
\int_0^1\log(1/t)\,dt=1,
\qquad
\int_0^1\log^2(1/t)\,dt=2,
\]
we get
\[
\|G_\psi\|_2^2
<2\int_0^1(124+8\log(1/t))^2dt
=34976<188^2.
\tag{7}
\]
Thus \(\|G_\psi\|_2<188\). From (1)-(2), \(\|R_B\psi\|_2<14\sqrt{32}<84\), so
\[
\boxed{|q_B(w,\psi)|<272\,\|w\|_2}
\tag{8}
\]
for the dense test class and therefore, by L2 continuity, for every \(w\in\mathcal K_B\). In particular the form functional \(w\mapsto a(w,\psi)\) has a unique bounded L2 extension, denoted \(L_\psi\).

The directional certificate at the anchor proves, with directed rational arithmetic,
\[
\boxed{a[\psi]=q_B[\psi]>0.14.}
\tag{9}
\]
Consequently
\[
\ell_A(v):={L_\psi(v)\over a[\psi]}
\quad\text{satisfies}\quad
|\ell_A(v)|<1943\,\|v\|_2.
\tag{10}
\]
No operator-domain invariance is used here.

## 2. The A-gauge core complement

Define on the Hilbert level
\[
\boxed{\mathcal K_{B,A}^0:=\ker L_\psi\subset\mathcal K_B.}
\tag{11}
\]
On the form domain this is exactly
\[
F_{B,A}^0:=\{w\in F_B:a(w,\psi)=0\}.
\tag{12}
\]
Since \(L_\psi(\psi)=a[\psi]\ne0\), every \(v\in\mathcal K_B\) has the unique decomposition
\[
v=P_Av+\ell_A(v)\psi,
\qquad
P_Av:=v-\ell_A(v)\psi\in\mathcal K_{B,A}^0.
\tag{13}
\]
The projection is oblique in L2 but bounded. On the form domain it is the exact \(a\)-orthogonal projection: by positivity of \(a\),
\[
a[P_Af]=a[f]-{|a(f,\psi)|^2\over a[\psi]}\le a[f].
\tag{14}
\]
Hence \(F_{B,A}^0\) is a closed form subspace, dense in \(\mathcal K_{B,A}^0\), and its compressed form \(a_A=a|_{F_{B,A}^0}\) still satisfies
\[
a_A[w]\ge10^{-13}\|w\|_2^2.
\tag{15}
\]

## 3. Complete Hilbert-space coordinates and explicit conditioning

Define
\[
\boxed{
\Phi_A:\mathcal K_{B,A}^0\oplus X\longrightarrow\mathcal K_b,
\qquad
\Phi_A(w,(t,s))=Jw+\widetilde L(t,s).
}
\tag{16}
\]
For \(u\in\mathcal K_b\), set
\[
s=u|_{(B,b)},\qquad
v=u|_{(-B,B)}+m_s\chi,
\qquad
t=\ell_A(v),\qquad w=v-t\psi.
\tag{17}
\]
Then \(v\in\mathcal K_B\), \(w\in\mathcal K_{B,A}^0\), and direct substitution gives \(\Phi_A(w,(t,s))=u\). Conversely restriction to the shell recovers \(s\), hence \(v=w+t\psi\), and application of \(L_\psi\) recovers \(t\). Thus (16) is a bounded bijection with zero kernel.

Let
\[
N_A^2=\|w\|_2^2+|t|^2+\|s\|_{L^2(B,b)}^2.
\]
The already proved lift bound \(\|\widetilde Lz\|_2\le8\|z\|_X\) gives, without any orthogonality assumption,
\[
\boxed{\|\Phi_A(w,z)\|_2^2\le65N_A^2.}
\tag{18}
\]

For the inverse, (10) and \(\|\psi\|_2<6\) imply
\[
|t|<1943\|v\|_2,
\qquad
\|w\|_2<11659\|v\|_2,
\]
so
\[
\|w\|_2^2+|t|^2
<139707530\,\|v\|_2^2.
\tag{19}
\]
The inherited moment bounds give
\[
|m_s|^2\le{36\over25}h\|s\|_2^2,
\qquad \|\chi\|_2^2\le18.
\]
At \(h\le10^{-20}\), therefore
\[
\|m_s\chi\|_2<6\cdot10^{-10}\|s\|_2.
\tag{20}
\]
Using \((a+\mu b)^2\le(1+\mu)(a^2+\mu b^2)\) with \(\mu=6\cdot10^{-10}\), (19)-(20) yield the uniform conservative bound
\[
\boxed{
{1\over140000000}N_A^2
\le\|\Phi_A(w,z)\|_2^2
\le65N_A^2.
}
\tag{21}
\]
The large inverse constant is deliberate; no attempt is made here to optimize it.

## 4. Form spaces and actual H1 sources

Let \(F_D\) and \(d\) be the complete shell form domain and form from the parent theorem. The restriction of (16) is a topological isomorphism
\[
\boxed{\Phi_A:F_{B,A}^0\oplus F_D\overset{\cong}{\longrightarrow}F_b.}
\tag{22}
\]
Indeed \(P_A\) is bounded in both L2 and the core form norm by (10) and (14); the old reduced coordinate theorem may therefore be transferred by a bounded finite-rank shear. Equivalently, one can repeat its closed-image proof using (21), boundedness of the cross operator, and form density of the actual sources.

The exact preimage of the original H1 sources is
\[
T_b^A=\left\{(w,(t,s)):\begin{array}{l}
 w\in H^1_{\rm even}(-B,B)\cap\mathcal K_{B,A}^0,\\
 s\in H^1(B,b),\ s(b)=0,\\
 \boxed{w(B)+t=s(B)}
\end{array}\right\}.
\tag{23}
\]
Then
\[
\boxed{\Phi_A(T_b^A)=\mathcal W_b^{\rm even}}
\tag{24}
\]
bijectively. The condition in (23) is the same physical gluing condition as before. No new Mellin condition is introduced, and \(w(B)\) need not vanish.

## 5. Exact removal of the pure trace coupling

On \(F_{B,A}^0\oplus F_D\), write
\[
\mathfrak F_A[w,z]
=a_A[w]+2\operatorname{Re}c_A(w,z)+d[z],
\qquad
c_A(w,z)=q_b(Jw,\widetilde Lz).
\tag{25}
\]
For \(z=(t,s)\), put \(Y_s=-m_s\chi+S\). Window functoriality on the fixed core gives
\[
q_b(Jw,\psi)=q_B(w,\psi)=a(w,\psi)=0
\qquad(w\in F_{B,A}^0).
\]
Therefore
\[
\boxed{
c_A(w,(t,s))=q_b(Jw,Y_s),
\qquad c_A(w,e)=0.
}
\tag{26}
\]
The scalar trace coordinate \(t\) has disappeared **exactly** from the forcing of the cross block. This does not mean that \(D^{-1}\) preserves the trace-zero shell subspace; a shell Riesz response may still generate a trace component through the internal geometry of \(D\). Only the direct pure-trace forcing is eliminated.

## 6. Consequence for the next Schur gate

If one proves on the complete A-gauge spaces
\[
|c_A(w,z)|^2\le\theta_A\,a_A[w]d[z],
\qquad 0\le\theta_A<1,
\tag{27}
\]
then exactly as in the corrected reduced theorem,
\[
q_b[\Phi_A(w,z)]
\ge(1-\sqrt{\theta_A})(a_A[w]+d[z]).
\]
Using (15), \(d\ge(32\cdot10^{13})^{-1}I\), and only the **forward** norm bound (18),
\[
\boxed{
q_b[u]\ge {1-\sqrt{\theta_A}\over65}
\min\left\{10^{-13},{1\over32\cdot10^{13}}\right\}\|u\|_2^2.
}
\tag{28}
\]
Thus the poor inverse constant in (21) is a domain/conditioning cost, but it does **not** enter the inverse-free relative-gap conversion.

The remaining mathematical obligation is still infinite-dimensional: control the complete A-gauge core-to-shell operator (or an equivalent Schur remainder) on the whole reduced core, including low/complement mixing and both tails. The new theorem removes the dominant algebraic trace channel; it does not prove an all-source continuation, the odd sector, `log(7)/2`, `a=1`, C1-GEOM, Objekt X, or RH.
