# Archivmanifest für 21 Branchkandidaten — Vorbereitungsstand vom 25. September 2026

**PREPARATION_SNAPSHOT / NO_TAG_EXECUTION_AUTHORIZATION / NO_DELETION_AUTHORIZATION**

Repository-Pfad: `00-uebersicht/ARCHIVE_MANIFEST_2026-09-25.md`; zugehöriger [JSON-Vorbereitungsstand](ARCHIVE_MANIFEST_2026-09-25.json). Die Statusangaben in beiden Dateien beschreiben den unten datierten Vorbereitungsstand, keine laufend aktualisierte Ausführungsbuchung. Der tatsächliche Manifest-Mergecommit, Manifest-Blob und SHA-256 der integrierten Dateibytes werden nach dem Merge separat zurückgelesen und in die Tag-Freigabevorlage übernommen; sie werden hier nicht vorweggenommen.

Geprüfte Basis: `main@c4c8d882d5ed69c5c507a65aba9463639b187631`; Snapshot: 2026-09-25 10:38:56 UTC. Bestand: 63 Branches, 56 Tags, 0 offene PRs. PR #163 und seine tatsächliche Manifest-Veröffentlichung sind abgeschlossen.

## Umfang und Wiederverwendung

**Verbindliche Namensentscheidung:** Die 18 neuen Tags verwenden ausschließlich `archive/2026-09-25/content-resolved/<unveränderter Branchpfad>`. Keine Alias-Tags. Bestehende Archivtags, insbesondere der Delta-Descent-Nachfahrenanker, bleiben unverändert. Diese Entscheidung ist keine Tag-Anlage- oder Löschfreigabe.

Genau zwei vollständig in main enthaltene PR-Arbeitsbranches und 19 bereits eingeordnete Inhaltsfälle. Die 19 Entscheidungen werden aus der integrierten Inhaltskarte/Familienprüfung vom 24. September übernommen; der Abschluss des Integritätsfalls steht im Nachtrag vom 25. September. Weder die alten 138 A/B-Entscheidungen noch die 559 Quellbindungen werden neu bewertet.

18 neue annotierte Archivtags sind vorgesehen. Für `research/sw1-delta-descent` wird der vorhandene geschützte Nachfahrenanker wiederverwendet. Für die beiden PR-Arbeitsbranches reicht die bestätigte Main-Abstammung. Annotiert bedeutet nicht kryptografisch signiert.

Bei späterer Löschung genau dieser 21 aus dem beobachteten Bestand verbleiben **42 Branches**. Der Arbeitsbranch von #163 und der historische Integritätsbranch sind ausdrücklich nicht Teil dieser Charge. Ein neu angelegter Manifest-Arbeitsbranch käme vorübergehend hinzu und wäre separat abzuschließen.

## Noch offener Verbraucherpunkt

`research/sw1-m1-nd-img2-descriptor` ist der einzige Push-Branch in [`.github/workflows/sw1-m1-nd-img2-descriptor-cert.yml`](https://github.com/Waschtl904/objekt-x-programm/blob/c4c8d882d5ed69c5c507a65aba9463639b187631/.github/workflows/sw1-m1-nd-img2-descriptor-cert.yml#L4). Vor seiner Löschung muss `main` in diesen Filter aufgenommen und der tatsächliche Main-Lauf bestätigt werden. Checker, Inputs, Pfadfilter und mathematische Aussagen bleiben dabei unverändert. Der manuelle Auslöser existiert bereits; es geht um den automatischen Main-Push.

Die drei übrigen Branchfilter für A-FOLD, A2/A10 und IMG0 enthalten bereits `main`. Sie führen keinen Checkout des alten Branchnamens aus und halten die Löschung nicht auf. Die historischen Branchnamen in den Registern/Audits bleiben datierte Herkunftsangaben; ihre zwölf gepinnten Commitstände sind über vorhandene Archivtags oder die vorgesehenen Spitzen erreichbar.

## Schutz und Reihenfolge

Ruleset 23888675: aktiv, Tagziel `refs/tags/archive/**/*`, Update- und Löschsperre, keine Ausnahmen oder Bypass-Akteure. Neue Taganlage ist nicht gesperrt. Die Konfiguration ist änderbar; absolute Unveränderlichkeit wird nicht behauptet.

1. Dieses Manifest und den IMG2-Auslöser prüfen und über einen freigegebenen PR integrieren. Anwendbare CI und tatsächlichen Main-Trigger bestätigen.
2. Erst danach in jede neue Annotation den tatsächlichen Manifest-Mergecommit, Manifest-Pfad, SHA-256 des integrierten Manifests, Originalbranch, erwarteten Head, historischen Status und Ruleset-Link aufnehmen.
3. Vor jeder Anlage den unveränderten Branchhead, offene PRs, freien Tagnamen und aktiven Schutz erneut prüfen. Keine bestehenden Tags ersetzen.
4. Nach der Anlage Tagobjekt, vollständige Annotation und aufgelöstes Commitziel vom Server zurücklesen.
5. Erst nach gesicherter Historie und letzter Referenzprüfung die separate Löschfreigabe genau dieser 21 Branchzeiger einholen. Nur eine Sitzung führt je Ref einen SHA-gebundenen Versuch aus; bewegte Heads bleiben stehen.

## Exakte Kandidaten

### 01. `ci/integrity-publication-reviewed-2026-09-24`

- Erwarteter Head: `ecf89ebb7b26e55b4b34a0db7ef4461cfa310df5`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 0.
- Inhalt: Vollständige Commit-Historie über main erhalten; integrierter PR-Arbeitsbranch.
- Historienanker: vollständige Abstammung über `main@c4c8d882d5ed69c5c507a65aba9463639b187631`; kein neuer Tag erforderlich.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 02. `docs/unique-family-register-2026-09-24`

- Erwarteter Head: `146ccf8b7bc1fe7d72d5bf87865abd0a29280056`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 0.
- Inhalt: Vollständige Commit-Historie über main erhalten; integrierter PR-Arbeitsbranch.
- Historienanker: vollständige Abstammung über `main@c4c8d882d5ed69c5c507a65aba9463639b187631`; kein neuer Tag erforderlich.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 03. `chore/root-archive-wave-a`

- Erwarteter Head: `fe8271657a587b0a8985c3d08791410b10115089`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 3.
- Inhalt: Alle sieben verschobenen Audit-/Agenda-Dateien sind bytegleich unter ihren ursprünglichen Root-Pfaden auf main vorhanden. Nur zwei Manifestfassungen und die historische Archiv-README fehlen dort; sie dokumentieren den verworfenen Navigationspilot, keine zusätzlichen Beweisfassungen.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/chore/root-archive-wave-a`.
- Vorgesehenes direktes Commitziel: `fe8271657a587b0a8985c3d08791410b10115089`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 04. `ci/validate-a1-fast-route-2026-09-21`

- Erwarteter Head: `7f2b5722610cbdc1289960345fcbccf3395aa99a`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 1.
- Inhalt: Einzige zusätzliche Fassung ist ein ausdrücklich temporärer Dokumentations-Probe-Text für die CI-Pfadklassifikation; kein mathematischer Inhalt und kein zu integrierender Produktivcode.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/ci/validate-a1-fast-route-2026-09-21`.
- Vorgesehenes direktes Commitziel: `7f2b5722610cbdc1289960345fcbccf3395aa99a`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 05. `ci/validate-legacy-workflow-fast-route-2026-09-21`

- Erwarteter Head: `07170515f10a96f9faea33869ac30a9cd80df1ac`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 1.
- Inhalt: Einzige zusätzliche Fassung ist ein ausdrücklich temporärer Dokumentations-Probe-Text für die CI-Pfadklassifikation; kein mathematischer Inhalt und kein zu integrierender Produktivcode.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/ci/validate-legacy-workflow-fast-route-2026-09-21`.
- Vorgesehenes direktes Commitziel: `07170515f10a96f9faea33869ac30a9cd80df1ac`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 06. `docs/current-front-navigation`

- Erwarteter Head: `9e11f9531ffd9a7dce5714f6e6749a5fea5b1bed`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 3.
- Inhalt: Endtree vollständig auf main. Die einzige dort byteweise fehlende Zwischenfassung unterscheidet sich vom integrierten Nachfolger ausschließlich durch zwei noch nicht präzisierte Quellenzellen für FG-1/FG-TR1. Der Nachfolger trennt Statusbuchung und Beweis-/Auditprovenienz; keine Aussage wird entfernt.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/docs/current-front-navigation`.
- Vorgesehenes direktes Commitziel: `9e11f9531ffd9a7dce5714f6e6749a5fea5b1bed`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 07. `research/sw1-a-fold-reconciliation`

- Erwarteter Head: `ba1cee8fd0507aebd88349daf90160f55755e357`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 7.
- Inhalt: B: AF.5a–AF.5g und AF.27a im Main-Nachfolger explizieren beide inversen Odd-Extensions; AF.9 korrigiert den auf das innere Intervall eingeschränkten Operator. Die ältere implizite Bijektivitätsbegründung wird historisch eingeordnet. Der Checker-Nachfolger ergänzt die inversen Abbildungen; der abschließende Main-Syntaxfix ersetzt ein wörtliches Backslash-n zwischen print-Anweisungen. Keine neue mathematische Prüfung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a-fold-reconciliation`.
- Vorgesehenes direktes Commitziel: `ba1cee8fd0507aebd88349daf90160f55755e357`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 08. `research/sw1-a0-coverage`

- Erwarteter Head: `0f2be5c7e1dd80bb0c85bbc52b5ce01679de7bd6`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 57.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a0-coverage`.
- Vorgesehenes direktes Commitziel: `0f2be5c7e1dd80bb0c85bbc52b5ce01679de7bd6`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 09. `research/sw1-a1-finite-cell`

- Erwarteter Head: `36f68c606b916a2830199826f698d21b14d508bb`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 60.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a1-finite-cell`.
- Vorgesehenes direktes Commitziel: `36f68c606b916a2830199826f698d21b14d508bb`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 10. `research/sw1-a2-a10-reconciliation`

- Erwarteter Head: `8e404a75a8a4f9e68bf87d3cc5556bd1da51a1d7`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 5.
- Inhalt: B: Der Main-Nachfolger ergänzt REC.17a–e und REC.20a–h mit expliziten Kernelbijektionen. W^{-1} bleibt auf Ran(W) beschränkt; auf dem Ambientraum lautet die Projektion WW*, nicht das typwidrige WW^{-1}. Die ältere stärkere/ungenau typisierte Form wird nicht wieder kanonisiert. Der endliche Checker bleibt vom analytischen Hilbertraumsatz getrennt.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a2-a10-reconciliation`.
- Vorgesehenes direktes Commitziel: `8e404a75a8a4f9e68bf87d3cc5556bd1da51a1d7`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 11. `research/sw1-a2-annulus-projection`

- Erwarteter Head: `cfff116954607626f075d16f26c6617e4e9b97d0`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 64.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a2-annulus-projection`.
- Vorgesehenes direktes Commitziel: `cfff116954607626f075d16f26c6617e4e9b97d0`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 12. `research/sw1-a3-free-coordinate-gram`

- Erwarteter Head: `073f6e277d3f7084fbac5d57dcb3ccdeefc94699`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 65.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a3-free-coordinate-gram`.
- Vorgesehenes direktes Commitziel: `073f6e277d3f7084fbac5d57dcb3ccdeefc94699`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 13. `research/sw1-a4-irrational-rotation-nogo`

- Erwarteter Head: `10d2b42266af7f8cd0801db5e8f32b21c6f57004`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 68.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a4-irrational-rotation-nogo`.
- Vorgesehenes direktes Commitziel: `10d2b42266af7f8cd0801db5e8f32b21c6f57004`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 14. `research/sw1-a5-two-sheet-transfer`

- Erwarteter Head: `dc462d3a1a8eeaeb1b304e51c034c8e721d9226c`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 72.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a5-two-sheet-transfer`.
- Vorgesehenes direktes Commitziel: `dc462d3a1a8eeaeb1b304e51c034c8e721d9226c`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 15. `research/sw1-a6-rotation-hole`

- Erwarteter Head: `0ac4dd943301ef7f78a509ad9418f7b3c74fc245`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 75.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a6-rotation-hole`.
- Vorgesehenes direktes Commitziel: `0ac4dd943301ef7f78a509ad9418f7b3c74fc245`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 16. `research/sw1-a7-finite-state-cocycle`

- Erwarteter Head: `8f70d7277c52017761e44cf53e6e47bd2801f8f9`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 79.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a7-finite-state-cocycle`.
- Vorgesehenes direktes Commitziel: `8f70d7277c52017761e44cf53e6e47bd2801f8f9`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 17. `research/sw1-a8-lower-finite-components`

- Erwarteter Head: `92230af645ea2f0549051edb138b32629b0f56da`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 82.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a8-lower-finite-components`.
- Vorgesehenes direktes Commitziel: `92230af645ea2f0549051edb138b32629b0f56da`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 18. `research/sw1-a9-knf-separator`

- Erwarteter Head: `8ccf4795ab8280fb262a9f75ff2a104817bfa812`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 113.
- Inhalt: B: Die einzige neue Audit-Zwischenfassung ist vollständig im Main-Nachfolger enthalten; dieser ergänzt §15.4B zur Nichtexistenz der 78 unmatched-Ziele. Die bereits registrierten A/B-Fassungen werden ausschließlich über identischen Quellpfad und Blob wiederverwendet. Die Main-Historienfassung des staggered-separator-Checkers unterscheidet sich nur durch den inzwischen integrierten Backslash-n-Syntaxfix. A2/A3/A8-Nachfolger und deren Domänengrenzen bleiben maßgeblich.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-a9-knf-separator`.
- Vorgesehenes direktes Commitziel: `8ccf4795ab8280fb262a9f75ff2a104817bfa812`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 19. `research/sw1-delta-descent`

- Erwarteter Head: `d73d3fdf4b1f919fc9526fc09ce206866b472704`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 52.
- Inhalt: Endtree vollständig in Main-Historie; jede ältere Fassung entweder bytegleich auf main/in Main-Historie oder mit exakt gleichem Quellpfad und Blob im integrierten A/B-Register. Keine erneute mathematische Bewertung.
- Bestehender Tag: `refs/tags/archive/2026-09-23/superseded/research-sw1-a10-finite-crossgram`.
- Tagobjekt: `8d0b36e26ecd49f1fe354269a972fc63a6c66962`; aufgelöstes Ziel: `45b1f97d4ee167365e853577ca8f4592429fc1cf`.
- Der Branchhead ist Vorfahr dieses Ziels: 0 branch-exklusive und 88 tagziel-exklusive Commits.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 20. `research/sw1-m1-nd-image-space`

- Erwarteter Head: `52ae23096d1965ba3eb9c7880471b20ff0c6a5b6`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 6.
- Inhalt: B: Der Main-Nachfolger ergänzt IMG.35a–d, IMG.42a–d und IMG.43a–d: P0-Injektivität des zulässigen Outputbilds, Faktorisierung durch U_H und beidseitige Kernelreduktion. Keine Ambient-G-Äquivarianz wird daraus abgeleitet. Historische GREEN-/Owner-Review-Wörter bleiben damalige scoped Angaben. Der Checker ergänzt den Outputtest und enthält den integrierten Syntaxfix.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-m1-nd-image-space`.
- Vorgesehenes direktes Commitziel: `52ae23096d1965ba3eb9c7880471b20ff0c6a5b6`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: Kein blockierender Verbraucher im geprüften Repository-/PR-Umfang gefunden.
- Löschfreigabe: **nicht erteilt**.

### 21. `research/sw1-m1-nd-img2-descriptor`

- Erwarteter Head: `2e193c5b5726ea66cb8f06de1e2cddbf963b887e`.
- Nicht auf der geprüften Main-Basis erreichbare Commits: 7.
- Inhalt: B: Der Main-Nachfolger ersetzt den numerischen Reziprokentest durch exakte endliche Zeilentyp-Prüfungen, entfernt R4II aus den im M1-Simplex erreichbaren Zeilen und trennt den analytischen L2-Multiplikatorbeweis. Keine Erhaltung von B_K durch D_R^{-1} wird behauptet. Der Workflow-Nachfolger nimmt identity_pivot als Eingabe, Hash und Prüfschritt auf.
- Noch anzulegender annotierter Tag: `refs/tags/archive/2026-09-25/content-resolved/research/sw1-m1-nd-img2-descriptor`.
- Vorgesehenes direktes Commitziel: `2e193c5b5726ea66cb8f06de1e2cddbf963b887e`. Anlage und Rückleseprüfung sind offen.
- Verbraucherprüfung: IMG2-Main-Push-Übernahme noch erforderlich.
- Löschfreigabe: **nicht erteilt**.

## Grenzen

Dieses Manifest sichert historische Provenienz und begründet keinen neuen mathematischen Status. KEEP_AUDIT, vorhandene Tags, nicht aufgeführte Branches und O8 bleiben unverändert. Externe Dienste oder nicht eingecheckte lokale Automationen sind nicht Teil des durchgeführten Verbraucherchecks.
