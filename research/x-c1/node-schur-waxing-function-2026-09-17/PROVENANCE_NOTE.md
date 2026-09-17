# Provenance note

The optimized Node-Schur package is append-only and independent of the older `connected-49_125-rest-schur-2026-09-17/SHA256SUMS` mismatch reported by external audit.

The older mismatch is **not** silently repaired here. Its proof blob on commit `58c12944bc4bc7adf54406160eb73a4e9b26dafb` is Git blob `5185f2e2f986e39bf6f228a445bdb1d5fc836f4e`; the existing manifest proof SHA-256 is known to be stale. A later repair must recompute SHA-256 from the exact committed raw bytes and change only that manifest entry.

This package therefore makes no claim that the older `49/125` package is currently SHA-256-clean.
