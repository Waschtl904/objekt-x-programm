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


---

## 6. Post-review hardening: IMG0/M1 species algebra

A review correctly identified that IMG1 uses the M1-FULL objects
\`free_sr\`, \`hub_sr\`, \`Nwrap\` and the integer \(m\). These are now
cross-checked explicitly against the already accepted IMG0 species extension.

Write a species as
\[
g=(s_g,\eta_g,\kappa_g),
\qquad
\phi_g(\theta)
=
s_g\theta+\frac{\eta_g}{2}L+\kappa_g\Delta,
\]
and
\[
\rho_g(\theta)=\phi_g(\theta)-N_g(\theta)L,
\qquad
N_g(\theta)=\left\lfloor\frac{\phi_g(\theta)}L\right\rfloor.
\]

For a physical source relation
\[
t=sx+\lambda_{\rm src}L+k_{\rm src}\Delta
\]
and an output species \(g_{\rm out}=(s_o,\eta_o,\kappa_o)\), the source
species is determined by
\[
s_i=ss_o,
\]
\[
\eta_i
\equiv
s\eta_o+2\lambda_{\rm src}
\pmod 2,
\]
and the M1 shift \(j\) by
\[
s_i j+\kappa_i
=
s\kappa_o+k_{\rm src}.
\]

The integer stored by M1-FULL as \(m\) is not a new species rule. It is
exactly
\[
\boxed{
m
=
\frac{\eta_i}{2}
-
\left(
s\frac{\eta_o}{2}+\lambda_{\rm src}
\right)
\in\mathbb Z.
}
\]

If
\[
x_{\rm out}
=
\rho_{g_{\rm out}}(\theta)+\ell_{\rm out}L,
\]
then direct substitution gives
\[
t
=
\rho_{g_{\rm in}}(\theta+j\Delta)
+
\ell_{\rm in}L
\]
with
\[
\boxed{
\ell_{\rm in}
=
s\bigl(\ell_{\rm out}-N_{g_{\rm out}}(\theta)\bigr)
+
N_{g_{\rm in}}(\theta+j\Delta)
-
m.
}
\]

This is exactly the IMG1 \`lin\` formula. Thus \`Nwrap\` merely converts
between \(\phi_g\) and its circle representative \(\rho_g\); it does not add
a new covariance or equivariance assumption.

New cross-check:

\`scripts/certify_sw1_m1_nd_img1_species_crosscheck.py\`

It re-derives all \(10\times4=40\) FREE and \(9\times4=36\) HUB
source-species relations from the physical affine equations, then checks:

- direct derivation \(=\) M1-FULL \`free_sr\`/\`hub_sr\`;
- direct derivation \(=\) IMG0 \`free_op_relation\`/\`hub_op_relation\`;
- \(m\) equals the integer \(L\)-wrap above;
- the \`lin\` formula agrees with the lift obtained from an independently
  assembled formal physical-source coefficient vector;
- at exact rational \(\theta\)-samples, the direct coordinate identity
  \[
  t_{\rm phys}
  =
  \rho_{g_{\rm in}}(\theta+j\Delta)+\ell_{\rm in}L
  \]
  holds with \(\ell_{\rm in}\) equal to the IMG1 formula;
- the \(P_0\) effective maps equal IMG0's
  \(\rho_g(\theta+j\Delta)\)-labels.

No IMG1 helper and no \`m1.Nwrap\` are used in these lift cross-checks.

### Review correction: removed tautological lift assertion

An earlier version of the species cross-check contained

\`\`\`python
lin = s * (lout - Nout) + Nin - m
rhs_lin = s * (lout - Nout) - m + Nin
assert lin == rhs_lin
\`\`\`

which is algebraically only \`a == a\` and therefore did **not** independently
verify the lift formula. That assertion has been removed.

The corrected script now separates three levels deliberately:

1. the analytic derivation above establishes the general formula by
   substituting \(\phi_g=\rho_g+N_gL\);
2. a formal coefficient implementation constructs the physical source and
   reconstructed species coordinate by different code paths and derives the
   required \(L\)-lift from their coefficient difference;
3. exact rational-\(\theta\) tests compare the actual physical coordinate
   against \(\rho_{g_{\rm in}}(\theta+j\Delta)+\ell_{\rm in}L\) directly.

Thus the certificate no longer attributes evidentiary force to the former
tautological assertion.

---

## 7. Post-review hardening: second physical implementation

The frozen \`EXPECTED_*\` values in the primary IMG1 script are a
reproducibility lock, not by themselves a second implementation.

Therefore a second code path was added:

\`scripts/certify_sw1_m1_nd_img1_direct_crosscheck.py\`

This script does **not** import the IMG1 effective-ledger script and does
**not** use M1-FULL's \`free_sr\`, \`hub_sr\` or \`Nwrap\` tables.

Instead it:

1. starts from the physical FREE/HUB source equations;
2. re-derives source species and \(j\);
3. determines the source lift directly from the physical source coordinate;
4. builds the reduced \(P_0\) operator state from that physical route alone;
5. compares its global statistics and deterministic state fingerprint with
   the primary IMG1 result.

It intentionally shares the already certified M1-FULL geometry fixture
(64 chamber representatives, B96 wall alphabet and physical row data). Hence
this is a **second implementation cross-check**, not an independent human or
blind cross-model review.

---

## 8. IMG1 transfer from \(r_0=7/2\) to \(3<r<4\)

The original IMG1 certificate is correctly scoped to the reference value
\[
r_0=\frac72.
\]

No silent all-\(r\) exhaustion is claimed.

However, the already promoted C1B2A-TRANSFER supplies the exact data needed
to transport the reduced ledger:

1. corresponding open parameter chambers have the same labeled Tope;
2. corresponding open circle atoms have the same cyclic B96 wall order;
3. therefore the fixed M1 raw ledger activates the same labeled
   FREE/HUB contributions and the same species/lift slots on corresponding
   atoms.

Define the termwise IMG1 reduction map \(\Pi\) on a \(P_0\)-output M1 term by
\[
\Pi:
(g_{\rm in},j,\ell_{\rm in},H/W,\text{coefficient},\text{provenance})
\longmapsto
(\ell_{\rm out},c,\alpha,H/W,\text{coefficient},\text{provenance}),
\]
where
\[
c=
\begin{cases}
\ell_{\rm in},&H,\\
3+\ell_{\rm in},&W,
\end{cases}
\]
and
\[
\boxed{
\alpha^{(r)}_{g_{\rm in},j}(\theta)
=
s\theta+\frac{\eta}{2}L(r)+(sj+\kappa)\Delta(r)
\pmod{L(r)}.
}
\]

The **label**
\[
(s,\eta/2,sj+\kappa)
\]
depends only on the species and M1 shift and is therefore independent of
\(r\). Only its geometric realization uses \(L(r)\) and \(\Delta(r)\).

Consequently \(\Pi\) is an \(r\)-independent combinatorial post-processing of
the transferred M1 term ledger. Hence the existing theorem
\[
\mathrm{M1\text{-}FULL}(7/2)
\Longrightarrow
\mathrm{M1\text{-}FULL}(r),
\qquad 3<r<4,
\]
implies the corresponding **symbolic IMG1 \(3\times6\) ledger formula** on
every corresponding open chamber/atom.

This is not a claim that the numerical operators for different \(r\) are
identical on one fixed circle. Their pullbacks use the actual \(L(r)\) and
\(\Delta(r)\). The claim is only that the labeled reduced formula transfers
under the already proved chamber/atom identification.

### Post-review CI provenance

The post-review hardening was reproduced on GitHub Actions with all three code paths:

- Run: \`33404371913\`
- Job: \`99528171354\`
- Head: \`606882c79062b4fee29271ce8e7897ee08568434\`
- Python: \`3.12.14\`
- Audit blob: \`958da558008319f3ec1053b51b47f53f552ad172\`
- primary IMG1 blob: \`d824bea626e5b97fbad5a75ed51097408f5b6144\`
- species/lift cross-check blob: \`73fdd446e7fd02e05495ff83c5344ddb2e40e3ab\`
- direct physical second-implementation blob: \`dd4aea5b694409adcdad28850eba622ed00e51cc\`
- M1-FULL blob: \`d73993a393b9d076c72bc77cbdf3610f4695c29c\`
- IMG0 blob: \`7f5b11bd80e5387b1c5e8d73be4c0e4140eed8d5\`

PASS results include:

\[
40\ \text{FREE species relations}
\quad+\quad
36\ \text{HUB species relations},
\]
with
\[
\text{direct physical derivation}
=
\text{M1 tables}
=
\text{IMG0 species rules}.
\]


The corrected lift cross-check additionally reports
\[
2508\ \text{exact rational-}\theta\text{ coordinate checks},
\]
together with
\[
\text{lift from independent formal source coefficients}
=
\text{IMG1 lin formula}.
\]

The second physical implementation independently reproduced
\[
117546\ \text{reduced terms},
\qquad
22\ \text{reduced states},
\]
and
\[
\mathrm{SHA256}
=
\texttt{1cffd33529534a15c941b67086217f8f8c47b0cc302cb2cf740b0e08c2ff4474}.
\]

It does not use the primary IMG1 helper, \`free_sr\`, \`hub_sr\`, or \`Nwrap\`.

### Transfer firewall

- the 6144-fold exhaustive run remains a reference-\(r_0\) certificate;
- the all-\(r\) statement is an analytic/combinatorial corollary of
  C1B2A-TRANSFER plus the termwise reduction \(\Pi\);
- no new \(\checkmark[M]\) promotion is created here;
- no injectivity follows.

