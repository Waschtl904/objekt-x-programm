# P11 R43 external destructive review reconciliation — PR #53 / `c7c6f04c...`

Date: 2026-09-03

## Purpose

Record the user-supplied Perplexity destructive review of the hardened R43 GC-AC layer with
exact-head scope and without silently propagating its verdict to later commits.

This is a provenance / governance record.  It does not itself alter the mathematical proof.

## Exact external review scope

Reviewer/system: **Perplexity**, supplied by the user as the designated external reviewer.

Exact reviewed PR head:

[
oxed{	exttt{c7c6f04cd601ea868cb536327504f6c90b3f0807}}
]

Exact reviewed R43 mathematical blob reported by the reviewer:

[
oxed{	exttt{74a91c71b8b08f60d448811c57ceeca6f6113c87}}
]

The review reports destructive GREEN verdicts for:

1. Szegő (Rightarrow T(r)	oinftyRightarrow L_Q<infty);
2. the non-PW unit-interval estimate and the scope firewall for Makarov--Poltoratski
   Theorem 3.6;
3. realization-independence of scalar nest multiplicity;
4. the atomless scalar-measure extension R43.10bp0;
5. the all-(m) holomorphy argument R43.10cq0--R43.10cs;
6. the measure argument R43.10cu--R43.10cw;
7. absence of hidden Hamiltonian-uniqueness / determinant-normalization assumptions.

The reviewer additionally recommends one presentation hardening: state explicitly why the
fixed form domain embeds continuously in (L^2(-1,1)).  That sentence is now incorporated
in the later R43 mathematical hardening.

## Governance classification

The review explicitly says that it reused destructive vectors from a previous turn.  Under
the repository's current definition of `independent GREEN (cross-model)`, a review session
which already knows the target argument / prior review thread is **nonblind** and does not
qualify for the formal cross-model subtype.

Accordingly the correct booking is

[
oxed{
	ext{external destructive GREEN (Perplexity, cross-model nonblind)}
}
]

on exactly (	exttt{c7c6f04c...}) and the seven scopes above.

It is **not** booked as formal `independent GREEN (cross-model)`, and it creates no
(checkmark[M]), freeze, Strong-Terminal, Object-X, or RH promotion.

## Head firewall

Git comparison shows that the active PR branch subsequently advanced ten commits beyond the
reviewed head.  Therefore the external verdict does not cover the later GC-AC wording repair,
the explicit null-support measure step, or the (b_U)/B-TIGHT/B-SIGN mathematics added after
(	exttt{c7c6f04c...}).

The post-review mathematical hardening is recorded separately and remains AI-reviewed /
candidate-level until an exact-head external recheck is obtained.

## Consequence for the active front

The external review substantially strengthens confidence in the terminal-free Gamma layer,
but the current live Strong-Terminal front remains:

[
	extbf{B-TIGHT}
quad+quad
	extbf{B-SIGN / B-ORIENT}.
]

The current coefficient

[
b_U=langle W_{R,S}^{[U]}arepsilon_R,arepsilon_Sangle
]

is a transport matrix coefficient.  No present theorem identifies it with an
Aleksandrov--Clark or canonical-system boundary parameter; such an identification would
itself require proof before Clark stability can be invoked.
