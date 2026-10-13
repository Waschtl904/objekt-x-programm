Objekt X — vollständige Taildomäne und korrelierte Schurfortsetzung
9. Oktober 2026
AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Lesereihenfolge: BERICHT.txt, HERLEITUNG.txt, CHECKS.json.

Ergebnis dieses Arbeitsblocks:
- Live-Main festgestellt: da50f0a21691e6fd253163e612a2af2898606581.
- Vollständiger begrenzter Replay des separaten positiven 4+8-Pakets bestanden.
- Exakte Domäne nach den tatsächlichen zwölf Funktionen und vollständige
  Finite/Tail-Schur- und Residualdarstellung formuliert.
- Bedingtes fernes Tail-Lemma: 64 verschwindende lokale Legendrekoeffizienten
  genügen zusammen mit den benannten Moment-, Kraft- und Kopplungsbedingungen
  für einen Boden 1/10 auf einem vollständigen unendlichen Teilraum.
- Der gesamte neue A8->A9-Tail und seine Kopplung bleiben OPEN.

Reproduzierbarer kleiner Check mit Python-Standardbibliothek:
  python3 check_tail.py

Er prüft die Paketbindungen, die exakte rationale neue Tailkonstante und
zwei ausdrücklich synthetische algebraische Kontrollfälle. Er beweist
keine Operatordomänenidentität und berechnet keine neuen Operatorintegrale.

FINITE_REPLAY.json und FINITE_REPLAY.log dokumentieren den in dieser Sitzung
wirklich ausgeführten vollständigen begrenzten Replay des Vorgängerpakets.
Das rund 50-MB-Originalarchiv ist nicht erneut beigepackt; sein SHA-256
und seine bestehende Identität stehen in SOURCE_BINDINGS.json.

sources/ enthält die konkret benutzten Herleitungen. GitHub-Texte sind
UTF-8-Lesekopien am angegebenen Commit; Git-Blob-IDs und lokale Bytehashes
sind getrennt verzeichnet. Historische dortige Statusangaben bleiben erhalten.
Insbesondere ist der alte feste M_--Normgate inzwischen widerlegt.

Kein GitHub-Schreibzugriff, keine Website, keine neue A9->A11-Rechnung.
