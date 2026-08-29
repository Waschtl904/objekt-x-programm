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


---

## 9. A9-J0 Zertifikatsstatus — Identitäts-Gram

Der Teilknoten A9-J0 wurde adversarial und reproduzierbar geprüft.

Zertifikat:

scripts/certify_sw1_a9_j0_identity_gram.py

Exakt geprüfter Commit:

901ea199c9c0e71bec2b23e89211b19daaf6e85a

Committed Script-Blob:

4bb6fdcb345f106e6d5b7f417ed5d5defb6db630

Ausführungsart:

Python-Standardbibliothek mit exakter fractions.Fraction-Arithmetik; die Konstanten werden als rationale Koeffizientenpaare von \((\log2,\log3)\) dargestellt.

Vor der Ausführung wurde für den tatsächlich ausgeführten Dateiinhalt der Git-Blob-SHA erneut berechnet und exakt mit dem committed Blob

4bb6fdcb345f106e6d5b7f417ed5d5defb6db630

abgeglichen.

Ergebnis:

SW1-A9-J0 IDENTITY-GRAM/PARITY CERTIFICATE: PASS

Zertifiziert wurden im Scope von \(J_R^*J_R\):

- exakt fünf KNF-Rekonstruktionsbranches und damit zehn ungeordnete Off-Diagonal-Paare;
- Nichtverschwindung aller zehn Rang-eins-Paarkoeffizienten unter \(p,q,r>0\);
- alle zehn affinen Paarrelationen aus A9.3;
- die Klassifikation bestehend vs. neu relativ zur A7-Rohmapliste;
- die exakten Identitäten
  \[
  e=L/2,\qquad d=L/2+\Delta;
  \]
- die Paritätsübergänge A9.8–A9.10;
- die exakte Ungleichung
  \[
  \Delta<L/2,
  \]
  hier über
  \[
  L/2-\Delta=\tfrac12\log(32/27)>0;
  \]
- die daraus folgende Disjunktheit des A8-Separatorfensters von seinem \(L/2\)-Shift.

Damit gilt für den **Teilknoten A9-J0**:

\[
\boxed{
\mathrm{A9\!-\!J0}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

### J0-Firewall

Dieser Status gilt ausschließlich für den Identitäts-Gram-Anteil

\[
J_R^*J_R.
\]

Insbesondere ist **nicht** gebucht, dass die zehn Kanten im vollständigen freien Gramoperator

\[
\mathfrak G_R=J_R^*J_R+J_R^*AJ_R
\]

überleben. Identische affine Kanäle aus \(J_R^*AJ_R\) müssen zuerst koeffizientenweise aggregiert werden; vollständige Cancellation bleibt bis A9-J1 ausdrücklich möglich.

Der Gesamtstatus von A9 bleibt daher

\[
\boxed{?[O].}
\]

Keine Promotion. Keine Separatorentscheidung für \(\mathfrak G_R\), keine Schur-Injektivität, kein HT-RED, kein Objekt X und keine RH-Folgerung.


---

## 10. A9-J1a — Überleben der genuin neuen KNF-Kanäle

A9-J1a isoliert denjenigen Teil von \(J_R^*(I+A)J_R\), der durch den rekonstruierten linken \(a\)-Branch entsteht und **genuin neue** affine Typen erzeugt.

Für \(0<u<R<\varepsilon\) liegt

\[
A_-(u)=a-u
\]

uniform in A1-R2. Dort besitzt \(I+A\) lokal die relevanten Kopplungen

\[
\lambda:=1+\alpha_A=1+c_1+c_5
\]

auf der Diagonale von \(A_-\), sowie

\[
A_-\leftrightarrow A_+:\ -c_1,
\qquad
A_-\leftrightarrow T_-:\ \beta_+,
\qquad
A_-\leftrightarrow T_+:\ \beta_-,
\qquad
A_-\leftrightarrow u:\ c_2.
\]

Mit

\[
s:=r/p>0,
\qquad
t:=q/p=2^{-3/4}>0
\]

und dem KNF-Koeffizientenvektor

\[
c=(1,-s,s,-t,t)
\]

ergibt die vollständige lokale Aggregation für die **genuin neuen** \(h/h\)-Kanäle:

\[
\boxed{
\begin{aligned}
C_{r_{a+b}}&=-s(1+c_5),\\
C_{\tau_d}&=+s(1+c_5),\\
C_{\tau_e}^{B_-T_-}&=s\,t,\\
C_{\tau_e}^{B_+T_+}&=s\,M,\\
C_{r_{T+b}}^{B_-T_+}&=-s\,M,\\
C_{r_{T+b}}^{B_+T_-}&=-s\,t,
\end{aligned}}
\]

wobei

\[
M
=
\lambda t+\beta_-
=
t\left(
1-\frac{(2\sqrt2-1)\log2}{8}
\right)>0.
\]

Die zweite \(\tau_e\)-Kombination vereinfacht sogar exakt über

\[
\lambda t-\beta_+=t.
\]

Damit ist **keiner** dieser sechs branchweisen neuen Beiträge durch \(J_R^*AJ_R\) ausgelöscht.

### 10.1 Zwei weitere neue z/h-Kanäle

Die rohe A1-Kante

\[
A_-(u)\leftrightarrow u
\]

mit Koeffizient \(c_2\) erzeugt nach KNF-Rekonstruktion insbesondere

\[
B_-(u)\leftrightarrow u:
\qquad
r_b(x)=b-x
\]

mit Gesamtkoeffizient

\[
\boxed{-s\,c_2\ne0},
\]

sowie

\[
B_+(u)\leftrightarrow u:
\qquad
\tau_{+b}(x)=x+b
\]

mit

\[
\boxed{+s\,c_2\ne0}.
\]

Da weder \(r_b\) noch \(\tau_{\pm b}\) in der vollständigen A7-Rohmapliste vorkommen, existiert kein zusätzlicher roher A1-Kanal desselben affinen Typs, der diese Beiträge noch canceln könnte.

Somit erweitert sich die genuin neue KNF-Typenliste auf

\[
\boxed{
\tau_{\pm d},
\quad
\tau_{\pm e},
\quad
\tau_{\pm b},
\quad
r_{a+b},
\quad
r_{T+b},
\quad
r_b.
}
\]

### 10.2 Auch b erzeugt keine neue irrationale Basisphase

Exakt gilt

\[
\boxed{
b=\frac32L+2\Delta
}
\]

und damit modulo \(L\)

\[
b\equiv \frac L2+2\Delta.
\]

Also ist auch der neue \(\tau_b/r_b\)-Mechanismus lediglich ein weiterer endlicher Paritäts-/Indexsprung über derselben \(\Delta\)-Rotation.

### 10.3 Zertifikat

Zertifikat:

scripts/certify_sw1_a9_j1a_new_channel_survival.py

Exakt geprüfter Commit:

6089f9f30c3365e5ea119fd60aa0db6a699961e8

Committed Script-Blob:

a3d89cbbea279fd74b7b5c689d9f2b59a0b9dc11

Tool:

Python / SymPy 1.14.0

Der tatsächlich ausgeführte Dateiinhalt wurde vor Ausführung erneut als Git-Blob gehasht und stimmt exakt mit

a3d89cbbea279fd74b7b5c689d9f2b59a0b9dc11

überein.

Ergebnis:

SW1-A9-J1a NEW-CHANNEL SURVIVAL CERTIFICATE: PASS

Damit gilt

\[
\boxed{
\mathrm{A9\!-\!J1a}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

### 10.4 J1a-Firewall

A9-J1a aggregiert vollständig die **genuin neuen** KNF-Kanäle, aber noch nicht sämtliche bereits aus A7 bekannten affinen Typen nach KNF-Transport.

Daher bleibt **A9-J1 als Ganzes** noch offen. Insbesondere ist noch nicht entschieden, welche bestehenden A7-Kanten im vollen Gramoperator durch Koeffizientencancellation verschwinden oder ihre Aktivitätsdomänen verändern.

Für einen Separatorbeweis kann jedoch bereits der sichere Supergraph verwendet werden, der alle A7-Rohkanten plus die oben zertifizierten neuen KNF-Kanten enthält: Falls schon dieser Supergraph einen wiederkehrenden Separator besitzt, besitzt ihn erst recht der tatsächliche Gramgraph.

Keine Promotion. Noch keine A9-Separatorentscheidung, keine Schur-Injektivität, kein HT-RED, kein Objekt X und keine RH-Folgerung.
