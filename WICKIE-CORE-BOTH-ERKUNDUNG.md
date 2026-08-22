# Wickie-Erkundung: core-both ($\sigma > d/2$)

**Datum:** 2026-08-22 (nach Runde 11)
**Status:** Erkundung, keine Beweise. Alle Aussagen sind $?[O]$ oder $?[K]$.
**Ziel:** Anwendung von Wickie-Frage 4 (Obstruktion als Werkzeug) und
Wickie-Frage 5 (Rücktransfer) auf den verbleibenden b2d-Fall
$\sigma > d/2$, um zu prüfen, ob ein 20×20-System wirklich nötig ist.

## Ausgangslage nach Runde 11

- b2d-upper: $\checkmark[M]$ lokaler Kill.
- b2d-core-single voll: $\checkmark[M]$.
- Voller Kernel für $\sigma \le d/2$: $\checkmark[M]$.
- **Verbleibend offen:** $\sigma > d/2$, insbesondere die core-both-Zone
  $x \in (d - \sigma, \sigma)$, wo sowohl $H(x)$ als auch $H(d-x)$
  simultan live-tails sind.

Corollary `cor:p12-P1-caseB` diagnostiziert bereits: die $2 \times 2$
Kopplung zwischen $H(x)$ und $H(d-x)$ ist nicht-degeneriert ($c_0 = 2r/p > 1$
elementar via $\log 3 > \log 2$), aber $l(x), l(d-x)$ sind nicht bekannt.

## Frage 5-Test: Ist $H(d-x)$ ein bereits gelöstes Problem?

Sei $x \in (d - \sigma, \sigma)$ (core-both Zone). Der störende Wert ist
$H(d-x) = h(T + d - x)$.

**Position von $T + d - x$:**
- $d - x \in (d - \sigma, R + \sigma)$? Nein, wir sind in core-both,
  also $x \in (d - \sigma, \sigma)$, damit $d - x \in (d - \sigma, \sigma)$
  (Symmetrie um $d/2$).
- $T + d - x \in (T + d - \sigma, T + \sigma) = (T + d - \sigma, S)$.
- Da $d - \sigma > 0$ (aus $\sigma < d$, weil $\sigma < \varepsilon <
  \varepsilon_{\max} < d/2 + \delta < d$), liegt $T + d - x > T$.
  Also im Tail-Bereich $(T, S)$.
- $H(d - x)$ ist eine LIVE-Tail-Größe.

**Frage 5-Rücktransfer:** Ist $H(d - x)$ vielleicht dasselbe Problem wie
$H(x)$? Formal:
- $H(x) = h(T + x)$, $x \in (d - \sigma, \sigma)$.
- $H(d - x)$ mit $d - x \in (d - \sigma, \sigma)$ ebenfalls.
- Die Zuordnung $x \mapsto d - x$ ist eine **Involution** auf der core-both
  Zone. Sie tauscht $H(x)$ und $H(d - x)$.

**Folgerung:** $H(x)$ und $H(d - x)$ sind Wertepaar unter der Involution
$\iota: x \mapsto d - x$. Beide sind gleichzeitig unbekannt oder gleichzeitig
tot.

**Frage 5 auf core-both:** Nein, hier ist keine trivial-tote Zone. Die
Involution bringt uns nicht in eine bereits erledigte Region — sie tauscht
zwei Unbekannte.

## Frage 4-Test: Wohin zeigt die Obstruktion?

**Beobachtung:** P1 an $x$ und P1 an $d - x$ geben das System
$$
\begin{pmatrix} 1 & c_0 \\ c_0 & 1 \end{pmatrix}
\begin{pmatrix} H(x) \\ H(d-x) \end{pmatrix}
= -\begin{pmatrix} l(x) \\ l(d-x) \end{pmatrix}
$$
mit $c_0 = 2r/p > 1$. Die Determinante $1 - c_0^2 \ne 0$.

**Also:** $(H(x), H(d-x))$ ist eindeutig durch $(l(x), l(d-x))$ bestimmt.

**Frage 4 auf core-both:** Die Obstruktion ist $l(x), l(d-x)$. Wo leben diese?
- $l(x) = h(T - x)$, $x \in (d - \sigma, \sigma)$.
- $T - x \in (T - \sigma, T - d + \sigma)$.
- Da $\sigma > d/2$: $T - d + \sigma > T - d/2 > a$ (wegen $d/2 < a$).
- Und $T - \sigma < T$ trivial.
- Also $T - x \in (T - \sigma, T - d + \sigma) \subset (a, T)$.
  (Der obere Rand $T - d + \sigma$: wenn $\sigma$ nahe $\varepsilon_{\max}$,
  ist $T - d + \sigma < T + \varepsilon_{\max} - d = T + \varepsilon_{\max} - d$;
  numerisch bleibt das $< T$ genau dann wenn $\sigma < d$, was in unserem
  Regime erfüllt ist.)

**$l(x)$ lebt also im upper-half $(a, T)$.** Und der upper-half war
seit Runde 6 ein Objekt für sich (Corollary `cor:p12-P1-subhalf` behandelt
$\sigma \le d/2$).

**Also die Wickie-Frage:** Können wir aus dem, was wir schon über
$(a, T)$ wissen, $l(x) = 0$ auf $(T - \sigma, T - d + \sigma)$ folgern?

Antwort momentan: **nein**. Der upper-half ist genau in dieser Runde nicht
erledigt. `cor:p12-P1-subhalf` gibt uns nur $l(x) = 0$ auf einem "horizon-generated
interval", aber unter $\sigma \le d/2$ — nicht unter $\sigma > d/2$.

## Frage 4 verallgemeinert: Gibt es einen Orbit?

Setze $\phi_1(x) := d - x$ (Involution). Dann $\phi_1^2 = \text{id}$; kein
Abstieg. Aber:

Was, wenn wir die zweite Obstruktion $l(x)$ selbst als Startpunkt nehmen?
$l(x) = h(T - x)$ mit $T - x \in (a, T)$. Wenden wir jetzt eine
E- oder H-Source-Gleichung an $u = T - x$ (oder $u = T + x$) an? Wir
bekommen neue Werte $h(u \pm a), h(u \pm b), h(u \pm 2a)$.

Für $u = T - x$, $x \in (d - \sigma, \sigma)$:
- $u - a = T - x - a = a - x$. Da $x < \sigma < \varepsilon_{\max} < a$:
  $a - x > 0$. Und $a - x < a$. Falls $a - x < R$: support-null.
  Numerisch für $R \sim e/2 = 0.072$ und $x \sim d/2 = 0.101$:
  $a - x = 0.347 - 0.101 = 0.246 > R$. Live.
- $u + a = T - x + a = 3a - x = T + a - x$. Falls $a - x < \sigma$:
  $T + a - x < S$, live-tail. Sonst zero-above.
  Bei $x \sim d/2$: $a - x = 0.246 \gg \sigma \sim 0.1$. Also
  zero-above-S. Weggefallen.
- $u - b = T - x - b = a - d - x + a$... nachrechnen: $T - x - b = 2a - b - x = e - x$.
  $x > d - \sigma > d - \varepsilon_{\max} > 0$: $e - x$ kann positiv oder
  negativ sein. Bei $x \sim d/2$: $e - x = 0.144 - 0.101 = 0.043 < R$.
  Support-null.
- $u + b = T - x + b$. Grössenordnung $T + e - x + d = T + e - x + d$... numerisch $\approx 0.693 - 0.101 + 0.549 = 1.14$. Über $c$. Zero.
- $u - T = -x$. Anti-refl: $h(x)$. $x \in$ live-lower. Term: $q \cdot (-h(x)) \cdot (-1) = q h(x)$? Signs sorgfältig.
- $u + T = T - x + T = 2T - x$. $\approx 1.286$, > c. Zero.

So $L h(T - x)$ hat live-Terme: $p h(a-x)$, $q h(x)$ (nach anti-refl), und
möglicherweise weitere. Genau nachrechnen wäre nötig.

**Wickie-Vermutung:** Vielleicht produzieren die Source-Gleichungen an
$u = T - x$ (oder $u = T + x$) eine Kette
$$
l(x) = h(T - x) \;\to\; h(a - x), h(x), \ldots
$$
die alle in bereits bewiesenen Zonen leben (unteres Halbintervall, das
Runde-11 abdeckt). Wenn ja, könnte $l(x) = 0$ auf $(T - \sigma, T - d + \sigma)$
elementar folgen. Dann wäre die core-both-Zone erledigt.

**Konkrete Aufgabe für nächste Runde:** Slot-by-slot-Analyse von
$L h(T - x)$ und $L h(T + x)$ an einem Testpunkt $x \sim d/2$, $\sigma \sim 3d/4$
(also $\sigma > d/2$), und Prüfung, welche neuen Werte auftauchen und ob sie
in Runde-11-Zonen landen.

**Status:** $?[O]$. Explorationshypothese, nicht Beweis.

## Frage 6-Test: Muss ich core-both wirklich beweisen?

**Frage:** Gibt es eine natürliche Symmetrie oder ein Substitutionsargument,
das core-both direkt aus core-single ableitet?

**Beobachtung:** Die Involution $x \mapsto d - x$ auf core-both entspricht
einer Symmetrie der Operator-Algebra? Nicht offensichtlich. Der Operator
$L$ ist nicht $\iota$-invariant, denn die Shifts $a, b, 2a$ interagieren
asymmetrisch mit $d$.

**Alternative Frage 6-Formulierung:** Gibt es einen Parameter-Fluss
$\sigma(t)$, $\sigma(0) > d/2$, $\sigma(1) \le d/2$, unter dem Kerne
erhalten bleiben (nicht entstehen)?

**Konzeptionell:** Wenn man $\sigma$ **stetig verkleinert**, verkleinert
sich auch der Tail $(T, S)$. Falls jeder Kern im $\sigma$-großen System
einen Kern im $\sigma$-kleinen System erzeugt, würde Runde 11 ($\sigma \le d/2$
tot) sofort core-both erledigen.

Aber Vorsicht: verkleinernd geht möglicherweise Information verloren. Der
umgekehrte Weg (kleines $\sigma$ zu großem) wäre nötig, aber das produziert
möglicherweise neue Kerne.

**Status:** $?[O]$. Perelman-Anleihe, aber ohne konkreten Fluss-Kandidaten.

## Was diese Erkundung liefert

Konkret drei Arbeitshypothesen für die nächste Runde:

**H1 (Frage 4/5):** $L h(T \pm x)$ an core-both-$x$ produziert nur Werte in
bereits erledigten Zonen. Falls ja: elementarer $l(x) = 0$-Beweis.

**H2 (Frage 6, statisch):** Involutions-Symmetrie in der Coefficient-Struktur
zwischen b2c ($d/2 \le R < e$) und b2d ($e/2 \le R < d/2$)? Nicht
offensichtlich vorhanden.

**H3 (Frage 6, Fluss):** $\sigma$-Deformation. Preservation direction of
kernels. Nicht sofort umsetzbar.

Die vielversprechendste ist H1. Sie ist konkret verifizierbar in einem
30-Zeilen-Python-Skript.

## Nächste Runde

Nicht Runde 12 sofort. Erst:

1. H1 elementar prüfen (30 Zeilen).
2. Falls H1 durchgeht: Beweisskizze für core-both, dann Runde 12.
3. Falls H1 scheitert: honest No-Go-Diagnose in einem Audit, dann Bau eines
   $M \times M$-Systems (Größe zu bestimmen).

**Kein Automatismus zu größeren Systemen. Wickie zuerst.**

## H1-Ergebnis (2026-08-22)

**H1 SCHEITERT am Testpunkt** $R = 0.085$, $\sigma = 0.110$, $x = d/2 = 0.101$.

Skript: `consolidation/wickie_h1_exploration.py`.

$L h(T - x)$ hat 2 unbekannte Live-Slots:
- $h(a - x) = h(0.246)$ — im upper-half $(a, T)$, unbekannt für $\sigma > d/2$
- $h(x) = h(0.101)$ — selbst im core-both, das gerade zu beweisen ist

$L h(T + x)$ hat 3 unbekannte Live-Slots:
- $h(a + x) = h(0.448)$, $h(e + x) = h(0.245)$, $h(x)$

**Diagnose:** Die naive Wickie-Frage-4/5-Anwendung liefert im core-both
keinen elementaren $l(x) = 0$-Beweis. Die entstehenden Werte leben in
noch nicht erledigten Zonen — insbesondere im core-both selbst
($h(x)$-Selbstreferenz).

**Ehrliche Konsequenz:** Für core-both brauchen wir tatsächlich einen
substantiellen neuen Ansatz. Kandidaten:

- **Größeres Source-System** ($20 \times 20$ oder mehr) mit einer
  neuen Wickie-5-Prüfung an jedem neuen Wert.
- **P1/P2-Fixpunkt-Iteration** an der Involution $x \leftrightarrow d - x$.
  Die $2 \times 2$-Matrix ist nicht-degeneriert; wenn $l(x) + l(d-x)$ und
  $l(x) - l(d-x)$ beide null wären, hätten wir $l = 0$ auf core-both.
  Das erfordert Beziehungen zwischen $l$-Werten an gespiegelten Punkten.
- **Frage 6 (Frey-Kurve)**: gibt es eine formale Konstruktion, die einen
  nichttrivialen $l$ im core-both auf einen Widerspruch mit bereits
  bewiesenen No-Go-Resultaten (R14, R30.5) abbildet?

H2 und H3 (statische Symmetrie, $\sigma$-Fluss) bleiben offen als spekulative
Meta-Fragen.

**Verifikation:** Der H1-Fehlschlag ist selbst ein Resultat — im Sinne des
Lakatos-Audit-Journals. Er dokumentiert, dass core-both echtes neues
mathematisches Material erfordert und nicht nur eine Bootstrap-Übung ist.

## R14

Vollständig gewahrt. Diese Erkundung berührt keinen M→PG-Übergang.
