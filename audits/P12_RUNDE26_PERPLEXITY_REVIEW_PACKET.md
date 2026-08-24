# P12 Round 26 — independent adversarial review packet

**Repo basis:** `Waschtl904/objekt-x-programm`, starting from
`main@9b0982e40b60730c4936eb8910ef425c883ccfb4` plus the Round-26 candidate chain.

**Status under review:** local theorem candidate only.  
P11 is FROZEN; R14 unchanged.

Please reconstruct from the canonical raw operator and the promoted Round-25
92-source certificate. Do not infer any global low-radius theorem.

Return:

- `R26-A MINUS ENLARGEMENT: GREEN / PARTIAL / FAIL`
- `R26-B J-MIRROR: GREEN / PARTIAL / FAIL`
- `R26-GLUING: GREEN / PARTIAL / FAIL`

---

## 1. Fixed selected source set

Use exactly the promoted Round-25 selected 92 rows:

- the 41 surviving Round-23 rows at the minus-horizon reference point;
- the 51-source Round-25 circuit.

The source `(-1,5,1)` is intentionally **not** part of this selected set.

Reconstruct every row only from

\[
Lh(u)=p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)].
\]

---

## 2. Review R26-A

Independently test whether the exact constant-pattern chamber of this fixed
92-row certificate is

\[
\eta<x<\chi,
\]

\[
\chi<R+x<2\eta,
\]

\[
x-R<\eta,
\]

\[
\chi-\eta<\sigma-x,
\]

\[
\sigma+x<3\eta,
\]

\[
x+\eta<\varepsilon<\varepsilon_{\max}.
\]

Required adversarial checks:

1. enumerate all selected source lower/upper horizon events;
2. enumerate all `92 x 6` raw slots, including odd-reflection sign changes;
3. verify that the eight non-arithmetic inequalities are genuine raw events;
4. verify that **no hidden ninth raw facet** cuts the interior;
5. verify that the original B25-minus rational box is strictly contained;
6. reconstruct the resulting matrix and check it is coefficient-for-coefficient
   the promoted Round-25 `M92`.

If all of this holds, the previously proved nonzero determinant may be reused;
no new determinant theorem is needed.

A key claim to challenge explicitly:

> `eps + x = kappa` is not a facet of the selected 92-row certificate, because
> the source `(-1,5,1)` whose horizon legality changes there is not selected.

---

## 3. Review R26-B

Apply exactly

\[
J(s,m,n)=(-s,m,n+s),\qquad x\mapsto\delta-x,
\]

with \(\delta=\eta+\chi\).

Check that the mirror chamber becomes

\[
\eta<x<\chi,
\]

\[
R+x>\chi,
\]

\[
\chi-\eta<x-R<\eta,
\]

\[
\sigma+x>2\chi,
\]

\[
\sigma-x<2\eta-\chi,
\]

\[
\varepsilon+x>\kappa=2\eta+\chi,
\qquad
\varepsilon<\varepsilon_{\max}.
\]

Independently reconstruct the mirrored 92 rows and verify

\[
M_{92}^{+}=M_{92}^{-}
\]

after the natural J-paired ordering.

---

## 4. Review the gluing

Check independently that the rational open box

\[
0.014<R<0.016,
\]

\[
0.0293<x<0.0296,
\]

\[
0.041<\sigma<0.043,
\]

\[
0.065<\varepsilon<0.075
\]

lies strictly in both chambers.

This must be a genuine **open overlap**, not only boundary contact.

If so, confirm that

\[
C_{26}^{-}\cup C_{26}^{+}
\]

is an open connected local corridor (each chamber convex and the intersection
open/nonempty).

Do not interpret this as complete coverage of either horizon wall.

---

## 5. Retained verifier

The candidate verifier uses exact atanh-series rational bounds for
`ln 2`, `ln 3`, `ln 5`, rewrites

\[
\delta=\eta+\chi,\quad
e=3\eta+2\chi,\quad
T=14\eta+10\chi,
\]

and proves the whole minus chamber by a four-dimensional polyhedral vertex
certificate:

- 20 feasible closed-chamber vertices;
- all 1628 selected source/slot inequalities checked at every vertex.

Please independently reproduce at least the facet set and a separate
whole-chamber implication check rather than merely trusting those counts.

---

## 6. Scope if GREEN

Permitted wording:

> The promoted Round-25 92-source certificate extends from its original
> rational box to the exact minus polyhedral chamber C26-minus and, by J,
> to a plus chamber. These two local chambers overlap on a nonempty open
> set, so they form one connected local horizon corridor. The same promoted
> M92 determinant certificate applies throughout.

Not permitted:

- full residual-overlap closure;
- full horizon-wall closure;
- a new global R-threshold;
- any P11/R14 consequence.
