# Objekt X — kanonische Forschungsroadmap v4.0

> **Stand:** 16. September 2026; Registry und Arbeitsdefinition unverändert.  
> **Nomenklatur-Trennung:** Zur Vermeidung von Namensraum-Kollisionen werden die historischen Einheitsfenster-Gates als `A1-G0` bis `A1-G7` geführt. Die aktive Konstruktionsspur von Objekt X verwendet die Stufen `X-C0` bis `X-C3`.

---

## Teilprogramm A: Historische A1-Zertifizierung (Eingefroren)

| Gate | Bezeichnung | Status | Befund / Import |
|---|---|---|---|
| **A1-G0** | Completionstruktur | `✓[M]` | COMMON-JUMP, Morse/Parität, $\lambda=1$, Fourier-Multiplikator |
| **A1-G1** | Omega1551 Schranke | `✓[K/M]` | Hochfrequenzboden $m_1(\xi) > 0.1$ für $|\xi| \ge 1551$ |
| **A1-G2** | Osipov N1102 | `✓[K/M]` | Prolate Konzentration $\mu_{1102} < 10^{-43}$, Schur-Penalty $< 1.5\cdot 10^{-40}$ |
| **A1-G3** | Finite Reduktion | `✓[K/M]` | Kanonische Reduktion auf $\le 1104$ Dimensionen |
| **A1-G4** | Legendre-Backend | `✓[M]` | Orthonormale Basis $M=2150$ ($1075 \times 1075$ pro Parität), Quadraturfehler $< 4\cdot 10^{-38}$ |
| **A1-G5E** | C-even Positivität | `✓[M]` | $A_e \succeq 10^{-35}I_{1075}$ zertifiziert (gemergt via PR #123) |
| **A1-G5O** | C-odd Positivität | `✓[M]` | $A_o \succeq 10^{-35}I_{1075}$ zertifiziert (gemergt via PR #124) |
| **A1-G6** | Komposition A1 | `✓[Author-verified]` | Zweipass-Autorenaudit in PR #131: $L_1 \succeq 9\cdot 10^{-36}I_{L^2(-1,1)}$; extern offen |
| **A1-G7** | All-window Skalierung | `?[O]` | Finite Schranken skalieren nicht automatisch zu RH (Landau–Widom-Barriere) |

*Stop-Regel:* Teilprogramm A ist auf Commit `0a7c970` eingefroren. Keine neuen Selbstaudits ohne externen Auslöser.

---

## Teilprogramm B: Aktive Objekt-X-Konstruktionsspur

```text
[X-C0-TYPE] ──> [X-C1-STORAGE] ──> [X-C1-GEOM] ──> [X-C2-ID] ──> [X-C3-WINDOW]
   (✓[M])            (✓[M])            (?[O])         (?[O])          (?[O])
                 Präfix-No-Go      Zweiseitige/    Polarisierte    Isometrische
                 bewiesen (< -1/20) Endpunkt-      Gram-Identität  Verklebung
                                   Faktorisierung
```

### Stufe X-C0: Gemeinsamer Vormediator `✓[M]`
- Konstruktion des gemeinsamen Gedächtnisraums $\mathfrak M = L^2(\mathbb R_x; \mathfrak h_r)$ mit $\mathfrak h = H^1(0,\infty)$ und Kern $k_t(r) = e^{-|r-t|/2}$.
- Physische Zustände $T_a^0 v$, wörtlich geschachtelte Fenstereinbettungen $T_b^0 i_{a,b} v = T_a^0 v$.
- Einheitliche Ausleseabbildung $\mathcal J_t$ für Primzahlpotenzen, kontinuierlichen Gamma-Anteil und Polmomente.

### Stufe X-C1: Speicherfluss & Nichtzirkuläre Geometrie `?[O]`
- **Status Speicherfluss:** Exakte Flussidentität $s_a[z_x] + \frac{d}{dx}F_a[z_x] = 2\operatorname{Re}(\overline{v(x)}\,(\mathcal B_a v)(x))$ mit $F_a \ge 0$ hergeleitet (`✓[M]`).
- **Präfix-No-Go:** Naive kausale nichtnegative Speicherflüsse $s_1 = R + V'$ mit $R, V \ge 0, V[0]=0$ sind auf glatten $\mathrm{NULLPOL}$-Funktionen im Einheitsfenster ausgeschlossen (`✓[M]`).
- **Aktives Gate X-C1-GEOM:** Zweiseitige oder endpunktbedingte Faktorisierung der Randform $2\operatorname{Re}(\overline{v} \mathcal B_a v)$.
- **Gate-Bedingung:** Bestehen des Prime-2-Mischtests $Q_{\mathrm{fin}}(f,g) = -\frac{\log 2}{\sqrt 2}\|f\|_2^2$ ohne vorausgesetzte Positivität.

### Stufe X-C2: Polarisierte Gram-Identität `?[O]`
- Konstruktion der konkreten Auswertungsabbildung $C_a: \mathcal K_a^0 \to \mathcal K_{X,a}$ mit
  ```math
  \langle C_a T_a^0 v, C_a T_a^0 w \rangle = Q_W(v,w)
  ```
  auf der gesamten Testklasse $\mathcal W_a$.

### Stufe X-C3: Fensterübertragung und Kozyklus `?[O]`
- Konstruktion kompatibler Einbettungen $J_{a,b}$ mit $J_{a,b} T_{X,a} v = T_{X,b} v$.
- *Struktureller Befund:* Nach exakten lokalen Gram-Identitäten ist die isometrische Verklebung algebraisch gesichert; es wird kein unbegründeter gleichmäßiger $L^2$-Koerzivitätsgap über alle Fenster verlangt.

---

## Konditionale Nebenstrecke: Rang-1-Defekt $\rho_1$ `?[O]`

- **Definition:** $\rho_1 = \langle d_1, \mathcal A_1^{-1} d_1 \rangle$ mit $d_1(x) = 2\sinh(x/2)$ für den vollen Operator $\mathcal A_1$.
- **Methode:** Richtungsbezogener unendlichdimensionaler Residuen-Pilot mit $u \in D(\mathcal A_1)$:
  ```math
  b(u) \le \rho_1 \le b(u) + \frac{\|r\|_2^2}{9\cdot 10^{-36}}.
  ```
- **Rolle:** Schließt bei $\rho_1 \le 1$ den ungeraden Weil-Transfer bei $a=1$; kein Blocker für die $\mathrm{NULLPOL}$-Forschung.
