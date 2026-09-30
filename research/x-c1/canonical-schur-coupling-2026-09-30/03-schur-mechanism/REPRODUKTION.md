# Reproduktion

Benötigt werden Python 3.13 und für den optionalen Quellenabgleich Git.
Der Rechner verwendet nur die Python-Standardbibliothek und benötigt keine
neuen Arb-Lösungen.

Im Paketverzeichnis:

```text
python verify_mechanism.py --out verification-replay.json
```

Dieser Lauf kontrolliert die vier mitgelieferten gebundenen Eingaben und die
neuen rationalen Schlüsse. Für den vollständigen byteweisen Vergleich aller
25 ursprünglichen Repository-Eingaben mit dem festen Commit:

```text
python verify_mechanism.py --out verification-replay.json --repo PFAD_ZUM_REPOSITORY
```

Der Checkout muss auf `8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b` stehen.
Die Git-Vertrauensausnahme gilt nur für den aufgerufenen Leseprozess; globale
Git-Einstellungen werden nicht verändert. Repository und Eingabepakete werden
nur gelesen.

Bei identischen Optionen ist die Ergebnis-JSON bytegleich. Mit und ohne
`--repo` unterscheidet sich ausschließlich der Bericht über den Quellenabgleich.

## Dateien

- `MECHANISM.md`: Ergebnisse, allgemeine Herleitungen und offene Fragen.
- `verify_mechanism.py`: vollständiger rationaler Rechner und Formelprüfungen.
- `verification.json`: Endpunkte, gerichtete Anzeigen und Prüfstatus.
- `verification.log`: tatsächlicher Lauf mit Vergleich der 25 Git-Blobs.
- `input_bindings.json`: SHA-256-Bindungen der vier Eingabedateien.
- `inputs/`: unveränderte frühere Belege; `prior_verification.json` ist der
  alte rationale Schlussbeleg, kein Ergebnis des neuen Rechners.
- `SHA256SUMS`: Prüfsummen aller übrigen Paketdateien.

Die analytischen Vorbedingungen und die großen gerichteten Matrixlösungen
werden nicht erneut bewiesen. Es wird insbesondere keine unabhängig neu
berechnete große Inverse behauptet.
