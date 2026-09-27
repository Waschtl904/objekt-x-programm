# Objekt X – unabhängiger Gesamtaudit

**Beginn:** 24. September 2026  
**Letzte Aktualisierung:** 27. September 2026  
**Zuletzt integrierter Audit-Korrekturstand:** **main@5100f85191830bd599849d9db8f73a8208046a67**  
**Arbeitsweise:** Mathematische Aussagen werden unabhängig geprüft. Statusdateien, frühere Audits und Repository-Markierungen dienen als Wegweiser, nicht als Beweis.  
**Ziel:** Eine verständliche, fortlaufend aktualisierte Landkarte des gesamten Objekt-X-Programms vom ursprünglichen Fragenkatalog bis zur aktuellen Forschungsfront.

---

## Fortschreibungsregel

Diese Datei ist das kanonische Arbeitsgedächtnis des unabhängigen Gesamtaudits.

Nach jedem weiteren Prüfdurchlauf werden zwei Ebenen gepflegt:

1. **Synthese:** Die oberen Kapitel werden direkt verbessert, korrigiert oder erweitert. Dort soll immer der aktuell beste, widerspruchsfreie Gesamtstand stehen.
2. **Prüfprotokoll:** Unten wird knapp festgehalten, was im jeweiligen Durchlauf tatsächlich geprüft, bestätigt, korrigiert, zurückgestuft oder offengelassen wurde.

Die Datei soll kein zweites überbordendes Paper werden. Ziel ist eine kompakte, nachvollziehbare Gesamtkarte. Detailbeweise bleiben in ihren jeweiligen Beweispaketen und Papers; hier stehen nur die für das Verständnis des Gesamtprogramms entscheidenden Aussagen und Abhängigkeiten.

---

# I. Fortlaufende Synthese

## 1. Ausgangspunkt des Programms

Objekt X entstand ursprünglich nicht aus einer feststehenden mathematischen Konstruktion, sondern aus einem sokratischen Fragenkatalog zur Riemannschen Vermutung. Die leitende Idee war, durch immer präzisere Fragen Voraussetzungen sichtbar zu machen, Fehlwege auszusondern und dadurch schrittweise zur mathematischen Struktur hinter der Riemannschen Zetafunktion vorzudringen.

Aus diesem Fragenkatalog entwickelte sich ein Forschungsjournal mit mehreren hundert NEU-Knoten. Später wurde versucht, die mathematische Substanz in Papers zu verdichten. Diese Verdichtung führte schließlich selbst wieder zu sehr großen Konstruktionen, insbesondere in P11 und P12.

Der gegenwärtige Audit rekonstruiert deshalb die mathematische Entwicklung erneut von ihren Grundlagen aus. Dokumentierter Status und tatsächliche mathematische Gültigkeit werden dabei strikt getrennt.

---

## 2. Elementare Ausgangsbasis

Die frühen elementaren Beobachtungen über Primzahlen modulo 30 tragen:

- Jede Primzahl größer als 5 liegt in einer der acht Restklassen
  ```math
  1,7,11,13,17,19,23,29 \pmod{30}.
  ```
- Diese Klassen bilden die Einheitengruppe
  ```math
  (\mathbb Z/30\mathbb Z)^\times
  ```
  und sind multiplikativ abgeschlossen.
- Für jede zu 30 teilerfremde Zahl gilt
  ```math
  a^4\equiv1\pmod{30}.
  ```

Eine frühe lakatosianische Interpretation musste jedoch korrigiert werden: Dass auch zusammengesetzte Zahlen wie $49$ das Viertpotenzgesetz erfüllen, widerlegt nicht die Aussage „Primzahlen größer als 5 erfüllen es“, sondern lediglich deren Umkehrung.

Damit gehört das Viertpotenzgesetz zum modularen Gerüst und nicht zur Primheit selbst.

---

## 3. Sieb, Nichtperiodizität und die frühe Objekt-X-Idee

Nach endlich vielen Teilbarkeitsausschlüssen entstehen periodische Restklassensysteme. Sie enthalten weiterhin unendlich viele zusammengesetzte Zahlen. Die Primzahlmenge selbst ist dagegen nicht schließlich periodisch.

Damit ist die frühe Analogie

> lokale Ausschlussregeln → globale nichtperiodische Ordnung

als heuristische Forschungsfrage interessant, aber nicht ausreichend, um Objekt X mathematisch herzuleiten.

Insbesondere erzwingen lokale Verbote allein keine besondere globale Ordnung. Schon sehr einfache symbolische Systeme zeigen, dass zahlreiche unterschiedliche globale Folgen dieselben lokalen Verbote erfüllen können.

Die historischen Vergleiche mit Penrose-Parkettierungen, Quasikristallen und Ulam-Strukturen sind daher als **Motivation**, nicht als bewiesene gemeinsame mathematische Struktur zu behandeln.

---

## 4. Zetafunktion und Bost–Connes

Die funktionale Gleichung der vervollständigten Zetafunktion erklärt die Symmetrie um

```math
\mathrm{Re}s=\frac12,
```

aber eine symmetrische Nullstellenmenge muss keineswegs vollständig auf dieser Geraden liegen. Symmetrie allein impliziert daher nicht RH.

Das Bost–Connes-System besitzt dagegen eine konkrete Verbindung zur Zetafunktion: Für seinen Hamiltonoperator mit

```math
H e_n=(\log n)e_n
```

ist

```math
\mathrm{Tr}(e^{-\beta H})
=
\sum_{n\ge1} n^{-\beta}
=
\zeta(\beta),
\qquad \beta>1.
```

Diese Identität ist mathematisch wesentlich, liefert aber noch keine Spektralisierung der nichttrivialen Zeta-Nullstellen. Das Spektrum dieses Hamiltonoperators besteht aus $\log n$, nicht aus den Nullstellen.

Frühere Formulierungen, verschiedene $L$-Funktionen hätten „dieselbe Nullstellenstruktur“, sind deshalb zu grob und müssen jeweils präzisiert werden.

---

## 5. Weil-Kriterium als gesicherter Zielrahmen

Die Weil-Quadratik ist der erste bislang überprüfte Punkt, an dem die Riemannsche Vermutung vollständig in eine Positivitätsfrage übersetzt wird.

Für eine Amplitude $a$ mit zentrierter Mellintransformierter $\mathcal M_a$ lautet die RH-freie Nullstellenform

```math
\mathfrak W(a)
=
\sum_\rho
m_\rho\,
\mathcal M_a(\rho)\,
\overline{\mathcal M_a(1-\bar\rho)}.
```

Unter RH gilt

```math
1-\bar\rho=\rho,
```

und daraus folgt

```math
\mathfrak W(a)
=
\sum_\rho m_\rho|\mathcal M_a(\rho)|^2
\ge0.
```

Auch die Rückrichtung trägt: Falls eine Nullstelle außerhalb der kritischen Geraden liegt, lassen sich geeignete Mellin-Testfunktionen konstruieren, welche dieses Nullstellenpaar isolieren und eine negative Richtung der Weil-Quadratik erzeugen.

Damit gilt tatsächlich

```math
\boxed{
\mathfrak W(a)\ge0\quad\forall a
\quad\Longleftrightarrow\quad
\mathrm{RH}.
}
```

Eine positive GNS- oder Hilbertraumrealisierung der Weil-Form darf daher nicht vorausgesetzt werden: Ihre Positivität enthält bereits den RH-Kern.

---

## 6. Die explizite Weil-Formel

Die im Projekt verwendete Normalisierung der expliziten Formel wurde unabhängig nachgerechnet.

Für den reell-geraden Testkern erhält man

```math
\sum_\rho F_h(\rho)
=
h(i/2)+h(-i/2)
+
\frac{1}{2\pi}
\int_{\mathbb R}
\left[
\mathrm{Re}\psi\!\left(\frac14+\frac{it}{2}\right)
-\log\pi
\right]h(t)\,dt
-
2\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
g(\log n).
```

Insbesondere ist für $n=p^k$

```math
\frac{\Lambda(n)}{\sqrt n}
=
\frac{\log p}{p^{k/2}}.
```

Die späteren Korrekturen des Gamma-Vorfaktors und des Gewichts $p^{-k/2}$ waren daher mathematisch notwendig und stimmen mit der klassischen Explizitformel überein.

---

## 7. Beim Audit entdeckte und korrigierte Fehler

### 7.1 Orientierung des archimedischen Skalierungsgenerators

Das Projekt verwendet

```math
\mathcal M_\infty f(t)
=
\int_0^\infty f(x)x^{it}\frac{dx}{x},
\qquad
H_\infty=-ix\frac d{dx}.
```

Bei der Fourierkonvention $e^{+ity}$ gilt

```math
\boxed{
\mathcal M_\infty H_\infty\mathcal M_\infty^{-1}
=
-M_t,
}
```

nicht $+M_t$.

Damit entspricht der Mellinparameter $t$ dem Generator-Spektralwert $-t$.

Die wesentliche Selbstadjungiertheit, die Spektrummenge

```math
\sigma(H_\infty)=\mathbb R
```

und alle geraden bzw. symmetrisierten Weil-Ausdrücke bleiben davon unberührt.

Orientierungsabhängige rohe Gamma-Realisierungen müssen dagegen mit $-H_\infty$ formuliert werden.

### 7.2 Logarithmischer Koordinatenwechsel

Für

```math
H(s)
=
\int_0^\infty h(x)x^s\frac{dx}{x}
```

und $x=e^u$ ist der richtige additive Test

```math
\boxed{
g(u)=e^{u/2}h(e^u).
}
```

Dann gilt

```math
\widehat g(t)
=
H\!\left(\frac12+it\right).
```

Die früher verwendete Formel

```math
h(e^{u/2})e^{u/2}
```

war falsch.

Beide Fehler wurden am 27. September 2026 über PR #176 korrigiert und nach erfolgreicher Validierung in main gemergt. Die Weil-Masterform, NEU-220l, die Hauptpapers P01–P12 sowie die O8/O9-Gates mussten durch diese Korrekturen nicht zurückgenommen werden.

---

## 8. Vorläufige Gesamtbilanz

Bis hierhin ist die folgende Kette unabhängig nachvollzogen:

**elementare Primzahlarithmetik → Zeta-Symmetrie → Weil-Explizitformel → Weil-Quadratik → RH als Positivitätsproblem**

Nicht hergeleitet ist bisher der entscheidende Schritt:

**Bost–Connes / Adelen → Positivität der vollständigen Weil-Form.**

Genau an diesem Übergang beginnt nach jetzigem Audit die eigentliche mathematische Aufgabe des Objekt-X-Programms.

---

## 9. Grenze zwischen klassischer Weil-Theorie und eigener Objekt-X-Konstruktion

Der Audit von NEU-220e bis NEU-252 zeigt eine klare Grenze zwischen drei Ebenen, die im historischen Forschungsfluss teilweise ineinander übergingen.

### 9.1 Operatorische Darstellung des Gammaterms

Die semifinite Darstellung

```math
\Lambda_\Gamma(h)
=
\frac{1}{2\pi}\,
\tau_\infty\!\left(
\gamma_\infty(-H_\infty)\,h(-H_\infty)
\right)
```

ist mathematisch korrekt. Sie ist jedoch noch **keine Herleitung des Gammafaktors aus einer neuen Geometrie**. Unter der Mellintransformation ist $-H_\infty$ gerade Multiplikation mit $t$; damit wird die Digammafunktion $\gamma_\infty(t)$ per Funktionalkalkül eingesetzt und anschließend integriert.

Auch der unitäre Quotient

```math
S_\infty(t)
=
\frac{\Gamma_{\mathbb R}(1/2-it)}
     {\Gamma_{\mathbb R}(1/2+it)}
```

und seine logarithmische Ableitung sind direkte Umformulierungen des bekannten archimedischen Faktors der Funktionalgleichung. Ein unabhängiges Operatorpaar $(H_0,H_1)$, dessen tatsächliche Streumatrix $S_\infty$ erzwingt, ist an dieser Stelle nicht konstruiert.

Beim Audit wurde zusätzlich ein Vorzeichenfehler in der Interpretation korrigiert: Die im Projekt verwendete algebraische Größe

```math
Q_\infty
=
i\,\mathscr S_\infty^*\,\partial_t\mathscr S_\infty
=
M_{\gamma_\infty^{\rm sym}}
```

ist das Negative des üblichen Wigner-Smith/Eisenbud-Wigner-Zeitverzögerungsoperators $-i\mathscr S_\infty^*\partial_t\mathscr S_\infty$. Die algebraische Gamma-Identität und die späteren Spurformeln bleiben davon unberührt.

### 9.2 Der schwache endlich-archimedische Anschluss

Die frühe Konstruktion

```math
\Lambda_{\mathbb A}^{\rm weak}
=
\Lambda_{\rm fin}
+
\Lambda_\Gamma
```

ist eine direkte Summe zweier bereits getrennter Funktionale. Sie ist typisierbar, enthält aber ausdrücklich

- keine Kreuzterme,
- keine adelische Wechselwirkung,
- keine gemeinsame positive Geometrie.

Sie ist daher Buchhaltung, noch keine eigentliche Kopplung.

Beim Audit wurden zwei frühe Typbehauptungen in NEU-220g korrigiert: Nullschnitt-Restriktionen eines allgemeinen Schwartz-Bruhat-Elements sind als Restriktionen kanonisch definiert und nicht auf reine Tensoren beschränkt. Sie sind allerdings keine Tensorfaktor-Projektionen und rekonstruieren das ursprüngliche adelische Element nicht. Außerdem ist Punktauswertung auf dem additiven Schwartzraum $\mathcal S(\mathbb R)$ stetig; der eigentliche Augmentationsengpass betrifft Typ, Kanonizität und Kompatibilität.

### 9.3 Erste echte projektinterne adelische Konstruktion

Eine erste klar definierte eigene Konstruktion erscheint später mit dem adelischen Amplitudenraum

```math
\mathcal S_{\rm adel}^{\rm amp}
=
\left\{
F\in\mathcal S(\mathbb A_\mathbb Q):
(P_{\rm Haar}F)|_{(0,\infty)}
\in C_c^\infty((0,\infty);\mathbb C)
\right\}
```

und dem Port

```math
R_{\rm PW}F(u)
=
e^{u/2}(P_{\rm Haar}F)(e^u).
```

Die Wohldefiniertheit lässt sich direkt prüfen. Noch wichtiger: Der Port ist tatsächlich surjektiv auf

```math
\mathcal A_{\rm PW}=C_c^\infty(\mathbb R;\mathbb C).
```

Für beliebiges $a\in\mathcal A_{\rm PW}$ liefert

```math
h_a(x)=
\begin{cases}
x^{-1/2}a(\log x), & x>0,\\
0, & x\le0,
\end{cases}
\qquad
E(a):=h_a\otimes\mathbf 1_{\widehat{\mathbb Z}}
```

einen expliziten Rechtsinversen:

```math
R_{\rm PW}E(a)=a.
```

Damit ist $R_{\rm PW}$ sogar eine **gesplittete Surjektion**.

### 9.4 Konsequenz für die „adelisch transportierte“ Weil-Form

NEU-252 definiert

```math
B_W^{\rm adel}(F,G)
:=
B_W(R_{\rm PW}F,R_{\rm PW}G).
```

Diese Definition ist mathematisch korrekt. Sie erzeugt jedoch keine neue positive Form, sondern ist exakt der Pullback der bereits bekannten Weil-Form.

Aus der Surjektivität von $R_{\rm PW}$ folgt sofort:

```math
B_W^{\rm adel}(F,F)\ge0\ \ \forall F
\qquad\Longleftrightarrow\qquad
B_W(a,a)\ge0\ \ \forall a\in\mathcal A_{\rm PW}.
```

Die rechte Seite ist nach dem Weil-Kriterium äquivalent zu RH.

Außerdem verschwindet $B_W^{\rm adel}$ auf dem Kern des Ports:

```math
F\in\ker R_{\rm PW}
\quad\Longrightarrow\quad
B_W^{\rm adel}(F,G)=0
\qquad\forall G.
```

Die dadurch entstehende adelische Form besitzt also zunächst keine zusätzliche Geometrie in den Richtungen, die vom Port vergessen werden. Nach Quotientierung durch $\ker R_{\rm PW}$ erhält man im Wesentlichen wieder die ursprüngliche Amplitudengeometrie.

**Auditfolgerung:** Der adelische Amplitudenport ist eine echte, projektinterne und mathematisch korrekte Konstruktion. Er **transportiert** das Weil-Problem in einen adelischen Quellenraum, löst oder reduziert die Positivitätsfrage aber noch nicht. Die endliche adelische Komponente wird im expliziten Rechtsinversen sogar durch den festen Standardvektor $\mathbf 1_{\widehat{\mathbb Z}}$ eingefroren.

### 9.5 Der nun präzise verbleibende mathematische Sprung

Nach diesem Durchlauf lautet die eigentliche Objekt-X-Frage schärfer:

> Gibt es auf der adelischen Quelle eine **RH-unabhängig erzeugte positive oder coercive Struktur**, die nicht bloß der Pullback der fertigen Weil-Form ist und deren Abstieg tatsächlich $B_W$ beziehungsweise seine Positivität erzwingt?

Genau dort beginnt die nächste Prüfphase. Historisch entspricht dies dem Übergang zu M4 und den späteren Positivitäts-, Haar-$L^2$- und Transportkonstruktionen.


---

# II. Prüfprotokoll

## Durchlauf 1

Elementare Grundlegung geprüft. Modulo-30-Struktur bestätigt; logischer Fehler beim vermeintlichen Gegenbeispiel zum Viertpotenzgesetz gefunden.

## Durchlauf 2

Übergang von Sieb-/Quasikristallanalogie zu Objekt X geprüft. Keine mathematische Herleitung gefunden; Status als Suchheuristik.

## Durchlauf 3

Zetafunktion, Bost–Connes und frühe spektrale Behauptungen geprüft. Echte BC-Zeta-Verbindung bestätigt; mehrere historische Formulierungen als zu stark erkannt.

## Durchlauf 4

Rückrichtung des Weil-Kriteriums geprüft. Separations-/Approximationselement bestätigt; globale Weil-Positivität ist tatsächlich äquivalent zu RH.

## Durchlauf 5

Normierung der expliziten Weil-Formel geprüft. Gamma- und Primzahlpotenzfaktoren bestätigt. Zwei mathematische Fehler entdeckt.

## Durchlauf 6

Übergang von der klassischen Weil-/Gamma-Seite zur ersten eigenen adelischen Konstruktion geprüft. Die semifinite Gamma-Realisierung und der lokale Faktor $S_\infty$ sind korrekte operatorische Umformulierungen bekannter Daten, aber noch keine intrinsische neue Spektralgeometrie. Der schwache endlich-archimedische Anschluss ist nur eine direkte Summe ohne Kopplung.

Der spätere Port $R_{\rm PW}:\mathcal S_{\rm adel}^{\rm amp}\twoheadrightarrow\mathcal A_{\rm PW}$ ist dagegen eine echte projektinterne Konstruktion und besitzt einen expliziten Rechtsinversen. Dadurch ist die adelisch transportierte Form $B_W^{\rm adel}=R_{\rm PW}^*B_W$ jedoch lediglich ein Pullback: Ihre globale Positivität ist exakt wieder äquivalent zur Positivität von $B_W$ und damit zu RH.

Zwei zusätzliche lokale Fehler in NEU-220f/g wurden über PR #177 korrigiert: Vorzeichen der Wigner-Smith-Zeitverzögerungsinterpretation sowie zwei zu starke Aussagen über adelische Restriktionen und Augmentationen.


## Korrekturblock – 27. September 2026

Die beiden Fehler samt direkter operatorischer Folgestellen wurden über PR #176 korrigiert und in main gemergt.

Geprüfter Ausgangspunkt für die Fortsetzung:

**main@a77950be027dc1576b016c6a53bfad7ff65a04e4**

---

# III. Nächster Prüfpunkt

Prüfung des **M4-Übergangs** ab NEU-253:

> Wird dort erstmals eine RH-unabhängige positive Geometrie konstruiert, die mehr ist als ein Pullback der Weil-Form? Welche Positivitäts-, Abschließbarkeits- und Haar-$L^2$-Firewalls sind tatsächlich bewiesen, und an welcher Stelle beginnt die spätere Transport-/C1-Linie?
