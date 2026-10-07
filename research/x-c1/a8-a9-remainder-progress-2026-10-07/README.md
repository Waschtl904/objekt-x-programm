# A8→A9: aktueller Stand des vollständigen Restes

7. Oktober 2026 · **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Der Anschluss von acht festen Quellen ist positiv. Für den gesamten neuen
Rest liegen die Raumdarstellung, ein eingefrorener Pilot und erste rigorose
Operatorbausteine vor. **Die volle Schranke ‖B_R‖<1 bleibt offen.**

## Einstieg und Belege

| Stufe | Ergebnis | Originalbericht |
| --- | --- | --- |
| Acht Quellen | Vier je Parität; positive Reserve nach vollständigem alten Schurabzug | [Bericht](packages/eight-source/BERICHT.txt) |
| Vollständiger Rest | Quotientenkoordinaten und kompakter Defektoperator | [Bericht](packages/remainder/BERICHT.txt) |
| Domäne und Kompaktheit | Analytische Begründung; fachliche externe Prüfung offen | [Lemmata](packages/domain/LEMMATA.txt) |
| Fester Pilot | Acht W_X-orthogonale Richtungen je Parität; Abnahme festgelegt | [Protokoll](packages/pilot/PROTOKOLL.txt) |
| Halbinverse | 16 vollständige Bilder mit gemeinsamem Fehler eingeschlossen | [Bericht](packages/half-inverse/BERICHT.txt) |
| Gewichtete alte Antwort | Rationale Faktorform und zwei partielle Fehlergrame | [Bericht](packages/weighted-response/BERICHT.txt) |

[Aussagen, Voraussetzungen und Beweiswege](PROOF.md) ·
[Archiv- und Dateibindungen](SOURCE_BINDINGS.json) ·
[unveränderte Originalarchive](archives/)

Alle sechs Archive bleiben bytegleich. Ihre Programme, Herleitungen und
Ergebnisse sind zusätzlich unter `packages/` lesbar. Die großen Eingaben
liegen in den Originalarchiven; zum Ausführen dient der folgende Wrapper.
Historische „GitHub unverändert“-Angaben beschreiben den Entstehungsstand.
Die übermittelten KI-Gegenprüfungen sind begrenzte Prüfungen und keine externe
fachmathematische Begutachtung.

## Nächste Rechnung

1. Die sechs empfindlichen gemeinsamen Fehlerkräfte T0 vΔ in der vollen
   H-Metrik und die vier Kopplungen CΔ in der M_-^{-1}-Metrik einschließen.
2. Ihre Werte an Y und die gemeinsamen Kreuzterme berechnen; daraus U00 bilden.
3. G01 und die volle komprimierte Tailnorm β_tail kontrollieren und den
   eingefrorenen Schurtest anwenden.

Der Pilotraum bleibt unverändert. Mehr Präzisionsbits allein beseitigen den
dominierenden logarithmischen Residualfehler der Halbinverse nicht. Das alte
185-dimensionale Komplement darf nicht mit dem neuen unendlichen Rest
verwechselt werden. Erst nach vollständigem Anschluss folgt A9→A11 als Test
derselben Regel.

## Prüfung und Reproduktion

Vom Repository-Stamm mit Python 3.13, ohne zusätzliche Bibliotheken:

```text
python -B research/x-c1/a8-a9-remainder-progress-2026-10-07/replay.py --output ../a8-a9-remainder-check
```

Das Ziel muss neu sein und außerhalb des Repositorys liegen. Der Wrapper
entpackt alle Archive nach Prüfung ihrer Hashes und geschlossenen Manifeste,
kontrolliert die lesbaren Kopien sowie die Bindungen zwischen den Stufen und
führt die Originalprüfer erneut aus:

- Acht-Quellen-Schlussmatrizen beider gespeicherten Präzisionsläufe;
- exakte Konstanten der Restdarstellung;
- Gramprüfungen und Präzisionsvergleich der eingefrorenen Pilotgeometrie;
- Halbinversenfehler, partielle 19I-Matrizen und Präzisionsvergleich;
- große ganzzahlige Positivitätszertifikate, rationale Faktorform und partielle
  gewichtete Fehlergrame.

Die neu erzeugten Prüfergebnisse müssen mit den gebundenen Ergebnissen
übereinstimmen. Die analytischen Domänen-/Kompaktheitslemmata werden über ihre
Dateibindungen erhalten; sie besitzen keinen maschinellen Beweis.

**Umfang dieser Abnahme:** erneute exakte Prüfung gespeicherter Zertifikate.
Keine erneute Ausführung der langen Operatorintegrationen; keine unabhängige
Rekonstruktion der ursprünglichen A8/A9-Modelle. Die vorhandenen numerischen
Läufe bei zwei Präzisionen bleiben samt Programmen und Ergebnissen gebunden.

Für vollständige numerische Wiederholungen enthalten die entpackten Originale
ihre unveränderten Anleitungen: [Acht Quellen](packages/eight-source/README.txt),
[Halbinverse](packages/half-inverse/REPRODUCE.txt) und
[alte Antwort](packages/weighted-response/REPRODUCE.txt).
Sie verwenden Python 3.13 und python-flint 0.9.0. Laufzeiten sind keine
mathematischen Daten; maßgeblich sind die angegebenen Intervall- und
Zertifikatsprüfungen.

### Vorab festgelegte Pflichtprüfungen dieser Integration

1. Der vollständige oben beschriebene begrenzte Replay, mit allen sechs
   Archiven und unveränderten Ergebnissen.
2. Negativkontrollen für beschädigte Bindungen und unerlaubte Entpackpfade;
   relevante und irrelevante CI-Pfade sowie Fehlerweitergabe.
3. Registry-Validator, deterministische Ansichten, Registry-Tests und
   historische Integritätsbindungen.
4. Erfolgreiche anwendbare CI am endgültigen PR-Head und am Main-Mergecommit.

Kein CI-Erfolg promotet die offenen Operatorgrößen oder den externen Review.
