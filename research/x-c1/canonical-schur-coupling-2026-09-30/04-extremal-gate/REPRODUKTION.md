# Reproduktion des symmetrischen Extremalgates

Benötigt wird Python 3.13. Der endgültige Prüfer verwendet ausschließlich die
Standardbibliothek. Im Paketverzeichnis:

```text
python -B verify_extremal_gate.py --out verification-replay.json
```

Die Ausgabe muss bytegleich mit `verification.json` sein. Ein Lauf dauert
je nach Rechner einige zehn Sekunden. Alle kleinen Matrixprüfungen verwenden
rationale Endpunkte; große Solver werden nicht aufgerufen.

## Inhalt

- `EXTREMAL_GATE.md`: Korollar, symmetrische Auswertung, genaue Definition der
  Zertifikatsrelaxation, Matrixlemma und Aussagegrenzen.
- `verify_extremal_gate.py`, `rational_tools.py`: vollständiger Prüfer.
- `candidate_proposals.json`: festgehaltene rationale Parameter. Ihre
  Entstehung durch eine numerische Suche ist für die endgültige Prüfung
  unerheblich; der Prüfer muss jeden Vorschlag selbst akzeptieren oder verwerfen.
- `input_bindings.json`, `inputs/`: fünf gebundene unveränderte Eingaben.
- `verification.json`, `verification.log`: Ergebnis und tatsächlicher Endlauf.
- `SHA256SUMS`: Bindung aller übrigen Paketdateien.

Die Alternativen werden deterministisch aus den Eingaben und Parametern
erzeugt. Der exakte rationale doppelte Eigenwert wird zusätzlich in der
Ergebnisdatei gespeichert. Die übrigen Matrixeinträge lassen sich durch den
Prüfer vollständig rekonstruieren.

Die Prüfungen belegen Zulässigkeit in der ausdrücklich angegebenen endlichen
Relaxation. Sie belegen keine Realisierbarkeit durch die ursprünglichen
Operatoren und Spektralprojektoren. `true_maximizer_isolated` bleibt `false`.
