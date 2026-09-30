# Gemeinsame kanonische Maximiererzertifikate

Dieser Integrationsblock enthält drei unveränderte lokale Pakete samt Originalarchiven:

1. [Gemeinsame Projektor- und Spektralmomente](01-projected-overlap/PROOF.md):
   engere gemeinsame Bedingungen schließen die beiden `axis_one`-Alternativen
   und die ungerade `double`-Alternative der früheren Relaxation aus.
2. [Gemeinsamer generalisierter Diskriminant](02-joint-discriminant/PROOF.md):
   für A9→A11 ist der tatsächliche größte generalisierte Eigenwert in beiden
   Paritäten einfach, mit uniform positivem Gap. Die gerade physische
   Maximiererrichtung ist bereits lokalisiert.
3. [Schurdefekt und Nichtproportionalität](03-schur-defect/PROOF.md):
   `R0=M0+289 W0`, `W0>=0`; `W0=gamma M0` ist in beiden Paritäten ausgeschlossen.
   Die Gamma-Gaps folgen aus Block 2. Gerade liefert zusätzlich `F1<0` einen
   direkten Ausschluss. Dies ist keine zweite unabhängige Gap-Zertifizierung.

Status: **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**. Die Rechnung setzt die
bereits positiven Terminals bis A11 voraus. Offen bleiben die ungerade
Richtungslokalisierung, bandweise Momente des tatsächlichen Maximierers,
allgemeines Renewal, A13-Positivität, eine kofinale positive Familie,
globales Objekt X und RH. PR #187 und der jüngere lokale ungerade
Projektorblock gehören nicht zu diesem Integrationsschnitt.

## Reproduktion

Python 3.13, ausschließlich Standardbibliothek, vollständige Git-Historie:

```sh
python -B research/x-c1/canonical-joint-maximizers-2026-09-30/replay.py --output /tmp/joint-maximizer-replay
```

Das Ausgabeziel muss neu sein und außerhalb des Checkouts liegen. Der Replay
prüft alle Dateimanifeste, Originalarchive und beiden historischen Beweisanker,
führt die drei Zertifizierer und ihre unabhängigen Kontrollen aus und verlangt
bytegleiche `verification.json`-Dateien. Die Quellenprüfungen werden frisch
ausgeführt; nur ihr protokollierter aktueller Git-Head darf abweichen.
Große Integrale und Operatorlösungen bleiben hashgebundene Eingaben.

`SOURCE_BINDINGS.json` unterscheidet den Integrationsausgangspunkt
`c53856b453564621a06124b7ec4f85a27acfa727`, den ursprünglichen Quellencommit
`8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b` und den publizierten Paketanker
`b5dc05f7fcc133ab2aeb3132d4bce0fa74f55a5d`. `PROOF.md` ist jeweils eine
bytegleiche Kopie des Originalberichts. Die Ergänzungen für die Repository-
Integration sind separat durch das Familienmanifest gebunden.
