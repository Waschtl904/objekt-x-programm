# P11 / R32 / SW1 — M1-ND-IMG1 effective 3×6 ledger candidate

## Status

\[
\boxed{\mathrm{M1\!-\!ND\!-\!IMG1}:\ \text{AI-GREEN candidate + independent GREEN (certificate)}}
\]

No \(\checkmark[M]\) promotion. No injectivity claim.

First CI:
- Run \`33355572113\`
- Job \`99376945769\`
- Head \`94df1bf1da40344d61a94b82367501c74de8a750\`
- Python \`3.12.14\`
- Audit blob \`530ec7cdd1fb1db2e72d973e24a1490c128c058e\`
- IMG1 script blob \`23510e94278d58720b498b10df198742bd40d97b\`
- M1-FULL blob \`d73993a393b9d076c72bc77cbdf3610f4695c29c\`
- IMG0 blob \`7f5b11bd80e5387b1c5e8d73be4c0e4140eed8d5\`

The hardened script must reproduce the frozen values below before the node is booked as \`independent GREEN (certificate)\`.

## 1. Exact object

\[
\mathscr N_R
=
R_{P_0}^{\rm out}\widehat{\mathscr C}_R(E_H\oplus E_W)
\]

acts on the six independent function channels
\[
u=(f_0,f_1,f_2,g_0,g_1,g_2),
\qquad
f\in\mathscr B_K,\quad g\in\mathscr B_W,
\]
and has three \(P_0\) output lifts.

This is a function-channel reduction, not a six-dimensional vector-space reduction. The analytic constraint \(f\in\mathscr B_K\) remains in force.

## 2. Effective pullbacks

If the M1 input species is \(g_{\rm in}=(s,\eta,\kappa)\) and the original M1 shift is \(j\), then IMG0 gives the base pullback

\[
\boxed{
\alpha_{g_{\rm in},j}(\theta)
=
s\theta+\frac{\eta}{2}L+(sj+\kappa)\Delta
\pmod L.
}
\]

The exact alphabet is

\[
\theta,\ \theta\pm\Delta,\ \theta\pm2\Delta,
\]
\[
-\theta+\Delta,\ -\theta+2\Delta,\ -\theta+3\Delta,\ -\theta+4\Delta,
\]
\[
-\theta+\frac L2+2\Delta,\quad
\theta+\frac L2-2\Delta,\quad
\theta+\frac L2+2\Delta.
\]

Only \(B_L,B_R,B_O\) generate \(L/2\)-pullbacks.

## 3. Exact \(3\times6\) form

On each open \(B_{96}\)-atom,

\[
(\mathscr N_Ru)_a(\theta)
=
\sum_{c=0}^{5}
\sum_{\alpha\in\mathcal A_{12}}
C_{a,c,\alpha}\,u_c(\alpha(\theta)),
\qquad a=0,1,2.
\]

Every contribution records:
- affine map;
- H/W input block;
- input lift;
- \(P_0\) output lift;
- exact symbolic coefficient;
- FREE row or HUB branch;
- source name;
- original input species;
- original M1 shift \(j\).

The certificate compares two paths on all \(64\times96=6144\) open reference atoms at \(r_0=7/2\):

1. direct physical \(P_0\) assembly;
2. M1 ledger followed by IMG0 species elimination.

It requires strong termwise equality, including coefficient and provenance, then equality of the reduced grouped signatures.

## 4. First-run exact data

\[
\boxed{\text{reduced active terms}=117546}
\]

\[
\boxed{\text{distinct reduced operator states}=22}
\]

\[
\boxed{
\mathrm{SHA256}
=
\texttt{1cffd33529534a15c941b67086217f8f8c47b0cc302cb2cf740b0e08c2ff4474}
}
\]

Nonzero \((\text{output},\text{input},\text{map})\)-cell histogram:

\[
\{14:314,\ 15:2615,\ 16:276,\ 23:1690,\ 24:669,\ 25:497,\ 26:83\}.
\]

Nonzero \(3\times6\) channel histogram:

\[
\{8:1754,\ 9:1213,\ 10:238,\ 14:1344,\ 15:251,\ 16:1260,\ 17:84\}.
\]

Aggregation multiplicity:

\[
\boxed{\{1:117546\}}.
\]

Thus there are no collisions at the natural reduced-cell level \((a,c,\alpha)\): every active grouped cell is a singleton.

## 5. Firewall

IMG1 does not prove
\[
\ker\mathscr N_R=\{0\}.
\]

It does not yet derive a recurrence, invert any outer block, solve the \(\mathscr B_K\) constraint, construct/exclude an admissible kernel function, add an actual-\(r\) promotion, or imply anything about Objekt X globally or RH.

The next legitimate step after hardened IMG1 is transfer/recurrence analysis on the true admissible function space.
