# Objekt X — exakter Grenznachweis auch für die Drei-Cut-Relaxation

3. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN  
Root: **UNRESOLVED**. Ausschließlich lokales Folgepaket.

## Ergebnis

**Der übermittelte Zwei-Cut-Grenznachweis ist nachgerechnet. Auch nach Hinzufügen des beschriebenen gemischten H₀-Cuts lässt sich der benötigte uniform positive F-Randwert in dieser letzten Koeffizientenrelaxation nicht beweisen.**

Ein neuer exakter Punkt erfüllt alle drei notwendigen Cuts strikt, liegt in den geerbten Koeffizientenintersektionen und hat bei erlaubtem Ausgangsrest null ein auf der ganzen reellen Achse negatives Surrogat. Er entsteht aus dem übermittelten Punkt durch nur eine zusätzliche Änderung: ε₃₅=−1, also Y₅₄ am unteren Root-Intervallrand.

Damit ist für genau diese Relaxation bereits vor einer größeren Drei-Multiplikatorsuche ein Hindernis bewiesen. Der Punkt ist selbst unzulässig: Die entgegengesetzte gemischte H₀-Richtung schließt sämtliche freien A-seitigen Vervollständigungen aus. Daraus folgt keine Unmöglichkeit für die tatsächliche Root-Familie.

## 1. Bestätigte Ausgangsbefunde

Der übermittelte Punkt hat ε₃₈=ε₃₉=1, ε₄₇=−1 und alle übrigen dargestellten Eingabesymbole null. Die Rekonstruktion bestätigt exakt:

- Beide bisherigen Cuts sind strikt positiv: Ψ₅>9,14·10⁻⁶ und Ψ₆>0,00256.
- Alle drei Surrogatkoeffizienten erfüllen die gespeicherten geerbten Koeffizientenintersektionen.
- Der führende Koeffizient ist negativ, die normierte Diskriminante liegt unter −0,0217 und das globale Maximum des Surrogats unter −0,00397.
- Alle sechs H₀-Diagonaluntergrenzen sind positiv; sieben Zweier-Hauptminoren haben negative obere Grenzen.
- Für z₊=e₄+(17/1000)e₅ ist die universelle obere Grenze von z₊ᵀH₀z₊ kleiner als −2,5·10⁻⁹.
- Der ungekürzte Stift hat eine positive Diskriminante; alle drei Koeffizientenkorrekturen liegen innerhalb der gespeicherten Fehlerradien.

Der daraus rekonstruierte gemischte Cut enthält 88 lineare und 260 quadratische Nichtnullterme in 88 ursprünglichen Symbolen. Sein Wert am übermittelten Punkt liegt ebenfalls unter −2,5·10⁻⁹. Alle 19 Domänen wurden exakt übertragen; die fünf bekannten vollständigen Punktfälle besitzen positive untere Cut-Grenzen. Keine ganze Fallbox wird ausgeschlossen.

Die im anderen Chat verlinkten neuen Skripte und JSON-Dateien wurden hier nicht als Dateien mitgeliefert. Eine Bytegleichheit mit jenem Folgepaket wird deshalb nicht behauptet. Nachgerechnet werden dessen mathematische Angaben und die angegebene Cut-Konstruktion aus unseren gebundenen Quellen.

## 2. Der zusätzliche Drei-Cut-Zeuge

Die vollständige Belegung lautet

\[
\varepsilon_{35}=-1,\quad \varepsilon_{38}=1,\quad
\varepsilon_{39}=1,\quad \varepsilon_{47}=-1,
\qquad \varepsilon_i=0\text{ für alle übrigen dargestellten Symbole}.
\]

Die Symbolkennungen sind die ursprünglichen, nicht fortlaufenden Kennungen der 156 Eingaben.

| Eintrag, Indizes ab 1 | Festlegung |
|---|---|
| Y₅₄, Symbol 35 | Unterer Intervallrand; einzige zusätzliche Änderung |
| Y₅₇, Symbol 38 | Oberer Intervallrand |
| Y₅₈, Symbol 39 | Oberer Intervallrand |
| Y₆₇, Symbol 46 | Mittelpunkt |
| Y₆₈, Symbol 47 | Unterer Intervallrand |

Alle anderen dargestellten Y-Einträge und die unkomprimierten B-seitigen Matrizen stehen an ihren tatsächlichen Intervallmitten. Die nicht dargestellten A-seitigen Größen bleiben frei. Die Zentrierung der Y-Inkremente im Kernel verändert weder Symbol noch Radius; der separate Audit prüft diese Zuordnung ausdrücklich.

### Alle drei Cuts sind strikt erfüllt

| Notwendige Bedingung | Wert ungefähr | Exakt geprüfte positive Reserve |
|---|---:|---:|
| Ψ₅ | 9,26679967372149·10⁻⁶ | > 9,26·10⁻⁶ |
| Ψ₆ | 0,002565841876077364 | > 0,00256 |
| Ψ_z₊ | 1,328569263700351·10⁻⁸ | > 1,32·10⁻⁸ |

Nach positiver Normierung durch 10²⁰ hat das gespeicherte Surrogat die Form P(s)=As²+Bs+C mit

\[
A\approx-1{,}3648698005820203,\qquad
B\approx0{,}12594035372462356,\qquad
C\approx-0{,}006882669621232034.
\]

Der rationale Audit bestätigt A<0, B²−4AC<−0,0217 und

\[
\max_{s\in\mathbb R}P(s)=C-\frac{B^2}{4A}
\approx-0{,}003977452455184451<-0{,}00397.
\]

Alle drei Koeffizienten liegen in ihren geerbten Intersektionen. Der Ausgangsrestvektor (0,0,0) ist in den drei individuellen symmetrischen Reststreifen erlaubt. Er wird ausdrücklich **nicht** als exakte höhere Korrektur des ursprünglichen Stifts ausgegeben.

## 3. Warum das den vorgeschlagenen Drei-Cut-Test entscheidet

Die hier untersuchte letzte Relaxation enthält genau die ursprüngliche Symbolbox, die drei notwendigen Bedingungen Ψ₅,Ψ₆,Ψ_z₊≥0, die individuellen symmetrischen Koeffizienten-Reststreifen und die geerbten individuellen Koeffizientenintersektionen. Weitere gemeinsame Rest-, Moment-, H₀- oder Stiftbedingungen sind in dieser Aussage nicht enthalten.

Am neuen Punkt ε* gilt für jedes feste reelle s und alle λ₅,λ₆,λ_z≥0:

\[
P(s;\varepsilon_*)-\lambda_5\Psi_5(\varepsilon_*)
-\lambda_6\Psi_6(\varepsilon_*)-\lambda_z\Psi_{z_+}(\varepsilon_*)-e(s)
\le P(s;\varepsilon_*)<0,
\]

wobei P und der unverändert bezahlte F-Rest e(s)≥0 durch denselben positiven Faktor 10²⁰ normiert sind. Die globale Untergrenze dieser Lagrange-Unterfunktion kann daher für keine Wahl der Multiplikatoren positiv sein. Auch eine exakte direkte Optimierung über die oben definierte Relaxation behält den negativen Punkt bei Rest null bei.

Dies ist ein algebraischer Existenznachweis für einen Relaxationszeugen, kein erfolgloser Suchlauf. Er gilt für alle reellen s und benötigt weder ein s-Raster noch eine vollständige numerische Multiplikatoroptimierung. Die vorgelagerte Punktsuche diente ausschließlich dem Finden des anschließend exakt verifizierten Punktes.

**Deshalb wurde keine größere Drei-Cut-Multiplikatorsuche ausgeführt.** Eine Verbesserung allein dieser Suche oder ihres Bereichsauswerters kann den benötigten positiven F-Randwert innerhalb derselben Relaxation nicht liefern.

Die Aussage betrifft weder sämtliche Root-Beweiswege noch die tatsächliche zulässige Operatorfamilie. Eine zusätzliche gemeinsame Bedingung oder eine gekoppelte Behandlung der höheren Reste beziehungsweise der definiten Stiftstruktur verändert die hier untersuchte Relaxation.

## 4. Der neue Punkt ist für alle freien A-Vervollständigungen unzulässig

Die vollständigen festgelegten Y-/B-Daten ergeben den exakten Transport

\[
C_T=(G_B+L_B/17)^{-1}Y^\top,\qquad D=C_T^\top G_BC_T.
\]

Die A-seitigen Einträge bleiben in ihren geerbten Intervallen. Der Audit prüft das Transportresiduum und sämtliche H₀-Eintragshüllen ohne die Inversion des Erzeugers zu übernehmen.

Alle sechs H₀-Diagonaluntergrenzen sind erneut positiv. Sieben Zweier-Hauptminoren haben negative obere Grenzen: (1,5), (2,5), (3,5), (4,5), (2,6), (3,6), (4,6).

Am neuen Punkt ist der gemischte Eintrag positiv:

\[
(H_0)_{45}\in[3{,}1255029636579916\cdot10^{-7},\,
3{,}142387509778572\cdot10^{-7}]
\]

(Dezimalwerte zur Orientierung). Entsprechend liefert die entgegengesetzte Richtung

\[
z_-=e_4-\frac{17}{1000}e_5
\]

für jede noch mögliche A-seitige Vervollständigung den exakten Ausschluss

\[
z_-^\top H_0z_-\le U_-
\approx-8{,}025135035944208\cdot10^{-9}
<-8\cdot10^{-9}.
\]

Der neue vollständige Punkt ist damit **CERTIFIED_INFEASIBLE**. Die wenigen genannten Y-Werte bei ansonsten freien Y-/B-Daten werden dadurch nicht ausgeschlossen.

Die ungekürzte Diskriminante ist nach derselben Normierung positiv, ungefähr 0,009300781888490135. Die normierten Korrekturen sind ungefähr

- ΔA = −0,00047033642074770454,
- ΔB = −0,00009725769297086269,
- ΔC = +0,0056859526359888946.

Alle liegen exakt innerhalb der gespeicherten Fehlerradien. Die Rechnung findet keinen unbezahlten Koeffizientenfehler und entscheidet keine dominante Fehlerursache auf der zulässigen Root-Familie.

## 5. Der nachgebaute gemischte Cut

Verwendet werden B=G_B+L_B/17, y_z=Yᵀz₊ und η=2499/2500. Rationale Gershgorin-Zeilensummen bestätigen G_B⪰ηI auf ganz Root. Für jeden festen rationalen w gilt die notwendige Bedingung

\[
\Psi_{z_+}=a_{z_+}^+-2w^\top y_z+w^\top G_Bw
+\frac2{17}w^\top L_Bw+\frac{\|L_Bw\|^2}{289\eta}\ge0.
\]

Dabei ist a_z⁺ die obere Intervallgrenze von zᵀG_Az mit den richtigen Vorzeichen aller Produkte zᵢzⱼ. Der feste Vektor w wird am übermittelten Punkt als B_*⁻¹G_B,*C_T,*z₊ gewählt und auf die nächste rationale Zahl mit Nenner 10¹⁶ gerundet; halbe Fälle werden nach oben gerundet. Alle erzeugten Koeffizienten sind exakt rational.

Die Herleitung folgt aus quadratischer Ergänzung, BG_B⁻¹B=G_B+2L_B/17+L_BG_B⁻¹L_B/289 und G_B⁻¹⪯η⁻¹I. Es entsteht kein zusätzlicher Taylor-Abbruchrest. Dass der Auswahlpunkt unzulässig ist, beeinträchtigt die für jedes feste w gültige Ungleichung nicht.

Der neue Zeuge zeigt konkret, dass dieser eine zusätzliche feste Richtungscut die Kopplung des H₀-Blocks (4,5) noch nicht erfasst. Eine gemeinsame Behandlung dieses Blocks ist daher ein begründeter nächster Prüfgegenstand. Die Ergänzung eines einzelnen gespiegelten Cuts könnte den gezeigten Punkt ausschließen; ihre ausreichende Stärke wäre damit noch nicht bewiesen. In diesem Paket werden weder ein vierter Cut noch ein neuer adaptiver Baum begonnen.

## 6. Prüfungen, Reproduktion und Herkunft

- Drei geschlossene Quellarchive samt Manifesten geprüft; keine Quelldatei verändert.
- Der gemeldete Punkt und der neue Punkt vollständig rational zurückgeführt; Kernel- und Transportresiduen exakt geprüft.
- Separater Audit aller 349 Koeffizienten des gemischten Cuts, beider globaler Negativitätsnachweise, der geerbten Koeffizientenintersektionen und der bezahlten Korrekturen.
- Fünf beschädigte Zertifikate verworfen: geändertes Symbol, falscher Transport, verfälschter Fehlerradius, falscher Surrogatkoeffizient und falscher Cut-Koeffizient.
- Separate direkte Rekonstruktion der Matrixformel auf allen 19 Domänen, zusätzlich zur Substitution des Erzeugers. Alle fünf bekannten vollständigen Punkte behalten positive untere Cut-Grenzen.
- Deterministische Punktsuche: zunächst 81 Punkte in den vier markanten Y-Koordinaten ohne Drei-Cut-Zeugen; anschließend 918 Belegungen mit einem zusätzlichen Eingabesymbol. 14 erfüllen die Drei-Cut-Zeugenbedingungen. Für den akzeptierten Nachweis genügt der oben dargestellte einzelne Punkt.
- Das ausgelieferte Paket wird über seinen Reproduktionswrapper erneut ausgeführt und verlangt Bytegleichheit aller acht Ergebnisquittungen.

Python 3.11 oder neuer; die Standardbibliothek wird unterstützt. Für die hier verwendete schnelle exakte Bruchrechnung:

```text
python -m pip install -r requirements.txt
python -B reproduce.py --out ../three-cut-replay
```

Der Wrapper rekonstruiert die neuen Zeugen, den Cut und die Domänen; er führt beide separaten Audits aus. Er wiederholt nicht den alten 783-Ziel-Lauf oder die alten Winkelrechnungen und erzeugt keine neuen Operatorintegrale. Die neun bisherigen bedingten Linien-/Winkelresultate, einschließlich slice/five_eighths ≤4,933780°, werden unverändert übernommen. Hier erfolgt keine neue Linien- oder Winkelpromotion.

Gebundene Quelle: PR #206, Head `c5c779d42a866db0b21ef02b18d3585e1a7450ec`. Eingabe-ZIP: `d1bad2d2edb730f34fab9b84a057938428f70acf2c8177a227e3529972b1abd4`; dessen Manifest: `9a4c8b8fff8c9c1c275d76855bd1373575af6b8c06eaecc0988cc308e47e552b`.

Die beiden Prüfer teilen den JSON-/Archivzugriff und den rationalen Zahlentyp mit dem Erzeuger; ihre Polynom-, Matrix- und Zertifikatsprüfungen sind separat implementiert. Die ursprünglichen Eingabeintervalle und Koeffizientenmodelle werden übernommen. Das ist keine vollständige neue Operatorrekonstruktion und keine externe Begutachtung.

Root, slice/two_thirds und die acht Diagnoseboxen bleiben UNRESOLVED; die acht Boxen sind keine Root-Überdeckung. GitHub, PR #187/A13 und der globale Verifikationssnapshot wurden nicht verändert. Allgemeines Renewal, kofinale Positivität, globales Objekt X und RH bleiben offen. Ein aktueller Live-GitHub-Stand wird nicht behauptet.
