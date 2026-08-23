# P12 Round 24 — independent adversarial review packet

**Repo basis to compare against:** `Waschtl904/objekt-x-programm`,
`main@c5f91fe07d4c1fac45ec83d769ddf13d8d1f6f41`.

This review concerns only P12 local raw-operator geometry below \(\rho\).
P11 is FROZEN and R14 is unchanged.

Please review the attached audit and verifier independently from the committed
Round-23 raw operator.

Return separate verdicts:

- `R24-A: GREEN / PARTIAL / FAIL`
- `R24-B: GREEN / PARTIAL / FAIL`
- `HORIZON ONE-STEP DIAGNOSTIC: GREEN / PARTIAL / FAIL`

No global \(R\)-threshold is under review.

---

## A. R24-A — enlarged fixed-42 pattern chamber

Starting from the committed 42 Round-23 sources, independently reconstruct all
six raw slots per source from

\[
Lh(u)=p[h(u-a)-h(u+a)]
+r[h(u-b)-h(u+b)]
+q[h(u-T)-h(u+T)].
\]

Check the claim that the same exact \(42\times42\) matrix remains valid
throughout

\[
0<R<\rho,
\]

\[
R<x<\delta-R,
\]

\[
\chi-R<x<\eta+R,
\]

\[
\max\{x,\delta-x\}<\sigma<
\min\{\kappa-x,x+\eta\},
\]

\[
\max\{\kappa-x,x+\eta\}<\varepsilon<\varepsilon_{\max}.
\]

In particular:

1. verify that \(R=\omega\) is not a source/support/horizon event for the
   selected 42-row block;
2. verify that \(x=\eta\) and \(x=\chi\) only toggle the unused lower-horizon
   source pairs
   \[
   (1,-1,2)\leftrightarrow(-1,1,-2),
   \]
   \[
   (-1,-1,3)\leftrightarrow(1,1,-3),
   \]
   and do not change any selected Round-23 row;
3. verify exact \(J(s,m,n)=(-s,m,n+s)\) closure;
4. verify that a point with \(R<\omega\), e.g.
   \[
   (R,x,\sigma,\varepsilon)
   =(0.01,\delta/2,0.04,0.07),
   \]
   reconstructs exactly the committed \(M_{42}\);
5. independently audit that no hidden raw-slot wall is omitted from the stated
   C42 chamber.

Do **not** interpret
\[
(\chi-\eta)/2
\]
as a canonical/operator threshold. It is only the feasibility floor of this
fixed source-pattern chamber.

If GREEN, R24-A may be booked only as a local scope extension of the already
proved Round-23 \(M_{42}\) kill.

---

## B. R24-B — paired support-wall / 44x44 extension

Define

\[
U_-=T+\kappa-x\leftrightarrow(-1,5,1),
\qquad
U_+=T+x+\eta\leftrightarrow(1,5,0).
\]

Check independently that the walls

\[
\sigma+x=\kappa,\qquad \sigma-x=\eta
\]

make \(U_-\) and \(U_+\), respectively, enter the support and add one new
column each.

Now add

\[
V_-=T+2\delta-x\leftrightarrow(-1,4,4),
\]

\[
V_+=T+x+\delta\leftrightarrow(1,4,3).
\]

Independently reconstruct their raw rows. In the claimed chamber they should be

\[
\{(-1,2,3):p,\ (-1,1,2):r,\ (-1,0,2):q\}
\]

and

\[
\{(1,2,2):p,\ (1,1,1):r,\ (1,0,1):q\},
\]

with no new visibility variables.

Review the chamber

\[
R<x<\delta-R,\qquad
\chi-R<x<\eta+R,
\]

\[
\max\{\kappa-x,x+\eta\}
<
\sigma
<
\min\{2\delta-x,x+\delta\},
\]

\[
\max\{2\delta-x,x+\delta\}
<
\varepsilon
<
\varepsilon_{\max}.
\]

Required checks:

1. all 44 sources are horizon-legal;
2. exactly 44 variables are live;
3. all 264 raw slots and odd-reflection signs;
4. exact \(J\)-closure and 22+22 block form;
5. independently reproduce
   \[
   \det M_{44}
   =
   -p^{18}r^6(p-q)(p+q)G_-G_+;
   \]
6. normalize using
   \[
   \beta=q/p,\qquad v=(r/p)^2
   \]
   and verify that the two degree-9 factors form a parity pair under
   \(\beta\mapsto-\beta\);
7. independently certify that both normalized factors are nonzero for the
   actual P12 weights. The retained verifier obtains strict positive
   intervals near
   \[
   0.03770850382320942
   \quad\text{and}\quad
   0.6120433841588828.
   \]

If GREEN, R24-B is a **local** support-wall theorem only.

---

## C. Horizon-wall one-step diagnostic

At

\[
\varepsilon+x=\kappa
\]

the source \((-1,5,1)\) leaves the horizon; at

\[
\varepsilon=x+\eta
\]

the source \((1,5,0)\) leaves.

Verify that each side is exactly a 41-row / 42-variable system obtained by
deleting one row from the invertible Round-23 matrix.

Then independently check the finite one-step replacement enumeration:

Any nonzero source row using only old Round-23 visibility variables must have
its source center one canonical shift \(a,b,T\) away from \(\pm\) one of the
old variables. After deduplication this gives 142 candidate source centers.

The verifier claims that on either horizon-loss side **none** of those
horizon-legal candidates produces a nonzero row contained entirely in the old
42-variable set.

This is only a one-step construction obstruction. It must NOT be promoted to
a global no-go theorem.

---

## Required final wording if GREEN

For R24-A:

> The original conditions \(R>\omega\) and \(\eta<x<\chi\) are not intrinsic
> walls of the selected Round-23 42-row block. The stated J-symmetric C42
> chamber reconstructs the same exact matrix, including points with
> \(R<\omega\).

For R24-B:

> The paired support walls admit a next-shell closure using
> \(V_-=T+2\delta-x\) and \(V_+=T+x+\delta\); the resulting 44x44 raw matrix is
> J-symmetric and rigorously invertible in the stated local chamber.

No Object-X or RH consequence is under review.
