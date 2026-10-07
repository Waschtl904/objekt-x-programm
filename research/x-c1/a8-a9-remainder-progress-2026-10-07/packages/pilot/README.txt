Objekt X — feste Restpilot-Abnahme, 6. Oktober 2026

BERICHT.txt: Ergebnis der Vorbereitung und offene Rechengrößen.
PROTOKOLL.txt / PROTOCOL.json: feste Raumdefinition und Abnahme.
GEOMETRY_768.json / GEOMETRY_1024.json: gerichtete Geometrieeinschließungen.
EXACT_GEOMETRY_CHECK.json: separate exakte Gram- und Vergleichsprüfung.

Kleine Prüfung mit Python-Standardbibliothek:
  python -B check_geometry.py

Neue Geometrieeinschließung mit python-flint 0.9.0:
  python -B geometry.py --bits 768 --out NEW_GEOMETRY_768.json
    --quotient-input inputs/QUOTIENT_NORM.json --protocol PROTOCOL.json

Die zweite Zeile gehört zum selben Aufruf. Falls python-flint separat liegt,
kann sein Elternverzeichnis über --deps angegeben werden. Ein bestehender
Ergebnispfad wird nicht überschrieben. Ein neuer Vergleichslauf kann
entsprechend 1024 Bit verwenden.

Die gerundeten Koeffizientenmittelpunkte sind keine exakt orthonormalen
Funktionen. Die genaue Basis ist durch die analytischen Definitionen und
die eindeutige Choleskyzerlegung festgelegt; JSON enthält Einschließungen.

Im Paket liegen keine B00-, Kreuz- oder Tail-Zertifikate. Der PASS-Status
des Geometrieprüfers darf nicht als vollständiger Operatorpilot gelesen
werden. Eingabekopien und Programme sind über SHA256SUMS gebunden.
