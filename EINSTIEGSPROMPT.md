# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 13. September 2026.**

## Arbeitskontext

Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository `Waschtl904/objekt-x-programm`.

Arbeite als strenger mathematischer Auditor und Research Assistant. Prüfe zuerst den aktuellen `main`-Stand live. Keine mathematische Promotion allein durch Merge, CI oder Numerik.

### Kanonische Hauptquellen

1. `CURRENT-FRONT.md`
2. `audits/P11_NP_DISCREPANCY_POLE_CLEARED_CORRELATION_2026-09-13.md`
3. `audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md`
4. `audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md`
5. `00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md`
6. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md`
7. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md`

ChatGPT übernimmt sämtliche GitHub-/Repository-Arbeiten. Externe Modelle sind Reviewer/Auditoren. Statusmarker strikt trennen.

---

## Aktueller mathematischer Stand

### 1. COMMON-JUMP / centered overlap

Auf

```math
D_{NP}=ker M(0)\cap ker M(1)
```

gilt

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v).
```

Per-prime sind die vollständigen Prime-Power-Blöcke exakt AR(1)-Matrizen. Einzelshift- und unabhängige Blocknormsummation sind als all-window-Hauptweg ausgeschlossen.

### 2. Null-pole autocorrelation gauge `✓[M]`

Mit

```math
C_v(t)=\langle T_tv,v\rangle
```

gilt

```math
\boxed{
\int_0^{2a}2\cosh(t/2)\operatorname{Re}C_v(t)dt=0.
}
```

### 3. Pole-cleared Prime discrepancy `✓[M]`

```math
\boxed{
d\mathfrak D(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dt)
-2\cosh(t/2)dt.
}
```

Dann exakt

```math
\boxed{
\mathcal O_a(v)
=2\int Re C_v(t)d\mathfrak D(t)
=-2\int_0^{2a}\mathfrak D(t)\frac{d}{dt}Re C_v(t)dt.
}
```

Der rohe `e^{t/2}`-PNT-Hauptterm ist damit auf der zulässigen Nullpolklasse exakt herauszentriert.

### 4. Pole-cleared zeta fingerprint `✓[M]`

Für `Re(s)>1/2`:

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=-\frac{d}{ds}\log[(s^2-1/4)\zeta(s+1/2)].
}
```

Die Nullpolzentrierung entfernt exakt die Polfaktoren `z=0,1`.

### 5. RH-hard scale

Unter RH gilt klassisch `D(T)=O(T^3)`. Umgekehrt impliziert bereits irgendein polynomialer Bound `D(T)=O(T^K)` RH. Also nicht versuchen, die Hauptfront durch eine globale absolute Diskrepanzschranke zu lösen.

---

## Nächster Default-Auftrag — NP-DISCREPANCY / NP-CORR

Zu beweisen bleibt

```math
\boxed{
\mathcal A(v)
\ge
-2\int_0^{2a}\mathfrak D(t)
\frac{d}{dt}\operatorname{Re}C_v(t)dt
\quad\forall v\in D_{NP}(a),\ a>0.
}
```

Arbeitsreihenfolge:

1. Sign-/Oszillationsstruktur von `D(t)` gegen positive-definite Autokorrelationen untersuchen.
2. `Q_0`-Transport von `C_v'(t)` explizit bestimmen.
3. AR(1)-Fasern als lokale Zerlegung derselben Diskrepanz nutzen, nicht separat normieren.
4. Toeplitz/Paley-Wiener/Prolate nur auf der **zentrierten** Diskrepanz testen.
5. Vor jeder Numerik eine Falsifikationsbedingung definieren; ein Korrelationszeuge gegen die Mechanismusklasse zählt als Fortschritt.

### Verbindliche No-Gos

```text
independent shift/block scalar norm sum       ×[M]
raw Prime amplitude × constant Prolate factor ×[M]
```

### Firewalls

- polynomialer Absolutbound für `D` ist bereits RH-hart;
- Inkommensurabilität der `log p`-Gitter allein beweist nichts;
- bekannte Kleinfensterpositivität nicht als Neuheit beanspruchen;
- all-`a`-Beweis bleibt RH-hart;
- Registry und Arbeitsdefinition nur separat promovieren.

## Status

```text
COMMON-JUMP / Q0                            ✓[M]
per-prime AR(1) fibers                     ✓[M]
null-pole correlation gauge                ✓[M]
pole-cleared Prime discrepancy             ✓[M]
NP-DISCREPANCY / anti-correlation          ?[O]
forward Object-X candidate architecture    ✓[M]_part
full positive Object-X / RH                ?[O]
```
