# Reproduktion

Benötigt wird ein Checkout von `Waschtl904/objekt-x-programm` auf
`6302a47cab2132f0d87dec29bbf21d7ce98e8f75`.

## Ohne zusätzliche Python-Pakete

```text
python -B verify_high_response.py --repo PFAD_ZUM_REPOSITORY --out FRISCHE_QUITTUNG_AUSSERHALB_DES_PAKETS.json
```

Die Quittung muss `verification.json` bytegleich reproduzieren. Dieser
Prüfer kontrolliert Bindungen und gespeicherte Rechenbudgets; er berechnet
die großen Operatorintegrale nicht neu. Der gemeinsame Richtungstest
wird erneut ausgeführt. Damit ist auch ohne installierbares python-flint
ein klar abgegrenzter Kontrolllauf möglich.

## Kleine unabhängige Arb-Kontrollen

Mit Python 3.13 und `python-flint==0.9.0`:

```text
python -m pip install -r requirements.txt
python -B verify_high_response.py --repo PFAD_ZUM_REPOSITORY --out FRISCHE_ARB_QUITTUNG.json --arb
```

Diese Quittung muss `verification_arb.json` bytegleich reproduzieren.
Die kleinen Tests vergleichen die Gamma-Rekonstruktion mit der alten
Basis-Engine, Shiftintegrale mit polynomialen Antiderivaten und den
vollständigen hochdimensionalen Restmechanismus an einem kleinen Modell
mit dessen unabhängig zusammengesetzter Parseval-Grammatrix.

## Vollständige Wiederholung ab den festen Kandidaten

```text
python -B verify_high_response.py --repo PFAD_ZUM_REPOSITORY --out FRISCHE_VOLLQUITTUNG.json --full
```

Dieser Modus rekonstruiert die Capture-Daten und wiederholt die großen
vollständigen Residualintegrale, die hohe Kanalanalyse und die beiden
Zielüberlappungen. Er verwendet die gespeicherten dyadischen Kandidaten;
die endliche Kandidatensuche muss für deren Residualzertifikat nicht
wiederholt werden. Die erneut berechneten Belege werden bytegleich
verglichen. Dieser zusätzliche volle Replay wurde beim Paketabschluss
nicht ausgeführt.

Eine neue Kandidatensuche kann separat mit `corrected_resolvent.py` ohne
`--resume-candidates` ausgeführt werden. Numerisch anders gewählte
Kandidaten müssen wieder durch ihre eigenen vollständigen Residuen
zertifiziert werden. Ein positiver oder invertierbarer endlicher Block
ersetzt diesen Schritt nicht.

Die vollständigen großen Terminal-Eingaben sind aus Platzgründen im
gebundenen Git-Checkout belassen. Ihre Hashes stehen in
`SOURCE_BINDINGS.json`; der Prüfer vergleicht zusätzlich die Git-Blobs.
Der vorherige Cross-Projector-Block ist in `inputs/previous_cross_projector.zip`
unverändert enthalten. Keine fehlgeschlagenen Vorläufe sind Teil der
akzeptierten Rechenbelege.
