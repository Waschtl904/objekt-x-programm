# P12 Adversarial Audit — GPTs 13-Source b2c-Certificate

**Date:** 2026-08-22 (dritte Runde, adversarial)
**Repository head at start:** `c7f7e35`
**Auditor:** Perplexity, strict adversarial mode.

## 0. Summary

GPTs zweiter Wurf für einen b2c-Beweis mit 13 horizont-legalen Quellen
wurde vollständig verifiziert — mit einer **wichtigen Einschränkung
der Gültigkeitsdomäne**, die GPTs Text nicht dokumentiert:

**Verified $\checkmark[M]$:**

1. **Operator-Konvention rekonstruiert:** $Lh(u) = \sum_{s} k_{s}[h(u-s) - h(u+s)]$
   mit $(k_a, k_b, k_{2a}) = (p, r, q)$ und Anti-Reflexion
   $h(-y) = -h(y)$ ($y > 0$).  Alle 13 GPTs $Q_i$ folgen unter dieser
   Konvention aus dem rohen Operator, Zeile für Zeile.
2. **Triangulare Elimination:** exakt gemäß GPT.  Rechnung mit sympy
   liefert die Schlussidentität $2 r (2 p^2 - q^2)/p^3 \cdot h(x) = 0$
   Zeile für Zeile.
3. **Row-Multiplier-Zertifikat:** exakt.  $\sum_j c_j Q_j =
   [2 \Delta (2p^2-q^2)/(p^2 r)]\, h(x)$ symbolisch, alle 12 anderen
   Koeffizienten identisch null.
4. **Determinante:** $\det M_{13} = 2 p^7 q r (p^2-q^2)(2p^2-q^2)$
   (GPT: $-2 p^7 q r \dots$, Vorzeichen aus Spalten-Ordnung, sonst gleich).
5. **P1 und P2 unbedingt** $\checkmark[M]$: die 6 Raw-Source-Gleichungen
   $A^\pm, B^\pm, T^\pm$ folgen aus der gleichen Konvention, mit
   Horizont-Legalität für alle $0 < x < \varepsilon$.

**Neue Domänen-Restriktion:**

Position $u_8 = a + b - x = T + d - x$ liegt nur dann im Horizont
$(0, T_0)$, wenn $d - x < \varepsilon$.  Da $x > R$, reicht
$d - R < \varepsilon$ hin, d.h. **$\varepsilon > d - R$**.

Bei $R = d/2$ heißt das $\varepsilon > d/2 \approx 0.1014$; der
zulässige $\varepsilon$-Slice hat Breite
$\varepsilon_{\max} - d/2 \approx 0.010$.  Bei $R \to e^{-}$ heißt
das $\varepsilon > d - e = \delta \approx 0.059$.

**GPTs Text** ("sigma < eps < eps_max") **erwähnt diese Bedingung
nicht.** Ohne sie ist $u_8$ nicht horizont-legal und die Ableitung
$Q_8$ ist nicht anwendbar.

## 1. Verifikation der Operator-Konvention

Aus GPTs $Q_1, \dots, Q_{13}$ wurde die zugrundeliegende Konvention
zurück-verfolgt:
$$
Lh(u) = p\,[h(u-a) - h(u+a)]
      + r\,[h(u-b) - h(u+b)]
      + q\,[h(u-2a) - h(u+2a)],
$$
mit
$$
h(-y) := -h(y) \quad \text{(anti-reflection at zero)},
\qquad h(y) := 0 \quad \text{für } y \notin (R, S).
$$

An **jeder** der 13 Source-Positionen produziert diese Konvention
exakt die $Q_i$-Form, die GPT angibt.  Reproduktion in
`verify_gpt_b2c_certificate.py` und `reverse_engineer_operator.py`.

Konsistenz mit Repo-b2b $E_\sigma$-Gleichung: bei $u = a + x$ (b2b's
Source) ergibt die Konvention $p h(x) - p H(x) - q h(a-x) = 0$ (mit
Support-Kill des $r$-Terms wegen $d - x < R$ in b2c-Domäne).  Das ist
Repo-b2b's $E_\sigma$ für $\mathrm{sgn}(x - d) = -1$, mit dem
$r$-Term durch Support entfernt.  Konsistent.

## 2. Verifikation der triangularen Elimination

Alle Zwischenschritte aus GPTs Text mit sympy verifiziert:

- $Q_6 \Rightarrow h(e+x) = 0$
- $Q_{10} \Rightarrow h(2d-x) = 0$
- $Q_{12}, Q_{13} \Rightarrow h(e-\delta+x) = h(e+2\delta-x) = 0$
- $Q_{11} \Rightarrow h(2e+x) = 0$
- $Q_7 \Rightarrow h(T+\delta-x) = 0$
- $Q_4 \Rightarrow h(a-x) = (q/p) h(x)$
- $Q_3 \Rightarrow h(a+x) = -(q/p) h(x)$
- $Q_8 \Rightarrow h(b-x) = -(qr/p^2) h(x)$
- $Q_1 \Rightarrow H(x) = (\Delta/p^2) h(x)$
- $Q_2 \Rightarrow H(d-x) = -(r/p) h(x)$
- $Q_5 \Rightarrow h(T-d+x) = (3r/p) h(x)$
- $Q_9 \Rightarrow h(T-d+x) = -r(p^2-2q^2)/p^3 \cdot h(x)$

Aus der Konsistenz $Q_5 = Q_9$: $2r(2p^2-q^2)/p^3 \cdot h(x) = 0$.

Da $r > 0$ und $2p^2 - q^2 = q^2(4\sqrt{2} - 1) > 0$ elementar
(aus $4\sqrt 2 > 1$, aequivalent zu $32 > 1$), folgt $h(x) = 0$.

## 3. Verifikation des Row-Multiplier-Zertifikats

GPTs 13 Multiplikatoren $c_1, \dots, c_{13}$ eingesetzt in
$\sum_j c_j Q_j$: sympy expandiert und zeigt, dass alle 12
Nicht-$h(x)$-Terme identisch verschwinden.  Übrig bleibt

$$
\sum_j c_j Q_j = \frac{2 \Delta (2p^2 - q^2)}{p^2 r} \cdot h(x).
$$

## 4. Verifikation der Determinante

$\det M_{13} = 2 p^7 q r (p^2 - q^2)(2p^2 - q^2)$ (Faktorisierung
symbolisch).  GPTs Vorzeichen $-1$ kommt aus einer anderen
Spalten-Reihenfolge; Betrag identisch, non-zero.

## 5. Kritische Domänen-Beschränkung

Position $u_8 = a + b - x = T + d - x$ liegt im Horizont $(0, T_0)$
mit $T_0 = T + \varepsilon$ **nur wenn** $d - x < \varepsilon$.

Da $x > R$ (defect strip), reicht $d - R < \varepsilon$ hin:

$$
\boxed{\;\text{Zusätzliche Bedingung: } \varepsilon > d - R.\;}
$$

Konsequenzen:

- Bei $R = d/2$: $\varepsilon \in (d/2, \varepsilon_{\max})
  \approx (0.1014, 0.1116)$, Breite $\approx 0.0102$.
- Bei $R = e^-$: $\varepsilon \in (\delta, \varepsilon_{\max})
  \approx (0.0589, 0.1116)$, Breite $\approx 0.053$.

**GPTs Text erwähnt diese Bedingung nicht.**  Sie ist notwendig für
Horizont-Legalität von $u_8$ und damit für die Anwendung von $Q_8$.

## 6. Konsequenz für den Repo-Stand

**b2c neu bewiesen als Slice-Theorem** (siehe
`papers/P12_sections/P12_A15_1b2c_MixedStripDescentToDHalf.tex`):

$$
\boxed{\;2a < T_0 < c,\ d/2 \le R < e,\ T < S < T_0,\ \varepsilon > d - R
\ \Rightarrow\ \ker L = 0 \quad \checkmark[M].}
$$

**Rest von b2c ($\varepsilon \le d - R$):** Open Problem
`open:p12-b2c-full-remaining`.

**b2d ($e/2 \le R < d/2$):** Open Problem `open:p12-b2d`.

**P1, P2 unbedingt bewiesen** (siehe
`P12_A15_1_PairedSourceIdentities.tex`):

- P1: $H(x) + l(x) + (2r/p) H(d-x) = 0$ für alle $0 < x < \varepsilon$.
- P2: $H(x) - l(x) - 2 D(x)/p^2 = 0$ mit
  $D(x) = \Delta_{-}\, h(x) + qr[h(e-x) - h(e+x)]$,
  $\Delta_{-} = p^2 - q^2 - r^2$.

Konsequenzen:

- **Case-B Nichtdegenariertheit:** $c_0 = 2r/p > 1$ elementar,
  $\det \binom{1\ c_0}{c_0\ 1} = 1 - c_0^2 \ne 0$.
- **Sub-Case $\sigma \le d/2$:** $H(d-x) = 0 \Rightarrow H(x) = -l(x)$;
  für $x \in (\sigma, \min(\varepsilon, d - \sigma))$: $l(x) = 0$.

## 7. Firewall

R14 unberührt.  Alle P12-Aussagen bleiben Modulus-Layer-only.

## 8. Verifikations-Skripte

- `consolidation/verify_gpt_b2c_certificate.py` — 13-Source-Zertifikat
- `consolidation/reverse_engineer_operator.py` — Operator-Konvention
- `consolidation/verify_gpt_P1P2.py` — P1/P2 aus 6 Axiomen
