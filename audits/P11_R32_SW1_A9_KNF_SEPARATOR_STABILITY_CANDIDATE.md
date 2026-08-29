# P11/R32 — SW1-A9 KNF Separator Stability Candidate

> **Stand:** 29. August 2026  
> **Stacked base:** research/sw1-a8-lower-finite-components@d99d4ef780dc47876ff0445e2bcd403f45679610  
> **Status:** ?[O] — KNF-Zusatzkanten strukturell begonnen; Separatorstabilität noch nicht entschieden; keine Promotion.  
> **Scope:** zusätzlicher freier Koordinatengraph von (mathfrak G_R=J_R^*(I+A)J_R) im unteren Chamber. A8 bleibt nur Input für den rohen A1-Graphen.

---

## 0. Ziel und Firewall

A8 liefert im unteren Chamber
[
0<arepsilon<Delta/2
]
endliche Zusammenhangskomponenten des vollständigen **rohen A1-Punktgraphen**.

Das genügt nicht für
[
mathfrak G_R=J_R^*(I+A)J_R,
]
weil die KNF-Rekonstruktion
[
J_R=Psi_R^{-1}
]
den linken (a)-Samplebranch durch fünf freie Samplebranches ersetzt.

A9 fragt ausschließlich:

[
oxed{
	ext{Erhalten die durch }J_R	ext{ erzeugten freien Koordinatenkanten die A8-Separatoren?}
}
]

Noch keine Aussage über Schur-Injektivität, HT-RED, Objekt X oder RH.

---

## 1. Exakte KNF-Rekonstruktion

Für (0<u<R) setze
[
A_+(u)=a+u,
qquad
B_-(u)=b-u,
qquad
B_+(u)=b+u,
]
[
T_-(u)=T-u,
qquad
T_+(u)=T+u.
]

Nach SW1-KNF gilt
[
oxed{
y(a-u)
=
y(A_+(u))
-rac rp,y(B_-(u))
+rac rp,y(B_+(u))
-rac qp,y(T_-(u))
+rac qp,y(T_+(u)).
}
	ag{A9.1}
]

Alle fünf Koeffizienten
[
1,quad -r/p,quad r/p,quad -q/p,quad q/p
]
sind ungleich Null.

---

## 2. Bereits der Identitätsteil erzeugt einen 5-Knoten-Grambeitrag

Schreibe den freien Fünfervektor bei festem (u) als
[
H(u)
=
igl(
h_A(u),
h_{B,-}(u),
h_{B,+}(u),
h_{T,-}(u),
h_{T,+}(u)
igr).
]

Der rekonstruierte linke (a)-Branch ist
[
x(u)=ccdot H(u),
qquad
c=
left(
1,-rac rp,rac rp,-rac qp,rac qp
ight).
]

Daher enthält
[
J_R^*J_R
]
auf diesem Fünferblock den positiven Rang-eins-Beitrag
[
oxed{c^*c.}
	ag{A9.2}
]

Vor Zusammenfassung mit dem (J_R^*AJ_R)-Anteil besitzt A9.2 zwischen jedem Paar der fünf freien Samplebranches einen nichtverschwindenden off-diagonalen Term.

**Cancellation-Firewall:** Daraus wird noch nicht behauptet, dass jeder dieser Einträge im vollständig aufsummierten Operator (mathfrak G_R) ungleich Null bleibt. Gleiche affine Kanäle aus (J_R^*AJ_R) müssen vor einem endgültigen Graphurteil koeffizientenweise zusammengeführt werden.

---

## 3. Affine Kanten des KNF-Fünferblocks

Die zehn ungeordneten Paare aus A9.2 realisieren die folgenden affinen Maps:

[
oxed{
egin{array}{c|c}
	ext{Paar}&	ext{affine Relation}\ hline
A_+leftrightarrow B_-&xmapsto a+b-x\
A_+leftrightarrow B_+&xmapsto x+d\
A_+leftrightarrow T_-&xmapsto 3a-x\
A_+leftrightarrow T_+&xmapsto x+a\
B_-leftrightarrow B_+&xmapsto 2b-x\
B_-leftrightarrow T_-&xmapsto x+e\
B_-leftrightarrow T_+&xmapsto T+b-x\
B_+leftrightarrow T_-&xmapsto T+b-x\
B_+leftrightarrow T_+&xmapsto x+e\
T_-leftrightarrow T_+&xmapsto 4a-x.
end{array}}
	ag{A9.3}
]

Gegenüber der A7-Rohmapliste sind bereits vorhanden:

[
r_{3a},qquad 	au_{pm a},qquad r_{2b},qquad r_{4a}.
]

Genuin neu durch die KNF-Rekonstruktion sind damit zunächst die vier affinen Typen

[
oxed{
	au_{pm d},
qquad
	au_{pm e},
qquad
r_{a+b},
qquad
r_{T+b}.
}
	ag{A9.4}
]

---

## 4. Entscheidende Reduktion: keine neue irrationale Phase

Mit
[
L=a-Delta
]
und
[
Delta=2d-a
]
folgt exakt
[
d=rac{a+Delta}{2},
qquad
e=a-d.
]

Da
[
a=L+Delta,
]
erhält man

[
oxed{
e=rac L2,
qquad
d=rac L2+Delta.
}
	ag{A9.5}
]

Damit erzeugen die neuen Translationen A9.4 **keine zweite unabhängige irrationale Rotation**.

Sie erweitern die A7-Basis lediglich um eine endliche Halbperioden-Parität.

---

## 5. Paritätserweiterter Cocycle

Definiere
[
etainmathbb Z/2mathbb Z
]
und die beiden Halbperiodenfasern

[
P_{n,eta}
=
x_0+nDelta+etarac L2
pmod L,
	ag{A9.6}
]
[
overline Q_{n,eta}
=
2b-x_0-nDelta+etarac L2
pmod L.
	ag{A9.7}
]

Dann wirken die neuen Translationen exakt als

[
oxed{
egin{array}{c|cc}
&P_{n,eta}&overline Q_{n,eta}\ hline
	au_{+e}&P_{n,eta+1}&overline Q_{n,eta+1}\
	au_{+d}&P_{n+1,eta+1}&overline Q_{n-1,eta+1}
end{array}}
	ag{A9.8}
]

mit Parität modulo (2). Für die inversen Translationen kehren sich die Indexsprünge um.

Für die beiden neuen Reflexionen gilt modulo (L):

[
a+b-2b=a-b=-dequiv rac L2-Delta,
]
[
T+b-2b=T-b=e=rac L2.
]

Daher

[
oxed{
r_{a+b}:
egin{cases}
P_{n,eta}mapsto overline Q_{n+1,eta+1},\
overline Q_{n,eta}mapsto P_{n-1,eta+1},
end{cases}}
	ag{A9.9}
]

und

[
oxed{
r_{T+b}:
egin{cases}
P_{n,eta}mapsto overline Q_{n,eta+1},\
overline Q_{n,eta}mapsto P_{n,eta+1}.
end{cases}}
	ag{A9.10}
]

Somit ist der neue (J_R^*J_R)-Graph ein **endlicher Paritätsaufsatz über derselben irrationalen Basissequenz**.

Insbesondere entsteht aus A9.4 kein dritter irrationaler Phasenparameter.

---

## 6. Warum A8 trotzdem nicht automatisch überlebt

A8 benutzt einen Separatorindex (n) mit

[
t_nin
S_arepsilon
:=
(arepsilon,Delta-arepsilon).
]

Für die zweite Paritätsfaser liegt die Phase am selben Index bei

[
t_n+rac L2pmod L.
]

Wegen
[
Delta<rac L2
]
sind
[
S_arepsilon
quad	ext{und}quad
S_arepsilon+rac L2
]
disjunkt.

Daher trennt ein A8-Hit in einer Paritätsfaser **nicht automatisch gleichzeitig** die zweite Faser.

Die neuen KNF-Kanten A9.8–A9.10 wechseln gerade diese Parität.

Folglich ist A8 nicht einfach als fertiger Separator für den freien Gramgraphen übertragbar.

Dies ist noch **kein expliziter Bypass** und noch kein No-Go. Es zeigt nur, dass A9 eine echte neue endliche Frontierfrage ist.

---

## 7. Nächste exakte Teilaufgaben

A9 wird in drei getrennten Stufen fortgesetzt.

### A9-J0 — Identitäts-Gram

Die vollständige Kanten-/Koeffiziententabelle des Beitrags
[
J_R^*J_R
]
wird inklusive A9.3–A9.10 maschinell zertifiziert.

### A9-J1 — Rest-Gram

Für
[
J_R^*AJ_R
]
werden die vollständigen A1-Rohkanten auf beiden Seiten durch (J_R) gezogen.

Dabei müssen alle identischen affinen Kanäle **vor** dem Graphurteil algebraisch zusammengefasst werden, um mögliche Koeffizientencancellations korrekt zu behandeln.

### A9-SEP — Separatorentscheidung

Auf dem dadurch entstehenden endlichen
[
(P/overline Q)	imes(mathbb Z/2)	imes	ext{Lift}
]
-Cocycle wird geprüft:

1. existiert ein gemeinsamer wiederkehrender Separatorzustand;
2. oder gibt es einen expliziten KNF-Bypass über die Paritätsfaser?

---

## 8. Aktueller Status

Der derzeit gesicherte neue Strukturpunkt ist:

[
oxed{
	ext{KNF fügt eine endliche Halbperioden-Parität hinzu, aber keine neue irrationale Basisrotation.}
}
	ag{A9.11}
]

Die eigentliche A9-Separatorfrage bleibt

[
oxed{?[O].}
]

Keine Promotion. Keine Aussage über endliche Komponenten von (mathfrak G_R), keine Schur-Injektivität, kein HT-RED, kein Objekt X und keine RH-Folgerung.
