# P11-O3f — Second-Moment-Kompressionsvarianz und polynomialer Theta-Witness

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3f]`  
**Vorgänger:** O3, O3d-I2, O3e  
**Direkte Schnittstellen:** O1, O2, O3, O3e  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, kein Beweis eines tatsächlichen polynomialen Witnesses, kein Beweis von `Theta_- -> 0`, kein Beweis von `chi_- ||Theta_-|| -> 0`, kein starker odd Terminaltransport, kein SYN, kein Seal.

---

## 0. Urteil

O3e hat gezeigt, dass der bisherige O3-Produktkanal

\[
\chi^{R,-}_{T_0,U}\,\|\Theta^-_{T_0,U}\|\to0
\]

wegen der in O3d-I2 bewiesenen superpolynomialen Konditionsdivergenz nur funktionieren kann, wenn `Theta_-` beyond all orders klein ist.

Der vorliegende Knoten identifiziert einen neuen, rein **First-Power-/Second-Moment-artigen** Witness, der einen Lower-Bound für `Theta_-` liefert.

Für festes

\[
0<R<S<T_0<U
\]

und auf dem odd Sektor setze

\[
A_R:=A_{T_0,U}^{R,-},
\qquad
A_S:=A_{T_0,U}^{S,-},
\qquad
W:=W_{R,S,-}^{[T_0]}.
\]

O3 liefert

\[
W^*W=I,
\qquad
W^*A_SW=A_R.
\]

Definiere den First-Power-Range-Defekt

\[
\boxed{
\mathscr B
:=(I-WW^*)A_SW.
}
\tag{O3f.1}
\]

Dann gilt exakt

\[
\boxed{
\mathscr B=A_SW-WA_R,
}
\tag{O3f.2}
\]

und

\[
\boxed{
\mathscr B^*\mathscr B
=
W^*A_S^2W-A_R^2
\ge0.
}
\tag{O3f.3}
\]

Damit ist

\[
\Delta_2
:=W^*A_S^2W-A_R^2
\]

eine positive **Second-Moment-Kompressionsvarianz**.

Der Hauptsatz dieses Knotens ist die quantitative Lower-Bound-Brücke

\[
\boxed{
\|\Theta^-_{T_0,U}\|
\ge
\frac{
\|\Delta_2\|
}{
2\,\|A_R\|\,\bigl(\sqrt{\|A_R\|}+\sqrt{\|A_S\|}\bigr)^2
}.
}
\tag{O3f.4}
\]

Wegen

\[
\|A_R\|\le\|A_S\|
\]

folgt die gröbere, aber sehr einfache Form

\[
\boxed{
\|\Theta^-_{T_0,U}\|
\ge
\frac{
\|W^*A_S^2W-A_R^2\|
}{
8\,\|A_R\|\,\|A_S\|
}.
}
\tag{O3f.5}
\]

Definiere daher den dimensionslosen Second-Moment-Witness

\[
\boxed{
\nu_{2;R,S}^{T_0,U}
:=
\frac{
\|W^*A_S^2W-A_R^2\|
}{
\|A_R\|\,\|A_S\|
}.
}
\tag{O3f.6}
\]

Dann

\[
\boxed{
\|\Theta^-_{T_0,U}\|
\ge
\frac18\,\nu_{2;R,S}^{T_0,U}.
}
\tag{O3f.7}
\]

Folglich genügt bereits ein polynomialer Lower-Witness

\[
\nu_{2;R,S}^{T_0,U_j}
\ge cU_j^{-M}
\]

entlang einer Folge `U_j -> infinity`, um den bisherigen O3-Produktkanal auszuschließen. Denn O3d-I2 liefert für jedes `N>0`

\[
U^{-N}\chi^{R,-}_{T_0,U}\to\infty.
\]

Mit `N=M+1` folgt dann sogar

\[
\boxed{
\chi^{R,-}_{T_0,U_j}
\|\Theta^-_{T_0,U_j}\|
\to\infty.
}
\tag{O3f.8}
\]

Dies ist **nur eine konditionale Reduktion**. O3f beweist noch keinen polynomialen Lower-Bound für `nu_2` in der echten P11-Arithmetik.

Status:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3f]
&\quad \checkmark[M]_{\rm first\text{-}power\ range\ defect}\\
&+\checkmark[M]_{\rm exact\ second\text{-}moment\ variance}\\
&+\checkmark[M]_{\rm square\text{-}root\ block\ reduction}\\
&+\checkmark[M]_{\rm quantitative\ Theta\ lower\ bound}\\
&+\checkmark[M]_{\rm polynomial\ nu_2\ witness\ kills\ O3\ product\ route}\\
&+?[O]_{\nu_2\ \rm polynomial\ lower\ witness}\\
&+?[O]_{\Theta^-_{T_0,U}\to0}\\
&+?[O]_{\chi^{R,-}_{T_0,U}\|\Theta^-_{T_0,U}\|\to0}\\
&+?[O]_{W_{R,S,-}^{[T]}\ \rm strong\ Cauchy}.
\end{aligned}
}
\]

---

# 1. Verbindliche O3-Daten

Fixiere

\[
0<R<S<T_0<U.
\]

Alle Operatoren in diesem Knoten werden auf den odd Sektoren betrachtet.

Schreibe

\[
A_R:=A_{T_0,U}^{R,-},
\qquad
A_S:=A_{T_0,U}^{S,-},
\qquad
W:=W_{R,S,-}^{[T_0]}.
\]

O3/O2 liefern exakt

\[
\boxed{W^*W=I,}
\tag{O3f.9}
\]

\[
\boxed{W^*A_SW=A_R.}
\tag{O3f.10}
\]

Daher ist

\[
P:=WW^*
\]

der orthogonale Projektor auf die abgeschlossene Range

\[
\mathcal M:=\operatorname{Ran}W.
\]

Ferner definiert O3

\[
D:=W^*A_S^{1/2}W,
\]

\[
\mathscr J:=A_R^{1/2}-D\ge0,
\]

und

\[
\boxed{
\Theta
=A_R^{-1/4}\mathscr J A_R^{-1/4},
\qquad0\le\Theta\le I.
}
\tag{O3f.11}
\]

Aus Jensen folgt

\[
\boxed{0\le D\le A_R^{1/2}.}
\tag{O3f.12}
\]

Insbesondere

\[
\|D\|\le\sqrt{\|A_R\|}.
\tag{O3f.13}
\]

---

# 2. First-Power-Range-Defekt

Definiere

\[
\boxed{
\mathscr B:=(I-P)A_SW.
}
\tag{O3f.14}
\]

Da

\[
PA_SW
=WW^*A_SW
=W(W^*A_SW)
=WA_R,
\]

folgt sofort

\[
\boxed{
\mathscr B
=A_SW-WA_R.
}
\tag{O3f.15}
\]

Damit misst `mathscr B` exakt das Versagen des First-Power-Intertwinings

\[
A_SW=WA_R.
\]

Es gilt

\[
\boxed{
\mathscr B=0
\iff
A_S\mathcal M\subseteq\mathcal M.
}
\tag{O3f.16}
\]

Da `A_S` selbstadjungiert ist, ist Invarianz von `mathcal M` äquivalent dazu, dass `mathcal M` reduzierend für `A_S` ist.

Dann ist sie auch reduzierend für jede stetige Funktion von `A_S`, insbesondere für `A_S^{1/2}`. Damit ist die exakte Nullstruktur konsistent mit O3:

\[
\mathscr B=0
\Longrightarrow
(I-P)A_S^{1/2}W=0
\Longrightarrow
\Theta=0.
\]

**Firewall:** Diese Nulläquivalenz liefert noch keine quantitative asymptotische Relation für kleine, aber nichtverschwindende `mathscr B`.

Status:

\[
\boxed{\checkmark[M]_{\rm first\text{-}power\ range\ defect}.}
\]

---

# 3. Exakte Second-Moment-Kompressionsvarianz

Aus (O3f.14):

\[
\begin{aligned}
\mathscr B^*\mathscr B
&=W^*A_S(I-P)A_SW\\
&=W^*A_S^2W-W^*A_SPA_SW.
\end{aligned}
\]

Der zweite Term ist

\[
\begin{aligned}
W^*A_SPA_SW
&=W^*A_SWW^*A_SW\\
&=(W^*A_SW)^2\\
&=A_R^2.
\end{aligned}
\]

Daher exakt

\[
\boxed{
\mathscr B^*\mathscr B
=W^*A_S^2W-A_R^2.
}
\tag{O3f.17}
\]

Insbesondere

\[
\boxed{
\Delta_2
:=W^*A_S^2W-A_R^2
=\mathscr B^*\mathscr B
\ge0.
}
\tag{O3f.18}
\]

und

\[
\boxed{
\|\Delta_2\|
=\|\mathscr B\|^2.
}
\tag{O3f.19}
\]

Dies ist die exakte operatorielle Varianz der Kompression für die Funktion `x -> x^2`.

Sie enthält genau die Information, die in der bloßen First-Power-Kompression

\[
W^*A_SW=A_R
\]

fehlt: die Kopplung von `A_S` zwischen `mathcal M` und `mathcal M^perp`.

Status:

\[
\boxed{\checkmark[M]_{\rm exact\ second\text{-}moment\ variance}.}
\]

---

# 4. Quadratwurzel-Blockzerlegung

Setze

\[
S:=A_S^{1/2}.
\]

Relativ zur orthogonalen Zerlegung

\[
\mathcal K^-_{X,S}
=\mathcal M\oplus\mathcal M^\perp
\]

definiere

\[
\boxed{
L:=(I-P)SW,
}
\tag{O3f.20}
\]

\[
\boxed{
E:=(I-P)S(I-P)\big|_{\mathcal M^\perp}.
}
\tag{O3f.21}
\]

Dann ist `E>=0` und

\[
\|E\|\le\|S\|=\sqrt{\|A_S\|}.
\tag{O3f.22}
\]

Außerdem ist

\[
P SW=W D.
\tag{O3f.23}
\]

## 4.1 Identität für `L^*L`

Es gilt

\[
\begin{aligned}
L^*L
&=W^*S(I-P)SW\\
&=W^*S^2W-W^*SPSW\\
&=A_R-D^2.
\end{aligned}
\]

Also

\[
\boxed{
L^*L=A_R-D^2.
}
\tag{O3f.24}
\]

Mit

\[
\mathscr J=A_R^{1/2}-D
\]

folgt die nichtkommutative Faktorisierung

\[
\begin{aligned}
A_R-D^2
&=A_R^{1/2}\mathscr J+\mathscr J D.
\end{aligned}
\]

Daher

\[
\boxed{
L^*L
=A_R^{1/2}\mathscr J+\mathscr J D.
}
\tag{O3f.25}
\]

## 4.2 Identität für `mathscr B`

Weiter

\[
\begin{aligned}
\mathscr B
&=(I-P)S^2W\\
&=(I-P)SP SW+(I-P)S(I-P)SW\\
&=LD+EL.
\end{aligned}
\]

Somit

\[
\boxed{
\mathscr B=LD+EL.
}
\tag{O3f.26}
\]

Dies ist die exakte Sylvester-artige Brücke vom First-Power-Range-Defekt `mathscr B` zum Square-Root-Leakage `L`.

Status:

\[
\boxed{\checkmark[M]_{\rm square\text{-}root\ block\ reduction}.}
\]

---

# 5. Quantitative Lower-Bound-Brücke zu `Theta`

Aus (O3f.25):

\[
\begin{aligned}
\|L\|^2
&=\|L^*L\|\\
&\le
\bigl(\|A_R^{1/2}\|+\|D\|\bigr)\|\mathscr J\|\\
&\le
2\sqrt{\|A_R\|}\,\|\mathscr J\|.
\end{aligned}
\]

Also

\[
\boxed{
\|\mathscr J\|
\ge
\frac{\|L\|^2}{2\sqrt{\|A_R\|}}.
}
\tag{O3f.27}
\]

Andererseits folgt aus

\[
\mathscr J=A_R^{1/4}\Theta A_R^{1/4}
\]

die obere Abschätzung

\[
\|\mathscr J\|
\le
\sqrt{\|A_R\|}\,\|\Theta\|.
\tag{O3f.28}
\]

Kombiniert:

\[
\boxed{
\|\Theta\|
\ge
\frac{\|L\|^2}{2\|A_R\|}.
}
\tag{O3f.29}
\]

Nun liefert (O3f.26)

\[
\begin{aligned}
\|\mathscr B\|
&\le
(\|D\|+\|E\|)\|L\|\\
&\le
\bigl(
\sqrt{\|A_R\|}
+
\sqrt{\|A_S\|}
\bigr)\|L\|.
\end{aligned}
\]

Damit

\[
\boxed{
\|L\|
\ge
\frac{\|\mathscr B\|}
{\sqrt{\|A_R\|}+\sqrt{\|A_S\|}}.
}
\tag{O3f.30}
\]

Einsetzen in (O3f.29):

\[
\boxed{
\|\Theta\|
\ge
\frac{
\|\mathscr B\|^2
}{
2\,\|A_R\|\,
\bigl(\sqrt{\|A_R\|}+\sqrt{\|A_S\|}\bigr)^2
}.
}
\tag{O3f.31}
\]

Da `W` isometrisch ist,

\[
\|A_R\|
=\|W^*A_SW\|
\le\|A_S\|.
\]

Somit

\[
\bigl(\sqrt{\|A_R\|}+\sqrt{\|A_S\|}\bigr)^2
\le4\|A_S\|.
\]

Daher die gröbere Form

\[
\boxed{
\|\Theta\|
\ge
\frac{\|\mathscr B\|^2}
{8\,\|A_R\|\,\|A_S\|}.
}
\tag{O3f.32}
\]

Mit (O3f.19):

\[
\boxed{
\|\Theta\|
\ge
\frac{
\|W^*A_S^2W-A_R^2\|
}{
8\,\|A_R\|\,\|A_S\|}.
}
\tag{O3f.33}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm quantitative\ Theta\ lower\ bound}.}
\]

---

# 6. Dimensionsloser Second-Moment-Witness

Definiere

\[
\boxed{
\nu_{2;R,S}^{T_0,U}
:=
\frac{
\|W^*A_S^2W-A_R^2\|
}{
\|A_R\|\,\|A_S\|
}.
}
\tag{O3f.34}
\]

Dann folgt aus (O3f.33):

\[
\boxed{
\|\Theta^-_{T_0,U}\|
\ge
\frac18\nu_{2;R,S}^{T_0,U}.
}
\tag{O3f.35}
\]

Damit ist die Suche nach einem polynomialen Theta-Witness auf einen Second-Moment-Kompressionsdefekt reduziert.

### Konditionaler No-Go für den O3-Produktkanal

Angenommen, es existieren

- festes `M<infinity`,
- `c>0`,
- eine Folge `U_j -> infinity`,

so dass

\[
\boxed{
\nu_{2;R,S}^{T_0,U_j}
\ge
cU_j^{-M}.
}
\tag{O3f.36}
\]

Dann

\[
\|\Theta^-_{T_0,U_j}\|
\ge
\frac c8U_j^{-M}.
\tag{O3f.37}
\]

O3d-I2 liefert für `N=M+1`

\[
U^{-(M+1)}\chi^{R,-}_{T_0,U}	o\infty.
\]

Also

\[
\begin{aligned}
\chi^{R,-}_{T_0,U_j}
\|\Theta^-_{T_0,U_j}\|
&\ge
\frac c8
\chi^{R,-}_{T_0,U_j}U_j^{-M}\\
&=
\frac c8
U_j
\left(
U_j^{-(M+1)}
\chi^{R,-}_{T_0,U_j}
\right)\\
&\longrightarrow+\infty.
\end{aligned}
\]

Damit

\[
\boxed{
\text{(O3f.36)}
\Longrightarrow
\chi^{R,-}_{T_0,U_j}\|\Theta^-_{T_0,U_j}\|
\to\infty.
}
\tag{O3f.38}
\]

Insbesondere ist der O3-Suffizienzkanal

\[
\chi_-\|\Theta_-\|\to0
\]

dann ausgeschlossen.

**Firewall:** Das ist kein Transport-No-Go. O3/O3e haben nur einen hinreichenden Kanal untersucht. Das Scheitern dieses Produkts beweist nicht, dass `W_{R,S,-}^{[T]}` keinen starken Grenzwert besitzt.

Status:

\[
\boxed{\checkmark[M]_{\rm polynomial\ nu_2\ witness\ kills\ O3\ product\ route}.}
\]

---

# 7. Explizite Gramdarstellung des neuen Targets

Schreibe wieder den fixed-base-terminal Horizont `T_0` aus.

Nach O1/O2 gilt

\[
A_S
=
G_{S,T_0}^{-1/2}
G_{S,U}
G_{S,T_0}^{-1/2},
\]

und

\[
W
=
G_{S,T_0}^{1/2}
J_{R,S}
G_{R,T_0}^{-1/2}.
\]

Daher

\[
\begin{aligned}
A_SW
&=
G_{S,T_0}^{-1/2}
G_{S,U}
J_{R,S}
G_{R,T_0}^{-1/2}.
\end{aligned}
\tag{O3f.39}
\]

Ferner

\[
\boxed{
P=WW^*
=
G_{S,T_0}^{1/2}
J_{R,S}
G_{R,T_0}^{-1}
J_{R,S}^*
G_{S,T_0}^{1/2}.
}
\tag{O3f.40}
\]

Somit besitzt der First-Power-Range-Defekt die exakte rohe Darstellung

\[
\boxed{
\mathscr B
=(I-P)
G_{S,T_0}^{-1/2}
G_{S,U}
J_{R,S}
G_{R,T_0}^{-1/2}.
}
\tag{O3f.41}
\]

Dies ist der nächste arithmetische Primäraudit-Gegenstand.

Anders als `A_S^{1/2}` enthält (O3f.41) **keine bewegliche Operatorquadratwurzel des Future-Metrikquotienten**. Die Schwierigkeit sitzt stattdessen in der off-diagonalen Projektion der Future-Grammetrik gegen die feste `T_0`-alte Range.

Das ist konzeptionell günstiger, aber noch kein Estimate.

---

# 8. Firewalls

## O3f-FW1 — Kein tatsächlicher polynomialer Witness

O3f beweist

\[
\nu_2\gtrsim U^{-M}
\Longrightarrow
\text{O3-Produktkanal scheitert}.
\]

O3f beweist **nicht**

\[
\nu_2\gtrsim U^{-M}.
\]

Diese Aussage ist offen.

## O3f-FW2 — Kein Transport-No-Go

Auch

\[
\chi_-\|\Theta_-\|\not\to0
\]

würde nur den bisherigen hinreichenden O3-Kanal ausschließen.

Es folgt daraus nicht

\[
W_{R,S,-}^{[T]}
\text{ konvergiert nicht stark}.
\]

## O3f-FW3 — Second-Moment-Daten sind mehr als die O3e-First-Power-Kompression

O3e zeigte, dass

\[
W^*A_SW=A_R
\]

allein `Theta` nicht bestimmt.

O3f widerspricht dem nicht. Der neue Operator

\[
W^*A_S^2W-A_R^2
\]

enthält zusätzliche Information: exakt den quadratischen off-diagonalen Range-Defekt.

## O3f-FW4 — Fixed-base-terminal

Alle asymptotischen Konsequenzen dieses Knotens gelten für festes

\[
R<S<T_0
\]

und

\[
U\to\infty.
\]

Kein gemeinsamer `T_0,U -> infinity`-Limes wird behauptet.

## O3f-FW5 — Norm-Lower-Bound ist hinreichend für negativen Produktentscheid, nicht notwendig

Auch wenn `nu_2` keinen polynomialen Lower-Bound besitzt, könnte der O3-Produktkanal aus anderen Gründen scheitern.

Umgekehrt ist ein polynomialer `nu_2`-Witness nur ein besonders sauberer genügender negativer Mechanismus.

---

# 9. Nächster Primäraudit

Der nächste konkrete Audit ist nicht mehr

> Schätze `Theta` direkt.

Sondern:

> Untersuche den off-diagonalen Future-Gram-Defekt
> \[
> \mathscr B
> =(I-P)
> G_{S,T_0}^{-1/2}
> G_{S,U}
> J_{R,S}
> G_{R,T_0}^{-1/2}
> \]
> und entscheide, ob
> \[
> \nu_{2;R,S}^{T_0,U}
> =
> \frac{\|\mathscr B\|^2}
> {\|A_R\|\|A_S\|}
> \]
> einen polynomialen Lower-Witness besitzt.

Mögliche Angriffspunkte:

1. feste glatte odd Testvektoren mit niedrigem Boundary-Jet;
2. explizite Future-Prime-Edge-Vektoren aus C5c/O3d-I2;
3. Vergleich von `A_SWy` mit seiner Projektion `WA_Ry`;
4. ein einzelner normierter Rayleigh-/Singularwert-Witness für `mathscr B`;
5. falls nötig eine Schur-/PNT-Zerlegung von (O3f.41).

Bis ein solcher Witness oder ein gegenteiliger beyond-all-orders Upper-Bound vorliegt, bleibt

\[
?[O]_{\nu_2\ \rm polynomial\ lower\ witness}.
\]

---

# 10. Schlussurteil

Der Jensen-Gate ist nach O3e nicht mehr auf bloße First-Power-Kompression reduzierbar. O3f zeigt jedoch, dass man die bewegliche Quadratwurzel teilweise umgehen kann, wenn man **eine Stufe höher** in der Kompressionshierarchie geht:

\[
\boxed{
W^*A_S^2W-A_R^2
=
\mathscr B^*\mathscr B.
}
\]

Dieser Operator misst exakt, wie stark die zukünftige Metrik die alte Terminalrange auf First-Power-Ebene verlässt.

Quantitativ gilt

\[
\boxed{
\|\Theta^-_{T_0,U}\|
\ge
\frac18
\frac{
\|W^*A_S^2W-A_R^2\|
}{
\|A_R\|\|A_S\|
}.
}
\]

Damit ist der nächste Entscheidungsmechanismus sehr konkret:

\[
\boxed{
\text{polynomialer normalisierter Second-Moment-Defekt}
\Longrightarrow
\text{O3-Produktkanal scheitert}.
}
\]

Ob dieser Defekt in der echten P11-Arithmetik polynomial groß ist, ist der neue offene Primäraudit.