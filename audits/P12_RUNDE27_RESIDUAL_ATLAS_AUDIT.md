# P12 Runde 27 — exakter Residual-Atlas und 43×43-Einschalen-Kandidat

**Status:** Kandidat; **nicht promotet**.  
**Repo-Basis:** `Waschtl904/objekt-x-programm`, `main@e8e1aa23655b4a0a9ee2e0f865ef3a201fc103cf`.  
**Input:** A15.1b2h/C42 `✓[M]_part`, A15.1b2i/C44 `✓[M]_part`, A15.1b2k/C26-Korridor `✓[M]_part`.  
**Firewall:** P11 FROZEN; R14 unverändert; keine Aussage zu Polar Gauge, Terminal Transport, Objekt X oder RH.

---

## 1. Ziel und notwendige Ebenentrennung

Round 27 vereinigt die bereits bewiesenen lokalen Kammern C42, C44 und
\(C_{26}^{-}\cup C_{26}^{+}\) und bestimmt, was im residual-overlap-Bereich

\[
0<R<\rho,\qquad R<\sigma<\varepsilon<\varepsilon_{\max}
\]

tatsächlich unbedeckt bleibt.

Dabei müssen zwei Ebenen strikt getrennt werden:

1. **physikalischer Parameterschatten** in \((R,\sigma,\varepsilon)\):
   Existiert wenigstens ein \(x\), für das ein lokales Zertifikat greift?
2. **Faseratlas** in \((R,x,\sigma,\varepsilon)\):
   Für welche einzelnen \(x\)-Fasern ist \(h(x)=0\) bereits erzwungen?

Ein Punkt im projizierten Schatten bedeutet nur

\[
\exists x:\ h(x)=0
\]

für den jeweiligen lokalen Mechanismus. Daraus folgt **keine** globale
Kerneltrivialität für den physikalischen Parameterpunkt. Diese Unterscheidung
ist für den Rest von P12 zwingend.

---

## 2. Konstanten

Wie bisher

\[
\eta=e-2\delta,\qquad
\chi=3\delta-e,\qquad
\delta=\eta+\chi,
\]

\[
\kappa=e-\delta=2\eta+\chi,
\qquad
E:=\varepsilon_{\max}=\frac12\log\frac54,
\qquad
\rho=E-\delta.
\]

Für den Atlas sind zusätzlich nützlich

\[
r_*:=\frac{\chi-\eta}{2},
\qquad
s_*:=\frac{3\eta+\chi}{2},
\qquad
t_*:=\frac{3\delta}{2}.
\]

Numerisch

\[
\eta\approx0.026058000569507,
\quad
\chi\approx0.032833517258685,
\]

\[
\delta\approx0.058891517828192,
\quad
\rho\approx0.052680257828913,
\]

\[
r_*\approx0.003387758344589,
\quad
s_*\approx0.055503759483603,
\quad
t_*\approx0.088337276742288.
\]

Der retained verifier zertifiziert mit gerichteten rationalen
Logarithmusschranken insbesondere

\[
0<r_*<\eta<\chi<\rho,
\qquad
2\eta<s_*<t_*<E,
\qquad
\frac\delta2<\rho.
\]

---

## 3. Exakte Projektion der bewiesenen Kammern

Sei

\[
\mathcal A:=\{(R,\sigma,\varepsilon):
0<R<\rho,\ R<\sigma<\varepsilon<E\}.
\]

Für eine Vierparameterkammer \(C\) bezeichne

\[
\pi(C):=\{(R,\sigma,\varepsilon):\exists x\ (R,x,\sigma,\varepsilon)\in C\}.
\]

Die Eliminierung von \(x\) ist hier reine Fourier--Motzkin-Elimination
einer Variablen. Der Verifier führt sie symbolisch aus und prüft die kompakten
Darstellungen gegen sämtliche erzeugten Ungleichungen auf den exakten
Polyederabschlüssen.

### 3.1 C42-Schatten

\[
\boxed{P_{42}:=\pi(C_{42})}
\]

ist exakt durch

\[
\boxed{\chi-\eta<2R<\delta,}
\]

\[
\boxed{R<\sigma,\qquad R+\sigma>\chi,\qquad 2\sigma>\delta,}
\]

\[
\boxed{\sigma+\varepsilon>\kappa,}
\]

\[
\boxed{2\sigma<3\eta+\chi,\qquad
       2\varepsilon>3\eta+\chi,}
\]

\[
\boxed{\varepsilon<E}
\]

gegeben.

### 3.2 C44-Schatten

\[
\boxed{P_{44}:=\pi(C_{44})}
\]

ist exakt durch

\[
\boxed{\chi-\eta<2R<\delta,}
\]

\[
\boxed{3\eta+\chi<2\sigma<3\delta,}
\]

\[
\boxed{2\varepsilon>3\delta,\qquad\varepsilon<E}
\]

gegeben.

Die restlichen physikalischen Ordnungsrelationen werden von diesen
Ungleichungen automatisch impliziert.

### 3.3 C26-Schatten

Für die beiden promovierten Round-26-Kammern ergibt die symbolische
Elimination überraschend

\[
\boxed{\pi(C_{26}^{-})=\pi(C_{26}^{+})=:P_{26}.}
\]

Der gemeinsame Schatten ist exakt

\[
\boxed{\chi-\eta<2R<2\eta,}
\]

\[
\boxed{\chi<\sigma<2\eta,\qquad\varepsilon>2\eta,}
\]

\[
\boxed{R+\sigma>2\chi-\eta,}
\]

\[
\boxed{\sigma-R<3\eta-\chi,}
\]

\[
\boxed{R+\varepsilon>\delta,\qquad\varepsilon<E.}
\]

Dies ist ein wichtiger Scope-Befund:

> Das J-Gluing von Round 26 vergrößert die **Faserabdeckung in x**, nicht den
> projizierten physikalischen Parameterbereich.

Der Korridor bleibt mathematisch stärker als eine einzelne C26-Kammer, aber
seine Stärke ist auf der Faserebene sichtbar.

---

## 4. Vereinigter physikalischer Schatten

Definiere

\[
\boxed{\mathcal U_{27}:=P_{42}\cup P_{44}\cup P_{26}.}
\]

Zwei Schwellen strukturieren den sichtbaren Teil besonders klar:

\[
s_* = \frac{3\eta+\chi}{2},
\qquad
t_* = \frac{3\delta}{2}.
\]

- \(P_{26}\) liegt unter \(\sigma<2\eta\) und oberhalb
  \(\varepsilon>2\eta\).
- \(P_{42}\) liegt unter \(\sigma<s_*\) und oberhalb
  \(\varepsilon>s_*\).
- \(P_{44}\) liegt unter \(\sigma<t_*\) und oberhalb
  \(\varepsilon>t_*\), mit \(\sigma>s_*\).
- alle drei Schatten verlangen \(R>r_*\).

Insbesondere trägt Round 26 im projizierten Bild eine echte
Niedrig-\(\varepsilon\)-Zunge unterhalb des C42-Niveaus bei; sein
J-Spiegel erzeugt dort aber keinen zweiten physikalischen Schatten.

---

## 5. Tatsächliche offene Restkomponenten

Um reine Grenzwände nicht fälschlich als offene Gebiete mitzuzählen, definieren
wir den **offenen unbedeckten Rest** relativ zu \(\mathcal A\) durch

\[
\mathcal G_{27}
:=
\mathcal A\setminus
\bigl(
\overline{P_{42}}^{\mathcal A}
\cup
\overline{P_{44}}^{\mathcal A}
\cup
\overline{P_{26}}^{\mathcal A}
\bigr).
\]

### Kandidat R27-A — Komponentenatlas

\[
\boxed{\mathcal G_{27}\text{ besitzt genau eine offene wegzusammenhängende Komponente.}}
\]

Es gibt also **nicht** mehrere getrennte residual-overlap-Inseln im
physikalischen Schattenatlas.

#### Pfadzertifikat

Alle drei projizierten Kammern sind für festes \((R,\sigma)\) in
\(\varepsilon\) nach oben monoton: ihre Bedingungen enthalten nur untere
\(\varepsilon\)-Schranken und die gemeinsame arithmetische Decke \(E\).
Daher kann ein Punkt außerhalb ihrer abgeschlossenen Vereinigung durch
Absenken von \(\varepsilon\) nicht neu in eine der Kammern eintreten.

Man senkt \(\varepsilon\) zunächst in einen der sicheren
Staircase-Korridore unterhalb der jeweils relevanten Ebene

\[
2\eta,\qquad s_*,\qquad t_*.
\]

Danach kann \(R\) auf einen Wert

\[
0<R<r_*
\]

abgesenkt werden. Dort ist die abgeschlossene Vereinigung sämtlicher drei
Schatten unmöglich, weil alle drei \(R\ge r_*\) verlangen. Die
\(R<r_*\)-Scheibe des ambienten Dreiecks

\[
R<\sigma<\varepsilon<E
\]

ist konvex. Damit lassen sich alle Punkte des offenen Restes zu einem
gemeinsamen Anker verbinden.

Falls ein Ausgangspunkt zufällig auf einer der reinen Atlas-Hyperflächen
\(\sigma=2\eta,s_*,t_*\) liegt, erlaubt die Offenheit von
\(\mathcal G_{27}\) zunächst eine beliebig kleine Perturbation weg von der
Hyperfläche; dadurch entsteht keine zusätzliche Komponente.

Vor unabhängiger Prüfung:

\[
\boxed{\mathrm{R27\!\!-\!A}:?[O].}
\]

---

## 6. Warum eine globale Komponente nicht die richtige Forschungsgranularität ist

Der topologische Befund bedeutet **nicht**, dass der Rest mathematisch
homogen ist. Innerhalb der einzigen globalen Restkomponente liegen mehrere
unterschiedliche Rohoperator-Pattern-Zellen.

Für den nächsten Fortschritt ist daher nicht die Topologie, sondern die Zahl
neuer Sichtbarkeitsvariablen, fehlender Source-Rows und Pattern-Facetten die
richtige Priorisierung.

Der günstigste Fronttyp liegt genau zwischen dem alten 42er-Supportpattern
und dem gepaarten 44er-Supportshell.

---

## 7. Priorität 1: einseitige 43×43-Supportschale

Setze wieder \(D:=\delta\) und \(K:=\kappa\).

### 7.1 Linke Zelle \(W_{43}^{<}\)

Definiere

\[
\boxed{x>\eta,}
\tag{43<.1}
\]

\[
\boxed{R<x,\qquad R+x>\chi,}
\tag{43<.2}
\]

\[
\boxed{x+\eta<\sigma,\qquad \sigma+x<\kappa,}
\tag{43<.3}
\]

\[
\boxed{x+\delta<\varepsilon<E.}
\tag{43<.4}
\]

Diese sieben Facetten implizieren automatisch

\[
0<R<x<\frac\delta2<\sigma<\varepsilon<E,
\qquad R<\rho.
\]

Die 42 Round-23/C42-Quellen erzeugen hier exakt **43** Sichtbarkeitsvariablen:
die 42 alten plus

\[
U_+=(1,5,0).
\]

Die nächste Schalenquelle

\[
V_+=(1,4,3)
\]

ist horizon-legal und erzeugt keine weitere Sichtbarkeitsvariable. Damit wird
das System exakt quadratisch:

\[
\boxed{M_{43}^{<}\in\operatorname{Mat}_{43\times43}.}
\]

Der Verifier bestimmt die konstante Pattern-Kammer nicht durch Sampling,
sondern aus allen 43 Source-Horizon-Bedingungen und allen kanonischen Rohslots.
Es entstehen **758** lineare Rohbedingungen. Der abgeschlossene
Siebenfacetten-Polyeder besitzt **12** relevante Ecken; sämtliche 758
Ungleichungen werden dort mit gerichteten rationalen Logarithmusschranken
zertifiziert.

Die sechs echten Rohoperator-Facetten sind

\[
x=\eta,\quad x=R,\quad R+x=\chi,\quad
\sigma=x+\eta,\quad \sigma+x=\kappa,\quad
\varepsilon=x+\delta,
\]

zuzüglich der arithmetischen Decke \(\varepsilon=E\).

Damit ist \(W_{43}^{<}\) eine exakte konstante Pattern-Zelle des ausgewählten
43-Source-Zertifikats.

### 7.2 J-Spiegel \(W_{43}^{>}\)

Unter

\[
J(s,m,n)=(-s,m,n+s),\qquad x\mapsto\delta-x
\]

geht \(W_{43}^{<}\) exakt über in

\[
\boxed{x<\chi,}
\]

\[
\boxed{x<\delta-R,\qquad x<R+\eta,}
\]

\[
\boxed{\sigma+x>\kappa,\qquad \sigma<x+\eta,}
\]

\[
\boxed{\varepsilon+x>2\delta,\qquad\varepsilon<E.}
\]

Die zusätzliche Quelle ist dort

\[
V_-=(-1,4,4)=J(V_+),
\]

und die neue Sichtbarkeitsvariable

\[
U_-=(-1,5,1)=J(U_+).
\]

In natürlicher J-gepaarter Ordnung bestätigt der Verifier

\[
\boxed{M_{43}^{>}=M_{43}^{<}.}
\]

---

## 8. Exakte Nichtentartung des 43×43-Kandidaten

Das 43er-System ist nicht nur strukturell günstig; sein Determinantentest
fällt ebenfalls positiv aus.

Da jede Matrixzeile homogen linear in \((p,q,r)\) ist, setze

\[
\beta=\frac qp=2^{-3/4},
\qquad
v=\left(\frac rp\right)^2
=\frac{\log3}{\log2}\sqrt{\frac8{27}}.
\]

Nach \(p=1\) und \(r/p=\sqrt v\) ergibt die exakte symbolische Elimination

\[
\det M_{43}^{<}
= p^{43}\,\beta\,v^{7/2}\,G_{43}(\beta,v),
\]

wobei

\[
\begin{aligned}
G_{43}(\beta,v)={}&36\beta^{16}-3\beta^{14}v^2+18\beta^{14}v-288\beta^{14}
+\beta^{12}v^3+14\beta^{12}v^2-282\beta^{12}v+1008\beta^{12}\\
&-3\beta^{10}v^3-215\beta^{10}v^2+1314\beta^{10}v-2016\beta^{10}
+\beta^8v^5-\beta^8v^4-134\beta^8v^3+1126\beta^8v^2-2970\beta^8v+2520\beta^8\\
&+\beta^6v^5-81\beta^6v^4+736\beta^6v^3-2529\beta^6v^2+3750\beta^6v-2016\beta^6\\
&-32\beta^4v^5+345\beta^4v^4-1425\beta^4v^3+2834\beta^4v^2-2718\beta^4v+1008\beta^4\\
&-6\beta^2v^6+91\beta^2v^5-473\beta^2v^4+1187\beta^2v^3-1573\beta^2v^2+1062\beta^2v-288\beta^2\\
&+8v^6-64v^5+210v^4-362v^3+346v^2-174v+36.
\end{aligned}
\]

Mit einem unabhängig von Fließkomma aufgebauten Fraction-Intervall für
\(\log2,\log3\), \(2^{-3/4}\) und \(\sqrt{8/27}\) liefert der retained
Verifier

\[
\boxed{
-0.048057943920223084
< G_{43}(\beta,v)
< -0.04805794392022283.
}
\]

Damit gilt für den Kandidaten exakt

\[
\boxed{\det M_{43}^{<}\ne0,\qquad\det M_{43}^{>}\ne0.}
\]

Folglich würde nach unabhängiger Bestätigung in beiden Zellen jede der 43
live visibility coordinates verschwinden.

### Kandidat R27-B

\[
\boxed{W_{43}^{<}\cup W_{43}^{>}\text{ ist lokal durch ein invertierbares }43\times43\text{-Zertifikat geschlossen}.}
\]

Vor unabhängiger Prüfung:

\[
\boxed{\mathrm{R27\!\!-\!B}:?[O].}
\]

Keine Promotion in P12 vor unabhängigem GREEN.

---

## 9. Warum W43 die mathematisch günstigste Front ist

Die Priorisierung ist strukturell, nicht heuristisch:

1. Gegenüber C42 kommt **genau eine** neue Sichtbarkeitsvariable hinzu.
2. **Eine** bereits kanonische nächste Schalenquelle stellt die Quadratur
   43×43 wieder her.
3. Die Zelle besitzt nur sechs echte Rohoperator-Facetten plus die
   arithmetische Decke.
4. Sie ist exakt J-symmetrisch; eine Seite genügt algebraisch.
5. Das 43×43-System ist ein natürlicher Ein-Zeilen/Ein-Spalten-Zwischenschritt
   zwischen dem promovierten M42- und M44-Mechanismus.
6. Die exakte Nichtentartung ist bereits im retained verifier zertifiziert.

Damit ist W43 vor den übrigen Restfronten zu bearbeiten bzw. unabhängig zu
reviewen.

---

## 10. Nachgeordnete Restfronten

Nach W43 bleiben insbesondere folgende strukturell schwierigere Familien:

- **next-shell horizon gap:** beide ersten Supportvariablen sind sichtbar,
  aber die gepaarten nächsten Schalenquellen sind noch nicht beide
  horizon-legal;
- **deep horizon remainder:** unterhalb bzw. außerhalb des Round-26-Korridors
  ändern sich weitere Horizon-/Supportmuster des 92er-Zertifikats;
- **outer-core remainder:** \(R\le r_*\) oder x-Fasern außerhalb des gemeinsamen
  C42/C44-Basiskerns; hier fehlt bereits die feste 42er-Ausgangsgeometrie.

Diese Familien sind **Pattern-Fronten innerhalb derselben globalen offenen
Restkomponente**, nicht getrennte topologische Inseln.

---

## 11. Verifier-Ausgabe

Der retained verifier soll liefern:

```text
R27_CONSTANT_ORDER = PASS
R27_C26_SHADOW_IDENTITY = PASS
R27_P42_COMPACT_EQUIV = PASS
R27_P44_COMPACT_EQUIV = PASS
R27_P26_COMPACT_EQUIV = PASS
R27_SINGLE_OPEN_REMAINDER_COMPONENT = PASS
R27_M43_RAW_SHAPE = PASS 43x43
R27_W43_GENUINE_RAW_FACETS = PASS
R27_W43_PATTERN_CERTIFICATE = PASS 12 vertices 758 raw inequalities
R27_W43_J_CHAMBER_MAP = PASS
R27_W43_J_MATRIX_IDENTITY = PASS
R27_M43_NORMALIZED_FACTOR_INTERVAL = PASS
R27_M43_DET_FACTOR = PASS
ROUND27_RESIDUAL_ATLAS_VERIFY = PASS
```

---

## 12. Scope und Booking vor Review

Round 27 behauptet vor unabhängiger Prüfung **nicht**:

- globale Injectivity für den residual overlap;
- dass der physikalische Parameterschatten eine Kerneltrivialität beweist;
- dass W43 bereits promotet ist;
- einen neuen globalen R-Threshold;
- irgendeine Änderung an P11 oder R14;
- Polar Gauge, Terminal Transport, Objekt X oder RH.

Vor Review bleibt die Buchung

\[
\boxed{\mathrm{R27\!\!-\!A}:?[O],\qquad
       \mathrm{R27\!\!-\!B}:?[O].}
\]
