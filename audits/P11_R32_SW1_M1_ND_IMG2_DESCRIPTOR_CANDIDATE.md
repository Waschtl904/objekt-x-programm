# P11/R32 — SW1 M1-ND IMG2 Descriptor / Identity-Pivot Candidate

> **Stand:** 31. August 2026  
> **Base:** `main@b47be753bc74028441ecd41365082efd567d515a`  
> **Arbeitsbranch:** `research/sw1-m1-nd-img2-descriptor`  
> **Status:** `AI-GREEN candidate` — Descriptor-/Pivot-Normalform; mechanisches Zertifikat im finite/algebraischen Scope. **Keine Promotion.**  
> **Scope-Firewall:** keine Injektivität von (mathscr N_R), kein (kerGamma_I={0}), keine Kontraktionsaussage, keine Rekurrenzlösbarkeit, kein Objekt X und keine RH-Folgerung.

---

## 0. Ziel

Nach IMG1 wirkt der effektive Operator

[
mathscr N_R:
mathscr B_Koplusmathscr B_W
longrightarrow
mathscr B_H^0
]

als endliche Summe affine Pullbacks auf drei Horizon- und drei Annulus-Funktionskanäle.

IMG2 isoliert zwei zusätzliche Strukturen:

1. die KNF-Zulässigkeit (mathscr B_K) lebt im **selben** Zwei-Blatt-/Paritäts-Cocycle wie IMG1;
2. der Horizon-Anteil besitzt einen kanonischen, rein lokalen Identitäts-Pivot (D_R).

Beides reduziert die nächste Nichtentartungsanalyse, ohne einen äußeren Shiftblock zu invertieren.

---

## 1. Gemeinsame affine Algebra

Die zwölf IMG1-Pullback-Typen werden als

[
alpha=(s,h,k),
qquad
	hetalongmapsto
s	heta+hL+kDelta
pmod L
]

geschrieben, mit (sin{pm1}), (hin{0,	frac12}) und ganzzahligem (k).

Die KNF-Row

[
0=
p[y(a-u)-y(a+u)]
+r[y(b-u)-y(b+u)]
+q[y(T-u)-y(T+u)]
]

verwendet modulo (L) exakt

[
egin{aligned}
a-u&=-u+Delta,&
a+u&=u+Delta,\
b-u&=-u+rac L2+2Delta,&
b+u&=u+rac L2+2Delta,\
T-u&=-u+2Delta,&
T+u&=u+2Delta.
end{aligned}
]

Alle sechs Typen gehören bereits zum IMG1-Alphabet.

Damit erzeugt die KNF-Bedingung keine neue irrationale Phase.

---

## 2. Feste KNF-Liftkanäle

Im C1B2A-normalisierten Scope gilt

[
Delta=1+2r,
qquad
L=4+10r,
qquad
E_{max}=rac{r+1}{2},
qquad
3<r<4,
]

und

[
0<u<R<arepsilon<E_{max}.
]

Das Descriptor-Zertifikat beweist die sechs strikten Ungleichungen

[
L<a-u<a+u<2L,
]

[
L<b-u<b+u<2L,
]

[
2L<T-u<T+u<3L.
]

Daher liegen die KNF-Samples im gesamten offenen SW1/M1-Scope fest in

[
apm u, bpm u
longleftrightarrow
f_1,
]

[
Tpm u
longleftrightarrow
f_2.
]

Die KNF-Zulässigkeit ist somit die interne Descriptor-Row

[
oxed{
egin{aligned}
0={}&
p,[f_1(-u+Delta)-f_1(u+Delta)]\
&+
r,[f_1(-u+L/2+2Delta)-f_1(u+L/2+2Delta)]\
&+
q,[f_2(-u+2Delta)-f_2(u+2Delta)].
end{aligned}}
]

Sie muss bei jeder späteren Rekurrenz gleichzeitig mitgeführt werden.

---

## 3. Zwei-Blatt-/Paritätsform

Schreibe formal

[
P_{n,eta}
=
t+nDelta+etarac L2,
]

[
Q_{n,eta}
=
-t+(4-n)Delta+etarac L2,
qquad
etainmathbb Z/2.
]

Für (alpha=(s,h,k)) folgt exakt:

### Orientierungserhaltend (s=+1)

[
P_{n,eta}mapsto
P_{n+k,etaoplusepsilon},
]

[
Q_{n,eta}mapsto
Q_{n-k,etaoplusepsilon}.
]

### Orientierungsumkehrend (s=-1)

[
P_{n,eta}mapsto
Q_{n+4-k,etaoplusepsilon},
]

[
Q_{n,eta}mapsto
P_{n+k-4,etaoplusepsilon},
]

wobei (epsilon=1) genau für (h=	frac12).

Für alle zwölf IMG1-Typen ist die maximale lokale Indexreichweite

[
oxed{|j|le3}.
]

Damit bleibt die gesamte IMG1+KNF-Dynamik ein finite-range Descriptor-System über **einer** irrationalen (Delta)-Rotation, zwei Blättern und einer (mathbb Z/2)-Parität.

---

# Teil II — Identitäts-Pivot

## 4. Einziger Identitätspullback

Der Identitätstyp ist

[
mathrm{Id}=(+1,0,0).
]

Das Pivot-Zertifikat leitet die effektiven P0-Pullbacks aus den kanonischen M1-Source-Relations her und prüft exakt:

[
oxed{
	ext{FREE-Quelle }I
	ext{ ist die einzige Quelle mit Pullback Id}.
}
]

Für sämtliche HUB-Quellen gilt

[
oxed{
	ext{kein HUB-Term besitzt den Identitätspullback}.
}
]

Außerdem liefert die Source-/Lift-Algebra für (I)

[
g_{m in}=P_0,
qquad
j=0,
qquad
m=0,
]

also auf jedem aktiven Ausgangslift genau denselben Horizon-Lift.

---

## 5. Rowtyp-Konstanten

Der Identitätskoeffizient hängt **nicht von (	heta)** innerhalb eines Rowtyps ab. Er ist eine der endlich vielen Konstanten

[
egin{array}{c|c}
	ext{Rowtyp}&d_{m row}\
hline
R0&1+2c_1\
R1&1+c_1\
R2,R3,R4I&1+alpha_A\
R4II,R5&1+alpha_b\
R6,R7&1+kappa.
end{array}
]

Mit

[
c_1>0,
qquad
alpha_A>0,
qquad
alpha_b>0,
qquad
kappa>0
]

folgt symbolisch

[
oxed{d_{m row}>1}
]

für jeden Rowtyp.

Im aktuellen M1-Scope ist (R4II) strukturell unerreichbar, denn

[
E_{max}
=
rac{r+1}{2}
<
rac{1+2r}{2}
=
rac{Delta}{2}
]

und sogar

[
rac{Delta}{2}-E_{max}
=
rac r2>0.
]

Es bleiben acht aktive Rowtypen.

---

## 6. Was die 6144-Atomprüfung wirklich beweist

Am Referenzwert (r_0=7/2) werden alle

[
64	imes96=6144
]

offenen Parameter-/Kreisatome exhaustiv geprüft.

Über allen aktiven P0-Horizon-Ausgangsslots ergeben sich

[
oxed{15227}
]

Slots.

Für **jeden** davon findet das Zertifikat exakt einen Identitätsterm, und zwar

[
(	ext{Horizon}, ell_{m in}=ell_{m out}, I, d_{m row}).
]

Also

[
oxed{
#	ext{Identity-Pivots}
=
#	ext{aktive Horizon-Ausgangsslots}
=
15227.
}
]

Diese Exhaustion beweist die **Rowtyp-/Slot-Zuordnung** am Referenzwert.

Sie ist **nicht** der funktionalanalytische Beweis der Operatornorm von (D_R^{-1}).

---

## 7. Analytischer Multiplikationsoperator-Schritt

Definiere auf

[
mathscr B_H^0
=
igoplus_{ell=0}^2
m_ell L^2(mathbb T_L)
]

den Operator

[
(D_R f)_ell(	heta)
=
d_R(	heta,ell),f_ell(	heta),
]

wobei (d_R(	heta,ell)) auf jedem offenen Rowatom genau die zugehörige Rowtyp-Konstante (d_{m row}) ist.

Die Rowgrenzen sind endlich viele Kreiswände und daher Nullmengen. A.e. nimmt (d_R) somit nur Werte aus der endlichen aktiven Menge

[
mathcal D
=
{d_{m row}:	ext{aktive Rowtypen}}.
]

Da jedes (dinmathcal D) exakt (>1) ist und (mathcal D) endlich ist, gilt

[
delta
:=
min_{dinmathcal D}(d-1)
>0.
]

Folglich

[
d_R(	heta,ell)
ge
1+delta
quad	ext{a.e.}
]

und daher ist der Multiplikationsoperator beschränkt invertierbar mit

[
(D_R^{-1}h)_ell(	heta)
=
rac{1}{d_R(	heta,ell)}h_ell(	heta).
]

Für einen diagonalen Multiplikationsoperator auf der direkten (L^2)-Summe gilt

[
oxed{
|D_R^{-1}|
=
operatorname*{ess,sup}_{	heta,ell}
rac1{d_R(	heta,ell)}
=
max_{dinmathcal D}rac1d
<1.
}
]

Das ist der unendlichdimensionale Funktionsraum-Schritt.

**Wichtig:** Der Code prüft nun auch die endlichen Prämissen

[
0<rac1{d_{m row}}<1
]

symbolisch/exakt; eine Gleitkommazahl wird hierfür nicht als Beweis verwendet.

---

## 8. All-(r)-Übertragung des Pivot-Skeletts

Die acht Rowkoeffizienten sind arithmetische Konstanten und hängen weder von (	heta) noch von (r) ab.

C1B2A-TRANSFER liefert bereits

[
mathrm{M1!-!FULL}(7/2)
Longrightarrow
mathrm{M1!-!FULL}(r),
qquad
3<r<4,
]

für die korrespondierenden offenen Parameterkammern und Kreisatome.

Die Identitätspullback-Eigenschaft der Quelle (I) ist species-/lift-algebraisch und ebenfalls (r)-unabhängig.

Damit überträgt sich die a.e. Rowtyp-Multiplikatorstruktur von (D_R) auf den gesamten offenen C1B2A-Scope.

Dies ist **kein** Anspruch, dass numerische Kreisoperatoren bei verschiedenen (r) identisch seien.

---

## 9. Legale Pivot-Gleichung

Schreibe

[
mathscr N_R(f,g)
=
D_Rf+mathcal R_Rf+mathcal H_Rg,
]

wobei (mathcal R_R) sämtliche nichtidentischen Horizon-Pullbacks und (mathcal H_R) sämtliche Annulus-/HUB-Pullbacks enthält.

Dann gilt auf (mathscr B_H^0)

[
mathscr N_R(f,g)=0
]

genau dann, wenn

[
oxed{
f
=
-D_R^{-1}
igl(
mathcal R_Rf+mathcal H_Rg
igr).
}
]

Hier wird ausschließlich der diagonale Multiplikationsoperator (D_R) invertiert.

Es wird **kein** äußerer Shiftblock und kein möglicherweise singulärer Transferblock invertiert.

---

## 10. Zusätzliche KNF-Invarianz-Firewall

Aus der beschränkten Invertierbarkeit auf (mathscr B_H^0) folgt **nicht**

[
D_R^{-1}mathscr B_K
subseteq
mathscr B_K.
]

Eine solche Invarianz ist hier weder behauptet noch bewiesen.

Für ein tatsächliches Kernelpaar ((f,g)inmathscr B_Koplusmathscr B_W) ist die Pivot-Gleichung natürlich äquivalent zur ursprünglichen Operatorgleichung, weil ihre linke Seite dasselbe (f) ist.

Aber eine iterative oder dynamische Verwendung von

[
fmapsto
-D_R^{-1}(mathcal R_Rf+mathcal H_Rg)
]

darf **nicht** als Selbstabbildung von (mathscr B_K) behandelt werden. Die KNF-Descriptor-Row aus Abschnitt 2 muss gleichzeitig mitgeführt werden.

---

## 11. Keine Kontraktionsaussage

Aus

[
|D_R^{-1}|<1
]

folgt ausdrücklich **nicht**

[
|D_R^{-1}mathcal R_R|<1.
]

Dafür wäre eine echte Operatornormabschätzung von (mathcal R_R) beziehungsweise der gesamten zusammengesetzten Rekurrenz nötig.

Daher folgt gegenwärtig weder eine Neumann-Reihe noch Unique Continuation noch Kerneltrivialität.

---

## 12. Zertifikate

### Descriptor

`scripts/certify_sw1_m1_nd_img2_descriptor.py`

prüft insbesondere:

- 12 IMG1-affine Typen;
- Zwei-Blatt-/Paritäts-Transitionsgesetz;
- maximale Indexreichweite (3);
- KNF-Typen als Teilmenge des IMG1-Alphabets;
- feste KNF-Kanäle;
- 1152 physische Referenz-Lift-/Map-Checks.

### Identity Pivot

`scripts/certify_sw1_m1_nd_img2_identity_pivot.py`

prüft insbesondere:

- Identitätspullback nur aus FREE-(I);
- kein HUB-Identitätspullback;
- exakte symbolische Positivität aller Rowmultiplikatoren;
- exakte symbolische Kehrwertschranken (0<1/d_{m row}<1);
- 6144 Referenzatome;
- 15227 aktive Horizon-Ausgangsslots;
- 15227 eindeutige Identitätspivots;
- (R4II=0) im M1-Scope.

---

## 13. Zulässige Buchung

Der neue strukturelle Stand ist

[
oxed{
	ext{IMG2-DESCRIPTOR/PIVOT:
AI-GREEN candidate
+ certificate im finite/algebraischen Scope.}
}
]

Insbesondere ist nun legitim:

[
oxed{
mathscr B_K
	ext{ als interne range-3 Descriptor-Row im IMG1-Cocycle}
}
]

und

[
oxed{
mathscr N_R
=
D_R+	ext{nichtidentische Transfers},
qquad
D_R^{-1}inmathcal B(mathscr B_H^0).
}
]

Nicht legitim ist weiterhin:

[
kermathscr N_R={0},
]

[
kerGamma_I={0},
]

eine Kontraktionsaussage oder eine (checkmark[M])-Promotion.
