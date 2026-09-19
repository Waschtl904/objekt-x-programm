# All-parity window amplification and quantitative conditional restart

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**. Anchor: `a659047e00d024c0daa3991ea59fd21afd9f8793`.

For B=log(5)/2, the all-source theorem with exactly the original two
Mellin conditions now reaches B+5*10^-19, with physical gap 3*10^-16.
Nested guarantees retain gap 3*10^-15 through B+10^-19 and 10^-15
through B+4*10^-19. The odd gap remains 10^-12 in all three ranges.

The second result is a conditional restart uniform for B<=a<b<=1:
if q_a>=epsilon I, 0<epsilon<=1, then h<=2^(-ceil(1600/epsilon))
and b<=1 imply q_b>=(epsilon/2)I. The actual full profile Schur norm
is <49/200. All five possible channels 2,3,4,5,7, all mixed terms,
the full core, and actual source form domains are controlled.

The explicit iteration has summable widths and diminishing gaps. No
nonaccumulating transport, uniform infinite-iteration gap, Connected
Unit-Window Coercivity, historical Strong Terminal, Object X or RH
claim follows.

Concurrent commit `829019d7e62f936ab4db903bb9c7758edf427609` is preserved:
its different shrinking-step chain retains a positive uniform gap floor
on a smaller endpoint band. Our halving example does not weaken that
result. This package's distinct advances are the larger actual window
and conditional estimates through b<=1 including channel 7.

From the repository root, using Python standard library only:

```text
python -B research/x-c1/all-parity-window-and-restart-2026-09-19/check_restart.py --verify
```

The run replays both parent matrix certificates and their entire inherited
chain, plus 349 universal-family regressions; it can take several minutes.
It passes 88 new exact checks, binds 95 inputs and verifies byte-identical JSON/log and seven payload
hashes. Read `PROOF.md` for the analytic arguments and precise scope,
`STATUS_DE.md` for the German status. Reproduction is not external audit.
