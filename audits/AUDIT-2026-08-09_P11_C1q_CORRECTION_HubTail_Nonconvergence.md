# P11-C1q — Targeted Correction: Haar-Quotient beseitigt Restsektor, aber nicht den globalen Hubtail

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1q-CORR]`  
**Bezug:** `AUDIT-2026-08-09_P11_C1q_HaarMeanZero_Quotient_LabelCollapse.md`, insbesondere §7  
**Status:**

\[
\boxed{[P11\text{-}C1q\text{-}CORR]\quad\checkmark[M]_{\rm corr}}
\]

## 0. Korrektur in einem Satz

Die strukturellen C1q-Befunde zum Haar-Mittelnullquotienten bleiben gültig:

- `P_0` vernichtet exakt die primspezifischen Restsektoren `K_p^0`;
- der Labelgram kollabiert auf Rang eins;
- `P_0\zeta_{p^k}=p^{-k/2}\zeta_1`;
- die Prime-Power-Markierungen gehen verloren.

**Korrigiert wird ausschließlich die Konvergenzbehauptung aus C1q §7.**

Nach dem Rang-eins-Kollaps liegen die quotientierten Primebeiträge alle im selben neutralen Hub `\mathbb C\zeta_1`. Die Koeffizienten für `k=1` sind

\[
c_p=\sqrt{\log p}\,p^{-3/4}.
\]

Quadratsummierbarkeit

\[
\sum_p c_p^2=\sum_p\frac{\log p}{p^{3/2}}<\infty
\]

genügt hier **nicht**, weil die analytischen Vektoren `D_{\log p}a` nicht orthogonal sind und die finite-adischen Labelvektoren nach Quotientierung identisch sind.

Die direkte quotientierte Hub-Synthese ist im Allgemeinen nicht Hilbertnorm-konvergent.

---

## 1. Der betroffene Hubtail

Für den primitiven `k=1`-Teil lautet die quotientierte Synthese

\[
H_Xa
:=
\sum_{p\le X}
\sqrt{\log p}\,p^{-3/4}
D_{\log p}a\otimes\zeta_1.
\]

Da `\|\zeta_1\|=1`, reduziert sich die Konvergenzfrage auf

\[
\sum_p c_pD_{\log p}a
\quad\text{in }L^2(\mathbb R).
\]

---

## 2. Block-Untergrenze

Wähle

\[
0\le a\in C_c^\infty(\mathbb R),
\qquad
 a(u)\ge1\quad(|u|\le\delta)
\]

für ein `\delta>0`.

Wir verwenden die P11-Konvention

\[
D_s=U_{s/2}-U_{-s/2}.
\]

Wähle `\varepsilon>0` so klein, dass

\[
\frac12\log(1+\varepsilon)<\delta.
\]

Betrachte den Primblock

\[
\mathcal P_X:=\{p:\ X\le p\le(1+\varepsilon)X\}.
\]

Die positiven Translationszentren `\frac12\log p` variieren über ein Intervall der Länge

\[
\frac12\log(1+\varepsilon)<\delta.
\]

Daher besitzen die verschobenen Plateaus

\[
U_{\frac12\log p}a,
\qquad p\in\mathcal P_X,
\]

für alle großen `X` ein gemeinsames Intervall `I_X` von Länge mindestens einer festen Konstanten `c_\delta>0`, auf dem jeder dieser Summanden mindestens `1` ist.

Auf demselben positiven Tail liegen die Gegenstücke `U_{-\frac12\log p}a` für großes `X` vollständig außerhalb des Trägers. Somit gilt auf `I_X`

\[
\left|
\sum_{p\in\mathcal P_X}c_pD_{\log p}a
\right|
\ge
\sum_{p\in\mathcal P_X}c_p.
\]

Folglich

\[
\left\|
\sum_{p\in\mathcal P_X}c_pD_{\log p}a
\right\|_2
\ge
c_\delta^{1/2}
\sum_{p\in\mathcal P_X}c_p.
\]

---

## 3. Primzahlsatz liefert unbeschränkte Blocknormen

Für `p\in[X,(1+\varepsilon)X]` gilt

\[
c_p\asymp \sqrt{\log X}\,X^{-3/4}.
\]

Mit dem Primzahlsatz

\[
\#\mathcal P_X\asymp_\varepsilon \frac{X}{\log X}
\]

folgt

\[
\sum_{p\in\mathcal P_X}c_p
\gtrsim_\varepsilon
\frac{X}{\log X}
\sqrt{\log X}\,X^{-3/4}
=
\frac{X^{1/4}}{\sqrt{\log X}}
\longrightarrow\infty.
\]

Damit

\[
\boxed{
\left\|
\sum_{p\in\mathcal P_X}c_pD_{\log p}a
\right\|_2
\longrightarrow\infty.}
\]

Die Partialsummen sind also nicht Cauchy.

Status: `✓[M]`.

---

## 4. Warum C1p diese Stelle nicht repariert

C1p behandelt die **P02-Momentensynthese**. Dort tritt vor dem Label bereits der zusätzliche Momentfaktor `n^{-1/2}` auf. Nach anschließender Hubprojektion besitzt der primitive Hubkoeffizient die stärkere Größenordnung

\[
\sqrt{\log p}\,p^{-5/4},
\]

und ist absolut summierbar.

C1q projiziert dagegen die **ungedämpfte Weil-Inzidenzsynthese** direkt auf den Hub. Dort entsteht nur

\[
\sqrt{\log p}\,p^{-3/4}.
\]

Daher darf die C1p-Hubkonvergenz nicht auf C1q übertragen werden.

---

## 5. Revidierter C1q-Endstand

| Aussage | korrigierter Status |
|---|---|
| `P_0` vernichtet `\oplus_pK_p^0` | `✓[K/M]` |
| quotientierter Labelgram hat Rang eins | `✓[M]` |
| Prime-Power-Markierungen kollabieren | `✓[M]` |
| diagonaler Einzelkanalfaktor wird `\log p/p^{3k/2}` | `✓[M]` |
| daraus folgt globale Hilbertnormkonvergenz der Hub-Synthese | `×[M]` |
| C1q §7 Konvergenzargument | `SUPERSEDED` durch diesen Audit |
| Haarquotient ist geeigneter finaler Objekt-X-Quotient | weiterhin `×[M]` |

Die Formulierung „Haarquotient kontrolliert die C1o-Divergenz“ ist künftig nur noch in folgendem engen Sinn zulässig:

\[
\boxed{
P_0\text{ entfernt die orthogonale primspezifische Restdivergenz,}
\text{ aber nicht die globale aligned-Hub-Divergenz}.}
\]

---

## 6. Konsequenz für C1z-B

Eine finite-adische Konditionierung vor Haar darf nicht nur die Restsektoren auf den Hub drücken. Andernfalls wird die Orthogonaldivergenz lediglich in einen nichtorthogonalen Hubtail verlagert.

Der nächste zulässige Test ist daher eine **source-gekoppelte p-adische Martingalkonditionierung**, die

1. die aktiven BC-Marken dort erhält, wo die Weil-Korrelation tatsächlich lebt;
2. die mittelfreien Martingalstufen außerhalb dieses Überlappungsbereichs konditioniert;
3. den neutralen Hub anschließend separat relativ/Feshbach-artig behandelt.

Dieser Test wird in P11-C1z-B durchgeführt.
