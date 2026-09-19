# Reduced trace quotient coordinates

2026-09-19 — **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

This package isolates the formal quotient step required after the full-shell pivot package `6f24422...`.

The unreduced completed coordinates have the exact gauge kernel

`span{(-psi,e)}`,

where `psi` is the moment-corrected trace mode and `e=(1,0)` is the completed shell trace coordinate. The package chooses the canonical `L2` gauge slice

`K_B^0 = K_B intersect psi^perp`

and proves that

`(K_B direct-sum X) / span{(-psi,e)}  ~=  K_B^0 direct-sum X`.

No physical source is removed and no Mellin condition is added. The reduced physical map retains the parent's norm bounds `1/32` and `65`.

The remaining even all-source gate is the single relative coupling number

`Theta_0(b) = sup |C_0(w,z)|^2 / (A_0[w] D[z])`.

If `Theta_0(b) <= theta_0 < 1`, then

`Q_b[u] >= (1-sqrt(theta_0))/(2080*10^13) ||u||_2^2`

on the even sector of the already certified tiny shell interval.

The package does not prove `Theta_0<1`, a new endpoint, or an odd-sector continuation.
