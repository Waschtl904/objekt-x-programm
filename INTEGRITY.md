# INTEGRITY.md — Hashbaum der Kernddateien

Dieses Manifest wird durch den Workflow `.github/workflows/integrity.yml`
und das Skript `scripts/build_integrity.sh` deterministisch aus den
unten aufgezaehlten Quelldateien erzeugt und veroeffentlicht.

Der Inhalt aendert sich ausschliesslich, wenn sich mindestens eine
dieser Quelldateien inhaltlich aendert. Zeitstempel werden bewusst
nicht in das Manifest aufgenommen, damit unveraenderte Quellen kein
neues Manifest erzeugen.

| Datei | SHA-256 |
|---|---|
| `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex` | `bdeb74e0d25b8d36f6792555e5b0a1dce49dbba293973fa58a31b205f6979684` |
| `papers/P11_sections/P11_O3af_Gamma_Symbol_Bridge.tex` | `19445e51ac26afb75dc4f76725c613570955fcefbaf3520c58c0fa5b856bdfc2` |
| `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md` | `77818aee8e1df25cf067ceb55ea205f35c520942895508f1bac09e75faffc6ce` |
| `00-grundlegung/ebene-XVI-objekt-x.md` | `2dd5ae5565ec7a34a2a474bf01d8411b85a10777800349281428127f95c8ca9d` |
| `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md` | `713331f59eccb7516bfb9403bb835f052a68f043aa1eb06fd8030ccef6c1cc71` |
| `.canary` | `e6c1afe34a565abf999843248c4fadaf1e55ae1ecd3bb1e8b009b872dfc00ba5` |
| `ATTRIBUTION.md` | `0c91e33942bb170a1f5a1ad0d58d11d080854881e9c55d38605b6689a19a4bfa` |
| `SECURITY.md` | `9fe60c1979524e4a54a1d39e3c4421ad037dd8a7469d747bdcc24ba86f031ef7` |
| `CITATION.cff` | `2285d4127fbc37337ba4b1b11381d06fbc1c9b9c75caccc45a52f5a759139ee1` |
| `LICENSE` | `9ba9550ad48438d0836ddab3da480b3b69ffa0aac7b7878b5a0039e7ab429411` |
| `tests/fixtures/dummy_credentials.json` | `bd5ef63aacbb09bf5578c68d9b2d64f3ac3d0dd14b2c572808f6122c529486a2` |

Reproduktion:

```
bash scripts/build_integrity.sh > INTEGRITY.md
bash scripts/verify_integrity.sh INTEGRITY.md
```
