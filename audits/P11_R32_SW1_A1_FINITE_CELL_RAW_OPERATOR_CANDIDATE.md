# P11/R32 — SW1-A1 Finite-Cell Raw Operator Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a0-coverage@846b856b0e07a40ac24236b1a05b7b430e86e3e0  
> **Status:** `AI-GREEN candidate + independent GREEN (certificate)` — vollständiges operatorwertiges finite-cell Rohsystem auf SW1 zertifiziert; **keine Promotion**.  
> **Scope:** erste augmentierte Gleichung auf SW1 nach A0-Coverage. Keine Injektivität.

---

## 0. Ziel und Firewall

Nach SW1-A0 ist der vollständige freie Koordinatenraum
\[
\mathcal K_R
\cong
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R^{\rm SW1})
\]
a.e. durch endlich viele räumliche Zellen abgedeckt.

A1 bestimmt nun die **erste augmentierte Gleichung**
\[
\boxed{
(I+A)y+HE_{\mathcal A}w=0
}
\tag{A1.1}
\]
auf diesen Zellen explizit.

Dabei ist
\[
A=R_{T_0}^*R_{T_0}
\]
die Summe der elf bereits auditierten Vier-Echo-Wörter.

**Wichtig:** finite-cell bedeutet hier eine endliche Matrix von
Restriktions-/Translations-/Reflexionsoperatoren zwischen \(L^2\)-Zellen.
Es bedeutet **nicht** endlichdimensionale Punktfasern und rechtfertigt noch keinen
gewöhnlichen Determinantentest.

---

## 1. Konstanten

Wie bisher:
\[
a=\frac12\log2,\qquad
b=\frac12\log3,\qquad
T=2a,
\]
\[
d=b-a,\qquad
e=T-b,\qquad
\Delta=d-e,
\qquad
T_0=T+\varepsilon.
\]

Für die elf Wortgewichte schreiben wir
\[
c_1,\ldots,c_{11}
\]
wie in HT.4 und setzen
\[
\alpha_A:=c_1+c_5,
\qquad
\alpha_b:=c_1+c_5+c_{11},
\]
\[
\kappa:=c_1+c_5+c_9+c_{10}+c_{11},
\]
\[
\beta_0:=-c_1+c_3,
\qquad
\beta_-:=-c_2-c_4,
\]
\[
\beta_+:=c_2+c_6,
\qquad
\beta_T:=-c_3-c_5-c_7-c_{10},
\qquad
\beta_b:=-c_{11}.
\tag{A1.2}
\]

---

## 2. Vollständige A-Row-Archetypen auf \(0<x<T_0\)

Die bereits unabhängig geprüfte A-Wall-Liste lautet
\[
\{\varepsilon,\ a-\varepsilon,\ a+\varepsilon,\ 2d-\varepsilon,\ T-\varepsilon\}.
\]

Zusätzlich trennen wir bei \(a\) und \(T\), um die Geradheitsfaltung der
Source-Argumente positiv zu schreiben.

Damit entstehen nur die folgenden Archetypen.

### A1-R0 — zentraler Strip

Für
\[
0<x<\varepsilon
\]
gilt
\[
\boxed{
\begin{aligned}
(Ay)(x)
={}&
2c_1y(x)
+c_2[y(a-x)+y(a+x)]\\
&+\beta_0[y(T-x)+y(T+x)].
\end{aligned}}
\tag{A1.3}
\]

Dies ist exakt die bereits bekannte innere Row DD.80.

### A1-R1 — breiter Companionstrip

Für
\[
\varepsilon<x<a-\varepsilon
\]
gilt
\[
\boxed{
(Ay)(x)
=
c_1y(x)
-c_1y(T-x)
+c_2y(a+x).
}
\tag{A1.4}
\]

DD.57 ist die bereits verwendete Teilrestriktion dieses Archetyps.

### A1-R2 — linke \(a\)-Schulter

Für
\[
a-\varepsilon<x<a
\]
gilt
\[
\boxed{
\begin{aligned}
(Ay)(x)
={}&
\alpha_Ay(x)
-c_1y(T-x)
+\beta_-y(3a-x)\\
&+\beta_+y(a+x)
+c_2y(a-x).
\end{aligned}}
\tag{A1.5}
\]

Dies ist die positive-Halbachsenform der Row DD.81.

### A1-R3 — rechte \(a\)-Schulter vor der ersten der beiden mittleren Walls

Setze
\[
m_\varepsilon
:=
\min\{a+\varepsilon,\ 2d-\varepsilon\}.
\tag{A1.6}
\]

Für
\[
a<x<m_\varepsilon
\]
gilt
\[
\boxed{
\begin{aligned}
(Ay)(x)
={}&
\alpha_Ay(x)
-c_1y(T-x)
+\beta_-y(3a-x)\\
&+\beta_+y(a+x)
+c_2y(x-a).
\end{aligned}}
\tag{A1.7}
\]

### A1-R4I — Chamber-I-Zwischenzelle

Falls
\[
\varepsilon<\frac{\Delta}{2},
\]
also
\[
a+\varepsilon<2d-\varepsilon,
\]
gilt auf
\[
a+\varepsilon<x<2d-\varepsilon
\]
exakt
\[
\boxed{
(Ay)(x)
=
\alpha_Ay(x)
-c_1y(T-x)
+\beta_-y(3a-x)
+c_2y(x-a).
}
\tag{A1.8}
\]

Hier ist der \(\beta_+\)-Source bereits horizon-tot, während Wort 11 noch geschlossen ist.

### A1-R4II — Chamber-II-Überlappzelle

Falls
\[
\varepsilon>\frac{\Delta}{2},
\]
also
\[
2d-\varepsilon<a+\varepsilon,
\]
gilt auf
\[
2d-\varepsilon<x<a+\varepsilon
\]
exakt
\[
\boxed{
\begin{aligned}
(Ay)(x)
={}&
\alpha_by(x)
-c_1y(T-x)
+\beta_-y(3a-x)\\
&+\beta_+y(a+x)
+c_2y(x-a)
+\beta_by(2b-x).
\end{aligned}}
\tag{A1.9}
\]

Dies ist die einzige räumliche Zelle, in der der neue Wort-11-Kanal bereits aktiv ist,
während der \(\beta_+\)-Source noch nicht horizon-tot ist.

Auf
\[
\varepsilon=\frac{\Delta}{2}
\]
kollabiert A1-R4I/R4II auf einen räumlichen Nullpunkt.

### A1-R5 — breiter B-/C-Strip

Setze
\[
M_\varepsilon
:=
\max\{a+\varepsilon,\ 2d-\varepsilon\}.
\tag{A1.10}
\]

Für
\[
M_\varepsilon<x<T-\varepsilon
\]
gilt
\[
\boxed{
\begin{aligned}
(Ay)(x)
={}&
\alpha_by(x)
-c_1y(T-x)
+\beta_-y(3a-x)\\
&+c_2y(x-a)
+\beta_by(2b-x).
\end{aligned}}
\tag{A1.11}
\]

Die Stage-8-Rows bei \(b\pm s\) und \(C\pm s\) sind Teilrestriktionen dieses
einzigen breiten Archetyps.

### A1-R6 — linker T-Tail

Für
\[
T-\varepsilon<x<T
\]
gilt
\[
\boxed{
\begin{aligned}
(Ay)(x)
={}&
\kappa y(x)
+\beta_0y(T-x)
+\beta_-y(3a-x)\\
&+\beta_Ty(2T-x)
+\beta_+y(x-a)
+\beta_by(2b-x).
\end{aligned}}
\tag{A1.12}
\]

Dies ist exakt die \(T-u\)-2TP-Row mit \(u=T-x\).

### A1-R7 — rechter T-Tail / Horizontschwanz

Für
\[
T<x<T+\varepsilon
\]
gilt
\[
\boxed{
\begin{aligned}
(Ay)(x)
={}&
\kappa y(x)
+\beta_0y(x-T)
+\beta_-y(3a-x)\\
&+\beta_Ty(2T-x)
+\beta_+y(x-a)
+\beta_by(2b-x).
\end{aligned}}
\tag{A1.13}
\]

Dies ist die \(T+u\)-2TP-Row mit \(u=x-T\).

Insbesondere ist die A0-Horizontschwanzzelle
\[
(T+R,T+\varepsilon)
\]
kein neuer A-Rowtyp.

---

## 3. Hubterm — vollständige finite Support-Wall-Liste

Für ungerades, auf dem Annulus nullfortgesetztes \(w\) gilt global
\[
\boxed{
\begin{aligned}
(HE_{\mathcal A}w)(x)
={}&p[w(x-a)-w(x+a)]\\
&+r[w(x-b)-w(x+b)]\\
&+q[w(x-T)-w(x+T)].
\end{aligned}}
\tag{A1.14}
\]

Die Supportbedingung ist jeweils
\[
R<|x\pm\tau|<S,
\qquad
\tau\in\{a,b,T\},
\qquad
S=T+\sigma.
\]

Auf der positiven Halbachse liegen sämtliche inneren Supportwände exakt in
\[
\boxed{
\sigma,\ e+\sigma,\ a+\sigma,\ 
a\pm R,\ b\pm R,\ T\pm R.
}
\tag{A1.15}
\]

Andere Lösungen von \(|x\pm\tau|=S\) liegen negativ oder jenseits \(T_0\).

Damit ist das aktive Hubmuster auf jeder Zelle der gemeinsamen
A0/A1-Partition konstant.

### Neue für A2 wichtige kleine-Tail-Umschaltung

Für
\[
0<x<\sigma
\]
ist zusätzlich der rechte \(T\)-Ast aktiv:
\[
\boxed{
-q\,w(T+x).
}
\tag{A1.16}
\]

Für
\[
\sigma<x<\varepsilon
\]
ist dieser Ast bereits außerhalb des Annulus:
\[
T+x>S.
\tag{A1.17}
\]

Diese Umschaltung beeinflusst nur die \(w\)-rechte Seite, nicht den positiven
y-Pivot aus Stage 12.

---

## 4. Gemeinsame vollständige positive Zellordnung

Für die offene Unterkammer
\[
0<\sigma<R
\]
lautet die gemeinsame Ordnung in Chamber I:
\[
\boxed{
\begin{aligned}
0<&\sigma<\varepsilon<e+\sigma<a-\varepsilon<a-R<a\\
&<a+\sigma<a+R<a+\varepsilon<2d-\varepsilon\\
&<b-R<b<b+R<T-\varepsilon<T-R<T<T+R<T+\varepsilon.
\end{aligned}}
\tag{A1.18}
\]

In Chamber II werden ausschließlich
\[
a+\varepsilon
\quad\text{und}\quad
2d-\varepsilon
\]
vertauscht.

Auf
\[
\sigma=R
\]
kollabiert nur die Zelle
\[
(a+\sigma,a+R)
\]
auf einen Nullpunkt.

Auf
\[
\varepsilon=\Delta/2
\]
kollabiert nur die mittlere A-Wall-Zelle.

Damit besitzt das vollständige positive Rohsystem a.e. endlich viele
räumliche Zellen; in beiden offenen \(\varepsilon\)-Chambers sind es 18.

---

## 5. Exakte finite-cell Operatorform

Seien
\[
I_1,\ldots,I_{18}
\]
die offenen Zellen aus A1.18 beziehungsweise der Chamber-II-Variante.

Setze
\[
\mathscr H_{\rm cell}
:=
\bigoplus_{j=1}^{18}L^2(I_j).
\tag{A1.19}
\]

Geradheit identifiziert die negative Halbachse kanonisch mit derselben
positiven Zellfamilie.

Jeder Term in A1.3–A1.13 ist auf einer Zelle eine der Operationen

- Identität;
- Restriktion;
- Nullfortsetzung;
- Translation \(x\mapsto x+c\);
- Reflexion \(x\mapsto c-x\);

jeweils mit Jacobi-Betrag \(1\).

Daher besitzt die erste augmentierte Gleichung die exakte Form
\[
\boxed{
\mathbb R_{\rm A1}Y
+
\mathbb H_{\rm A1}w
=
0
}
\tag{A1.20}
\]
auf \(\mathscr H_{\rm cell}\), wobei

- \(\mathbb R_{\rm A1}\) eine endliche \(18\times18\)-Matrix aus partiellen
  Translations-/Reflexionsoperatoren ist;
- \(\mathbb H_{\rm A1}\) eine endliche Zellmatrix der drei Hubshifts ist.

A1.20 ist **operatorwertig**: die Matrixeinträge sind Operatoren zwischen
\(L^2\)-Intervallen, keine Skalare.

---

## 6. Einbau von KNF

Die zweite augmentierte Gleichung ist bereits durch
\[
y\in\mathcal K_R
\]
eingebaut.

Auf dem linken \(a\)-Samplebranch gilt
\[
\boxed{
y(a-u)
=
y(a+u)
-\frac rp[y(b-u)-y(b+u)]
-\frac qp[y(T-u)-y(T+u)],
\qquad0<u<R.
}
\tag{A1.21}
\]

Somit ist der Zellvektor \(Y\) in A1.20 nicht frei auf allen 18 Zellen.
Nach Einsetzen von A1.21 ist er ein beschränktes lineares Bild der freien
KNF-Koordinaten
\[
(z,h)\in
\mathcal Z_R^+
\oplus
L^2(\mathcal V_R^{\rm SW1}).
\]

Schreibe dieses Rekonstruktionsbild als
\[
Y=\mathbb J_{\rm KNF}(z,h).
\tag{A1.22}
\]

Dann lautet das vollständige A1-Rohsystem exakt
\[
\boxed{
\mathbb R_{\rm A1}\mathbb J_{\rm KNF}(z,h)
+
\mathbb H_{\rm A1}w
=
0.
}
\tag{A1.23}
\]

Wegen A0 enthält A1.23 **alle** freien \(z\)- und \(h\)-Klassen einschließlich
des Horizontschwanzes.

---

## 7. Äquivalenz mit der ersten augmentierten Gleichung

Die positive Zellzerlegung überdeckt
\[
(0,T_0)
\]
bis auf eine endliche Nullmenge.

A1.3–A1.13 sind auf jeder A-Wall-Zelle die direkte Elf-Wort-Auswertung von \(A\);
A1.14 ist die direkte Drei-Shift-Hubformel.

Daher gilt a.e. exakt
\[
\boxed{
\mathbb R_{\rm A1}\mathbb J_{\rm KNF}(z,h)
+
\mathbb H_{\rm A1}w
=0
}
\]
genau dann, wenn
\[
\boxed{
(I+A)\widehat\Phi_R(z,0,h)
+
HE_{\mathcal A}w
=0.
}
\tag{A1.24}
\]

A1 ist damit ein vollständiger **Rohsystem-Satz**, kein bloßer Teilblock.

---

## 8. Entscheidende Firewall: finite cells \(\neq\) finite Dimension

A0/A1 liefern eine endliche Zahl räumlicher Zustände, aber
\[
L^2(I_j)
\]
ist für jede Zelle positiver Länge unendlichdimensional.

Außerdem koppeln die Row-Archetypen die Zellen durch echte
Translationen und Reflexionen.

Daher folgt aus A1 **nicht**, dass sich das Problem auf eine gewöhnliche
endliche Matrix mit skalaren Einträgen reduziert.

Ein späterer Determinantentest ist nur dann legitim, wenn zusätzlich eine
endliche Orbit-/Fiberreduktion oder eine andere endliche Profilkompression
bewiesen wird.

---

## 9. Nächster Knoten

Nach A1 ist die Coverage- und Rohsystemfrage getrennt von der eigentlichen
Injektivitätsfrage.

Der nächste korrekte Schritt ist
\[
\boxed{
\text{A2: KNF-Schur-Elimination des y-Teils und exakter induzierter Annulusoperator.}
}
\tag{A1.25}
\]

Zu bestimmen ist ein Operator
\[
\mathcal L_{\rm ann}^{\rm SW1}
\]
mit
\[
\boxed{
\ker\mathcal K_{I,A}
\cong
\ker\mathcal L_{\rm ann}^{\rm SW1}
}
\tag{A1.26}
\]
auf dem SW1-Scope.

Erst danach ist die Frage
\[
\ker\Gamma_I=\{0\}
\]
wieder direkt erreichbar.

**Keine Aussage in A1 beweist A2-Injektivität, HT-RED, Closed Range,
Objekt X oder RH.**

---

## 10. Review-/Zertifikatsstatus

Das reproduzierbare Zertifikat
`scripts/certify_sw1_a1_raw_archetypes.py`
wurde auf der exakt committed Fassung mit Python/SymPy 1.14.0 ausgeführt.

Committed Script-Blob:
`eb9d99593f6a34f429f5a723b9362d18db46f171`.

Ergebnis: **PASS**.

Das Zertifikat prüft insbesondere:

- alle elf Vier-Echo-Wörter direkt;
- die exhaustive Rekonstruktion der fünf inneren A-Wände in beiden \(\varepsilon\)-Chambers;
- die neun Row-Archetypen A1-R0 bis A1-R7 einschließlich R4I/R4II;
- die Degeneration \(\varepsilon=\Delta/2\);
- die vollständige positive Hub-Support-Wall-Liste;
- die zusätzliche Umschaltung des rechten T-Hubasts bei \(x=\sigma\).

Damit gilt ausschließlich für das Rohsystem:
\[
\boxed{
\mathrm{SW1\!-\!A1}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

Keine Promotion. Die Injektivität des resultierenden Operators bleibt offen.

