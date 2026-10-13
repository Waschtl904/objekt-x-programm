Objekt X — Modellfehler-Gegenprüfung und skalarer Integralanschluss

Beginn: ANSCHLUSS_GPT2.txt, dann HERLEITUNG.txt.

Rationaler Replay mit Python 3.10 oder neuer, ohne Fremdpakete:
    python -B reproduce.py

Er prüft die Dateibindungen, spielt das unveränderte v2-Eingangspaket
rational nach und rekonstruiert die vollständigen neuen Kongruenzen.
Die beiden vollständigen Originalantwortdateien sind eingebunden.
Ein optionales --receipt DATEI schreibt eine externe Prüfquittung.

Dateien:
data/SCALAR_GATE.json: feste rationale Gewichtungen und Polynome.
data/FINITE_TARGET_INPUT.json: aktuelle vollständige Zielmatrizeingaben.
data/DIRECTIONAL_DERIVATIVE_TARGET.json: unverändertes E_dir.
data/SCALAR_GATE_AUDIT.json: rational bestätigte Kongruenzgrenzen.
data/MODEL_ERROR_REPLAY_RECEIPT.json: hier ausgeführter Eingangsreplay.
data/CURRENT_SNAPSHOT_AUDIT.json: Vergleich mit verfügbaren Originalen.
data/SCALAR_DIAGNOSTIC.json: ausschließlich numerische Orientierung.
inputs/: unverändertes v2-ZIP und vollständige Originalantwortdateien.

build_scalar_gate.py schlägt die feste Gewichtung mit python-flint vor;
audit_scalar_gate.py prüft sie unabhängig mit rationalen Intervallen.
Der Replay benötigt den Vorschlagsalgorithmus und python-flint nicht.
diagnose_scalar_gate.py benötigt numpy und python-flint und verwendet
ausschließlich die beigefügten älteren Gauß-Punktdatensätze. Er ist
kein Bestandteil des Positivitätsbeweises.

Keine Ausführung dieses Pakets berechnet den vollständigen neuen
globalen Integralgram. Alle Statusfelder hierzu bleiben false.
Originalarchive werden nicht verändert; temporäre Eingangsreplays
laufen in einem eigenen entpackten Verzeichnis.
