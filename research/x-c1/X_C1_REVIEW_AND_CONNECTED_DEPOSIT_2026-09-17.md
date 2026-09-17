# X-C1 — Revieweingang und Sicherung der verbundenen Fensterkonstruktion

**Datum:** 17. September 2026. **Art:** append-only Forschungsablage, kein neuer mathematischer Audit.
**Elternstand:** `4871a5343a996be49e66a565d1e232b2ecd38f54` auf PR #137.
**Gelesener main:** `d18f545d8d0a662e978102f84341a5b11a40d5a4`.

## 1. Neu eingegangenes Gutachten, eng gebundener Prüfgegenstand

[Unverändertes technisches Gutachten](reviews/PR137_4871a53_REVIEW_RECEIVED_2026-09-17.md), vom Nutzer als Markdown eingereicht.
Es nennt den vollständigen Commit `4871a5343a996be49e66a565d1e232b2ecd38f54` und die Dreizellen-Faktorisierung, induzierte Schur-Kopplung, Carleman-Nahtanalyse und den bedingten Schur-Schritt als Prüfumfang.
Sein Urteil ist positiv; seine Empfehlung lautet ausdrücklich: kein Merge, Forschungs-Draft beibehalten.
Die Aussage über 35 erfolgreiche Prüfungen wird als Aussage dieses Gutachtens bewahrt, nicht als heutige Neuausführung des Prüfers.

**Reviewereignis:** `POSITIVE-WRITTEN-REVIEW-RECEIVED / TARGET 4871a53 / SCOPED`.
Die Originaldatei bezeichnet ihren Verfasser nicht namentlich und enthält keine eigenen Ausführungslogs. Hier wird weder eine zusätzliche Identität noch eine eigene Prüfung der Reviewer-Unabhängigkeit behauptet.
Der im Gutachten selbst weitergeführte Status `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN` wird nicht stillschweigend geändert. Das positive eingegangene Urteil ist trotzdem als neues Ereignis sichtbar; es wird nicht als bloß fehlendes Feedback behandelt.
Keine pauschale Freigabe der übrigen PR-Dateien, kein GitHub-APPROVE im Namen eines anderen Reviewers und keine Registry-Promotion.

## 2. Späteres verbundenes Fenster separat erhalten

[Originales Connected-Arbeitspaket](connected-3_8-2026-09-17/README.md) mit [Nachweis](connected-3_8-2026-09-17/X_C1_CONNECTED_MOMENT_FACTORIZATION.md), [Prüfer](connected-3_8-2026-09-17/check_connected_constants.py), vorhandenen Log-/JSON-Ausgaben und ursprünglichem SHA256SUMS.
Alle sechs Dateien sind unverändert aus `X_C1_Verbundene_Quellen_2026-09-17.zip` übernommen. ZIP-SHA-256: `792950102cbb34463d6f75efa7a2159dde2d1ab50f475d95ee72083cf695b8eb`.
Die fünf ursprünglichen Manifesteinträge wurden gegen die enthaltenen Bytes geprüft. Die separat vorliegende Nachweisdatei ist ebenfalls bytegleich mit dem ZIP-Eintrag.

**Status:** `X-C1-CONNECTED-3/8 / AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.
Behaupteter Satz des Autortextes: expliziter positiver Output auf `H1_0(-3/8,3/8) intersect ker E_+ intersect ker E_-`, mit `Q_W[u] > (487/20008)||u||^2 > (1/50)||u||^2` für nichtverschwindende Quellen.
Das ist ein zusammenhängendes Teilfenster mit aktivem Prime-2-Kanal, NICHT das vollständige Einheitsfenster oder eine Erweiterung, die die ganze Prime-3-Dreizellenfamilie enthält.
Das oben eingegangene Gutachten prüft diesen späteren Text NICHT. Sein positives Urteil wird nicht auf die Connected-Konstruktion übertragen.

Die Formulierungen »kein Push/keine Repository-Änderung« im ursprünglichen Paket dokumentieren dessen Entstehungsrunde. Die heutige erste Repository-Ablage ändert diese historischen Dateien nicht rückwirkend.

## 3. Bytebindung und tatsächliche heutige Prüfungen

| Datei | Git-Blob-SHA1 |
|---|---|
| Eingereichtes Gutachten | `c9f4d10018864fddc42c064a39affcf3f6336c51` |
| Paket-README | `5e717c20b694be1e992460266a17dddfc531faea` |
| Paket-SHA256SUMS | `980fc7f36269adb17efc8379749b9c85acdfa4cf` |
| Connected-Nachweis | `fb8e6e568f2719fd02a957aedece34de75c4825c` |
| Connected-Prüfer | `93e51b81b9b0ea5ab9578430bbefd1a12957030f` |
| Vorhandenes connected_checks.log | `9173243d85c79933ccc5488f33f15e40579965b3` |
| Vorhandenes connected_results.json | `491bbc03b4be257b18095a4515e56692f3fb69b1` |

Gutachten: 4381 Bytes; SHA-256 `3c4b9d8506287e193590bfa05cfc302f9f516f46f6fbc34c6171827bc92c38b3`.
Connected-Nachweis: 21149 Bytes; SHA-256 `b19cdc50a91f73ae4eb0fb6d630d9ef08ae8abb532f51ce78a0075554208edc9`.
Heute geprüft: Paketmanifest, Bytes, UTF-8 und Python-Syntax. Kein mathematischer Checker wurde erneut ausgeführt. Die 40 Checks im mitkopierten Protokoll sind die vorhandenen lokalen Ergebnisse der Konstruktionsrunde, kein heutiger CI-Lauf oder externer Vollbeweis.

Zur optionalen Reproduktion aus einem frischen Verzeichnis den unveränderten `check_connected_constants.py` ausführen; er schreibt `connected_results.json` in das Arbeitsverzeichnis. Die vollständigen unendlichdimensionalen Behauptungen bleiben analytische Beweispflichten.

## 4. Nächster mathematischer Gegenstand, kein Navigationsauftrag

Die variable Knotenfunktion und regionale Gammaenergie im größeren verbundenen Fenster gemeinsam kontrollieren. Die zwei globalen Momente erhalten; zusätzliche niedrige Richtungen nicht durch erfundene weitere NULLPOL-Bedingungen entfernen.
Diese Ablage sichert Fortschritt und Gutachten. Sie startet keinen neuen A1-/C0-Audit, schreibt keine historische Spezifikation um und ändert weder main noch die Registry.
PR #137 bleibt Draft. Kein Merge oder Auto-Merge, kein neuer Workflow und kein angeforderter CI-Lauf. Ein späterer Mergeentscheid wird getrennt für einen definierten Quellstand und Prüfumfang getroffen; das offene Vollfensterziel allein verbietet nicht grundsätzlich die spätere Übernahme eines geprüften Teilresultats.
