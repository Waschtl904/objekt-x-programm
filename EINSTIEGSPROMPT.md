# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**
> Dieser Text ist der operative Einstieg für eine neue Session. Ältere Stände sind über Git erhalten und nicht als heutige Arbeitsanweisung zu verwenden.

## Arbeitskontext

Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor und Research Assistant. Prüfe zu Beginn den aktuellen `main`-Stand direkt im Repository. Verwende kanonische mathematische Quellen vor älteren Navigations-/Archivdokumenten. Keine Behauptung darf durch Merge, CI oder numerische Evidenz still promotet werden.

### Kanonische operative Quellen

1. `CURRENT-FRONT.md`
2. `00-uebersicht/AKTUELLER_STAND.md`
3. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
4. `00-uebersicht/DAG.md`
5. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`
6. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`

Aktueller mathematischer Strang zusätzlich:

- `audits/P11_OBJECT_X_AR1_OX_GRAM_CONSOLIDATION_2026-09-12.md`
- `audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md`
- `audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md`
- `audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md`
- `audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md`

### Governance

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Perplexity dient ausschließlich als externer Reviewer/Auditor und nimmt keine Repo-Mutationen vor.

Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`.

---

## Aktueller mathematischer Stand

### 1. Strong Terminal / C6

Fixed-pair Strong Terminal/C6 liegt für jedes feste `0<R<S` im ungeraden P11-Graphraum vor. Keine Radienuniformität, Operatornormkonvergenz, Object-X- oder RH-Folgerung.

### 2. Prime-Power-/AR(1)-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q.
```

Die P11-Restseite besitzt die exakte Weil-Tail-Normalform.

### 3. OX-GRAM

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

Arbiträre rückwärts konstruierte Kontraktorexistenz ist kein Object-X-Gate.

### 4. OX-GEN-A `✓[M]`

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Prime-only-A2 bleibt `×[M]` im engen Scope.

### 5. POS-DIL-1

Die Companion-Symmetrien erzwingen `M=tI`; minimale Blockpositivität liefert `M=I`; volle positive `rho`-Invarianz ist nur trivial.

Prime-moment-Hilbertisierung:

```math
V_Nv=\kappa_N^{-1/2}(\sqrt{w_n}\,\mathcal EK_nv)_{n\in N},
```

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

`OX-GEN-A2'` insgesamt `✓[M]_part`.

### 6. POS-DIL-2A `×[M]`

Bei `a=1/2` ist die bestehende `G_{1/2}^+`-Masse zu klein für unit-gain Shorting:

```math
\|\mathcal Ev_\varepsilon\|^2\to32\sinh^2\frac14,
```

```math
G_{1/2}^+(v_\varepsilon)\to1+\sqrt2(\log2)^2,
```

mit strikt größerem Momentwert. Notwendiger Defekt `delta_0>5/32`.

### 7. POS-DIL-2B — erster äußerer Prime-Shell `✓[M]` bei a=1/2

Definiere rein aus der Shift-Geometrie

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
\qquad c_n=\frac12\log n,
```

und

```math
H_a^{out}(v,w)=\sum_{n\in\mathscr S_a^{out}}
\frac{\Lambda(n)}{\sqrt n}\langle K_nv,K_nw\rangle.
```

Für `c_n>a` sind die verschobenen Fenster disjunkt:

```math
\boxed{\|K_nv\|^2=2\|v\|^2.}
```

Die resultierende Skalarmasse stammt daher exakt aus echten Prime-Kanälen.

Bei `a=1/2` enthält der Shell insbesondere `3,4,5`, und

```math
G_{1/2}^+(v)+H_{1/2}^{out}(v)>\frac83\|v\|^2,
```

während

```math
\|\mathcal Ev\|^2<\frac83\|v\|^2.
```

Somit uniform für alle Testfunktionen:

```math
\boxed{
\|\mathcal Ev\|^2
\le G_{1/2}^+(v)+H_{1/2}^{out}(v).
}
```

Mit `A=G+H_out` gilt außerdem

```math
\boxed{
\begin{pmatrix}A&R_0\\R_0&A\end{pmatrix}\succeq0.
}
```

Dies ist ein positiver gemeinsamer Prime-/`r_0`-Schurbaustein bei `a=1/2`.

---

## Nächste Default-Arbeitsfolge

1. **POS-DIL-2C / SHELL-BOOKING:** klären, wie die reale positive Energie der Kanäle `c_n>a` in einer exakten gemeinsamen Geometrie bilanziert werden kann, ohne die Weilform künstlich zu vergrößern. Prüfe Shell-Differenzen, Teleskopierung, AR(1)-Root/Hub und `1-u_k`.
2. **POS-DIL-2C / RADIUS:** bestimme algebraisch den Radiusbereich, auf dem derselbe erste Außenshell die Momentmasse dominiert.
3. **OX-GEN-B:** `r_1`/`c_aI` erst nach sauberer Buchungsanalyse; Shellmasse nicht still mit `c_aI` identifizieren.
4. Parallel AR(1)/Martingal-Faktorisierung theorem-ready verschriftlichen.

---

## Firewalls

Nicht behaupten:

- Außenshell-Positivität sei schon eine volle Weil-Identität;
- der Radius-1/2-Satz sei radienuniform;
- Shellmasse = `c_aI`;
- POS-DIL-2A sei ein globaler No-Go;
- positiver Schurblock = Object X oder RH.

PR #91, PR #49 und R37/G4c bleiben separate Nebenfronten. Es gibt weiterhin keine vollständige Object-X-Realisierung und keinen RH-Beweis.
