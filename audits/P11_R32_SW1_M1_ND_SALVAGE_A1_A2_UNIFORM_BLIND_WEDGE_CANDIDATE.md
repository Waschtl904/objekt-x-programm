# P11/R32 — SW1 M1-ND SALVAGE-A1/A2 Uniform Blind Wedge Candidate

> **Stand:** 1. September 2026  
> **Branch:** \`research/sw1-m1-nd-salvage-phase-diagram\`  
> **Status:** AI-GREEN candidate + exact finite/algebraic certificate for the new geometry; **no promotion yet**.  
> **Certificate:** \`scripts/certify_sw1_m1_nd_salvage_a1_a2_uniform_blind_wedge.py\`.

---

## 1. Statement and scope

Set

\[
h:=d-3\Delta.
\]

Using the physical constants,

\[
\boxed{
h=\frac{T-10\Delta}{4}
=\frac{8\log2-5\log3}{2}>0
}
\tag{A12.1}
\]

because \(2^8>3^5\).

Define

\[
\boxed{
\varepsilon_c:=\frac h2=\frac{T-10\Delta}{8}.
}
\tag{A12.2}
\]

Moreover

\[
\boxed{
\varepsilon_c<\frac{\Delta}{2}
}
\tag{A12.3}
\]

because this is equivalent to \(11\log2<7\log3\), hence to
\(2^{11}<3^7\).

Candidate theorem:

> For every
> \[
> 0<\varepsilon<\varepsilon_c,\qquad
> 0<R<\varepsilon,\qquad
> 0<\sigma<R,
> \]
> the current effective SW1 operator satisfies
> \[
> \boxed{\ker\mathscr N_R\ne\{0\}.}
> \tag{A12.4}
> \]

Since \(\varepsilon<\Delta/2\) and \(R<\varepsilon\), one has
\(R+\varepsilon<2\varepsilon<\Delta\), so the whole wedge lies in the
lower SW1 chamber where A7 applies.

---

## 2. The 24-gap Horizon barrier

For

\[
s\in\{0,a\},\qquad k=0,\ldots,5,\qquad j\in\{0,1\},
\]

define

\[
F_{s,k,j}
=
\left(
s+k\Delta+jh+\varepsilon,\,
s+k\Delta+(j+1)h-\varepsilon
\right).
\tag{A12.5}
\]

Because \(0<\varepsilon<h/2\), every gap has width

\[
h-2\varepsilon>0.
\]

Let

\[
\boxed{
F_\varepsilon=\bigcup_{s,k,j}F_{s,k,j}.
}
\tag{A12.6}
\]

The exact certificate proves uniformly on the full open
\(0<\varepsilon<\varepsilon_c\) interval:

- all 24 gaps are nonempty;
- they are strictly ordered and pairwise disjoint;
- they lie in \((0,T)\).

Set

\[
K_\varepsilon:=(0,T+\varepsilon)\setminus F_\varepsilon
\]

up to the finite boundary set.

---

## 3. Maximal KNF sampling lies in \(K_\varepsilon\)

Define the boundary-majorant sampling set

\[
U_\varepsilon^{\max}
=
(a-\varepsilon,a+\varepsilon)
\cup
(b-\varepsilon,b+\varepsilon)
\cup
(T-\varepsilon,T+\varepsilon).
\tag{A12.7}
\]

For every actual \(0<R<\varepsilon\),

\[
U_R\subset U_\varepsilon^{\max}.
\tag{A12.8}
\]

The certificate proves

\[
\boxed{
U_\varepsilon^{\max}\cap F_\varepsilon=\varnothing.
}
\tag{A12.9}
\]

Hence \(U_R\subset K_\varepsilon\).

---

## 4. FREE invariance

Use exactly the nine lower-chamber A7 maps

\[
\tau_{\pm a},\quad
\tau_{\pm T},\quad
r_a,\ r_T,\ r_{3a},\ r_{4a},\ r_{2b}
\tag{A12.10}
\]

with the exact A7.1–A7.9 domains.

For every forbidden gap and every nonempty map/domain intersection, the
certificate checks that its image is covered by \(F_\varepsilon\).

There are exactly

\[
\boxed{70}
\]

such nonempty pieces.

The script also checks the inverse graphing structure:

- \(+a\leftrightarrow-a\);
- \(+T\leftrightarrow-T\);
- \(r_T,r_{3a},r_{4a},r_{2b}\) are involutions on invariant domains;
- \(r_a\) swaps its two domain components.

Thus \(F_\varepsilon\) is invariant in both graph directions. Therefore,
away from the finite boundary set,

\[
\boxed{
K_\varepsilon
\text{ is invariant under the full A7 equivalence relation.}
}
\tag{A12.11}
\]

Consequently

\[
\boxed{
V_{\varepsilon,R}
=
\operatorname{Sat}_{\mathcal E_\varepsilon}(U_R)
\subset K_\varepsilon.
}
\tag{A12.12}
\]

No component-cardinality or Mass-Transport estimate is used.

---

## 5. Fourteen uniform Annulus gaps

Let

\[
\mathcal C=
\{
0,\Delta,2\Delta,3\Delta,
d,d+\Delta,d+2\Delta,
a,a+\Delta,a+2\Delta,a+3\Delta,
b,b+\Delta,b+2\Delta
\}.
\tag{A12.13}
\]

For \(c\in\mathcal C\), define

\[
B_{\varepsilon,c}
=
(c+\varepsilon,\ c+h-\varepsilon)
\tag{A12.14}
\]

and

\[
\boxed{
B_\varepsilon
=
\bigcup_{c\in\mathcal C}B_{\varepsilon,c}.
}
\tag{A12.15}
\]

The certificate proves uniformly:

1. all 14 intervals are nonempty;
2. they are strictly ordered and pairwise disjoint;
3. they lie in \((\varepsilon,T)\).

The complement \(K_\varepsilon\) consists of exactly 25 interval cells.

For each cell, the certificate evaluates the complete physical positive Hub
source list

\[
|x-a|,\ x+a,\ |x-b|,\ x+b,\ |x-T|,\ x+T.
\tag{A12.16}
\]

The absolute-value maps are split at \(a,b,T\). This yields exactly

\[
\boxed{153}
\]

nonempty image pieces, and every one is proved disjoint from every component
of \(B_\varepsilon\). Hence

\[
\boxed{
H(K_\varepsilon)\cap B_\varepsilon=\varnothing.
}
\tag{A12.17}
\]

By A12.12,

\[
H(V_{\varepsilon,R})\cap B_\varepsilon=\varnothing.
\tag{A12.18}
\]

Because \(R<\varepsilon\) and \(S=T+\sigma>T\),

\[
B_\varepsilon\subset(\varepsilon,T)\subset(R,S).
\tag{A12.19}
\]

So \(B_\varepsilon\) is a genuine positive Annulus blind set for every
admissible \(R,\sigma\) in the wedge.

---

## 6. Uniform blind measure

Each blind interval has width \(h-2\varepsilon\), hence

\[
\begin{aligned}
|B_\varepsilon|
&=14(h-2\varepsilon)\\
&=
\boxed{
\frac72(T-10\Delta-8\varepsilon)
}.
\end{aligned}
\tag{A12.20}
\]

For \(0<\varepsilon<\varepsilon_c\), this is strictly positive.

Crucially,

\[
\boxed{
|B_\varepsilon|
\text{ has no }R\text{-decay.}
}
\tag{A12.21}
\]

---

## 7. Kernel handoff

Choose

\[
0\ne w_+\in L^2(B_\varepsilon)
\]

and let \(0\ne g\in\mathscr B_W\) be its IMG0 basislift reconstruction.

The parameter-uniform analytic handoff is recorded separately in

\`audits/P11_R32_SW1_M1_ND_SALVAGE_A1_A2_ANALYTIC_HANDOFF_CANDIDATE.md\`.

It gives

\[
\Pi_{V_{\varepsilon,R}}\mathcal H_Rg=0,
\]

and for

\[
f=-\mathscr T_B^{-1}\mathcal H_Rg
\]

one obtains

\[
\Pi_{V_{\varepsilon,R}}f=0.
\]

Since \(U_R\subset V_{\varepsilon,R}\), all six KNF sample values vanish, so

\[
f\in\mathscr B_K.
\]

Therefore

\[
\mathscr N_R(f,g)=0
\]

with \(g\ne0\). Hence the candidate conclusion is A12.4.

---

## 8. Interpretation

If A12.4 survives adversarial review, the current finite-level geometry is
degenerate on the open wedge

\[
\boxed{
0<\varepsilon<
\frac{T-10\Delta}{8},
\quad
0<R<\varepsilon,
\quad
0<\sigma<R.
}
\tag{A12.22}
\]

This is qualitatively stronger than the previously promoted single witness:

- old proof: \(O(R)\) visibility upper bound plus Mass Transport;
- new proof: explicit graph-invariant Horizon barrier plus an
  \(R\)-independent positive Annulus blind set.

---

## 9. Scope firewall

Not claimed yet:

- degeneracy for \(\varepsilon\ge\varepsilon_c\);
- that \(\varepsilon_c\) is the exact global phase boundary;
- injectivity anywhere on the visible side;
- any upper-chamber statement;
- a separate promotion of \(\ker\Gamma_I\ne0\);
- Object-X failure;
- any RH conclusion.

The numerical phase-diagram probe is discovery evidence only.

---

## 10. Promotion gate

Before any \(\checkmark[M]_{\rm neg}\) booking for A12.22:

1. verify the exact sign engine and \(\varepsilon_c<\Delta/2\);
2. verify that the 70 FREE pieces exhaust all A7 gap/domain intersections;
3. verify that forward+inverse \(F_\varepsilon\)-invariance implies
   \(K_\varepsilon\)-invariance a.e.;
4. verify that the 153 Hub pieces exhaust the physical six-map list;
5. verify that the imported reducing/Hub/KNF handoff is parameter-uniform.

Until then: **candidate only**.
