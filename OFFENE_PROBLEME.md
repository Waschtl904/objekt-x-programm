# Offene Probleme — aktuelle POS-DIL-Priorität

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [AKTUELLER_STAND](00-uebersicht/AKTUELLER_STAND.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md), [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

## Geschlossen im dokumentierten Scope

### OX-GEN-A `✓[M]`

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Prime-only-A2 bleibt `×[M]` im engen Scope.

### POS-DIL-1 `✓[M]` / `×[M]` gemischt

Die natürliche positive Companion-Klasse liefert `M_min=I`; volle positive `rho`-Invarianz ist nur trivial. Die Prime-moment-Abbildung realisiert

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

### POS-DIL-2A bestehende G-Masse `×[M]`

Bei `a=1/2` ist unit-gain Shorting innerhalb der unveränderten `G_{1/2}^+`-Norm ausgeschlossen. Notwendiger Plateau-Massendefekt:

```math
\delta_0>\frac5{32}.
```

### POS-DIL-2B erster äußerer Prime-Shell `✓[M]` bei a=1/2

Definiere

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\}.
```

Für jeden Shell-Kanal gilt exakt

```math
\|K_nv\|^2=2\|v\|^2.
```

Daher ist

```math
H_a^{out}(v)=2B_a^{out}\|v\|^2
```

die Restriktion echter Prime-Kanalenergie, keine künstliche Diagonalmasse.

Bei `a=1/2`:

```math
\boxed{
\|\mathcal Ev\|^2
\le G_{1/2}^+(v)+H_{1/2}^{out}(v)
}
```

auf der ganzen Testklasse; folglich trägt die augmentierte positive Form `R_0` kontraktiv und liefert einen positiven Schurblock.

Kanonische Quelle: `audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md`.

---

## Priorität 0 — POS-DIL-2C / SHELL-BOOKING `?[O]`

Frage:

> Wie kann die positive Energie der äußeren Prime-Kanäle `c_n>a` in einer **exakten gemeinsamen Prime-/Archimedean-Geometrie** bilanziert werden, ohne die volle Weilform durch bloßes Hinzufügen positiver Energie zu verändern?

Zu prüfen:

1. die ursprüngliche Herkunft der reinen lokalen Identitätsmasse aus Kanälen `c_n>a` vor dem lokalen Cutoff;
2. Shell-Differenzen und mögliche Teleskopierungen;
3. die AR(1)-Root/Hub-Zerlegung
   ```math
   T_q^*T_q+uu^*=R_q;
   ```
4. die POS-DIL-1-Amplitude `1-u_k` als möglicher Buchungsindikator;
5. erst danach eine mögliche Beziehung zum offenen `c_aI`-Block.

**Erfolgskriterium:** Die volle Ziel-Form muss unverändert bleiben; keine rückwärts aus `Q_{B_a}` definierte Positivitätswurzel.

Ein negativer Ausgang zählt nur für eine vorab definierte Buchungsklasse.

---

## Priorität 1 — POS-DIL-2C / RADIUS `?[O]`

Bestimme den maximalen Radiusbereich, auf dem der geometrisch gleiche Shell

```math
\mathscr S_a^{out}=\{n:p^k,\ a<c_n\le2a\}
```

die Dominanz

```math
\|\mathcal Ev\|^2
\le G_a^+(v)+H_a^{out}(v)
```

liefert.

Bevorzugt: endliche algebraische Intervallanalyse an Prime-Power-Ein-/Austrittsschwellen; Numerik nur zur Orientierung oder Gegenvektorsuche.

---

## Priorität 2 — OX-GEN-B `?[O]`

- regulärer `r_1''`-Korrektor;
- dominanter Skalarblock `c_aI`.

Der Außenshell wird ausdrücklich **nicht** bereits als `c_aI` gebucht.

---

## Priorität 3 — vollständiger Object-X-Pfad

- genuine X candidate `?[O]`;
- exakte volle Weil-Gram-Identität `?[O]`;
- Object-X-Realisierung `?[O]`;
- Weil-Kriterium-Scope `?[O]`;
- RH `?[O]`.

---

## Spur B

Prime-Power-AR(1)/Martingal-Faktorisierung theorem-ready und RH-unabhängig verschriftlichen; nicht als Objekt X vermarkten.

---

## Separate Nebenfronten

- R37/G4c separat offen.
- PR #91 analytischer Draft ohne übertragenes unabhängiges Exact-Head-GREEN.
- PR #49 Candidate-only; kein stiller Merge.

---

## Gesperrte Überdehnungen

Nicht behaupten:

- POS-DIL-2A schließe alle positiven Erweiterungen aus;
- der Außenshell sei bereits eine exakte Weil-Buchung;
- die Außenshellmasse sei bereits `c_aI`;
- der Radius-1/2-Satz sei radienuniform;
- ein positiver Schurblock sei bereits Object X oder RH.
