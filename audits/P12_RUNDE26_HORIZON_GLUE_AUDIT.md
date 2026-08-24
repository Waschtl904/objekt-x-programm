# P12 Runde 26 — exakte 92er-Facetten und Horizon-Gluing

**Status:** lokaler Theorem-Kandidat; **nicht promotet**.  
**Repo-Basis:** `Waschtl904/objekt-x-programm`, `main@9b0982e40b60730c4936eb8910ef425c883ccfb4`.  
**Input:** A15.1b2j / Round 25, `✓[M]_part`, invertierbarer 92×92-Horizon-Circuit.  
**Firewall:** P11 FROZEN; R14 unverändert; keine Aussage zu Polar Gauge, Terminal Transport, Objekt X oder RH.

---

## 1. Ziel

Round 25 bewies den 92×92-Circuit zunächst nur auf der kleinen rationalen Box

\[
0.0195<R<0.0205,\quad
0.0275<x<0.0285,\quad
0.0395<\sigma<0.0405,\quad
0.0550<\varepsilon<0.0559.
\]

Round 26 bestimmt stattdessen die **exakte konstante Pattern-Kammer der fest gewählten 92 Round-25-Zeilen**, identifiziert sämtliche echten Rohoperator-Facetten und verklebt diese Kammer mit ihrem \(J\)-Spiegel über eine offene Schnittmenge.

Es wird **keine neue Determinante** gebraucht: innerhalb der neuen Kammern ist die Rohmatrix koeffizientenweise exakt dieselbe bereits promovierte Matrix \(M_{92}\).

---

## 2. Konstanten

Wie bisher

\[
\eta=e-2\delta,\qquad
\chi=3\delta-e,\qquad
\delta=\eta+\chi,
\]

und

\[
\kappa=e-\delta=2\eta+\chi.
\]

Ferner

\[
e=3\eta+2\chi,\qquad
T=14\eta+10\chi.
\]

Numerisch

\[
\eta\approx0.026058000569507,\qquad
\chi\approx0.032833517258685.
\]

Die arithmetische Obergrenze bleibt

\[
\varepsilon_{\max}=\frac12\log\frac54.
\]

---

## 3. Der feste Minus-92-Zertifikatssatz

Verwendet werden exakt dieselben 92 Quellen wie in Round 25:

- 41 überlebende Quellen des Round-23-Blocks;
- der 51-Quellen-Horizon-Circuit aus Round 25.

Die alte verlorene Quelle `(-1,5,1)` gehört **nicht** zum ausgewählten 92er-Zertifikat. Deshalb ist ihre spätere Wieder-Legalität kein Pattern-Wechsel der ausgewählten Matrix.

Aus allen

\[
92\times 6
\]

kanonischen Rohslots sowie den 92 Source-Horizon-Bedingungen entstehen 1628 lineare Sign-/Support-/Horizon-Ungleichungen.

Nach exakter Reduktion bleibt eine Kammer mit **nur acht echten Rohfacetten**.

---

## 4. Exakte Minus-Kammer \(C_{26}^{-}\)

Definiere

\[
\boxed{\eta<x<\chi,}
\tag{26-.1}
\]

\[
\boxed{\chi<R+x<2\eta,}
\tag{26-.2}
\]

\[
\boxed{x-R<\eta,}
\tag{26-.3}
\]

\[
\boxed{\chi-\eta<\sigma-x,}
\tag{26-.4}
\]

\[
\boxed{\sigma+x<3\eta,}
\tag{26-.5}
\]

\[
\boxed{x+\eta<\varepsilon<\varepsilon_{\max}.}
\tag{26-.6}
\]

Diese Bedingungen implizieren automatisch

\[
0<R<x<\sigma<\varepsilon<\varepsilon_{\max}.
\]

Außerdem gilt

\[
R<\eta<\rho,
\]

also liegt die gesamte Kammer im residual-overlap-Bereich unter \(\rho\).

### Kandidat R26-A

Für jeden Parameterpunkt in \(C_{26}^{-}\) rekonstruieren die 92 ausgewählten Quellen **exakt dieselbe symbolische Matrix \(M_{92}\)** wie in Round 25.

Da Round 25 bereits unabhängig GREEN für

\[
\det M_{92}\neq0
\]

erhalten hat, folgt in \(C_{26}^{-}\)

\[
\boxed{h(x)=0,\qquad h(\delta-x)=0}
\]

für jeden Kernelvektor.

Vor unabhängiger Prüfung:

\[
\boxed{\text{R26-A}:?[O].}
\]

---

## 5. Die acht echten Rohoperator-Facetten

Der neue Verifier zeigt zwei Richtungen:

1. Jede der folgenden acht Ungleichungen tritt tatsächlich als Rohoperator-Ereignis auf.
2. Alle übrigen 1620 Rohbedingungen werden durch diese acht plus \(\varepsilon<\varepsilon_{\max}\) impliziert.

Damit beschreiben sie exakt die verbundene konstante Pattern-Kammer des fest ausgewählten 92er-Zertifikats innerhalb der P12-Arithmetik.

| Facette | Rohoperator-Ereignis |
|---|---|
| \(x=\eta\) | u.a. Quelle `(1,-1,2)` erreicht \(u=0\); insgesamt 7 Rohereignisse |
| \(x=\chi\) | Signwechsel des Slots `(1,1,-3)` |
| \(R+x=\chi\) | \(|x-\chi|\) trifft die untere Supportgrenze |
| \(R+x=2\eta\) | Koordinate \(2\eta-x\) trifft \(R\); 6 Rohslots |
| \(x-R=\eta\) | Koordinate \(x-\eta\) trifft \(R\); 6 Rohslots |
| \(\sigma-x=\chi-\eta\) | ein live upper-support Modus trifft \(T+\sigma\); 3 Rohslots |
| \(\sigma+x=3\eta\) | ein bisher oberhalb liegender Modus trifft \(T+\sigma\) |
| \(\varepsilon=x+\eta\) | Quelle `(1,5,0)` trifft den oberen Horizont |

Die Round-25-Dezimalgrenzen `0.0195,0.0205,...` sind daher **keine mathematischen Facetten**.

---

## 6. Wichtiger Horizon-Befund

Die ehemalige harte Minus-Horizon-Wand lautet

\[
\varepsilon+x=\kappa.
\]

Sie ist **keine Facette von \(C_{26}^{-}\)**.

Das ist kein Widerspruch zu Round 25: die Quelle `(-1,5,1)`, deren Legalität dort wechselt, wurde aus dem 92er-Zertifikat bereits entfernt.

Folglich läuft dieselbe invertierbare 92er-Matrix lokal **durch diese Horizon-Wand hindurch**.

Round 26 zeigt daher stärker als Round 25:

\[
\boxed{\varepsilon+x=\kappa\text{ ist für das ausgewählte 92er-Zertifikat keine Barriere.}}
\]

Dies ist eine lokale Zertifikatsaussage, kein globaler Horizon-Wall-Satz.

---

## 7. \(J\)-Spiegelkammer \(C_{26}^{+}\)

Unter

\[
J(s,m,n)=(-s,m,n+s),\qquad x\mapsto\delta-x,
\]

geht \(C_{26}^{-}\) exakt in die Plus-Kammer über:

\[
\boxed{\eta<x<\chi,}
\tag{26+.1}
\]

\[
\boxed{R+x>\chi,}
\tag{26+.2}
\]

\[
\boxed{\chi-\eta<x-R<\eta,}
\tag{26+.3}
\]

\[
\boxed{\sigma+x>2\chi,}
\tag{26+.4}
\]

\[
\boxed{\sigma-x<2\eta-\chi,}
\tag{26+.5}
\]

\[
\boxed{\varepsilon+x>\kappa,\qquad\varepsilon<\varepsilon_{\max}.}
\tag{26+.6}
\]

Die gespiegelten 92 Quellen und 92 Variablen liefern koeffizientenweise

\[
\boxed{M_{92}^{+}=M_{92}^{-}.}
\]

Damit folgt auch in \(C_{26}^{+}\)

\[
\boxed{h(x)=h(\delta-x)=0.}
\]

Vor unabhängiger Prüfung:

\[
\boxed{\text{R26-B}:?[O].}
\]

---

## 8. Offene Überlappung — echtes Gluing

Die beiden Kammern berühren sich nicht bloß an einer Randfläche.

Die rationale Box

\[
\boxed{0.014<R<0.016,}
\]

\[
\boxed{0.0293<x<0.0296,}
\]

\[
\boxed{0.041<\sigma<0.043,}
\]

\[
\boxed{0.065<\varepsilon<0.075}
\tag{B26-cap}
\]

liegt strikt in

\[
C_{26}^{-}\cap C_{26}^{+}.
\]

Der Verifier bestätigt dies mit gerichteten rationalen Schranken für \(\log2,\log3,\log5\).

Damit sind \(C_{26}^{-}\) und \(C_{26}^{+}\)

- offen,
- konvex,
- mit nichtleerer offener Schnittmenge.

Also ist

\[
\boxed{C_{26}^{-}\cup C_{26}^{+}}
\]

ein offener zusammenhängender lokaler Horizon-Korridor.

Es gibt innerhalb dieses Korridors **keine Nahtlücke zwischen der Minus- und Plus-Zertifikatsseite**.

---

## 9. Exaktes Polyederzertifikat

Der retained verifier arbeitet nicht mit Stichproben als Beweis.

Er schreibt

\[
\delta=\eta+\chi,\quad e=3\eta+2\chi,\quad T=14\eta+10\chi
\]

und betrachtet den abgeschlossenen Polyederabschluss von \(C_{26}^{-}\).

In vier Parameterdimensionen besitzt dieser Abschluss 20 relevante Ecken.

Für jede der 1628 linearen Rohbedingungen wird das Minimum auf allen 20 Ecken mit **exakten rationalen Intervallen** für

\[
\eta,\chi,\varepsilon_{\max}
\]

zertifiziert.

Ausgabe:

```text
R26_EIGHT_RAW_FACETS = PASS
R26_POLYHEDRAL_PATTERN_CERTIFICATE = PASS 20 vertices 1628 raw inequalities
R26_B25_STRICT_SUBSET = PASS
R26_J_CHAMBER_MAP = PASS
R26_J_MATRIX_IDENTITY = PASS
R26_OPEN_OVERLAP_BOX = PASS
ROUND26_HORIZON_GLUE_VERIFY = PASS
```

Damit ist die Scope-Erweiterung selbst algebraisch/polyedrisch abgesichert; es wird nicht von ein paar zufälligen Punkten extrapoliert.

---

## 10. Was Round 26 nicht behauptet

Round 26 schließt **nicht**

- den vollständigen residual overlap \(0<R<\rho,\sigma>R\);
- die gesamten beiden Horizon-Wände;
- einen neuen globalen Radius-Threshold;
- irgendeinen P11/R14-Schritt.

Insbesondere werden weder \(\omega\) noch die Search-Tiefe 21 noch eine andere neu auftauchende Zahl als Schwelle gebucht.

---

## 11. Empfohlene unabhängige Prüfung

Perplexity sollte unabhängig kontrollieren:

1. die acht Facetten aus den 92 Quellen und sechs Rohslots;
2. dass diese acht tatsächlich alle weiteren Rohbedingungen implizieren;
3. dass die Round-25-B25−-Box strikt in \(C_{26}^{-}\) liegt;
4. die exakte \(J\)-Transformation auf \(C_{26}^{+}\);
5. die offene Überlappungsbox `B26-cap`;
6. dass innerhalb beider Kammern tatsächlich exakt die bereits GREEN-geprüfte \(M_{92}\) rekonstruiert wird.

Falls GREEN, wäre die richtige Buchung

\[
\boxed{\text{Round 26 horizon corridor}:\checkmark[M]_{\rm part}.}
\]

Keine globale Promotion unter \(\rho\).
