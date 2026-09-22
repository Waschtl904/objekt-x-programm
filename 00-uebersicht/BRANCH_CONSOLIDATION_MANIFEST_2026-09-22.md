# Branch consolidation manifest — 2026-09-22

Read-only inventory. **No branch is deleted by this document. No mathematical
status changes.**

## Snapshot

- Ancestry baseline used for the 195 legacy branches:
  `5dcf96e2d3fe977051d7d65febb1ed7b7ef03901` (main immediately after PR #152).
- Current main when this compact manifest was created:
  `526d2c25c906f3656582e46ca723fd8d65df8957` (after proof-reconciliation PR #153).
- The #153 reconciliation adds proof text/provenance on top of the baseline;
  every branch classified with zero unique commits at the earlier baseline
  remains contained in the newer main.
- Legacy non-main branches inventoried: **195**.
- PR #151 is closed as duplicate/superseded by #152/#153; its branch remains
  preserved because it still has unique commit history.

## Conservative result

- `DELETE_CANDIDATE_AFTER_APPROVAL`: **81**
- `KEEP_PROVENANCE`: **2**
- `REVIEW_UNIQUE`: **112**

Only `DELETE_CANDIDATE_AFTER_APPROVAL` branches are candidates for the later
deletion phase. The label is not deletion authorization.

Branches with unique commits remain `REVIEW_UNIQUE` until their exact
successor/provenance is established. Current canonical-navigation references
remain `KEEP_PROVENANCE`.

## Machine-readable manifest

The following fenced CSV is the complete 195-branch inventory.

```csv
branch,head_sha,merge_status_at_baseline,unique_commits,pr_links,canonical_navigation_reference,category,recommendation,successor,reason
__tmp_unused_p06,3e996e83be242eb12a073e1b71da027624d715c3,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
__tmp_unused_p06_2,3e996e83be242eb12a073e1b71da027624d715c3,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
__tmp_unused_p06_3,3e996e83be242eb12a073e1b71da027624d715c3,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/a1-composition-2026-09-15,0a7c970fc5983c9c198915e2c7c1f6280834b13a,UNMERGED_UNIQUE,8,#131:closed,no,AUDIT_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
audit/legacy-result-recovery-candidates-2026-09-20,21ae2c037dcb98c5b24c2be7619fcd7237d179f7,UNMERGED_UNIQUE,2,,no,AUDIT_UNIQUE,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
audit/p11-r32-a-wall-reduction,03db72affb6e24bd5e9477a8cbdac16b1633e504,UNMERGED_UNIQUE,1,#5:merged,no,AUDIT_UNIQUE,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
audit/p11-r32-ht-a4b-single-chamber,8466e33e487b08ca94aca08d5f69bf1e09775bff,UNMERGED_UNIQUE,4,#9:merged,no,AUDIT_UNIQUE,REVIEW_UNIQUE,,4 unique commit(s); provenance/supersession review required.
audit/p11-r32-sw1-self-contained-theorem,f8f9f107b9c6879611ecb492979737a5541141e9,UNMERGED_UNIQUE,4,#10:merged,no,AUDIT_UNIQUE,REVIEW_UNIQUE,,4 unique commit(s); provenance/supersession review required.
audit/p11-r32-tail-fg-pivot,772f3a5fd99d23c6b44d447de7e73dc606828bb5,UNMERGED_UNIQUE,2,#7:merged,no,AUDIT_UNIQUE,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
audit/r36-a14-2b-regression,7425b5013124e1bc4efc33431ae8658695bf7e53,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-2c-q-density-hardening,207992ce02fc76ea43fa40757b8d9f506e20424d,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-2d-r015-open-strip,ec39dec6e4d5681f5e4bed3891ee7404af9b9203,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-2e-middle-wedge,2727d49531f659344aed0847d29010b1f5825b7e,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-2f-unified-sub-b-strip,b1b322ace330ec378925a1efcfb89c46988edbdb,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-2g-super-d-relation,f884adbc0389e989889d304de1cab571d7df469a,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-2h-full-sub-b-classification,3b22ce3b7368b7619454e7053893cbea4a7cdca1,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-2i-complete-two-shift,9950e590950106e07ca712dd6ef7f0fa976cb436,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-3a-three-shift-boundary,0a7b5751bbae34e72390811e5f07faf328c1b6ad,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-3a-uc-proof-repair,489f41d69ebcda75a496239c49ada0291640d77b,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/r36-a14-boundary-domain-horizon,885489d482b43ce5024a4d655a00322c7935e258,IN_MAIN_AT_BASELINE,0,,no,AUDIT_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
audit/x-c0-cancel-first-2026-09-16,c700d8a2b56d60bcaa84c64a772b4b581854b96d,UNMERGED_UNIQUE,10,#138:closed,no,AUDIT_UNIQUE,REVIEW_UNIQUE,,10 unique commit(s); provenance/supersession review required.
cert/np-prolate-1-root-bracket-repair-2026-09-15,5721efb401c4b8128d6be7513c559bc3f86f1581,UNMERGED_UNIQUE,22,#126:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,22 unique commit(s); provenance/supersession review required.
chore/integrity-workflow-race-fix,ebaa488a17137c9a2d4eaf2576f7259cbf2bc913,UNMERGED_UNIQUE,3,#95:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
chore/root-archive-wave-a,fe8271657a587b0a8985c3d08791410b10115089,UNMERGED_UNIQUE,3,#92:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
ci/a1-c-even-gated-certificate-2026-09-21,69135711465d0bf73d638c2ecda22dd19908ee3f,IN_MAIN_AT_BASELINE,0,#146:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
ci/legacy-pr-workflow-path-hygiene-2026-09-21,d1fbf8ca5ae98ecf13bd28e6697e67a7a03dbcea,IN_MAIN_AT_BASELINE,0,#148:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
ci/validate-a1-fast-route-2026-09-21,7f2b5722610cbdc1289960345fcbccf3395aa99a,UNMERGED_UNIQUE,1,#147:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
ci/validate-legacy-workflow-fast-route-2026-09-21,07170515f10a96f9faea33869ac30a9cd80df1ac,UNMERGED_UNIQUE,1,#149:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
docs/current-front-navigation,9e11f9531ffd9a7dce5714f6e6749a5fea5b1bed,UNMERGED_UNIQUE,3,#11:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
docs/current-front-post-pr35,5abe52b53b88dac7ef8ce9fcd406bcac88ce030b,UNMERGED_UNIQUE,14,#36:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,14 unique commit(s); provenance/supersession review required.
docs/k-r-notation-cleanup-2026-08-26,767ca114b5156a88958c399710594b5f3bf77969,IN_MAIN_AT_BASELINE,0,#2:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
docs/legacy-survivor-reconciliation-2026-09-20,a14b93532773010096a52330f93e094e02a5e284,IN_MAIN_AT_BASELINE,0,#144:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
docs/object-x-consolidation-2026-08-26,43768c7d31fc6ea33ebc78bdf6b2a7fc416fb48a,UNMERGED_UNIQUE,17,#1:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,17 unique commit(s); provenance/supersession review required.
docs/object-x-longterm-definition-2026-08-26,622a0de711828de93bfff05a709ae4e8b40887be,IN_MAIN_AT_BASELINE,0,#3:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
docs/object-x-research-roadmap-2026-08-26,38b2efa0f11505d499fbf86ae6c2a9522c67b5ae,UNMERGED_UNIQUE,3,#4:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
docs/ox-gen-session-handoff-2026-09-13,4c8e05a626e95bfed112189acedc59b35798229d,UNMERGED_UNIQUE,7,#99:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,7 unique commit(s); provenance/supersession review required.
docs/post-c6-entrypoint-sync,690c96e153d3c148be604109e90196c1110ef8f1,IN_MAIN_AT_BASELINE,0,#93:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
docs/post-img0-analytic-hardening,4b61a19d269d0b60f91874f4ecb0214a42e90a99,UNMERGED_UNIQUE,3,#44:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
docs/post-pr10-front-sync,4d9313bc4064b5478b0bacc0af1e5b323038b322,UNMERGED_UNIQUE,2,#12:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
docs/post-pr144-research-state-sync-2026-09-21,a64bdd9b6f389a269392a16b3b7ce6342d395b0d,IN_MAIN_AT_BASELINE,0,#145:merged,yes,MERGED_HISTORY,KEEP_PROVENANCE,,Contained in main but referenced by current canonical navigation.
docs/post-pr34-c1b2a-sync,174aba0d8d14b296e6d8e3609d64e9f06bc7a4d5,UNMERGED_UNIQUE,3,#35:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
docs/post-pr38-a-fold-sync,36637d981a891cefe1b97d50e353424cf8da0171,UNMERGED_UNIQUE,2,#39:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
docs/post-pr40-m1-nd-sync,0ced406da23be7d2863336e5983bd0cb48aad676,UNMERGED_UNIQUE,2,#41:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
docs/post-pr42-img0-sync,297a2a76191d40c0bd77e0e3bb6a9af0242a8953,UNMERGED_UNIQUE,2,#43:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
docs/readme-project-independence-2026-09-21,27cb7fab980fd8d777b36cfd47554711efef4bbc,UNMERGED_UNIQUE,1,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
docs/research-state-registry-2026-09-20,1ca26e1f059ca113bc2d794213b452aa21e399ab,UNMERGED_UNIQUE,5,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,5 unique commit(s); provenance/supersession review required.
docs/risk-based-governance-2026-09-21,059a720131095730e3cbcd54e3a0e7b39c4096cc,IN_MAIN_AT_BASELINE,0,#150:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
docs/sync-current-front-pr49-terminal,c4ee01a696892dff662aff963731f2436cbcf5be,UNMERGED_UNIQUE,7,#50:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,7 unique commit(s); provenance/supersession review required.
feat/vor-iota-prime-7D-firewall,9f5b620d73ff91348f05e23e95ca8ce7a068cd65,IN_MAIN_AT_BASELINE,0,#97:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
fix/arxiv-2608-24827-author-zhu-2026-09-13,c03c1f3aa43416fe8f2951002614988e2aa03d59,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
fix/p12-stale-subwedge-reference,5a9a6b851d71530efd8cc41bac7c76bf321ffcaf,UNMERGED_UNIQUE,4,#37:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,4 unique commit(s); provenance/supersession review required.
freeze/forward-dil-3dc1caa,3dc1caa2870020b238c21a852328bab1c384deb7,UNMERGED_UNIQUE,28,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,28 unique commit(s); provenance/supersession review required.
freeze/pr116-6b5956e,6b5956e69dfcb8124e8e31083613fd89c5f35fb3,UNMERGED_UNIQUE,18,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,18 unique commit(s); provenance/supersession review required.
freeze/pr116-hard-audit-524bc5f,524bc5f08b822eeae751196eb9f8acb989bd1122,UNMERGED_UNIQUE,19,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,19 unique commit(s); provenance/supersession review required.
freeze/prime-circle-weyl-04e2256,04e2256919d2726c31db7febe7810a137a8ff77d,UNMERGED_UNIQUE,33,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,33 unique commit(s); provenance/supersession review required.
freeze/rp2-kernel-ac57408,ac574089215767f3b353fd6d6af0649b4ded454c,UNMERGED_UNIQUE,29,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,29 unique commit(s); provenance/supersession review required.
freeze/rp2-line-weyl-6206950,620695070db6ce9693ed5a1848a2fa66145f41ec,UNMERGED_UNIQUE,32,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,32 unique commit(s); provenance/supersession review required.
freeze/rp2-weyl-c06500b,c06500b9f09571bc40536ebe81157fbb0e741ae9,UNMERGED_UNIQUE,31,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,31 unique commit(s); provenance/supersession review required.
governance/active-front-pr61,5d5d48f83ffd4f490eb376332f38dba84b450e4d,UNMERGED_UNIQUE,1,#62:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
governance/active-front-pr61-head2,6b996cdd245c9e716f116567b1247cdfc1b2eb7c,UNMERGED_UNIQUE,2,#63:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
governance/active-front-pr64,eee9d8042dfe40d9e6bb1f303fda36d3a6597e33,IN_MAIN_AT_BASELINE,0,#65:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
governance/active-front-pr66,ca1b6d6f296c29446b02948f4a25a1a8de1d605e,IN_MAIN_AT_BASELINE,0,#67:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
governance/active-front-pr80-pr81,3745bad9880470f0a814a99963a523292ac6b41e,IN_MAIN_AT_BASELINE,0,#82:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
governance/track-r43-pr68-pr70,e097106cf85582b65fc28b74922fac09fe8c2ed0,IN_MAIN_AT_BASELINE,0,#71:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
governance/track-r43-pr72,45ca84fe83b9c73ee970a5eeaa754e380dd89ebc,IN_MAIN_AT_BASELINE,0,#73:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
governance/track-r43-pr74,dd7b3bb831d21bd2ba66505bd0dcdbf1193e4d7e,IN_MAIN_AT_BASELINE,0,#75:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
governance/track-r43-pr76,7a8645f0aacf0a15723b81189a2ac9be3d4e8222,IN_MAIN_AT_BASELINE,0,#77:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
governance/track-r43-pr78,71c8a9dd7c8fcd335367bfc7acf149c192a49dd5,IN_MAIN_AT_BASELINE,0,#79:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
p11-e2e-r23-r35-hardening-2026-08-21,b4f3b861021be47a285d41db16937810a202192a,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
p11-final-e2e-freeze-2026-08-21,86e4fe4bf6182313978fe7a2e8cd1c1d9cf9c539,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
p11-final-freeze-2026-08-21,f88c960cbb08514b7e84c31208ed6a75e2248793,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
p11-fix-definition-env-2026-08-21,76427aed94ed196b53d779599b9c7a2a39d77aef,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
p11-freeze-bookkeeping-2026-08-21,3d60e19697420040ea8fede5dd5fc87703dfe92e,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
p11-freeze-reconciliation-2026-08-21,36fe665c2cfb255eaff8bf016270c7769926f45f,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
promotion/ht-a4b-sw1-m,bc8ae703ca6a309e9bf991c9194b631ae4bd8797,UNMERGED_UNIQUE,2,#13:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
promotion/ht-a4b-sw1-m-record,7520807b33f041ee6f4a182506c123e7cf240718,UNMERGED_UNIQUE,7,#14:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,7 unique commit(s); provenance/supersession review required.
r36-a11-consolidation,fe599fa4fb485bec9e84eb54f1b2303de21c0d01,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r36-a11-preimage-a13,0ceeeab8741045e40fd40037fa119ec1334e87bf,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r36-a13c-gamma-pairing,5df0f7bcd0990d241197bd05dc39a6bf67c3f0f5,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r36-a14-hardening-incidence,25f27b87f0a227b335076c95f44aa615b453e473,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r36-a14-visibility-cells,37b0abba4e78fc674ee6bb00fd6bc3e37aedc710,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-cond-flagdyn-reverse-normal-bridge,7d8a9e47c96962f49afedba83f1090a1598f5386,IN_MAIN_AT_BASELINE,0,#66:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-full-rest-local-decay-cond-limit,112f611727dbd3386bff5e11b9a5d5d143cdee6b,UNMERGED_UNIQUE,1,#89:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
r43-geometric-mean-resolvent-leakage,4a28bde4d02e983d32ba9e2c28c0110445a7685b,IN_MAIN_AT_BASELINE,0,#57:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-good-normal-tail-reduction,0e57cf230291abd16ce88b0ceed95d68036799e5,IN_MAIN_AT_BASELINE,0,#58:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-hard11-level0-saturation,e29545a6040640e754e885888826d1cf235df58c,IN_MAIN_AT_BASELINE,0,#61:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-o1-local-interval-uniformity,775158ee656d03bc3601857e8cb0e47fa791caf1,IN_MAIN_AT_BASELINE,0,#87:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-post-c6-source-descent-weil-separation,1a6c8777c803bcf7ef34e74b9979578f05c5b40b,UNMERGED_UNIQUE,1,#91:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
r43-reverse-extension-countertest,5a5776c36ed31475ef6e8a715371307f1f6b8341,IN_MAIN_AT_BASELINE,0,#69:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-extension-galerkin-graph-proxy,25c27bd7f0646e7a63c3cba109336c6414fee72b,IN_MAIN_AT_BASELINE,0,#72:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-extension-multichannel-toy,1a64e9d1841de170f96dd9d9f018ec41da46e415,IN_MAIN_AT_BASELINE,0,#70:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-extension-multichannel-toy-2,5a5776c36ed31475ef6e8a715371307f1f6b8341,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-extension-multichannel-toy-3,5a5776c36ed31475ef6e8a715371307f1f6b8341,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-extension-multichannel-toy-clean,5a5776c36ed31475ef6e8a715371307f1f6b8341,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-extension-multichannel-toy-final,5a5776c36ed31475ef6e8a715371307f1f6b8341,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-mean-localization-diagnostic,d2d8b9077a61f5d103bcec02548fdf29fa282c2e,IN_MAIN_AT_BASELINE,0,#76:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-normal-schur-extension,b9b3b70929df482588ad07c96dc3c1c06faa2fce,IN_MAIN_AT_BASELINE,0,#68:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-occupancy-kernel-firewall,6807d1e04588de81d0e5b4c14a0a4e8e5756ba97,IN_MAIN_AT_BASELINE,0,#78:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-reflection-common-mode-firewall,4ca4abb37e7fcaa8d045e94ad5f816d481ec40d0,IN_MAIN_AT_BASELINE,0,#81:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-reverse-shift-variance-mean-firewall,117cb0afdde12b984808fbf97d24c28252a81acb,IN_MAIN_AT_BASELINE,0,#74:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-schur-corr-structured-hub-proxy,4abccc2dd29d87f914440478c286dbc6edf11169,IN_MAIN_AT_BASELINE,0,#83:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-schur-var-delta-sweep,3e4e5a73679db9f88624869587c4bd3bc3fec266,IN_MAIN_AT_BASELINE,0,#84:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-schur-xband-anchor-recheck,8f49e2397ff991b378600b092ce9b52c26b58fd0,IN_MAIN_AT_BASELINE,0,#86:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-schur-xband-comm,4381c73e4220953899d8484a0ed58cd4815256d9,IN_MAIN_AT_BASELINE,0,#85:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-shellwise-collar-common-mode-firewall,483421fe5eb94a4474103083ec998f4dfa3e4266,IN_MAIN_AT_BASELINE,0,#80:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-structured-schur-leakage,b221e6c2c4fc0b379b1b71d0100e482d8861448e,IN_MAIN_AT_BASELINE,0,#55:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-translation-resolvent-transfer,08153af2447dfd58973ddf93d8acedbf1dabe601,IN_MAIN_AT_BASELINE,0,#56:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
r43-transported-collar-prime-band,ff327e3fb59dcfde7bd8260e779919961dd6f88d,IN_MAIN_AT_BASELINE,0,#64:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/a1-c-even-2026-09-14,419202e376b75b872a31b77a126ca5e784d9b3ed,IN_MAIN_AT_BASELINE,0,#122:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/a1-c-even-spd-gate-2026-09-14,69d9f15d38216ef003310bf4c72d2f7065436db9,IN_MAIN_AT_BASELINE,0,#123:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/a1-c-odd-2026-09-14,4f5bc7b2f5e90092b95c80d90aab9a102853cf73,IN_MAIN_AT_BASELINE,0,#124:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/a1-finite-gate-architecture-2026-09-14,4b41e7c830652634f371d5b33d839486f1c0969b,UNMERGED_UNIQUE,5,#121:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,5 unique commit(s); provenance/supersession review required.
research/a1-highfreq-prolate-tail-2026-09-13,5351fadaae8e103888a9e39b3d1c239b901f9476,UNMERGED_UNIQUE,15,#113:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,15 unique commit(s); provenance/supersession review required.
research/a1-legendre-dlmf-tail-2026-09-13,5f6bb7af90a14091201b6811358f53c376886bce,UNMERGED_UNIQUE,3,#119:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
research/a1-legendre-finite-certificate-2026-09-13,c6e018ddb111f14925276506f54a2e49a44183b2,UNMERGED_UNIQUE,3,#117:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
research/a1-legendre-quadrature-budget-2026-09-13,e5e01c773afe77519638c968cf148565cbfee846,UNMERGED_UNIQUE,10,#118:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,10 unique commit(s); provenance/supersession review required.
research/a1-omega1551-finite-reduction-2026-09-13,503dacfa163013fe37cec2a2b43d0cfa7484995d,UNMERGED_UNIQUE,11,#115:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,11 unique commit(s); provenance/supersession review required.
research/a1-osipov1102-finite-reduction-2026-09-14,9e0e8b7899312d1656470c348f675b1133ce30ab,UNMERGED_UNIQUE,16,#120:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,16 unique commit(s); provenance/supersession review required.
research/a1-schur-bounded-remainder-2026-09-13,5c5f6bad473b2b3fb7dcaaab84869ec0158644f1,UNMERGED_UNIQUE,10,#114:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,10 unique commit(s); provenance/supersession review required.
research/critical-half-forward-dilation-gate-2026-09-15,76d5c9671df3b84bd5a9b4257b4b9f07f9749490,UNMERGED_UNIQUE,29,#127:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,29 unique commit(s); provenance/supersession review required.
research/critical-half-green-tree-bridge-2026-09-13,1e1682f2c0bddee622c651418522b8f9391244a7,UNMERGED_UNIQUE,55,#116:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,55 unique commit(s); provenance/supersession review required.
research/critical-half-prime-circle-weyl-2026-09-15,04e2256919d2726c31db7febe7810a137a8ff77d,UNMERGED_UNIQUE,33,#132:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,33 unique commit(s); provenance/supersession review required.
research/critical-half-rp2-kernel-2026-09-15,ac574089215767f3b353fd6d6af0649b4ded454c,UNMERGED_UNIQUE,29,#128:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,29 unique commit(s); provenance/supersession review required.
research/critical-half-rp2-line-weyl-2026-09-15,620695070db6ce9693ed5a1848a2fa66145f41ec,UNMERGED_UNIQUE,32,#130:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,32 unique commit(s); provenance/supersession review required.
research/critical-half-rp2-point-weyl-2026-09-15,1888a95841641ed3974602c17f8d6896c2ee015c,UNMERGED_UNIQUE,32,#129:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,32 unique commit(s); provenance/supersession review required.
research/critical-half-rp2-source-filtration-2026-09-15,23849b3dbd4345d771721c201d7214212fa93ccb,UNMERGED_UNIQUE,30,#135:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,30 unique commit(s); provenance/supersession review required.
research/critical-half-rp2-star-bulk-2026-09-15,385680bbc6f4f4d244f6fe2e433ac1b425938d22,UNMERGED_UNIQUE,30,#133:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,30 unique commit(s); provenance/supersession review required.
research/critical-half-total-weyl-self-energy-2026-09-15,5b5f17a5afd45e8f7b15bc3121b8a869dceb28a1,UNMERGED_UNIQUE,35,#134:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,35 unique commit(s); provenance/supersession review required.
research/first-chamber-raw-td-cocycle-o1-o7-2026-09-22,e3a648488cf1cecbb504e08e2906745db233d659,UNMERGED_UNIQUE,9,#151:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,#152+#153,Draft PR #151 closed as duplicate/superseded by merged #152 and #153; branch retains unique commits/provenance and requires explicit review before deletion.
research/np-common-jump-gram-2026-09-13,0688205ed81baa7ad108de921c22f3de8161f0e8,UNMERGED_UNIQUE,8,#107:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/np-discrepancy-pole-cleared-correlation-2026-09-13,57f1c8ea7fbab327b1d1af52bdbfe5581654d5ec,UNMERGED_UNIQUE,8,#110:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/np-dual-a1-morse-diagnostic-2026-09-13,c54ca237457efdafc74dd0e1f3e73bcbac451058,UNMERGED_UNIQUE,6,#112:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,6 unique commit(s); provenance/supersession review required.
research/np-dual-completion-screw-audit-2026-09-13,d96463f28458925d57ec7f2a040456c8b5d063b0,UNMERGED_UNIQUE,11,#111:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,11 unique commit(s); provenance/supersession review required.
research/np-gap-q0-first-channel-2026-09-13,c9ed27f5d601fb96dcba18334ed2fc37003da3ba,UNMERGED_UNIQUE,8,#108:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/np-gap-review-corrections-prime-overlap-2026-09-13,dff68efd48f60f8627ce6a25a2e22c4db4c196ba,UNMERGED_UNIQUE,18,#109:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,18 unique commit(s); provenance/supersession review required.
research/nullpole-strategic-reclassification-2026-09-13,f544552080e4607500d02d51ecbe76445def0cd0,UNMERGED_UNIQUE,8,#106:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/ox-gen-a-generator-plane-2026-09-13,40bb203384ab0f3357d0abb4967fa0617fb21f3b,UNMERGED_UNIQUE,8,#100:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/ox-gram-ar1-consolidation-2026-09-12,cc630d50741c4908db3bd8d2aba1049039d766e2,UNMERGED_UNIQUE,19,#98:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,19 unique commit(s); provenance/supersession review required.
research/pos-dil-1-prime-moment-2026-09-13,7dcc6732437c3999b0e973dbc4bc6bb9979185c6,UNMERGED_UNIQUE,8,#101:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/pos-dil-2-feature-shorting-nogo-2026-09-13,c4a5036d9b6a189a142d16ec4754fada7a7173c8,UNMERGED_UNIQUE,8,#102:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/pos-dil-2b-first-exterior-shell-2026-09-13,21de4068d45a91f1a278b781d5c088095996c6d9,UNMERGED_UNIQUE,8,#103:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/pos-dil-2c-exact-shell-gauge-r0-2026-09-13,1ce47b7d1340875e98fc476188b0e2a776a4c0d4,UNMERGED_UNIQUE,8,#105:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/pos-dil-2c-shell-radius-2026-09-13,d14b7e0126f1a097d6061c7ec69462f9a059cb70,UNMERGED_UNIQUE,8,#104:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/r43-gcac-hardening,81c591675be14345943cca961c5da965b2c8eef6,IN_MAIN_AT_BASELINE,0,#53:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/r43-hub-jump-orientation,528153ec944a8201afe9235a53d96afc944fa9fc,IN_MAIN_AT_BASELINE,0,#88:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/r43-positive-root-anchor,084b8b7855601c5fae87bf4e59a00648ffbb9116,IN_MAIN_AT_BASELINE,0,#90:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/r43-structured-cond,4c77beb3345e92f3c2d9ebddd838775d4c7ecf3d,IN_MAIN_AT_BASELINE,0,#54:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/rp2-mixer-source-compat-2026-09-15,8f7b0f67844c245b9def75bcd477dcbe2d239451,UNMERGED_UNIQUE,32,#136:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,32 unique commit(s); provenance/supersession review required.
research/strong-terminal-r37-two-shift-mismatch,ab3e6bc5379b756e525b6e63f22ce350438a6739,IN_MAIN_AT_BASELINE,0,#52:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/sw1-2tp,d39b8603adb373ae31471e863c72b555b804020a,UNMERGED_UNIQUE,7,#17:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,7 unique commit(s); provenance/supersession review required.
research/sw1-a-fold-reconciliation,ba1cee8fd0507aebd88349daf90160f55755e357,UNMERGED_UNIQUE,7,#38:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,7 unique commit(s); provenance/supersession review required.
research/sw1-a0-coverage,0f2be5c7e1dd80bb0c85bbc52b5ce01679de7bd6,UNMERGED_UNIQUE,57,#20:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,57 unique commit(s); provenance/supersession review required.
research/sw1-a1-finite-cell,36f68c606b916a2830199826f698d21b14d508bb,UNMERGED_UNIQUE,60,#21:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,60 unique commit(s); provenance/supersession review required.
research/sw1-a10-crossgram-cocycle,591a376197d8e320e8f23a682755da7b8d4d639e,UNMERGED_UNIQUE,56,#34:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,56 unique commit(s); provenance/supersession review required.
research/sw1-a10-finite-crossgram,45b1f97d4ee167365e853577ca8f4592429fc1cf,UNMERGED_UNIQUE,124,#33:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,124 unique commit(s); provenance/supersession review required.
research/sw1-a2-a10-reconciliation,8e404a75a8a4f9e68bf87d3cc5556bd1da51a1d7,UNMERGED_UNIQUE,5,#40:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,5 unique commit(s); provenance/supersession review required.
research/sw1-a2-annulus-projection,cfff116954607626f075d16f26c6617e4e9b97d0,UNMERGED_UNIQUE,64,#22:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,64 unique commit(s); provenance/supersession review required.
research/sw1-a2-certificate,ef0c07cf419fc2a5939f97fb15dd28168b7bd7ae,UNMERGED_UNIQUE,2,#29:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
research/sw1-a3-certificate,5401319b28a53cef3562e64ad2d750721081a840,UNMERGED_UNIQUE,5,#30:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,5 unique commit(s); provenance/supersession review required.
research/sw1-a3-free-coordinate-gram,073f6e277d3f7084fbac5d57dcb3ccdeefc94699,UNMERGED_UNIQUE,65,#23:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,65 unique commit(s); provenance/supersession review required.
research/sw1-a4-irrational-rotation-nogo,10d2b42266af7f8cd0801db5e8f32b21c6f57004,UNMERGED_UNIQUE,68,#24:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,68 unique commit(s); provenance/supersession review required.
research/sw1-a5-two-sheet-transfer,dc462d3a1a8eeaeb1b304e51c034c8e721d9226c,UNMERGED_UNIQUE,72,#25:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,72 unique commit(s); provenance/supersession review required.
research/sw1-a6-rotation-hole,0ac4dd943301ef7f78a509ad9418f7b3c74fc245,UNMERGED_UNIQUE,75,#26:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,75 unique commit(s); provenance/supersession review required.
research/sw1-a7-finite-state-cocycle,8f70d7277c52017761e44cf53e6e47bd2801f8f9,UNMERGED_UNIQUE,79,#27:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,79 unique commit(s); provenance/supersession review required.
research/sw1-a8-lower-finite-components,92230af645ea2f0549051edb138b32629b0f56da,UNMERGED_UNIQUE,82,#28:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,82 unique commit(s); provenance/supersession review required.
research/sw1-a8-midpoint-degeneracy-fix,6360f6f7d214a42f54e002ff6da5bed163e4bf88,UNMERGED_UNIQUE,7,#31:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,7 unique commit(s); provenance/supersession review required.
research/sw1-a9-knf-separator,8ccf4795ab8280fb262a9f75ff2a104817bfa812,UNMERGED_UNIQUE,113,#32:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,113 unique commit(s); provenance/supersession review required.
research/sw1-awi,fe489896af592940a6d63e0395f215ab65d2540b,UNMERGED_UNIQUE,8,#18:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,8 unique commit(s); provenance/supersession review required.
research/sw1-bl7,57362a090897bae7545cccfd2c28f10b6a55411d,UNMERGED_UNIQUE,2,#16:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
research/sw1-delta-descent,d73d3fdf4b1f919fc9526fc09ce206866b472704,UNMERGED_UNIQUE,52,#19:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,52 unique commit(s); provenance/supersession review required.
research/sw1-knf,0b0114d3403a92c59a5572be820aad595b1dc53e,UNMERGED_UNIQUE,3,#15:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
research/sw1-m1-nd-image-space,52ae23096d1965ba3eb9c7880471b20ff0c6a5b6,UNMERGED_UNIQUE,6,#42:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,6 unique commit(s); provenance/supersession review required.
research/sw1-m1-nd-img1,28753fa150532bab839fc6f8f554bf3bc123d1da,UNMERGED_UNIQUE,20,#45:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,20 unique commit(s); provenance/supersession review required.
research/sw1-m1-nd-img2-descriptor,2e193c5b5726ea66cb8f06de1e2cddbf963b887e,UNMERGED_UNIQUE,7,,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,7 unique commit(s); provenance/supersession review required.
research/sw1-m1-nd-img3-eliminator,dad038c8d72774cfa40d73ec751a9c61ff5e48c8,UNMERGED_UNIQUE,80,#46:merged,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,80 unique commit(s); provenance/supersession review required.
research/sw1-m1-nd-salvage-phase-diagram,2ed1583f074574c2fdb5a48203d63d520a86b5f6,UNMERGED_UNIQUE,20,#49:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,20 unique commit(s); provenance/supersession review required.
research/terminal-191d-schur-diagnostic-2026-09-20,bfb267f7fc7aa6ec523441cbd56f6c2bed93bda2,UNMERGED_UNIQUE,15,,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,15 unique commit(s); provenance/supersession review required.
research/x-c0-common-memory-2026-09-16,72208f2cefdd76bcb6656d931f4b19aea07b25e6,IN_MAIN_AT_BASELINE,0,#137:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/x-c1-inherited-resonance-shell-schur-2026-09-18,19e4630a7f0d4c8232f8ee81c4b483355ed2f505,IN_MAIN_AT_BASELINE,0,#143:merged,yes,RESEARCH_MERGED_HISTORY,KEEP_PROVENANCE,,Contained in main but referenced by current canonical navigation.
research/x-c1-moment-edge-compensation-2026-09-16,29f2e8535bcf0838610f598533f74e01f444bf01,UNMERGED_UNIQUE,5,,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,5 unique commit(s); provenance/supersession review required.
research/x-c1-moment-gamma-followup-2026-09-17,6e1a90aa32f109570337ca17b62d82087494a46d,UNMERGED_UNIQUE,1,#142:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
research/x-c1-post-unit-q8-horizon-extension-2026-09-21,9ab580c0e6014b5e8f185c2b77101506579e0a77,IN_MAIN_AT_BASELINE,0,#152:merged,no,RESEARCH_MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
research/x-c1-seam-energy-2026-09-17,a94b011880363e4abc99cc8838bd9371e16d526e,UNMERGED_UNIQUE,2,#141:closed,no,RESEARCH_UNIQUE,REVIEW_UNIQUE,,2 unique commit(s); provenance/supersession review required.
review/critical-half-116-6b5956e-2026-09-15,987eea510edb451aa6dfce38b6edb3b1accd0f11,UNMERGED_UNIQUE,28,#125:closed,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,28 unique commit(s); provenance/supersession review required.
review/pr137-freeze-2026-09-17,58c12944bc4bc7adf54406160eb73a4e9b26dafb,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
review/strong-terminal-r37-two-shift-mismatch,b3d7a043e3097076ecaeef3d13d91db2263591e3,IN_MAIN_AT_BASELINE,0,#51:merged,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
roadmap/canonical-research-roadmap-v2,bb47cced071367fecf7cd266c3bc005d40f0f7ef,UNMERGED_UNIQUE,13,#59:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,13 unique commit(s); provenance/supersession review required.
roadmap/post-59-main-sync,0027562e52e877417641fb555e623510c4e36f38,UNMERGED_UNIQUE,10,#60:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,10 unique commit(s); provenance/supersession review required.
round14-core-both-full-b2d,4d9c6d0780feac88f991535844fee6eedf04b082,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
status/ht-tail-components-promotion,4725074e0385572d494ca94d58e0e83826f0ea59,UNMERGED_UNIQUE,1,#8:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
status/legacy-scoped-survivor-reconciliation-2026-09-20,91c48b5cb974579762c817aa641fee497603db6c,UNMERGED_UNIQUE,5,,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,5 unique commit(s); provenance/supersession review required.
status/neu-a-wall-1-promotion,3d399296543ba758b9b4751d821275669ad775fa,UNMERGED_UNIQUE,1,#6:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
sync/m1-nd-img4-postmerge,c9fbdd1aac0a0c2bdb83e516b0bad6e26d480c1d,UNMERGED_UNIQUE,3,#47:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,3 unique commit(s); provenance/supersession review required.
sync/m1-nd-img4-registry-fix,4975d4a7218ddba9eb0f0efd44b61b45ec61ba0f,UNMERGED_UNIQUE,1,#48:merged,no,UNIQUE_HISTORY,REVIEW_UNIQUE,,1 unique commit(s); provenance/supersession review required.
tmp/ignore,18050e052ee053920357bdc60f6b380cd0dbe611,IN_MAIN_AT_BASELINE,0,,no,MERGED_HISTORY,DELETE_CANDIDATE_AFTER_APPROVAL,,No commits unique versus baseline main and no literal reference in current canonical navigation.
```

## Limits of this pass

The current-navigation reference field scans the canonical live navigation
files, not every historical proof file in the repository. Before deleting a
provenance-sensitive branch, perform a branch-specific reference/successor
check. Create an immutable archive tag first when a unique historical tip must
remain reachable.

Branch deletion is a separate operation requiring explicit approval.
