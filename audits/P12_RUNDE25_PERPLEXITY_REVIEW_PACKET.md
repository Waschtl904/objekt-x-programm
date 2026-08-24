# P12 Round 25 — independent adversarial review packet

**Repo basis:** `Waschtl904/objekt-x-programm`, starting from
`main@38807dfe189a6cdc7386e78e0c40c17169317a8a` plus the Round-25 candidate commit.

**Status under review:** local theorem candidate only.  P11 is FROZEN; R14 is unchanged.

Please reconstruct the result independently from the canonical raw operator, not from the claimed determinant interval.

Return one main verdict:

- `R25: GREEN / PARTIAL / FAIL`

and, separately if desired:

- `DEPTH-21 SEARCH DIAGNOSTIC: GREEN / PARTIAL / NOT CHECKED`.

---

## A. Reconstruct the horizon-loss side

Use

\[
Lh(u)=p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)].
\]

At the reference point

\[
(R,x,\sigma,\varepsilon)=(0.020,0.028,0.040,0.0555),
\]

check independently that among the committed Round-23 42 sources exactly

\[
(-1,5,1)
\]

is lost at the upper horizon, while `(1,5,0)` remains horizon-legal.  The surviving old block should therefore have 41 rows and 42 old visibility coordinates.

Verify that the old visibility set contains both `(1,0,0)` and `(-1,0,1)`, corresponding to `h(x)` and `h(delta-x)`.

---

## B. Check the whole open box

The claimed chamber is

\[
0.0195<R<0.0205,
\]
\[
0.0275<x<0.0285,
\]
\[
0.0395<\sigma<0.0405,
\]
\[
0.0550<\varepsilon<0.0559.
\]

Independently verify, preferably with exact rational bounds for `ln 2` and `ln 3`, that throughout the entire box:

1. all 41 retained Round-23 rows are horizon-legal;
2. all 51 new circuit sources are horizon-legal;
3. `(-1,5,1)` is uniformly above the horizon;
4. `(1,5,0)` remains uniformly below the horizon;
5. every odd-reflection sign and every support live/dead decision is constant.

The theorem requires whole-box pattern stability, not merely the reference point.

---

## C. Reconstruct the 51-source circuit

Use exactly the 51 sources listed in

`audits/P12_RUNDE25_HORIZON_DEPTH21_AUDIT.md`

and reconstruct all six raw slots of every source.

Required counts:

\[
41\text{ old rows},
\qquad
42\text{ old variables},
\]

\[
51\text{ circuit rows},
\qquad
50\text{ genuinely new variables}.
\]

Thus the final matrix must be

\[
\boxed{92\times92}.
\]

No hand-reduced row is allowed.

---

## D. Independently certify det(M92) != 0

Scale `p` from each row and use

\[
\beta=q/p=2^{-3/4},
\qquad
\alpha=r/p
=\sqrt{\frac{\log3}{\log2}}(2/3)^{3/4}.
\]

The committed verifier uses exact rational input brackets plus 120-digit directed-rounding interval Gaussian elimination and obtains

\[
D_{92}\in
(
1.9850792121557575604061864810750\times10^{-5},
1.9850792121557575604139727620295\times10^{-5}
).
\]

Please independently certify nonzero determinant.  You do not need to reproduce the same interval algorithm; exact symbolic factorization, rational interval arithmetic, Arb-style ball arithmetic, or another rigorous method is acceptable.

The essential claim is

\[
\det M_{92}\ne0
\]

for the actual P12 weights, not merely generic rank.

---

## E. J symmetry and conclusion

Check

\[
J(s,m,n)=(-s,m,n+s),
\qquad x\mapsto\delta-x,
\]

and verify that the mirror raw matrix is coefficient-identical after J-ordering.

If the determinant certificate is valid, confirm that all 92 visibility coordinates vanish and therefore every kernel vector satisfies, for a.e. x in `(0.0275,0.0285)`,

\[
h(x)=0,
\qquad
h(\delta-x)=0.
\]

Equivalently the two open strips

\[
I_-=(0.0275,0.0285),
\qquad
I_+=(\delta-0.0285,\delta-0.0275)
\]

are killed in this local parameter chamber.

---

## F. Search-depth wording

The statement that a breadth-first search first found an effective circuit at shift distance 21 is **diagnostic**, not part of the theorem.

Do not interpret 21 as a canonical threshold.  The review may return `NOT CHECKED` on this diagnostic without affecting a GREEN verdict for the explicit 92 x 92 theorem candidate.

No statement about Polar Gauge, Terminal Transport, Objekt X or RH is under review.
