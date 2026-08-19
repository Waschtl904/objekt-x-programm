# P11 End-to-End Referee R36-A — Localized hub range: density versus annihilator kernel

Date: 2026-08-19

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
\operatorname{Ran}(P_AH_{T_0})\stackrel?{=}L^2(A)
\qquad\Longleftrightarrow\qquad
\ker(H_{T_0}E_A)\stackrel?{=}\{0\}.
\]
No existence of a localized annihilator is assumed. No statement about R30-F is made.

## Repo sync

`main` at start of this audit: `971cd849ca3586f58ee5a858b1fbd6b3d388ec0f` —
"Hook P11_O3ag (R35 contraction no-go / resolvent repair) into the O3 chain after O3af".

Inputs: P11 §2 definitions of the source hub \(H_{T_0}\); R32 module
`P11_O3ae_HubOffSupport_Representation.tex`, especially Proposition O3AE.1 and
Theorem O3AE.2; R35 module/audit for the firewall that no localized annihilator is to
be presupposed.

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
\(H_{T_0}E_Ay=0\) becomes a finite translation system on the source interval.
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
Equivalently, because \(E_Ay\) vanishes off \(A\), this is a finite linear system of
translated annular traces of \(y\) on the source interval \((-T_0,T_0)\).

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

## 3. What the present repository does and does not prove

The existing O3 chain proves antisymmetry of \(H_{T_0}\) and an exact off-support translation
formula, but nowhere in R1–R35 is a nonzero annular vector \(y\) constructed with
\(H_{T_0}E_Ay=0\), nor is there a theorem forcing every such \(y\) to vanish.
The current repository also contains no Paley–Wiener, Fourier-symbol, or Volterra-triangular
argument for the operator \(y\mapsto H_{T_0}E_Ay\) on annulus-supported data. Thus:

### Open Problem R36-A (first gate)

\[
\boxed{
\ker(H_{T_0}E_A)\stackrel?{=}\{0\}
\qquad\text{equivalently}\qquad
\overline{\operatorname{Ran}(P_AH_{T_0})}\stackrel?{=}L^2(A).
}
\tag{R36.4}
\]

Status: \(\boxed{\text{R36-A}\quad ?[O].}\)

This is the **only** status claimed in the present audit.

---

## 4. Conditional next step if the kernel is nontrivial

Suppose a future argument produces a nonzero
\[
0\ne y\in\ker(H_{T_0}E_A).
\]
Then, and only then, one may ask whether it detects the concrete annular target
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
\ker(H_{T_0}E_A)=\{0\},
\]
then by Lemma R36-A1 the localized hub range is dense in \(L^2(A)\). This kills the
simple dual annihilator route: there is no nontrivial continuous linear functional on
\(L^2(A)\) vanishing on the whole localized hub range. But even then, one still does
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
| R36-A kernel triviality / nontriviality | ?[O] |
| R36-B annihilator obstruction from a nontrivial kernel vector with \(\langle y,d_{R,S}\rangle\ne0\) | ✓[M] conditional |
| Any conclusion on R30-F | not obtained |

### What this audit adds

- It isolates the **first exact localized gate**:
  \(\ker(H_{T_0}E_A)\stackrel?=\{0\}\), equivalently density of the localized hub range.
- It rewrites that gate as the concrete finite translation equation (R36.3), using only the
  explicit prime-power form of \(H_{T_0}\).
- It records the precise conditional obstruction lemma R36-B, with the correct requirement
  \(\langle y,d_{R,S}\rangle\ne0\).

### What this audit explicitly does not deliver

- No proof that the kernel is nontrivial.
- No proof that the kernel is trivial.
- No proof that the concrete target \(d_{R,S}\) lies or does not lie in the actual localized
  hub range.
- No statement upgrading \(\operatorname{Ran}\Sigma_{T_0}\subseteq\operatorname{Ran}H_{T_0}\) to an
  equality.
- No statement about R30-F, polar gauge, terminal transport, Object-X, or RH.

### Next mathematical target

The next legitimate step is still exactly the one prescribed in the brief:
try to solve the concrete finite translation equation (R36.3) on annulus-supported data,
either by constructing a nonzero kernel vector \(y\) or by proving uniqueness \(y=0\).
Only if a nonzero kernel vector exists should one then test whether it pairs nontrivially
with \(d_{R,S}\).
