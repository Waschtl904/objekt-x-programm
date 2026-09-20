# Bewegliche Endpunkte: uniforme Blockreserven auf einem endlichen Band

Stand: 2026-09-19. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.
Anker: `b1c01860fef2a960cae57634041f75b29d37f836`.

Für B=log(5)/2 gilt jetzt autorenseitig für sämtliche ursprünglichen
Zwei-Mellin-Quellen mit 0<b<=B+10^-10:

    Q_W[u] > 2*10^-15 ||u||_2^2.

Im Odd-Sektor gilt >10^-12. Die zusätzliche Breite ist 200-mal größer
als das äußere Fenster B+5*10^-13 von b1c0186.

Der strukturelle Fortschritt ist eine tatsächlich mit dem Endpunkt
wachsende Zerlegung. Pro Parität bleiben 31 Soft-Koordinaten; der volle
Hard-Raum nimmt sämtliche angesammelten Profile auf und enthält weiter
den unendlichen Core-Tail. Für jeden Endpunkt a im Band [B,B+10^-10]
gelten dieselben Schranken:

| Größe | Zertifizierte Schranke |
| --- | --- |
| Vollständiger Hard-Boden, Referenzkoordinaten | >2/5 |
| Vollständiger Hard-Boden, physische Norm | >1/15 |
| Low/Hard-Kopplung | Norm <3 |
| Tatsächlicher harmonischer Lift | Norm <15/2 |
| Physische Konditionierung der harmonischen Gesamtkoordinaten | Quadratische Faktoren 1/162 und 486 |
| Soft-Schur-Boden Even / Odd | >8*10^-13 / >4*10^-10 |
| Vollständiger Profilboden | >2 log(2/(a-B))-5 |

Die Verschärfung des Profilbodens folgt aus der exakten Gamma-Stammfunktion
und einer frühen Auswertung der Konstantenkürzung. Beide Mellinkorrektoren,
alle Mischterme, der volle Operatorrest und der neu aktive Kanal 5 bleiben
enthalten. Kanal 7 wird auf diesem Band noch nicht erreicht.

Tatsächliche orthogonale Projektionen in der positiven Formmetrik liefern
eine exakte Transportidentität. Die Veränderung der geerbten Near-Null-Linie
hat über jede Unterteilung des Bandes ein gemeinsames Energiebudget;
die Summe ihrer quadrierten physischen Änderungen ist <8.2*10^-12.
Die ursprüngliche physische Quelle bleibt unverändert. Die Near-Null-
Projektion ist eine Koordinate dieser Quelle, keine neue Quellenauswahl.
Die übrigen 61 Low-Koordinaten behalten ihre vollständigen Mischterme.

Zwei gleich große Schritte von 5*10^-11 füllen das Band. Die bewiesenen
Blockkonstanten hängen nicht von der Zahl der Unterteilungen ab. Jeder
zuvor erreichte neue Endpunkt a<=B+5*10^-13 gestattet diesen nächsten
Schritt. Der gesamte angesammelte Profilraum bleibt dabei erhalten.

**Grenze des Ergebnisses:** Dies schließt nur die endliche Bandversion
von MOVING-ENDPOINT BLOCK-ADAPTIVE RESERVE RENEWAL. Die quantitative
Vergleichsrechnung bleibt am Core B verankert. Eine weitere Erneuerung
jenseits von B+10^-10, nicht summierbare Schritte, ein makroskopischer
Transport, Positivität bis log(7)/2 oder 1, Connected Unit-Window
Coercivity, Full C1-GEOM und Objekt X bleiben offen. RH wird nicht erreicht.

Der parallele Commit `a0ea6f80f317e4ef1132fc02c86be5bd2064e738` bleibt
vollständig erhalten. Er liefert den beweglichen High-Tail-Boden >1/41
auf B<=a<=1 bei 191 offenen Low-Koordinaten je Parität. Das ist ein
komplementärer Satz über einen anderen Hard-Raum; seine größere
Endpunktreichweite wird nicht mit unseren vollständigen Blockschranken
auf dem kleinen Band vermischt.
Sein normaler Aufruf `--verify` erzeugt 26 statt der veröffentlichten
25 Prüfungen und scheitert deshalb am JSON-Vergleich. `--math-only --verify`
reproduziert die 25 Prüfungen und sieben Hashes; der anschließende Aufruf
ohne Modusargument prüft zusätzlich alle vier Eingabebindungen erfolgreich.
Beide Aufrufe wurden ausgeführt. PROOF.md, Abschnitt 10, dokumentiert
diese Modusabweichung append-only; es ist kein arithmetischer Gegenbefund.

80 neue exakte Prüfungen, 111 bytegebundene Eingaben, die vollständige
frühere Prüfkette, zwei
neue rationale LDL-Vergleiche mit insgesamt 62 positiven Pivots und
sämtliche neuen Konstanten werden reproduziert. JSON, Log und
SHA-256-Manifest gehören zum Paket. Die unendlichdimensionalen
Projektionsidentitäten sind analytische Beweise in PROOF.md; der Checker
ist kein unabhängiges Audit dieser Argumente. Historische Dateien bleiben
unverändert; die Transportleiter erhält ausschließlich einen Nachtrag.
