Objekt X — stärkerer vollständiger alter hoher Boden
8. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Ergebnis: alter hoher Boden 91/50 statt 2/3; in beiden Paritäten eine
streng kleinere gemeinsame 12x12-Obermatrix der alten Inversenergie.
Der endliche neue Schurtest und der vollständige neue Rest bleiben offen.

Lesereihenfolge: BERICHT.txt, HERLEITUNG.txt, EXACT_CHECK.json.

Schneller Replay (Python-Standardbibliothek; getestet mit Python 3.13):
  python reproduce.py --out meine_pruefquittung.json

Er prüft sämtliche Manifestbindungen, die rationalen Konstanten,
vier vollständige 191D-Inversenzertifikate, die gemeinsame zwölfspaltige
Fehlerrechnung, die strikte Obermatrixverbesserung, vier endliche
Schurrekonstruktionen und den Vergleich von 288 Obermatrixeinträgen.
Die 191D-Ganzzahlmultiplikationen können einige Minuten beanspruchen.
Nicht mit python -O ausführen: die Prüfungen verwenden assert.

Eine erneute gerichtete Rechnung benötigt zusätzlich python-flint==0.9.0.
Das ist eine Algebrawiederholung auf gespeicherten Integralen, keine neue
Operatorintegration. Beispiel, jeweils aus dem Paketverzeichnis:
  python work/high-floor-2026-10-08/compute_upper.py --bits 1024 --tag rerun --out response_rerun_1024.json
  python work/high-floor-2026-10-08/compute_upper.py --bits 1536 --tag rerun --out response_rerun_1536.json
  python work/high-floor-2026-10-08/diagnose_next.py

Die Diagnose ist von den Zertifikaten getrennt: ihre Zahlen sind lokale
Empfindlichkeiten einer Oberhülle, keine bewiesenen künftigen Gewinne.

Die analytische Herleitung ist neuer zu begutachtender Inhalt. Ein
erfolgreicher Rechnerlauf ersetzt keine Prüfung dieser Herleitung oder
der geerbten Formidentitäten. Kein externer mathematischer Review erfolgt.

Die alten Response-Felder bleiben teilweise als Provenienz erhalten.
Aktualisiert und verwendet werden U, U-L und der korrelierte C-Mittelpunkt.
Alte relative Breiten und weitere Diagnosen sind keine neuen Ergebnisse.

Die beiden Präzisionsläufe zertifizieren sich jeweils selbst. Ihre rationalen
Obermatrizen unterscheiden sich maximal um weniger als 6e-54. Dies ist kein
Intervallüberlappungstest. Die Hilfsmatrizen P im endlichen Schurtest werden
je Lauf rational festgelegt; keine frühere Präregistrierung wird behauptet.

Pfade sind relativ zum Paket und unter Windows/POSIX lesbar. Es gibt keine
Netzwerkzugriffe. Originalarchive bleiben unverändert; die benötigten
Quell-Dateien sind einzeln byteidentisch eingebunden und hashgebunden.
