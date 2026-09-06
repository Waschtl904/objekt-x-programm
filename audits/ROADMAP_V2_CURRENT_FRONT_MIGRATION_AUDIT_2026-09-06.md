# Roadmap v2 — CURRENT-FRONT migration / loss audit

**Date:** 2026-09-06  
**Scope:** governance/navigation only  
**Compared:** PR #59 base `CURRENT-FRONT.md` versus the consolidated v2 current-front layer  
**Mathematical status effect:** none

---

## 0. Purpose

PR #59 deliberately shortens `CURRENT-FRONT.md`. This audit checks that the shortening does not silently delete information that still has to remain **operative**.

The test is not “did every old line survive?” The old file had accumulated historical theorem ledgers, candidate inventories, old front descriptions, review vocabulary and detailed finite-level provenance that already belong to canonical papers/audits or `ACTIVE_THEOREM_REGISTRY.md`.

The correct question is:

> Did any information needed to understand or safely continue the **current R43 / Strong-Terminal front** disappear without a canonical replacement pointer?

Verdict below: **no such loss found after the v2.1.1 correction pass.**

---

## 1. Old header / GC-AC-era front

The pre-v2 header contained:

- an older main/head ledger;
- the `research/r43-gcac-hardening` branch;
- the GC-AC candidate status;
- the old primary B-FLAGDYN formulation;
- detailed review provenance tied to old heads.

### Classification

**Superseded operational state.**

The current front is now the post-PR54 structured-COND stack. Volatile stack data live only in `00-uebersicht/ACTIVE_FRONT.yaml`; old head/review provenance remains in Git history, the Registry and the canonical R43 audits.

No old GC-AC status is promoted, negated or rewritten by this migration.

---

## 2. Old finite-level / M1-ND / SW1 blocks

The pre-v2 file contained many lines on:

- M1-ND-SMALLR;
- the explicit Small-R witness;
- M1-ND-SALVAGE;
- PR #49;
- P12 restricted-tail injectivity;
- HT-A1/A2/A3/A4a;
- FG-1 / FG-TR1 / CG-FG1;
- SW1-KNF, SW1-BL7, SW1-2TP, SW1-AWI;
- PR #10;
- A2–A10 / C1B2A / M1-FULL details.

### Classification

**Historical/adjacent status inventory, not current R43 head-layer material.**

These results remain in:

- `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`;
- their canonical audit/paper/promotion files;
- Git history;
- older roadmap/status snapshots.

The current navigation layer retains the only fact that is presently needed for research prioritization: the universal positive finite-level/SW1 route is negatively closed in its booked scope and salvage is not the active default.

No theorem-level finite result is deleted or demoted by shortening `CURRENT-FRONT.md`.

---

## 3. R38–R42 and the fixed-normal Strong-Terminal gate

The pre-v2 file contained the individual R38–R42 summaries and the reduction to

`Re<epsilon_R,K_{R,S}^{T,U}epsilon_R> -> 1`.

### Classification

**Operative — retained.**

The consolidated current front retains:

- fixed `0<R<S` scope;
- the fixed-normal observable;
- the target limit;
- exact Registry governance wording `FROZEN — independently verified AI-GREEN`;
- the Registry firewall that this wording is not automatically one of the formal independent-GREEN subtypes;
- R43 OPEN.

Individual R38–R42 theorem summaries remain in the Registry and their canonical audits instead of being duplicated again in the head layer.

---

## 4. B-FLAGTIGHT / B-FLAGDYN / B-SIGN content

The pre-v2 file contained:

- exact Tightness gate `lim_m limsup_U q_m(U)=0`;
- fixed-source observable `Q_{m,U}=W_U^*P_mW_U`;
- the moving-range cocycle firewall;
- the C2 horizon-gauge formulation;
- B-FLAGDYN;
- B-SIGN/B-ORIENT;
- `Strong Terminal <=> liminf L > -1` under B-TIGHT.

### Classification

**Operative — core retained; detailed old derivation delegated.**

The new `CURRENT-FRONT.md` retains:

- `Q_{m,U}` and `q_m(U)`;
- exact B-FLAGTIGHT equivalence;
- B-FLAGDYN as terminal variation of the fixed-source observable;
- B-FLAGMOD/B-FLAGPHASE only as a stronger sufficient route;
- B-SIGN/B-ORIENT;
- the sharp post-tightness `liminf L>-1` criterion.

The older detailed moving-range-cocycle and C2 horizon-gauge derivation remains in the canonical R43 FlagDyn/O1 audits and Git history. It is not rewritten as a new theorem here.

The current COND direct route is now explicitly separated from the stronger B-METINC operator route, which was not yet represented correctly in the old front.

---

## 5. “Not currently worked on” / P12 / Round-29 blocks

The pre-v2 file explicitly listed several non-priority fronts and explained why Round 29 / M68 was not needed for the then-current SW1 route.

### Classification

**Historical prioritization.**

The active front has moved from SW1 to R43. The new head layer therefore no longer needs a multi-paragraph proof of why Round 29 is not needed for SW1.

The new current front retains the strategic rule that finite-level salvage, R37/G4c and final Object-X work are not automatically the default while R43/B remains productive.

P12 scope and Round-29 provenance remain in their canonical files and Registry entries.

---

## 6. Reading order

The pre-v2 file contained a mandatory reading order.

### Classification

**Operative — retained and improved.**

The new order explicitly inserts `ACTIVE_FRONT.yaml` and the canonical roadmap before the Registry/canonical source layers, while preserving the rule that historical files are consulted only for a named provenance/error question.

---

## 7. Status nomenclature / epistemic authority

The pre-v2 file duplicated the Registry definitions of:

- AI-GREEN;
- independent GREEN subtypes;
- `✓[M]`;
- human-review guidance.

### Classification

**Must not be duplicated in CURRENT-FRONT.**

The authoritative vocabulary is `ACTIVE_THEOREM_REGISTRY.md`. Keeping a second full copy in `CURRENT-FRONT.md` creates exactly the drift risk that Roadmap v2 is designed to remove.

The new current front therefore imports the exact R38–R42 governance string and points to the Registry for the definitions.

---

## 8. Five-point merge rule

The pre-v2 file contained the sequence:

`Merge -> Main-Check -> Registry -> Current Front -> next mathematics`.

### Classification

**Operative — retained and extended.**

The new front keeps the merge/rollback sequence and inserts `ACTIVE_FRONT` as the volatile metadata layer.

The exact heads themselves are no longer copied into the front.

---

## 9. Old giant short-status theorem table

The pre-v2 file ended with a large finite-level status table.

### Classification

**Registry material — intentionally removed from CURRENT-FRONT.**

Its canonical replacement is `ACTIVE_THEOREM_REGISTRY.md` plus theorem sources.

Keeping it in both places would create two status ledgers and violate the v2 authority split.

---

## 10. New information added by the v2 front

The consolidation does more than delete old material. It adds information needed by the present front:

1. the active Draft stack is represented by one volatile source, `ACTIVE_FRONT.yaml`;
2. parent heads are pinned explicitly;
3. Draft-source theorem IDs are distinguished from Registry entries;
4. the exact geometric-mean resolvent transport is surfaced;
5. the Good-Normal reduction to transported collar mass plus the two hard diagonal channels is surfaced;
6. structured direct and global operator routes are separated;
7. the direct COND-to-B-FLAGDYN composition is explicitly an OPEN bridge;
8. unknown decay quantifiers remain unresolved;
9. Object-X definition is separated from X-candidate and X-realization status;
10. R37/G4c has no edge to the X route while its dependency is unresolved.

---

## 11. Migration verdict

```text
CURRENT-FRONT consolidation: PASS as navigation migration
```

Subject to the ordinary PR #59 review firewall, the shortened front loses no information that must remain uniquely operative there.

Removed material is one of:

- historical/superseded front state;
- theorem/review inventory owned by the Registry;
- detailed mathematics owned by canonical audits/papers;
- non-current finite-level prioritization.

The current R43/Strong-Terminal gates and essential firewalls remain visible.

**No mathematical promotion follows from this audit.**
