# CURRENT FRONT — Objekt X / POS-DIL

> **Operative Kopfschicht — zuerst lesen.**
> **Redaktioneller Stand:** 13. September 2026; keine Registry-Promotion.
> **Konsolidierungsquellen:** [AR(1)/Weil-Tail/OX-GRAM](audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md), [Gate-2/OX-GEN](audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md), [OX-GEN-A](audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md), [POS-DIL-1](audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md), [POS-DIL-2 Unit-Gain No-Go](audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md).
> **Strategie:** [kanonische Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md).
> **Suchgegenstand:** [Objekt-X-Arbeitsdefinition](00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).
> **Buchungen:** [Theorem-/Review-Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

Diese Datei ordnet die Arbeit; sie beweist nichts. Der aktuelle `main`-Head und PR-Zustände werden live aus GitHub gelesen. Bei Konflikten ist die kanonische mathematische Quelle im benannten Scope maßgeblich.

## 1. Verfügbarer Strong-Terminal-Baustein

Der integrierte positive Wurzelanker plus R42.51 liefert Strong Terminal/C6 für jedes **feste** `0<R<S` im **ungeraden P11-Graphraum**.

**Scope:** keine Radienuniformität, keine Operatornormkonvergenz, kein gerader Gesamtsektor, keine vollständige Objekt-X-Realisierung und keine RH-Folgerung.

## 2. Prime-Power-/AR(1)-Struktur

Exakt:

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2},
```

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q,
```

und die P11-Restseite besitzt die exakte Weil-Tail-Normalform.

Cross-prime Root-Gram ist fensterloser Bulk, kein Boundaryterm.

## 3. Endliche Suzuki-/OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

Die bloße Existenz eines kontraktiven Faktors ist als Objekt-X-Gate zirkulär/vakuant. Offen ist eine **vorwärts konstruierte kanonische** gemeinsame Geometrie.

CERT-HARDEN ist im dokumentierten endlichen Scope geschlossen; dies ist kein globaler Positivitäts-/RH-Beweis.

## 4. OX-GEN-A — gemeinsamer Exponentialgenerator `✓[M]`

Mit

```math
\mathcal Ev=(E_+(v),E_-(v)),
\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}),
```

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
D_n=\lambda_n\operatorname{diag}(-1,1),
```

gilt

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E.
```

Suzukis elementarer archimedischer Teil erfüllt

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
r_0(\log n)=-4\lambda_n^2.
```

Mit `P=[[0,1],[1,0]]`, `J=-P`:

```math
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle.
```

Prime-only-A2 aus `{w_n,lambda_n}` bleibt `×[M]` im dokumentierten engen Scope.

## 5. POS-DIL-1 — positiver Prime-moment-Quotientenbaustein

Setze

```math
S=\operatorname{diag}(-1,1)=D_n/\lambda_n=2\rho'(0).
```

### 5.1 Companion-Rigidität `✓[M]`

```math
PMP=M,
\qquad SMS=M
```

zwingt für Hermiteformen

```math
M=tI.
```

Die Blockpositivität

```math
\begin{pmatrix}M&J\\J&M\end{pmatrix}\succeq0
```

ist genau für `t>=1` möglich. Minimaler positiver Begleiter in dieser Klasse:

```math
\boxed{M_{\min}=I.}
```

Volle positive `rho`-Invarianz erzwingt dagegen `M=0`; die exakte unitäre Same-space-Hilbertisierung der Boost-Darstellung ist `×[M]` im engen Scope.

### 5.2 Prime-moment Hilbertisierung `✓[M]`

Für eine endliche nichtleere Prime-Power-Menge `N`:

```math
\kappa_N=\sum_{n\in N}w_n\lambda_n^2,
```

```math
V_Nv=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}.
```

Dann

```math
\boxed{\|V_Nv\|^2=|E_+(v)|^2+|E_-(v)|^2,}
```

und mit `\mathbb P_N=\oplus P`

```math
\boxed{R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.}
```

Für `n=p^k`, `q_p=p^{-1/2}`:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

`OX-GEN-A2'` bleibt insgesamt `✓[M]_part`.

## 6. POS-DIL-2A — unit-gain FEATURE-SHORTING ausgeschlossen `×[M]`

Der nach POS-DIL-1 vorab definierte Gate

```math
\|\mathcal Ev\|^2\stackrel?\le G_a^+(v)
```

fällt bereits bei

```math
a=\frac12.
```

Für die geraden Plateau-Funktionen `v_epsilon in H_0^1(-1/2,1/2)`, die gegen `1_{(-1/2,1/2)}` konvergieren, gilt exakt:

```math
\mathcal D(v_\varepsilon)\to0,
```

```math
|R_0(v_\varepsilon,v_\varepsilon)|
=\|\mathcal Ev_\varepsilon\|^2
\longrightarrow
32\sinh^2\frac14,
```

während bei `a=1/2` nur der Prime-Kanal `n=2` aktiv ist und

```math
G_{1/2}^+(v_\varepsilon)
\longrightarrow
1+\sqrt2(\log2)^2.
```

Elementar:

```math
32\sinh^2\frac14>2>
1+\sqrt2(\log2)^2.
```

Daher existiert für alle hinreichend kleinen `epsilon` die strikte Verletzung

```math
\boxed{
|R_0(v_\varepsilon,v_\varepsilon)|
>G_{1/2}^+(v_\varepsilon).
}
```

### Konsequenzen `×[M]`

Es gibt bei `a=1/2` weder

1. einen Kontraktor `C` mit
   ```math
   CF_{1/2}^+v=V_{N_{1/2}}v,
   \qquad \|C\|\le1,
   ```
   für eine exakte Hilbert-Featureabbildung `||F_{1/2}^+v||^2=G_{1/2}^+(v)`, noch
2. allgemeiner einen Target-Operator `A` mit `||A||<=1`, so dass
   ```math
   R_0(v,w)=\langle Fv,AFw\rangle
   ```
   bei `||Fv||^2=G_{1/2}^+(v)` gilt, noch
3. einen positiven unit-diagonalen Schurblock mit `G_{1/2}^+` auf beiden Diagonalen und `R_0` als Kreuzform.

Dies ist ein Klassen-No-Go für die **bestehende** positive Featuremasse, nicht gegen POS-DIL-1 oder jede positive Erweiterung.

## 7. Exakter notwendiger Massendefekt `✓[M]`

Definiere

```math
\boxed{
\delta_0
=32\sinh^2\frac14
-1-\sqrt2(\log2)^2>0.
}
```

Die elementaren rationalen Schranken liefern sogar

```math
\delta_0>\frac5{32}.
```

Jede zusätzliche positive Form `H`, die eine unit-gain Realisierung nach Augmentation `G_{1/2}^++H` tragen soll, muss entlang der Plateaufolge notwendig

```math
\liminf_{\varepsilon\downarrow0}H(v_\varepsilon,v_\varepsilon)
\ge\delta_0
```

liefern.

## 8. Neue operative Hauptfrage: POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION

Die bestehende lokale positive Featureform ist bei `a=1/2` nachweislich zu klein. Gesucht wird jetzt die **schwächste intrinsische zusätzliche positive Masse**, die den Defekt `delta_0` liefert und `R_0` im selben positiven Umraum tragen kann.

Zulässige Kandidateninputs, noch **keine Lösung**:

- AR(1)-Root/Hub-Komponente `u_k=q_p^k`;
- die Prime-moment-Amplitude `1-u_k`;
- globale Prime-Kanäle außerhalb des lokalen Suzuki-Cutoffs, die auf dem Fenster reine lokale Masse tragen;
- logarithmische `log|D|`-Geometrie.

Nicht zulässig als Erfolg:

- beliebige Diagonalmasse von Hand;
- fertige Weilform `Q_{B_a}`;
- RH;
- rückwärts definierte Positivitätswurzel;
- stilles Identifizieren der fehlenden Masse mit `c_aI`.

Beide Ausgänge bleiben offen: intrinsische positive Massenergänzung oder ein weiterer enger Klassen-No-Go.

## 9. Status

```text
OX-GEN-A common generator plane                         ✓[M]
POS-DIL-1 prime-moment Hilbertization                  ✓[M]
POS-DIL-2A unit-gain shorting at a=1/2                 ×[M]
necessary plateau mass deficit delta_0                 ✓[M]
OX-GEN-A2' overall                                     ✓[M]_part
POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION              ?[O]
OX-GEN-B / r_1 / c_aI                                  ?[O]
genuine X candidate / full Weil-Gram / Object X / RH  ?[O]
```

## 10. Governance / Nebenfronten

- Registry bleibt ohne automatische Promotion unverändert.
- PR #91 bleibt analytischer Draft ohne übertragenes unabhängiges Exact-Head-GREEN.
- PR #49 bleibt Candidate-only ohne stillen Merge.
- R37/G4c bleibt separat offen.
- Kein Object-X- oder RH-Abschluss.
