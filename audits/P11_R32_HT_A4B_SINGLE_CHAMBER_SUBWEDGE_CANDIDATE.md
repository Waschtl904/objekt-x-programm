# P11/R32 — HT-A4b-SW1: Single-FG-Chamber-Subwedge unter (R+arepsilon<Delta)

**Status:** Rechenkandidat; keine Promotion.  
**Arbeitsname:** `HT-A4b-SW1`.  
**Repo-Basis:** `main@9d85df51f926d976d7d685dc0000fd7ff41609fb`.  
**Scope:** ausschließlich die restricted-tail-Klasse
[
0<sigmale R<arepsilon,qquad R+arepsilon<Delta,
]
mit
[
T<S=T+sigma<T_0=T+arepsilon<c.
]
**Abhängigkeit:** `HT-A4a FG CLASSIFICATION OF SIX ARGUMENTS: independently GREEN candidate`.  
**Firewall:** keine globale Promotion von HT-A4b, HT-RED, A0 oder Schur-Cross-Gram-Injektivität.

---

## 0. Ziel

Das vollständige HT-A4b-Problem auf dem ganzen offenen Dreieck
[
0<R<arepsilon<c-T
]
enthält zehn Parameterflächen und 15 offene Tail-FG-Chambers.

Dieses Audit prüft bewusst nur den kleineren offenen Subwedge
[
oxed{
mathfrak W_{m SW1}
=
{(R,arepsilon):
0<R<arepsilon, R+arepsilon<Delta}.
}
	ag{SW1.1}
]

Zu zeigen ist:

1. alle fünf inneren Tail-FG-(s)-Wände liegen auf (mathfrak W_{m SW1}) strikt rechts des Integrationsintervalls ((R,arepsilon));
2. damit ist die Fiber-Graph-Klassifikation der sechs Tail-Argumente auf dem gesamten (s)-Intervall konstant;
3. keine der zehn HT.31-Parameterflächen schneidet das Innere von (mathfrak W_{m SW1});
4. (mathfrak W_{m SW1}) ist nichtleer und mit einem (R	o0)-Descent vereinbar;
5. die separat bereits bekannte A-Wall-/HT-A3-Kollision bei (arepsilon=Delta/2) bleibt sichtbar und darf nicht mit der FG-Chamber-Struktur verwechselt werden.

---

## 1. Konstanten und Ordnung

Es gelten
[
d=b-a=rac12lograc32,
qquad
e=T-b=rac12lograc43,
]
[
Delta=d-e=rac12lograc98,
qquad
arepsilon_{max}=c-T=rac12lograc54.
]

Numerisch:
[
Deltaapprox0.05889151783,
quad
arepsilon_{max}approx0.11157177566,
]
[
eapprox0.14384103623,
quad
dapprox0.20273255405.
]

Insbesondere
[
oxed{
0<Delta<arepsilon_{max}<e<d.
}
	ag{SW1.2}
]

Außerdem
[
e>2Delta,
]
denn
[
e-2Delta
=
rac12lograc{256}{243}>0.
	ag{SW1.3}
]

Damit
[
C:=rac{e-Delta}{2}>rac{Delta}{2}.
	ag{SW1.4}
]

---

## 2. Sofortige Folgen der Standing-Hypothese

Aus
[
0<R<arepsilon,
qquad
R+arepsilon<Delta
]
folgt
[
2R<R+arepsilon<Delta,
]
also
[
oxed{
R<rac{Delta}{2}.
}
	ag{SW1.5}
]

Ferner
[
oxed{
arepsilon<Delta-R<Delta.
}
	ag{SW1.6}
]

Damit liegt (mathfrak W_{m SW1}) vollständig in Zone I des Tail-FG-Audits.

---

## 3. Alle fünf Tail-FG-(s)-Wände sind inaktiv

Nach HT.28 sind die fünf inneren Wände
[
D_-=Delta-R,
qquad
D_0=Delta,
qquad
D_+=Delta+R,
]
[
E=e-R,
qquad
A_*=d-R.
]

Für ((R,arepsilon)inmathfrak W_{m SW1}) gilt wegen (SW1.6)
[
D_-=Delta-R>arepsilon.
	ag{SW1.7}
]

Dann unmittelbar
[
D_0=Delta>D_->arepsilon,
	ag{SW1.8}
]
[
D_+=Delta+R>Delta>arepsilon.
	ag{SW1.9}
]

Wegen (e>Delta)
[
E=e-R>Delta-R=D_->arepsilon.
	ag{SW1.10}
]

Wegen (d>e)
[
A_*=d-R>e-R=E>arepsilon.
	ag{SW1.11}
]

Somit
[
oxed{
D_-,D_0,D_+,E,A_*
otin(R,arepsilon)
}
	ag{SW1.12}
]
und sogar alle fünf liegen strikt rechts von (arepsilon).

Es gibt daher auf dem gesamten offenen (s)-Intervall keinen Tail-FG-Umschaltpunkt.

---

## 4. Vollständige Membership-Tabelle der sechs Tail-Argumente

Sei
[
R<s<arepsilon
]
und
[
y=widehatPhi_R(z,0,h)inmathcal K_R.
]

Die drei bereits in HT.23 permanent blinden Werte bleiben
[
y(s)=z(s),
qquad
y(a-s)=z(a-s),
qquad
y(T+s)=z(T+s).
	ag{SW1.13}
]

Für (a+s) gilt nach HT.24 der Wechsel erst bei
[
s=d-R=A_*.
]
Nach (SW1.11) ist (A_*>arepsilon), also
[
oxed{y(a+s)=z(a+s).}
	ag{SW1.14}
]

Für (T-s) gilt nach HT.25 der Wechsel erst bei
[
s=e-R=E.
]
Nach (SW1.10) ist (E>arepsilon), also
[
oxed{y(T-s)=z(T-s).}
	ag{SW1.15}
]

Für (2d-s) gilt wegen
[
s<arepsilon<Delta-R
]
die strikte Ungleichung
[
Delta-s>R.
]
Daher
[
|s-Delta|>R
]
und nach HT.26
[
oxed{y(2d-s)=z(2d-s).}
	ag{SW1.16}
]

Damit lautet die vollständige Membership-Tabelle:

| Argument | Typ auf ganz ((R,arepsilon)) |
|---|---|
| (s) | (Z) |
| (a-s) | (Z) |
| (a+s) | (Z) |
| (T-s) | (Z) |
| (2d-s) | (Z) |
| (T+s) | (Z) |

Insbesondere ist das HT-A4a-Tripel
[
oxed{ZZZ}
	ag{SW1.17}
]
auf dem gesamten Tail-Intervall konstant.

Der private (x_0)-Ast ist hier vakuum:
[
s<arepsilon<Delta,
]
also kann der Bereich
[
Delta<s<Delta+R
]
nicht erreicht werden.

---

## 5. Herkunft und Ausschluss aller zehn HT.31-Flächen

Die zehn Flächen aus HT.31 entstehen vollständig aus Randtreffern der fünf (s)-Wände sowie der einzigen aktiven Wall-Wall-Kollision.

### 5.1 (D_-)-Randtreffer

[
D_-=arepsilon
iff
arepsilon=Delta-R.
]

Dies ist exakt die Randfläche
[
R+arepsilon=Delta
]
von (mathfrak W_{m SW1}), nicht dessen Inneres.

[
D_-=R
iff
R=rac{Delta}{2},
]
unmöglich im Inneren wegen (SW1.5).

### 5.2 (D_0)-Randtreffer

[
D_0=arepsilon
iff
arepsilon=Delta,
]
unmöglich wegen (arepsilon<Delta-R<Delta).

[
D_0=R
iff
R=Delta,
]
unmöglich wegen (R<Delta/2).

### 5.3 (D_+)-Randtreffer

[
D_+=arepsilon
iff
arepsilon=Delta+R,
]
unmöglich, da bereits (arepsilon<Delta-R).

### 5.4 (E)-Randtreffer

[
E=arepsilon
iff
R+arepsilon=e.
]

Da (e>Delta), widerspricht dies (R+arepsilon<Delta).

[
E=R
iff
R=rac e2.
]

Da (e>Delta), gilt (e/2>Delta/2), im Widerspruch zu (SW1.5).

### 5.5 (A_*)-Randtreffer

[
A_*=arepsilon
iff
R+arepsilon=d,
]
unmöglich wegen (d>Delta).

[
A_*=R
iff
R=rac d2,
]
unmöglich wegen (d/2>Delta/2>R).

### 5.6 Einzige aktive Wall-Wall-Kollision

Die einzige HT.31-Wall-Wall-Fläche ist
[
R=C=rac{e-Delta}{2}.
]

Nach (SW1.4)
[
C>rac{Delta}{2}>R,
]
also liegt auch diese Fläche außerhalb des Subwedges.

Damit gilt:

[
oxed{
	ext{Keine der zehn HT.31-Flächen schneidet das Innere von }mathfrak W_{m SW1}.
}
	ag{SW1.18}
]

---

## 6. Identifikation mit Chamber I.1

In §12 des Tail-FG-Audits lautet Chamber I.1:
[
0<R<rac{Delta}{2},
qquad
arepsilon<Delta-R.
]

Nach (SW1.5)–(SW1.6) ist dies exakt auf (mathfrak W_{m SW1}) erfüllt.

Daher
[
oxed{
mathfrak W_{m SW1}subset mathrm{I.1}
}
	ag{SW1.19}
]
und wegen
[
arepsilon<Delta-R
iff
R+arepsilon<Delta
]
ist (mathfrak W_{m SW1}) gerade die (R<arepsilon)-Teilmenge der I.1-Bedingung.

Im hier relevanten Tail-Sektor kollabiert die **Fiber-Graph-Membership-Geometrie** somit auf genau einen offenen Typ:
[
oxed{ZZZ.}
	ag{SW1.20}
]

---

## 7. Nichtleere und expliziter Zeugenpunkt

Setze
[
R_0=rac{Delta}{6},
qquad
arepsilon_0=rac{Delta}{3}.
]

Dann
[
0<R_0<arepsilon_0
]
und
[
R_0+arepsilon_0
=
rac{Delta}{2}
<
Delta.
]

Also
[
oxed{
(R_0,arepsilon_0)inmathfrak W_{m SW1}.
}
	ag{SW1.21}
]

Für das restricted-tail-Stratum kann zusätzlich
[
sigma_0=rac{Delta}{12}
]
gewählt werden. Dann
[
0<sigma_0le R_0<arepsilon_0.
	ag{SW1.22}
]

Der Subwedge ist daher offen und nichtleer.

---

## 8. Verträglichkeit mit einem (R	o0)-Descent

Fixiere irgendein
[
0<arepsilon_*<Delta.
]

Für jede Folge
[
R_ndownarrow0
]
mit schließlich
[
R_n<min{arepsilon_*,Delta-arepsilon_*}
]
gilt
[
0<R_n<arepsilon_*,
qquad
R_n+arepsilon_*<Delta.
]

Mit beispielsweise
[
sigma_n=rac{R_n}{2}
]
gilt zusätzlich
[
0<sigma_nle R_n.
]

Somit ist die Standing-Hypothese
[
R+arepsilon<Delta
]
mit einem (R	o0)-Descent im restricted-tail-Stratum kompatibel.

Dies ist nur eine Parameterverträglichkeitsaussage. Es folgt daraus keine C6-, Strong-Terminal- oder Konvergenzaussage.

---

## 9. Wichtige Nuance: HT-A3/A-Wall kollabiert nicht vollständig

Die erste HT-A3-Kollision lautet
[
I_bcap I_-
earnothing
iff
arepsilon-R>Delta.
]

Unter
[
R+arepsilon<Delta
]
gilt
[
arepsilon-R<arepsilon+R<Delta,
]
also
[
oxed{
I_bcap I_-=arnothing.
}
	ag{SW1.23}
]

Die zweite HT-A3-Kollision lautet jedoch
[
I_bcap I_+
earnothing
iff
R<rac{Delta}{2}<arepsilon.
]

Auf (mathfrak W_{m SW1}) ist (R<Delta/2) automatisch. Daher reduziert sich diese Bedingung zu
[
oxed{
I_bcap I_+
earnothing
iff
arepsilon>rac{Delta}{2}.
}
	ag{SW1.24}
]

Folglich besitzt der Single-FG-Chamber-Subwedge weiterhin die bereits aus NEU-A-WALL-1 bekannte Parameterwand
[
oxed{
arepsilon=rac{Delta}{2}.
}
	ag{SW1.25}
]

Genauer:

- für (arepsilon<Delta/2): kein (I_b)-/(I_+)-Overlap;
- für (arepsilon=Delta/2): die offenen Shells berühren sich nur an einem L2-nulligen Endpunkt;
- für (arepsilon>Delta/2): positiver (I_b)-/(I_+)-Overlap.

Daher:

[
oxed{
	ext{ein FG-Chamber bedeutet nicht ein vollständiges A0-Wall-Chamber.}
}
	ag{SW1.26}
]

Die volle A-Wall/Fiber-Graph-Geometrie des Subwedges zerfällt weiterhin in zwei offene A-Wall-Unterkammern plus die Parameterdegenerationsfläche (arepsilon=Delta/2).

Diese Fläche ist eine echte Parameterkonfiguration und darf nicht als L2-Nullmenge wegdefiniert werden.

---

## 10. Kandidatenurteil

Der hier nachgewiesene eingeschränkte Satz lautet:

[
oxed{
egin{minipage}{0.88linewidth}
Unter
[
0<sigmale R<arepsilon,
qquad
R+arepsilon<Delta,
]
liegen alle fünf Tail-FG-(s)-Wände strikt außerhalb von ((R,arepsilon)). Die sechs Tail-Argumente sind auf dem gesamten (s)-Intervall direkte Blind-(z)-Koordinaten; der (x_0)-Ast tritt nicht auf. Keine der zehn HT.31-Flächen schneidet das Innere dieses Subwedges.
end{minipage}
}
	ag{SW1.27}
]

Arbeitsstatus vor unabhängigem Review:

```text
HT-A4b-SW1 SINGLE-FG-CHAMBER SUBWEDGE: ?[O]

HT-A4b TAIL-FG COMMON REFINEMENT EXHAUSTIVITY: ?[O]
HT-RED TAIL GAUSSIAN ELIMINATION:              ?[O]
A0 FULL FREE-COORDINATE COVERAGE:              ?[O]
SCHUR CROSS-GRAM INJECTIVITY:                  ?[O]
```

Insbesondere wird **nicht** behauptet, dass die globale 15-Chamber-Exhaustivität bereits geprüft oder geschlossen ist.

---

## 11. Konsequenz für die nächste Rechnung

Falls `HT-A4b-SW1` unabhängiges GREEN erhält, kann der erste exakte Downstream-Angriff auf dem Subwedge mit der uniformen Tail-Membership
[
(Z,Z,Z,Z,Z,Z)
]
arbeiten.

Dabei muss die A-Wall-Aufspaltung
[
arepsilon<Delta/2,
qquad
arepsilon=Delta/2,
qquad
arepsilon>Delta/2
]
weiterhin getrennt bleiben.

Dieses Audit selbst führt **keine** Downstream-Elimination durch.

---

## 12. Firewall

Aus `HT-A4b-SW1` folgt nicht:

- globale Exhaustivität der zehn HT.31-Flächen / 15 Chambers;
- HT-A4b global;
- HT-RED;
- Trivialität des reduzierten Kernes;
- A0-Abschluss;
- (kerGamma_I={0});
- Schur-Cross-Gram-Injektivität;
- Closed Range / bounded below;
- Strong Terminal Transport;
- Objekt X;
- RH.

---

## 13. Adversarialer Review-Auftrag

Vor einer Statusbuchung sind unabhängig zu prüfen:

1. die Ordnung (0<Delta<arepsilon_{max}<e<d);
2. (e>2Delta) und damit (C>Delta/2);
3. die Folgerungen (R<Delta/2) und (arepsilon<Delta-R);
4. dass alle fünf (s)-Wände (D_-,D_0,D_+,E,A_*) strikt rechts von (arepsilon) liegen;
5. die sechs Membership-Zeilen (SW1.13)–(SW1.16);
6. dass der (x_0)-Ast vakuum ist;
7. die Herkunft jeder der zehn HT.31-Flächen und ihr Ausschluss aus dem Inneren;
8. die Identifikation mit Chamber I.1;
9. den expliziten Zeugenpunkt ((Delta/6,Delta/3)) und optional (sigma=Delta/12);
10. die (R	o0)-Verträglichkeit;
11. die HT-A3-Nuance: (I_bcap I_-) ist ausgeschlossen, (I_bcap I_+) bleibt genau für (arepsilon>Delta/2) möglich;
12. dass (arepsilon=Delta/2) als Parameterwand A0-relevant bleibt;
13. die Scope-Firewall.

Keine Promotion und kein Merge ohne unabhängiges GREEN gegen den exakten PR-Diff.
