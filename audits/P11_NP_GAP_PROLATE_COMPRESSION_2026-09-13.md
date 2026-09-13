# P11 Audit — NP-GAP as a rank-2-shorted prolate Birman--Schwinger problem

**Datum:** 13. September 2026  
**Basisbranch:** `research/critical-half-green-tree-bridge-2026-09-13`  
**Rolle:** theorem-level Strukturreduktion plus klar getrennte numerische Diagnostik.  
**Registry:** unverändert.  
**Nonclaim:** kein globaler NP-GAP-/Object-X-/RH-Beweis.

---

## 0. Kurzurteil

Die aktuelle Critical-half-/Scattering-Front kann auf jedem festen Fenster als **kompaktes Prolate-/Birman--Schwinger-Problem** formuliert werden.

Die zwei NULLPOL-Bedingungen werden dabei nicht nur als Nebenbedingungen behandelt, sondern exakt als Rang-2-Shorting des Paley--Wiener-Reproduktionskerns.

Fuer das Laborfenster `a=1/2` zeigt die numerische Diagnostik, dass diese Rang-2-Kompression die Spur des gesamten negativen Multiplikatorblocks sehr stark reduziert (ungefaehr von `2.775` auf `0.450`). Das ist **keine Zertifizierung**, aber ein starker Hinweis, dass die richtige positive Architektur eine komprimierte Prolate-/Hardy-Geometrie und keine punktweise Faktorisierung ist.

Status:

```text
centered-gap monotonicity in a                         ✓[M]
exact translation-orbit chain bound                    ✓[M]
NULLPOL reproducing-kernel rank-2 shorting              ✓[M]
negative multiplier block trace class                   ✓[M]
explicit trace formula                                  ✓[M]
prolate/Birman--Schwinger reduction                     ✓[M]_part
finite-mode / trace diagnostics at a=1/2                diagnostic only
sharp NP-GAP all a                                      ?[O]
Object X / RH                                           ?[O]
```

---

## 1. Centered gap is monotone under window exhaustion

Let

```math
\mathscr D_{NP,a}
= C_c^\infty(-a,a)\cap\ker M(0)\cap\ker M(1).
```

Define the centered Rayleigh infimum

```math
\boxed{
g(a)
:=
\inf_{0\ne v\in\mathscr D_{NP,a}}
\frac{Q_W(v)}{\|v\|_2^2}.
}
```

If `0<a<b`, then

```math
\mathscr D_{NP,a}\subset\mathscr D_{NP,b}.
```

Moreover the centered COMMON-JUMP form is cutoff-gauge invariant on old vectors:

```math
Q_{W,b}(v)=Q_{W,a}(v)
\qquad(v\in\mathscr D_{NP,a}).
```

Therefore

```math
\boxed{
g(b)\le g(a).}
```

Thus new prime thresholds do **not** raise the centered gap. They only rewrite the same global Weil form on a larger support class.

Equivalently, if

```math
\lambda_{NP}(a)
=\inf\frac{\|X_av\|^2}{\|v\|^2},
```

then

```math
\boxed{
g(a)=\lambda_{NP}(a)-\Gamma_a}
```

is the invariant monotone quantity.

Strategic consequence: the all-window problem is an exhaustion/direct-limit problem, not an induction in which each newly entering prime repairs the previous radius.

---

## 2. Exact orbit-chain lower bound for one translation jump

Let `I=(-a,a)` have length `L=2a`, let `P_I` be multiplication by `1_I`, and let

```math
A_t:=P_I(T_t+T_{-t})P_I.
```

For fixed `t>0`, decompose `I` into orbits modulo `t`. Every orbit meets `I` in a finite chain. The maximal chain length is

```math
N(t)=\left\lfloor\frac{L}{t}\right\rfloor+1
\qquad(0<t\le L),
```

while for `t>L` every chain has length one.

On a chain of length `N`, `A_t` is the adjacency matrix of the path graph `P_N`, whose largest eigenvalue is

```math
2\cos\frac{\pi}{N+1}.
```

Hence

```math
\boxed{
\|A_t\|
=2\cos\frac{\pi}{N(t)+1}
\qquad(0<t\le L),
}
```

and `A_t=0` for `t>L`.

Since

```math
K_t^*K_t=2I-A_t,
```

we obtain the exact support-only bound

```math
\boxed{
\|K_tv\|_2^2
\ge
c_L(t)\|v\|_2^2,
}
```

with

```math
c_L(t)=
2-2\cos\frac{\pi}{N(t)+1}
\quad(0<t\le L),
```

and `c_L(t)=2` for `t>L`.

Checks:

- if `t>L/2`, then `N=2` and `c_L(t)=1`;
- if `t>L`, then `c_L(t)=2`;
- as `t\downarrow0`, `c_L(t)\sim \pi^2t^2/L^2`.

This gives an exact discrete-orbit form of the finite-window nonlocal Poincare mechanism. At `a=1/2`, integrating this bound against `h(t)dt` is rigorous in principle but numerically weaker than the previously derived Schur/resolvent bound; it is therefore retained as a structural lemma, not as the main positivity route.

---

## 3. Paley--Wiener formulation and the finite-window multiplier

Use the unitary Fourier transform. Let

```math
PW_a=\mathcal F L^2(-a,a).
```

On NULLPOL define

```math
\mathcal N_a
:=
\{F\in PW_a:F(i/2)=F(-i/2)=0\}.
```

By the Critical-half range theorem,

```math
\boxed{
\mathcal N_a=(z^2+1/4)PW_a
}
```

on the smooth test class.

For the canonical finite-window COMMON-JUMP representation the centered multiplier is

```math
\boxed{
\tau_a(z)
=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)-\log\pi
-2\sum_{\log n\le2a}
\frac{\Lambda(n)}{\sqrt n}\cos(z\log n).
}
```

Then

```math
\boxed{
Q_W(v)=\int_{\mathbb R}|F(z)|^2\tau_a(z)\,dz,
\qquad F=\widehat v\in\mathcal N_a.
}
```

The multiplier satisfies

```math
\tau_a(z)=\log\frac{|z|}{2\pi}+O_a(1)
\qquad(|z|\to\infty),
```

so its negative set is compact.

---

## 4. Exact NULLPOL reproducing-kernel shorting

The Paley--Wiener reproducing kernel is

```math
\boxed{
K_a(z,w)
=
\frac{\sin(a(z-\overline w))}
{\pi(z-\overline w)}.
}
```

Let

```math
\lambda_+=i/2,
\qquad
\lambda_-=-i/2.
```

Define the two kernel vectors

```math
k_\pm(z)=K_a(z,\lambda_\pm)
```

and the `2x2` Gram matrix

```math
G_{\sigma\tau}=K_a(\lambda_\sigma,\lambda_\tau).
```

Explicitly,

```math
\boxed{
G
=\frac1\pi
\begin{pmatrix}
\sinh a & a\\
a & \sinh a
\end{pmatrix}.
}
```

Since `sinh a>a` for `a>0`, `G` is strictly positive.

The orthogonal projection from `PW_a` onto the codimension-2 NULLPOL space therefore has reproducing kernel

```math
\boxed{
K_{NP,a}(z,w)
=
K_a(z,w)
-k(z)^*G^{-1}k(w),
}
```

where

```math
k(z)=(k_+(z),k_-(z))^T.
```

Thus NULLPOL is an **exact rank-2 shorting** of Paley--Wiener geometry.

This is the reproducing-kernel counterpart of

```math
\mathscr D_{NP,a}=L_{1/2}C_c^\infty(-a,a).
```

---

## 5. The entire negative danger is a compact trace-class block

Split

```math
\tau_a=\tau_{a,+}-\tau_{a,-},
\qquad
\tau_{a,\pm}\ge0.
```

On `\mathcal N_a` set

```math
A_{a,-}
:=P_{\mathcal N_a}M_{\tau_{a,-}}P_{\mathcal N_a}.
```

Because `tau_{a,-}` has compact support and `K_{NP,a}(z,z)` is locally bounded, `A_{a,-}` is positive trace class. Its trace is exactly

```math
\boxed{
\operatorname{tr}A_{a,-}
=
\int_{\mathbb R}
\tau_{a,-}(z)K_{NP,a}(z,z)\,dz.
}
```

In particular

```math
\|A_{a,-}\|
\le
\operatorname{tr}A_{a,-}.
```

More generally, for every bounded Borel set `E`, the NULLPOL concentration operator

```math
C_{a,E}
=P_{\mathcal N_a}M_{1_E}P_{\mathcal N_a}
```

is trace class with

```math
\boxed{
\operatorname{tr}C_{a,E}
=\int_EK_{NP,a}(z,z)\,dz.
}
```

This is precisely a rank-2-shorted prolate/time-band concentration operator.

---

## 6. Birman--Schwinger / prolate reduction

Let

```math
A_{a,+}
=P_{\mathcal N_a}M_{\tau_{a,+}}P_{\mathcal N_a}.
```

Then

```math
Q_W(F)=\langle F,(A_{a,+}-A_{a,-})F\rangle.
```

Because `tau_a(z)\to+infty`, the positive part controls the complement of a bounded frequency set. The only possible negative spectrum of the compressed Weil form is therefore generated by the compact block `A_{a,-}`.

Whenever a positive reference lower bound for `A_{a,+}` is fixed, the remaining test is a compact Birman--Schwinger norm condition of the form

```math
\boxed{
\left\|
A_{a,+}^{-1/2}A_{a,-}A_{a,+}^{-1/2}
\right\|\le1.
}
```

The exact implementation may use a slightly shifted/coercive positive reference operator if convenient; the key theorem-level point is that the negative side is trace class and belongs to an explicit prolate shorting.

Therefore a rigorous proof can be organized by:

1. certify the finitely many leading eigenvalues of the shorted concentration/Birman--Schwinger operator;
2. control the remaining tail by its trace or Hilbert--Schmidt norm;
3. keep the high-frequency positive part analytically outside the finite numerical block.

This is a non-circular route: no Weil positivity is used as input.

---

## 7. Special laboratory `a=1/2`

At

```math
a=1/2
```

only the prime power `n=2` appears in the canonical finite-window multiplier:

```math
\boxed{
\tau_{1/2}(z)
=
\operatorname{Re}\psi\left(\frac14+\frac{iz}{2}\right)-\log\pi
-\sqrt2\log2\,\cos(z\log2).
}
```

The exact threshold is

```math
\Gamma_{1/2}
=\kappa_*+\sqrt2\log2.
```

### 7.1 Prime shift has an exact two-edge block

Let `t=log2`. Since

```math
1/2<t<1=2a,
```

every `t`-orbit in the support interval has length at most two. If

```math
C_t=P_IT_tP_I,
```

then

```math
C_t^2=0,
```

and `C_t+C_t^*` is fiberwise the `2x2` path adjacency matrix on the two edge intervals, with spectrum contained in

```text
{-1,0,+1}.
```

Hence the centered prime contribution

```math
-w_2(C_t+C_t^*)
```

is an explicit matched-edge defect of operator norm exactly `w_2=(log2)/sqrt2`.

This isolates the only arithmetic negative block at `a=1/2`.

### 7.2 Finite gamma-mode diagnostic

Using the positive resolvent expansion

```math
\Phi_\infty(D)
=\sum_{m\ge0}
\frac2{\mu_m}D^2(D^2+\mu_m^2)^{-1},
\qquad
\mu_m=2m+1/2,
```

an independent Ritz diagnostic on smooth Critical-half lifted trial spaces indicates that the first `40` positive gamma modes together with the `p=2` jump already cross the exact threshold `Gamma_{1/2}`; the remaining gamma tail is positive.

This is **diagnostic only**: a finite Ritz lower eigenvalue is not a lower bound for the full operator. The significance is strategic: a proof at `a=1/2` can plausibly be reduced to a finite rational-resolvent certification plus a positive tail, rather than requiring the whole infinite gamma ladder at once.

### 7.3 Rank-2 NULLPOL trace reduction diagnostic

For `a=1/2`, numerical quadrature of the exact trace formula gives approximately

```text
unshorted PW negative trace     2.775
NULLPOL-shorted negative trace  0.450
```

for the canonical finite multiplier above.

Thus the two exact NULLPOL evaluations remove roughly `84%` of the dangerous negative trace in this laboratory.

Again: these numbers are **not theorem certificates** until enclosed with interval arithmetic. The exact theorem is the trace formula itself.

A pure one-line trace domination using only

```math
\|A_-\|\le tr(A_-)
```

and

```math
\|C_E\|\le tr(C_E)
```

is still too coarse; at least the leading shorted prolate eigenvalue(s) must be controlled rather than replacing the whole concentration norm by its trace.

---

## 8. Narrow No-Go for a naive Blaschke cancellation

The prime scattering factor can be written

```math
S_p(z)
=
\frac{w}{b_q(w)},
\qquad
w=e^{iz\log p},
\qquad
q=p^{-1/2},
```

where

```math
b_q(w)=\frac{w-q}{1-qw}
```

is a degree-one Blaschke factor.

Its central zero corresponds to `z=i/2`, suggesting a rank-one model-space relation. However the exponential covering produces the full periodic family

```math
z=i/2+\frac{2\pi k}{\log p},
\qquad k\in\mathbb Z.
```

The single NULLPOL condition `F(i/2)=0` does not annihilate the entire periodic prime defect. Equivalently, in physical space one can choose `u` as two small matched bumps separated by `log p`; then `v=L_{1/2}u` is automatically NULLPOL while the prime shift correlation remains nonzero.

Therefore:

```text
"central NULLPOL zero alone kills the full prime Blaschke defect"  ×[M]
```

The correct object is the full shorted Paley--Wiener/prolate compression above.

---

## 9. New preferred gate

Replace the previous vague `CRIT-HALF-COMPRESS-1` by the precise gate

```text
NP-PROLATE-1 / a=1/2
```

Goal:

1. work with the exact rank-2-shorted kernel `K_{NP,1/2}`;
2. isolate the compact negative set of `tau_{1/2}`;
3. certify the leading eigenvalues of the corresponding weighted prolate/Birman--Schwinger operator with Arb or another rigorous interval method;
4. bound the residual spectrum by trace/Hilbert--Schmidt tails;
5. use analytic high-frequency positivity outside the certified block.

PASS would give a genuinely forward proof of the sharp NULLPOL lower-frame bound at `a=1/2` in the new Critical-half architecture.

FAIL would provide an explicit negative eigenfunction and therefore a decisive local counterexample to the current route.

---

## 10. Firewalls

Do not claim from this audit alone:

- NP-GAP at `a=1/2` is proved;
- the diagnostic traces are certified intervals;
- a finite Ritz PASS proves the infinite-dimensional operator inequality;
- the negative block is finite rank (it is trace class, generally infinite rank);
- the central Blaschke zero by itself removes the prime defect;
- all-window NP-GAP, Object X, or RH is solved;
- publication novelty is established.
