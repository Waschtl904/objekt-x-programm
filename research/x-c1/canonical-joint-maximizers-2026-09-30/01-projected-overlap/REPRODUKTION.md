# Reproduktion der gemeinsamen Projektorschranken

Python 3.11 oder neuer genügt. Es werden keine zusätzlichen Pakete benötigt.
Im entpackten Paketverzeichnis ausführen:

```text
python -B check_projected_overlap.py
python -B verify_projected_overlap.py --out replay.json
```

`replay.json` muss strukturell dieselbe JSON-Datei wie `verification.json`
ergeben. Der neue Prüfer schreibt explizit UTF-8 mit LF; die Abnahme prüft
hier zusätzlich Bytegleichheit. Die unverändert übernommenen historischen
Inputs behalten ihre ursprünglichen Zeilenenden. Sie dürfen vor der
Hashprüfung nicht durch ein Werkzeug neu gespeichert werden.

Für die optionale erneute Prüfung gegen ein vorhandenes kanonisches Repository:

```text
python -B audit_sources.py --repo /pfad/zum/objekt-x-programm --out source-replay.json
```

Das Repository muss die in `input_bindings.json` und `audit_sources.py`
angegebenen historischen Git-Objekte enthalten. `audit_sources.py` vergleicht
25 ursprüngliche Quellen am mathematischen Beweisanker und fünf übernommene
Paketdateien am veröffentlichten Forschungshead. Es verändert das Repository
nicht. Der beobachtete aktuelle lokale Head darf im späteren Replay vom
damaligen Integrationsstand abweichen.

## Dateien

| Datei | Funktion |
| --- | --- |
| `PROJECTED_OVERLAP.md` | Aussage, vollständige neue Herleitung, Tabellen, Grenzen |
| `verify_projected_overlap.py` | Gerichteter rationaler Prüfer auf beiden Quittungen |
| `check_projected_overlap.py` | Exaktes nichtkommutierendes Operatorbeispiel und Fehlerprüfungen |
| `audit_sources.py` | Frische Bytebindung an historische Git-Objekte |
| `input_bindings.json` | SHA-256 der fünf unveränderten Inputs |
| `inputs/primary.json`, `inputs/crosscheck.json` | Vollständige Resolventenmomente aus 1024 und 1280 Bit |
| `inputs/outer_primary.json` | Gemeinsame physische Trialbasen, Energien und Überlappungen |
| `inputs/candidate_proposals.json` | Unveränderte rationale Parameter der Gegenmodelle |
| `inputs/extremal_verification.json` | Gebundene frühere Extremalgate-Quittung |
| `verification.json`, `verification.log` | Neue exakte Quittung und Laufprotokoll |
| `source_audit.json` | Ergebnis der frischen Quellenbindung |
| `SHA256SUMS` | Bytebindung aller übrigen Paketdateien |

Die neue Rechnung führt keine weiteren großen Integral- oder Operatorlösungen
aus. Der Prüfer benutzt die früher zertifizierten vollständigen
Resolventenschranken als Voraussetzungen. Der neue Status lautet
`CERTIFIED_PROJECTED_OVERLAP_JOINT_MOMENT_GATE`; der wissenschaftliche Status
bleibt `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.
