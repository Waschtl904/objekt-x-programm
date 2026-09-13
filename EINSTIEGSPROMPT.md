# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

## Arbeitskontext

Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor und Research Assistant. Prüfe zuerst den aktuellen `main`-Stand live. Keine mathematische Promotion allein durch Merge, CI oder Numerik.

### Kanonische Quellen

1. `CURRENT-FRONT.md`
2. `00-uebersicht/AKTUELLER_STAND.md`
3. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
4. `00-uebersicht/DAG.md`
5. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`
6. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`

Aktueller Strang zusätzlich:

- `audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md`
- `audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md`
- `audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md`
- `audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md`
- `audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md`

### Governance

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Perplexity ist nur externer Reviewer/Auditor. Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`.

---

## Aktueller mathematischer Stand

### Strong Terminal / Prime-AR(1)

Fixed-pair Strong Terminal/C6 liegt im ungeraden P11-Graphraum vor. Prime-Power-Geometrie:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad T_q^*T_q+uu^*=R_q.
```

### OX-GEN-A / POS-DIL-1

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Prime-moment-Hilbertisierung:

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

### POS-DIL-2A

Die unveränderte lokale `G_{1/2}^+`-Featuremasse ist für unit-gain Shorting zu klein; Plateau-Defekt `delta_0>5/32`.

### POS-DIL-2B/2C-R — erster Außenshell

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
\qquad c_n=\frac12\log n.
```

```math
H_a^{out}(v,w)=\sum_{n\in\mathscr S_a^{out}}
\frac{\Lambda(n)}{\sqrt n}\langle K_nv,K_nw\rangle.
```

Für jeden Shell-Kanal:

```math
\|K_nv\|^2=2\|v\|^2.
```

Daher

```math
H_a^{out}(v)=2B_a^{out}\|v\|^2.
```

Für **alle** `0<a<=1` wurde rein elementar bewiesen:

```math
-\log a+2B_a^{out}>4\sinh a.
```

Mit

```math
G_a^+(v)\ge(-\log a)\|v\|^2,
\qquad
\|\mathcal Ev\|^2\le4\sinh(a)\|v\|^2
```

folgt

```math
\boxed{
\|\mathcal Ev\|^2
\le G_a^+(v)+H_a^{out}(v),
\qquad0<a\le1.
}
```

und damit

```math
\boxed{
\begin{pmatrix}
G_a^++H_a^{out}&R_0\\
R_0&G_a^++H_a^{out}
\end{pmatrix}\succeq0
\qquad(0<a\le1).
}
```

**Radiusfrage geschlossen `✓[M]`.** `OX-GEN-A2'` bleibt insgesamt `✓[M]_part`, weil die exakte Weil-Buchung noch fehlt.

---

## Nächster Default-Auftrag

**POS-DIL-2C-B / EXACT-SHELL-BOOKING.**

Untersuche algebraisch, wie `H_a^{out}` in einer exakten gemeinsamen Prime-/Archimedean-Geometrie gegengebucht/renormalisiert werden kann, ohne die Weilform zu verändern.

Reihenfolge:

1. Außenkanal-Identitätsmasse vor der Cutoff-Umschreibung rekonstruieren.
2. Shell-Differenzen/Teleskopierung prüfen.
3. Gegenbuchung über `T_q^*T_q+uu^*=R_q` prüfen.
4. Rolle der Amplitude `1-u_k` untersuchen.
5. Erst danach `c_aI` oder `r_1` anbinden.

Keine weitere bloße Positivitätsverstärkung als Hauptfortschritt verbuchen.

---

## Firewalls

- Außenshellmasse ist nicht bereits `c_aI`.
- Radiuspositivität ist keine exakte Weil-Buchung.
- `r_1`, volle Weil-Gram-Identität, Object X und RH bleiben offen.
- PR #91, PR #49 und R37/G4c bleiben separat.
