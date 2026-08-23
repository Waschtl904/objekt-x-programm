# P12 Runde 22 — Promotion

**Status:** `✓[M]` — all-R restricted-tail theorem after independent GREEN review.  
**Reviewed commit:** `17e911dc27fd95b55f8a91f8e16887bd6e385f93`.  
**Repo review basis:** `main@cddc6c5793f18a3dc02f65697063b395c9f7d897`.  
**Firewall:** P11 FROZEN. R14 unchanged. No Polar Gauge, Strong/Terminal Transport, Object X, or RH implication.

## Promoted theorem

Let
\[
T=2a,\qquad 2a<T_0<c,\qquad
\sigma:=S-T,\qquad \varepsilon:=T_0-T,
\]
with
\[
0<\sigma<\varepsilon<\varepsilon_{\max}.
\]
Then
\[
\boxed{
0<R<T,\qquad 0<\sigma\le R
\Longrightarrow
\ker L_{R,T+\sigma,T_0}^{\{a,b,2a\}}=\{0\}.
}
\]

Thus the restricted-tail sector has no positive lower-radius threshold.

## Independent review record

Perplexity independently loaded the committed Round-22 files from GitHub and reran the retained verifier in a separate Python/SymPy environment. It reproduced

```text
ROUND22_RESTRICTED_TAIL_ALL_R_STRUCTURAL_STRESS = PASS 500000
rho is not used as an R lower bound; rho = 0.05268025782891303
```

It also independently checked the four constant comparisons used by the proof:

\[
\varepsilon_{\max}<e,
\]
\[
a-\varepsilon_{\max}>d,
\]
\[
d-\varepsilon_{\max}>e/2,
\]
\[
d-e/2>e/2.
\]

The reviewer returned **GREEN** and confirmed that the assumption
\[
R\ge\rho
\]
is unnecessary throughout the restricted-tail regime \(\sigma\le R\).

## Booking

Round 22 is promoted from review candidate to
\[
\boxed{\checkmark[M].}
\]

Consequently, for future low-radius work the sector
\[
\sigma\le R
\]
is closed for every \(R>0\). The only genuinely low-radius mixed-strip geometry still requiring new work is the overlap sector
\[
\sigma>R.
\]
