# Neuer gemeinsamer Grad-11-Vergleich — ungeprüfte Autorenfassung

**GPT 2 · 26. Oktober 2026 · AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**

Diese Veröffentlichung macht einen eingefrorenen Autorenbefund zur Prüfung zugänglich.
Die gezielte Gegenprüfung der neuen Route durch GPT 1 und eine externe Begutachtung
stehen aus. H1–H4 bleiben Voraussetzungen. Checkliste: **3/10; Punkt 4 offen**.
Dies ist kein Abschluss von Objekt X oder der tatsächlichen Weil-Positivität auf dem
gesamten vorgesehenen Funktionsraum.

## Einstieg und vollständiges Belegarchiv

- [Autorenbericht](AUTHOR_RESULT.txt)
- [Abhängigkeitskarte und Prüfgrenzen](DEPENDENCIES.md)
- [Originale Reproduktionsanleitung](REPRODUCE.txt)
- [Vollständiges unverändertes ZIP herunterladen](https://github.com/Waschtl904/objekt-x-programm/releases/download/grad11-even-author-2026-10-26-v1/Objekt-X-Neuer-Vergleich-Grad11-GPT2-2026-10-26.zip)
- [Release mit Archiv, Identitätsdatei und eigenständigem Prüfer](https://github.com/Waschtl904/objekt-x-programm/releases/tag/grad11-even-author-2026-10-26-v1)
- [Archividentität](ARCHIVE_IDENTITY.json), [ursprüngliches Gesamtmanifest](ARCHIVE_MANIFEST.json),
  [Bindung jeder Lesekopie an ihr Archivmitglied](READING_MANIFEST.json)
- [Dokumentierter Auslieferungscheck](DELIVERY_CHECK.json)

Das Vollarchiv hat **360.325.509 Byte** und den SHA-256
`024f20f0c6086aefabb6e3d759f91aaa466906a864c673c0c0b467f3ee627946`.
Das ursprüngliche Manifest hat SHA-256 `3a388b3051f65b502db718b72c4e690c73c4fbf4a649360ca9afeb66b85389f2`.
Die Auswahl hier enthält lesbare Originaltexte, ausgewählte exakte Ergebnisdateien
und Prüferquellen. Alle 4.704 gerichteten Abschnittsbelege, die 24 analytisch
bezahlten Randstücke, Caches, Eingänge und historischen Originalarchive sind im
Vollarchiv enthalten. Die Lesekopien allein sind keine vollständige Reproduktionsumgebung.

## Berichtete Aussage

Für den festgelegten geraden zwölfdimensionalen Eingaberaum berichtet die neue
Autorenherleitung unter ihren benannten Voraussetzungen:

```text
K_P[c] - <h_c, Q1^-1 h_c> >= 3.990384872e-19 G_W[c].
```

Die endliche rationale Reserve ist `Gp >= 4e-19 G_W`; der gemeinsame ganze
Restpreis einschließlich aller Mischterme ist nach oben gerundet
`theta <= 0.002403782`. Die Schlussreserve ist `(1-theta) * 4e-19`.
Die genaue Aussage und ihre Domänen stehen im [Vergleichssatz](proofs/COMPARISON_THEOREM.txt).
Keine Erweiterung auf andere Parität, andere Räume oder sonstige Koeffizientenklassen
wird durch diese Einstiegsseite behauptet.

## Neue analytische Beweiskette

1. [Globale Formordnung](proofs/FULL_FORM_ORDER.txt): tatsächliche Kopplungen,
   negativer Young-Gegenterm, vollständiger Fo-Block und unendliches Komplement.
2. [Gemeinsame Quellenkette](proofs/SOURCE_INTERFACE_CHAIN.txt) und
   [gerichtete D-Fehleranwendung](proofs/DIRECT_D_APPLICATION.txt).
3. [Ganze Quellen-/Fehleranwendung](proofs/WHOLE_SOURCE_APPLICATION.txt):
   neue Koeffizienten und Fo-plus-T-Rest, ohne pauschale Übernahme alter Fehlerpreise.
4. [Konturen, Quadratur und Randstücke](proofs/NEW_CONTOUR_APPLICATION.txt),
   ergänzend [Nahnullverfeinerung](proofs/NEAR_ZERO_PROOF.txt).
5. [Gemeinsames Restlemma mit Mischtermen](proofs/JOINT_REST_LEMMA.txt) und
   [algebraischer Schluss zum Raumvergleich](proofs/COMPARISON_THEOREM.txt).

Zentrale exakte Daten: [endlicher Abschluss](evidence/SOURCE_ARITHMETIC_CLOSURE.json),
[rationaler LDL-Audit](evidence/SOURCE_CLOSED_GAP_EXACT_AUDIT.json),
[gemeinsame Testabbildung](evidence/COMMON_TEST_MAP_EXACT.json),
[Reservematrix und Inverse](evidence/JOINT_TAIL_GEOMETRY.json),
[ganzer Restschluss](evidence/JOINT_REST_BUDGET.json).

## Herkunft, Prüfung und unveränderte historische Angaben

Die Forschungsreferenz ist die im Originalarchiv bytegebundene Eingabekette:
[tatsächlich gelesene Eingänge](evidence/REPRODUCTION_INPUTS.json),
[historische Quellenbindungen](historical/SOURCE_BINDINGS.json) und
[H1–H4 mit historischen Commitankern](historical/HYPOTHESEN_QUELLEN.json).
Die dort angegebenen älteren Commitreferenzen behalten ihre Bedeutung.
Der bei der Veröffentlichung beobachtete Main und Elterncommit dieses
Bereitstellungszweigs ist `9a9e0e554508d308e96f10983a307f980d5c3b04`. Er ersetzt keine historische Forschungsreferenz.
Der neue Veröffentlichungscommit ist über den festen Release-Tag identifiziert.

Die ursprünglichen Texte und JSON-Dateien bleiben byteidentisch, einschließlich
damaliger Angaben wie „keine Veröffentlichung“, `publication_or_GitHub_write:false`
oder älterer komponentenbezogener Statusfelder. Diese Aussagen beschreiben ihren
Entstehungszeitpunkt. Die jetzige gesonderte Veröffentlichung wurde vom Nutzer
beauftragt und führt keine mathematische Statuspromotion durch.
Die frühere [GPT1-Prüfung des Hochraumbodens](historical/high-floor/GPT1-ANALYTISCHE-PRUEFUNG.txt)
betrifft ausschließlich ihren damaligen Block, nicht die neue Vergleichsroute.

Die vorhandenen Autorenchecks und die rationale Rekombination gespeicherter
Belege sind keine unabhängige analytische Prüfung. Details und Befehle stehen
in der [Abhängigkeitskarte](DEPENDENCIES.md).

## Für Perplexity und andere Leser

Zuerst diese Seite, dann die einzelnen Beweisdateien öffnen. Zu jedem Prüfvotum
angeben, welche Dateien tatsächlich zugänglich waren und welche Aussagen selbst
nachvollzogen wurden. Ein erreichbarer ZIP-Link belegt noch keinen Archivdownload,
Byteabgleich, Rechenlauf oder vollständigen Beweisaudit. Die Prüferquellen in
`checkers/` sind Lesekopien; auszuführen sind sie in der ursprünglichen Struktur
des entpackten Vollarchivs. Diese Veröffentlichung verändert Main nicht und
beauftragt keine neue Forschungsrechnung oder automatische Integration.
