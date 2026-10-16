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

Gilt für `fixed_X` = eingefrorene Regel `A9_A11_N12_MIDPOINT_INVERSE_60_V1`;
`audit_S` ist ein getrennter Kandidat. Der Nachtrag (SHA `00a66e85…ded0a0`) ergänzt
die Zusicherung `h < 101/1000` in einer gebundenen Arbeitskopie bei bytegleichen
Ergebnisdateien.

Offen bleiben `||W9||` (obere Schranke), `Q_D`, die gewichtete Fehlerenergie, die
Modellenergie `R_hat* W9 R_hat` und damit das A9->A11-Zertifikat. Der
gewichtete Fehlerfaktor ist ein Koeffizient zu einer noch unbewiesenen oberen
`W9`-Norm; eine Untergrenze darf dort nicht eingesetzt werden. Der korrekte
Anschluss an die Spike-Kalibrierung verwendet die Quellentransformation `N`
(PROOF.md, Abschnitt 5, mit Korrekturvermerk).

## Reproduktion

```bash
python3 scripts/replay_whole_response_gram.py --output /tmp/whole-response-gram-check
python3 -m unittest discover -s tests -p test_whole_response_gram_replay.py
```

Etwa 3 min: Bindung beider Archive, versiegelter `verify.py` des Originals,
Nachtragsprüfer mit `h`-Guard, Quittungsvergleiche (576 exakte Gram-Vergleiche,
48 positive Pivots), paritätsabhängige Metrikkonstanten. `--full-input`
wiederholt zusätzlich den F12/D12-Eingangsreplay.
`independent_quadrature_check.py` (mpmath) ist eine numerische Plausibilisierung
per direkter Quadratur, kein zusätzlicher Beweis; Bericht in
`reports/INDEPENDENT_QUADRATURE.json`.

## Dateien

- `archives/` Original (SHA `b8677c0bb085f40052e52953ec39112894fbaa0f9f5d9997df8ae546238f41ee`) und Nachtrag (SHA `00a66e8584062b8057264b9b0dda48f89a013dc9b3756241a770bb74f2ded0a0`)
- `original/` bytegleiche sichtbare Kopien (PROOF.txt, BERICHT.txt, ANSCHLUSS_GPT1.txt, Prüfskripte, Audit-JSONs); `original/nachtrag/` NACHTRAG.txt, PATCH_BINDING.json, gepatchter Prüfer, Gegenprüftext
- `SOURCE_BINDINGS.json` / `.sha256` Bindungskatalog
- `reports/EXPECTED_RECEIPT.json`, `reports/EXPECTED_ADDENDUM_RECEIPT.json`, `reports/INDEPENDENT_QUADRATURE.json`
- `PROOF.md` Integrationstext mit nachgerechneter Kette, Gegencheck und Anmerkungen
