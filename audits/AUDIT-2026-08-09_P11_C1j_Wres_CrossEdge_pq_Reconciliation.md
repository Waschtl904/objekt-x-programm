# P11-C1j — Wres-Kreuzkantenpaarung im Minimalfall `pq`: Reconciliation mit dem Mangoldt-Träger

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1j]`  
**Vorgänger:** P11-C1i  
**Primärquellen:** NEU-044-x3, NEU-228b, NEU-229, NEU-250j, eingefrorenes P05  

**Urteil:**

\[
\boxed{[P11-C1j]\quad\checkmark[M]_{\rm part}}
\]

Der Minimalfall

\[
E_{r;q\xrightarrow p pq},
\qquad
E_{r';p\xrightarrow q pq}
\]

zeigt tatsächlich eine mögliche nichtverschwindende **Pullback-`Wres`-Überlappung** nach Kollaps auf denselben Zielsektor `V_{pq}`. Dieser Mechanismus ist jedoch **nicht** der gesuchte kanonische Prime-Power-Labelkern:

1. der Pullback verliert die Kantenmarkierung und macht den relativen Primclock auf dem kollabierten Ziel nicht funktoriell wohldefiniert;
2. die kantendiagonale relative Hebung erhält die Markierung, setzt aber Kreuzprimkanten definitorisch orthogonal;
3. der gemeinsame Zielindex `pq` liegt auf dem Mischträger `\Lambda(pq)=0`, nicht auf dem Weil-Prime-Power-Träger;
4. spätere Knoten liefern keinen kanonischen Mediator vom Prime-Power-Träger in diesen Mischsektor.

Damit ist die `pq`-Kollision ein echter Nachweis möglicher nichtorthogonaler **Geometrie**, aber kein direkter Ursprung der gesuchten Weil-gewichteten Kreuzprimkopplung.

---

## 1. Der Minimaltest

Betrachte für `p\neq q`

\[
e_{p|pq}:=E_{r;q\xrightarrow p pq},
\qquad
e_{q|pq}:=E_{r';p\xrightarrow q pq}.
\]

Unter der Kollapsabbildung

\[
\kappa(E_{r;m\xrightarrow p pm})=E_{r,pm}
\]

gilt

\[
\kappa(e_{p|pq})=E_{r,pq},
\qquad
\kappa(e_{q|pq})=E_{r',pq}.
\]

Die Markierungen `p` und `q` sind nach `\kappa` nicht mehr vorhanden.

Status: `✓[M]`.

---

## 2. Variante A: Pullback-`Wres` ist nicht kantendiagonal

NEU-044-x3 definiert

\[
\langle x,y\rangle_\kappa
:=
\langle\kappa x,\kappa y\rangle_{Wres}.
\]

Im Minimalfall:

\[
\boxed{
\langle e_{p|pq},e_{q|pq}\rangle_\kappa
=
\langle E_{r,pq},E_{r',pq}\rangle_{Wres}.
}
\]

Die rechte Seite enthält keinen Kantenfaktor `\delta_{p,q}^{edge}`. Unter der dort vorausgesetzten nichtausgearteten Zielpaarung ist der Ausdruck im Allgemeinen nicht null.

Damit:

\[
\boxed{
\text{Pullback-}Wres\text{ kann echte Kreuzprimüberlappung erzeugen.}
}
\]

Status: `✓[M]` im exakt dort formulierten Pullback-Scope.

---

## 3. Aber: derselbe Pullback zerstört die Clock-Funktorialität

Auf den markierten Kanten gilt

\[
T_{rel}e_{p|pq}=\log p\,e_{p|pq},
\qquad
T_{rel}e_{q|pq}=\log q\,e_{q|pq}.
\]

Nach Kollaps werden beide jedoch auf denselben Zielsektor `V_{pq}` abgebildet. Ein Operator auf dem kollabierten Ziel müsste demselben Zielvektor zugleich `\log p` und `\log q` zuweisen.

Für `p\neq q` ist das unmöglich.

\[
\boxed{
\text{Nichtorthogonaler Pullback-Kollaps}
\Longrightarrow
\text{Verlust des funktoriellen relativen Primclocks.}
}
\]

Status: `✓[M]`.

Damit kann der bloße Kollaps nicht zugleich

- die Primmarkierung vergessen,
- echte Kreuzüberlappung erzeugen,
- und den markierungsabhängigen Clockoperator erhalten.

---

## 4. Variante B: kantendiagonale relative Hebung

NEU-044-x3 führt alternativ die definitorische Paarung

\[
\boxed{
\left\langle
E_{r;m\xrightarrow p pm},
E_{r';m'\xrightarrow q qm'}
\right\rangle_{Wres,rel}
:=
\delta_{p,q}\delta_{m,m'}
\langle E_{r,pm},E_{r',pm}\rangle_{Wres}.
}
\]

Diese erhält die Kantenmarkierung und macht `T_{rel}` wohldefiniert.

Für `p\neq q` gilt aber sofort

\[
\boxed{
\langle e_{p|pq},e_{q|pq}\rangle_{Wres,rel}=0.
}
\]

Ihre Intrinsizität aus `Wres_{BC}^{top}` blieb bereits in NEU-044-x3 OPEN.

Status:

- Kantendiagonalität: `✓[M]` als Definition;
- intrinsische Herleitung: `?[O]`.

---

## 5. Das Dilemma ist strukturell, nicht nur notational

Die beiden historischen Varianten realisieren entgegengesetzte Vorteile:

| Paarung | Kreuzprimüberlappung | Kantenmarkierung / Clock | Intrinsizität |
|---|---:|---:|---:|
| Pullback `\kappa^*Wres` | generisch möglich | verliert sie | aus Kollaps definiert |
| kantendiagonales `Wres_rel` | nein | erhält sie | `?[O]` |

Damit liefert NEU-044-x3 **keine** einzelne Paarung, die bereits alle P11-Anforderungen erfüllt.

---

## 6. Spätere Gramfaseranalyse verschärft die Quellenfrage

NEU-228b/229 analysieren eine intrinsische verbundene Form auf Liftfasern. Der entscheidende Befund ist:

- positive Kernblöcke lassen sich formtheoretisch typisieren;
- ein nichttrivialer Mischblock benötigt ein intrinsisches lineares Funktional / einen kontraktiven Riesz-Vektor;
- aus dem damals gelesenen Quellenbestand ist dieser Mischblock nicht konstruiert;
- der Befund ist ein **Quellen-No-Go**, kein Existenz-No-Go gegen jeden möglichen Mischblock.

Für P11 bedeutet das:

\[
\boxed{
\text{Nichtorthogonalität im kollabierten Ziel ersetzt nicht die fehlende intrinsische globale Mischstruktur.}
}
\]

---

## 7. NEU-250j: Trägertrennung

Für eine Kreuzprimkollision

\[
pm_p=qm_q=M,
\qquad p\neq q,
\]

muss `M` mindestens zwei verschiedene Primteiler besitzen. Daher

\[
\omega(M)\ge2
\quad\Longrightarrow\quad
\Lambda(M)=0.
\]

Somit

\[
\boxed{
\operatorname{supp}\Lambda
\cap
\operatorname{supp}(\text{Kreuzprimkollision})
=\varnothing.
}
\]

Insbesondere:

\[
\Lambda(pq)=0.
\]

Der Minimaltest `pq` lebt also gerade **nicht** auf einem Prime-Power-Sektor mit diagonalem Weilgewicht.

Status: `✓[M]`.

---

## 8. Prime-Power-Träger versus Mischträger

Definiere

\[
\mathcal P^*:=\{p^k:p\text{ prim},k\ge1\},
\]

und

\[
\mathcal M:=\{M:\omega(M)\ge2\}.
\]

Dann

\[
\mathbb N_{\ge2}=\mathcal P^*\sqcup\mathcal M,
\]

mit

\[
\Lambda|_{\mathcal P^*}\neq0,
\qquad
\Lambda|_{\mathcal M}=0.
\]

Die direkte `pq`-Kollisionsgeometrie lebt in `\mathcal M`, während die diagonalen Weilkoeffizienten in `\mathcal P^*` leben.

\[
\boxed{
\text{lokale Weilgewichte und direkte Kreuzprimkollision liegen auf disjunkten Trägern.}
}
\]

---

## 9. Dynamik vermittelt derzeit nicht zwischen den Trägern

NEU-250j hält bindend fest: Die damals vorhandene `\Theta/D_{rel}`-Dynamik erhält Primkanal/Faser und liefert keinen konstruierten Transfer

\[
\mathcal H_{\mathcal P^*}
\longrightarrow
\mathcal H_{\mathcal M}.
\]

Damit folgt aus einem nichttrivialen Kreuzblock im Mischsektor nicht automatisch ein Kreuzblock auf dem Weil-Prime-Power-Träger.

\[
\boxed{
K_{pq}\neq0\text{ im gesamten Graphraum}
\not\Rightarrow
K_{pq}\neq0\text{ auf }\mathcal H_{\mathcal P^*}.
}
\]

Status: `✓[M]`.

---

## 10. Reconciliation mit P11-C1i

C1i liefert für jedes Prime-Power-Label `(p,k)` einen typkorrekten lokalen Kettenzustand

\[
\eta_{p,k}=p^{-k/4}\chi_{p,k}
\]

mit

\[
\langle\eta_{p,k},T_{rel}\eta_{p,k}\rangle
=\frac{\log p}{p^{k/2}}.
\]

Für verschiedene Primlabels sind diese Zustände im rohen markierten Graphraum orthogonal.

C1j zeigt:

- nach Kollaps kann Nichtorthogonalität entstehen;
- aber dann geht genau die Markierungsinformation verloren, die die Prime-Clock-Energie unterscheidet;
- außerdem liegt der gemeinsame Kollisionssektor außerhalb des Mangoldt-Trägers.

Daher kann der C1i-Kettenlift nicht durch bloßen `Wres`-Kollaps zu `C_R^{can}` erweitert werden.

---

## 11. Was der `pq`-Test dennoch positiv liefert

Der negative Direktweg enthält eine wichtige konstruktive Information:

\[
\boxed{
\mathcal M\text{ ist ein natürlicher Kandidat für einen reinen Mediatorraum.}
}
\]

Er muss selbst kein diagonales Mangoldtgewicht tragen. Eine hypothetische Architektur könnte vielmehr

\[
\mathcal H_{\mathcal P^*}
\stackrel{F}{\longrightarrow}
\mathcal H_{\mathcal M}
\stackrel{F^*}{\longrightarrow}
\mathcal H_{\mathcal P^*}
\]

verwenden, so dass die Mischsektoren ausschließlich Off-Diagonalgeometrie vermitteln.

NEU-250j nennt genau diesen Mediatorweg als offen und nicht widerlegt.

**Firewall:** Ein kanonischer Operator `F` ist im bisher gelesenen Quellenbestand nicht konstruiert.

---

## 12. Abstrakter positiver Mediator-Gramkern

Falls künftig ein kanonischer Operator

\[
F_R:
\bigoplus_{\alpha\in F_R}\mathcal K_\alpha
\longrightarrow
\mathcal H_{\mathcal M,R}
\]

konstruiert wird, ist

\[
\boxed{C_R^{med}:=F_R^*F_R\ge0}
\]

automatisch ein positiver Label-Gramoperator.

Seine Kreuzblöcke wären

\[
(C_R^{med})_{\alpha\beta}=F_\alpha^*F_\beta.
\]

Damit passt der Mediatorweg exakt zum C1g-Schema einer positiven Labelgeometrie.

Dies ist nur ein abstraktes Faktorisierungslemma; Existenz und Kanonizität von `F_R` bleiben `?[O]`.

---

## 13. Statusmatrix

| Aussage | Status |
|---|---|
| Pullback-`Wres` im `pq`-Minimalfall kann kreuzprim-nichtorthogonal sein | `✓[M]` im NEU-044-Scope |
| Pullback erhält relative Clockmarkierung | `×[M]` |
| kantendiagonales `Wres_rel` erhält Clock | `✓[M]` als Definition |
| kantendiagonales `Wres_rel` besitzt Kreuzprimblock | `×[M]` |
| Intrinsizität der kantendiagonalen Hebung | `?[O]` |
| `pq`-Kollisionssektor trägt Mangoldtgewicht | `×[M]`; `\Lambda(pq)=0` |
| direkte Graphkollision liefert `C_R^{can}` auf Prime-Power-Labels | `×[M]` |
| vorhandene `Theta/D_rel`-Dynamik vermittelt `P* -> M` | `×[M]` im NEU-250j-Scope |
| Mischsektor als möglicher Mediatorraum | `?[O]` |
| `C_R^{med}=F_R^*F_R` wäre bei kanonischem `F_R` PSD | `✓[M]` abstrakt |
| kanonischer Mediatoroperator `F_R` | `?[O]` |

---

## 14. Endurteil

Der historische `pq`-Test ist für P11 wichtiger als ein bloßes „Kreuzblock ja/nein“:

\[
\boxed{
\text{Er zeigt, dass Nichtorthogonalität beim Vergessen der Markierung entsteht,}
\text{ während die lokale Arithmetik gerade die Markierung benötigt.}
}
\]

Die gesuchte Objekt-X-Geometrie muss daher beides gleichzeitig leisten:

1. Prime-Power-/Primmarkierung erhalten;
2. dennoch einen kanonischen gemeinsamen Überlappungsmechanismus zulassen.

Der rohe Kollaps erfüllt nur Punkt 2; die kantendiagonale Graphhebung nur Punkt 1.

---

## 15. Nächster Knoten

\[
\boxed{[P11\text{-}C1k]\quad\text{Mediator-Audit: existiert aus BC-/adelischer Multiplikation ein kanonischer }\mathcal P^*\to\mathcal M\text{-Operator?}}
\]

Zu prüfen ist gezielt, ob die Multiplikations-/Semigruppenstruktur bereits eine source-defined Abbildung vom Prime-Power-Sektor in gemischt zusammengesetzte Sektoren liefert, deren adjungierte Rückkopplung einen positiven Label-Gramkern erzeugt — ohne die `\Lambda=0`-Mediatorzustände als zusätzliche diagonale Weilkoeffizienten zu zählen.
