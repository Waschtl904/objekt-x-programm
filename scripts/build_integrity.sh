#!/usr/bin/env bash
# Deterministischer Generator fuer INTEGRITY.md.
# Kein Zeitstempel im Manifest -> das Manifest aendert sich NUR, wenn
# sich mindestens eine der ueberwachten Dateien inhaltlich aendert.
# Zeitstempel wird optional als Kommentar hinter der Tabelle gefuehrt.
set -euo pipefail

FILES=(
  "papers/P11_Global_Coupling_and_Object_X_Candidate_Geometry.tex"
  "papers/P11_sections/P11_O3af_Gamma_Symbol_Bridge.tex"
  "00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md"
  "00-grundlegung/ebene-XVI-objekt-x.md"
  "00-uebersicht/ACTIVE_THEOREM_REGISTRY.md"
  ".canary"
  "ATTRIBUTION.md"
  "SECURITY.md"
  "CITATION.cff"
  "LICENSE"
  "tests/fixtures/dummy_credentials.json"
)

cat <<'HEAD'
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
HEAD

for f in "${FILES[@]}"; do
  if [ -f "$f" ]; then
    H=$(sha256sum -- "$f" | awk '{print $1}')
    printf "| \`%s\` | \`%s\` |\n" "$f" "$H"
  else
    printf "| \`%s\` | MISSING |\n" "$f"
  fi
done

cat <<'TAIL'

Reproduktion:

```
bash scripts/build_integrity.sh > INTEGRITY.md
bash scripts/verify_integrity.sh INTEGRITY.md
```
TAIL
