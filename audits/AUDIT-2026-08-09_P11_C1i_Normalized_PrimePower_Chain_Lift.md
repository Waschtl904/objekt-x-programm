# P11-C1i — Direktaudit des normalisierten Prime-Power-Kettenlifts

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1i]`  
**Vorgänger:** P11-C1h  
**Primärquellen:** NEU-043 (relativer Primclock auf graph-erweitertem Raum), NEU-044 (relative Primkanten-Normierung / orthogonale Graphsumme), P05 (eingefrorene Scope-Firewalls), P01 (exakte Prime-Power-Halbgewichte)  

**Urteil:**

\[
\boxed{[P11-C1i]\quad\checkmark[M]_{\rm part}}
\]

Der normalisierte Prime-Power-Kettenlift ist auf dem **graph-erweiterten kinematischen Relativraum** typkorrekt und reproduziert nach der Amplitude `p^{-k/4}` exakt das gewünschte Diagonalgewicht `\log p/p^{k/2}`. Er liefert sogar eine natürliche nichtorthogonale Hierarchie **innerhalb eines festen Primkanals**. Er ist jedoch nicht als kanonische globale Labelgeometrie konstruiert: die inneren Kantenvektoren und die Gleichgewichtung sind nicht source-selektiert, und verschiedene Primlabels bleiben im rohen Graphraum orthogonal.

Damit wird der Kandidat als **lokaler/diagonaler Baustein** behalten, aber als Lösung von `C_R^{can}` verworfen.

---

## 1. Graph-erweiterter Relativraum und Primclock

NEU-043 definiert den graph-erweiterten Raum

\[
\mathcal H_{\rm rel,N}
=
\bigoplus_{p\le N}\bigoplus_{m\in S_N}
\mathcal H_{m\xrightarrow p pm}.
\]

Auf jedem `p`-markierten Kantenraum gilt

\[
\boxed{
T_{\rm rel}E_{r;m\xrightarrow p pm}
=
\log p\,E_{r;m\xrightarrow p pm}.
}
\]

Damit ist jede lineare Kombination innerhalb der Summe aller `p`-Kanten ein Eigenvektor von `T_{rel}` mit Eigenwert `\log p`, sofern sie im Definitionsbereich liegt.

NEU-044 fixiert den kinematischen Graphraum als orthogonale Direktsumme der markierten Kantenräume. Diese Orthogonalität ist definitorische Graphstruktur; sie darf nicht mit einer bereits hergeleiteten induzierten `Wres`-Kreuzgeometrie verwechselt werden.

Status: `✓[M]`.

---

## 2. Prime-Power-Kette

Fixiere eine Primzahl `p` und einen Exponenten `k\ge1`.

Die zugehörige formale Kette ist

\[
1\xrightarrow p p\xrightarrow p p^2\xrightarrow p\cdots\xrightarrow p p^k.
\]

Wähle für `j=0,\ldots,k-1` normierte Vektoren

\[
e_{p,j}\in\mathcal H_{p^j\xrightarrow p p^{j+1}},
\qquad
\|e_{p,j}\|=1.
\]

Wegen der orthogonalen Graphsumme gilt

\[
\langle e_{p,i},e_{p,j}\rangle=\delta_{ij}.
\]

Definiere den gleichgewichteten Kettenvektor

\[
\boxed{
\chi_{p,k}
:=
\frac1{\sqrt{k}}
\sum_{j=0}^{k-1}e_{p,j}.
}
\]

Dann

\[
\boxed{\|\chi_{p,k}\|^2=1.}
\]

Status: `✓[M]` nach Wahl der normierten inneren Kantenvektoren.

---

## 3. Der verbotene Faktor `k` verschwindet korrekt

Da jede Kante derselben `p`-Kette unter `T_{rel}` den Eigenwert `\log p` trägt,

\[
T_{\rm rel}\chi_{p,k}
=
\log p\,\chi_{p,k}.
\]

Daher

\[
\boxed{
\langle\chi_{p,k},T_{\rm rel}\chi_{p,k}\rangle
=
\log p.
}
\]

Dies ist gerade **nicht**

\[
k\log p.
\]

Damit respektiert der normalisierte Kettenvektor die P06-Firewall

\[
\log(p^k)=k\log p\neq\Lambda(p^k)=\log p.
\]

Status: `✓[M]`.

---

## 4. Halbgewichtsamplitude

Setze

\[
\boxed{
\eta_{p,k}:=p^{-k/4}\chi_{p,k}.
}
\]

Dann

\[
\|\eta_{p,k}\|^2
=p^{-k/2}
\]

und

\[
\boxed{
\langle\eta_{p,k},T_{\rm rel}\eta_{p,k}\rangle
=
\frac{\log p}{p^{k/2}}
=
\frac{\Lambda(p^k)}{\sqrt{p^k}}.
}
\]

Damit reproduziert der Kettenlift exakt das P01/P02-Prime-Power-Gewicht.

Status: `✓[M]` algebraisch auf dem gewählten graph-erweiterten Kettenmodell.

---

## 5. Was `1/sqrt(k)` tatsächlich leistet

Innerhalb des Ansatzes „gleichgewichtete Summe von `k` orthogonalen Kantenvektoren“ ist der Faktor `1/\sqrt{k}` bis auf Phase die eindeutige Normierung auf Norm eins.

Aber `T_{rel}` selektiert diese Gleichgewichtung **nicht**: Auf der gesamten `p`-markierten Kettensumme wirkt der Clockoperator bereits skalar mit `\log p`. Jeder normierte Vektor

\[
\sum_{j=0}^{k-1}a_j e_{p,j},
\qquad
\sum_j|a_j|^2=1,
\]

hat dieselbe Clockerwartung

\[
\log p.
\]

Daher:

\[
\boxed{
T_{\rm rel}\text{ erklärt die richtige Energie, aber nicht die Gleichgewichtskoeffizienten.}
}
\]

Eine Symmetrie, die die `k` Kanten der Kette kanonisch gleichsetzt, ist im eingefrorenen P05-Stand nicht bewiesen.

Status der Gleichgewichtung als kanonische Wahl: `?[O]`.

---

## 6. Was `p^{-k/4}` tatsächlich leistet

Wenn ein normierter Kettenzustand die Clockenergie `\log p` trägt und das gewünschte quadratische Gewicht

\[
\frac{\log p}{p^{k/2}}
\]

reproduziert werden soll, muss seine skalare Amplitude betragsmäßig

\[
|a_{p,k}|=p^{-k/4}
\]

sein.

Damit ist `p^{-k/4}` innerhalb **dieses** quadratischen Realisierungstyps algebraisch erzwungen, bis auf Phase.

Es folgt daraus jedoch nicht, dass die bestehende Wres-/BC-/Liftgeometrie bereits genau diese Vektoramplitude konstruiert. P01 fixiert das resultierende Halbgewicht, nicht automatisch den vorliegenden Kettenvektor.

Status:

- algebraische Notwendigkeit im Ansatz: `✓[M]`;
- source-intrinsische Herleitung: `?[O]`.

---

## 7. Exponenthierarchie innerhalb eines festen Primkanals

Wähle die Kettenvektoren für verschiedene Exponenten kohärent aus derselben unendlichen `p`-Kette. Dann gilt für `k,\ell\ge1`

\[
\begin{aligned}
\langle\chi_{p,k},\chi_{p,\ell}\rangle
&=
\frac{1}{\sqrt{k\ell}}
\sum_{i<k}\sum_{j<\ell}\langle e_{p,i},e_{p,j}\rangle\\
&=
\boxed{
\frac{\min(k,\ell)}{\sqrt{k\ell}}.
}
\end{aligned}
\]

Damit entsteht innerhalb eines festen Primlabels ein nichttrivialer positiver Exponent-Gramkern

\[
\boxed{
c^{(p)}_{k\ell}
=
\frac{\min(k,\ell)}{\sqrt{k\ell}}.
}
\]

Für die halbgewichteten Zustände:

\[
\boxed{
\langle\eta_{p,k},\eta_{p,\ell}\rangle
=
p^{-(k+\ell)/4}
\frac{\min(k,\ell)}{\sqrt{k\ell}}.
}
\]

Positivität ist automatisch, da dies ein Gramkern der Kettenvektoren ist.

**Firewall:** Diese Formel ist nur so kanonisch wie die kohärente gleichgewichtete Kettenwahl selbst.

---

## 8. Kreuzprimblöcke im rohen Graphraum

Für `p\neq q` liegen die markierten `p`- und `q`-Kanten in verschiedenen Summanden der definitorisch orthogonalen Graphsumme. Daher

\[
\boxed{
\langle\chi_{p,k},\chi_{q,\ell}\rangle=0
\qquad(p\neq q).
}
\]

Ebenso

\[
\langle\eta_{p,k},\eta_{q,\ell}\rangle=0.
\]

Damit liefert der rohe Kettenlift nur eine blockdiagonale Primgeometrie

\[
C_R=\bigoplus_p C_R^{(p)}.
\]

Er kann daher **nicht** die in P11 gesuchte mögliche globale Kreuzprimkopplung erklären.

Dies steht nicht im Widerspruch zu P05: P05 sagt nur, dass globale Primorthogonalität nicht strukturell erzwungen ist; im kinematischen Graphraum ist sie definitorisch vorhanden.

---

## 9. Kollaps-/Wres-Paarung ist genau der fehlende Schritt

NEU-043 hält die relevante Frage ausdrücklich offen:

\[
\left\langle
E_{r;m\xrightarrow p n},
E_{r';m'\xrightarrow q n}
\right\rangle_{Wres,rel}
\stackrel{?}{=}0
\qquad(p\neq q).
\]

Nach Kollaps können verschiedene Primkanten denselben Zielsektor erreichen, etwa

\[
q\xrightarrow p pq,
\qquad
p\xrightarrow q pq.
\]

Ob die induzierte `Wres`-GNS-Paarung diese Markierungen orthogonal lässt oder nicht, ist **nicht** durch die kinematische Direktsumme entschieden.

Damit liegt genau hier die mögliche Quelle einer echten arithmetischen Labelkopplung.

---

## 10. Kein Konflikt mit dem eingefrorenen P05-Rang-eins-Modell

NEU-044 enthält historische/definitorische Aussagen zu `c_p`. P05 hat die daraus früher zu stark gelesene Nichtentartung und Hebungsunabhängigkeit ausdrücklich zurückgestuft:

\[
c_p\neq0,
\qquad
|c_p|^2\asymp(\log p)^2/p
\]

sind im eingefrorenen P05-Endstand nicht unbedingte Resultate.

C1i verwendet daher **keine** solche `c_p`-Nichtentartung. Der Kettenlift lebt allein auf dem graph-erweiterten kinematischen Relativraum und benutzt nur dessen definitorische Normierung und den bewiesenen Primclock.

---

## 11. Statusmatrix

| Aussage | Status |
|---|---|
| `T_rel=log p` auf jeder graph-erweiterten `p`-Kante | `✓[M]` |
| definitorische Orthogonalität verschiedener markierter Kantenräume im Graphraum | `✓[M]` / kinematische Struktur |
| normierter gleichgewichteter `chi_{p,k}` hat Norm 1 | `✓[M]` nach innerer Vektorwahl |
| Clockerwartung `=log p` | `✓[M]` |
| `eta_{p,k}=p^{-k/4}chi_{p,k}` reproduziert `log p/p^{k/2}` | `✓[M]` |
| `1/sqrt(k)` durch Clock eindeutig selektiert | `×[M]` |
| `p^{-k/4}` algebraisch erzwungen im quadratischen Gewichtsansatz | `✓[M]` |
| `p^{-k/4}` source-intrinsisch konstruiert | `?[O]` |
| gleicher-Prim-Exponentkernel `min(k,l)/sqrt(kl)` | `✓[M]` für kohärente gleichgewichtete Kettenwahl |
| Kreuzprimkernel im rohen Graphraum nichtnull | `×[M]` |
| induzierte `Wres`-Kreuzprimgeometrie nach Kollaps | `?[O]` |
| Kettenlift als kanonisches `C_R^{can}` | `×[M]` im derzeitigen Stand |

---

## 12. Endurteil

Der normalisierte Kettenlift löst eine echte Teilfrage:

\[
\boxed{
\text{Prime-Power-Exponent }k
\text{ kann mit relativen }p\text{-Kanten kompatibel gemacht werden,}
\text{ ohne den verbotenen Faktor }k\log p\text{ zu erzeugen.}
}
\]

Aber er löst **nicht** die globale Labelkopplung. Der Grund ist nun exakt lokalisiert:

\[
\boxed{
\text{Die fehlende Information sitzt in der induzierten Paarung zwischen verschieden markierten relativen Kanten, nicht in der Primclock.}
}
\]

---

## 13. Nächster Knoten

\[
\boxed{[P11\text{-}C1j]\quad\text{Direktaudit der }Wres\text{-Kreuzkantenpaarung im Minimalfall }n=pq.}
\]

Minimaler Test:

\[
\left\langle
E_{r;q\xrightarrow p pq},
E_{r';p\xrightarrow q pq}
\right\rangle_{Wres,rel}.
\]

Zu klären ist, ob spätere P05-/NEU-Knoten die in NEU-043 noch offene Kantendiagonalität entschieden, partiell typisiert oder durch eine andere Paarung ersetzt haben. Nur hier kann der Kettenansatz eine echte Kreuzprim-Labelgeometrie gewinnen.
