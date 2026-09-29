# Kritischer Unterraum und relative Kopplung

28. September 2026 · lokaler Forschungsblock zu A₈ → A₉ und A₉ → A₁₁

## Ergebnis

Die vorgeschlagene Zerlegung lässt sich auf dem vollständigen Quellenraum konstruieren. Der alte Diagonalblock bleibt bei physischer Nullfortsetzung exakt erhalten: **Auf dieser Ebene gilt E = 0.** Für beide bekannten Übergänge wurde mit derselben Konstruktion die relative Kopplung κ eingeschlossen, jeweils für gerade und ungerade Quellen sowie einen, zwei und drei alte kritische Vektoren.

**In allen zwölf Fällen gilt κ < 1. Die Kopplung liegt allerdings sehr nahe an 1.** Bei drei Richtungen liegt der verbleibende relative Energierest 1−κ für A₈ → A₉ zwischen Größenordnungen 10⁻⁹ und 10⁻⁸, für A₉ → A₁₁ zwischen 10⁻¹⁵ und 10⁻¹⁴. Der zweite Übergang verschärft damit das Problem erheblich.

Diese Auswertung setzt die bereits vorliegenden vollständigen Zertifikate des **neuen** Terminals voraus. Dass κ < 1 gilt, ist unter dieser Voraussetzung grundsätzlich zu erwarten. Der neue Befund ist die quantitative Einschließung seines Abstands zu 1 für explizit festgelegte alte Quellenräume. **Ein von der neuen Terminalrechnung unabhängiger Erneuerungsbeweis liegt damit noch nicht vor.**

Die Rechnung bleibt lokal. Repository-Dateien, Main, historische Beweise, Registry und Verifikationssnapshot wurden nicht verändert. Es wurde keine weitere Kammer berechnet.

## 1. Festgelegte Daten und Quellenräume

Alle elf eingelesenen Repository-Dateien wurden byteweise gegen den Commit [`d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`](https://github.com/Waschtl904/objekt-x-programm/tree/d16ba43ebb20f2c61f43379fc65d7a9b9dba76de) geprüft. Dateipfade und SHA-256-Werte stehen in `coupling_bounds.json`.

Für jeden alten Terminal A und jede Parität werden die ersten r = 1, 2, 3 Vektoren aus dem vorausgehenden Strukturvergleich festgehalten. Ihre 70-stelligen Dezimalkoeffizienten in `critical_vectors.json` werden als **exakte rationale Zahlen** gelesen. Anschließend wird die alte Mellinbedingung durch die mathematisch exakte Momentkorrektur erfüllt; die benötigten Momente werden durch die ursprünglichen Intervalle eingeschlossen.

Damit ist

\[
K_A^{(r)}=\operatorname{span}\{v_{A,1},\ldots,v_{A,r}\}
\]

ein konkret definierter Quellenraum. Die drei Räume sind ineinander enthalten. Für ihre Auswahl werden keine Eigenvektoren des neuen Terminals verwendet. Die Koeffizienten-Grammatrix und die alte Form-Grammatrix wurden durch gerichtete LDL-Rechnung als positiv bestätigt.

**Grenze dieser Auswahl:** Die Richtungen stammen aus der Diagnose der alten hinreichenden Schur-Untergrenze F. Sie sind keine zertifizierte Spektralprojektion der tatsächlichen Form. Ein Spektralschwellenwert τ und ein belastbarer Gap auf dem alten Komplement sind noch nicht bewiesen. Der Raum selbst und seine positive alte Formenergie sind dagegen eingeschlossen.

Physisch wird durch Nullfortsetzung transportiert:

\[
W x=J_{A,B}\sum_{i=1}^r x_i v_{A,i}.
\]

Die neue Legendreentwicklung von W hat im Allgemeinen unendlich viele Koeffizienten. Die Rechnung schneidet diesen Anteil nicht ab: Neue niedrige Projektionen werden eingeschlossen; der vollständige übrige duale Anteil wird durch eine Gramidentität bezahlt, siehe Abschnitt 5.

## 2. Exakter alter Block und das richtige Schurkriterium

Für die hier betrachteten Terminals ist

\[
b_B(u,v)=q_B(u,v)+17\langle u,v\rangle
\]

eine vollständige positive Formnorm. Setze

\[
G=W^*W,\qquad S_{ij}=q_A(v_{A,i},v_{A,j}),\qquad
\mathsf B=S+17G.
\]

In diesem Bericht bezeichnet S die **alte Formenergie der ausgewählten Quellen**, nicht eine zuvor eliminierte F-Matrix. Die Formnaturality liefert exakt

\[
q_B(Wx,Wy)=x^*Sy.
\]

Mit N = (ran W)^{\perp_{b_B}}, dem b-orthogonalen Komplement des Bildraums von W, zerfällt die neue Form als

\[
q_B(Wx+n)=x^*Sx+2\operatorname{Re}(x^*Cn)+b_B(n,Dn).
\]

Dabei ist D der bezüglich b_B dargestellte Operator der eingeschränkten Form auf N. Wegen der Orthogonalität gilt die besonders einfache Formel

\[
(Cn)_i=q_B(W_i,n)=-17\langle W_i,n\rangle.
\]

**Hier gilt E = 0.** Wird anschließend ein weiterer Block eliminiert, verändert dessen Schurkorrektur auch den verbleibenden alten Diagonalblock. Exakter alter Block und bereits durchgeführte zusätzliche Elimination dürfen deshalb nicht zugleich ohne Korrektur behauptet werden.

Falls D ≥ dI mit d > 0 und S > 0, setze

\[
Z=S-CD^{-1}C^*,\qquad
\kappa=\|S^{-1/2}CD^{-1}C^*S^{-1/2}\|
=\|S^{-1/2}CD^{-1/2}\|^2.
\]

Dann gilt durch Quadratergänzung

\[
q_B(Wx+n)=x^*Zx+
\|D^{1/2}(n+D^{-1}C^*x)\|_{b_B}^2.
\]

Insbesondere liefert κ < 1 die relative Untergrenze Z ≥ (1−κ)S und strikte Positivität der vollständigen Form. Eine globale Normreserve erfordert zusätzlich die Normen der Koordinaten- und Scherabbildung.

### Was über D bereits bekannt ist

Aus dem vorhandenen neuen Terminalzertifikat q_B ≥ c_B I folgt

\[
\frac{c_B}{c_B+17}I\preceq D\preceq I
\quad\text{im b_B-Skalarprodukt}.
\]

| Neues Terminal | Verwendeter physischer Boden c_B | Geerbter Boden für D |
| --- | --- | --- |
| A₉ | 10⁻³⁵ | 1/(17·10³⁵ + 1) |
| A₁₁ | 10⁻⁵⁰ | 1/(17·10⁵⁰ + 1) |

Das ist ein positiver, aber sehr kleiner Boden. Er ist kein unabhängig aus alten Daten hergeleiteter robuster Komplement-Gap. Gerade diese Abhängigkeit verhindert derzeit die Nutzung als eigenständigen Fortsetzungsbeweis.

Die Zahl 17 gilt für die hier untersuchten Terminals. Bei beliebig großen endlichen Horizonten muss die Verschiebung gemäß dem allgemeinen Formnormsatz angepasst werden. Mit b = q + ρI ersetzen ρ, 2ρ und ρ² die folgenden Faktoren 17, 34 und 289.

## 3. Endliche Formel für die vollständige Kopplung

Eine Darstellung sämtlicher unendlicher C- und D-Koordinaten ist nicht erforderlich. Sei Q_B der positive selbstadjungierte L²-Operator der geschlossenen Form auf dem Mellin-nulligen Quellenraum. Seine beschränkte Inverse ist hier durch das vorhandene neue Terminalzertifikat verfügbar. Definiere

\[
T_{ij}=\langle W_i,Q_B^{-1}W_j\rangle,\qquad
R=S+34G+289T.
\]

Dann gilt exakt

\[
\boxed{Z=\mathsf B R^{-1}\mathsf B.}
\]

Begründung: Der durch q_B im b_B-Hilbertraum dargestellte Operator \(\mathcal A\) erfüllt \(\mathcal A^{-1}=I+17Q_B^{-1}\). Somit gilt \(R_{ij}=b_B(W_i,\mathcal A^{-1}W_j)\). Die inverse komprimierte Matrix ist der Schurrest in b-orthonormalen Quellkoordinaten. Die Rückkehr zu den ursprünglichen Quellkoeffizienten liefert die beiden Faktoren \(\mathsf B\).

Diese Faktoren sind wesentlich: Die ausgewählten Quellen sind nicht b-orthonormal. Daraus folgt

\[
1-\kappa=
\lambda_{\min}(S^{-1/2}ZS^{-1/2})
=\frac{1}{\lambda_{\max}(R\mathsf B^{-1}S\mathsf B^{-1})}.
\]

Das letzte Produkt ist zu einer positiv definiten symmetrischen Matrix ähnlich. Liegen R₋ ≤ R ≤ R₊ vor, so liefern

\[
t_- = \operatorname{tr}(R_-\mathsf B^{-1}S\mathsf B^{-1}),\qquad
t_+ = \operatorname{tr}(R_+\mathsf B^{-1}S\mathsf B^{-1})
\]

die konservativen Grenzen

\[
\boxed{\frac{1}{t_+}\le 1-\kappa\le\frac{r}{t_-}.}
\]

Alle Matrixprodukte, Inversen und Spuren wurden einschließlich der Eingabeunsicherheiten mit gerichteter Intervallarithmetik berechnet. Es wird keine punktgenaue κ-Zahl behauptet.

## 4. Gemessene Schranken

Die Tabelle zeigt **1−κ**, also die kleinste verbleibende Energie relativ zum alten S nach optimaler Komplementkorrektur. Beide Enden wurden für die Anzeige zusätzlich nach außen gerundet. Die exakten rationalen Schranken stehen in `coupling_bounds.json`.

| Übergang | Parität | r | Untergrenze für 1−κ | Obergrenze für 1−κ |
| --- | --- | ---: | ---: | ---: |
| A₈ → A₉ | gerade | 1 | 3.200·10⁻⁶ | 7.514·10⁻⁶ |
| A₈ → A₉ | gerade | 2 | 3.613·10⁻⁸ | 1.701·10⁻⁷ |
| A₈ → A₉ | gerade | 3 | 1.146·10⁻⁹ | 8.220·10⁻⁹ |
| A₈ → A₉ | ungerade | 1 | 5.377·10⁻⁶ | 1.171·10⁻⁵ |
| A₈ → A₉ | ungerade | 2 | 5.905·10⁻⁸ | 2.601·10⁻⁷ |
| A₈ → A₉ | ungerade | 3 | 1.842·10⁻⁹ | 1.229·10⁻⁸ |
| A₉ → A₁₁ | gerade | 1 | 3.134·10⁻¹¹ | 6.838·10⁻¹¹ |
| A₉ → A₁₁ | gerade | 2 | 7.680·10⁻¹⁴ | 3.369·10⁻¹³ |
| A₉ → A₁₁ | gerade | 3 | 1.031·10⁻¹⁵ | 6.819·10⁻¹⁵ |
| A₉ → A₁₁ | ungerade | 1 | 5.387·10⁻¹¹ | 1.213·10⁻¹⁰ |
| A₉ → A₁₁ | ungerade | 2 | 1.297·10⁻¹³ | 5.880·10⁻¹³ |
| A₉ → A₁₁ | ungerade | 3 | 1.844·10⁻¹⁵ | 1.261·10⁻¹⁴ |

Für den geraden dreidimensionalen Raum beim zweiten Übergang bedeutet dies etwa

\[
1-6.819\cdot10^{-15}\le\kappa\le1-1.031\cdot10^{-15}.
\]

Normale Maschinenzahlen würden solche Aussagen beim Subtrahieren von 1 unnötig ungenau wiedergeben. Deshalb wird der Abstand selbst gespeichert.

Die Resultate zeigen:

- Hohe geometrische Überlappung der Quellen garantiert keine komfortable relative Energiereserve.
- Die ganze Kopplung in das neue Komplement ist energetisch nahezu maximal, bezogen auf den alten kritischen Block.
- Die Erweiterung von einer auf drei alte Richtungen verbessert den kleinsten relativen Rest in diesen Rechnungen nicht. Daraus folgt keine allgemeine Monotonieaussage für beliebige Raumwahlen.
- Die zwölf positiven Reste liefern weder einen gemeinsamen Boden für alle künftigen Terminals noch ein unabhängiges Verfahren zu ihrer Fortsetzung.

## 5. Wie der vollständige hohe Raum bezahlt wird

Verwendet wird die vorhandene neue Zerlegung u = M(Ec+y). In ihren Koordinaten seien L der tatsächliche niedrige Block, B_h die tatsächliche Kopplung zum gesamten hohen Raum und δ der bewiesene hohe Boden. Es gelten

\[
F\preceq L-\delta^{-1}B_hB_h^*,\quad F>0,\qquad
B_hB_h^*\preceq H^{up},
\]

mit δ = 2/3 bei A₉ und δ = 1 bei A₁₁. Das gespeicherte Modell liefert

\[
\|L-L_0\|\le e_L,\qquad
H^{up}=\frac{1001}{1000}G_0+1001e_B^2I.
\]

Für eine Quelle Wz zerfällt ihr dualer Vektor bezüglich M in az im niedrigen und hz im vollständigen hohen Raum. Schreibe G_h = h* h. Die Variationsformel für Q_B⁻¹ liefert durch Beschränkung auf niedrige Testquellen

\[
T_- = a^*(L_0+e_LI)^{-1}a\preceq T.
\]

Für die Obergrenze wird die untere Form durch vollständige Quadratergänzung invertiert. Mit Young und
\(\|F^{-1/2}B_h\|^2\le\operatorname{tr}(F^{-1}H^{up})\) folgt

\[
T\preceq T_+:=
2a^*F^{-1}a+
\left(\frac{2\operatorname{tr}(F^{-1}H^{up})}{\delta^2}+\frac1\delta\right)G_h.
\]

Das ist eine Schranke für die ganze Resolvente. Sie ersetzt den hohen Raum nicht durch endlich viele Moden. Die Breite der resultierenden κ-Intervalle stammt auch aus dieser Young-Abschätzung, der Spurbeschränkung und den Modellfehlern; mehr Rechenstellen allein beseitigen sie nicht.

### Vollständige duale Gramidentität

Seien e der normierte Momentträger der Parität, m die neue cosh-/sinh-Momentfunktion und βᵢ = ⟨e,Wᵢ⟩. Die physische Nullfortsetzung erhält die Mellinbedingung exakt. Auf dem trägerfreien Raum hat die Momentkorrektur die Form M = I − e m*/⟨m,e⟩. Daher gilt

\[
\boxed{G_h=G+
\frac{\|m\|^2}{|\langle m,e\rangle|^2}\,\beta\beta^*-a^*a.}
\]

Das folgt aus ⟨m,Wᵢ⟩ = 0 und Parseval. Im normierten Referenzintervall ist \(\|m\|^2=(\sinh B/B\pm1)/2\). Die Differenz enthält alle hohen Koeffizienten der Nullfortsetzung, auch wenn diese unendlich viele sind.

Die niedrigen physischen Überlappungen sind Integrale von Polynomen. Die verwendeten 489 bzw. 583 Gauss-Legendre-Knoten reichen für deren exakte Integration; Knoten, Gewichte, Endpunkte und Koeffizienten werden durch Arb eingeschlossen. Zur stabilen Auswertung wird Pₙ am dyadischen Mittelpunkt des Argumentintervalls berechnet und die Argumentunsicherheit mit \(|P_n'|\le n(n+1)/2\) auf [−1,1] bezahlt.

## 6. Was der minimierende Graph tatsächlich aussagt

Der Graph

\[
\mathcal G=\{Wx-D^{-1}C^*x:x\in\mathbb R^r\}
\]

ist exakt der Raum der q-minimierenden Quellen bei festgehaltener b-Projektion auf den alten Raum. Er ist q-orthogonal zu N. Seine Form-Grammatrix ist Z.

Es gibt auch eine exakte Resolventendarstellung der minimierenden Quelle:

\[
u_{\min}(x)=(I+17Q_B^{-1})W R^{-1}\mathsf B x.
\]

**Dieser Graph ist nicht automatisch der neue spektrale kritische Raum.** In b-orthonormalen Blockkoordinaten erfüllt ein Eigenvektor des durch q in b dargestellten Operators mit Eigenwert 0 ≤ λ < d vielmehr

\[
n=-(D-\lambda I)^{-1}C^*x.
\]

Der Unterschied zum minimierenden Graphen ist beschränkt durch

\[
\|[(D-\lambda I)^{-1}-D^{-1}]C^*\|
\le\frac{\lambda}{d-\lambda}\|D^{-1}C^*\|.
\]

Für eine nützliche spektrale Aussage braucht man also einen quantitativ getrennten Komplement-Gap und Kontrolle des Eigenwertbereichs. Beides folgt nicht aus den bisherigen Winkelmessungen. Auch eine kleine L²-Norm der Graphkorrektur wurde hier nicht zertifiziert. Die einfache Schranke

\[
\|D^{-1}C^*x\|_{L^2}^2
\le c_B^{-1}x^*(S-Z)x
\]

ist wegen des winzigen verwendeten c_B dafür zu schwach. Die Rechnung kontrolliert die relative Formenergie der Korrektur, nicht bereits deren kleine räumliche Größe.

## 7. Prüfung und nächster Forschungsengpass

Tatsächlich ausgeführt wurden:

1. Alle zwölf Schranken mit python-flint 0.9.0 und 1024-Bit-Arb-Arithmetik.
2. Alle zwölf Schranken erneut mit 1280 Bit und jeweils acht zusätzlichen Gauss-Knoten. Die Intervalle überlappen; sämtliche angezeigten Ergebnisziffern stimmen überein.
3. Acht unabhängige Prüfungen mit exakter rationaler Standardbibliotheksarithmetik: sechs nichtorthogonale Block-/Graph-Beispiele, die vollständige duale Mellin-Gramidentität sowie eine gekoppelte Low-/High-Resolventenprüfung.
4. Erneute Kontrolle aller elf Repository-Eingaben gegen den gepinnten Commit und SHA-256-Bindung der alten Vektoren.

Die endlichen rationalen Beispiele prüfen die Normalisierung und Umsetzung der Formeln. Die allgemeinen Aussagen beruhen auf den angegebenen Herleitungen. Der vollständige ursprüngliche Aufbau der drei Terminalmodelle und deren ursprüngliche Zertifikatsprüfungen wurde in diesem Block nicht erneut ausgeführt; sie sind gebundene Voraussetzungen. Die hochpräzise Wiederholung verwendet dieselbe Intervallbibliothek und ist keine zweite unabhängige Implementierung.

**Der nächste notwendige Schritt ist jetzt genauer eingegrenzt:** Ein geeigneter mitgeführter kritischer Raum muss einen belastbaren Komplement-Gap ermöglichen, und die relative Kopplung muss aus alten Daten plus analytischen Wand-/Tail-Abschätzungen kontrolliert werden. Das Einsetzen der bereits bewiesenen neuen Gesamtpositivität muss dabei entfallen. Zusätzlich ist für eine Dynamik des kritischen Raums dessen spektrale Nähe zum minimierenden Graphen zu zeigen.

Die Rechnung liefert dafür eine Warnung an jede Abschätzung: Der relevante Abstand liegt bereits beim zweiten bekannten Übergang bis hinunter zur Größenordnung 10⁻¹⁵. Eine grobe absolute Fehlerkontrolle wird voraussichtlich nicht genügen. Benötigt wird Kontrolle relativ zur alten kritischen Formenergie.

**Status:** lokale, an die bestehenden Terminalzertifikate gebundene Kopplungsschranken. Keine allgemeine Low-Schur-Erneuerung, kein neuer externer Review und keine globale Aussage zu Objekt X oder zur Riemannschen Hypothese.

## Paketinhalt

- `coupling_bounds.json`: vollständige primäre Intervallergebnisse und Eingabebindungen.
- `coupling_bounds_crosscheck.json`: Wiederholung mit höherer Präzision und mehr Knoten.
- `critical_vectors.json`: unveränderte alte rationale Vektoren aus dem Strukturvergleich.
- `critical_subspace_coupling.py`: tatsächlich ausgeführte Intervallrechnung.
- `verify_critical_subspace_coupling.py`: unabhängige rationale Formel- und Bindungsprüfung.
- `verification.json`: ausgeführte Prüfungen und Ergebnisvergleich.
- `REPRODUKTION.md`: Voraussetzungen, Aufrufe und Grenzen der Reproduktion.
- `SHA256SUMS`: Dateibindungen des fertigen Pakets.
