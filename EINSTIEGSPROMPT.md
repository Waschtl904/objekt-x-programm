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

Aktueller Hauptaudit:

- `audits/P11_NULLPOLE_STRATEGIC_RECLASSIFICATION_2026-09-13.md`

Auxiliary Pole-layer-Provenienz:

- `audits/P11_OX_GEN_A_COMMON_EXPONENTIAL_GENERATOR_2026-09-13.md`
- `audits/P11_POS_DIL_1_PRIME_MOMENT_HILBERTIZATION_2026-09-13.md`
- `audits/P11_POS_DIL_2_UNIT_GAIN_FEATURE_SHORTING_NOGO_2026-09-13.md`
- `audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md`
- `audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md`
- `audits/P11_POS_DIL_2C_EXACT_SHELL_GAUGE_R0_ABSORPTION_2026-09-13.md`

### Governance

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Perplexity dient ausschließlich als externer Reviewer/Auditor. Statusmarker strikt trennen: `✓[M]`, `✓[K/M]`, `✓[M]_part`, `✓[M]_neg`, `×[M]`, `?[O]`.

---

## Aktueller mathematischer Stand

### 1. Lokale Weil-Normalform

Für `0<a<=1` im kanonischen Suzuki-Gauge:

```math
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
```

### 2. Polfunktionale identifiziert `✓[M]`

```math
M(v)(s)=\int_{\mathbb R}v(x)e^{(s-1/2)x}\,dx,
```

```math
\boxed{E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).}
```

Auf der Nullpolklasse

```math
\mathscr D_{NP}=\{v:M(v)(0)=M(v)(1)=0\}
```

gilt exakt

```math
R_0=0,
\qquad
\|\mathcal Ev\|^2=0.
```

Für komplexe `v`:

```math
R_0(v,v)
=-2\operatorname{Re}(E_+(v)\overline{E_-(v)}).
```

### 3. Restricted global Weil criterion

Connes–Consani Proposition C.1: Für jede endliche Nullstellenmenge `F superset {0,1}` ohne nichttriviale Zeta-Nullstelle bleibt die **globale** Weil-Vorzeichenbedingung auf Testfunktionen mit `\tilde g|_F=0` RH-äquivalent.

**Firewall:** keine fixed-`a`-RH-Äquivalenz daraus ableiten.

### 4. Strategische Reklassifikation

OX-GEN-A bleibt `✓[M]`, aber als exakte **Pole-layer geometry**. Die frühere Deutung als notwendiger Object-X-Klassenschnitt ist zurückgezogen.

POS-DIL #101--#105 bleibt mathematisch gültig und wird als

```text
AUX-POS-DIL / full-class pole-layer route
```

geführt. Nicht mehr Default-Hauptfront.

### 5. Nullpol-Normalform

Auf Nullpol:

```math
\boxed{
Q_{B_a}(v)
=G_a^+(v)-c_a\|v\|^2-R_1(v,v).
}
```

Der verbleibende aktive Kern ist damit

```text
positive Prime/log|D| geometry
minus scalar ledger
minus R_1.
```

### 6. Gauge-Firewall

PR #105 bleibt exakt: Außen-Prime-Kanäle können positive Featuremasse und denselben Skalarbetrag gegeneinander verschieben. Daher ist `c_a` ohne Gaugewahl nicht isoliert kanonisch.

Auf der Nullpol-Hauptroute entweder:

- originalen Suzuki-Gauge explizit fixieren; oder
- gaugeinvariante Reststruktur formulieren.

---

## Nächster Default-Auftrag

**NULLPOL-CORE / NP-R1 zuerst.**

Arbeite in dieser Reihenfolge:

1. Rekonstruiere `R_1` aus den kanonischen Suzuki-/OX-GRAM-Quellen vollständig polarisiert.
2. Bestimme `R_1`-Parität, Spiegelung, Translation/Faltung und mögliche Spektral-/Generatorrepräsentationen.
3. Restriktiere jede Kandidatenstruktur ausdrücklich auf `M(v)(0)=M(v)(1)=0`.
4. Definiere eine natürliche Generator-/Absorptionsklasse **vor** dem Ergebnis und prüfe Konstruktion oder No-Go.
5. Behandle den Skalarledger parallel im fixed Suzuki gauge und gaugeinvariant.
6. Bevorzuge einen gemeinsamen Mechanismus für `R_1` + Skalarrest.

### Verbindliche Hauptfront-Frage

> Wirkt und schneidet dieser Mechanismus die zulässige Geometrie auch nach der Nullpolrestriktion?

Wenn nein: als auxiliary dokumentieren, nicht als Object-X-Hauptfortschritt.

---

## Präzisierungen / Firewalls

- Companion-Block bei `t=1` nur semidefinit/entartet; strikt positiv erst `t>1`.
- Anti-Kovarianz-No-Go lässt `b in C` frei.
- Die alte Rayleigh-Obstruktion ist extern numerisch im geraden Sektor lokalisiert; sie ist für NULLPOL-CORE nicht tragend.
- OX-GEN-A/POS-DIL nicht als falsch bezeichnen.
- Keine Aussage für fixed `a` als vollständiges RH-Kriterium ohne separaten Satz.
- `R_1`, Skalarrest, Object X und RH bleiben offen.
