# X-C1 FULL-RESIDUAL-SCHUR — Gamma rescue at a=0.3930110

Date: 2026-09-17
Status: `AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN`
Parent: corrected Node-Schur commit `9aa5cb1edac72fc683c5c9aba5a1f0639fbbf8bb` on PR #137.
Scope: the full connected NULLPOL class W_a = H^1_0((-a,a);C) intersect ker(E_+) intersect ker(E_-), with a=393011/1000000.
No A1 import, no third Mellin condition, no numerical-eigenvalue or quadrature proof.

## Result

At this same endpoint the corrected optimized Node-only full even gap is already strictly negative. Retaining a controlled part of the previously unused nonconstant Gamma residual restores positivity:

`Q_W[u] > (1/4000) ||u||_2^2` for every nonzero u in W_a.

The positive Prime-2 difference residual is not needed and remains unused reserve.

## Gamma residual

Put L=2a and

`R_Gamma[u] = integral_{x<y} r_a(y-x) |u(y)-u(x)|^2 dx dy`,
`r_a(t)=g(t)-g(L)`, `g(t)=h(t)-1/(2t)`.

Both R_Gamma and the Prime-2 difference form annihilate the constant mode e_0 exactly. Adding them therefore creates no new Mellin-moment penalty.

For normalized `e_2(x)=sqrt(5/L) P_2(x/a)` one has exactly

`integral_{-a}^{a-t} |e_2(x+t)-e_2(x)|^2 dx = 60 t^2 (L-t)^3 / L^5`.

The analytic waxing lemma gives g'(t)<0 on (0,2]. Hence for 0<t<=L/2,
`r_a(t) >= g(L/2)-g(L)`, and therefore

`R_Gamma[e_2] >= (21 L / 32) (g(L/2)-g(L)) > 1/100`.

The checker gets g(L) from the already certified Node intervals through
`h(L)=(lambda_2+C-1)/L`, and encloses g(L/2) by an exact rational alternating series.

Since g(0+)=1/4 and g decreases,
`0 <= r_a(t) <= 1/4-g(L)`. The graph-Laplacian estimate then gives

`R_Gamma[u] <= 2 L (1/4-g(L)) ||u||^2 < (27/500) ||u||^2`.

## Infinite-dimensional Schur step

Use only the fraction s=2/5 of R_Gamma. Write `x=alpha e_2+y`, where y belongs to the closed even tail span of e_4,e_6,... . Positivity gives

`R_Gamma[alpha e_2+y] >= s |alpha|^2 R_Gamma[e_2] - s/(1-s) R_Gamma[y]`.

Thus the even-tail floor becomes

`delta_Gamma = delta - s/(1-s) ||R_Gamma|| > 99/200`.

For the Node part take the fixed rational split theta=18/25 and mu=theta*m. The only constant-mode penalty is

`K = C + theta/(1-theta) m`.

On C e_2 direct-sum Y_even the remaining block satisfies

`D = delta_Gamma I + mu P_Y P_J P_Y >= delta_Gamma I`,
`b = mu P_Y P_J e_2`.

With p=<e_2,P_J e_2>, the Schur complement obeys

`sigma_full >= lambda_2 + s R_Gamma[e_2] + mu p (1-mu/delta_Gamma)`.

The exact checker proves

`mu < delta_Gamma/2` and `sigma_full > 1/500`.

After square completion,

`eta_full = min(sigma_full,delta_Gamma)/(1+mu/delta_Gamma)^2 > 1/800`.

This is an infinite-dimensional Schur estimate; no finite matrix replaces the tail space.

## Moment transport and normalization

The even NULLPOL condition gives `|u_0|^2 <= beta_e ||x||^2`. Because the Gamma and Prime-2 residuals annihilate e_0, the only u_0 penalty is K|u_0|^2 from the Node split. Hence

`Q_even[u] >= (eta_full-beta_e K) ||x||^2`,

and the checker proves

`eta_full-beta_e K > 3/10000`.

Only now use the norm comparison

`||u_even||^2 <= (1+beta_e) ||x||^2`.

The final division by 1+beta_e is a separate checker step, yielding

`Q_even[u] > (1/4000) ||u_even||^2`.

The odd sector remains `Q_odd[u] > (1/4) ||u_odd||^2` from the corrected parent anchors. Parity therefore gives the announced full NULLPOL gap.

## Certificate and limits

`check_x_c1_full_residual_3930110.py` makes nine exact `fractions.Fraction` PASS decisions: Gamma e_2 floor, Gamma operator norm, reduced tail, mu<delta_Gamma/2, Schur pivot, pre-moment gap, post-moment numerator, final even gap after division by 1+beta_e, and odd gap.

This is a genuine mechanism beyond the corrected Node crossing. It does not prove a global residual-waxing threshold, the Prime-3 regime, the unit window, all-window C1-GEOM, Object X, or RH.
