# Adaptiver gemeinsamer Odd-Winkeltest nach der Y68-Trennung

## Gegenstand und gebundene Voraussetzungen

Dieser Block verwendet den kanonischen Stand
`65e7614683b5cf59db93d8a687d815cbff677612`. `SOURCE_BINDINGS.json` bindet
acht unverändert kopierte Eingaben an diesen Commit. Das eingebettete
Vorgängerarchiv wird vor dem Entpacken mit seinem ursprünglichen SHA-256
und anschließend mit seinen inneren Manifesten geprüft.

Die bereits zertifizierten Stage-A-Einträge werden mit beiden geerbten
Projektor-/Momentquittungen geschnitten. Zusätzlich gilt die neue
primal-duale Schranke

\[
Y_{68}\in[0.0410706614,0.0725344674].
\]

Der tatsächliche Schnitt benutzt die exakten rationalen Endpunkte aus
`inputs/gate.json`. Er wird mit `inputs/angle.json` exakt verglichen.
Die vier Teilungsachsen sind \(Y_{57},Y_{58},Y_{67},Y_{68}\).
Alle anderen Y-Einträge und sämtliche Gram-, Energie- und inversen
Energieintervalle bleiben erhalten. Es werden keine neuen Operatorintegrale
gerechnet. Der globale mathematische Verifikationssnapshot wird nicht verändert.

## Sichere Filter und ein gemeinsamer physischer Winkel

Für jede Box wird das unveränderte `BoxModel` des Vorgängers ausgewertet.
Es verwendet

\[
X=(G_B+L_B/17)^{-1}Y^*,\quad
H_0=G_A-X^*G_BX,\quad H_\nu=L_A-X^*L_BX-\nu H_0.
\]

Eine strikt negative obere Schranke für eine notwendige PSD-Diagonale
oder den geerbten Hauptminor auf den Richtungen 5 und 6 schließt die ganze
Box aus. Diese äußeren Tests bilden nur einen Teil der gemeinsamen
Zulässigkeitsbedingungen ab. Ihr Bestehen beweist keine Existenz.
Ein nicht entscheidbarer Nenner oder eine nicht entscheidbare
Intervalleinschließung führt zu UNRESOLVED, nicht zu einem Ausschluss.

Für überlebende Boxen wird dieselbe Kernbasis

\[
N=(-Y_l^{-1}Y_r,I_2)^T
\]

in allen Kompressionen und beiden inversen Energiefunktionalen verwendet.
Der überlieferte positive Eigenwertgap und der physische Rang-eins-Projektor
liefern eine rationale Einschließung \(\sin^2\theta\le s\) bezüglich
**derselben festen Referenz** für alle Boxen. Die Metrik ist die physische
Gram-Matrix \(G_B\), nicht die euklidische Koordinatenmetrik.

Eine obere Schranke für die gesamte symmetrische Korridorbreite ist

\[
w(s)=2\arcsin\sqrt{s}\;\frac{180}{\pi}.
\]

Für \(s<1/2\) wird sie durch gerichtete rationale Auswertung von
\(2\arctan\sqrt{s/(1-s)}\) eingeschlossen. Für \(s>1/2\) wird die
reziproke Darstellung \(180^\circ-2\arctan\sqrt{(1-s)/s}\) mit einer
unteren Arkustangensschranke verwendet. Die Punkte 0, 1/2 und 1 werden
exakt behandelt. Die geerbte rationale Arkustangensreihe und Machin-Formel
für Pi bezahlen ihre Restterme. Eine zweite Implementierung mit Arb
kontrolliert die berichteten Winkelobergrenzen.

**Eine Box wird nur bei \(w_{\rm upper}<10^\circ\) freigegeben.**
Der alte Boolesche Wert `within_target_corridor` wird ignoriert.
Insbesondere ergibt \(s=0.01\) ungefähr 11.47834 Grad Gesamtbreite und
darf hier kein GREEN auslösen. Die strikte Fünf-Grad-Schwelle liegt zwischen
0.00759612349 und 0.00759612350.

Die formale Hülle von 180 Grad bei \(s=1\) ist uninformativ. Sie behauptet
weder einen tatsächlichen Winkel von 180 Grad noch die Existenz weit
getrennter zulässiger Geraden.

## Adaptive Teilung und vollständige Überdeckung

Vor dem Hauptlauf sind Budget, Auswahlregel und Ziel in `parameters.json`
festgehalten: höchstens 255 Baumknoten, Tiefe 16 und 1.017 Auswertungen für
die Teilungswahl. Bei jeder noch problematischen Box werden **alle vier**
Halbierungen geprüft. Die lexikographische Auswahl bevorzugt:

1. mehr ausgeschlossene Kinder;
2. mehr Kinder unter der strikten Winkelgrenze;
3. kleinere maximale und anschließend kleinere mittlere Winkelobergrenze;
4. erst bei Gleichstand die relativ zur Ausgangsbox größere Seitenbreite;
5. zuletzt die feste Reihenfolge der Variablennamen.

Die Reihenfolge problematischer Blätter richtet sich nach größter
Winkelobergrenze, größtem relativen Volumen und Kennung. Die Reihenfolge
ändert weder die geprüfte Familie noch die Abnahmeschwelle.

Jede Halbierung verwendet den **exakten rationalen Mittelpunkt**. Beide
Kinder teilen eine Grenzfläche und überdecken ihren Elternbereich exakt.
Der getrennte Auditor rekonstruiert jede Teilung, prüft alle Kindboxen und
vergleicht die Summe der relativen Blattvolumina mit exakt 1. Die rekursive
Partitionsprüfung verhindert, dass sich Überlappungen und Lücken in dieser
Volumensumme gegenseitig verbergen. Nicht gewählte Probeteilungen sind
keine zusätzlichen Blätter.

Damit liegt jede gemeinsam zulässige Vervollständigung der Ausgangsbox
in mindestens einem nicht ausgeschlossenen Blatt. Wenn sämtliche dieser
Blätter um dieselbe Referenz eine Breite unter 10 Grad zertifizieren,
gilt dieser Korridor für die ganze Familie. Verschiedene lokale Referenzen
oder bloß enge individuelle Eigenwertintervalle würden hierfür nicht genügen.

## Drei wissenschaftliche Ausgänge

- **GREEN:** Die vollständige Überdeckung ist geprüft und jedes nicht
  ausgeschlossene Blatt liegt strikt im gemeinsamen Korridor unter 10 Grad.
- **NEW STRUCTURAL OPEN:** Ein gesonderter vollständiger Punktezertifikatsnachweis
  liefert zwei zulässige Vervollständigungen der neuen Familie mit einem
  gerichteten Linienabstand größer als 10 Grad. Überlebende Boxen genügen nicht.
- **UNRESOLVED:** Ein festgelegtes Budget ist erreicht und mindestens ein
  Blatt bleibt unentschieden, ohne solchen Gegenzeugennachweis.

Eine vollständig ausgeschlossene Familie wird als Konsistenzfehler
abgewiesen; sie erhält kein leeres GREEN. Dieser Lauf konstruiert keine
neuen zulässigen Punkte. Die fünf bereits zertifizierten Punkte dienen
als Schutz gegen falsche Ausschlüsse. Ihre Existenz stammt aus dem
gebundenen Vorgängerbeweis, nicht aus Boxüberleben.

## Diagnose ohne Aussagepromotion

Acht über den verbleibenden Baum verteilte Blätter erhalten zusätzliche
Vier-Achsen-Halbierungstests. Ferner werden einzelne Achsen sowie alle
vier Achsen gleichzeitig auf ihre Mittelpunkte gesetzt. Diese letzten
Versuche sind **bedingte Diagnosen**, weder eine Überdeckung noch
Existenzbeweise. Ein weiterer separater Test beschränkt die vier Achsen
auf die engen Hüllen der fünf bereits zertifizierten Punkte und behält
alle übrigen Unsicherheiten bei.

Sieben weitere zentrale Diagnosefälle schränken zusätzlich einzelne oder
alle Momentgruppen beziehungsweise alle Y-Einträge auf die bereits
zertifizierten Daten des zentralen Modells ein. Die vollständige Enthaltenheit
dieser engen Daten in den ursprünglichen Hüllen wird ausdrücklich geprüft.
Diese Einschränkungen gelten nur in den bezeichneten Diagnosefällen;
der eigentliche Baum behält sämtliche Unsicherheiten. Ein enges Ergebnis
für einen solchen zentralen Spezialfall lokalisiert nicht die ganze Familie.

Breite Hüllen auch in diesen bedingten Tests können ein Defizit der
aktuellen Auswertungsform anzeigen. Sie beweisen weder, dass jede weitere
Teilung scheitern muss, noch dass eine bestimmte neue Messung notwendig ist.
Insbesondere ist eine häufig gewählte Achse bei reinen Gleichständen kein
Sensitivitätsnachweis und keine Rechtfertigung für neue Y58-Integrale.

## Technische Reproduktion und Grenzen

Nur die von festen linken Y-Blöcken und festen Faktoren abhängigen
Neumann-Hüllen werden zwischengespeichert. Beide Produkte mit dem jeweils
aktuellen rechten Y-Block und derselben aktuellen Kernbasis werden neu
gerechnet. Der Schlüssel enthält sämtliche abhängigen festen Eingaben.
Die gespeicherte und die ursprüngliche Auswertung stimmen in getrennten
Kontrollen exakt überein, auch bei geändertem linken Y-Eintrag.

`audit_certificate.py` prüft die Baumstruktur und Auswahlregeln getrennt
vom Suchalgorithmus und wiederholt jede gespeicherte eindeutige numerische
Boxauswertung. Beide Programme verwenden die geerbte rationale
Intervall-Engine; dies ist keine unabhängige Neuimplementierung der großen
Operatorrechnungen. Die Winkelumrechnung wird zusätzlich durch Arb geprüft.

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Das Laufresultat und
die genauen Zählwerte stehen in `verification.json` und `ADAPTIVE_ANGLE_GATE.md`.
Eine uniforme ungerade Lokalisierung wird nur bei GREEN behauptet.
Bandmomente tatsächlicher Maximierer, Renewal, A13-Positivität, kofinale
positive Familie, globales Objekt X und RH werden durch diesen Block
nicht bewiesen. #187 bleibt separat und unverändert.
