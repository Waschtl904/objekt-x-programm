# Offene Probleme — aktuelle POS-DIL-Priorität

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [AKTUELLER_STAND](00-uebersicht/AKTUELLER_STAND.md), [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](00-uebersicht/DAG.md), [Registry](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).

## Geschlossen im dokumentierten Scope

### OX-GEN-A `✓[M]`

Prime-Kanäle und `r_0` liegen auf derselben zweidimensionalen Translation-/Reflexions-Generator-Ebene.

### POS-DIL-1 `✓[M]` / enger No-Go `×[M]`

Die Prime-moment-Hilbertisierung erfüllt

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

Volle positive `rho`-Invarianz auf positivem Rang 2 ist nur trivial.

### POS-DIL-2A bestehende G-Masse `×[M]`

Bei `a=1/2` ist die unveränderte `G_{1/2}^+`-Norm zu klein für unit-gain Shorting.

### POS-DIL-2B/2C-R erster Außenshell `✓[M]`

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
```

```math
H_a^{out}(v)=2B_a^{out}\|v\|^2.
```

Für **alle** `0<a<=1` gilt

```math
\boxed{
\|\mathcal Ev\|^2
\le G_a^+(v)+H_a^{out}(v).
}
```

Damit ist für jeden Radius im lokalen Scope auch der entsprechende `R_0`-Schurblock positiv.

Kanonische Radiusquelle: `audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md`.

---

## Priorität 0 — POS-DIL-2C-B / EXACT-SHELL-BOOKING `?[O]`

Frage:

> Wie kann die positive Energie der äußeren Prime-Kanäle in einer **exakten unveränderten Weil-Geometrie** erscheinen, ohne dass `H_a^{out}` bloß zusätzlich zur Ziel-Form addiert wird?

### A. Vor-Cutoff-Rekonstruktion

Bestimme exakt, wo die reine lokale Identitätsmasse der Kanäle `c_n>a` in der ungekürzten Prime-Darstellung sitzt und durch welche lokale Umschreibung/Cutoff-Buchung sie verschwindet.

### B. Shell-Differenzen / Teleskopierung

Prüfe, ob benachbarte Shift-Shells eine kanonische Differenzzerlegung erzeugen, in der positive Außenmasse und eine Gegenkomponente exakt bilanzieren.

### C. AR(1)-Root/Hub-Gegenbuchung

Nutze

```math
T_q^*T_q+uu^*=R_q
```

und prüfe, ob die Shellenergie pro Primast gegen Root-/Hub-Masse gebucht werden kann.

### D. Quotientenamplitude `1-u_k`

Die POS-DIL-1-Identität

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-u_k)S
```

macht `1-u_k` zum natürlichen Kandidaten für eine Buchungs-/Differenzrolle. Das ist zu beweisen oder in einer vorab definierten Klasse auszuschließen.

**Erfolgskriterium:** exakte Formgleichheit; keine fertige Weil-Positivität, kein RH, keine rückwärts definierte Wurzel.

---

## Priorität 1 — OX-GEN-B `?[O]`

- `r_1`;
- `c_aI`.

Erst nach exakter Shell-Buchung darf geprüft werden, ob die dabei auftretende Skalarmasse mit einem Teil von `c_aI` zusammenhängt. Keine stille Identifikation.

---

## Priorität 2 — vollständiger Object-X-Pfad

- genuine X candidate `?[O]`;
- exakte volle Weil-Gram-Identität `?[O]`;
- Object-X-Realisierung `?[O]`;
- Weil-Kriterium-Scope `?[O]`;
- RH `?[O]`.

---

## Separate Nebenfronten

- Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständiger RH-unabhängiger Satz;
- R37/G4c separat offen;
- PR #91 analytischer Draft;
- PR #49 Candidate-only.

---

## Gesperrte Überdehnungen

Nicht behaupten:

- der Außenshell sei bereits exakte Weil-Buchung;
- Außenshellmasse = `c_aI`;
- positiver `R_0`-Schurblock = vollständiges Objekt X;
- Radiuspositivität = RH.
