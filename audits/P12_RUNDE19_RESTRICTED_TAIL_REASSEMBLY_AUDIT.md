# P12 Runde 19 — Final \(\rho\)-reassembly audit

**Status:** Region-B restricted-tail closure `✓[M]_part` after independent raw-operator GREEN; global \(\rho\)-descent remains `?[O]`.  
**Independent review:** Perplexity independently reconstructed B1–B4 from the raw operator, reproduced the four-way partition and 200000-point structural stress, and returned GREEN for Region B while explicitly keeping Region D open.  
**Repo basis:** `Waschtl904/objekt-x-programm`, `main` at Round 18 commit
`d4484bf9d563d8a0922685d0dd94b913f5a7fd04`.  
**Firewall:** P11 FROZEN. R14 untouched. No Polar Gauge, terminal transport,
Object X, or RH implication.

---

## 0. Purpose

Round 18 received independent GREEN and is committed as `✓[M]_part`.
The question is whether the already committed pieces now reassemble to

\[
\boxed{
\rho\le R<T,\qquad T<S<T_0<c
\Longrightarrow
\ker L_{R,S,T_0}^{\{a,b,2a\}}=\{0\}.
}
\]

Write

\[
\sigma:=S-T,\qquad
\varepsilon:=T_0-T,
\qquad
0<\sigma<\varepsilon<\varepsilon_{\max}.
\]

The answer of this audit is:

\[
\boxed{\text{NO global promotion yet.}}
\]

The parameter space splits into four disjoint regions. Three are closed or
reduce to a small review-candidate lemma. One positive-area low-radius
large-tail wedge remains genuinely open.

---

## 1. Exact parameter partition

For the target range \(\rho\le R<T\), split as follows.

### A. High radius
\[
R\ge e/2.
\]

Round 14 proves the full mixed strip for every
\(0<\sigma<\varepsilon<\varepsilon_{\max}\).

**Status:** `✓[M]`.

### B. Low radius, restricted tail
\[
\rho\le R<e/2,\qquad 0<\sigma\le R.
\]

This case is **not** covered by the stated b2b theorem, because b2b assumes
\(R\ge e/2\).  However it admits a short direct reduction to b1; see §2.

**Status:** `✓[M]_part` after independent raw-operator GREEN.

### C. Low-radius overlap below \(e/2\)
\[
\rho\le R<\sigma<e/2.
\]

Round 18 gives
\[
h=0\quad\text{a.e. on }(0,\sigma).
\]
Round 17 then kills the full tail
\[
H(t)=h(T+t)=0,\qquad 0<t<\sigma.
\]
Thus the actual support collapses to \((\sigma,T)\).  The endpoint theorem b1
applies with effective lower radius \(R_{\rm eff}=\sigma>0\).

**Status:** `✓[M]_part` chain, subject only to the final bookkeeping review.

### D. Low radius, large tail
\[
\boxed{
\rho\le R<e/2\le\sigma<\varepsilon<\varepsilon_{\max}.
}
\]

No committed theorem closes this region.

- Round 14 requires \(R\ge e/2\).
- b2b requires \(R\ge e/2\).
- Rounds 15H–18 assume \(\sigma<e/2\).
- b1 applies only after the tail has been killed.
- Merely “rebasing to \(R_{\rm eff}=e/2\)” is invalid unless one first proves
  \(h=0\) on \((R,e/2)\).

This region has positive parameter volume; it is not a boundary or
measure-zero issue.

**Status:** `?[O]` — genuine remaining mathematics.

Therefore the full \(\rho\)-descent cannot yet be promoted.

---

# 2. New restricted-tail closure (Region B)

Assume

\[
\rho\le R<e/2,\qquad
0<\sigma\le R,\qquad
\sigma<\varepsilon<\varepsilon_{\max},
\]
and let \(h\in\ker L_{R,T+\sigma,T_0}^{\{a,b,2a\}}\).

We show that Region B reduces to b1 without using the b2b theorem.

## 2.1 Lower-half equation is exactly the endpoint equation

For \(x\in(R,a)\), the only mixed-tail branch that can contaminate the
endpoint E-equation is \(h(T+x)\).

But
\[
x>R\ge\sigma
\quad\Longrightarrow\quad
T+x\ge T+\sigma=S,
\]
so that branch is support-zero a.e.

Hence the canonical E-equation on \((R,a)\) is exactly the same
homogeneous equation used in b1/A14.3a:

\[
p h(x)+r\,\operatorname{sgn}(x-d)h(|x-d|)
-qh(a-x)=0.
\]

The repaired A14.3a lower-circle unique-continuation argument therefore applies
verbatim and yields

\[
\boxed{h=0\quad\text{a.e. on }(R,a).}
\tag{B1}
\]

No assumption \(R\ge e/2\) is used here.

## 2.2 Horizon source creates the same null strip as b1

For \(0<t<\varepsilon\), the horizon-legal source \(u=T+t\) has the exact
raw equation

\[
p\,h(a+t)+r\,h(e+t)+q\,h(t)=0.
\tag{B2}
\]

Both lower values vanish:

- \(h(t)=0\) either by support (\(t\le R\)) or by (B1) (\(R<t<a\));
- \(e+t<a\) because \(\varepsilon<e\), so \(h(e+t)=0\) either by support
  or by (B1).

Therefore

\[
\boxed{
h(a+t)=0\quad\text{for a.e. }0<t<\varepsilon.
}
\tag{B3}
\]

Define
\[
l(z):=h(T-z).
\]
Then (B3) is the right-sided null strip

\[
l(z)=0
\quad\text{for }a-\varepsilon<z<a.
\tag{B4}
\]

## 2.3 High reflection is uncontaminated on exactly that strip

In the mixed problem, the old high-reflection source can in principle acquire
tail terms.  On the strip used in (B4), however,

\[
z>a-\varepsilon>d>e/2>R\ge\sigma.
\]

Thus every tail value with offset \(z\) is above \(S=T+\sigma\).
The other possible forward \(b\)-branch has tail offset \(z-e\), and

\[
z-e>d-\varepsilon
>d-\varepsilon_{\max}
>e/2
>R\ge\sigma.
\]

Hence the old high reflection is genuinely unchanged there:

\[
q\,l(z)+p\,l(a-z)=0,
\qquad
a-\varepsilon<z<a.
\tag{B5}
\]

Using \(l(z)=0\) from (B4), put \(w=a-z\).  Then

\[
\boxed{
l(w)=0\quad\text{for a.e. }0<w<\varepsilon.
}
\tag{B6}
\]

This step uses only the seed strip; no claim is made that the whole mixed
upper-circle cocycle is tail-free.

## 2.4 P1 kills the entire tail

The committed paired-source identity P1 is unconditional for
\(0<t<\varepsilon\):

\[
H(t)+l(t)+\frac{2r}{p}H(d-t)=0,
\qquad H(t):=h(T+t).
\tag{P1}
\]

For \(0<t<\sigma\), (B6) gives \(l(t)=0\).

Also
\[
d-t>d-\sigma\ge d-R>d-e/2>e/2>\sigma,
\]
so \(H(d-t)=0\) by tail support.

Therefore P1 gives

\[
\boxed{H(t)=0\quad\text{for a.e. }0<t<\sigma.}
\tag{B7}
\]

Thus the whole mixed tail \((T,T+\sigma)\) vanishes.

## 2.5 Reduction to b1

After (B7), \(h\) is actually supported in \((R,T)\) and satisfies the same
kernel equation with the same source horizon \(T_0\).  The endpoint theorem
b1 applies directly:

\[
\boxed{h=0.}
\]

Hence the proposed new Region-B theorem is

\[
\boxed{
\rho\le R<e/2,\quad 0<\sigma\le R,\quad
\sigma<\varepsilon<\varepsilon_{\max}
\Longrightarrow
\ker L_{R,T+\sigma,T_0}^{\{a,b,2a\}}=\{0\}.
}
\]

**Status:** `✓[M]_part` after independent raw-operator GREEN.

---

# 3. Region C reassembly check

Assume

\[
\rho\le R<\sigma<e/2,\qquad
\sigma<\varepsilon<\varepsilon_{\max}.
\]

Round 18 gives

\[
h=0\quad\text{a.e. on }(0,\sigma).
\]

This is exactly the premise of the independently GREEN Round-17 full-tail
lemma.  Therefore

\[
H(t)=0\quad\text{a.e. for }0<t<\sigma.
\]

Since \(l(t)=h(T-t)\) is also killed by the Round-17 conclusion, no mixed tail
remains.  The support is contained in \((\sigma,T)\).

Because \(\sigma>0\), b1 applies with lower radius \(\sigma\).  Hence

\[
\boxed{h=0.}
\]

No b2b invocation is needed.

---

# 4. Why Region D is not a bookkeeping gap

Assume

\[
\rho\le R<e/2\le\sigma<\varepsilon<\varepsilon_{\max}.
\]

The previous reassembly sketch suggested “rebase to \(e/2\) and use Round 14”.
This is not licensed.

To invoke Round 14 with effective lower radius \(e/2\), one must first establish

\[
h=0\quad\text{a.e. on }(R,e/2).
\tag{D1}
\]

Neither Round 18 nor Round 17 provides (D1):

- Round 18 explicitly works in \(\sigma<e/2\), and its support-visibility
  reductions use that upper-support inequality.
- Round 17 is conditional on a post-defect null interval and also works below
  the \(e/2\) tail seam.
- For \(\sigma\ge e/2\), additional upper/tail slots become live in the
  Round-18 raw rows.

So Region D needs a new local interface theorem or a different back-transfer
argument.  It cannot be promoted by citation/reassembly alone.

A useful internal split is

\[
e/2\le\sigma\le d/2
\quad\text{versus}\quad
d/2<\sigma<\varepsilon_{\max},
\]
because committed P1 changes from the one-tail relation
\(H(x)=-l(x)\) to the two-tail Case-B system across \(\sigma=d/2\).

That is the next mathematical front.

---

# 5. Corrected global status

After independent GREEN of the new Region-B lemma:

\[
\boxed{
\begin{array}{ll}
R\ge e/2: & \checkmark[M] \quad\text{(Round 14)},\\[1mm]
\rho\le R<e/2,\ \sigma\le R:
    & \checkmark[M]_{\rm part}\quad\text{(Round 19)},\\[1mm]
\rho\le R<\sigma<e/2:
    & \checkmark[M]_{\rm part}\quad\text{(Rounds 18+17+b1)},\\[1mm]
\rho\le R<e/2\le\sigma:
    & ?[O]\quad\text{(genuine remaining wedge).}
\end{array}
}
\]

Despite Region-B GREEN, the full \(\rho\)-descent remains

\[
\boxed{?[O]}
\]

until Region D is solved and the final four-way union is independently audited.

---

# 6. Correction to the earlier Round-17 §8.2 sketch

The earlier reassembly sketch said, informally, that in the restricted-tail
case all terms of a P2 defect form vanish after the lower kill.

That assertion is unnecessary and should not be used.

The clean proof is instead:

\[
\text{lower E kill}
\to
h(a+t)=0
\to
l(t)=0
\to
\text{P1}
\to
H(t)=0
\to
\text{b1}.
\]

This avoids any unsupported global claim about P2/D-terms.

---

# 7. Independent review record

The independent reviewer reconstructed the Region-B argument from the canonical raw
operator rather than accepting the reduced equations.  In particular the review
confirmed:

1. For \(\sigma\le R\), the E-source on \(x\in(R,a)\) has no live tail branch.
2. The repaired A14.3a lower-circle kill applies unchanged.
3. At \(u=T+t\), \(0<t<\varepsilon\), the raw row reduces exactly to
   \[
   p h(a+t)+r h(e+t)+q h(t)=0.
   \]
4. The horizon null strip \(h(a+t)=0\), \(0<t<\varepsilon\), follows.
5. On \(a-\varepsilon<z<a\), every mixed-tail contaminant in the high-reflection
   source is support-dead, including the branch with offset \(z-e\).
6. The back-transport gives \(l(w)=0\), \(0<w<\varepsilon\).
7. The committed P1 identity is valid on the required range.
8. For \(0<t<\sigma\), \(d-t>\sigma\), hence P1 kills \(H(t)\).
9. Reduction to b1 is legitimate with the same \(T_0\).
10. The four-way partition is exhaustive, Region D has positive volume, and no
    committed theorem currently closes it.

The reviewer independently reproduced:

- `FOUR_WAY_PARTITION = PASS` with counts A=387963, B=10608, C=584, D=845;
- `RESTRICTED_TAIL_STRUCTURAL_STRESS = PASS 200000`;
- the explicit Region-D interior witness
  \(R\approx0.0623004\), \(\sigma\approx0.0917461\),
  \(\varepsilon\approx0.1016590\).

**Review verdict recorded:** Region B GREEN / `✓[M]_part`; full
\(\rho\)-descent remains `?[O]` because of D.

This audit does not promote the global theorem.
