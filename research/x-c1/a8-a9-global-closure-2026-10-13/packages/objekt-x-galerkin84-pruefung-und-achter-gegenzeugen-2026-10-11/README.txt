Objekt X — Galerkin84-Prüfung und Achter-Gegenzeugen

Schneller eigenständiger rationaler Replay (Python 3, Standardbibliothek):

  python reproduce.py

Dabei werden alle Manifestbindungen und die neuen Gegenzeugen geprüft.
Der Replay bestätigt nicht die analytischen Voraussetzungen der geerbten
Operatorgrenzen. Diese sind in BERICHT.txt ausdrücklich aufgeführt.

Neuerzeugung aus dem gebundenen Originalpaket:

1. Das Originalpaket Objekt-X-Galerkin84-und-Verlusttest-2026-10-11.zip
   frisch entpacken. Erwartete SHA256:
   461eee1352a82cadf9c9a8ec6540f782ad9ceb0490c0fa28afa93392dccd7c28
2. Im Originalpaket dessen reproduce.py ausführen. Das entpackt auch
   die gebundenen Vorgänger und prüft die Originalzertifikate.
3. Aus diesem Rückgabepaket:

   python check_bridge_obstruction.py --root PFAD_ZUM_ORIGINALPAKET --out NEUER_AUSGABEORDNER

   Die beiden JSON-Dateien müssen inhaltlich identisch mit den hier
   beigelegten Dateien sein. Die Ausgabedateien enthalten keine lokalen
   absoluten Pfade.

4. Optional die hypothetischen Galerkin-Matrizen erneut aufbauen:

   python rebuild_conditional_gates.py --root PFAD_ZUM_ORIGINALPAKET --out NEUE_GATE_QUITTUNG.json

   Hierfür wird python-flint 0.9.0 benötigt; --deps PFAD kann ein lokales
   Paketverzeichnis angeben. Keine numerische Eigenwertsuche wird benutzt.

Die Dateien REPLAY_ORIGINAL.json und FINITE_SCHUR_REPLAY.json sind Quittungen
der hier ausgeführten Prüfungen, keine frischen Operatorintegrationen.
Das große Originalarchiv wird in diesem Rückgabepaket nicht dupliziert.

Alle Ergebnisse bleiben AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.
