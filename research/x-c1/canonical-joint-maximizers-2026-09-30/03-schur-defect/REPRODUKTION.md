# Reproduktion des Schurdefekt Proportionalitätsgates

Benötigt wird Python 3.11 oder neuer mit Standardbibliothek. Keine weiteren
Pakete und kein Netzwerkzugriff sind erforderlich. Das ZIP entpacken und
im Ordner `canonical-schur-defect-2026-09-30` ausführen:

```powershell
python -B check_schur_defect.py
python -B verify_schur_defect.py --out replay.json
```

Python ohne `-O` oder `-OO` starten, da die Prüfer Assertions verwenden.
Die zweite Anweisung erzeugt eine neue Quittung. Diese muss bytegleich mit
`verification.json` sein; unter PowerShell beispielsweise prüfen mit:

```powershell
(Get-FileHash -Algorithm SHA256 replay.json).Hash -eq (Get-FileHash -Algorithm SHA256 verification.json).Hash
```

Erwartetes Endergebnis:

```text
BOTH JOINT SCHUR-DEFECT PROPORTIONALITY GATES: NO COMPLETION; PASS
```

## Enthaltene Abhängigkeit

`inputs/Gemeinsamer-generalisierter-Diskriminant-2026-09-30.zip` ist das
unveränderte vorherige Prüfpaket, SHA256:

```text
c9760daa202b4eda079d1d2b9cdbd792a1579ba56e573d79f7c8140d75889844
```

Der neue Prüfer kontrolliert diesen festen Hash, alle 17 internen
Manifesteinträge und die sicheren relativen Archivpfade, bevor er den
Inhalt in ein temporäres Verzeichnis schreibt. Dort führt er den
vorherigen rationalen Certifier auf beiden Präzisionsquittungen aus.
Die Ausgabe muss bytegleich mit dessen archivierter `verification.json`
sein. Das temporäre Verzeichnis wird anschließend entfernt.

Für die Herleitung des gemeinsamen Gaps ist im enthaltenen Archiv
`JOINT_DISCRIMINANT.md` maßgeblich; die Quellenbindung und die geerbten
Voraussetzungen sind dort und in `REPRODUKTION.md` dokumentiert.
Der neue Lauf überprüft die vorhandene Quellenbindung über das unveränderte
Archiv. Er ruft keine GitHub-Quellen frisch ab und berechnet keine großen
Integral- oder Operatorzertifikate erneut.

## Dateien und Bedeutung

- `SCHUR_DEFECT.md`: Herleitung, Schranken und Aussagegrenze.
- `verify_schur_defect.py`: Abhängigkeitsreplay und neue rationale Schranken.
- `check_schur_defect.py`: exakte algebraische Tests und Negativkontrollen.
- `verification.json`: exakte rationale Grenzen für beide Eingabeläufe.
- `verification.log`: erfolgreiche abschließende Prüfung und Replay.
- `SHA256SUMS`: Hashmanifest aller anderen Dateien dieses Pakets.

Die Eingabequittungen bleiben an die mathematische Basis
`8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b` gebunden. Der dokumentierte
Integrationsstand ist `c53856b453564621a06124b7ec4f85a27acfa727`.
Dieses neue Paket ist lokal; eine Veröffentlichung ist kein Bestandteil
dieses Replays. Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
