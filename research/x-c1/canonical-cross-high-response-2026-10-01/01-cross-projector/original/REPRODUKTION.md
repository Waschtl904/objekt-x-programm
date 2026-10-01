# Reproduktion des Kreuzprojektorversuchs

Benötigt werden Python 3.13, Git und `python-flint==0.9.0`. Das Repository
`Waschtl904/objekt-x-programm` muss auf dem gebundenen Commit
`6302a47cab2132f0d87dec29bbf21d7ce98e8f75` ausgecheckt sein. Die unveränderten großen Eingaben werden aus
diesem Checkout gelesen und gegen `SOURCE_BINDINGS.json` sowie Git geprüft.
Sie werden im ZIP nicht ein zweites Mal mitgeliefert.

```text
python -m pip install -r requirements.txt
python -B verify_cross_projector.py --repo PFAD_ZUM_REPOSITORY --out FRISCHE_QUITTUNG_AUSSERHALB_DES_PAKETS.json
```

Der kleine Replay prüft das Manifest, die Quellen, beide Präzisionsbelege,
abstrakte Kontrollfälle und bytegleiche Wiederholungen von Stufe A und der
Richtungsprüfung. Seine Quittung muss bytegleich mit `verification.json` sein.
Die ursprünglichen Integralrechnungen werden dabei nicht wiederholt.

Der vollständige Replay wiederholt zusätzlich beide gerichteten Filterläufe:

```text
python -B verify_cross_projector.py --repo PFAD_ZUM_REPOSITORY --out FRISCHE_VOLLQUITTUNG.json --full
```

Der Vollreplay verlangt bytegleiche Neuberechnungen von `filter_1024.json`
und `filter_1536.json`. Diese zusätzliche Wiederholung der großen
Operatorläufe gehört nicht zum kleinen Replay.
Die Vollquittung trägt entsprechend `full_operator_runs_replayed: true` und
eine längere Schrittliste. Die Rechenzeit ist deutlich größer als beim
kleinen Replay. Eine kleinere Rechenpräzision wird für die hochgradigen
polynomialen Überlappungen nicht akzeptiert; zusätzlich ist eine explizite
Breitenschranke für die Überlappungsintervalle eingebaut.

`parameters.json` enthält die vor den Operatorläufen fixierte Abnahme.
`ANALYTIC_ARGUMENT.txt` enthält die vollständigen Residuen- und
Projektorabschätzungen. Die Belege sind keine externe analytische Abnahme.
