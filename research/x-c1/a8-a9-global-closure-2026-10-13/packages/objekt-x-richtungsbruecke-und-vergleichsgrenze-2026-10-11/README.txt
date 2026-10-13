Objekt X — Richtungsbrücke und Vergleichsgrenze, 11. Oktober 2026

Mit BERICHT.txt beginnen. HERLEITUNG.txt enthält die genaue Aussage,
ihre Operatorvoraussetzungen und die vollständigen Fehlerpreise.

Schneller eigenständiger rationaler Replay, Python 3 Standardbibliothek:

  python -B reproduce.py

Der Replay prüft Manifest, neue Matrixuntergrenzen, 640 Präzisionsvergleiche,
vier gerichtete rationale Eigenwert-Obertests, die rationalen unteren
Prüfrichtungen und die zwei oberen Vergleichsgegenzeugen. Er führt keine
Operatorintegration aus und beweist geerbte analytische Voraussetzungen
nicht neu. Ein absichtlich indefiniter Kontrollfall muss abgewiesen werden.

Optional: sämtliche neuen Integrale und Matrizen frisch erzeugen:

1. Gebundenes Originalpaket frisch entpacken und dessen reproduce.py
   ausführen, damit die gebundenen Vorgänger entpackt sind.
2. Mit Python inklusive python-flint 0.9.0, numpy und scipy:

   python -B rebuild_from_parent.py --root PFAD_ZUM_ENTPACKTEN_ORIGINALPAKET

Das schreibt nur einen neuen Arbeitsordner im entpackten Originalpaket.
Es werden vier neue Integrationen (zwei Paritäten, zwei Präzisionen), die
beiden Matrixrechnungen und der rationale Audit ausgeführt. Der Audit muss
inhaltlich identisch sein. In den Integraldateien darf nur seconds abweichen.
Die Programme sind beigelegt; die Rechenbibliotheken sind nicht beigelegt.

Gebundenes großes Originalpaket, unverändert:
Objekt-X-Galerkin84-und-Verlusttest-2026-10-11.zip
SHA256 461eee1352a82cadf9c9a8ec6540f782ad9ceb0490c0fa28afa93392dccd7c28

Eingegangenes Prüfpaket, unverändert:
Objekt-X-Galerkin84-Pruefung-und-Achter-Gegenzeugen-2026-10-11.zip
SHA256 0fbf3728ef7f532b28c5dbb5fb4ad8710fbe450a731c956bf2afcc688aecb564

AUDIT_INPUT.json enthält einen gebundenen rationalen Datenauszug. Die
Integral- und Matrixdateien enthalten ihre eigenen Herkunftsbindungen.
Der kompakte Eingang BRIDGE_OBSTRUCTION_INPUT.json wurde hier nochmals
aus dem gebundenen Original rekonstruiert.

Die neuen Brücken sind verbessert, aber der notwendige endliche Test
bleibt negativ. Der zusätzliche Gegenzeuge widerlegt nur den gemeinsamen
Vergleich bei festem U_op und L_+. Keine negative tatsächliche Schurform,
kein Tailboden 1/20 und kein Abschluss A8->A9 werden behauptet.

AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN
