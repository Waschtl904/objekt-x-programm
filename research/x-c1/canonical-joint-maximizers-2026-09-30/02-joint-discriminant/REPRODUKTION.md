# Reproduktion des gemeinsamen Diskriminanten

Benötigt wird Python 3.11 oder neuer. Zusätzliche Bibliotheken sind für
die endgültige rationale Rechnung nicht erforderlich.

Im entpackten Paketverzeichnis ausführen:

```text
python -B check_joint_discriminant.py
python -B verify_joint_discriminant.py --out replay.json
```

`replay.json` muss strukturell mit `verification.json` übereinstimmen.
Der neue Prüfer schreibt explizit UTF-8 und LF. Daher wird bei der
Abnahme zusätzlich Bytegleichheit geprüft. Historische Inputs behalten
ihre ursprünglichen Zeilenenden und dürfen vor dem Hashvergleich nicht
neu gespeichert werden.

Die optionale erneute Quellenprüfung benötigt ein vorhandenes Repository
mit den historischen Git-Objekten und das unveränderte vorherige Archiv:

```text
python -B audit_sources.py --repo /pfad/zum/objekt-x-programm --projected-archive /pfad/Gemeinsame-Projektorueberlappungen-2026-09-30.zip --out source-replay.json
```

Der beobachtete lokale Head in einem späteren Quellen-Replay darf vom
historischen Integrationsstand abweichen. Beweisanker und Inputbytes
müssen weiterhin stimmen.

## Inhalt

| Datei | Zweck |
| --- | --- |
| `JOINT_DISCRIMINANT.md` | Ergebnis, gemeinsame Familie, vollständige neue Herleitung und Grenzen |
| `verify_joint_discriminant.py` | Rationaler Certifier für beide Paritäten und Quittungen |
| `interval_tools.py` | Gerichtete rationale Grundoperationen |
| `check_joint_discriminant.py` | Exakte Identitäten und Negativkontrollen |
| `rank_one_parameters.json` | Feste rationale Hilfsparameter, keine Operatorannahmen |
| `audit_sources.py` | Frische Byteprüfung der geerbten Voraussetzungen |
| `input_bindings.json` | SHA-256 der sechs unveränderten Inputs |
| `inputs/primary.json`, `inputs/crosscheck.json` | Vollständige Resolventenmomente aus 1024 und 1280 Bit |
| `inputs/outer_primary.json` | Physische Trialenergien und Überlappungen |
| `inputs/resolvent_verification.json` | Frühere rationale Prüfung der Resolventenmomente |
| `inputs/projected_verification.json` | Neue gemeinsame Projektor- und Momentenschranken |
| `inputs/projected_source_audit.json` | Quellenquittung des vorherigen lokalen Blocks |
| `verification.json`, `verification.log` | Neues Zertifikat und abschließendes Prüfprotokoll |
| `source_audit.json` | Ergebnis der frischen Quellenprüfung |
| `SHA256SUMS` | Bytebindung aller übrigen Paketdateien |

Erwarteter Status: `JOINT_GENERALIZED_DISCRIMINANT_STRICTLY_POSITIVE`.
Wissenschaftlicher Status: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.
Die tatsächlichen maximalen verallgemeinerten Eigenwerte sind beide einfach;
ein physischer Richtungskegel wird bislang nur für die gerade Parität
ausgewiesen. Es werden keine neuen großen Operatorlösungen ausgeführt.
