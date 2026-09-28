# A9: zweite Kammer lokal positiv zertifiziert

27. September 2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

**SECOND-CHAMBER TERMINAL POSITIVITY ist lokal hergeleitet und das
Rechenzertifikat mit zwei Arithmetiken geprüft.**

Am Endpunkt `A9=log(3)` wurden die vollständigen neuen Modellmatrizen
berechnet: sechs aktive Kanäle `2,3,4,5,7,8`, sechs Integrationszellen,
296 niedrige Koordinaten je Parität und Gamma-Polynomgrad 224.
q=9 bleibt am Endpunkt inaktiv.

## Ergebnis

Für die konkrete C1a-Familie und die ursprünglichen zwei Mellinbedingungen gilt
auf den vollständigen Quellenformräumen für **alle 1≤A≤A9** der gemeinsame Boden

\[
\boxed{q_A[u]\ge 10^{-35}\|u\|_2^2,\qquad
G_A\succeq\frac{1}{12\cdot10^{35}+1}I.}
\]

Die Reserve wird durch die neue Terminalrechnung gewonnen und durch
physische Nullfortsetzung samt O10-Formnaturality auf das Intervall übertragen.
Mit `Δ_A=G_A^(1/2)` sind daher

\[
U^X_{A,B}=\Delta_BM^T_{A,B}\Delta_A^{-1}
\]

isometrische Einbettungen und erfüllen das Cocycle für `1≤A≤B≤C≤A9`,
einschließlich der q=8-Wand. Die ausführliche Verbindung steht in
[SCHUR_AND_TRANSPORT.md](SCHUR_AND_TRANSPORT.md).

## Tatsächlich ausgeführte Prüfungen

| Prüfung | Ergebnis |
| --- | --- |
| Neue Tail-, Domänen- und Kodimensionsvorbereitung | 72 exakte Kontrollen; sieben Repository-Eingaben commitgebunden geprüft |
| Neue Geometrie und alternative Integralzusammensetzung, Grad 15 | 239 Vergleiche bestanden |
| Vollständiger Modellaufbau | Rohe Grade 0–593, Gamma Grad 224, 3072 Bit; alle sechs Kanäle und Zellen |
| Gerichtete Arb-Prüfung der bezahlten Schur-Untermatrix | 21 Prüfgruppen; **296 positive Pivots je Parität** |
| Unabhängige Ganzzahlintervalle, ohne Arb oder Generatorimport | 37 Prüfgruppen; erneut **296 positive Pivots je Parität** |

Die unabhängige Prüfung ergibt folgende gerundete Anzeigen ihrer exakten
physischen Untergrenzen:

| Parität | Physische Untergrenze, gerundete Anzeige |
| --- | --- |
| Gerade | `6.970512911394308551550E-35` |
| Ungerade | `6.475113837453108915595E-32` |

Maßgeblich sind die exakten rationalen Werte in `integer_results.json`.
Der gemeinsame oben gewählte Boden ist kleiner als beide Untergrenzen.

## Was gegenüber O8 neu bewiesen und neu gerechnet wurde

- Beim q=2-Kanal entstehen rechts von A8 Viererketten. Seine Norm wird mit
  dem goldenen Schnitt bezahlt; nur das q=8-Gewicht zu ergänzen reicht nicht.
- Der neue Verlust ist höchstens `31481/5000`. Der Schnitt bei Grad 594/595
  liefert den vollständigen physischen High-Floor `2/3`, Defektboden `1/19`
  und Kodimension 296 je Parität.
- Der Gammafehler ist auf dem größeren Radius `11/10` neu eingeschlossen.
- Beide niedrigen Formen und die Grams der **gesamten** hohen Modellantwort
  sind neu berechnet. V², S² und alle gemischten Beiträge sind enthalten.
- Die hohe Mellinkorrektur, der Gammafehler und die Normumrechnung sind bezahlt.
  Die Graphmetrik und der tatsächliche Defekt-Schurrest sind in der analytischen
  Verbindung ausdrücklich berücksichtigt.

## Lesereihenfolge und eingefrorener Vorbereitungsstand

1. Dieses Dokument ist der aktuelle Ergebnisstand.
2. [PROOF.md](PROOF.md) enthält die vorher abgeschlossene Tail-/Domänenherleitung
   und das Fehlerbudget. Seine Aussagen „Terminal offen“ dokumentieren den
   Zeitpunkt **vor** der anschließend ausgeführten Rechnung.
3. [SCHUR_AND_TRANSPORT.md](SCHUR_AND_TRANSPORT.md) verbindet die Rechenmatrix
   mit dem vollständigen Schurrest und den korrigierten Transporten.
4. `reserve_results.json`, `common_reserve.json` und `integer_results.json`
   enthalten die tatsächlichen späteren Zertifikatsresultate.
5. [AUDIT.md](AUDIT.md) trennt Rechenprüfung, Quellenbindung und offene externe Abnahme.

`PROOF.md` und seine ursprüngliche Quittung `CHECK_RESULTS.json` bleiben
bytegebunden erhalten. `PACKAGE_STATUS.json` bezeichnet den abschließenden
Paketstand. Alle Dateien sind in `SHA256SUMS` gebunden.

## Lokale Reproduktion

Benötigt werden Python 3.13 und für Aufbau/Arb-Prüfung `python-flint==0.9.0`.
Die Ganzzahlprüfung benötigt nur die Python-Standardbibliothek.
Aus dem entpackten Paketverzeichnis:

```text
python check_a9.py --output replay_reserve.json
python common_reserve.py --input replay_reserve.json --output replay_common.json
python verify_integer_a9.py --output replay_integer.json
python check_normalization_a9.py --model normalization_model.json.gz --output replay_normalization.json
```

Der Ganzzahlprüfer kontrolliert die mitgelieferten Originalmatrizen und
rekonstruiert deren Fehlerterme selbst. `both_parities_strictly_certified`
beziehungsweise `both_parities_certified` müssen wahr sein; ein bloßer
Prozessabschluss der Arb-Prüfung genügt nicht.

Die Tail-Arithmetik kann mit `python check_tail.py --output replay_tail.json`
erneut laufen. Mit `--repository PFAD` werden zusätzlich die sieben
Git-Eingaben geprüft; ohne Repositoryzugriff entfallen nur diese sieben
Quellenkontrollen. Die ursprünglichen Quittungsdateien sollten erhalten bleiben.

Für einen erneuten vollständigen Integralaufbau:

```text
python generate_a9.py --degree 593 --gamma 224 --precision 3072 --output replay_model.json.gz
python check_a9.py --model replay_model.json.gz --output rebuilt_reserve.json
```

Der vollständige Aufbau ist wesentlich aufwendiger als die Zertifikatsprüfung.
Die Programme benötigen keine GitHub-Schreibberechtigung.

## Reichweite

Das Paket ist **lokal**; O10 und A9 wurden hier nicht veröffentlicht oder
auf Main integriert. O8/O9 sind bereits durch PR #174 und #175 integriert.
Main wurde inzwischen durch PR #176 auf `a77950be027dc1576b016c6a53bfad7ff65a04e4`
weitergeführt. Der [Abgleich der Normierungskorrektur](MAIN_COMPATIBILITY.md)
bestätigt die unveränderte Bedeutung der hier gebundenen konkreten A9-Form.

Offen bleiben die externe analytische Abnahme, die q=9-Wand strikt rechts
von A9, eine unbeschränkte positive Fortsetzung und sämtliche globalen
Aussagen zu Objekt X und RH.
