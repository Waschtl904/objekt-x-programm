# Rechenpaket: vier Quellen und vollständige alte inverse Energie

4. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN

Einstieg: [Ergebnis](ERGEBNIS.md). Die mathematische Begründung mit Voraussetzungen steht in [NACHWEIS.md](NACHWEIS.md).

Dieses Paket enthält alle numerischen Eingaben für die **neue** Rechnung, deren Code und die gespeicherten Resultate. Zum erneuten Lauf sind Python und `python-flint==0.9.0` erforderlich. Die Abhängigkeit wird nicht mitgeliefert. Getestete Umgebung: Python 3.13.7 unter Windows, python-flint 0.9.0. Der Reproduktionslauf selbst benötigt keinen Netzwerkzugriff.

## Reproduktion

Abhängigkeit bei Bedarf in einer eigenen Python-Umgebung installieren:

```text
python -m pip install -r requirements.txt
```

Danach aus dem entpackten Paket starten; das Zielverzeichnis darf noch nicht existieren und muss außerhalb des Pakets liegen:

```text
python -B reproduce.py --out ../inverse-energy-replay
```

Der Lauf prüft zuerst das geschlossene SHA256-Manifest. Er berechnet alle neuen gemischten Paarungen bei 3072 Bit, die vollständigen alten Energieobergrenzen bei 2048 Bit und die exakten rationalen Schlusszertifikate erneut. Anschließend vergleicht er die Ergebnisse und prüft das unveränderte Manifest nochmals. Die Laufzeiten in `FINAL_GATE.json` werden beim Vergleich ausgelassen; alle übrigen Felder müssen übereinstimmen. Die gemischte Ergebnisdatei muss byteidentisch sein.

Der zusätzliche 4096-Bit-Lauf ist bereits als Referenz enthalten. Um ihn ebenfalls neu auszuführen:

```text
python -B reproduce.py --out ../inverse-energy-replay-two-precisions --second-precision
```

Standardmäßig wird die frisch erzeugte 3072-Bit-Rechnung mit der gebundenen 4096-Bit-Referenz verglichen. Der Laufbericht unterscheidet ausdrücklich, ob die zweite Präzision in diesem Lauf ebenfalls neu berechnet wurde. Für eine bereits vorhandene Bibliothek unterstützt der Wrapper `--deps PFAD`; dieser optionale Pfad wird nur für Python-Importe verwendet.

Die exakte Schlussprüfung allein benötigt keine externe Bibliothek:

```text
python -B code/check_inverse_energy_exact.py --gate expected/FINAL_GATE.json --mixed expected/SOURCE_MIXED_3072.json --second-mixed expected/SOURCE_MIXED_4096.json --out ../energy-exact-check.json
```

Diese kurze Prüfung kontrolliert die Schlussmatrizen und 36 Gamma-Polynomidentitäten. Sie ersetzt den vollständigen neuen Rechenlauf und die analytische Prüfung der Voraussetzungen nicht.

## Inhalt

| Pfad | Bedeutung |
| --- | --- |
| `inputs/` | Acht unveränderte Modelle, Quell- und Gramzertifikate aus den gebundenen vorherigen Rechnungen |
| `vendor/` | Zwei unveränderte Rechenmodule aus dem ursprünglichen Residualpaket |
| `code/compute_source_mixed.py` | Neue vollständige gemischte Paarungen, ohne hohe Trunkierung der Logarithmus-/Shiftwirkung |
| `code/compute_inverse_energy_gate.py` | Alte Schurmatrix, zertifizierte Inverse, K und inverse Energieobergrenzen |
| `code/check_inverse_energy_exact.py` | Separater Schlussprüfer mit ausschließlich rationaler Standardbibliotheksarithmetik |
| `expected/SOURCE_MIXED_3072.json`, `SOURCE_MIXED_4096.json` | Ausgeführte Paarungsrechnungen mit identischen gespeicherten numerischen Blöcken |
| `expected/FINAL_GATE.json` | Gerichtete Energieergebnisse; maßgeblich sind `mixed_trials` mit `young_parameter = 1/10000000` |
| `expected/INDEPENDENT_ENERGY_CHECK.json` | Exakte positive Untergrenzen und 36 algebraische Kontrollen |
| `provenance/` | Unveränderte ursprüngliche Herleitungen und Bindungen zur Einordnung |
| `SOURCE_BINDINGS.json` | Herkunft, Prüfsummen und fester Repository-Stand |
| `SHA256SUMS` | Geschlossenes Manifest aller Paketdateien außer sich selbst |

`FINAL_GATE.json` bewahrt außerdem die ausgeführten gröberen Abschätzungsversuche unter `trials` und `source_trials`. Deren fehlende positive Zertifizierung ist kein negativer Befund für die wirkliche Form. Die tatsächlich erfolgreichen abschließenden Rechnungen stehen unter `mixed_trials`.

Die Originaltexte unter `provenance/` wurden bytegleich übernommen. Ihre internen relativen Verweise beziehen sich auf ihr ursprüngliches Repository bzw. Archiv; die Ursprungsorte stehen in `SOURCE_BINDINGS.json`. Diese Originaltexte können frühere offene Arbeitsstände beschreiben. Für den neuen Befund sind `ERGEBNIS.md` und `NACHWEIS.md` maßgeblich.

## Grenzen der Wiederholung

Der Lauf rekonstruiert die neuen gemischten Integrale und sämtliche neuen Energiemajoranten. Er übernimmt die ursprünglichen A8/A9-Modelle, die vorherigen gemeinsamen Quellbudgets, die Gramaudits sowie die analytische Formraum- und Operatoranbindung. Er regeneriert nicht die ganze frühere Beweiskette aus den ursprünglichen Operatorintegralen.

Die vier Quellen besitzen danach einen positiven Anschluss an den vollständigen alten Raum. Der gesamte neue Quotient und die Konstruktion von Objekt X bleiben offen. GitHub wird von keinem dieser Programme verändert.
