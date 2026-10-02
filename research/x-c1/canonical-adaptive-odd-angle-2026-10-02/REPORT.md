# CANONICAL-JOINT-ODD-ANGLE-AFTER-Y68

2. Oktober 2026 · **UNRESOLVED** · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

## Ergebnis

Die adaptive zertifizierte Boxzerlegung wurde vollständig bis zum vorher
festgelegten Budget ausgeführt. Sie liefert noch keinen gemeinsamen
ungeraden physischen Winkelkorridor unter 10 Grad und keinen neuen
STRUCTURAL-OPEN-Nachweis.

| Prüfgröße | Ergebnis |
|---|---:|
| Baumknoten | 255 |
| Terminale Blätter | 128 |
| Ausgeschlossene Blätter | 0 |
| Blätter mit zertifizierter Breite unter 10° | 0 |
| Unentschiedene Blätter | 128 |
| Auswertungen für Baum und Teilungswahl | 1.017 |
| Zusätzliche Auswertungen an acht terminalen Diagnoseboxen | 104 |
| Eindeutige Boxauswertungen im Hauptzertifikat | 1.121 |
| Tatsächlich erreichte maximale Tiefe | 11 |
| Stoppgrund | vorab festgelegtes Knotenbudget |

77 Blätter haben eine geringfügig bessere Hülle als 180°. Die
**Obergrenzen** der Blätter liegen insgesamt im nach außen gerundeten Bereich
**[177.914891426°, 180°]**. Dies sind keine Untergrenzen tatsächlicher Winkel.
Die globale Hülle bleibt 180° und ist uninformativ.

Die Ausgangsbox wird exakt überdeckt. Die rationalen relativen Blattvolumina
summieren sich zu 1; darüber hinaus wird jede einzelne Eltern-Kind-Partition
geprüft. Alle fünf bereits zertifizierten zulässigen Punkte liegen weiterhin
in nicht ausgeschlossenen Blättern. Es wurden keine neuen zulässigen Punkte
konstruiert; Boxüberleben wird nicht als Existenzbeweis verwendet.

## Die 10°-Grenze ist korrigiert

GREEN verlangt in jedem überlebenden Blatt eine rigorose gesamte Breite
**strikt unter 10° bezüglich derselben Referenz**. Das alte Boolesche Kriterium
`sin² ≤ 0.01` wird ignoriert: Es erlaubt etwa **11.47834°** Gesamtbreite.

Die neue Winkelumrechnung behandelt auch den Bereich über 45° Halbwinkel
durch die reziproke Arkustangensdarstellung. Sie verwendet rationale
gerichtete Schranken. Eine unabhängige Arb-Rechnung mit 768 Bit bestätigt
alle 210 verschiedenen geprüften Winkelobergrenzen aus Baum, Diagnosen
und Grenzwertkontrollen.

## Welche Teilungen wirken?

Bei jeder problematischen Box wurden alle vier Halbierungen ausprobiert.
Die Entscheidung bevorzugt Ausschlüsse, enge Kinder und dann bessere
Winkelobergrenzen. Erst bei Gleichstand entscheidet die relative Seitenbreite.

| Achse | Gewählte Teilungen insgesamt | Gewählt bei unterschiedlichen Sensitivitätswerten |
|---|---:|---:|
| Y57 | 17 | 0 |
| Y58 | 28 | 2 |
| Y67 | 32 | 15 |
| Y68 | 50 | 50 |

Bei 60 der 127 Entscheidungen waren die vier Winkel-/Ausschlussbewertungen
gleich. Solche Entscheidungen sind kein Sensitivitätsnachweis.

An acht über den verbleibenden Baum verteilten Blättern wurden weitere
Halbierungen getestet. Die jeweils größte beobachtete Verbesserung der
schlechtesten Kinderobergrenze betrug ungefähr:

| Halbierte Achse | Größte Verbesserung unter diesen acht Proben |
|---|---:|
| Y57 | 0.3983° |
| Y58 | 0.1895° |
| Y67 | 1.4235° |
| Y68 | 1.1432° |

Das sind Verbesserungen von berechneten Obergrenzen in den bezeichneten
Proben, keine uniformen Sensitivitätskonstanten. Die Daten liefern derzeit
**keinen dominierenden Y58-Engpass**, der eine isolierte neue Dualrechnung
rechtfertigen würde. Sie beweisen nicht, dass genauere Y58-Daten nutzlos wären.

## Der wichtigere Diagnosebefund

Die vier Kreuzkorrelationen allein sind im gegenwärtigen Auswerter nicht
der einzige Grund für breite Hüllen. Beschränkt man sie auf die extrem
engen Koordinatenhüllen der fünf bekannten zulässigen Punkte, behält aber
alle übrigen Unsicherheiten, bleiben die berechneten Gesamtbreiten ungefähr
zwischen **163.16° und 174.90°**.

Am bereits zertifizierten zentralen Modell wurde zusätzlich gezielt geprüft,
welche Datenbeschränkungen die Hülle verändern:

| Bedingte Dateneinschränkung | Berechnete Gesamtbreite, ungefähr |
|---|---:|
| Nur die vier Teilungskoordinaten eng beim zentralen Punkt | 163.162463° |
| Alle Y-Einträge beim zentralen Punkt | 155.030194° |
| Vier Koordinaten und G_B beim zentralen Modell | 163.155451° |
| Vier Koordinaten und L_B beim zentralen Modell | 116.720693° |
| Vier Koordinaten und Z_B beim zentralen Modell | 159.369820° |
| Vier Koordinaten und alle vollen Momentmatrizen beim zentralen Modell | 102.985115° |
| Alle Y-Einträge und alle vollen Momentmatrizen beim zentralen Modell | 1.903077° |

Die Tabelle verwendet die gebundenen Daten des bekannten zentralen Modells,
keine frei ausgewählten Mittelpunktmatrizen. Ihre Enthaltenheit in den
ursprünglichen Intervallen wird geprüft. Die angegebenen Dezimalwerte
sind diagnostische Näherungsanzeigen; genaue rationale Obergrenzen stehen
in `uncertainty_groups.json`.

**Der letzte Tabellenwert ist kein GREEN für die vollständige Familie.**
Er betrifft einen bedingten zentralen Spezialfall. Im eigentlichen Baum
werden sämtliche Nebenintervalle vollständig beibehalten.

Die stärkste beobachtete Verbesserung durch eine einzelne Momentgruppe
entsteht hier bei L_B. Die gemeinsame Behandlung von Y und den Momentdaten
ist damit der nächste konkrete Prüfpunkt im Winkelauswerter. Aus diesen
Diagnosen folgt weder die Notwendigkeit einer neuen L_B-Rechnung noch ein
No-Go für weitere Boxzerlegung.

## Prüfung, Quellen und Aussagegrenze

- Acht Eingabedateien sind bytegenau an
  `main@65e7614683b5cf59db93d8a687d815cbff677612` gebunden. Das eingebettete
  Vorgängerarchiv wird zusätzlich mit seinen ursprünglichen Hashes geprüft.
- Der getrennte Auditor kontrolliert alle Partitionen, Teilungsbewertungen,
  Statusentscheidungen und wiederholt sämtliche 1.121 gespeicherten
  eindeutigen numerischen Boxauswertungen. Alle Ergebnisquittungen stimmen.
- Eine weitere Prüfung rekonstruiert alle 127 Blattentscheidungen aus der
  vorher festgelegten Priorität und verwirft eine manipulierte Reihenfolge.
- Negativkontrollen prüfen unter anderem falsches GREEN, fehlende Blätter,
  Boxüberleben statt Punktezertifikat und die strikte 10°-Grenze.
- Die unveränderten geerbten Kontrollen prüfen PSD-Ausschlüsse, die physische
  Gram-Metrik, den Faktor 17 und manipulierte Archive.
- Die Zwischenspeicherung von Neumann-Hüllen wird gegen die ursprüngliche
  Rechnung exakt geprüft. Die numerische Nachrechnung verwendet dieselbe
  rationale Grundengine; Arb kontrolliert die Winkel unabhängig.

Neue große Operatorintegrale und neue duale Y58-Daten wurden nicht erzeugt.
Keine vollständige unabhängige Neuimplementierung der großen Operatorrechnung
und kein abgeschlossener externer Gesamtaudit werden behauptet.

Der alte gedrehte Gegenzeuge bleibt durch Y68 ausgeschlossen. Für die
verschärfte Familie bleibt der uniforme ungerade Winkel **UNRESOLVED**.
Bandmomente tatsächlicher Maximierer folgen erst nach dieser Lokalisierung.
Renewal, A13-Positivität, eine kofinale positive Familie, globales Objekt X
und RH bleiben offen.

**Nächster sachlicher Schritt:** Im gemeinsamen Winkelauswerter die
Unsicherheiten und Abhängigkeiten zwischen Y, N und den Momentmatrizen,
insbesondere der Energie, genauer aufschlüsseln. Die vorliegenden Daten
begründen noch keinen neuen isolierten Y58-Dualblock.

Dieses Paket ist lokal abgeschlossen und nicht integriert. Der kanonische
Main-Stand bleibt `65e7614683b5cf59db93d8a687d815cbff677612`;
#187 bleibt separat und unverändert.
