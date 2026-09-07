# P11 / R43 — SCHUR-XBAND-COMM

**Date:** 2026-09-07. **Status:** Draft; local algebra plus finite numerical proxy.
**Independent review:** not performed. **Registry promotion:** none.

## 1. Scope and reproducibility

Parent: PR #84, branch `r43-schur-var-delta-sweep`, exact commit
`3e4e5a73679db9f88624869587c4bd3bc3fec266`.
Its parent is PR #83, exact commit `4abccc2dd29d87f914440478c286dbc6edf11169`.
Both PRs were read through the GitHub connector and were open, Draft and unmerged.
The original files were fully retrieved, transferred locally, and verified against
the connector's Git blob SHA, not merely visually copied:

| Parent script | Git blob SHA |
| --- | --- |
| `P11_R43_SCHUR_CORR_STRUCTURED_HUB_PROXY_2026-09-06.py` | `237bf3406debcc3d2ec757ce547d3759c55a1fc2` |
| `P11_R43_SCHUR_VAR_DELTA_SWEEP_2026-09-06.py` | `bb0ccb9e788bb0949ab1ea01b80ad6f6ce5fef4d` |

Both original assertion suites passed locally. The new script checks these hashes
before importing the parent modules. It requires NumPy and SciPy; the parents
remain unchanged standard-library scripts.

```sh
OPENBLAS_NUM_THREADS=1 python audits/P11_R43_SCHUR_XBAND_COMM_2026-09-07.py \
  --parents --output r43-xband-results.json
```

Measured environment: CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0.
The new suite records **1011 identity/error checks**, with tolerance `5e-11`,
strictly below `1e-10`. The largest recorded error is `4.648143553782e-12`,
in `boundary_source_identity_4_BT_2`. The final script also contains exact integer
matrix assertions and inequality/positivity checks, not included in that count.
Recorded checks include both relative residuals (`check`) and absolute zero
residuals (`zero`); the maximum is a test diagnostic, not a common physical norm.
No interval-arithmetic or independent certification is claimed.

Full results are emitted as JSON: all 27 pair decompositions, all 27 large-shift
controls, 45 global supplementary decompositions, matrix/conditioning tests,
boundary-source tests, nine source-subspace spectra and 18 off-grid bridges.

## 2. Model and one sign correction

Use exactly the parent graph: integer nodes `[-30,30]` and `[-40,40]`, centers
`10,12,14`, source radii `4,6,8`, and baseline half-width `0.15`.

```text
graph masses = 44.59817706246725, 120.89687763600345, 329.1851915820806
hub masses   = 1.1572520185069353, 1.7361325665411198, 2.6546513413534485
```

Write `A=A_U=I+L_U`, `B_U=A^{-1}`, `C=Btilde=iota^* B_V iota` and
`Q=B_U # C`. Here Q is the **actual matrix geometric mean of the finite proxy**,
not the analytic P11 operator. The symbol C for this endpoint is separate from
the source-specific commutator contribution `C_h` below.

With `tau_h x(u)=x(u-h)` and `h=t_j-t_i>0`, the correct right-strip orientation is

```math
(T_h-I)x(z-t_i)=x(z-t_j)-x(z-t_i).
```

The handover displayed the opposite difference. On the left strip use `h=-(t_j-t_i)`
and the base point `z+t_i`. Every pair is oriented as target j minus base i.
Changing both amplitudes' signs would leave their interference unchanged; mixing
orientations between the two amplitudes would not be legitimate.

For each active star z, use `W(z)=sum_all_active W_i(z)` and
`rho_ij(z)=W_i(z)W_j(z)/W(z)`. The exact pairwise identity is

```math
V_{inter}(x)=\sum_z\sum_{i<j}\rho_{ij}(z)|m_j(z)-m_i(z)|^2.
```

For the center graph, `m_i(z)=x(z-sign(z)t_i)`. All three channels are active at
all 20 strip nodes. The pair-weighted observations form a seminorm, not a
positive-definite norm on the entire old-window space. The JSON's relative
quantities use the same denominator `G=(Bv)^* A(Bv)` for every term in one case.
The incidence Gram equals the independently assembled ANOVA matrix. A deliberately
wrong pair-only denominator gives `1.349444679951` times the correct variance on
the seeded random control: the test rejects it.

## 3. Exact decomposition and measured outcome

For each signed pair shift set

```math
A_h=B(T_h-I)v,\quad C_h=(T_hB-BT_h)v,\quad X_h=(T_h-I)Bv=A_h+C_h.
```

All three transports, all source radii, both pair magnitudes `2,4`, and both strip
orientations are tested. The three large shifts `10,12,14` are supplementary
negative controls evaluated on the same sampler, **not additional ANOVA pairs**.

The reported identity is the full signed quadratic identity

```math
\|X\|_{rel}^2=\|A\|_{rel}^2+\|C\|_{rel}^2+2\Re\langle A,C\rangle_{rel}.
```

No triangle estimate is substituted for these measurements. Summing the three
actual pairs gives the following table; each entry is divided by G.

| X | B | A2/G | C2/G | 2AC/G | Vinter/G |
| --- | --- | ---: | ---: | ---: | ---: |
| 4 | BU | .124295350791 | .000490310214 | -.008420976804 | .116364684201 |
| 4 | BT | .054004748443 | .000183322576 | -.002570785555 | .051617285464 |
| 4 | Q | .082181500660 | .000164246545 | -.004488131234 | .077857615971 |
| 6 | BU | .107839366223 | .000436905183 | -.003964537543 | .104311733862 |
| 6 | BT | .058771135852 | .000517295217 | -.006842759482 | .052445671586 |
| 6 | Q | .079551374738 | .000268449853 | -.005484227525 | .074335597067 |
| 8 | BU | .074905627006 | .000324609257 | +.002515515047 | .077745751310 |
| 8 | BT | .049410035727 | .000808837566 | -.009844177675 | .040374695619 |
| 8 | Q | .060840752951 | .000280036495 | -.004849137710 | .056271651736 |

Consequences, strictly for these proxies:

- The commutator term is small relative to the transported hub difference, but
  the variance is not. Across the nine cases, `||C||rel/||A||rel` ranges from
  `.0447055` to `.1279449`.
- For Q, the surviving variance is `94.7386%, 93.4435%, 92.4901%` of A2 for
  X=4,6,8. There is modest cancellation, not a cancellation mechanism eliminating
  the dominant channel.
- For BU at X=8, the summed interference is **positive**, and in fact all three
  actual pairs have positive interference. Destructive interference is not an
  automatic property of this structured source/transport construction.

### Local reduction lemma: small relative commutators preserve the main term

Let the weighted observations over all pairs be concatenated into a Hilbert
space. Suppose `X=A+C` and `||C|| <= epsilon ||A||`, with `epsilon<1`. Then

```math
(1-\epsilon)^2\|A\|^2\le\|X\|^2\le(1+\epsilon)^2\|A\|^2.
```

Proof: apply the reverse and ordinary triangle inequalities to `A+C` and square.
This is a **consequence after** the exact signed decomposition, not a replacement
for it. Along any family with a uniform `epsilon<=epsilon_0<1`, normalized
cross-band variance tends to zero if and only if the normalized transported
hub-difference energy tends to zero. Hence making the commutator small does not
by itself provide the missing decay; it makes the remaining main term decisive.
The lemma is exact. Its hypotheses for the analytic/canonical family remain open.

A separate exact negative control takes `B=I` and arbitrary `v=e_17` on the same
old grid. All commutators vanish, but the pair variance is positive. This refutes
an arbitrary-source implication from commuting transport to zero variance. It is
**not** a counterexample in the restricted compact-hub source family.

## 4. Stronger numerical test: the complete finite odd-source subspace

Do not rely only on the three smooth bumps. For radius X, take the complete
`X-1` dimensional space spanned by `delta_k-delta_-k`, `1<=k<X`. Apply the same
finite hub to every basis direction. Assemble the observation matrices `RA,RC`
and verify `RD=RA+RC=incidence B Hsource`.

Let `GA=RA^*RA`, `GC=RC^*RC`, `GD=RD^*RD`, and
`GG=Hsource^* B A B Hsource`. When GA is positive definite, standard Rayleigh
quotients give the exact characterization

```math
\epsilon_{sup}^2=\lambda_{max}(GC,GA),\qquad
\inf_{f\ne0}\frac{V_{inter}(BHf)}{\|A(f)\|^2}=\lambda_{min}(GD,GA).
```

The characterization is algebraic; the following eigenvalue evaluations are
floating-point diagnostics, **not interval-certified all-source inequalities**.

| X | B | dimension | epsilon_sup | min V/A2 | max V/A2 |
| --- | --- | ---: | ---: | ---: | ---: |
| 4 | BU | 3 | .0737610225 | .9153013186 | .9804964499 |
| 4 | BT | 3 | .0955782597 | .9205827224 | .9920411790 |
| 4 | Q | 3 | .0592172060 | .9294630881 | .9836035629 |
| 6 | BU | 5 | .1275260566 | .8710415177 | 1.1480232834 |
| 6 | BT | 5 | .2023264510 | .6846636190 | 1.0006717146 |
| 6 | Q | 5 | .1154248364 | .8277761521 | .9862890321 |
| 8 | BU | 7 | .1672848663 | .8559794798 | 1.1579068625 |
| 8 | BT | 7 | .2097965878 | .6819242098 | 1.0143386790 |
| 8 | Q | 7 | .1157528874 | .8231608153 | .9988381983 |

For Q at X=8, the numerical `V/G` range over this entire subspace is
`[.0046965241394, .0855379955748]`, and `cond(GA)=61.4722711808`.
This tests every discrete odd direction, including oscillatory combinations, not
just a finite random selection. It does not cover continuous sources, additional
prime shifts, moving windows, or canonical conditioned data.

The full finite hub is
`Hfull=-sum_i a_i(T_(t_i/2)-T_(-t_i/2))`. Matrix tests additionally show
`[T_h,Hfull] f=0` on these source spaces for `h=+/-2,+/-4`. This has a simple exact
support proof: all intermediate shifts stay inside the old interval since
`(X-1)+7+4 <= 18 < 30`. Thus, on this finite bulk source class,

```math
B\Delta_h Hfull f=B Hfull\Delta_h f.
```

It does not establish a group law for compressed translations on arbitrary data.

## 5. Q: SPD, Riccati and the correct stability scale

The compressed large resolvent is built independently from the full inverse and
from its block Schur complement:

```math
C=(A_{OO}-A_{ON}A_{NN}^{-1}A_{NO})^{-1}=(A+K)^{-1}.
```

Here the strip-strip off-diagonal block is zero: a strip has ten integer points,
so the largest same-strip distance is nine, below every graph shift. Opposite
strips are farther apart than every shift. Therefore K is an exact sum of
independent star Schur matrices. For a star with weighted old incidence vector g,

```math
K_z=\operatorname{diag}(w)-\frac{gg^*}{1+W}
=\left(\operatorname{diag}(w)-\frac{gg^*}{W}\right)
 +\frac{gg^*}{W(1+W)}\succeq0.
```

Thus `K=VAR+MEAN>=0`. This star independence is geometry-specific, not asserted
for the full P11 strip operator.

Set `Kbar=A^{-1/2} K A^{-1/2}`. Then exactly

```math
Q=A^{-1/2}(I+Kbar)^{-1/2}A^{-1/2},\qquad
H=A^{1/2}QA^{1/2}=(I+Kbar)^{-1/2}.
```

This construction agrees numerically with the separate generic geometric-mean
formula `BU^(1/2)(BU^(-1/2) C BU^(-1/2))^(1/2)BU^(1/2)`.

| matrix | minimum eigenvalue | maximum eigenvalue | condition number |
| --- | ---: | ---: | ---: |
| BU | .0005731407180 | 1.0000000000 | 1744.7722149 |
| BT | .0005719658912 | .7566200727 | 1322.8412470 |
| Q | .0005726120012 | .8698154397 | 1519.0311029 |
| H | .7281305582 | 1.0000000000 | 1.3733800742 |

Relative Frobenius residual of `QAQ=C`: `4.331957011554e-13`.
`lambda_max(Kbar)=.886172828244`.

### Local stability lemma, including its norm qualification

For `D=[T,Q]`, taking the commutator of `QAQ=C` gives

```math
QAD+DAQ=F_T,\quad F_T=[T,C]-Q[T,A]Q.
```

Multiply on both sides by `A^(1/2)`, and write
`Dhat=A^(1/2)DA^(1/2)`, `Fhat=A^(1/2)F_TA^(1/2)`. Then

```math
H Dhat+Dhat H=Fhat.
```

In an orthonormal eigenbasis of the SPD matrix H, each matrix entry is divided
by `lambda_i(H)+lambda_j(H)`. The inverse exists uniquely and its **exact induced
Frobenius norm in these weighted coordinates** is

```math
\frac1{2\lambda_{min}(H)}=\frac{\sqrt{1+\|Kbar\|_2}}2.
```

It is attained on a rank-one matrix from a minimum eigenvector of H. In this
proxy the constant is `.686690037106`. Small absolute eigenvalues of Q do not
create a near-null Sylvester denominator in this energy metric.

However, this does **not** immediately bound the pair observation seminorm,
or replace the need to estimate Fhat. Converting this estimate crudely back to
unweighted Frobenius norm gives `cond(A)*.686690... = 1198.11769696`, not `.686690`.
The matrix identity and an independently solved Sylvester equation are checked
for h=2,4,10,12,14. No analytic uniform bound on Kbar is claimed.

Background for the standard Sylvester separation principle: Nick Higham,
“What Is the Sylvester Equation?”, 2020-09-01,
<https://nhigham.com/2020/09/01/what-is-the-sylvester-equation/>.
The Schur normalization and the formula above are derived explicitly here.

## 6. Compression and boundary-resolvent control

For zero extension E and restriction P, direct insertion of `EP+(I-EP)=I` gives

```math
T_hT_k-T_{h+k}=-P\tau_h(I-EP)\tau_k E.
```

For same-sign shifts on an interval this is zero. For opposite shifts,
`T_-2 T_2-I` is exactly minus the projection onto the last two grid points.
The integer matrix test agrees entrywise with this projection. The rightmost
unit impulse loses norm 1; a smooth right-boundary bump loses `.884774008517`
of its norm. All three raw bulk hubs have zero loss. The latter is a support
fact, not an operator group law.

For BU, the resolvent identity is checked in its correct order:

```math
[T,BU]=BU[A,T]BU.
```

Let `L0=P L_infinity E`, with full infinite degree `2 sum_i w_i`, and let Dlost
be the missing-edge diagonal. Then

```math
A=I+L0-Dlost,\qquad [A,T]=[L0,T]-[Dlost,T].
```

The two terms and their sum have the expected boundary row/column support;
for shift h a valid shell is `U-|u| < 14+|h|`.

For BT, do not reuse A: use `F=A+K` and
`[T,BT]=BT[F,T]BT`. This is independently compared with the exact large-window
compression formula, where `N=I-EE^*` and `T=E^*T_V E`:

```math
[T,BT]=E^*[T_V,BV]E-E^*T_V N BV E+E^*BV N T_V E.
```

The last two excursion terms are retained. The Schur commutator is also boundary
supported. No assertion that the inverse of Q has the same locality is made.

### Local no-go for a distance-only arbitrary-boundary-input estimate

Right-strip old preimages run through `17,...,30`; left-strip preimages are
reflections. These already lie in the boundary shells, not at increasing
distance from them. If R is a positive-shift pair sampler and Pboundary is the
shell projection, then, for a sampled node u in the shell,

```math
\|R B Pboundary\|_2\ge\sqrt{\rho}\,B_{uu}
\ge\frac{\sqrt{\rho}}{1+2\sum_i w_i}>0.
```

The first inequality follows by testing `e_u` and retaining its corresponding
observation coordinate. For BU the second is the SPD inequality
`(A^{-1})_uu>=1/A_uu`; for BT use the same inequality in the full A_V inverse.
Its proof is Cauchy-Schwarz applied to `A^(1/2)e_u` and `A^(-1/2)e_u`.
The degree bound is uniform for a fixed-weight/fixed-shift family `V=U+10`,
`U>=30`. Hence arbitrary boundary data cannot be made negligible by an asserted
growing separation which does not exist in this sampler.

Actual weighted transfer norms and conservative positive lower bounds:

| h | B | norm R B Pboundary | proved lower bound from degrees |
| --- | --- | ---: | ---: |
| 2 | BU | 2.8518811635 | .0090567441 |
| 2 | BT | 2.1391227778 | .0090567441 |
| 4 | BU | 1.7247646834 | .0055007652 |
| 4 | BT | 1.2943759433 | .0055007652 |

The actual source-specific commutators are much smaller than this worst-case
bound. For example X=8, BT, h=2 has observed `||R C_h||/sqrt(G)=.0147043706193`,
while `||R BT Pboundary|| ||[F,T]x||/sqrt(G)=3.21613032549`.
The bound is valid but very lossy. This leaves room for source-specific moment
or cancellation estimates; it does not supply them for canonical data.

## 7. Off-grid bridge: do not identify band means with center samples

For #84's prime-resolved microgeometry, the active band masses depend on z,
including partial activity near the endpoint of the band centered at 10.
All-band denominators are recomputed at the same z.

Write `e_i=m_i-x(z-sign(z)t_i)`. Then exactly

```math
m_j-m_i=(T_h-I)x(z-sign(z)t_i)+(e_j-e_i).
```

The off-grid test retains this remainder and its signed interference:

```math
V_{inter}=E_{center}+E_{remainder}+2\Re\langle center,remainder\rangle.
```

It verifies this identity, the direct weighted ANOVA identity, the pair formula,
and the original #84 implementation for both delta=.15 and .005, all radii and
all three transports. The band-center resolvents remain frozen, as in #84.

Representative Q, X=8:

| delta | intra/G | inter/G | center/G | remainder/G | 2center,remainder/G |
| --- | ---: | ---: | ---: | ---: | ---: |
| .15 | .0002828459884 | .0551838249730 | .0560946668593 | .0000049941363 | -.0009158360227 |
| .005 | .0000003076734 | .0561307251176 | .0561711547580 | .0000000089444 | -.0000404385847 |

Thus the finite Q extension also exhibits a persistent inter-band contribution
at the two tested widths. This is not an asymptotic theorem, nor a full new
bandwidth sweep for Q. The center experiment and finite-width experiment remain
explicitly distinguished.

## 8. Bookings and next gate

**Local exact algebra, proved above (`✓[M]_local`):** corrected signed pair
orientation; weighted pair representation; small-relative-commutator reduction;
conditional source-space Rayleigh characterization; bulk source/hub commutation;
Schur-normalized Sylvester stability; compression-defect and compressed-resolvent
identities; fixed-shift proxy boundary-distance obstruction.
These labels describe the displayed finite/bounded-matrix lemmas, not an
independent review or repository theorem-registry promotion.

**Numerical only (`✓[M]_proxy`):** parent reproduction, finite Q construction,
conditioning/residual values, all energy tables, complete finite odd-source
spectra, and the two-width off-grid bridge.

**Negative result with restricted scope (`×[M]_neg,local`):** commutation alone
cannot imply variance decay for arbitrary old-grid data; a distance-only argument
cannot make this fixed-shift proxy's worst-case boundary transfer vanish.
The observed constructive interference at BU, X=8 is numerical proxy evidence,
not an interval-certified sign theorem for transcendental weights.

**OPEN (`?[O]`):** canonical source, true P11 transport, analytic relative
commutator bounds, uniform source-energy decay, and the continuum/moving-window
transfer. No Strong Terminal/C6 or other global status has changed.

The next mathematical gate is **R43-SCHUR-XBAND-HUB-DIFF**: estimate the actual
pair-weighted energy of `Q Delta_h H_U^* E_R f_rev`, normalized by the same graph
energy of `x_rev`, with the true conditioned source and true transport.
The finite bulk identity reduces the proxy main term further to
`B Hfull Delta_h f`; it does not justify that reduction in the analytic model
without its own support/domain check.

An independent reviewer can separately certify finite source-Gram inequalities
(e.g. the numerical candidates `GC < .12^2 GA` and `GD > .82 GA` for Q on X=8)
with directed rounding. That is a finite audit task, not a substitute for the
source-energy gate.

## 9. Firewalls

The script never constructs `G_(R,cond)^(-1/2) epsilon_R`, the analytic Q, or the
canonical x_rev. All center shifts are even integers, so the proxy graph has two
lattice components; this discretization feature is checked and is not promoted
to arithmetic structure. The off-grid experiment resolves primes only in the hub
and sampler, not the resolvents. No conclusion about reverse-normal stretch
decay, FD23-UNIF, FLAGDYN/TIGHT, Strong Terminal/C6, Object X, or RH follows from
these calculations. Existing Draft PRs, their files, and the registry are unchanged.

## Appendix: all actual center-pair energy decompositions

Columns are divided by the common G in each source/transport case. Both strip
orientations are included. Pairs `(10,12)` and `(12,14)` have magnitude 2;
`(10,14)` has magnitude 4. The interference column is signed.

| X | B | pair | A2/G | C2/G | 2AC/G | pair variance/G |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| 4 | BU | 10,12 | 0.00652176273748 | 2.01731005995e-05 | -4.68939278154e-05 | 0.00649504191026 |
| 4 | BU | 10,14 | 0.0520966888728 | 0.000220228931692 | -0.005139786577 | 0.0471771312275 |
| 4 | BU | 12,14 | 0.0656768991806 | 0.00024990818142 | -0.00323429629895 | 0.0626925110631 |
| 4 | BT | 10,12 | 0.0026259530985 | 4.25301047766e-06 | -6.27096246558e-05 | 0.00256749648432 |
| 4 | BT | 10,14 | 0.0233912737205 | 0.000152653227208 | -0.00184192206396 | 0.0217020048837 |
| 4 | BT | 12,14 | 0.0279875216241 | 2.6416338493e-05 | -0.000666153866298 | 0.0273477840963 |
| 4 | Q | 10,12 | 0.00414854447267 | 5.94438193575e-06 | -4.91274981567e-05 | 0.00410536135644 |
| 4 | Q | 10,14 | 0.0350138339395 | 0.000100257199592 | -0.00295021766713 | 0.032163873472 |
| 4 | Q | 12,14 | 0.0430191222477 | 5.8044963555e-05 | -0.0014887860692 | 0.0415883811421 |
| 6 | BU | 10,12 | 0.00455302409746 | 3.51563481223e-05 | 5.78563598407e-05 | 0.00464603680542 |
| 6 | BU | 10,14 | 0.0506761989329 | 0.000154175161979 | -0.00284067079379 | 0.0479897033011 |
| 6 | BU | 12,14 | 0.0526101431926 | 0.000247573672499 | -0.00118172310913 | 0.0516759937559 |
| 6 | BT | 10,12 | 0.00238125716023 | 2.84370085415e-05 | -0.00025325790087 | 0.0021564362679 |
| 6 | BT | 10,14 | 0.0282530115592 | 0.000328412833708 | -0.00423952839361 | 0.0243418959993 |
| 6 | BT | 12,14 | 0.0281368671321 | 0.000160445374285 | -0.00234997318753 | 0.0259473393188 |
| 6 | Q | 10,12 | 0.00327608011326 | 1.8237967147e-05 | -0.000123065964061 | 0.00317125211635 |
| 6 | Q | 10,14 | 0.0378266560345 | 0.00014818089958 | -0.00363239428168 | 0.0343424426524 |
| 6 | Q | 12,14 | 0.0384486385906 | 0.000102030986767 | -0.0017287672791 | 0.0368219022982 |
| 8 | BU | 10,12 | 0.00343568397199 | 3.71013434979e-05 | 0.000211469918124 | 0.00368425523362 |
| 8 | BU | 10,14 | 0.0367193044349 | 9.74535033653e-05 | 0.000269222582293 | 0.0370859805205 |
| 8 | BU | 12,14 | 0.0347506385988 | 0.000190054410396 | 0.0020348225466 | 0.0369755155558 |
| 8 | BT | 10,12 | 0.00228149868489 | 6.63737999638e-05 | -0.000516769082699 | 0.00183110340215 |
| 8 | BT | 10,14 | 0.0242266677214 | 0.000376400535466 | -0.00500018580529 | 0.0196028824516 |
| 8 | BT | 12,14 | 0.0229018693208 | 0.000366063230653 | -0.00432722278665 | 0.0189407097648 |
| 8 | Q | 10,12 | 0.00279711581591 | 3.18530253903e-05 | -0.000232270037357 | 0.00259669880394 |
| 8 | Q | 10,14 | 0.0298029313765 | 0.000121895218525 | -0.00286283323755 | 0.0270619933574 |
| 8 | Q | 12,14 | 0.0282407057587 | 0.000126288250647 | -0.00175403443467 | 0.0266129595746 |
