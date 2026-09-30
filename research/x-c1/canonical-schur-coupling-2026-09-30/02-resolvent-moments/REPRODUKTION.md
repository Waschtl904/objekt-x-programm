# Reproduktion

Benötigt werden Python 3.13, python-flint 0.9.0, Git und ein Checkout von
`Waschtl904/objekt-x-programm` auf
`8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b`.

```text
python check_interval_guards.py
python resolvent_moments.py --repo REPOSITORY --out primary-replay.json --bits 1024
python resolvent_moments.py --repo REPOSITORY --out crosscheck-replay.json --bits 1280
python verify_resolvent_moments.py --repo REPOSITORY --primary primary-replay.json --crosscheck crosscheck-replay.json --out verification-replay.json
```

Für die Kontrolle der gespeicherten Daten genügt die Python-Standardbibliothek:

```text
python verify_resolvent_moments.py --repo REPOSITORY --primary primary.json --crosscheck crosscheck.json --out verification-replay.json
```

Der vollständige Lauf dauert mehrere Minuten je Präzision. Laufzeitfelder sind
nicht deterministisch. Der Standardbibliotheks-Replay mit den unveränderten
gespeicherten Eingaben erzeugt dieselbe Ergebnis-JSON wie `verification.json`.

Der Checkout wird nur gelesen. Alle 25 Eingaben werden byteweise mit Git-Blobs
des festgelegten Commits verglichen. Die ursprünglichen analytischen Beweise,
Terminalspektren und Integrale bleiben gebundene Voraussetzungen.

## Dateien und Bedeutung

- `CANONICAL_RESOLVENT_MOMENTS.md`: vollständige Herleitung und Grenzen.
- `resolvent_moments.py`: gerichtete Modell-, Raum- und Momentrechnung.
- `primary.json`, `crosscheck.json`: die beiden vollständigen neuen Rechenläufe.
- `verify_resolvent_moments.py`: rationale Prüfung der echten kanonischen
  Raumkoordinaten und der kleinen Auswertung; kein vollständiger zweiter
  großer Intervallsolver.
- `verification.json`: maßgebliche rationale κ-Grenzen und positive inverse
  Diagonalintervalle. `display_outward` ist nach außen gerundet.
- `check_interval_guards.py`: fünf gezielte Prüfungen gegen nichtendliche
  Zwischenwerte und falsche Quadratschätzungen.
- `verification.log`: erfolgreicher abschließender Replay und Randfallprüfungen.
- `SHA256SUMS`: Bindung der übrigen Paketdateien.

`physical_energy_entries` und `physical_inverse_energy_entries` sind echte
Eintragsintervalle in der im Bericht definierten L²-Basis. Negative untere
Intervallendpunkte bedeuten keine negative tatsächliche Diagonale; die positiven
Loewner-Böden und die rational verfeinerten Diagonalintervalle gelten zusätzlich.
Die Rohmatrizen beziehen sich auf V₀ und müssen gemeinsam mit dessen Gram-Matrix
interpretiert werden. Hilfsräume werden nicht mit echten Spektralräumen gleichgesetzt.
