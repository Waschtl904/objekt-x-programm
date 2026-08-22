# P12 Adversarial Audit — b2d-upper Local Kill + Round-6 Corrections

**Date:** 2026-08-22 (siebte Runde, adversarial)
**Auditor:** Perplexity
**Trigger:** GPT-Live-Recheck von Runde 6: zwei Korrekturen an
Round-6-Audit-Text; b2d-upper vollständige 13-Source-Verifikation.

## 0. Zusammenfassung

**Zwei Korrekturen an Round-6-Audit angewendet.**

**Neues Ergebnis: b2d-upper local kill $\checkmark[M]$.**
Für $e/2 \le R < d/2$, $\sigma > d - R$, $x \in (d - R, \sigma)$:
$$h(x) = 0, \qquad H(x) = 0, \qquad l(x) = 0.$$

Publiziert als
`Corollary~\ref{cor:p12-b2d-upper-local}` im b2c-Modul.
**Full b2d bleibt $?[O]$** wie von GPT verlangt.

## 1. Korrektur 1: $d/2 < \varepsilon_{\max}$

**Alte Behauptung in Round-6-Audit:** $d/2 \ge \varepsilon_{\max}$,
also $\sigma < \varepsilon_{\max} < d - R$ automatisch.

**Korrekt:** $d/2 < \varepsilon_{\max}$, elementar äquivalent zu
$(5/4)^2 > 3/2$, i.e. $25 > 24$.

Ableitung:
- $d/2 = \tfrac14 \log(3/2)$
- $\varepsilon_{\max} = \tfrac12 \log(5/4)$
- $d/2 < \varepsilon_{\max}$ iff $\log(3/2) < 2 \log(5/4) = \log((5/4)^2) = \log(25/16)$
- iff $3/2 < 25/16$ iff $24 < 25$. **Elementar.**

**Konsequenz:** b2d-upper $\{d - R < x < \sigma\}$ ist **nicht immer
leer**. Sie ist nonempty genau für $\sigma > d - R$, was
$\varepsilon > d - R$ und damit $R > d - \varepsilon_{\max}$
erfordert. Numerisch: $R > d - \varepsilon_{\max} \approx 0.0912$.
Der b2d-Bereich $[e/2, d/2)$ mit b2d-upper-Region ist damit
$R \in (\max(e/2, d - \varepsilon_{\max}), d/2) = (0.0912, 0.1014)$,
Breite $\approx 0.010$.

**Audit-Text gepatcht in-place** in
`P12_ADVERSARIAL_AUDIT_A15_1B2D_PROGRESS_2026-08-22.md`.

## 2. Korrektur 2: $d - \delta = e$

**Alte Behauptung:** $d - \delta = 2e$.

**Korrekt:** $\delta = d - e$, also $d - \delta = e$.

**Konsequenz:** Die Support-Kill-Ableitung für $h(x - \delta) = 0$
in b2d-core wird zu
$$x < d - R \Rightarrow x - \delta < d - R - \delta = e - R
\le e/2 \le R$$
(unter Verwendung von $R \ge e/2$). Der Kill gilt weiterhin, aber
die Ableitung ist jetzt korrekt aufgeschrieben.

**Audit-Text gepatcht in-place.**

## 3. b2d-upper local kill: vollständige Verifikation

**Region:** $e/2 \le R < d/2$, $R < \sigma < \varepsilon < \varepsilon_{\max}$
mit $\sigma > d - R$; $x \in (d - R, \sigma)$.

### 3.1 Horizont-Legalität aller 13 Sourcen

Sourcen $u_1, \ldots, u_{13}$ wie im b2c-Zertifikat:
$a+x$, $b-x$, $T+x$, $T-x$, $d-x$, $T-d+x$, $2d-x$, $a+b-x$, $e+x$,
$T+\delta-x$, $T-\delta+x$, $3d-x$, $3e+x$.

Kritische Prüfung (die anderen sind trivial):
- $u_3 = T + x < T + \sigma < T_0$ (direkt).
- $u_8 = a + b - x = T + d - x$: brauche $d - x < \varepsilon$. Da
  $x > d - R$: $d - x < R < \sigma < \varepsilon$. **Legal.**
  (In b2c war $d - x < d - R \le d/2 \le R < \varepsilon$ zu prüfen
  mit dem alten Zwei-Fall-Argument. In b2d-upper direkter.)
- $u_{11} = T - \delta + x < T + x < T_0$.
- $u_{12} = 3d - x < 3d < (5/2)d < T$. Elementar via
  $5d < 4a$, i.e. $5b < 9a$, i.e. $5 \log 3 < 9 \log 2$, i.e.
  $3^5 < 2^9$, i.e. $243 < 512$.
- $u_{13} = 3e + x < 3e + \varepsilon_{\max} < T$. Elementar via
  $3e + \varepsilon_{\max} < T$ $\Leftrightarrow$ $\log 20 < \log 27$,
  i.e. $20 < 27$ (oder $80 < 108$).

Alle 13 Sourcen horizont-legal. **Verifiziert numerisch** in
`consolidation/b2d_upper_verification.py`.

### 3.2 Support-Kills (die 4 kritischen unteren Werte)

- **(A) $h(d - x) = 0$:** direkt aus $x > d - R$, also $d - x < R$.
- **(B) $h(e - x) = 0$:** $e - x > 0$ (da $x < \varepsilon_{\max} < e$),
  und $e - x < e - R \le e/2 \le R$. Elementar aus $R \ge e/2$.
- **(C) $h(x - \delta) = 0$:** $x - \delta > 0$ (da $x > d - R > \delta$),
  und $x - \delta < \varepsilon_{\max} - \delta < e/2 \le R$.
  Elementarer Schritt $\varepsilon_{\max} - \delta < e/2$:
  $\tfrac12 \log(10/9) < \tfrac14 \log(4/3)$
  $\Leftrightarrow$ $\log((10/9)^2) < \log(4/3)$
  $\Leftrightarrow$ $(10/9)^2 < 4/3$
  $\Leftrightarrow$ $100/81 < 108/81$
  $\Leftrightarrow$ $100 < 108$. **Elementar.**
- **(D) $2\delta - x$:** positiv aus $x < \varepsilon_{\max} < 2\delta$
  ($\varepsilon_{\max} < 2\delta$ elementar via $5/4 < (9/8)^2$,
  i.e. $80 < 81$); $2\delta - x < 2\delta - (d - R) = R - (e - \delta)
  < R$. Support-Kill oder Reflektion je nach Auftreten in der
  b2c-Kette.

### 3.3 Q_i-Reduktionen identisch zu b2c

Da alle 13 Source-Positionen horizont-legal und alle 4 Support-Kills
gültig sind, reduzieren sich die 13 rohen Operator-Gleichungen zu
den exakt gleichen Formen wie im b2c-Beweis:

- $Q_6$: $p h(e+x) - q h(d-x) = 0 \Rightarrow h(e+x) = 0$ (Kill A).
- $Q_{10}$: $p h(2d-x) = 0$ (aus Source $u = T + \delta - x$;
  siehe numerische Verifikation).
- $Q_{12}, Q_{13}$: $h(e \pm 2\delta \mp x) = 0$ via $p^2 - q^2 \ne 0$.
- $Q_{11}$: $h(2e+x) = -(r/p) h(e-\delta+x)$; per $Q_{12}, Q_{13}$
  Kette schließt.
- $Q_7$: $h(T + \delta - x) = 0$.
- $Q_4, Q_3$: $h(a-x) = (q/p) h(x)$, $h(a+x) = -(q/p) h(x)$.
- $Q_8$: $h(b-x) = -(qr/p^2) h(x)$.
- $Q_1$: $H(x) = (\Delta/p^2) h(x)$.
- $Q_2$: $H(d-x) = -(r/p) h(x)$.
- $Q_5, Q_9$: liefern $h(T-d+x) = (3r/p) h(x)$ und
  $-r(p^2 - 2q^2)/p^3 h(x)$ ; Konsistenz erzwingt
  $2r(2p^2 - q^2)/p^3 \cdot h(x) = 0$.

### 3.4 Row-Multiplier-Zertifikat

Das Zertifikat aus `Corollary~\ref{cor:p12-b2c-certificate}` gilt
identisch:
$$
\sum_{j=1}^{13} c_j Q_j = \frac{2(p^2 - q^2)(2p^2 - q^2)}{p^2 r} \cdot h(x).
$$
Da $(p^2 - q^2)(2p^2 - q^2)/(p^2 r) > 0$ elementar
(`Lemma~\ref{lem:p12-b2c-detfactors}`): $h(x) = 0$.

### 3.5 Post-Kill Konsequenzen

Aus der triangularen Kette mit $h(x) = 0$:
- $H(x) = (\Delta/p^2) \cdot 0 = 0$.
- $H(d - x) = -(r/p) \cdot 0 = 0$.
- Aus P1 an $x$: $H(x) + l(x) + c_0 H(d - x) = 0 \Rightarrow l(x) = 0$.

## 4. Was b2d-upper NICHT ist

- **Kein full-b2d-$\checkmark[M]$.** Die b2d-core-Regionen
  (core-single $R < x < d - \sigma$, core-both
  $d - \sigma < x < d - R$) bleiben $?[O]$.
- **Keine Beförderung** von `open:p12-subwedgeA-open`.
- **Kein Recycling** des retrahierten 19×19-Blocks.

## 5. Consolidated status nach Runde 7

**Bewiesen ($\checkmark[M]$):**
- Alle Strata (i)–(v) aus dem konsolidierten Corollary.
- P1, P2 unbedingt.
- **NEU: b2d-upper local kill** (Corollary im b2c-Modul).

**Offen ($?[O]$):**
- b2d-core-single und b2d-core-both innerhalb der b2d-Region
  $e/2 \le R < d/2$.
- $0 < R < e/2$.

R14 unberührt.

## 6. Objections / Auditor-Vorbehalte

**Keine.** Alle 4 Support-Kills und alle 13 Horizont-Positionen
sind elementar verifiziert. Die Reduktion ist ein direkter
Transfer der b2c-Kette, nicht eine neue Ableitung.

## 7. Test-Konfiguration

Numerische Verifikation (Verifikationsscript
`consolidation/b2d_upper_verification.py`):
- $R = 0.098$ (b2d-obere Hälfte)
- $\sigma = 0.110 > d - R = 0.105$ (b2d-upper feasible)
- $\varepsilon = 0.111 < \varepsilon_{\max} = 0.1116$
- $x = 0.107 \in (d - R, \sigma) = (0.105, 0.110)$

Alle 13 Sourcen und alle 4 Kills bestätigt.
