# P11 / R43 — primitive shifted-preimage occupancy kernel: corrected weight asymptotics and firewall

**Date:** 2026-09-06  
**Status:** local/conditional audit on top of PR #76; no reverse-normal decay claim  
**Exact parent head:** `d2d8b9077a61f5d103bcec02548fdf29fa282c2e`

## 0. Purpose and scope

PR #76 isolates, in the primitive `k=1` star model, the coherent weighted-mean penalty

\[
M(z)=\frac{W(z)}{1+W(z)}\,|\bar x_w(z)|^2
\le
\frac{1}{1+W(z)}\sum_{p\in A(z)}w_p\,|x(z-\log p)|^2.
\tag{OK0}
\]

A tempting next step is to change variables from the new-strip point `z` to the old preimage `u=z-\log p` and bound the resulting geometric occupancy kernel in `L^\infty`.

This note checks that route destructively.

The main conclusions are:

1. the large-prime tail proposed from `w_p\sim(\log p)p^{-3/2}` is algebraically incorrect;
2. the correct primitive weight is asymptotically `w_p\asymp(\log p)p^{-1/2}`;
3. after the denominator `1+W(z)` is retained, the occupancy kernel does have an exponential boundary-layer profile, but its boundary height is of order `V-U`, not `O(\log U/U)`;
4. hence a bare `L^\infty` occupancy estimate and the existing unweighted PR-#64 collar mass do not close the reverse mean channel;
5. the corrected open target is a **weighted opposite-boundary occupancy estimate for the actual structured vector**.

Everything below is confined to the primitive `k=1` star/occupancy reduction used in PR #74/#76.  No statement here upgrades the full P11 extension operator, reverse-normal decay, FD23-UNIF, FLAGDYN/TIGHT, Strong Terminal/C6, Object X, or RH.

---

## 1. Correct primitive prime weight

PR #64 defines

\[
\boxed{
 w_p=(\log p)(p-1)p^{-3/2}.
}
\tag{OK1}
\]

Since

\[
(p-1)p^{-3/2}=p^{-1/2}(1-p^{-1}),
\]

we have, for every `p\ge2`,

\[
\boxed{
\frac12(\log p)p^{-1/2}
\le w_p\le
(\log p)p^{-1/2}.
}
\tag{OK2}
\]

Thus, writing `t=\log p`,

\[
\boxed{w_p\asymp t e^{-t/2}.}
\tag{OK3}
\]

It is **not** true that `w_p\asymp t e^{-3t/2}`.

This correction is already consistent with PR #64 CE2, where fixed multiplicative prime bands satisfy

\[
\sum_{e^t\le p\le \Lambda e^t}w_p\gtrsim e^{t/2}.
\tag{OK4}
\]

Consequently the raw large-prime sum

\[
\sum_{p>U^C}w_p
\]

is not a decaying tail; without a horizon cutoff it diverges.  Therefore the proposed estimate

\[
\sum_{p>U^C}(\log p)p^{-3/2}=O(U^{-C/2+1})
\]

does not apply to the actual primitive weight `w_p`.

### Local booking

```text
R43-COND-REVERSE-OCCUPANCY-LARGE-PRIME-RAW-TAIL ×[M]
```

---

## 2. Fixed-log-band upper and lower mass

PR #64 supplies the lower fixed-band bound.  The same Chebyshev upper estimate gives the matching upper bound: for one fixed `\Lambda>1` and all sufficiently large `t`,

\[
\boxed{
 c_0e^{t/2}
\le
\sum_{e^t\le p\le \Lambda e^t}w_p
\le
C_0e^{t/2}.
}
\tag{OK5}
\]

Indeed, Chebyshev gives `\#\{p\in[x,\Lambda x]\}\asymp x/\log x`, while each such prime has `w_p\asymp(\log x)x^{-1/2}`.

Summing fixed multiplicative bands geometrically therefore yields, for `T` large,

\[
\boxed{
\sum_{p\le e^T}w_p\asymp e^{T/2}.
}
\tag{OK6}
\]

No PNT is required.

---

## 3. Primitive positive-strip occupancy kernel

Consider first the positive new strip

\[
\mathcal N_+=(U,V).
\]

For the centered primitive `k=1` endpoint geometry, a new-strip endpoint `z\in(U,V)` can couple to an old endpoint

\[
 u=z-\log p\in(-U,U).
\tag{OK7}
\]

Equivalently, for fixed `z`, the active logarithmic shifts satisfy

\[
 z-U<\log p<z+U.
\tag{OK8}
\]

Define the primitive positive-strip total star weight

\[
W_+(z):=
\sum_{p:\ z-\log p\in(-U,U)}w_p.
\tag{OK9}
\]

The change of variables in the Cauchy occupancy bound gives the old-window kernel

\[
\boxed{
\omega_+(u)
:=
\sum_{p:\ U<u+\log p<V}
\frac{w_p}{1+W_+(u+\log p)}.
}
\tag{OK10}
\]

Thus the positive-strip primitive mean is bounded by

\[
\int_U^V M(z)\,dz
\le
\int_{-U}^U\omega_+(u)|x(u)|^2\,du.
\tag{OK11}
\]

The negative strip has the reflected kernel

\[
\omega_-(u)=\omega_+(-u)
\tag{OK12}
\]

up to the harmless endpoint/null-set conventions of the centered translation model.

### Typing / eligibility remark

The old point in OK7 is an endpoint of the centered difference.  The martingale eligibility variable is the midpoint, not the new-strip endpoint itself.  Hence a condition of the form

```text
J_{p,U}(z)=1   with z in the new strip
```

is not the correct way to formulate the primitive edge.  The endpoint geometry OK7--OK8 is the appropriate star-model condition used here.

---

## 4. Denominator asymptotics

For `z\in(U,V)` and large `U`, the active interval in OK8 reaches up to logarithmic size `z+U`.

Using one fixed Chebyshev band immediately below that upper endpoint gives

\[
W_+(z)\gtrsim e^{(z+U)/2}.
\tag{OK13}
\]

Conversely, OK6 gives

\[
W_+(z)\le\sum_{p\le e^{z+U}}w_p
\lesssim e^{(z+U)/2}.
\tag{OK14}
\]

Hence

\[
\boxed{
W_+(z)\asymp e^{(z+U)/2}
}
\tag{OK15}
\]

uniformly in the positive strip once `U` is sufficiently large.

This is the true large-prime self-normalization mechanism: the raw prime-band mass grows like `e^{t/2}`, but the denominator grows at the same exponential scale determined by the largest admissible shifts.

---

## 5. Occupancy boundary-layer profile

Fix an old point `u\in(-U,U)` and write its distance from the **opposite** old boundary as

\[
 d_+(u):=u+U.
\tag{OK16}
\]

For a prime contributing to OK10 put `t=\log p` and `z=u+t`.  By OK15,

\[
\frac{1}{1+W_+(u+t)}
\asymp
 e^{-(u+t+U)/2}.
\tag{OK17}
\]

Now group the admissible `t`-interval

\[
U-u<t<V-u
\tag{OK18}
\]

into fixed logarithmic bands of the same width used in OK5.  In each full band, the numerator mass is `\asymp e^{t/2}` while the denominator factor is `\asymp e^{-(u+t+U)/2}`.  Therefore **each full active logarithmic band contributes**

\[
\asymp e^{-(u+U)/2}=e^{-d_+(u)/2}
\tag{OK19}
\]

to `\omega_+(u)`.

There are `\asymp 1+(V-U)` such fixed-width bands.  Consequently, away from only `O(1)` endpoint-band effects,

\[
\boxed{
\omega_+(u)
\asymp
(1+V-U)e^{-(u+U)/2}.
}
\tag{OK20}
\]

For the two-sided strip, the corresponding upper profile is

\[
\boxed{
\omega(u)
\lesssim
(1+V-U)
\left(
 e^{-(U+u)/2}
 +e^{-(U-u)/2}
\right).
}
\tag{OK21}
\]

Thus the primitive occupancy kernel is indeed exponentially concentrated near the old boundaries — but each strip sees most strongly the **opposite** old boundary.

### Important consequence

If `V-U\asymp U` (for example on a dyadic step `V\in[cU,2U]` with `c>1` fixed), then

\[
\boxed{
\|\omega\|_{L^\infty(-U,U)}\asymp U,
}
\tag{OK22}
\]

not `O(\log U/U)`.

Hence the route

\[
\mathcal O_{U,V}(x)
\le
\|\omega\|_\infty\|x\|_2^2
\]

cannot prove the required decay from `\|x\|_2\le1`.

### Local bookings

```text
R43-COND-REVERSE-PRIMITIVE-OCCUPANCY-BOUNDARY-LAYER ✓[M]_local
R43-COND-REVERSE-OCCUPANCY-LINF-DECAY ×[M]
```

The first booking is confined to the primitive star/occupancy model of this note; it is not an operatorwide P11 theorem.

---

## 6. Relation to PR #64 collar escape

On a dyadic interval `V\le2U`, OK21 gives outside an `r`-collar

\[
\omega(u)\lesssim Ue^{-r/2}.
\tag{OK23}
\]

With `r=8\log U`, the **bulk** occupancy weight is therefore

\[
\boxed{
\omega(u)\lesssim U^{-3}
\qquad
\text{whenever }U-|u|\ge8\log U.
}
\tag{OK24}
\]

So the bulk part is harmless.

However, inside the same collar one only has the crude scale

\[
\omega(u)\lesssim U.
\tag{OK25}
\]

PR #64 gives for the actual structured transported vector only

\[
\|\chi_{U,8\log U}x_{\rm rev}\|_2^2
=O\!\left(\frac{\log U}{U}\right).
\tag{OK26}
\]

Combining OK25 with OK26 by a supremum estimate gives at best an `O(\log U)` bound, not the desired `O(\log U/U)`.

Therefore **unweighted collar mass alone is one full factor of `U` too weak** for the primitive occupancy kernel at the boundary peak.

This is consistent with the constant-profile obstruction in PR #72/#74: geometric normalization alone does not force the coherent mean to decay.

---

## 7. Corrected open target

The mean route is not dead; it is simply sharper than a small-/large-prime split.

The corrected quantity is a weighted opposite-boundary occupancy, schematically

\[
\boxed{
\int_{-U}^{U}
(1+V-U)
\left(
 e^{-(U+u)/2}+e^{-(U-u)/2}
\right)
|x_{\rm rev}(u)|^2\,du.
}
\tag{OK27}
\]

A bound

\[
\boxed{
\text{OK27}
=O\!\left(\frac{\log U}{U}\right)
}
\tag{OK28}
\]

would close the primitive coherent mean channel via OK11/OK21.

But OK28 is strictly stronger than the currently available unweighted PR-#64 collar mass estimate.  It requires additional structure of the actual

\[
x_{\rm rev}=\mathcal Q_{U,V}H_U^*E_{R,U}f_{\rm rev}
\]

near the **opposite boundary layers**, or a stronger use of the full Schur/least-squares denominator than the pointwise Cauchy majorant OK0.

### Revised roadmap targets

```text
ROADMAP-COND-REVERSE-SHIFTED-PREIMAGE-OCCUPANCY          ?[O]
ROADMAP-COND-REVERSE-WEIGHTED-OPPOSITE-COLLAR           ?[O]
ROADMAP-COND-REVERSE-PRIME-SHIFT-MEAN-CONTROL           ?[O]
ROADMAP-COND-REVERSE-PRIME-SHIFT-VARIANCE-CONTROL       ?[O]
ROADMAP-COND-REVERSE-NORMAL-STRETCH-DECAY                ?[O]
```

---

## 8. Firewall and consequence

This audit rejects only the proposed proof shortcut

```text
small-prime collar + absolutely summable large-prime raw tail
    => ||omega||_infty = O(log U/U)
    => reverse mean decay.
```

The failure is caused by the exact factor `(p-1)` in `w_p`, which changes the large-prime scale from `p^{-3/2}` to `p^{-1/2}`.

What survives is useful:

- the denominator `1+W(z)` self-normalizes the huge raw large-prime mass;
- the resulting primitive occupancy kernel has an explicit exponential boundary-layer shape;
- its bulk is extremely small at the PR-#64 collar scale;
- only a weighted boundary-layer estimate for the **actual structured vector** remains.

No reverse-normal stretch decay, cheap full extension, FD23-UNIF, B-FLAGDYN/TIGHT, Strong Terminal/C6, Object-X realization, or RH conclusion is made.

Keep Draft.
