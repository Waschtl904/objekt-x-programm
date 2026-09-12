#!/usr/bin/env bash
# Prueft, ob ein uebergebenes INTEGRITY.md exakt zu den aktuell im
# Arbeitsbaum vorhandenen Quelldateien passt. Exit 0 bei Uebereinstimmung.
set -euo pipefail

MANIFEST="${1:-INTEGRITY.md}"
if [ ! -f "$MANIFEST" ]; then
  echo "verify_integrity: manifest not found: $MANIFEST" >&2
  exit 2
fi

# Erwartetes Manifest aus dem aktuellen Snapshot neu erzeugen und
# byte-genau vergleichen. Zeitstempellos, also stabil vergleichbar.
EXPECTED=$(mktemp)
trap 'rm -f "$EXPECTED"' EXIT
bash scripts/build_integrity.sh > "$EXPECTED"

if diff -u "$EXPECTED" "$MANIFEST" >/dev/null; then
  echo "verify_integrity: OK ($MANIFEST matches current source snapshot)"
  exit 0
fi

echo "verify_integrity: MISMATCH ($MANIFEST does not match current sources)" >&2
diff -u "$EXPECTED" "$MANIFEST" >&2 || true
exit 1
