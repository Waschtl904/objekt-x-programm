# Offene Probleme — Konsolidierte Liste

> **Operative Front seit 2. September 2026:** B / Strong Terminal, derzeit R43. R38--R42 sind frozen als independently verified AI-GREEN; Strong Terminal / C6 bleibt \(?[O]\) und ist für jedes feste \(0<R<S\) auf genau die Normalbahn \(W_{R,S}^{[U]}\varepsilon_R\), äquivalent auf \(\operatorname{Re}\langle\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R\rangle\to1\), reduziert. R43 ist offen / exploratory. R37/G4c bleibt separat offen. Siehe [CURRENT-FRONT.md](CURRENT-FRONT.md) und [ACTIVE_THEOREM_REGISTRY.md](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md).  
> **Historischer Hinweis:** Der nachfolgende Abschnitt „Aktuelle Front (Stand NEU-250a)“ dokumentiert die Wres-/BC-Front vom 6. August 2026 und ist **nicht mehr die heutige Prioritätsangabe**. Seine lokalen offenen Knoten bleiben als historische Problemprovenienz erhalten, soweit sie nicht separat geschlossen oder reklassifiziert wurden.

Kompakte Gesamtbilanz: [STATUS.md](STATUS.md) · Alle Dokumente: [INDEX.md](INDEX.md) ·
Verbindliche Karte aller Bedingungen an Objekt X: [Ebene XVI — Kontrollblatt](00-grundlegung/ebene-XVI-objekt-x.md)

> **Ebenentrennung beachten.** HP-1–HP-7 sind Realisierungsbedingungen für $H_X$, keine
> Axiome von $X$. Das Stieltjes-Profil des NEU-221-Strangs impliziert das HP-Profil **nicht**
> — Fortschritt an `[O-221-1c1a–d]` darf nicht als Fortschritt an HP-2/HP-3 verbucht werden.

---

# Operative Front — R43 / Single-Normal Strong-Terminal Gate

## [P11-R43-C6] — letzter fixed-pair Strong-Terminal-Gate ❓ [O]

Frozen R42 beweist für jedes feste \(0<R<S\) starke Konvergenz des echten Future-Transports
auf
\[
H_R^0=\ker\beta_R^{(0)}.
\]
Mit dem kanonischen Riesz-/Jet-0-Normalvektor
\[
\varepsilon_R=e_{R,0}
\]
bleibt exakt
\[
\boxed{
\operatorname{Re}
\langle
\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R
\rangle
\longrightarrow1
\quad?
}
\]
für \(T,U\to\infty\).

**Ergebnisoffene Klassifikation:**

- Grenzwert \(1\): Strong Terminal für das feste Paar geschlossen;
- persistenter Defekt \(<1\): Strong-Terminal-No-Go;
- kein zweiparametriger Grenzwert: ebenfalls kein Strong Terminal.

**Aktuelle R43-Untergates:**

1. **Gamma-Zyklizität über Zwischenradien**
   \[
   \overline{
   Y_{R,S}V_R+
   \operatorname{span}\{Y_{Q,S}\zeta_Q:R<Q<S\}
   }
   =V_S
   \quad?
   \]
   — vollständig terminalfreie feste Gamma-Geometrie.
2. **Quantitative Edge-Schicht:** intern hergeleiteter Hochrisikokandidat
   \[
   D_U(z_U,z_U)=O(U^{-1}),
   \]
   noch nicht extern verifiziert.
3. **Dritter Edge-Offblock:** selbst ein Skalargrenzwert von \(UD_U\) wäre source-kompatibel
   und reicht nicht; erforderlich wäre eine reskalierte Edge-Form samt Ziel-Offblock.

**Governance:** R43 ist AI-GREEN internal exploratory candidate, nicht frozen und nicht
\(\checkmark[M]\). R37/G4c bleibt davon unabhängig offen.

---

# Teil I — Historische Front (Stand NEU-250a, 6. August 2026)

## Priorität 0 — Neuer aktiver Tiefenknoten

### `[O-221-1c1a0-C]`: BC-Repräsentation eines primitiven relativen Primkantenvektors ❓ [O]

> Eröffnet: 6. August 2026 — NEU-250a · Vorgänger NEU-250 → Ausgang E → NEU-250a → Ausgang B

**Ausgangslage.** NEU-250a (Knoten [O-221-1c1a0-B]) hat bewiesen: Die BC-Residuenarchitektur (NEU-15–25) stellt keine Repräsentationsabbildung

$$j_{p,N}: \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} \longrightarrow F^3A_{\mathrm{BC}}^{\mathrm{an}}$$

bereit. Dies ist die tiefste gemeinsame Lücke des gesamten Wres-Strangs.

**Minimalziel dieses Knotens.** Für $p=2$ und einen einzelnen primitiven Erzeuger $E^{\mathrm{rel}}_{R;1\to2}$ ist ein explizites BC-Element oder BC-Kozykel

$$j_{2,N}\left(E^{\mathrm{rel}}_{R;1\to2}\right)$$

zu konstruieren, das folgende sechs Bedingungen erfüllt:

| Nr. | Bedingung | Inhalt |
|---|---|---|
| 1 | Typkorrektheit | $j_{2,N}(E_R)\in F^3A_{\mathrm{BC}}^{\mathrm{an}}$ oder äquivalentem Residuumsmodul |
| 2 | Linearität | $j_{2,N}(\alpha E_R+\beta E_{R'})=\alpha j_{2,N}(E_R)+\beta j_{2,N}(E_{R'})$ |
| 3 | Indexverträglichkeit | Indizes $p,m,R$ aus BC-Monoid-/Fourierindizes rekonstruierbar |
| 4 | Involutionsverträglichkeit | $j_{2,N}(E_R)^*$ explizit berechenbar |
| 5 | Residuenfähigkeit | $\lambda_\beta^{\mathrm{mod}}(R_3(j_{2,N}(E_R)^* j_{2,N}(E_{R'})))$ bei $\beta=1$ auswertbar |
| 6 | Nichttautologie | $j_{2,N}$ darf nicht so definiert werden, dass ein gewünschter Gramwert definitionsgemäß entsteht |

**Erst danach** darf der erste konkrete Gramwert $h_{2,N}(E_R,E_{R'})$ berechnet werden.

**Forschungsdokument:** [`NEU-250a`](07-weil-explizitformel/NEU-250a_O221-1c1a0-B_Typisierung_Dirichletresiduumsform_relativer_Primkantenraum.md)

**DAG-Position:**
```
NEU-250 ──E──► NEU-250a ──B──► [O-221-1c1a0-C]  ← aktiver Knoten
                                       ↓
                              [O-221-1c1a0] (Hebungsabstieg, übergeordnet)
```

---

## Priorität 1 — Hebungsabstieg des Kopplungsvektors

### `[O-221-1c1a0]`: Zulässige Differenzmenge und Rohkopplung ❓ [O]

> Eröffnet: 26. Juli 2026 — NEU-221e · Vorgänger `[O-221-1c1a]` `✓[M]_part`
> **Präzisierung 6. August 2026:** Vorläufer `[O-221-1c1a0-C]` freigeschaltet und als nächster Konstruktionsschritt eingetragen.

**Ausgangslage.** NEU-46 verwendet den relativen Vektor als **zyklischen** Vektor einer
Weyl-Funktion. Damit ist die Hebungsfrage **nicht** durch Normgleichheit entschieden:
Verschieden gewählte, gleich normierte Hebungen können verschiedene
Resolventenmatrixstellen, Spektralmaße und inverse Momente erzeugen.

**Bewiesenes Kriterium (NEU-221e).** Der Kopplungsvektor steigt genau dann von der
Hebungsfaser auf den primitiven Kanal ab, wenn

$$\widetilde T_p^{\mathrm{raw}}\bigl(\Delta_p^{\mathrm{adm}}\bigr) \subseteq \mathcal N_{\mathrm{Wres,rel}},
\qquad \Delta_p^{\mathrm{adm}} = \mathcal A_p^{\mathrm{adm}} - \mathcal A_p^{\mathrm{adm}}.$$

**Neuer Vorläufer (NEU-250a).** Das Wres-Radikal $\mathcal N_{\mathrm{Wres,rel}}$ ist erst nach Konstruktion von $j_{p,N}$ verfügbar. Daher ist `[O-221-1c1a0-C]` als Pflichtvorläufer eingetragen.

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
Positivität der Momentfolge.

**Forschungsdokument:** [`NEU-220w`](07-weil-explizitformel/NEU-220w_Hankelvollstaendigkeit_Moment-GNS_und_semifinite_Atomizitaet.md)

---

## Priorität 3 — Reparaturpfade nach dem O-219-No-Go

### `[O-219-6]`: Zyklizität ohne gewöhnliche Zyklizität ❓ [O]

> Eröffnet: 24. Juli 2026 — NEU-219u

| Reparaturpfad | Anforderung | Status |
|---|---|---|
| Orbitshift | Lift mit $\kappa \neq 0$ | Neue Konstruktion, eigener Knoten |
| Ladungsneutralisation | algebraische Neutralisation | Neue Konstruktion |
| Andere Koeffizientenkategorie | parazyklisch, $\sigma$-zyklisch | `[O-219-5]` teilweise beschritten |
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

**Frage:** Existiert ein explizit konstruierter Fourierkoeffizient $\ell_{s_0,m_0}\neq 0$ mit $s_0\neq 0$?

---

## Kritisch — Zweiter offener Hauptstrang

### NEU-141.D: Regulierte Spur im kritischen Streifen ❓ [O]

> Eröffnet: Juli 2026 — NEU-141

**Frage:** Gilt $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}})$ für $0 < \Re\beta \leq 1$?

---

### NEU-57: Singulärwert-Wachstum von $J^-$ ❓ [O]

> Eröffnet: 29. Juni 2026 — NEU-56

---

## Offen (mittelfristig)

### X.3.25 / X.3.24 / X.3.23 / X.3.16 / X.3.14 / X.2.1 / OP-4

> Unverändert gegenüber Stand NEU-161 rev.5 — siehe Archivversion.

---

## Abgeschlossene Probleme

### NEU-246 bis NEU-250 (6. August 2026)

| Eintrag | Thema | Resultat |
|---|---|---|
| NEU-246 | Typ-Grad-Kerninvarianzaudit, Koszul-Kandidat | ✓ [M] |
| NEU-247, 247a, 247b | Tensor-Lift Typbrücke, Domänenpräzisierung | ✓ [M] |
| NEU-248 | Wohldefiniertheit Tensoroperator | ✓ [M] |
| NEU-249 | Präzisierungen Notation/Konstruktion/Stabilität | ✓ [M] |
| NEU-250 | Wres-Minimalblock Kleinfallprüfung | ✓ [M] → **Ausgang E** |
| NEU-250a | Typisierung Dirichletresiduumsform, relativer Primkantenraum | ✓ [M]_part → **Ausgang B** |

### NEU-144 bis NEU-160 (Juli 2026)

> Vollständige Dokumentation in den thematischen Strangordnern. Stand unverändert.

### NEU-57 bis NEU-143 (29. Juni — 9. Juli 2026)

> Vollständige Dokumentation in den thematischen Strangordnern. Stand unverändert.

### NEU-1 bis NEU-56 (19. — 29. Juni 2026)

> Stand unverändert.

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

Aktueller Haupt-Engpass (Wres-Strang):
  j_{2,N}(E^rel_{R;1->2}) als explizites residuenfaehiges BC-Element  => [O-221-1c1a0-C]
```
