# Pflege des kanonischen Forschungsstands

`RESEARCH_STATE.yaml` ist die einzige operative Statusquelle. Die drei Ansichten
`CURRENT_STATE.md`, `NEXT_GATES.md` und `SURVIVOR_REGISTRY.md` sind vollständig
generiert. Beweise, Arbeitsdefinition und Auditregeln bleiben eigene fachliche
Autoritäten; ihre präzisen Belegfassungen sind mit Commit, Pfad und SHA-256
gebunden. Diese Trennung wird durch die CI geprüft, nicht mathematisch bewiesen.

## Einen Stand aktualisieren

1. Den tatsächlichen Branchstand lesen und die relevanten neuen Beweispakete
   samt Scope, Grenzen und dokumentierter Reproduktion prüfen.
2. `verified_through` nur auf den tatsächlich geprüften vollständigen Commit
   setzen. Er darf hinter HEAD liegen; ein späterer Dokumentationscommit macht
   den geprüften mathematischen Snapshot nicht automatisch ungültig. `branch_head_at_generation`
   hält zusätzlich den bei der Registererzeugung beobachteten Dokumentations-Branch-Head
   fest. Dieses Feld beschreibt nur die Dokumentationsabstammung und darf niemals als
   mathematische Verifikation oder Snapshot-Promotion gelesen werden.
3. Wiederverwendbare Resultate, offene Obligationen und die beiden Fronten in
   `RESEARCH_STATE.yaml` aktualisieren. Historische Zwischenzertifikate bleiben
   in ihren Paketen; ersetzte Resultate verlassen die kompakte Auswahl.
4. Die Ansichten erzeugen und die Prüfungen unten ausführen. Bei einer gewollten
   Änderung des Ausgabeformats `render_version` in der Statusdatei erhöhen.
5. Fachliche Statusänderung und zugehörige generierte Ansichten gemeinsam
   reviewen. Ein Checker-PASS oder Merge ändert keinen mathematischen Status.

Python 3.10 oder neuer und Git mit vollständiger Historie genügen; keine
zusätzlichen Python-Pakete und kein Netzwerkzugriff sind für die Checks nötig.
Ausnahme ist die ausdrücklich gewählte Remote-CI-Prüfung
`--check-integration-ci`; der Registry-Workflow führt sie zusätzlich aus.
Die `.yaml`-Dateien verwenden **die JSON-Teilmenge von YAML 1.2**. Das ist eine
bewusste Einschränkung: UTF-8, doppelte Anführungszeichen, keine Kommentare,
keine doppelten Schlüssel und keine nichtendlichen Zahlen. Dadurch benötigt
der Parser keine neue Abhängigkeit.

Vom Repository-Stamm aus:

```text
python scripts/generate_research_state.py
python scripts/generate_research_state.py --check
python scripts/check_research_state.py
python scripts/check_research_state.py --check-integration-ci
python -m unittest discover -s tests -p test_research_state.py -v
python scripts/validate_active_front.py
```

Zusätzlich prüft `check_research_state.py --base-ref <vollständiger-Commit-SHA>`
den Vergleich zum Basisstand: generiertes Markdown darf nicht ohne Änderung
der Statusdatei geändert werden, und der Metadaten-Einführungsanker bleibt
unverändert. Die neue CI verwendet bei PRs deren Basis, bei Pushes `before`.

Der bisherige Frontvalidator bleibt unverändert und prüft weiterhin den
historischen PR-Stack. Sein alter Ausgabetext ist kein Nachweis, dass die alte
Front operativ aktuell ist. Der neue Workflow ergänzt diesen Check ausdrücklich.

## Integration beobachten, historische Anker erhalten

`published_baseline.sha`, `live_frontier.verified_through` und
`live_frontier.branch_head_at_generation` haben unterschiedliche historische
Bedeutungen. Weder ein Merge noch ein CI-PASS setzt diese Felder automatisch auf
den späteren Main-Head. Auch die Resultat-Integrationseinträge bleiben relativ
zur eingefrorenen publizierten Basis zu lesen.

Für die zusätzliche Git-/CI-Ebene dient seit Schema 2
`current_integration_observation`. Sie erfasst Beobachtungsdatum, Main-Commit,
integrierten Forschungsbranch samt Head, Reconciliation-Merge sowie den
Research-State-CI-Lauf mit Versuch, Commitbindung, URL und Ergebnis. Die Feldnamen
und Prüfungen sind im [Schema](RESEARCH_STATE_SCHEMA.md) erklärt. Diese Beobachtung
ist selbst ein datierter Snapshot und keine Behauptung, dass ein Remote-HEAD
dauerhaft unverändert bleibt.

Bei einem reinen Integrations-Sync:

1. Main- und Forschungsbranch-Head sowie den erfolgreichen CI-Laufversuch lesen.
2. Nur die Beobachtung und das Registerdatum aktualisieren; bei einer geänderten
   Darstellung zusätzlich `render_version` erhöhen. Die eingefrorenen Anker,
   fachlichen Status und Integrationseinträge unverändert lassen.
3. Alle drei Ansichten generieren und die Offlineprüfungen ausführen.
4. Den aufgezeichneten CI-Lauf mit `--check-integration-ci` gegen GitHub prüfen
   und den vollständigen Registry-Workflow auf dem neuen Commit bestehen lassen.

Der Onlinecheck benötigt GitHub-Zugriff, optional `GH_TOKEN`, im Workflow mit
`contents: read` und `actions: read`. Er bindet den aufgezeichneten Laufversuch
statt einen späteren Wiederholungslauf stillschweigend zu übernehmen. Ein
Abfragefehler bleibt ein Prüfungsfehler. Die Offlineprüfungen benötigen weiterhin
weder Zugangsdaten noch Netzwerk.

## Zukünftige Pakete und META.yaml

Es gibt keine Rückrüstung der eingefrorenen Beweispakete. Der feste
Einführungsanker steht unter `metadata_policy.enforced_after`. Ein danach neu
hinzukommendes Verzeichnis `research/**/PROOF.md` benötigt `META.yaml`. Diese
mechanische Erkennung verlangt für ein rein lokales Paket lediglich die explizite
Deklaration `local_only: true`; sie stuft es nicht zum strategischen Fortschritt
hoch. Strategische Pakete deklarieren mindestens eines von `closes`, `opens`
oder `supersedes`. Ein strategischer Forschungsbeitrag ist in diesem Schema als
solches Beweispaket anzulegen; beiläufige Notizen ohne `PROOF.md` werden vom
Validator nicht semantisch als strategisch erkannt.

Das [Metadatenschema](../scripts/schemas/META.schema.json) und die
[Vorlage](../scripts/schemas/META.example.json) geben die Felder vor. Ein No-Go
muss `kind: NO_GO`, `AUTHOR_DERIVED_NO_GO`,
`NEGATIVE_FOR_CANDIDATE_CLASS`, einen konkreten Scope und eine ausdrückliche
Kandidatengrenze tragen. Ein leeres `does_not_claim` ist unzulässig.

Der erste Paketcommit kann seinen eigenen SHA nicht in `META.yaml` enthalten.
Deshalb bindet META den aktuellen `PROOF.md`-Inhalt per SHA-256. Der Ablauf ist:

1. Neues Paket und META gemeinsam erstellen. Neue Obligationen beziehungsweise
   bekannte Ziel-IDs im Register deklarieren. Effekte und Abhängigkeiten dürfen
   nicht auf unbenannte IDs zeigen.
2. Das Paket zunächst unter `pending_packages` mit `id`, `meta_path` und
   `status: PENDING_STATUS_REVIEW` sichtbar machen. `verified_through` bleibt
   dabei der vorherige geprüfte Stand. Ein deklariertes `closes` ist in diesem
   Stadium eine Behauptung des Pakets, keine automatische Gate-Promotion.
3. Nach Veröffentlichung und Statusprüfung das wiederverwendbare Resultat mit
   dem tatsächlichen Commit und seinen Belegen registrieren, den geprüften
   Snapshot gegebenenfalls anheben und den Pending-Eintrag entfernen.

Ein ausdrücklich `local_only` deklariertes Paket benötigt keinen Pending-Eintrag
und keine Änderung der aktiven Fronten. Sein META bleibt als lokale Einordnung
prüfbar; es darf keine strategischen Gate-Effekte deklarieren.

`META.yaml` ist kein Ersatz für vollständige Inputs, Beweise oder Paketchecker.
`reproduction_status: RECORDED_PACKAGE_CHECKS` bedeutet im Survivorregister:
Ein unveränderliches Prüflog ist verlinkt. Es behauptet keinen erneuten Lauf
durch diesen Navigationsvalidator. Externe Prüfung und Integration sind eigene
Felder. Externe Prüfung erfordert eine zusätzliche gepinnte Review-Provenienz.

## Historische Navigation erhalten

Die unter `historical_navigation` aufgeführten Dateien erhalten nur den
standardisierten Banner. Der bisherige Inhalt bleibt bytegleich mit dem
angegebenen Commit; SHA-256 und vollständiger Bytevergleich sichern dies ab.
Bei YAML besteht der Banner aus Kommentaren. Keine Beweise werden verschoben,
gelöscht oder umgeschrieben. Die Arbeitsdefinition bleibt ausdrücklich eine
Definitionsautorität und erhält keinen pauschalen Historisierungsbanner.

Zusätzlich kontrolliert der Validator Dateinamen mit `CURRENT`, `ACTIVE` oder
`AKTUELL` im Repository-Stamm, in `00-uebersicht/` und `00-grundlegung/`.
Eine solche Datei muss generiert, historisiert oder als fachliche Ausnahme
begründet sein. Datierte Archivtexte und beliebige andere Dateinamen werden
nicht automatisch auf alle sprachlichen Aktualitätsansprüche geprüft.

## Reichweite der Kontrolle

Der Validator prüft Schema, IDs, Abhängigkeiten, erklärte Statuskonsistenz,
Belegpfade und Hashes, Git-Abstammung der Integrationsangaben, generierte Bytes,
historische Originale und neue Paketmetadaten. Er beweist keine Mathematik und
versteht nicht jede denkbare Bedeutungsinkonsistenz freier Texte. `MERGED`
bezieht sich auf die erklärte gepinnte Main-Basis, nicht auf einen vom Check
heimlich aus dem Netz abgefragten späteren Stand.

Die genaue Struktur ist in [RESEARCH_STATE_SCHEMA.md](RESEARCH_STATE_SCHEMA.md)
beschrieben; der ausführbare Validator ist die normative Schemaimplementierung.
