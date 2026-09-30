# Reproduktion

Voraussetzung: Python 3.10 oder neuer und Git. Eine Arbeitskopie des kanonischen
Repositories muss auf Commit `8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b` stehen.
Das Programm liest die Arbeitskopie und vergleicht ihre Eingaben byteweise mit
den Git-Blobs dieses Commits. Es verändert keine Repository-Dateien oder Referenzen.

```text
python verify_relative_kappa.py --repo PFAD_ZUM_REPOSITORY --out PFAD_ZUM_NEUEN_PRUEFBELEG.json
```

Erwartet: vier positive geerbte Untergrenzen für 1−κ,
26 commitgebundene Dateien und neun erfolgreiche rationale Formelprüfungen.
Die resultierende JSON-Datei ist bei gleichen Eingaben bytegleich zur beiliegenden
`verification.json`.

`RELATIVE_KAPPA.md` enthält den analytischen Beweis und die genaue Bedeutung
der Schranken. Der Prüfer baut keine Terminalintegrale auf und berechnet keine
neuen echten Spektralprojektoren oder inversen E-Momente. Die veröffentlichten
Terminal- und Spektralraumzertifikate bleiben Voraussetzungen.

`SHA256SUMS` bindet die übrigen Dateien dieses Pakets. Der ZIP-Inhalt ist ein
lokales Forschungsergebnis mit offenem externem Review.
