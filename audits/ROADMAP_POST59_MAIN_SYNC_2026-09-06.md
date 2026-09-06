# PR #59 post-merge main sync audit

**Date:** 2026-09-06  
**Scope:** governance/navigation only; no mathematical promotion.

## 1. Verified merge

PR #59 was squash-merged only after destructive review round 2 returned GREEN on the exact reviewed head.

The merge was performed with an expected-head guard, so GitHub would have rejected the operation had the reviewed head moved.

Post-merge live verification confirmed that `main` advanced to the GitHub-created merge/squash commit and that its parent is the pre-PR-59 main commit.

No PR #55–#58 mathematics was modified by this merge.

## 2. Registry check

`ACTIVE_THEOREM_REGISTRY.md` was checked after the merge.

Result:

- PR #59 is a governance/navigation refactor;
- it creates no theorem booking, review promotion, freeze, Object-X realization, or RH claim;
- therefore no theorem/review-status row requires promotion or mutation as part of this post-merge sync;
- the local R43-COND IDs from PR #55–#58 remain Draft-source IDs until their own exact promotion/merge workflow.

Accordingly the status-critical Registry is intentionally left mathematically unchanged.

## 3. Main-SHA self-reference issue

The first version of `ACTIVE_FRONT.yaml` stored a field of the form

```text
main.sha = <current main commit>
```

and the validator required the root Draft parent to equal that value.

After PR #59 merged, two facts became simultaneously true:

1. live `main` advanced because of a governance-only commit;
2. the mathematical Draft stack #55–#58 remained correctly rooted on its earlier exact base and must not be silently rebased.

More fundamentally, a versioned file cannot permanently store the SHA of the commit containing that same file as an exact current-head value: committing an update to the field creates a new commit SHA and immediately makes the stored value stale.

Therefore schema v3 separates two notions:

- **live current main head:** read directly from GitHub `refs/heads/main`, not self-recorded in a versioned file;
- **historical mathematical stack-root base:** stored exactly as `stack_root_base_sha` and preserved across later unrelated governance commits.

This is not a relaxation of exact-head governance. It removes an impossible self-reference while preserving the exact dependency heads that matter mathematically.

## 4. Stack immutability firewall

The post-merge sync does **not** rebase PR #55, #56, #57, or #58.

Their exact heads and dependency chain remain the same. In particular:

- root Draft base remains the exact historical main commit on which PR #55 was built;
- each child `parent_head_sha` remains equal to its parent PR's exact head;
- later navigation/governance commits on `main` do not promote or rewrite those Draft-source claims.

If a mathematical PR is later deliberately rebased, that produces a new exact head and requires the appropriate re-audit/review workflow.

## 5. Validator change

`validate_active_front.py` now checks:

1. current main is declared `tracking: live` with source `github:refs/heads/main`;
2. no self-recorded current-main SHA field is reintroduced;
3. `stack_root_base_sha` is 40-hex;
4. the root Draft `parent_head_sha` equals `stack_root_base_sha`;
5. every child `parent_pr` points to an earlier stack member;
6. every child `parent_head_sha` equals the exact parent head;
7. child base branches match parent branches;
8. exact stack/base SHAs are not duplicated into operative navigation files.

The validator remains governance-only and proves no mathematics.

## 6. Operative-front sync

`CURRENT-FRONT.md` and `00-uebersicht/AKTUELLER_STAND.md` are updated to state explicitly:

- current `main` is read live;
- the mathematical Draft stack has a separately pinned historical root base;
- governance-only main advancement does not rebase the active mathematical stack;
- the active mathematical priorities and all Strong-Terminal/Object-X/RH firewalls are unchanged.

## 7. Final status of this sync

This post-merge sync changes only repository governance semantics needed to make the new single-source ledger logically coherent after its first real merge.

It does **not** prove or promote:

- any PR #55–#58 local theorem;
- transported collar decay;
- hard-channel saturated decay;
- structured COND leakage decay;
- B-METINC-COND/GEO/NEW/WIDTH;
- B-FLAGDYN/TIGHT;
- B-SIGN/B-ORIENT;
- Strong Terminal/C6;
- R37/G4c;
- a genuine X candidate;
- Object-X realization;
- RH.

After this governance sync is merged and live-verified, the next mathematical work may resume from the unchanged active R43 front.
