# X-C1-CONNECTED-3/8 — lokales Arbeitspaket

Stand: 17. September 2026. Neue analytische Autorenableitung; externe Prüfung offen.
Kein GitHub-Push oder Merge wurde für dieses Paket ausgeführt.

1. X_C1_CONNECTED_MOMENT_FACTORIZATION.md: vollständiger Nachweis, Output, Formdomain und Grenzen.
2. check_connected_constants.py: Python-Standardbibliothek, 40 unterstützende exakte Skalar-/Polynomchecks.
3. connected_checks.log und connected_results.json: tatsächlich erzeugte lokale Ausgaben.
4. SHA256SUMS: Identität dieser Dateien, keine unabhängige Beweisfreigabe.

Reproduktion aus einem frischen Verzeichnis:
    python /pfad/check_connected_constants.py > connected_checks.log

Der Prüfer schreibt connected_results.json in das aktuelle Arbeitsverzeichnis.
Der analytische Beweis der Operatoridentitäten bleibt eigenständig nötig.
Kein A1-Replay, kein CI-Lauf, keine Ausgabe auf dem ganzen Fenster (-1,1),
kein all-window- oder Objekt-X-/RH-Abschluss und keine Literatur-Neuheitsbehauptung.
