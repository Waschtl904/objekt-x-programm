# Wickie-Fragen: Meta-Werkzeuge für Objekt X

**Erstellt:** 2026-08-22 (nach Runde 11)
**Status:** Programm-Meta-Dokument, kein Theorem
**Motivation:** Wenn der direkte Angriff an derselben Wand endet, verändere
die Spielregeln, ohne die Logik zu verletzen. Umgehen, spiegeln, gegen sich
selbst verwenden — statt stärker schlagen.

Drei historische Referenzen:

| Meister | Frage-Verschiebung |
|---------|--------------------|
| Gödel | Von „Was ist beweisbar?" zu „Kann eine Aussage über ihre eigene Beweisbarkeit sprechen?" |
| Wiles | Von „$a^n + b^n = c^n$?" zu „Welches unmögliche Objekt müsste bei Gegenbeispiel existieren?" |
| Perelman | Von „Welche Form hat dieser Raum?" zu „Was passiert, wenn ich die Geometrie fließen lasse?" |

Diese Verschiebungen sind mathematisch ernst zu nehmen, nicht als Metaphern.

## Die sechs Fragen

### Frage 1 (Wiles) — Frey-Kurve eines Gegenbeispiels

**Frage:** Welches unmögliche Objekt würde ein RH-Gegenbeispiel erzeugen?

Nicht direkt fragen: „Wie beweise ich, dass alle Nullstellen auf $\Re s = 1/2$
liegen?" Sondern: Angenommen, es gibt eine Nullstelle $\rho$ außerhalb der
kritischen Linie. Welches Objekt müsste dadurch in unserer Geometrie
existieren?

Ziel: eine Kette der Form
$$
\rho \notin \tfrac{1}{2} + i\mathbb{R}
\;\Longrightarrow\;
\text{pathologisches } v_\rho \text{ in Objekt-X-Geometrie}
$$
und unabhängig
$$
\text{Objekt-X-Struktur}
\;\Longrightarrow\;
v_\rho \text{ kann nicht existieren.}
$$

**Was $v_\rho$ sein könnte:** nichtpositiver Zustandsvektor, verbotene Signatur,
unmögliche Defektmode, nichtunitärer Charakter, nichtschließbarer Kanal,
inkompatible Polarstruktur, verbotener spektraler Winkel.

**Passt zum Programm:** Wir haben schon viele No-Go-Resultate (R14-Firewall,
R30.5-Audit). Vielleicht müssen sie nicht nur Straßen sperren, sondern ein
hypothetisches Gegenbeispiel zwingen, auf einer gesperrten Straße zu fahren.

**R14-Firewall-Warnung:** Diese Frage verlangt Aussagen über die Beziehung
zwischen Objekt X und Nullstellen. Sie darf nicht zu einer verkleideten
direkten RH-Behauptung werden. Die zulässige Formulierung ist: "Objekt X
zwingt Weil-Positivität; Weil-Positivität ist RH-äquivalent." Der Frey-Schritt
ist nur zulässig, wenn er im M/PG-Formalismus bleibt, ohne den terminalen
Transport zu behaupten.

**Status:** $?[O]$. Konzeptionell die produktivste offene Meta-Frage.

### Frage 2 (Gödel) — Selbstkonsistente Struktur

**Frage:** Kann die gesuchte Struktur auf ihre eigenen Daten zurückwirken
oder als Fixpunkt definiert werden?

Statt einen Operator $T$ vorzugeben und sein Spektrum zu berechnen: Suche
nach einem Objekt, das eine Selbstkonsistenzbedingung
$$
T = \Phi(\operatorname{Spec} T)
\qquad\text{oder}\qquad
X = \Phi(X)
$$
erfüllt. Objekt X wäre dann ein Fixpunkt einer kanonischen Konstruktion.

**Kontrollierte Selbstreferenz:** $X \to \text{arithmetische/spektrale Daten
von } X \to \text{Rekonstruktion von } X$.

**Nicht:** naive Gödelisierung ("Dieser Operator sagt etwas über sich selbst").
Das wäre philosophische Verzierung ohne mathematischen Gehalt.

**Sondern:** Fixpunktsätze in geeigneten Funktionalräumen, Bootstrap-Konsistenz
zwischen algebraischen und spektralen Daten, Verlangens-nach-Existenz-Argumente.

**Status:** $?[O]$. Kein konkreter Ankerpunkt in der jetzigen Algebra. Zukunftsmusik.

### Frage 3 (Perelman) — Fluss statt Konstruktion

**Frage:** Kann ich das statische Problem durch einen Fluss ersetzen?

Statt Objekt X zu erraten:
$$
X_0 \longrightarrow X_t \longrightarrow X_\infty
$$
mit einem Funktional
$$
\frac{d}{dt} E(X_t) \le 0.
$$

Klassifikation durch Evolution statt durch Konstruktion. $X_\infty$ ist der
verbleibende Fixpunkt mit gewünschter Weil-/Gram-Struktur.

**Große offene Frage:** Welcher Fluss? Welches Funktional?

**Status:** $?[O]$. Reine Programm-Frage. Kein Kandidat aktuell.

### Frage 4 (Wickie) — Obstruktion als Werkzeug

**Frage:** Kann ich die Obstruktion selbst als Werkzeug verwenden?

Wenn ein störender Term entsteht, nicht fragen "wie werde ich ihn los", sondern
"wohin zeigt er?"

Konkret: wenn $h(x)$ einen Wert $h(\phi(x))$ erzeugt, entsteht ein Orbit
$x, \phi(x), \phi^2(x), \ldots$, und statt jeden Wert einzeln zu eliminieren,
zeige: jeder Orbit trifft irgendwann eine bereits tote Zone.

**Neue Interpretation:** Visibility-Wechsel sind kein Anwachsen der Matrixdimension,
sondern ein gerichteter Graph
$$
\text{aktive Werte} \longrightarrow \text{neu erzeugte Werte}.
$$

Wenn dieser Graph einen wohlfundierten Abstieg besitzt (etwa eine Höhe
$\mathcal{H}(\phi(x)) < \mathcal{H}(x)$), können ganze Familien von Matrixzellen
auf einmal erledigt werden.

**Status:** $\checkmark[M]_{\text{partial}}$. Der η-Bootstrap in Runde 11 ist die
einfachste Instanz: die Abbildung $\phi(x) = x - \eta$ trifft in einem Schritt
den bereits toten Slice $C_{19}$. Verallgemeinerung: Kettenraum-Analyse möglicher
Visibility-Orbits im b2d/b2c-Chamber.

### Frage 5 (η-Trick) — Rücktransfer prüfen

**Frage:** Ist die scheinbar neue Schwierigkeit vielleicht nur ein bereits
gelöstes Problem an einem anderen Punkt?

**Sehr oft ist die Antwort: gar nichts Neues.**

**Status:** $\checkmark[M]$. Runde 11 ist der Existenzbeweis. Die η-Wand
verschwindet in einem einzigen Rücktransfer nach $x - \eta \in C_{19}$.

**Programm-Regel:** Bei jeder neuen Visibility-Wand zuerst fragen:
"Was ist der neue Wert, wenn ich ihn richtig zurücktransportiere?"
Erst dann, wenn diese Frage wirklich "etwas Neues" ergibt, ein größeres
System bauen.

### Frage 6 (Meta) — Was muss ich nicht beweisen?

**Frage:** Was müsste ich nicht beweisen, wenn ich das Problem anders
formulieren könnte?

Dies ist die Meta-Frage über den anderen fünf. Sie fragt nicht nach einer
Technik, sondern nach dem richtigen Rahmen.

**Anwendung auf jetzigen Stand:** Wir haben in Runde 11 den vollen Kernel für
$\sigma \le d/2$ bewiesen. Der verbleibende Fall ist $\sigma > d/2$: core-both.
Der direkte Angriff wäre ein größeres finites System. Die Wickie-Frage lautet:

- Muss ich core-both wirklich beweisen, oder gibt es eine natürliche
  Fortsetzung/Symmetrie/Reduktion?
- Ist core-both möglicherweise selbst wieder ein bereits gelöstes Problem
  unter einer nichttrivialen Abbildung?
- Gibt es einen Fluss auf $\sigma$, unter dem $\sigma > d/2$-Kerne in
  $\sigma \le d/2$-Kerne fließen?

Diese Fragen sind offen. Aber sie sind das richtige Fragenrepertoire, bevor
man ein 20×20 oder 21×21 System aufsetzt.

## Programm-Regeln (verbindlich)

Diese Regeln sind ab jetzt Teil des Objekt-X-Arbeitsstils:

1. **Vor jedem größeren finiten System:** Frage-5-Test durchführen. Ist der
   scheinbar neue Wert vielleicht schon tot?
2. **Bei jeder neuen Obstruktion:** Frage 4 durchführen. Wohin zeigt der
   störende Term? Erzeugt er einen wohlfundierten Orbit?
3. **Bei jeder festgefahrenen Direkt-Attacke:** Frage 6 (Meta) durchführen.
   Muss das wirklich direkt bewiesen werden?
4. **Frage 1 (Frey-Kurve)** ist momentan die produktivste offene Meta-Frage.
   Wenn eine Session Kapazität für eine Meta-Erkundung hat, ist das das Ziel
   mit der höchsten strategischen Rendite.
5. **Frage 2 (Fixpunkt) und Frage 3 (Fluss)** bleiben in Reserve. Kein
   Zwang zur Anwendung, aber im Kopf behalten.

## Was diese Fragen nicht sind

Diese Fragen sind **keine** Ersetzung für die R14-Firewall oder die
Lakatos-Audit-Journal-Disziplin.

- Sie können nicht rechtfertigen, dass wir M→PG-Übergänge behaupten, die wir
  nicht bewiesen haben.
- Sie können nicht rechtfertigen, dass wir Kandidaten zu Sätzen hochstufen.
- Sie können nicht "Kreativität" gegen "Strenge" ausspielen.

Sie sind ein **strategisches Fragenrepertoire vor der Techniken-Auswahl**,
nicht ein Freibrief für weniger sorgfältige Beweise.

## Verlaufsverfolgung

Ab Runde 12 wird für jede Session dokumentiert, welche Wickie-Frage(n)
angewendet wurden. Nicht jede Runde muss eine Wickie-List enthalten — aber
falls eine angewendet wurde, wird sie hier vermerkt.

| Runde | Datum | Wickie-Frage(n) | Effekt |
|-------|-------|----------------|--------|
| 11 | 2026-08-22 | 4, 5 | η-Wand kollabiert per Rücktransfer, kein 20×20 nötig |
| 8-10 | 2026-08-22 | (implizit 5) | 19×19 direkt gebaut, kein Meta-Angriff |
| 4 (b2c full) | ~ | (direkt) | Automatik-Ausnutzung von ε>d-R in Case (ii) |

## R14-Firewall

Alle Wickie-Fragen sind mit R14 kompatibel. Insbesondere Frage 1 verlangt
sorgfältige Formulierung: die Frey-Kurve eines RH-Gegenbeispiels darf nur im
M/PG-Rahmen konstruiert werden, ohne den terminalen Transport oder die
Objekt-X-Existenz zu behaupten.

Kein Punkt dieses Dokuments überschreitet M→PG.
