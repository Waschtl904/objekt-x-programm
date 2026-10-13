Objekt X — Unendlicher Dualrest und Außenrichtungsprüfung, 11. Oktober 2026

BERICHT.txt enthält Ergebnis und Grenzen.
INFINITE_REDUCTION.txt enthält den neuen globalen Anschluss mit Beweis.
EXTERNAL_PROBES.txt beschreibt die zusätzlich integrierten Prüffunktionen.
data/ enthält neue tatsächliche Integrationen, rationale Richtungen,
Matrix-/Fehlerdaten und die globale skalare Rechnung.
code/ enthält die Programme für die frischen Integrationen und Herleitungen.
logs/ dokumentiert die vier ausgeführten neuen Integrationen.

Rationaler Replay nach Entpacken, ohne zusätzliche Bibliotheken:

  python -B reproduce.py

Er prüft Dateibindungen, vollständige skalare Momentrestgrenzen, die
bedingte grobe Normrechnung, 9504 neue Präzisionsvergleiche und die beiden
Neuner-Zertifikate durch rationale Intervall-LDL-Prüfung. Die analytischen
Form-/Quellenvoraussetzungen werden durch diesen Replay nicht bewiesen.
Die neuen GPT-2-Antworten oder ein vollständiger Residualgram liegen nicht bei.

Für neue Integrationen werden Python, python-flint, numpy sowie der
Galerkin84-Vorgänger mit dem neu aufgebauten direct-rest84-Zweig benötigt.
ROOT muss auf dessen Wurzel zeigen; die gebundenen Quellen stehen in den
JSON-Dateien. Es werden keine Originalarchive verändert.

Beispiel für die gerade Parität (Ausgabedatei darf noch nicht existieren):

  python -B code/compute_external_probe.py --root ROOT --proposal data/even_proposal.json --count 8 --bits 3072 --parity even --out PROBE_EVEN_NEU.json
  python -B code/analyze_probe.py --root ROOT --probe PROBE_EVEN_NEU.json --out RESULT_EVEN_NEU.json
  python -B code/build_infinite_reduction.py --root ROOT --out INFINITE_REDUCTION_NEU.json

Für die ungerade Parität entsprechend odd_proposal.json und --parity odd.
Die 4096-Bit-Läufe verwenden --bits 4096. Modelle werden mit gerichteten
Intervallen verglichen, nicht anhand identischer Laufzeiten oder Hashes
von Dateien mit Laufzeitfeldern. Die großen Vorgängerarchive sind extern
gebunden und nicht erneut eingebettet.

Nicht mit Python -O starten: assert-Anweisungen gehören zu den Prüfungen.
Ein erfolgreicher Replay bedeutet weiterhin FULL_REMAINDER_CERTIFIED=false.
