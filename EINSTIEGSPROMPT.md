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
- `audits/P11_POS_DIL_2C_EXACT_SHELL_GAUGE_R0_ABSORPTION_2026-09-13.md`

### Governance

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Perplexity ist nur externer Reviewer/Auditor. Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`.

---

## Aktueller mathematischer Stand

### 1. Lokale Weil-Normalform

Für `0<a<=1`:

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

### 2. OX-GEN-A / POS-DIL-1

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

### 3. Exterior-shell Geometrie

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\}.
```

Jeder Außenkanal `c_n>a` ist auf dem Fenster reine Identitätsmasse:

```math
w_n\langle K_nv,K_nw\rangle
=2w_n\langle v,w\rangle.
```

Für den ersten Außenshell

```math
A_a^{out}:=G_a^++H_a^{out}
\succeq\mathcal E^*\mathcal E
```

für alle `0<a<=1`.

### 4. Exakte Prime-cutoff-Gauge `✓[M]`

Für jede endliche Außenkanalmenge `J`:

```math
Q_{B_a}
=(G_a^++H_{a,J})-(c_a+b_J)I-R_0-R_1,
```

```math
b_J=2\sum_{n\in J}\frac{\Lambda(n)}{\sqrt n}.
```

Für den ersten Shell:

```math
c_a^{out}=c_a+A_{e^{4a}}-A_{e^{2a}}.
```

Damit ist der isolierte `c_a`-Wert cutoff-gaugeabhängig und nicht ohne Gauge-Fixierung kanonisch.

### 5. Exakte positive `R_0`-Absorption `✓[M]`

```math
D_a^{out}=A_a^{out}-\mathcal E^*\mathcal E\succeq0,
```

```math
L_+(v)=E_+(v)+E_-(v)
=2\int_{-a}^a\cosh(x/2)v(x)\,dx.
```

Dann

```math
P_a^{(0)}
:=A_a^{out}-R_0
=D_a^{out}+L_+^*L_+\succeq0.
```

Und exakt

```math
\boxed{
Q_{B_a}=P_a^{(0)}-c_a^{out}I-R_1,
\qquad0<a\le1.
}
```

Der elementare archimedische `r_0`-/`R_0`-Layer ist damit positiv absorbiert, während die volle Weilform unverändert bleibt.

---

## Nächster Default-Auftrag

**OX-GEN-B / `R_1` + gaugeinvarianter Skalarrest.**

Arbeite algebraisch zuerst:

1. Rekonstruiere die exakte polarisierte Formel bzw. den Kernel von `R_1` aus den kanonischen Suzuki-/OX-GRAM-Quellen.
2. Bestimme Parität, Translation-/Reflexionssymmetrien und mögliche Generatorrepräsentationen.
3. Definiere eine natürliche positive Absorptions-/Intertwinerklasse **vor** dem Ergebnis und prüfe Konstruktion oder No-Go.
4. Behandle den skalaren Ledger gaugeinvariant; den nackten Wert `c_a` nicht als kanonisch voraussetzen.
5. Prüfe bevorzugt eine gemeinsame Behandlung von `R_1` und Skalarrest.

Keine weitere beliebige Diagonalaugmentation als Fortschritt verbuchen.

---

## Firewalls

- `P_a^{(0)}` ist noch nicht die volle Weil-Gram-Realisierung.
- `R_1` und der endgültige Skalarrest bleiben offen.
- Keine Aussage für `a>1` ohne separaten Beweis.
- Object X und RH bleiben offen.
- PR #91, PR #49 und R37/G4c bleiben separate Nebenfronten.
