Objekt X — Gegenprüfung ganzer F12/D12-Funktionen und Fehlertransport
15. Oktober 2026

Mit ANSCHLUSS_GPT2.txt und HERLEITUNG_GPT1.md beginnen.

Vollständiger frischer Paket-Replay (Python 3.11+, Standardbibliothek):
  python -B -X utf8 verify.py --output ../new-unused-directory
Das Ausgabeziel muss neu und außerhalb des Pakets sein.

Originalarchiv: originals/Objekt-X-A9-A11-Ganze-Kraftfunktionen-und-D12-2026-10-15.zip
Es bleibt unverändert. Der Replay baut dessen drei Ergebnisdateien neu auf,
prüft dann unabhängig sämtliche Funktionsspalten und führt den neuen
Fehlertransport aus. Ältere eingebettete Replays werden nicht nochmals gestartet.

Die wichtigsten Quittungen:
reports/AUDIT.json                  Umfang und ausdrückliche Grenzen
reports/ORIGINAL_REPLAY_AUDIT.json   tatsächlich frischer Eingangsreplay
reports/INDEPENDENT_FUNCTIONS.json  unabhängige Ganzfunktions-/Momentprüfung
reports/RESPONSE_ERROR_BUDGET.json  feste rationale Antworten, exakte Projektions-
                                   koeffizientenintervalle, direkte K-Fehlerpreise

Projektierte gespeicherte D-Modelle auswerten, nach einem Replay:
  python -B evaluate_projected_D.py --source ../new-unused-directory/input/objekt-x-whole-functions12-2026-10-15 --budget reports/RESPONSE_ERROR_BUDGET.json --parity even --index 0 --fraction 1/2
Die Ergebnisintervalle gelten für das exakt projizierte MODELL, nicht punktweise
für die tatsächliche Wirkungsfunktion. Der wahre Abstand ist global L2 zertifiziert.
Die Projektion benutzt den exakten Momentkoeffizienten, nicht seinen Mittelpunkt.

Offen: vollständige W9-Verstärkung und gesamte Residualenergie, kompakter Gate,
A9->A11-Abschluss und neue A11-Inverse. GitHub wurde nicht verändert.
