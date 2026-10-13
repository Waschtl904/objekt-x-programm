Objekt X — globaler Gram und vollständige niedrige Projektion
13. Oktober 2026

ERGEBNIS: Beide vollständigen globalen Gram-Bedingungen (C5) bestehen.
Unter den geerbten Voraussetzungen gilt U_g<=H=E_dir/10920 für den
tatsächlichen regularisierten Rest. Die externe Gegenprüfung steht aus.
Mit BERICHT.txt beginnen; ANSCHLUSS_GPT1.txt nennt den nächsten Auftrag.

Gegenstand ist der ganze 203x203-Gram der zusammengesetzten globalen
Modellfunktion nach rationalem Abzug der drei führenden Logarithmen
und nach orthogonaler Projektion auf Grade ab 104. Beide Ränder,
alle Primzellen, sämtliche Kreuzterme und alle Näherungsreste bleiben
enthalten. Die zugehörige vollständige physische Modellabweichung ist
im eingebetteten Vorgängerpaket v2 gebunden.

PROOF.txt enthält die vollständige analytische Integrationsherleitung.
data/GRAM_*.json enthält Gram, 104x203-Projektion, hohen Gram und Fehler.
data/AUDIT_*.json enthält die unabhängigen rationalen Matrixprüfungen.
snapshot/ enthält die unveränderten verwendeten Eingabefelder und Code.
SNAPSHOT_ORIGINS.json dokumentiert die Herkunft der Feldauszüge.
MANIFEST.json bindet alle ausgelieferten Dateien mit SHA256.

Rationaler Replay, nur Python-Standardbibliothek:
 python reproduce.py --receipt PRUEFQUITTUNG.json

Vollständiger Neuaufbau einschließlich aller Integrationen:
 python reproduce.py --rebuild --python PFAD_ZUM_MATHEMATIK_PYTHON
                     --deps PFAD_ZU_PYTHON_FLINT_0_9_0
                     --receipt NEUAUFBAU.json

Der Neuaufbau ist rechenintensiv. Er speichert örtliche Zwischenstände.
Die pkl.gz-Zwischenstände sind ausschließlich selbst erzeugte Laufdaten;
fremde Pickle-Dateien dürfen nicht geladen werden. Sie gehören nicht zum
ausgelieferten Beweiszertifikat. Der rationale Replay benötigt sie nicht.

Alle operatorbezogenen Aussagen bleiben von den geerbten Operator-
und Domänenvoraussetzungen abhängig. Der Abschluss A8->A9 und der
Tailboden 1/20 dürfen erst nach vollständiger Schlussprüfung behauptet
werden; dieses Paket enthält diese Behauptung nicht.
