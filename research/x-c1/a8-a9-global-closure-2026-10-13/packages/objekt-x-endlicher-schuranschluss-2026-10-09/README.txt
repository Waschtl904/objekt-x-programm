Objekt X — positiver endlicher gemeinsamer 4+8-Schuranschluss
9. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Ergebnis: Nach Eliminierung des alten Raums und des Viererblocks gilt
in beiden Paritäten Sigma_Y >= (1/25000) WY auf denselben acht Y-Spalten.
Der ganze unendliche neue Rest bleibt offen.

Lesen: BERICHT.txt; danach HERLEITUNG.txt und EXACT_CHECK.json.

Schneller vollständiger Paket-Replay mit der Python-Standardbibliothek:
  python reproduce.py --out meine_pruefquittung.json

Getestet mit Python 3.13. Nicht mit python -O ausführen, da die Prüfer
assert verwenden. Der Replay kann wegen der acht 191D-Ganzzahlprüfungen
mehrere Minuten benötigen. Er zeigt die abgeschlossenen Schritte an.
Er prüft alle Manifestbindungen und reproduziert die rationalen Schluss-
zertifikate. Er wiederholt nicht die vollständigen Gamma-Matrixintegrationen.

Optionale gerichtete Neuberechnung, mit python-flint==0.9.0:
Die Programme liegen in work/gamma-low-2026-10-09. Die großen Läufe
nacheinander starten. Es gab bei paralleler Ausführung einen Speicherabbruch;
der anschließende einzelne Wiederholungslauf ist vollständig abgeschlossen.

Neue Ausgaben getrennt erzeugen, etwa aus dem Paketverzeichnis:
  python work/gamma-low-2026-10-09/compute_correction.py --bits 3072 --out rerun/CORRECTION_3072.json
  python work/gamma-low-2026-10-09/compute_upper.py --bits 3072 --correction rerun/CORRECTION_3072.json --tag rerun_default --out rerun/RESPONSE_3072.json
  python work/gamma-low-2026-10-09/compute_upper.py --bits 3072 --correction rerun/CORRECTION_3072.json --tag rerun_tight --padding 1/100000000 --out rerun/RESPONSE_TIGHT_3072.json
  python work/gamma-low-2026-10-09/compute_shell_gamma.py --bits 3072 --out rerun/SHELL_GAMMA_3072.json

Analog mit 4096 Bit und neuen Dateinamen. Zusätzliche Inversenzertifikate
werden im Programmverzeichnis unter dem gewählten neuen --tag abgelegt.
Die gespeicherten Originalergebnisse werden so erhalten. Die Schurprogramme
verwenden bewusst die gebundenen offiziellen Eingaben; reproduce.py prüft
genau diese ursprünglichen Zertifikate. Keine Netzwerkzugriffe.

Erhaltene Stufen:
  RESPONSE_*, SCHUR_*: nur alte Gamma224-Korrektur, t=1/1000; noch offen.
  SCHUR_SHELL_*: zusätzlich direkte Schalen-Gamma-Form; noch offen.
  RESPONSE_TIGHT_*, SCHUR_SHELL_TIGHT_*: t=10^-8 samt Gegenfehler; positiv.
  SCHUR_EXACT.json: rekonstruierte Stufen und vier positive Endzertifikate.

Die zuvor verwendeten Response-Dateien enthalten weitere historische Felder.
Aktuell ausgewertet werden die gemeinsame obere/untere Energie, U-L und
der signierte C-Mittelpunkt. Alte U00-Diagnosen sind keine neuen Resultate.

Die beigefügte Gegenprüfung des Nutzers bestätigt das Vorgängerpaket 91/50.
Sie ist keine Gegenprüfung der hier neu durchgeführten Gamma-Rechnungen.
Auch zwei Präzisionsläufe ersetzen keine externe mathematische Begutachtung.

Die analytische Bedeutung bleibt von den geerbten Form-/Domänenidentitäten
und Modellmajoranten abhängig. Der frühere konservative feste M_--Normgate
bleibt widerlegt. Dieses Paket behauptet weder FULL_REMAINDER_CERTIFIED
noch eine Konstruktion von Objekt X. GitHub wurde nicht verändert.
