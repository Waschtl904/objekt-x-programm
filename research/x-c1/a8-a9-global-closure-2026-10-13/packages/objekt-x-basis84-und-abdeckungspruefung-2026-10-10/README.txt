Objekt X — tatsächliche Basis84 und Abdeckungsprüfung, 10. Oktober 2026

Start: BERICHT.txt. Vollständige Herleitung: HERLEITUNG.txt.
Die Nutzerübergabe und das letzte tatsächliche Rechenpaket sind unverändert
in inputs/ enthalten, einschließlich aller gebundenen Vorgängerarchive.

Python-Standardbibliothek:
  python reproduce.py

Prüft alle Archiv-/Manifestbindungen, die beiden übergebenen Prüfprogramme,
die tatsächliche rationale Basis, die vollständige lokale Fehlerbezahlung
und die erwartete Ablehnung des konservativen Gesamtgates. REPLAY.json ist
die Prüfquittung. Entpackte Vorgänger entstehen unter work/. Dieser Replay
führt keine ursprünglichen großen Operatorintegrationen erneut aus.

Zusätzlich mit Python 3.12 und python-flint 0.9.0:
  python reproduce.py --compute

Erzeugt die neuen gerichteten Funktions-/Normrechnungen erneut und prüft sie
anschließend rational. Eine lokale Bibliotheksinstallation kann durch
--deps PFAD angegeben werden. Auf dem Autorenrechner wurde python-flint 0.9.0
mit 768 Bit verwendet. Der normale rationale Replay benötigt es nicht.

BASIS_*.json enthält die exakten rationalen Basis- und Fitdaten sowie
vollständige analytisch begründete Fehlergrenzen. GATE_*.json enthält
tatsächliche konservative Eingaben im Format des übergebenen Prüfers.
Beide müssen COVERAGE_BOUND_INCONCLUSIVE ergeben. Nur die ersten 65
Zeilen als Gesamtzertifikat einzureichen wäre sachlich falsch.

FULL_REMAINDER_CERTIFIED=false. EXTERNAL_REVIEW_OPEN.
