Objekt X — gemeinsame Verlustbilanz, 10. Oktober 2026

Start: BERICHT.txt. Formeln, Fehler und neue offene Aufgabe: HERLEITUNG.txt.
Alle früheren Originalarchive bleiben unverändert im gebundenen Vorgänger.
Voraussetzung: Python 3.12 und python-flint 0.9.0 (pip install python-flint==0.9.0).

  python reproduce.py

Prüft das neue Manifest, vier verschachtelte Archivbindungen und sämtliche
geerbten Manifeste, setzt die neue endliche Verlustbilanz erneut zusammen
und prüft 499 Intervallvergleiche. Erzeugt REPLAY.json. Benötigt Speicher
für entpackte Vorgängerarchive. Kein erneuter Lauf der langen Integrationen.
Optional kann --deps PFAD eine lokale python-flint-Installation angeben.

  python reproduce.py --integrate

Wiederholt zusätzlich alle neuen Integrationen und Kalibrierungen in einem
eigenen Unterverzeichnis. Dafür eine frische Paketentpackung verwenden.
Keine Integrationen der übernommenen ursprünglichen Zertifikate werden
erneut ausgeführt. Der neue Gram auf ganz T wird ebenfalls nicht berechnet.

Die dokumentierten zwei Prüfrichtungen sind kein Vollraumbeweis.
Die starre 11-%-Teilaufgabe ist widerlegt; der volle gemeinsame Test bleibt offen.
FULL_REMAINDER_CERTIFIED=false; EXTERNAL_REVIEW_OPEN.
