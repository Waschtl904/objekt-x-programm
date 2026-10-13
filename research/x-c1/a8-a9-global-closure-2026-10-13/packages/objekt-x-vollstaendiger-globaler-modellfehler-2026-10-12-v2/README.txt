Objekt X — vollständiger globaler Modellfehler, 12. Oktober 2026

Neu geschlossen, unter den gebundenen Operatorvoraussetzungen:
der vollständige tatsächliche L2-Modellfehler der globalen Residualfunktion.
Gerade <1.2e-11; ungerade <2.3e-13, jeweils in der D-dualen hohen Norm.
Das liegt deutlich unter den erlaubten bisherigen Modellfehlerbudgets.

Zuerst ANSCHLUSS_GPT1.txt, dann PROOF.txt lesen.

Standard-Replay (nur Python-Standardbibliothek):
  python -B reproduce.py --receipt QUITTUNG.json

Frischer vollständiger Neuaufbau (zusätzlich python-flint):
  python -B reproduce.py --rebuild --receipt QUITTUNG_NEUAUFBAU.json

Optional: --python PFAD und --deps VERZEICHNIS für eine vorhandene
Mathematikumgebung. Der Neuaufbau integriert sämtliche Teilintervalle,
einschließlich der unendlichen logarithmischen Randenergie, mit 4096 Bit
und einer anderen Aufteilung als im ersten Lauf. Laufzeit mehrere Minuten.

Die Dateien unter snapshot sind unveränderte Feldauszüge mit SHA256-
Herkunftsbindung. Das frühere Funktionsmodell mit seiner Herleitung und
seinem eigenen Prüfer liegt unverändert als ZIP unter inputs bei.

Noch offen: der globale Modellgram samt niedriger Projektion.
A8->A9 und der Tailboden 1/20 sind nicht bewiesen.
