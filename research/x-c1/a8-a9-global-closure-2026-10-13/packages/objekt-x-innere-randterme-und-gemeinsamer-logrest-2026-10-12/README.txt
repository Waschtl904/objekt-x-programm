Objekt X — Innerer Rand und gemeinsamer Logarithmusrest
12. Oktober 2026

Start: ANSCHLUSS_GPT1.txt, BERICHT.txt, PROOF.txt.

Reproduzierbare rationale Prüfung, Python-Standardbibliothek:

python -B reproduce.py --responses-zip PFAD/Objekt-X-Neue-Antworten84-und-Residualbudget-2026-10-11.zip --common-zip PFAD/Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip

Das Programm entpackt frisch, kontrolliert alle Hashes und Manifeste,
führt den rationalen Replay des eingebetteten Eingangspakets aus und
rekonstruiert den neuen gemeinsamen Randtest. JSON-Inhalte werden nach
dem Parsen verglichen, sodass Windows/Linux-Zeilenenden unschädlich sind.

Enthalten:
- vier TRACES-Dateien: vollständige gerichtete Randintegrationen,
- INNER_LOG_1536.json: unabhängige direkte innere Sprungrechnung,
- zwei COMPOSED-Dateien: gemeinsam gebildete drei Randzeilen,
- audit.py und AUDIT.json: rationaler Aufbau und 206x206-Schurtests,
- compute_endpoint_traces.py: ausführbare vollständige Randintegration,
- build_endpoint_engine.py und endpoint_tail.py: Herkunft des Integrators,
- compute_inner_log.py und compose.py: gerichtete Modellrechnungen,
- eingebettetes Eingangs-ZIP und gebundener alter Operatorinput.

Für einen erneuten gerichteten Neuaufbau werden python-flint, die
gebundenen Vorpakete und der bisherige Arbeitsbaum benötigt:

python -B compute_endpoint_traces.py --root ARBEITSBAUM --parity even --bits 3072 --out NEUE_DATEI.json

Ebenso odd sowie jeweils 4096 Bit. Eine bestehende Ausgabedatei wird
nicht überschrieben. Der rationale Replay benötigt diesen Arbeitsbaum
und python-flint nicht.

Gültiges Ergebnis: vollständiger gemeinsamer Logarithmusanteil ab
Grad 104 <0,2 % bzw. <0,4 % der richtungsabhängigen Budgetmatrix,
unter den geerbten Operatorannahmen und der offengelegten Randherleitung.
Kein vollständiger Residual-, Tailboden- oder A8->A9-Abschluss.
