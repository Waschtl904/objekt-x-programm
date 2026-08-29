# P11/R32 — SW1-A5 Two-Sheet Transfer Normal Form Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a4-irrational-rotation-nogo@8ccb35421ecb9a0c0976d85e5975ac8a97e21dd7  
> **Status:** ?[O] — Zwei-Blatt-Normalform hergeleitet; Zertifikat/Re-Review offen; keine Promotion.  
> **Scope:** vollständige affine Normalform aller nichttrivialen A1-Echoabbildungen. Keine Endlichkeits- oder Injektivitätsaussage.

---

## 0. Motivation

A4 zeigt im oberen Chamber eine konkrete irrationale Rotation. Im unteren Chamber
\[
0<\varepsilon<\frac{\Delta}{2}
\]
wird diese Rotation durch Horizon-/Gate-Cuts unterbrochen, aber zusätzliche Echoäste bleiben aktiv.

Um die volle Punktorbitfrage nicht weiter direkt im kontinuierlichen \(x\)-Raum zu verfolgen, reduzieren wir zuerst die gesamte affine Echoalgebra auf höchstens zwei Rotationsblätter über \(\mathbb Z\).

---

## 1. Grundlänge

Setze
\[
\boxed{
L:=a-\Delta.
}
\tag{A5.1}
\]

Mit
\[
\Delta=2b-3a
\]
folgt
\[
\boxed{
L=4a-2b=2e.
}
\tag{A5.2}
\]

Außerdem
\[
\boxed{
a=L+\Delta,
\qquad
T=2L+2\Delta,
\qquad
2b=3L+4\Delta.
}
\tag{A5.3}
\]

Da
\[
\frac{\Delta}{L}\notin\mathbb Q
\]
nach A4, ist die Rotation
\[
t\mapsto t+\Delta\pmod L
\]
irrational.

---

## 2. Vollständige Menge der affinen A1-Quellabbildungen

Aus den Archetypen A1-R0 bis A1-R7 treten als nichttriviale physische Source-Maps ausschließlich auf:

### Translationen
\[
\boxed{
\tau_{+a}(x)=x+a,\quad
\tau_{-a}(x)=x-a,\quad
\tau_{+T}(x)=x+T,\quad
\tau_{-T}(x)=x-T.
}
\tag{A5.4}
\]

### Reflexionen
\[
\boxed{
r_a(x)=a-x,\quad
r_T(x)=T-x,\quad
r_{3a}(x)=3a-x,\quad
r_{4a}(x)=4a-x,\quad
r_{2b}(x)=2b-x.
}
\tag{A5.5}
\]

Ob eine dieser Kanten an einem gegebenen Punkt tatsächlich aktiv ist, wird weiterhin durch die A1-Zell-/Horizon-Cuts entschieden. A5 verändert keine Gatebedingung.

---

## 3. Zwei Rotationsblätter

Fixiere einen beliebigen Referenzpunkt \(x_0\). Definiere modulo \(L\)

\[
\boxed{
P_n
:=
x_0+n\Delta
\pmod L,
}
\tag{A5.6}
\]

\[
\boxed{
Q_n
:=
2b-x_0+n\Delta
\pmod L,
}
\tag{A5.7}
\]
für \(n\in\mathbb Z\).

Dann erhalten alle Translationen die Blattorientierung:

\[
\boxed{
\begin{aligned}
\tau_{+a}:&\ P_n\mapsto P_{n+1},\quad Q_n\mapsto Q_{n+1},\\
\tau_{-a}:&\ P_n\mapsto P_{n-1},\quad Q_n\mapsto Q_{n-1},\\
\tau_{+T}:&\ P_n\mapsto P_{n+2},\quad Q_n\mapsto Q_{n+2},\\
\tau_{-T}:&\ P_n\mapsto P_{n-2},\quad Q_n\mapsto Q_{n-2}.
\end{aligned}}
\tag{A5.8}
\]

Die Reflexionen wechseln das Blatt:

\[
\boxed{
\begin{array}{c|c|c}
\text{Map}
&
P_n\mapsto
&
Q_n\mapsto
\\ \hline
r_a
&
Q_{-n-3}
&
P_{-n-3}
\\
r_T
&
Q_{-n-2}
&
P_{-n-2}
\\
r_{3a}
&
Q_{-n-1}
&
P_{-n-1}
\\
r_{4a}
&
Q_{-n}
&
P_{-n}
\\
r_{2b}
&
Q_{-n}
&
P_{-n}.
\end{array}}
\tag{A5.9}
\]

### Beweisbeispiel

Für \(r_{3a}\):
\[
3a-(x_0+n\Delta)
=
(2b-x_0)+(-n-1)\Delta
\pmod L,
\]
denn
\[
3a-2b=-\Delta.
\]

Für \(r_a\):
\[
a-2b
=
-2L-3\Delta,
\]
also modulo \(L\)
\[
a-(x_0+n\Delta)
=
(2b-x_0)+(-n-3)\Delta.
\]

Die übrigen Zeilen folgen identisch aus A5.3.

---

## 4. Vollständigkeitslemma

Jede endliche Komposition aktiver A1-Echoabbildungen, die bei \(x_0\) startet, liegt modulo \(L\) in

\[
\boxed{
\{P_n:n\in\mathbb Z\}
\cup
\{Q_n:n\in\mathbb Z\}.
}
\tag{A5.10}
\]

### Beweis

Die Aussage gilt bei Start trivial.

A5.8 zeigt, dass jede zulässige Translation ein \(P_n\) wieder auf ein \(P_m\) und ein \(Q_n\) wieder auf ein \(Q_m\) abbildet.

A5.9 zeigt, dass jede zulässige Reflexion zwischen den beiden Blättern wechselt.

Induktion über die Wortlänge liefert A5.10.

Somit erzeugt die gesamte A1-Echoalgebra **keine dritte irrationale Phase**.

---

## 5. Physische Horizon-Lifts sind endlich

Die Zwei-Blatt-Normalform ist zunächst modulo \(L\). Ein physischer Punkt im Horizont kann ein Lift

\[
P_n+kL
\quad\text{oder}\quad
Q_n+kL
\]
sein.

Auf SW1 gilt
\[
T_0=T+\varepsilon
=
2a+\varepsilon.
\]

Ferner
\[
\begin{aligned}
3L-T_0
&=
3(a-\Delta)-(2a+\varepsilon)\\
&=
a-3\Delta-\varepsilon\\
&>
a-4\Delta
>0,
\end{aligned}
\tag{A5.11}
\]
weil
\[
\varepsilon<\Delta
\]
und der feste Stage-6-Slack
\[
a-4\Delta>0
\]
bereits zertifiziert ist.

Daher
\[
\boxed{
T_0<3L.
}
\tag{A5.12}
\]

Ein Restklasse modulo \(L\) besitzt somit in
\[
(0,T_0)
\]
höchstens drei physische Lifts.

Für einen festen Rotationsindex \(n\) existieren deshalb über beiden Blättern zusammen höchstens sechs physische Horizon-Kandidaten.

---

## 6. Diskrete Transferdarstellung

Die vollständige physische Echo-Komponente eines Ausgangspunktes ist damit ein Teilgraph eines endlichen-Lift-Graphen über

\[
\boxed{
\mathbb Z\times\{P,Q\}\times\{0,1,2\},
}
\tag{A5.13}
\]
wobei nicht tatsächlich vorhandene Lifts entfernt werden.

Die Kanten ändern den Rotationsindex nur durch die in A5.8–A5.9 angegebenen ganzzahligen Regeln.

Die komplizierte kontinuierliche Frage wird dadurch auf einen diskreten, endlich-stufigen Cocycle über der irrationalen Basisrotation

\[
t_n=t_0+n\Delta\pmod L
\tag{A5.14}
\]
reduziert.

Gate-/Horizon-Cuts werden zu einer endlichen Familie von Intervallbedingungen an \(t_n\).

---

## 7. Kollision der beiden Blätter

Für spezielle Ausgangspunkte können die beiden Mengen

\[
\{P_n\}
\quad\text{und}\quad
\{Q_n\}
\]
zusammenfallen.

Dies erfordert
\[
2x_0
\equiv
2b+k\Delta
\pmod L
\]
für ein \(k\in\mathbb Z\).

Für festes \(k\) ist dies modulo \(L\) nur eine endliche Punktmenge. Über alle \(k\) entsteht höchstens eine abzählbare Ausnahmemenge.

Für fast jedes \(x_0\) sind die beiden Blätter daher disjunkt.

Falls eine Kollision auftritt, reduziert sie die Zahl physischer Zustände; sie erzeugt keine dritte Phase und verschärft die Orbitkomplexität nicht.

---

## 8. Unterer Chamber: das A4-Loch in der Zwei-Blatt-Sprache

Für
\[
0<\varepsilon<\frac{\Delta}{2}
\]
setze wie in der Fortsetzung von A4

\[
A_\varepsilon:=2d-\varepsilon,
\qquad
B_\varepsilon:=T-\varepsilon,
\]
\[
I_\varepsilon=(A_\varepsilon,B_\varepsilon),
\qquad
|I_\varepsilon|=L.
\]

Der A4-Rotationspfad ist nur bis

\[
\boxed{
C_\varepsilon
:=
T+\varepsilon-\Delta
}
\tag{A5.15}
\]
fortsetzbar.

Denn
\[
B_\varepsilon-C_\varepsilon
=
\Delta-2\varepsilon>0.
\]

Somit entsteht auf jedem Blatt eine offene Hole-Zone der Länge

\[
\boxed{
h_\varepsilon
=
\Delta-2\varepsilon.
}
\tag{A5.16}
\]

Außerhalb dieser Zone realisieren die A4-Pfade weiterhin
\[
t\mapsto t+\Delta\pmod L.
\]

Der volle Graph besitzt jedoch zusätzliche Blattwechselkanten aus A5.9.
Deshalb folgt aus dem Hole allein **noch nicht** die Endlichkeit der vollständigen Komponenten.

A5 isoliert nun exakt die verbleibende Frage:

> Kann der finite-state Zwei-Blatt-Cocycle die beiden Hole-Zonen unbegrenzt umgehen, oder erzeugen die Cuts wiederkehrende Separatoren?

---

## 9. Nächster Knoten

Der nächste aktive Knoten ist

\[
\boxed{
\text{A6-LC: unterer Chamber — Separator-/Bypass-Klassifikation im Zwei-Blatt-Transfergraphen.}
}
\tag{A5.17}
\]

Zu beweisen ist eine der beiden Alternativen:

1. **Finite-component theorem:** jede physische Komponente ist endlich, eventuell ohne uniformen Bound für
   \[
   \varepsilon\uparrow\Delta/2;
   \]

2. **zweiter unendlicher Transfer:** eine konkrete zulässige Bypassfolge erzeugt trotz Hole eine unendliche Komponente.

**Firewall:** A5 ist nur eine exakte affine Normalform. Keine Aussage über
\(\ker\mathcal L_{\rm ann}^{\rm SW1}\), \(\ker\Gamma_I\), HT-RED, Objekt X oder RH.
