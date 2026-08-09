# P11-C1e — Endliche Weil-Trunkierungen sind indefinit: Defekt-/Kontraktionsproblem

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1e]`  
**Vorgänger:** P11-C1d  
**Primärbasis:** P11-C1d, NEU-220c, P02  

**Urteil:**

\[
\boxed{[P11-C1e]\quad\checkmark[M]_{\rm neg}\;\text{für Positivität der wörtlichen endlichen Weil-Trunkierung auf dem vollen Testkern}.}
\]

Jede endliche Prime-Power-Trunkierung der exakt geschriebenen Weilform besitzt bereits im Gamma+Prim-Multiplikatorteil einen unendlichen negativen Index. Der Rang-2-Polterm kann diesen nicht beseitigen. Daher kann ein endliches positives Objekt-X-Grammodell **nicht** einfach mit der wörtlich prime-getrunkerten Weilform identifiziert werden.

Dies ist kein No-Go gegen positive **andere** endliche Grammodelle mit Restterm/Kompression und kein No-Go gegen die globale Objekt-X-Architektur.

---

## 1. Endliche Prime-Power-Trunkierung

Sei `F` eine endliche Menge von Prime-Power-Labels

\[
\alpha=(p,m),
\qquad
\ell_\alpha=m\log p,
\qquad
w_\alpha=\frac{\log p}{p^{m/2}}>0.
\]

Setze

\[
W_F:=\sum_{\alpha\in F}w_\alpha.
\]

Die prime-getrunkerte Form lautet

\[
B_W^F
:=
B_\Gamma+B_{\rm pole}+B_{\rm fin}^F,
\]

mit

\[
B_{\rm fin}^F(a,b)
=-2\sum_{\alpha\in F}w_\alpha g_{a,b}(\ell_\alpha).
\]

---

## 2. Spektraler Multiplikator von Gamma + endlichen Primdaten

Aus P11-C1d bzw. direkt aus P02 folgt für den Diagonalwert

\[
B_\Gamma(a,a)+B_{\rm fin}^F(a,a)
=
\frac1{2\pi}\int_{\mathbb R}
M_F(t)|\widehat a(t)|^2\,dt,
\]

mit

\[
\boxed{
M_F(t)
:=
A_\infty(t)
-2\sum_{\alpha\in F}w_\alpha\cos(t\ell_\alpha).
}
\]

Da `A_\infty` und die Kosinusterme stetig und gerade sind, ist `M_F` stetig und gerade.

Am Ursprung:

\[
\boxed{
M_F(0)
=A_\infty(0)-2W_F.
}
\]

NEU-220c liefert

\[
A_\infty(0)
\approx-5.37218341922566558<0.
\]

Da `W_F\ge0`:

\[
\boxed{M_F(0)<0}
\]

für **jede** endliche Trunkierung `F`, einschließlich `F=\varnothing`.

---

## 3. Negatives Frequenzintervall

Aus der Stetigkeit folgt: Es existieren

\[
\delta_F>0,
\qquad
c_F>0
\]

mit

\[
M_F(t)\le-c_F
\qquad(|t|<\delta_F).
\]

Wähle beliebig viele linear unabhängige

\[
\varphi_1,\ldots,\varphi_N
\in C_c^\infty((-\delta_F,\delta_F))
\]

und setze

\[
a_j=\mathcal F^{-1}\varphi_j\in\mathcal S(\mathbb R).
\]

Für jede nichttriviale Linearkombination `a` gilt

\[
(B_\Gamma+B_{\rm fin}^F)(a,a)
\le
-\frac{c_F}{2\pi}
\int|\widehat a(t)|^2dt
<0.
\]

Somit

\[
\boxed{
\operatorname{ind}_-(B_\Gamma+B_{\rm fin}^F)=\infty
}
\]

auf der Schwartz-Ebene.

Status: `✓[M]`.

---

## 4. Der Polterm kann den negativen Index nicht schließen

NEU-220c/P11-C1d zeigen

\[
\operatorname{rank}B_{\rm pole}\le2.
\]

Ein endlich-rangiger hermitescher Zusatz kann einen unendlichen negativen Index nicht beseitigen. Konkret: Aus einem negativ definiten Unterraum beliebig großer Dimension kann man einen beliebig großen Unterraum im Kern der beiden Randfunktionale

\[
a\mapsto\widehat a(i/2),
\qquad
a\mapsto\widehat a(-i/2)
\]

wählen. Dort verschwindet `B_{\rm pole}`.

Daher

\[
\boxed{
\operatorname{ind}_-(B_W^F)=\infty.
}
\]

Der NEU-220c-Abschneide-/Gram-Matrix-Transfer überträgt den Befund auch auf `C_c^\infty(\mathbb R)`.

Status: `✓[M]_{neg}`.

---

## 5. Konsequenz für endliche Objekt-X-Modelle

Ausgeschlossen ist die Identifikation

\[
\boxed{
\text{positives endliches Grammodell}
\equiv
B_W^F\text{ auf dem gesamten Testkern}.
}
\]

Damit ist eine alte naheliegende Lesart von OX-Z2 gesperrt.

Zulässig bleiben insbesondere:

1. eine **andere** positive Form `G_F` mit kontrolliertem Rest
   \[
   G_F=B_W^F+R_F;
   \]
2. eine positive Form auf einem kanonischen echten gemeinsamen Quellenbild/Graphen statt auf freien Koordinaten;
3. eine größere positive Quellenarchitektur, deren Kompression erst nach nichtorthogonaler Kopplung die gewünschte Weilform bzw. einen kontrollierten Näherungsblock erzeugt;
4. renormierte/defektkontrollierte Grenzmodelle, sofern ihr Operator-/Formgrenzwert tatsächlich bewiesen wird.

---

## 6. Exakte Defektfaktorisierung aus C1d

P11-C1d liefert für endliches `F`

\[
\begin{aligned}
B_W^F(a,b)
={}&
\mathcal E_\infty(a,b)
+\mathcal E_F(a,b)
+P_+(a)\overline{P_+(b)}\\
&-
\Bigl[
(2W_F-A_\infty(0))\langle a,b\rangle
+P_-(a)\overline{P_-(b)}
\Bigr].
\end{aligned}
\]

Definiere den positiven Analyseoperator formal durch

\[
\mathcal A_Fa
:=
\left(
[s\mapsto\sqrt{\omega_\infty(s)}D_sa],
(\sqrt{w_\alpha}D_{\ell_\alpha}a)_{\alpha\in F},
P_+(a)
\right)
\]

in

\[
\mathcal H_{+,F}
:=
L^2((0,\infty),ds;L^2(\mathbb R))
\oplus
\bigoplus_{\alpha\in F}L^2(\mathbb R)
\oplus\mathbb C,
\]

wobei die erste Komponente bereits die Gewichtung `\omega_\infty` enthält.

Definiere den Defektoperator

\[
\boxed{
\mathcal C_Fa
:=
\left(
\sqrt{2W_F-A_\infty(0)}\,a,
P_-(a)
\right)
}
\]

in

\[
\mathcal H_{-,F}:=L^2(\mathbb R)\oplus\mathbb C.
\]

Dann gilt exakt

\[
\boxed{
B_W^F(a,b)
=
\langle\mathcal A_Fa,\mathcal A_Fb\rangle_{+,F}
-
\langle\mathcal C_Fa,\mathcal C_Fb\rangle_{-,F}.
}
\]

Dies ist eine kanonische finite Krein-/Defektfaktorisierung, keine positive Gramrealisierung.

---

## 7. Kontraktionslemma

Für einen beliebigen Unterraum `\mathscr D\subset\mathcal A_{PW}` gilt:

\[
B_W^F(a,a)\ge0
\quad\forall a\in\mathscr D
\]

ist äquivalent zu

\[
\|\mathcal C_Fa\|
\le
\|\mathcal A_Fa\|
\quad\forall a\in\mathscr D.
\]

Falls diese Ungleichung gilt, definiert

\[
K_F(\mathcal A_Fa):=\mathcal C_Fa
\]

auf `\mathcal A_F(\mathscr D)` einen wohldefinierten Kontraktor: Ist `\mathcal A_Fa=0`, folgt aus der Ungleichung `\mathcal C_Fa=0`; außerdem

\[
\|K_F\mathcal A_Fa\|
\le\|\mathcal A_Fa\|.
\]

Er setzt sich stetig auf den Abschluss des positiven Quellenbildes fort.

Umgekehrt impliziert eine Faktorisierung

\[
\boxed{
\mathcal C_F=K_F\mathcal A_F,
\qquad\|K_F\|\le1,
}
\]

sofort `B_W^F\ge0` auf `\mathscr D`.

Damit ist das Positivitätsproblem äquivalent zu einem **source-induced contractive factorization problem**.

Status: `✓[M]` als abstraktes Lemma.

---

## 8. Negatives Resultat auf dem vollen Testkern

Aus §4 folgt, dass `B_W^F` auf `\mathcal A_{PW}` unendlichen negativen Index besitzt. Daher existiert **kein** Kontraktor

\[
K_F:\overline{\mathcal A_F(\mathcal A_{PW})}\to\mathcal H_{-,F}
\]

mit

\[
\mathcal C_F=K_F\mathcal A_F
\]

auf dem gesamten Testkern.

\[
\boxed{
\text{Die in C1d vorgeschlagene full-source Poincaré-/Frame-Ungleichung ist für jedes endliche }F\text{ falsch.}
}
\]

Das ist stärker als „noch unbewiesen“.

---

## 9. Was P11 nun wirklich suchen muss

Der Defekt kann nicht auf dem **vollen endlichen Testkern** durch die vorhandenen Diagonal-Inzidenzenergien kontrolliert werden.

Daher muss mindestens eine der folgenden Strukturen hinzukommen:

### A. Kanonischer echter Quellenunterraum / Graph

Eine arithmetisch definierte Relation beschränkt die unabhängig möglichen Analyse-/Defektkoordinaten.

### B. Nichtorthogonale Erweiterung der positiven Analysegeometrie

Die latenten Kreuzblöcke

\[
G_{s,t}(a,b)=\langle D_sa,D_tb\rangle,
\qquad s\ne t,
\]

werden durch eine **kanonische** globale Synthese-/Korrespondenzstruktur aktiviert, ohne als zusätzlicher Weil-Summand addiert zu werden.

### C. Positive Approximation mit echtem Restterm

Ein positives Grammodell `\mathfrak G_F` erfüllt nicht `\mathfrak G_F=B_W^F`, sondern

\[
\mathfrak G_F=B_W+R_F
\quad\text{oder eine präzise cutoff-kompatible Variante},
\]

mit separat bewiesenem Grenzverhalten des Restterms.

Diese drei Möglichkeiten sind nicht exklusiv.

---

## 10. Reconciliation mit NEU-230 und NEU-250

NEU-230 verlangte endliche positive Grammodelle vor dem Grenzübergang. C1e präzisiert:

\[
\boxed{
\text{Solche positiven Modelle können nicht die bloßen wörtlichen Prime-Trunkierungen }B_W^F\text{ sein.}
}
\]

NEU-250 verlangte bereits ein gemeinsames Quellenbild und verbot eine positive freie Vollblockmatrix. C1e bestätigt diese Notwendigkeit nun in der neuen gemeinsamen Inzidenzsprache.

---

## 11. Statusmatrix

| Aussage | Status |
|---|---|
| `M_F(t)=A_\infty(t)-2\sum_{\alpha\in F}w_\alpha\cos(t\ell_\alpha)` | `✓[M]` |
| `M_F(0)=A_\infty(0)-2W_F<0` | `✓[M]` |
| unendlicher negativer Index von `B_\Gamma+B_{fin}^F` | `✓[M]_{neg}` |
| Polterm beseitigt diesen Index | `×[M]` |
| `B_W^F\ge0` auf vollem `\mathcal A_{PW}` | `×[M]` |
| finite positive Grammodelle identisch mit wörtlichem `B_W^F` | `×[M]` |
| Defektfaktorisierung `B_W^F=||A_F\cdot||^2-||C_F\cdot||^2` | `✓[K/M]` |
| Kontraktionskriterium auf einem gegebenen Unterraum | `✓[M]` |
| full-source Kontraktor für endliches `F` | `×[M]` |
| kanonischer echter Quellenunterraum/Graph | `?[O]` |
| kanonische Nutzung latenter Off-Diagonal-Gramblöcke | `?[O]` |
| positive Modelle mit kontrolliertem Restterm | `?[O]` |

---

## 12. Wichtigster Befund

C1c/C1d lieferten erstmals eine konkrete gemeinsame Inzidenzgeometrie.

C1e zeigt nun ebenso klar, **wo deren bloße Diagonalenergie nicht reicht**:

\[
\boxed{
\text{Die fehlende Objekt-X-Struktur muss echte globale Quellenabhängigkeit bzw. nichtorthogonale Kopplung enthalten.}
}
\]

Nicht weil „Off-Diagonalität schön wäre“, sondern weil die wörtlichen endlichen Diagonal-/Trunkierungsmodelle mathematisch unendlich viele negative Richtungen behalten.

---

## 13. Nächster Knoten

\[
\boxed{[P11\text{-}C1f]\quad\text{Kanonische Synthese des latenten Kanten-Gramkerns }G_{s,t}.}
\]

Zu prüfen ist, ob aus der gemeinsamen adelischen Quelle oder der relativen Primkantenkorrespondenz ein **nicht frei wählbarer** Syntheseoperator auf der Kantenlängenachse entsteht, dessen Gramoperator Off-Diagonalwerte `G_{s,t}` aktiviert und dessen Kompression mit der exakten Weilform kompatibel bleibt.
