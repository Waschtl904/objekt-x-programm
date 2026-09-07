# R43-Stackintegration: 20 geprüfte PRs auf main

Am 7. September 2026 wurde der bestehende R43-Forschungsstack nach ausdrücklicher
Merge-Freigabe des Nutzers integriert. Alle 20 PRs wurden einzeln in ihrer
Abhängigkeitsreihenfolge auf `main` gemergt; es wurde kein weiterer
Forschungs-Draft angelegt.

## Ergebnis und Reichweite

Die integrierten PRs sind:

```text
55, 56, 57, 58, 61, 64, 66, 68, 69, 70,
72, 74, 76, 78, 80, 81, 83, 84, 85, 86
```

Der letzte Forschungs-Merge, vor diesem Governance-Abschluss, ist
`2ae9407cd3111113ef01d40e5270e4c9c3f6df07`. Das ist ein historischer
Integrationsanker, nicht der selbstreferenziell gespeicherte aktuelle
`main`-Head. Der aktuelle Head wird weiterhin live aus GitHub gelesen.

Das maschinenlesbare [Merge-Manifest](R43_MERGE_REVIEW_2026-09-07/merged_manifest.json)
enthält für jeden PR den tatsächlich geprüften Head, vorheriges `main`,
Merge-Commit und GitHub-URL. Sämtliche Merges verwenden reguläre
Merge-Commits; ihre beiden Eltern wurden jeweils gegen
`[vorheriges main, geprüfter PR-Head]` kontrolliert.

Keine Branches wurden gelöscht, keine Historie erzwungen umgeschrieben und
keine Admin-Umgehung verwendet. Der unabhängige
[PR #49](https://github.com/Waschtl904/objekt-x-programm/pull/49) wurde nicht
verändert und gehört nicht zu diesem Stack.

## Reviews und notwendige Korrekturen

Fünf getrennte, read-only arbeitende AI-Reviewer prüften die tatsächlichen
Dateiänderungen und benötigten Primärdefinitionen. Ihre Freigaben beziehen
sich auf die dokumentierten lokalen beziehungsweise endlichen
Forschungsumfänge, nicht auf einen Vollbeweis von P11, eine blinde
Cross-Model-Zertifizierung, ein Intervallzertifikat oder einen menschlichen
Review.

| Reviewgruppe | Bericht | Abschluss |
|---|---|---|
| PR55–58 | [Schur-/Resolventengrundlagen](R43_MERGE_REVIEW_2026-09-07/review_55_58.md) | Freigegeben im dokumentierten Scope |
| PR61/64 | [Retained Rows und Collar](R43_MERGE_REVIEW_2026-09-07/review_61_64.md) | PR64 nach begrenzter Korrektur freigegeben |
| PR66/68/74/78/80/81 | [Reverse-Normal und No-Go-Audits](R43_MERGE_REVIEW_2026-09-07/review_66_81.md) | PR78/80 nach begrenzten Korrekturen freigegeben |
| PR69/70/72/76/83/84 | [Numerische Proxy-Regressionen](R43_MERGE_REVIEW_2026-09-07/review_numeric_69_84.md) | Originale und unabhängige Gegenrechnungen bestanden |
| PR85/86 | [XBAND, Anker und CI](R43_MERGE_REVIEW_2026-09-07/review_85_86.md) | PR86 nach Action-Pinning freigegeben |

Die historischen Blocker wurden nicht nachträglich als bestanden ausgegeben.
Vor Integration wurden folgende Änderungen in den bestehenden PRs
vorgenommen und an den neuen Heads gezielt nachgeprüft:

- **PR64:** Die falsche Behauptung, Konstanten lägen im Kern des vollständigen
  Residualoperators, wurde ausdrücklich zurückgezogen. Die ursprüngliche
  Collar-Abschätzung und die anschließenden CE-Formeln wurden nicht geändert.
  Gemergter Korrektur-Head:
  `ff327e3fb59dcfde7bd8260e779919961dd6f88d`.
- **PR78:** Die zweiseitige Occupancy-Vergleichsaussage setzt nun explizit
  eine feste ausreichend große Mindeststreifenbreite voraus. Für beliebige
  positive Breiten bleibt nur die obere Schranke mit `1+L`.
  Gemergter Korrektur-Head:
  `6807d1e04588de81d0e5b4c14a0a4e8e5756ba97`.
- **PR80:** Der Faktor `1+L` und der Hub-Aktivierungscutoff
  `p^k <= exp(2U)` wurden wiederhergestellt. Nicht reproduzierbare
  Gaußtabellen wurden zurückgezogen; die konstante Proxy-Tabelle ist
  explizit als `2r/61` definiert. Die Schärfeillustration wurde auf
  Verteilungsinformation beziehungsweise das primitive Modell begrenzt,
  nicht auf den vollständigen Restgraphen übertragen.
  Gemergter Korrektur-Head:
  `483421fe5eb94a4474103083ec998f4dfa3e4266`.
- **PR86:** Die drei Actions wurden auf verifizierte vollständige
  Commit-IDs gepinnt; mathematischer Code und Bericht blieben unverändert.
  Gemergter Korrektur-Head:
  `8f49e2397ff991b378600b092ce9b52c26b58fd0`.

Der korrigierte PR86-Head bestand den
[GitHub-CI-Lauf vor dem Merge](https://github.com/Waschtl904/objekt-x-programm/actions/runs/34096126971).
Die in den Reviewberichten genannten zusätzlichen Arbeitsprotokolle sind
Provenienzkennungen der Nachrechnung; die exakten geprüften Repository-Blobs
und analytischen Begründungen sind in den Berichten selbst festgehalten.

## Governance und unveränderte mathematische Grenzen

`ACTIVE_FRONT.yaml` enthält die vollständige historische Abhängigkeitskette
mit `open_pr_count: 0`. Historische `head_sha`/`parent_head_sha`/`base`-Pins
bleiben erhalten; tatsächliche, gegebenenfalls korrigierte Merge-Heads und
GitHub-Ziele stehen getrennt in `merged_head_sha`, `merge_commit_sha` und
`github_base`. So werden die ursprünglichen Reviewabhängigkeiten nicht
nachträglich durch eine erfundene neue Parent-Kette ersetzt.

Die vier Navigationsdateien wurden entsprechend abgeglichen. Historische
Bezeichnungen wie „Draft-source ID“ bezeichnen die Herkunft einer Aussage,
nicht einen weiterhin offenen GitHub-PR. Der unveränderte
`scripts/validate_active_front.py` besteht den abschließenden lokalen
Metadatencheck für alle 20 Einträge.

`00-uebersicht/ACTIVE_THEOREM_REGISTRY.md` bleibt gegenüber dem
Ausgangs-main `94433f2c04097cea618557ae4d86a51e5805b915` byte-identisch:

```text
SHA256 54d92ee861b2b68fe6e06ca772b2a1e8fbdf49ec49be857966b7b5121797ae77
```

Merge bedeutet hier Aufnahme geprüfter, begrenzter Forschungsarbeit.
R43 und die globalen Fragen zu kanonischer Quelle, Reverse-Normal-Decay,
FD23-UNIF, FLAGDYN/TIGHT, Strong Terminal/C6, Objekt X und RH werden dadurch
nicht geschlossen. Es erfolgt keine neue Registry-Buchung und kein
mathematischer Freeze.

## Nachkontrolle

Nach dem Governance-Commit werden die beiden vorhandenen XBAND-Workflows
ausdrücklich auf dessen `main`-Head gestartet. Der aktuelle CI-Zustand
gehört zu den jeweiligen GitHub-Ausführungen; dieser versionierte Audit
behauptet keinen unveränderlichen aktuellen CI-Status und speichert nicht
den SHA seines eigenen späteren Commits.

Alle korrigierten Audit-Blobs wurden nach der Stackintegration erneut mit
den freigegebenen Fassungen verglichen. Der reguläre Merge hat sowohl diese
Korrekturen als auch die bereits vorher auf `main` vorhandene Governance
erhalten.
