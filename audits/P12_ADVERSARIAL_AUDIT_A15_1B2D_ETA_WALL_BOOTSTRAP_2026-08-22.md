# P12 Adversarial Audit — A15.1 b2d η-Wall Bootstrap

**Datum:** 2026-08-22 (Runde 11)
**Modul:** `papers/P12_sections/P12_A15_1b2d_EtaWallBootstrap.tex`
**Ziel:** Full b2d-core-single local kill + Erweiterung des Parameter-Wedge auf $\sigma \le d/2$.

## Status

- **Theorem `thm:p12-b2d-core-single-full`** (b2d-core-single voll): `✓[M]`
- **Corollary `cor:p12-b2d-wedge-plus`** (Wedge $\sigma \le d/2$ voll): `✓[M]`

**Kein** full b2d — $\sigma > d/2$ bleibt offen (core-both).

## Kernidee

Die Visibility-Wand bei $x = R + \eta$ ist eine **Rückkopplung um genau einen $\eta$-Sprung**:
- Post-wall Q18+ hat den zusätzlichen Term $-r\, h(x - \eta)$.
- Aber $y := x - \eta$ liegt für jedes post-wall $x$ wieder im bewiesenen Slice $C_{19}$.
- Also $h(y) = 0$ per Runde-9, Q18+ kollabiert auf Q18, gleiche $M_{19}$.

## Verifizierte Punkte

### 1. Nur Q18 ändert sich (Slot-by-Slot)

Numerisch (Skript `consolidation/round11_eta_wall_bootstrap.py`) an Testpunkt $R = 0.074$, $\sigma = 0.101$, $x = 0.1005$ (post-wall):

- **Q1-Q17, Q19**: alle Live-Slots identisch zu Runde 9 (numerisch verifiziert).
- **Q18**: 3 Live-Slots statt 2. Neuer Slot ist $-r\, h(0.0744) = -r\, h(x - \eta)$.

Elementare Begründung: Die Support/Horizont-Bedingungen K1-K3 und H1-H5 nutzen $x < d - \sigma$, $x < \varepsilon_{\max}$, $x > R$; **keine** verwendet $R + \eta$. Nur K4 ($x - \eta < R$) tut das.

### 2. Bootstrap $y \in C_{19}$

Für post-wall $x \in W = (R+\eta, \min\{\sigma, d-\sigma\})$:

- $y > R$: aus $x > R+\eta$.
- $y < \sigma$, $y < d-\sigma$: trivial.
- $y < R + \eta$: aus $x < d - \sigma < d - (R+\eta)$, also $y < d - R - 2\eta$. Zusammen mit $R \ge e/2$: es genügt $d - 3\eta < e$, d.h. $7\delta < 3e$.

### 3. Elementare Ungleichung $7\delta < 3e$

$\delta = \tfrac12 \log(9/8)$, $e = \tfrac12 \log(4/3)$.

$$7\delta < 3e \iff (9/8)^7 < (4/3)^3 \iff 3^{17} < 2^{27}$$

Direkt: $3^{17} = 129\,140\,163 < 2^{27} = 134\,217\,728$. **Elementar.**

### 4. Kollaps Q18+ → Q18

Nach $h(y) = 0$ verschwindet der neue Slot. Q18+ = $p\,h(a-2\delta-x) - r\,h(x-\eta) - q\,h(2\delta+x) = 0$ wird zu $p\,h(a-2\delta-x) - q\,h(2\delta+x) = 0$, die alte Q18-Zeile. Gleiche 19×19-Matrix.

### 5. Nichttrivialer post-wall Bereich

$R^* := d/2 - \eta$. Post-wall existiert nur für $R < R^*$. Wir brauchen $R^* > e/2$ (sonst gäbe es keinen $R$-Wert im wedge, wo post-wall auftritt).

$R^* > e/2 \iff \delta > 2\eta \iff 5\delta > 2e \iff (9/8)^5 > (4/3)^2 \iff 3^{12} > 2^{19}$.

Direkt: $3^{12} = 531\,441 > 2^{19} = 524\,288$. **Elementar.**

Der problematische Radiusbereich ist $[e/2, R^*) \approx [0.0719, 0.0753)$, Breite $\approx 0.0034$.

### 6. Erweiterte Runde-10-Propagation (Corollary `cor:p12-b2d-wedge-plus`)

Bei $\sigma \le d/2$: $\min\{\sigma, d-\sigma\} = \sigma$. Volle CS-Kill gibt $l(x) = 0$ auf $(R, \sigma)$. Rest von Runde 10 (Steps 2-5) läuft unverändert:

- Step 2: $H(d-x) = 0$ via $d - x > \sigma$. P1 → $H(x) = 0$.
- Step 3: $E_0$ auf $(R, a)$. b2b Steps 1-5.
- Step 4: kleiner Tail via P1/P2 wie Runde 10.
- Step 5: b1.

**Die Bedingung $\sigma \le R + \eta$ fällt komplett weg.**

## A.e.-Behandlung

- $x = R + \eta$ ist Randpunkt (Maßnull).
- Translation $x \mapsto x - \eta$ ist Maß-erhaltend.
- $h \in L^2$: alle punktweisen Aussagen bis auf Maßnull.
- Kein Problem.

## Was jetzt offen bleibt

- $\sigma > d/2$: **core-both**-Stratum. Bei $x \sim d/2$ sind sowohl $H(x)$ als auch $H(d-x)$ live-tails.
- Corollary `cor:p12-P1-caseB` diagnostiziert dies bereits: die $2 \times 2$-Kopplung ist zwar nicht-degeneriert, aber $l(x), l(d-x)$ sind nicht null.
- Full b2d bleibt Open Problem.

## Was NEU $\checkmark[M]$ ist

- **Full b2d-core-single local kill**: $h = 0$ auf $(R, \min\{\sigma, d-\sigma\})$ für alle $e/2 \le R < d/2$, $R < \sigma < \varepsilon < \varepsilon_{\max}$.
- **Voller Kernel-Trivialitätssatz** auf $\{e/2 \le R < d/2, R < \sigma \le d/2, \sigma < \varepsilon < \varepsilon_{\max}\}$.

## R14-Firewall

**Bleibt intakt.** Kein Satz überschreitet M→PG. P11 unverändert.

## Repo

- HEAD nach Runde 10: `e6721f3`.
- Nach diesem Commit: Full core-single + erweiterte Wedge-Corollary.
- CI: erwartet SUCCESS.
