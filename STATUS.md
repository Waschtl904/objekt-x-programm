# Statusregister

Verdichtete Gesamtbilanz des Programms ohne Zwischenschritte. Für die vollständige
Dokumentliste siehe [INDEX.md](INDEX.md), für die Verzweigungsbedingungen der offenen
Knoten [OFFENE_PROBLEME.md](OFFENE_PROBLEME.md).

> Stand: 3. August 2026 · letzter Eintrag NEU-228 · Direktaudits NEU-210/211 verbucht

> **Konsolidierungsnotiz, aktualisiert 2. September 2026:** Dieses Statusregister bleibt die Bilanz des NEU-Journalkerns und ist **nicht** die operative Frontdatei. Aktuell maßgeblich sind [CURRENT-FRONT.md](CURRENT-FRONT.md), [ACTIVE_THEOREM_REGISTRY.md](00-uebersicht/ACTIVE_THEOREM_REGISTRY.md) und die aktuelle P11-Strong-Terminal-Auditfolge R38--R43. R38--R42 sind frozen als independently verified AI-GREEN ohne kanonische \(\checkmark[M]\)-Promotion; R43 ist offen. Strong Terminal/C6 ist auf einen fixed-pair Normal-Kernel-Koeffizienten reduziert; R37/G4c bleibt separat offen.
>
> Die in diesem Dokument referenzierten früheren Objekt-X-Architekturen — insbesondere
> Ebene XVI Revision 2 und die P04/Suzuki-Hypothese — sind seit 26. August 2026 als
> **historische Kandidaten-/Constraint-Architekturen** einzuordnen, nicht als aktuelle
> Identitätsdefinition von X. Ihre separat bewiesenen route-spezifischen Sätze und No-Gos
> behalten ihre jeweilige Provenienz und ihren lokalen Status.

Historisch reklassifizierte Karte der bis 26. Juli 2026 gebuchten Bedingungen, Brücken,
Realisierungsprofile und No-Gos:
[Ebene XVI — Kontrollblatt](00-grundlegung/ebene-XVI-objekt-x.md).
Sie ist weiterhin ein wichtiges Constraint-/Provenienzregister, aber **nicht** die aktuelle
Single Source of Truth für die Identität von Objekt X.

Kanonisches Eingangsblatt für den HH-Strang:
[AUDITSTAND-2026-08-03.md](AUDITSTAND-2026-08-03.md).

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

## Statuskorrekturen 2026-08-03 (Direktaudit NEU-210/211)

| Knoten | Alte Aussage | Neue Aussage | Status |
|---|---|---|---|
| [O-209-6c] | $M_{g,r}X_N \to 0$ in Norm | **widerlegt** — Gegenbeispiel $m=2,n=1,r=\tfrac{1}{2}$ | `✗[M]` |
| [O-209-6d] | (neu) | $M_{g,r}X_N$ schließlich konstant | `✓[M]` |
| [O-211-3] geschrieben | $D_g(e(r)) := 0$ | **widerlegt** — verletzt BC-Kreuzrelation | `✗[M]` |
| [O-211-3corr] | (neu) | $D_g^{\mathrm{corr}}(e(r)) = \mu_m C_{m,n;r} \mu_n^*$ | `✓[M]` |
| [O-charged-HH1-analytic] | offen | $[D_g^{\mathrm{corr}}] \neq 0$ in $HH^1(A_{\mathrm{alg}}, A_{C^*})_g$ — **erster gesicherter positiver HH-Befund im geladenen Sektor** | `✓[M]` |
| NEU-222 §0 | „[O-209-6] vollständig geschlossen“ | Nur [O-209-6a/b/d] geschlossen; [O-209-6c] `✗[M]` | Auditwarnung |
| HH-Kette NEU-212–218 | als tragfähig auf Basis NEU-211 | **Beweispflicht:** Kompatibilität mit $D_g^{\mathrm{corr}}$ zu prüfen | `?[O]` re-audit |

Vollständige Belege: [ARCHIV-AUDIT-NEU210.md](ARCHIV-AUDIT-NEU210.md), [ARCHIV-AUDIT-NEU211.md](ARCHIV-AUDIT-NEU211.md).

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
| **[O-charged-HH1-analytic]** $[D_g^{\mathrm{corr}}]\neq 0$ in $HH^1(A_{\mathrm{alg}},A_{C^*})_g$ | **NEU-211 (nach Direktaudit 2026-08-03)** |

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
| **[O-209-6c]** | $M_{g,r}X_N \to 0$ — **widerlegt** (Direktaudit 2026-08-03) | NEU-210 / ARCHIV-AUDIT-NEU210 |
| **[O-211-3] geschrieben** | $D_g(e(r)):=0$ — **widerlegt** (Direktaudit 2026-08-03) | NEU-211 / ARCHIV-AUDIT-NEU211 |
| Bimodul | globaler Bimodul-No-go via Zentralisatorbeweis | NEU-215 |
| **O-219** | $t\Phi_0 = g^{-\beta}\Phi_0$ mit $g^{-\beta}\neq 1$ — **keine gewöhnliche zyklische Klasse in $HC^4(A_{\mathrm{alg}})$** | NEU-219u |
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
| 0 | **HH-Kette re-audit** | NEU-212→216→217→218→222: Kompatibilität mit $D_g^{\mathrm{corr}}(e(r))=\mu_mC_{m,n;r}\mu_n^*$ | AUDITSTAND-2026-08-03 |
| 1 | `[O-221-1c1a0]` | Gilt $\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}$? | NEU-221e |
| 1b | `[O-221-1c1b/c/d]` | $E_{D}(\{0\})\Psi_N = 0$; inverse Momente; globale Kopplung in $D_{\mathrm{scatt},N}$ | NEU-221d |
| 2 | `[O-220-1]` | Adelische Quellkonstruktion der positiven Momentfolge (RH-stark) | NEU-220w / NEU-221 |
| 3 | `[O-161]` | Existiert ein explizit konstruiertes $\ell_{s_0,m_0}\neq 0$ mit $s_0\neq 0$? | NEU-161/162 |
| 4 | `[O-141-D]` | Regularisierungsschema für $\operatorname{Tr}_{\mathrm{reg}}$ im kritischen Streifen $0<\Re\beta\le 1$ | NEU-141 |
| 5 | `[O-223-2]` | Feshbach-Transfer $K_N(z)$; Leerfaser-Risiko $\mathcal L_p$; $\sum_p\operatorname{Tr}|M_p(z)|<\infty$ | NEU-56/223/228 |
| 6 | `[X.3.25]` | $\sup_a \sum_b \lvert\Theta_{ba}\rvert/\ell(a) < \infty$ exakt? | NEU-55 |
| 7 | `[O-188-0..3]` | $H\notin\mathrm{LC}(\hat{\mathbb Z})$ mit $\alpha_k(H)-H\in\mathrm{LC}(\hat{\mathbb Z})$? | NEU-188 |
| 8 | — | Rückrichtung: $\operatorname{Spec}\subset\mathbb R \Rightarrow \mathrm{RH}$ | — |

> **Aktuellere P11-Front:** Die obige Prioritätenliste ist der NEU-Journalkern vom
> 3. August und nicht mehr operativ. Nach der negativen finite-level SW1-Entscheidung wurde
> die aktive Forschung auf B / Strong Terminal verlagert. R38--R42 sind frozen; R43 ist der
> offene aktuelle Block. Der fixed-pair C6-Gate lautet
> \(\operatorname{Re}\langle\varepsilon_R,K_{R,S}^{T,U}\varepsilon_R\rangle\to1\ ?\).
> Siehe CURRENT-FRONT und ACTIVE_THEOREM_REGISTRY.

---

## 6. Bewusste Kataloglücken

| Nummer | Grund |
|---|---|
| NEU-126 | Rückleseprotokoll $W_N$ (NEU-62). Teile 126.A und 126.B verloren; nur Gesamtzweck und 126.C inhaltlich bekannt. Eine Rekonstruktion aus Zusammenfassungen wurde als methodisch nicht vertretbar verworfen. Der inhaltliche Anschluss läuft direkt über NEU-127. |
| NEU-1 – NEU-9 (ohne NEU-3) | Vorlaufeinträge vor Beginn der systematischen Journalführung; nicht als eigene Blätter erhalten |
| NEU-57 | als eigenes Blatt nie angelegt — der Knoten (Singulärwert-Wachstum von $J^-$) wird in NEU-56 geführt |
| NEU-129, NEU-191, NEU-198, NEU-221a/b | im Journal übersprungen; der inhaltliche Anschluss läuft über den jeweils folgenden Eintrag |

**Historischer Hinweis zur Ebenentrennung (Ebene XVI Revision 2):** HP-1–HP-7 wurden dort als **Realisierungsbedingungen** für $H_X$, nicht als Axiome von $X$, geführt. Seit 26. August 2026 ist Ebene XVI selbst als historisches Constraint-/Architekturblatt reklassifiziert; diese Ebenentrennung bleibt als lokale Buchführungsregel der damaligen Architektur gültig.

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