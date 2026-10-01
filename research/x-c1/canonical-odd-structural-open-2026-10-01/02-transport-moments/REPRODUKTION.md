# Reproduktion des gemeinsamen Transportmomenttests

Python 3.11 oder neuer, nur Standardbibliothek. Im entpackten Paketordner:

```powershell
python -B check_transport_gate.py
python -B verify_transport_gate.py --out replay.json
(Get-FileHash -Algorithm SHA256 replay.json).Hash -eq (Get-FileHash -Algorithm SHA256 verification.json).Hash
```

Ohne `-O` oder `-OO` ausführen, da die Prüfungen Assertions verwenden.
Die letzte Zeile muss `True` ergeben. Erwartete Abschlussmeldung:

```text
TRANSPORT MOMENT EXCLUSIONS CERTIFIED; ACTUAL ODD LOCALIZATION REMAINS OPEN.
```

Der Prüfer kontrolliert zuerst den festen SHA-256 und das vollständige
Manifest des eingebetteten unveränderten Projektorarchivs. Dessen Certifier
reproduziert die älteren gebundenen Pakete; auch seine eigene Quittung muss
bytegleich sein. Beide neuen Beispiele werden einmal aus den primären
Eingaben definiert und unverändert gegen beide Präzisionsquittungen geprüft.
Matrizen und Cayley-Drehung werden exakt rational berechnet; gerichtete
Intervalle benutzen das geerbte Gitter mit 160 Dezimalstellen.

`check_transport_gate.py` prüft einen unabhängigen nichtkommutierenden
gemeinsamen Operator, die Projektionsidentitäten, einen Fall mit getrennt
positiven Grammatrizen und falschem Spektralsupport, einen negativen
gemischten Zeugen bei positiven Diagonalen sowie Archivmanipulation.

Optional ist eine frische Quellenprüfung mit einer vollständigen lokalen
Kopie des kanonischen Repositories möglich:

```powershell
python -B audit_sources.py --repo C:\Pfad\objekt-x-programm --out source_audit_replay.json
```

Sie vergleicht zwei zusätzlich eingebettete Beweistexte am kanonischen
Main-Commit und die geerbten Quellenbindungen. Repository-Dateien werden
nicht verändert. Der aktuelle lokale Head wird als Beobachtung protokolliert
und kann bei einer späteren Wiederholung abweichen.

`verification.log` dokumentiert die abschließende Abnahme und den
bytegleichen Replay. `SHA256SUMS` bindet alle übrigen Dateien.
Status: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.
