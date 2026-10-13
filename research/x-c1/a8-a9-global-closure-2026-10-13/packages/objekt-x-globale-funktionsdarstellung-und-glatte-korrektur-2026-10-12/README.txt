Objekt-X-Globale-Funktionsdarstellung-und-glatte-Korrektur-2026-10-12

Mit ANSCHLUSS_GPT1.txt und PROOF.txt beginnen.

Neu: ein vollständiger Auswerter des rohen Funktionsmodells auf der
ganzen Schale, vollständige Cauchy-Transformationen der Logarithmen und
ein separater rationaler Fehlerpreis <10^-300 für die glatte Moment-
und T-Projektionskorrektur oberhalb Grad 103.

Offen: der globale Modellgram und die übrige tatsächliche Modellabweichung.
Die Kontrollpunkte sind keine globale Integrations- oder Positivitätsprüfung.

Reiner rationaler Replay (Python >=3.11, Standardbibliothek):
 python -B reproduce.py

Frischer Aufbau beider Funktionsmodelle mit 4096 Bit und unabhängige
Kontrolle der Cauchy-Primitiven (python-flint 0.9):
 python -B reproduce.py --rebuild

Falls python-flint in einer getrennten Laufzeit liegt:
 python -B reproduce.py --rebuild --python PFAD_ZU_PYTHON --deps PAKETVERZEICHNIS

Das Datenverzeichnis enthält dieselben Modelle bei 3072 und 4096 Bit.
1218 Punktwertintervalle werden verglichen; zusätzlich werden alle
609 Logkoeffizienten je Parität gegen den Vorgänger abgeglichen.
Die finite Projektion P_<104 und das globale Gram-Integral sind hier
noch nicht berechnet. Keine Zahl in diesem Paket ist als Tailboden gemeint.

snapshot enthält ausschließlich unveränderte benötigte Eingabefelder und
die verwendeten mathematischen Hilfsprogramme. SNAPSHOT_ORIGINS.json
nennt die Hashes der vollständigen Vorgänger und der tatsächlichen Auszüge.
Die Extraktion ändert keine der verwendeten Zahlen. Der neue Prüfer
funktioniert nach dem Entpacken ohne den früheren Arbeitsverzeichnisbaum.
Die unveränderten C0-Zeilen und E_dir-Koeffizienten des Reviews liegen
zusätzlich in data/DIRECTIONAL_DERIVATIVE_TARGET.json. Zur späteren
Auswertung der Zielmatrix gehören weiterhin die vollständigen D- und
M_upper-Daten des gebundenen Antwortpakets; ein neuer Matrixtest wird
durch dieses Beilegen nicht behauptet.

Alle Operatoraussagen bleiben unter den geerbten Voraussetzungen.
FULL_REMAINDER_CERTIFIED=false; TAIL_FLOOR_1_OVER_20_CERTIFIED=false.
