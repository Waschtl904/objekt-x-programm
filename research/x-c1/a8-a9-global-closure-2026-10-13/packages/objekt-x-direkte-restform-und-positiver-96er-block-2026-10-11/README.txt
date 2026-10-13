Objekt X — Direkte Rest84 und positiver gemeinsamer 96er-Vergleich
11. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Mit BERICHT.txt beginnen, danach HERLEITUNG.txt.

Standardbibliothek-Replay, Python 3:

  python -B reproduce.py

Dieser Replay prüft alle neuen Manifestbindungen, die beiden eingebetteten
Vorgängerbindungen, die neue direkte Matrix und die negativen Gegenrichtungen
der alten Majorante. Er rekonstruiert anschließend mit exakten rationalen
Intervallen die neue 191er-Inverskongruenz, alle 9216 Antwortmatrixeinträge,
die vollständigen Fehlerpreise und die positive 96er-Untergrenze je Parität.
Das kann einige Minuten dauern. Es werden dabei keine Integrale neu berechnet.

Vollständige neue Integrationen und Matrixrechnungen erneut ausführen:

  python -B rebuild_from_parent.py --root PFAD_ZUM_ENTPACKTEN_GROSSEN_ORIGINAL

Voraussetzungen: python-flint 0.9.0, numpy und scipy; die verwendete lokale
Referenzumgebung hat numpy 2.5.3 und scipy 1.18.1. Das große Originalpaket
zuerst frisch entpacken und dessen reproduce.py ausführen, damit alle
gebundenen Vorgänger im erwarteten Verzeichnisbaum liegen.
Das neue Programm schreibt einen neuen Arbeitsordner und kopiert die
benötigten versiegelten Richtungsbrückendaten in dessen Nachbarordner.

Großes Originalpaket, hier wegen seines Umfangs nicht nochmals enthalten:
Objekt-X-Galerkin84-und-Verlusttest-2026-10-11.zip
SHA256 461eee1352a82cadf9c9a8ec6540f782ad9ceb0490c0fa28afa93392dccd7c28

Unverändert eingebetteter jüngster Eingang:
Objekt-X-Richtungsbruecken-Pruefung-und-Konstantentest-2026-10-11.zip
SHA256 ec6b5398a8ac3ddb1038e7e4cb3ceaee5b2eebccf534137a3d7b14be0993e511

Die neuen direkten Integrale stehen in DIRECT_REST_*_3072/4096.json.
Die 92er-Reihenfolge ist J84,Y8. REFINED_COMMON96.json verwendet dagegen
die Reihenfolge physische z4,Y8,J84. Ihre H84-/Kraftfelder sind neue Daten
für die neue Inversmajorante; die zwölf endlichen Kraftzeilen sind nicht
mit P residualisiert. Kein altes Residuum wird weiterverwendet.

REFINED_INPUT.json ist der deterministische Auszug der gebundenen alten
vollständigen Kraft- und Gramdaten. build_audit_input.py erzeugt ihn neu.
Die Dateien mit Endung _model enthalten numerische Integralintervalle;
die zusätzlichen analytischen Fehler werden erst in den entsprechenden
Operator- und Vergleichsabschätzungen bezahlt.

Die endliche positive Reserve ist relativ zu diag(K12,alt,I84), nicht
relativ zur vollen L2-Norm und nicht als Tailboden 1/20 zu verstehen.
Alle geerbten analytischen Operatorvoraussetzungen bleiben Voraussetzungen.
A8->A9 und der vollständige unendliche Rest sind offen.
