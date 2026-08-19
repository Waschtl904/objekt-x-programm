# P11 End-to-End Referee R36-A — Localized hub range: density versus annihilator kernel

Date: 2026-08-19 (continued 2026-08-19: exposed-cell lemma, support bound, peeling scheme; corrected 2026-08-19: known-zero exposed cells, repaired support proof, parity split; corrected again 2026-08-19: removed superfluous \(\varepsilon\)-condition in A4, retyped A3/A5 with full-line known-zero sets, added odd-sector unitary reduction R36-A9/A10)

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

**Correction (added in the exposed-cell continuation).** The Target statement above
previously displayed the left-hand side as the unclosed range \(\operatorname{Ran}(P_AH_{T_0})\)
with an unresolved \(\stackrel?=\); the operative object throughout R36-A1/A2/A3 is always
the **closure** \(\overline{\operatorname{Ran}(P_AH_{T_0})}\), and the equivalence with
\(\ker(H_{T_0}E_A)=\{0\}\) is a proved fact (R36-A1), not an open question.

## Repo sync

`main` at start of this audit: `971cd849ca3586f58ee5a858b1fbd6b3d388ec0f` —
"Hook P11_O3ag (R35 contraction no-go / resolvent repair) into the O3 chain after O3af".
`main` at start of the first continuation: `0d62bc711926267a65036c9230bd0923f9747d45`.
`main` at start of the exposed-cell/peeling continuation: `1db839139d48682fbb87ad49d9e0d5175fdcf881`.
`main` at start of the known-zero/parity-split repair: `81bfb752fcb93ad8895d9ba8abd7abf0a7127e64` —
"Repair R36-A: strengthen A3 to known-zero exposed-cell lemma, fix A4 proof using left-near-edge
interval and positive gap g, weaken A6 to sufficiency only, and add A7/A8 parity split showing only
odd kernel matters for R36-B". Commit confirmed by direct read-through.

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
A trivial kernel kills the simple Hahn–Banach annihilator route, but does **not** yet show
that the concrete target vector \(d_{R,S}:=P_A(\phi_S-C_{\Gamma,S}j_{R,S})\) lies in the
actual range; it only removes the possibility of detecting a failure by a continuous
annihilator.

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
\(H_{T_0}E_Ay=0\) in \(L^2(-T_0,T_0)\) if and only if for a.e. \(u\in(-T_0,T_0)\),
\[
\boxed{
\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\Bigl[(E_Ay)(u-\tau_{p,k})-(E_Ay)(u+\tau_{p,k})\Bigr]=0.
}
\tag{R36.3}
\]

### Proof

This is the definition of \(H_{T_0}\) from P11 §2 / equation (2.5), applied to \(E_Ay\).
\(\square\)

Status: \(\boxed{\text{R36-A2}\quad\checkmark[M].}\)

---

## 2a. Compact reformulation and the full-line known-zero exposed-cell lemma

Let
\[
\Lambda_{T_0}:=\{\pm\tau_{p,k}:(p,k)\in\mathcal P_{T_0}\},
\qquad
a_{\tau_{p,k}}:=c_{p,k},\quad a_{-\tau_{p,k}}:=-c_{p,k},
\]
and, following the reorganization requested in this correction, work throughout with the
**full-line** zero extension
\[
f:=E_{T_0}E_Ay\in L^2(\mathbb R),
\qquad
\operatorname{supp}f\subset A,
\]
where \(E_{T_0}\) is zero extension of \(L^2(-T_0,T_0)\)-functions to all of \(\mathbb R\).
Equation (R36.3) reads, for a.e. \(u\in(-T_0,T_0)\),
\[
\boxed{
(H_{T_0}f)(u)=\sum_{\lambda\in\Lambda_{T_0}}a_\lambda f(u-\lambda)=0.
}
\tag{R36.3$'$}
\]
All \(a_\lambda\ne0\).

### Lemma R36-A3 (full-line known-zero exposed-cell lemma)

Let \(Z\subset\mathbb R\) be **any** measurable set (not necessarily contained in
\((-T_0,T_0)\)) on which \(f\) is already known to vanish a.e. Let \(I\subset A\) be a
nonempty open interval and \(\lambda_*\in\Lambda_{T_0}\). Put \(J:=I+\lambda_*\). Suppose
\[
J\subset(-T_0,T_0)
\qquad\text{and}\qquad
J-\lambda\subset Z\ \ \text{for every }\lambda\in\Lambda_{T_0}\setminus\{\lambda_*\}.
\tag{R36.7}
\]
Then every \(f=E_{T_0}E_Ay\) solving (R36.3\('\)) satisfies \(y=0\) a.e. on \(I\).

In particular, \(Z\) may be taken to include points outside \((-T_0,T_0)\) (where \(f\)
vanishes automatically because \(E_{T_0}\) is a zero extension) and points outside \(A\)
(where \(f\) vanishes automatically because \(E_A\) is a zero extension); the lemma only
requires that \(Z\) be a known-zero set for \(f\) on all of \(\mathbb R\), by whatever
combination of these two automatic reasons or prior peeling stages.

### Proof

Fix \(u\in J\subset(-T_0,T_0)\). By (R36.3\('\)), \(\sum_\lambda a_\lambda f(u-\lambda)=0\).
For \(\lambda\ne\lambda_*\), \(u-\lambda\in J-\lambda\subset Z\), so \(f(u-\lambda)=0\) a.e.
Hence the sum reduces to \(a_{\lambda_*}f(u-\lambda_*)=0\), and since \(a_{\lambda_*}\ne0\),
\(f(u-\lambda_*)=0\) for a.e. \(u\in J\), i.e. \(f=0\) a.e. on \(J-\lambda_*=I\). Because
\(I\subset A\), \(f|_I=y|_I\), so \(y=0\) a.e. on \(I\).
\(\square\)

Status: \(\boxed{\text{R36-A3}\quad\checkmark[M].}\)

### Remark (why not a global Fourier argument)

Equation (R36.3\('\)) only asserts \(H_{T_0}f=0\) on the finite window \((-T_0,T_0)\);
outside that window the full translation sum may be nonzero. R36-A3 never uses the
equation outside \((-T_0,T_0)\), so no global exponential-polynomial uniqueness argument
is smuggled in, even though \(Z\) itself is now allowed to range over all of \(\mathbb R\).

### Corollary R36-A4 (outer support constraint via \(\tau_{\max}\))

Let \(\tau_{\max}:=\max_{(p,k)\in\mathcal P_{T_0}}\tau_{p,k}\). If
\(0\ne y\in\ker(H_{T_0}E_A)\), \(f=E_{T_0}E_Ay\), \(b:=\operatorname{ess\,sup}\operatorname{supp}f\)
(so \(b\le S\)), then necessarily
\[
\boxed{b+\tau_{\max}\ge T_0,\qquad\text{i.e.}\qquad b\ge T_0-\tau_{\max}.}
\]
Symmetrically \(a:=\operatorname{ess\,inf}\operatorname{supp}f\) satisfies
\(a\le-T_0+\tau_{\max}\), giving
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
Suppose for contradiction \(b+\tau_{\max}<T_0\). Choose any
\[
0<\varepsilon<g/4.
\]
(No further condition on \(\varepsilon\) is needed or imposed; the earlier draft's extra
requirement \(b+\tau_{\max}-\varepsilon>T_0-2\varepsilon\) is superfluous and is removed
here, since it is not implied by \(0<\varepsilon<g/4\) whenever \(T_0-(b+\tau_{\max})>g/4\),
and is not needed for the argument below.)

By the definition of \(b\) as the essential supremum of \(\operatorname{supp}f\), there is a
nonempty open interval \(I\subset(b-\varepsilon,b)\cap A\) on which \(f\) is not a.e. zero.
Put \(J:=I+\tau_{\max}\). Since \(I\subset(b-\varepsilon,b)\),
\[
\sup J<b+\tau_{\max}<T_0,
\]
using the contradiction hypothesis directly, so \(J\subset(-T_0,T_0)\) without any further
restriction on \(\varepsilon\). For every competing \(\lambda\in\Lambda_{T_0}\setminus\{\tau_{\max}\}\),
\[
J-\lambda=I+(\tau_{\max}-\lambda)\subset(b-\varepsilon+g,\,b+g)\subset(b,\infty),
\]
since \(\tau_{\max}-\lambda\ge g\) and \(\varepsilon<g/4<g\). Because \(b\) is the essential
supremum of \(\operatorname{supp}f\), \(f=0\) a.e. on \((b,\infty)\), which is a known-zero set
\(Z:=(b,\infty)\) in the sense of the full-line Lemma R36-A3 (no intersection with
\((-T_0,T_0)\) is needed, by the generalization above). Lemma R36-A3 then applies with
\(\lambda_*:=\tau_{\max}\), giving \(f=0\) a.e. on \(I\), a contradiction. Hence
\(b+\tau_{\max}\ge T_0\). The symmetric bound for \(a\) follows by the mirrored argument with
\(\lambda_*:=-\tau_{\max}\) and known-zero set \((-\infty,a)\).
\(\square\)

Status: \(\boxed{\text{R36-A4}\quad\checkmark[M].}\)

This is not yet a proof of \(\ker(H_{T_0}E_A)=\{0\}\); it is the first concrete **support
constraint** every hypothetical nonzero kernel vector must obey.

---

## 2b. Iterative peeling scheme (full-line typing)

Define a decreasing sequence of closed subsets \(A=K_0\supseteq K_1\supseteq\cdots\), and,
for each \(n\), the **full-line known-zero set**
\[
Z_n:=\mathbb R\setminus K_n.
\]
(Since any kernel vector's zero-extended representative \(f\) is supported in \(K_n\) once
stage \(n\) has been justified — see R36-A5 below — every point of \(\mathbb R\setminus K_n\)
is a known-zero point for \(f\), whether because it lies outside \((-T_0,T_0)\), outside
\(A\), or in a portion of \(A\) already cleared at an earlier stage.) Given \(K_n\), let
\[
K_{n+1}:=K_n\setminus\bigcup\Bigl\{I\subset K_n\text{ open}:\ \exists\,\lambda_*\in\Lambda_{T_0}\text{ with }J=I+\lambda_*\subset(-T_0,T_0)\text{ and }J-\lambda\subset Z_n\ \forall\lambda\ne\lambda_*\Bigr\}.
\]

### Proposition R36-A5 (peeling correctness)

For every \(n\), every \(0\ne y\in\ker(H_{T_0}E_A)\) with \(f=E_{T_0}E_Ay\) satisfies
\(f=0\) a.e. on \(Z_n\)-complement's complement, i.e. \(y=0\) a.e. on \(A\setminus K_n\).

### Proof

Induction on \(n\). The case \(n=0\) is vacuous. Assume \(f=0\) a.e. on
\(\mathbb R\setminus K_n=Z_n\) restricted to \(A\) (i.e. \(y=0\) a.e. on \(A\setminus K_n\));
combined with the automatic vanishing of \(f\) outside \((-T_0,T_0)\) and outside \(A\), this
means \(f=0\) a.e. on all of \(Z_n=\mathbb R\setminus K_n\), justifying the use of \(Z_n\) as
a known-zero set in Lemma R36-A3 at stage \(n\). For an interval \(I\) removed at stage
\(n+1\), every competing translate sends \(J=I+\lambda_*\) into \(Z_n\), so Lemma R36-A3
applies and gives \(y=0\) a.e. on \(I\). Hence \(y=0\) a.e. on
\(A\setminus K_{n+1}=(A\setminus K_n)\cup(\text{removed intervals})\), and
\(f=0\) a.e. on \(Z_{n+1}\) follows since \(Z_{n+1}=\mathbb R\setminus K_{n+1}\) differs from
\(Z_n\) only within \(A\).
\(\square\)

Status: \(\boxed{\text{R36-A5}\quad\checkmark[M].}\)

### Corollary R36-A6 (peeling sufficiency and residual support)

Let \(K_\infty:=\bigcap_nK_n\).

- If \(|K_\infty|=0\), then \(\ker(H_{T_0}E_A)=\{0\}\).
- Contrapositively, \(\ker(H_{T_0}E_A)\ne\{0\}\Rightarrow|K_\infty|>0\).
- \(K_\infty\ne\varnothing\) alone does **not** produce a nonzero kernel vector; it is only an
  **unexposed / multi-hit residual** on which no interval was ever isolated by a single
  active translate. Whether \(K_\infty\) actually carries a nonzero kernel vector requires a
  separate functional-equation analysis.

Status: \(\boxed{\text{R36-A6}\quad\checkmark[M]\text{ (sufficiency only; no equivalence claimed)}.}\)

---

## 2c. Parity split

Let \((Jf)(u):=f(-u)\). Since \(D_sJ=-JD_s\) and \(H_{T_0}\) is a finite linear combination
of such \(D_s\) with symmetric windowing,

### Proposition R36-A7 (parity split for the localized kernel)

\[
\boxed{H_{T_0}J=-JH_{T_0}.}
\tag{R36.9}
\]
Consequently \(y\in\ker(H_{T_0}E_A)\Rightarrow y_{\mathrm{ev}},y_{\mathrm{odd}}\in\ker(H_{T_0}E_A)\),
and the kernel is the orthogonal direct sum of its even and odd sectors.

Status: \(\boxed{\text{R36-A7}\quad\checkmark[M].}\)

### Corollary R36-A8 (only the odd kernel can matter for R36-B)

\(d_{R,S}\) is odd (since \(\phi_S=\operatorname{sgn}(u)I_0(|u|)\) is odd, \(j_{R,S}\) is odd
inherited from the R30/R31/R32 minus-sector chain, and \(C_{\Gamma,S}\) has even symbol,
preserving parity). Hence every even \(y\in\ker(H_{T_0}E_A)\) satisfies
\(\langle y,d_{R,S}\rangle=0\); only the odd kernel can matter for R36-B.

Status: \(\boxed{\text{R36-A8}\quad\checkmark[M].}\)

---

## 2d. Unitary reduction of the odd kernel to the half-annulus

Define, for \(h\in L^2(R,S)\),
\[
(U_-h)(x):=\frac{1}{\sqrt2}\operatorname{sgn}(x)\,h(|x|)\,\mathbf 1_{\{R<|x|<S\}}.
\]

### Proposition R36-A9 (unitary reduction of the odd annular kernel)

\(U_-:L^2(R,S)\to L^2_{\mathrm{odd}}(A)\) is unitary. Because \(H_{T_0}\) maps odd functions
to odd functions and even to even (R36-A7), the kernel equation for an odd \(y=U_-h\) is
equivalent to its restriction to \(u\in(0,T_0)\), and there takes the explicit form
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

### Proof sketch

Unitarity of \(U_-\) is a direct computation: \(\|U_-h\|^2_{L^2(A)}=\int_R^S|h(x)|^2\,dx\)
by the symmetric change of variables \(x\mapsto-x\) on \((-S,-R)\), and every odd
\(y\in L^2(A)\) is of this form with \(h(x)=\sqrt2\,y(x)\) on \((R,S)\). By R36-A7, for odd
\(y\), \((H_{T_0}E_Ay)(-u)=-(H_{T_0}E_Ay)(u)\), so \(H_{T_0}E_Ay=0\) on \((-T_0,T_0)\) iff it
vanishes on \((0,T_0)\) alone. Substituting \(f=E_Ay=E_AU_-h\) into (R36.3) for \(u\in(0,T_0)\)
and using \(f(u+\tau_{p,k})=\frac1{\sqrt2}\mathbf 1_{(R,S)}(u+\tau_{p,k})h(u+\tau_{p,k})\) (since
\(u+\tau_{p,k}>0\)) and
\(f(u-\tau_{p,k})=\frac1{\sqrt2}\operatorname{sgn}(u-\tau_{p,k})\mathbf1_{(R,S)}(|u-\tau_{p,k}|)h(|u-\tau_{p,k}|)\)
(since \(f\) is odd, \(f(u-\tau_{p,k})=\operatorname{sgn}(u-\tau_{p,k})f(|u-\tau_{p,k}|)\)) gives, after
canceling the overall factor \(1/\sqrt2\), exactly (R36.10). The identification (R36.11)
follows since \(U_-\) is a linear isomorphism onto \(L^2_{\mathrm{odd}}(A)\) intertwining the
two kernel equations term by term.

Status: \(\boxed{\text{R36-A9}\quad\checkmark[M]\text{, modulo a routine but not yet independently re-verified check of all extension/normalization factors in the substitution step above.}}\)

### R36-A10 (folded translation structure)

Equation (R36.10) is **not** a plain finite translation equation on \((R,S)\): the term
indexed by \(\tau_{p,k}\) hits \(h\) at the argument \(|u-\tau_{p,k}|\), which folds about
\(0\). For fixed \((p,k)\) and \(u\in(0,T_0)\), the relevant hit points on the
positive half-annulus \((R,S)\) arise from three affine isometries of \(x\)-space back to
\(u\)-space,
\[
\boxed{u=x+\tau_{p,k},\qquad u=x-\tau_{p,k},\qquad u=\tau_{p,k}-x,}
\]
corresponding respectively to the plain translate \(u+\tau_{p,k}=x\), and the two folded
cases \(u-\tau_{p,k}=x\) (when \(u>\tau_{p,k}\)) or \(\tau_{p,k}-u=x\) (when \(u<\tau_{p,k}\)),
both arising from \(|u-\tau_{p,k}|=x\). The correct description of the resulting peeling
problem on \((R,S)\) is therefore a **folded translation peeling on the positive
half-annulus**, governed by this finite family of affine isometries with explicit signs
(\(+1\) for the plain translate terms, and \(\operatorname{sgn}(u-\tau_{p,k})\) for the folded
terms), and not by the naive halved copy of the peeling scheme of §2b.

Status: \(\boxed{\text{R36-A10}\quad\checkmark[M]\text{ (structural identification of the folded isometry family; no peeling run performed yet)}.}\)

### Sharper gate for R36-B

By R36-A8/A9, the annihilator route for R36-B is entirely controlled by
\[
\boxed{
\ker(H_{T_0}E_A)\cap L^2_{\mathrm{odd}}(A)\ \simeq\ \ker L_{R,S,T_0}\ \stackrel?{=}\ \{0\}.
}
\tag{R36.12}
\]
Triviality of this smaller odd/folded kernel already kills the annihilator route for
R36-B, regardless of the size of any even kernel. Conversely, a single nonzero
\(h\in\ker L_{R,S,T_0}\) with \(\langle U_-h,d_{R,S}\rangle\ne0\) already suffices for the
R36-B obstruction. This is a strictly sharper target than the full R36-A gate (R36.4).

---

## 3. What the present repository does and does not prove

This correction (i) removes an unnecessary and possibly unsatisfiable extra condition on
\(\varepsilon\) from the R36-A4 proof, keeping only \(0<\varepsilon<g/4\); (ii) retypes the
exposed-cell lemma and the peeling scheme so that the known-zero set is a genuine subset of
\(\mathbb R\), with \(Z_n=\mathbb R\setminus K_n\), rather than being artificially confined to
\((-T_0,T_0)\) or to \(A\setminus K_n\); (iii) adds the unitary reduction R36-A9 of the odd
annular kernel to a half-annulus equation \(L_{R,S,T_0}h=0\), and identifies (R36-A10) the
folded translation structure of that equation. Nowhere is a nonzero \(y\) or \(h\)
constructed, and no peeling run on the folded half-annulus problem has been performed. Thus:

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

Unchanged in substance from the previous continuation, now phrased through R36-A9: if a
future argument produces \(0\ne h\in\ker L_{R,S,T_0}\), set \(y:=U_-h\), and Lemma R36-B
applies verbatim as before with the odd \(y\).

### Lemma R36-B (conditional annihilator test) — unchanged

Assume \(0\ne y\in\ker(H_{T_0}E_A)\) and \(\langle y,d_{R,S}\rangle\ne0\). Then
\(P_A\Sigma_{T_0}j_{R,S}\ne d_{R,S}\), by the same proof as before (Proposition O3AE.1
antisymmetry and \(H_{T_0}E_Ay=0\)).

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
| R36-A4 outer support constraint via \(\tau_{\max}\) (superfluous \(\varepsilon\)-condition removed) | ✓[M] |
| R36-A5 peeling-scheme correctness (full-line \(Z_n=\mathbb R\setminus K_n\) typing) | ✓[M] |
| R36-A6 peeling sufficiency and residual-support criterion | ✓[M] |
| R36-A7 parity split | ✓[M] |
| R36-A8 only odd kernel matters for R36-B | ✓[M] |
| R36-A9 unitary reduction of odd kernel to half-annulus equation \(L_{R,S,T_0}\) | ✓[M] (modulo routine re-check of normalization) |
| R36-A10 folded translation isometry structure on \((R,S)\) | ✓[M] structural |
| R36-A kernel triviality (full annulus) | ?[O] |
| Sharper gate \(\ker L_{R,S,T_0}=?\{0\}\) (odd/folded) | ?[O] |
| R36-B annihilator obstruction, conditional | ✓[M] conditional |
| R30-F | not obtained |

### What this correction adds

- Removes the superfluous and possibly unsatisfiable extra \(\varepsilon\)-condition from
  the R36-A4 proof; only \(0<\varepsilon<g/4\) is used, and \(\sup J<b+\tau_{\max}<T_0\)
  follows directly from \(I\subset(b-\varepsilon,b)\) and the contradiction hypothesis.
- Retypes R36-A3 and R36-A5 to use full-line known-zero sets
  \(Z_n=\mathbb R\setminus K_n\), making explicit that competing translates are inactive
  whenever they land outside \((-T_0,T_0)\), outside \(A\), or in an already-cleared part of
  \(A\) — without any new mathematical assumption, only cleaner typing.
- Adds R36-A9: a unitary identification of the odd annular kernel with the kernel of an
  explicit half-annulus operator \(L_{R,S,T_0}\) on \(L^2(R,S)\).
- Adds R36-A10: identifies the resulting problem as a **folded translation peeling on the
  positive half-annulus**, governed by the three affine isometries
  \(x\mapsto x+\tau,\,x\mapsto x-\tau,\,x\mapsto\tau-x\), which is structurally different
  from (and not simply a halved copy of) the peeling scheme of §2b.
- States the sharper gate (R36.12): triviality of \(\ker L_{R,S,T_0}\) alone already kills
  the annihilator route for R36-B, independent of any even kernel.

### What this audit explicitly does not deliver

- No proof that \(\ker(H_{T_0}E_A)\) or \(\ker L_{R,S,T_0}\) is trivial or nontrivial.
- No folded peeling run has been performed on \((R,S)\).
- No independent re-verification of every extension/normalization constant in the R36-A9
  substitution beyond the sketch given.
- No statement about R30-F, polar gauge, terminal transport, Object-X, or RH.

### Next mathematical target

Define and run a folded-translation peeling scheme on \((R,S)\) using the three isometries
of R36-A10, tracking a decreasing sequence of subsets of \((R,S)\) analogous to §2b but with
the known-zero test built from all three isometry types. Only if this leaves a
positive-measure unexposed residual should a separate functional-equation search for a
nonzero \(h\) begin. Only then would Lemma R36-B be invoked. No numerical choice of a
concrete \(T_0\) is made at this stage.
