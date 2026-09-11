# Vor-ι′ finite-window Rest/Feshbach firewall — Draft package

**Status:** analytical candidate package; pre-push audit completed.  No registry promotion, no Object-X claim, no RH claim.

**Base used for publication:** `main@a757da3aeb263fdf041898f69bd80afe6322f5ee`.

This package consolidates the finite-window `R=1` source-first checks that followed PR #91.  Its purpose is narrow:

1. record the type correction that the earlier placeholders `H_A`, `E_{\mathcal A}`, `\Pi_{\mathcal A}` are not defined `main` data;
2. test two actually defined P11 arithmetic Gram mechanisms on the explicit PR-#91 zero-jet/prime-2 witness;
3. prove that the **native** Rest Gram and the **native** Feshbach/Schur Gram both miss the required Weil mixed-form calibration;
4. keep every stronger/global source realization open.

Files in this package:

- `audit.md` — consolidated mathematical statement and scope;
- `provenienz.md` — reconciliation/error chronology;
- `scripts/check_vor_iota_prime_m012_and_feshbach.py` — finite symbolic-position moment reproduction and diagnostic resolvent interval;
- `scripts/check_vor_iota_prime_rational_certificate.py` — exact rational implication from five coarse moment inequalities to the firewall separation;
- `scripts/check_vor_iota_prime_traeger_stabilitaet.py` — epsilon/support stability diagnostic.

Run from repository root:

```bash
python scripts/check_vor_iota_prime_m012_and_feshbach.py
python scripts/check_vor_iota_prime_rational_certificate.py
python scripts/check_vor_iota_prime_traeger_stabilitaet.py
```

The floating-point scripts are reproducibility diagnostics, not interval certificates.  The exact rational script proves the **implication** from the five coarse moment inequalities to the separation; it does not independently interval-certify those moment inputs.

The intended governance sequence is:

`pre-push package audit -> Draft PR -> remote SHA/byte verification -> exact-head review -> only then any merge decision`.
