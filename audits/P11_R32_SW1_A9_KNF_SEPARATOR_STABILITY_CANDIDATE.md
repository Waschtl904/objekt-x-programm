# P11/R32 — SW1-A9 KNF Separator Stability Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a8-lower-finite-components@d99d4ef780dc47876ff0445e2bcd403f45679610  
> **Status:** ?[O] — KNF-Zusatzkanten strukturell begonnen; Separatorstabilität noch nicht entschieden; keine Promotion.  
> **Scope:** zusätzlicher freier Koordinatengraph von \(\mathfrak G_R=J_R^*(I+A)J_R\) im unteren Chamber. A8 bleibt nur Input für den rohen A1-Graphen.

---

## 0. Ziel und Firewall

A8 liefert im unteren Chamber
\[
0<\varepsilon<\Delta/2
\]
endliche Zusammenhangskomponenten des vollständigen **rohen A1-Punktgraphen**.

Das genügt nicht für
\[
\mathfrak G_R=J_R^*(I+A)J_R,
\]
weil die KNF-Rekonstruktion
\[
J_R=\Psi_R^{-1}
\]
den linken \(a\)-Samplebranch durch fünf freie Samplebranches ersetzt.

A9 fragt ausschließlich:
\[
\boxed{
\text{Erhalten die durch }J_R\text{ erzeugten freien Koordinatenkanten die A8-Separatoren?}
}
\]

Noch keine Aussage über Schur-Injektivität, HT-RED, Objekt X oder RH.

---

## 1. Exakte KNF-Rekonstruktion

Für \(0<u<R\) setze
\[
A_+(u)=a+u,\qquad
B_-(u)=b-u,\qquad
B_+(u)=b+u,
\]
\[
T_-(u)=T-u,\qquad
T_+(u)=T+u.
\]

Nach SW1-KNF gilt
\[
\boxed{
y(a-u)
=
y(A_+(u))
-\frac rp\,y(B_-(u))
+\frac rp\,y(B_+(u))
-\frac qp\,y(T_-(u))
+\frac qp\,y(T_+(u)).
}
\tag{A9.1}
\]

Alle fünf Koeffizienten
\[
1,\quad -r/p,\quad r/p,\quad -q/p,\quad q/p
\]
sind ungleich Null.

---

## 2. Identitäts-Gram: 5-Knoten-Rang-eins-Beitrag

Schreibe
\[
H(u)=
\bigl(
h_A(u),h_{B,-}(u),h_{B,+}(u),h_{T,-}(u),h_{T,+}(u)
\bigr)
\]
und
\[
c=
\left(
1,-\frac rp,\frac rp,-\frac qp,\frac qp
\right).
\]

Der rekonstruierte linke \(a\)-Branch ist
\[
x(u)=c\cdot H(u).
\]

Daher enthält
\[
J_R^*J_R
\]
auf diesem Fünferblock den positiven Rang-eins-Beitrag
\[
\boxed{c^*c.}
\tag{A9.2}
\]

Vor Zusammenfassung mit dem Anteil \(J_R^*AJ_R\) besitzt A9.2 zwischen jedem Paar der fünf freien Samplebranches einen nichtverschwindenden off-diagonalen Term.

**Cancellation-Firewall:** Daraus wird noch nicht behauptet, dass jeder dieser Einträge im vollständig aufsummierten Operator \(\mathfrak G_R\) ungleich Null bleibt. Gleiche affine Kanäle aus \(J_R^*AJ_R\) müssen vor einem endgültigen Graphurteil koeffizientenweise zusammengeführt werden.

---

## 3. Affine Kanten des KNF-Fünferblocks

Die zehn ungeordneten Paare aus A9.2 realisieren:
\[
\boxed{
\begin{array}{c|c}
\text{Paar}&\text{affine Relation}\\ \hline
A_+\leftrightarrow B_-&x\mapsto a+b-x\\
A_+\leftrightarrow B_+&x\mapsto x+d\\
A_+\leftrightarrow T_-&x\mapsto 3a-x\\
A_+\leftrightarrow T_+&x\mapsto x+a\\
B_-\leftrightarrow B_+&x\mapsto 2b-x\\
B_-\leftrightarrow T_-&x\mapsto x+e\\
B_-\leftrightarrow T_+&x\mapsto T+b-x\\
B_+\leftrightarrow T_-&x\mapsto T+b-x\\
B_+\leftrightarrow T_+&x\mapsto x+e\\
T_-\leftrightarrow T_+&x\mapsto 4a-x.
\end{array}}
\tag{A9.3}
\]

Gegenüber der A7-Rohmapliste sind bereits vorhanden:
\[
r_{3a},\qquad \tau_{\pm a},\qquad r_{2b},\qquad r_{4a}.
\]

Genuin neu durch die KNF-Rekonstruktion sind zunächst
\[
\boxed{
\tau_{\pm d},
\qquad
\tau_{\pm e},
\qquad
r_{a+b},
\qquad
r_{T+b}.
}
\tag{A9.4}
\]

---

## 4. Keine neue irrationale Phase

Mit
\[
L=a-\Delta,
\qquad
\Delta=2d-a
\]
folgt
\[
d=\frac{a+\Delta}{2},
\qquad
e=a-d.
\]

Da
\[
a=L+\Delta,
\]
gilt exakt
\[
\boxed{
e=\frac L2,
\qquad
d=\frac L2+\Delta.
}
\tag{A9.5}
\]

Damit erzeugen die neuen Translationen A9.4 **keine zweite unabhängige irrationale Rotation**. Sie erweitern die A7-Basis nur um eine endliche Halbperioden-Parität.

---

## 5. Paritätserweiterter Cocycle

Definiere
\[
\eta\in\mathbb Z/2\mathbb Z
\]
und
\[
P_{n,\eta}
=
x_0+n\Delta+\eta\frac L2
\pmod L,
\tag{A9.6}
\]
\[
\overline Q_{n,\eta}
=
2b-x_0-n\Delta+\eta\frac L2
\pmod L.
\tag{A9.7}
\]

Dann:
\[
\boxed{
\begin{array}{c|cc}
&P_{n,\eta}&\overline Q_{n,\eta}\\ \hline
\tau_{+e}&P_{n,\eta+1}&\overline Q_{n,\eta+1}\\
\tau_{+d}&P_{n+1,\eta+1}&\overline Q_{n-1,\eta+1}
\end{array}}
\tag{A9.8}
\]
mit Parität modulo \(2\). Für die inversen Translationen kehren sich die Indexsprünge um.

Für die neuen Reflexionen gilt
\[
a+b-2b=a-b=-d\equiv \frac L2-\Delta\pmod L,
\]
\[
T+b-2b=T-b=e=\frac L2.
\]

Daher
\[
\boxed{
r_{a+b}:
\begin{cases}
P_{n,\eta}\mapsto \overline Q_{n+1,\eta+1},\\
\overline Q_{n,\eta}\mapsto P_{n-1,\eta+1},
\end{cases}}
\tag{A9.9}
\]
und
\[
\boxed{
r_{T+b}:
\begin{cases}
P_{n,\eta}\mapsto \overline Q_{n,\eta+1},\\
\overline Q_{n,\eta}\mapsto P_{n,\eta+1}.
\end{cases}}
\tag{A9.10}
\]

Somit ist der neue \(J_R^*J_R\)-Graph ein **endlicher Paritätsaufsatz über derselben irrationalen Basissequenz**. Es entsteht kein dritter irrationaler Phasenparameter.

---

## 6. Warum A8 nicht automatisch überlebt

A8 benutzt
\[
t_n\in
S_\varepsilon
:=
(\varepsilon,\Delta-\varepsilon).
\]

Für die zweite Paritätsfaser liegt die Phase am selben Index bei
\[
t_n+\frac L2\pmod L.
\]

Wegen
\[
\Delta<\frac L2
\]
sind
\[
S_\varepsilon
\quad\text{und}\quad
S_\varepsilon+\frac L2
\]
disjunkt.

Daher trennt ein A8-Hit in einer Paritätsfaser **nicht automatisch gleichzeitig** die zweite Faser. Die neuen KNF-Kanten A9.8–A9.10 wechseln gerade diese Parität.

Folglich ist A8 nicht einfach als fertiger Separator für den freien Gramgraphen übertragbar.

Dies ist noch **kein expliziter Bypass** und noch kein No-Go. Es zeigt nur, dass A9 eine echte neue endliche Frontierfrage ist.

---

## 7. Nächste Teilaufgaben

### A9-J0 — Identitäts-Gram

Die vollständige Kanten-/Koeffiziententabelle von
\[
J_R^*J_R
\]
wird inklusive A9.3–A9.10 maschinell zertifiziert.

### A9-J1 — Rest-Gram

Für
\[
J_R^*AJ_R
\]
werden die vollständigen A1-Rohkanten auf beiden Seiten durch \(J_R\) gezogen.

Identische affine Kanäle müssen **vor** dem Graphurteil algebraisch zusammengefasst werden, damit mögliche Koeffizientencancellations korrekt behandelt werden.

### A9-SEP — Separatorentscheidung

Auf dem endlichen
\[
(P/\overline Q)\times(\mathbb Z/2)\times\text{Lift}
\]
-Cocycle wird geprüft:

1. existiert ein gemeinsamer wiederkehrender Separatorzustand;
2. oder gibt es einen expliziten KNF-Bypass über die Paritätsfaser?

---

## 8. Aktueller Status

Der derzeitige Strukturkandidat lautet:
\[
\boxed{
\text{KNF fügt eine endliche Halbperioden-Parität hinzu, aber keine neue irrationale Basisrotation.}
}
\tag{A9.11}
\]

Die eigentliche A9-Separatorfrage bleibt
\[
\boxed{?[O].}
\]

Keine Promotion. Keine Aussage über endliche Komponenten von \(\mathfrak G_R\), keine Schur-Injektivität, kein HT-RED, kein Objekt X und keine RH-Folgerung.
