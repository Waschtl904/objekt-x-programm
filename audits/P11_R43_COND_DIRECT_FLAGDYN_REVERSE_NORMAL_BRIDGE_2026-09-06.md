# P11 / R43 — direct conditioning-to-FLAGDYN bridge via reverse-normal stretch

**Date:** 2026-09-06  
**Status:** exact/local bridge reduction on top of PR #64; reverse-normal decay and FD23 uniformity remain OPEN  
**Exact parent head:** `7409b9a13028fb8dc0fc44fb210e4783b6feaf7c`

## 0. Purpose and firewall

PR #64 proves, on the resolvent-transported structured scalar conditioning channel, the homogeneous one-sided estimate

\[
\sup_{V>U}
\frac{(\Delta s_{\rm cond}^{U,V}(f))_+}{Q_U(f)}
\le C\frac{\log U}{U}
\tag{BR0}
\]

for every nonzero source datum `f` in the fixed-source graph space and all sufficiently large `U`.

The present note asks exactly how much of this scalar result can be transported into the O1 modulus channel used by `B-FLAGDYN`.

Two facts are proved.

1. BR0 is stronger than a single-vector estimate: because it holds for every source vector, it gives a genuine **one-sided operator cap** for the normalized old-conditioning metric increment.
2. A one-sided cap alone still does **not** control flag motion.  The missing scalar quantity is the positive reverse stretch of the fixed source normal.  An exact vectorwise square-root estimate reduces the conditioning-stage O1 modulus defect to this reverse-normal stretch plus the already proved PR-#64 forward cap.

This note does **not** prove reverse-normal decay, `FD23-UNIF`, the GEO or NEW metric channels, the polar-phase channel, full `B-FLAGDYN`, `B-FLAGTIGHT`, Strong Terminal/C6, Object-X realization, or RH.

All bookings below are local Draft-source bookings only.  No Registry promotion is made.

---

## 1. The exact old-conditioning intermediate metric

Fix one source radius `X` and `X<U<V`.  Let

\[
v_{X,U}(f):=H_U^*E_{X,U}f,
\qquad
B_U=(I+R_U^*R_U)^{-1},
\qquad
\widetilde B_{U,V}:=\iota^*B_V\iota,
\]

where `\iota=E_{U,V}`.

Define the old-conditioning intermediate quadratic form by keeping the terminal-`U` hub geometry fixed and replacing only the Feshbach denominator:

\[
\boxed{
q_{X,\mathrm{cond}}^{U,V}(f)
:=
\mathfrak c_{\Gamma,X}[f]
+
\langle v_{X,U}(f),\widetilde B_{U,V}v_{X,U}(f)\rangle.
}
\tag{BR1}
\]

Let `G_{X,U}` be the frozen terminal-`U` metric on the fixed source graph space and let `G_{X,\mathrm{cond}}^{U,V}` be the positive boundedly invertible metric represented by BR1.  Then

\[
\boxed{
\langle f,
(G_{X,\mathrm{cond}}^{U,V}-G_{X,U})f\rangle
=
\Delta s_{\rm cond}^{U,V}(f).
}
\tag{BR2}
\]

This is exactly the old-conditioning stage of the frozen SW14/SW15 metric split; no GEO or NEW term is included.

### Pullback compatibility across a fixed source pair

Fix `0<R<S<U<V` and let `E=E_{R,S}`.  Zero extension satisfies

\[
E_{S,U}E=E_{R,U}.
\]

Hence the terminal-`U` hub vector in BR1 is literally the same after source zero extension, and the Gamma form has the frozen pullback identity. Therefore

\[
\boxed{
G_{R,\mathrm{cond}}^{U,V}
=E^*G_{S,\mathrm{cond}}^{U,V}E.
}
\tag{BR3}
\]

The same identity already holds for the baseline terminal-`U` metrics:

\[
G_{R,U}=E^*G_{S,U}E.
\tag{BR4}
\]

Define the baseline normalized isometry

\[
W_U:=G_{S,U}^{1/2}E G_{R,U}^{-1/2}
\tag{BR5}
\]

and the channel-relative positive metrics

\[
\boxed{
A_{X,\mathrm{cond}}^{U,V}
:=
G_{X,U}^{-1/2}
G_{X,\mathrm{cond}}^{U,V}
G_{X,U}^{-1/2}.
}
\tag{BR6}
\]

Then BR3--BR5 give the exact O1 compression relation

\[
\boxed{
W_U^*A_{S,\mathrm{cond}}^{U,V}W_U
=A_{R,\mathrm{cond}}^{U,V}.
}
\tag{BR7}
\]

Thus the old-conditioning stage by itself is a legitimate positive two-source metric comparison to which the O1 square-root/modulus algebra applies.

---

## 2. PR #64 implies a one-sided normalized operator cap

Put

\[
\mathbf H_{X,\mathrm{cond}}^{U,V}
:=
A_{X,\mathrm{cond}}^{U,V}-I
=
G_{X,U}^{-1/2}
(G_{X,\mathrm{cond}}^{U,V}-G_{X,U})
G_{X,U}^{-1/2}.
\tag{BR8}
\]

PR #64 gives, for every nonzero source vector and all sufficiently large `U`, uniformly in `V>U`,

\[
\frac{(\langle f,
(G_{X,\mathrm{cond}}^{U,V}-G_{X,U})f\rangle)_+}
{\langle f,G_{X,U}f\rangle}
\le
\varepsilon_U,
\qquad
\varepsilon_U:=C_X\frac{\log U}{U}.
\tag{BR9}
\]

For every real scalar `a`, `a\le a_+`.  Hence BR9 implies the quadratic-form inequality

\[
G_{X,\mathrm{cond}}^{U,V}-G_{X,U}
\preceq
\varepsilon_U G_{X,U}.
\tag{BR10}
\]

After congruence,

\[
\boxed{
\mathbf H_{X,\mathrm{cond}}^{U,V}
\preceq
\varepsilon_U I,
\qquad
A_{X,\mathrm{cond}}^{U,V}
\preceq
(1+\varepsilon_U)I.
}
\tag{BR11}
\]

This is a genuine one-sided operator statement.  It does **not** give a lower bound for `\mathbf H_{X,\mathrm{cond}}`, an operator-norm bound, or a spectral-width estimate.

### Local draft booking

```text
R43-COND-RELATIVE-ONE-SIDED-OPERATOR-CAP ✓[M]
```

Scope: the old-conditioning intermediate metric only, conditional on the exact PR-#64 parent result.

---

## 3. Abstract one-sided-cap modulus lemma

Let `W:H_R\to H_S` be an isometry and put `P=WW^*`.  Let `A_S` be bounded positive and invertible with

\[
0<A_S\preceq cI,
\qquad c\ge1,
\tag{BR12}
\]

and define

\[
A_R:=W^*A_SW.
\tag{BR13}
\]

Set

\[
B:=W^*A_S^{1/2}W,
\qquad
L:=(I-P)A_S^{1/2}W,
\tag{BR14}
\]

\[
J:=A_R^{1/2}-B\succeq0,
\qquad
M:=A_S^{1/2}W-WA_R^{1/2}=L-WJ.
\tag{BR15}
\]

The ranges of `L` and `WJ` are orthogonal.  The frozen O1 identity gives

\[
A_R=B^2+L^*L.
\tag{BR16}
\]

### Lemma 1 — vectorwise modulus control from a one-sided cap

For every `y\in H_R`,

\[
\boxed{
\|My\|^2
\le
\frac32
\left(
 c\|y\|^2-
 \langle y,A_Ry\rangle
\right).
}
\tag{BR17}
\]

### Proof

Write

\[
n:=\|y\|^2,
\qquad
a:=\langle y,A_Ry\rangle.
\]

The scalar inequality `\sqrt t\ge t/\sqrt c` on `[0,c]` gives by functional calculus

\[
A_S^{1/2}\succeq c^{-1/2}A_S.
\]

Compressing by `W`,

\[
B\succeq c^{-1/2}A_R.
\tag{BR18}
\]

Therefore

\[
\langle y,By\rangle\ge a/\sqrt c.
\]

By Cauchy--Schwarz,

\[
\|By\|^2
\ge
\frac{|\langle y,By\rangle|^2}{\|y\|^2}
\ge
\frac{a^2}{cn}
\tag{BR19}
\]

when `y\ne0` (the zero vector is trivial).  Using BR16,

\[
\|Ly\|^2
=a-\|By\|^2
\le
a-\frac{a^2}{cn}
\le cn-a.
\tag{BR20}
\]

For `J`, positivity gives `0\preceq J\preceq A_R^{1/2}` and therefore `\|J\|\le\sqrt c`.  Moreover,

\[
\begin{aligned}
\langle y,Jy\rangle
&=
\langle y,A_R^{1/2}y\rangle-\langle y,By\rangle\\
&\le
\sqrt{an}-\frac a{\sqrt c}.
\end{aligned}
\tag{BR21}
\]

Hence

\[
\|Jy\|^2
\le
\|J\|\langle y,Jy\rangle
\le
\sqrt{can}-a.
\tag{BR22}
\]

For `0\le a\le cn`, the elementary inequality

\[
\sqrt{can}-a
\le
\frac{cn-a}{2}
\tag{BR23}
\]

is equivalent, after division by `cn` and setting `s=\sqrt{a/(cn)}`, to `-(s-1)^2\le0`.

Finally `Ly\perp WJy`, so

\[
\|My\|^2
=
\|Ly\|^2+
\|Jy\|^2
\le
\frac32(cn-a),
\]

proving BR17. \(\square\)

### Local draft booking

```text
R43-COND-ONE-SIDED-CAP-MODULUS-LEMMA ✓[M]
```

No terminal asymptotics are contained in this abstract lemma.

---

## 4. Exact reverse-normal reduction for the conditioning modulus channel

Apply Lemma 1 to

\[
A_S=A_{S,\mathrm{cond}}^{U,V},
\qquad
A_R=A_{R,\mathrm{cond}}^{U,V},
\qquad
c=1+\varepsilon_U,
\tag{BR24}
\]

using BR7 and BR11.

Let

\[
C_{X,\mathrm{cond}}^{U,V}
:=(G_{X,\mathrm{cond}}^{U,V})^{1/2}G_{X,U}^{-1/2}
=\mathcal U_X A_X^{1/2}
\tag{BR25}
\]

be the corresponding polar decomposition.  For the fixed source normal `\varepsilon_R`, put

\[
u_{R;U,V}:=\mathcal U_R^*\varepsilon_R,
\qquad \|u_{R;U,V}\|=1.
\tag{BR26}
\]

The unprojected conditioning-stage O1 modulus vector is

\[
z_{\mathrm{cond}}(U,V)
:=
\mathcal U_S M A_R^{-1/2}\mathcal U_R^*\varepsilon_R.
\tag{BR27}
\]

Projection and the unitary `\mathcal U_S` can only decrease norm, so the conditioning contribution to FD17 satisfies

\[
\mathfrak d^{\mathrm{cond}}_{m,\mathrm{mod}}(U,V)
\le
\|z_{\mathrm{cond}}(U,V)\|.
\tag{BR28}
\]

Apply BR17 with

\[
y=A_R^{-1/2}u_{R;U,V}.
\]

Then

\[
\langle y,A_Ry\rangle=1,
\qquad
\|y\|^2
=
\langle u_{R;U,V},A_R^{-1}u_{R;U,V}\rangle.
\]

Define the positive reverse-normal stretch

\[
\boxed{
\rho^{\mathrm{rev}}_{R;U,V}
:=
\left(
\langle u_{R;U,V},A_R^{-1}u_{R;U,V}\rangle-1
\right)_+.
}
\tag{BR29}
\]

Equivalently,

\[
\rho^{\mathrm{rev}}_{R;U,V}
=
\left(
\|(C_{R,\mathrm{cond}}^{U,V})^{-1}\varepsilon_R\|^2-1
\right)_+.
\tag{BR30}
\]

Since

\[
(1+\varepsilon_U)t-1
=
\varepsilon_U+(1+\varepsilon_U)(t-1)
\le
\varepsilon_U+(1+\varepsilon_U)(t-1)_+,
\]

BR17 gives the central bridge estimate

\[
\boxed{
\bigl(\mathfrak d^{\mathrm{cond}}_{m,\mathrm{mod}}(U,V)\bigr)^2
\le
\|z_{\mathrm{cond}}(U,V)\|^2
\le
\frac32
\left[
\varepsilon_U
+(1+\varepsilon_U)
\rho^{\mathrm{rev}}_{R;U,V}
\right].
}
\tag{BR31}
\]

This estimate is **vectorwise** and contains no global spectral width and no pairwise Sylvester coercivity denominator.

### Local draft booking

```text
R43-COND-REVERSE-NORMAL-MODULUS-BRIDGE ✓[M]
```

The booking is the exact implication BR31 only.  Decay of `rho_rev` is not proved.

---

## 5. Why the PR-#64 forward estimate alone cannot close FLAGDYN

The reverse-normal term in BR31 is not a cosmetic artifact.  A two-dimensional exact countermodel shows that a zero positive forward variation can coexist with nonzero modulus rotation.

Let

\[
H_S=\mathbb C^2,
\qquad
H_R=\mathbb C,
\qquad
W(1)=e_1,
\]

and put

\[
v=\frac{e_1+e_2}{\sqrt2},
\qquad
A_S=I-\alpha vv^*,
\qquad
0<\alpha<1.
\tag{BR32}
\]

Then

\[
A_S-I=-\alpha vv^*\preceq0.
\]

Thus the positive part of every forward scalar metric increment is exactly zero: the strongest possible analogue of BR9 holds with `\varepsilon=0`.

Compression gives

\[
A_R=W^*A_SW=1-\frac\alpha2.
\tag{BR33}
\]

Since `v` is the `1-\alpha` eigenvector of `A_S`, one obtains

\[
A_S^{1/2}e_1
=
\frac{1+\sqrt{1-\alpha}}2e_1
+
\frac{\sqrt{1-\alpha}-1}{2}e_2.
\tag{BR34}
\]

Therefore the normalized modulus update

\[
A_S^{1/2}W A_R^{-1/2}-W
\]

has nonzero `e_2` component

\[
\boxed{
\frac{\sqrt{1-\alpha}-1}
{2\sqrt{1-\alpha/2}}
e0.
}
\tag{BR35}
\]

At the same time

\[
A_R^{-1}-1
=
\frac{\alpha}{2-\alpha}>0,
\tag{BR36}
\]

so the reverse-normal term in BR31 detects exactly the obstruction missed by the one-sided forward cap.

### Local negative booking

```text
R43-COND-POSITIVE-VARIATION-ALONE-FLAGDYN-NOGO ✓[M]_neg
```

Scope: the implication “one-sided/positive forward scalar variation alone controls the modulus channel” is false, even in dimension two.  This is not a no-go for the reverse-normal route, B-FLAGDYN, or Strong Terminal.

---

## 6. Geometric-chain summability conditional on reverse-normal decay

Take the geometric chain

\[
U_k=U_0 2^k.
\tag{BR37}
\]

PR #64 supplies

\[
\varepsilon_{U_k}
\le C\frac{\log U_k}{U_k}.
\tag{BR38}
\]

Introduce the open reverse-normal target

\[
\boxed{
\sup_{V\in[U_k,U_{k+1}]}
\rho^{\mathrm{rev}}_{R;U_k,V}
\le
C_{\rm rev}\frac{\log U_k}{U_k}.
}
\tag{BR39?}
\]

If BR39 holds, BR31 gives a summable unprojected majorant

\[
\boxed{
\sup_{V\in[U_k,U_{k+1}]}
\|z_{\mathrm{cond}}(U_k,V)\|
\le
C\sqrt{\frac{\log U_k}{U_k}}
=:b_k,
}
\tag{BR40}
\]

and

\[
\boxed{
\sum_{k\ge0}b_k<\infty.
}
\tag{BR41}
\]

Indeed `U_k=U_0 2^k` makes `b_k=O(\sqrt{k/2^k})`.

This eliminates the old need for a global spectral-width majorant and pairwise coercivity factors for the **conditioning-stage vectorwise modulus channel**.

However, FD23 requires more than a summable unprojected majorant.  For each fixed interval one still needs projected uniformity:

\[
\boxed{
\Delta^{\mathrm{cond}}_{m,k}
:=
\sup_{V\in[U_k,U_{k+1}]}
\|P_m z_{\mathrm{cond}}(U_k,V)\|
\longrightarrow0
\quad(m\to\infty).
}
\tag{BR42?}
\]

This is the conditioning-stage form of the existing `FD23-UNIF` gate.  It would follow, for example, from relative compactness of the family

\[
\{z_{\mathrm{cond}}(U_k,V):V\in[U_k,U_{k+1}]\}
\]

for each fixed `k`, but no such continuity/compactness theorem is imported here.

If BR39 and BR42 both hold, dominated convergence on the counting measure gives

\[
\boxed{
\lim_{m\to\infty}
\sum_{k\ge0}
\Delta^{\mathrm{cond}}_{m,k}=0.
}
\tag{BR43}
\]

Thus the conditioning contribution to the FD23 modulus sum is closed under exactly these two additional hypotheses.

### Local conditional booking

```text
R43-COND-REVERSE-NORMAL-PLUS-FD23UNIF-IMPLIES-COND-FLAGMOD-CONTRIBUTION ✓[M]
```

Meaning: the implication `(BR39 + BR42) => BR43` is proved.  Neither premise is booked as proved.

---

## 7. Resulting front

Before this note, the direct bridge was schematically

```text
PR64 relative scalar COND summability
        |
        ?
        v
B-FLAGDYN / FD23
```

The exact analysis now factors the missing arrow as

```text
PR64 forward positive variation
        |
        v
one-sided normalized operator cap          ✓[M] (local Draft)
        |
        +-------------------------------+
        |                               |
        v                               v
reverse-normal stretch decay ?[O]       FD23-UNIF ?[O]
        |                               |
        +---------------+---------------+
                        |
                        v
conditioning contribution to FD23 modulus sum
```

Roadmap labels:

```text
ROADMAP-COND-REVERSE-NORMAL-STRETCH-DECAY
  type: research-subquestion
  math_status: null
  research_status: open

ROADMAP-COND-FD23-UNIF
  type: research-subquestion
  math_status: null
  research_status: open
```

The next preferred calculation is BR39: estimate the reverse metric stretch of the single fixed source normal.  This is a scalar quantity and is strictly smaller than controlling the full negative spectral width of the conditioning increment.

---

## 8. Firewalls

Still OPEN:

```text
ROADMAP-COND-REVERSE-NORMAL-STRETCH-DECAY
FD23-UNIF / ROADMAP-COND-FD23-UNIF
B-METINC-GEO
B-METINC-NEW
full B-FLAGMOD / B-FLAGDYN
B-FLAGPHASE
B-FLAGTIGHT
B-SIGN / B-ORIENT
Strong Terminal / C6
genuine X candidate / Object-X realization
RH
```

The stronger operatorwide nodes also remain OPEN:

```text
B-METINC-COND
B-METINC-WIDTH
R43-MI-LOEWNER
```

No claim is made that BR31 controls the GEO or NEW channels, or the polar phase.  No implication from this conditioning-stage bridge to Strong Terminal is booked.

Keep this mathematics Draft.  Do not merge or promote without a fresh destructive review of the exact resulting head.
