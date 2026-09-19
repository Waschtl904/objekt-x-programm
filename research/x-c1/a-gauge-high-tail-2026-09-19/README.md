# A-gauge high-tail contraction

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 2026-09-19.

For `B=log(5)/2` and the full structural interval `0<h=b-B<=10^-20`, this
package binds the endpoint tail provenance and proves the complete A-gauge
high-tail block bound

`G_HH <= 63/73 I < I`.

The tail is the physical image of the even endpoint Mellin reconstruction
of all Legendre modes of degree at least 64. The pinned endpoint certificate
gives `even_tail_floor=0.71944862845...`; after its norm factor this implies
a physical core floor `a[f]>(7/10)||f||^2`.

Intersecting with the A-gauge core and the energy-orthogonal complement of
the fixed near-null direction yields

`F_A = span{v_A} direct-sum_a L_A direct-sum_a H_A`, with `dim L_A<=31`.

The high-tail proof uses the exact prime weights `Lambda(q)/sqrt(q)`, a
sharpened full Carleman+prime coefficient below `6.62`, the negligible shell
moment correction, and the already proved shell floor `2 log(2/h)-19`.
It includes the entire infinite coretail and complete shell. The inherited
Near/High mixed block is also bounded by Gram positivity.

This is a WIDTH-AMPLIFICATION structural result, not an all-source theorem
at `h=10^-20`. The remaining gate is the finite `L_A` block together with
Near/Low and Low/High interactions and the norm of the complete block Gram.
No odd result, PR, merge, or main change is claimed.
