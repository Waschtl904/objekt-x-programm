# P11 / R43 — B-METINC GEO block front

**Date:** 2026-09-04  
**Status:** OPEN research front

**Companion audits:**
- `audits/P11_R43_B_METINC_GEO_BLOCK_FIREWALL_2026-09-04.md`
- `audits/P11_R43_GEO_STRIP_BMIX_NORMMIX_FD23_COMPACTNESS_AUDIT_2026-09-04.md`
- `audits/P11_R43_BMIX_INTERTWINING_FESHBACH_ABSORPTION_2026-09-04.md`
- `audits/P11_R43_COND_COMPRESSION_REANCHOR_AUDIT_2026-09-04.md`

## Current front

With the type-correct residual intertwining defect `C_{V,U}=R_VQ_I-\widetilde Q_I R_V` and `B_V=(I+R_V^*R_V)^{-1}`,

\[
\|Q_BB_VQ_I\|
\le
\frac12\left(\|C_{V,U}B_VQ_I\|+\|C_{V,U}B_VQ_B\|\right)
\le\|C_{V,U}B_V\|\le\|C_{V,U}\|.
\]

For `0<V-U<log(2)/2`, the frozen martingale cutoff yields `\widetilde Q_B R_V=0` and hence `C_{V,U}=-R_VQ_B`. Thus the preferred quantitative BMIX target is `||R_VQ_BB_V||`.

The COND definition check is now exact. The canonical SW14 old-conditioning term is

\[
\langle v_U,(\iota^*B_V\iota-B_U)v_U\rangle,
\qquad
\iota=E_{U,V},
\]

so the current definition genuinely carries the terminal-window embedding. If `A_T=R_T^*R_T`, decompose the terminal-`V` source space as `Ran(iota)\oplus\mathcal N` and set

\[
\Delta A=\iota^*A_V\iota-A_U,
\qquad
\Sigma=\iota^*A_VP_{\mathcal N}
(I_{\mathcal N}+P_{\mathcal N}A_VP_{\mathcal N})^{-1}
P_{\mathcal N}A_V\iota.
\]

Then the desired order is equivalent to

\[
\boxed{\iota^*B_V\iota\preceq B_U\iff \Delta A\succeq\Sigma.}
\]

Hence `CANONICAL-PSD-REALIZATION` does not close by an `iota=id` shortcut. The next canonical COND calculation is to identify the actual `\Delta A` and Schur-coupling `\Sigma` for frozen `R_V` and test this exact criterion. Reanchoring comes only after a positive chain has been established.

## Live tree

```text
B-METINC-WIDTH [OPEN]
├─ B-METINC-NEW [OPEN]
├─ B-METINC-GEO [OPEN]
│  ├─ R43-GEO-RAW-STRIP ✓[M]
│  ├─ B-METINC-GEO-BMIX [OPEN]
│  │  ├─ FESHBACH-ABSORPTION ✓[M]
│  │  ├─ RESIDUAL-DEAD-LAYER ✓[M]
│  │  ├─ RESIDUAL-MARK-GRAM ✓[M]
│  │  └─ conditioned defect decay/summability [OPEN]
│  └─ B-METINC-GEO-BDRY [OPEN]
├─ B-METINC-NORMMIX [OPEN]
├─ B-METINC-COND [OPEN]
│  ├─ RESOLVENT-ANTITONE-TELESCOPE ✓[M]
│  ├─ COND-PSD-INCREMENT-ABSTRACT ✓[M]
│  ├─ COND-COMPRESSION-SCHUR-CRITERION ✓[M]
│  ├─ COND-DISCRETE-ABEL-DECOMPOSITION ✓[M]
│  ├─ COND-REANCHOR-SUFFICIENT ✓[M]
│  ├─ COND-REANCHOR-BOUNDEDNESS-NOGO ✓[M]_neg
│  ├─ COND-CANONICAL-PSD-REALIZATION [OPEN]
│  └─ COND-FIXED-SOURCE-REANCHOR [OPEN]
└─ FD23-UNIF [OPEN]
   └─ FD23-TAIL-COMPACTNESS-EQUIV ✓[M]
```

Downstream remains `B-METINC -> B-FLAGMOD`, together with `B-FLAGPHASE` as the sufficient route to `B-FLAGTIGHT`, then `B-SIGN`, then Strong Terminal. No converse is added.

## Exact BMIX identities

Because `R_V` acts between source and residual field spaces, source projection `Q_I` and residual projection `\widetilde Q_I` are distinct. Then

\[
C_{V,U}Q_I=\widetilde Q_B R_VQ_I,
\qquad
C_{V,U}Q_B=-\widetilde Q_I R_VQ_B,
\]

and

\[
[R_V^*R_V,Q_I]=R_V^*C_{V,U}-C_{V,U}^*R_V.
\]

Retaining both Feshbach factors gives

\[
Q_BB_VQ_I=-Q_BB_VR_V^*C_{V,U}B_VQ_I+Q_BB_VC_{V,U}^*R_VB_VQ_I,
\]

with `||R_VB_V||=||B_VR_V^*||<=1/2`. This is `R43-BMIX-FESHBACH-ABSORPTION ✓[M]` locally; BMIX remains OPEN.

The exact prime-power defect formula is

\[
(C_{V,U}f)(u)=\sum_{p,k}\sqrt{\log p}\,p^{-k/4}([D_{k\log p},M_U]E_Vf)(u)\otimes\mathsf Q_V(u)\eta_{p,k}.
\]

Support localization alone does not imply norm smallness.

The fine-step dead-layer theorem `R43-RESIDUAL-DEAD-LAYER ✓[M]` follows from the frozen source-dependent depth. For residual marks, with `r=min{k,l,J_{p,V}(u)}`,

\[
\langle q_{p,k;V},q_{p,l;V}\rangle=\begin{cases}p^{r-(k+l)/2}-p^{-(k+l)/2},&r\ge1,\\0,&r=0,\end{cases}
\]

hence `0<=<q_{p,k;V},q_{p,l;V}><=p^{-|k-l|/2}`. This is `R43-RESIDUAL-MARK-GRAM ✓[M]` locally.

## Exact COND identities

For a positive same-space chain `A_0\preceq A_1\preceq\cdots`, the resolvents `B_j=(I+A_j)^{-1}` decrease and

\[
\sum_j\langle x,(B_j-B_{j+1})x\rangle\le\|x\|^2
\]

for each fixed `x`. This is the abstract `R43-RESOLVENT-ANTITONE-TELESCOPE ✓[M]`; it does not by itself apply to the compressed canonical term.

For a moving path `v_j=x+\delta_j` and a positive telescoping chain `D_j=B_j-B_{j+1}`, Cauchy-Schwarz inside the `D_j`-form gives, for every `\varepsilon>0`,

\[
\sum_j\langle v_j,D_jv_j\rangle
\le
(1+\varepsilon)\|x\|^2
+(1+\varepsilon^{-1})\sum_j\|\delta_j\|^2.
\]

Thus square-summable drift around a fixed anchor is sufficient. Boundedness alone is not: on `\ell^2`, taking tail projections `B_j` and `v_j=e_j` gives unit-bounded vectors but infinite accumulated energy. These are local abstract results only; the canonical R43 path condition remains OPEN.

## Remaining firewalls

BMIX conditioned decay/summability, BDRY, NORMMIX, canonical COND PSD realization, canonical reanchor control, and concrete FD23-UNIF remain OPEN.

## Governance

Local exact only: `R43-GEO-RAW-STRIP ✓[M]`, `R43-BMIX-FESHBACH-ABSORPTION ✓[M]`, `R43-RESIDUAL-DEAD-LAYER ✓[M]`, `R43-RESIDUAL-MARK-GRAM ✓[M]`, `FD23-TAIL-COMPACTNESS-EQUIV ✓[M]`, `R43-RESOLVENT-ANTITONE-TELESCOPE ✓[M]`, `R43-COND-PSD-INCREMENT-ABSTRACT ✓[M]`, `R43-COND-COMPRESSION-SCHUR-CRITERION ✓[M]`, `R43-COND-DISCRETE-ABEL-DECOMPOSITION ✓[M]`, `R43-COND-REANCHOR-SUFFICIENT ✓[M]`, and `R43-COND-REANCHOR-BOUNDEDNESS-NOGO ✓[M]_neg`.

All project gates remain OPEN, including B-METINC-GEO-BMIX, B-METINC-GEO-BDRY, B-METINC-NORMMIX, B-METINC-COND, FD23-UNIF, B-METINC-NEW, B-METINC-WIDTH, B-METINC, B-FLAGMOD, B-FLAGPHASE, B-FLAGTIGHT, B-SIGN, Strong Terminal/C6, and R43. No freeze, no formal independent GREEN, no Object-X/RH promotion. R38–R42 unchanged/frozen; R37/G4c separate and OPEN.
