# P12 Adversarial Audit — A15.1 b2d Parameter Wedge

**Datum:** 2026-08-22 (Runde 10, `HEAD = 77c0c34 + this commit`)
**Modul:** `papers/P12_sections/P12_A15_1b2d_ParameterWedge.tex`
**Ziel:** Voller Kernel-Trivialitätssatz auf zweidimensionaler b2d-Teilregion.

## Status

`✓[M]` — genuiner b2d-Teilsatz. **Kein** full b2d.

## Behauptung

Auf dem Parameter-Wedge

$$
e/2 \le R < d/2, \quad R < \sigma < \varepsilon < \varepsilon_{\max}, \quad \sigma \le d/2, \quad \sigma \le R + \eta
$$

gilt $\ker L_{R,S,T_0}^{\{a,b,2a\}} = \{0\}$, wobei $\eta = e - 2\delta = \tfrac12 \log(256/243)$.

## Wedge ist nicht leer

- Bei $R = e/2$: $R + \eta = e - \delta = \kappa$. Elementar $\kappa < d/2$ via $2\kappa < d \iff 4a < 7d \iff 11 \log 2 < 7 \log 3 \iff 2^{11} < 3^7 \iff 2048 < 2187$.
  Also bei $R = e/2$: bindende Grenze ist $\sigma \le R + \eta = \kappa$; $\sigma$-Streifen der Breite $\eta \approx 0.026$ ist nicht leer.
- Bei $R$ nahe $d/2$: $R + \eta$ wächst mit $R$; bindende Grenze ist $\sigma \le d/2$. $\sigma$-Streifen $(R, d/2]$ wird schmaler aber bleibt nicht leer.
- Konkret bei $R = 0.085$, $\sigma \in (0.085, 0.101]$: passt.

## Beweisstruktur — 5 Schritte

### Step 1: $C_{19}$ deckt $(R, \sigma)$ ganz

- $\sigma \le d/2 \Rightarrow d - \sigma \ge \sigma$.
- $\sigma \le R + \eta$ direkt.
- Also für $x \in (R, \sigma)$: $x < \min\{\sigma, d-\sigma, R+\eta\}$ (= $\sigma$).
- Theorem `thm:p12-b2d-core-single-slice` anwendbar an jedem $x$.

**Kritischer Punkt**: Vollrang $\det M_{19} \ne 0$ erzwingt den ganzen Visibility-Vektor $v = 0$, nicht nur $h(x)$. Insbesondere:
- $l(x) = h(T-x) = 0$
- $h(e+x) = 0$

Beide Werte sind in den 19 aufgezählten Visibility-Positionen enthalten (siehe Runde 9 Audit, Tabelle Zeilen 5 und 6).

### Step 2: $H(x) = 0$ auf $(R, \sigma)$ via P1

- $x \in (R, \sigma)$: $d - x > d - \sigma \ge \sigma$, also $H(d-x) = 0$ (Support).
- P1 (`thm:p12-P1`): $H(x) + l(x) + (2r/p) H(d-x) = 0$.
- $l(x) = 0$ (Step 1), $H(d-x) = 0$: also $H(x) = 0$.

### Step 3: $(E_0)$ homogen auf ganz $(R, a)$

- Auf $(R, \sigma)$: $H(x) = 0$ (Step 2), Tail-Term verschwindet.
- Auf $(\sigma, a)$: $\mathbf 1_{x < \sigma} = 0$, Tail-Term verschwindet.
- Also $(E_0)$: $p h(x) + r \operatorname{sgn}(x-d) h(|x-d|) - q h(a-x) = 0$ auf $(R, a)$.

**b2b-Beweisstruktur Steps 1-5** greifen verbatim, unter:
- $R < e$: elementar via $R < d/2 < e$, wobei $d < 2e$ (elementar $27 < 32$).
- $e/2 \le R$: Voraussetzung.
- $R > \delta$: via $R \ge e/2 > \delta$, elementar $e > 2\delta$ (i.e. $27 > 16$).

Ergebnis: $h = 0$ auf $(R, a)$.

**b2b-Step 6** (der einzige Step in b2b, der $\sigma \le R$ braucht) wird **nicht** benutzt. Stattdessen kommt der kleine Tail in Step 4.

### Step 4: kleiner Tail $H = l = 0$ auf $(0, R)$

Für $0 < t < R$: $t < \varepsilon$, also P1/P2 gültig.

Die drei $h$-Werte in $D(t) = (p^2 - q^2 - r^2) h(t) + qr[h(e-t) - h(e+t)]$:

- $h(t) = 0$: $t < R$ (Support).
- $h(e+t) = 0$: $e + t \in (e, e+R)$. $e > R$ (aus $R < d/2 < e$). $e + R < a$ (aus $R < d$). Also $e + t \in (R, a)$, wo $h = 0$ nach Step 3.
- $h(e-t) = 0$: entweder $e - t < R$ (Support) oder $e - t \in [R, e) \subset (R, a)$, wo $h = 0$.

Daher $D(t) = 0$, und P2 (`thm:p12-P2`): $H(t) - l(t) = 2 D(t)/p^2 = 0$, also $H(t) = l(t)$.

Ferner: $d - t > d - R > d/2 \ge \sigma$ (aus $R < d/2$). Also $H(d - t) = 0$.
P1: $H(t) + l(t) + (2r/p) H(d-t) = 0$, also $H(t) + l(t) = 0$.

Zusammen: $H(t) = l(t) = 0$ auf $(0, R)$.

Mit Step 2: $H \equiv 0$ auf $(0, \sigma)$. Der ganze Tail $(T, S)$ ist weg.

### Step 5: Reduktion auf b1

- $h$ jetzt in $(R, T)$ getragen.
- $L_{T_0} h = 0$ gilt weiter (weggenommene Werte waren null).
- Theorem `thm:p12-b1` in Allgemeinheit $2a < T_0 < c$, $0 < R < T$, $S = T$: gültig da $R < d/2 < T$.
- Also $h = 0$.

## Verifikations-Skript

`consolidation/round10_parameter_wedge.py` — numerische Prüfung aller 5 Steps an Testpunkt $R = 0.085$, $\sigma = 0.099$, $\varepsilon = 0.11$. Alle Steps checken.

## Elementare Ungleichungen

Alle im Beweis benutzten sind aus dem P12-Bestand oder elementar:

| # | Ungleichung | Reduktion |
|---|-------------|-----------|
| $\eta > 0$ | | $256 > 243$ |
| $\kappa < d/2$ | Wedge-Nichtleere bei $R = e/2$ | $2048 < 2187$ |
| $R < e$ | $R < d/2 < e$, i.e. $d < 2e$ | $27 < 32$ |
| $R > \delta$ | via $R \ge e/2 > \delta$, i.e. $e > 2\delta$ | $27 > 16$ |
| $e > R$ | via $d/2 < e$ | $27 < 32$ (dieselbe) |
| $e + R < a$ | via $R < d$ | trivial ($R < d/2 < d$) |
| $\alpha > 1$ | b2b-Lemma | schon bewiesen |
| $F < 0$ | Runde-8-Lemma | schon bewiesen |

## Was ist NICHT bewiesen

- $\sigma > d/2$: case-B-Regime, sowohl $H(x)$ als auch $H(d-x)$ live an $x \sim d/2$.
- $\sigma > R + \eta$: post-$\eta$-Visibility-Wall, $h(x - \eta)$ wird live in $Q_{18}$.
- Full b2d bleibt Open Problem.

## R14-Firewall

Bleibt intakt. Kein Satz überschreitet M→PG. Alles strikt M-Schicht.

## Repo

- HEAD nach Runde 9: `77c0c34` (b2d-core-single Slice-Theorem).
- Nach diesem Commit: Parameter-Wedge-Theorem als eigenständige Section.
- CI: erwartet SUCCESS.
