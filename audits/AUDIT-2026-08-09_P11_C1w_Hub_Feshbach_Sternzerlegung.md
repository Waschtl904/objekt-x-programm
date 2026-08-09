# P11-C1w — Exakter Hub-Feshbach-Test der BC-Sternzerlegung

**Datum:** 9. August 2026  
**Block:** P11 — Global Coupling and the Object-X Candidate Geometry  
**Status:** `✓[M]_part` mit zwei modellgebundenen Negativbefunden  
**Vorgänger:** C1u, C1v  
**Schnittstellen:** P10-O05, P10-O07, P10-O13

> **Scope-Firewall.** Dieser Knoten untersucht die kanonische Sternspaltung des C1-BC-GCD-Zielraums und den Schurkomplementmechanismus für den direkten C1-Syntheseoperator. Er ist kein allgemeiner No-Go gegen andere Feshbach-, Fenster-, Quotienten- oder archimedisch gekoppelte Konstruktionen.

---

## 0. Ausgangslage

Aus C1n/C1u:

\[
K_{\mathcal P^*}
=
\mathbb C\zeta_1
\oplus
K^0,
\qquad
K^0:=\bigoplus_pK_p^0,
\]

mit

\[
P_0:=|\zeta_1\rangle\langle\zeta_1|,
\qquad
Q_0:=I-P_0.
\]

Die direkte Synthese lautet

\[
\mathcal V_R a
=
\sum_{n\in\mathcal N_R}
\sqrt{\lambda_n}\,D_{\log n}a\otimes\zeta_n,
\qquad
\lambda_n=\frac{\Lambda(n)}{\sqrt n}.
\]

Im Fourierbild ist sie faserweise von Rang eins:

\[
\widehat{\mathcal V_R a}(\xi)
=
\widehat a(\xi)\,v_R(\xi),
\]

wobei

\[
\boxed{
v_R(\xi)
:=
\sum_{n\in\mathcal N_R}
\sqrt{\lambda_n}\,
d_n(\xi)\,\zeta_n,
\qquad
d_n(\xi):=2i\sin\!\left(\frac{\xi\log n}{2}\right).}
\tag{C1w.1}
\]

Zerlege exakt

\[
\boxed{v_R(\xi)=h_R(\xi)\zeta_1+r_R(\xi),
\qquad r_R(\xi)\in K^0.}
\tag{C1w.2}
\]

---

# 1. Expliziter Hubkoeffizient

Da

\[
\langle\zeta_1,\zeta_n\rangle=n^{-1/2},
\]

gilt

\[
\boxed{
h_R(\xi)
=
\sum_{n\in\mathcal N_R}
\sqrt{\lambda_n}\,n^{-1/2}d_n(\xi).}
\tag{C1w.3}
\]

Für `n=p^k`:

\[
\sqrt{\lambda_{p^k}}\,p^{-k/2}
=
\sqrt{\log p}\,p^{-3k/4}.
\]

Damit ist der höhere-Prime-Power-Anteil `k>=2` absolut summierbar. Der einzige wachsende Teil ist der Primterm

\[
\sum_{p\le X}\sqrt{\log p}\,p^{-3/4}d_p(\xi),
\qquad X=e^{2R}.
\]

Durch PNT + partielle Summation gilt für festes `xi != 0`

\[
\boxed{|h_R(\xi)|
=O_\xi\!\left(\frac{X^{1/4}}{\sqrt{\log X}}\right),
\qquad
|h_R(\xi)|^2
=O_\xi\!\left(\frac{\sqrt X}{\log X}\right).}
\tag{C1w.4}
\]

---

# 2. Restenergie besitzt mindestens `sqrt(X)`-Wachstum

Setze

\[
\rho_R(\xi):=\|r_R(\xi)\|^2.
\]

Für Hochbandprimzahlen

\[
\sqrt X<p\le X
\]

liegt im Labelcutoff nur `k=1`. In den paarweise orthogonalen Restsektoren `K_p^0` kann daher keine höhere `p^k`-Komponente den Primanteil kompensieren.

Wie in C1u folgt

\[
\rho_R(\xi)
\ge
4\sum_{\sqrt X<p\le X}
\frac{\log p}{\sqrt p}
\left(1-\frac1p\right)
\sin^2\!\left(\frac{\xi\log p}{2}\right).
\tag{C1w.5}
\]

Für jedes feste `xi != 0` enthält das letzte feste logarithmische Periodenfenster vor `log X` ein Teilintervall, auf dem der Sinusquadratterm von null weg beschränkt ist. PNT auf dem entsprechenden festen multiplikativen Intervall liefert daher

\[
\boxed{ho_R(\xi)\ge c_\xi\sqrt X
\qquad(R\gg_\xi1).}
\tag{C1w.6}
\]

Insbesondere

\[
\rho_R(\xi)\to\infty
\qquad(\xi\ne0).
\]

---

# 3. Regularisierter positiver Feshbach-Block

Der reine Operator `V_R V_R^*` ist faserweise `|v_R><v_R|` und damit Rang eins. Auf dem großen Restsektor ist der reine `Q_0`-Block nicht invertierbar. Der Moore–Penrose-Schurkomplement des reinen Rang-eins-Grams degeneriert, sobald `r_R != 0`.

Der minimale positive, bereits durch C1u ausgezeichnete Regularisierungsblock ist daher

\[
\boxed{B_R:=I+\mathcal V_R\mathcal V_R^*.}
\tag{C1w.7}
\]

Im Fourierpunkt `xi` besitzt er bezüglich

\[
K_{\mathcal P^*}
=
\mathbb C\zeta_1\oplus K^0
\]

die Blockform

\[
B_R(\xi)
=
\begin{pmatrix}
1+|h_R|^2 & h_R\langle r_R,\cdot\rangle\\
\overline{h_R}r_R & I_{K^0}+|r_R\rangle\langle r_R|
\end{pmatrix}.
\tag{C1w.8}
\]

Alle folgenden Schurkomplemente sind daher exakt berechenbar.

---

# 4. Eliminiere den Rest: effektive Hub-Selbstenergie

Mit der Sherman–Morrison-Identität

\[
(I+|r\rangle\langle r|)^{-1}
=I-\frac{|r\rangle\langle r|}{1+\|r\|^2}
\]

folgt

\[
\langle r,(I+|r\rangle\langle r|)^{-1}r\rangle
=\frac{\rho}{1+\rho}.
\]

Das Schurkomplement auf dem Hub ist daher

\[
\boxed{
F_R^{\rm hub}(\xi)
=
1+rac{|h_R(\xi)|^2}{1+\rho_R(\xi)}.}
\tag{C1w.9}
\]

Die effektive Hub-Selbstenergie lautet

\[
\boxed{
\Sigma_R^{\rm hub}(\xi)
:=
\frac{|h_R(\xi)|^2}{1+\rho_R(\xi)}.}
\tag{C1w.10}
\]

Aus (C1w.4) und (C1w.6):

\[
0\le\Sigma_R^{\rm hub}(\xi)
\le
\frac{C_\xi\sqrt X/\log X}{c_\xi\sqrt X}
=O_\xi\!\left(\frac1{\log X}\right).
\]

Also

\[
\boxed{
\Sigma_R^{\rm hub}(\xi)\longrightarrow0
\qquad\text{für jedes feste }\xi\ne0.}
\tag{C1w.11}
\]

**Interpretation:** Die große orthogonale Hochprim-Restenergie wird durch die Feshbach-Elimination nicht in eine endliche nichttriviale Hub-Selbstenergie umgewandelt. Sie **screened** den Hub asymptotisch vollständig.

Damit

\[
F_R^{\rm hub}(\xi)\to1.
\]

Status: `✓[M]_{neg,scope}` gegen den naiven Hub-Feshbach-Endpunkt.

---

# 5. Eliminiere den Hub: der Rest bleibt divergent

Das Schurkomplement auf `K^0` lautet exakt

\[
\boxed{
F_R^{\rm rest}(\xi)
=
I_{K^0}
+
\frac{1}{1+|h_R(\xi)|^2}
|r_R(\xi)\rangle\langle r_R(\xi)|.}
\tag{C1w.12}
\]

Der nichttriviale Rang-eins-Anteil besitzt Operatornorm

\[
\tau_R(\xi)
=
\frac{\rho_R(\xi)}{1+|h_R(\xi)|^2}.
\tag{C1w.13}
\]

Mit (C1w.4), (C1w.6) folgt für großes `R`

\[
\tau_R(\xi)
\ge
\frac{c_\xi\sqrt X}{1+C_\xi\sqrt X/\log X}
\gtrsim_\xi \log X.
\]

Also

\[
\boxed{
\tau_R(\xi)\longrightarrow\infty
\qquad(\xi\ne0).}
\tag{C1w.14}
\]

**Interpretation:** Der Hub reduziert die Restdivergenz höchstens stark in der Größenordnung, beseitigt sie aber nicht. Der primspezifische Restsektor kann nicht einfach über den neutralen Hub regularisiert werden.

Status: `✓[M]_{neg,scope}`.

---

# 6. Translationinvarianz bleibt erhalten

Sowohl

\[
\Sigma_R^{\rm hub}(\xi)
\]

als auch die Faserkoeffizienten von `F_R^{rest}` hängen weiterhin nur von der Fourierfrequenz `xi` ab. Die Hub-Feshbach-Elimination bricht daher die reine Translationinvarianz **nicht**.

Insbesondere ist der effektive Huboperator

\[
M_{\Sigma_R^{\rm hub}}
\]

für festes `R` ein Multiplikationsoperator auf `L^2(R)`.

Sofern `Sigma_R^{hub}` nicht identisch null ist, ist er auf dem nichtatomaren `L^2(R)` nicht kompakt und liegt in keiner endlichen Schattenklasse.

Damit liefert auch der kanonische Hub-Feshbach-Weg keine direkte P10-O07-Brücke.

---

# 7. Generalisierung mit festem positivem Regulator `c`

Für

\[
B_{R,c}:=cI+\mathcal V_R\mathcal V_R^*,
\qquad c>0,
\]

lautet das Hub-Schurkomplement

\[
\boxed{
F_{R,c}^{\rm hub}(\xi)
=
c+
\frac{c|h_R(\xi)|^2}{c+\rho_R(\xi)}.}
\tag{C1w.15}
\]

und der nichttriviale Restanteil

\[
\boxed{
\frac{c}{c+|h_R(\xi)|^2}|r_R\rangle\langle r_R|.}
\tag{C1w.16}
\]

Für jedes **feste** `c>0` bleibt die qualitative Entscheidung unverändert:

- Hub-Selbstenergie `->0`;
- Restanteil divergiert;
- Translationinvarianz bleibt;
- keine Schattenkompaktheit.

Ein `R`-abhängiger Regulator `c_R` wäre ein neuer Renormierungsparameter und muss separat auf Kanonizität geprüft werden; er wird hier nicht rückwärts gewählt.

---

# 8. Reconciliation mit P10-O05/O13/O07

### O05

Die Sternzerlegung liefert eine echte kanonische Prime–Prime-Mediatorstruktur über `zeta_1`. C1w zeigt jedoch, dass **vollständige Eliminierung** eines der beiden Sternteile nicht die gesuchte globale Geometrie erzeugt.

### O13

Die positive nichtskalare C1u-Metrik bleibt ein gültiger Kandidat. Der zusätzliche kanonische Hub-Schurkomplement ist exakt berechenbar, führt aber im festen-Regulator-Scope zu trivialem Hubgrenzwert beziehungsweise divergentem Rest.

### O07

Bleibt OPEN. Der Hub-Feshbach-Test ist weiterhin translationinvariant und daher nicht kompakt.

---

# 9. Strukturelle Konsequenz

C1w lokalisiert den fehlenden Mechanismus weiter:

\[
\boxed{
\text{Objekt-X-Kompression kann weder}
\\
\text{(a) nur den Rest in den neutralen Hub eliminieren, noch}
\\
\text{(b) nur den Hub aus den Restsektoren eliminieren.}}
\]

Die erfolgreiche Struktur muss **beide Ebenen gleichzeitig behalten**, aber ihre Kopplung durch eine zusätzliche nichttranslationinvariante relative Geometrie verändern.

Das spricht gegen einen reinen Stern-Schurkomplement-Endpunkt und für eine echte **zweistufige Geometrie**:

\[
\text{Translations-/Inzidenzraum}
\quad\leftrightarrow\quad
\text{BC-Sternraum}
\quad\leftrightarrow\quad
\text{zusätzliche relative/archimedische Kompressionsschicht}.
\]

---

## 10. Nächster atomarer Knoten

\[
\boxed{\text{P11-C1x: Gibt es einen source-kanonischen }R\text{-abhängigen Schur-Skalenparameter }c_R?}
\]

Nicht rückwärts zu wählen, sondern ausschließlich aus vorhandenen Daten abzuleiten. Kandidaten dürfen nur aus bereits kanonischen Größen stammen, etwa:

1. effektive BC-GCD-Dimension / Framegröße;
2. source-induzierter Labelcutoff `N_R`;
3. Gamma-Inzidenzmasse auf derselben `D_s`-Skala;
4. eine echte relative Projektion, falls sie neu konstruiert wird.

Zu testen ist, ob irgendeine solche Skala gleichzeitig

- den Hub-Screening-Limes nichttrivial macht,
- den Rest beschränkt,
- die Weil-Halbgewichte nicht rückwärts verändert,
- und die Translationinvarianz ausreichend bricht beziehungsweise eine nachgeschaltete kompakte Ebene zulässt.

P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal.
