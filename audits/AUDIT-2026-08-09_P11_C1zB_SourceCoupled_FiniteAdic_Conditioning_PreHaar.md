# P11-C1z-B — Source-gekoppelte finite-adische Konditionierung vor Haar

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1z-B]`  
**Vorgänger:** C1l, C1m, C1q-CORR, C1r, C1t, C1y  
**Route:** Z-B — finite-adische Konditionierung vor `P_Haar`  
**Status:**

\[
\boxed{[P11\text{-}C1z\text{-}B]\quad\checkmark[K/M]_{\rm part}}
\]

## 0. Urteil

Z-B liefert erstmals eine **kanonische, positive, source-gekoppelte und nichttranslationinvariante finite-adische Konditionierung** der BC-Prime-Power-Geometrie.

Der zentrale Operator koppelt die p-adische Martingaltiefe an die Entfernung eines logarithmischen Quellpunkts `u` vom Rand des Source-Fensters `[-R,R]`. Für ein Prime-Power-Label `p^k` bleibt die volle BC-Markierung exakt dort erhalten, wo die zugehörige Weil-Korrelation

\[
a(u+k\log p/2)\overline{a(u-k\log p/2)}
\]

überhaupt ungleich null sein kann. Außerhalb dieses Überlappungsbereichs werden tiefere p-adische Martingalstufen kanonisch wegkonditioniert.

Dies erreicht drei Dinge zugleich:

1. die C1l-Labelinformation bleibt **vor Haar** erhalten;
2. die C1r-Restsektoren werden source-lokalisiert und bei festem `R` endlich;
3. die volle analytische Translationinvarianz aus C1y wird gebrochen.

Aber es gibt eine harte Restfirewall:

\[
\boxed{
\text{jede unital finite-adische Konditionierung fixiert den neutralen Hub }\zeta_1.}
\]

Daher bleibt der aligned Hubtail mit Koeffizienten `\sqrt{\log p}\,p^{-3/4}` bestehen. Nach C1q-CORR ist dieser Tail im Allgemeinen nicht Hilbertnorm-konvergent.

Somit ist Z-B **kein fertiger Objekt-X-Kompressor**, aber ein echter konstruktiver Fortschritt:

\[
\boxed{
\text{finite-adische Restgeometrie kanonisch kontrolliert}
\quad+\quad
\text{ein einziger neutraler Hub bleibt separat zu regularisieren}.}
\]

Der nächste zulässige Schritt ist deshalb eine source-window-/Feshbach-artige Behandlung **nur dieses verbleibenden Hubs**, nicht mehr der gesamten unkontrollierten Prime-Restgeometrie.

---

# 1. Ausgangslage aus C1l/C1m

C1l beweist, dass der totale Haar-Port

\[
P_{\rm Haar}F(x)=\int_{\mathbb A_f}F(x,y)\,dy
\]

die BC-Rangeinformation nicht erhält. Insbesondere faktorisiert der Momentkanal

\[
M_nF(x)=\int F(x,y)\overline{\zeta_n(y)}\,dy
\]

nicht durch `R_PW`.

C1m konstruiert deshalb für den source-induzierten endlichen Labelcutoff

\[
\mathcal N_R=\{p^k:p^k\le e^{2R}\}
\]

den endlichen BC-Raum

\[
K_R=\operatorname{span}\{\zeta_n:n\in\mathcal N_R\},
\qquad
\zeta_n=\sqrt n\,E_n,
\]

mit strikt positiver GCD-Grammatrix

\[
\langle\zeta_n,\zeta_m\rangle
=\frac{\gcd(n,m)}{\sqrt{nm}}.
\]

Die Z-B-Frage lautet:

\[
\boxed{
\text{Kann eine kanonische finite-adische Konditionierung vor Haar}
\text{ die divergente Restgeometrie kontrollieren, ohne die relevanten Marks zu zerstören?}}
\]

---

# 2. Pure aktive Conditional Expectation ist exakt wirkungslos

Fixiere `R` und definiere die endliche Sigma-Algebra

\[
\mathfrak F_R^{\rm act}
:=
\sigma\bigl(E_n:n\in\mathcal N_R\bigr)
\]

auf `\widehat{\mathbb Z}`.

Sei

\[
Q_R^{\rm act}
:=
\mathbb E[\,\cdot\mid\mathfrak F_R^{\rm act}]
\]

die zugehörige `L^2`-Conditional Expectation.

Da jedes `E_n`, `n\in\mathcal N_R`, bereits `\mathfrak F_R^{act}`-messbar ist,

\[
Q_R^{\rm act}E_n=E_n,
\]

also

\[
\boxed{
Q_R^{\rm act}\zeta_n=\zeta_n
\qquad(n\in\mathcal N_R).}
\tag{C1zB.1}
\]

Damit

\[
\boxed{
Q_R^{\rm act}|_{K_R}=I_{K_R}.}
\tag{C1zB.2}
\]

Für die direkte Prime-Power-Synthese

\[
\mathcal T_Ra
=
\sum_{n\in\mathcal N_R}
\sqrt{\frac{\Lambda(n)}{\sqrt n}}
D_{\log n}a\otimes\zeta_n
\]

folgt exakt

\[
\boxed{
(I\otimes Q_R^{\rm act})\mathcal T_Ra
=\mathcal T_Ra.}
\tag{C1zB.3}
\]

Die C1o/C1t-Divergenz wird also nicht einmal verändert.

Status: `✓[K/M]_{neg,pure}`.

---

# 3. Allgemeines Preservation-No-Go für pure finite-adische Projektionen

Der vorige Befund ist nicht speziell an die Sigma-Algebra `\mathfrak F_R^{act}` gebunden.

## Satz C1zB.1

Sei `Q` ein orthogonaler Projektor auf einem finite-adischen `L^2`-Raum. Falls

\[
\|Q\zeta_n\|=\|\zeta_n\|=1
\qquad
\forall n\in\mathcal N_R,
\]

dann gilt

\[
\boxed{Q\zeta_n=\zeta_n\quad\forall n\in\mathcal N_R}
\]

und daher

\[
\boxed{Q|_{K_R}=I.}
\]

### Beweis

Für einen orthogonalen Projektor gilt

\[
\|\zeta_n\|^2
=
\|Q\zeta_n\|^2+\|(I-Q)\zeta_n\|^2.
\]

Normerhalt impliziert daher `(I-Q)\zeta_n=0`. `□`

### Konsequenz

Eine pure finite-adische Conditional Expectation kann die aktive Synthese nur dann nichttrivial komprimieren, wenn sie mindestens einige aktive Labelnormen beziehungsweise Markierungen verändert.

Noch schärfer: Soll eine Sigma-Algebra `\mathfrak G_R` alle aktiven `E_n` exakt erhalten, dann müssen alle `E_n` `\mathfrak G_R`-messbar sein, also

\[
\mathfrak F_R^{\rm act}\subseteq\mathfrak G_R.
\]

Auf dem von den aktiven Labels erzeugten Raum ist die Conditional Expectation dann wieder die Identität.

Damit ist klar:

\[
\boxed{
\text{Z-B darf nicht nur im finite-adischen Faktor von der Source-Position unabhängig wirken.}}
\tag{C1zB.4}
\]

---

# 4. p-adische Filtration und exakte Conditional-Expectation-Formel

Fixiere eine Primzahl `p`. Setze

\[
E_{p^j}=1_{p^j\widehat{\mathbb Z}},
\qquad j\ge0,
\]

mit `E_{p^0}=E_1`.

Für `J\ge0` sei

\[
\mathfrak F_{p,J}
:=
\sigma(E_p,E_{p^2},\ldots,E_{p^J}),
\]

wobei `\mathfrak F_{p,0}` die triviale p-adische Sigma-Algebra bezeichnet.

Sei

\[
Q_{p,J}:=\mathbb E[\,\cdot\mid\mathfrak F_{p,J}].
\]

Für `k\le J` ist `E_{p^k}` messbar und bleibt fixiert.

Für `k>J` gilt auf dem Atom `E_{p^J}` die bedingte Wahrscheinlichkeit

\[
\frac{m(E_{p^k})}{m(E_{p^J})}
=
\frac{p^{-k}}{p^{-J}}
=p^{-(k-J)}.
\]

Daher

\[
\boxed{
Q_{p,J}E_{p^k}
=
p^{-(k-J)}E_{p^J}
\qquad(k>J).}
\tag{C1zB.5}
\]

Für die normierten Rangevektoren

\[
\zeta_{p^k}=p^{k/2}E_{p^k}
\]

folgt

\[
\boxed{
Q_{p,J}\zeta_{p^k}
=
\begin{cases}
\zeta_{p^k},&k\le J,\\[1mm]
p^{-(k-J)/2}\zeta_{p^J},&k>J.
\end{cases}}
\tag{C1zB.6}
\]

Für `J=0` erhält man exakt den C1q-Haar-Hubwert

\[
Q_{p,0}\zeta_{p^k}=p^{-k/2}\zeta_1.
\]

Die Familie `J=0,1,2,\ldots` interpoliert damit kanonisch zwischen vollem Haar-Kollaps und vollständiger p-adischer Markauflösung.

Status: `✓[K/M]`.

---

# 5. Martingalinterpretation — Conditional Expectation ist Level-Cutoff

C1r definiert

\[
d_{p,j}
=E_{p^{j+1}}-p^{-1}E_{p^j}
\]

und die normierten Martingalvektoren

\[
\psi_{p,j}
=\sqrt{\frac{p^{j+2}}{p-1}}\,d_{p,j}.
\]

Für `j<J` ist `\psi_{p,j}` bereits `\mathfrak F_{p,J}`-messbar, also

\[
Q_{p,J}\psi_{p,j}=\psi_{p,j}.
\]

Für `j\ge J` liefert (C1zB.5)

\[
Q_{p,J}E_{p^{j+1}}
=p^{-(j+1-J)}E_{p^J},
\]

und

\[
p^{-1}Q_{p,J}E_{p^j}
=p^{-1}p^{-(j-J)}E_{p^J}
=p^{-(j+1-J)}E_{p^J}.
\]

Also

\[
\boxed{
Q_{p,J}\psi_{p,j}
=
\begin{cases}
\psi_{p,j},&j<J,\\
0,&j\ge J.
\end{cases}}
\tag{C1zB.7}
\]

Damit ist p-adische Conditional Expectation in den C1r-Koordinaten **kein frei gewählter Dämpfer**, sondern ein exakter kanonischer Martingal-Levelcutoff.

---

# 6. Source-gekoppelte Tiefe

Nun wird erstmals die finite-adische Filtration an die logarithmische Source-Geometrie gekoppelt.

Für `R>0`, `u\in\mathbb R` und eine Primzahl `p` definiere

\[
\boxed{
J_{p,R}(u)
:=
\max\left\{0,
\left\lfloor
\frac{2(R-|u|)_+}{\log p}
\right\rfloor
\right\}.}
\tag{C1zB.8}
\]

Äquivalent ist `J_{p,R}(u)` die größte p-adische Tiefe `J`, für die

\[
|u|+\frac J2\log p\le R.
\]

Interpretation:

`J_{p,R}(u)` zählt exakt, wie viele Prime-Power-Halbkanten der Längen

\[
\frac12\log p,
\frac22\log p,
\ldots
\]

vom Punkt `u` aus noch vollständig im Source-Fenster `[-R,R]` Platz haben.

---

# 7. Der source-gekoppelte Conditional-Expectation-Operator

Auf dem BC-Prime-Power-Unterraum

\[
K_{\mathcal P^*}
=
\mathbb C\zeta_1
\oplus
\bigoplus_pK_p^0
\]

definiere faserweise

\[
\boxed{
\mathsf Q_R(u)\zeta_1=\zeta_1,
\qquad
\mathsf Q_R(u)\psi_{p,j}
=
1_{\{j<J_{p,R}(u)\}}\psi_{p,j}.}
\tag{C1zB.9}
\]

Da für festes `R` die Funktionen `J_{p,R}(u)` nur an endlich vielen Schwellen innerhalb jedes kompakten `u`-Bereichs springen, ist `u\mapsto\mathsf Q_R(u)` messbar.

Definiere auf

\[
L^2(\mathbb R;K_{\mathcal P^*})
\]

den zerlegbaren Operator

\[
\boxed{
(\mathsf Q_R F)(u)
:=
\mathsf Q_R(u)F(u).}
\tag{C1zB.10}
\]

Dann gilt:

1. `\mathsf Q_R^2=\mathsf Q_R`;
2. `\mathsf Q_R^*=\mathsf Q_R`;
3. `0\le\mathsf Q_R\le I`;
4. `\|\mathsf Q_R\|=1`;
5. faserweise ist `\mathsf Q_R(u)` die Restriktion einer finite-adischen Conditional Expectation auf die durch die entsprechenden p-adischen Filtrationsstufen erzeugte Sigma-Algebra.

Somit ist `\mathsf Q_R` ein kanonischer positiver Quellprojektor.

Status: `✓[K/M]`.

---

# 8. C1y wird tatsächlich verlassen: Translationinvarianz bricht

Die Schwellentiefe hängt von `|u|` ab. Für generisches `t\ne0` gilt daher

\[
J_{p,R}(u+t)\ne J_{p,R}(u)
\]

auf einer Menge positiven Maßes.

Folglich

\[
\boxed{
[\mathsf Q_R,U_t\otimes I]\ne0
\qquad\text{für generisches }t\ne0.}
\tag{C1zB.11}
\]

Damit liegt `\mathsf Q_R` ausdrücklich **außerhalb** der in C1y ausgeschlossenen translationsinvarianten Regulatorklasse.

Wichtig: Dies beweist noch keine erfolgreiche globale Regularisierung; es erfüllt lediglich erstmals die von C1y erzwungene Symmetriebrechungsbedingung auf quellenkanonische Weise.

---

# 9. Exakte Labelwirkung

Aus (C1zB.6) folgt für jedes Prime-Power-Label `p^k`:

\[
\boxed{
\mathsf Q_R(u)\zeta_{p^k}
=
\begin{cases}
\zeta_{p^k},&k\le J_{p,R}(u),\\[1mm]
p^{-(k-J_{p,R}(u))/2}
\zeta_{p^{J_{p,R}(u)}},&k>J_{p,R}(u).
\end{cases}}
\tag{C1zB.12}
\]

mit der Konvention `\zeta_{p^0}=\zeta_1`.

Für die C1n-Restvektoren

\[
\eta_{p,k}
=\sqrt{p-1}
\sum_{j=0}^{k-1}p^{(j-k)/2}\psi_{p,j}
\]

ergibt sich

\[
\boxed{
\mathsf Q_R(u)\eta_{p,k}
=
\sqrt{p-1}
\sum_{j=0}^{\min(k-1,J_{p,R}(u)-1)}
 p^{(j-k)/2}\psi_{p,j}.}
\tag{C1zB.13}
\]

Insbesondere für den primitiven Kanal:

\[
\boxed{
\mathsf Q_R(u)\eta_{p,1}
=
1_{\{|u|\le R-\frac12\log p\}}
\eta_{p,1}.}
\tag{C1zB.14}
\]

Die C1o-Hochprimdivergenz wird damit nicht labelweise künstlich gedämpft, sondern ihre primspezifische Restkomponente wird exakt auf den source-geometrisch zulässigen Überlappungsbereich lokalisiert.

---

# 10. Korrelationserhaltungssatz

Sei

\[
a\in C_c^\infty([-R,R]).
\]

Fixiere `p^k` und setze

\[
s=k\log p.
\]

Falls

\[
a(u+s/2)\overline{a(u-s/2)}\ne0,
\]

dann liegen beide Punkte `u\pm s/2` in `[-R,R]`. Daher

\[
\max\{|u+s/2|,|u-s/2|\}
=|u|+s/2
\le R.
\]

Also

\[
|u|+\frac{k}{2}\log p\le R,
\]

und somit

\[
J_{p,R}(u)\ge k.
\]

Nach (C1zB.12):

\[
\boxed{
\mathsf Q_R(u)\zeta_{p^k}=\zeta_{p^k}
\quad\text{auf dem gesamten Träger der }p^k\text{-Korrelation}.}
\tag{C1zB.15}
\]

Das ist der wichtigste positive Z-B-Satz.

Die finite-adische Markierung wird **genau dort vollständig erhalten, wo der eigentliche Weil-Kreuzterm lebt**.

Außerhalb dieses Bereichs können nur die einseitigen Translations-/Baselineanteile von `D_s a` auftreten; dort darf die Martingaltiefe source-kanonisch reduziert werden.

Status: `✓[K/M]`.

---

# 11. Der konditionierte Restsektor ist bei festem Source-Fenster endlich

Definiere formal den konditionierten Restoperator

\[
\mathcal T_{R,\rm res}^{\bowtie}a(u)
:=
\sum_p\sum_{k\ge1}
\sqrt{\frac{\log p}{p^{k/2}}}
D_{k\log p}a(u)
\otimes
\mathsf Q_R(u)\eta_{p,k}.
\tag{C1zB.16}
\]

Falls `\mathsf Q_R(u)\eta_{p,k}\ne0`, muss mindestens

\[
J_{p,R}(u)\ge1
\]

gelten. Also

\[
p\le e^{2(R-|u|)}\le e^{2R}.
\]

Damit treten nur endlich viele Primzahlen im Restsektor auf.

Außerdem liegt der Restbereich stets in `|u|\le R`. Ist dort

\[
D_{k\log p}a(u)\ne0,
\]

so muss mindestens einer der Punkte `u\pm k\log p/2` im Träger `[-R,R]` liegen. Daher

\[
\frac{k}{2}\log p\le R+|u|\le2R,
\]

also

\[
\boxed{p^k\le e^{4R}.}
\tag{C1zB.17}
\]

Folglich enthält (C1zB.16) für festes `R` tatsächlich nur endlich viele nichtverschwindende `(p,k)`-Beiträge.

Somit ist

\[
\boxed{
\mathcal T_{R,\rm res}^{\bowtie}
\text{ auf jedem Source-Level }R
\text{ ein wohldefinierter endlicher positiver Analysebaustein}.}
\tag{C1zB.18}
\]

Dies ist deutlich stärker als die bloße C1r-Martingalkoordinatisierung: Die Restgeometrie ist nun **source-gekoppelt endlich**.

---

# 12. Warum der neutrale Hub unverändert bleibt

Jede Conditional Expectation ist unital. Daher

\[
\mathsf Q_R(u)\zeta_1=\zeta_1.
\]

Aus der Sternzerlegung

\[
\zeta_{p^k}
=p^{-k/2}\zeta_1+\eta_{p,k}
\]

folgt

\[
\boxed{
\mathsf Q_R(u)\zeta_{p^k}
=
p^{-k/2}\zeta_1
+
\mathsf Q_R(u)\eta_{p,k}.}
\tag{C1zB.19}
\]

Der Hubkoeffizient `p^{-k/2}` ist **vollständig unabhängig von der gewählten p-adischen Tiefe**.

Damit ist die Wirkung jeder solchen unitalen finite-adischen Konditionierung strukturell getrennt:

\[
\boxed{
\text{Restsektor veränderbar}
\qquad\text{aber}\qquad
\text{Haarmittel/Hub starr}.}
\tag{C1zB.20}
\]

Dies ist kein Nachteil der speziellen Wahl (C1zB.8), sondern eine allgemeine Conditional-Expectation-Firewall.

---

# 13. Der verbleibende Hubtail ist genau C1q-CORR

Setzt man die exakten Weil-Lokalgewichte ein, besitzt der Hubteil des primitiven Kanals `k=1` den Vektorkoeffizienten

\[
\sqrt{\frac{\log p}{\sqrt p}}\,p^{-1/2}
=
\boxed{\sqrt{\log p}\,p^{-3/4}.}
\]

Somit enthält jede vollständige konditionierte Synthese den Tail

\[
\sum_p
\sqrt{\log p}\,p^{-3/4}
D_{\log p}a\otimes\zeta_1.
\tag{C1zB.21}
\]

C1q-CORR beweist durch Primblöcke und gemeinsame Translationsplateaus, dass dieser Tail für geeignete nichtnegative kompakte Testfunktionen nicht Hilbertnorm-Cauchy ist.

Daher

\[
\boxed{
\text{source-gekoppelte finite-adische Conditional Expectation allein}
\not\Rightarrow
\text{globale positive Weil-Synthese}.}
\tag{C1zB.22}
\]

Status: `✓[M]_{neg,hub}`.

---

# 14. Reconciliation mit C1q

C1q bleibt richtig in den strukturellen Aussagen:

\[
P_0K_p^0=0,
\]

Rang-eins-Kollaps und Markverlust.

C1q-CORR korrigiert nur die frühere Folgerung, dass die resultierende direkte Hub-Synthese wegen des diagonalen Faktors `\log p/p^{3/2}` automatisch konvergiere.

Die richtige Unterscheidung lautet:

\[
\boxed{
\text{Quadratische Einzelkanalgewichte sind summierbar,}
\quad
\text{aber die Hub-Vektoren sind nicht orthogonal}.}
\]

C1z-B verwendet daher **keinen** C1q-Konvergenzschluss.

---

# 15. Reconciliation mit C1t und C1y

## C1t

C1t schließt positive labeldiagonale Regulatoren aus, die für jedes feste Label punktweise gegen die Identität zurückkehren.

`\mathsf Q_R` ist nicht von diesem Typ:

- es ist in der `\zeta_{p^k}`-Basis nicht diagonal;
- tiefere Labels werden auf gröbere p-adische Level abgebildet;
- die Wirkung hängt von `u` ab;
- die Martingalstufen werden source-geometrisch konditioniert.

C1t wird daher nicht verletzt.

## C1y

C1y verlangt, dass der nächste ernsthafte Kompressor die volle Translationinvarianz bricht.

Nach (C1zB.11) erfüllt `\mathsf Q_R` diese notwendige Bedingung.

Aber C1y wird nicht „widerlegt“: Der verbleibende Hub muss noch durch eine ebenfalls nichttranslationinvariante analytische/relative Operation behandelt werden.

---

# 16. Was Z-B mathematisch erreicht hat

Vor C1z-B war die offene Lage:

\[
\text{Haar zu grob}
\quad\text{vs.}\quad
\text{volle BC-Geometrie divergent}.
\]

Jetzt existiert eine kanonische Zwischenstruktur:

\[
\boxed{
\text{source-position}
\longmapsto
\text{zulässige p-adische Martingaltiefe}
\longmapsto
\text{finite-adische Conditional Expectation}.}
\]

Sie besitzt gleichzeitig:

1. **BC-Kanonizität:** nur `E_{p^j}` und Haarmaß;
2. **Source-Kanonizität:** nur Abstand zum Rand `[-R,R]`;
3. **Positivität:** orthogonale Conditional Expectation;
4. **Marktreue auf dem Weil-Korrelationsträger:** Satz (C1zB.15);
5. **Restkontrolle:** endlicher konditionierter Restsektor auf jedem `R`;
6. **Symmetriebruch:** kein Kommutant des vollen Translationsflusses;
7. **keine willkürlichen Tailgewichte**.

Das ist ein echter Objekt-X-Vorbaustein.

---

# 17. Was Z-B ausdrücklich noch nicht erreicht

Nicht bewiesen sind:

- globale Hilbertnormkonvergenz der vollständigen exakten Weil-Synthese;
- ein positiver globaler Grenzraum `\mathcal K_X`;
- Schatten-/Kompaktheitskontrolle im Sinn P10-O07;
- Mosco-/Resolventenkonvergenz;
- eine exakte Identität des konditionierten positiven Gramoperators mit `B_W`;
- ein operatorieller Finite Part des neutralen Hubs;
- ein globaler Feshbach-Grenzwert.

Insbesondere bleibt

\[
\boxed{\text{der neutrale Hub das nächste harte Objekt}.}
\]

---

# 18. Statusmatrix

| Aussage | Status |
|---|---|
| aktive finite-adische CE `Q_R^{act}` erhält alle aktiven Labels | `✓[K/M]` |
| dieselbe CE reguliert die direkte Synthese | `×[M]` — exakt wirkungslos |
| jede orthogonale finite-adische Projektion mit exaktem aktiven Normerhalt fixiert `K_R` | `✓[M]` |
| Formel `Q_{p,J}\zeta_{p^k}` | `✓[K/M]` |
| CE = harter Martingal-Levelcutoff in `\psi_{p,j}` | `✓[K/M]` |
| source-Tiefe `J_{p,R}(u)` kanonisch definiert | `✓[M]` |
| `\mathsf Q_R` orthogonaler positiver Projektor | `✓[K/M]` |
| `\mathsf Q_R` bricht volle Translationinvarianz | `✓[M]` |
| aktive `p^k`-Marke bleibt auf Korrelationsträger exakt erhalten | `✓[K/M]` |
| konditionierter Restsektor ist für festes `R` endlich | `✓[M]` |
| neutraler Hub wird durch CE gedämpft | `×[M]` — Unitalitätsfirewall |
| vollständige konditionierte Weil-Synthese konvergiert | `×[M]` im direkten Hub-Scope |
| Z-B liefert finalen Objekt-X-Kompressor | `?[O]` / noch nein |

---

# 19. Nächster atomarer Knoten

Z-B hat die unkontrollierte Restgeometrie auf ein endliches source-gekoppeltes Objekt reduziert. Es wäre daher ineffizient, jetzt wieder die gesamte Labelgeometrie zu regularisieren.

Der nächste Test soll nur noch den starren Hub angreifen:

\[
\boxed{
[P11\text{-}C1z\text{-}B1]
\quad
\text{source-windowed Hub-Feshbach nach finite-adischer Martingalkonditionierung}.}
\]

Konkret:

1. behalte den endlichen konditionierten Restoperator `\mathcal T_{R,res}^{\bowtie}`;
2. isoliere den neutralen Hub `\mathbb C\zeta_1`;
3. ersetze den in C1w/C1y translationsinvarianten Hubregulator durch einen source-window-/Randoperator auf `[-R,R]`;
4. prüfe den neuen Schurterm gegen den exakten Gamma-Inzidenzkanal;
5. teste erstmals Schatten-/Kompaktheitsverhalten, nachdem die infinite primspezifische Restmultiplizität entfernt ist.

Damit verschmelzen die ursprünglich getrennten Routen Z-B und Z-A in einer erzwungenen Reihenfolge:

\[
\boxed{
\text{Z-B zuerst: finite-adische Restkonditionierung}
\quad\Longrightarrow\quad
\text{Z-A nur noch auf dem neutralen Hub}.}
\]

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
