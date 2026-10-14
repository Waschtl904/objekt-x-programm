Objekt X — Gegenprüfung des ursprünglichen Basis84-Tailbodens
14. Oktober 2026

Beginnen mit BERICHT.txt, danach HERLEITUNG_GPT2.txt.

Inhalt:
  inputs/: unverändertes vollständiges Eingangspaket;
  reports/FULL_SOURCE_REPLAY.json: hier frisch ausgeführter vollständiger
    Original-Replay mit beiden externen Quellen und 574 Pivots;
  reports/INDEPENDENT_AUDIT.json: eigene Bruchrechnung und zusätzliche
    direkte Quellenkette Antwort -> Common96 -> ursprüngliche Basis;
  verify.py: wiederholbare Prüfungen mit der Python-Standardbibliothek;
  MANIFEST.json: Dateigrößen und SHA256 aller festen Paketdateien.

Schneller Replay aus einem frisch entpackten Verzeichnis:
  python -B -X utf8 verify.py

Erneuter direkter Quellenabgleich mit den großen Originalarchiven:
  python -B -X utf8 verify.py --schur-package PFAD/Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13.zip --basis-package PFAD/Objekt-X-Basis84-und-Abdeckungspruefung-2026-10-10.zip

Vollständige erneute 574-Pivot-Rechnung zusätzlich:
  python -B -X utf8 verify.py --full-source-replay --schur-package PFAD/Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13.zip --basis-package PFAD/Objekt-X-Basis84-und-Abdeckungspruefung-2026-10-10.zip

Die Originalarchive sind extern, aber durch ihre SHA256 gebunden. Der
Standardlauf weist nicht ausgeführte optionale Prüfungen ausdrücklich aus.
Er prüft das gespeicherte vollständige Protokoll auf Übereinstimmung mit
dem Eingangspaket, erklärt dies aber nicht zum neu ausgeführten Pivotlauf.
REPLAY.json ist die jeweils neu erzeugte Quittung und nicht Teil des Siegels.

Alle Resultate sind bedingt auf die bezeichneten analytischen Eingaben.
Eine externe Gesamtbegutachtung und Objekt X insgesamt bleiben offen.
