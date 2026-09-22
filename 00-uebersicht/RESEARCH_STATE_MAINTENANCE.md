# Pflege des kanonischen Forschungsstands

`RESEARCH_STATE.yaml` ist die einzige operative Statusquelle. Die generierten
Ansichten sind Navigation, keine mathematische Promotion.

Der [gemeinsame Abnahmeablauf](../CONTRIBUTING.md) trennt Mathematik,
Infrastruktur und Dokumentation nach der tatsächlichen Auswirkung. Die
folgenden Schritte gelten für Registry-Pflege; sie machen eine unveränderte
README- oder Linkkorrektur nicht zu einem mathematischen Re-Audit.

## Rollen strikt getrennt halten

1. `published_baseline`: zuletzt ausdrücklich registrierter und gepinnter
   gemergter Main-Stand. Nur Integration; nicht notwendigerweise identisch mit
   dem aktuellen Git-Head.
2. `verified_research_snapshot`: letzter tatsächlich mathematisch geprüfter
   vollständiger Research-Commit. Ein Merge, Dokumentationscommit oder CI-PASS
   hebt `verified_through` nicht automatisch an.
3. `verified_research_snapshot.observed_branch_head`: später beobachteter
   Branch-Head; nur Abstammungsinformation.
4. `registry_sync`: ungemergter Registry-/Dokumentationskandidat gegen die
   gepinnte Baseline. `mathematical_review_changed` bleibt zwingend `false`.
5. `current_integration_observation`: zusätzliche datierte Git-/CI-Provenienz;
   ebenfalls keine mathematische Verifikation.

## Einen Stand aktualisieren

1. Main, Registry und relevante Beweispakete lesen.
2. `published_baseline` nur nach tatsächlicher Git-Integration anheben.
3. Survivor-`integration_status` relativ zu dieser Baseline pflegen; Beweis-,
   Review- und mathematische Status bleiben orthogonal.
4. `verified_research_snapshot.verified_through` nur mit eigenem
   mathematischem Prüfgrund anheben.
5. Reine Sync-Arbeit unter `registry_sync` dokumentieren.
6. Bei Bedarf eine commitgebundene `current_integration_observation` mit
   `mathematical_status_change: false` ergänzen.
7. Generierte Views erneuern und alle Validatoren ausführen.

Vom Repository-Stamm:

```text
python scripts/generate_research_state.py
python scripts/generate_research_state.py --check
python scripts/check_research_state.py
python scripts/check_research_state.py --check-integration-ci
python -m unittest discover -s tests -p test_research_state.py -v
python scripts/validate_active_front.py
```

Die Remote-CI-Prüfung benötigt GitHub-Zugriff und bindet ausschließlich den
aufgezeichneten Integrationslauf. Sie beweist keine Mathematik.

Ein späterer Dokumentations- oder Infrastrukturmerge erzwingt für sich allein
keinen neuen Registry-Snapshot. Der aktuelle Git-Head wird im Merge-Abgleich
festgestellt; die gepinnten Registry-Felder dokumentieren weiterhin ihren
jeweils ausdrücklich angegebenen Stand. Werden Integrationsangaben bewusst
aktualisiert, gelten die obigen Schritte einschließlich Commitbindung und
Regeneration. Ein bloßes Gleichziehen aller SHA-Felder ist keine Synchronisation.

## Neue Forschungspakete

Neue `research/**/PROOF.md`-Verzeichnisse nach dem Metadatenanker benötigen
`META.yaml`. Strategische Pakete werden zunächst als
`PENDING_STATUS_REVIEW` sichtbar gemacht; lokale Pakete dürfen
`local_only: true` verwenden. META bindet den aktuellen `PROOF.md`-Inhalt
per SHA-256 und darf keinen Review- oder Integrationsstatus selbst promoten.

## Historische Navigation

Historische Navigationsdateien behalten ihren Originalkörper bytegleich hinter
dem standardisierten Banner. Alte Beweisdateien werden nicht umgeschrieben.

Die aktive Repository-`README.md` ist davon ausgenommen: Ihre Rolle
`ACTIVE_REPOSITORY_ENTRY` steht ausdrücklich unter `navigation_exceptions`.
Sie darf als Einstieg bearbeitet werden und verweist für aktuelle Statusangaben
auf das Register und dessen generierte Ansichten. Die frühere README-Fassung
bleibt über den in der Ausnahme dokumentierten Commit und SHA-256 erhalten.
Diese Ausnahme lockert weder die übrigen historischen Bytebindungen noch
Beweisanker, Review-Status oder mathematische Claims.

## Reichweite des Validators

Geprüft werden Schema, IDs, Abhängigkeiten, erklärte Statuskonsistenz,
Belegpfade/-hashes, Git-Abstammung, generierte Bytes, historische Originale,
META-Lifecycle sowie optional die aufgezeichnete Integrations-CI.

Nicht geprüft wird mathematische Wahrheit. Checker-PASS, CI und Merge ersetzen
keinen analytischen Audit.
