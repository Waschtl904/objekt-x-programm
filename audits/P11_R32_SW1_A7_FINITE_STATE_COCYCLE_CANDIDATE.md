# P11/R32 — SW1-A7 Lower-Chamber Finite-State Cocycle Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a6-rotation-hole@0b090ebb0c59c79529fb6d4e626f33876abbfcab  
> **Status:** `AI-GREEN candidate + independent GREEN (certificate)` — finite-state Cocycle vollständig zertifiziert; **keine Promotion**.  
> **Scope:** voller roher A1-Punktgraph im unteren \(\varepsilon\)-Chamber. Keine Komponent-Endlichkeit und keine Schur-Injektivität.

---

## 0. Ziel

Nach A5 liegt die gesamte affine Echoalgebra auf höchstens zwei irrationalen Blättern modulo
\[
L=a-\Delta.
\]

A6 zeigt, dass der spezielle A4-Rotationssubgraph im unteren Chamber
\[
0<\varepsilon<\frac{\Delta}{2}
\]
durch ein offenes Hole in endliche Rotationssegmente zerfällt.

A7 beschreibt nun **alle** zusätzlichen A1-Bypasskanten als finite-state Cocycle über derselben irrationalen Basisrotation.

---

## 1. Exakte Aktivitätsdomänen der neun affinen Maps

Im unteren Chamber gilt die A1-Reihenfolge
\[
0<\varepsilon<a-\varepsilon<a<a+\varepsilon<2d-\varepsilon<T-\varepsilon<T<T+\varepsilon.
\]

Aus A1-R0 bis A1-R7 folgt, nach Vereinigung aller Zellen mit demselben Source-Map, die folgende vollständige Liste.

### Translation \(+a\)

\[
\boxed{
\tau_{+a}(x)=x+a
\quad\text{ist aktiv genau auf}\quad
D_{+a}=(0,a+\varepsilon).
}
\tag{A7.1}
\]

### Translation \(-a\)

\[
\boxed{
\tau_{-a}(x)=x-a
\quad\text{ist aktiv genau auf}\quad
D_{-a}=(a,T_0).
}
\tag{A7.2}
\]

### Translation \(+T\)

\[
\boxed{
\tau_{+T}(x)=x+T
\quad\text{ist aktiv genau auf}\quad
D_{+T}=(0,\varepsilon).
}
\tag{A7.3}
\]

### Translation \(-T\)

\[
\boxed{
\tau_{-T}(x)=x-T
\quad\text{ist aktiv genau auf}\quad
D_{-T}=(T,T_0).
}
\tag{A7.4}
\]

### Reflexion \(r_a\)

\[
\boxed{
r_a(x)=a-x
}
\]
ist aktiv genau auf
\[
\boxed{
D_{r_a}
=
(0,\varepsilon)
\cup
(a-\varepsilon,a).
}
\tag{A7.5}
\]

### Reflexion \(r_T\)

\[
\boxed{
r_T(x)=T-x
\quad\text{ist aktiv genau auf}\quad
D_{r_T}=(0,T).
}
\tag{A7.6}
\]

### Reflexion \(r_{3a}\)

\[
\boxed{
r_{3a}(x)=3a-x
\quad\text{ist aktiv genau auf}\quad
D_{r_{3a}}=(a-\varepsilon,T_0).
}
\tag{A7.7}
\]

### Reflexion \(r_{4a}\)

\[
\boxed{
r_{4a}(x)=4a-x
\quad\text{ist aktiv genau auf}\quad
D_{r_{4a}}=(T-\varepsilon,T_0).
}
\tag{A7.8}
\]

### Reflexion \(r_{2b}\)

\[
\boxed{
r_{2b}(x)=2b-x
\quad\text{ist aktiv genau auf}\quad
D_{r_{2b}}=(2d-\varepsilon,T_0).
}
\tag{A7.9}
\]

Diese neun offenen Domänen enthalten den vollständigen rohen A1-Punktgraphen; Selbstloops wurden ausgelassen.

---

## 2. Lokaler Zwei-Blatt-Index

Wie in A5 definieren wir
\[
P_n=x_0+n\Delta\pmod L.
\]

Für den zweiten Ast ist die für lokale Indexsprünge bequemere Konvention
\[
\boxed{
\overline Q_n
:=
Q_{-n}
=
2b-x_0-n\Delta
\pmod L.
}
\tag{A7.10}
\]

Damit werden alle Echoindexänderungen **lokal**.

### Blatt-erhaltende Translationen

\[
\boxed{
\begin{array}{c|cc}
 &P_n&\overline Q_n\\ \hline
\tau_{+a}&P_{n+1}&\overline Q_{n-1}\\
\tau_{-a}&P_{n-1}&\overline Q_{n+1}\\
\tau_{+T}&P_{n+2}&\overline Q_{n-2}\\
\tau_{-T}&P_{n-2}&\overline Q_{n+2}
\end{array}}
\tag{A7.11}
\]

### Blattwechselnde Reflexionen

\[
\boxed{
\begin{array}{c|cc}
 &P_n&\overline Q_n\\ \hline
r_a&P_n\mapsto\overline Q_{n+3}
&\overline Q_n\mapsto P_{n-3}\\
r_T&P_n\mapsto\overline Q_{n+2}
&\overline Q_n\mapsto P_{n-2}\\
r_{3a}&P_n\mapsto\overline Q_{n+1}
&\overline Q_n\mapsto P_{n-1}\\
r_{4a}&P_n\mapsto\overline Q_n
&\overline Q_n\mapsto P_n\\
r_{2b}&P_n\mapsto\overline Q_n
&\overline Q_n\mapsto P_n.
\end{array}}
\tag{A7.12}
\]

Insbesondere ändert jede rohe A1-Kante den lokalen Index um höchstens
\[
\boxed{3.}
\tag{A7.13}
\]

---

## 3. Kanonische Kreisphase

Setze
\[
\mathbb T_L=\mathbb R/L\mathbb Z
\]
und
\[
\boxed{
t_n
=
t_0+n\Delta\pmod L,
\qquad
0\le t_n<L.
}
\tag{A7.14}
\]

Die \(P\)-Restklasse am Index \(n\) ist \(t_n\).

Wegen
\[
2b\equiv4\Delta\pmod L
\]
ist die \(\overline Q\)-Restklasse am selben lokalen Index
\[
\boxed{
q_n
=
4\Delta-t_n
\pmod L.
}
\tag{A7.15}
\]

Damit wird der gesamte Zwei-Blatt-Graph durch **eine einzige** irrationale Basissequenz \(t_n\) gesteuert.

---

## 4. Höchstens sechs Liftzustände pro Index

A5 beweist
\[
T_0<3L.
\]

Daher besitzt jede Restklasse \(t\in[0,L)\) im positiven Horizont
\[
(0,T_0)
\]
höchstens die drei Lifts
\[
t,\quad t+L,\quad t+2L,
\]
sofern der jeweilige Wert kleiner als \(T_0\) ist.

Dasselbe gilt für \(q_n\).

Definiere deshalb die feste Zustandsmenge
\[
\boxed{
\mathscr S
=
\{P_0,P_1,P_2,\overline Q_0,\overline Q_1,\overline Q_2\},
}
\tag{A7.16}
\]
wobei der Unterindex hier den Lift \(k=0,1,2\) und **nicht** den Rotationsindex bezeichnet.

Am Rotationsindex \(n\) ist der physische Wert eines Zustands
\[
P_k:
\quad
x=t_n+kL,
\tag{A7.17}
\]
beziehungsweise
\[
\overline Q_k:
\quad
x=q_n+kL,
\tag{A7.18}
\]
falls
\[
0<x<T_0.
\]

Nicht vorhandene Lifts werden einfach gelöscht.

---

## 5. Finite-state Cocycle

Für jedes
\[
t\in\mathbb T_L
\]
und jedes untere-Chamber-\(\varepsilon\) definiert die Domänentabelle A7.1–A7.9 eine endliche Menge zulässiger Kanten zwischen

\[
(n,s)
\quad\text{und}\quad
(n+j,s'),
\]
mit
\[
s,s'\in\mathscr S,
\qquad
|j|\le3.
\]

Schreibe diese Kantenrelation als
\[
\boxed{
\mathfrak E_\varepsilon(t)
\subset
\mathscr S\times\{-3,-2,-1,0,1,2,3\}\times\mathscr S.
}
\tag{A7.19}
\]

Dann ist der vollständige rohe A1-Punktgraph eines Ausgangspunktes ein Teilgraph des skew-product Graphen

\[
\boxed{
(n,s)
\longmapsto
(n+j,s'),
\qquad
(s,j,s')\in
\mathfrak E_\varepsilon(t_n),
}
\tag{A7.20}
\]
über der irrationalen Rotation
\[
t_{n+1}=t_n+\Delta\pmod L.
\]

Alle kontinuierlichen Gate-/Horizonentscheidungen sind jetzt in einer **endlichen** Intervallentscheidung für die sechs möglichen physischen Werte A7.17–A7.18 enthalten.

---

## 6. Warum eine reine Phasenbarriere zu stark wäre

Ein fixer Kreiswert \(t_n\) bestimmt zwar alle sechs **möglichen** Liftwerte, aber nicht jeder mögliche Lift muss in der konkreten Zusammenhangskomponente erreichbar sein.

Darum genügt eine Bedingung
\[
t_n\in U
\]
allein im Allgemeinen nicht, um einen Separator im vollen Graphen zu beweisen.

Die richtige Zustandsgröße ist die erreichbare Liftmenge
\[
\boxed{
\mathcal A_n
\subseteq\mathscr S.
}
\tag{A7.21}
\]

Wegen
\[
|\mathscr S|=6
\]
existieren nur
\[
\boxed{
2^6=64
}
\tag{A7.22}
\]
mögliche Liftmengen.

Da die Kanten Reichweite höchstens \(3\) besitzen, kann ein Separator-/Frontieralgorithmus mit einem endlichen Fenster aus höchstens drei benachbarten Schichten formuliert werden.

Ein naiver Frontierzustand
\[
(\mathcal A_{n-2},\mathcal A_{n-1},\mathcal A_n)
\]
besitzt höchstens
\[
\boxed{
64^3=262144
}
\tag{A7.23}
\]
formale Zustände, bevor offensichtliche Unmöglichkeitsbedingungen entfernt werden.

Das ist endlich und maschinenklassifizierbar.

---

## 7. Exakte Reduktion der unteren-Chamber-Frage

Die vollständige rohe Punktorbitfrage lautet nun:

> Besitzt der finite-state Cocycle A7.20 einen bi-unendlichen erreichbaren Pfad, oder erzeugt die irrationale Basissequenz wiederkehrende leere Frontierzustände?

Damit sind die beiden möglichen Resultate exakt:

### Finite-component outcome
Falls jede erreichbare Frontierbahn in endlicher Zeit einen Separatorzustand trifft, sind alle rohen A1-Punktkomponenten endlich.

### Infinite-bypass outcome
Falls ein zulässiger wiederkehrender Zustandszyklus mit nichtzero Nettoindex existiert und entlang der irrationalen Basis unendlich fortsetzbar ist, entsteht ein echter zweiter unendlicher Transfermechanismus.

---

## 8. Beziehung zu A6

Der A6-Rotationssubgraph entspricht nur einem kleinen Teil der Kantenrelation \(\mathfrak E_\varepsilon(t)\).

Sein Hole
\[
|H_\varepsilon|=\Delta-2\varepsilon
\]
erzeugt dort endliche Segmente.

A7 zeigt exakt, was ein Bypass leisten müsste:
Er muss an einem A6-Hole-Hit über einen anderen Liftzustand bzw. das andere Blatt springen und später wieder in eine fortsetzbare Rotationsschicht eintreten.

Dies ist jetzt eine endliche Zustandsfrage.

---

## 9. Nächster Knoten

Der nächste aktive Knoten ist

\[
\boxed{
\text{A8-LC: exakte Frontier-/Separator-Suche im 6-State-, Range-3-Cocycle.}
}
\tag{A7.24}
\]

Vorgehen:

1. alle A7-Domänengrenzen in Kreisphasen \(t\) zurückziehen;
2. dadurch \(\mathbb T_L\) in endlich viele Transferzellen zerlegen;
3. die exakte Kantenrelation \(\mathfrak E_\varepsilon(t)\) je Zelle erzeugen;
4. erreichbare Frontierzustände reduzieren;
5. nach einem wiederkehrenden Separatorwort oder einem echten unendlichen Bypass suchen.

**Firewall:** A7 ist eine endliche Transferreduktion. Sie beweist noch nicht die Endlichkeit der vollen Komponenten, keine Injektivität von \(\mathcal L_{\rm ann}^{\rm SW1}\), kein HT-RED, kein Objekt X und keine RH-Folgerung.

---

## 10. Review-/Zertifikatsstatus

Das committed Zertifikat
`scripts/certify_sw1_a7_finite_state_cocycle.py`
wurde mit Python/SymPy 1.14.0 auf der exakt committed Fassung ausgeführt.

Script-Blob:
`9b347e90df55060de6367b92baa13873ce965f17`.

Ergebnis: **PASS**.

Zertifiziert werden:

- die neun unteren-Chamber-Aktivitätsdomänen;
- die vollständige lokale P/Qbar-Indexsprungtabelle;
- maximale Kantenreichweite \(3\);
- Steuerung beider Blätter durch eine einzige Kreisphase;
- \(T_0<3L\) und damit höchstens sechs Liftzustände pro Index;
- der formale Frontierzustandsraum \(64^3\).

Damit gilt:
\[
\boxed{
\mathrm{SW1\!-\!A7}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

Keine Promotion. A8-LC muss erst die tatsächlich erreichbaren Frontierzustände klassifizieren.

