Objekt X — Schurabschluss: Gegenprüfung und zusätzliche Reserve
13. Oktober 2026

Mit BERICHT.txt beginnen; PRUEFHERLEITUNG.txt enthält die mathematische
Gegenprüfung und die neue exakte Umformung. INDEPENDENT_REVIEW.json enthält
sämtliche rationalen Zusatzgrenzen. OUR_FULL_CHAIN_REPLAY.json dokumentiert
den ausgeführten frischen Replay der gesamten gebundenen Vorgängerkette.
CONTROLS_REPLAY.json enthält die erneut ausgeführten Bausteinkontrollen.

Das kompakte Paket enthält das große Eingangsarchiv nicht noch einmal.
Erforderlicher Eingang:
 Objekt-X-Globaler-Schurabschluss-A8-A9-2026-10-13.zip
 SHA256 65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba

Schneller unabhängiger rationaler Replay (nur Python-Standardbibliothek):
 python -B reproduce_review.py --input-zip PFAD_ZUM_EINGANG.zip
                              --receipt EIGENE_PRUEFUNG.json

Zusätzlich die ganze gebundene Vorgängerkette frisch nachspielen:
 python -B reproduce_review.py --input-zip PFAD_ZUM_EINGANG.zip
                              --full-chain --receipt VOLLE_PRUEFUNG.json

Ohne --full-chain führt der schnelle Replay nicht nochmals alle großen
rationalen Matrixrechnungen der Vorgänger aus. Seine Quittung weist das
ausdrücklich aus. Auch --full-chain erzeugt die globalen Integrationen
nicht neu; dieser optionale Neuaufbau liegt weiterhin im Grampaket.

Die vier frischen Arb-Kontrollquittungen stimmen exakt mit den gebundenen
Originaldaten überein. Ihre Erzeuger sind unverändert im eingebetteten
Grampaket des Eingangs enthalten: test_primitives.py, check_geometry.py,
check_log_groups.py und test_radius_price.py, mit python-flint 0.9.0.

A8->A9 ist bedingt auf die angegebenen analytischen Voraussetzungen
bestätigt. Tailboden 1/20, weitere Horizonte, Objekt X insgesamt und RH
werden nicht behauptet. Die externe mathematische Begutachtung ist offen.
