# Statusregister

Verdichtete Gesamtbilanz des Programms ohne Zwischenschritte. Für die vollständige
Dokumentliste siehe [INDEX.md](INDEX.md), für die Verzweigungsbedingungen der offenen
Knoten [OFFENE_PROBLEME.md](OFFENE_PROBLEME.md).

> Stand: 26. Juli 2026 · letzter Eintrag NEU-222

Verbindliche Karte aller Bedingungen an Objekt X, nach logischen Ebenen getrennt:
[Ebene XVI — Kontrollblatt](00-grundlegung/ebene-XVI-objekt-x.md).

---

## Legende

| Marke | Bedeutung |
|---|---|
| `✓ [M]` | vollständig bewiesen |
| `✓ [K]` | konstruktiv/typgeprüft — Objekt wohldefiniert, Konsequenzen offen |
| `✓ [R]` | Reduktionssatz oder methodisches Resultat |
| `⚠ [M]` | konditional — gilt unter noch offenen Voraussetzungen |
| `✗ [M]` | No-Go — Route gesichert ausgeschlossen |
| `❓ [O]` | offener Knoten |

Zusätze: `_part` teilweise geschlossen · `_neg` negativ geschlossen · `[K/M]` konstruktiv mit bewiesenen Teilaussagen.

---

## 1. Die beiden RH-Äquivalenzen

| Äquivalenz | Formulierung | Marke | Eintrag |
|---|---|---|---|
| Jacobi-Kanal | $\mathrm{RH} \iff \operatorname{Spec}(\lim_N A_N^{\mathrm{Jac},-}) \subset \mathbb R$ | `⚠ [M]` | NEU-63D |
| Herglotz-Form | $\mathrm{RH} \iff m_{\mathrm{arith}}(z)$ Herglotz | `⚠ [M]` | NEU-63D |
| Temperiertheit | RH-äquivalentes Kriterium über Prim-Pol-Renormierung | `✓ [M]` | NEU-220q |
| Similarity | beschränkte Similarity zu positiver Metrik $\iff$ RH | `✓ [M]` | NEU-220t |
| **Hankel-Kanal** | $\mathrm{RH} \iff H_N^{(0)}\succeq 0 \wedge H_N^{(1)}\succeq 0\ \forall N$ | `✓ [M]` | NEU-220w |

Der Hankel-Kanal ist die derzeit stärkste unkonditionale Äquivalenz des Programms:
Hin- und Rückrichtung sind vollständig bewiesen, mit den Momenten

$$\mu_k = -\frac{k+1}{(2k+2)!}\,(\log\Xi)^{(2k+2)}(0), \qquad H_N^{(0)}=(\mu_{i+j})_{i,j=0}^N,\quad H_N^{(1)}=(\mu_{i+j+1})_{i,j=0}^N.$$

Was fehlt, ist nicht die Äquivalenz, sondern eine **adelische Quellkonstruktion**, die
die Positivität der Momentfolge unabhängig liefert.

---

## 2. Gesicherter Kern `✓ [M]`

### Primkanten-Architektur

| Resultat | Eintrag |
|---|---|
| Relative Primkanten $\mathcal H_{\mathrm{rel},N} = \bigoplus_{p\le N}\bigoplus_m \mathcal H_{m\to pm}$ strukturell notwendig | NEU-44 |
| Kantendiagonalität von $\mathrm{Wres}_{\mathrm{rel}}$ (pq-Test) | NEU-44 |
| Rang-1-Struktur und explizite Definition von $C_p^{\mathrm{rel}}$, stabil unter Störungen | NEU-44.X / 44.X' |
| Relative Feshbach-Determinante mit Euler-Mangoldt-Struktur | NEU-45 |
| Fourier-Hebungsformel $T_p^{\mathrm{rel}} = \log p$ | NEU-42 |
| Reinheitslemma der relativen Primclock | NEU-43 |
| Welt-2-Entscheidung: $\lVert\varepsilon_p\rVert^2 = 1$, $\lvert c_p\rvert^2 = O((\log p)^2/p)$ | NEU-135D |
| Nichtentartung und Hebungsunabhängigkeit der Primkanalgewichte | NEU-152/153 |

### Analytischer Kanal

| Resultat | Eintrag |
|---|---|
| Arithmetische Identifikation der Weyl-/Stieltjes-Funktion | NEU-63 |
| Möbius-Feshbach-Identität, primitive Mangoldt-Reduktion | NEU-68 |
| Nicht-Backtracking-/Ihara-Reduktion des Divisorgraphen | NEU-70 |
| Bochner-Tor für logarithmische Korrelationskerne | NEU-94 |
| Renormalisierte Selbstenergie $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$: Zerlegung, Konvergenz, Spurklasse | NEU-136/137 |
| Mangoldt-Spur $\operatorname{Tr}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)) = -\zeta'/\zeta(\beta)$ für $\Re\beta>1$ | NEU-141 |
| PSWF-Brücke, abstraktes Edge-Schur-Nelson-Lemma, Primschalen-Abel-Lemma | NEU-130/131/133 |
| Geglättete Mellin-Finite-Part-Spur, Restkontrolle auf nullstellenvermeidenden Konturen | NEU-148/149 |
| Xi-Masterkontur: exakte Vorzeichen, Faktor 2, Polresiduen, keine Doppelzählung trivialer Nullstellen | NEU-220k |
| Konvergenz der Nullstellensumme und Horizontalabschätzung | NEU-220k |

### Kohomologischer Kanal

| Resultat | Eintrag |
|---|---|
| Minimaler Hochschild-Komplex mit induzierter BC-Zeitwirkung | NEU-174 |
| Gewichtraumkomplex und geladener Kettenprojektor | NEU-175 |
| Vier-Prim-Polynommodell: explizite geladene $HH^4$-Klasse und Dualzyklus | NEU-178 |
| Restriktionssatz für geladene äußere Derivationen | NEU-187 |
| Logarithmischer Koeffiziententyp $\mathcal B^{\log}$: submultiplikative Norm ohne Renormierung, scharfe Konstanten, Transportstabilität | NEU-216 |
| Geladener Koeffiziententyp $\mathcal A^{\log}$ konstruiert, $D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}$ | NEU-216 |
| Lokaler $p$-Block, globale Nichtinnerheit, Grad-1-Pfad geschlossen | NEU-217 |
| Cup-Aufstieg: $L^{\mathrm{cup}}_{g;\mathbf p}\in Z^4(A_{\mathrm{alg}},M)_g$ | NEU-218 |
| Vollständige $U_{g^{-1}}$-Buchführung, $s=-1$ global bewiesen | NEU-219t |

---

## 3. No-Go-Resultate `✗ [M]`

| No-Go | Aussage | Eintrag |
|---|---|---|
| Kategorial | $X \neq m_{\mathrm{arith}}$; $m_{\mathrm{arith}} = \Pi_\gamma(X)$ ist nur der Spektralschatten | NEU-114/115 |
| Direkt-Summe | Obstruktion für den kollektiven Birman–Schwinger-Operator | NEU-50 |
| Dichte | kanalabhängige Kopplung erfüllt die Dichtebedingung der Labelmenge nicht | NEU-82 |
| Nilpotenz | Barriere für Spur und Determinante | NEU-86 |
| Normierung | Bruch zwischen Spurklasse und Mangoldt-Spur; $R_p \gtrsim p/\log p$ unbeschränkt | NEU-140/141 |
| Skalar-Renormierung | keine skalare Renormierung der Jacobi-Koeffizienten möglich | NEU-123.H |
| Nullkozykel regulär | $Z(A_{\mathbb Q})_g = 0$ für $g\neq 1_\Gamma$ | NEU-182/183 |
| Nullkozykel verdreht | $Z^0(A,{}_{\mathrm{id}}A_{\sigma_\beta}) = 0$ für $\Re\beta>0$ | NEU-183 |
| Augmentationsblindheit | reguläre Potentiale sind im Kommutatorquotienten unsichtbar | NEU-196/200 |
| Charakterkern | Singularträger separierbarer Primkanäle, Ketten-No-go | NEU-207/209 |
| Bimodul | globaler Bimodul-No-go via Zentralisatorbeweis | NEU-215 |
| **O-219** | $t\Phi_0 = g^{-\beta}\Phi_0$ mit $g^{-\beta}\neq 1$ — der kanonische Basislift liefert **keine** gewöhnliche zyklische Klasse in $HC^4(A_{\mathrm{alg}})$ | NEU-219u |
| Off-Axis | Trägheitsklassifikation aller Metrikblöcke; Positivitäts-No-Go und Similarity-No-Go | NEU-220t |
| Determinante | gewöhnliche Spurklassen-Determinante für $\Xi$ ausgeschlossen | NEU-220u |
| Hilbertspur | operatorischer Ursprung von $\Lambda_\Gamma$ erfordert semifinite, nicht gewöhnliche Spur | NEU-220e |

### Was das O-219-No-Go präzise sagt

$$\tilde L_0 \in Z^4(A_{\mathrm{alg}}, I_0) \quad\text{(typkorrekt)}, \qquad t\Phi_0 = g^{-\beta}\Phi_0, \qquad g^{-\beta}\neq 1.$$

Der Faktor $g^{-\beta}$ ist **eingabeunabhängig** — alle $h_i^{\pm\beta}$ heben sich auf —
und wird durch die Spektraleigenschaft von $U_{g^{-1}}$ im KMS-Zustand strukturell erzwungen.
Kein Orbitgewicht $\lambda$ kann ihn kompensieren, da $\tilde L_0(A_{\mathrm{alg}}^{\otimes 4})\subseteq I_0$
den Faktor $\lambda^0=1$ trägt.

Zulässige Reparaturpfade — jeder erfordert eine neue Konstruktion:

| Pfad | Anforderung |
|---|---|
| Orbitshift | Lift mit $\kappa\neq 0$; benötigt explizit $T^k$ oder $\tau^k$ |
| Ladungsneutralisation | algebraische Neutralisation vor der zyklischen Auswertung |
| Andere Koeffizientenkategorie | parazyklisch, $\sigma$-zyklisch oder getwistet-zyklisch |
| Weil-/Gammafaktorpaarung | gewöhnliche Zyklizität ersetzen — dies ist der ab NEU-220 beschrittene Pfad |

---

## 4. Konditionale Resultate `⚠ [M]`

| Resultat | Offene Voraussetzung | Eintrag |
|---|---|---|
| Essentielle Selbstadjungiertheit von $iJ^-$ auf $D_0^{\mathrm{eff}}$ | exakter Nachweis der Nelson-Bedingungen (Schur-Test, $\gamma_N$-Wahl) | NEU-53–55 |
| Selbstadjungiertheit von $D_N^{\mathrm{rel}}$ | Nelson-Matrixabschätzung und Konfinement | NEU-53/54 |
| Automatische Äußerlichkeit geladener Derivationen | Existenz einer vollständigen Erweiterung auf $A_{\mathbb Q}^{\mathrm{alg}}$ | NEU-188 |
| Hankelvollständigkeit und Moment-GNS-Weyl-Modell | Positivitätsvoraussetzung | NEU-220w |
| Nullstellenterm $\to \sum_\gamma \lvert\hat f(\gamma)\rvert^2$ strukturell | Bombieri-Normalisierung exakt | NEU-112/113 |
| Test 114.4: $m\to p^k m \Rightarrow \Lambda(p^k)$ | vollständige Rückbindung an $X$ | NEU-114 |

---

## 5. Offene Hauptknoten `❓ [O]`

Nach Dringlichkeit geordnet.

| # | Knoten | Frage | Eintrag |
|---|---|---|---|
| 1 | `[O-221-1c1a0]` | Gilt $\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}$? Erfordert: $\widehat{\mathcal E}_p^{\mathrm{adm}}$ vollständig definieren, Rohzielraum und Wres-Radikal fixieren, Test auf der Differenzmenge rechnen. Normgleichheit genügt nicht — verlangt ist Invarianz des zyklischen Spektralmaßes | NEU-221e |
| 1b | `[O-221-1c1b/c/d]` | $E_{D}(\{0\})\Psi_N = 0$; $\int\lvert\lambda\rvert^{-2k-2}d\mu_{\Psi_N}<\infty$ für $k=0,1,2$; globale Kopplung in $D_{\mathrm{scatt},N}$ | NEU-221d |
| 2 | `[O-220-1]` | Adelische Quellkonstruktion der positiven Momentfolge (RH-stark) | NEU-220w / NEU-221 |
| 3 | `[O-161]` | Existiert ein explizit konstruiertes $\ell_{s_0,m_0}\neq 0$ mit $s_0\neq 0$ in $L_3^\circ = \sum_{s,m}\ell_{s,m}e_sV_m$? | NEU-161/162 |
| 4 | `[O-141-D]` | Regularisierungsschema für $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}})$ im kritischen Streifen $0<\Re\beta\le 1$ | NEU-141 |
| 5 | `[O-57]` | Divergiert $s_k(J^-\vert_{H_{\mathrm{rel}}^{\mathrm{eff}}})$ oder akkumuliert es? Gilt $\sum_p \operatorname{Tr}\lvert M_p(z)\rvert<\infty$ gleichmäßig auf Kompakta? | NEU-56/57 |
| 6 | `[X.3.25]` | Gilt $\sup_a \sum_b \lvert\Theta_{ba}\rvert/\ell(a) < \infty$ exakt statt nur heuristisch? | NEU-55 |
| 7 | `[O-188-0..3]` | Existiert $H\notin \mathrm{LC}(\hat{\mathbb Z})$ mit $\alpha_k(H)-H\in\mathrm{LC}(\hat{\mathbb Z})$ für alle $k$, verträglich mit allen Kreuzrelationen? | NEU-188 |
| 8 | — | Rückrichtung: $\operatorname{Spec}\subset\mathbb R \Rightarrow \mathrm{RH}$ | — |

---

## 6. Bewusste Kataloglücken

| Nummer | Grund |
|---|---|
| NEU-126 | Rückleseprotokoll $W_N$ (NEU-62). Teile 126.A und 126.B verloren; nur Gesamtzweck und 126.C inhaltlich bekannt. Eine Rekonstruktion aus Zusammenfassungen wurde als methodisch nicht vertretbar verworfen. Der inhaltliche Anschluss läuft direkt über NEU-127. |
| NEU-1 – NEU-9 (ohne NEU-3) | Vorlaufeinträge vor Beginn der systematischen Journalführung; nicht als eigene Blätter erhalten |
| NEU-57 | als eigenes Blatt nie angelegt — der Knoten (Singulärwert-Wachstum von $J^-$) wird in NEU-56 geführt |
| NEU-129, NEU-191, NEU-198, NEU-221a/b | im Journal übersprungen; der inhaltliche Anschluss läuft über den jeweils folgenden Eintrag |

**Hinweis zur Ebenentrennung (ab Ebene XVI Revision 2):** HP-1–HP-7 sind **Realisierungsbedingungen** für $H_X$, keine Axiome von $X$. Das Stieltjes-Profil des NEU-221-Strangs impliziert das HP-Profil **nicht**.

---

## 7. Nummernkollisionen

Mehrere Journalnummern wurden bei parallelen Verzweigungen doppelt vergeben. Beide
Dokumente sind erhalten und über den Index unterscheidbar.

| Nummer | Dokumente |
|---|---|
| NEU-10 | drei Werkzeugblätter (RD-Skalenkorrektur, Beurling-Groupoid, OP-16f4b-Verifikation) |
| NEU-13, NEU-15, NEU-16 | je zwei Werkzeugblätter |
| NEU-118 | Bombieri-Normalisierung / X-Rigidität R1-Nachweis |
| NEU-123.F | Ergebnisblatt / numerische Diagnose |
| NEU-166b | Rollen-/Provenienzentscheidung / Typ-Domänen-Deszentaudit |
| NEU-183 | Quellen-/Präsentationsaudit / Zentrumstest |
| NEU-193 | dualer Hochschildzyklus / Paarungstest |
| NEU-217 | lokaler $p$-Block / gcd-Fallzerlegung / lokal-globaler Klebeknoten |
| NEU-218 | Cup-Aufstieg / vollständiger Abschluss |
| NEU-219 | Finalaudit / zyklischer Koeffiziententyp |
| NEU-219u | No-Go-Theorem / Abschlussaudit |
| NEU-219y | Zieltypbrücke $D_g$ / Unit-Slot-Zeuge |
| NEU-220k | Konturtransport-Konvergenz / Xi-Masterkontur |
