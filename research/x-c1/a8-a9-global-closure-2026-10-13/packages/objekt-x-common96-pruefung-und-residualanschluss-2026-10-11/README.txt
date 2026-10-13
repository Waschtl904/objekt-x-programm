Objekt X — Prüfung Common96 und Residualanschluss, 11. Oktober 2026

BERICHT.txt: Ergebnis, tatsächlicher Reproduktionsumfang und Einschränkungen.
RESIDUALANSCHLUSS.txt: konkrete neue Residualidentität, Metrik und Beweisziel.
RESIDUAL_SETUP.json / check_residual_setup.py: neue rationale skalare Prüfung.
FRESH_REBUILD_REVIEW.json: Vergleichsquittung des tatsächlich ausgeführten
  frischen Neuaufbaus einschließlich der nicht zertifizierenden Abweichungen.
INPUT_AUDIT_COPY.json: unveränderte Kopie der nachgerechneten Eingangsquittung.
logs/: Protokolle des Eingangs-Replays und des vollständigen Neuaufbaus.
MANIFEST.json: SHA256-Bindung der Dateien dieses Rückgabepakets.

Das rund 70 MB große Eingangspaket ist extern gebunden, nicht eingebettet:
Objekt-X-Direkte-Restform-und-Positiver-96er-Block-2026-10-11.zip
SHA256 06b4cc975b8e6bd8f6088a151ea1dcaebd38862f7a50e3f2f2b22ebb05afef51

Schneller Replay mit Python 3.10 oder neuer, nur Standardbibliothek:

  python -B reproduce.py --input-zip /pfad/zum/Eingangspaket.zip

Prüft beide Manifeste, Archivbindung, Kopie der Eingangsquittung und die
neuen skalaren Aussagen einschließlich D84-Zeilensummenschranken. Dieser
schnelle Replay wiederholt weder den vollständigen rationalen Matrixaudit
noch die vier frischen Integrationen.

Zusätzlich den vollständigen rationalen Matrixprüfer des Eingangs ausführen:

  python -B reproduce.py --input-zip /pfad/zum/Eingangspaket.zip --full-input-replay

Die vier vollständigen neuen Integrationen wurden bei Erstellung dieses
Berichts bereits ausgeführt. Eine erneute Ausführung benötigt den großen
Galerkin84-Vorgänger und die in dessen Umgebung verwendeten Bibliotheken;
hierfür gilt rebuild_from_parent.py samt README im Eingangspaket.

Python nicht mit -O starten; assert-Anweisungen gehören zu den Prüfungen.
Ein erfolgreicher Replay bestätigt weiterhin KEINEN unendlichen Rest.
