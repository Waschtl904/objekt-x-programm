# O8 und O9 in der ersten geschlossenen Kammer

**AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.** Für die konkrete C1a-Fortführung auf
1 ≤ A ≤ B ≤ C ≤ A₈ = log(8)/2, mit genau den ursprünglichen zwei Mellinbedingungen
und den Kanälen {2,3,4,5,7}.

- [O8-Beweis](o8-rechenstand/PROOF.md), insbesondere §7: vollständiger Formraum,
  neue hohe Reserve 2/3, vollständige Kopplungs-Grams und 191 positive gerichtete
  LDL-Pivots je Parität. Gemeinsamer physischer Boden 12/10³⁰ und Defektboden
  24/(23·10³⁰+24) > 10⁻³⁰.
- [Graph- und Schuranbindung](o8-schur-abgleich/GRAPH_SCHUR.md): Elimination des
  vollständigen hohen Raums und Kongruenz zum exakten Defekt-Schurrest.
- [Reproduktion](o8-reproduktion/REPRODUKTION.md): eigenständig implementierte
  Ganzzahl-Intervallrechnung sowie Wiederholung des ursprünglichen Arb-Prüfers.
- [O9-Beweis](o9-positive-transporte/PROOF.md): korrigierte Readouts und Räume,
  isometrische Transporte, Quellintertwining und Cocycle auf der ganzen Kammer.

## Herkunft und Status

Die vorhandenen mathematischen Dateien und Zahlenzertifikate stammen aus den
lokalen Paketen vom 27. September 2026. Ihre damaligen Angaben wie „lokal“,
„O8 bleibt OPEN“ oder „keine GitHub-Schreibzugriffe“ beschreiben den jeweiligen
Entwicklungs- oder Reproduktionsschritt. Ebenso bleibt der erfolglose erste
hinreichende Test mit hoher Reserve 1/2 dokumentiert; er ist kein Gegenbeweis
gegen die Formpositivität. Der erfolgreiche Nachweis verwendet 2/3.

Die [Quellbindungen](SOURCE_BINDINGS.json) dokumentieren Herkunft und unveränderte
numerische Quellen; das [Manifest](SHA256SUMS) bindet die publizierten Dateien.
Die operative Statusquelle bleibt die zentrale [Registry](../../../00-uebersicht/RESEARCH_STATE.yaml).
Das Paket wird zunächst zur Statusübernahme vorgemerkt. Nach erfolgreicher
Integration kann der Registry-Sync seine konkreten Beweis- und Reproduktionscommits
als MERGED registrieren. Der frühere globale Verifikationssnapshot bleibt erhalten.

## Verbindliche Abnahme

Vor dem Abnahmelauf festgelegt:

1. Eingabehashes, veröffentlichte Datei- und Codebindungen sowie Beweislinks prüfen.
2. Rationale Tail-Prüfungen (34 und 11 Gruppen), Arb-Zertifikat mit 2/3
   (20 Gruppen), rationale gemeinsame Reserve, unabhängige Ganzzahlprüfung
   (35 Gruppen) und Graph-Schur-Prüfung (42 Gruppen) ausführen.
3. Kleines Normierungsmodell direkt gegen die vollständigen Integrale prüfen
   (233 Vergleiche); O9-Algebra exakt rational prüfen (47 Gruppen).
4. Mathematische Ergebnisfelder mit den gespeicherten Zertifikaten vergleichen;
   ausschließlich gemessene Laufzeiten und daraus folgende Protokollhashes dürfen
   beim Replay abweichen. Beide gespeicherten Untermatrizen müssen bytegleich sein.
5. Registry-, Metadaten-, historische Front- und anwendbare GitHub-CI-Prüfungen.

Der vollständige 383/160-Modellgenerator wurde im ursprünglichen lokalen Paket
ausgeführt. Eine erneute Berechnung aller Integralmatrizen ist hier ein optionaler
Zusatzlauf; die unabhängige Zertifikatsarithmetik übernimmt die gebundenen
vollständigen Modellintervalle. Kein Lauf wird als externe analytische Abnahme
ausgegeben. Die neue CI wiederholt die verpflichtenden Paketprüfungen.

Vom Repositorywurzelverzeichnis:

```sh
python -m pip install -r research/x-c1/first-chamber-o8-o9-2026-09-27/o8-rechenstand/requirements.txt
python research/x-c1/first-chamber-o8-o9-2026-09-27/replay.py --output /tmp/o8-o9-replay
```

Der Replay liest die gebundenen Paketdateien und rechnet in einer frischen Kopie.
Er schreibt Ergebnisse in das angegebene neue Ausgabeverzeichnis.
Neu erzeugte Tail- und Rundungsprotokolle werden inhaltlich vollständig verglichen.
Für nachfolgende Hashbindungen verwendet er danach die identischen Originalinhalte
mit ihren gespeicherten Zeilenenden; die neuen Protokolle bleiben im Ausgabeordner.

O10 rechts von A₈, erneuerbare Profilreserve, unbeschränkte/kofinale Fortsetzung,
globale Weil-Positivität, Objekt X und RH werden dadurch nicht geschlossen.
