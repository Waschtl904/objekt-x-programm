# Prolate-Salvage-Audit — Independent Point-by-Point Verification

**Date:** 2026-08-22 (fifth round)
**Auditor:** Perplexity, adversarial mode
**Trigger:** User request to salvage reusable building blocks from
two earlier prolate repositories rather than resurrect the old
Prolate→Weil→RH narrative.
**Sources audited:**
- `Waschtl904/prolate-primes-paper` (17 papers, prime-based PSWF
  Gram programme, targeting Connes–Consani–Moscovici arXiv:2511.22755)
- `Waschtl904/prolate-gram-coercivity` (~20 papers, prolate Gram
  coercivity + Airy universality)

**Charge:** For each of six User-nominated claims (three positive
salvage candidates, three critical verdicts), independently verify
against the actual repository text before any decision to import
into the Objekt-X programme.

**Meta-rule:** No `✓[M]` booking in the P11/P12 programme based on
any old-repo lemma unless the lemma is re-verified in the P11/P12
convention with horizon-legality and type-compatibility explicitly
checked.

## 0. Overall verdict

All six User claims independently verified as correct on the merits.
Distinctions and refinements are noted per item.

## 1. Kandidat A — Gram $G = M^*M > 0$ from PSWF evaluation

**Location:** `prolate-primes-paper/paper1_FINAL.tex`, Lemma B
(Unisolvency and Gram Positivity), lines 513–536.

**User claim:** $\checkmark[M]$; sauber, Prime-Arithmetik nicht
verwendet.

**Independent verification:** Confirmed. The lemma proves $G = M^*M$
positive definite from three inputs:
1. $V_N$ is a Chebyshev system (Karlin–Studden 1966, Slepian 1978,
   Bonami–Karoui);
2. Any $N$ pairwise-distinct sampling points give $\operatorname{rank}
   M = N$;
3. Hence $G = M^*M \succ 0$.

The paper itself makes the firewall explicit in Remark 4.15:
"Lemma B uses only pairwise distinctness of $\mathbf{p}$. The
arithmetic of primes plays no role here."

**Refinement of user claim:** The lemma is Standard Chebyshev-system
theory. Its value is not the lemma itself (which is textbook) but
the **design pattern**: arithmetic feature vectors →
$\mathrm{Ev}^*\mathrm{Ev}$ → positive finite Gram.

**Import recommendation:** As a **design pattern**, not a theorem.
Book as a programme-note in Objekt-X, not as a $\checkmark[M]$
theorem in P11/P12. Any concrete P12 use requires new statement,
new proof, new horizon check.

**Verdict:** User-claim confirmed with refinement.

## 2. Kandidat B — Paper XII Residual/Gap principle

**Location:** `prolate-primes-paper/paper12_DRAFT.tex`, Theorem
`thm:mechanism` (Exact Mechanism Factorization), lines 736–793,
combined with Theorem `thm:abstract` (Main Principle), lines
933–944.

**User claim:** $\checkmark[M]$ as abstract theorem; potentially
useful for P11 transport.

**Independent verification:** Confirmed. The theorem factors
$R_k = \|(A_k - A)\varphi\|/\gamma_k + |\lambda_k - \lambda|/\gamma_k$
through three exact steps:
- (M1) Rank-1 scalar reduction: $\|P - Q\| = \|(I - Q) u\|$ for
  rank-1 projections $P = u \otimes u$, $Q = v \otimes v$ (Bhatia
  1997, Ch. 1);
- (M2) Spectral gap resolvent bound: $\|(A_k - \lambda_k)^{-1}
  |_{\mathrm{ran}(I - P_k)}\| \le 1/\gamma_k$;
- (M3) SOT residual triangle: $\|(A_k - \lambda_k)\varphi\|
  \le \|(A_k - A)\varphi\| + |\lambda_k - \lambda|$, using
  $(A - \lambda)\varphi = 0$.

All three steps are standard perturbation-theoretic building blocks
(Kato / Reed–Simon / Davis–Kahan lineage). The paper's contribution
is the **framing** as direction-sensitive vs. norm-based
perturbation (Remark 5.10, `rem:input-comparison`), and the
non-embeddability observation (Remark 5.12,
`rem:nonreducibility`).

**Structural caveat (meta-audit).** For a P11 application, one
would need to verify:
1. Existence of an isolated simple eigenvalue $\lambda$ of the
   limit operator $W^{[\infty]}_{R,S,-}$;
2. A corresponding isolated simple eigenvalue branch $\lambda_k$
   for the approximants, with spectral gap $\gamma_k > 0$ and
   $\lambda_k \to \lambda$;
3. The sharp relative estimate
   $$
   \frac{\|(A_k-A)\varphi\|+|\lambda_k-\lambda|}{\gamma_k}\to 0.
   $$
   In particular, a uniform bound $\gamma_k\ge\gamma_0>0$ is
   sufficient but **not necessary**: $\gamma_k$ may tend to zero
   provided the numerator is $o(\gamma_k)$;
4. Identification of the correct test vector $\varphi$.

None of these are currently established in P11. The theorem is a
**tool**, not a technical step forward.

**Import recommendation:** As a candidate **attack strategy** for
the P11 strong-transport open problem, with the explicit
prerequisite that the four hypotheses above be verified in the
P11 setting. Book as a research-direction note, not a technical
$\checkmark[M]$ import into the P11/P12 canon.

**Verdict:** User-claim confirmed. Meta-caveat added: import is
programmatic, not technical.

## 3. Kandidat C — NEU-189 Type-Firewall

**Location:** `prolate-primes-paper/NEU-189_typaudit_operatorrealisierung.md`,
full file (163 lines).

**User claim:** $\checkmark[M]$ as methodological firewall; direct
import into Objekt-X foundations.

**Independent verification:** Confirmed with strong endorsement.
The audit establishes:
- $\Omega_p \in Z^4(A, A) = \operatorname{Hom}_{\mathbb C}(A^{\otimes 4}, A)$
  is a 4-linear map, not an operator;
- Even with a faithful representation $\pi : A \to B(\mathcal{H})$,
  one only obtains a 4-linear operator-valued map
  $A^{\otimes 4} \to B(\mathcal{H})$, not a distinguished operator
  in $B(\mathcal{H})$;
- A canonical operator $\rho_{\mathrm{op}}([\Omega_p])$ requires
  one of four minimal structures: fixed evaluation points, an
  operator-valued 4-cycle, a universal differential calculus with
  spectral triple, or a Kasparov / correspondence product;
- Without such a contraction structure, the question of
  representative independence is not even well-posed.

This is exactly the type-discipline used throughout P11/P12: a
statement of the correct type must precede any theorem about it.

**Import recommendation:** **Direct import** as a general Objekt-X
firewall rule. Add to the P12 preamble (or a shared
`_firewalls.md`) as:

> **Firewall Type-Realisierung** (aus NEU-189): Ein Kohomologie-
> Kozykel $[\omega] \in HH^*(A, A)$ ist noch kein Operator. Eine
> $\checkmark[M]$-Aussage über $\rho_{\mathrm{op}}([\omega])$
> erfordert die vorherige Spezifikation einer typisierten
> Kontraktions- oder Realisierungsstruktur (feste Auswertungs-
> punkte, Vierzyklus, spektrales Tripel, Kasparov-Produkt).

**Verdict:** User-claim confirmed.

## 4. Kritik 1 — Prime-T.2 exponential quadrature

**Location:** `prolate-primes-paper/paper1_FINAL.tex`,
Proposition `prop:T2` (Condition (T.2) for prime sampling),
lines 566–745; and the setup Definition `def:T2`, lines 241–274.

**User claim:** $\times[M]$ as proved; Voronoi weights missing;
polynomial-to-exponential upgrade unjustified.

**Independent verification:** Confirmed.

The error matrix is defined (line 247) as
$E_N := G_{VM} - G_c^{(N)}$, where $(G_c^{(N)})_{mn} := \lambda_n(c)
\delta_{mn}$, and the paper claims (lines 255–259):

> "$G_c^{(N)}$ is the continuous analog of $G_{VM}$: it is exactly
> what $G_{VM}$ would equal if the discrete sum $\sum_{j=1}^N$ were
> replaced by the integral $\int_{-T}^T$. Hence $E_N$ measures the
> quadrature error between discrete sampling and Lebesgue
> integration."

**This is the core error.** The discrete sum $\sum_j \psi_m(p_j)
\overline{\psi_n(p_j)}$ (no weights) is **not** the discrete
approximation of $\int_{-T}^T \psi_m \overline{\psi_n}\, dx$. A
proper Voronoi quadrature would carry cell widths $|I_j|$ as
weights:
$$\sum_j |I_j|\, \psi_m(p_j) \overline{\psi_n(p_j)} \;\approx\;
\int \psi_m \overline{\psi_n}\, dx.$$
No general asymptotic for the **unweighted** sum is asserted here;
any statement such as a mean-gap rescaling would require its own
normalization/measure argument. It is not needed for the present
$\times[M]$ verdict.

The subsequent Off-Diagonal analysis (Step 2, lines 605–637) uses
$\sum_j |I_j|^2 \|g'\|_\infty$ as if it bounds
$|\sum_j g(p_j) - \int g|$; but this bound applies to the
**weighted** quadrature $\sum_j |I_j| g(p_j) - \int g$, not to the
unweighted sum. The identity is dimensionally mismatched.

Additionally, Step 3 (lines 673–698) manufactures exponential
decay by squeezing the Kulikov *lower* bound
$1 - \lambda_n \ge e^{-2\delta c}$ against the Landau–Widom
*upper* bound $1 - \lambda_n \le C(\varepsilon) e^{-\eta c}$
with $\eta > 2\delta$, then folding this into $\|\psi_n\|_\infty$
control. The bound derivation is not transparent, and even
granting the intermediate steps, the resulting exponential rate
would only be valid *if* the Voronoi-quadrature framing were
correct, which it is not.

**Import recommendation:** Do not import. The $E_N$ object itself
is well-defined; the claimed $\|E_N\|_2 \le \varepsilon_N =
O(e^{-\delta' N})$ is not established.

**Verdict:** User-claim confirmed.

## 5. Kritik 2 — O4-B2 Airy off-diagonal decay, edge uniformity

**Location:** `prolate-gram-coercivity/O4_B2_airy_offdiag_decay.tex`,
Lemma `lem:offdiag` (Off-diagonal Airy decay), line 80, with proof
occupying sections `sec:phase`, `sec:statphase`,
`sec:discretisation`.

**User claim:** $?[O]$; $t_n = \cos(\pi n/(2N)) \to 0$ at edge
$n \to N$ breaks the required uniform positive lower bound.

**Independent verification:** Confirmed.

The claim in Lemma `lem:phasescaling` (lines 214–222) asserts
$\inf_{p \in [-1,1]} |\Psi(p)| \ge c_\Psi > 0$ uniformly in
$m \in \mathcal{I} = [(1-\delta)N, N) \cap \mathbb{Z}$. The
associated proof (lines 224–231) is a "Proof sketch — TODO"
citing the eigenvalue-spacing bound $\kappa_0 c^{-1}$ from
`ass:gap`.

**Structural issue:** For $n \in \mathcal{I}$, one has $t_n
= \cos(\pi n/(2N))$. At $n = N$: $t_N = 0$; at $n = (1-\delta)N$:
$t_n = \sin(\pi\delta/2) > 0$. Hence $t_n$ takes all values in
$(0, \sin(\pi\delta/2))$ as $n$ ranges over $\mathcal{I}$. Any
quantity depending on $t_n$ as a scale (which $\Psi(p)$ does via
the Langer variable $\zeta_n$) cannot be uniformly bounded below
by a $t_n$-independent constant.

Furthermore, the proof of Proposition `prop:statphase` (van der
Corput with cubic phase, lines 190–210) and the derivative bound
in Lemma `lem:Fprime` are both marked "Proof sketch — TODO." The
overall Lemma `lem:offdiag` therefore has multiple open technical
gaps, not just the edge uniformity.

**Import recommendation:** Do not import the lemma as stated.
The van der Corput idea with cubic phase is mathematically sensible
and could conceivably yield $|m - n|^{-3/2}$ decay in a properly
handled scaling regime; but the current text does not deliver
this, and a repaired version would need a separate proof addressing
the edge geometry (perhaps with a further sub-decomposition of
$\mathcal{I}$).

**Verdict:** User-claim confirmed.

## 6. Kritik 3 — O4-B3 Jaffard invertibility

**Location:** `prolate-gram-coercivity/O4_B3_jaffard_invertibility.tex`,
Theorem `thm:jaffard` (lines 94–120) and Theorem
`thm:jaffard_algebra` (Jaffard 1990, lines 214–226), with
Corollary `cor:jaffard_general` (lines 232–239).

**User claim (a):** Zeta-Konstante falsch: aus $|G_{mn}| \le C
|m-n|^{-3/2}$ folgt Off-Diagonal-Bound $2C\, \zeta(3/2)$, nicht
$2C(\zeta(3/2) - 1)$.

**Verification (a):** Confirmed. The proof of Schur test
(lines 145–159) computes
$$\sum_{n \ne m} |G_{mn}| \le \sum_{k=1}^\infty 2 \cdot \frac{C}{k^{3/2}}
= 2C\, \zeta(3/2).$$
The paper then writes $C_J = 2C(\zeta(3/2) - 1)$ "after absorbing
the $k = 0$ diagonal term" (line 167). But there is no $k = 0$
term in the off-diagonal sum — the diagonal is handled separately
via $|G_{mm} - 1| = O(c^{-1/6})$. The correct expression is
$C_J = 2C\, \zeta(3/2)$; numerically the Neumann threshold
$C_J < 1$ becomes $C < 1/(2\zeta(3/2)) \approx 0.191$, rather
than the paper's $C < 1/(2(\zeta(3/2) - 1)) \approx 0.312$.

The error tightens the required $C$ by a factor $\zeta(3/2) /
(\zeta(3/2) - 1) \approx 1.62$, but does not change the qualitative
direction of the argument.

**User claim (b):** Jaffard beweist keine Invertibilität — er
setzt sie voraus. Zirkulär als Invertibilitäts-Beweiser.

**Verification (b):** Confirmed structurally, with nuance. The
paper itself, in `cor:jaffard_general` (lines 232–239), assumes
"$G$ is positive definite on $\ell^2(\mathcal{I})$ (which holds
whenever $\lambda_{\min}(G) > 0$ as an $\ell^2$-operator)" and
then in the subsequent Remark 4.5 (lines 241–248) explicitly
identifies this as an external input:

> "Corollary reduces the invertibility question to the
> $\ell^2$-positivity of $G$, which is exactly the content of O5:
> $\lambda_{\min}(G) \ge c_2^{\rm Airy} > 0$. Thus in the regime
> where $C_J \ge 1$, the Jaffard argument still gives the required
> bound, but now requires O5 as an input."

So the paper is honest about the dependency in principle. The
circularity the User warns about is a **usage pattern** in the
larger programme (later papers may treat Jaffard as if it settled
invertibility), not a formal circularity within O4-B3 as written.

**Import recommendation:** Import the **Jaffard principle** —
"invertibility + off-diagonal decay ⇒ localized inverse" — as
a tool for future Objekt-X finite-arithmetic Gram matrices, with
the explicit reminder that invertibility must be established
separately. Do not import the specific Neumann threshold from
this paper without recomputing the constant.

**Verdict:** User-claim confirmed with structural refinement.

## 7. Summary table for Objekt-X import

| Item | Verified verdict | Import type |
|---|---|---|
| A: Gram $G = M^*M$ | $\checkmark[M]$ | Design pattern, not theorem |
| B: Paper XII Residual/Gap | $\checkmark[M]$ (abstract) | Attack strategy for P11 transport, prerequisites open |
| C: NEU-189 Type-Firewall | $\checkmark[M]$ | Direct import as programme-wide firewall |
| Kritik 1: Prime-T.2 | $\times[M]$ | Do not import |
| Kritik 2: O4-B2 edge uniformity | $?[O]$ | Do not import; keep idea in reserve |
| Kritik 3a: $\zeta(3/2)$ constant | $\times[M]$ | Recompute if needed |
| Kritik 3b: Jaffard as invertibility | Structural warning | Import Jaffard as tool, not as invertibility-prover |

## 8. Meta-notes on the larger old-repo narrative

The two prolate repos target the Connes–Consani–Moscovici
Prolate/PSWF spectral programme (arXiv:2511.22755), a very
different mathematical setting from the P11/P12 localised-hub
operator with three shifts $\{a, b, 2a\}$ over $\log 2, \log 3$.
Any technical import must therefore also verify **type
compatibility**: e.g. the finite PSWF Gram $G_{VM}$ is over
$\mathbb{C}^N$; the P11/P12 operator is over $L^2(R, S)$. The
salvaged items above (A, B, C) are those most likely to survive
this type-compatibility test.

## 9. What this audit does NOT do

- **Does not import any theorem into P11/P12 as** $\checkmark[M]$.
  Any actual technical import requires a separate,
  P11/P12-native proof.
- **Does not open a new active research front.** The current
  P12 open problems (b2d, $R < e/2$) remain the active technical
  targets.
- **Does not endorse the old Prolate→Weil→RH narrative.** The
  narrative is retired; only isolated building blocks are
  salvaged.

## 10. Firewall

R14 firewall of P11 unchanged. No item of this audit imports a
statement to the polar-gauge, terminal-transport, Object-X, or
RH layer.