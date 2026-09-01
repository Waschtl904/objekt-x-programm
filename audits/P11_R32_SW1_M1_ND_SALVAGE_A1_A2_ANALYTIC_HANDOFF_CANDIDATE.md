# P11/R32 — SALVAGE-A1/A2 Analytic Handoff Candidate

> **Stand:** 1. September 2026  
> **Status:** interner analytischer Handoff für Gate D; keine eigenständige Promotion.  
> **Zweck:** zeigen, dass der neue uniform-blind-Wedge nur parameteruniforme
> IMG0/IMG3/IMG4-Bausteine benutzt und nicht den alten speziellen
> (arepsilon_0=Delta/4)-Mass-Transport-Teil.

---

## 1. Scope

Fixiere

[
0<arepsilon<arepsilon_c
:=
rac{T-10Delta}{8}.
]

Da

[
arepsilon_c<Delta/2,
]

liegt der gesamte neue Wedge im unteren A7-Chamber.

Weiter:

[
0<R<arepsilon,
qquad
0<sigma<R.
]

---

## 2. FREE graph: nur A7 wird benötigt

A7 ist ausdrücklich für den gesamten unteren Chamber

[
0<arepsilon<Delta/2
]

formuliert.

Die vollständige nichtdiagonale physische FREE-Mapliste ist

[
	au_{pm a},
quad
	au_{pm T},
quad
r_a,r_T,r_{3a},r_{4a},r_{2b}.
	ag{HOF.1}
]

Der neue exakte SALVAGE-A1/A2-Check beweist, dass

[
K_arepsilon
]

unter genau diesem vollständigen Graphing invariant ist.

Für jedes (R<arepsilon) gilt

[
U_Rsubset U_arepsilon^{max}subset K_arepsilon.
]

Daher

[
V_{arepsilon,R}
:=
operatorname{Sat}_{mathcal E_arepsilon}(U_R)
subset K_arepsilon.
	ag{HOF.2}
]

Hier wird weder ein Komponentenbound noch ein Separator-Return-Bound benutzt.

---

## 3. Horizonoperator ist parameteruniform

IMG3 beweist auf dem gesamten IMG0-Horizonraum

[
oxed{
mathscr T_B
=
V^*(I+A)V.
}
	ag{HOF.3}
]

Dabei ist (V) die unitäre positive-Halbachsenidentifikation.

Da

[
I+Age I,
]

gilt für jeden SW1-Parameter

[
oxed{
mathscr T_Bge I
}
	ag{HOF.4}
]

und somit

[
mathscr T_B^{-1}
]

beschränkt.

Sei

[
M_{V_{arepsilon,R}}h
=
1_{V_{arepsilon,R}}h
]

auf dem physischen Horizon und

[
Pi_{arepsilon,R}
=
V^*M_{V_{arepsilon,R}}V.
]

Weil (V_{arepsilon,R}) per Definition unter dem vollständigen A7-Graphing
gesättigt ist, gilt auf jeder aktiven FREE-Kante

[
1_{V_{arepsilon,R}}(x)
=
1_{V_{arepsilon,R}}(phi(x)).
]

Damit kommutiert der Multiplikator termweise mit allen Pullbacks und
Diagonalmultiplikatoren:

[
M_{V_{arepsilon,R}}(I+A)
=
(I+A)M_{V_{arepsilon,R}}.
]

Transportiert:

[
oxed{
Pi_{arepsilon,R}mathscr T_B
=
mathscr T_BPi_{arepsilon,R},
}
	ag{HOF.5}
]

und wegen HOF.4

[
oxed{
Pi_{arepsilon,R}mathscr T_B^{-1}
=
mathscr T_B^{-1}Pi_{arepsilon,R}.
}
	ag{HOF.6}
]

Dieser Schritt kennt weder (arepsilon_0=Delta/4) noch 780.

---

## 4. Annulus-Hub ist parameteruniform

IMG0 identifiziert

[
mathscr B_W
=
igoplus_{k=0}^2 n_kL^2(mathbb T_L)
]

mit beliebigen positiven Annulus-(L^2)-Daten.

Der unitäre Odd-Transport

[
W:mathscr B_W	omathscr H_-^{m ann}
]

und die physische Hubabbildung

[
H=HE_{mathcal A}
]

geben exakt

[
oxed{
mathcal H_R
=
V^*HW.
}
	ag{HOF.7}
]

Die sechs positiven Source-Maps sind für jeden SW1-Parameter

[
|x-a|, x+a, |x-b|, x+b, |x-T|, x+T.
	ag{HOF.8}
]

SALVAGE-A2 beweist für

[
B_arepsilon
subset(arepsilon,T)
]

und jeden (xin K_arepsilon), dass keiner der sechs Werte HOF.8 in
(B_arepsilon) liegt.

Wegen HOF.2 gilt dies insbesondere auf
(V_{arepsilon,R}).

---

## 5. Zulässiger Annulusvektor

Da

[
R<arepsilon
]

und

[
S=T+sigma>T,
]

gilt

[
B_arepsilon
subset
(arepsilon,T)
subset
(R,S).
	ag{HOF.9}
]

Wähle

[
0
e w_+in L^2(B_arepsilon).
]

IMG0 liefert einen eindeutigen

[
0
e ginmathscr B_W.
]

Aus HOF.7–HOF.9:

[
oxed{
Pi_{arepsilon,R}mathcal H_Rg=0.
}
	ag{HOF.10}
]

---

## 6. KNF-Handoff

Setze

[
f
=
-mathscr T_B^{-1}mathcal H_Rg.
]

Mit HOF.6 und HOF.10:

[
Pi_{arepsilon,R}f=0.
]

Damit verschwindet die positive physische Horizonrekonstruktion von (f)
auf

[
V_{arepsilon,R},
]

also insbesondere auf

[
U_R.
]

IMG2/KNF charakterisiert den zulässigen Horizonraum durch die einzige Row

[
p[f(a-u)-f(a+u)]
+r[f(b-u)-f(b+u)]
+q[f(T-u)-f(T+u)]
=0
]

für fast jedes (0<u<R).

Alle sechs Samplewerte liegen in (U_R) und verschwinden. Daher

[
oxed{
finmathscr B_K.
}
	ag{HOF.11}
]

Schließlich

[
mathscr N_R(f,g)
=
mathscr T_Bf+mathcal H_Rg
=
0.
]

Wegen (g
e0):

[
oxed{
kermathscr N_R
e{0}.
}
	ag{HOF.12}
]

---

## 7. Was aus IMG4 nicht importiert wird

Der neue Wedge-Beweis benutzt ausdrücklich **nicht**:

- den a.e.-780-Komponentenbound;
- die (pm14)-Separatordeckung;
- Mass Transport;
- die alte Maßschranke (28080R);
- den speziellen Witness (R_0=T/100000);
- P12 zur eigentlichen Kernelkonstruktion.

P12 kann weiterhin nur zur Interpretation verwendet werden, dass der
Annulusvektor kein trivialer äußerer Hubkernel ist.

---

## 8. Internes Gate-D-Verdict

Unter Verwendung der bereits kanonischen IMG0/IMG2/IMG3/IMG4-Identitäten ist
der Handoff von der neuen exakten Geometrie zum tatsächlichen zulässigen
(mathscr N_R)-Kernel parameteruniform auf

[
0<arepsilon<arepsilon_c,
quad
0<R<arepsilon,
quad
0<sigma<R.
]

[
oxed{
	ext{Gate D: intern GREEN candidate.}
}
]

Keine neue Promotion wird durch dieses Dokument allein erzeugt.
