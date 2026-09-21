# Research-state schema, Version 2

Normative ausführbare Implementierung:
[`scripts/research_state.py`](../scripts/research_state.py),
`validate_structure`, `validate_meta` und `validate`.
Unbekannte oder fehlende Objektfelder werden abgelehnt. Alle Pfade sind sichere
repositoryrelative POSIX-Pfade; Commit-IDs sind 40-stellige kleingeschriebene
Hexwerte, Inhaltsprüfsummen SHA-256 mit 64 Hexstellen.

| Objekt/Feld | Struktur und Bedeutung |
|---|---|
| `schema_version`, `render_version` | Schema 2; positive ganzzahlige Ausgabeversion. |
| `state_date`, `repository` | Datum `YYYY-MM-DD`; dieses Repository. |
| `published_baseline` | `branch`, `sha`, `integration_status`, `meaning`, `mathematical_status`, `review_status`: gepinnte gemergte Main-Basis. |
| `live_frontier` | `branch`, `branch_head_at_generation`, `verified_through`, `integration_status`, `review_status`, `head_policy`: geprüfter historischer Snapshot mit Integration relativ zur eingefrorenen Basis plus der damals beobachtete Dokumentations-Branch-Head. `branch_head_at_generation` ist nur eine dokumentarische Abstammungsmarke und keine mathematische Verifikation. Head-Policy exakt `VERIFIED_SNAPSHOT_NOT_CURRENT_HEAD`. |
| `current_integration_observation` | Datierte Git-/CI-Beobachtung unabhängig von Baseline, Verifikationsanker und historischen Integrationseinträgen; genaue Felder und Prüfungen unten. |
| `authority_roles` | `definition`, `review_rules`: jeweils `{commit,path,sha256}`; dazu `proof_principle` als Text. |
| `fronts` | Exakt zwei strategische Achsen. Kanonisch seit `7998887`: `unified_terminal` und `global_continuation`; der Validator akzeptiert für historische Übergangstests auch die frühere Paarung `transport` und `c1`. Jede Front trägt `id`, `title`, `mathematical_status: OPEN`, `strategic_status: ACTIVE_FRONT`, `target_scope`, nichtleere `obligation_ids`, `uses_results`, `accepted_progress`, `insufficient` und `candidate` (Survivor-ID oder null). |
| `obligations` | Liste aus `id`, `title`, `mathematical_status: OPEN`, `scope`; keine ID darf zugleich Survivor sein. |
| `results` | Nichtleere Auswahl verwendbarer Survivors; vollständige Felder siehe unten. |
| `global_status` | `connected_unit_window_coercivity`, `full_c1_geom`, `object_x`, `global_weil_gram_identity`, `global_weil_positivity`, `rh`. Objekt X `NOT_CONSTRUCTED` und globale Gram-Identität `AUTHOR_DERIVED` schließen sich aus. |
| `historical_navigation` | Liste aus `path`, `as_of`, `content_commit`, `content_sha256`, `note`. Der Originalinhalt wird vor dem Banner aus Git gelesen. |
| `navigation_exceptions` | Liste begründeter fachlicher Ausnahmen: `path`, `role`, `reason`. |
| `metadata_policy` | Fester `enforced_after`-Commit, `discovery: NEW_RESEARCH_PROOF_DIRECTORIES`, `format: JSON_SUBSET_OF_YAML_1_2`. |
| `pending_packages` | Liste aus `id`, `meta_path`, `status: PENDING_STATUS_REVIEW`; sichtbar, jedoch nicht als Survivor promoviert. |

## Separate Integrationsbeobachtung

Schema 2 ergänzt genau diese Ebene. Die bestehenden Snapshot- und Resultatfelder
werden durch die Migration nicht umgedeutet. `render_version: 3` kennzeichnet die
explizite Trennung in den generierten Ansichten.

Pflichtfelder von `current_integration_observation`:

- `observed_at`: gültiges Datum `YYYY-MM-DD`, nicht nach `state_date`;
- `main_sha`: vollständiger beobachteter Main-Commit;
- `integrated_research_branch`, `integrated_research_head`: beobachteter Branchname
  und vollständiger Head-Commit; der Commit muss Vorfahr von `main_sha` sein;
- `reconciliation_merge`: vollständiger Merge-Commit mit mindestens zwei Eltern,
  ebenfalls in `main_sha` enthalten;
- `ci_run_id`, `ci_run_attempt`: positive ganze Zahlen, keine booleschen Werte;
- `ci_head_sha`: exakt `main_sha`;
- `ci_url`: exakt `https://github.com/Waschtl904/objekt-x-programm/actions/runs/<ci_run_id>`;
- `ci_conclusion`: exakt `success`, entsprechend der GitHub-API;
- `mathematical_status_change`: exakt `false`; die Beobachtung ist keine Promotion.

Der Offlinevalidator prüft diese Struktur, die Commitexistenz, die angegebene
Abstammung und dass `main_sha` im geprüften Checkout enthalten ist. Er fragt weder
einen aktuellen Remote-HEAD ab noch leitet er neue Verifikations- oder Reviewstatus
aus dem Merge ab. Der gespeicherte Branchname ist eine historische Beobachtung;
die spätere Existenz des Remote-Branches ist keine Validierungsbedingung.

Mit `--check-integration-ci` wird zusätzlich der genaue GitHub-Laufversuch abgefragt.
Run-ID, Versuch, `head_sha`, Branch `main`, Ereignis `push`, Status `completed`,
Ergebnis `success`, URL und der Workflowpfad
`.github/workflows/validate-research-state.yml` müssen übereinstimmen. Der Lauf
muss spätestens am Beobachtungstag abgeschlossen worden sein. Fehler bei der
Abfrage sind kein PASS. Der Registry-Workflow führt diesen zusätzlichen Schritt
mit ausschließlich lesenden GitHub-Berechtigungen aus. Ohne diesen Schalter
bestätigt ein lokaler PASS nur die interne CI-Bindung, nicht den Remote-Lauf.

Der neue Workflow validiert den Synchronisationscommit, während die Beobachtung
weiterhin den früheren Main-Lauf bindet. Beide CI-Aussagen sind verschieden; es
wird keine Selbstreferenz auf den noch nicht erzeugten Commit verlangt.

## Survivor-Felder

Jeder Survivor trägt:

- `id`, `title`, nichtleeren `scope`, nichtleere `claim`-Liste;
- `mathematical_status`: `AUTHOR_DERIVED` oder `AUTHOR_DERIVED_NO_GO`;
- `review_status`: `EXTERNAL_REVIEW_OPEN`, `SCOPED_GREEN` oder
  `EXTERNALLY_REVIEWED_WITH_PROVENANCE`, letzteres mit zusätzlichem
  `external_review_evidence: {commit,path,sha256}`;
- `integration_status`: `MERGED` oder `RESEARCH_BRANCH_UNMERGED`;
- `strategic_status: REUSABLE_COMPONENT`;
- `reproduction_status`: `RECORDED_PACKAGE_CHECKS`, `ANALYTIC_ONLY` oder
  `NOT_APPLICABLE`, dazu `reproduction_evidence` als Liste gepinnter Belege;
  genau bei `RECORDED_PACKAGE_CHECKS` ist diese Liste nichtleer;
- `claim_polarity`: `POSITIVE_RESULT`, `CONSTRUCTION`,
  `EQUIVALENCE_OR_REDUCTION` oder `NEGATIVE_FOR_CANDIDATE_CLASS`;
- `depends_on`, `supersedes`, `replaced_by`: Listen bekannter IDs;
  Abhängigkeiten müssen azyklisch sein. Ein ersetzter Eintrag wird aus der
  Survivor-Auswahl entfernt, daher ist `replaced_by` dort leer;
- `canonical_commit`, `canonical_proof`, `proof_sha256`;
- nichtleere `negative_claim_boundary` und nichtleere `does_not_claim`-Liste.

`AUTHOR_DERIVED_NO_GO` und `NEGATIVE_FOR_CANDIDATE_CLASS` müssen genau gemeinsam
auftreten. `scope` benennt die ausgeschlossene Klasse und
`negative_claim_boundary` deren Grenze. Bei anderen Resultaten erläutert das
Grenzfeld insbesondere, dass kein Negativitätsbefund behauptet wird.

Die Beziehungen nennen ausgewählte Register-Abhängigkeiten; die vollständige
mathematische Eingabeliste bleibt im Beweispaket. Replaced-/Supersession-Historie
bleibt über Git und die eingefrorenen Pakete zugänglich; dieses kompakte Register
ist kein zweites Vollarchiv.

Die aggregierten Baseline-/Frontier-Reviewfelder bleiben in Schema 2
`EXTERNAL_REVIEW_OPEN`. Eine spätere externe Gesamtprüfung verlangt eine bewusst
erweiterte, mit Review-Provenienz versehene Aggregationsregel. Einzelresultate
können bereits heute einen eigenen gepinnten Review-Beleg führen.
