# P11 / R43 — geometric-mean resolvent transport and exact metric-leakage bound

**Date:** 2026-09-06  
**Status:** exact local operator reduction; `B-METINC-COND` and Strong Terminal remain OPEN  
**Stack base:** PR #56 head `08153af2447dfd58973ddf93d8acedbf1dabe601`

## 0. Scope and governance firewall

This note is stacked on the frozen PR #56 head and does not modify PR #55 or PR #56.

It has two purposes:

1. repair the proof gap in the statement `||(L_{U,V})_-||<1` at a fixed finite pair without appealing to finite dimensionality;
2. replace the global negative-spectrum route by an exact **symmetric resolvent transport** of the Schur form.

The second point is the main result. It shows that the actual compressed-inverse increment can be written exactly as the negative Schur form evaluated on a canonical positive contraction applied to the original old-source vector. Hence the PR-#55 saturated-leakage bound transfers to the true metric increment, but on a resolvent-transported structured class.

No decay rate, summability theorem, `B-METINC-COND`, `B-METINC`, `B-FLAGDYN/TIGHT`, `B-SIGN/B-ORIENT`, Strong Terminal/C6, Object X or RH is proved here.

---

## 1. Frozen COND algebra

For `X<U<V`, retain

\[
M=R_V\iota,
\qquad
S=R_VP_{\mathcal N},
\qquad
\Phi_S=SS^*(I+SS^*)^{-1},
\]

and

\[
K:=K_{U,V}^{\rm Schur}
=M^*(I+SS^*)^{-1}M-R_U^*R_U.
\tag{GM1}
\]

The exact residual nesting gives

\[
K=C^*C-M^*\Phi_S M.
\tag{GM2}
\]

Put

\[
\mathscr A:=I+R_U^*R_U,
\qquad
\mathscr G:=\mathscr A+K.
\tag{GM3}
\]

Then

\[
\boxed{
\mathscr G
=I+M^*(I+SS^*)^{-1}M
\succeq I.
}
\tag{GM4}
\]

The frozen block-Schur formula gives

\[
\boxed{
B_U=\mathscr A^{-1},
\qquad
\iota^*B_V\iota=\mathscr G^{-1}.
}
\tag{GM5}
\]

Both `\mathscr A` and `\mathscr G` are bounded, positive and boundedly invertible at every fixed finite horizon pair.

---

## 2. Repair of the strict relative spectral gap

Define, as in PR #56,

\[
L:=\mathscr A^{-1/2}K\mathscr A^{-1/2}.
\tag{GM6}
\]

Then

\[
I+L
=\mathscr A^{-1/2}\mathscr G\mathscr A^{-1/2}.
\tag{GM7}
\]

The mere assertion `I+L>0` would not by itself justify a strict uniform spectral gap in infinite dimension. Here, however, (GM4) yields the stronger operator inequality

\[
I+L
\succeq
\mathscr A^{-1/2}I\mathscr A^{-1/2}
=\mathscr A^{-1}.
\tag{GM8}
\]

Since `\mathscr A` is bounded and `\mathscr A\succeq I`,

\[
\mathscr A^{-1}
\succeq
\|\mathscr A\|^{-1}I.
\tag{GM9}
\]

Consequently

\[
\boxed{
I+L\succeq \|\mathscr A\|^{-1}I>0,
}
\tag{GM10}
\]

and therefore

\[
\boxed{
L\succeq
-\Bigl(1-\|\mathscr A\|^{-1}\Bigr)I.
}
\tag{GM11}
\]

Thus, with the standard negative part `L_-:=(-L)_+`,

\[
\boxed{
\|L_-\|
\le
1-\|\mathscr A\|^{-1}
<1.
}
\tag{GM12}
\]

This repairs the strict inequality from PR #56 without any finite-dimensional assumption. It is a fixed-pair statement only; `\|\mathscr A_U\|` may grow with `U`, so GM12 supplies no useful cofinal gap by itself.

### Local booking

```text
R43-COND-FIXED-PAIR-RELATIVE-SPECTRAL-GAP ✓[M]
```

No terminal decay is included.

---

## 3. Canonical symmetric resolvent transport

Define

\[
\boxed{
\mathcal Q_{U,V}
:=
\mathscr A^{-1/2}(I+L)^{-1/2}\mathscr A^{-1/2}.
}
\tag{GM13}
\]

This operator is positive and selfadjoint.

Using GM5 and GM7,

\[
\mathscr A^{1/2}\mathscr G^{-1}\mathscr A^{1/2}
=(I+L)^{-1}.
\]

Hence, in Kubo--Ando geometric-mean notation,

\[
\boxed{
\mathcal Q_{U,V}
=B_U\#(\iota^*B_V\iota).
}
\tag{GM14}
\]

Indeed, for positive invertible `P,Q`,

\[
P\#Q
=P^{1/2}(P^{-1/2}QP^{-1/2})^{1/2}P^{1/2},
\]

and substituting `P=B_U=\mathscr A^{-1}`, `Q=\mathscr G^{-1}` gives GM13.

Because

\[
0<B_U\preceq I,
\qquad
0<\iota^*B_V\iota\preceq I,
\]

monotonicity of the operator geometric mean gives

\[
\boxed{
0<\mathcal Q_{U,V}\preceq I.
}
\tag{GM15}
\]

Thus the resolvent transport is a canonical positive contraction. This is a norm statement only; it does not imply preservation of spatial support or of the raw hub shell.

The geometric mean also satisfies the Riccati identities

\[
\boxed{
\mathcal Q\,\mathscr A\,\mathcal Q
=\mathscr G^{-1}=\iota^*B_V\iota,
}
\tag{GM16}
\]

and

\[
\boxed{
\mathcal Q\,\mathscr G\,\mathcal Q
=\mathscr A^{-1}=B_U.
}
\tag{GM17}
\]

---

## 4. Exact symmetric factorization of the compressed-inverse increment

From PR #56,

\[
\iota^*B_V\iota-B_U
=\mathscr A^{-1/2}\bigl((I+L)^{-1}-I\bigr)\mathscr A^{-1/2}.
\tag{GM18}
\]

Since `L` commutes with every bounded Borel function of `L`,

\[
(I+L)^{-1}-I
=-L(I+L)^{-1}
=-(I+L)^{-1/2}L(I+L)^{-1/2}.
\tag{GM19}
\]

Also

\[
K=\mathscr A^{1/2}L\mathscr A^{1/2}.
\]

Combining these identities with GM13 gives the exact **operator** factorization

\[
\boxed{
\iota^*B_V\iota-B_U
=-\mathcal Q_{U,V}\,K_{U,V}^{\rm Schur}\,\mathcal Q_{U,V}.
}
\tag{GM20}
\]

This is stronger than the scalar formula from PR #56. It is a symmetric congruence of the Schur sign operator by a canonical positive contraction.

### Direct hand check

Indeed,

\[
\begin{aligned}
\mathcal QK\mathcal Q
&=\mathscr A^{-1/2}(I+L)^{-1/2}
\underbrace{\mathscr A^{-1/2}K\mathscr A^{-1/2}}_{L}
(I+L)^{-1/2}\mathscr A^{-1/2}\\
&=\mathscr A^{-1/2}L(I+L)^{-1}\mathscr A^{-1/2},
\end{aligned}
\]

which is the negative of GM18.

### Local booking

```text
R43-COND-GEOMETRIC-MEAN-RESOLVENT-FACTORIZATION ✓[M]
```

---

## 5. Exact transfer of saturated leakage to the true metric increment

Insert the frozen Schur decomposition GM2 into GM20:

\[
\boxed{
\iota^*B_V\iota-B_U
=
\mathcal Q M^*\Phi_S M\mathcal Q
-\mathcal Q C^*C\mathcal Q.
}
\tag{GM21}
\]

Therefore, as an operator upper bound,

\[
\boxed{
\iota^*B_V\iota-B_U
\preceq
\mathcal Q M^*\Phi_S M\mathcal Q.
}
\tag{GM22}
\]

For every old-source vector `v`,

\[
\boxed{
\bigl(\langle v,(\iota^*B_V\iota-B_U)v\rangle\bigr)_+
\le
\langle M\mathcal Qv,\Phi_S M\mathcal Qv\rangle.
}
\tag{GM23}
\]

Using the exact PR-#55 push-through identity,

\[
\langle Mx,\Phi_S Mx\rangle
=\|(I+S^*S)^{-1/2}S^*Mx\|^2,
\]

GM23 becomes

\[
\boxed{
\bigl(\langle v,(\iota^*B_V\iota-B_U)v\rangle\bigr)_+
\le
\left\|
(I+S^*S)^{-1/2}S^*M\mathcal Q_{U,V}v
\right\|^2.
}
\tag{GM24}
\]

This is the exact resolvent-transfer statement that the scalar PR-#55 bound could not provide on the **untransported** vector.

For the actual structured vector

\[
v_U(f)=H_U^*E_{X,U}f,
\]

we obtain

\[
\boxed{
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
\le
\left\|
(I+S^*S)^{-1/2}S^*M
\mathcal Q_{U,V}H_U^*E_{X,U}f
\right\|^2.
}
\tag{GM25}
\]

Moreover the exact scalar identity behind it is

\[
\boxed{
\Delta s_{\rm cond}^{U,V}(f)
=-\langle \mathcal Qv_U,
K_{U,V}^{\rm Schur}\mathcal Qv_U\rangle.
}
\tag{GM26}
\]

Hence the earlier firewall is resolved as follows:

> scalar saturated leakage at `v_U` does not transfer directly to the inverse increment, but saturated leakage at the canonical geometric-mean transported vector `\mathcal Q_{U,V}v_U` does.

### Local booking

```text
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND ✓[M]
```

This is an exact local theorem. It does not contain a terminal rate.

---

## 6. The new structured class

Define the canonical resolvent-transported structured class

\[
\boxed{
\mathcal V_{X;U,V}^{\rm res}
:=
\mathcal Q_{U,V}\,\operatorname{Ran}(H_U^*E_{X,U}).
}
\tag{GM27}
\]

Then GM25 says that `B-METINC-COND` no longer requires a global estimate of `||(L_{U,V})_-||`. It is sufficient to control the saturated nuisance leakage on this transported class.

A sufficient quantitative target along a cofinal chain is therefore

\[
\boxed{
\left\|
(I+S^*S)^{-1/2}S^*Mx
\right\|
\le A_{X,f}e^{-(2+\eta/2)U},
\qquad
x=\mathcal Q_{U,V}v_U(f),
}
\tag{GM28}
\]

for some `\eta>0`. Then

\[
\bigl(\Delta s_{\rm cond}^{U,V}(f)\bigr)_+
\le A_{X,f}^2e^{-(4+\eta)U},
\]

which is compatible with the already proved one-sided step-floor reserve.

Crucially, GM28 is weaker in one direction and stronger in another than PR #55's original structured target:

- it avoids global negative-spectrum control;
- but it requires leakage control after the nonlocal positive contraction `\mathcal Q_{U,V}`.

No claim is made that `\mathcal Q_{U,V}` preserves the terminal collar or the raw prime-power support of `v_U`.

---

## 7. Why this bypasses the global `||L_-||` route

The PR-#56 transfer through a relative lower bound

\[
K\succeq-\delta\mathscr A
\]

remains mathematically valid. GM12 repairs the fixed-pair strictness needed to define such a `\delta<1`.

However, for the structured metric increment the new identity GM25 is sharper as a research reduction: it does not require proving that the entire negative spectral subspace of `L` is small. Instead it asks only for saturated leakage on the one canonically transported structured vector/class actually seen by the inverse metric.

Thus the active quantitative node should be refined to

```text
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
```

with target GM28.

The older node

```text
R43-COND-RELATIVE-NEGATIVE-SPECTRAL-DECAY ?[O]
```

may be retained as a stronger alternative route, but it is no longer logically necessary for `B-METINC-COND`.

---

## 8. Adversarial checks / firewalls

1. **Infinite-dimensional spectral-gap firewall.** `I+L>0` alone is insufficient for `||L_-||<1`; GM10 uses the stronger exact bound `\mathscr G\succeq I` and boundedness of `\mathscr A`.
2. **Congruence is not support preservation.** `0\preceq\mathcal Q\preceq I` gives norm contraction, not locality. The raw collar-shell theorem for `v_U` cannot be applied unchanged to `\mathcal Qv_U`.
3. **No commutation assumed.** GM20 is derived through the relative operator `L`; it does not assume `\mathscr A` and `K` commute.
4. **No global spectral decay.** GM25 bypasses `||L_-||`; no terminal estimate on the negative spectrum is booked.
5. **No hidden Loewner positivity.** GM22 is only an upper bound on the signed inverse increment. It does not assert `\iota^*B_V\iota\succeq B_U` or the reverse.
6. **No decay from contraction alone.** `\mathcal Q\preceq I` does not imply `\langle \mathcal Qv,T\mathcal Qv\rangle\le\langle v,Tv\rangle` for an unrelated positive `T`.
7. **No Strong-Terminal promotion.** Even GM28, if proved, would address only the positive part of canonical COND; the remaining metric front and downstream gates retain their existing firewalls.

---

## 9. Status ledger

New local theorem-level bookings:

```text
R43-COND-FIXED-PAIR-RELATIVE-SPECTRAL-GAP         ✓[M]
R43-COND-GEOMETRIC-MEAN-RESOLVENT-FACTORIZATION  ✓[M]
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND     ✓[M]
```

Retained / refined OPEN nodes:

```text
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
R43-COND-RELATIVE-NEGATIVE-SPECTRAL-DECAY             ?[O]  stronger optional route
R43-COND-STRUCTURED-WITNESS-EXCLUSION                  ?[O]
R43-COND-EPSILON-RELAXED-TELESCOPE                     ?[O]
B-METINC-COND                                           ?[O]
B-METINC                                                ?[O]
B-FLAGMOD / B-FLAGDYN                                   ?[O]
B-FLAGTIGHT                                             ?[O]
B-SIGN / B-ORIENT                                       ?[O]
Strong Terminal / C6                                    ?[O]
Object X / RH                                           ?[O]
```

No merge/freeze/promotion beyond these local exact identities.

---

## 10. Next attack

The quantitative target is now the single object

\[
\boxed{
\mathfrak L_{U,V}^{\rm res}(f)
:=(I+S^*S)^{-1/2}S^*M
\mathcal Q_{U,V}H_U^*E_{X,U}f.
}
\tag{GM29}
\]

The next proof attempt should exploit the exact source-side identity

\[
S^*M=P_{\mathcal N}A_V\iota
\]

and split the normal-equation shifts into

\[
|k-\ell|a_p\le r(U),
\qquad
|k-\ell|a_p>r(U),
\qquad
(k+\ell)a_p,
\]

but now with the crucial additional task of controlling what the geometric-mean contraction `\mathcal Q_{U,V}` does to the raw structured hub shell.

A productive subgoal is a quasi-locality or weighted-energy estimate for `\mathcal Q_{U,V}` rather than exact support preservation. Because `\mathcal Q` is built canonically from the two old-source inverse metrics, such an estimate would be precisely the resolvent-stability statement needed by GM25.
