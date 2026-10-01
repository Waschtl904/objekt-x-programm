# Reproduktion des rationalen ungeraden Boxtests

Python 3.11 oder neuer, ausschließlich Standardbibliothek. Im Paketordner:

```powershell
python -B check_box_gate.py
python -B verify_box_gate.py --out replay.json
(Get-FileHash -Algorithm SHA256 replay.json).Hash -eq (Get-FileHash -Algorithm SHA256 verification.json).Hash
```

Ohne `-O` oder `-OO` ausführen. Die Prüfer verwenden Assertions.
Der Hashvergleich muss `True` ergeben. Erwartete Abschlussmeldung:

```text
STRUCTURAL_OPEN : 7 nodes, 4 leaves; physical witness separation >= 89.987266 degrees.
```

`parameters.json` legt die vier Variablen, die bevorzugte Teilungsreihenfolge,
den Zielkorridor, die Budgetgrenzen und die mathematische Stoppregel fest.
Der vollständige Eingabebaum ist an den SHA-256 des unveränderten
Vorgängerarchivs gebunden. Keine binären Gleitkommazahlen gehen in den
Certifier ein. Die gerichtete Arithmetik benutzt rationale Zahlen und
ein Gitter mit 160 Dezimalstellen.

Jeder Baumknoten enthält seine Box, Ausschlussgründe oder überlebende
Projektoreinschließung und etwaige separat zertifizierte Punktzeugen.
Überleben einer Box wird ausdrücklich nicht als Existenznachweis gewertet.
Die genaue gemeinsame Konstruktion der Punktzeugen wird aus dem
eingebetteten Paket vollständig erneut geprüft.

Optional kann die Quellenbindung frisch gegen das kanonische Repository
geprüft werden:

```powershell
python -B audit_sources.py --repo C:\Pfad\objekt-x-programm --out source_audit_replay.json
```

`verification.log` dokumentiert die abschließende Abnahme. `SHA256SUMS`
bindet alle übrigen Dateien. Status: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.
