# X-C1 optimized Node-Schur waxing

Append-only research package for PR #137, dated 17 September 2026.

Status: `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`.

Main result: after the proven connected checkpoint `a=49/125`, the fully optimized Prime-2-only node-Schur certificate has its first rigorously localized failure threshold in

`0.3930108 < a_node < 0.3930109`.

A fixed split `theta=0.79142` is rigorously positive on the entire interval `[0.392,0.3930108]`; at `a=0.3930109` strict concavity and a certified optimizer bracket show that even the global `theta` optimum is negative. The odd gap remains `>1/4`.

This is a limit of the stated certificate architecture, not a negative Weil witness. The nonconstant positive Gamma remainder, Prime-2 difference energy and C15 remain unused.

Files:
- `X_C1_NODE_SCHUR_WAXING_FUNCTION.md`
- `check_x_c1_node_schur_waxing.py`
- `node_schur_waxing_checks.log`
- `node_schur_waxing_results.json`
- `SHA256SUMS`
