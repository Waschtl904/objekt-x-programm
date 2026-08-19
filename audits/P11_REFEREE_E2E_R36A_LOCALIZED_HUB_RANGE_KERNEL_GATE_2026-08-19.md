# P11 End-to-End Referee R36-A — Localized hub range: density versus annihilator kernel

Date: 2026-08-19 (continued 2026-08-19: exposed-cell lemma, support bound, peeling scheme;
corrected 2026-08-19: known-zero exposed cells, repaired support proof, parity split;
corrected again 2026-08-19: removed superfluous \(\varepsilon\)-condition in A4, retyped A3/A5
with full-line known-zero sets, added odd-sector unitary reduction R36-A9/A10;
corrected again 2026-08-19: fixed the A9 parity direction, removed the now-unnecessary A9
normalization caveat, replaced A10 by the two-map branch geometry, added R36-A11 folded
known-zero exposed-cell lemma)

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

## Repo sync

`main` at start of this audit: `971cd849ca3586f58ee5a858b1fbd6b3d388ec0f`.
`main` at start of the first continuation: `0d62bc711926267a65036c9230bd0923f9747d45`.
`main` at start of the exposed-cell/peeling continuation: `1db839139d48682fbb87ad49d9e0d5175fdcf881`.
`main` at start of the known-zero/parity-split repair: `81bfb752fcb93ad8895d9ba8abd7abf0a7127e64`.
`main` at start of this correction: `736730485f663066eddc78f9713047e01b3af50e` —
"Fix superfluous epsilon condition in R36-A4 proof, retype A3/A5 with full-line known-zero sets
Z_n = R\K_n, and add odd-sector reduction R36-A9 (unitary half-annulus kernel) and R36-A10
(folded translation isometry structure)". Commit confirmed by direct read-through.

Inputs: P11 §2 definitions of the source hub \(H_{T_0}\); R32 module
`P11_O3ae_HubOffSupport_Representation.tex`, especially Proposition O3AE.1 and
Theorem O3AE.2; R35 module/audit for the firewall that no localized annihilator is to
be presupposed; R30 baseline module `P11_O3ac_Riesz_Support_Radius.tex` for the oddness
of \(\phi_S\).

---

## 1. Exact operator identity for the localized range gate

### Lemma R36-A1 (adjoint identity)

For \(T_A=P_AH_{T_0}:L^2(-T_0,T_0)\to L^2(A)\),
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

Since \(P_A^*=E_A\) and \(H_{T_0}^*=-H_{T_0}\) (Prop. O3AE.1),
\(T_A^*=(P_AH_{T_0})^*=H_{T_0}^*E_A=-H_{T_0}E_A\). The duality identity
\(\overline{\operatorname{Ran}T_A}=(\ker T_A^*)^\perp\) gives (R36.2).
\(\square\)

Status: \(\boxed{\text{R36-A1}\quad\checkmark[M].}\)

### Firewall

A trivial kernel kills the simple Hahn–Banach annihilator route, but does not yet show that
the concrete target \(d_{R,S}:=P_A(\phi_S-C_{\Gamma,S}j_{R,S})\) lies in the actual (not just
dense) range.

---

## 2. Concrete form of the kernel equation

Let
\[
\tau_{p,k}:=\frac{k\log p}{2},
\qquad
c_{p,k}:=\sqrt{\log p}\,p^{-3k/4},
\qquad
\mathcal P_{T_0}:=\{(p,k):p^k\le e^{2T_0}\}.
\]

### Proposition R36-A2 (explicit kernel equation)

For \(y\in L^2(A)\), \(H_{T_0}E_Ay=0\) in \(L^2(-T_0,T_0)\) iff for a.e. \(u\in(-T_0,T_0)\),
\[
\boxed{
\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\Bigl[(E_Ay)(u-\tau_{p,k})-(E_Ay)(u+\tau_{p,k})\Bigr]=0.
}
\tag{R36.3}
\]

Status: \(\boxed{\text{R36-A2}\quad\checkmark[M].}\)

---

## 2a. Full-line known-zero exposed-cell lemma

Let \(\Lambda_{T_0}:=\{\pm\tau_{p,k}:(p,k)\in\mathcal P_{T_0}\}\),
\(a_{\tau_{p,k}}:=c_{p,k}\), \(a_{-\tau_{p,k}}:=-c_{p,k}\), and
\(f:=E_{T_0}E_Ay\in L^2(\mathbb R)\), \(\operatorname{supp}f\subset A\). Equation (R36.3) reads,
for a.e. \(u\in(-T_0,T_0)\),
\[
\boxed{
(H_{T_0}f)(u)=\sum_{\lambda\in\Lambda_{T_0}}a_\lambda f(u-\lambda)=0.
}
\tag{R36.3$'$}
\]

### Lemma R36-A3 (full-line known-zero exposed-cell lemma)

Let \(Z\subset\mathbb R\) be any measurable set on which \(f\) is already known to vanish
a.e. Let \(I\subset A\) be a nonempty open interval and \(\lambda_*\in\Lambda_{T_0}\). Put
\(J:=I+\lambda_*\). If \(J\subset(-T_0,T_0)\) and \(J-\lambda\subset Z\) for every
\(\lambda\in\Lambda_{T_0}\setminus\{\lambda_*\}\), then every \(f=E_{T_0}E_Ay\) solving
(R36.3\('\)) satisfies \(y=0\) a.e. on \(I\).

Status: \(\boxed{\text{R36-A3}\quad\checkmark[M].}\)

### Corollary R36-A4 (outer support constraint via \(\tau_{\max}\))

Let \(\tau_{\max}:=\max_{(p,k)\in\mathcal P_{T_0}}\tau_{p,k}\). If
\(0\ne y\in\ker(H_{T_0}E_A)\), \(f=E_{T_0}E_Ay\), \(b:=\operatorname{ess\,sup}\operatorname{supp}f\),
then \(b+\tau_{\max}\ge T_0\); symmetrically \(a:=\operatorname{ess\,inf}\operatorname{supp}f\)
satisfies \(a\le-T_0+\tau_{\max}\). (Proof: as previously repaired, using
\(g:=\min_{\lambda\ne\tau_{\max}}(\tau_{\max}-\lambda)>0\), \(0<\varepsilon<g/4\), and an
interval \(I\subset(b-\varepsilon,b)\cap A\); no further condition on \(\varepsilon\) is
needed.)

Status: \(\boxed{\text{R36-A4}\quad\checkmark[M].}\)

---

## 2b. Iterative peeling scheme

With \(Z_n:=\mathbb R\setminus K_n\), \(A=K_0\supseteq K_1\supseteq\cdots\),
\[
K_{n+1}:=K_n\setminus\bigcup\{I\subset K_n\text{ open}:\exists\lambda_*,\ J=I+\lambda_*\subset(-T_0,T_0),\ J-\lambda\subset Z_n\ \forall\lambda\ne\lambda_*\}.
\]

### Proposition R36-A5 / Corollary R36-A6

Every \(0\ne y\in\ker(H_{T_0}E_A)\) vanishes a.e. on \(A\setminus K_n\) for every \(n\). If
\(K_\infty:=\bigcap_nK_n\) has measure zero, then \(\ker(H_{T_0}E_A)=\{0\}\); contrapositively
\(\ker(H_{T_0}E_A)\ne\{0\}\Rightarrow|K_\infty|>0\). \(K_\infty\ne\varnothing\) is only an
unexposed / multi-hit residual, not itself a kernel vector.

Status: \(\boxed{\text{R36-A5, R36-A6}\quad\checkmark[M]\text{ (sufficiency only)}.}\)

---

## 2c. Parity split — corrected direction

Let \((Jf)(u):=f(-u)\).

### Proposition R36-A7 (anticommutation)

\[
\boxed{H_{T_0}J=-JH_{T_0}.}
\tag{R36.9}
\]

Status: \(\boxed{\text{R36-A7}\quad\checkmark[M].}\) (Unchanged; only its consequence for
parity mapping, stated in the previous R36-A9 remark, was wrong and is corrected below.)

### Corrected parity consequence

**Correction.** The previous continuation asserted, incorrectly, that \(H_{T_0}\) maps odd
functions to odd functions. The correct consequence of (R36.9) is the opposite parity flip.
Let \(f\) be odd, i.e. \(Jf=-f\). Then
\[
H_{T_0}(Jf)=H_{T_0}(-f)=-H_{T_0}f,
\]
while by (R36.9), \(H_{T_0}(Jf)=(H_{T_0}J)f=-JH_{T_0}f\). Equating,
\[
-H_{T_0}f=-JH_{T_0}f
\quad\Longrightarrow\quad
J(H_{T_0}f)=H_{T_0}f,
\]
so \(H_{T_0}f\) is **even**. Symmetrically, \(H_{T_0}\) maps even functions to odd functions.
Thus
\[
\boxed{H_{T_0}:\ \text{odd}\longrightarrow\text{even},\qquad H_{T_0}:\ \text{even}\longrightarrow\text{odd}.}
\]
Consequently, for \(y\in\ker(H_{T_0}E_A)\), the even/odd decomposition \(y=y_{\mathrm{ev}}+y_{\mathrm{odd}}\)
still splits the kernel equation into two independent equations \(H_{T_0}E_Ay_{\mathrm{ev}}=0\)
and \(H_{T_0}E_Ay_{\mathrm{odd}}=0\) (this step used only linearity, not the wrong parity-mapping
claim), so the orthogonal direct-sum splitting of R36-A7 stands. What changes is only *why* the
half-interval reduction below works: since \(y_{\mathrm{odd}}\) is odd, \(E_Ay_{\mathrm{odd}}\)
is odd, so \(H_{T_0}E_Ay_{\mathrm{odd}}\) is **even**, and an even function vanishes a.e. on
\((-T_0,T_0)\) iff it vanishes a.e. on \((0,T_0)\). Hence
\[
\boxed{
H_{T_0}E_Ay_{\mathrm{odd}}=0\text{ on }(-T_0,T_0)
\iff
H_{T_0}E_Ay_{\mathrm{odd}}=0\text{ on }(0,T_0).
}
\]

Status: \(\boxed{\text{R36-A7 (anticommutation)}\quad\checkmark[M]\text{; corrected parity-mapping consequence}\quad\checkmark[M]\text{; previous odd}\to\text{odd claim retracted}.}\)

### Corollary R36-A8 (only the odd kernel can matter for R36-B) — unaffected

\(d_{R,S}\) is odd (R30 baseline oddness of \(\phi_S\), inherited oddness of \(j_{R,S}\), even
symbol of \(C_{\Gamma,S}\)). Hence every even \(y\in\ker(H_{T_0}E_A)\) satisfies
\(\langle y,d_{R,S}\rangle=0\); only the odd kernel can matter for R36-B. This conclusion did
not depend on the (incorrect) odd\(\to\)odd claim and is unaffected by the correction above.

Status: \(\boxed{\text{R36-A8}\quad\checkmark[M].}\)

---

## 2d. Unitary reduction of the odd kernel to the half-annulus — caveat removed

Define, for \(h\in L^2(R,S)\),
\[
(U_-h)(x):=\frac{1}{\sqrt2}\operatorname{sgn}(x)\,h(|x|)\,\mathbf 1_{\{R<|x|<S\}}.
\]

### Proposition R36-A9 (unitary reduction of the odd annular kernel)

\(U_-:L^2(R,S)\to L^2_{\mathrm{odd}}(A)\) is unitary:
\[
\|U_-h\|^2_{L^2(A)}=\int_{-S}^{-R}\tfrac12|h(|x|)|^2\,dx+\int_R^S\tfrac12|h(x)|^2\,dx
=\tfrac12\|h\|^2+\tfrac12\|h\|^2=\|h\|^2,
\]
using the substitution \(x\mapsto-x\) on \((-S,-R)\); each half-annulus contributes exactly
half the norm. Because \(E_Ay_{\mathrm{odd}}\) is odd, hence \(H_{T_0}E_Ay_{\mathrm{odd}}\) is even
(corrected parity consequence above), the kernel equation for odd \(y=U_-h\) is equivalent to
its restriction to \(u\in(0,T_0)\), where it takes the explicit form
\[
\boxed{
(L_{R,S,T_0}h)(u):=\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\Bigl[
\operatorname{sgn}(u-\tau_{p,k})\,\mathbf 1_{(R,S)}(|u-\tau_{p,k}|)\,h(|u-\tau_{p,k}|)
-\mathbf 1_{(R,S)}(u+\tau_{p,k})\,h(u+\tau_{p,k})
\Bigr]=0
}
\tag{R36.10}
\]
for a.e. \(u\in(0,T_0)\), and
\[
\boxed{
\ker(H_{T_0}E_A)\cap L^2_{\mathrm{odd}}(A)\ \simeq\ \ker L_{R,S,T_0}.
}
\tag{R36.11}
\]

### Proof

Unitarity is the direct computation above. The equivalence of the full-window and
half-window kernel equations follows from the corrected parity consequence, not from the
previously claimed (incorrect) odd\(\to\)odd mapping. The substitution
\(f(u+\tau_{p,k})=\frac1{\sqrt2}\mathbf1_{(R,S)}(u+\tau_{p,k})h(u+\tau_{p,k})\) (as
\(u+\tau_{p,k}>0\)) and
\(f(u-\tau_{p,k})=\frac1{\sqrt2}\operatorname{sgn}(u-\tau_{p,k})\mathbf1_{(R,S)}(|u-\tau_{p,k}|)h(|u-\tau_{p,k}|)\)
(using oddness of \(f\)) into (R36.3) on \((0,T_0)\), after cancelling the common factor
\(1/\sqrt2\), gives exactly (R36.10) termwise, confirming the requester's independent
termwise check. \(\square\)

Status: \(\boxed{\text{R36-A9}\quad\checkmark[M].}\) The previous caveat "modulo a routine but
not yet independently re-verified check of all extension/normalization factors" is **removed**:
both the unitarity computation and the termwise substitution have now been verified
independently, and the parity-direction error that motivated re-checking has been isolated and
fixed above without affecting (R36.10)–(R36.11).

---

## 2e. Corrected branch geometry (replaces the former R36-A10)

### Branch table for fixed \(x\in(R,S)\)

For a fixed \((p,k)\) with \(\tau:=\tau_{p,k}\) and a fixed target value \(x\in(R,S)\), equation
(R36.10) shows that \(x\) is hit by the term at \(u\) exactly when one of the following holds,
with the indicated sign as it enters \((L_{R,S,T_0}h)(u)=0\):

| Condition | \(u=\) | Sign in \(L\) |
|---|---|---|
| \(u-\tau=x\) | \(x+\tau\) | \(+c_\tau\) |
| \(u+\tau=x\) | \(x-\tau\) | \(-c_\tau\) |
| \(\tau-u=x\) | \(\tau-x\) | \(-c_\tau\) |

This corrects the former R36-A10, which had assigned the plain-translate term \(u+\tau=x\)
the sign \(+1\) (it is \(-c_\tau\), matching the minus sign in front of
\(\mathbf1_{(R,S)}(u+\tau)h(u+\tau)\) in (R36.10)) and had geometrically swapped the roles of
the first two rows.

### Two-map reformulation

The three branches collapse to two geometric maps on \(x\)-space:
\[
\boxed{
\Phi_{\tau,+}(x):=x+\tau,\qquad\text{weight }+c_\tau,
}
\qquad
\boxed{
\Phi_{\tau,-}(x):=|x-\tau|,\qquad\text{weight }-c_\tau,
}
\]
since \(\Phi_{\tau,-}(x)=x-\tau\) for \(x>\tau\) and \(\Phi_{\tau,-}(x)=\tau-x\) for \(x<\tau\),
recovering exactly the second and third rows of the table with the common weight
\(-c_\tau\). Equation (R36.10), read as an equation indexed by the target point \(u\), is thus
generated by the finite family of weighted maps \(\{\Phi_{\tau,+},\Phi_{\tau,-}\}_{(p,k)\in\mathcal P_{T_0}}\).

\(\Phi_{\tau,-}\) is continuous but **not affine on all of \((R,S)\)** when \(\tau\in(R,S)\),
since it has a corner at \(x=\tau\). It is affine on each side of that corner.

### R36-A10 (cell decomposition and affine branch geometry)

Let
\[
\{R,S\}\cup\{\tau_{p,k}:(p,k)\in\mathcal P_{T_0},\,R<\tau_{p,k}<S\}
\]
be the finite set of breakpoints in \(\overline{(R,S)}\), and let
\[
(R,S)=\bigcup_\alpha I_\alpha
\]
be the resulting finite decomposition into open cells with no breakpoint in their interior.
On each cell \(I_\alpha\) and for each active \(\tau=\tau_{p,k}\), the map \(\Phi_{\tau,+}\) is
affine (indeed a pure translation) on all of \((R,S)\), and \(\Phi_{\tau,-}\) restricted to
\(I_\alpha\) is affine, equal to \(x\mapsto x-\tau\) if \(I_\alpha\) lies entirely to the right of
\(\tau\), or to \(x\mapsto\tau-x\) if \(I_\alpha\) lies entirely to the left of \(\tau\) (no cell
contains \(\tau\) in its interior, by construction of the breakpoint set).

Status: \(\boxed{\text{R36-A10}\quad\checkmark[M]\text{ (corrected branch table and two-map/cell-decomposition geometry; replaces the previous, incorrectly assigned three-branch statement)}.}\)

---

## 2f. R36-A11: folded known-zero exposed-cell lemma

### Lemma R36-A11 (folded known-zero exposed-cell lemma on the half-annulus)

Let \(Z\subset(R,S)\) be a measurable set on which \(h\) is already known to vanish a.e. Let
\(I\subset(R,S)\) be a nonempty open interval contained in a single cell \(I_\alpha\) of the
breakpoint decomposition, and let \(B_*\in\{\Phi_{\tau,+},\Phi_{\tau,-}:(p,k)\in\mathcal P_{T_0}\}\)
be one of the active branch maps, restricted to \(I_\alpha\) (hence affine on \(I\)). Put
\(J:=B_*(I)\). Suppose
\[
J\subset(0,T_0)
\qquad\text{and}\qquad
B(I)\subset Z\ \text{for every other active branch }B\ne B_*\text{ that maps }I\text{ into }(0,T_0).
\]
Then every \(h\) solving \((L_{R,S,T_0}h)(u)=0\) a.e. on \((0,T_0)\) satisfies
\[
\boxed{h=0\quad\text{a.e. on }I.}
\]

### Proof

Fix \(u\in J\); write \(u=B_*(x)\) for \(x\in I\) via the inverse of the affine isometry
\(B_*\). By (R36.10), \((L_{R,S,T_0}h)(u)=0\) is a finite sum over all active
\((p,k)\)-branches evaluated at \(u\); each summand is a scalar multiple of
\(\mathbf1_{(R,S)}(y)h(y)\) for the corresponding preimage \(y=B^{-1}(u)\) under the relevant
branch \(B\). For every branch \(B\ne B_*\) that sends some point of \(I\) into \((0,T_0)\), the
hypothesis places \(B(I)\subset Z\) (understood via the same identification of branch and
preimage), so the corresponding term vanishes a.e. on \(J\) because \(h=0\) a.e. on \(Z\)
(branches not mapping any point of \(I\) into \((0,T_0)\) contribute no term at all, by the
indicator functions in (R36.10)). Hence the sum reduces to the single nonzero-weight term
coming from \(B_*\), which forces \(h(B_*^{-1}(u))=0\) for a.e. \(u\in J\), i.e. \(h=0\) a.e. on
\(I=B_*^{-1}(J)\).
\(\square\)

Status: \(\boxed{\text{R36-A11}\quad\checkmark[M].}\)

This is precisely the positive-half-annulus, folded analogue of Lemma R36-A3.

### Folded peeling scheme (definition only, not yet run)

Define \(K_0^-:=(R,S)\supseteq K_1^-\supseteq K_2^-\supseteq\cdots\) by removing, at each stage,
every open subinterval of a cell that is exposed in the sense of Lemma R36-A11 with known-zero
set \(Z_n^-:=(R,S)\setminus K_n^-\). By the same induction as in R36-A5,
\[
\boxed{
|K_\infty^-|=0\ \Longrightarrow\ \ker L_{R,S,T_0}=\{0\},
}
\]
where \(K_\infty^-:=\bigcap_nK_n^-\), and **not** the converse; a nonempty positive-measure
\(K_\infty^-\) is again only an unexposed / multi-hit residual on the half-annulus, requiring a
separate functional-equation analysis before any nonzero \(h\) could be exhibited.

Status: \(\boxed{\text{folded peeling scheme}\quad\checkmark[M]\text{ definition and sufficiency-direction correctness; no run performed}.}\)

### Sharper gate for R36-B (unchanged in content, now resting on corrected R36-A9/A10/A11)

\[
\boxed{
\ker(H_{T_0}E_A)\cap L^2_{\mathrm{odd}}(A)\ \simeq\ \ker L_{R,S,T_0}\ \stackrel?{=}\ \{0\}.
}
\tag{R36.12}
\]
If trivial, the annihilator route for R36-B is dead regardless of any even kernel. If a nonzero
\(0\ne h\in\ker L_{R,S,T_0}\) is found, the next and only remaining question is
\[
\langle U_-h,d_{R,S}\rangle\stackrel?{=}0.
\]
Only a negative answer here (i.e. \(\ne0\)) feeds Lemma R36-B.

---

## 3. What the present repository does and does not prove

This correction (i) fixes the parity-mapping direction: \(H_{T_0}\) maps odd functions to
**even** functions (and vice versa), not odd to odd as previously and incorrectly stated; the
half-window reduction is preserved because it only needed that \(H_{T_0}E_Ay_{\mathrm{odd}}\)
is even, which still holds; (ii) removes the R36-A9 normalization caveat, since both the
unitarity computation and the termwise substitution into (R36.10) have now been independently
verified; (iii) replaces the former R36-A10 by a corrected branch table and the two-map
reformulation \(\Phi_{\tau,+}(x)=x+\tau\) (weight \(+c_\tau\)) and \(\Phi_{\tau,-}(x)=|x-\tau|\)
(weight \(-c_\tau\)), together with the breakpoint cell decomposition needed to make
\(\Phi_{\tau,-}\) affine on each cell; (iv) adds R36-A11, the folded known-zero exposed-cell
lemma on \((R,S)\), and defines (without running) the corresponding folded peeling scheme.
No nonzero \(y\) or \(h\) is constructed anywhere, and no peeling run — full-annulus or
folded half-annulus — has been executed. Thus:

### Open Problem R36-A (first gate) and sharper odd gate

\[
\ker(H_{T_0}E_A)\stackrel?{=}\{0\}
\qquad\text{(R36-A, status ?[O])},
\qquad
\ker L_{R,S,T_0}\stackrel?{=}\{0\}
\qquad\text{(sharper gate for R36-B, status ?[O])}.
\]

---

## 4. Conditional next step if the odd kernel is nontrivial

Unchanged: if a future argument produces \(0\ne h\in\ker L_{R,S,T_0}\), set \(y:=U_-h\), and
Lemma R36-B applies verbatim.

### Lemma R36-B (conditional annihilator test) — unchanged

Assume \(0\ne y\in\ker(H_{T_0}E_A)\) and \(\langle y,d_{R,S}\rangle\ne0\). Then
\(P_A\Sigma_{T_0}j_{R,S}\ne d_{R,S}\) (Proposition O3AE.1 antisymmetry and
\(H_{T_0}E_Ay=0\)).

Status: \(\boxed{\text{R36-B}\quad\checkmark[M]\ \text{conditional}.}\)

---

## 5. If the kernel is trivial

Unchanged: dense range only, not automatic exact-range membership of \(d_{R,S}\).

---

## 6. Verdict and route map

| Item | Status |
|---|---|
| R36-A1 adjoint identity and dense-range equivalence | ✓[M] |
| R36-A2 explicit finite translation kernel equation | ✓[M] |
| R36-A3 full-line known-zero exposed-cell lemma | ✓[M] |
| R36-A4 outer support constraint via \(\tau_{\max}\) | ✓[M] |
| R36-A5/A6 peeling correctness and sufficiency | ✓[M] |
| R36-A7 anticommutation \(H_{T_0}J=-JH_{T_0}\); corrected parity-mapping consequence (odd\(\to\)even, even\(\to\)odd) | ✓[M] (previous odd\(\to\)odd claim retracted) |
| R36-A8 only odd kernel matters for R36-B | ✓[M] |
| R36-A9 unitary reduction of odd kernel to half-annulus equation \(L_{R,S,T_0}\) | ✓[M] (normalization caveat removed) |
| R36-A10 corrected branch table / two-map geometry / cell decomposition | ✓[M] |
| R36-A11 folded known-zero exposed-cell lemma on \((R,S)\) | ✓[M] |
| Folded peeling scheme on \((R,S)\) | defined, sufficiency-only, not run |
| R36-A kernel triviality (full annulus) | ?[O] |
| Sharper gate \(\ker L_{R,S,T_0}=?\{0\}\) (odd/folded) | ?[O] |
| R36-B annihilator obstruction, conditional | ✓[M] conditional |
| R30-F | not obtained |

### What this correction adds

- Fixes the R36-A9 parity-mapping direction: \(H_{T_0}\) sends odd functions to even functions
  and even functions to odd functions, derived directly from \(H_{T_0}J=-JH_{T_0}\); the
  half-window reduction to \((0,T_0)\) is re-derived from the correct fact that
  \(H_{T_0}E_Ay_{\mathrm{odd}}\) is even.
- Removes the R36-A9 normalization caveat after independently verifying both the unitarity
  computation \(\|U_-h\|^2=\|h\|^2\) and the termwise substitution into (R36.10).
- Replaces the former (miscategorized) R36-A10 branch table with the corrected table and the
  two-map reformulation \(\Phi_{\tau,+}(x)=x+\tau\) (weight \(+c_\tau\)),
  \(\Phi_{\tau,-}(x)=|x-\tau|\) (weight \(-c_\tau\)), together with the breakpoint cell
  decomposition of \((R,S)\) needed for affinity of \(\Phi_{\tau,-}\) on each cell.
- Adds R36-A11, the folded known-zero exposed-cell lemma, and defines the associated folded
  peeling scheme on \((R,S)\) (not yet run), with the same sufficiency-only conclusion
  \(|K_\infty^-|=0\Rightarrow\ker L_{R,S,T_0}=\{0\}\).

### What this audit explicitly does not deliver

- No proof that \(\ker(H_{T_0}E_A)\) or \(\ker L_{R,S,T_0}\) is trivial or nontrivial.
- No folded peeling run has been performed on \((R,S)\).
- No statement about R30-F, polar gauge, terminal transport, Object-X, or RH.

### Next mathematical target

Run the folded peeling scheme defined in §2f explicitly on \((R,S)\), using the cell
decomposition and the two branch maps \(\Phi_{\tau,\pm}\) of R36-A10, for a representative
choice of \(R,S\) but still without committing to a concrete \(T_0\). Track
\(K_0^-\supseteq K_1^-\supseteq\cdots\) explicitly; either exhibit \(|K_N^-|=0\) at some finite
stage, or characterize the geometry of a surviving positive-measure residual \(K_\infty^-\).
Only after that should a functional-equation search for a nonzero \(h\) begin, followed by the
pairing test \(\langle U_-h,d_{R,S}\rangle\stackrel?=0\) and finally Lemma R36-B.
