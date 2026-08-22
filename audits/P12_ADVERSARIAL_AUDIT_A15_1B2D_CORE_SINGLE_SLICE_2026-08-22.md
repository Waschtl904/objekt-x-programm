# P12 Adversarial Audit — A15.1 b2d-core-single slice

**Datum:** 2026-08-22 (Runde 9, `HEAD = d942149 + this commit`)
**Modul:** `papers/P12_sections/P12_A15_1b2d_MixedSubWedgeAFullTail.tex`
**Ziel:** Genuiner 19-Source-Local-Kill auf einem Slice von b2d-core-single.

## Status

`✓[M]` — bewiesen unter expliziter Slice-Bedingung; **kein** full-b2d-Status.

## Slice-Definition (C19)

$$
e/2 \le R < d/2, \quad R < \sigma < \varepsilon < \varepsilon_{\max}
$$
$$
R < x < \min\{\sigma, \; d-\sigma, \; R + \eta\}
$$

wobei $\eta := e - 2\delta = \tfrac12 \log(256/243) > 0$ und $\kappa := e - \delta$.

## Verifikationsmethode

`consolidation/gpt_19x19_full_verification.py` (Perplexity, Runde 9):

- Testpunkt: $R = 0.075$, $\sigma = 0.09$, $\varepsilon = 0.11$, $x = 0.085$
  (verifiziert im Slice-Interior).
- Alle 19 $u_i$-Werte in $(0, T_0)$ numerisch bestätigt.
- Für jedes $u_i$: raw operator $L h(u_i)$ symbolisch berechnet, mit Anti-Reflexion und Support-Kills gemäß R, σ. Alle 19 reduzierten Formen matchen exakt GPTs $Q_i$.
- **19/19 Sources: Source-Formen und Support-Kills numerisch verifiziert.**

## Source-Positionen

| $i$ | $u_i$ | Reduzierte $Q_i$-Terme (nach Kills) |
|-----|-------|--------------------------------------|
|  1  | $b - x$                   | $+p\,h(d{-}x) - r\,h(x) - q\,h(e{+}x)$ |
|  2  | $b + x$                   | $+p\,h(d{+}x) + r\,h(x)$ |
|  3  | $a - x$                   | $-p\,h(x) - p\,h(T{-}x) - r\,h(d{+}x) - q\,h(a{+}x)$ |
|  4  | $T - x$                   | $+p\,h(a{-}x) - q\,h(x)$ |
|  5  | $T + x$                   | $+p\,h(a{+}x) + r\,h(e{+}x) + q\,h(x)$ |
|  6  | $a + e + x = T - d + x$   | $+p\,h(e{+}x) - q\,h(d{-}x)$ |
|  7  | $e - x$                   | $-p\,h(d{+}x) - p\,h(a{+}e{-}x) - r\,h(2d{+}x) - r\,h(T{-}x) - q\,h(b{+}x) - q\,h(T{+}e{-}x)$ |
|  8  | $a + e - x$               | $-p\,h(T{+}e{-}x) - r\,h(\delta{+}x) - q\,h(d{+}x)$ |
|  9  | $d + x$                   | $-p\,h(b{+}x) - r\,h(a{-}x) - q\,h(a{+}e{-}x)$ |
| 10  | $3d + x$                  | $+p\,h(d{+}\delta{+}x) + r\,h(\delta{+}x)$ |
| 11  | $2d + x$                  | $+p\,h(\delta{+}x) - q\,h(2e{-}x)$ |
| 12  | $2e - x$                  | $-p\,h(\delta{+}x) - p\,h(T{-}\delta{-}x) - r\,h(d{+}\delta{+}x) - r\,h(T{+}e{-}x) - q\,h(2d{+}x)$ |
| 13  | $T - \delta - x$          | $+p\,h(2e{-}x) - q\,h(\delta{+}x)$ |
| 14  | $\delta + x$              | $-p\,h(2e{-}x) - p\,h(2d{+}x) - r\,h(a{+}e{-}x) - r\,h(3d{+}x) - q\,h(T{-}\delta{-}x)$ |
| 15  | $T + e - x$               | $+p\,h(a{+}e{-}x) + r\,h(2e{-}x)$ |
| 16  | $d + \delta + x$          | $-p\,h(3d{+}x) - r\,h(2e{-}x) - q\,h(3e{-}x)$ |
| 17  | $a + 2\delta + x$         | $+p\,h(2\delta{+}x) - q\,h(a{-}2\delta{-}x)$ |
| 18  | $4e - x = T - 2\delta - x$ | $+p\,h(a{-}2\delta{-}x) - q\,h(2\delta{+}x)$ |
| 19  | $a + 3e - x = T + \kappa - x$ | $+p\,h(3e{-}x) + r\,h(a{-}2\delta{-}x)$ |

## Lower-Support-Kills (K1–K4)

Elementar auf ganz $C_{19}$:

- **K1**: $0 < e - x < R$ via $x > R \ge e/2$.
- **K2**: $0 < x - \delta < R$ via $(10/9)^2 < 4/3$, d.h. $100 < 108$.
- **K3**: $|x - \kappa| < R$ in beiden Fällen $x \ge \kappa$ und $x < \kappa$.
- **K4**: $0 < x - \eta < R$: $\eta > 0$ via $256 > 243$, $e/2 > \eta$ via $3^9 > 2^{14}$ (19683 > 16384), $x < R + \eta$ ist Slice-Grenze.

## Upper-Support-Kills (H1–H5)

Elementar auf $C_{19}$:

- **H1**: $d - x > \sigma$ direkt aus $x < d - \sigma$.
- **H2**: $x + \sigma < 2\varepsilon_{\max} < a$ via $25 < 32$, d.h. $(5/4)^2 < 2$.
- **H3**: $\delta + x > \sigma$ via $\delta + e/2 > \varepsilon_{\max}$, elementar $100 < 108$.
- **H4**: $2e - x > \sigma$ via $\log(5/4) < \log(4/3)$, d.h. $15 < 16$.
- **H5**: $a - 2\delta - x > \sigma$ via $2\varepsilon_{\max} < a - 2\delta$, elementar $2025 < 2048$ (aus $25/16 < 128/81$).

**H5 ist die schärfste Ungleichung** und trägt die $Q_{18}$-Upper-Kills.

## Horizont-Legalität

Alle 19 $u_i \in (0, T_0)$ numerisch verifiziert (`gpt_19x19_full_verification.py`). Nichttriviale Fälle:

- $u_5 = T + x$: $x < \sigma < \varepsilon$, also $u_5 < T + \varepsilon = T_0$.
- $u_{15} = T + e - x$: benötigt $e - x > 0$ (K1: $e > x$? — nein, K1 sagt $e - x < R < \varepsilon$; genau das reicht: $u_{15} < T + \varepsilon = T_0$).
- $u_{19} = T + \kappa - x$: in Fällen $x \ge \kappa$ und $x < \kappa$ getrennt via K3.
- $u_{17}$: $T - u_{17} = a - 2\delta - x$; via $x < R + \eta$ zeigt sich $a - 2\delta - x > R > 0$.

## Determinante

Aus Runde 8 (`consolidation/gpt_19x19_verification.py`), symbolisch mit sympy:

$$
\det M_{19} = p^8 \, r \, (p-q)^3 \, (p+q)^3 \, F
$$

mit $F = 2p^4 - 3p^2q^2 - p^2r^2 + q^4 - q^2r^2$.

- $p, r, (p-q), (p+q) > 0$ elementar.
- $F < 0$ elementar via $53^2 < 38^2 \cdot 2$ ($2809 < 2888$) und $\sqrt{2/3} > 4/5$ ($50 > 48$).

Also $\det M_{19} \ne 0$, Kern trivial, alle 19 Visibility-Werte inkl. $h(x) = 0$.

## Genuine Visibility Wall bei $x = R + \eta$

$K_4$ ist die entscheidende Slice-Grenze. Sobald $x > R + \eta$, wird $h(x - \eta)$ in $Q_{18}$ live und das 19×19-System ist nicht mehr das richtige geschlossene System. Für den Rest von b2d-core-single ist ein **20×20-System oder Propagation** nötig.

## Beanspruchter Status

- **$\checkmark[M]$**: 19-Source-Kill auf $C_{19}$ (Perplexity + GPT + adversarial audit).
- **Nicht beansprucht**: full b2d, full core-single, core-both.

## Nächster Angriff (nicht in diesem Commit)

Parameterbereich $(R, \sigma)$ mit $\sigma \le \min\{d - \sigma, R + \eta\}$ analysieren — d.h. $\sigma \le d/2$ und $\sigma \le R + \eta$. Auf diesem Parameterkeil deckt $C_{19}$ den gesamten Defektstreifen $(R, \sigma)$ ab. Falls die bestehende Propagation legal anschließt, entstünde ein neuer parameterweiter b2d-Teilsatz **ohne** 20. Variable.

## R14-Firewall

Bleibt intakt. Kein Satz überschreitet den M→PG-Übergang; alles bleibt strikt in der M-Schicht.

## Repo-Zustand

- HEAD nach Runde 8: `d942149` (b2d-upper corollary im b2c-Modul).
- Nach diesem Commit: b2d-core-single Slice-Theorem als eigenständige Section in b2d-Modul.
- CI: erwartet SUCCESS.
