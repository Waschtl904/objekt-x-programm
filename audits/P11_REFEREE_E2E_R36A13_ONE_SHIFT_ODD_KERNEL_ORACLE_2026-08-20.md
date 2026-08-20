# P11 End-to-End Referee R36-A13 — Exact one-shift odd-kernel oracle

Date: 2026-08-20

## Purpose

This note gives an exact control theorem for the folded odd-sector kernel in the first P11
terminal chamber. It is intended as a mathematical oracle/regression theorem for any later
folded-peeling implementation.

It uses the repaired half-annulus operator from R36-A9/R36-A11':

\[
(L_{R,S,T_0}h)(u)
=\sum_{(p,k)\in\mathcal P_{T_0}}c_{p,k}
\Bigl[
\operatorname{sgn}(u-\tau_{p,k})\mathbf1_{(R,S)}(|u-\tau_{p,k}|)
 h(|u-\tau_{p,k}|)
-\mathbf1_{(R,S)}(u+\tau_{p,k})h(u+\tau_{p,k})
\Bigr].
\]

No statement about full R36-A kernel triviality, R30-F, Object X, polar gauge, terminal
transport, or RH is made.

---

## 1. One active shift

Assume exactly one shift \(\tau>0\) is active. Then, up to the nonzero scalar \(c_\tau\),

\[
(Lh)(u)
=
\operatorname{sgn}(u-\tau)\mathbf1_{(R,S)}(|u-\tau|)h(|u-\tau|)
-
\mathbf1_{(R,S)}(u+\tau)h(u+\tau),
\quad 0<u<T_0.
\tag{A13.1}
\]

The first P11 terminal chamber has

\[
\tau=\tau_{2,1}=\frac{\log2}{2},
\qquad
\frac{\log2}{2}\le T_0<\frac{\log3}{2}.
\]

Since

\[
\frac{\log3}{2}<\log2=2\tau,
\]

one has automatically

\[
T_0<2\tau.
\tag{A13.2}
\]

---

## 2. Exact middle-case classification

### Theorem R36-A13.1 (one-shift no-overlap kernel)

Assume

\[
0<R<\tau<S<T_0<2\tau.
\]

Put

\[
\boxed{
r:=\min\{S-\tau,\ \tau-R,\ 2\tau-T_0\}>0.
}
\tag{A13.3}
\]

Then

\[
\boxed{
\ker L_{R,S,T_0}
=
\left\{
 h\in L^2(R,S):
 \operatorname{ess\,supp}h\subset(\tau-r,\tau+r),\quad
 h(\tau+t)=-h(\tau-t)\text{ for a.e. }0<t<r
\right\}.
}
\tag{A13.4}
\]

Consequently

\[
\boxed{\dim\ker L_{R,S,T_0}=\infty.}
\tag{A13.5}
\]

### Proof

For \(0<u<\tau\), equation (A13.1) becomes

\[
0=-(\mathbf1_{(R,S)}(\tau-u)h(\tau-u)
+\mathbf1_{(R,S)}(\tau+u)h(\tau+u)).
\tag{A13.6}
\]

Both points \(\tau\pm u\) lie in \((R,S)\) exactly for

\[
0<u<m,
\qquad
m:=\min\{S-\tau,\tau-R\}.
\]

Hence

\[
h(\tau+u)=-h(\tau-u)
\quad\text{for a.e. }0<u<m.
\tag{A13.7}
\]

Where only one of the two points remains in \((R,S)\), the surviving value is forced to zero.
Thus any kernel vector is supported inside the symmetric interval
\((\tau-m,\tau+m)\).

For \(\tau<u<T_0\), one has \(u+\tau>2\tau>S\), so the second term in (A13.1) vanishes.
Also \(u-\tau>0\), and therefore

\[
0=\mathbf1_{(R,S)}(u-\tau)h(u-\tau).
\]

Thus

\[
h(x)=0\quad\text{for a.e. }R<x<T_0-\tau.
\tag{A13.8}
\]

Reflecting this zero region through the antisymmetry (A13.7) removes the symmetric region on
the right. The surviving radius around \(\tau\) is therefore

\[
\min\{m,\ 2\tau-T_0\}=r,
\]

which proves the necessary support and antisymmetry conditions in (A13.4).

Conversely, let \(h\) satisfy the right-hand side of (A13.4). On \(0<u<r\), the two folded
values cancel by antisymmetry. For \(r\le u<\tau\), any surviving argument lies outside the
support \((\tau-r,\tau+r)\). For \(\tau<u<T_0\), the possible argument \(u-\tau\) has distance
\(2\tau-u\ge2\tau-T_0\ge r\) from \(\tau\), hence again lies outside the essential support;
the \(u+\tau\) term is outside \((R,S)\). Therefore \(Lh=0\) a.e. on \((0,T_0)\).
This proves equality in (A13.4).

Finally, choose an arbitrary nonzero \(g\in L^2(0,r)\), define
\(h(\tau+t)=g(t)\), \(h(\tau-t)=-g(t)\), and set \(h=0\) elsewhere. This embeds
\(L^2(0,r)\) into the kernel, proving infinite dimension.
\(\square\)

Status:

\[
\boxed{\text{R36-A13.1}\quad\checkmark[M].}
\]

The correct firewall is **one-shift no-overlap**, not one-shift in general. Indeed
\(S<T_0<2\tau\) implies \(S-R<2\tau\), so the plain-plus image and the folded-minus image do
not overlap in the way that would create a translation relation \(h(x+2\tau)=h(x)\).

---

## 3. Two boundary regimes

### Proposition R36-A13.2 (shift at or left of the half-annulus)

Assume one active shift and

\[
\tau\le R<S<T_0.
\]

Then

\[
\boxed{\ker L_{R,S,T_0}=\{0\}.}
\tag{A13.9}
\]

### Proof

Fix \(x\in(R,S)\) and put \(u=x-\tau\in(0,T_0)\). The \(u+\tau\) term in (A13.1) equals
\(-h(x)\). If \(x-2\tau\notin(R,S)\), the other term is zero and hence \(h(x)=0\). If
\(x-2\tau\in(R,S)\), then \(x>2\tau\) and the other term is \(+h(x-2\tau)\), so

\[
h(x)=h(x-2\tau).
\]

Iterating subtracts \(2\tau>0\) and after finitely many steps exits below \(R\), where the
zero extension gives zero. Hence \(h(x)=0\) a.e.
\(\square\)

Status: \(\boxed{\text{R36-A13.2}\quad\checkmark[M].}\)

### Proposition R36-A13.3 (shift at or right of the half-annulus)

Assume one active shift and

\[
R<S\le\tau\le T_0.
\]

Then

\[
\boxed{\ker L_{R,S,T_0}=\{0\}.}
\tag{A13.10}
\]

### Proof

For \(x\in(R,S)\), put \(u=\tau-x\in[0,T_0)\) (the endpoint \(u=0\) is irrelevant a.e.).
Then \(|u-\tau|=x\) and \(\operatorname{sgn}(u-\tau)=-1\). Moreover
\(u+\tau=2\tau-x>S\), so the plus term is absent. Equation (A13.1) gives

\[
-h(x)=0.
\]

Thus \(h=0\) a.e.
\(\square\)

Status: \(\boxed{\text{R36-A13.3}\quad\checkmark[M].}\)

---

## 4. Exact first-chamber iff theorem

Combining the three cases gives, throughout the first P11 terminal chamber

\[
\frac{\log2}{2}\le T_0<\frac{\log3}{2},
\qquad 0<R<S<T_0,
\]

the exact equivalence

\[
\boxed{
\ker L_{R,S,T_0}\ne\{0\}
\quad\Longleftrightarrow\quad
R<\frac{\log2}{2}<S.
}
\tag{A13.11}
\]

**In words:** in the first terminal chamber the odd localized kernel is nontrivial exactly
when the unique active shift \(\tau_{2,1}=\log2/2\) lies strictly inside the positive
half-annulus \((R,S)\). In that case the kernel is infinite-dimensional and is given exactly
by (A13.4). If the shift lies at or outside either endpoint, the odd kernel is trivial.

Status:

\[
\boxed{\text{first-chamber odd-kernel classification}\quad\checkmark[M].}
\]

Via R36-A9,

\[
U_-(\ker L_{R,S,T_0})
=
\ker(H_{T_0}E_A)\cap L^2_{\rm odd}(A),
\]

so (A13.11) is also the exact classification of the **odd** localized annihilator kernel in
this chamber. It says nothing about the even kernel.

---

## 5. Regression firewall for folded peeling

In the nontrivial middle case define

\[
C_{T_0}:=(\tau-r,\tau+r).
\]

Every nonzero kernel vector is supported in \(C_{T_0}\), and arbitrary antisymmetric
\(L^2\)-data on the right half of \(C_{T_0}\) generate kernel vectors. Therefore any correct
sufficiency-only folded peeling must satisfy

\[
\boxed{
C_{T_0}\subseteq K_\infty^-
\quad\text{modulo null sets}.
}
\tag{A13.12}
\]

In particular,

\[
\boxed{|K_\infty^-|\ge2r>0.}
\tag{A13.13}
\]

A computed result \(|K_\infty^-|=0\) in this parameter regime is therefore a definite error
in the peeling theorem or implementation. Equality \(K_\infty^-=C_{T_0}\) is **not** required:
the peeling criterion is sufficient only and may fail to detect all forced-zero regions.

Status:

\[
\boxed{\text{A13 regression firewall}\quad\checkmark[M].}
\]

---

## 6. Strategic meaning and firewalls

- A nontrivial odd kernel is an opportunity for the conditional annihilator route; it is not a
  failure by itself. One still needs a vector pairing nontrivially with \(d_{R,S}\).
- Odd-kernel triviality in the two boundary regimes kills only that odd annihilator route. It
  does **not** imply full dense range, because the even kernel may remain.
- The theorem is intentionally restricted to the first terminal chamber/no-overlap regime.
  It does not assert that a single shift can never have a nontrivial or trivial kernel in wider
  annuli with \(S-R>2\tau\), where a translation relation \(h(x+2\tau)=h(x)\) can arise.
- No conclusion about R30-F follows from A13 alone.

Current statuses:

| Item | Status |
|---|---|
| R36-A13.1 exact middle-case kernel | ✓[M] |
| R36-A13.2 \(\tau\le R\) odd kernel trivial | ✓[M] |
| R36-A13.3 \(\tau\ge S\) odd kernel trivial | ✓[M] |
| first P11 terminal chamber iff classification | ✓[M] |
| A13 regression firewall | ✓[M] |
| even localized kernel | ?[O] |
| full R36-A kernel triviality | ?[O] |
| R36-B pairing/nonorthogonality in middle case | ?[O] at this node |
| R30-F | ?[O] |

## 7. Next target

Before implementing a general folded peeling or passing to multi-shift chambers, test the
R36-B pairing on the exact kernel family (A13.4). Separately, develop terminal chambers only
after the A11' preimage repair is treated as the canonical folded-peeling lemma.
