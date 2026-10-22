# Gamma-Reparatur des festen geraden Zeugen

Bedingte Ergänzung zu [#252](../w9-residual-centered-control-even-2026-10-21/PROOF.md):
**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**, PENDING_STATUS_REVIEW.
[Herleitung](PROOF.md) · [offene analytische Pflichten](OPEN_OBLIGATIONS.md).
Die eingefrorene ursprüngliche Funktionsdarstellung enthält den dokumentierten
inneren Gamma-Fehler; sie ist allein kein Beleg für das reparierte Modell.

| Weg | Ganze Restenergie, bedingt | Unveränderter Deckel |
|---|---:|---:|
| Rohe Operatorabschätzung der Korrektur | <1.391e-10 | 1e-9 |
| Direkt integrierte Korrekturfunktion | <4.632e-11 | 1e-9 |

84 vollständige arithmetische Differenzintervalle sind in den jeweiligen
Fehlerhüllen enthalten. Die ganze Norm wird unabhängig davon integriert.

## Reproduktion

Python 3.12.14, python-flint 0.9.0, 3072 Bit; aus dem Repository-Stamm:

```text
python -B research/x-c1/w9-gamma-repair-even-2026-10-22/verify.py --check
python -B research/x-c1/w9-gamma-repair-even-2026-10-22/test_controls.py
```

Der Standardlauf prüft alle neuen und 567 geerbten Dateibindungen, exakte
Kernel-/Radiuskontrollen, die portable rationale Hüllen-/Budgetprüfung,
die unabhängige Normrechnung und den radiuskorrigierten inneren Randbeleg.
Temporäre Ausgaben liegen außerhalb des gebundenen Pakets. Für die zusätzliche
Neuberechnung aller 16 neuen äußeren Abschnitte:

```text
python -B research/x-c1/w9-gamma-repair-even-2026-10-22/verify.py --replay-panels
```

Diese Option braucht hier ungefähr drei Minuten. Die 65 älteren signierten
Abschnitte und 411 historischen Energieabschnitte werden nicht erneut integriert.
Die aktuelle Abnahme folgt dem vorab festgelegten Umfang in ACCEPTANCE.json.

`MANIFEST.json` bindet die neue Revision. `ORIGINAL_SHA256SUMS.txt` innerhalb
der beiden Nachweissammlungen bezeichnet jeweils deren historische Eingänge,
nicht die nach Guard-/Portabilitätskorrektur entstandene Revision. Die
abgeleitete portable Paarungsprüfung hat zusätzlich ihr eigenes aktuelles
Summenverzeichnis. Historische Arbeitspläne sind Belege, keine automatisch
auszuführenden Aufträge. Aktive Prüfeinstiege weisen Python -O/-OO zurück.
Die paketlokale `.gitattributes` erhält die gebundenen Dateibytes auch bei
Windows-Checkouts mit automatischer Zeilenenden-Konvertierung.

Die Pfade des inneren Replays werden aus dem aktuellen Checkout abgeleitet;
keine Windows-Laufwerksbuchstaben oder Symlinks sind erforderlich.
Vollständige Quellen-/Modellidentifikation und externe Gesamtabnahme bleiben
offen. Die zweite Richtung bleibt zurückgestellt.
