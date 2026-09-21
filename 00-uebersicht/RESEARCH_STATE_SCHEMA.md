# Kanonisches Forschungsregister — Schema 2

`00-uebersicht/RESEARCH_STATE.yaml` ist die einzige operative Statusquelle. Das
Schema trennt bewusst Rollen, die auch dann verschieden bleiben, wenn einzelne
SHA-Werte zeitweise übereinstimmen.

| Feld | Bedeutung |
|---|---|
| `published_baseline` | Rein integrative, gemergte Main-Basis: `branch`, `sha`, `integration_status: MERGED`, `meaning`. Dieses Objekt trägt **keinen** mathematischen Review-Status. |
| `verified_research_snapshot` | Mathematisch geprüfter vollständiger Research-Snapshot: `branch`, `verified_through`, `observed_branch_head`, `review_status`, `head_policy`, `meaning`. `observed_branch_head` ist nur eine spätere beobachtete Abstammungsmarke und keine Verifikation. |
| `registry_sync` | Rein dokumentarischer/operativer Sync-Kandidat: `branch`, `base_sha`, `candidate_head_at_generation`, `integration_status`, `head_policy`, `mathematical_review_changed: false`, `meaning`. Dieses Objekt darf keine mathematische Verifikation erzeugen. |
| `authority_roles` | `definition`, `review_rules`: jeweils `{commit,path,sha256}`; dazu `proof_principle`. |
| `fronts` | Exakt zwei strategische Achsen; aktuell `unified_terminal` und `global_continuation`. |
| `obligations` | Offene Gates mit `id`, `title`, `mathematical_status: OPEN`, `scope`. |
| `results` | Nichtleere Auswahl verwendbarer Survivors mit getrenntem mathematischem, Review-, Integrations- und Reproduktionsstatus. |
| `transport_status` | Explizite Trennung des scoped P11 fixed-pair Strong Terminal von der offenen C1-Horizontkompatibilität. |
| `global_status` | Aggregierte globale Grenzen einschließlich Objekt X, Weil-Positivität und RH. |
| `historical_navigation` | Gepinnte historische Navigation mit bytegleichem Originalkörper. |
| `navigation_exceptions` | Begründete fachliche Ausnahmen von der Navigationsklassifikation. |
| `metadata_policy` | Fester Einführungsanker und Regeln für neue `research/**/PROOF.md`-Pakete. |
| `pending_packages` | Noch nicht promovierte strategische Pakete mit `PENDING_STATUS_REVIEW`. |

## Zentrale Invarianten

1. `published_baseline.sha` bezeichnet Integration, nicht mathematische
   Neuverifikation.
2. `verified_research_snapshot.verified_through` darf nur nach tatsächlicher
   Prüfung eines vollständigen Commits angehoben werden.
3. `verified_research_snapshot.observed_branch_head` muss von
   `verified_through` abstammen, darf aber weiter vorne liegen.
4. `registry_sync.base_sha` muss exakt der veröffentlichten Baseline
   entsprechen.
5. `registry_sync.candidate_head_at_generation` muss von dieser Basis
   abstammen. Das Feld ist ausdrücklich nur ein beobachteter Kandidat-Stand.
6. `registry_sync.mathematical_review_changed` ist zwingend `false`.
   Registry-Syncs dürfen keinen Review- oder Satzstatus selbst erzeugen.
7. Für `MERGED`-Survivors muss der kanonische Beweiscommit Vorfahr der
   `published_baseline` sein. Für noch ungemergte Survivors wird gegen
   `verified_research_snapshot.verified_through` geprüft.
8. Checker-PASS, CI und Merge sind keine mathematische Prüfung.

## Survivor-Felder

Jeder Survivor trägt mindestens `id`, `title`, `scope`, eine nichtleere
`claim`-Liste, `mathematical_status`, `review_status`,
`integration_status`, `strategic_status: REUSABLE_COMPONENT`,
`reproduction_status`, `reproduction_evidence`, `claim_polarity`,
`depends_on`, `supersedes`, `replaced_by`, `canonical_commit`,
`canonical_proof`, `proof_sha256`, `negative_claim_boundary` und eine
nichtleere `does_not_claim`-Liste.

`AUTHOR_DERIVED_NO_GO` und `NEGATIVE_FOR_CANDIDATE_CLASS` müssen genau
gemeinsam auftreten. `SCOPED_GREEN` ist ein Review-Status mit ausdrücklich
begrenztem Scope, keine globale Promotion.

Der ausführbare Validator in `scripts/research_state.py` ist normativ für die
mechanischen Invarianten. Er validiert keine mathematische Wahrheit.
