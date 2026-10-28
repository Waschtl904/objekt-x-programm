# Fester Komplementvergleich ell12: ausreichende Route ausgeschlossen

Bereits der vollständig bezahlte Zwölfer-Kopplungspreis liefert
`M_* > 215033/47500 > D_hi` und `S_suff[ell12] < −0,154160692`.
Die tatsächliche Schurform wird dadurch nicht widerlegt. Der bestandene
v2-Zwölfervergleich bleibt getrennt. H1–H4 übernommen, externe Prüfung und
Punkt 4 offen, Checkliste 3/10.

- [Beweis und Reichweite](PROOF.md)
- [Unveränderter GPT1-Abschlussbericht](review/GPT1_ABSCHLUSS.txt)
- [Exakte rationale Entscheidung](review/COUPLING_ONLY_DECISION_RATIONAL.json)
- [Identität des vollständigen Originalarchivs](ARCHIVE.json)
- [Originalarchiv: Transportteil 1](archives/Objekt-X-ell12-Finite-Energie-Abnahme-GPT1-2026-10-28.zip.part01),
  [Teil 2](archives/Objekt-X-ell12-Finite-Energie-Abnahme-GPT1-2026-10-28.zip.part02),
  [Teil 3](archives/Objekt-X-ell12-Finite-Energie-Abnahme-GPT1-2026-10-28.zip.part03)
- [Ursprüngliche Reproduktionshinweise](review/REPRODUCTION_FINAL.txt)
- [Späterer Nachtrag: eine quellenbezogene Schärfung und ihr günstiger Test](SOURCE_SPECIFIC_ADDENDUM.md)

## Vorab festgelegter Pflichtumfang dieser Veröffentlichung

Dies ist eine mathematische Veröffentlichung eines bereits projektintern
geprüften Routenausschlusses, einschließlich technischer Belegbindung und
Statusnavigation. Der neue lokale Paketstatus ist `AUTHOR_DERIVED_NO_GO /
EXTERNAL_REVIEW_OPEN`; die Registry führt ihn als `PENDING_STATUS_REVIEW`.
Ein Merge ist keine externe Begutachtung und keine globale Statuspromotion.

Pflichtprüfungen am endgültigen Commit:

1. Archivgröße/SHA-256, CRC und Byte-/SHA-Abgleich aller 584 Mitglieder;
   bytegleiche lesbare Originalkopien und Veröffentlichungsmanifest.
2. Frischer Standardbibliothekslauf des rationalen Schlussprüfers in einer
   separaten temporären Archivkopie und dessen zwölf Positiv-/Negativkontrollen.
3. Diff- und Linkprüfung, deterministische Registry-Ansichten und die
   anwendbare Registry-CI; die neue CI dieses Pakets führt denselben begrenzten
   Beleg-/Entscheidungscheck aus.
4. Getrennter quellenbezogener Nachtrag: zwei unabhängige rationale Prüfer,
   gebundene Eingänge, zehn Schutzkontrollen und neun arithmetische Relationen.
   Die neue Herleitung wird gezielt geprüft; kein neuer Inverslauf.

Vom Repository-Stamm:

```sh
python research/x-c1/ell12-complement-route-stop-even-2026-10-28/verify_publication.py
python scripts/generate_research_state.py --check
```

Der erste Befehl benötigt nur Python 3 und ändert keine Originaldatei.
Die technische Übertragung ist auf drei Teile verteilt. Ihre Konkatenation
in der in ARCHIVE.json angegebenen Reihenfolge ergibt das unveränderte
19.944.025-Byte-ZIP; der Prüfer kontrolliert zuerst alle Teile und danach
die vollständige ursprüngliche Archividentität. Ein eigenständiges ZIP kann
im Paketverzeichnis mit `cat archives/*.part* > /tmp/ell12-original.zip`
zusammengesetzt werden. Die Teile sind keine neuen Autorenrevisionen.
Er bestätigt den dokumentierten letzten arithmetischen Schluss und seine
gebundenen Belege; die analytische Anwendungsprüfung steht im Abschlussbericht.
Die 424/71 Integrationen, der Inversanschluss und frühere Gesamtprüfungen
werden nicht wiederholt. Die entfallene ganze Restintegration ist kein
fehlender Bestandteil des Ausschlussbeweises.

Der Archivbericht nennt zum damaligen Abschlusszeitpunkt korrekt noch keine
GitHub-Veröffentlichung. Diese neue Veröffentlichung ist ein späterer,
separater Schritt; historische Originalberichte werden nicht umgeschrieben.
