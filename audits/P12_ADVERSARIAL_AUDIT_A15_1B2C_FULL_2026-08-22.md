# P12 Adversarial Audit — Full b2c Restored, P1/P2 Horizon Wording Fixed

**Date:** 2026-08-22 (fourth round, adversarial)
**Repository head at start:** `a578522`

## 0. Zusammenfassung

Zwei User-Korrekturen an der dritten Runde adversarial nachvollzogen und im Repo umgesetzt.

## 1. Die $\varepsilon > d - R$-Restriktion ist illusorisch

In der dritten Runde hatte ich b2c auf einen Slice mit
zusätzlicher Bedingung $\varepsilon > d - R$ eingeschränkt.
Der User hat gezeigt: diese Bedingung ist im 13-Source-Fall,
den wir tatsächlich brauchen, **automatisch erfüllt**.

**Zwei-Fall-Argument des Users** (unabhängig verifiziert):

Das 13-Source-Zertifikat wird nur in Fall (ii) $\sigma > R$
benötigt. In diesem Fall gilt

$$
R \ge d/2 \ \Longrightarrow\ 2R \ge d \ \Longrightarrow\ d - R \le R,
$$
und da $R < \sigma < \varepsilon$:
$$
d - R \le R < \sigma < \varepsilon,
$$
also $\varepsilon > d - R$ automatisch. Damit ist
$u_8 = a + b - x = T + d - x$ im Horizont $(0, T_0)$ für alle
$x \in (R, \sigma)$.

Umgekehrt: der von mir als "offen" gebuchte Bereich $\varepsilon \le d - R$
liegt vollständig in Fall (i):
$$
\varepsilon \le d - R \le R \ \Longrightarrow\ \sigma < \varepsilon \le R,
$$
also $\sigma \le R$; das ist genau die b2b-restricted-tail-Domäne.

**Konsequenz:** Full b2c ist $\checkmark[M]$:

$$
\boxed{\;2a < T_0 < c,\quad d/2 \le R < e,\quad T < S < T_0
\ \Longrightarrow\ \ker L = 0\;}
$$

`open:p12-b2c-full-remaining` ist entfernt (redundant mit b2b).

## 2. P1/P2 Horizont-Text logisch korrekt formuliert

Alte Formulierung "all six positions are strictly less than $c$
and hence less than $T_0$" ist logisch invalid, da $T_0 < c$.

Neue Formulierung: pro Source direkt $< T_0$ mit elementaren
Rechtfertigungen.

| Source | Schranke | Elementarer Grund |
|---|---|---|
| $a - x$ | $< a < T < T_0$ | trivial |
| $a + x$ | $< a + \varepsilon_{\max} = c - a < T$ | $16 > 5$ ($4\log 2 > \log 5$) |
| $b - x$ | $< b < T$ | $4 > 3$ ($2\log 2 > \log 3$) |
| $b + x$ | $< b + \varepsilon_{\max} = \tfrac12\log(15/4) < T = \log 2$ | $16 > 15$ |
| $T - x$ | $< T < T_0$ | trivial |
| $T + x$ | $< T + \varepsilon = T_0$ | direkt |

Alle sechs Ungleichungen sind elementare rationale Vergleiche in
$\{\log 2, \log 3, \log 5\}$, ohne Transzendenz-Input.

## 3. b2d bleibt offen

Wie vom User ausdrücklich verlangt: **b2d nicht befördern.**
`open:p12-b2d` bleibt offen. Der nächste Angriffspunkt ist ein
horizont-legales typisiertes Zertifikat / Kokykel für den echten
symmetrischen Defekt-Kern in $e/2 \le R < d/2$. Kein Recyceln des
alten undokumentierten 19×19-Blocks.

## 4. Konsolidierter Statusstand nach vierter Runde

**Bewiesen ($\checkmark[M]$):**

| Stratum | Reichweite | Theorem |
|---|---|---|
| (i) | $S < T$ | b0 |
| (ii) | $S = T$ | b1 |
| (iii) | $T < S < T_0$, $R \ge e$ | b2a |
| (iv) | $T < S < T_0$, $e/2 \le R < e$, $\sigma \le R$ | b2b |
| (v) | $T < S < T_0$, $d/2 \le R < e$ | **b2c (voll)** |
| P1 | $H(x) + l(x) + (2r/p) H(d-x) = 0$ für $0 < x < \varepsilon$ | thm:p12-P1 |
| P2 | $H(x) - l(x) - 2 D(x)/p^2 = 0$ | thm:p12-P2 |

**Konsolidiert:** $\ker L = 0$ für den gesamten mixed strip
$d/2 \le R < T$.

**Offen ($?[O]$):**

- b2d: $e/2 \le R < d/2$
- $0 < R < e/2$

**Firewall R14** unberührt.

## 5. Was ist verifiziert (Repo-nachhaltig)

- 13-Source-Zertifikat: symbolische Verifikation der triangularen
  Elimination (`consolidation/verify_gpt_b2c_certificate.py`)
- Operator-Konvention: aus Q_i zurückverfolgt und mit b2b $E_\sigma$
  konsistent (`consolidation/reverse_engineer_operator.py`)
- P1/P2 aus 6 Raw-Source-Gleichungen: sympy-Multiplikatorvektor
  (`consolidation/verify_gpt_P1P2.py`)
- Zwei-Fall-Argument: elementar arithmetisch aus $R \ge d/2, \sigma > R$.
