Objekt-X-Globalmodell-Gegenpruefung-und-Fehlerrueckbindung-2026-10-12

Mit BERICHT.txt und ANSCHLUSS_GPT2.txt beginnen. PROOF_REVIEW.txt enthält
die neuen bedingten Herleitungen. inputs enthält das unveränderte
Eingangspaket; data enthält gebundene Auszüge und die neuen Rechendaten.

Reiner rationaler Replay, Python >=3.11, Standardbibliothek:
 python -B reproduce_review.py

Rationaler Replay plus erneute numerische Gramdiagnose aus den neuen
gespeicherten Quadraturwerten, mit python-flint 0.9, NumPy und SciPy:
 python -B reproduce_review.py --diagnostic

Frischer Aufbau beider Eingangsmodelle und Cauchy-Kontrollen:
 python -B reproduce_review.py --rebuild-models

Optional kann --deps VERZEICHNIS einen zusätzlichen Python-Paketpfad setzen.
--receipt DATEI schreibt eine Prüfquittung. Der schnelle Replay ist keine
erneute physische Funktionsauswertung und kein Quadraturfehlernachweis.

Vier neue Quadraturen vollständig neu berechnen:
Das ZIP aus inputs zuerst in einen eigenen Ordner entpacken. Dann je
Parität mit dessen entpacktem Paketverzeichnis als --package ausführen:

 python -B probe_global_gram.py --package PAKETORDNER --parity even --outdir NEUER_ORDNER
 python -B probe_global_gram.py --package PAKETORDNER --parity odd --outdir NEUER_ORDNER

Der Ausgabepfad muss neue REBUILT_EVEN/ODD-Dateien aufnehmen können.
--orders 128,256 ist die Voreinstellung. Diese Rechnung benötigt mehrere
Minuten pro Parität. Die Vorschläge und Quadraturmatrizen sind ausdrücklich
keine vollständigen oberen Gramgrenzen.

data/BOOTSTRAP_INPUT.json enthält unveränderte benötigte Felder aus den
gebundenen Antwort-, Quell- und Logpaketen; darunter die vollständigen
beiden M_upper-Matrizen. Herkunft und Dateihashes stehen in den Daten und
PROVENANCE.json. Der Prüfer rekonstruiert die Spuren, Verstärkungsfaktoren
und zulässigen Fehlerpreise exakt rational.

data/quadrature enthält NPZ-Dateien mit Knoten, Gewichten, Modellwerten,
Grad-103-Vorschlägen und numerischen Gramen. Die separaten POINTS-Dateien
enthalten gerichtete rationale Punktwertintervalle. Die Koeffizienten in
POLYNOMIAL_CANDIDATES.json sind festgelegte dyadische rationale Vorschläge.

Alle Aussagen bleiben an die geerbten analytischen Voraussetzungen gebunden.
FULL_REMAINDER_CERTIFIED=false; TAIL_FLOOR_1_OVER_20_CERTIFIED=false.
