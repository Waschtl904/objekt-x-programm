# P11/R32 — SW1-A8 Lower-Chamber Finite Raw Components Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a7-finite-state-cocycle@901134463449f16ab2a228135026f1ef8449dfbf  
> **Status:** `AI-GREEN candidate + independent GREEN (certificate)` — midpoint-korrigierter wiederkehrender Separator und Endlichkeit der rohen A1-Komponenten geprüft; **keine Promotion**.  
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

A8.8–A8.9 zeigen, dass dies sämtliche möglichen mittleren State-Labels exhaustiert. Auf dem regulären Separatorbereich (S_\varepsilon^{\rm reg}) sind diese Labels nach Abschnitt 10A zusätzlich physisch paarweise kompatibel mit der Links/Rechts-Stufung; die einzige Cross-Sheet-Degeneration liegt bei dem ausdrücklich entfernten Punkt (s=\Delta/2).

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
t_n\in S_\varepsilon^{\rm reg}
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

Da beide Komponenten von
\[
S_\varepsilon^{\rm reg}
=
(\varepsilon,\Delta/2)
\cup
(\Delta/2,\Delta-\varepsilon)
\]
offen und nichtleer sind, existieren nach Minimalität in beiden Indexrichtungen unendlich viele reguläre Separatorindizes.

Die Komponent-Endlichkeit folgt direkt und ohne versteckte Uniformitätsannahme. Fixiere einen Knoten mit Rotationsindex \(m_0\). Wegen der beidseitig unendlichen Separatorwiederkehr wähle Separatorindizes \(n_-\) und \(n_+\) mit
\[
n_-\le m_0-4,
\qquad
n_+\ge m_0+1.
\]
Dann liegt \(m_0\ge n_-+4\), also kann seine Zusammenhangskomponente wegen A8.13 keinen Index \(m\le n_--1\) enthalten. Ebenso liegt \(m_0\le n_+-1\), also kann dieselbe Komponente keinen Index \(m\ge n_++4\) enthalten.

Damit ist ihr Indexsupport in dem endlichen Intervall
\[
[n_-,\,n_++3]\cap\mathbb Z
\]
enthalten. Da pro Schicht höchstens sechs physische Liftzustände existieren, ist jede rohe A1-Zusammenhangskomponente endlich.

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


---

## 10. Review-/Zertifikatsstatus

Der A8-Kandidat wurde adversarial gegen die vollständige A7-Indexsprungtabelle geprüft.

Das committed Zertifikat

`scripts/certify_sw1_a8_lower_finite_components.py`

wurde auf dem exakten Git-Head

`197770e5b28e7b829fc5be695ea44cbe968483d5`

in der committed Fassung mit Script-Blob

`f0369406e44081c3df04164950d9a463850bd208`

unter Python/SymPy 1.14.0 ausgeführt.

Ergebnis: **PASS**.

Das Zertifikat prüft im endlichen/algebraischen Scope:

- die exakten SW1-Konstantenrelationen einschließlich \(4\Delta<L\);
- die vollständige Existenz/Nichtexistenz der dritten Lifts in den vier mittleren Schichten;
- die exhaustive Aufteilung aller 20 mittleren State-Labels in die Links-/Rechts-Stufung A8.10; die physische Eindeutigkeit dieser Stufung wird durch den Supplemental Midpoint-Certificate auf (S_\varepsilon^{\rm reg}) abgesichert;
- alle \(20\cdot9=180\) Source-Map-Fälle der A7-Kantentabelle;
- dass exakt die zehn Cross-Kandidaten A8.11–A8.12 verbleiben;
- dass alle zehn auf dem gesamten offenen Separatorparameterbereich strikt gate-inaktiv sind;
- die maximale A7-Indexreichweite \(|j|\le3\) sowie die Invers-/Reflexionssymmetrie der rohen Kanten;
- die exakte Reduktion der Irrationalitätsfrage \(\Delta/L\notin\mathbb Q\) auf ein nichtsinguläres ganzzahliges \(2\times2\)-System; der letzte Schritt benutzt eindeutige Primfaktorzerlegung.

Die Wiederkehr jedes offenen Separatorintervalls und die daraus folgende beidseitige Existenz von Separatorindizes benutzen separat den klassischen Minimalitätssatz für irrationale Kreisrotationen. Abschnitt 7 macht daraus explizit einen endlichen Indexsupport jeder Komponente; hierfür wird keine Uniformität in \(\varepsilon\uparrow\Delta/2\) benötigt.

Damit gilt ausschließlich im expliziten Scope des vollständigen **rohen A1-Punktgraphen** im unteren Chamber:

\[
\boxed{
\mathrm{SW1\!-\!A8}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

Keine Promotion. Keine Aussage über KNF-\(J_R\)-Zusatzkanten, \(\mathfrak G_R\)-Punktkomponenten, Schur-Injektivität, HT-RED, Objekt X oder RH.


---

## 10A. Supplemental audit — Midpoint-Degeneration und Scope-Korrektur

Ein nachträglicher adversarialer Check der **physischen** Identifikation der P-/\(\overline Q\)-Labels fand genau eine zuvor nicht explizit behandelte Degeneration.

Für

\[
P_j^{(k)}=s+j\Delta+kL,
\qquad
Q_m^{(\ell)}=(4-m)\Delta-s+\ell L
\]

würde eine Cross-Sheet-Kollision die Gleichung

\[
2s=(4-m-j)\Delta+(\ell-k)L
\]

erzwingen.

Das Supplemental Certificate enumeriert exhaustiv alle in A8.8–A8.10 tatsächlich vorkommenden P-/Q-Liftpaare. Mit den exakten Schranken

\[
\boxed{4\Delta<L<5\Delta}
\]

bleibt im Bereich \(0<s<\Delta\) genau eine mögliche Kollisionsphase:

\[
\boxed{s=\Delta/2.}
\]

Dort treten genau zehn Cross-Sheet-State-Pair-Koinzidenzen **innerhalb der 20 A8-Mittelblocklabels** auf. Außerhalb dieses Einzelpunkts existiert innerhalb dieses endlichen Mittelblockledgers keine solche Doppelbelegung. Diese Aussage ist ausdrücklich **keine** Behauptung, dass sich die beiden bi-unendlichen Rotationsblätter global nur am Midpoint schneiden könnten. Der globale Kollisionsfall wird separat in Abschnitt 10B behandelt.

Deshalb ist die punktweise Separatoraussage A8.13 ausschließlich auf

\[
S_\varepsilon^{\rm reg}
=
(\varepsilon,\Delta/2)
\cup
(\Delta/2,\Delta-\varepsilon)
\]

zu lesen.

Die lokale Midpoint-Korrektur allein genügt noch nicht zur Behandlung möglicher **globaler** P-/\(\overline Q\)-Sheet-Kollisionen. Die Endlichkeitsaussage A8.14 bleibt dennoch gültig, aber ihre vollständige physische Rechtfertigung verwendet zusätzlich das Quotientenlemma aus Abschnitt 10B.

Supplemental certificate:

scripts/certify_sw1_a8_midpoint_degeneracy_fix.py

Commit:

2b65a54346f6c29c8617b666ffe0887b2a630d81

Committed Script-Blob:

b2efc57b005b950ab02b08ba49dfb3018baccd8e

Der tatsächlich ausgeführte Dateiinhalt ergab exakt denselben Git-Blob-SHA.

Ergebnis:

SW1-A8 MIDPOINT DEGENERACY FIX CERTIFICATE: PASS

Damit bleibt die zulässige A8-Buchung

\[
\boxed{
\mathrm{SW1\!-\!A8}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

mit der korrigierten punktweisen Separator-Domäne \(S_\varepsilon^{\rm reg}\).

**Firewall:** Dies ist eine Scope-Korrektur des rohen A8-Separatorlemmas, keine KNF-/A9-Aussage. Keine Promotion und keine Änderung der globalen Schur-/HT-/Objekt-X-/RH-Firewall.


---

## 10B. Globaler Sheet-Kollisionsquotient — vollständige physische Reparatur

A5.7 weist ausdrücklich darauf hin, dass für spezielle Ausgangspunkte die beiden bi-unendlichen Rotationsblätter zusammenfallen können. Daher ist eine bloße Prüfung der vier A8-Mittelschichten **nicht** hinreichend, um globale physische Injektivität der formalen P-/\(\overline Q\)-Labels zu behaupten.

Die korrekte Behandlung ist ein Quotientenargument.

### 10B.1 Formale Cover-Aussage

Die A7/A8-Indexrechnung wird zunächst auf dem formalen Zwei-Blatt-Cover

\[
\mathbb Z\times\{P,\overline Q\}\times\{0,1,2\}
\]

gelesen.

Auf diesem Cover sind die Labels definitionsgemäß verschieden. Der ursprüngliche A8-Cross-Edge-Check und die maximale Reichweite \(3\) liefern deshalb den formalen Separator ohne irgendeine physische Quotientenannahme.

Insbesondere bleibt die formale Endlichkeit der Cover-Komponenten für

\[
0<\varepsilon<\Delta/2
\]

durch die irrationale Wiederkehr des offenen Separatorfensters bestehen.

### 10B.2 Struktur einer globalen Sheet-Kollision

Falls sich die beiden physischen Rotationsblätter schneiden, gilt für geeignete ganze Indizes

\[
P_n=\overline Q_m.
\]

Wegen

\[
\Delta/L\notin\mathbb Q
\]

ist die Summe \(K=n+m\) eindeutig: zwei verschiedene Werte \(K_1,K_2\) würden

\[
(K_1-K_2)\Delta\equiv0\pmod L
\]

und damit Rationalität von \(\Delta/L\) erzwingen.

Somit besitzt jede globale Kollision die Form

\[
\boxed{
P_n=\overline Q_{K-n}
}
\]

für alle entsprechenden Orbitlabels.

Definiere die Involution

\[
\boxed{
J_K(P_n)=\overline Q_{K-n},
\qquad
J_K(\overline Q_n)=P_{K-n}.
}
\]

Für die spätere A9-Parität gilt allgemeiner

\[
J_{K,\delta}(P_{n,\eta})
=
\overline Q_{K-n,\eta+\delta},
\qquad
\delta\in\mathbb Z/2.
\]

### 10B.3 Graphautomorphismus

Die A7-Indexsprungtabelle besitzt für jeden affinen Maptyp die Symmetrie

\[
j_{\overline Q}=-j_P.
\]

Daher kommutiert \(J_K\) exakt mit allen neun A7-Übergängen.

Die Gate-/Horizon-Entscheidung hängt ausschließlich vom **physischen Punkt \(x\)** ab. Zwei durch \(J_K\) identifizierte Labels besitzen deshalb dieselbe Aktivität.

Somit ist \(J_K\) ein Automorphismus des formalen aktiven Covergraphen.

### 10B.4 Endlichkeit überlebt den Quotienten

Sei \(C\) eine formale Zusammenhangskomponente. Ihre Sättigung unter der physischen Identifikation ist

\[
\boxed{
C\cup J_K(C).
}
\]

Da \(J_K^2=I\), werden also höchstens **zwei** formale Komponenten miteinander verklebt.

A8 beweist die Endlichkeit jeder formalen Cover-Komponente. Folglich ist auch jede physische Quotientenkomponente endlich.

Damit ist A8.14 vollständig physisch gerechtfertigt, auch auf den abzählbaren globalen Sheet-Kollisionsstrata.

### 10B.5 Zertifikat

Zertifikat:

scripts/certify_sw1_sheet_collision_quotient.py

Commit der ersten A8-Fassung:

9d537c2a820473161cc79496bb171c3ed8be7b00

Committed Script-Blob:

a1e62d885788c9b3eb696fd7709b81193e345410

Exakte committed Ausführung:

SW1 GLOBAL SHEET-COLLISION QUOTIENT CERTIFICATE: PASS

Das Zertifikat prüft die Involutions- und Kommutationsidentitäten für sämtliche neun A7-Typen sowie bereits für die neun späteren A9-KNF-Typen und beide Paritätsoffsets \(\delta=0,1\).

Der analytische Input \(\Delta/L\notin\mathbb Q\) bleibt separat der bereits auditierten A4/A5-Irrationalitätsstufe entnommen.

### 10B.6 Korrigierte Aussagehierarchie

Damit ist zu unterscheiden:

1. **formaler A8-Coverseparator:** universell im A8-Scope;
2. **direkte physische Links/Rechts-Partition:** kann bei Sheet-Kollisionen als Labelpartition versagen;
3. **physische Komponentenendlichkeit A8.14:** bleibt durch das Quotientenlemma vollständig gültig.

Die Midpoint-Korrektur 10A ist weiterhin eine echte lokale Label-Degeneration und bleibt dokumentiert; sie ist jedoch nicht mehr die alleinige Rechtfertigung der physischen Endlichkeit.

Keine Promotion. Keine KNF-Gram-, Schur-, HT-RED-, Objekt-X- oder RH-Folgerung.
