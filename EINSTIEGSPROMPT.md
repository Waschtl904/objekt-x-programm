# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**
> Dieser Text ist der operative Einstieg für eine neue Session. Ältere Stände sind über Git erhalten und nicht als heutige Arbeitsanweisung zu verwenden.

## Kopierbarer Arbeitskontext

Ich arbeite am Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor und Research Assistant. Prüfe zu Beginn den aktuellen `main`-Stand direkt im Repository. Verwende kanonische mathematische Quellen vor älteren Navigations- oder Archivdokumenten. Keine Behauptung darf durch einen Merge oder einen positiven numerischen Test still promotet werden.

### Kanonische operative Quellen

Lies in dieser Reihenfolge:

1. `CURRENT-FRONT.md`
2. `00-uebersicht/AKTUELLER_STAND.md`
3. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
4. `00-uebersicht/DAG.md`
5. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`
6. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`

Für den aktuellen mathematischen Strang zusätzlich:

- `audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md`
- `audits/P11_OX_GRAM_GATE2_AND_OX_GEN_2026-09-12.md`
- `audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md`
- `audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md`
- `audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md`

### Governance

Für **Objekt X** übernimmt ChatGPT sämtliche GitHub-/Repository-Arbeiten. Perplexity dient ausschließlich als externer Reviewer/Auditor und nimmt keine Repo-Mutationen vor.

Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`. Reviewer-/Governance-Status erzeugen keine automatische mathematische Promotion.

---

## Aktueller mathematischer Stand

### Strong Terminal / C6

Für jedes feste `0<R<S` gilt im ungeraden P11-Graphraum der fixed-pair Strong-Terminal/C6-Abschluss aus positivem Wurzelanker plus R42.51. Keine Radienuniformität, Operatornormkonvergenz, vollständige gerade Sektor- oder Object-X-/RH-Folgerung.

### Prime-Power-/AR(1)-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q.
```

Die P11-Restseite besitzt die exakte Weil-Tail-Normalform.

### OX-GRAM

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

Die bloße Existenz irgendeines rückwärts aus `Q` definierten Kontraktors ist kein Object-X-Gate.

### OX-GEN-A `✓[M]`

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}),
```

```math
\mathcal EK_n=D_n\mathcal E,
\qquad
D_n=\lambda_n\operatorname{diag}(-1,1),
```

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Prime-only-A2 aus `{w_n,lambda_n}` bleibt `×[M]` im engen Scope.

### POS-DIL-1

Mit `S=D_n/lambda_n=2rho'(0)` erzwingen `PMP=M` und `SMS=M` die Form `M=tI`; minimale Blockpositivität liefert `M=I`. Volle positive `rho`-Invarianz erzwingt dagegen `M=0`.

Für jede endliche nichtleere Prime-Power-Menge `N`:

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

### POS-DIL-2A / unit-gain FEATURE-SHORTING `×[M]`

Der vorab definierte Gate

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

```math
G_{1/2}^+(v_\varepsilon)
\to1+\sqrt2(\log2)^2,
```

und exakt

```math
32\sinh^2\frac14>2>1+\sqrt2(\log2)^2.
```

Daher gibt es in der bestehenden `G_{1/2}^+`-Featuregeometrie weder ein unit-gain Shorting `C F^+=V` noch irgendein kontraktives Target-observable für `R_0`.

Notwendiger Zusatzmassendefekt:

```math
\boxed{
\delta_0=32\sinh^2\frac14-1-\sqrt2(\log2)^2>\frac5{32}.
}
```

---

## Nächste Default-Arbeitsfolge

1. **POS-DIL-2B / INTRINSIC-MASS-AUGMENTATION:** schwächste positive Zusatzmasse aus vorhandener Prime-/AR(1)-Root/Hub-/`log|D|`-Geometrie suchen, die am Plateau mindestens `delta_0` liefert und `R_0` im selben positiven Umraum trägt.
2. Globale Prime-Kanäle außerhalb des lokalen Suzuki-Cutoffs dürfen geprüft werden, aber nur mit korrekter Buchungsrichtung; keine beliebige Diagonalmasse und keine stille Identifikation mit `c_aI`.
3. **OX-GEN-B:** `r_1` und/oder `c_aI` erst einbeziehen, wenn ihre Rolle vorwärts aus gemeinsamer Geometrie motiviert ist.
4. Parallel die AR(1)/Martingal-Faktorisierung als eigenständigen RH-unabhängigen Satz verschriftlichen.

---

## Nicht reaktivieren

Nicht wieder als aktive Front verwenden: matched-cutoff, OX-REN/OX-REN', Vier-Boundary-Erklärung, cross-prime als Fensterrand, „Nichtunitarität = genau Hub“, klassische `H^{1/2}`-Deutung des `1/|x-y|`-Kerns, `0.603` als Konstante, reine OX-GRAM-Existenztests, Prime-only-Rang-2-Gram ohne Zusatzstruktur, die Behauptung POS-DIL-1 erkläre bereits `r_1/c_aI`, oder die Überdehnung des POS-DIL-2A-No-Go auf alle positiven Erweiterungen.

---

## Offene Nebenfronten

- PR #91: analytischer Draft, kein übertragener unabhängiger Exact-Head-GREEN.
- PR #49: Candidate-only.
- R37/G4c: separat offen.

Es gibt weiterhin **keine vollständige Object-X-Realisierung und keinen RH-Beweis**.
