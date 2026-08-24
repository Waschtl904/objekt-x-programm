# P12 Runde 25 — Horizon-Wall depth-21 circuit

**Status:** local theorem candidate; **not promoted**.  
**Repo basis:** `Waschtl904/objekt-x-programm`, `main@38807dfe189a6cdc7386e78e0c40c17169317a8a`.  
**Input:** Round 24 C42/C44 local chambers, both `✓[M]_part`.  
**Firewall:** P11 FROZEN; R14 unchanged; no Polar Gauge, Terminal Transport, Objekt X or RH claim.

---

## 1. Target wall

In the Round-24 C42 geometry define

\[
U_-(x)=T+\kappa-x\leftrightarrow(-1,5,1),
\qquad
U_+(x)=T+x+\eta\leftrightarrow(1,5,0).
\]

The two horizon walls are

\[
\varepsilon+x=\kappa
\]

and

\[
\varepsilon=x+\eta.
\]

Round 24 established that crossing either wall removes one of the old 42 source rows and leaves a `41 x 42` old-variable system.  The prior one-step search was only a research diagnostic, not a no-go theorem.

Round 25 studies the **minus wall**, where

\[
\kappa-x>\varepsilon
\]

so the source `(-1,5,1)` is no longer horizon-legal, while

\[
x+\eta<\varepsilon
\]

keeps `(1,5,0)` legal.

---

## 2. Exact open chamber B25-

Work in the rational open box

\[
\boxed{
0.0195<R<0.0205,
}
\]

\[
\boxed{
0.0275<x<0.0285,
}
\]

\[
\boxed{
0.0395<\sigma<0.0405,
}
\]

\[
\boxed{
0.0550<\varepsilon<0.0559.
}
\tag{B25-}
\]

The retained verifier proves from exact rational atanh-series bounds for `ln 2` and `ln 3` that throughout the whole box

\[
0<R<x<\sigma<\varepsilon<\varepsilon_{\max},
\]

\[
\kappa-x>\varepsilon,
\qquad
x+\eta<\varepsilon,
\]

and hence `U_-` is uniformly above the source horizon while `U_+` remains uniformly horizon-legal.

It also checks every source and every canonical raw slot against the support and horizon walls with exact rational interval arithmetic.  Thus the row pattern used below is constant on the whole open box, not merely at one floating test point.

---

## 3. The surviving Round-23 block

At the reference point

\[
(R,x,\sigma,\varepsilon)=(0.020,0.028,0.040,0.0555),
\]

exactly one source from the 42-source Round-23 family is lost:

\[
(-1,5,1).
\]

The remaining 41 rows still see exactly the original 42 old visibility variables.  Hence the old block is

\[
41\times42.
\]

In particular the old visibility set contains both

\[
(1,0,0)\leftrightarrow h(x)
\]

and

\[
(-1,0,1)\leftrightarrow h(\delta-x).
\]

---

## 4. Search diagnostic: why the next shell is genuinely deeper

A breadth-first search was organized by canonical shift distance from the old visibility set.  The search is **diagnostic only** and is not part of the theorem statement.

At the one-sided horizon-loss point:

- distance 1 reproduces the old 142-style one-step obstruction;
- distance 2 still yields no left dependency in the new-variable rows;
- in the retained generic-rank scan, distances through 20 remain free of an effective new-variable circuit;
- at distance 21 a first effective circuit appears.

No claim is made that `21` is a canonical arithmetic threshold.  It is only the first depth found by this particular breadth-first source search.

---

## 5. The 51-source / 50-new-variable circuit

A fundamental circuit can be isolated using exactly the following 51 horizon-legal sources:

```text
(-1,1,-1),
(-1,2,-4),(-1,2,-3),(-1,2,-2),(-1,2,-1),
(-1,3,-5),(-1,3,-4),(-1,3,-3),(-1,3,-2),(-1,3,-1),
(-1,4,-5),(-1,4,-4),(-1,4,-3),(-1,4,-2),(-1,4,-1),
(-1,5,-5),(-1,5,-4),(-1,5,-3),(-1,5,-2),(-1,5,-1),(-1,5,0),
(-1,6,-4),(-1,6,-3),(-1,6,-2),(-1,7,-4),
(1,-2,5),(1,-2,6),
(1,-1,2),(1,-1,3),(1,-1,4),(1,-1,5),(1,-1,6),(1,-1,7),
(1,0,2),(1,0,3),(1,0,4),(1,0,5),(1,0,6),(1,0,7),(1,0,8),
(1,1,3),(1,1,4),(1,1,5),(1,1,6),(1,1,7),(1,1,8),
(1,2,4),(1,2,5),(1,2,6),(1,2,7),(1,3,4).
```

Every row is reconstructed only from

\[
Lh(u)=
p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)],
\]

odd reflection, support cutoff, and the horizon cutoff.

Relative to the 42 old visibility coordinates these 51 rows introduce **exactly 50 new coordinates**.  Hence the new-variable block has shape

\[
\boxed{N_{51}:51\times50.}
\]

This is the finite circuit that was absent in the shallow source shells.

---

## 6. The 92 x 92 closure

Append the 51 circuit rows to the 41 surviving Round-23 rows, and order the columns as

- the 42 old visibility coordinates;
- the 50 new circuit coordinates.

The result is a square raw-operator matrix

\[
\boxed{M_{92}\in M_{92}(\mathbb R).}
\]

No reduced or hand-inserted row is used.

The retained verifier reconstructs all `92 x 6` canonical raw slots and obtains exactly 92 live columns.

---

## 7. Rigorous nondegeneracy certificate

Factor out `p` from each row and set

\[
\beta=\frac qp=2^{-3/4},
\]

\[
\alpha=\frac rp
=
\sqrt{\frac{\log3}{\log2}}\left(\frac23\right)^{3/4}.
\]

Thus

\[
\det M_{92}=p^{92}D_{92}(\beta,\alpha).
\]

The verifier first proves exact rational enclosures for `beta` and `alpha`:

- `beta` is bracketed by rational decimals whose fourth powers straddle `1/8`;
- `ln 2` and `ln 3` are bracketed by positive atanh series with explicit rational remainders;
- `sqrt(8/27)` is bracketed by exact rational square comparisons;
- these bounds give a rational bracket for
  \[
  \alpha^2=\frac{\log3}{\log2}\sqrt{\frac8{27}},
  \]
  and hence a rational bracket for `alpha`.

It then performs 120-digit **directed-rounding interval Gaussian elimination** on the full scaled 92 x 92 matrix.  Every pivot interval excludes zero.  The final determinant enclosure is

\[
\boxed{
D_{92}\in
(
1.9850792121557575604061864810750\times10^{-5},
1.9850792121557575604139727620295\times10^{-5}
).
}
\]

In particular

\[
\boxed{D_{92}>0}
\]

and since `p>0`,

\[
\boxed{\det M_{92}\ne0.}
\]

This is a rigorous interval certificate, not a floating rank test.

---

## 8. Local theorem candidate

Because `M92` is invertible, all 92 visibility coordinates vanish.  In particular, for every kernel vector and for a.e. `x` in the B25- strip,

\[
\boxed{h(x)=0}
\]

and simultaneously

\[
\boxed{h(\delta-x)=0.}
\]

Thus, for every fixed

\[
0.0195<R<0.0205,
\quad
0.0395<\sigma<0.0405,
\quad
0.0550<\varepsilon<0.0559,
\]

a kernel vector vanishes on the two open intervals

\[
\boxed{I_-=(0.0275,0.0285)}
\]

and

\[
\boxed{I_+=\delta-I_-
=(\delta-0.0285,\delta-0.0275)}.
\]

The exact involution

\[
J(s,m,n)=(-s,m,n+s),
\qquad x\mapsto\delta-x,
\]

maps the minus-wall matrix to its mirror matrix coefficient-for-coefficient.

---

## 9. Scope

This does **not** close the full horizon wall and does **not** give a new global lower-radius threshold.

It proves one explicit open chamber on the far side of the previously hard horizon wall.  The significance is structural:

- the one-step obstruction is not a true barrier;
- a finite deeper circuit exists;
- it can be certified by a closed raw matrix;
- the certificate kills a paired low strip rather than only one point.

Before independent review:

\[
\boxed{\text{R25 horizon-depth21 local closure: theorem candidate}.}
\]

No Polar Gauge, Terminal Transport, Objekt X or RH consequence is claimed.
