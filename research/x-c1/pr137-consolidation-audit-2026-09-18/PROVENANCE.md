# Provenance, corrections and exact-byte findings

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.**
Frozen mathematical target: `fc597f6129db57787c85ec20627ed608233187ba`.
The new deposit is append-only. A future branch head may advance; the
inputs below remain identified by the frozen commit and blob hashes.

## Scope and integrity

frozen_inputs.json lists 134 exact historical files: all 129 blobs under
research/x-c1 at the target, four check_x_c1 scripts, and the imported
COMMON-JUMP audit. Each is bound by Git blob SHA-1, byte length and a
fresh SHA-256. There are 19 package SHA256SUMS files. Fourteen match
every listed payload; five contain nine stale entries. This is not a
claim that all other repository files or all historical commits were
audited. The local snapshot was checked against the remote Git blobs;
local stale checkout bytes were not used as evidence of remote defects.

The seven central packages' manifests all match. The full historical
comparison, including expected and actual digests, is preserved in
historical_manifest_audit.json. New SHA256SUMS covers the consolidation
payload and does not hash itself. Its frozen-input ledger provides a
new byte inventory, not a retroactive repair or validation of old proofs.

| Historical package with mismatch | Affected payloads |
|---|---|
| analytic-waxing-function-2026-09-17 | X_C1_ANALYTIC_WAXING_FUNCTION.md, check_x_c1_analytic_waxing_function.py |
| connected-193_500-2026-09-17 | README.md, X_C1_CONNECTED_WAXING_193_500.md, check_x_c1_connected_193_500.py |
| connected-19_50-2026-09-17 | check_x_c1_connected_19_50.py |
| connected-387_1000-2026-09-17 | check_x_c1_connected_387_1000.py |
| node-schur-waxing-2026-09-17 | X_C1_NODE_SCHUR_WAXING_FUNCTION.md, check_x_c1_node_schur_waxing.py |

None of these nine mismatches is explained by simply converting CRLF
to LF. Their cause is not inferred. The older reported
connected-49_125-rest-schur manifest currently matches at the frozen
target; this current observation does not erase its previously reported
mismatch. The corrected node-schur-waxing-function manifest also matches.

## Known mathematical corrections / interpretation corrections

- At `9aa5cb1edac72fc683c5c9aba5a1f0639fbbf8bb`, the Node-Schur final
  even normalization changed from eta-beta*K/(1+beta) to
  (eta-beta*K)/(1+beta). The local a bracket survived; the theta bracket
  became (0.791428,0.791429). This is recorded in that package's README,
  proof and PROVENANCE_NOTE. Old scalar crossings are not used as
  limits on the actual form in the consolidated endpoint theorem.
- Prime powers use Lambda(p^k)=log(p), in particular w_4=log(2)/2.
  The universal family and segment-4 package explicitly retain this.
- The monomial source audit at `9d9c48de...` evaluates actual energy;
  certificate shear/moment losses must not be subtracted a second time.
- `fc597f6...` separates physical zero extension from full-window shape
  dilation: only the former is the constant-Rayleigh inherited branch.
  A rising selected family is not a rising variational minimum.
- OPEN_PROBLEMS.md supplies an additional domain correction to Â§5 of
  the monotonicity note. It excludes the unproved H1_0 orthogonal shell
  decomposition from the consolidated theorem inventory without
  retracting monotonicity Â§Â§1-4.

## Historical review and status

X_C1_REVIEW_AND_CONNECTED_DEPOSIT_2026-09-17.md records a scoped written
positive review of `4871a5343a996be49e66a565d1e232b2ecd38f54`. The preserved
review names no independently verified reviewer identity and supplies no
separate execution logs. Its own status remains AUTHOR-DERIVED /
EXTERNAL-REVIEW-OPEN. It does not cover the later endpoints or imply
approval of all PR files. We preserve that review event, but do not
promote it or describe fresh author replay as independent review.

The present deposit neither edits the PR description nor issues a
review, merge, Registry promotion or main change. It is a scoped
consolidation for review, not a completed external review.

## Concurrent consolidation

While these checks ran, `21fade97f35089617d07a111ab64082404084319`
added five documentation files under pr137-consolidated-milestone-2026-09-18
on top of the same frozen target, without changing its historical files.
This supplementary audit is deposited after that commit and preserves
it. The 134-file inventory and 19-manifest census explicitly describe
fc597f6, not all later branch additions. The new supplement does not
claim to be an independent external audit of GPT 1.
