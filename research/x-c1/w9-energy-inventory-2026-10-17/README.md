# W9-Energie: Bestand und Fehlerkontrolle

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN** für die bedingte Herleitung;
**vollständiger Energievergleich OPEN**. Aufbauend auf #236, ohne neue Suche.

Die festen Gewichte, alten Quellen-/Kopplungsgrame und neuen ungerichteten
Restmaps sind vorhanden. Für neue Residuen fehlen insbesondere B8 T_h h,
die hohen Kreuzgrame mit g_F und gJ, alle 84 bloßen Basis-Paarungen und
der vollständige R_L-Dualterm. Keiner der vier vollständigen Energieanteile
wird aus den bisherigen Skalarmaps als fertig berechnet ausgegeben.

Die passende Fehlerkontrolle ist eine gemeinsame Matrix
`Q_D >= DeltaD* W9 DeltaD`, gewonnen aus fünf gewichteten Feature-Gramen.
Die Herleitung enthält obere und untere Energiehüllen, damit ein späterer
Ausschlusstest nicht versehentlich eine Obergrenze als Untergrenze verwendet.

Eine neue grobe Normrechnung liefert bedingt `||W9|| < 10^195 / 10^183`.
Die daraus verfügbaren Fehleroberpreise `10^134 / 10^120` sind praktisch
unbrauchbar; sie schätzen nicht die tatsächliche Fehlergröße. Eine brauchbare
gewichtete Matrixhülle bleibt nötig. Die 0.15-Prozent-Modellreserve aus #236
wird nicht als Beweis verwendet.

[Herleitung, Datentabelle und nächster Rechenplan](PROOF.md).
[Maschinenlesbarer geprüfter Bestand](INVENTORY.json).

```sh
python3 research/x-c1/w9-energy-inventory-2026-10-17/verify.py
```

Nur Python-Standardbibliothek. Hashgebundene Eingaben werden als geprüfte
Bytes weiterverwendet; keine Kindprozesse oder neue Archivimporte.
Der Replay prüft Inventar, rationale Normpreise und Kontrollalgebra, nicht
die geerbte analytische Gesamtherleitung. Kein neuer vollständiger W9-Gram,
kein N12-Abschluss und keine Änderung der bisherigen Zertifikate.
