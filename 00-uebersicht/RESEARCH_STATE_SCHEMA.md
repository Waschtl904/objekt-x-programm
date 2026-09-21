# Research-state schema, Version 2

Normative ausführbare Implementierung:
[`scripts/research_state.py`](../scripts/research_state.py).

Schema 2 trennt vier unterschiedliche Rollen und zusätzlich die gepinnte
Integrations-/CI-Provenienz. Keine Rolle darf stillschweigend als eine andere
gelesen werden.

| Objekt/Feld | Struktur und Bedeutung |
|---|---|
| `published_baseline` | Aktuelle gepinnte gemergte Main-Basis: `branch`, `sha`, `integration_status: MERGED`, `meaning`. Rein integrativ; kein mathematischer Review-Status. |
| `verified_research_snapshot` | Mathematisch geprüfter vollständiger Snapshot: `branch`, `verified_through`, `observed_branch_head`, `review_status`, `head_policy`, `meaning`. Der beobachtete Branch-Head ist keine zusätzliche Verifikation. |
| `registry_sync` | Ungemergter Registry-/Dokumentationskandidat: `branch`, `base_sha`, `candidate_head_at_generation`, `integration_status`, `head_policy`, `mathematical_review_changed: false`, `meaning`. |
| `current_integration_observation` | Datierte zusätzliche Git-/CI-Provenienz für einen beobachteten Main-Stand; keine mathematische Promotion. |
| `authority_roles` | Definition, Reviewregeln und Proof-Principle mit gepinnter Provenienz. |
| `fronts` | Exakt zwei aktive strategische Fronten. |
| `obligations` | Offene Gates. |
| `results` | Verwendbare Survivors mit getrennten mathematischen, Review-, Integrations- und Reproduktionsstatus. |
| `transport_status` | Scoped P11 fixed-pair Strong Terminal getrennt von offener C1-Horizontkompatibilität. |
| `global_status` | Globale Grenzen einschließlich Objekt X, Weil-Positivität und RH. |

## Kerninvarianten

1. `published_baseline.sha` bezeichnet den aktuellen gepinnten integrierten
   Main-Stand und erzeugt keine mathematische Neuverifikation.
2. `verified_research_snapshot.verified_through` darf nur nach tatsächlicher
   mathematischer Prüfung eines vollständigen Commits angehoben werden.
3. `observed_branch_head` darf später liegen, muss von `verified_through`
   abstammen und ist ausdrücklich keine Verifikation.
4. `registry_sync.base_sha` muss exakt `published_baseline.sha` sein.
5. `registry_sync.candidate_head_at_generation` muss von dieser Basis
   abstammen; es ist nur ein beobachteter Kandidat-Stand.
6. `registry_sync.mathematical_review_changed` ist zwingend `false`.
7. `current_integration_observation` darf nur erfolgreiche, commitgebundene
   Integrations-/CI-Provenienz speichern und hat
   `mathematical_status_change: false`.
8. Ein `MERGED`-Survivor muss mit seinem kanonischen Beweiscommit Vorfahr der
   `published_baseline` sein. Ein noch ungemergter Survivor wird gegen den
   `verified_research_snapshot` geprüft.
9. CI, Merge und Registry-Sync sind keine unabhängige mathematische Prüfung.

## current_integration_observation

Pflichtfelder bleiben:

- `observed_at`;
- `main_sha`;
- `integrated_research_branch`, `integrated_research_head`;
- `reconciliation_merge`;
- `ci_run_id`, `ci_run_attempt`, `ci_head_sha`, `ci_url`,
  `ci_conclusion`;
- `mathematical_status_change: false`.

Der Offlinevalidator prüft Commitexistenz und Abstammung. Mit
`--check-integration-ci` wird zusätzlich genau der aufgezeichnete GitHub-Lauf
gegen Run-ID, Versuch, Commit, Branch, Ereignis, Workflowpfad und Ergebnis
gebunden. Diese Onlineprüfung bleibt von mathematischer Verifikation getrennt.

## Survivor-Felder

Jeder Survivor trägt insbesondere `mathematical_status`, `review_status`,
`integration_status`, Beweis-/Reproduktionsprovenienz, Scope,
`negative_claim_boundary` und `does_not_claim`.

`AUTHOR_DERIVED_NO_GO` und `NEGATIVE_FOR_CANDIDATE_CLASS` müssen gemeinsam
auftreten. `SCOPED_GREEN` ist ein begrenzter Review-Status und keine globale
Promotion.

Der ausführbare Validator ist normativ für mechanische Invarianten, nicht für
mathematische Wahrheit.
