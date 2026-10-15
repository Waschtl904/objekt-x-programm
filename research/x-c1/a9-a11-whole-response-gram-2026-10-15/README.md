# Vollständiger Antwortgram und verschärfter Modellfehlertransport (2026-10-15)

**Status:** AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN / RESEARCH_BRANCH_UNMERGED.

Versiegeltes Autorenpaket zum A9->A11-Schritt: rationale 12x12-Obermatrizen
`G_T >= T T*` für die vollständig zusammengesetzten Antwortfunktionen auf der
ganzen physischen Schale (logarithmischer Rand und alle Modellfehler
eingeschlossen) und daraus direkte K-Modellfehlerpreise.

| | gerade | ungerade |
| --- | --- | --- |
| Antwortnorm `||T||` | `< 6 838 544` | `< 784 134` |
| direkter K-Modellfehler | `< 1.661e-24` | `< 2.183e-26` |
| gewichteter Fehlerfaktor je Einheit `w >= ||W9||` | `< 5.90e-62` | `< 7.75e-64` |

Offen bleiben `||W9||`, `Q_D`, die Modellenergie `R_hat* W9 R_hat` und damit
das A9->A11-Zertifikat. Nach der Spike-Kalibrierung sind die Modellfehler
gegenüber dem Skalar `<Jv, R_hat z>` irrelevant (PROOF.md, Abschnitt 5).

## Reproduktion

```bash
python3 scripts/replay_whole_response_gram.py --output /tmp/whole-response-gram-check
python3 -m unittest discover -s tests -p test_whole_response_gram_replay.py
```

Etwa 90 s: Archiv-, Mitglieds- und Kopienbindung, versiegelter `verify.py`,
Quittungsvergleich (576 exakte Gram-Vergleiche, 48 positive Pivots).
`--full-input` wiederholt zusätzlich den F12/D12-Eingangsreplay.
`independent_quadrature_check.py` (mpmath) ist der unabhängige Gegencheck per
direkter Quadratur; sein Bericht liegt in `reports/INDEPENDENT_QUADRATURE.json`.

## Dateien

- `archives/…zip` gebundenes Autorenpaket (SHA `b8677c0b…41ee`), enthält das F12/D12-Funktionsarchiv und die eingefrorene Antwortregel
- `original/` bytegleiche sichtbare Kopien (PROOF.txt, BERICHT.txt, ANSCHLUSS_GPT1.txt, Prüfskripte, Audit-JSONs)
- `SOURCE_BINDINGS.json` / `.sha256` Bindungskatalog
- `reports/EXPECTED_RECEIPT.json`, `reports/INDEPENDENT_QUADRATURE.json`
- `PROOF.md` Integrationstext mit nachgerechneter Kette, Gegencheck und Anmerkungen
