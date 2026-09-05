# P11 / R43 — round-2 review reconciliation and step-floor dynamics

**Date:** 2026-09-05  
**Reviewed head:** `ca155fbf1aa0489ba7d2d97514c3fd4aba9308da`  
**Scope:** reconcile the second destructive cross-model review of the two-prime COND no-go; harden TP20/H4 quantifiers; derive exact consequences of the `c_*e^{-4U}` step floor.  
**Status:** theorem-level local hardening and new floor-dynamics consequences. `PARTITION-SELECTIVE-PSD`, the epsilon-relaxed route, structured-vector COND, `B-METINC-COND`, B-FLAGTIGHT and Strong Terminal/C6 remain OPEN.

---

## 0. External-review outcome and one correction to the proposed promotion

The second cross-model review found no defect in TP22, TP23, TP24, TP25 or TP26 and accepted the non-exact-overlap sieve. It requested four hardenings:

1. TP20 should carry the already used sufficiently-late geometry hypothesis;
2. the maximizing `rho` prime in Section 8 should be shown explicitly to be available;
3. the finite active channel set in H4 should be bounded by a concrete prime-power envelope independent of `ell`;
4. the step floor should be converted into a precise partition-dynamics statement and an epsilon-route summability constraint.

Items 1--3 are correct and are supplied below.

For item 4, one proposed formulation from the review was

```text
delta_j = o(1/j) is necessary for the epsilon route.
```

That statement is **not valid without an additional regularity hypothesis**. A summable nonnegative sequence need not be `o(1/j)` (sparse spikes give a counterexample), and `o(1/j)` is not sufficient for summability (`1/(j log j)` is the standard counterexample). The correct unconditional consequence is the harmonic firewall proved in Section 6.

No previous theorem booking is weakened.

---

## 1. TP20 geometry threshold made explicit

Recall

\[
a_p=\frac12\log p,
\qquad p\in\{2,3\},
\]

and the witness intervals

\[
I_Q\subset(U,U+h),
\qquad I_P=I_Q-a_p,
\]

with `I_Q` centered at `U+epsilon`, `epsilon=h/2`, and `ell<h/4`.

The strict positive adjacent overlap used in TP17 is supported on

\[
I_Q-2a_p.
\]

Set the uniform geometry threshold

\[
\boxed{U_{\rm geom}:=2a_3=\log 3.}
\tag{R2.1}
\]

If `U>U_geom`, then for both witness primes `p=2,3` the whole interval `I_Q-2a_p` lies on the positive side of the old window. Indeed its left endpoint is bounded below by

\[
U+\epsilon-2a_p-\frac\ell2
>
U-2a_p>0,
\]

because `epsilon>ell/2` and `U>2a_3>=2a_p`. Its right endpoint is below `U` because

\[
\epsilon+\frac\ell2<\frac58h<2a_p.
\]

On this interval,

\[
a_p<U-u<2a_p,
\]

and

\[
2a_p<V-u<3a_p,
\]

using `epsilon=h/2`, `ell<h/4` and the TP11 bound `h<a_2/8<=a_p/8`. Therefore exactly

\[
J_{p,U}=1,
\qquad
J_{p,V}=2.
\tag{R2.2}
\]

Hence the correctly scoped primewise statement is:

\[
\boxed{
U>U_{\rm geom},\quad U\notin E_p
\Longrightarrow
\forall h\in(0,h_p(U)):\ K_{U,U+h}^{\rm Schur}\not\succeq0,
}
\tag{R2.3}
\]

where

\[
h_p(U)=
\min\left\{
\frac{a_2}{8},
\frac{\delta_p}{16},
\frac{\rho_{p,U}}{64}
\right\}.
\tag{R2.4}
\]

This **scope-corrects TP20 as a standalone lemma**. TP23 and TP26 were already stated only after choosing `U_0>2a_3`, so their truth and their bookings are unchanged.

Book:

```text
R43-COND-TP20-GEOMETRY-SCOPE-HARDENING ✓[M]
```

---

## 2. Finite active-channel envelope independent of `ell`

The H4 companion used finiteness of the active translated channel set. We now give a concrete envelope that is fixed before `ell` is chosen.

In the frozen translation convention, a residual term in prime sector `r` and index `k` can meet a source packet only through

\[
u\pm k a_r\in I,
\qquad a_r=\frac12\log r,
\]

with both the residual row `u` and the packet `I` inside the terminal window `(-V,V)`.

Therefore any contributing channel satisfies

\[
k a_r<2V.
\]

Equivalently,

\[
\boxed{r^k<e^{4V}.}
\tag{R2.5}
\]

There are only finitely many prime powers below the fixed number `e^{4V}`. Thus the cross inner product may be enveloped, before choosing `ell`, by the finite set

\[
\mathcal A_V
:=
\{(r,k,l,\sigma,\tau):
 r\ {m prime},\ k,l\ge1,\ r^k<e^{4V},\ r^l<e^{4V},\ \sigma,\tau\in\{\pm1\}\}.
\tag{R2.6}
\]

Define all displacement mismatches on this finite **ell-independent** superset and take the smallest nonzero absolute mismatch. Shrinking `ell` below one quarter of that number excludes every non-exact overlap. Since the superset is fixed by `(U,h)` through `V=U+h`, there is no circular dependence of the active set on `ell`.

This strengthens H1--H4 and makes the dependency order explicit:

```text
U -> h -> V -> finite envelope A_V -> mismatch gap mu -> ell.
```

Book:

```text
R43-COND-H4-ACTIVE-ENVELOPE-NONCIRCULARITY ✓[M]
```

---

## 3. The maximizing-rho witness prime is automatically available

By definition

\[
E_p=\{U:2U-a_p\in\Lambda\},
\qquad
\rho_{p,U}=\operatorname{dist}(2U-a_p,\Lambda).
\]

Hence exactly

\[
\boxed{U\in E_p\iff\rho_{p,U}=0.}
\tag{R2.7}
\]

Since TP22 gives

\[
E_2\cap E_3=\varnothing,
\]

at most one of `rho_{2,U},rho_{3,U}` can vanish. Therefore

\[
\max\{\rho_{2,U},\rho_{3,U}\}>0,
\]

and every prime attaining that maximum satisfies `rho_{p,U}>0`, hence `U\notin E_p` and is an available witness prime.

Thus the Section-8 instruction

```text
choose an available witness prime with maximal rho
```

is always realizable; no hidden availability assumption is present.

Book:

```text
R43-COND-MAX-RHO-WITNESS-AVAILABILITY ✓[M]
```

---

## 4. Exact exhaustion of the simple adjacent-support firewall

The same-side support margin used by the present witness is

\[
\delta_p=2a_2-a_p
=\frac12\log\frac4p.
\]

Therefore

\[
\delta_p>0
\iff p<4.
\]

Among primes this is exactly

\[
\boxed{p\in\{2,3\}.}
\tag{R2.8}
\]

So the current **simple adjacent-support firewall** is not merely stopped at `p=3`; it is exhausted exactly by the two primes used in the theorem.

This does **not** prove that every conceivable `p>=5` witness is impossible. It proves only that extending the present argument to `p>=5` requires genuinely new cancellation/support geometry rather than another mechanical prime substitution.

Book:

```text
R43-COND-SIMPLE-ADJACENT-FIREWALL-PRIME-SET ✓[M]
```

---

## 5. Exact step-floor dynamics: the floor alone is not a partition obstruction

Let `c>0` and define the abstract floor-saturating terminal sequence

\[
\boxed{
U_{j+1}=U_j+c e^{-4U_j}.
}
\tag{R2.9}
\]

This sequence is **not claimed to be a PSD partition**. It is used only to test whether the necessary lower-step constraint

\[
h_j\ge c e^{-4U_j}
\]

is itself incompatible with a fine cofinal partition.

### 5.1 Cofinality

The sequence is strictly increasing. If it were bounded above, it would converge to a finite `L`; but then

\[
U_{j+1}-U_j=c e^{-4U_j}\ge c e^{-4L}>0,
\]

contradicting convergence. Hence

\[
\boxed{U_j\to\infty.}
\tag{R2.10}
\]

Consequently

\[
h_j:=U_{j+1}-U_j=c e^{-4U_j}\to0.
\tag{R2.11}
\]

Thus the floor constraint alone is compatible with a cofinal partition whose mesh tends to zero.

### 5.2 Sharp first-order asymptotic

Put

\[
x_j:=e^{4U_j}.
\]

Then

\[
\begin{aligned}
x_{j+1}-x_j
&=x_j\left(\exp\left(\frac{4c}{x_j}\right)-1\right).
\end{aligned}
\]

Since `x_j->infinity`,

\[
\boxed{x_{j+1}-x_j\to4c.}
\tag{R2.12}
\]

Stolz--Cesaro therefore gives

\[
\boxed{
\frac{e^{4U_j}}{j}=\frac{x_j}{j}\longrightarrow4c.
}
\tag{R2.13}
\]

Equivalently,

\[
\boxed{
U_j=\frac14\log(4cj)+o(1),
\qquad
h_j\sim\frac1{4j}.
}
\tag{R2.14}
\]

This proves, rather than merely asserts, that the exponential step floor cannot by itself kill `PARTITION-SELECTIVE-PSD`.

Book with the explicit scope `floor constraint alone`:

```text
R43-COND-STEP-FLOOR-NONOBSTRUCTION ✓[M]
```

`R43-COND-PARTITION-SELECTIVE-PSD ?[O]` remains OPEN because (R2.9) supplies no PSD sign information.

---

## 6. Harmonic firewall for the epsilon-relaxed route

Along the floor-saturating sequence, (R2.13) gives

\[
\boxed{
e^{-4U_j}\sim\frac1{4cj}.
}
\tag{R2.15}
\]

Let `delta_j>=0` be any per-step epsilon defect along this sequence.

### 6.1 Same-order defects cannot telescope absolutely

If there is a constant `kappa>0` such that eventually

\[
\delta_j\ge\kappa e^{-4U_j},
\tag{R2.16}
\]

then for all large `j`,

\[
\delta_j\ge\frac{\kappa}{8c}\frac1j,
\]

and therefore

\[
\boxed{\sum_j\delta_j=\infty.}
\tag{R2.17}
\]

In particular a defect satisfying

\[
\delta_j\asymp e^{-4U_j}
\]

is **not summable** on a floor-near chain.

### 6.2 A clean sufficient reserve

If for some `eta>0`

\[
\delta_j\le C e^{-(4+\eta)U_j},
\tag{R2.18}
\]

then

\[
\delta_j=O\left(j^{-1-\eta/4}\right),
\]

so

\[
\boxed{\sum_j\delta_j<\infty.}
\tag{R2.19}
\]

Thus a genuine exponential reserve beyond exponent `4` is a simple sufficient mechanism on the exact floor chain.

### 6.3 Why `o(1/j)` is not booked as an unconditional necessary condition

Two elementary counterexamples prevent that promotion:

- Summability does not imply `o(1/j)` without regularity: set `delta_j=1/j` when `j=2^n` and `delta_j=0` otherwise. Then `sum delta_j<infinity`, but `j delta_j=1` on infinitely many indices.
- `o(1/j)` is not sufficient: `delta_j=1/(j\log j)` for `j>=2` satisfies `j delta_j->0` but the series diverges.

Therefore the theorem-level unconditional statement is the **same-order harmonic no-go** (R2.16)--(R2.17), not a bare `o(1/j)` criterion.

Book:

```text
R43-COND-EPSILON-FLOOR-HARMONIC-FIREWALL ✓[M]
```

This is a constraint on any epsilon argument that deliberately operates on a floor-saturating or quantitatively floor-comparable chain. It does not prove that every admissible cofinal partition must have this density.

---

## 7. Formal strictness of TP23 over the old cofinal bad-pair theorem

TP23 implies the old theorem directly. Given arbitrary `U_*,h_*>0`, choose

\[
U:=\max\{U_*,U_0\}
\]

and then

\[
h:=\frac12\min\{h_*,h_0(U)\}>0.
\]

TP23 gives `K_{U,U+h}^{Schur}` non-PSD. Thus the old `forall U_* forall h_* exists U exists h` statement follows.

The converse does not supply a bad neighbourhood at **every** late terminal, so TP23 is genuinely stronger as a logical statement.

Book:

```text
R43-COND-TWO-PRIME-STRICT-STRENGTH ✓[M]
```

---

## 8. Corrected live taxonomy after round 2

```text
R43-COND-TWO-PRIME-POINTWISE-LOCAL-NOGO          ✓[M]_neg
R43-COND-TWO-PRIME-NONEXACT-OVERLAP-HARDENING   ✓[M]
R43-COND-TP20-GEOMETRY-SCOPE-HARDENING           ✓[M]
R43-COND-H4-ACTIVE-ENVELOPE-NONCIRCULARITY       ✓[M]
R43-COND-MAX-RHO-WITNESS-AVAILABILITY             ✓[M]
R43-COND-SIMPLE-ADJACENT-FIREWALL-PRIME-SET       ✓[M]
R43-COND-PARTITION-PSD-STEP-FLOOR                 ✓[M]  # necessary only
R43-COND-STEP-FLOOR-NONOBSTRUCTION                ✓[M]  # floor constraint alone
R43-COND-EPSILON-FLOOR-HARMONIC-FIREWALL          ✓[M]  # floor-comparable chains
R43-COND-TWO-PRIME-STRICT-STRENGTH                 ✓[M]

R43-COND-PARTITION-SELECTIVE-PSD                  ?[O]
R43-COND-EPSILON-RELAXED-TELESCOPE                ?[O]
structured-vector COND                            OPEN
B-METINC-COND                                     OPEN
B-FLAGTIGHT                                       OPEN
Strong Terminal/C6                                OPEN
```

No `delta_j=o(1/j)` booking is made without an additional regularity hypothesis.
No `p>=5` global impossibility theorem is made; only the present simple-firewall method is certified exhausted.

---

## 9. Governance

This audit is a post-review hardening of head `ca155fb...` and therefore creates a new PR head. PR #54 must remain Draft until the exact new head and complete diff are independently re-read.

No freeze, no formal independent GREEN, no merge, no Strong-Terminal/C6, Object-X or RH promotion is made here.