# P11 End-to-End Referee R33 — explicit P02-to-P11 archimedean Gamma symbol bridge

Date: 2026-08-19

## Target

Close the manuscript-level interface `?[O]` identified in R31 as (R31.8):
\[
m_\Gamma = c_0 + c_1 q_\Gamma,\qquad c_1\ne0,
\]
so that R31-B (pure exact-Gamma anti-locality) becomes citable directly for
the concrete P11 operator \(C_{\Gamma,S}\) rather than only for the abstract
P02 symbol.

No polar-gauge, terminal-transport, Object-X, or RH consequence is drawn.

## Repo sync

`main` at start of this audit: `9312e04...` — "Reposition R32 as annular
rewriting under antisymmetry".

The R31, R31-Zweitcheck, and R32 modules are in the current inputs.  P11 itself
still records only
\[
m_\Gamma(\xi) = 1 + g_\infty(\xi),\qquad m_\Gamma(\xi)\asymp\log(2+|\xi|),
\]
without an explicit formula for \(g_\infty\).  P02 fixes the exact symbol
\[
\gamma_\infty(t) = -\tfrac12\log\pi + \tfrac12\psi(\tfrac14 + \tfrac{it}{2}).
\]

---

## 1. Convergent Digamma difference

### Lemma R33-A

For every \(\xi\in\mathbb R\),
\[
q_\Gamma(\xi) - q_\Gamma(0) = \sum_{n=0}^\infty
\left[\frac1{n+\tfrac14} - \frac{n+\tfrac14}{(n+\tfrac14)^2+\tfrac{\xi^2}{4}}\right],
\tag{R33.1}
\]
where \(q_\Gamma(\xi) := -\log\pi + \operatorname{Re}\psi(\tfrac14 + \tfrac{i\xi}{2})\).
The series converges absolutely and each term is nonnegative.

### Proof

Set \(z = \tfrac14 + \tfrac{i\xi}{2}\).  The absolutely convergent Digamma
series \(\psi(z) = -\gamma_{\rm E} + \sum_{n\ge0}[1/(n+1) - 1/(n+z)]\) gives
\[
\operatorname{Re}\psi(z)
= -\gamma_{\rm E} + \sum_{n\ge0}\left[\frac1{n+1} - \frac{n+\tfrac14}{(n+\tfrac14)^2+\tfrac{\xi^2}{4}}\right].
\]
Subtracting the same series at \(\xi=0\) removes \(-\gamma_{\rm E}\) and the
\(1/(n+1)\)-terms, leaving (R33.1).  Nonnegativity is termwise: with
\(y := n+\tfrac14\), \(x := |\xi|/2\),
\[
\frac1y - \frac{y}{y^2+x^2} = \frac{x^2}{y(y^2+x^2)} \ge 0.
\]
\(\square\)

Status:
\[
\boxed{\text{R33-A (convergent digamma difference)} \quad \checkmark[M].}
\]

**Note:** This is the same convergent identity used in GPT's R31 distributional-
kernel second check (`audits/P11_REFEREE_E2E_R31_SECOND_CHECK_DISTRIBUTIONAL_KERNEL_2026-08-19.md`).
It is reused here as the constructive definition of \(g_\infty\), not merely
as a distributional device.

---

## 2. Constructive definition of \(g_\infty\)

### Definition R33-B

\[
\boxed{g_\infty(\xi) := q_\Gamma(\xi) - q_\Gamma(0).}
\tag{R33.2}
\]

By R33-A, \(g_\infty \ge 0\) with \(g_\infty(0) = 0\), so
\(m_\Gamma := 1 + g_\infty \ge 1\).

Numerically \(q_\Gamma(0) = \psi(\tfrac14) - \log\pi \approx -5.372183\), so
\(g_\infty(\xi) \approx q_\Gamma(\xi) + 5.372\).

---

## 3. Symbol properties

### Proposition R33-C

Under Definition R33-B, \(m_\Gamma = 1 + g_\infty\) satisfies:

(i) \(m_\Gamma: \mathbb R \to [1,\infty)\), even, real-analytic;

(ii) \(m_\Gamma(\xi) = \log|\xi| + (1 - \log 2 - \psi(\tfrac14)) + o(1)\) as
\(|\xi|\to\infty\); in particular \(m_\Gamma(\xi) \asymp \log(2+|\xi|)\);

(iii) The dilation inequality
\[
m_\Gamma(\lambda\xi) \le \lambda^2\,m_\Gamma(\xi)
\qquad\text{for all }\lambda \ge 1,
\tag{R33.3}
\]
required in the direct-terminal-bridge module (equation DT.25).

### Proof of (iii)

Set \(y_n := n + \tfrac14\), \(x := |\xi|/2\), and
\(s_n(\xi) := \frac{x^2}{y_n(y_n^2 + x^2)}\), so that
\(g_\infty(\xi) = \sum_{n\ge0} s_n(\xi)\).  For \(\lambda \ge 1\),
\[
\frac{s_n(\lambda\xi)}{s_n(\xi)}
= \lambda^2 \cdot \frac{y_n^2 + x^2}{y_n^2 + \lambda^2 x^2}
\le \lambda^2,
\]
because \(y_n^2 + \lambda^2 x^2 \ge y_n^2 + x^2\).  Summing over \(n\) gives
\(g_\infty(\lambda\xi) \le \lambda^2 g_\infty(\xi)\).  Since \(\lambda^2 \ge 1\),
\[
m_\Gamma(\lambda\xi) = 1 + g_\infty(\lambda\xi)
\le \lambda^2 + \lambda^2 g_\infty(\xi)
= \lambda^2\,m_\Gamma(\xi).
\]
\(\square\)

### Proof of (ii)

The digamma asymptotic \(\psi(z) = \log z - \tfrac{1}{2z} + O(1/z^2)\) in the
sector avoiding the negative real axis gives, at \(z = \tfrac14 + i\xi/2\)
with \(|\xi| \to \infty\),
\(\operatorname{Re}\psi(z) = \log(|\xi|/2) + O(1/|\xi|^2)\).  Hence
\[
q_\Gamma(\xi) = -\log\pi + \log(|\xi|/2) + o(1) = \log|\xi| - \log(2\pi) + o(1),
\]
and
\[
m_\Gamma(\xi) = 1 + q_\Gamma(\xi) - q_\Gamma(0)
= \log|\xi| + (1 - \log(2\pi) - q_\Gamma(0)) + o(1)
= \log|\xi| + (1 - \log 2 - \psi(\tfrac14)) + o(1).
\]
Positivity of \(m_\Gamma\) and boundedness on compact intervals close the
`\asymp\log(2+|\xi|)`-claim.  \(\square\)

Status:
\[
\boxed{\text{R33-C (symbol properties incl.\ dilation R33.3)} \quad \checkmark[M].}
\]

---

## 4. The affine bridge

### Corollary R33-D

Under R33-B,
\[
\boxed{
m_\Gamma(\xi) = c_0 + c_1 q_\Gamma(\xi)
\qquad\text{with}\qquad
c_1 = 1,\quad c_0 = 1 - q_\Gamma(0) = 1 + \log\pi - \psi(\tfrac14).
}
\tag{R33.4}
\]
Numerically \(c_0 \approx 6.372183\), \(c_0 > 0\), and \(c_1 = 1 \ne 0\), so
(R31.8) is satisfied.

### Proof

Immediate from R33-B and \(m_\Gamma = 1 + g_\infty\).  \(\square\)

Status:
\[
\boxed{\text{R33-D (affine bridge)} \quad \checkmark[M].}
\]

---

## 5. Transfer of R31-B to the concrete P11 operator

### Corollary R33-E

Under Definition R33-B and Corollary R33-D, Proposition R31-B (pure exact-Gamma
anti-locality) applies to the P11 multiplier \(m_\Gamma\) with \(c_1 = 1\).
Consequently:

- For every nonzero \(f \in L^2(\mathbb R)\) with
  \(\operatorname{ess\,supp} f \subset [-R, R]\), the full-line action of
  \(m_\Gamma\) cannot vanish on any nonempty open subinterval of \((R,\infty)\)
  nor of \((-\infty,-R)\).
- The off-diagonal kernel of \(m_\Gamma\), away from the diagonal, is
  \[
  K_\Gamma(u) = -\frac{e^{-|u|/2}}{1-e^{-2|u|}}, \qquad u \ne 0.
  \]
- The right-hand side of the R31 annular identity (R31.14) is real-analytic
  on each half-annulus, now interpreted as a property of the concrete
  \(C_{\Gamma,S}\) rather than of the abstract P02 symbol.

Status:
\[
\boxed{\text{R33-E (R31-B transferred to concrete P11)} \quad \checkmark[M].}
\]

---

## 6. Verdict and remaining status

| Item | Status |
|---|---|
| R33-A convergent digamma difference | ✓[M] |
| R33-B constructive definition of \(g_\infty\) | ✓[M] |
| R33-C symbol properties (positivity, asymptotics, dilation) | ✓[M] |
| R33-D affine bridge \(m_\Gamma = 1 + q_\Gamma - q_\Gamma(0)\) | ✓[M] |
| R33-E transfer of R31-B to concrete \(C_{\Gamma,S}\) | ✓[M] |
| P02→P11 symbol bridge (R31.8) as manuscript gate | now ✓[M] (was ?[O]) |
| R30-F: \(R_*(S,T_0) = S\) | ?[O] unchanged |
| R32-F: annular analytic-vs-shift-sum gate | ?[O] unchanged |
| Polar gauge / terminal transport consequence | not obtained |

### What R33 changes

- The interface debt from R31 is closed: R31-B is now a theorem about the
  concrete P11 operator \(C_{\Gamma,S}\), not just about the abstract P02
  symbol.
- The direct-terminal-bridge dilation inequality DT.25 acquires a proof (it
  was previously invoked without one, referring to "the explicit positive
  series for \(g_\infty\)" without displaying that series).
- The formula
  \(g_\infty(\xi) = \sum_{n\ge0}\frac{\xi^2/4}{(n+\tfrac14)((n+\tfrac14)^2 + \xi^2/4)}\)
  is now the canonical repo-visible definition.

### What R33 does not change

- R30-F remains open.
- R32-F remains open.
- The R31-D countermodel (coarse Schur models allowed) still stands; R33 does
  not attack it.
- No polar-gauge, terminal-transport, Object-X, or RH consequence.

### Numerical verification

A grid check of Lemma R33-A against \(q_\Gamma\) computed via
`scipy.special.digamma` at \(\xi \in \{0, 0.5, 1, 3, 10, 100\}\) matches to
7–10 significant figures for the truncated series; the affine bridge (R33.4)
is exact by construction.  These checks are performed in the working
notebook `consolidation/r31_verification.py` (not committed) and are consistency
sanity-checks, not proofs.

### Adversarial defence

The constructive choice \(c_1 = 1\) is the natural normalisation: the P11
form (2.8) uses the Fourier prefactor \(1/(2\pi)\), matching P02's Corollary
`cor:bgamma-diag`.  With \(c_1 = 1\) the asymptotic prefactor of \(m_\Gamma\)
is exactly \(1 \cdot \log|\xi|\), and any \(c_1 \ne 0\) would produce the same
qualitative asymptotic class \(m_\Gamma \asymp \log(2+|\xi|)\).  Different
choices of \(c_1\) would rescale \(m_\Gamma\) but leave the R31-B anti-locality
theorem intact (the theorem is stated for every \(c_1 \ne 0\)).

The choice \(c_0 = 1 - q_\Gamma(0)\) is forced by the P11 normalisation
\(m_\Gamma \ge 1\) with equality at \(\xi = 0\); any additive shift would
either violate \(m_\Gamma \ge 1\) or break the natural P02 diagonal identity.

### Next mathematical target

With R33 closed, the natural next task returns to R32-F / R30-F:

- Study the regularity of \(g_{R,S} = -B_{T_0}H_{T_0}E_{S,T_0}j_{R,S}\) on
  annular subintervals.  A partial route via Neumann-series expansion of
  \(B_{T_0} = (I + R_{T_0}^*R_{T_0})^{-1}\) becomes tractable now that the
  explicit \(g_\infty\)-formula is in play.
- Alternatively, identify a fingerprint property of the annular Schur range
  that the R31-D countermodel does not carry.
