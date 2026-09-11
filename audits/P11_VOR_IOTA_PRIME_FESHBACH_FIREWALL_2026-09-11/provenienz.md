# Provenienz — Vor-ι′ Rest/Feshbach firewall

This file records the main reconciliation points so that corrected conclusions are not detached from their failure history.

## F1 — old global-source placeholders exposed

The earlier Vor-Δ layout treated `H_A` and `E_{\mathcal A}` as existing P11 data.  Reading `main@a757da3a...` showed that the corresponding global source/adelic/Gram construction is still open.  The old baseline `E_{\mathcal A}|_{D_W^-}` was therefore downgraded to a placeholder.

## F2 — `\Pi_{\mathcal A}` candidate withdrawn

The proposed `L^(1)=\Pi_{\mathcal A}H_{T_0}^*\iota_{T_0}` required a projection/embedding that was not verified as defined `main` data.  The candidate was withdrawn rather than completed by inventing new data.

## F3 — finite-window reset

The search was reset to actual P11 objects at fixed radius.  The useful main-native linear blocks are `\widetilde R_R` and `B_R^{1/2}H_R^*`; they are building blocks, not X-candidates.

## F4 — Rest-Gram coefficient correction

The exact native Rest mixed value is

\[
\langle R_1a,R_1b\rangle=\frac{4-7\sqrt2}{32}\log2.
\]

An intermediate arithmetic note misread `2^{-3/2}` and produced a wrong coefficient.  The corrected value was independently reproduced.

## F5 — lobe normalization and collision bugs

The first Feshbach moment implementation missed the source factor `1/sqrt(2)` and mishandled the `p=5` collision at `u=0`.  Correct treatment accumulates equal-position amplitudes before squaring; the `p=5` pair cancels exactly.

The corrected symbolic engine reproduces the closed `m_0(v_\pm)` formulas.

## F6 — Rest versus Hub cutoffs separated

An early `m_1` implementation risked importing the Hub cutoff `p^k<=e^{2R}` into the Rest sum.  P11's `Phi_{p,a,R}` instead has its own `k>=a+1` sum, made effectively finite by `E_R` and the `Omega` window.  After synchronizing this convention, all `m_1` sectors reproduced.

## F7 — `R_1^*R_1` derived before implementation

`m_2` was not computed by running the sector-norm routine twice.  Using `D_s^*=-D_s` and `K_s^{tr}=P_1D_sE_1`, the intermediate `Omega` zero extension was kept explicitly and `A=R_1^*R_1` was implemented as the adjoint composition.  The check `<v,Av>=m_1(v)` then closes.

## F8 — bilinear-form and target-notation corrections

An intermediate note incorrectly identified a polarized `m_1(v_+)-m_1(v_-)` quantity with `<R_1a,R_1b>`; the contradiction with the already certified Rest value exposed the type error.

A separate transcription/rendering mistake wrote the Weil target as `-log 2/2`; the correct PR-#91 target throughout the final proof is

\[
-\frac{\log2}{\sqrt2}.
\]

## F9 — rational hardening and governance

The final Feshbach separation is expressed both through the reproduced moment interval and through an exact rational implication from five coarse moment inequalities.  The latter removes floating-point arithmetic from the **last separation step**, while explicitly not pretending to interval-certify the moment inputs by itself.

Governance is likewise separated:

`pre-push package audit -> Draft PR -> remote SHA/byte verification -> exact-head review -> merge decision`.

No registry promotion or merge is implied by publication of the Draft PR.
