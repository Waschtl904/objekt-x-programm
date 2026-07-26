# Offene Probleme — Konsolidierte Liste

> **Aktuelle Front: 26. Juli 2026 — NEU-221e**  
> Der untere Teil dieser Datei ist der konsolidierte Stand vom 15. Juli 2026 (NEU-161 rev.5).
> Er bleibt gültig, soweit er nicht durch die aktuelle Front überholt ist.

Kompakte Gesamtbilanz: [STATUS.md](STATUS.md) · Alle Dokumente: [INDEX.md](INDEX.md) ·
Verbindliche Karte aller Bedingungen an Objekt X: [Ebene XVI — Kontrollblatt](00-grundlegung/ebene-XVI-objekt-x.md)

> **Ebenentrennung beachten.** HP-1–HP-7 sind Realisierungsbedingungen für $H_X$, keine
> Axiome von $X$. Das Stieltjes-Profil des NEU-221-Strangs impliziert das HP-Profil **nicht**
> — Fortschritt an `[O-221-1c1a–d]` darf nicht als Fortschritt an HP-2/HP-3 verbucht werden.

---

# Teil I — Aktuelle Front (Stand NEU-221e)

## Priorität 1 — Hebungsabstieg des Kopplungsvektors

### `[O-221-1c1a0]`: Zulässige Differenzmenge und Rohkopplung ❓ [O]

> Eröffnet: 26. Juli 2026 — NEU-221e · Vorgänger `[O-221-1c1a]` `✓[M]_part`

**Ausgangslage.** NEU-46 verwendet den relativen Vektor als **zyklischen** Vektor einer
Weyl-Funktion. Damit ist die Hebungsfrage **nicht** durch Normgleichheit entschieden:
Verschieden gewählte, gleich normierte Hebungen können verschiedene
Resolventenmatrixstellen, Spektralmaße und inverse Momente erzeugen. Norminvarianz
entspricht nur dem Test $f\equiv 1$.

**Bewiesenes Kriterium (NEU-221e).** Der Kopplungsvektor steigt genau dann von der
Hebungsfaser auf den primitiven Kanal ab, wenn

$$\widetilde T_p^{\mathrm{raw}}\bigl(\Delta_p^{\mathrm{adm}}\bigr) \subseteq \mathcal N_{\mathrm{Wres,rel}},
\qquad \Delta_p^{\mathrm{adm}} = \mathcal A_p^{\mathrm{adm}} - \mathcal A_p^{\mathrm{adm}}.$$

Die stärkere Inklusion auf ganz $K_p$ ist hinreichend, aber nur äquivalent, wenn jede
Kernrichtung als Differenz exakt zulässiger Hebungen realisiert wird — nicht bewiesen.

**Drei Aufgaben des Knotens:**

1. Alle Bedingungen an eine Hebung als homogen-linear, affin, quadratisch oder nichtlinear
   klassifizieren und $\widehat{\mathcal E}_p^{\mathrm{adm}}$ vollständig definieren.
   Postulierte, nicht konstruierte Operatoren ($R_{p,j}$, NEU-165b) sind unzulässig.
2. Rohzielraum $\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}$, Wres-Radikal
   $\mathcal N_{\mathrm{Wres,rel}}$ und Quotientenabbildung explizit fixieren.
3. Den Test auf Erzeugern bzw. expliziten Kurven in $\Delta_p^{\mathrm{adm}}$ rechnen.

**Typwarnungen.** Bei indefiniter Form ist das Radikal **nicht** die Menge isotroper
Vektoren. Der Schluss von $C_pC_p^{\#}=C_p'C_p'^{\#}$ auf Phasenäquivalenz setzt die
positive Hilbertrealisierung voraus. Die Rang-eins-Eigenschaft von
$C_p[\widehat\varepsilon_p]$ folgt aus dem eindimensionalen Definitionsraum und sagt nichts
über Rang oder Beschränktheit von $T_p^{\mathrm{rel}}$.

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

**Frage:** Lässt sich $(\mu_k)$ als Momentfolge eines adelisch konstruierten positiven
Operators realisieren — und nicht nur als Umformulierung der RH?

Dies ist der Knoten, an dem NEU-221 ansetzt. Das Moment-GNS-Weyl-Modell aus NEU-220w ist
**konditional zur Positivitätsvoraussetzung** — es setzt voraus, was zu zeigen wäre.

**Forschungsdokument:** [`NEU-220w`](07-weil-explizitformel/NEU-220w_Hankelvollstaendigkeit_Moment-GNS_und_semifinite_Atomizitaet.md)

---

## Priorität 3 — Reparaturpfade nach dem O-219-No-Go

### `[O-219-6]`: Zyklizität ohne gewöhnliche Zyklizität ❓ [O]

> Eröffnet: 24. Juli 2026 — NEU-219u

Das No-Go-Theorem zeigt $t\Phi_0 = g^{-\beta}\Phi_0$ mit eingabeunabhängigem $g^{-\beta}\neq 1$.
Jede positive Reparatur muss mindestens eine Struktur wirklich ändern:

| Reparaturpfad | Anforderung | Status |
|---|---|---|
| Orbitshift | Lift mit $\kappa \neq 0$; benötigt explizit $T^k$ oder $\tau^k$ | Neue Konstruktion, eigener Knoten |
| Ladungsneutralisation | algebraische Neutralisation vor der zyklischen Auswertung | Neue Konstruktion |
| Andere Koeffizientenkategorie | parazyklisch, $\sigma$-zyklisch, getwistet-zyklisch | `[O-219-5]` teilweise beschritten |
| Weil-/Gammafaktorpaarung | gewöhnliche Zyklizität ersetzen | **aktiv beschritten** ab NEU-220 |

**Forschungsdokument:** [`NEU-219u`](06-hochschild-bc-algebra/NEU-219u_Abschluss_O219_NoGo_Theorem.md)

---

### `[O-188-0]` – `[O-188-3]`: Erweiterbarkeit punktierter Kozykel ❓ [O]

> Eröffnet: 19. Juli 2026 — NEU-188

**Frage:** Existiert $H \notin \mathrm{LC}(\hat{\mathbb Z})$ mit $\alpha_k(H) - H \in \mathrm{LC}(\hat{\mathbb Z})$
für alle $k$?

Dies ist die zentrale Regularitätsbedingung für den **teilerfremden** Teil, aber kein
vollständiges Äquivalent zur Erweiterbarkeit. Ein geeignetes $H$ muss zusätzlich die
Transferbedingungen bei nicht teilerfremden Indizes erfüllen `[O-188-2]`, mit der
differenzierten Projektionsrelation $\mu_k\mu_k^* = \tfrac1k\sum_j e(j/k)$ verträglich sein (E3),
sämtliche Kreuzrelationen respektieren (E7, `[O-188-3]`) und tatsächlich eine Derivation auf
dem vollständigen $A_{\mathbb Q}^{\mathrm{alg}}$ definieren — nicht nur formal auf Generatoren.

Das Resultat „nichttriviale Klasse $\Rightarrow$ äußere Derivation" (Satz 188.2) ist daher
**konditional**, nicht unbedingt gesichert.

---

# Teil II — Konsolidierter Stand vom 15. Juli 2026 (NEU-161 rev.5)

> Die folgenden Einträge stammen aus dem Stand vor dem kohomologischen und dem
> Weil-Strang. Sie sind weiterhin offen, stehen aber nicht mehr an der aktiven Front.

---

## Kritisch — Engpass des Standes NEU-161

### NEU-161: Nichttriviale Fourierladung von $L_3^\circ$ ❓ [O]

> Eröffnet: 15. Juli 2026

**Frage:** Existiert ein explizit konstruierter Fourierkoeffizient $\ell_{s_0,m_0}\neq 0$ mit $s_0\neq 0$ in $L_3^\circ = \sum_{s,m}\ell_{s,m}e_sV_m$?

**Quellenprüfungsbefund (161.A):** Früheste Quelle ist NEU-42 §10 (`01-primkanten-werkzeuge/NEU-042_x3_fourierhebung_laplace_p_minus_s.md`). Dort ist $s\neq 0$ **Rechenbedingung, kein Ergebnis** — kein konstruktiv fixierter Vektor, keine explizite Formel für $\ell_{s,m}$. Zusätzlich offen (NEU-42 §6): $L_3^\circ$ muss auf $m=1$ projizieren oder relativ normalisiert werden.

**Ausgangsbefund:** $?[O]$ — Nichttrivialität nur vorausgesetzt.

**Verzweigung (161.B):**

| Marker | Bedingung | Folge |
|---|---|---|
| $\checkmark[M]$ | Explizites $\ell_{s_0,m_0}\neq 0$ konstruiert | Zeugenroute 161.C–E beginnt |
| $\checkmark[M]_{\exists\text{-Wahl}}$ | Zulässige Wahl $L_3^\circ=e_{s_0}V_{m_0}$, $m$-Bedingung geprüft | Zeugenroute 161.C–E beginnt |
| $\checkmark[M]_{\mathrm{deg}}$ | Strukturelle Nullladung | Degeneration des Kopplungsmechanismus |

**Nächste Aufgabe:** Neues Blatt NEU-162 — Konstruktion oder zulässige Wahl von $\ell_{s_0,m_0}\neq 0$.

**Forschungsdokument:** `05-primkanal-fourierladung/NEU-161_Nichttriviale_Fourierladung_L3circ.md`

---

## Kritisch — Zweiter offener Hauptstrang

### NEU-141.D: Regulierte Spur im kritischen Streifen ❓ [O]

> Eröffnet: Juli 2026 — NEU-141

**Frage:** Gilt $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}) $ für $0 < \Re\beta \leq 1$?

| Ebene | Objekt | Status |
|---|---|---|
| S1-Existenz | $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$, $\Re\beta > 0$ | ✓ [M] NEU-137 |
| Mangoldt-Spur gewöhnlich | $R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$, $\Re\beta > 1$ | ✓ [M] |
| Regulierte Spur (krit. Streifen) | $\operatorname{Tr}_{\mathrm{reg}}$, $0 < \Re\beta \leq 1$ | ❓ [O] |

**Nächste Aufgabe:** NEU-141.D — Regularisierungsschema für $\beta\downarrow 0$.

---

### NEU-57: Singulärwert-Wachstum von $J^-$ ❓ [O]

> Eröffnet: 29. Juni 2026 — NEU-56

**Frage:** Divergiert die Singulärwert-Asymptotik $s_k(J^-|_{H_{\mathrm{rel}}^{\mathrm{eff}}})$ (Weg A über $\tilde L$ wieder möglich) oder akkumuliert sie (nur Weg B)?

```
1. Singulärwert-Asymptotik s_k(J^-|H_rel^eff): divergent oder akkumulierend?
2. Gilt Sum_p Tr|M_p(z)| < infty gleichmäßig auf Kompakta? (Spurklasse via K_pq, NEU-51)
3. Ist die RH-Hinrichtung mit reiner Spektralmaß-Form (Weg B) vollständig
   formulierbar, ohne Weg A?
```

**Forschungsdokument:** `01-primkanten-werkzeuge/NEU-056_x3_gammaN_konfinement_obstruktion.md`

---

## Offen (mittelfristig)

### X.3.25: Schur-Test exakt (Nelson-Bed. 1) ❓ [O]

> 29. Juni 2026 — NEU-55

Gilt $\sup_a \sum_b |\Theta_{ba}|/\ell(a) < \infty$ exakt (nicht nur heuristisch)?
Heuristik ist plausibel, exakter Beweis ausstehend.

**Forschungsdokument:** `01-primkanten-werkzeuge/NEU-055_x3_nelson_matrixabschaetzung_schur.md`

---

### X.3.24: Essentielle Selbstadjungiertheit von $iJ^-$ ⚠ [M] (unter Bedingungen)

> 29. Juni 2026 — NEU-53–55

**Gesichert (unter Nelson-Bedingungen):** $iJ^-$ wesentlich selbstadjungiert auf $D_0^{\mathrm{eff}}$.
**Offen:** Exakter Nachweis der Nelson-Bedingungen (Schur-Test, $\gamma_N$-Wahl).

**Forschungsdokument:** `01-primkanten-werkzeuge/NEU-054_x3_nelson_selbstadjungiertheit_konfinement.md`

---

### X.3.23: Spektralalternativen für $D_{\mathrm{rel}}$ ❓ [O]

> 29. Juni 2026 — NEU-53

| Weg | Voraussetzung | Status |
|---|---|---|
| A — Diskret | Kompakter Resolvent | ❓ [O] — hängt von Konfinement |
| B — Spektralmaß | Nur Selbstadjungiertheit | ✓ [M] strukturell, robuster Standard |
| C — Gemischt | — | ❓ [O] |

**Forschungsdokument:** `01-primkanten-werkzeuge/NEU-053_x3_operatorstatus_drel_selbstadjungiertheit.md`

---

### X.3.16: Intrinsizität von $Wres_{\mathrm{rel}}$ ❓ [O]

> 28. Juni 2026 — NEU-44

**Frage:** Kann die kantendiagonale relative Paarung direkt aus $Wres_{BC}^{\mathrm{top}}$ und der $\tilde\omega_2$-Korrespondenz abgeleitet werden?

**Gesichert (NEU-44):** Pullback-$Wres$ nicht kantendiagonal ✗ [M]; kantendiagonale Hebung $Wres_{\mathrm{rel}}$ als Definition ✓ [M].

---

### X.3.14: Gamma-Faktor-Intrinsifizierung ❓ [O]

Archimedische Korrektur (Gamma-Faktor) im relativen Graphraum.
Gesichert: $\xi'/\xi$ aus Gamma-Korrektur von $\zeta'/\zeta$ (NEU-28). Offen: Formulierung auf $H_{\mathrm{rel},N}$.

---

### X.2.1: Rückrichtung RH ❓ [O]

```
RH => Spec(A_N^-) subset R   [Hinrichtung: strukturell plausibel]
Spec(A_N^-) subset R => RH  [Rückrichtung: offen]
```

---

### OP-4: Frobenius-Funktional auf $A_{2D}^r$ ❓ [O]

Verbindung: OP-4 und X.6 könnten dasselbe Problem sein.

---

## Abgeschlossene Probleme

### NEU-144 bis NEU-160 (Juli 2026)

> Diese Einträge sind in den thematischen Strangordnern dokumentiert. Kurzübersicht:

| Eintrag | Thema | Resultat |
|---|---|---|
| NEU-144–150 | Weitere Ausarbeitung Spurklassen, Selbstenergie, Kanalgewichte | ✓/⚠ [M] |
| NEU-151–160 | Präzisierungen Zeugenroute, Kantengeometrie, Separationsbedingungen | ✓/⚠ [M] |
| **NEU-161 rev.1–2** | Zeugenroute Grundstruktur, Verzweigungsknoten | ✓ [M] strukturell |
| **NEU-161 rev.3** | Dritter Ausgang $?[O]$ als Rückverlagerung, nicht Scheitern | ✓ [M] |
| **NEU-161 rev.4** | Funktionalanalytische Präzisierung Variante B; Hahn–Banach / Koordinatenfunktional | ✓ [M] |
| **NEU-161 rev.5** | Quellenprüfung NEU-42 §10 abgeschlossen; Befund $?[O]$ eingetragen | ✓ [M] Protokoll |

### NEU-57 bis NEU-143 (29. Juni — 9. Juli 2026)

> Vollständige Dokumentation in den thematischen Strangordnern. Ausgewählte Meilensteine:

| Eintrag | Thema | Resultat |
|---|---|---|
| NEU-57 | Singulärwert-Wachstum $J^-$ | Engpass eröffnet ❓ [O] |
| NEU-100–112 | Formfaktor, Weil, Jacobi-Realisierung | ✓ [M] |
| NEU-113–120 | Bombieri-Normalisierung, $C_\xi$-Fix | ✓ [M] |
| NEU-121–123 | Jacobi-Grenzoperator, Renormierungsbarriere | ✓/⚠ [M] |
| NEU-125, 130 | PSWF-Brücke, Prä-Lanczos-Metrik | ✓ [M] |
| NEU-131 | Edge-Schur-Nelson-Lemma (abstrakt) | ✓ [M] |
| NEU-132–133 | $H_1/H_2/H_3$-rel, Primschalen-Abel-Lemma | ✓/❓ [M/O] |
| NEU-134 | Relative Kanalgewichte $|c_p|^2 = O((\log p)^2/p)$ | ❓ [O] |
| NEU-135D | Welt-2-Entscheidung; $\|\varepsilon_p\|^2=1$ | ✓ [M] |
| NEU-141 | $R_p\gtrsim p/\log p$; drei Spurklassen-Ebenen | ✓ [M] (S1+S2); ❓ [O] (S3) |
| NEU-142–143 | T2-Audit (Edge vs. Vertex), T2-Abschluss | ✓ [M] unter Orthogonalität |

### NEU-1 bis NEU-56 (19. — 29. Juni 2026)

| Problem | Zugang | Resultat |
|---|---|---|
| OP-1: Spektralinvarianz $A_{2D}^r$ | NEU-10 | Jauré–Măntoiu 2022 ✓ [M] |
| OP-2: $[\omega_2]\neq 0$ | NEU-15 | BV-Argument ✓ [M] |
| OP-3: $[L_3]\neq 0$ | NEU-17–20 | $C'_{4,1}\neq 0$ ✓ [M] |
| OP-4.1: Frobenius-Wodzicki | NEU-21–25 | B beiderseitig nicht-ausgeartet ✓ [M] |
| Mangoldt-Schicht (X.3.9) | NEU-39 | $P_N + \operatorname{Tr}^{\mathrm{conn}} \Rightarrow \zeta'/\zeta$ ✓ [M] |
| Kanonischer Kopplungsoperator | NEU-41 | Fourier-geladene Hebung ✓ [M] |
| Laplace-Realisierung $p^{-s}$ | NEU-42 | $T_p^{\mathrm{rel}}=\log p$ ✓ [M] |
| Reinheitslemma Graph | NEU-43 | $\Pi_{\mathrm{rel},p}\Psi_p=\Psi_p$ ✓ [M] |
| $pq$-Kollisionstest | NEU-44 | Graphraum strukturell notwendig ✓ [M] |
| Drei-Determinanten-Bild | NEU-45 | $D_{\mathrm{prim}}$ exakt, Weyl-Korr. identifiziert ✓ [M] |
| Weyl-Korrekturen $M_p(z)$ | NEU-46 | Strukturell kontrolliert ✓/⚠ [M] |
| Archimedische Separation | NEU-47 | Hadamard-Divisor-Zuordnung ✓ [M] |
| Residuenbilanz, Divisorneutralität | NEU-48 | ✓ [M] |
| Birman-Schwinger-Indexsatz | NEU-49 | ✓/✗ [M] |
| Off-Diagonal-Kopplung | NEU-50 | Direkt-Summen-Obstruktion ✗ [M] |
| Resolventen-Matrixelement $K_{pq}$ | NEU-51 | Spurklasse-Form ✓/⚠ [M] |
| Spektralbasis $\eta$ vs. Eigenbasis | NEU-52 | Globale Spektralformel ✓/✗ [M] |
| Drei-Ebenen Spektralalternativen | NEU-53 | Robuste Spektralmaß-Form ✓ [M] |
| Nelson-Strategie + flache Achsen | NEU-54 | Hauptbeweis-Weg gesetzt ⚠ [M] |
| Matrixabschätzung Nelson-Bed. | NEU-55 | Heuristisch plausibel ✓/⚠ [M] |
| $\gamma_N$-Spannung / Konfinement | NEU-56 | $C/\log N$ widerlegt; skalar unvereinbar; SA bleibt ✗/✓ [M] |

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

Aktueller Haupt-Engpass:
Nichttriviale Fourierladung von L_3^circ  => NEU-162
```
