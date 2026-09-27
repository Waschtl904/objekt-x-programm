> Historischer Entwicklungs-/Reproduktionsbericht. Aktueller Paketeinstieg: [O8/O9](../README.md).

# O8 bei A₈: Rechenzertifikat lokal reproduziert

27. September 2026 · **AUTHOR_DERIVED_LOCAL / CERTIFICATE_REPRODUCED_LOCAL / EXTERNAL_REVIEW_OPEN**

Der im eingereichten Audit benannte Reproduktionsschritt ist jetzt ausgeführt. Das ausgelieferte Archiv wurde geprüft, die vorhandenen Prüfer liefen aus einer frisch entpackten Arbeitskopie erfolgreich durch, und ein separat implementierter Prüfer hat beide 191-dimensionalen Zertifikate mit exakter Ganzzahl-Intervallarithmetik bestätigt.

**Ergebnis: jeweils 191 strikt positive gerichtete LDL-Pivots und derselbe gemeinsame physische Boden 1,2·10⁻²⁹ sowie Defektboden >10⁻³⁰.**

## 1. Hashbindungen und Wiederholung der Originalprüfer

Geprüft wurde das tatsächlich zuvor ausgelieferte Archiv `O8_A8_mit_Schurabgleich_2026-09-27.zip` mit SHA-256

```text
16bc2ea4d194b15f9240662286ac3ba38b46cafaf532890c77eb033e2ee62ea0
```

Nach erfolgreichem Archivtest wurden alle 40 Einträge des ursprünglichen Rechenmanifests und alle acht Einträge des Graphnachtragsmanifests gegen die entpackten Dateien geprüft. Die feste Archivbindung umfasst außerdem beide Manifestdateien und den damaligen Einstiegstext.

In einer neuen Arbeitskopie wurden anschließend die mitgelieferten Skripte ausgeführt:

| Schritt | Ergebnis |
|---|---|
| `refine_tail.py` | Alle elf Prüfungen bestehen; Ergebnisdatei bytegleich |
| `check_a8.py --high-floor 2/3` | Beide 191-Pivot-Läufe bestehen; alle mathematischen Ergebnisfelder und Pivotintervalle identisch |
| Gespeicherte Untermatrizen | Beide komprimierten Matrixdaten zusammen bytegleich zum Original |
| `check_common_reserve.py` | Gemeinsame rationale Abrundung bestätigt |

Im Reserveprotokoll unterscheiden sich ausschließlich die gemessenen Laufzeiten. Deshalb ändert sich dessen Dateihash und entsprechend die Hashreferenz im gemeinsamen Reserveprotokoll. Diese erwartete Änderung wurde beim Vergleich ausdrücklich berücksichtigt.

Der Ablauf steht in [original_replay_results.json](original_replay_results.json); die tatsächlich neu geschriebenen Dateien heißen [replayed_refined_tail.json](replayed_refined_tail.json), [replayed_reserve_refined.json](replayed_reserve_refined.json) und [replayed_common_reserve.json](replayed_common_reserve.json). Die Ausgaben der drei Prozesse liegen als `*_replay.log` bei.

## 2. Separater Prüfer mit exakten Ganzzahlintervallen

[verify_integer_intervals.py](verify_integer_intervals.py) verwendet ausschließlich die Python-Standardbibliothek. Er importiert keinen ursprünglichen Generator oder Prüfer und verwendet kein Arb/FLINT.

Jedes Intervall wird durch zwei ganze Zahlen l≤u auf dem Raster S=10¹²⁰ dargestellt: [l/S,u/S]. Addition und Subtraktion sind auf diesem Raster exakt. Multiplikation und Division werden nach außen gerundet; beim Quadrieren wird ein möglicher Nulldurchgang berücksichtigt. Divisionen sind nur bei nachgewiesen strikt positiven Nennerintervallen zulässig. Die elementaren Rechenoperationen werden zusätzlich anhand exakter rationaler Rand- und Innenwerte mit wechselnden Vorzeichen geprüft.

Der Prüfer führt folgende Schritte neu aus:

1. Er kontrolliert die Datenbindungen, Dimensionen, Symmetrie und Endpunktparameter.
2. Er rekonstruiert die beiden inversen Reihenpolynome aus den ausgelieferten Gamma-Koeffizienten. Deren Produkte mit den endlichen Nennerreihen liefern exakt verschwindende Anfangsresiduen. Mit den geometrisch eingeschlossenen Fakultätstails entsteht genau die gespeicherte rationale Gamma-Fehlerobergrenze.
3. Er berechnet die hohen Mellinmajoranten und e_B=2γ_K+24ε_p neu. Ebenso bestätigt er den rationalen Überschuss der hohen Reserve 2/3.
4. Er bildet aus allen gespeicherten L₀-/G₀-Intervallen die gerichtete Untermatrix neu:

\[
F=L_0-\frac{3003}{2000}G_0
-\left(4\gamma_K+\frac{3003}{2}(2\gamma_K+24\varepsilon_p)^2\right)I.
\]

   Für jeden Eintrag prüft er, dass das ausgelieferte Untermatrixintervall diese neue Einschließung enthält. Erst danach verwendet er die vollständigen gespeicherten Matrixintervalle für die LDL-Rechnung.
5. Er berechnet beide LDL-Zerlegungen mit den eigenen Ganzzahlintervallen. Sämtliche 382 unteren Pivotgrenzen sind strikt positiv.
6. Er löst die Dreieckssysteme erneut, schließt tr(F⁻¹) ein und gewinnt daraus σ≥1/obere Grenze von tr(F⁻¹).
7. Er gewinnt die Kopplungsnormobergrenze aus dem vollständigen Gram, kontrolliert die verwendete Wurzelobergrenze durch exaktes Quadrieren und rechnet die physischen und T-Reserven neu um.

Die Rechnung besteht **35 gruppierte Prüfungen**. Die vollständigen Pivotintervalle, rationalen Reserveböden und Eingabehashes stehen in [integer_results.json](integer_results.json). Die Zahl 35 bezeichnet Prüfgruppen; die beiden jeweils 191 Pivotprüfungen sind darin enthalten.

## 3. Neu berechnete Reserven

Die Anzeigen in der Tabelle sind gerundet; maßgeblich sind die exakten unteren Grenzen im Ergebnis-JSON.

| Parität | Positive Pivots | Schur-Boden σ, ungefähr | Physischer Boden, ungefähr | Defektboden, ungefähr |
|---|---:|---:|---:|---:|
| Gerade | 191/191 | 1,11289013953·10⁻²⁶ | 1,23256343485·10⁻²⁹ | 1,07179429118·10⁻³⁰ |
| Ungerade | 191/191 | 7,79686433754·10⁻²⁴ | 8,61066526013·10⁻²⁷ | 7,48753500881·10⁻²⁸ |

Der eigenständige Prüfer bestätigt exakt

\[
c_{\rm phys}\ge\frac{12}{10^{30}},\qquad
\eta\ge\frac{24}{23\cdot10^{30}+24}>10^{-30}.
\]

Er prüft die ursprüngliche erfolgreiche Untermatrix mit gebündeltem Mellin-/Gamma-Kopplungsfehler. Die später ergänzte Graphmatrix bleibt ein zusätzliches, bereits dokumentiertes Zertifikat. Die Übertragung auf den exakten Schurrest steht im [Graphnachtrag](../o8-schur-abgleich/GRAPH_SCHUR.md).

## 4. Umfang der Unabhängigkeit

**Unabhängig implementiert und gerechnet:** Gamma-Residualkontrolle aus den gelieferten Polynomkoeffizienten, Aufbau der ausreichenden Matrix aus den Modellintervallen, gesamte Intervall-LDL-Arithmetik, inverse Spur und Normumrechnung. Der Zweitprüfer nutzt eine andere Zahlenrepräsentation als der ursprüngliche Arb-Prüfer.

**Übernommene Eingaben:** die vollständigen L₀-/G₀-Modellintervalle aus der Integralengine, die analytische Identifikation ihres Operators, die Formraumherleitung und die analytischen hohen Schranken. Der Modellgenerator wurde in diesem Block nicht erneut ausgeführt oder durch eine zweite vollständige Integralengine ersetzt.

Die Prüfung wurde lokal durch denselben Arbeitsagenten ausgeführt. Eine eigenständige Implementierung ist keine organisatorisch unabhängige externe Abnahme. Der eingereichte positive analytische Prüftext ist als Eingabe abgelegt; sein Verfasserstatus wird daraus nicht zusätzlich abgeleitet. Daher bleibt **EXTERNAL_REVIEW_OPEN** bestehen. Die zuvor fehlende lokale Reproduktion der Matrixzertifikate liegt jetzt vor.

## 5. Reproduktion durch einen weiteren Prüfer

Das Gesamtarchiv enthält die tatsächlichen Matrizen, JSON-Dateien und Quelltexte. Nach dem Entpacken kann die unabhängige Zertifikatsprüfung vom Archivwurzelverzeichnis aus ohne Zusatzpakete gestartet werden:

```powershell
python o8-reproduktion/verify_integer_intervals.py --package o8-rechenstand --output o8-reproduktion/independent_repeat.json
```

Verwendet wurde Python 3.13. Der Prüfer benötigt nur dessen Standardbibliothek und schreibt die neue Ergebnisdatei sowie ein gleichnamiges Protokoll. Beim hier dokumentierten Lauf las er die frisch reproduzierte Arbeitskopie; deren mathematische Ergebnisfelder stimmen mit den ursprünglichen Dateien überein. Wegen der Laufzeiten können Ergebnis- und Folgehashes abweichen, während die Eingabematrizen identisch bleiben.

Für eine Wiederholung der ursprünglichen Arb-Prüfer stehen die [Anleitung und Abhängigkeiten](../o8-rechenstand/README.md) ebenfalls im Archiv. Dafür ist python-flint 0.9.0 erforderlich. Die unabhängige Ganzzahlprüfung benötigt diese Bibliothek nicht.

## 6. Forschungs- und Repository-Status

Für die konkrete C1a-Fortführung auf 1≤A≤log(8)/2 liegt nun ein lokal reproduzierter positiver Rechenbefund mit der dokumentierten analytischen Anbindung vor. Das schafft die im eingereichten Audit geforderte zusätzliche Grundlage zur Beurteilung des autorenseitigen O8-Ergebnisses.

In diesem Block erfolgten keine GitHub-Schreibzugriffe, keine Registry-Promotion und kein erneuter administrativer Repository-Audit. O9, O10 und globale Aussagen bleiben getrennt.
