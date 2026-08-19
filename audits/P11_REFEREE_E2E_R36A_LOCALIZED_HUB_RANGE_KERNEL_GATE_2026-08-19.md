# P11 End-to-End Referee R36-A — Localized hub range: density versus annihilator kernel

Date: 2026-08-19 (continued 2026-08-19: exposed-cell lemma, support bound, peeling scheme)

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
`main` at start of this continuation: `0d62bc711926267a65036c9230bd0923f9747d45` —
"Add R36-A audit: localized hub range density versus annihilator kernel gate…".

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
\(L^2(A)\). (Terminology note: this continuation replaces the earlier phrase "finite
linear system" by "finite translation equation/system" to avoid the misleading suggestion
of a finite-dimensional linear-algebra system.)

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

### Lemma R36-A3 (exposed-cell lemma)

Let \(I\subset A\) be a nonempty open interval and \(\lambda_*\in\Lambda_{T_0}\). Put
\(J:=I+\lambda_*\). Suppose
\[
J\subset(-T_0,T_0)
\qquad\text{and}\qquad
(J-\lambda)\cap A=\varnothing\ \ \text{for every }\lambda\in\Lambda_{T_0}\setminus\{\lambda_*\}.
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
For \(\lambda\ne\lambda_*\), \(u-\lambda\in J-\lambda\), and by hypothesis
\((J-\lambda)\cap A=\varnothing\); since \(f\) vanishes off \(A\), every such term
vanishes: \(f(u-\lambda)=0\). Hence the sum reduces to the single term
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

Suppose for contradiction \(b+\tau_{\max}<T_0\). Take \(\lambda_*=\tau_{\max}\) and a small
open interval \(I\subset(b,b+\delta)\cap A\) with \(\delta>0\) small enough that
\(J:=I+\tau_{\max}\subset(b+\tau_{\max}-\delta,\,b+\tau_{\max}+\delta)\subset(-T_0,T_0)\); this
is possible since \(b+\tau_{\max}<T_0\) strictly. By definition of \(b\) as the essential
supremum of the support, such \(I\) with \(f\) not a.e. zero on it exist for every
\(\delta>0\) (else \(b\) would be smaller). For every other \(\lambda\in\Lambda_{T_0}\setminus\{\tau_{\max}\}\),
\(\lambda<\tau_{\max}\) (as \(\tau_{\max}\) is the strict maximum of the \(\tau_{p,k}\), and
\(\Lambda_{T_0}\) also contains the negatives \(-\tau_{p,k}<0<\tau_{\max}\)), so
\(J-\lambda\subset(b+\tau_{\max}-\lambda-\delta,\,b+\tau_{\max}-\lambda+\delta)\) lies strictly
to the right of \(b\) once \(\delta\) is small enough (since \(\tau_{\max}-\lambda>0\)), hence
\((J-\lambda)\cap A\subset(b,S]\) can be made empty by shrinking \(\delta\) below
\(\tau_{\max}-\lambda\) for every one of the finitely many \(\lambda\ne\tau_{\max}\)
(finiteness of \(\mathcal P_{T_0}\) makes a single small enough \(\delta\) suffice for all of
them simultaneously), using also that \(f\) vanishes a.e. beyond \(b\) by definition of \(b\).
Hypothesis (R36.7) of Lemma R36-A3 then holds for this \(I,\lambda_*=\tau_{\max}\), giving
\(y=0\) a.e. on \(I\) — contradicting that \(I\) was chosen with \(f\) not a.e. zero on it.
Hence \(b+\tau_{\max}\ge T_0\). The symmetric statement for \(a\) follows by the same
argument using \(\lambda_*=-\tau_{\max}\) on an interval just left of \(a\).
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
K_{n+1}:=K_n\setminus\bigcup\{I\subset K_n\text{ open}: \exists\,\lambda_*\in\Lambda_{T_0}\text{ with }J=I+\lambda_*\subset(-T_0,T_0)\text{ and }(J-\lambda)\cap K_n=\varnothing\ \forall\lambda\ne\lambda_*\}.
\]
(At stage \(n+1\) the exposed-cell test of Lemma R36-A3 is re-run using the *shrunk* set
\(K_n\) in place of \(A\), since terms landing in \(A\setminus K_n\) are already known to
vanish from the previous stage and so no longer count as "active.")

### Proposition R36-A5 (peeling correctness)

For every \(n\), every \(0\ne y\in\ker(H_{T_0}E_A)\) satisfies
\(y=0\) a.e. on \(A\setminus K_n\).

### Proof

Induction on \(n\). The case \(n=0\) is vacuous (\(A\setminus K_0=\varnothing\)). Assume
\(y=0\) a.e. on \(A\setminus K_n\). For an interval \(I\) removed at stage \(n+1\), the
defining condition says every competing translate \(\lambda\ne\lambda_*\) sends \(J=I+\lambda_*\)
back into a point outside \(K_n\), i.e. into \(A\setminus K_n\) or outside \(A\) entirely; in
both cases \(f(u-\lambda)=0\) there, either because \(f\) vanishes off \(A\) or by the
inductive hypothesis. The exposed-cell argument of Lemma R36-A3 then applies verbatim with
\(K_n\) replacing \(A\), giving \(y=0\) a.e. on \(I\). Since \(A\setminus K_{n+1}=(A\setminus K_n)\cup(\text{removed intervals})\), the claim propagates to \(n+1\).
\(\square\)

Status: \(\boxed{\text{R36-A5}\quad\checkmark[M]\text{ (correctness of the peeling scheme, for every finite or infinite run length)}.}\)

### Corollary R36-A6 (dichotomy)

Let \(K_\infty:=\bigcap_nK_n\).

- If \(K_\infty=\varnothing\) (in particular if the process terminates at some finite
  \(K_N=\varnothing\)), then every \(y\in\ker(H_{T_0}E_A)\) vanishes a.e. on \(A\), i.e.
  \[
  \boxed{\ker(H_{T_0}E_A)=\{0\}.}
  \]
- If \(K_\infty\ne\varnothing\), this does **not** by itself produce a nonzero kernel vector.
  It shows only that any nonzero kernel vector must be supported (up to null sets) inside
  \(K_\infty\), and that on \(K_\infty\) every point lies in a **translation cycle**: no
  single exposed translate isolates it, i.e. the exposed-cell test (R36.7) fails at every
  point of \(K_\infty\) for every stage. Existence of an actual nonzero \(y\) supported on
  \(K_\infty\) then requires a separate functional-equation analysis of these cycles, not
  performed here.

### Proof

The first bullet is immediate from Proposition R36-A5 applied at the terminating or limiting
stage. The second bullet is a restatement of what removal at each stage requires: a point
survives into \(K_\infty\) exactly when it is never exposed, i.e. it always sits on a
translation orbit with at least two competing active translates at every stage — a
translation cycle in the stated sense. Proposition R36-A5 gives no information about
vanishing on \(K_\infty\) itself, since no interval inside \(K_\infty\) was ever removed.
\(\square\)

Status: \(\boxed{\text{R36-A6}\quad\checkmark[M]\text{ (dichotomy is rigorous; neither branch of the dichotomy is resolved for the concrete }\mathcal P_{T_0}\text{ here)}.}\)

### What remains open

Whether the concrete peeling process (run with the actual finite set
\(\Lambda_{T_0}=\{\pm\tau_{p,k}:(p,k)\in\mathcal P_{T_0}\}\) attached to a given \(T_0\), and a
given annulus \(A=A_{R,S}\)) terminates with \(K_N=\varnothing\), or instead stabilizes at a
nonempty \(K_\infty\), is not decided in this audit. This is now the precise combinatorial-
geometric question to which R36-A reduces.

---

## 3. What the present repository does and does not prove

The existing O3 chain proves antisymmetry of \(H_{T_0}\) and an exact off-support translation
formula. This continuation adds the exposed-cell lemma (R36-A3), the resulting outer support
constraint (R36-A4), and the correctness of an iterative peeling scheme (R36-A5/A6) that
reduces the kernel-triviality question to a finite geometric question about the concrete
shift set \(\Lambda_{T_0}\) and the annulus \(A\). Nowhere in R1–R36-A(continuation) is a
nonzero annular vector \(y\) constructed with \(H_{T_0}E_Ay=0\), nor is there a proof that the
peeling process empties \(A\) for every relevant \((R,S,T_0)\). No Paley–Wiener,
Fourier-symbol, or Volterra-triangular argument for the operator \(y\mapsto H_{T_0}E_Ay\) on
annulus-supported data is used or needed, precisely because such an argument would not respect
the finite-window restriction (see the Remark after Lemma R36-A3). Thus:

### Open Problem R36-A (first gate)

\[
\boxed{
\ker(H_{T_0}E_A)\stackrel?{=}\{0\}
\qquad\text{equivalently}\qquad
\overline{\operatorname{Ran}(P_AH_{T_0})}\stackrel?{=}L^2(A)
\qquad\text{equivalently}\qquad
K_\infty\stackrel?{=}\varnothing.
}
\tag{R36.4}
\]

Status: \(\boxed{\text{R36-A}\quad ?[O].}\)

This is the **only** status claimed for the ultimate kernel question in the present audit.

---

## 4. Conditional next step if the kernel is nontrivial

Suppose a future argument produces a nonzero
\[
0\ne y\in\ker(H_{T_0}E_A).
\]
By R36-A5/A6, any such \(y\) is necessarily supported (up to null sets) in the un-peelable
residue \(K_\infty\) and, by R36-A4, its support extends to within \(\tau_{\max}\) of the
window boundary. Then, and only then, one may ask whether \(y\) detects the concrete annular
target
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
(in particular if the peeling scheme of §2b is shown to empty \(A\), \(K_\infty=\varnothing\)),
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
| R36-A3 exposed-cell lemma | ✓[M] |
| R36-A4 outer support constraint via \(\tau_{\max}\) | ✓[M] |
| R36-A5/A6 peeling-scheme correctness and dichotomy (\(K_\infty=\varnothing\) vs. \(\ne\varnothing\)) | ✓[M] (correctness); which branch holds is ?[O] |
| R36-A kernel triviality / nontriviality for the concrete \(\Lambda_{T_0}\), \(A_{R,S}\) | ?[O] |
| R36-B annihilator obstruction from a nontrivial kernel vector with \(\langle y,d_{R,S}\rangle\ne0\) | ✓[M] conditional |
| Any conclusion on R30-F | not obtained |

### What this continuation adds

- Fixes the Target-section rendering slip: the operative equivalence is stated with the
  correctly closed range \(\overline{\operatorname{Ran}(P_AH_{T_0})}\); this was already
  correct in R36-A1 and the firewall, and is now also correct in the Target statement.
- Replaces "finite linear system" by "finite translation equation/system" to avoid
  suggesting a finite-dimensional linear-algebra system; the solution space \(L^2(A)\)
  remains infinite-dimensional.
- Proves the exposed-cell lemma R36-A3: a translate that lands in the source window with no
  competing translate landing in the annulus forces the annular vector to vanish on the
  corresponding sub-interval.
- Derives the first concrete support constraint R36-A4: any nonzero kernel vector's support
  must reach within \(\tau_{\max}\) of \(\pm T_0\).
- Sets up and proves correctness of an iterative peeling scheme (R36-A5/A6) reducing R36-A to
  a finite geometric dichotomy: either the peeling empties \(A\) (kernel trivial), or a
  residue \(K_\infty\ne\varnothing\) survives, consisting entirely of translation cycles, on
  which a nonzero kernel vector would have to be constructed by a separate argument.
- Explicitly rules out a premature global Fourier/exponential-polynomial uniqueness argument,
  since the hub equation is only imposed on the finite window \((-T_0,T_0)\), not on all of
  \(\mathbb R\).

### What this audit explicitly does not deliver

- No proof that the kernel is nontrivial.
- No proof that the kernel is trivial, i.e. no proof that the peeling scheme empties \(A\) for
  the concrete \(\Lambda_{T_0}\), \(A_{R,S}\).
- No analysis of the translation cycles that may survive on a nonempty \(K_\infty\).
- No proof that the concrete target \(d_{R,S}\) lies or does not lie in the actual localized
  hub range.
- No statement upgrading \(\operatorname{Ran}\Sigma_{T_0}\subseteq\operatorname{Ran}H_{T_0}\) to an
  equality.
- No statement about R30-F, polar gauge, terminal transport, Object-X, or RH.

### Next mathematical target

Run the peeling scheme of §2b explicitly for the concrete finite set
\(\Lambda_{T_0}=\{\pm\tau_{p,k}:(p,k)\in\mathcal P_{T_0}\}\) and a representative annulus
\(A_{R,S}\), tracking \(K_0\supseteq K_1\supseteq\cdots\) explicitly. Either exhibit a finite
stage \(N\) with \(K_N=\varnothing\) (proving \(\ker(H_{T_0}E_A)=\{0\}\)), or identify the
precise translation-cycle structure of a surviving \(K_\infty\) and analyze the resulting
cycle functional equations as a candidate route to a nonzero \(y\). Only once one of these two
outcomes is settled should the conditional Lemma R36-B be invoked.
