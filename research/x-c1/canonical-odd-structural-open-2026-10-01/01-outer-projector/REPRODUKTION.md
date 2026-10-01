# Reproduktion des ungeraden Projektorblocks

Python 3.11 oder neuer, nur Standardbibliothek, kein Netzwerk. Das ZIP
entpacken und im Ordner `canonical-odd-projector-2026-09-30` ausführen:

```powershell
python -B check_odd_projector.py
python -B verify_odd_projector.py --out replay.json
(Get-FileHash -Algorithm SHA256 replay.json).Hash -eq (Get-FileHash -Algorithm SHA256 verification.json).Hash
```

Python ohne `-O` oder `-OO` starten. Die Prüfungen verwenden Assertions.
Die letzte Anweisung muss `True` ausgeben. Erwartetes Endergebnis:

```text
OUTER PROJECTOR OBSTRUCTION CERTIFIED; ACTUAL ODD LOCALIZATION REMAINS OPEN.
```

## Abhängigkeiten und Bindung

Das Paket enthält das unveränderte Schurdefekt-ZIP mit SHA256

```text
4ed89ec928ba1573c6f295bf4038588568c1e5b9f4fdff69ee8e318eb4733c5b
```

Darin liegt wiederum das unveränderte Diskriminanten-ZIP. Der neue Prüfer
kontrolliert den festen Archivhash und sämtliche Manifestbindungen vor
dem Entpacken. Er führt den Schurdefektprüfer aus, der seinerseits den
Diskriminantenprüfer reproduziert. Beide Quittungen müssen bytegleich sein.
Erst danach werden die neuen Beispiele und Projektoren berechnet.

Die Eingaben bleiben an `8a82b7a972172c45cc4d3bc0297cc7fc0bbb2c7b` gebunden.
Dokumentierter Integrationsstand:
`c53856b453564621a06124b7ec4f85a27acfa727`.
Die alten großen Integral- und Operatorbeweise bleiben Voraussetzungen;
sie werden nicht erneut berechnet. Es werden keine Quellen frisch von
GitHub abgerufen und keine Repository-Dateien verändert.

## Neue Prüfung

Die Konstruktion in `completion_math.py` benutzt exakte rationale
Matrixoperationen. Positivität, Quellenordnungen und Projektoren werden
mit den gebundenen gerichteten Intervallhilfen des Diskriminantenpakets
überprüft. Deren Zwischengitter hat 160 Dezimalstellen. Der Parameter in
`parameters.json` ist fest; seine Herkunft aus einer explorativen Suche
ist für die Prüfung seiner Folgen unerheblich.

Beide Beispiele werden einmal aus der primären Eingabe exakt definiert
und danach unverändert gegen beide Präzisionsquittungen geprüft. Sie
haben je Kammer gemeinsame Spektralmaße. Die zusätzliche gemeinsame
Transportbedingung ist bewusst ein getrennter Test: Die gedrehte
Alternative scheitert daran. Der Prüfer gibt deshalb ausdrücklich
`actual_odd_projector_localized: false` und
`common_physical_transport_realization_claimed: false` aus.

`check_odd_projector.py` prüft ein nichtkommutierendes gemeinsames Maß,
den oberen Spektralprojektor samt physischer Normierung, die Unterscheidung
vom unteren Projektor, die Residualzuordnung und die Ablehnung eines
veränderten Abhängigkeitsarchivs vor dem Entpacken.

`verification.log` enthält die abschließenden Läufe und den bytegleichen
Replay. `SHA256SUMS` bindet alle übrigen Dateien. Der wissenschaftliche
Status bleibt **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
