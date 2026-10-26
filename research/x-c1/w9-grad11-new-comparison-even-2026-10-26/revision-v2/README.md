# Grad-11-Vergleich v2 — gezielt gegengeprüft unter H1–H4

**Gezielte projektinterne Gegenprüfung von v2 abgeschlossen: PASS unter H1–H4
für den festgelegten reellen Zwölferraum.**

AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN. Checkliste **3/10**, Punkt 4 und der
vollständige A9→A11-Anschluss bleiben offen. Diese versionierte Bereitstellung
erfolgt auf einem Forschungsbranch mit Draft-PR; sie ist keine Integration in Main.

## Zuerst lesen

- **[GPT1-Gesamtvotum](gpt1/overall/GPT1-GESAMTVOTUM.txt)** mit Voraussetzungen,
  analytischem Anschluss, tatsächlichem Prüfumfang und Aussagegrenzen.
- [Autorenrevision v2](author/revision_review/BERICHT_V2.txt) und
  [Änderungsübersicht v1→v2](author/revision_review/DIFF_V1_V2.txt).
- [Frühere gezielte v2-Gegenprüfung](gpt1/targeted/GPT1-REVISION-V2-GEGENPRUEFUNG.txt)
  und [späterer Gesamtstatus](gpt1/overall/OVERALL_REVIEW_STATUS.json).
- [H1–H4 im vollständigen Wortlaut](gpt1/overall/HYPOTHESEN.txt) und
  [historische Quellenanker](gpt1/overall/HYPOTHESEN_QUELLEN.json).

Die ursprünglichen Angaben `UNRESOLVED` im Autorenbericht und der engere
Prüfumfang des früheren GPT1-Berichts bleiben bytegleich. Sie beschreiben
ihren jeweiligen Zeitpunkt. Das spätere Gesamtvotum schließt die dort noch
offene gezielte Gegenprüfung; eine externe Abnahme behauptet es nicht.

## Bestätigte Aussage und Grenzen

Für sämtliche reellen Linearkombinationen des festgelegten zwölfdimensionalen
geraden Eingaberaums gilt unter H1–H4:

```text
K_P[c] - <h_c,Q1^-1 h_c> >= 3.99038487528413e-19 G_W[c].
```

Die äußere Antwort P0 bleibt unverändert. Die neue Unterform Q1 und die
gemeinsame rationale Testabbildung sind im Gesamtvotum bezeichnet. Die
Zusatzpreise einschließlich inverser Young-Gewichte, sämtliche elf alten
Fehlerkomponenten und alle **144 Restkreuzgewichte** sind bezahlt.

- [Erneuerter exakter Restschluss](author/results/JOINT_REST_BUDGET_V2.json):
  `theta = 0.002403781178965734… < 1`.
- [Endliche Fehler-/Eliminationsrechnung](author/results/SOURCE_ARITHMETIC_CLOSURE_V2.json)
  und [rationaler LDL-Nachweis](author/results/SOURCE_CLOSED_GAP_EXACT_AUDIT_V2.json).
- [Unabhängige Radiusprüfung](gpt1/targeted/INDEPENDENT_RADIUS_AUDIT.json),
  [rationale Schlussprüfung](gpt1/targeted/INDEPENDENT_EXACT_AUDIT.json) und
  [Prüfer-Negativkontrollen](gpt1/targeted/INDEPENDENT_CHECKER_CONTROLS.json).
- [Analytische Quellenbindungen](gpt1/overall/ANALYTIC_SOURCE_BINDINGS.json),
  [neue rationale Formordnungsanker](gpt1/overall/NEW_FORM_ORDER_ANCHORS.json)
  und [konkrete Hüllenanwendungen](gpt1/overall/APPLICATION_BINDINGS.json).

Die **4.704 gespeicherten Abschnittsbelege** wurden rekombiniert, nicht durch
GPT1 neu integriert. Alle **5.263 v1-Originaldateien** bleiben unverändert.
Die neue genaue Reserve ist gegenüber dem ungerundeten v1-Wert minimal
kleiner; die größere Dezimalanzeige gegenüber dem konservativ gerundeten
ersten Bericht ist keine Verbesserung.

Die Aussage umfasst nicht ungerade Parität, den benötigten gesamten
Ergänzungsraum und dessen Anschluss oder eine vollständige neue Inversmajorante
für weitere konstruktive Schritte. Der ganze Rest der hier festgelegten zwölf
Quellen ist bezahlt; das ist von einem Abschluss des gesamten vorgesehenen
Funktionsraums zu unterscheiden. Der alte Routenausschluss bleibt gültig.

## Unveränderte Archive und Abhängigkeit

| Datei | Byte | SHA-256 |
| --- | ---: | --- |
| [Erforderliches v1-Basisarchiv](https://github.com/Waschtl904/objekt-x-programm/releases/download/grad11-even-author-2026-10-26-v1/Objekt-X-Neuer-Vergleich-Grad11-GPT2-2026-10-26.zip) | 360.325.509 | `024f20f0c6086aefabb6e3d759f91aaa466906a864c673c0c0b467f3ee627946` |
| [Additive Autorenrevision v2](https://github.com/Waschtl904/objekt-x-programm/releases/download/grad11-even-reviewed-2026-10-26-v2/Objekt-X-Grad11-Revision-v2-2026-10-26.zip) | 11.873.565 | `aa5d5df0a068991972ba7eb5f60de9106f865cc53a891330394847666251e4fa` |
| [GPT1-Gesamtvotumspaket](https://github.com/Waschtl904/objekt-x-programm/releases/download/grad11-even-reviewed-2026-10-26-v2/Objekt-X-Grad11-v2-GPT1-Gesamtvotum-2026-10-26.zip) | 175.084 | `1a5d6e4b5b60164891333917211fd65fd828fda2fea820a3a32959a7f61e2957` |

**v2 ist ohne v1 keine vollständige Reproduktionsumgebung.** Das Basisarchiv
wird ausschließlich von der bestehenden v1-Veröffentlichung referenziert.
Es wird weder neu verpackt, erneut hochgeladen noch in die Git-Historie kopiert.
Das GPT1-Gesamtvotumspaket enthält das frühere gezielte GPT1-v2-Prüfpaket
unverändert als verschachteltes ZIP. Eine zweite Archivkopie ist nicht nötig.
GitHubs automatisch erzeugte „Source code“-Archive ersetzen diese Dateien nicht.

[Archivdeskriptor](ARCHIVES.json) ·
[Originales v2-Manifest](author/REVISION_MANIFEST.json) ·
[Originales GPT1-Manifest](gpt1/overall/MANIFEST.json) ·
[Bindung der veröffentlichten Lesekopien](PUBLICATION_MANIFEST.json).

**Fehlender separater Beleg:** Die Datei
`Objekt-X-Grad11-Revision-v2-Beleg-2026-10-26.json` wurde GPT1 nicht als eigene
Datei vorgelegt. Ihr Inhalt und ihr Hash werden nicht als geprüft dargestellt.
Die hier genannten Archividentitäten hat GPT1 an den empfangenen ZIPs selbst
festgestellt. [Prüfidentitäten](gpt1/overall/REVIEW_IDENTITIES.json).

## Prüfstufen und Reproduktion

Der [unveränderte v2-Prüfer](author/verify_revision_v2.py) ist der maßgebliche
Autorenprüfer. Der historische v1-Prüfer besitzt die dokumentierte Lücke unter
optimiertem Python; seine früheren Erfolgsmeldungen ersetzen keinen v2-Test.
v2 weist `-O`, `-OO` und `PYTHONOPTIMIZE` ausdrücklich ab.

Nach Download von v1 und v2 kann mit gewöhnlichem Python die Byte- und
rationale Zertifikatsprüfung in einem neuen Zielordner ausgeführt werden:

```bash
python -B author/verify_revision_v2.py \
  --base /pfad/Objekt-X-Neuer-Vergleich-Grad11-GPT2-2026-10-26.zip \
  --revision /pfad/Objekt-X-Grad11-Revision-v2-2026-10-26.zip \
  --revision-sha256 aa5d5df0a068991972ba7eb5f60de9106f865cc53a891330394847666251e4fa \
  --destination /pfad/NEUER_ORDNER
```

Details: [Autorenbefehle, Abschnitt 4](author/revision_review/BERICHT_V2.txt),
[GPT1-Reproduktion und Prüfumfang](gpt1/overall/REPRODUCE.txt). Lesekopien von
einzelnen Prüfern sind in ihrer ursprünglichen entpackten Struktur auszuführen;
diese Repository-Auswahl ersetzt nicht die vollständigen Archive.

Der neue [Veröffentlichungsprüfer](verify_publication.py) kontrolliert allein
Datei-/Archivbindungen und den Erhalt der v1-Veröffentlichung:

```bash
python -B verify_publication.py \
  --v1 /pfad/Objekt-X-Neuer-Vergleich-Grad11-GPT2-2026-10-26.zip \
  --v2 /pfad/Objekt-X-Grad11-Revision-v2-2026-10-26.zip \
  --gpt1 /pfad/Objekt-X-Grad11-v2-GPT1-Gesamtvotum-2026-10-26.zip \
  --git-ref HEAD
```

Ein PASS dieses Byteprüfers ist keine neue mathematische Gegenprüfung.
Diese Veröffentlichung führt keine Forschungsrechnung aus. Die neuen
Begleittexte sind von allen unveränderten Originalkopien im Manifest getrennt.
Die 48 Dateien des v1-Veröffentlichungscommits bleiben vollständig bytegleich.
