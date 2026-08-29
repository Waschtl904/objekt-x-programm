# P11/R32 — SW1-A9 KNF Separator Stability Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a8-lower-finite-components@d99d4ef780dc47876ff0445e2bcd403f45679610  
> **Status:** ?[O] gesamt — A9-J0/J1/FS/DOM zertifiziert; für den kleinen unteren Subchamber `0<ε<(6Δ-L)/4` sind staggered KNF-Separator und endliche physische Punktkomponenten zertifiziert; im komplementären unteren Subchamber existiert bereits ein partieller Bypass, vollständige Klassifikation dort weiter offen; keine Promotion.  
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


---

## 11. A9-J1(full) — vollständiger lokaler 6×6-KNF-Gramblock

Der vollständige lokale Effekt der KNF-Rekonstruktion kann exakt auf einen einzigen physischen Stern reduziert werden.

Für \(0<u<R<\varepsilon\) ist

\[
A_-(u)=a-u
\]

der einzige rekonstruierte physische Branch. Wegen \(a-\varepsilon<A_-(u)<a\) liegt er uniform in A1-R2. Die A1-R2-Zeile koppelt \(A_-\) ausschließlich an

\[
u,\qquad A_+,\qquad T_-,\qquad T_+
\]

sowie an sich selbst. Durch Selbstadjungiertheit existieren keine weiteren physischen Kanten, die \(A_-\) von außen treffen.

Außerhalb dieses Sterns wirkt \(J_R\) auf den freien physischen Koordinaten identisch. Daher ist die gesamte Änderung von \(I+A\) zu

\[
\mathfrak G_R=J_R^*(I+A)J_R
\]

durch den Pullback des lokalen physischen Blocks auf

\[
\{u,A_-,A_+,B_-,B_+,T_-,T_+\}
\]

bestimmt.

Nach Elimination von \(A_-\) bleibt der freie 6-Knoten-Block

\[
\boxed{
\{u,A_+,B_-,B_+,T_-,T_+\}.
}
\]

### 11.1 Exakte 15 Off-Diagonal-Kanäle

Alle \(\binom62=15\) Off-Diagonal-Einträge sind exakt ungleich Null:

\[
\boxed{
\begin{array}{c|c|c}
\text{Paar}&\text{affiner Typ}&\text{Vorzeichen}\\ \hline
u\leftrightarrow A_+&\tau_a&+\\
u\leftrightarrow B_-&r_b&-\\
u\leftrightarrow B_+&\tau_b&+\\
u\leftrightarrow T_-&r_T&-\\
u\leftrightarrow T_+&\tau_T&-\\
A_+\leftrightarrow B_-&r_{a+b}&-\\
A_+\leftrightarrow B_+&\tau_d&+\\
A_+\leftrightarrow T_-&r_{3a}&-\\
A_+\leftrightarrow T_+&\tau_a&+\\
B_-\leftrightarrow B_+&r_{2b}&-\\
B_-\leftrightarrow T_-&\tau_e&+\\
B_-\leftrightarrow T_+&r_{T+b}&-\\
B_+\leftrightarrow T_-&r_{T+b}&-\\
B_+\leftrightarrow T_+&\tau_e&+\\
T_-\leftrightarrow T_+&r_{4a}&-
\end{array}
}
\]

Insbesondere sind die beiden vom Blindkoordinatenpunkt \(u\) ausgehenden neuen Kanäle separat:

\[
\boxed{
C_{r_b}=-s\,c_2\ne0,
\qquad
C_{\tau_b}=+s\,c_2\ne0.
}
\]

### 11.2 Exakte Vorzeichenfirewall

Keines der 15 Vorzeichen wird numerisch entschieden.

Für die zwei zuvor empfindlichsten Faktoren verwendet das Zertifikat die exakten positiven Größen

\[
H:=4+\log2-\sqrt2\,\log2,
\]

\[
K:=8+\log2-2\sqrt2\,\log2
\]

und beweist sogar die strikten Margen

\[
\boxed{H>3,\qquad K>6.}
\]

Damit ist insbesondere die frühere \(M\)-Positivität nicht mehr auf einen Dezimalcheck gestützt.

### 11.3 Reproduzierbares Zertifikat

Zertifikat:

scripts/certify_sw1_a9_j1_full_local_6x6.py

Commit:

c3d03291e97f11664121e182d62335cd1c249ab4

Committed Script-Blob:

88519300148ae3badc9860473784bce3d068e033

Der tatsächlich ausgeführte Dateiinhalt wurde als Git-Blob gehasht und ergab exakt

88519300148ae3badc9860473784bce3d068e033.

Ergebnis:

SW1-A9-J1 FULL LOCAL 6x6 CERTIFICATE: PASS

SymPy 1.14.0.

Damit gilt für den vollständigen lokalen KNF-Änderungsblock:

\[
\boxed{
\mathrm{A9\!-\!J1}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

### 11.4 Globaler Graphledger nach J1

Der freie Gramgraph kann nun exakt so gelesen werden:

1. alle rohen A7-Kanten zwischen freien physischen Punkten, die den rekonstruierten Branch \(A_-\) nicht benutzen, bleiben unverändert;
2. der physische Branch \(A_-\in(a-R,a)\) ist keine freie Koordinate;
3. für jedes \(0<u<R\) ersetzt ihn der vollständig zertifizierte 6×6-Block aus Abschnitt 11.1.

Damit ist die Kanten-/Cancellation-Frage von A9-J1 geschlossen.

**Offen bleibt ausschließlich A9-SEP:** Ob dieser nun exakt bekannte erweiterte Graph einen wiederkehrenden gemeinsamen Separator besitzt oder einen echten KNF-Bypass zulässt.

Keine Promotion. Keine Schur-Injektivität, kein HT-RED, kein Objekt X und keine RH-Folgerung.


---

## 12. A9-SEP-BYPASS(part) — regulärer KNF-Bypass auf offenem Subchamber

Der explorativ gefundene Midpoint-Pfad darf wegen der A8-Midpoint-Degeneration **nicht** als Beweis verwendet werden. Abschnitt 12 ersetzt ihn vollständig durch einen regulären Phasenbeweis mit

\[
s\neq\Delta/2.
\]

### 12.1 Exakte Bypass-Schwelle

Setze

\[
\boxed{
s_*:=\frac L2-2\Delta.
}
\]

Aus

\[
L-4\Delta=\log(256/243)>0
\]

folgt

\[
s_*>0.
\]

Ferner

\[
5\Delta-L
=
\frac12\log\!\left(\frac{3^{12}}{2^{19}}\right)>0
\]

und daher

\[
\boxed{
0<s_*<\Delta/2.
}
\]

### 12.2 Offenes Parametergebiet

Betrachte den unteren SW1-Subchamber

\[
\boxed{
0<\sigma\le R<\varepsilon<\Delta/2,
\qquad
\varepsilon<s_*+R.
}
\tag{A9.12}
\]

Wegen \(R<\varepsilon<\Delta/2\) gilt automatisch

\[
R+\varepsilon<2\varepsilon<\Delta,
\]

also liegt A9.12 vollständig im SW1-Scope.

Definiere stärker das **linke reguläre Bypassintervall**

\[
I_{\rm by}^{<}
:=
\left(
\max\{\varepsilon,s_*\},
\min\{\Delta-\varepsilon,s_*+R,\Delta/2\}
\right).
\]

Es ist wichtig, dass **nicht** angenommen wird

\[
s_*+R<\Delta/2.
\]

Diese Ungleichung folgt aus A9.12 im Allgemeinen nicht und wird auch nicht benötigt.

Für die Nichtleerheit von \(I_{\rm by}^{<}\) genügen die sechs Paarungleichungen

\[
\varepsilon<\Delta-\varepsilon,
\qquad
\varepsilon<s_*+R,
\qquad
\varepsilon<\Delta/2,
\]

\[
s_*<\Delta-\varepsilon,
\qquad
s_*<s_*+R,
\qquad
s_*<\Delta/2.
\]

Die erste und dritte folgen aus \(\varepsilon<\Delta/2\), die zweite ist gerade A9.12, die letzten beiden sind trivial aus \(R>0\) beziehungsweise \(s_*<\Delta/2\), und

\[
s_*<\Delta-\varepsilon
\]

folgt aus \(s_*<\Delta/2\) und \(\varepsilon<\Delta/2\).

Damit

\[
\boxed{
I_{\rm by}^{<}\neq\varnothing.
}
\]

Wir wählen von nun an

\[
\boxed{
s\in I_{\rm by}^{<}.
}
\]

Dann gilt automatisch

\[
\varepsilon<s<\Delta/2,
\]

also liegt der Bypass ausdrücklich im **linken** regulären A8-Separatorintervall. Ein mögliches Überschreiten des Midpoints durch den oberen KNF-Fensterrand \(s_*+R\) ist irrelevant.

Setze

\[
\boxed{
u:=s-s_*.
}
\]

Dann gilt exakt

\[
\boxed{
0<u<R.
}
\]

Außerdem ist

\[
s\in
(\varepsilon,\Delta/2)
\cup
(\Delta/2,\Delta-\varepsilon)
=
S_\varepsilon^{\rm reg},
\]

also eine reguläre A8-Separatorphase nach der Midpoint-Korrektur.

### 12.3 Expliziter Indexpfad

Im paritätserweiterten Cocycle existiert der Pfad

\[
\boxed{
\begin{aligned}
P_{-1,1}
&\xrightarrow{r_T}
\overline Q_{1,1}
\xrightarrow{r_{2b}}
P_{1,1}
\xrightarrow{r_{3a}}
\overline Q_{2,1}
\xrightarrow{r_{2b}}
P_{2,1}\\
&\xrightarrow{r_{3a}}
\overline Q_{3,1}
\xrightarrow{r_{2b}}
P_{3,1}
\xrightarrow{r_{3a}}
\overline Q_{4,1}
\xrightarrow{r_{2b}}
P_{4,1}\\
&\xrightarrow{\tau_{-e}\ {\rm(KNF)}}
P_{4,0}
\xrightarrow{r_T}
\overline Q_{6,0}.
\end{aligned}
}
\tag{A9.13}
\]

Er verbindet damit lokale Indizes

\[
\boxed{-1\longrightarrow 6.}
\]

Die verwendeten physischen Repräsentanten können exakt als

\[
\begin{aligned}
y_{-1}&=s+\frac L2-\Delta,\\
x_1&=\frac32L+3\Delta-s,\\
x_2&=\frac32L+\Delta+s,\\
x_3&=\frac32L+2\Delta-s,\\
x_4&=\frac32L+2\Delta+s,\\
x_5&=\frac32L+\Delta-s,\\
x_6&=\frac32L+3\Delta+s,\\
x_7&=\frac32L-s,\\
x_8&=\frac32L+4\Delta+s,\\
x_9&=L+4\Delta+s,\\
y_6&=L-2\Delta-s
\end{aligned}
\]

gewählt werden.

Das Zertifikat prüft sowohl sämtliche affine Gleichungen in A9.13 als auch ihre P-/\(\overline Q\)-Indexkongruenzen modulo \(L\).

### 12.4 Gate- und Free-Coordinate-Prüfung

Alle verwendeten rohen Kanten liegen exakt in ihren A7-Domänen:

- \(r_T\) an den beiden Enden;
- \(r_{2b}\) an \(x_1,x_3,x_5,x_7\);
- \(r_{3a}\) an \(x_2,x_4,x_6\).

Sämtliche benötigten Randabstände werden im Zertifikat als **strictly positive symbolic margins** ausgewertet; es gibt keinen numerischen Gate-Test.

Ebenso wird geprüft:

- \(y_{-1}\) und \(y_6\) liegen strikt unter \(a-R\);
- alle inneren \(x_1,\ldots,x_9\) liegen strikt oberhalb \(a\).

Der rekonstruierte freie Nicht-Koordinaten-Branch

\[
(a-R,a)
\]

wird daher nirgends als Graphknoten benutzt.

### 12.5 Die einzige KNF-Kante

Aus

\[
u=s-s_*
\]

folgt exakt

\[
x_8=T+u,
\qquad
x_9=b+u.
\]

Da

\[
e=T-b=L/2,
\]

ist

\[
x_8\xrightarrow{\tau_{-e}}x_9
\]

genau die J1-Kante

\[
T_+\leftrightarrow B_+.
\]

A9-J1(full) beweist für ihren Koeffizienten exakt Nichtverschwindung; der dortige heikle Faktor besitzt sogar die Marge

\[
K>6.
\]

Somit ist A9.13 ein tatsächlicher Pfad des freien Gramgraphen und kein bloßer formaler Affinpfad.

### 12.6 Zertifikat

Zertifikat:

scripts/certify_sw1_a9_regular_phase_bypass.py

Commit:

48b6ea8380e19487a909822ff114b0770a086a4b

Committed Script-Blob:

f70c277a5d91507784634be2bd720da3467c1303

Der tatsächlich ausgeführte Dateiinhalt ergab exakt denselben Git-Blob-SHA.

Ergebnis:

SW1-A9 REGULAR-PHASE KNF BYPASS CERTIFICATE: PASS

SymPy 1.14.0.

Damit ist zulässig:

\[
\boxed{
\mathrm{A9\!-\!SEP\!-\!BYPASS(part)}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

### 12.7 Exakte Negativaussage

Auf dem offenen Subchamber A9.12 gilt:

\[
\boxed{
\text{Die A8-Separatoren übertragen sich nicht universell auf }
\mathfrak G_R.
}
\]

Genauer: Für jedes Parameterpaar in A9.12 existiert eine **reguläre** A8-Phase \(s\in S_\varepsilon^{\rm reg}\), die im rohen A1-Graphen Separatorphase ist, im KNF-erweiterten freien Gramgraphen aber durch A9.13 umgangen wird.

### 12.8 Strikte Firewall

Nicht bewiesen ist:

1. dass **jede** Phase in \(S_\varepsilon^{\rm reg}\) einen KNF-Bypass besitzt;
2. dass im Subchamber A9.12 überhaupt **kein anderer** wiederkehrender Separator existiert;
3. dass die freien Gramkomponenten unendlich sind;
4. dass im komplementären unteren Bereich
   \[
   \varepsilon\ge s_*+R
   \]
   dasselbe geschieht;
5. irgendeine Schur-/Cross-Gram-Nichtinjektivität.

Der Gesamtstatus

\[
\boxed{\mathrm{A9\!-\!SEP}:?[O]}
\]

bleibt deshalb bestehen.

**Scan-Firewall:** Frühere endliche Fensterscans werden ausschließlich als Exploration behandelt. „Kein Separator im gescannten Fenster gefunden“ ist **keine** Nichtexistenzaussage und wird nicht als mathematischer Status gebucht.


---

## 13. A9-FS — vollständiger paritätserweiterter finite-state Cocycle

Nach A9-J1 ist die affine Typenliste des freien Gramgraphen vollständig bekannt. Sie besteht aus

\[
\{\tau_{\pm a},\tau_{\pm T},r_a,r_T,r_{3a},r_{4a},r_{2b}\}
\]

aus A7 sowie den genuin neuen KNF-Typen

\[
\boxed{
\tau_{\pm e},
\quad
\tau_{\pm d},
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

Mit der Parität \(\eta\in\mathbb Z/2\) gilt:

### 13.1 Alte A7-Typen

Alle A7-Typen erhalten die Parität. Ihre lokalen Indexsprünge bleiben exakt die A7-Sprünge und erfüllen

\[
|j|\le3.
\]

### 13.2 Neue Translationen

Aus

\[
e=L/2,\qquad
d=L/2+\Delta,\qquad
b=3L/2+2\Delta
\]

folgt modulo \(L\):

\[
\begin{array}{c|cc}
&P_{n,\eta}&\overline Q_{n,\eta}\\ \hline
\tau_{+e}&P_{n,\eta+1}&\overline Q_{n,\eta+1}\\
\tau_{+d}&P_{n+1,\eta+1}&\overline Q_{n-1,\eta+1}\\
\tau_{+b}&P_{n+2,\eta+1}&\overline Q_{n-2,\eta+1}.
\end{array}
\]

Die inversen Translationen kehren die Indexsprünge um.

### 13.3 Neue Reflexionen

Modulo \(L\) gilt

\[
(a+b)-2b\equiv L/2-\Delta,
\]

\[
(T+b)-2b\equiv L/2,
\]

\[
b-2b\equiv L/2-2\Delta.
\]

Daher:

\[
r_{a+b}:
\quad
P_{n,\eta}\leftrightarrow\overline Q_{n+1,\eta+1},
\]

\[
r_{T+b}:
\quad
P_{n,\eta}\leftrightarrow\overline Q_{n,\eta+1},
\]

\[
r_b:
\quad
P_{n,\eta}\leftrightarrow\overline Q_{n+2,\eta+1},
\]

mit den entsprechend negativen Rücksprüngen von \(\overline Q\) nach \(P\).

Die neuen KNF-Typen haben daher maximale Indexreichweite \(2\). Zusammen mit A7 bleibt die Gesamt-Reichweite

\[
\boxed{|j|\le3.}
\]

### 13.4 Formale Zustandszahl

A7 liefert weiterhin

\[
T_0<3L.
\]

Pro Blatt und Paritätsfaser existieren deshalb höchstens drei positive Lifts. Der formale Zustandsraum pro Rotationsindex besitzt somit höchstens

\[
\boxed{
2\ \text{Blätter}
\times
2\ \text{Paritäten}
\times
3\ \text{Lifts}
=
12
}
\]

Labels.

**Physische Quotienten-Firewall:** Formal verschiedene Labels, die denselben physischen Punkt repräsentieren, müssen identifiziert werden. Solche Koinzidenzen können die Zahl physischer Zustände nur reduzieren; sie dürfen niemals als zwei getrennte Graphknoten verwendet werden. Die A8-Midpoint-Korrektur ist hierfür das erste konkrete Beispiel.

### 13.5 Zertifikat

Zertifikat:

scripts/certify_sw1_a9_full_finite_state_cocycle.py

Commit:

30e7b630fa0208d6d4941bca06249efc0f1f0246

Committed Script-Blob:

715ba55a40e2b86119758913b25e132351571727

Der aus GitHub gelesene Dateiinhalt wurde lokal erneut nach dem Git-Blob-Verfahren gehasht und ergab exakt denselben SHA

715ba55a40e2b86119758913b25e132351571727.

Ergebnis der exakten committed Ausführung:

SW1-A9 FULL KNF FINITE-STATE COCYCLE CERTIFICATE: PASS

Verwendet wird ausschließlich exakte fractions.Fraction-Arithmetik.

Damit gilt:

\[
\boxed{
\mathrm{A9\!-\!FS}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

### 13.6 Firewall

A9-FS ist eine endliche Transferreduktion. Sie beweist weder endliche noch unendliche Zusammenhangskomponenten.

Der Gesamtstatus bleibt

\[
\boxed{\mathrm{A9\!-\!SEP}:?[O].}
\]

Der nächste notwendige Schritt ist die exakte Aktivitäts-/Gate-Tabelle der neuen KNF-Kanten und anschließend die quotient-bewusste Frontierklassifikation des 12-Label-Cocycles.


---

## 14. A9-DOM — exakte Aktivitätsdomänen der neuen KNF-Kanten

A9-J1 beweist die Nichtverschwindung aller 15 lokalen freien K6-Kanten. Für die Frontierfrage muss zusätzlich bekannt sein, **wo** die genuin neuen affinen Typen aktiv sind.

Für jedes

\[
0<u<R
\]

sind die sechs freien lokalen Punkte

\[
u,\quad
A_+=a+u,\quad
B_-=b-u,\quad
B_+=b+u,\quad
T_-=T-u,\quad
T_+=T+u.
\]

Daraus folgen, modulo Endpunkte/Nullmengen, exakt die folgenden neuen Domänen.

### 14.1 \(r_b\)

\[
u\leftrightarrow b-u
\]

liefert

\[
\boxed{
D_{r_b}
=
(0,R)\cup(b-R,b).
}
\]

### 14.2 \(\tau_{\pm b}\)

\[
u\xrightarrow{+b}b+u
\]

liefert

\[
\boxed{
D_{+b}=(0,R),
\qquad
D_{-b}=(b,b+R).
}
\]

### 14.3 \(r_{a+b}\)

\[
a+u\leftrightarrow b-u
\]

liefert

\[
\boxed{
D_{r_{a+b}}
=
(a,a+R)\cup(b-R,b).
}
\]

### 14.4 \(\tau_{\pm d}\)

\[
a+u\xrightarrow{+d}b+u
\]

liefert

\[
\boxed{
D_{+d}=(a,a+R),
\qquad
D_{-d}=(b,b+R).
}
\]

### 14.5 \(\tau_{\pm e}\)

Die beiden Kanten

\[
b-u\xrightarrow{+e}T-u,
\qquad
b+u\xrightarrow{+e}T+u
\]

geben

\[
\boxed{
D_{+e}
=
(b-R,b)\cup(b,b+R),
}
\]

und invers

\[
\boxed{
D_{-e}
=
(T-R,T)\cup(T,T+R).
}
\]

### 14.6 \(r_{T+b}\)

Aus

\[
b-u\leftrightarrow T+u,
\qquad
b+u\leftrightarrow T-u
\]

folgt

\[
\boxed{
D_{r_{T+b}}
=
(b-R,b)\cup(b,b+R)
\cup
(T-R,T)\cup(T,T+R).
}
\]

Alle neuen KNF-Domänen sind damit auf die direkten sechs KNF-Fenster beschränkt. Außerhalb dieser Fenster entsteht durch \(J_R\) kein genuin neuer affiner Kantentyp.

### 14.7 Zertifikat

Zertifikat:

scripts/certify_sw1_a9_new_knf_domains.py

Commit:

f565d359f754d0e8c1cd01464977497bf00485b8

Committed Script-Blob:

5b7fa5747514f0b8c7363bfaa36e7eff2e89f1f4

Der aus GitHub gelesene Inhalt wurde erneut nach dem Git-Blob-Verfahren gehasht; der Hash stimmt exakt mit dem committed Blob überein.

Ergebnis:

SW1-A9 NEW KNF ACTIVITY-DOMAIN CERTIFICATE: PASS

SymPy, ausschließlich exakte symbolische Identitäten.

Damit gilt

\[
\boxed{
\mathrm{A9\!-\!DOM}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

### 14.8 Frontier-Firewall

Mit A9-FS und A9-DOM ist die Übergangsrelation nun endlich und vollständig spezifiziert. Noch offen ist die dynamische Erreichbarkeitsklassifikation.

Insbesondere folgt aus der Existenz des zertifizierten Teil-Bypasses in Abschnitt 12 weiterhin **nicht**, dass eine Komponente unendlich ist.

Der nächste Knoten ist die quotient-bewusste Frontierklassifikation:

\[
\boxed{
\mathrm{A9\!-\!FRONTIER}:?[O].
}
\]


---

## 15. A9-SEP-SMALL — staggered KNF-Separator und endliche Punktkomponenten

Die explorative Zahl „84 Cross-Kandidaten“ war **nicht exhaustiv** und wird verworfen.

Die vollständige kombinatorische Analyse ergibt stattdessen:

- zwei A8-Mittelblöcke mit jeweils 20 formalen Labels;
- insgesamt 40 relevante Mittelblocklabels;
- neun gerichtete neue KNF-Maptypen;
- daraus exakt
  \[
  \boxed{128}
  \]
  gerichtete formale Cross-Kandidaten.

Diese 128 gerichteten Fälle entsprechen generisch

\[
\boxed{95}
\]

ungerichteten physischen Edge-Klassen:

- 62 nur einmal im Mittelblockledger erfasste Klassen;
- 33 reziprok doppelt erfasste Klassen.

Damit wird die Redundanz explizit dokumentiert; „128 geprüft“ wird **nicht** als 128 unabhängige mathematische Phänomene interpretiert.

### 15.1 Exakte Schwelle

Setze

\[
s_*:=\frac L2-2\Delta.
\]

Definiere

\[
\boxed{
\varepsilon_*
:=
\frac{\Delta-s_*}{2}
=
\frac{6\Delta-L}{4}.
}
\]

Aus

\[
4\Delta<L<5\Delta
\]

folgt

\[
\boxed{
0<\varepsilon_*<\Delta/2.
}
\]

Wir betrachten

\[
\boxed{
0<\varepsilon<\varepsilon_*.
}
\tag{A9.15}
\]

### 15.2 Gemeinsames staggered Phasenfenster

Für einen Index \(n\) setze

\[
t_n=s.
\]

Parität \(0\) verwendet den A8-Separator bei \(n\).

Parität \(1\) wird um zwei Indizes nach links versetzt. Wegen

\[
t_{n-2}+\frac L2
=
s-2\Delta+\frac L2
=
s+s_*
\]

ist ihre A8-Phase am Index \(n-2\)

\[
s+s_*.
\]

Beide Phasen liegen gleichzeitig im A8-Fenster

\[
(\varepsilon,\Delta-\varepsilon)
\]

genau für

\[
\boxed{
s\in
W_\varepsilon
:=
(\varepsilon,\Delta-\varepsilon-s_*).
}
\]

Die Länge ist

\[
|W_\varepsilon|
=
\Delta-2\varepsilon-s_*
=
2(\varepsilon_*-\varepsilon)>0.
\]

Somit ist \(W_\varepsilon\) ein nichtleeres offenes Intervall.

### 15.3 Kombinierter Seitenindex

Für Parität \(0\) verwenden wir die A8-Stufung mit Mittelindizes

\[
n,n+1,n+2,n+3.
\]

Für Parität \(1\) verwenden wir dieselbe A8-Stufung, aber mit Mittelindizes

\[
n-2,n-1,n,n+1.
\]

Die alten A7-Kanten erhalten die Parität. Daher werden sie auf jeder Paritätsfaser separat durch den bereits zertifizierten **formalen** A8-Separator blockiert.

Alle neuen KNF-Kanten wechseln die Parität und besitzen Indexreichweite höchstens \(2\).

Eine neue KNF-Kante, die den kombinierten Links/Rechts-Schnitt kreuzt, muss daher mindestens einen Endpunkt in einem der beiden vierlagigen Mittelblöcke besitzen. Eine direkte Kante von einem asymptotisch linken Außenbereich in einen asymptotisch rechten Außenbereich würde mindestens Indexsprung \(3\) benötigen und ist für die neuen KNF-Typen unmöglich.

Damit ist die Enumeration der

\[
40\times9
\]

Source-Map-Möglichkeiten vor der Cross-Filterung kombinatorisch vollständig.

### 15.4 Exakte 128er-Cross-Prüfung

Das Zertifikat erzeugt aus diesem vollständigen Ledger exakt 128 gerichtete Cross-Kandidaten.

Für ihre neuen KNF-Aktivitätsdomänen werden insgesamt

\[
\boxed{218}
\]

Intervall-Ausschlussungleichungen geprüft, die sich auf

\[
\boxed{42}
\]

verschiedene symbolische Margen reduzieren.

Jede dieser 42 Margen wird **exakt** als nichtnegative Linearkombination der strikt positiven Grundslacks

\[
g>0,
\qquad
\frac12-g>0,
\qquad
R>0,
\qquad
\varepsilon-R>0,
\]

\[
s-\varepsilon>0,
\qquad
\Delta-\varepsilon-s-s_*>0
\]

dargestellt, nach Normierung \(\Delta=1\).

Es gibt keinen numerischen Gate-Test.

Ergebnis:

\[
\boxed{
\text{0 aktive neue KNF-Cross-Kanten unter den 128 vollständigen Kandidaten.}
}
\]

### 15.5 Formales Separatorlemma

Folglich gibt es im vollständigen **formalen** A9-Cover keine Kante zwischen den beiden kombinierten Seiten.

Asymptotisch gilt für einen Separatorindex \(n\):

- alle Zustände mit Index
  \[
  m\le n-3
  \]
  liegen links;
- alle Zustände mit Index
  \[
  m\ge n+4
  \]
  liegen rechts.

Daher:

\[
\boxed{
t_n\in W_\varepsilon
\Longrightarrow
\text{kein formaler KNF-Pfad verbindet }
m\le n-3
\text{ mit }
m\ge n+4.
}
\tag{A9.16}
\]

### 15.6 Irrationale Wiederkehr und formale Komponentenendlichkeit

Wegen

\[
\Delta/L\notin\mathbb Q
\]

trifft die Basisrotation jedes nichtleere offene Intervall, insbesondere \(W_\varepsilon\), in beiden Indexrichtungen unendlich oft.

Fixiere einen formalen Knoten mit Index \(m_0\).

Wähle einen Separatorindex \(n_-\) weit links mit

\[
n_-\le m_0-4
\]

und einen Separatorindex \(n_+\) weit rechts mit

\[
n_+\ge m_0+3.
\]

Dann liegt \(m_0\) bezüglich des linken Separators sicher auf der rechten und bezüglich des rechten Separators sicher auf der linken Seite.

Damit kann seine formale Komponente keine Indizes

\[
m\le n_--3
\]

und keine Indizes

\[
m\ge n_++4
\]

enthalten.

Der Indexsupport liegt also in einem endlichen ganzzahligen Intervall. Nach A9-FS existieren pro Index höchstens zwölf formale Labels.

Somit:

\[
\boxed{
0<\varepsilon<\varepsilon_*
\Longrightarrow
\text{jede formale Zusammenhangskomponente des vollständigen KNF-Gramgraphen ist endlich.}
}
\tag{A9.17}
\]

### 15.7 Globale physische Sheet-Kollisionen

Eine bloße lokale Label-Kollisionsprüfung wäre für A9.17 nicht ausreichend.

Falls sich zwei der formalen Rotationsorbits physisch schneiden, liefert die Irrationalität von \(\Delta/L\) einen eindeutigen ganzzahligen Indexparameter \(K\) und einen Paritätsoffset

\[
\delta\in\mathbb Z/2
\]

mit der Identifikation

\[
\boxed{
J_{K,\delta}(P_{n,\eta})
=
\overline Q_{K-n,\eta+\delta}.
}
\]

Die beiden Paritätscosets \(P_{\eta=0}\) und \(P_{\eta=1}\) können wegen der Irrationalität nicht miteinander zusammenfallen; ebenso können nicht zwei verschiedene \(\delta\)-Offsets gleichzeitig auftreten.

Das Zertifikat

scripts/certify_sw1_sheet_collision_quotient.py

beweist für **alle 18 gerichteten Übergangstypen** — neun A7-Typen plus neun neue A9-Typen — exakt

\[
J_{K,\delta}\circ E
=
E\circ J_{K,\delta}
\]

für beide \(\delta=0,1\).

Da die Gate-/Supportentscheidung nur vom physischen Punkt \(x\) abhängt, ist \(J_{K,\delta}\) ein Graphautomorphismus des formalen aktiven Covers.

Eine physische Quotientenkomponente ist daher die Projektion der Sättigung

\[
C\cup J_{K,\delta}(C)
\]

einer formalen Komponente \(C\).

Es werden höchstens zwei formale Komponenten verklebt.

Aus A9.17 folgt somit physisch:

\[
\boxed{
0<\varepsilon<\frac{6\Delta-L}{4}
\Longrightarrow
\text{jede physische Punktkomponente des vollständigen freien KNF-Gramgraphen ist endlich.}
}
\tag{A9.18}
\]

### 15.8 Zertifikate

**Staggered separator**

scripts/certify_sw1_a9_staggered_separator.py

Commit:

0c95b4d0127178ec5153384ab204100c9ee1bb2e

Committed Script-Blob:

c24b9c2d35f032f42924a2378f3faae73a9b1f4b

Der tatsächlich ausgeführte Dateiinhalt wurde erneut nach dem Git-Blob-Verfahren gehasht und ergab exakt denselben SHA.

Ergebnis:

SW1-A9 STAGGERED KNF SEPARATOR CERTIFICATE: PASS

**Globaler Sheet-Kollisionsquotient**

scripts/certify_sw1_sheet_collision_quotient.py

A9-Commit:

312d136241410f53146f83845d58602c9fa1d9cf

Committed Script-Blob:

a1e62d885788c9b3eb696fd7709b81193e345410

Exakte committed Ausführung:

SW1 GLOBAL SHEET-COLLISION QUOTIENT CERTIFICATE: PASS

### 15.9 Zulässige Buchung

Damit gilt:

\[
\boxed{
\mathrm{A9\!-\!SEP\!-\!SMALL}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
\]

und als Konsequenz im exakt angegebenen Subchamber:

\[
\boxed{
\mathrm{A9\!-\!FINITE\!-\!SMALL}:
\text{endliche physische KNF-Punktkomponenten}.
}
\]

### 15.10 Strikte Firewall

Nicht bewiesen ist:

1. endliche KNF-Komponenten für
   \[
   \varepsilon_*\le\varepsilon<\Delta/2;
   \]
2. irgendeine Aussage für den oberen \(\varepsilon\)-Chamber;
3. Invertierbarkeit oder Nichtentartung der endlichen Gramblöcke;
4. \(\ker\mathcal L_{\rm ann}^{SW1}=\{0\}\);
5. \(\ker\Gamma_I=\{0\}\);
6. HT-RED, Objekt X oder RH.

Der **gesamte A9-Knoten** bleibt deshalb

\[
\boxed{?[O],}
\]

aber sein kleine-\(\varepsilon\)-Separator-/Endlichkeits-Subknoten ist zertifiziert.
