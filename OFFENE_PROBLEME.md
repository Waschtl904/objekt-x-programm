# Offene Probleme — X-C1, Diagnose und Governance

> **Stand:** 16. September 2026.  
> Operative Spezifikationen: [CURRENT-FRONT](CURRENT-FRONT.md) · [A1 Statuskapsel](research/x-c0/A1_COMP_STATUS_CAPSULE.md) · [X-C0 Spezifikation](X_CANDIDATE_C0_SPEC.md) · [X-C1 Speicherfluss](research/x-c1/X_C1_STORAGE.md).

---

## 1. Abgeschlossen / Eingefroren

### `[A1-COMP]` `✓[Author-verified / External-open]`
- Finite Legendre-Paritätsblöcke $A_e \succeq 10^{-35}I$, $A_o \succeq 10^{-35}I$ (gemergt via PR #123 und #124).
- Quadratur-, Tail- und Auswertungsbudgets geschlossen.
- Vollständige Ganzzahl-Gleichheitsbrücke zwischen kanonischer und historischer Matrix geschlossen (Lauf 35005611795).
- Zusammengesetzter Operator: $L_1 \succeq 9\cdot 10^{-36}I_{L^2(-1,1)}$ auf Draft-PR #131 (Head `0a7c970`, Review 5218037890).
- Eingefroren als konditionaler Import; Stop-Regel aktiv.

### `[X-C0-TYPE]` `✓[M]`
- Gemeinsamer Vormediator $\mathfrak M = L^2(\mathbb R_x; \mathfrak h_r)$ mit $\mathfrak h = H^1(0,\infty)$ und Kern $k_t(r) = e^{-|r-t|/2}$.
- Physische Zustände $T_a^0 v$, wörtlich geschachtelte Fenstereinbettungen.
- Prime-, Gamma- und Polports aus demselben Feld abgeleitet.

### `[X-C1-STORAGE-NO-GO]` `✓[M]`
- Exakte Flussidentität $s_a[z_x] + \frac{d}{dx}F_a[z_x] = 2\operatorname{Re}(\overline{v(x)}\,(\mathcal B_a v)(x))$ mit $F_a \ge 0$.
- Kausaler Präfix-No-Go für naive nichtnegative Speicher $V \ge 0, V[0]=0$ auf glatter $\mathrm{NULLPOL}$-Rampe ($< -1/20$) bewiesen.

---

## 2. Aktive Front: Priorität 0 — `[X-C1-GEOM]` `?[O]`

Gesucht ist eine nichtzirkuläre Faktorisierung oder positive Auswertung für die signierte Randform
```math
2\operatorname{Re}\left( \overline{v(x)}\,(\mathcal B_a v)(x) \right),
```
nachdem naive kausale Speicherflüsse ausgeschlossen sind.

### Zulässige Lösungswege
1. **Zweiseitige/terminale Speicher:** Vorübergehend negative Speicherwerte $V_a(x) < 0$ (mit $V_a = \widetilde V_a - F_a$), die am rechten Rand exakt zurückgegeben werden.
2. **Genuin zweiseitige Randwert-Faktorisierung:** Direkte Faktorisierung der Randform $2\operatorname{Re}(\overline{v} \mathcal B_a v)$ unter Einbeziehung beider Endpunkte und der globalen $\mathrm{NULLPOL}$-Momentbedingungen.

### Harte Gates
- Exakte Reproduktion des Prime-2-Mischterms $Q_{\mathrm{fin}}(f,g) = -\frac{\log 2}{\sqrt 2}\|f\|_2^2$ auf disjunkten Trägern.
- Absicherung gegen Vorzeichenfehler durch komplexe Mischtests $f \pm ig$.
- Keine Annahme von $Q_W \ge 0$ zur Definition der Operatoren (Zirkularitätsverbot).

---

## 3. Konditionale Nebenstrecke: Priorität 1 — `[RHO-1-DIAGNOSE]` `?[O]`

Rigorose Schranke für das ungerade Rang-1-Defektfunktional
```math
\rho_1 = \sup_{v\ne0} \frac{|E_+(v)-E_-(v)|^2}{\mathfrak A_1[v]} = \langle d_1, \mathcal A_1^{-1} d_1 \rangle.
```

- **Verfahren:** Richtungsbezogener Residualtest mit $u \in D(\mathcal A_1)$, $r = d_1 - \mathcal A_1 u$:
  ```math
  b(u) \le \rho_1 \le b(u) + \frac{\|r\|_2^2}{9\cdot 10^{-36}}.
  ```
- **Ziel:** Sauberes Intervall oder numerische Schranke für den vollen Operator $\mathcal A_1$.
- **Firewall:** $\rho_1$ misst nicht den lokalen Präfixdefekt und ist kein Blocker für die $\mathrm{NULLPOL}$-Forschung.

---

## 4. Folge-Gates

- **`[X-C2-ID]` `?[O]`:** Polarisierte Gram-Identität $\langle C_a T_a^0 v, C_a T_a^0 w \rangle = Q_W(v,w)$ auf Basisfunktionen.
- **`[X-C3-WINDOW]` `?[O]`:** Kompatible Verbindungsabbildungen $J_{a,b}$ und Konsistenz des additiven Fenster-Kokzyklus $F_b - F_a \ge 0$.
- **`[EXT-REVIEW-A1]` `?[O]`:** Unabhängige externe Begutachtung des eingefrorenen PR #131 bzw. Benchmark-Abgleich mit Fremdzertifikaten.
