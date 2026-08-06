# Offene Probleme — Konsolidierte Liste

> **Aktuelle Front: 6. August 2026 — NEU-250a**  
> Der untere Teil dieser Datei ist der konsolidierte Stand vom 15. Juli 2026 (NEU-161 rev.5).
> Er bleibt gültig, soweit er nicht durch die aktuelle Front überholt ist.

Kompakte Gesamtbilanz: [STATUS.md](STATUS.md) · Alle Dokumente: [INDEX.md](INDEX.md) ·
Verbindliche Karte aller Bedingungen an Objekt X: [Ebene XVI — Kontrollblatt](00-grundlegung/ebene-XVI-objekt-x.md)

> **Ebenentrennung beachten.** HP-1–HP-7 sind Realisierungsbedingungen für $H_X$, keine
> Axiome von $X$. Das Stieltjes-Profil des NEU-221-Strangs impliziert das HP-Profil **nicht**
> — Fortschritt an `[O-221-1c1a–d]` darf nicht als Fortschritt an HP-2/HP-3 verbucht werden.

---

# Teil I — Aktuelle Front (Stand NEU-250a)

## Priorität 0 — Aktiver Tiefenknoten (neu: 6. August 2026)

### `[O-221-1c1a0-C]`: BC-Repräsentation eines primitiven relativen Primkantenvektors ❓ [O]

> Eröffnet: 6. August 2026 — NEU-250a (Ausgang B) · Vorgänger `[O-221-1c1a0-B]` `✓[M]_part`

**DAG-Kette:**
$$\text{NEU-250} \longrightarrow \boxed{\text{Ausgang E}} \longrightarrow \text{NEU-250a} \longrightarrow \boxed{\text{Ausgang B}} \longrightarrow [O\text{-}221\text{-}1c1a0\text{-C}]$$

**Ausgangslage.** NEU-250a hat bewiesen: Die BC-Residuenarchitektur (NEU-15–25) liefert keine Repräsentationsabbildung
$$j_{p,N}: \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} \longrightarrow F^3A_{\mathrm{BC}}^{\mathrm{an}}$$
aus den vorhandenen Quellen. Ohne $j_{p,N}$ sind relative Wres-Paarung, Grammatrix, Radikal und Hebungsabstieg sämtlich untypisiert.

**Kleinstes Ziel dieses Knotens:**

Für $p=2$ und einen einzelnen primitiven Erzeuger $E^{\mathrm{rel}}_{R;1\to2}$ ist
$$j_{2,N}\!\left(E^{\mathrm{rel}}_{R;1\to2}\right)$$
als explizites, residuenfähiges BC-Element oder als expliziter BC-Kozykel zu konstruieren.

**Sechs Pflichtbedingungen:**

| Nr. | Bedingung | Status |
|---|---|---|
| C1 | Typkorrektheit: $j_{2,N}(E_R) \in F^3A_{\mathrm{BC}}^{\mathrm{an}}$ | \u2753 [O] |
| C2 | Linearität | \u2753 [O] |
| C3 | Indexverträglichkeit (BC-Monoid- und Fourierindizes) | \u2753 [O] |
| C4 | Involutionsverträglichkeit: $j_{2,N}(E_R)^*$ explizit berechenbar | \u2753 [O] |
| C5 | Residuenfähigkeit: $\lambda_\beta^{\mathrm{mod}}(R_3(j_{2,N}(E_R)^* j_{2,N}(E_{R'})))$ bei $\beta=1$ auswertbar | \u2753 [O] |
| C6 | Nichttautologie: $j_{2,N}$ darf nicht so definiert werden, dass der Gramwert definitionsgemäß entsteht | \u2753 [O] |

**Primärquellen:** NEU-15–25 (`01-primkanten-werkzeuge/`) für BC-Architektur; NEU-221e für relativen Rohzielraum.

**Forschungsdokument:** [`NEU-250a`](07-weil-explizitformel/NEU-250a_O221-1c1a0-B_Typisierung_Dirichletresiduumsform_relativer_Primkantenraum.md)

---

## Priorität 1 — Hebungsabstieg des Kopplungsvektors

### `[O-221-1c1a0]`: Zulässige Differenzmenge und Rohkopplung ❓ [O]

> Eröffnet: 26. Juli 2026 — NEU-221e · Vorgänger `[O-221-1c1a]` `✓[M]_part`  
> **Hinweis:** Dieser Knoten setzt `[O-221-1c1a0-C]` als Vorläufer voraus.

**Ausgangslage.** NEU-46 verwendet den relativen Vektor als **zyklischen** Vektor einer
Weyl-Funktion. Damit ist die Hebungsfrage **nicht** durch Normgleichheit entschieden:
Verschieden gewählte, gleich normierte Hebungen können verschiedene
Resolventenmatrixstellen, Spektralmaße und inverse Momente erzeugen. Norminvarianz
entspricht nur dem Test $f\equiv 1$.

**Bewiesenes Kriterium (NEU-221e).** Der Kopplungsvektor steigt genau dann von der
Hebungsfaser auf den primitiven Kanal ab, wenn

$$\widetilde T_p^{\mathrm{raw}}\bigl(\Delta_p^{\mathrm{adm}}\bigr) \subseteq \mathcal N_{\mathrm{Wres,rel}},
\qquad \Delta_p^{\mathrm{adm}} = \mathcal A_p^{\mathrm{adm}} - \mathcal A_p^{\mathrm{adm}}.$$

**Drei Aufgaben des Knotens:**

1. Alle Bedingungen an eine Hebung klassifizieren und $\widehat{\mathcal E}_p^{\mathrm{adm}}$ vollständig definieren.
2. Rohzielraum $\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}$, Wres-Radikal $\mathcal N_{\mathrm{Wres,rel}}$ und Quotientenabbildung explizit fixieren.
3. Den Test auf Erzeugern bzw. expliziten Kurven in $\Delta_p^{\mathrm{adm}}$ rechnen.

**Forschungsdokument:** [`NEU-221e`](07-weil-explizitformel/NEU-221e_Affine_Hebungsfaser_Wres-Quotient_und_Spektralmassabstieg_Psip.md)

---

### `[O-221-1c1b/c/d]`: Zyklisches Tripel für den Weil-Momentoperator ❓ [O]

> Eröffnet: 26. Juli 2026 — NEU-221d

**Frage:** Ist $(\mathcal H_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N)$ ein vollständig typisiertes
zyklisches Tripel, sodass $\Omega_{X,N} = (D_N^{\mathrm{rel}})^{-1}\Psi_N$ und
$J_{X,N} = (D_N^{\mathrm{rel}})^{-2}$ als verfügbar markiert werden dürfen?

| Teilfrage | Status |
|---|---|
| $D_N^{\mathrm{rel}}$ selbstadjungiert | ✓ [M] über NEU-53/54 |
| $\Psi_p = C_p^{\mathrm{rel}}\varepsilon_p$ formal definiert | ✓ [K]_part — NEU-46 §1, Gl. 46.5–6 |
| $\varepsilon_p, \Psi_p$ als konkrete Hilbertvektoren typisiert | ❓ [O] |
| $\lVert\Psi_N\rVert$ quellseitig fixiert | ❓ [O] |
| Nullmodusfreiheit $E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N = 0$ | ❓ [O] |
| $\int\lvert\lambda\rvert^{-2k-2}\,d\mu_{\Psi_N} < \infty$ für $k=0,1,2$ | ❓ [O] |
| Vollständig gekoppelte endlich-archimedische Geometrie | ❓ [O] |

**Forschungsdokument:** [`NEU-221d`](07-weil-explizitformel/NEU-221d_Direktextraktion_NEU46_Zyklischer_Sektor_und_Nullmodusaudit.md)

---

## Priorität 2 — Positivitätsquelle für das Hankel-Kriterium

### `[O-220-1]`: Adelische Konstruktion der Momentfolge ❓ [O] (RH-stark)

> Eröffnet: 26. Juli 2026 — NEU-220w

**Ausgangslage:** Die Äquivalenz
$\mathrm{RH} \iff H_N^{(0)}\succeq 0 \wedge H_N^{(1)}\succeq 0\ \forall N$
ist unkonditional bewiesen (NEU-220w). Was fehlt, ist eine **unabhängige Quelle** für die
Positivität der Momentfolge $\mu_k = -\tfrac{k+1}{(2k+2)!}(\log\Xi)^{(2k+2)}(0)$.

**Forschungsdokument:** [`NEU-220w`](07-weil-explizitformel/NEU-220w_Hankelvollstaendigkeit_Moment-GNS_und_semifinite_Atomizitaet.md)

---

## Priorität 3 — Reparaturpfade nach dem O-219-No-Go

### `[O-219-6]`: Zyklizität ohne gewöhnliche Zyklizität ❓ [O]

> Eröffnet: 24. Juli 2026 — NEU-219u

| Reparaturpfad | Anforderung | Status |
|---|---|---|
| Orbitshift | Lift mit $\kappa \neq 0$ | Neue Konstruktion, eigener Knoten |
| Ladungsneutralisation | algebraische Neutralisation vor zyklischer Auswertung | Neue Konstruktion |
| Andere Koeffizientenkategorie | parazyklisch, $\sigma$-zyklisch, getwistet-zyklisch | `[O-219-5]` teilweise beschritten |
| Weil-/Gammafaktorpaarung | gewöhnliche Zyklizität ersetzen | **aktiv beschritten** ab NEU-220 |

**Forschungsdokument:** [`NEU-219u`](06-hochschild-bc-algebra/NEU-219u_Abschluss_O219_NoGo_Theorem.md)

---

### `[O-188-0]` – `[O-188-3]`: Erweiterbarkeit punktierter Kozykel ❓ [O]

> Eröffnet: 19. Juli 2026 — NEU-188

**Frage:** Existiert $H \notin \mathrm{LC}(\hat{\mathbb Z})$ mit $\alpha_k(H) - H \in \mathrm{LC}(\hat{\mathbb Z})$ für alle $k$?

---

# Teil II — Konsolidierter Stand vom 15. Juli 2026 (NEU-161 rev.5)

> Die folgenden Einträge stammen aus dem Stand vor dem kohomologischen und dem
> Weil-Strang. Sie sind weiterhin offen, stehen aber nicht mehr an der aktiven Front.

---

## Kritisch — Engpass des Standes NEU-161

### NEU-161: Nichttriviale Fourierladung von $L_3^\circ$ ❓ [O]

> Eröffnet: 15. Juli 2026

**Frage:** Existiert ein explizit konstruierter Fourierkoeffizient $\ell_{s_0,m_0}\neq 0$ mit $s_0\neq 0$ in $L_3^\circ = \sum_{s,m}\ell_{s,m}e_sV_m$?

**Quellenprüfungsbefund (161.A):** Früheste Quelle ist NEU-42 §10. Dort ist $s\neq 0$ **Rechenbedingung, kein Ergebnis**.

**Ausgangsbefund:** $?[O]$ — Nichttrivialität nur vorausgesetzt.

---

## Kritisch — Zweiter offener Hauptstrang

### NEU-141.D: Regulierte Spur im kritischen Streifen ❓ [O]

> Eröffnet: Juli 2026 — NEU-141

**Frage:** Gilt $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}})$ für $0 < \Re\beta \leq 1$?

| Ebene | Objekt | Status |
|---|---|---|
| S1-Existenz | $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$, $\Re\beta > 0$ | ✓ [M] NEU-137 |
| Mangoldt-Spur gewöhnlich | $R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$, $\Re\beta > 1$ | ✓ [M] |
| Regulierte Spur (krit. Streifen) | $\operatorname{Tr}_{\mathrm{reg}}$, $0 < \Re\beta \leq 1$ | ❓ [O] |

---

### NEU-57: Singulärwert-Wachstum von $J^-$ ❓ [O]

> Eröffnet: 29. Juni 2026 — NEU-56

---

## Offen (mittelfristig)

### X.3.25: Schur-Test exakt (Nelson-Bed. 1) ❓ [O]

### X.3.24: Essentielle Selbstadjungiertheit von $iJ^-$ ⚠ [M] (unter Bedingungen)

### X.3.23: Spektralalternativen für $D_{\mathrm{rel}}$ ❓ [O]

### X.3.16: Intrinsizität von $Wres_{\mathrm{rel}}$ ❓ [O]

### X.3.14: Gamma-Faktor-Intrinsifizierung ❓ [O]

### X.2.1: Rückrichtung RH ❓ [O]

### OP-4: Frobenius-Funktional auf $A_{2D}^r$ ❓ [O]

---

## Abgeschlossene Probleme

### NEU-144 bis NEU-160 (Juli 2026)

| Eintrag | Thema | Resultat |
|---|---|---|
| NEU-144–150 | Spurklassen, Selbstenergie, Kanalgewichte | ✓/⚠ [M] |
| NEU-151–160 | Zeugenroute, Kantengeometrie, Separationsbedingungen | ✓/⚠ [M] |
| **NEU-161 rev.1–5** | Zeugenroute Grundstruktur bis Quellenprüfungsabschluss | ✓ [M] Protokoll |

### NEU-57 bis NEU-143 (29. Juni — 9. Juli 2026)

| Eintrag | Thema | Resultat |
|---|---|---|
| NEU-57 | Singulärwert-Wachstum $J^-$ | Engpass eröffnet ❓ [O] |
| NEU-100–112 | Formfaktor, Weil, Jacobi-Realisierung | ✓ [M] |
| NEU-113–120 | Bombieri-Normalisierung, $C_\xi$-Fix | ✓ [M] |
| NEU-125, 130 | PSWF-Brücke, Prä-Lanczos-Metrik | ✓ [M] |
| NEU-131 | Edge-Schur-Nelson-Lemma (abstrakt) | ✓ [M] |
| NEU-135D | Welt-2-Entscheidung; $\|\varepsilon_p\|^2=1$ | ✓ [M] |
| NEU-141 | $R_p\gtrsim p/\log p$; drei Spurklassen-Ebenen | ✓ [M] (S1+S2); ❓ [O] (S3) |

### NEU-1 bis NEU-56 (19. — 29. Juni 2026)

| Problem | Zugang | Resultat |
|---|---|---|
| OP-1: Spektralinvarianz $A_{2D}^r$ | NEU-10 | ✓ [M] |
| OP-2: $[\omega_2]\neq 0$ | NEU-15 | ✓ [M] |
| OP-3: $[L_3]\neq 0$ | NEU-17–20 | $C'_{4,1}\neq 0$ ✓ [M] |
| OP-4.1: Frobenius-Wodzicki | NEU-21–25 | ✓ [M] |
| Mangoldt-Schicht (X.3.9) | NEU-39 | ✓ [M] |
| Kanonischer Kopplungsoperator | NEU-41 | ✓ [M] |
| Laplace-Realisierung $p^{-s}$ | NEU-42 | ✓ [M] |
| Reinheitslemma Graph | NEU-43 | ✓ [M] |
| $pq$-Kollisionstest | NEU-44 | ✓ [M] |
| Weyl-Korrekturen $M_p(z)$ | NEU-46 | ✓/⚠ [M] |
| Birman-Schwinger-Indexsatz | NEU-49 | ✓/✗ [M] |
| Spektralbasis $\eta$ vs. Eigenbasis | NEU-52 | ✓/✗ [M] |
| Nelson-Strategie + flache Achsen | NEU-54 | ⚠ [M] |
| $\gamma_N$-Spannung / Konfinement | NEU-56 | ✗/✓ [M] |

---

## Feshbach-Architektur (X.3) — Aktueller Gesamtstand

```
Feshbach-Operator:
F_N^{rel}(z,beta) auf H_{rel,N} (+) p_N                              ✓ [M]

Primdeterminante:
D_{prim,N}(beta) = zeta_N(beta)^{-1}                                  ✓ [M]
-d/dbeta log D_{prim} = zeta_N'/zeta_N                                ✓ [M]

Weyl-Korrektur:
M_p(z) = (C_p^{rel})^# (z-D_{rel,p}^-)^{-1} C_p^{rel}               ✓ [M] kontrolliert

Renormierte Selbstenergie:
Sigma_rel^ren(beta) = Sum_p p^{-beta}/(1-p^{-beta}) P_p              ✓ [M]
Tr(R Sigma_rel^ren(beta)) = -zeta'/zeta(beta)  fuer Re(beta) > 1     ✓ [M] (NEU-141)
Tr_reg(R Sigma_rel^ren(beta))  fuer 0 < Re(beta) <= 1                ❓ [O] (NEU-141.D)

Nelson-Energieoperator:
L eta_{p;m;r,u} = ell(p,m,r,u) eta                                    ✓ [M]
iJ^- wesentlich s.a. auf D_0^eff  [unter Nelson-Bed.]                ✓ [M] unter Bed.

Weg A (kompakter Resolvent) ueber L:                                  ✗ [M] (NEU-56)
Weg B (Spektralmass):                                                 ✓ [M] robuster Standard

Aktueller Haupt-Engpass (6. August 2026):
j_{2,N}(E^rel_{R;1->2}) als BC-Element konstruieren  =>  [O-221-1c1a0-C]
```
