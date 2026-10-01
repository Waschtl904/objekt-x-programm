# Reproduktion der Projektorgrenze unter Transportmomenten

Python 3.11 oder neuer, nur Standardbibliothek. Im entpackten Paketordner:

```powershell
python -B check_projector_transport.py
python -B verify_projector_transport.py --out replay.json
(Get-FileHash -Algorithm SHA256 replay.json).Hash -eq (Get-FileHash -Algorithm SHA256 verification.json).Hash
```

Ohne `-O` oder `-OO` ausführen, da der Prüfer Assertions verwendet.
Der Hashvergleich muss `True` ergeben. Erwartete Abschlussmeldung:

```text
Physical angle >= 89.987266 degrees. No actual odd localization is claimed.
```

Der neue Certifier bindet das vollständige unveränderte Transportarchiv,
prüft dessen Manifest und reproduziert seine Quittung bytegleich. Darin
sind die älteren drei Replays enthalten. Die neue Korrektur ist exakt
rational definiert. Ihre Auswertung benutzt gerichtete rationale
Intervalle mit 160 Dezimalstellen; binäre Gleitkommazahlen gehen nicht in
den Nachweis ein.

Beide korrigierten Y-Matrizen werden vollständig in ihren zertifizierten
Eintragshüllen eingeschlossen. Die exakte Kerninvarianz folgt aus der im
Bericht bewiesenen Invertierbarkeit der linken Korrektur. Die ursprüngliche
Kernbasis, ihre komprimierten Momente und ihre Projektoren werden deshalb
wiederverwendet und gegen beide Präzisionsquittungen geprüft.

Eine frische Quellenprüfung ist mit einer vollständigen lokalen Kopie des
kanonischen Repositories möglich:

```powershell
python -B audit_sources.py --repo C:\Pfad\objekt-x-programm --out source_audit_replay.json
```

Sie verändert das Repository nicht. Der darin beobachtete lokale Head kann
bei einer späteren Wiederholung abweichen. `SHA256SUMS` bindet alle übrigen
Paketdateien. Status: `AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN`.
