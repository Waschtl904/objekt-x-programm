# Research-state schema, Version 1

Normative ausführbare Implementierung:
[`scripts/research_state.py`](../scripts/research_state.py),
`validate_structure`, `validate_meta` und `validate`.
Unbekannte oder fehlende Objektfelder werden abgelehnt. Alle Pfade sind sichere
repositoryrelative POSIX-Pfade; Commit-IDs sind 40-stellige kleingeschriebene
Hexwerte, Inhaltsprüfsummen SHA-256 mit 64 Hexstellen.

| Objekt/Feld | Struktur und Bedeutung |
|---|---|
| `schema_version`, `render_version` | Schema 1; positive ganzzahlige Ausgabeversion. |
| `state_date`, `repository` | Datum `YYYY-MM-DD`; dieses Repository. |
| `published_baseline` | `branch`, `sha`, `integration_status`, `meaning`, `mathematical_status`, `review_status`: gepinnte gemergte Main-Basis. |
| `live_frontier` | `branch`, `verified_through`, `integration_status`, `review_status`, `head_policy`: geprüfter ungemergter Snapshot. Head-Policy exakt `VERIFIED_SNAPSHOT_NOT_CURRENT_HEAD`. |
| `authority_roles` | `definition`, `review_rules`: jeweils `{commit,path,sha256}`; dazu `proof_principle` als Text. |
| `fronts` | Exakt zwei strategische Achsen. Kanonisch seit `7998887`: `unified_terminal` und `global_continuation`; der Validator akzeptiert für historische Übergangstests auch die frühere Paarung `transport` und `c1`. Jede Front trägt `id`, `title`, `mathematical_status: OPEN`, `strategic_status: ACTIVE_FRONT`, `target_scope`, nichtleere `obligation_ids`, `uses_results`, `accepted_progress`, `insufficient` und `candidate` (Survivor-ID oder null). |
| `obligations` | Liste aus `id`, `title`, `mathematical_status: OPEN`, `scope`; keine ID darf zugleich Survivor sein. |
| `results` | Nichtleere Auswahl verwendbarer Survivors; vollständige Felder siehe unten. |
| `global_status` | `connected_unit_window_coercivity`, `strong_terminal`, `full_c1_geom`, `object_x`, `global_weil_gram_identity`, `global_weil_positivity`, `rh`. Objekt X `NOT_CONSTRUCTED` und globale Gram-Identität `AUTHOR_DERIVED` schließen sich aus. |
| `historical_navigation` | Liste aus `path`, `as_of`, `content_commit`, `content_sha256`, `note`. Der Originalinhalt wird vor dem Banner aus Git gelesen. |
| `navigation_exceptions` | Liste begründeter fachlicher Ausnahmen: `path`, `role`, `reason`. |
| `metadata_policy` | Fester `enforced_after`-Commit, `discovery: NEW_RESEARCH_PROOF_DIRECTORIES`, `format: JSON_SUBSET_OF_YAML_1_2`. |
| `pending_packages` | Liste aus `id`, `meta_path`, `status: PENDING_STATUS_REVIEW`; sichtbar, jedoch nicht als Survivor promoviert. |

Jeder Survivor trägt:

- `id`, `title`, nichtleeren `scope`, nichtleere `claim`-Liste;
- `mathematical_status`: `AUTHOR_DERIVED` oder `AUTHOR_DERIVED_NO_GO`;
- `review_status`: `EXTERNAL_REVIEW_OPEN` oder
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

Die aggregierten Baseline-/Frontier-Reviewfelder bleiben in Schema 1
`EXTERNAL_REVIEW_OPEN`. Eine spätere externe Gesamtprüfung verlangt eine bewusst
erweiterte, mit Review-Provenienz versehene Aggregationsregel. Einzelresultate
können bereits heute einen eigenen gepinnten Review-Beleg führen.
