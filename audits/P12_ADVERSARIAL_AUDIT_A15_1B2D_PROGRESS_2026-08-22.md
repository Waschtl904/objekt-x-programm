# P12 Adversarial Audit — b2d Progress (kein Beförderung)

**Date:** 2026-08-22 (sechste Runde, adversarial)
**Auditor:** Perplexity
**Trigger:** GPT-Live-Recheck: (a) 5<8 Textfix in P1/P2, (b) b2d
next-front investigation. GPT verbot ausdrücklich Beförderung ohne
uniform domain cover.

## 0. Zusammenfassung

1. **Patch $5 < 8$**: Der P1/P2-Horizont-Beweis für $a + x < T$
   wurde von der irrigen "$16 > 5$"-Kette auf die richtige
   "$c < 3a \Leftrightarrow \log 5 < 3 \log 2 \Leftrightarrow 5 < 8$"-Kette
   korrigiert.

2. **b2d partial progress (nicht befördert):**
   Die $b2d$-Region $e/2 \le R < d/2$, $\sigma > R$ zerfällt in
   drei geometrisch natürliche Teilregionen:
   - **b2d-upper** ($x > d - R$): plausibel via adaptiertem b2c-Zertifikat, aber nicht 100% verifiziert.
   - **b2d-core-single** ($R < x < d - \sigma$ mit $\sigma < d - R$):
     partielle algebraische Struktur bewiesen, aber **kein Kill**.
   - **b2d-core-both** ($d - \sigma < x < \min(\sigma, d-R)$):
     P1-2×2-System löst $H(x), H(d-x)$ in $l(x), l(d-x)$, aber
     erneut kein Kill von $h$.

**Verdikt b2d:** $?[O]$ bleibt. Keine Beförderung. Ehrliche
Diagnose als "partial reduction, no closure".

## 1. Patch $5 < 8$

Alte Formulierung (Ordering von Runde 4): "equivalent to $2a > c/2$,
i.e.\ $2\log 2 > \tfrac12\log 5$, elementary since $16 > 5$".

Diese Umformung ist inkorrekt: $2\log 2 > \tfrac12\log 5$ ist äquivalent zu
$4\log 2 > \log 5$, i.e.\ $\log 16 > \log 5$, i.e.\ $16 > 5$.
Aber die Original-Aussage $a + \varepsilon_{\max} = c - a < T = 2a$
ist äquivalent zu $c < 3a$, i.e.\ $\tfrac12\log 5 < \tfrac32\log 2$,
i.e.\ $\log 5 < 3\log 2 = \log 8$, i.e.\ **$5 < 8$**.

Beide Ungleichungen ($16 > 5$ und $5 < 8$) sind elementar wahr,
aber die zweite ist die algebraisch korrekte Umformung der
Original-Aussage. **Patch angewendet** in
`papers/P12_sections/P12_A15_1_PairedSourceIdentities.tex`.

Kompilierung: REF PASS nach dem Patch.

## 2. b2d Region-Splitting

Für $e/2 \le R < d/2$, $\sigma > R$, $x \in (R, \sigma)$:

- $d - R > d/2 \ge \varepsilon_{\max}$, also $\sigma < \varepsilon <
  \varepsilon_{\max} < d - R$ **stets**. Konsequenz: die Bedingung
  "$\sigma < d - R$" ist automatisch. Damit:
  - für $x < d - \sigma$: $d - x > \sigma$, also $H(d-x) = 0$ (Tail-Support).
  - für $x > d - \sigma$: $d - x < \sigma$, also $H(d-x)$ lebendig.

- $d - x$ vs $R$: für $x < d - R$: $d - x > R$, also $h(d-x)$ lebendig lower support.
  Für $x > d - R$: $d - x < R$, also $h(d-x) = 0$ (Support).

Drei Teilregionen in $b2d$-Region:

| Region | Range | $h(d-x)$ | $H(d-x)$ | Strategie |
|---|---|---|---|---|
| b2d-upper | $x \in (d - R, \sigma)$ | 0 | live | adaptiertes b2c-Zertifikat |
| b2d-core-both | $x \in (d - \sigma, d - R)$ | live | live | P1 2×2-System |
| b2d-core-single | $x \in (R, d - \sigma)$ | live | 0 | P1 einseitig |

## 3. b2d-upper: Kandidaten-Beobachtung teilweise bestätigt

Für $x > d - R$: $h(d-x) = 0$ per Support (wie in b2c). Frage: gilt
das b2c-Zertifikat mit R-Ersatz durch $R \ge e/2$?

Prüfung Position-für-Position: der b2c-Beweis nutzt an mehreren
Stellen $R \ge d/2$ für Support-Kills (z.B. $h(2d-x) = 0$ verlangt
$2d - x > S = T + \sigma$ oder $2d - x < R$; für $R < d/2$
möglicherweise ungültig).

**Konkrete Prüfung von Q6:** Bei Source $u = T - d + x$ ist der
horizont-legale reduzierte Ausdruck
$$
p\, h(e+x) - q\, h(d-x) = 0.
$$

In b2c ($R \ge d/2$): $h(d-x) = 0$ per Support, also $p\, h(e+x) = 0$.
In b2d-upper ($x > d - R$, $R < d/2$): $h(d-x) = 0$ auch per Support,
also $p\, h(e+x) = 0$. Gleicher Kill. **Konsistent.**

**Aber:** die anderen 12 Q_i müssen ebenfalls positionsweise geprüft
werden. Das ist noch nicht vollständig gemacht. Für b2d-upper daher:

$$b2d\text{-upper: } \text{plausibel } \checkmark[M], \text{ aber} \times[M] \text{ als vollständig verifiziert.}$$

## 4. b2d-core-single: partielle Struktur

In diesem Bereich ($R < x < d - \sigma$): $H(d-x) = 0$, $H(x) = -l(x)$
(aus P1 an $x$), $l(d-x) = c_0 l(x)$ (aus P1 an $d-x$, $c_0 = 2r/p$).

Verwendete horizont-legale Sourcen an $x$ und $d-x$ ($u = a \pm x$,
$b \pm x$, $T \pm x$; alle horizont-legal aus P1/P2-Modul):

Support-Kills automatisch (elementar aus $R \ge e/2$ und $x < d - R$):
- $h(e-x) = 0$: $e - x < e - R \le e/2 < R$.
- $h(x - \delta) = 0$: **korrigierte Ableitung (2026-08-22 GPT-Recheck):**
  $\delta = d - e$, also $d - \delta = e$ (nicht $2e$ wie in der ersten
  Version). Dann $x - \delta < d - R - \delta = e - R \le e/2 \le R$.

Triangulare Elimination liefert:
- $h(a - x) = (q/p)\, h(x)$   [aus $T^-(x)$]
- $h(e + x) = (q/p)\, h(d - x)$   [aus $T^-(d-x)$]
- $h(a + x) = -(qr/p^2)\, h(d-x) - (q/p)\, h(x)$   [aus $T^+(x)$]
- $h(b - x) = -(qr/p^2)\, h(x) - (q/p)\, h(d-x)$   [aus $T^+(d-x)$]
- $h(d - x) = \dfrac{pr}{p^2 - q^2}\, h(x)$   [aus $A^+(d-x)$]

Rest-Gleichung $A^+(x)$ liefert:
$$
\bigl[(p^2 - q^2)^2 - p^2 r^2\bigr]\, h(x) + p^2 (p^2 - q^2)\, l(x) = 0.
$$

**Elementarer Sign-Beweis für den Koeffizienten** $(p^2 - q^2)^2 - p^2 r^2$:
Teile durch $p^4$: $F' / p^4 = (1 - B)^2 - \theta$ mit
$B = 2^{-3/2}$, $\theta = (r/p)^2 = (\log 3 / \log 2)(2/3)^{3/2}$.

- $(1 - B)^2 < 4/5$: äquivalent zu $\sqrt{5}(1 - B) < 2$,
  quadriert zu $5(1 - B)^2 < 4$, also
  $5 - 10 B + 5 B^2 < 4$, also $5 B^2 - 10 B + 1 < 0$.
  Mit $B = 2^{-3/2}$: $5/8 - 10/(2\sqrt 2) + 1 = 5/8 - 5\sqrt 2/2 + 1
  = 13/8 - 5\sqrt 2/2$. Prüfe $< 0$: $13/8 < 5\sqrt 2/2$
  iff $26 < 40 \sqrt 2$ iff $676 < 3200$. **Elementar.**
- $\theta > 4/5$: bereits im b2d-Vorläufer-Audit als elementar
  bewiesen (via $\sqrt{2/3} > 4/5 \Leftrightarrow 50 > 48$
  plus $\log 3 / \log 2 > 3/2 \Leftrightarrow 9 > 8$).

Kombiniert: $(1 - B)^2 < 4/5 < \theta$, also $(p^2 - q^2)^2 - p^2 r^2
= p^4[(1-B)^2 - \theta] < 0$, strikt negativ.

Damit ist die Reflektions-Relation
$$
\boxed{\;h(x) = \dfrac{p^2 (p^2 - q^2)}{p^2 r^2 - (p^2 - q^2)^2}\, l(x)\;}
$$
mit strikt positivem Nenner.

**Interpretation.** Diese Relation koppelt $h(x)$ (unterer Support)
mit $l(x) = h(T - x)$ (oberer Support-Reflektion an $T$). Sie ist
**keine Kill-Aussage**; sie ist eine eindeutige Abhängigkeit.

**Warum das keinen Kill gibt.** Ich hatte kurzfristig überlegt, ob
die Symmetrie der 6-Sourcen-Reduktion an $x$ vs. an $d-x$ eine
Überbestimmung erzeugt, aus der $l(x) = 0$ folgt. Das ist bei
näherer Betrachtung **falsch**: die Reduktion ist bereits reflexions-
symmetrisch aufgesetzt (beide "an $x$" und "an $d-x$" Sourcen im
selben System), und liefert nur eine einzige algebraische Kette
für $h(d-x)/h(x)$ und $h(x)/l(x)$. Es gibt keinen unabhängigen
zweiten Kanal, der einen Kill erzwingen würde.

**Verdikt b2d-core-single:** partielle Struktur $\checkmark[M]$
(Reflektions-Relation), Kernel-Kill $?[O]$.

## 5. b2d-core-both: analoges Setup, kein Kill

In diesem Bereich ($d - \sigma < x < \min(\sigma, d - R)$): 2×2-System
aus P1 an $x$ und $d-x$ mit $c_0 = 2r/p$:
$$
\begin{pmatrix} 1 & c_0 \\ c_0 & 1 \end{pmatrix}
\begin{pmatrix} H(x) \\ H(d-x) \end{pmatrix}
= -\begin{pmatrix} l(x) \\ l(d-x) \end{pmatrix}.
$$
Determinante $1 - c_0^2 \ne 0$ (elementar $c_0 > 1$).
Löst $H(x), H(d-x)$ in $l(x), l(d-x)$.

Analoge 6-Sourcen-Reduktion mit Support-Kills liefert wieder eine
einzige algebraische Kette, nicht mehr. **Kein Kill von $h$.**

**Verdikt b2d-core-both:** analog $?[O]$.

## 6. Wo der Kill fehlt: strukturelle Diagnose

Die 6 horizont-legalen $A^\pm, B^\pm, T^\pm$-Sourcen an $x$ und $d-x$
liefern ein System, dessen Reduktion nach Support-Kills auf **eine**
skalare Relation $h(x) = K\, l(x)$ zusammenschrumpft.

Zur Auslöschung von $h(x)$ bräuchte man einen **unabhängigen Kanal**
zwischen $l(x)$ und $h$-Werten im unteren Support. Zwei Kandidaten:

(a) **Zusätzliche horizont-legale Sourcen** außerhalb $\{a, b, 2a\}$-Shifts,
z.B. bei $u = 2d - x$, $u = e + x$, $u = 3e + x$, $u = a - x$
(letzteres benötigt Anti-Reflektion an null; horizont-legal aber
möglicherweise redundant zu bereits verwendeten).
Diese sind genau die Sourcen aus dem b2c-13-Zertifikat, die bei
$R \ge d/2$ funktionierten. Bei $R < d/2$ müssen die Support-Kills
neu geprüft werden.

(b) **Kokykel-Struktur** $\tilde A = D A_U D$ aus A14.3a (Prolate-Repo)
in Form einer $\delta$-Translation. Konkrete Analyse steht noch aus.

## 7. Was b2d bräuchte für Beförderung

- Uniform domain cover für alle drei Sub-Regionen (upper, core-both, core-single) mit **jeweils** horizont-legalem Kill-Zertifikat.
- Explizite Enumeration jeder Source und Beweis, dass sie in $(0, T_0)$ liegt.
- Determinanten- oder festere Matrix-Faktorisierung.
- Keine Wiederverwendung des retrahierten 19×19-Blocks.

**Aktueller Stand:** all das ist $?[O]$.

## 8. Firewall

R14 unberührt. Keine Aussage dieses Audits importiert in die
Polar-Gauge-/Terminal-Transport-/Objekt-X-/RH-Ebene.

## 9. Auditor-Ehrlichkeit

Ich hatte kurz überlegt zu behaupten, das Konsistenz-Argument
zwischen "$h(x) = K l(x)$" und "$h(d-x) = K l(d-x)$" gebe einen
Kill. Bei sorgfältigerer Prüfung: die Reduktion an $d-x$ ist
**keine unabhängige Ableitung**, sondern dieselbe Kette in
gespiegelter Notation. Der behauptete "Konflikt" ist ein Artefakt
falscher Zählung. Kein Kill.

Das ist die Art von Fehler, den mein Auditor-Modus verbietet.
Zurückgezogen, bevor er im Repo landet.
