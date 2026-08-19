# P11 End-to-End Referee R36-A — Localized hub range: density versus annihilator kernel

Date: 2026-08-19 (continued 2026-08-19: exposed-cell lemma, support bound, peeling scheme; corrected 2026-08-19: known-zero exposed cells, repaired support proof, parity split)

## Target

Start R36 as an adversarial audit of the **localized hub range**, exactly in the
sense requested after R35. Fix
\[
0<R<S<T_0,
\qquad
A:=A_{R,S}=(-S,-R)\cup(R,S),
\]
and define the localized hub operator
\[
T_A:=P_AH_{T_0}:L^2(-T_0,T_0)\to L^2(A),
\]
where \(P_A\) is restriction to the annulus and \(E_A=P_A^*\) is zero extension.
Using only the concrete finite prime-translation formula for \(H_{T_0}\), determine the
first gate:
\[
\boxed{
\overline{\operatorname{Ran}(P_AH_{T_0})}=L^2(A)
\qquad\Longleftrightarrow\qquad
\ker(H_{T_0}E_A)=\{0\}.
}
\]
No existence of a localized annihilator is assumed. No statement about R30-F is made.

**Correction (added in this continuation).** The Target statement above previously
displayed the left-hand side as the unclosed range \(\operatorname{Ran}(P_AH_{T_0})\)
with an unresolved \(\stackrel?=\); the operative object throughout R36-A1/A2/A3 is always
the **closure** \(\overline{\operatorname{Ran}(P_AH_{T_0})}\), and the equivalence with
\(\ker(H_{T_0}E_A)=\{0\}\) is a proved fact (R36-A1), not an open question. Only the
kernel triviality itself, (R36.4) below, remains \(?[O]\). This corrects a rendering slip;
no mathematical content of R36-A1 changes.

## Repo sync

`main` at start of this audit: `971cd849ca3586f58ee5a858b1fbd6b3d388ec0f` —
"Hook P11_O3ag (R35 contraction no-go / resolvent repair) into the O3 chain after O3af".
`main` at start of the first continuation: `0d62bc711926267a65036c9230bd0923f9747d45` —
"Add R36-A audit: localized hub range density versus annihilator kernel gate…".
`main` at start of the exposed-cell/peeling continuation: `1db839139d48682fbb87ad49d9e0d5175fdcf881` —
"Continue R36-A: fix Target closure typo, rename finite linear system to finite translation equation, add exposed-cell lemma (R36-A3), tau_max outer support constraint (R36-A4), and iterative peeling scheme with correctness dichotomy".

Inputs: P11 §2 definitions of the source hub \(H_{T_0}\); R32 module
`P11_O3ae_HubOffSupport_Representation.tex`, especially Proposition O3AE.1 and
Theorem O3AE.2; R35 module/audit for the firewall that no localized annihilator is to
be presupposed; R30 baseline module `P11_O3ac_Riesz_Support_Radius.tex` for the oddness
of \(\phi_S\).

---

## 1. Exact operator identity for the localized range gate

### Lemma R36-A1 (adjoint identity)

For
\[
T_A=P_AH_{T_0}:L^2(-T_0,T_0)\to L^2(A)
\]
one has
\[
\boxed{T_A^*=H_{T_0}^*E_A=-H_{T_0}E_A.}
\tag{R36.1}
\]
Consequently
\[
\boxed{
\overline{\operatorname{Ran}(P_AH_{T_0})}=L^2(A)
\quad\Longleftrightarrow\quad
\ker(H_{T_0}E_A)=\{0\}.
}
\tag{R36.2}
\]

### Proof

Since \(P_A^*=E_A\) and Proposition O3AE.1 gives \(H_{T_0}^*=-H_{T_0}\),
\[
T_A^*=(P_AH_{T_0})^*=H_{T_0}^*E_A=-H_{T_0}E_A.
\]
The Hilbert-space duality identity
\(\overline{\operatorname{Ran}T_A}=(\ker T_A^*)^\perp\) gives
\[
\overline{\operatorname{Ran}(P_AH_{T_0})}=L^2(A)
\iff
\ker(T_A^*)=\{0\}
\iff
\ker(H_{T_0}E_A)=\{0\}.
\]
\(\square\)

Status: \(\boxed{\text{R36-A1}\quad\checkmark[M].}\)

### Firewall

Equation (R36.2) is a statement about **dense range**, not necessarily exact surjectivity.
Even if \(\ker(H_{T_0}E_A)=\{0\}\), one obtains only
\[
\overline{\operatorname{Ran}(P_AH_{T_0})}=L^2(A),
\]
not automatically
\(
\operatorname{Ran}(P_AH_{T_0})=L^2(A)
\).
Thus a trivial kernel kills the simple Hahn–Banach annihilator route, but does **not** yet
show that the concrete target vector
\[
d_{R,S}:=P_A(\phi_S-C_{\Gamma,S}j_{R,S})
\]
lies in the actual range; it only removes the possibility of detecting a failure by a
continuous annihilator.

---

## 2. Concrete form of the kernel equation

By Theorem O3AE.2 applied to vectors supported in the annulus \(A\), the equation
\(H_{T_0}E_Ay=0\) becomes a finite translation equation on the source interval.
Let
\[
\tau_{p,k}:=\frac{k\log p}{2},
\qquad
c_{p,k}:=\sqrt{\log p}\,p^{-3k/4},
\qquad
\mathcal P_{T_0}:=\{(p,k):p^k\le e^{2T_0}\}.
\]

### Proposition R36-A2 (explicit kernel equation)

For \(y\in L^2(A)\), the zero extension \(E_Ay\) satisfies
\[
H_{T_0}E_Ay=0
\quad\text{in }L^2(-T_0,T_0)
\]
if and only if for a.e. \(u\in(-T_0,T_0)\),
\[
\boxed{
\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\Bigl[(E_Ay)(u-\tau_{p,k})-(E_Ay)(u+\tau_{p,k})\Bigr]=0.
}
\tag{R36.3}
\]
Equivalently, because \(E_Ay\) vanishes off \(A\), this is a **finite translation
equation** for the annular trace \(y\): the sum has finitely many translated-copy terms,
although the underlying unknown \(y\) ranges over the infinite-dimensional space
\(L^2(A)\).

### Proof

This is the definition of \(H_{T_0}\) from P11 §2 / equation (2.5), with the finite active
set \(\mathcal P_{T_0}\), applied to the vector \(E_Ay\). Since \(E_Ay\in L^2(-T_0,T_0)\) and
is supported in \(A\), all terms are well defined and the equality in \(L^2\) is exactly the
boxed finite translation identity.
\(\square\)

Status: \(\boxed{\text{R36-A2}\quad\checkmark[M].}\)

### Interpretation

R36-A is therefore reduced to a **pure finite translation-cancellation question**:
does the annulus-supported vector \(y\) admit a nonzero solution of the concrete equation
(R36.3), or does that equation force \(y=0\)? At this stage neither outcome is assumed.

---

## 2a. Compact reformulation: an exposed-cell peeling scheme

Write (R36.3) compactly. Let
\[
\Lambda_{T_0}:=\{\pm\tau_{p,k}:(p,k)\in\mathcal P_{T_0}\},
\qquad
a_{\tau_{p,k}}:=c_{p,k},\quad a_{-\tau_{p,k}}:=-c_{p,k},
\]
so that with \(f:=E_Ay\) (hence \(\operatorname{supp}f\subset A\)), equation (R36.3) reads
\[
\boxed{
(H_{T_0}f)(u)=\sum_{\lambda\in\Lambda_{T_0}}a_\lambda f(u-\lambda)=0
\qquad\text{for a.e. }u\in(-T_0,T_0).
}
\tag{R36.3$'$}
\]
All \(a_\lambda\ne0\) since \(c_{p,k}=\sqrt{\log p}\,p^{-3k/4}>0\).

### Lemma R36-A3 (known-zero exposed-cell lemma)

Let \(Z\subset(-T_0,T_0)\) be a measurable set on which \(f\) is already known to vanish
a.e.  Let \(I\subset A\) be a nonempty open interval and \(\lambda_*\in\Lambda_{T_0}\). Put
\(J:=I+\lambda_*\). Suppose
\[
J\subset(-T_0,T_0)
\qquad\text{and}\qquad
J-\lambda\subset Z\ \ \text{for every }\lambda\in\Lambda_{T_0}\setminus\{\lambda_*\}.
\tag{R36.7}
\]
Then every \(f=E_Ay\) solving (R36.3\('\)) satisfies
\[
\boxed{y=0\quad\text{a.e. on }I.}
\]

### Proof

Fix \(u\in J\). By (R36.3\('\)),
\[
\sum_{\lambda\in\Lambda_{T_0}}a_\lambda f(u-\lambda)=0.
\]
For \(\lambda\ne\lambda_*\), \(u-\lambda\in J-\lambda\subset Z\), so by assumption
\(f(u-\lambda)=0\) a.e. there. Hence the sum reduces to the single term
\[
a_{\lambda_*}f(u-\lambda_*)=0.
\]
Since \(a_{\lambda_*}\ne0\), \(f(u-\lambda_*)=0\) for a.e. \(u\in J\), i.e. \(f=0\) a.e. on
\(J-\lambda_*=I\). Because \(I\subset A\), \(f|_I=y|_I\), so \(y=0\) a.e. on \(I\).
\(\square\)

Status: \(\boxed{\text{R36-A3}\quad\checkmark[M].}\)

### Remark (why not a global Fourier argument)

On all of \(\mathbb R\), \(\sum_\lambda a_\lambda f(\cdot-\lambda)=0\) for compactly
supported \(f\) would be attackable via the exponential-polynomial symbol
\(\sum_\lambda a_\lambda e^{-i\lambda\xi}\), whose zero set is discrete, forcing
\(\widehat f\equiv0\) hence \(f=0\). That argument is **not legitimate here**: equation
(R36.3\('\)) only asserts \(H_{T_0}f=0\) on the finite window \((-T_0,T_0)\); outside that
window the full translation sum \(\sum_\lambda a_\lambda f(\cdot-\lambda)\) is entirely
unconstrained and may be nonzero. R36-A3 avoids this trap by only ever using the equation
on points \(u\in(-T_0,T_0)\) and only ever concluding vanishing on the correspondingly
shifted interval \(I=J-\lambda_*\subset A\subset(-T_0,T_0)\); no global exponential-
polynomial uniqueness is invoked.

### Corollary R36-A4 (outer support constraint via \(\tau_{\max}\))

Let
\[
\tau_{\max}:=\max_{(p,k)\in\mathcal P_{T_0}}\tau_{p,k}.
\]
If \(0\ne y\in\ker(H_{T_0}E_A)\) and \(f=E_Ay\), \(b:=\operatorname{ess\,sup}\operatorname{supp}f\)
(so \(b\le S\) since \(\operatorname{supp}f\subset A\subset[-S,S]\)), then necessarily
\[
\boxed{b+\tau_{\max}\ge T_0,\qquad\text{i.e.}\qquad b\ge T_0-\tau_{\max}.}
\]
Symmetrically, \(a:=\operatorname{ess\,inf}\operatorname{supp}f\) satisfies
\(a\le-T_0+\tau_{\max}\). Consequently
\[
\boxed{
\operatorname{ess\,sup}\operatorname{supp}y\ge T_0-\tau_{\max}
\qquad\text{and}\qquad
\operatorname{ess\,inf}\operatorname{supp}y\le-(T_0-\tau_{\max}).
}
\tag{R36.8}
\]

### Proof

Let
\[
g:=\min_{\lambda\in\Lambda_{T_0}\setminus\{\tau_{\max}\}}(\tau_{\max}-\lambda)>0.
\]
The positivity is immediate because \(\tau_{\max}\) is the strict largest element of the
finite set \(\Lambda_{T_0}\). Suppose for contradiction that
\[
b+\tau_{\max}<T_0.
\]
Choose \(0<\varepsilon<g/4\) small enough that
\[
b+\tau_{\max}-\varepsilon>T_0-2\varepsilon
\qquad\text{and in particular}
\qquad
(b-\varepsilon)+\tau_{\max}<T_0.
\]
By the definition of \(b=\operatorname{ess\,sup}\operatorname{supp}f\), there exists a nonempty open
interval
\[
I\subset(b-\varepsilon,b)\cap A
\]
on which \(f\) is not a.e. zero. Put \(J:=I+\tau_{\max}\). Then
\[
J\subset(-T_0,T_0)
\]
by the strict inequality \((b-\varepsilon)+\tau_{\max}<T_0\). For every competing
\(\lambda\in\Lambda_{T_0}\setminus\{\tau_{\max}\}\),
\[
J-\lambda=I+(\tau_{\max}-\lambda)
\subset (b-\varepsilon+g,\,b+g)
\subset(b,\infty),
\]
because \(\tau_{\max}-\lambda\ge g\) and \(\varepsilon<g/4\). Since \(b\) is the essential
supremum of the support of \(f\), one has \(f=0\) a.e. on \((b,\infty)\). Hence every
competing translate lands in the known zero set
\[
Z:=(b,\infty)\cap(-T_0,T_0).
\]
Lemma R36-A3 therefore applies with \(\lambda_*:=\tau_{\max}\), proving \(f=0\) a.e. on
\(I\), a contradiction. Thus \(b+\tau_{\max}\ge T_0\).

The symmetric lower support bound follows by applying the same argument to the reflected
left edge with \(\lambda_*:=-\tau_{\max}\). Concretely, if
\(a:=\operatorname{ess\,inf}\operatorname{supp}f>-T_0+\tau_{\max}\), choose a nonempty open interval
\(I\subset(a,a+\varepsilon)\cap A\) on which \(f\) is not a.e. zero and set
\(J:=I-\tau_{\max}\); then for every \(\lambda\ne-\tau_{\max}\),
\(J-\lambda=I-(\tau_{\max}+\lambda)\subset(-\infty,a)\) for \(\varepsilon\) sufficiently
small, so all competing translates lie in a known zero set and Lemma R36-A3 again yields a
contradiction.
\(\square\)

Status: \(\boxed{\text{R36-A4}\quad\checkmark[M].}\)

This is not yet a proof of \(\ker(H_{T_0}E_A)=\{0\}\); it is the first concrete **support
constraint** every hypothetical nonzero kernel vector must obey.

---

## 2b. Iterative peeling scheme

Corollary R36-A4 is the first instance of a general procedure. Define a decreasing sequence
of closed subsets
\[
A=K_0\supseteq K_1\supseteq K_2\supseteq\cdots
\]
as follows: given \(K_n\), let
\[
K_{n+1}:=K_n\setminus\bigcup\{I\subset K_n\text{ open}: \exists\,\lambda_*\in\Lambda_{T_0}\text{ with }J=I+\lambda_*\subset(-T_0,T_0)\text{ and }J-\lambda\subset A\setminus K_n\text{ for all }\lambda\ne\lambda_*\}.
\]
(At stage \(n+1\) the known-zero exposed-cell test of Lemma R36-A3 is re-run using the
already-cleared set \(A\setminus K_n\) as the known zero set. Thus terms landing in
\(A\setminus K_n\) are treated as inactive, even if they still lie geometrically inside the
annulus.)

### Proposition R36-A5 (peeling correctness)

For every \(n\), every \(0\ne y\in\ker(H_{T_0}E_A)\) satisfies
\(y=0\) a.e. on \(A\setminus K_n\).

### Proof

Induction on \(n\). The case \(n=0\) is vacuous (\(A\setminus K_0=\varnothing\)). Assume
\(y=0\) a.e. on \(A\setminus K_n\). For an interval \(I\) removed at stage \(n+1\), the
defining condition says every competing translate \(\lambda\ne\lambda_*\) sends
\(J=I+\lambda_*\) into the already-cleared zero set \(A\setminus K_n\). Thus the inductive
hypothesis provides the known zero set required by Lemma R36-A3, which yields
\(y=0\) a.e. on \(I\). Since
\(A\setminus K_{n+1}=(A\setminus K_n)\cup(\text{removed intervals})\), the claim propagates
to \(n+1\).
\(\square\)

Status: \(\boxed{\text{R36-A5}\quad\checkmark[M]\text{ (correctness of the peeling scheme, for every finite or infinite run length)}.}\)

### Corollary R36-A6 (peeling sufficiency and residual support)

Let \(K_\infty:=\bigcap_nK_n\).

- If \(K_\infty\) has measure zero (in particular if \(K_\infty=\varnothing\), hence in
  particular if the process terminates at some finite \(K_N=\varnothing\)), then every
  \(y\in\ker(H_{T_0}E_A)\) vanishes a.e. on \(A\), i.e.
  \[
  \boxed{\ker(H_{T_0}E_A)=\{0\}.}
  \]
- Equivalently, contrapositively,
  \[
  \boxed{\ker(H_{T_0}E_A)\ne\{0\}\ \Longrightarrow\ |K_\infty|>0.}
  \]
- If \(K_\infty\ne\varnothing\), this does **not** by itself produce a nonzero kernel vector.
  It shows only that any nonzero kernel vector must be supported (up to null sets) inside
  \(K_\infty\), and that on \(K_\infty\) no open interval is isolated by a single active
  translate in the sense of Lemma R36-A3. This is an **unexposed / multi-hit residual**, not
  yet a proved closed translation cycle. Existence of an actual nonzero \(y\) supported on
  \(K_\infty\) then requires a separate functional-equation analysis, not performed here.

### Proof

By Proposition R36-A5, every kernel vector vanishes a.e. on \(A\setminus K_n\) for every
\(n\), hence also on
\[
A\setminus K_\infty=\bigcup_n(A\setminus K_n).
\]
Therefore any kernel vector is supported (up to null sets) inside \(K_\infty\). If
\(|K_\infty|=0\), an \(L^2\)-vector supported on \(K_\infty\) must vanish a.e., giving
\(\ker(H_{T_0}E_A)=\{0\}\). The contrapositive is immediate. The final bullet is simply the
negation of removability under the peeling rule: points surviving in \(K_\infty\) were never
shown to vanish by a single-exposed-translate argument, but no actual kernel vector is thereby
constructed.
\(\square\)

Status: \(\boxed{\text{R36-A6}\quad\checkmark[M]\text{ (sufficient peeling criterion only; no equivalence between }K_\infty\neq\varnothing\text{ and kernel existence is claimed)}.}\)

### What remains open

Whether the concrete peeling process (run with the actual finite set
\(\Lambda_{T_0}=\{\pm\tau_{p,k}:(p,k)\in\mathcal P_{T_0}\}\) attached to a given \(T_0\), and a
given annulus \(A=A_{R,S}\)) yields \(|K_\infty|=0\), or instead leaves a positive-measure
unexposed residual, is not decided in this audit. This is now the precise combinatorial-
geometric sufficiency test delivered by peeling; it is **not** an equivalent reformulation of
kernel existence.

---

## 2c. Parity split

Let \(J\) denote reflection,
\[
(Jf)(u):=f(-u).
\]
Because \(D_s=U_{s/2}-U_{-s/2}\) and reflection conjugates translations by
\(JU_aJ=U_{-a}\), one has
\[
D_sJ=(U_{s/2}-U_{-s/2})J=J(U_{-s/2}-U_{s/2})=-JD_s.
\]
Since \(H_{T_0}\) is a finite linear combination of such \(D_s\), with symmetric windowing,
one gets the corresponding anticommutation for the finite-window hub.

### Proposition R36-A7 (parity split for the localized kernel)

One has
\[
\boxed{H_{T_0}J=-JH_{T_0}.}
\tag{R36.9}
\]
Consequently, if \(y\in\ker(H_{T_0}E_A)\), then its even and odd parts
\[
y_{\mathrm{ev}}:=\frac{y+Jy}{2},
\qquad
y_{\mathrm{odd}}:=\frac{y-Jy}{2}
\]
also satisfy
\[
H_{T_0}E_Ay_{\mathrm{ev}}=0,
\qquad
H_{T_0}E_Ay_{\mathrm{odd}}=0.
\]
Thus the kernel splits as the orthogonal direct sum of its even and odd sectors.

### Proof

Using the concrete P11 definition
\(H_{T_0}=P_{T_0}\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}D_{k\log p}E_{T_0}\), the identity
\(D_sJ=-JD_s\) together with the symmetry of the terminal window gives
\[
H_{T_0}J=P_{T_0}\sum c_{p,k}D_{k\log p}E_{T_0}J
=-P_{T_0}J\sum c_{p,k}D_{k\log p}E_{T_0}
=-JH_{T_0}.
\]
Because the annulus \(A=(-S,-R)\cup(R,S)\) is symmetric, \(JE_A=E_AJ\). Hence if
\(H_{T_0}E_Ay=0\), then
\[
H_{T_0}E_A(Jy)=H_{T_0}JE_Ay=-JH_{T_0}E_Ay=0.
\]
Linear combinations yield the same for \(y_{\mathrm{ev}}\) and \(y_{\mathrm{odd}}\), and the
orthogonal direct-sum decomposition is the standard parity decomposition in \(L^2(A)\).
\(\square\)

Status: \(\boxed{\text{R36-A7}\quad\checkmark[M].}\)

### Corollary R36-A8 (only the odd kernel can matter for R36-B)

The annular forcing target
\[
d_{R,S}:=P_A(\phi_S-C_{\Gamma,S}j_{R,S})
\]
is odd. Therefore every even kernel vector \(y\in\ker(H_{T_0}E_A)\) satisfies
\[
\langle y,d_{R,S}\rangle=0.
\]
In particular, only the **odd** part of the localized kernel can contribute to the
conditional annihilator test R36-B.

### Proof

The baseline forcing \(\phi_S(u)=\operatorname{sgn}(u)I_0(|u|)\) is explicitly odd in the R30
baseline module. The R30/R31/R32 chain works in the minus/odd sector, so the inherited
Riesz vector \(j_{R,S}=E_{R,S}\rho_{R,T_0}\) is odd as well. The Gamma operator
\(C_{\Gamma,S}\) has even symbol multiplier \(m_\Gamma\) (P11/O3af), hence preserves parity;
therefore \(C_{\Gamma,S}j_{R,S}\) is odd, and so is their difference \(\phi_S-C_{\Gamma,S}j_{R,S}\),
whence also its annular restriction \(d_{R,S}\). Pairing an even \(y\) with an odd
\(d_{R,S}\) gives zero by symmetry.
\(\square\)

Status: \(\boxed{\text{R36-A8}\quad\checkmark[M].}\)

This does not prove kernel triviality, but it **halves the relevant search space for R36-B**:
for obstruction purposes one only needs to study the odd kernel, which on the symmetric
annulus is determined by its values on \((R,S)\).

---

## 3. What the present repository does and does not prove

The existing O3 chain proves antisymmetry of \(H_{T_0}\) and an exact off-support translation
formula. This continuation sharpens the exposed-cell lemma to a known-zero version
(R36-A3), repairs the outer support proof (R36-A4), and corrects the peeling conclusion so
that it is a **sufficient** criterion for kernel triviality (R36-A6), not an equivalence.
It also adds a parity decomposition (R36-A7/A8), showing that only the odd localized kernel
can matter for the conditional obstruction test. Nowhere in R1–R36-A(continuation) is a
nonzero annular vector \(y\) constructed with \(H_{T_0}E_Ay=0\), nor is there a proof that the
peeling process yields \(|K_\infty|=0\) for every relevant \((R,S,T_0)\). No Paley–Wiener,
Fourier-symbol, or Volterra-triangular argument for the operator \(y\mapsto H_{T_0}E_Ay\) on
annulus-supported data is used or needed, precisely because such an argument would not respect
the finite-window restriction (see the Remark after Lemma R36-A3). Thus:

### Open Problem R36-A (first gate)

\[
\boxed{
\ker(H_{T_0}E_A)\stackrel?{=}\{0\}.
}
\tag{R36.4}
\]

Equivalently, by R36-A1,
\[
\overline{\operatorname{Ran}(P_AH_{T_0})}\stackrel?{=}L^2(A).
\]
A sufficient peeling criterion is now available:
\[
|K_\infty|=0\ \Longrightarrow\ \ker(H_{T_0}E_A)=\{0\},
\]
but the converse is **not** claimed. If a nonzero kernel exists, then necessarily
\(|K_\infty|>0\) by R36-A6.

Status: \(\boxed{\text{R36-A}\quad ?[O].}\)

This is the **only** status claimed for the ultimate kernel question in the present audit.

---

## 4. Conditional next step if the kernel is nontrivial

Suppose a future argument produces a nonzero
\[
0\ne y\in\ker(H_{T_0}E_A).
\]
By R36-A5/A6, any such \(y\) is necessarily supported (up to null sets) in the un-peelable
residue \(K_\infty\), which must have positive measure, and by R36-A4 its support extends to
within \(\tau_{\max}\) of the window boundary. By R36-A7/A8, only the odd component can matter
for the obstruction pairing. Then, and only then, one may ask whether \(y\) detects the
concrete annular target
\[
d_{R,S}:=P_A(\phi_S-C_{\Gamma,S}j_{R,S}).
\]

### Lemma R36-B (conditional annihilator test)

Assume \(0\ne y\in\ker(H_{T_0}E_A)\) and
\[
\langle y,d_{R,S}\rangle\ne0.
\tag{R36.5}
\]
Then
\[
P_A\Sigma_{T_0}j_{R,S}\ne d_{R,S}.
\tag{R36.6}
\]
Hence the annular compensation identity cannot hold for this triple
\((R,S,T_0)\).

### Proof

For every \(f\in L^2(-T_0,T_0)\),
\[
\langle y,P_A\Sigma_{T_0}f\rangle
=\langle E_Ay,\Sigma_{T_0}f\rangle
=\langle E_Ay,H_{T_0}B_{T_0}H_{T_0}^*f\rangle
=\langle H_{T_0}^*E_Ay,B_{T_0}H_{T_0}^*f\rangle.
\]
By Proposition O3AE.1, \(H_{T_0}^*=-H_{T_0}\), and since \(H_{T_0}E_Ay=0\), the right-hand
side vanishes. Thus
\[
\langle y,P_A\Sigma_{T_0}f\rangle=0
\qquad\text{for every }f.
\]
Taking \(f=j_{R,S}\) gives
\(
\langle y,P_A\Sigma_{T_0}j_{R,S}\rangle=0
\), whereas by assumption \(\langle y,d_{R,S}\rangle\ne0\). Therefore
\(P_A\Sigma_{T_0}j_{R,S}\ne d_{R,S}\).
\(\square\)

Status: \(\boxed{\text{R36-B}\quad \checkmark[M]\ \text{conditional on existence of }y\ne0\text{ with }\langle y,d_{R,S}\rangle\ne0.}\)

### Copy-edit firewall

The contradiction requires
\[
\boxed{\langle y,d_{R,S}\rangle\ne0,}
\]
not \(=0\). Any statement with \(=0\) would be useless for the obstruction argument.

---

## 5. If the kernel is trivial

If a future proof yields
\[
\ker(H_{T_0}E_A)=\{0\}
\]
(in particular if the peeling scheme of §2b is shown to leave only a null residual,
\(|K_\infty|=0\)), then by Lemma R36-A1 the localized hub range is dense in \(L^2(A)\). This
kills the simple dual annihilator route: there is no nontrivial continuous linear functional
on \(L^2(A)\) vanishing on the whole localized hub range. But even then, one still does
**not** get automatic representability of \(d_{R,S}\) as
\(P_AH_{T_0}g\) for some \(g\), because dense range need not equal actual range. The next
possible fingerprint would then be the harder question
\[
d_{R,S}\stackrel?\in \operatorname{Ran}(P_AH_{T_0}),
\qquad
\text{despite always having }d_{R,S}\in\overline{\operatorname{Ran}(P_AH_{T_0})}
\text{ if density holds.}
\]
That stricter membership problem cannot be detected by an ordinary annihilator.

---

## 6. Verdict and route map

| Item | Status |
|---|---|
| R36-A1 adjoint identity \(T_A^*=-H_{T_0}E_A\) and dense-range equivalence | ✓[M] |
| R36-A2 explicit finite translation kernel equation for \(y\) | ✓[M] |
| R36-A3 known-zero exposed-cell lemma | ✓[M] |
| R36-A4 outer support constraint via \(\tau_{\max}\) | ✓[M] |
| R36-A5 peeling-scheme correctness | ✓[M] |
| R36-A6 peeling sufficiency and residual-support criterion | ✓[M] |
| R36-A7 parity split for the localized kernel | ✓[M] |
| R36-A8 only the odd kernel can matter for R36-B | ✓[M] |
| R36-A kernel triviality / nontriviality for the concrete \(\Lambda_{T_0}\), \(A_{R,S}\) | ?[O] |
| R36-B annihilator obstruction from a nontrivial kernel vector with \(\langle y,d_{R,S}\rangle\ne0\) | ✓[M] conditional |
| Any conclusion on R30-F | not obtained |

### What this continuation adds

- Repairs the mathematical bug in the earlier proof of R36-A4: the contradiction interval is
  now chosen **left** of the essential right support edge, exactly where nonzero mass is
  guaranteed by the definition of essential supremum.
- Strengthens R36-A3 from a purely geometric exposed-cell statement to the **known-zero
  exposed-cell lemma**, which is the form actually used by the iterative peeling scheme.
- Corrects R36-A6: peeling yields a **sufficient** criterion for kernel triviality
  (\(|K_\infty|=0\Rightarrow\ker(H_{T_0}E_A)=\{0\}\)), not an equivalent reformulation of
  the kernel question. A nonempty residual is only an unexposed / multi-hit support region,
  not by itself a kernel vector.
- Replaces the earlier over-strong “translation cycle” language by the weaker and correct
  “unexposed / multi-hit residual” language.
- Adds the parity split R36-A7 and the odd-target corollary R36-A8. For the later R36-B
  obstruction search, only the **odd** localized kernel is relevant.

### What this audit explicitly does not deliver

- No proof that the kernel is nontrivial.
- No proof that the kernel is trivial, i.e. no proof that the peeling scheme yields
  \(|K_\infty|=0\) for the concrete \(\Lambda_{T_0}\), \(A_{R,S}\).
- No proof that a positive-measure residual \(K_\infty\) actually supports a nonzero kernel
  vector.
- No analysis of the potentially complicated orbit structure generated by the incommensurable
  shifts (e.g. \(\log3/\log2\notin\mathbb Q\)).
- No proof that the concrete target \(d_{R,S}\) lies or does not lie in the actual localized
  hub range.
- No statement upgrading \(\operatorname{Ran}\Sigma_{T_0}\subseteq\operatorname{Ran}H_{T_0}\) to an
  equality.
- No statement about R30-F, polar gauge, terminal transport, Object-X, or RH.

### Next mathematical target

The mathematically clean next step is now to combine **odd parity reduction** with the
peeling scheme: run §2b on the odd sector only, tracking whether the known-zero exposed-cell
criterion empties the odd residual set or leaves a positive-measure unexposed remainder. Only
if such an odd remainder survives should one begin a separate functional-equation search for a
nonzero odd kernel vector. Only after that would the conditional obstruction lemma R36-B come
into play.
