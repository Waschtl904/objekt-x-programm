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
| `papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex` | `6a6698a18a4643f190850ac9b2005d2ec3d26ded4cac06e91b076a6d49eccd7c` |
| `papers/P11_sections/P11_O3af_Gamma_Symbol_Bridge.tex` | `19445e51ac26afb75dc4f76725c613570955fcefbaf3520c58c0fa5b856bdfc2` |
| `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md` | `19d3cdc076dbc65204e68eff2962291c4f15663d2f8cce4d7b4fc29a1941ddbe` |
| `00-grundlegung/ebene-XVI-objekt-x.md` | `2dd5ae5565ec7a34a2a474bf01d8411b85a10777800349281428127f95c8ca9d` |
| `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md` | `8c7f0b69d7326e074e6b4db2ab967cc2d59bbe24026353b63c49deda9700aaba` |
| `.canary` | `dd23f298793df6a9142e793ef23010ac6a2683a8603c33638fb346f2b9c366e1` |
| `ATTRIBUTION.md` | `497f63305df3bae4e72f1c71f293561671cbe77f711828c6f66aef3f8acac640` |
| `SECURITY.md` | `1b3726621bc6a9de6e9db0887d5f3a855e38d26f0ac7f5a854cd6f6431db8833` |
| `CITATION.cff` | `67e04f14734e1128a2bc99ef322dbfb751c343389a6b360372ce063f049e67fe` |
| `LICENSE` | `9ba9550ad48438d0836ddab3da480b3b69ffa0aac7b7878b5a0039e7ab429411` |
| `tests/fixtures/dummy_credentials.json` | `bd5ef63aacbb09bf5578c68d9b2d64f3ac3d0dd14b2c572808f6122c529486a2` |

Reproduktion:

```
bash scripts/build_integrity.sh > INTEGRITY.md
bash scripts/verify_integrity.sh INTEGRITY.md
```
