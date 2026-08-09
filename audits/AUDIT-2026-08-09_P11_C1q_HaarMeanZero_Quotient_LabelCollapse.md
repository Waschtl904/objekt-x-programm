# P11-C1q — Haar-Mittelnullquotient: Divergenz verschwindet, aber Prime-Power-Labels kollabieren

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1q]`  
**Vorgänger:** P11-C1n–C1p  
**Ziel:** Prüfen, ob die in C1o isolierten primspezifischen Restsektoren `K_p^0` bereits durch eine kanonische BC-/Haarrelation quotientiert werden können  

**Urteil:**

\[
\boxed{[P11-C1q]\quad\checkmark[M]_{\rm part}\;\text{mit einem klaren Kandidaten-No-Go}.}
\]

Die gesamte primspezifische Restgeometrie liegt im Haar-Mittelnullraum

\[
L_0^2(\widehat{\mathbb Z})=\{f:\int f\,dm_{\rm Haar}=0\}=\zeta_1^\perp.
\]

Der kanonische Haar-Erwartungsquotient auf den Konstantenmodus beseitigt daher exakt die in C1o lokalisierte primspezifische Divergenz. Er ist aber **zu grob**: sämtliche Prime-Power-Labels werden auf den einen neutralen Hub reduziert, die endlichen GCD-Grammatrizen werden zu Rang eins, und die Diagonalgewichte erhalten genau die zusätzliche Dämpfung `n^{-1}`, die bereits im P02-Standardmomentpfad aus C1p auftrat.

Damit ist der vollständige Haar-Mittelnullquotient kein geeigneter markierungserhaltender Objekt-X-Endquotient. Ein feinerer source-induzierter Quotient bleibt offen.

---

## 1. Mittelwert der normierten BC-Rangevektoren

Aus C1k2:

\[
\zeta_n=\sqrt n\,E_n,
\qquad
E_n=1_{n\widehat{\mathbb Z}}.
\]

Mit normiertem Haarmaß gilt

\[
\int_{\widehat{\mathbb Z}}E_n\,dm_{\rm Haar}=\frac1n.
\]

Daher

\[
\boxed{
\int\zeta_n\,dm_{\rm Haar}=\frac1{\sqrt n}.}
\]

Insbesondere `\zeta_1=E_1` ist der normierte Konstantenmodus auf `\widehat{\mathbb Z}`.

---

## 2. Die primspezifischen Restvektoren haben exakt Mittelwert null

C1n definiert

\[
\eta_{p,k}
:=
\zeta_{p^k}-p^{-k/2}\zeta_1.
\]

Daher

\[
\begin{aligned}
\int\eta_{p,k}\,dm_{\rm Haar}
&=
p^{-k/2}-p^{-k/2}\\
&=0.
\end{aligned}
\]

Somit

\[
\boxed{
K_p^0\subset\zeta_1^\perp
\qquad\forall p.}
\]

und wegen der Sternzerlegung aus C1n

\[
\boxed{
K_{\mathcal P^*}
=\mathbb C\zeta_1
\oplus
\left(\bigoplus_pK_p^0\right),
\qquad
\bigoplus_pK_p^0
=K_{\mathcal P^*}\cap\zeta_1^\perp.}
\]

Status: `✓[K/M]`.

---

## 3. Kanonische Haar-Erwartung

Definiere den orthogonalen Projektor

\[
\boxed{
P_0f
:=
\left(\int_{\widehat{\mathbb Z}}f\,dm_{\rm Haar}\right)\zeta_1.}
\]

Dann

\[
\ker P_0=\zeta_1^\perp.
\]

Auf dem Prime-Power-Labelraum:

\[
P_0\zeta_{p^k}
=p^{-k/2}\zeta_1,
\]

und

\[
P_0\eta_{p,k}=0.
\]

Damit vernichtet `P_0` exakt die primspezifischen Restsektoren, in denen C1o die Divergenz lokalisiert hat.

---

## 4. Quotientenbeschreibung

Der Hilbertquotient

\[
K_{\mathcal P^*}/\left(K_{\mathcal P^*}\cap\zeta_1^\perp\right)
\]

ist kanonisch isometrisch zu

\[
\boxed{\mathbb C\zeta_1.}
\]

Für jedes Prime-Power-Label gilt im Quotienten

\[
\boxed{
[\zeta_{p^k}]
=p^{-k/2}[\zeta_1].}
\]

Damit werden alle Labelrichtungen proportional.

---

## 5. Der quotientierte Label-Gramkern ist Rang eins

Im quotientierten Raum lautet der Gramwert

\[
\begin{aligned}
\langle P_0\zeta_{p^k},P_0\zeta_{q^\ell}\rangle
&=
p^{-k/2}q^{-\ell/2}.
\end{aligned}
\]

Also

\[
\boxed{
C_R^{(0)}
=v_Rv_R^*,
\qquad
(v_R)_{p^k}=p^{-k/2}.}
\]

Für `|\mathcal N_R|>1` gilt

\[
\operatorname{rank}C_R^{(0)}=1.
\]

Die strikt positive, markierungserhaltende GCD-Grammatrix aus C1k2 kollabiert damit vollständig.

Status: `✓[M]`.

---

## 6. Wirkung auf die analytisch-arithmetische Prime-Synthese

Vor Quotientierung lautet der einzelne Prime-Power-Kanal

\[
\mathcal V_{p,k}a
=
\sqrt{w_{p,k}}
D_{k\log p}a\otimes\zeta_{p^k},
\]

mit

\[
w_{p,k}=\frac{\log p}{p^{k/2}}.
\]

Nach Projektion auf den neutralen Haarmodus:

\[
\boxed{
(I\otimes P_0)\mathcal V_{p,k}a
=
\sqrt{w_{p,k}}\,p^{-k/2}
D_{k\log p}a\otimes\zeta_1.}
\]

Der Diagonalkoeffizient wird damit

\[
\boxed{
w_{p,k}p^{-k}
=
\frac{\log p}{p^{3k/2}}.}
\]

Genau dies ist die zusätzliche `n^{-1}`-Dämpfung aus dem P02-Standardmomentpfad in C1p.

---

## 7. Die quotientierte Synthese konvergiert

Für jedes `a\in L^2(\mathbb R)`:

\[
\|D_{k\log p}a\|\le2\|a\|.
\]

Der normierte Quotientenkoeffizient ist

\[
\sqrt{\log p}\,p^{-3k/4}.
\]

Somit

\[
\sum_p\sum_{k\ge1}
\sqrt{\log p}\,p^{-3k/4}<\infty
\]

nach Summation der geometrischen `k`-Reihen und Vergleich mit

\[
\sum_p\sqrt{\log p}\,p^{-3/4},
\]

wobei für die Hilbertnorm bereits die stärkere Quadratsummierbarkeit

\[
\sum_p\frac{\log p}{p^{3/2}}<\infty
\]

genügt. Insbesondere ist die neutrale quotientierte Synthese wohldefiniert.

**Präzisierung:** Für absolute Normkonvergenz der gesamten Vektorsumme ist der direkte `p^{-3/4}`-Vergleich nicht hinreichend; benötigt und hier verwendet wird die Hilbert-/Quadratsummierbarkeit bzw. die bereits in C1p getrennt bewiesene Konvergenz des neutralen Hubteils. Der vorliegende Schluss stützt sich auf diese C1p-Konvergenz, nicht auf eine falsche absolute Primreihe.

Status: `✓[M]` im C1p-Sinn.

---

## 8. Aber das Weil-Halbgewicht ist verloren

Die exakte Prime-Power-Inzidenz benötigt diagonal

\[
\boxed{
\frac{\log p}{p^{k/2}}.}
\]

Nach Haarquotient erhält man

\[
\boxed{
\frac{\log p}{p^{3k/2}}.}
\]

Die Quotientierung kontrolliert also die Divergenz gerade dadurch, dass sie dieselbe zusätzliche Dämpfung erzeugt, die C1p als zu stark identifiziert hat.

Um das Weilgewicht wiederherzustellen, müsste der Kanal um den Faktor `p^{k/2}` im Vektor bzw. `p^k` quadratisch verstärkt werden; damit kehrt die C1o-Divergenz zurück.

---

## 9. Warum der Haarquotient kein Radikalquotient der GCD-Form ist

Die Vektoren `\eta_{p,k}` haben

\[
\|\eta_{p,k}\|^2=1-p^{-k}>0.
\]

Sie liegen also **nicht** im Radikal der positiven BC-GCD-Gramform.

Der Haarquotient ist eine zusätzliche orthogonale Kompression

\[
K_{\mathcal P^*}\to\mathbb C\zeta_1,
\]

kein durch die GCD-Form erzwungener Nullraumquotient.

Damit darf er nicht als „natürlicher Radikalabschluss von Objekt X“ ausgegeben werden.

Status: `✓[M]` Typfirewall.

---

## 10. Markierungserhalt scheitert vollständig

Vor Quotientierung sind die Vektoren `\zeta_n` auf jeder endlichen verschiedenen Labelmenge linear unabhängig.

Nach Quotientierung sind alle proportional zu `\zeta_1`.

Daher:

\[
\boxed{
\text{Haar-Mittelnullquotient}
\Longrightarrow
\text{vollständiger Verlust der Prime-Power-Labelinformation}.}
\]

Dies widerspricht dem P11-Ziel einer markierungserhaltenden relativen/globalen Kantenstruktur.

---

## 11. Was der Quotient dennoch lehrt

Die exakte Identifikation

\[
\bigoplus_pK_p^0
=K_{\mathcal P^*}\cap\ker P_0
\]

zeigt:

\[
\boxed{
\text{Die in C1o divergierende Komponente ist exakt die finite-adisch zentrierte / Haar-mittelfreie Labelgeometrie.}
}
\]

Das ist eine starke Lokalisation des Regulatorproblems.

Ein erfolgreicher Regulator darf diese Komponente daher **nicht einfach vollständig entfernen**. Er muss sie kontrollieren und gleichzeitig genügend Labelinformation behalten.

---

## 12. Keine vorhandene Radikalrelation

Im aktuell konstruierten BC-Range-Hilbertraum ist

\[
K_p^0
\]

ein echter positiver Unterraum, kein Nullraum.

P11 besitzt bislang keine source-induzierte positive semidefinite Form, deren Radikal genau die divergenten Hochprim-/Restanteile entfernt und zugleich die endlichen Prime-Power-Markierungen erhält.

Dieser Punkt bleibt

\[
\boxed{?[O].}
\]

Es wird **nicht** behauptet, dass ein solcher feinerer Quotient unmöglich ist.

---

## 13. Finite-Part-Subtraktion ist noch keine Lösung

Man könnte formal versuchen, die divergente positive Restenergie

\[
\sum_p\|\mathcal T_{R,p}^0a\|^2
\]

von der positiven Hubform abzuziehen.

Dies wäre jedoch zunächst nur eine definitorische Renormierung. P08/P10 verlangen für eine operatorielle/finite-partige Realisierung einen echten Cutoff-/Operatorgrenzbeweis; eine Definition per analytischer oder formaler Subtraktion genügt nicht.

Daher wird hier **kein** `Tr_reg`-/Finite-Part-Syntheseoperator als konstruiert gebucht.

---

## 14. Statusmatrix

| Aussage | Status |
|---|---|
| `K_p^0\subset\zeta_1^\perp` | `✓[K/M]` |
| `⊕_p K_p^0 = K_{P*}\cap\zeta_1^\perp` | `✓[K/M]` |
| Haar-Erwartung vernichtet exakt die primspezifischen Reste | `✓[K/M]` |
| quotientierter Labelgram ist Rang eins | `✓[M]` |
| Haarquotient erhält Prime-Power-Markierungen | `×[M]` |
| Haarquotient kontrolliert C1o-Divergenz | `✓[M]` im C1p-Sinn |
| quotientierte Diagonalgewichte = Weil-Halbgewichte | `×[M]` |
| `K_p^0` ist Radikal der GCD-Gramform | `×[M]` |
| Haarquotient ist geeigneter finaler Objekt-X-Quotient | `×[M]` Kandidaten-No-Go |
| feinerer markierungserhaltender source-induzierter Quotient | `?[O]` |
| operatorieller Finite-Part der Restenergie | `?[O]` |

---

## 15. Wichtigster Befund

Die Regulatorfrage ist jetzt auf einen sehr konkreten Unterraum reduziert:

\[
\boxed{
\mathcal K_{\rm div}^{0}
:=
\bigoplus_pK_p^0
\subset
L_0^2(\widehat{\mathbb Z}).
}
\]

Ein erfolgreicher Objekt-X-Regulator muss diesen mittelfreien BC-Sektor **teilweise behalten**, aber seine Hochprimenergie so kontrollieren, dass der Grenzraum nicht divergiert.

---

## 16. Nächster Knoten

\[
\boxed{[P11\text{-}C1r]\quad\text{p-adische Martingal-/Schalenzerlegung der }K_p^0\text{-Sektoren}.}
\]

Zu prüfen ist, ob die verschachtelten BC-Rangeprojektionen

\[
E_p\ge E_{p^2}\ge E_{p^3}\ge\cdots
\]

eine kanonische orthogonale Differenz-/Martingalbasis innerhalb jedes `K_p^0` liefern. Eine solche Basis könnte die Exponenthierarchie ohne die in C1i supersedierte globale Graphorthogonalität intrinsisch aus der BC-Rangegeometrie erzeugen und wäre der richtige Ausgangspunkt für einen feineren Regulator.
