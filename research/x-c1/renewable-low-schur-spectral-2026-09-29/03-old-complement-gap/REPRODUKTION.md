# Reproduktion: alter Komplement-Gap

## Voraussetzungen

- Vorhandener Repository-Checkout mit HEAD exakt `d16ba43ebb20f2c61f43379fc65d7a9b9dba76de`.
- Python 3.13 und python-flint 0.9.0 für die gerichtete Rechnung. Für den unabhängigen Ganzzahlprüfer genügt Python ohne Zusatzbibliotheken.
- Die ausgelieferten `old_vectors.json` und `fixed_vectors.json`.

Die Skripte lesen das Repository. Sie ändern keine Dateien darin und wechseln keine Referenzen. Der im Arb-Skript verwendete Git-Pfad ist der tatsächlich verwendete Windows-Pfad `C:\Program Files\Git\cmd\git.exe`. Auf anderen Systemen ist ausschließlich die Variable `git` entsprechend anzupassen. Der Ganzzahlprüfer sucht Git automatisch.

## Gleiche Quellenräume erneut auswerten

Die folgenden Aufrufe verwenden die bereits fixierten Koeffizienten. Sie sind für den direkten Ergebnisvergleich vorzuziehen:

```text
python old_complement_gap.py --repo PFAD_ZUM_REPOSITORY --old-vectors old_vectors.json --fixed-vectors fixed_vectors.json --out replay-primary --bits 1024
python old_complement_gap.py --repo PFAD_ZUM_REPOSITORY --old-vectors old_vectors.json --fixed-vectors fixed_vectors.json --out replay-crosscheck --bits 1280
python verify_old_complement_gap.py --primary replay-primary/gap_bounds.json --crosscheck replay-crosscheck/gap_bounds.json --vectors fixed_vectors.json --old-vectors old_vectors.json --repo PFAD_ZUM_REPOSITORY --out replay-verification.json
```

Die sechs Räume werden jeweils für r = 1,…,20 geprüft. Ihre tatsächliche Definition ist der rationale Koeffizientenvektor mit der exakten alten Mellinkorrektur. Koeffizienten oder Momente werden nicht zu einer angenommenen exakten Eigenrichtung erklärt.

## Auswahl der zusätzlichen Richtungen erneut ausführen

```text
python old_complement_gap.py --repo PFAD_ZUM_REPOSITORY --old-vectors old_vectors.json --out replay-selection --bits 1024 --max-rank 20 --iterations 32
```

Dieser Aufruf hält die ersten drei alten Richtungen fest und erzeugt die zusätzlichen Diagnoserichtungen durch inverse Iteration. Für die Zertifikatsaussage ist keine exakte Eigenvektorkonvergenz nötig. Entscheidend ist anschließend die Auswertung der fixierten rationalen Quellen. Für Vergleiche verschiedener Präzisionen immer dieselbe `fixed_vectors.json` benutzen; andernfalls würden sich die untersuchten Räume ändern.

## Nur die gelieferten Ergebnisse unabhängig nachrechnen

```text
python verify_old_complement_gap.py --primary gap_bounds.json --crosscheck gap_bounds_crosscheck.json --vectors fixed_vectors.json --old-vectors old_vectors.json --repo PFAD_ZUM_REPOSITORY --out replay-verification.json
```

Ohne `--repo` entfallen die zehn Git-/Dateibindungen. Alle 120 Ganzzahl-Replays, die positiven Projektionspivots, die beiden rationalen Formelprüfungen, Präzisionsvergleiche und Kontrollen der ersten drei unveränderten Richtungen werden weiterhin ausgeführt.

Der Ganzzahl-Replay startet bei den gespeicherten Projektions-Grammatrizen des 1280-Bit-Laufs. Deren Nenner ist 10¹⁴⁰; die unabhängigen Rechenintervalle benutzen 220 Dezimalstellen. Dieser Replay ist unabhängig von Arb für die anschließenden LDL-, Projektions-, Energie- und Normschritte. Er rekonstruiert die Projektions-Grammatrizen nicht erneut aus den ursprünglichen Integralen.

## Maßgebliche Ergebnisse

- `tau_lower_exact`: geerbter Boden c/(c+17) aus dem jeweiligen alten Terminal.
- `integer_replay_raw_upper_exact`: Obergrenze aus dem unabhängigen Zeugen-Replay.
- `combined_raw_upper_exact`: konservatives Maximum dieser Obergrenze und der beiden Arb-Läufe.
- `monotone_upper_exact`: Minimum dieser konservativen Zeugenwerte über alle größeren oder gleichen untersuchten Ränge.
- `upper_witness_rank`: Rang, dessen Zeuge die monotone Obergrenze liefert.
- `relative_L2_distance_to_K_squared_upper_exact`: Distanzschranke für den eigenen Zeugen zum Raum seines eigenen Ranges. Sie wird nicht durch die monotone Hülle auf kleinere Räume übertragen.

Die Dateien enthalten exakte rationale Endpunkte. Dezimale Anzeigen und Laufzeiten dienen der Lesbarkeit. Die ursprünglichen Terminalmodelle und deren globale Positivitätszertifikate werden hier nicht neu aufgebaut.
