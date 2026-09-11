# Vor-ι′ — native Rest/Feshbach firewall at `R=1`

## 0. Scope and non-claims

This note is a **finite-window building-block audit**.  It neither constructs a global source space nor an Object-X realization.  It makes no RH claim and does not promote anything to the theorem registry.

The tested P11 mechanisms are the already-defined finite-window objects

\[
\mathscr H_R=L^2(-R,R),\qquad
R_R,\qquad
H_R,\qquad
B_R=(I+R_R^*R_R)^{-1},\qquad
\Sigma_R=H_RB_RH_R^*.
\]

The earlier symbols `H_A`, `E_{\mathcal A}` and `\Pi_{\mathcal A}` are **not used as existing main data**.  Their former use in Vor-Δ/Vor-ι was a placeholder for the still-open global source/adelic/Gram construction.

All conclusions below concern the **native** Gram pairings of the stated finite-window P11 blocks.  They do not exclude a later nontrivial source recoding, mediator, pre-Schur cross-term geometry, or another Object-X architecture.

## 1. PR-#91 calibration witness

Use the PR-#91 odd smooth pair `a,b` supported in `(-1,1)`, with

\[
\beta(a)=\beta(b)=0,\qquad
\langle a,b\rangle_{L^2}=0,\qquad
B_{\rm pole}(a,b)=0.
\]

Its correlation support meets positive `log n` only at `log 2`, where

\[
g_{a,b}(\log2)=\frac12.
\]

Hence the exact mixed-form firewall is

\[
\boxed{
B_W(a,b)-\mathfrak c_\Gamma[a,b]
=-\frac{\log2}{\sqrt2}.
}
\tag{F1}
\]

This is a mixed-pair calibration, not a negative diagonal and not a universal no-go.

## 2. Native Rest Gram

P11 (3.4)/(3.5) gives the canonical full-rest analysis map and

\[
\langle \widetilde R_1 f,\widetilde R_1 g\rangle
=\langle R_1f,R_1g\rangle.
\]

Exact lobe bookkeeping for the PR-#91 witness gives

\[
\boxed{
\langle R_1a,R_1b\rangle
=\frac{4-7\sqrt2}{32}\log2.
}
\tag{F2}
\]

Since

\[
\frac{4-7\sqrt2}{32}\log2\ne-\frac{\log2}{\sqrt2},
\]

the native additive Rest realization

\[
\mathfrak c_{\Gamma,1}[f,g]+\langle R_1f,R_1g\rangle
\]

has **d-weak PASS** (the zero-jet pairing is genuinely changed) but **d-exact FAIL**.

This does not exclude `R_1`/`\widetilde R_1` as a later mediated feature map.

## 3. Native Feshbach/Schur Gram

Set

\[
A:=R_1^*R_1\ge0,\qquad
x:=H_1^*a,\qquad y:=H_1^*b,
\]

\[
v_+:=x+y,\qquad v_-:=x-y.
\]

The native Schur pairing is exactly

\[
\boxed{
\langle\Sigma_1a,b\rangle
=\langle(I+A)^{-1}x,y\rangle.
}
\tag{F3}
\]

For

\[
m_j(v)=\langle A^jv,v\rangle\quad(j=0,1,2),
\]

with `m_0(v)=||v||^2`, the reconciled finite lobe calculation gives

| quantity | `v_+` | `v_-` |
|---|---:|---:|
| `m_0` | 1.637322379399263 | 2.617580522867810 |
| `m_1` | 2.619026483293040 | 4.413637746886540 |
| `m_2` | 5.827373366984125 | 10.320698292415832 |

The implementation derives `A=R_1^*R_1` from the martingale decomposition; it does **not** apply the sector-norm routine twice.  The check

\[
\langle v_\pm,Av_\pm\rangle=m_1(v_\pm)
\]

is reproduced to machine precision by the diagnostic script.

## 4. Spectral-moment/Cauchy-Schwarz bounds

For

\[
Q(v):=\langle(I+A)^{-1}v,v\rangle
=\int_0^\infty\frac1{1+t}\,d\mu_v(t),
\]

Cauchy-Schwarz gives

\[
\boxed{Q(v)\ge\frac{m_0(v)^2}{m_0(v)+m_1(v)}}
\tag{F4}
\]

and

\[
\boxed{Q(v)\le m_0(v)-\frac{m_1(v)^2}{m_1(v)+m_2(v)}}.
\tag{F5}
\]

The reproduced diagnostics yield

\[
Q(v_+)\in[0.6298413642,0.8252249365],
\]

\[
Q(v_-)\in[0.9744723504,1.2954851051].
\]

By real polarization,

\[
\langle(I+A)^{-1}x,y\rangle
=\frac14\bigl(Q(v_+)-Q(v_-)\bigr),
\]

so

\[
\boxed{
-0.16641094
<\langle\Sigma_1a,b\rangle
<-0.03731185.
}
\tag{F6}
\]

The target (F1), `-log(2)/sqrt(2)=-0.490129...`, lies far outside this interval.

## 5. Exact rational separation implication

The failure does not require the displayed decimal endpoints once the following coarse moment inequalities are available:

\[
m_0(v_+)>\frac{163}{100},\quad
m_1(v_+)<\frac{263}{100},
\]

\[
m_0(v_-)<\frac{262}{100},\quad
m_1(v_-)>\frac{441}{100},\quad
m_2(v_-)<\frac{1033}{100}.
\tag{F7}
\]

Monotonicity in (F4)/(F5) gives

\[
Q(v_+)>\frac{26569}{42600},\qquad
Q(v_-)<\frac{191707}{147400},
\]

hence

\[
\boxed{
\langle\Sigma_1a,b\rangle
>-\frac{10626119}{62792400}
>-\frac{17}{100}.
}
\tag{F8}
\]

The even alternating-harmonic partial sum

\[
T_{20}=\frac{155685007}{232792560}
>\frac23
\]

lies below `log 2`; and `sqrt(2)<3/2`.  Therefore

\[
-\frac{\log2}{\sqrt2}
<-\frac49
<-\frac{44}{100}.
\tag{F9}
\]

Combining (F8) and (F9),

\[
\boxed{
\langle\Sigma_1a,b\rangle
>-\frac{17}{100}
>-\frac{44}{100}
>-\frac{\log2}{\sqrt2}.
}
\tag{F10}
\]

Thus the target cannot equal the native Schur pairing.

**Epistemic note.** `check_vor_iota_prime_rational_certificate.py` proves the implication (F7) `=>` (F10) using exact rational arithmetic.  It does not independently interval-certify (F7); those five inequalities are inputs furnished by the reconciled symbolic-position/moment calculation and should be reviewed at exact head.

## 6. Epsilon robustness

The PR-#91 construction allows the initial smooth bump to be narrowed.  With a symmetric bump of half-width `epsilon`, exact prime-exponent tuples determine all lobe centers.  The stability checker finds a minimum separation

\[
d_{\min}\approx0.00222717517,
\]

so the conservative choice

\[
\epsilon<d_{\min}/4\approx5.57\cdot10^{-4}
\]

keeps all relevant bump supports disjoint in the post-cancellation `m_0/m_1/m_2` bookkeeping.  In particular `10^{-4},10^{-5},10^{-6}` lie safely inside the same combinatorial regime.  The exact coefficients and the resulting firewall interval therefore do not change under these refinements.

The script reports **103 distinct post-cancellation generated positions** for its explicitly defined relevant set.  This count is bookkeeping-convention dependent; the invariant used in the argument is the positive minimum separation, not the raw-node count.

## 7. Verdict and exact scope

For the PR-#91 witness at `R=1`:

\[
\boxed{
\text{native Rest Gram: d-weak PASS, d-exact FAIL},
}
\]

\[
\boxed{
\text{native Feshbach/Schur Gram: d-weak PASS, d-exact FAIL}.
}
\]

The second d-weak statement follows from (F6), which excludes zero.

What is **not** excluded:

- a nontrivial mediator acting on these linear arithmetic features;
- a different linear source recoding;
- pre-Schur nonorthogonal Hub/Rest cross terms;
- descent/global source spaces;
- Object X in another architecture;
- RH.

The global Vor-Δ route remains **STAND-BY** until a locally calibrated mechanism is actually present.

## 8. Reproduction and review status

The three companion scripts are intended for exact-head destructive review.  No script output is promoted to a theorem certificate merely because it runs.  The native FAIL should be accepted only within the stated finite-window scope after review of the operator conventions, witness normalization, moment bookkeeping and the rational implication.
