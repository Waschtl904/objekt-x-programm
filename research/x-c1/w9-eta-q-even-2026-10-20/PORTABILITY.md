# Technische Revision: portable Eingabepfade

21. Oktober 2026. Ausgangsstand: d4fec6573e040c44435fbb2e68b492873e1fea44
in PR #250. Der Linux-Sammelreplay brach vor der eta-q-Rechnung mit
`FileNotFoundError` ab: eine Eingabebindung enthielt Windows-Trennzeichen.

`INPUT_BINDINGS.json` verwendet jetzt durchgehend `/`. Der Leser akzeptiert
auch die historische Schreibweise mit `\` und gemischte Trennzeichen.
Er interpretiert beide plattformunabhängig als relative Pfade, verwirft
absolute Pfade, Laufwerksangaben und Elternpfade und prüft nach Auflösung
weiterhin die Begrenzung auf das Eingabe- beziehungsweise Paketverzeichnis.
Damit werden auch nach außen führende symbolische Verknüpfungen abgewiesen.
Die gelesenen Bytes werden weiterhin genau einmal eingelesen, hashgeprüft
und als unveränderlicher Snapshot verwendet. Paket- und Archivmember-Hashes
bleiben Pflichtprüfungen.

Geändert werden ausschließlich Pfadbehandlung, eine Pfadschreibweise,
zugehörige Paketbindungen und die technischen Regressionstests.
`run`, `RESULT.json`, Beweis, mathematische Eingaben und deren SHA-256-Werte
bleiben unverändert. Die historische `ACCEPTANCE.json` bezeichnet weiterhin
ihren ursprünglichen Verifikationscommit und ihr Archiv; sie ist keine
Abnahme dieser technischen Revision. Die neue Manifestbindung ergänzt
den historischen Stand, der im Git-Verlauf erhalten bleibt.

Pflichtprüfungen für diese Revision, vor dem Lauf festgelegt:

- `test_paths.py`: gleiche Snapshotbytes bei `/`, `\` und gemischten
  Pfaden; unveränderlicher Snapshot; falsche Datei-, Alias-, Paket- und
  Archivmember-Hashes; Elternpfade, absolute Pfade, Laufwerksangaben und
  Symlink-Ausbruch. Symlink-Test unter Linux verpflichtend; nur bei
  fehlendem lokalen Betriebssystemrecht wird er lokal übersprungen.
- Bytegleicher eta-q-Replay und unabhängiger rationaler Audit; anschließend
  der bislang dadurch blockierte #250-Replay einschließlich Audit unter
  Linux im bestehenden W9-Workflow. Die drei Ergebnisdateien bleiben
  bytegleich zu den veröffentlichten Originalen.
- Paket-/Eingabebindungen, Register, erzeugte Ansichten, Active Front und
  Diff prüfen. Anwendbare GitHub-Checks am endgültigen Head abschließen.

Dies ist keine neue Forschungsrechnung. Der Kontrollweg ruht; neue
Unterform, Punkt 4, N12 und externe Prüfung bleiben offen.
