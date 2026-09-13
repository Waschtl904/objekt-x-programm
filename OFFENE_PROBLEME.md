# Offene Probleme — aktuelle POS-DIL-Priorität

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [AKTUELLER_STAND](00-uebersicht/AKTUELLER_STAND.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md), [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).
>
> Fixed-pair Strong Terminal/C6 ist im ausgewiesenen ungeraden P11-Scope verfügbar. OX-GEN-A und POS-DIL-1 sind im dokumentierten Scope geschlossen. Die unit-gain FEATURE-SHORTING-Klasse von POS-DIL-2A ist bei `a=1/2` exakt ausgeschlossen. Operative Hauptfront: **POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION**.

---

## Geschlossen: OX-GEN-A `✓[M]`

Mit

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle
```

sind Prime-Kanäle und Suzukis `r_0` zwei Funktoren derselben zweidimensionalen Translation-/Reflexions-Geometrie.

Prime-only-A2 aus `{w_n,lambda_n}` bleibt `×[M]` im dokumentierten engen Scope.

---

## Geschlossen: POS-DIL-1

### `[POS-DIL-1A]` Symmetrierigider Companion `✓[M]`

Mit `S=D_n/lambda_n=2rho'(0)` zwingen

```math
PMP=M,
\qquad SMS=M
```

die Form `M=tI`; minimale Blockpositivität liefert `M_min=I`.

### `[POS-DIL-1B]` Volle positive rho-Invarianz `×[M]`

```math
\rho(t)^*M\rho(t)=M\ \forall t,
\qquad M\succeq0
\Longrightarrow M=0.
```

### `[POS-DIL-1C]` Prime-moment Hilbertisierung `✓[M]`

```math
V_Nv=\kappa_N^{-1/2}
(\sqrt{w_n}\,\mathcal EK_nv)_{n\in N},
\qquad
\kappa_N=\sum_{n\in N}w_n\lambda_n^2.
```

Dann

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

`OX-GEN-A2'` insgesamt: `✓[M]_part`.

---

## Geschlossen: POS-DIL-2A / unit-gain FEATURE-SHORTING `×[M]`

Der vorab definierte Test

```math
\|\mathcal Ev\|^2\stackrel?\le G_a^+(v)
```

fällt bei `a=1/2`.

Für eine explizite gerade Plateaufolge `v_epsilon in H_0^1(-1/2,1/2)` gilt

```math
|R_0(v_\varepsilon,v_\varepsilon)|
=\|\mathcal Ev_\varepsilon\|^2
\to32\sinh^2\frac14,
```

während

```math
G_{1/2}^+(v_\varepsilon)
\to1+\sqrt2(\log2)^2.
```

Exakt:

```math
32\sinh^2\frac14>2>
1+\sqrt2(\log2)^2.
```

Daher ausgeschlossen:

- kontraktives `C F^+=V` mit `||C||<=1`;
- jedes Target-observable `A` mit `||A||<=1`, `R_0=<F.,AF.>` und `||Fv||^2=G_{1/2}^+(v)`;
- unit-diagonaler positiver Schurblock mit `G_{1/2}^+` und Kreuzform `R_0`.

Kanonische Quelle: `audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md`.

---

## Geschlossen: notwendiger Plateau-Massendefekt `✓[M]`

```math
\boxed{
\delta_0
=32\sinh^2\frac14
-1-\sqrt2(\log2)^2
>\frac5{32}>0.
}
```

Jede positive Zusatzform `H`, die nach Augmentation `G_{1/2}^++H` eine unit-gain Realisierung tragen soll, muss notwendig

```math
\liminf_{\varepsilon\downarrow0}
H(v_\varepsilon,v_\varepsilon)
\ge\delta_0
```

liefern.

---

## Priorität 0 — POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION `?[O]`

Frage:

> Welche schwächste **intrinsisch aus bereits vorhandener Geometrie erzeugte positive Zusatzmasse** kann den nachgewiesenen Defekt `delta_0` liefern und `R_0` im selben positiven Umraum tragen?

Zulässige Kandidateninputs:

- AR(1)-Root/Hub-Komponente `u_k=q_p^k`;
- Prime-moment-Komplement `1-u_k`;
- globale Prime-Kanäle außerhalb des lokalen Suzuki-Cutoffs, die auf dem Fenster reine lokale Masse tragen;
- bereits vorhandene positive `log|D|`-Featuregeometrie.

Anforderungen an eine positive Lösung:

1. Zusatzmasse vorwärts aus vorhandenen Daten erzeugen;
2. am Plateau-Gate `a=1/2` mindestens `delta_0` liefern;
3. `R_0` im selben positiven Umraum realisieren;
4. keine beliebige Diagonalergänzung;
5. saubere Buchungsrichtung gegenüber dem weiterhin offenen `c_aI`-Block.

Ein negatives Resultat zählt nur für eine **vorab definierte** natürliche Augmentationsklasse.

---

## Priorität 1 — OX-GEN-B `?[O]`

- `[OX-R1]` regulärer `r_1''`-Korrektor;
- `[OX-SCALAR]` dominanter Skalarblock `c_aI`.

POS-DIL-2A beweist, dass zusätzliche positive Masse nötig ist, aber identifiziert deren Quelle **nicht**. Insbesondere darf `delta_0` nicht still mit `c_aI` gleichgesetzt werden.

---

## Priorität 2 — vollständiger Objekt-X-Pfad

- `[OX-CANDIDATE]` Genuine X candidate `?[O]`;
- `[OX-WEIL-GRAM]` exakte volle Weil-Gram-Identität `?[O]`;
- `[OX-REALIZATION]` Object-X-Realisierung `?[O]`;
- `[OX-WEIL-SCOPE]` Weil-Kriterium-Scope `?[O]`;
- `RH` `?[O]`.

---

## Spur B

`[AR1-WRITEUP]` Prime-Power-AR(1)/Martingal-Faktorisierung theorem-ready, RH-unabhängig und ausdrücklich nicht als Objekt X verschriftlichen.

---

## Separate / geparkte Probleme

- R37/G4c `?[O]` separat offen.
- Historische R43-COND-/FD23-/Flagfragen: eigene Quantoren, nicht Default-Priorität.
- PR #91: analytischer Draft ohne übertragenes unabhängiges Exact-Head-GREEN.
- PR #49 / SW1 salvage: Candidate-only, kein stiller Merge.

---

## Nicht erneut öffnen ohne neuen Widerspruch

- fixed-pair Strong Terminal/C6 im dokumentierten ungeraden Scope;
- OX-GRAM-Existenzfrage als zirkuläres/vakuantes X-Gate;
- CERT-HARDEN im dokumentierten endlichen Scope;
- OX-GEN-A;
- Prime-only-A2 im engen Scope;
- POS-DIL-1A/B/C;
- POS-DIL-2A unit-gain Shorting bei `a=1/2`.

---

## Gesperrte Altdeutungen

Nicht reaktivieren: PR91 Rang-1-Zeugenmatrix; `3/4` als freie Dämpfung; Vier-Boundary-Erklärung; cross-prime als Boundary; „Nichtunitarität = Hub“; matched cutoff / OX-REN; klassische `H^{1/2}`-Deutung des `1/|x-y|`-Kerns; `0.603` als Konstante; reine OX-GRAM-Existenzsweeps; Prime-Gram auf dem Rang-2-Quotienten ohne Zusatzstruktur; Behauptung, POS-DIL-1 erkläre bereits `r_1` oder `c_aI`; Behauptung, POS-DIL-2A sei ein globaler No-Go gegen positive Erweiterungen.
