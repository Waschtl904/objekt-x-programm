# Objekt X – unabhängiger Gesamtaudit

**Beginn:** 24. September 2026  
**Letzte Aktualisierung:** 27. September 2026  
**Zuletzt integrierter Audit-Korrekturstand:** **main@0aad2bda6a1cb7d4b28d6e3cc732ddde87b199d2**  
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

## 10. M4 und die Haar-$L^2$-Firewall

Der M4-Strang (`NEU-253` bis `NEU-257`) fragt erstmals ausdrücklich nach einer **RH-unabhängigen positiven Hintergrundgeometrie** für die vollständige Weil-Form.

### 10.1 Was tatsächlich konstruiert wird

Über den adelischen Lift $S_{\rm PW}$ und seinen adjungierten Port erhält man eine Koisometrie

```math
\overline R_{\rm PW}:L^2(\mathbb A_\mathbb Q)\longrightarrow L^2(\mathbb R,du),
\qquad
\overline R_{\rm PW}S_{\rm PW}=I.
```

Damit ist

```math
L^2(\mathbb A_\mathbb Q)/\ker\overline R_{\rm PW}
\cong
L^2(\mathbb R,du).
```

Der daraus hervorgehende positive Hintergrundraum ist also schlicht

```math
H_0=L^2(\mathbb R,du).
```

Diese Konstruktion ist RH-unabhängig und mathematisch korrekt. Sie macht $B_W$ aber noch nicht positiv und kontrolliert die Form auch nicht in einer Majorantnorm.

### 10.2 Die Weil-Form ist auf diesem Hintergrund unbeschränkt

Für die Modulationsfolge $a_N(u)=e^{iNu}\varphi(u)$ mit $\|\varphi\|_2=1$ ergibt der korrigierte Gamma-Normierungsabgleich

```math
B_\Gamma(a_N,a_N)=\log N+O(1),
```

während Prim- und Polblock in diesem Regime nur $O(1)$ beziehungsweise $o(1)$ beitragen. Somit

```math
B_W(a_N,a_N)=\log N+O(1)\longrightarrow+\infty
```

bei $\|a_N\|_2=1$. Ein beschränkter Riesz-Operator auf Haar-$L^2$ scheidet daher aus.

Beim Audit wurden hierzu drei lokale Fehler in `NEU-255/256` korrigiert: das Fourier-Shift-Vorzeichen, ein unzulässiger exponentieller Schwartz-Schwanz und ein verlorener Faktor $1/\pi$ im Gamma-Block. PR #178 enthält diese Reparaturen; der Unbeschränktheitsbefund bleibt bestehen.

### 10.3 Semibeschränktheit ist bereits RH

Der entscheidende Schritt aus `NEU-257` trägt unabhängig nach.

Nimmt man eine untere $L^2$-Schranke an,

```math
B_W(a,a)\ge-\lambda\|a\|_2^2
\qquad\forall a\in C_c^\infty(\mathbb R),
```

dann ist $W+\lambda\delta_0$ positiv-definit. Der Bochner-Schwartz-Satz macht diese positive Distribution temperiert; damit ist auch $W$ temperiert. Nach dem Benedetto-Joyner-Kriterium ist die Temperiertheit der Weil-Distribution äquivalent zu RH.

Umgekehrt liefert RH durch das Weil-Kriterium sogar $B_W(a,a)\ge0$. Daher:

```math
B_W\text{ ist auf Haar-}L^2\text{ nach unten semibeschränkt}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
```

Eine RH-freie Herleitung der Semibeschränktheit wäre also bereits ein RH-Beweis und kann nicht als bloß technischer Vorbereitungslemma betrachtet werden.

### 10.4 Unter RH ist dieselbe Form auf Haar-$L^2$ nicht abschließbar

Unter RH besitzt die Weil-Form die atomare Spektraldarstellung

```math
B_W(a,b)
=
\sum_{\gamma}m_\gamma\,\hat a(-\gamma)\,\overline{\hat b(-\gamma)}.
```

Das repräsentierende Maß ist rein atomar und daher singulär gegenüber dem Lebesgue-Maß des Haar-$L^2$-Raums.

`NEU-257` gibt darüber hinaus einen direkten Nicht-Abschließbarkeitszeugen an: Es existiert eine Folge $a_n\to0$ in $L^2$, die bezüglich der Weil-Form Cauchy ist, deren Weil-Norm aber gegen einen strikt positiven Atomwert konvergiert. Damit ist $B_W$ unter RH auf $H_0=L^2(\mathbb R)$ nicht abschließbar.

### 10.5 Konsequenz: Kato/KLMN auf Haar-$L^2$ ist strukturell ausgeschlossen

Der ursprünglich in `NEU-256` erwogene relative Formansatz würde gleichzeitig Semibeschränktheit und Abschließbarkeit liefern. Das kann auf Haar-$L^2$ nicht eintreten:

```math
\text{Semibeschränktheit}
\Longrightarrow
\mathrm{RH}
\Longrightarrow
\text{Nicht-Abschließbarkeit auf Haar-}L^2.
```

Der Kato/KLMN-Pfad ist daher nicht nur noch unbewiesen, sondern **als Realisierungsweg für die vollständige Weil-Form auf diesem Hintergrund ausgeschlossen**.

### 10.6 Wo die positive Geometrie unter RH tatsächlich lebt

Unter RH ist die natürliche Vervollständigung nicht Haar-$L^2$, sondern der atomare Nullstellenraum

```math
\mathcal H_W
\cong
L^2(\tau)
\cong
\ell^2(\Gamma,m_\gamma).
```

Diese Identifikation ist mit Suzukis Konstruktion konsistent. Sie ist jedoch **konditional unter RH** und verwendet die Nullstellen selbst. Sie liefert deshalb noch keine RH-freie arithmetische Quelle für Objekt X.

### 10.7 Bilanz von M4

M4 liefert damit keinen neuen Positivitätsmechanismus. Es liefert vielmehr eine wichtige Firewall:

- Der Haarraum ist ein natürlicher positiver **Referenzraum**, aber nicht der Abschlussraum der Weil-Form.
- $L^2$-Semibeschränktheit der vollständigen Weil-Form ist bereits RH-äquivalent.
- Unter RH ist die Form auf diesem Referenzraum nicht abschließbar.
- Eine selbstadjungierte semibeschränkte Kato-Realisierung $A_X$ auf Haar-$L^2$ kann daher nicht die gesuchte Objekt-X-Geometrie sein.
- Die eigentliche offene Aufgabe verschiebt sich auf eine andere, RH-frei konstruierte positive Geometrie, deren Beziehung zur Weil-Form erst anschließend bewiesen werden müsste.
---

## 11. Finite Suzuki-Stufen: echte RH-freie Operatoren, aber keine RH-freie Grenzpositivität

Der Strang `NEU-259/260` reagiert auf die Haar-$L^2$-Firewall, indem er die vollständige Weil-Form auf endliche Intervalle lokalisiert und dort selbstadjungierte Operatoren konstruiert. Dieser Weg ist mathematisch substanziell, verschiebt den RH-Kern aber in die globale Kompatibilität und den Grenzübergang.

### 11.1 Die finite Weil-Form ist tatsächlich die lokalisierte vollständige Weil-Form

Nach dem Normierungsabgleich in `NEU-258` ist die Repo-Form einschließlich Pol-, Gamma- und Primzahlpotenzblock mit der kanonischen Literatur-Weil-Form identifiziert. Suzukis $Q_W^a$ ist deren Lokalisierung auf $(-a,a)$. Auf dem gemeinsamen Testkern gilt daher

```math
B_W|_{C_c^\infty(-a,a)}=Q_W^a.
```

Der zuvor in `NEU-259` offene separate Polterm-Randaudit war für diese Testkernidentität nicht mehr nötig und wurde in PR #179 geschlossen.

### 11.2 Was an jeder endlichen Stufe RH-frei positiv ist

Für jedes feste $a>0$ besitzt die lokalisierte Form einen selbstadjungierten, nach unten beschränkten Operator

```math
A_a=A_a^*,
\qquad
\lambda_a:=\inf\sigma(A_a)>-\infty,
\qquad
A_a\ge\lambda_a I.
```

Für jeden Shift $\lambda<\lambda_a$ ist

```math
T_{a,\lambda}:=A_a-\lambda I>0
```

und definiert den Hilbertraum $\mathcal H(T_{a,\lambda})$. Diese Positivität ist jedoch **durch Spektralverschiebung erzeugt**. Sie ist nicht die Aussage $Q_W^a\ge0$.

Das Vorzeichen des unverschobenen Spektralbodens enthält weiterhin den RH-Kern:

```math
\mathrm{RH}
\quad\Longleftrightarrow\quad
\lambda_a\ge0\ \text{für alle }a>0.
```

Die finite positive Metrik würde daher auch dann existieren, wenn RH falsch wäre: Man müsste den Shift lediglich unter den dann eventuell negativen Spektralboden legen.

### 11.3 Reelle finite Spektren sind ebenfalls RH-frei

Auf jedem $\mathcal H(T_{a,\lambda})$ besitzt der minimale Operator $i\,d/dx$ Defizitindizes $(1,1)$ und eine $S^1$-Familie selbstadjungierter Erweiterungen $\overline{\mathscr D}_{a,\theta}$. Deren Spektren sind die Nullstellen der endlichen charakteristischen Funktion $W(a,\theta;z)$ und deshalb reell.

Dies ist ein echtes RH-freies Hilbert-Pólya-artiges **Finite-Intervall-Phänomen**. Es beweist jedoch noch keine Annäherung an die Zeta-Nullstellen.

### 11.4 Der gesamte globale Spektralinhalt steckt im Grenzübergang

Der gewünschte Schritt ist die von Suzuki formulierte kompakte Grenzrelation

```math
e^{\phi(a,z)}W(a,\theta(a);z)
\longrightarrow
z^2\frac{\xi(1/2-iz)}{\xi'(1/2-iz)}.
```

Sie ist kein Satz der finiten Theorie, sondern der offene Grenzschritt. Würde eine solche Relation mit der nötigen lokalen Gleichmäßigkeit bewiesen, würden die reellen finiten Spektren die RH-relevante Nullstellenstruktur im Grenzwert erzwingen.

Damit liegt die Schwierigkeit nicht in der Existenz selbstadjungierter finiter Operatoren, sondern in ihrer **richtigen Auswahl und kontrollierten globalen Konvergenz**.

### 11.5 Lokale $\lambda$-Gaugefreiheit wird global zur RH-Firewall

Für festes $a$ sind verschiedene Shifts $\lambda<\lambda_a$ topologisch äquivalent. Für Intervalle $a<b$ ist die natürliche Nullfortsetzung $E_{a,b}$ jedoch nur für den unverschobenen Weil-Anteil exakt kompatibel:

```math
Q_W^b(E_{a,b}v)=Q_W^a(v).
```

Für die verschobenen Normen gilt

```math
\|E_{a,b}v\|_{T_{b,\lambda(b)}}^2
-
\|v\|_{T_{a,\lambda(a)}}^2
=
(\lambda(a)-\lambda(b))\|v\|_2^2.
```

Nullfortsetzung ist also nur bei einem gemeinsamen Shift isometrisch.

Ein einziger endlicher Shift $\lambda_*$, der unter allen Spektralböden $\lambda_a$ liegt, existiert genau bei einer uniformen Untergrenze der finiten Weil-Formen. Eine solche Untergrenze würde sofort eine globale Haar-$L^2$-Untergrenze von $B_W$ liefern. Nach der Firewall aus Durchlauf 7 ist dies bereits RH-äquivalent.

```math
\text{gemeinsamer isometrischer Shift für alle Intervalle}
\quad\Longleftrightarrow\quad
\mathrm{RH}.
```

Der Parameter $\lambda$ ist daher nur **lokal** ein harmloser Gaugeparameter. Global gehört seine Kontrolle zur eigentlichen Übergangsgeometrie.

### 11.6 Die übrigen Grenzdaten sind nicht RH-frei kanonisiert

`NEU-260b` nutzt die Parität und reduziert die selbstadjungierte Erweiterungsfreiheit korrekt von $U(1)$ auf zwei Zweige $\{+P,-P\}$. Das Vorzeichen wird dadurch aber noch nicht gewählt.

`NEU-260b.2` zeigt nur konditional: **falls** Suzukis Grenzrelation gilt, ist der falsche Paritätszweig asymptotisch ausgeschlossen. Diese Selektion benutzt damit gerade den noch offenen Grenzmechanismus, der RH implizieren würde; sie ist keine unabhängige arithmetische Auswahl.

Die vorgeschlagenen BC/KMS- und Frobenius-Selektoren besitzen in diesem Strang keine konstruierte Abbildung auf die Defizienzlinien. Zudem existieren im aktuellen `main` keine ausgearbeiteten Dateien `NEU-260c` oder `NEU-260d`; die $\phi$-Normalisierung und die Übergangsoperatoren $J_{a,b}$ bleiben in diesem historischen Strang daher offen.

### 11.7 Kein bewiesener Operatorgrenzwert

Im geprüften Strang liegt weder eine RH-freie Mosco-Konvergenz der Formen noch eine starke Resolventenkonvergenz der ausgewählten selbstadjungierten Operatoren noch ein bereits konstruierter Hilbert-Direktgrenzraum $\mathcal K_X$ vor.

Die kanonische $L^2$-Nullfortsetzung existiert, aber die $T$-Hilbertnormen sind bei RH-freien, $a$-abhängigen Shifts nicht isometrisch kompatibel. Der zusätzliche Transport $J_{a,b}$ ist deshalb echte neue Mathematik und nicht durch Suzukis finite Sätze geliefert.

### 11.8 Bilanz von Durchlauf 8

Der Suzuki-Weg ist der bislang klarste RH-freie finite Operatorrahmen des Programms. Er erfüllt den entscheidenden Zirkularitätstest auf jeder **festen** Stufe: selbstadjungierte Operatoren und reelle Spektren existieren auch dann, wenn RH falsch wäre.

Was fehlt, ist genau das, was für Objekt X entscheidend wäre:

- keine unverschobene positive Weil-Form auf allen finiten Stufen ohne RH;
- keine uniforme RH-freie Untergrenze über $a$;
- kein kanonisch kompatibles Hilbert-Direktsystem;
- keine RH-freie Auswahl aller Grenzdaten;
- kein bewiesener Grenzübergang von den reellen finiten Spektren zu den Zeta-Ordinaten.

Der Ansatz approximiert daher **nicht einfach nur den unter RH bekannten atomaren Raum**, ist aber auch noch keine RH-freie positive Objekt-X-Geometrie. Er komprimiert die globale Schwierigkeit sehr präzise in die Übergangs- und Grenzwertfrage.
---

## 12. P02/P03: Schnittstelle und Firewall, noch keine positive Objekt-X-Geometrie

Die ersten verdichteten Papers P02 und P03 übernehmen die NEU-Ergebnisse insgesamt wesentlich sauberer als die historischen Zwischenknoten. Nach dem unabhängigen Re-Audit bleibt aber eine klare Rollenverteilung:

- **P02** konstruiert eine echte adelische Testdaten-Schnittstelle und die vollständige hermitesche Weil-Form.
- **P03** beweist einen strukturellen No-Go für den naheliegenden Haar-$L^2$-Abschluss.
- Keines der beiden Papers erzeugt eine neue RH-unabhängige Positivität der vollständigen Weil-Form.

### 12.1 Was P02 wirklich konstruiert

Der kanonische finite-vacuum Port verwendet den Standardvektor $\mathbf 1_{\widehat{\mathbb Z}}$:

```math
(P_{\rm Haar}F)(x)
=
\int_{\widehat{\mathbb Z}}F(x,y)\,dy
=
\int_{\mathbb A_f}F(x,y)\mathbf 1_{\widehat{\mathbb Z}}(y)\,dy.
```

Darauf baut der Amplitudenport

```math
R_{\rm PW}F(u)
=
e^{u/2}(P_{\rm Haar}F)(e^u)
```

auf. Er ist surjektiv auf

```math
\mathcal A_{\rm PW}=C_c^\infty(\mathbb R;\mathbb C)
```

und besitzt den expliziten Rechtsinversen

```math
S_{\rm PW}a
=
h_a\otimes\mathbf 1_{\widehat{\mathbb Z}},
\qquad
h_a(x)=x^{-1/2}a(\log x)\ \ (x>0).
```

Diese Konstruktion ist eigenständig, RH-frei und nicht bloß Notation.

### 12.2 Die RH-freie Positivität in P02 ist nur Autokorrelationspositivität

Für $a\in\mathcal A_{\rm PW}$ entsteht durch Evenisierung der Autokorrelation ein Testkern mit

```math
h_{a,a}(t)
=
\frac12\bigl(|\hat a(t)|^2+|\hat a(-t)|^2\bigr)
\ge0.
```

Das ist eine echte positive Fourier-/Gramstruktur. Sie ist jedoch **nicht** die Positivität der arithmetischen Weil-Form. Die vollständige Form wird anschließend komponentenweise als

```math
B_W
=
B_{\rm pole}+B_\Gamma+B_{\rm fin}
```

eingesetzt und mit der Literatur-Weil-Form identifiziert. Der Primzahlpotenzblock besitzt kein eigenes positives Vorzeichen; gerade seine Wechselwirkung mit den übrigen Blöcken enthält den RH-Inhalt.

Entfernt man aus P02 alle Definitionen, die bereits $B_W$ enthalten, bleiben damit als positive RH-freie Struktur im Wesentlichen der Standard-Haarvektor, der surjektive Port und die gewöhnliche Autokorrelations-/Fourierpositivität. Es bleibt **kein positiver arithmetischer Operator**, dessen Abstieg $B_W\ge0$ erzwingen würde.

### 12.3 Surjektivität verhindert einen Positivitätsgewinn durch Pullback

Definiert man auf der adelischen Quelle

```math
B_W^{\rm adel}(F,G)
:=
B_W(R_{\rm PW}F,R_{\rm PW}G),
```

dann gilt wegen der Surjektivität

```math
B_W^{\rm adel}(F,F)\ge0\ \ \forall F
\quad\Longleftrightarrow\quad
B_W(a,a)\ge0\ \ \forall a\in\mathcal A_{\rm PW}.
```

Außerdem

```math
\ker R_{\rm PW}
\subset
\mathrm{Rad}(B_W^{\rm adel}),
```

und

```math
\mathcal S_{\rm adel}^{\rm amp}/\ker R_{\rm PW}
\cong
\mathcal A_{\rm PW}.
```

Die adelische Pullback-Geometrie reproduziert also exakt die ursprüngliche Amplitudengeometrie. Dies wurde im post-freeze Patch P02~3.6 ausdrücklich als **Pullback-Firewall** aufgenommen.

### 12.4 P03 ist ein No-Go-Paper, kein Positivitätspapier

P03 bestätigt und verdichtet die M4-Firewall:

```math
\exists\lambda\ge0:
\quad
B_W(a,a)\ge-\lambda\|a\|_2^2\ \forall a
\quad\Longleftrightarrow\quad
\mathrm{RH}.
```

Unter RH ist die Form auf dem positiven Referenzraum $H_0=L^2(\mathbb R,du)$ zugleich nicht abschließbar, weil ihr Spektralmaß rein atomar und gegenüber Lebesgue singulär ist. Die explizite Folgenkonstruktion bestätigt die Nicht-Abschließbarkeit direkt.

Damit ist P03 mathematisch wertvoll gerade als **Architektur-Firewall**:

- Haar-$L^2$ ist ein natürlicher RH-freier Referenzraum;
- es ist nicht der Abschlussraum der vollständigen Weil-Form;
- KLMN/Friedrichs auf diesem Hintergrund kann Objekt X nicht liefern;
- der unter RH natürliche Weil-Raum $\ell^2(\Gamma,m_\gamma)$ bleibt konditional.

### 12.5 Korrekturen beim Paper-Re-Audit

Im ursprünglichen P02 Patch~3.5 war die als „exact NEU-250r definition“ bezeichnete Haarprojektion fälschlich als Integration über ganz $\mathbb A_f$ geschrieben. Das ist zwar als Schwartz-Bruhat-Funktional wohldefiniert, aber **nicht** der in NEU-250o/255 und im Haar-$L^2$-Transport verwendete finite-vacuum Port. P02 Patch~3.6 verwendet nun konsistent $\mathbf 1_{\widehat{\mathbb Z}}$.

Zusätzlich wurde ein harmloser Zwischen-Vorzeichenfehler im Polterm-Hermitezitätsbeweis korrigiert und die vollständige Literaturidentifikation einschließlich Polblock explizit gemacht. P03 wurde auf diesen Port synchronisiert und die Definition des signed zero set sprachlich präzisiert.

Diese Änderungen wurden über PR #180 integriert.

### 12.6 Anschluss an die spätere C1-Linie

Der konkrete finite-horizon Kern von P11 und der späteren C1-Linie verwendet P02/P03 **nicht als fertige globale Objekt-X-Geometrie**.

P11 beginnt source-first mit

```math
\mathscr H_R=L^2(-R,R),
```

source-abhängigen p-adischen Martingalprojektionen, Gamma-Graphräumen und Feshbach-Korrekturen. Im selben Paper bleibt die Aufgabe, diese finite source-window Geometrie mit einer kanonischen globalen adelischen Quelle und dem Weil-Amplitudenport zu verbinden, ausdrücklich ein offenes globales Problem.

Die historische Rolle von P02/P03 ist daher:

```math
\text{P02: adelische Schnittstelle}
\quad+\quad
\text{P03: globale Haar-}L^2\text{-Firewall}
\quad\Longrightarrow\quad
\text{spätere Suche nach neuer finiter source-first Geometrie}.
```

Der spätere Defektoperator, starke Transport und die lokale C1-Positivität stammen nicht aus einem bereits in P02/P03 vorhandenen positiven Operator. Sie sind echte spätere Konstruktionen.
---

## 13. P04: korrekte finite Verdichtung, aber lokale Normalisierung ist kein globaler Transport

P04 verdichtet die Suzuki-Fenster insgesamt vorsichtig: selbstadjungierte finite Operatoren, positive verschobene Hilberträume und die Paritätsreduktion werden als RH-freie finite Aussagen behandelt; der Direktgrenzraum und die Übergangskarten bleiben conjectural.

### 13.1 Die lokale Arbeitsnormalisierung ist korrekt

Für jedes feste $a>0$ ist

```math
\lambda_{\rm w}(a)=\lambda_a-1
```

zulässig und liefert

```math
T_a^{\rm w}
=
A_a-(\lambda_a-1)I
\ge I.
```

Das ist eine saubere RH-freie Normalisierung jeder einzelnen endlichen Stufe relativ zu ihrem eigenen Spektralboden.

Die Bezeichnung „canonical working normalization“ war jedoch zu stark. Die Zahl $1$ ist eine feste bequeme Wahl, nicht eine mathematisch erzwungene globale Kanonisierung.

### 13.2 Der Shiftdefekt zwischen zwei Fenstern

Für $0<a<b$ und Nullfortsetzung $E_{a,b}$ gilt auf dem gemeinsamen Testkern

```math
Q_W^b(E_{a,b}v,E_{a,b}v)=Q_W^a(v,v).
```

Bei beliebigen zulässigen Shifts folgt

```math
\|E_{a,b}v\|_{T_{b,\lambda(b)}}^2
-
\|v\|_{T_{a,\lambda(a)}}^2
=
(\lambda(a)-\lambda(b))\|v\|_2^2.
```

Für P04s Wahl $\lambda_{\rm w}(a)=\lambda_a-1$ wird daraus

```math
\|E_{a,b}v\|_{T_b^{\rm w}}^2
-
\|v\|_{T_a^{\rm w}}^2
=
(\lambda_a-\lambda_b)\|v\|_2^2.
```

Der gemeinsame Abstand $1$ vom jeweiligen lokalen Spektralboden normalisiert die Stufen also einzeln, macht die natürliche Nullfortsetzung aber im Allgemeinen **nicht isometrisch**.

### 13.3 Ein gemeinsamer Shift wäre bereits RH

Ein endlicher Shift $\lambda_*$ mit

```math
\lambda_*<\lambda_a
\qquad\forall a>0
```

würde für jede kompakt getragene Testfunktion eine globale Haar-$L^2$-Untergrenze liefern. Nach P03/NEU-257 ist genau diese globale Semibeschränktheit RH-äquivalent.

Umgekehrt erlaubt RH wegen $\lambda_a\ge0$ für alle $a$ jeden festen negativen Shift. Daher:

```math
\exists\lambda_*\in\mathbb R:
\ \lambda_*<\lambda_a\ \forall a
\quad\Longleftrightarrow\quad
\mathrm{RH}.
```

Diese Firewall schließt nur den offensichtlichen gemeinsamen-Shift-/Nullfortsetzungsweg aus. Sie schließt **nicht** eine andere RH-freie Familie nichttrivialer Transporte $J_{a,b}$ aus. Deren Beschränktheit oder Isometrie, Cocycle-Eigenschaft und Operatorintertwining wären aber echte neue Sätze.

### 13.4 Die Parität reduziert, selektiert aber nicht

P04s Paritätssatz trägt:

```math
U(1)
\longrightarrow
\{+P,-P\}
\cong
\mathbb Z_2.
```

Die frühere Formulierung $\theta_{\rm can}(a)\in\{0,\pi\}$ konnte jedoch eine Kanonisierung suggerieren, die nicht bewiesen ist. Korrekt sind zwei **paritätsstabile** Zweige.

`NEU-260b.1` zeigt, dass Stetigkeit eine bereits getroffene Vorzeichenwahl nur propagieren könnte. `NEU-260b.2` schließt den falschen Zweig lediglich konditional auf Suzukis conjecturalen Grenzmechanismus asymptotisch aus. Eine unabhängige RH-freie Phasenselektion liegt damit weiterhin nicht vor.

### 13.5 P04 behauptet den globalen Raum nicht als Satz

Positiv ist, dass P04 den entscheidenden globalen Schritt bereits ausdrücklich als offen formuliert:

- $J_{a,b}$ sind nicht konstruiert;
- der induktive Grenzraum $\mathcal K_X$ ist eine Hypothese;
- die Suzuki-Grenzrelation ist eine Vermutung;
- die $\phi$-Normalisierung bleibt offen.

Im aktuellen Repository existieren zudem keine ausgearbeiteten Dateien `NEU-260c` oder `NEU-260d`; sie waren historische geplante Folgeknoten.

Der Audit hat daher nicht P04s Grundarchitektur widerlegt, sondern seine **lokal/global-Grenze geschärft**.

### 13.6 Typkorrektur

Eine kleine Typpräzisierung wurde ebenfalls vorgenommen: Die Defizitindizes $(1,1)$ gehören zum zugrunde liegenden minimalen symmetrischen Operator $\mathscr D_a$. Die Operatoren $\overline{\mathscr D}_{a,\theta}$ sind dessen selbstadjungierte Erweiterungen und haben als solche keine nichttrivialen Defizitindizes mehr.

### 13.7 Bilanz

P04 ist nach Korrektur eine saubere finite Schnittstelle:

```math
\text{RH-freie finite selbstadjungierte Geometrie}
\quad+\quad
\text{lokale positive Shiftmetrik}
\quad+\quad
\text{offene globale Transportdaten}.
```

Es enthält noch keinen global kompatiblen Objekt-X-Raum. Genau die fehlenden $J_{a,b}$ markieren rückblickend den Punkt, an dem die spätere starke Transport- und C1-Linie tatsächlich neue Mathematik hinzufügen musste.
---

## 14. P05–P10: Zwischenphase aus lokalen Bausteinen, Diagnostik und Firewalls

Dieser Block ist bewusst ein **Struktur- und Abhängigkeitsaudit**, kein erneutes vollständiges Re-Proving jedes einzelnen Lemmas der sechs Papers. Geprüft wurden die Satzkerne, ihre Positivitätsquelle, die ausdrücklich gesetzten Firewalls und die tatsächliche spätere Verwendung in P11/C1.

### 14.1 P05 – Relative Prime Channels and Arithmetic Edge Geometry

P05 besitzt einen tragfähigen lokalen Kern. In auditierten Primfasern wird der relative Generator als Transportoperator identifiziert:

```math
D_{\rm rel}|_{\mathcal H_{p,a}}
\cong
2i\kappa_p^{\rm tr}\frac{d}{dt}
```

mit rein absolutstetigem Spektrum. Damit wird gerade ausgeschlossen, dass dieser Generator bereits der diskrete Hilbert–Pólya-Endoperator ist.

Gesichert sind außerdem projektionswertige Kreuzspektralmaße, mögliche Überlappung verschiedener Primkanalbilder, die Matrixkoeffizientenform

```math
g_a(\log p)=\mathrm{Re}\langle a,U_{\log p}a\rangle,
```

und die arithmetische Identität

```math
\frac{\Lambda(p^m)}{\sqrt{p^m}}
=
\frac{\log p}{p^{m/2}}.
```

Die Positivitätsquelle ist jedoch nur lokal/modellrelativ; insbesondere ist der Matrixkoeffizient **kein Normquadrat**. Exakt zulässige Nichtnull-Lifts, Nichtentartung $c_p\ne0$, Liftunabhängigkeit, vollständige Primzahlpotenzoperatorik und globale Gramkopplung bleiben offen.

Für P11 überlebt daher vor allem die **Architekturfrage**: Prime-Power-Kanäle dürfen nicht vorschnell orthogonalisiert oder als fertige globale positive Blöcke behandelt werden. Die konkrete P11-Realisierung wird aber neu als source-first Martingalgeometrie aufgebaut; P05s alter $D_{\rm rel}$ wird nicht zum C1-Operator fortgesetzt.

**Rolle:** tragfähiger lokaler Baustein + Schnittstelle; globale Realisierung später ersetzt.

### 14.2 P06 – Jacobi, Feshbach and Divisor Graph

P06s robuster Satzkern ist die endliche Schur-/Feshbach-Grammatik. Endliche Feshbach-Identitäten, Weyl-/Stieltjes-Resolventensprache und finite Divisorpfad-/Trace-Geometrie sind mathematisch sinnvoll im jeweils typisierten endlichen Modell.

Gleichzeitig beweist P06 ein wichtiges historisches No-Go: Im konkreten NEU-088–90-Scaling kollabiert der symmetrisierte Resolventenblock in Hilbert–Schmidt-Norm und

```math
D_N(z)\longrightarrow1,
```

nicht zu einem nichttrivialen $C\xi(z)$-Grenzwert.

Das ist ausdrücklich **kein allgemeiner Feshbach-No-Go**. Die eigentliche Firewall lautet vielmehr:

```math
\text{endliche Feshbachidentität}
\ne
\text{Schattennorm-kontrollierter globaler Grenzoperator}.
```

Genau diese finite Feshbach-Sprache überlebt später in P11 am stärksten. Dort wird sie jedoch auf **neuen** source-first Operatoren realisiert:

```math
\Sigma_R
=
H_R(I+R_R^*R_R)^{-1}H_R^*
\ge0.
```

Die alte Determinantenskalierung, der alte diskrete Eigenbasisansatz und der historische $D_{\rm rel}$-Endoperator werden nicht übernommen.

**Rolle:** tragfähiges algebraisches Werkzeug + modellbezogene No-Go-Diagnose; Feshbach-Struktur in P11 neu instanziiert.

### 14.3 P07 – Weil Form Statistics

P07 bündelt mehrere statistische und Herglotz-orientierte Suchpfade. Tragfähig sind unter anderem Skalentriage, verschiedene PSD-/Korrelationskonstruktionen, die einseitige LFF→Rampen-Implikation und das Herglotz-Kriterium.

Beim unabhängigen Audit fiel jedoch ein echter RH-Typfehler auf. Die alte Fassung definierte zunächst das positive reelle Nullstellenmaß **unter RH** und behauptete anschließend

```math
m_{\rm arith}\text{ Herglotz}
\Longleftrightarrow
\mathrm{RH}.
```

Das war logisch zirkulär typisiert. Nach Patch 6 ist jetzt RH-frei

```math
m_{\rm arith}(z)
:=
-\frac{\Xi'(z)}{\Xi(z)}
```

als meromorphe Funktion definiert, und korrekt gilt

```math
m_{\rm arith}\text{ holomorph und Herglotz auf }\mathbb C^+
\quad\Longleftrightarrow\quad
\mathrm{RH}.
```

Erst unter RH existiert die positive reelle Nevanlinna-Maßdarstellung

```math
\mu_{\rm arith}
=
\sum_\gamma m_\gamma\delta_\gamma,
```

und erst dann wird die Weil-Auswertung einer Autokorrelation zur Summe von Absolutquadraten. Ohne RH bleibt die Nullstellenseite die gepaarte Weilform.

Die Jacobi-/Herglotz-Grenzarchitektur bleibt konditional: Würden echte Herglotz-Approximanten lokal gleichmäßig gegen $-\Xi'/\Xi$ konvergieren, wäre RH bereits bewiesen. Selbstadjungierter Jacobi-Kandidat, kanonische Renormierung und der Grenzübergang fehlen.

In P11/C1 wird dieser statistische/Herglotz-Pfad nicht als konstruktiver Kern weiterverwendet.

**Rolle:** diagnostische/bedingte Schnittstelle und historischer Suchpfad; keine direkte C1-Geometrie.

### 14.4 P08 – Renormalized Prime Operators and Finite-Part Structures

P08 enthält zwei getrennte Stränge. Im Jacobi-Strang kollabiert die erste Lanczos-Kante; ein allgemeines skalares Renormierungs-No-Go ist aber nicht bewiesen, weil die entscheidende stärkere Quotientenasymptotik offen bleibt.

Im arithmetischen Strang ist die wichtigste saubere Korrektur der exakte Mangoldt-Mellin-Kanal. Die geeignete geglättete Mangoldt-Summe besitzt die korrekte Mellin-Darstellung; Prime-only-Abkürzungen verwechseln dagegen $\vartheta$ und $\psi$.

Viele operatorische Aussagen bleiben ausdrücklich konditional: feste-$\beta$-Spurklasse, intrinsisches T2, Nichtentartung der Primkanäle, primdiagonale Mangoldt-Observable, operatorieller Finite Part und Fredholm-Realisierung.

Der Schutzsatz von P08 ist deshalb weiterhin gültig:

```math
\text{analytische Fortsetzung von }-\zeta'/\zeta
\ne
\text{konstruierter operatorieller Finite Part}
\ne
\text{Objekt-X-/Hilbert–Pólya-Operator}.
```

P11 verwendet diese konkrete Renormierungs-/Finite-Part-Architektur nicht als Kern. Ihre wichtigste Wirkung ist diagnostisch: alte skalare/Jacobi-/Prime-only-Abkürzungen werden nicht wieder geöffnet.

**Rolle:** Renormierungsdiagnose + analytische Schnittstelle; überwiegend durch spätere source-first Architektur ersetzt.

### 14.5 P09 – BC, Hochschild and Charged Cohomology

P09 besitzt einen eigenständigen algebraischen Seitenbefund: eine nichttriviale neutrale Hochschildklasse sowie eine geladene äußere Derivation und ein nichttrivialer geladener Cup in einem erweiterten logarithmischen Koeffizientenmodul.

Diese Nichttrivialität ist jedoch **kohomologisch**, nicht Hilbert-positiv. Die zyklische Verfeinerung folgt nicht automatisch; mehrere kanonische zyklische/Hopf-Reparaturen scheitern, und für den kanonischen skalaren Basislift gilt

```math
t\Phi_0\ne C\Phi_0
\qquad\forall C\in\mathbb C.
```

P09 baut keine Weil-/Gamma-Paarung, keinen positiven Gramraum und keinen Hilbert–Pólya-Operator. Im aktuellen P11/C1-Kern findet sich keine direkte Verwendung dieser Hochschildklassen.

**Rolle:** tragfähiger algebraischer Seitenzweig + zyklische Firewall; für die heutige C1-Linie historisch seitlich.

### 14.6 P10 – No-Go Theorems for Canonical Global Coupling

P10 ist bewusst keine Konstruktionsstufe, sondern die systematische Sammlung der bis dahin belastbaren Sperren. Besonders wichtig bleiben:

- lokaler Rang-eins-/Primkanalbefund ist keine globale positive Gramgeometrie;
- Transportgenerator ist kein diskreter HP-Endoperator;
- finite Feshbach-Identität ist keine globale Schatten-/Fredholmtheorie;
- die konkrete alte Determinantenskalierung kollabiert;
- LFF/Rampe, Jacobi, Primeclock, Prime-only-Mellin, Finite-Part- und mehrere Hochschild/KMS-Reparaturen dürfen nicht überinterpretiert werden.

P10 schließt Objekt X ausdrücklich **nicht** aus. Als offener Rest bleiben gerade die Strukturen, die P11 später neu angreift:

```math
\text{globale nichtorthogonale Gramkopplung}
+
\text{Primzahlpotenzkanäle}
+
\text{archimedischer Kanal}
+
\text{positive globale Weil-Geometrie}.
```

P10 überlebt daher in P11/C1 nicht als Operator, sondern als **Architekturverfassung**: alte Abkürzungen sind gesperrt und spätere Konstruktionen müssen ihre Typ- und Grenz-Firewalls respektieren.

**Rolle:** No-Go-/Firewall-Ergebnis; stark als Constraint übernommen.

### 14.7 Abhängigkeitsmatrix P05–P10 → P11/C1

| Paper | Satzkern | Positivitätsquelle | Haupt-Firewall | Tatsächliches Überleben in P11/C1 | Hauptrolle |
| --- | --- | --- | --- | --- | --- |
| **P05** | lokale Primkanäle, Transportnormalform, Kreuzspektralmaße, Mangoldt-Gewichte | lokal/modellrelativ; Matrixkoeffizienten, kein Normquadrat | Lift/Nichtentartung/globaler Gramraum offen | Motive und Typgrenzen; konkrete Quelle in P11 durch Martingalmodell neu gebaut | Baustein + Schnittstelle |
| **P06** | finite Schur/Feshbach-Grammatik, Resolventen- und Divisorgraph-Sprache | keine globale Positivität; finite Algebra | kein Schattenlimes; alte Determinante $\to1$ | **Feshbach-Grammatik direkt strukturell übernommen**, aber mit neuen P11-Operatoren | Baustein + No-Go |
| **P07** | Statistik, PSD-Testkegel, LFF/Rampe, RH-freies Herglotz-Kriterium | Testkegel-PSD; positive Nullstellenmaßform erst unter RH | Grenz-Jacobi/Herglotz würde bereits RH tragen | keine direkte C1-Konstruktion | diagnostische/konditionale Schnittstelle |
| **P08** | Jacobi-Kollapsdiagnose, exakter Mangoldt-Mellin-Kanal | keine neue globale positive Form; positive Prä-Lanczos-Metrik offen | Finite Part/Spurklasse/Operatorbrücke offen | hauptsächlich Firewalls; konkrete Architektur nicht übernommen | Diagnose / ersetzte Vorstufe |
| **P09** | nichttriviale geladene Hochschildstruktur | kohomologische Nichttrivialität, keine Hilbertpositivität | zyklische/Weil-/Gram-Brücke fehlt | keine direkte Verwendung im P11/C1-Kern | algebraischer Seitenzweig |
| **P10** | konsolidierte No-Gos P05–P09 | keine neue Positivitätsquelle | schützt vor falschen Abkürzungen | stark als Design-Constraints/Provenienz | Firewall |

### 14.8 Gesamtbild der Zwischenphase

Die Zwischenpapers liefern damit nicht den gesuchten globalen positiven Operator. Ihre historische Leistung ist eine andere:

```math
\text{P05–P06: lokale/finite Mechanismen}
\quad+\quad
\text{P07–P09: Diagnostik und Seitenpfade}
\quad+\quad
\text{P10: konsolidierte Firewalls}
```

führen zu einem stark eingeschränkten Suchraum. P11 beginnt anschließend tatsächlich mit einer neuen source-first finite-window Konstruktion, statt einen der alten globalen Kandidaten einfach fortzusetzen.

Die stärkste direkte Kontinuität ist **P06 → P11** über die Feshbach-/Schur-Sprache. P05 wirkt vor allem über Primkanal-/Nichtorthogonalitäts-Firewalls. P07–P09 werden nicht zum konstruktiven C1-Kern. P10 bleibt als Negativ- und Typenkontrolle wirksam.

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


## Durchlauf 7

M4 (`NEU-253` bis `NEU-257`) geprüft. Der adelische Haartransport erzeugt den RH-unabhängigen positiven Referenzraum $H_0=L^2(\mathbb R)$, aber keine Positivität der Weil-Form. Die vollständige Form ist dort unbeschränkt; nach Korrektur der Gamma-Normierung gilt für eine normierte Modulationsfolge $B_W(a_N,a_N)=\log N+O(1)$.

Der zentrale Firewall-Satz trägt: $L^2$-Semibeschränktheit von $B_W$ ist äquivalent zu RH. Unter RH ist $B_W$ auf Haar-$L^2$ zugleich nicht abschließbar; `NEU-257` enthält dafür einen direkten Folgenbeweis. Damit ist der Kato/KLMN-Weg auf diesem Hintergrund strukturell ausgeschlossen.

Die unter RH natürliche Weil-Vervollständigung ist stattdessen der atomare Raum $\mathcal H_W\cong\ell^2(\Gamma,m_\gamma)$; dies ist jedoch konditional und noch keine RH-freie Objekt-X-Konstruktion.

Im Zuge des Audits wurden Fourier-Shift, Schwartz-Schwanz und Gamma-$1/\pi$-Normierung in `NEU-255/256` über PR #178 korrigiert.

## Durchlauf 8

`NEU-259/260` und Suzukis aktueller finite-Intervall-Rahmen geprüft. Die lokalisierten Formen $Q_W^a$ sind RH-frei semibeschränkt und erzeugen selbstadjungierte $A_a$; nach einem Shift $\lambda<\lambda_a$ entstehen positive Hilberträume und selbstadjungierte first-order Erweiterungen mit reellen Spektren.

Diese Positivität ist jedoch Shift-Positivität, nicht Weil-Positivität. $Q_W^a\ge0$ für alle $a$ ist bereits RH-äquivalent. Ein gemeinsamer Shift, der die Nullfortsetzungen in allen $T$-Normen isometrisch machen würde, ist ebenfalls RH-äquivalent, weil er eine uniforme globale Haar-$L^2$-Untergrenze erzeugen würde.

Die vollständige Testkernidentität $B_W|_{C_c^\infty(-a,a)}=Q_W^a$ wurde geschlossen; außerdem wurde der Vorzeichenfehler $A_a\ge-\lambda_aI$ zu $A_a\ge\lambda_aI$ korrigiert. Diese und die globale Gauge-Firewall wurden über PR #179 integriert.

Parität reduziert die Erweiterungsfreiheit RH-frei auf zwei Zweige, selektiert aber keinen eindeutig. Die stärkste Zweigselektion in `NEU-260b.2` ist konditional auf Suzukis noch offene Grenzrelation. Ein RH-freier Direktgrenzraum, Mosco-/Resolventengrenzwert oder kanonischer $J_{a,b}$ ist in diesem historischen Strang nicht konstruiert.

## Durchlauf 9

P02 und P03 direkt geprüft. P02 enthält einen echten RH-freien surjektiven adelischen Port, die Autokorrelations-/Fourierpositivität und eine saubere komponentenweise Definition der vollständigen Weil-Form. Die arithmetische Positivität wird aber nicht aus dem Port hergeleitet. Wegen der Surjektivität ist Positivität des adelischen Pullbacks exakt äquivalent zur ursprünglichen Weil-Positivität.

P03 ist dagegen ein konsistentes No-Go-Paper: Haar-$L^2$ ist nur positive Referenzgeometrie; Semibeschränktheit ist RH-äquivalent und unter RH ist die Form dort nicht abschließbar. Das Paper konstruiert keinen positiven Objekt-X-Operator.

Beim Re-Audit wurde P02s finite Projektion von der falschen Integration über ganz $\mathbb A_f$ auf die tatsächlich verwendete Paarung mit $\mathbf 1_{\widehat{\mathbb Z}}$ korrigiert; außerdem wurden Polterm-Hermitezität und die Pullback-Firewall explizit bereinigt. P03 wurde synchronisiert. PR #180 enthält diese Korrekturen.

Der spätere P11/C1-Kern verwendet P02/P03 vor allem als Schnittstelle beziehungsweise Firewall. Die konkrete source-first finite-window Geometrie mit Martingalprojektionen, Gamma-Graphen und Feshbach-Korrekturen ist eine spätere neue Konstruktion; die globale adelische Anbindung bleibt in P11 selbst als offene Verpflichtung stehen.

## Durchlauf 10

P04 vollständig gegen die finite Suzuki- und Uniform-Shift-Firewall geprüft. Die lokale Wahl $\lambda_{\rm w}(a)=\lambda_a-1$ ist RH-frei und liefert $T_a^{\rm w}\ge I$, kanonisiert aber nur die einzelne Stufe.

Für Nullfortsetzung zwischen zwei Fenstern wurde der exakte Shiftdefekt eingetragen. Ein gemeinsamer Shift, der alle Stufen isometrisch kompatibel machen würde, ist RH-äquivalent. Alternative nichttriviale Transporte $J_{a,b}$ bleiben logisch möglich, müssen aber eigenständig konstruiert werden.

Die Paritätsreduktion $U(1)\to\mathbb Z_2$ trägt, selektiert jedoch keinen eindeutigen Zweig. `NEU-260b.2` liefert nur eine konditionale asymptotische Auswahl unter Suzukis Grenzvermutung. Defizitindizes wurden korrekt dem minimalen symmetrischen Operator zugeordnet.

P04 behauptet weder $J_{a,b}$ noch den induktiven Grenzraum als Satz; der globale Teil war bereits conjectural. PR #181 schärft diese lokal/global-Grenze und synchronisiert P04 mit den aktuellen NEU-Audits.

## Durchlauf 11

P05–P10 als gebündelte Zwischenphase geprüft. P05 enthält tragfähige lokale Primkanal-/Transport- und arithmetische Gewichtsaussagen, aber keine globale Grampositivität. P06 liefert die finite Feshbach-/Schur-Grammatik, die später strukturell in P11 wiederkehrt; die historische Determinantenskalierung kollabiert dagegen auf $D_N\to1$.

P07/P08/P09 sind überwiegend diagnostische, konditionale oder seitliche Pfade. In P07 wurde ein echter RH-Typfehler korrigiert: $m_{\rm arith}=-\Xi'/\Xi$ ist nun RH-frei meromorph definiert; positive reelle Nevanlinna-Maßdarstellung und Summe-von-Quadraten-Weilbrücke sind explizit RH-konditional. PR #182 und die synchronisierte Markdown-Quelle enthalten die Korrektur.

P08s belastbarer Kern sind Renormierungsdiagnosen und der korrekte Mangoldt-Mellin-Kanal; die operatorische Finite-Part-/Fredholm-Brücke bleibt offen. P09 liefert echte geladene Hochschildstruktur, aber keine positive Weil-/Gramgeometrie und wird im heutigen C1-Kern nicht direkt verwendet.

P10 bleibt als No-Go-/Firewall-Sammlung architektonisch wichtig. Es sperrt die alten Abkürzungen, ohne die spätere nichtorthogonale source-first Objekt-X-Geometrie auszuschließen. Die Abhängigkeitsmatrix zeigt als stärkste konstruktive Kontinuität P06→P11; P05 liefert vor allem Typ-/Primkanalgrenzen, P07–P09 werden weitgehend nicht in C1 fortgeführt.

## Korrekturblock – 27. September 2026

Die beiden Fehler samt direkter operatorischer Folgestellen wurden über PR #176 korrigiert und in main gemergt.

Geprüfter Ausgangspunkt für die Fortsetzung:

**main@a77950be027dc1576b016c6a53bfad7ff65a04e4**

---

# III. Nächster Prüfpunkt

Nun **P11 selbst neu lesen**, aber erstmals aus der unabhängig rekonstruierten Vorgeschichte heraus:

> Welche Teile von P11 sind wirklich neue source-first Mathematik, welche sind nur re-instantiierte endliche Feshbach-/Gamma-Bausteine, und an welchem exakten Punkt beginnt die heute relevante Defekt-/Transport-/C1-Linie?

Besonders zu trennen sind finite-horizon Positivität, Gamma-Graphraum, Martingal-Restgeometrie, Feshbach-Schur-Korrektur, Übergangsmetriken, starker Transport und die ausdrücklich weiterhin offenen globalen Gram-/adelischen/Fredholm-Schichten.
