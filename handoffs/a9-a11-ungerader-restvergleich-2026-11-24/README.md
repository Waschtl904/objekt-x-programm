# A9 → A11 am festen ungeraden Zeugen

**Die endliche Vorprüfung ist bestanden.** Für die Positivität des vollständigen Vergleichs an diesem Zeugen genügt die Schranke ⟨rₒ, R_L rₒ⟩ ≤ 8,1·10⁻⁹ für die gemeinsame Restquelle rₒ = νₒ − Hₒ Jwₒ auf dem ganzen alten Raum. Diese Ganzraumschranke, der gekoppelte Quotientenvergleich und die Inversausgabe U₁₁ sind offen. Die Herleitung verwendet die im Projekt ausgewiesenen Form-, Domänen- und Eingangszertifikate. Externe Prüfung offen.

| Für die Gegenprüfung | Datei |
| --- | --- |
| Beide Ordnungen für den neuen ungeraden Zwölferblock, Quellenidentität, Fehler und hinreichende Schwelle | [Beweisnotiz vom 24. November](BEWEIS.md) |
| Rationaler Block Kₒ, alle 84 Koeffizienten von wₒ, zwölf zusammengefasste Kraftkoeffizienten und exakte Intervallenden | [Ergebnisdaten](ERGEBNIS.json) |
| Eingabestand, Pfade, Git-Blob- und SHA-256-Werte | [Eingabebindungen](EINGABEBINDUNGEN.json) |
| Rechnung aus den gebundenen Projektdaten | [Numerischer Prüfer](odd_coupled_24.py) |
| Schlussungleichung aus den gespeicherten rationalen Endpunkten | [Kurzprüfer](endpunkte.py) |
| Früherer Ausschluss der skalaren Young-Familie am selben äußeren Zeugen | [Vorprüfung vom 23. November](vorpruefung/BEWEIS.md) · [Ergebnis](vorpruefung/ERGEBNIS.json) · [Prüfer](vorpruefung/odd_dual_check.py) |

**Erste offene Prüfstelle.** Die 84 Paarungen geben eine obere Schranke für das endliche Restfeature. Der Nachweis auf dem orthogonalen Rest erfordert eine gerichtete Einschließung der gesamten ungeraden Quelle einschließlich Spiegel-, Momentlift-, Quellen- und Randfehlern in der alten Dualmetrik. Die im Ergebnisfeld `sufficient_d` gespeicherte Zahl bezeichnet das Ziel für diese Rechnung.

## Reproduktion

Im Verzeichnis dieser Datei prüft `python endpunkte.py` mit der Python-Standardbibliothek die Schlussrechnung. Für diese GitHub-Fassung liest der Kurzprüfer das frühere Ergebnis direkt aus `vorpruefung/ERGEBNIS.json`. Die beiden Beweisnotizen, numerischen Prüfer und Ergebnisdateien entsprechen bytegenau dem Prüfpaket.

Die numerischen Prüfer benötigen Python mit `python-flint==0.9.0` und die historischen Quelldateien des unten genannten Eingabestands mit ihren ursprünglichen Bytes. Der erste Befehl berechnet den restzentrierten Vergleich, der zweite den älteren Familienausschluss.

```text
python odd_coupled_24.py PFAD_ZUM_EINGABESTAND replay_24.json
python vorpruefung/odd_dual_check.py PFAD_ZUM_EINGABESTAND replay_23.json
```

Der mathematische Eingabestand ist `18dd92f89f889c1f506673fefee33e4544b22038`. Das historische Eingabeverzeichnis dokumentiert zusätzlich die ursprünglichen Archivmitglieder und deren Inhaltsprüfsummen. [Historische Eingabebindungen](https://github.com/Waschtl904/objekt-x-programm/blob/18dd92f89f889c1f506673fefee33e4544b22038/research/x-c1/w9-partial-energy-2026-10-18/INPUT_BINDINGS.json)
