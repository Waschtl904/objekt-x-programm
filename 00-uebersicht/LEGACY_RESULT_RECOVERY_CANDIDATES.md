# LEGACY RESULT RECOVERY — CANDIDATE INVENTORY

> **NON-AUTHORITATIVE RECOVERY LIST — NO REGISTRY PROMOTION**
>
> Date: 2026-09-20  
> Repository snapshot scanned: \`main@2c23a4f11db16061c92e3dba2a921edd1f067cc8\`  
> Role: provenance/status archaeology only.  
> This file is **not** a mathematical truth source, does not modify any theorem status,
> and must not be used to infer Object X, global Weil positivity, or RH.

## 0. Recovery rules used

The scan covered the repository tree under

- \`audits/\`
- \`research/\`
- \`papers/\`
- \`00-uebersicht/\`

with priority given to status-bearing paths and records containing or named by
markers such as \`FROZEN\`, \`FINAL\`, \`SEALED\`, \`PROMOTION\`,
\`GREEN\`, \`READY\`, \`CLOSED\`, \`RECONCILIATION\`, and
\`no Registry-Promotion\`.

The purpose is to locate results that are plausibly still mathematically valid
but are missing, stale, or ambiguously represented in
\`00-uebersicht/RESEARCH_STATE.yaml\`.

No proof was rewritten. No old negative branch was reopened. No result below is
promoted by this document.

### Action labels

- **PROMOTE-CANDIDATE** — strong provenance signal; send to independent status audit.
- **PROMOTE-WITH-NARROW-SCOPE-CANDIDATE** — likely valid, but only under an explicit narrow scope.
- **RETAIN-HISTORICAL-COMPANION** — mathematically useful, but likely not needed as an operative survivor.
- **NEEDS-TARGETED-AUDIT** — insufficient to book without a focused check.
- **CERTIFICATE/DIAGNOSTIC-ONLY** — not a theorem-level survivor candidate.
- **SUPERSEDED-SUBRESULT** — mathematically absorbed by a stronger later theorem; retain provenance.

## 1. High-priority status contradictions

Three concrete status drifts were found.

1. **P02 and P03:** their manuscript headers are explicitly \`FROZEN ✓[K/M]\`
   on 2026-08-08, while \`papers/README_papers.md\` still lists both as
   \`Entwurf\`.
2. **P11 fixed-pair Strong Terminal:** the final R43 root-anchor package and
   its exact-blob review establish a scoped strong fixed-pair limit, while the
   new \`RESEARCH_STATE.yaml\` still contains the undifferentiated field
   \`strong_terminal: OPEN\`.
3. **P11/R42 tangential transport:** R42 contains a later freeze addendum
   declaring it independently verified AI-GREEN, but it is absent from the new
   survivor registry even though R43 uses it as an explicit dependency.

These are governance/status discrepancies, not new mathematical proofs.

---

# Candidate inventory

## C01 — P02-ADELIC-WEIL-AMPLITUDE-PORT

- **Original date:** 2026-08-08.
- **Primary path:** \`papers/P02_Adelic_Weil_Amplitude_Port.tex\`.
- **Current blob on scanned main:** \`c3fb26a1b4c1c383834a790d630b0d9df08f714e\`.
- **Historical status:** manuscript title and abstract explicitly say
  \`Patch 3.5 — FROZEN ✓[K/M]\`.
- **Actual scope:** surjective port
  \[
  R_{\rm PW}:\mathcal S_{\rm adel}^{\rm amp}\twoheadrightarrow
  C_c^\infty(\mathbb R;\mathbb C),
  \]
  sesquilinear evenisation, Paley–Wiener test kernel, componentwise complete
  Hermitian Weil form, Hermitian symmetry, normalization matching the literary
  Weil form.
- **Dependencies named by source:** NEU-220k, NEU-250n--r, NEU-252,
  NEU-258 Patch 1; fixed Fourier convention and Haar normalization.
- **Later objection scan:** no later mathematical contradiction located.
  P03 explicitly treats P02 Patch 3.5 as canonical. The later P11/C1 work does
  not negate the port theorem.
- **Registry state:** absent from \`RESEARCH_STATE.yaml\`.
- **Status inconsistency:** \`papers/README_papers.md\` still calls P02
  \`Entwurf\`.
- **Proposed action:** **PROMOTE-CANDIDATE** or at minimum correct the stale
  paper-index status.
- **Does not imply:** positivity of the full Weil form, Object X, RH.

## C02 — P03-HAAR-L2-FIREWALL

- **Original date:** 2026-08-08.
- **Primary path:** \`papers/P03_Haar_L2_Firewall.tex\`.
- **Current blob:** \`b100c0018d587bef445674151ec1c8e7f7c809d6\`.
- **Historical status:** \`Sync Patch 3 — FROZEN ✓[K/M]\`.
- **Actual scope:** on \(L^2(\mathbb R,du)\):
  - semiboundedness of the Weil form iff RH;
  - under RH the Weil form is not closable because the spectral measure is
    purely atomic/singular;
  - explicit non-closability sequence;
  - KLMN does not apply on Haar-\(L^2\);
  - under RH the Weil Hilbert space is the zero-spectrum
    \(\ell^2(\Gamma,m_\gamma)\) realization.
- **Dependencies:** P02 normalization; Alpay–Jorgensen closability criterion;
  Suzuki/Bombieri/Benedetto–Joyner inputs exactly as cited in the manuscript.
- **Later objection scan:** no later mathematical contradiction located.
- **Registry state:** absent.
- **Status inconsistency:** \`papers/README_papers.md\` still calls P03
  \`Entwurf\`.
- **Proposed action:** **PROMOTE-CANDIDATE** with all RH-conditional clauses
  preserved exactly.
- **Does not imply:** an RH-free positive Hilbert realization or RH.

## C03 — P05-RELATIVE-PRIME-CHANNELS-SYN

- **Original date:** 2026-08-09.
- **Primary path:** \`papers/P05_Relative_Prime_Channels_and_Arithmetic_Edge_Geometry.tex\`.
- **Current blob:** \`ceadf51d31b75b237b111876bab4f04e1d664faa\`.
- **Historical status:** \`papers/README_papers.md\` books P05 as
  \`FROZEN ✓[K/M]\`.
- **Scope:** typed relative prime-channel geometry, fixed-\(p\) collision
  structure, transport normal form in audited prime sectors, spectral-measure
  formulation, nonorthogonal prime images, arithmetic prime-power identities.
  Several lift/nondegeneracy/global operator statements remain explicitly open
  or conditional.
- **Dependencies:** Pass-A Group F and the P05 primary/secondary SYN audits.
- **Later objection scan:** no direct contradiction found. P10 preserves P05
  firewalls; later C1 uses a different architecture.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION** unless the registry is
  intentionally expanded to include the full paper-level theorem base.
- **Reason not to auto-promote:** this is a synthesis suite mixing proved,
  partial, conditional, and open items rather than one single theorem.

## C04 — P06-JACOBI-FESHBACH-DIVISOR-GRAPH-SYN

- **Original date:** 2026-08-09.
- **Primary path:** \`papers/P06_Jacobi_Feshbach_and_Divisor_Graph.tex\`.
- **Current blob:** \`bb1e76c2e8492eadbf6ea569ddac0084f1e7dee0\`.
- **Historical status:** P06 is listed \`FROZEN ✓[K/M]\` in the paper index.
- **Scope:** finite Jacobi/Feshbach identities, spectral-measure rather than
  false discrete-eigenbasis interpretation, divisor-graph trace structure,
  and the audited collapse of the NEU-088--90 determinant path.
- **Dependencies:** Group-G Pass-A reconciliation and P06 primary/secondary
  SYN audits.
- **Later objection scan:** no direct contradiction found. Later work retains
  the firewall “finite Feshbach identity ≠ global Schatten/Fredholm limit”.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION**.

## C05 — P07-WEIL-FORM-STATISTICS-SYN

- **Original date:** 2026-08-09.
- **Primary path:** \`papers/P07_Weil_Form_Statistics.tex\`.
- **Current blob:** \`8bf848b975b77d646806e4f79b0ae1fac1dd46ca\`.
- **Historical status:** \`FROZEN ✓[K/M]\` in the paper index.
- **Scope:** statistical/correlation and Herglotz interfaces of the Weil-form
  program, with conditional RH/SPC portions kept conditional.
- **Important later re-audit:**  
  \`audits/AUDIT-2026-08-09_P07_Externcheck_GM_aN_Targeted-Reaudit.md\`,
  blob \`2c63abb17a6a8b76ebe4f1f8e670a085ce5b5e1e\`, rejects a supposed
  Goldston–Montgomery counterfinding and adds the valid necessary condition
  \(a_N\to0\) under local-uniform Herglotz convergence.
- **Later objection scan:** no rollback of P07 found; the targeted re-audit
  says explicitly that P07 is not mathematically rolled back.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION**.

## C06 — P08-RENORMALIZED-PRIME-OPERATORS-SYN

- **Original date:** 2026-08-09.
- **Primary path:** \`papers/P08_Renormalized_Prime_Operators_and_Finite_Part_Structures.tex\`.
- **Current blob:** \`a06b235fc94852bf923cd9d8444e25c82420d65b\`.
- **Historical status:** \`FROZEN ✓[K/M]\` in the paper index.
- **Pass-A seal:**  
  \`audits/AUDIT-2026-08-09_P08_PassA_FINAL_SEAL.md\`,
  blob \`a2206c32e6d3fdf9bddf733eae6004c9bf0c0643\`; this earlier seal
  was procedural and explicitly preceded the SYN freeze.
- **Scope:** renormalization diagnostics, conditional relative Schatten
  statements, exact Mellin/Mangoldt channel distinctions, finite-part
  firewalls. Many operator-realization claims remain conditional/open.
- **Later objection scan:** no direct rollback found.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION**.

## C07 — P09-BC-HOCHSCHILD-CHARGED-COHOMOLOGY

- **Original date:** 2026-08-09.
- **Primary path:** \`papers/P09_BC_Hochschild_and_Charged_Cohomology.tex\`.
- **Current blob:** \`ec70c86fb30921de330a364a7670e611b8450407\`.
- **Historical status:** manuscript says **SYN FINAL AUDITED**.
- **Pass-A seal:**  
  \`audits/AUDIT-2026-08-09_P09_PassA_FINAL_SEAL.md\`,
  blob \`41b55bff2d7a6f53895a6aa8d1e68e2f686cd771\`.
- **Core scope:** neutral algebraic Hochschild-4 class; charged corrected
  \(HH^1\) class in the stated coefficient module; nontrivial charged
  \(HH^4\) cup in \(\mathfrak M_{\rm glob}^{\log}\); KMS/twist and canonical
  rotation no-go statements with explicit firewalls.
- **Later objection scan:** no direct contradiction found. The program later
  moved to P11/global coupling; P09 does not claim a Weil/Gram realization.
- **Registry state:** absent and not listed in the old paper index table.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION** or
  **PROMOTE-WITH-NARROW-SCOPE-CANDIDATE** if the registry is intended to
  represent all durable project theorems.

## C08 — P10-CANONICAL-GLOBAL-COUPLING-NOGO-SUITE

- **Original date:** 2026-08-09.
- **Primary path:** \`papers/P10_No-Go_Theorems_for_Canonical_Global_Coupling.tex\`.
- **Current blob:** \`1c905c39a8e5c168cf2367a6311253f88a89fb5b\`.
- **Final seal:**  
  \`audits/AUDIT-2026-08-09_P10_PassA_FINAL_SEAL.md\`,
  blob \`af715c9461fb868056fbccaa3fee40fbf42969d5\`.
- **Historical status:** final seal books **P10 — SYN FROZEN ✓[K/M]**.
- **Scope:** 53 scoped no-go/supersession/firewall slots and 29 explicitly
  open/conditional slots; includes the corrected NEU-088--90 determinant
  collapse and several route-specific exclusions.
- **Later objection scan:** no wholesale rollback found. Later C1 work is
  consistent with the central P10 firewall that local/finite models do not
  automatically produce the global positive geometry.
- **Registry state:** absent except for newer, separately proved C1 no-go
  entries.
- **Proposed action:** **PROMOTE-WITH-NARROW-SCOPE-CANDIDATE** as a historical
  no-go suite, or retain P10 as the canonical companion source rather than
  duplicating 53 registry entries.
- **Important firewall:** do not collapse \`SUPERSEDED\`,
  \`✓[M]_neg\`, and \`OPEN\` into one negative status.

## C09 — P11-FINITE-HORIZON-CANDIDATE-GEOMETRY-FREEZE

- **Freeze date:** 2026-08-21.
- **Freeze record:** \`audits/P11_FREEZE_RECORD_2026-08-21.md\`.
- **Freeze-record blob:** \`d78ac4a7b04542ccd541d9e5d5153bdb5e58491e\`.
- **Validated freeze tree:** \`main@3d60e19697420040ea8fede5dd5fc87703dfe92e\`.
- **Current manuscript path:** \`papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex\`.
- **Current manuscript blob:** \`f2a95fc6cdf4f5645af09ab03c159e5d54feda0b\`
  (do **not** substitute this later blob for the freeze pin without review).
- **Historical status:** \`P11 FROZEN ✓[K/M]\` at explicitly stated
  finite-horizon / Candidate-Geometry scope.
- **Core scope:** source conditioning, Gamma graph spaces, finite-window
  Feshbach/Schur geometry, exact graph transitions/pullbacks, positive terminal
  metrics, same-terminal normalized isometries, finite-window compactness and
  Schatten no-go, pure-Gamma Mosco/strong-resolvent backbone, direct terminal
  bridge and audited route-specific diagnostics.
- **Later developments:** R42/R43 later close parts that the freeze record
  still listed as open (notably fixed-pair strong terminal transport).
  This is an extension, not a contradiction of the frozen finite-horizon core.
- **Registry state:** no single P11-frozen-core survivor.
- **Proposed action:** **PROMOTE-WITH-NARROW-SCOPE-CANDIDATE** or
  **RETAIN-HISTORICAL-COMPANION**. Any survivor must pin the actual freeze
  tree/record, not silently use the later manuscript blob.
- **Does not imply:** P11-wide global Object X, RH, or the new C1
  unbounded-horizon compatibility.

## C10 — P11-R27-CONSTRAINED-GAMMA-MOSCO-AND-INVERSE-ROOT

- **Original date:** 2026-08-15.
- **Primary path:**  
  \`audits/P11_REFEREE_E2E_R27_CONSTRAINED_GAMMA_MOSCO_LIMIT_2026-08-15.md\`.
- **Current blob:** \`5e51053f4124204be25798ae822f80ca63b26108\`.
- **Historical status inside source:**
  - R27-A Mosco limit: \`✓[M]\`;
  - R27-B baseline-whitened constrained limit: \`✓[M]\`;
  - R27-C concrete resolvent strong limits: \`✓[M]\`;
  - R27-D concrete inverse-square-root strong limits: \`✓[M]\`.
- **Scope:** fixed source graph spaces, constrained Gamma limit on the
  codimension-one hyperplane, strong resolvent/inverse-root limits.
- **Later use:** explicitly imported by R42 and the R43 strong-terminal stack.
- **Later objection scan:** no direct contradiction found; R27 itself correctly
  says it does not settle moving polar factors or Strong Terminal by itself.
- **Registry state:** absent.
- **Proposed action:** **PROMOTE-CANDIDATE** if R42/R43 are promoted, because
  it is a named structural dependency rather than merely historical context.

## C11 — P11-R42-TANGENTIAL-STRONG-TRANSPORT

- **Original document date:** 2026-09-02, with later freeze addendum.
- **Primary path:**  
  \`audits/P11_REFEREE_E2E_R42_DUAL_NORMAL_DIRECTION_AND_ETA_BLINDNESS_2026-09-02.md\`.
- **Current blob:** \`804d9040db4867f5f3967fbccc62e189492a7e2e\`.
- **Historical status evolution:** the file begins as
  \`AI-GREEN internal candidate only\`, but its later audit/freeze section
  explicitly states:
  \[
  \text{R42 FROZEN — independently verified AI-GREEN.}
  \]
- **Key theorem:** R42.51 gives strong convergence of the genuine future
  transport on the infinite-dimensional closed codimension-one hard-constraint
  hyperplane \(H_R^0\).
- **Additional role:** R42.60 reduces full fixed-pair Strong Terminal/C6 to
  the orbit of one source-normal vector.
- **Dependencies named by source:** frozen R38, R40, R41 and canonical R24/R27;
  R27 is separately listed above.
- **Later objection scan:** no later mathematical rebuttal found. R43 explicitly
  imports R42.51 as the tangential half of the final strong fixed-pair result.
- **Registry state:** absent.
- **Proposed action:** **PROMOTE-WITH-NARROW-SCOPE-CANDIDATE** after GPT2
  checks the final freeze section and its bound dependency pins.
- **Does not imply:** full-space strong convergence by itself, uniformity in
  \(R,S\), operator-norm convergence.

## C12 — P11-FIXED-PAIR-STRONG-TERMINAL

- **Original date:** 2026-09-07.
- **Primary theorem path:**  
  \`audits/P11_R43_POSITIVE_ROOT_ANCHOR_STRONG_TERMINAL_2026-09-07.md\`.
- **Final theorem blob:** \`a3229f0882a31046434389e5915badea686dae73\`.
- **Exact-blob review package:**  
  \`audits/R43_C6_ROOT_ANCHOR_REVIEW_2026-09-07/README.md\`,
  blob \`e590e37e53726c6c9ce5006480dc247ac122203d\`.
- **Definition basis named by package:**  
  \`55a3a1617513cc5d82c47d0cfd606c6b0894c984\`.
- **Historical status:** theorem file explicitly says no Registry-Promotion;
  review concludes **READY / SCOPED GREEN** and records exact reviewed blobs.
- **Exact scope:**
  for every fixed \(0<R<S<\infty\), on the original odd P11 graph spaces,
  \[
  W_{R,S}^{[U]}\varepsilon_R\to\varepsilon_S
  \quad\text{strongly as }U\to\infty,
  \]
  and together with R42.51,
  \[
  W_{R,S}^{[U]}(v+a\varepsilon_R)
  \to W_{R,S}^{(0)}v+a\varepsilon_S.
  \]
  Hence the fixed-pair C6/Strong-Terminal step is closed relative to the
  named P11/R42 inputs.
- **Review hardening:** the destructive review found a real older
  null-extension boundary-Lipschitz defect, replaced it with the stronger
  boundary-trace repair, and the final review says no open finding remains in
  the checked five-file package.
- **Later objection scan:** no later mathematical rebuttal found. Later
  2026-09-19/20 overview files calling “Strong Terminal OPEN” trace to status
  carry-forward and do not supply a new counterexample or proof failure.
- **Current registry conflict:** \`global_status.strong_terminal = OPEN\`.
- **Proposed action:** **PROMOTE-WITH-NARROW-SCOPE-CANDIDATE — HIGHEST PRIORITY**.
- **Required future name:** use a scoped ID such as
  \`P11-FIXED-PAIR-STRONG-TERMINAL\`, never an unqualified
  \`STRONG-TERMINAL\`.
- **Does not claim:**
  - uniform convergence in \(R,S\);
  - operator-norm convergence;
  - a rate;
  - the new C1 unbounded-terminal-horizon compatibility;
  - global Object X or RH.

## C13 — P11-R32-PROMOTED-TRANSVERSALITY-SUITE

- **Promotion date:** 2026-08-25.
- **Canonical promotion record:**  
  \`audits/P11_R32_PROMOTION_RECORD_2026-08-25.md\`.
- **Current blob:** \`3e83d5d35b83effdd6175cde702682663053b115\`.
- **Historical status:** explicit project authorization:
  “promote die GREENen Resultate gesammelt”.
- **Promoted components recorded there:**
  - CTX-1 — horizon-adaptive central transversality, \`✓[M]_part\`;
  - NS-1a — first noncentral invisible shell, \`✓[M]\`;
  - NS-1 — first noncentral-shell transversality, \`✓[M]_part\`;
  - SS-1a — second noncentral boundary shell, \`✓[M]\`;
  - SS-L — exact 10-of-11 word classification, \`✓[M]\`;
  - SP-1 — scalar profile compression, \`✓[M]_part\`;
  - ST-1 — second noncentral-shell transversality, \`✓[M]_part\`.
- **Scope:** explicit R32 shell/transversality strata only; the record itself
  contains a hard “not promoted” section for stronger global claims.
- **Later developments:** many later R32/SW1 candidates/no-gos refine other
  classification/globalization routes. This scan located no direct statement
  that the seven explicitly promoted results above were mathematically
  revoked.
- **Registry state:** absent.
- **Proposed action:** **NEEDS-TARGETED-AUDIT** as a suite before any survivor
  booking, because the later R32 branch is large and contains method-specific
  no-gos. If retained, preserve the individual \`_part\` scopes.

## C14 — P12-A15.1-INJECTIVITY-AND-LOCAL-OVERLAP-SUITE

- **Primary consolidated manuscript:**  
  \`papers/P12_Adelic_Hub_Injectivity_Program.tex\`.
- **Current manuscript blob:** \`f3d317f282d7219156478adf0bb292adb5704e4a\`.
- **Scope in manuscript:** global kernel triviality in the established P12
  strata and a sequence of exact local low-radius overlap certificates.
- **Explicit promotion chain:**
  - Round 22 restricted-tail all-\(R\): blob
    \`c9cc8ec33cb6a1ebd26d68770a0fb7ce492477bb\`, \`✓[M]\`;
  - Round 23 C42 overlap seed:
    \`9fee24f3a205650557d1af3f4b6e2889a7900962\`, \`✓[M]_part\`;
  - Round 24 C42/C44:
    \`61cd566cf55cb6ff3b8336372878e9c9b9210467\`, \`✓[M]_part\`;
  - Round 25 M92 horizon-wall local circuit:
    \`bcd2daa2bca8ab7b9f1c46d7b6be9592e52d87f2\`, \`✓[M]_part\`;
  - Round 26 glued M92 corridor:
    \`9df867dafae47f21a4002e34cdd152905eb3d0fe\`, \`✓[M]_part\`;
  - Round 27 residual shadow atlas + one-sided M43 shell:
    \`c14a0a5a28cb4f86adcda3bcb1eb6f2961e720e3\`, \`✓[M]_part\`;
  - Round 28 central M68 double-horizon box:
    \`443c92a201ac1aa3b195eb198524051f681d8c30\`, \`✓[M]_part\`;
  - Round 29 epsilon-invariant M68 bridge:
    \`c56ca3a19740fa95d9cd1e6ad9692f296e76d00e\`, \`✓[M]_part\`.
- **Later objection scan:** current P12 manuscript still incorporates and
  states these promoted local certificates. No direct revocation found.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION** or
  **PROMOTE-WITH-NARROW-SCOPE-CANDIDATE** if the registry is to include
  non-current but durable theorem suites.
- **Important firewall:** local round promotions are not a global descent
  theorem below the remaining overlap region and imply no Strong Terminal,
  Object X, or RH.

## C15 — P11-AR1-WEIL-TAIL-ALGEBRA

- **Original date:** 2026-09-12.
- **Primary path:**  
  \`audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md\`.
- **Current blob:** \`a9591ad1153250b88400967fc899f6136a266b7d\`.
- **Historical status:** consolidation document; explicitly “kein
  Registry-Eintrag, kein Freeze”.
- **Durable exact subresults marked \`✓[M]\`:**
  - exact prime-power coefficient ledger
    \(C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4}\);
  - normalized AR(1)/Kac–Murdock–Szegő structure;
  - exact tail transform \(T_q^*T_q+uu^*=R_q\);
  - exact P11 rest-side Weil-tail normal form.
- **Later objection scan:** the same document itself withdraws several
  overinterpretations (e.g. wrong operator-order “hub = nonunitarity”
  reading). Later OX-GEN/POS-DIL work builds on the surviving algebraic part.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION**; if promoted at all,
  promote only the explicit algebraic identities, not the discarded
  interpretations.

## C16 — P11-OX-GEN-A-COMMON-EXPONENTIAL-GENERATOR

- **Original date:** 2026-09-13.
- **Primary path:**  
  \`audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md\`.
- **Current blob:** \`9060a3b8cd7d4116c6a5b57582d3400568bc3e85\`.
- **Historical status:** theorem-level internal audit, no Registry-Promotion.
- **Scope:** compactly supported test functions / zero extensions; Suzukis
  \(r_0\)-part only; \(r_1\) and scalar block remain open.
- **Exact subresults marked \`✓[M]\`:**
  - \(\mathcal ET_t=\rho(t)\mathcal E\);
  - \(\mathcal EK_n=D_n\mathcal E\);
  - \(r_0\) is the character form of the same rank-2 translation
    representation;
  - exact \(r_0(\log n)=-4\lambda_n^2\);
  - polarized rank-2/parity form and prime-channel anti-covariance.
- **Later objection scan:** POS-DIL-1 and POS-DIL-2 explicitly import this
  structure; no direct contradiction found. The later coupled C1 mediator is
  strategically different and does not by itself refute the rank-2 algebra.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION** or
  **PROMOTE-WITH-NARROW-SCOPE-CANDIDATE** after GPT2 checks the exact
  rank-2 scope.

## C17 — P11-POS-DIL-1-PRIME-MOMENT-HILBERTIZATION

- **Original date:** 2026-09-13.
- **Primary path:**  
  \`audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md\`.
- **Current blob:** \`88ebb26ad9bb4a50a33f47fb8fa1f3acb56efb71\`.
- **Historical status:** theorem-level internal audit; no Registry-Promotion.
- **Basis named by source:** \`main@48d1656cdf9be877e57ca1187d5679733603f295\`.
- **Scope:** OX-GEN rank-2 plane and \(r_0\) only.
- **Core results:** symmetry rigidity \(M=tI\), sharp minimal positive
  companion \(M_{\min}=I\), exact prime-moment feature realization, plus the
  scoped no-go for a nonzero positive \(\rho(t)\)-invariant metric on the same
  rank-2 plane.
- **Later objection scan:** POS-DIL-2A tests the next predeclared shorting gate;
  it does not invalidate POS-DIL-1.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION**.

## C18 — P11-POS-DIL-2A-UNIT-GAIN-SHORTING-NOGO

- **Original date:** 2026-09-13.
- **Primary path:**  
  \`audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md\`.
- **Current blob:** \`7ed3ed6e08b4cef1f8f17c9394b22c08d832f3ed\`.
- **Basis named by source:** \`main@ecf8216f3d66c9b0be6636afea216bdfd53142ac\`.
- **Historical status:** theorem-level internal no-go, \`×[M]\` for the
  predeclared unit-gain feature-shorting class.
- **Exact scope:** \(a=1/2\), localized positive feature form \(G_{1/2}^+\);
  excludes a contractive unit-gain target realization of the \(r_0\) rank-2
  mass inside that unaugmented feature geometry.
- **Later developments:** POS-DIL-2B/2C add intrinsic exterior-shell mass and
  therefore escape the excluded class. This confirms the no-go is
  class-specific rather than refuted.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION** as a scoped no-go.
- **Does not exclude:** augmented feature geometry, gain \(>1\), or the later
  coupled C1 mediator.

## C19 — P11-POS-DIL-2C-EXTERIOR-SHELL-GAUGE-AND-R0-ABSORPTION

- **Original date:** 2026-09-13.
- **Primary final path:**  
  \`audits/P11_POS_DIL_2C_EXACT_SHELL_GAUGE_R0_ABSORPTION_2026-09-13.md\`.
- **Current blob:** \`b69e2b503c43d8d15356219306df4bb6366aa8ab\`.
- **Basis named by source:** \`main@6415bbf5a1a78974213c8b2222b0950e8a4dd070\`.
- **Precursor radius theorem:**  
  \`audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md\`,
  blob \`a02f798b7f088ea7949fa96c1e12fb6c167e4fb3\`.
- **Earlier special case:** POS-DIL-2B at \(a=1/2\), blob
  \`5373a7649e82cac427428902be8cf6b15a6352c8\`.
- **Historical status:** theorem-level internal audit; no Registry-Promotion.
- **Scope:** localized Suzuki/Weil form for \(0<a\le1\), \(H_0^1(-a,a)\)
  zero-extended test class.
- **Core exact results:**
  - exterior channels with \(c_n>a\) satisfy
    \(H_{a,J}=2\sum_{n\in J}\Lambda(n)n^{-1/2}\,I\);
  - exact exterior-shell gauge leaves the full localized Weil form unchanged;
  - first exterior shell gives \(A_a^{out}\succeq\mathcal E^*\mathcal E\);
  - exact positive absorption \(P_a^{(0)}=A_a^{out}-R_0\succeq0\);
  - remaining scalar block and \(R_1\) are not closed.
- **Later objection scan:** no direct mathematical contradiction found.
  The later C1 mediator is a different positive architecture and became the
  operative path.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION** or
  **NEEDS-TARGETED-AUDIT** if considered for active reuse.
- **Supersession note:** POS-DIL-2B is a **SUPERSEDED-SUBRESULT** of this wider
  radius/gauge package, not a false theorem.

## C20 — P11-R43-LOCAL-O1-AND-JUMP-DECAY-AUXILIARIES

- **Original date:** 2026-09-07.
- **Local-O1 path:**  
  \`audits/P11_R43_O1_LOCAL_INTERVAL_UNIFORMITY_2026-09-07.md\`,
  blob \`03f9cf519fab66b3d00a5f60690d967adbaa5e95\`.
- **Jump-decay/orientation path:**  
  \`audits/P11_R43_HUB_JUMP_DECAY_AND_CONDITIONAL_ORIENTATION_2026-09-07.md\`,
  blob \`501ea5acfdcbb812ba25534b9d4503ab307a18aa\`.
- **Historical status:** analytic theorem drafts; Local-O1 explicitly says no
  independent GREEN booking, and the jump-decay document says no automatic
  status promotion.
- **Scope:** local cell continuity / one-sided strong limits of the terminal
  ingredients and quantitative decay of actual activation jumps; orientation
  closure remains conditional on tightness.
- **Relation to later R43 result:** the direct positive-root-anchor proof of
  C12 bypasses the previously open global tightness budget. Therefore these
  auxiliary theorems are no longer required to justify C12.
- **Registry state:** absent.
- **Proposed action:** **RETAIN-HISTORICAL-COMPANION**; do not promote merely
  because C12 later succeeds by another route.

---

# Explicit non-survivor / diagnostic findings from the same scan

## D01 — OX-GRAM-GATE2-FINITE-ARB-DIAGNOSTIC

- **Path:** \`audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md\`.
- **Blob:** \`7b9fe1b3432b17be37529eb9dd65675ea8aef9d0\`.
- **Finding:** 42/42 finite Arb-Cholesky tests were reported positive, but the
  document itself identifies unresolved certificate-hardening issues:
  Bernoulli-tail enclosure, float-derived cutoff/endpoint bounds, and direct
  interval positivity semantics.
- **Classification for recovery:** **CERTIFICATE/DIAGNOSTIC-ONLY**.
- **Do not promote** the finite positivity evidence as an infinite-dimensional
  theorem.

## D02 — POS-DIL-2B-SPECIAL-RADIUS

- **Path:** \`audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md\`.
- **Blob:** \`5373a7649e82cac427428902be8cf6b15a6352c8\`.
- **Finding:** theorem-level special case at \(a=1/2\).
- **Later stronger result:** C19/POS-DIL-2C proves the radius statement for all
  \(0<a\le1\) and then gives exact shell-gauge bookkeeping.
- **Classification for recovery:** **SUPERSEDED-SUBRESULT**, not false.
- **Action:** retain as provenance; do not create a redundant survivor if C19
  is retained.

---

# Registry-reconciliation questions for GPT 2

The independent status audit should answer, for every candidate above:

1. Does the bound blob correspond to the final reviewed theorem text?
2. Is the historical GREEN/FROZEN/PROMOTED marker mathematical or merely
   documentary/technical?
3. Are all named dependencies still valid at their pinned scope?
4. Is there any later **concrete mathematical** objection, rather than only a
   later status file that carried an older OPEN value forward?
5. Was only a method superseded, or was the theorem itself invalidated?
6. Are room, topology, quantifiers, parity, horizon, and uniformity explicit?
7. Should the result be an operative survivor, a historical companion, or no
   registry entry at all?

## Special mandatory check

For C12, do not use the short label “Strong Terminal” without qualifiers.

The exact distinction to preserve is

\[
\boxed{
\text{P11 fixed-pair strong terminal on the original odd graph spaces}
}
\]

versus

\[
\boxed{
\text{new C1 unbounded-terminal-horizon compatibility across prime-power walls}.
}
\]

C12 concerns the first. The second remains open.

---

# Recovery-scan conclusion

This inventory found **at least three genuine status-reconciliation problems**
(P02, P03, and P11 fixed-pair Strong Terminal/R42 dependency), plus a broader
set of old explicit promotions and theorem-level packages that are absent from
the new compact registry.

That does **not** mean all candidates should be promoted.

The next step is independent adversarial classification. No registry file,
generated state view, proof, or current research front has been changed by this
scan.
