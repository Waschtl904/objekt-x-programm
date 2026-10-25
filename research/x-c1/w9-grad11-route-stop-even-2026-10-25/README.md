# Grad-11: bedingter Ausschluss der festen Vergleichsroute

**Erstveröffentlichungsstand vom 25. Oktober 2026; technische Ergänzung siehe unten.** Dieser Forschungsbranch stellt die bereits eingefrorene GPT2-Lieferung, die abgeschlossene gezielte GPT1-Gegenprüfung und ihre Belegkette als Draft zur Einsicht bereit. Veröffentlichung und mathematische Abnahme bleiben getrennt; ein Merge ist nicht freigegeben.

Referenz: [`137940b4e8ea391af408992ae17fb4eebbd6d7c7`](https://github.com/Waschtl904/objekt-x-programm/commit/137940b4e8ea391af408992ae17fb4eebbd6d7c7), Tree `6b9d0fbf4850b80ab92092ddd8238049e7dba701`.

## Ergebnis und Grenze

Unter den übernommenen **H1–H4** erfüllt der eingefrorene zulässige W-Einheitszeuge außerhalb des bisherigen Zweiraums

\[
E_{\mathrm{fix}}[s]\ge F_T[s]>K_P[s],\qquad
F_{\mathrm{lo}}-K_{P,\mathrm{hi}}>1.0476\cdot10^{-6}.
\]

Damit scheitert der positive Vergleich auf dem gesamten vorgesehenen geraden Grad-11-Raum mit **dieser unveränderten äußeren Antwort und `Q_new`**. Weitere Ganzrestintegrationen oder eine bloße Verbesserung des inneren Tests können dieselbe feste Vergleichsenergie nicht retten. Die vollständigen rationalen Endpunkte stehen in den verlinkten Originalbelegen.

Dies beweist **keine negative tatsächliche Weil-Richtung**. Andere äußere Antworten, Unterformen oder Majoranten der tatsächlichen A9-Inverse werden nicht ausgeschlossen. Die Mischterm-Erklärung bleibt getrennte Modelldiagnose. L1 und der bisherige reelle Zweiraumnachweis bleiben unberührt. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN; Checkliste 3/10; Punkt 4, A9→A11 und Objekt X offen.** Die kurze Nennung von H1–H4 ersetzt nicht deren vollständigen Wortlaut und Quellenanker.

## Direkt lesbare Originale

Alle Dateien unter `originals/` sind unveränderte Originalkopien. Ihre historischen Aussagen wie „Gegenprüfung ausstehend“, „keine Veröffentlichung beauftragt“ oder lokale Pfade werden nicht nachträglich umgeschrieben. Die zeitlich spätere Gegenprüfung und diese Veröffentlichung werden separat zugeordnet.

| Inhalt | Originalkopie |
| --- | --- |
| GPT2-Autorenbericht | [BERICHT.txt](originals/grad11-review/input/BERICHT.txt) |
| Vollständige Voraussetzungen / Quellen | [HYPOTHESEN.txt](originals/grad11-review/input/HYPOTHESEN.txt), [HYPOTHESEN_QUELLEN.json](originals/grad11-review/input/HYPOTHESEN_QUELLEN.json) |
| Plan und eingefrorener rationaler Zeuge | [PLAN.txt](originals/grad11-review/input/PLAN.txt), [DIAGNOSTIC-DIRECTION.json](originals/grad11-review/input/DIAGNOSTIC-DIRECTION.json) |
| Gerichtete Autorenergebnisse / Endpunktaudit | [DIRECTED-DIAGNOSTIC.json](originals/grad11-review/input/DIRECTED-DIAGNOSTIC.json), [ENDPOINT-AUDIT.json](originals/grad11-review/input/ENDPOINT-AUDIT.json) |
| GPT1-Gegenprüfbericht / unabhängiger Audit | [GPT1-GEGENPRUEFUNG.txt](originals/grad11-review/GPT1-GEGENPRUEFUNG.txt), [INDEPENDENT-AUDIT.json](originals/grad11-review/INDEPENDENT-AUDIT.json) |
| Frische GPT1-Ergebnisse | [DIRECTED-DIAGNOSTIC.json](originals/grad11-review/replay/DIRECTED-DIAGNOSTIC.json), [ENDPOINT-AUDIT.json](originals/grad11-review/replay/ENDPOINT-AUDIT.json) |
| Belegkette vom 25.10.2026 | [Belegkette](originals/Objekt-X-Grad11-Belegkette-GPT1-2026-10-25.txt) |
| Historische Quellenbindungen | [SOURCE_BINDINGS.json](originals/grad11-review/input/sources/SOURCE_BINDINGS.json), [REMOTE-REFERENCES.json](originals/grad11-review/input/REMOTE-REFERENCES.json) |
| Originalmanifeste | [Autorenmanifest](originals/grad11-review/input/MANIFEST.json), [GPT1-Paketmanifest](originals/PACKAGE-MANIFEST.json) |
| Reproduktionsanleitungen | [GPT2](originals/grad11-review/input/REPRODUKTION.txt), [GPT1](originals/grad11-review/REPRODUKTION-GPT1.txt) |

Die übrigen Textmitglieder des Gegenprüfpakets, einschließlich Programme, Modelle, Logs und Pfadpatches, liegen ebenfalls unter `originals/` mit ihren ursprünglichen Paketpfaden. Zur numerischen Reproduktion ist das ZIP separat zu entpacken; dessen Verzeichnisstruktur und gepinnte Eingänge sind maßgeblich. Die Lesekopien sind keine neue Installation und keine Einladung zu weiteren Rechnungen.

## Archividentitäten

| Archiv | Byte | SHA-256 |
| --- | ---: | --- |
| GPT1-Gegenprüfpaket, [Archivdeskriptor](archives/ARCHIVE.json) | 12838318 | `9fa36e19fcacc2f0392149d9b8c0f29b9b47a0987ce77be6631a4fcc437c0ca7` |
| Eingebettetes GPT2-Originalarchiv | 875069 | `be2b1ab43514454cfec95dd1283d81e8d2f34745f4cf1554ecfd2d6811888e93` |

Das GPT2-Original liegt im GPT1-ZIP unter `upload/Objekt-X-Grad11-Machbarkeitsanalyse-GPT2-2026-10-25.zip`; keine zweite eigenständige Archivkopie wird publiziert. Auch das darin bereits gebundene historische Zweiraumarchiv bleibt unverändert enthalten. Kein ZIP wurde neu verpackt.

Die unveränderten GPT1-ZIP-Bytes liegen wegen der 16-MiB-Anfragegrenze des Veröffentlichungsconnectors in zwei geordneten Binärteilen: [Teil 1](archives/Objekt-X-Grad11-Gegenpruefung-GPT1-2026-10-25.zip.parts/part-001.bin) und [Teil 2](archives/Objekt-X-Grad11-Gegenpruefung-GPT1-2026-10-25.zip.parts/part-002.bin). Der Deskriptor bindet Größen, Offsets und Teilhashes. Zusammensetzen im Paketverzeichnis, ohne Entpacken oder Neuverpacken:

```bash
cat archives/Objekt-X-Grad11-Gegenpruefung-GPT1-2026-10-25.zip.parts/part-001.bin archives/Objekt-X-Grad11-Gegenpruefung-GPT1-2026-10-25.zip.parts/part-002.bin > /tmp/Objekt-X-Grad11-Gegenpruefung-GPT1-2026-10-25.zip
sha256sum /tmp/Objekt-X-Grad11-Gegenpruefung-GPT1-2026-10-25.zip
```

Der Byteprüfer rekonstruiert das Archiv ebenfalls in dieser Reihenfolge im Speicher und kontrolliert seine vollständige Originalidentität, alle eingebetteten Originalbindungen und sämtliche Lesekopien.

Die gesonderte Original-Belegkette hat 8880 Byte und SHA-256 `7e4e67c889a211c84aa79ef5ec40b660d310ac5e8dc23d22d43401b75d75882c`.

## Prüfumfang und Veröffentlichungsbindung

Der abgeschlossene Forschungsprüflauf umfasste Eingabezulässigkeit, Anwendung der gemeinsamen ganzen Quellen-/Formfehler einschließlich Homogenität, unabhängige Einschließung der 144 Metrikeinträge, Momentlift, einen frischen F/K-Replay (K: 55 Abschnitte, je 128 Knoten) und exakte rationale Endpunktrekombination. Die historischen Grundlagen wurden übernommen; keine unabhängige Neuerzeugung aller 411 früheren Ganzrestintegrationen oder externe Gesamtbegutachtung wird behauptet.

Dieser Veröffentlichungsschritt prüft ausschließlich Originalbytes, Archivmitglieder, Kopien, Git-Blobs, Navigation und Diff-Scope. Er führt keine Forschungsrechnung aus. Die sechs neuen Begleitdateien sind diese README, `.gitattributes`, [ARCHIVE.json](archives/ARCHIVE.json), [PUBLICATION_MANIFEST.json](PUBLICATION_MANIFEST.json), [PUBLICATION_CHECK.md](PUBLICATION_CHECK.md) und [verify_publication.py](verify_publication.py). Sie gehören nicht zu den eingefrorenen Originalen.

Der neue Prüfer kontrolliert nur Bytes und Archivbindungen:

```bash
python3 research/x-c1/w9-grad11-route-stop-even-2026-10-25/verify_publication.py
# Gegen Git-Blobs eines ausdrücklich gewählten veröffentlichten Commits:
python3 research/x-c1/w9-grad11-route-stop-even-2026-10-25/verify_publication.py --git-ref HEAD
```

Das Veröffentlichungsmanifest bindet alle übrigen Dateien dieses Verzeichnisses mit Größe, SHA-256 und Herkunft; sich selbst bindet es über den Git-Commit. Der tatsächliche nachgelagerte Abgleich des veröffentlichten Heads wird in der Draft-PR-Beschreibung mit vollständigem Head- und Tree-SHA dokumentiert. Grüne CI wäre keine zusätzliche mathematische Abnahme und keine Mergefreigabe.


## Technische Ergänzung: gebundene historische Referenzkopien

Diese neue Begleitnotiz ergänzt den Erstveröffentlichungsstand `a8d69b04f683e34a7bb3c33b35959e1f3bda4e14`. Die dortige Draft-/Freigabeangabe und das Feld `scope` des Veröffentlichungsmanifests beschreiben den damaligen Veröffentlichungsauftrag. Für den technischen Folgecommit wurde gesondert die begrenzte Reparatur mit anschließendem normalem Merge freigegeben, sofern sämtliche vereinbarten Prüfungen und die PR-CI bestehen, der Diff im freigegebenen Umfang bleibt und Main weiterhin auf der oben genannten Referenz steht. Ein CI-Erfolg allein erteilt keine Freigabe. Der tatsächliche Integrationsstand wird in PR #260 dokumentiert; diese Notiz behauptet keinen bereits erfolgten Merge.

Die neue [Referenzdeklaration](../../../00-uebersicht/REFERENCE_COPIES.json) benennt ausschließlich die beiden historischen `PROOF.md`-Kopien aus `w9-new-k-schur-underform-even-2026-10-20` und `w9-residual-centered-control-even-2026-10-21` unter `originals/grad11-review/input/references/research/x-c1/`. Beide sind bytegleich mit ihren ursprünglichen Repositorypfaden am bereits registrierten Integrationscommit `4ede0b70e2df1f133c762d7b0e6527338d597874`. Diese zusätzliche Herkunftsbindung ersetzt keine Quellenverweise in den eingefrorenen Originalen.

Der [Validator](../../../scripts/research_state.py) behält die vollständige `proof_paths()`-Erkennung bei. Nur exakt deklarierte, validierte Kopien mit Rolle `ARCHIVED_REFERENCE_ONLY` werden von der eigenen `META.yaml`-Pflicht ausgenommen. Er prüft striktes Schema, eindeutige sichere Einzelpfade, reguläre Zieldateien ohne Symlinks in sämtlichen Pfadkomponenten, reguläre Git-Quelldateien (`100644` oder `100755`), vollständige Quellcommits innerhalb des registrierten Integrationsstands, SHA-256 und vollständige Bytegleichheit. Beim Basisvergleich muss die Quelle auch im zuvor registrierten Integrationsstand liegen; dessen gleichzeitige Fortschreibung darf eine neue Quelle nicht legitimieren. Selbstbindungen, deklarierte aktuelle oder historische Kopienketten sowie die gleichzeitige Ausweisung als kanonischer Beweis, Pending- oder META-Paket werden abgewiesen. Ordnernamen wie `originals` und `references` gewähren keine Ausnahme.

Die [Regressionstests](../../../tests/test_research_state.py) decken gültige Kopien und die genannten Manipulationen ab; sie sind zusätzlich unter optimiertem Python auszuführen. Alle neuen Ablehnungen verwenden explizite Prüfungen, keine wegoptimierbaren `assert`-Anweisungen. Der vollständige Validator mit Basisvergleich, die generierten Ansichten und der Veröffentlichungs-/Byteabgleich bleiben Pflichtprüfungen. Tatsächliche Befehle, Ergebnisse und commitgebundene PR-CI werden in der PR-Beschreibung protokolliert.

Der technische Folgecommit betrifft genau fünf Dateien: Validator, Tests, neue Referenzdeklaration, diese README und deren Eintrag in `PUBLICATION_MANIFEST.json`. Der gesamte PR ist damit nicht mehr ausschließlich eine additive Veröffentlichung im Paketpfad. Das historische [Veröffentlichungsprotokoll](PUBLICATION_CHECK.md) bleibt unverändert auf seinen damaligen Umfang bezogen. Originalarchive, Originalkopien, sämtliche übrigen Manifestbindungen, historische Anker und mathematische Statusangaben bleiben unverändert. Die Herkunftsprüfung ist keine mathematische Neuprüfung oder Statusaufwertung.
