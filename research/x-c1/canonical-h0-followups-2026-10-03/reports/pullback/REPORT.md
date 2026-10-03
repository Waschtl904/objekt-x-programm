# Objekt X: Rücktest des Root-Relaxationszeugen

**3. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

**Ergebnis: `CERTIFIED_INFEASIBLE` für den vollständig angegebenen Symbolpunkt.**
Eine bereits geerbte Transportbedingung schließt ihn einschließlich aller noch
freien A-seitigen Vervollständigungen aus. **Root bleibt `UNRESOLVED`.**
Es gibt keinen neuen Operator-Gegenzeugen, keine Statuspromotion und keine
Änderung auf GitHub. PR #206 bleibt ein offener Entwurf.

## 1. Was geprüft wurde

Ausgangspunkt ist der von GPT 1 gelieferte Koeffizientenzeuge zu
[PR #206](https://github.com/Waschtl904/objekt-x-programm/pull/206), Head
`c5c779d42a866db0b21ef02b18d3585e1a7450ec`:

| Symbol | Tatsächliche Eingabe, Indizes ab 1 | Wert |
| --- | --- | --- |
| ε38 | Y57 | unterer Intervallrand |
| ε39 | Y58 | oberer Intervallrand |
| ε46 | Y67 | unterer Intervallrand |
| ε47 | Y68 | unterer Intervallrand |

Die Zuordnung wurde aus den ausgeführten Eingabekonstruktoren der gebundenen
Engine erfasst und separat gegen die Quelldaten geprüft. Insgesamt sind
**156 Eingabesymbole mit Labels zwischen 0 und 239, mit Lücken**, vorhanden:
48 Y-Einträge sowie jeweils 36 symmetrische Einträge von G_B, L_B und Z_B.
Die Zahl 156 ist keine obere Labelgrenze.

Alle weiteren dargestellten Symbole sind wie im Auftrag null. Damit sind
die übrigen Y-Einträge und die B-seitigen Matrizen durch ihre tatsächlichen
Intervallmitten festgelegt. Dies folgt aus der ausdrücklich gegebenen
Symbolbelegung. **G_A, L_A, Z_A und andere nicht dargestellte Größen bleiben
in ihren geerbten Einschlüssen frei.** Für sie wurde keine Punktvervollständigung
erfunden. Rundungsreste sind Rechenfehlerhüllen und keine zusätzlichen frei
gewählten Operatorinputs.

Der Ausgangspunkt verwendet die vollständigen, nach Stage A und Y68 bereits
intersektierten Eingabeintervalle der Root.

## 2. Der entscheidende Ausschluss

Die geerbte notwendige Bedingung lautet mit der gemeinsamen Transportmatrix C:

```math
C=(G_B+L_B/17)^{-1}Y^\top,
\qquad H_0=G_A-C^\top G_B C\succeq0.
```

Sie steht bereits im
[geerbten Box-Checker, Methode `transport`](https://github.com/Waschtl904/objekt-x-programm/blob/c5c779d42a866db0b21ef02b18d3585e1a7450ec/research/x-c1/canonical-odd-structural-open-2026-10-01/04-rational-box-gate/box_math.py).
Die entsprechende Quelldatei ist auch im versiegelten Eingabepaket enthalten.

C wurde rational berechnet und die Gleichung
`(G_B+L_B/17) C = Y^T` exakt geprüft. Für jede noch mögliche A-seitige
Vervollständigung gilt daher

```math
(H_0)_{ii}\le (G_A)_{ii}^{\mathrm{oberer\ Rand}}-(C^\top G_B C)_{ii}=:U_i.
```

Der Prüfer und ein separater rationaler Audit bestätigen exakt:

```math
U_5<-\frac{11}{10^6}<0,
\qquad U_6<-\frac{43}{4000}<0.
```

Zur Orientierung: U5 ≈ −0,00001103040426103039 und
U6 ≈ −0,01075154433708879. Die Entscheidungen beruhen auf den vollständigen
rationalen Zahlen in `PULLBACK.json` und `PULLBACK_AUDIT.json`.

Eine positiv semidefinite Matrix kann keine negative Diagonale haben.
Schon eine dieser beiden Ungleichungen schließt den vollständigen Symbolpunkt
aus. Weitere Bedingungen können diese Verletzung nicht reparieren. Der
Ausschluss benötigt weder neue Operatorintegrale noch eine Einschränkung
der bisher freien A-seitigen Daten.

**Die vier Y-Randwerte allein sind damit nicht ausgeschlossen.** Ein zusätzlicher
Test fixierte nur diese vier Werte und ließ alle anderen Eingabeintervalle
frei. Der geerbte Intervallfilter fand dann weder eine negative Diagonalobergrenze
noch einen negativen oberen Zweier-Hauptminor von H0 oder Hν. Das ist
`NOT_EXCLUDED`, kein Existenznachweis. Der zertifizierte Ausschluss betrifft
die vollständige Symbolbelegung des gelieferten Zeugen.

## 3. Ungekürzter Stift und gemeinsame Korrektur

Für die festgelegten Eingaben wurden ohne Taylor-Abbruch rational berechnet:

```math
X=-Y_L^{-1}Y_R,\quad N=\begin{bmatrix}X\\I\end{bmatrix},\quad
G=N^\top G_BN,\quad L=N^\top L_BN,\quad Z=N^\top Z_BN,
```

sowie R, M_tilde und die drei Koeffizienten der Liniengleichung nach
[PROOF.md](https://github.com/Waschtl904/objekt-x-programm/blob/c5c779d42a866db0b21ef02b18d3585e1a7450ec/research/x-c1/canonical-y-kernel-second-order-2026-10-03/PROOF.md).
Beide linearen Systeme haben exakt verschwindende Residuen. Die komprimierten
G-, L- und M_tilde-Matrizen sind an diesem algebraischen Punkt positiv definit.

Nach Division der Liniengleichung durch 10^20 ergeben sich folgende
**Darstellungswerte**; die Rechnung verwendet ausschließlich rationale Zahlen:

| Koeffizient | Gespeichertes Grad-zwei-Polynom | Ungekürzte Rechnung | Korrektur |
| --- | ---: | ---: | ---: |
| A | −1,5053666397890604 | −1,484307484490109 | +0,021059155298951478 |
| B | +0,09787222986530487 | +0,12680225252341829 | +0,028930022658113418 |
| C | −0,004463560994481951 | −0,0012209174244331236 | +0,003242643570048827 |

Die Diskriminante des Surrogats ist exakt kleiner als −0,01729. In der
ungekürzten Rechnung ist sie positiv, ungefähr **0,008829943760890852**.
Jede der drei Korrekturen liegt innerhalb ihres gespeicherten Fehlerradius.
Die Ausgabe-Reste können an diesem festgelegten Eingabepunkt also nicht
unabhängig als null gewählt werden, wenn sie die exakte Rechnung darstellen sollen.

Das bestätigt eine verlorene Abhängigkeit innerhalb der letzten Relaxation.
Der Punkt ist zugleich durch H0 unzulässig. Daher liefert diese Rechnung
**keine zulässige Vervollständigung** und entscheidet nicht, wie groß der
Einfluss höherer Terme auf der zulässigen Root-Familie ist.

## 4. Die gelieferte Neumann-Diagnose ist reproduziert

Aus den gespeicherten H- und q-Schranken wurde die rationale Lösung
`t* = (I−M)^−1 M² b` erneut berechnet. Das 6×6-System mit zwei rechten Seiten
ist exakt erfüllt. In allen zwölf Komponenten liegt t* zwischen null und
der gespeicherten Schranke. Die maximale relative Verbesserung stimmt exakt
mit der gelieferten JSON-Quittung überein und ist kleiner als **1,5 × 10^−12**.

Dies betrifft die Summationsreserve derselben nichtnegativen Vergleichsreihe.
Es bewertet weder den wahren signierten Rest noch seine Verstärkung in der
Liniengleichung.

## 5. Vergleich auf denselben 19 Fällen

Verglichen wurden die gespeicherte Auswertung und eine gemeinsame Auswertung
jedes linearen Terms mit seinem zugehörigen Diagonalquadrat. Die vollständigen
gespeicherten Fehlerradien bleiben erhalten. Rationale Extremwerte werden
nach außen auf Vielfache von 10^−90 gerundet; auch Newton-Bilder werden
nach außen gerundet. Diese zusätzliche Rundung ist einschließend.

Zusätzlich wurde jede Variante mit dem geerbten gemeinsamen H0/Hν-Filter
für die gesamte jeweilige Eingabebox kombiniert. Alle 19 Boxen überleben
diesen Vorfilter, sodass die beiden Varianten mit Vorfilter jeweils dieselben
Resultate wie ihre Variante ohne Vorfilter liefern.

| Fallgruppe | Bisherige Auswertung | Gruppierte Auswertung |
| --- | --- | --- |
| Root | offen | offen |
| Fünf vollständige geerbte Punkte | alle maximal isoliert | alle maximal isoliert |
| Schnitt central | ≤ 2,933357° | ≤ 2,933357° |
| Schnitt quarter | ≤ 3,070163° | ≤ 3,070163° |
| Schnitt half | ≤ 3,642693° | ≤ 3,642652° |
| Schnitt five_eighths | offen | offen |
| Schnitt two_thirds | offen | offen |
| Acht Diagnoseboxen | alle offen | alle offen |

Die dargestellten Winkelobergrenzen sind nach oben auf sechs Nachkommastellen
gerundet. Es handelt sich um physische Gesamtwinkel zur unveränderten
Referenz. Alle Einzelwerte, Randvorzeichen, Ableitungseinschlüsse, Newton-Schritte
und physischen Winkelhüllen stehen in `FACTOR_COMPARISON.json`.
Der separat erwähnte frühere five_eighths-Folgeaudit ist nicht Bestandteil
dieser Rechnung.

**Grenze dieses Vergleichs:** Ein Vorfilter der vollständigen Box optimiert
F noch nicht über die durch H0/Hν eingeschränkte gemeinsame Symbolmenge.
Dieser stärkere Teil des vorgeschlagenen Faktorvergleichs ist hier nicht
implementiert. Die Gleichheit der Vorfiltervarianten widerlegt seine mögliche
Wirksamkeit nicht. Der vollständige Zeuge wird beim punktweisen Rücktest
ausgeschlossen, obwohl der gröbere Boxfilter die Root weiterhin durchlässt.

## 6. Prüfungen und Reichweite

- Zwei vollständige Läufe dieses Diagnoseprüfers erzeugen bytegleiche
  `PULLBACK.json`- und `FACTOR_COMPARISON.json`-Dateien.
- 361 Kontrollen der eindimensionalen Extremwertformel, 15 Kontrollen
  gerichteter Rundung, drei Inversenkontrollen und zwei H0-Kontrollen.
- Symbolumbenennung um +10000 reproduziert die gelieferten Koeffizienten.
- Separater rationaler Pullback-Audit: 156 Eingaben, beide linearen Systeme,
  drei komprimierte Matrizen, drei bezahlte Korrekturen und die beiden
  universellen H0-Diagonalausschlüsse bestätigt.
- Separater Auswertungsaudit: 19 Fälle, 64 Tripel aus Randwerten und Ableitung,
  acht maximale Wurzelzertifikate und 35 Newton-Schritte.
- Elf Winkelumrechnungen durch Arb mit 768 Bit nach außen geprüft.

Die originalen Operatorquellen und Eingabekonstruktoren werden übernommen;
die neue rationale Rückrechnung und ihre Quittungen werden separat geprüft.
Es gab keinen unabhängigen Neuaufbau der Operatorintegrale, keinen neuen
adaptiven Baum und keinen vollständigen Neuaufbau aller ursprünglichen
Koeffizientenmodelle. Die acht Diagnoseboxen sind keine Überdeckung der Root.

## 7. Konsequenz für den nächsten Versuch

Der Rücktest benennt einen konkreten bereits vorhandenen Ausschluss:
**die gemeinsamen H0-Diagonalbedingungen für die Spalten 5 und 6.**
Sie sind ein begründeter Ausgangspunkt für eine Verschärfung der letzten
Relaxation. Dazu müssen die Transportgleichung
`(G_B+L_B/17) C = Y^T` und die Bedingungen
`(G_A)ii − c_i^T G_B c_i >= 0` mit denselben Symbolen in die Auswertung
von F eingehen. Sämtliche höheren Terme und Rundungen bleiben einzuschließen.

Ein solcher gemeinsamer Auswerter ist als nächster gesonderter Versuch zu
entwickeln. Ein Ausschluss dieses einen Punktes garantiert noch kein
uniformes positives Randvorzeichen. Aus dem Ergebnis folgt auch keine
alleinige oder dominante Ursache für die Offenheit der ganzen Root.

Für einen Abschluss gelten weiterhin die maximale Linie auf der vollständigen
Root-Familie und ein physischer Gesamtwinkel strikt unter 10°. Objekt X,
kofinale Positivität und RH bleiben offen.

## 8. Quellen und Reproduktion

Das mitgelieferte versiegelte PR-Quellarchiv hat SHA-256
`b6f6078172ac97f5dcd61fb0ed76acd44e0b0a2c53a82ac554c831cd6732a663`.
Seine 81 Dateiinhalte werden vor der Ausführung geprüft. Die enthaltene
Vergleichsquittung ist bytegleich an den im Auftrag genannten Hash
`15ff4034f358bfdfea4eb9f61899c4be65794d0e079b28e6534a55bf38fcd0d8` gebunden.
Auch GitHub meldet für CI-Artefakt 11267809682 den angegebenen Digest
`4b031b63761b0f039e5dafe3a23e6c0893041481901ee817939aecffe3c95d7f`.
Die beiden ZIP-Hashes bezeichnen unterschiedliche Archive; hier verwendet
wird das versiegelte PR-Quellarchiv.

Vom entpackten Diagnoseverzeichnis, Python 3.11 oder neuer:

```text
python -B verify_pullback.py --source-archive inputs/PR206_SOURCE.zip --prior-diagnosis inputs/ROOT_DIAGNOSIS_GPT1.json --out ../pullback-replay
python -B audit_pullback.py --source-archive inputs/PR206_SOURCE.zip --receipt ../pullback-replay/PULLBACK.json --out ../pullback-independent.json
```

Diese beiden Prüfer benötigen ausschließlich die Standardbibliothek.
Für den zusätzlichen Auswertungs- und Winkelaudit wird `python-flint==0.9.0`
benötigt:

```text
python -m pip install -r requirements-audit.txt
python -B audit_factors.py --source-archive inputs/PR206_SOURCE.zip --receipt ../pullback-replay/FACTOR_COMPARISON.json --out ../factor-independent.json
```

Ausgabepfade müssen neu sein. `ACCEPTANCE.json` bindet Prüfer, Quittungen
und Audits; `MANIFEST.json` enthält die Hashes aller Paketdateien außer sich selbst.
