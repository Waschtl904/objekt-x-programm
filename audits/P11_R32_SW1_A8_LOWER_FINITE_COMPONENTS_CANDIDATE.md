# P11/R32 — SW1-A8 Lower-Chamber Finite Raw Components Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a7-finite-state-cocycle@901134463449f16ab2a228135026f1ef8449dfbf  
> **Status:** ?[O] — universeller Separator hergeleitet; Zertifikat/Re-Review offen; keine Promotion.  
> **Scope:** vollständiger **roher A1-Punktgraph** im unteren Chamber. Noch keine KNF-\(J_R\)-Zusatzkopplungen und keine Schur-Injektivität.

---

## 0. Unterer Chamber und Separatorphase

Wir arbeiten unter
\[
\boxed{
0<\varepsilon<\frac{\Delta}{2}.
}
\tag{A8.1}
\]

Setze
\[
L=a-\Delta.
\]

Nach A7 wird der rohe A1-Punktgraph durch die irrationale Basissequenz
\[
t_m=t_0+m\Delta\pmod L
\]
gesteuert.

Fixiere einen Index \(n\), an dem
\[
\boxed{
t_n=s\in S_\varepsilon:=(\varepsilon,\Delta-\varepsilon).
}
\tag{A8.2}
\]

Das Intervall ist wegen A8.1 offen und nichtleer:
\[
|S_\varepsilon|
=
\Delta-2\varepsilon>0.
\tag{A8.3}
\]

Wir verschieben den Index und setzen im Folgenden \(n=0\).

---

## 1. Die vier mittleren Kreisphasen

Da
\[
0<s<\Delta
\]
und
\[
4\Delta<L
\]
gilt für die \(P\)-Restklassen in den Schichten \(j=0,1,2,3\) ohne Modulo-Wrap
\[
\boxed{
p_j=s+j\Delta.
}
\tag{A8.4}
\]

Für
\[
\overline Q_j
\]
gilt ebenso
\[
\boxed{
q_j=(4-j)\Delta-s.
}
\tag{A8.5}
\]

Alle \(p_j,q_j\) liegen strikt in \((0,L)\).

---

## 2. Physische Lifts

A7 beweist
\[
T_0<3L.
\]

Ferner
\[
T_0
=
2L+2\Delta+\varepsilon.
\tag{A8.6}
\]

Für eine Restklasse \(r\in(0,L)\) existieren daher immer die Lifts
\[
r,\qquad r+L,
\]
und der dritte Lift
\[
r+2L
\]
existiert genau dann, wenn
\[
\boxed{
r<2\Delta+\varepsilon.
}
\tag{A8.7}
\]

Schreibe
\[
P_j^{(k)}:=p_j+kL,
\qquad
Q_j^{(k)}:=q_j+kL.
\]

Aus
\[
\varepsilon<s<\Delta-\varepsilon
\]
folgt:

\[
\boxed{
P_0^{(2)},P_1^{(2)},Q_2^{(2)},Q_3^{(2)}
\text{ existieren},
}
\tag{A8.8}
\]
während
\[
\boxed{
Q_0^{(2)},Q_1^{(2)},P_2^{(2)},P_3^{(2)}
\text{ nicht existieren}.
}
\tag{A8.9}
\]

Beispielsweise
\[
p_1=\Delta+s
<
2\Delta-\varepsilon
<
2\Delta+\varepsilon,
\]
während
\[
p_2=2\Delta+s
>
2\Delta+\varepsilon.
\]

Analog für die \(Q\)-Lifts.

---

## 3. Universelle Links/Rechts-Stufung

Wir erklären alle Schichten
\[
m\le -1
\]
als **links** und alle
\[
m\ge4
\]
als **rechts**.

In den vier mittleren Schichten setzen wir:

\[
\boxed{
\begin{array}{c|l|l}
j&\mathscr L_j&\mathscr R_j\\ \hline
0&
\{P_0^{(1)},P_0^{(2)},Q_0^{(0)},Q_0^{(1)}\}
&
\{P_0^{(0)}\}
\\[1mm]
1&
\{P_1^{(2)},Q_1^{(0)},Q_1^{(1)}\}
&
\{P_1^{(0)},P_1^{(1)}\}
\\[1mm]
2&
\{Q_2^{(0)},Q_2^{(1)}\}
&
\{P_2^{(0)},P_2^{(1)},Q_2^{(2)}\}
\\[1mm]
3&
\{Q_3^{(0)}\}
&
\{P_3^{(0)},P_3^{(1)},Q_3^{(1)},Q_3^{(2)}\}.
\end{array}}
\tag{A8.10}
\]

A8.8–A8.9 zeigen, dass dies sämtliche physisch möglichen mittleren Zustände exhaustiert.

---

## 4. Die einzigen zehn theoretischen Cross-Kanten

Setzt man die vollständige A7-Indexsprungtabelle in A8.10 ein, bleiben exakt zehn Maps übrig, die **formal** von links nach rechts oder von rechts nach links wechseln könnten.

Sie sind:

### Vom rechten Mittelblock nach links

\[
\begin{array}{c|c}
\text{Source}&\text{Map}\\ \hline
P_0^{(0)}&\tau_{-a}\\
P_0^{(0)}&\tau_{-T}\\
P_1^{(0)}&\tau_{-T}\\
P_1^{(1)}&\tau_{-T}\\
Q_2^{(2)}&r_a
\end{array}
\tag{A8.11}
\]

### Vom linken Mittelblock nach rechts

\[
\begin{array}{c|c}
\text{Source}&\text{Map}\\ \hline
P_1^{(2)}&r_a\\
Q_2^{(0)}&\tau_{-T}\\
Q_2^{(1)}&\tau_{-T}\\
Q_3^{(0)}&\tau_{-a}\\
Q_3^{(0)}&\tau_{-T}.
\end{array}
\tag{A8.12}
\]

Alle anderen A7-Kanten bleiben formal auf derselben Seite.

---

## 5. Alle zehn Cross-Kanten sind inaktiv

Wir benutzen nur die exakten A7-Aktivitätsdomänen
\[
D_{-a}=(a,T_0),
\qquad
D_{-T}=(T,T_0),
\]
und
\[
D_{r_a}
=
(0,\varepsilon)
\cup
(a-\varepsilon,a).
\]

### 5.1 \(P_0^{(0)}\)

\[
P_0^{(0)}=s<\Delta<a.
\]

Daher sind sowohl
\[
\tau_{-a}
\]
als auch
\[
\tau_{-T}
\]
inaktiv.

### 5.2 \(P_1^{(0)}\)

\[
P_1^{(0)}
=
s+\Delta
<
2\Delta
<a<T.
\]

Also ist
\[
\tau_{-T}
\]
inaktiv.

### 5.3 \(P_1^{(1)}\)

Wegen
\[
L+\Delta=a
\]
gilt
\[
P_1^{(1)}
=
s+\Delta+L
=
a+s<T
\]
da \(s<\Delta<a\).

Also ist
\[
\tau_{-T}
\]
inaktiv.

### 5.4 \(Q_2^{(2)}\)

\[
Q_2^{(2)}
=
(2\Delta-s)+2L
=
T-s.
\]

Da
\[
T-s>a,
\]
liegt dieser Punkt oberhalb beider \(r_a\)-Aktivitätsfenster.

Also ist
\[
r_a
\]
inaktiv.

### 5.5 \(P_1^{(2)}\)

\[
P_1^{(2)}
=
s+\Delta+2L
=
T-\Delta+s.
\]

Wegen
\[
T-\Delta+s>a
\]
liegt auch dieser Punkt oberhalb der beiden \(r_a\)-Fenster.

Also ist
\[
r_a
\]
inaktiv.

### 5.6 \(Q_2^{(0)}\)

\[
Q_2^{(0)}
=
2\Delta-s
<
2\Delta
<T.
\]

Also ist
\[
\tau_{-T}
\]
inaktiv.

### 5.7 \(Q_2^{(1)}\)

\[
Q_2^{(1)}
=
2\Delta-s+L
=
a+\Delta-s
<
a+\Delta
<T.
\]

Also ist
\[
\tau_{-T}
\]
inaktiv.

### 5.8 \(Q_3^{(0)}\)

\[
Q_3^{(0)}
=
\Delta-s
<
\Delta<a.
\]

Damit sind sowohl
\[
\tau_{-a}
\]
als auch
\[
\tau_{-T}
\]
inaktiv.

Somit existiert **keine aktive A1-Kante zwischen der linken und rechten Stufung**.

---

## 6. Separatorlemma

A7 beweist, dass jede rohe A1-Kante den lokalen Rotationsindex um höchstens \(3\) ändert.

Daher kann keine Kante direkt von einer Schicht
\[
m\le-1
\]
in eine Schicht
\[
m\ge4
\]
springen.

Jeder Pfad von links nach rechts müsste also in den mittleren Schichten \(0,1,2,3\) mindestens einmal die Stufung A8.10 wechseln.

Abschnitt 5 beweist, dass eine solche aktive Cross-Kante nicht existiert.

Damit:

\[
\boxed{
t_n\in(\varepsilon,\Delta-\varepsilon)
\Longrightarrow
\text{kein roher A1-Pfad verbindet }
m\le n-1
\text{ mit }
m\ge n+4.
}
\tag{A8.13}
\]

Dies ist ein universeller **3-Schichten-Separator**.

Er gilt unabhängig davon, welche der physisch möglichen Lifts in einer konkreten Zusammenhangskomponente bereits erreicht wurden.

---

## 7. Irrationale Wiederkehr der Separatoren

Nach A4/A5 gilt
\[
\frac{\Delta}{L}\notin\mathbb Q.
\]

Daher ist
\[
t_m=t_0+m\Delta\pmod L
\]
für jeden Startpunkt dicht in \(\mathbb T_L\).

Da
\[
S_\varepsilon=(\varepsilon,\Delta-\varepsilon)
\]
offen und nichtleer ist, existieren in beiden Indexrichtungen unendlich viele Separatorindizes.

Zwischen zwei aufeinanderfolgenden Separatoren liegen nur endlich viele Rotationsschichten.

Da pro Schicht höchstens sechs physische Liftzustände existieren, ist jede rohe A1-Zusammenhangskomponente endlich.

Also:

\[
\boxed{
0<\varepsilon<\Delta/2
\Longrightarrow
\text{jede Zusammenhangskomponente des vollständigen rohen A1-Punktgraphen ist endlich.}
}
\tag{A8.14}
\]

Für jedes feste \(\varepsilon\) sind die Separator-Hitting-Gaps wegen Minimalität und Kompaktheit sogar uniform beschränkt.

Es wird keine uniforme Bound für
\[
\varepsilon\uparrow\Delta/2
\]
behauptet.

---

## 8. Was A8 ausdrücklich noch nicht schließt

A8.14 betrifft den **rohen A1-Graphen auf den physischen \(y\)-Punkten**.

Der freie KNF-Gramoperator
\[
\mathfrak G_R
=
J_R^*(I+A)J_R
\]
enthält zusätzlich die Rekonstruktionsabbildung
\[
J_R.
\]

Insbesondere ersetzt KNF den linken \(a-u\)-Branch durch eine Linearkombination der fünf freien Samplebranches.

Beim Übergang von \(I+A\) zu
\[
J_R^*(I+A)J_R
\]
können dadurch zusätzliche freie Koordinatenkanten entstehen, die rohe A1-Komponenten miteinander verbinden.

Deshalb folgt aus A8.14 noch **nicht**
\[
\text{finite point components of }\mathfrak G_R.
\]

Der nächste Knoten ist:

\[
\boxed{
\text{A9-KNF: Separatorstabilität unter der KNF-Rekonstruktion }J_R.
}
\tag{A8.15}
\]

---

## 9. Firewall

A8 beweist keine Injektivität von
\[
\mathcal L_{\rm ann}^{\rm SW1},
\]
keinen trivialen Schur-Kern, kein HT-RED, keine Closed-Range-/bounded-below-Aussage, kein Objekt X und keine RH-Folgerung.

Es beweist ausschließlich die Endlichkeit der **rohen** A1-Punktkomponenten im unteren \(\varepsilon\)-Chamber.
