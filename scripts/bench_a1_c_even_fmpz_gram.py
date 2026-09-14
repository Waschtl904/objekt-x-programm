#!/usr/bin/env python3
"""Performance-only benchmark for the proposed exact dyadic C-even midpoint.

NO theorem or acceptance decision depends on these timings.  The benchmark
measures FLINT integer Gram products with the frozen C-even column dimension
1075 and 192-bit integer entries, which is the scale of a 2^-192 dyadic
weighted-vector proposal.
"""

from time import perf_counter
from flint import fmpz_mat, ctx

ctx.threads = 2
COLS = 1075
BITS = 192
ROWS = (128, 256, 512, 1024)

print("A1 C-even exact dyadic Gram benchmark")
print(f"threads={ctx.threads} cols={COLS} bits={BITS}", flush=True)
for rows in ROWS:
    t0 = perf_counter()
    a = fmpz_mat.randbits(rows, COLS, BITS)
    t1 = perf_counter()
    g = a.transpose() * a
    t2 = perf_counter()
    # Force one deterministic read so the product cannot be optimized away.
    checksum = g[0, 0] + g[COLS - 1, COLS - 1]
    print(
        f"rows={rows} build={t1-t0:.6f}s gram={t2-t1:.6f}s "
        f"total={t2-t0:.6f}s checksum_bits={abs(int(checksum)).bit_length()}",
        flush=True,
    )
    del g, a

print("DIAGNOSTIC ONLY: timings are not a mathematical certificate")
