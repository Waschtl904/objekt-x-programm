# Prüfstand des allgemeinen Wand-Lemmas

27. September 2026 · **AUTHOR_DERIVED_LOCAL / EXTERNAL_REVIEW_OPEN**

## Neue Arbeit

Neu hergeleitet wurden die universelle Frequenzmajorante, die expliziten
Ein-Wand-Grenzen, direkte Verhältnisse über endlich viele Wände und
horizontabhängige vollständige Quell-/Defektschranken. Die q=9-Daten wurden
als Instanz eingesetzt. Die zwei-Wand-Familie bis A11 und die Erhaltung
der bekannten Positivität auf den alten Bildern sind ausgeschrieben.

Der Nachweis verwendet keine neue positive Terminalmatrix und nimmt keine
Positivität auf dem gesamten dritten Kammerraum an.

## Prüfungen

`verify_wall.py` bestand mit 109 Kontrollen. Die ersten analytischen
Majoranten werden durch exakte rationale beziehungsweise formale
Polynomidentitäten gestützt. Frequenzabtastung wird nicht eingesetzt.
Die 56 geordneten Testtripel prüfen die Aktivierungszuordnung an beiden
Wänden und im Kammerinneren; das Cocycle für alle reellen Terminals folgt
aus der symbolischen Kürzung im Beweis, nicht aus diesen endlich vielen Fällen.

Rationale Quellproben kontrollieren die beiden Mellinbedingungen durch
exakte Ableitungsidentitäten sowie die sesquilineare Trägergeometrie.
Ein endliches Kompressionsbeispiel hält die logische Grenze zwischen altem
positivem Bild und größerem vollständigem Carrier ausdrücklich fest.

Sieben Repository-Quellen wurden erneut aus ihren festen Commits gelesen.
Alle sechs manifestierten Dateien des alten O10-Pakets und alle 34 des
A9-Pakets bestanden den Bytevergleich. Ausgewählte Eingaben und Quittungen
sind im neuen Paket unverändert enthalten.

## Vorhandenes A9-Zertifikat und Nutzerbericht

Der A9-Boden `10^(-35)` und sein Defektboden werden aus dem zuvor geprüften,
unveränderten Paket importiert. Seine Arb- und Ganzzahlquittungen samt
gemeinsamer Reserve sind aneinander und an das alte Manifest gebunden.
In diesem Arbeitsblock wurden weder der große Arb-Modellaufbau noch der
alte Ganzzahlprüfer erneut ausgeführt; ein solcher Lauf wird nicht behauptet.

Der Nutzer berichtet zusätzlich seinen eigenen getrennten Ganzzahllauf
für beide Paritäten sowie 65 Tail-Kontrollen ohne Repositorypfad.
Sein Bericht nennt ausdrücklich keinen neuen Arb-/Normalisierungslauf.
Diese Auditmitteilung wird in genau diesem Umfang festgehalten. Sie ist
keine hier nachträglich ausgeführte Prüfung und keine vollständige externe
analytische Abnahme des neuen allgemeinen Lemmas.

## Offen und erhalten

Offen bleiben die externe analytische Prüfung, der neue vollständige
Tail-/Low-Nachweis am Terminal A11, eine kofinale positive Fortsetzung und
alle globalen Aussagen. Insbesondere ist die q=3-Kettennorm in der dritten
Kammer neu zu bezahlen.

Die alten Beweise, Quittungen und mathematischen Anker wurden nicht geändert.
Es gab keine GitHub-Schreibaktion, Registry-Änderung, Branch- oder Taglöschung.
Der zwischenzeitliche Main-Fortschritt ist getrennt in `MAIN_CHECK.md`
mit seiner tatsächlichen Auswirkung auf die verwendeten Eingaben behandelt.

## Herkunft und Lizenz

Grundlage ist [Waschtl904/objekt-x-programm](https://github.com/Waschtl904/objekt-x-programm).
Die vorhandene CC-BY-4.0-Lizenz liegt bytegleich unter
`inputs/REPOSITORY_LICENSE.txt`. `SOURCE_BINDINGS.json` dokumentiert die
Quellen und die neu abgeleiteten Texte. Die vollständige neue Lieferung
ist durch `SHA256SUMS` gebunden.
