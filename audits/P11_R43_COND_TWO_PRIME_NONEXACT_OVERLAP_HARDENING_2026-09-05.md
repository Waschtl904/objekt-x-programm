# P11 / R43 — two-prime non-exact overlap hardening

**Date:** 2026-09-05  
**Scope:** repair/hardening of TP15–TP18 in `audits/P11_R43_COND_TWO_PRIME_POINTWISE_LOCAL_NOGO_2026-09-05.md`  
**Status:** local exact proof repair; the two-prime pointwise-local no-go and its step-floor conclusion are unchanged. `B-METINC-COND`, partition-selective PSD, epsilon-relaxed control, structured-vector COND, Strong Terminal/C6 remain OPEN.

## 0. Why this companion is needed

The two-prime audit correctly identifies the exact displacement equations

\[
|k-l|a_r=a_p
\quad\text{or}\quad
(k+l)a_r=a_p,
\qquad a_r=\tfrac12\log r,
\]

but the wording in TP15 can be read too quickly: for source intervals of positive length `ell`, geometric overlap initially requires a displacement mismatch of size **less than `ell`**, not literal equality.

The older `p=2` kernel audit explicitly inserted the missing finite-mismatch step:

> at fixed terminal `V` only finitely many translated intervals are active, so shrink `ell` until every non-exact mismatch is disjoint.

This companion reinstates that firewall for the `p=2,3` theorem. It is a proof-hygiene repair, not a change to the theorem or its quantifiers.

---

## 1. Finite active displacement set

Fix

\[
p\in\{2,3\},\qquad U>0,\qquad 0<h<h_p(U),\qquad V=U+h.
\]

Choose `I_Q subset (U,V)` centered as in the two-prime audit and put

\[
I_P=I_Q-a_p.
\]

At fixed finite terminal `V`, the frozen residual operator has only finitely many active prime-power channels. Indeed a nonzero residual summand must satisfy the finite-window support and martingale-cutoff restrictions, hence only finitely many pairs `(r,k)` occur. Consequently only finitely many pairs of translated copies of `I_P` and `I_Q` can meet the terminal window.

For each active prime `r`, active indices `k,l`, and translation signs

\[
\sigma,\tau\in\{+1,-1\},
\]

define the center displacement mismatch

\[
\Delta_{r,k,l}^{\sigma,\tau}
:=\sigma k a_r-\tau l a_r-a_p.
\tag{H1}
\]

Let `D_{U,h,p}` be the finite set of all such mismatches arising from active pairs that can contribute to the cross inner product `\langle Mf,Sg\rangle`.

Remove the exact zero mismatches and define

\[
\mu_{U,h,p}
:=
\min\{ |\Delta|:\Delta\in D_{U,h,p},\ \Delta\ne0\}.
\tag{H2}
\]

If there is no nonzero mismatch, set `mu_{U,h,p}=+infinity`. Since the active set is finite,

\[
\boxed{\mu_{U,h,p}>0.}
\tag{H3}
\]

---

## 2. Additional interval-length choice

After `U`, `h`, and the active finite set are fixed, choose the witness interval length with the additional constraint

\[
0<\ell<\frac14\mu_{U,h,p},
\tag{H4}
\]

in addition to all support/resonance constraints already imposed in TP12.

Two intervals of equal length `ell` whose centers differ by at least `mu_{U,h,p}` are then disjoint. Therefore every non-exact active displacement mismatch gives zero contribution.

Hence:

\[
\boxed{
\text{an active translated }I_P\text{-copy and }I_Q\text{-copy can overlap only if }
\Delta_{r,k,l}^{\sigma,\tau}=0.
}
\tag{H5}
\]

This is the precise justification for passing from geometric overlap to the exact equations in TP15.

The extra condition (H4) is harmless for all theorem quantifiers: the witness interval length is free to depend on the already chosen pair `(U,h)`, and no positive lower bound on `ell` is used anywhere in the kernel or step-floor argument.

---

## 3. Classification of the exact zero mismatches

Equation (H1) with `Delta=0` reads

\[
\sigma k a_r-\tau l a_r=a_p.
\tag{H6}
\]

There are three relevant sign patterns.

### 3.1 Same translation signs

If `sigma=tau=+1`, then

\[
(k-l)a_r=a_p.
\]

If `sigma=tau=-1`, then

\[
(l-k)a_r=a_p.
\]

Thus in both cases

\[
|k-l|a_r=a_p.
\tag{H7}
\]

Exponentiating gives

\[
r^{|k-l|}=p.
\]

Since `p` is prime,

\[
\boxed{r=p,\qquad |k-l|=1.}
\tag{H8}
\]

The product of the two translation signs is positive in both same-sign cases.

### 3.2 Opposite signs with positive sum

If `sigma=+1`, `tau=-1`, then

\[
(k+l)a_r=a_p.
\tag{H9}
\]

But for `p in {2,3}`,

\[
a_p<2a_2\le(k+l)a_r,
\]

because `k+l>=2` and every prime `r>=2`. Therefore (H9) is impossible.

### 3.3 Opposite signs with negative sum

If `sigma=-1`, `tau=+1`, then the left side of (H6) equals

\[
-(k+l)a_r<0,
\]

and cannot equal `a_p>0`.

Therefore the only exact surviving overlaps are precisely

\[
\boxed{r=p,\quad |k-l|=1,\quad \sigma=\tau.}
\tag{H10}
\]

---

## 4. Noncancellation and strict positivity

For every surviving overlap (H10), the translation-sign product is positive. The frozen projected-mark Gram formula is

\[
\langle q_{p,k}^{(J)},q_{p,l}^{(J)}\rangle
=p^{-(k+l)/2}\bigl(p^{\min(J,k,l)}-1\bigr)\ge0.
\tag{H11}
\]

The first adjacent overlap `(l,k)=(1,2)` on the interval `I_Q-2a_p` has terminal depth `J=2` and contributes exactly

\[
\ell(\log p)(p-1)p^{-9/4}>0.
\tag{H12}
\]

Thus all surviving terms are nonnegative and at least one is strictly positive:

\[
\boxed{\langle Mf,Sg\rangle>0.}
\tag{H13}
\]

Consequently

\[
\boxed{S^*Mf\ne0.}
\tag{H14}
\]

Together with the already proved full-operator kernel statement `Cf=0`, this gives

\[
\boxed{
\langle f,K_{U,U+h}^{\rm Schur}f\rangle
=-\|(I+S^*S)^{-1/2}S^*Mf\|^2<0.
}
\tag{H15}
\]

---

## 5. Effect on TP23 and TP26

The repair only adds the post-`h` interval-length restriction (H4). Therefore it does not change the available terminal-step radius `h_p(U)` and does not change the two-prime exceptional-set argument.

In particular the theorem remains

\[
\boxed{
\exists U_0>0\ \forall U\ge U_0\ \exists h_0(U)>0\ \forall h\in(0,h_0(U)):
K_{U,U+h}^{\rm Schur}\not\succeq0.
}
\]

and the nonoptimal universal radius floor remains

\[
\boxed{h_0(U)\ge c_*e^{-4U}}
\]

for all sufficiently large `U`.

No conclusion about `PARTITION-SELECTIVE-PSD`, the epsilon-relaxed route, the structured vector, `B-METINC-COND`, or Strong Terminal is changed.

---

## 6. Booking

Book the repair as

```text
R43-COND-TWO-PRIME-NONEXACT-OVERLAP-HARDENING ✓[M]
```

and read TP15–TP18 of the primary two-prime audit together with this companion.

This hardening restores the explicit finite-mismatch firewall already present in the older `p=2` proof and removes the most obvious adversarial objection before external re-review.