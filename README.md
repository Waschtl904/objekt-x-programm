# Objekt-X-Programm

**Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese**

Spektrale, nichtkommutative und arithmetische Zugänge zur RH — dokumentiert als
lückenlos nachvollziehbare Kette aus Konstruktionen, Tests, Audits und No-Go-Resultaten.

> **Stand:** 26. Juli 2026 · **letzter Eintrag:** NEU-226 · **330 Forschungsdokumente**

[Kontrollblatt Objekt X](00-grundlegung/ebene-XVI-objekt-x.md) · [Gesamtindex](INDEX.md) · [Statusregister](STATUS.md) · [Offene Probleme](OFFENE_PROBLEME.md) · [Glossar](GLOSSAR.md) · [Konventionen](KONVENTIONEN.md) · [Literatur](REFERENCES.md) · [Einstiegsprompt](EINSTIEGSPROMPT.md)

---

## Worum es geht

Das Programm untersucht, ob sich die Riemannsche Hypothese als **Spektraleigenschaft eines
konkret konstruierten Operatorobjekts** formulieren lässt — genannt **Objekt X**.

$$
\text{Objekt X} \;=\; \bigl(A_{2D}^{r},\; [\tilde\omega_2],\; [L_3],\; \mathrm{Wres}^{\mathrm{top}}_{\mathrm{BC}},\; m \xrightarrow{\;p\;} pm \bigr)
$$

Die fünf Komponenten sind: eine 2-dimensionale Spektraltripel-Algebra, eine
Hochschild-2-Klasse, eine Hochschild-4-Klasse, die Wodzicki-Residuum-Spurform auf der
Bost–Connes-Algebra sowie die fünfte Schicht der **relativen Primkanten** $m \to pm$.

Zwei RH-Äquivalenzen strukturieren das Programm:

$$
\mathrm{RH} \iff \operatorname{Spec}\bigl(\lim_N A_N^{\mathrm{Jac},-}\bigr) \subset \mathbb{R}
\qquad\text{(Jacobi-Kanal, NEU-63D)}
$$

$$
\mathrm{RH} \iff H_N^{(0)} \succeq 0 \ \text{ und } \ H_N^{(1)} \succeq 0 \quad \forall N \ge 0
\qquad\text{(Hankel-Kanal, NEU-220w)}
$$

mit den Hankelmatrizen $H_N^{(0)}=(\mu_{i+j})_{i,j\le N}$, $H_N^{(1)}=(\mu_{i+j+1})_{i,j\le N}$
über den Momenten $\mu_k = -\tfrac{k+1}{(2k+2)!}(\log\Xi)^{(2k+2)}(0)$ der Riemannschen $\Xi$-Funktion.

### Was dieses Repository nicht ist

Es enthält **keinen Beweis der Riemannschen Hypothese**. Es ist ein offengelegtes
Arbeitsjournal: Jeder Eintrag trägt eine explizite epistemische Statusmarke, negative
Resultate werden gleichrangig dokumentiert, und mehrere zentrale Knoten sind ausdrücklich
offen. Die Dokumente sind **nicht peer-reviewed**.

---

## Die epistemische Methode

Das Programm folgt einer lakatosianischen Disziplin: Ein harter Kern von Konstruktionen
wird durch einen Schutzgürtel aus Tests umgeben, und jede Behauptung erhält eine Marke,
die ihren Sicherungsgrad angibt.

| Marke | Bedeutung |
|---|---|
| `✓ [M]` | Mathematisch gesichert — vollständiger Beweis im Dokument |
| `✓ [K]` | Konstruktiv/typgeprüft — Objekt existiert und ist wohldefiniert, Konsequenzen noch offen |
| `✓ [R]` | Methodisches Resultat oder Reduktionssatz |
| `⚠ [M]` | Konditional gesichert — gilt unter noch offenen Voraussetzungen |
| `✗ [M]` | No-Go: widerlegt oder Obstruktion gesichert |
| `❓ [O]` | Explizit offener Knoten |

Zusätze wie `[M]_part` (teilweise), `[M]_neg` (negativ geschlossen) oder `[K/M]` treten
im Fließtext auf. Offene Knoten tragen eindeutige Bezeichner der Form `[O-219-5e1h]`
und bilden zusammen einen gerichteten azyklischen Abhängigkeitsgraphen (DAG).

**Journalnummerierung.** `NEU-XXX` ist **keine Qualitätsangabe**, sondern eine fortlaufende
Journalnummer. Buchstabensuffixe (`NEU-219u`) bezeichnen Verfeinerungen innerhalb eines
Stranges. Nummern können mehrfach vergeben sein, wenn ein Strang parallel verzweigte —
solche Fälle sind im [Gesamtindex](INDEX.md) sichtbar.

---

## Aufbau des Repositories

| Strang | Umfang | Inhalt |
|---|---|---|
| [00 — Grundlegung](00-grundlegung/README.md) | 19 | Minimalaxiome, Ebenen I–XVI, Spektraltriage, adelische und archimedische Basiskonzepte |
| [01 — Primkanten-Algebra und Werkzeuge](01-primkanten-werkzeuge/README.md) | 57 | NEU-3 – NEU-57: Wodzicki-Residuum, BC-Resolvente, Feshbach-Reduktion, Fourier-Hebung, Nelson-Selbstadjungiertheit |
| [02 — Jacobi-Limes und Divisorgraph](02-jacobi-limes/README.md) | 33 | NEU-58 – NEU-90: Weyl-/Stieltjes-Funktion, Möbius-Feshbach-Identität, Ihara-Reduktion, Schleifeninvarianten |
| [03 — Weil-Form und Nullstellenstatistik](03-weil-form-statistik/README.md) | 31 | NEU-91 – NEU-120: Bochner-Tor, Goldston–Montgomery-Transfer, GUE-Formfaktor, Herglotz-Weil-Brücke |
| [04 — Grenzoperator und Renormierung](04-grenzoperator-renormierung/README.md) | 41 | NEU-121 – NEU-150: Jacobi-Grenzoperator, PSWF-Brücke, Selbstenergie, Mangoldt-Spur, Mellin-Finite-Part |
| [05 — Primkanal und Fourierladung](05-primkanal-fourierladung/README.md) | 33 | NEU-151 – NEU-173: Kanalgewichte, Rohkopplungsquotient, Zeugenroute für $L_3^\circ$, Typfundament |
| [06 — Hochschild-Kohomologie der BC-Algebra](06-hochschild-bc-algebra/README.md) | 78 | NEU-174 – NEU-219z: geladene $HH^4$-Klassen, Zentrumstests, singuläre Derivationen, $\mathcal B^{\log}$, O-219-No-Go |
| [07 — Weil-Explizitformel und Hankelpositivität](07-weil-explizitformel/README.md) | 29 | NEU-220 – NEU-221e: Gammafaktor, Konturtransport, Krein-Raum, Spektraldeterminante, Hankel-Hierarchie |
| [Audits und Methodik](audits/README.md) | 4 | Strangübergreifende Korrekturaudits und Strukturdiagnosen |

Jeder Strangordner enthält eine eigene `README.md` mit vollständiger Dokumenttabelle.

---

## Aktueller Stand (26. Juli 2026)

### Gesicherter Kern

| Resultat | Marke | Eintrag |
|---|---|---|
| Relative Primkanten $\mathcal H_{\mathrm{rel},N}$ strukturell notwendig | `✓ [M]` | NEU-44 |
| Kantendiagonale Hebung $\mathrm{Wres}_{\mathrm{rel}}$, Feshbach-Operator $\mathbb F_N^{\mathrm{rel}}$ | `✓ [M]` | NEU-44 |
| Fourier-Hebungsformel $T_p^{\mathrm{rel}} = \log p$ | `✓ [M]` | NEU-42 |
| Selbstadjungiertheit von $D_{\mathrm{rel}}$ (unter Nelson-Bedingungen) | `⚠ [M]` | NEU-53/54 |
| PSWF-Brücke und Kancellationslemma | `✓ [M]` | NEU-130/131 |
| Welt-2-Entscheidung $\lVert\varepsilon_p\rVert^2 = 1$ | `✓ [M]` | NEU-135D |
| Mangoldt-Spur $\operatorname{Tr}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}) = -\zeta'/\zeta(\beta)$ für $\Re\beta>1$ | `✓ [M]` | NEU-141 |
| Logarithmischer Koeffiziententyp $\mathcal B^{\log}$, $\mathcal A^{\log}$ vollständig konstruiert | `✓ [M]` | NEU-216 |
| Geladener Cup-Aufstieg $L^{\mathrm{cup}}_{g;\mathbf p}\in Z^4(A_{\mathrm{alg}},M)_g$ | `✓ [M]` | NEU-218 |
| Xi-Masterkontur mit exakten Vorzeichen und Polbuchhaltung | `✓ [M]` | NEU-220k |
| Vollständige Hankel-Hierarchie ist RH-äquivalent | `✓ [M]` | NEU-220w |

Zentrale Formeln in kompakter Form:

```
H_rel,N          = ⊕_{p≤N} ⊕_m H_{m→pm}                          (NEU-44)
T_p^rel(e_u0 V_p)= −u0·s0·log(p)·ℓ_{s0,m0}·E_*^rel               (NEU-42 §10)
Σ_rel^ren(β)     = Σ_p p^{−β}/(1−p^{−β})·P_p                      (NEU-136)
Tr(R·Σ_rel^ren)  = −ζ'/ζ(β),  Re β > 1                            (NEU-141)
|c_p|²           = O((log p)² / p)                                (NEU-135D)
R_p              = log(p)/|c_p|² ≳ p/log(p)   [unbeschränkt]      (NEU-141)
μ_k              = −(k+1)/(2k+2)!·(log Ξ)^(2k+2)(0)               (NEU-220w)
```

### Gesicherte No-Go-Resultate

Negative Strukturresultate sind hier gleichwertige Ergebnisse — sie schließen Routen
dauerhaft und lokalisieren das Hindernis.

| No-Go | Eintrag |
|---|---|
| `X = m_arith` ist kategorial falsch; $m_{\mathrm{arith}} = \Pi_\gamma(X)$ ist nur der Spektralschatten | NEU-114/115 |
| Direkt-Summen-Obstruktion für den kollektiven Birman–Schwinger-Operator | NEU-50 |
| Dichte-No-Go für kanalabhängige Kopplung | NEU-82 |
| $Z(A_{\mathbb Q})_g = 0$ für $g\neq 1_\Gamma$ — reguläre geladene Nullkozykelroute ausgeschlossen | NEU-182/183 |
| $Z^0(A, {}_{\mathrm{id}}A_{\sigma_\beta}) = 0$ für $\Re\beta>0$ — verdrehte Nullkozykelroute ausgeschlossen | NEU-183 |
| Globaler Bimodul-No-Go via Zentralisatorbeweis | NEU-215 |
| **O-219-NoGo:** kanonischer Basislift $\tilde L_0$ ist typkorrekter Kozykel, aber $t\Phi_0 = g^{-\beta}\Phi_0 \neq \Phi_0$ — keine gewöhnliche zyklische Klasse in $HC^4$ | NEU-219u |
| Off-Axis-Trägheit: Positivitäts-No-Go und Similarity-No-Go im Nullstellenpaar-Kreinraum | NEU-220t |
| Gewöhnliche Spurklassen-Determinante für $\Xi$ ausgeschlossen | NEU-220u |

Das O-219-No-Go ist das strukturell schärfste Resultat des Programms: Es zeigt, dass die
Zyklizitätsobstruktion **eingabeunabhängig** im Faktor $g^{-\beta}$ sitzt und aus der
Spektraleigenschaft von $U_{g^{-1}}$ im KMS-Zustand folgt. Eine positive Reparatur
erfordert zwingend eine andere Koeffizientenkategorie (parazyklisch, $\sigma$-zyklisch
oder getwistet-zyklisch) oder einen echten Orbitshift $\kappa \neq 0$.

### Aktive Front

| Strang | Engpass | Status |
|---|---|---|
| **Weil-Momentquelle** (primär) | Hebungsabstieg: gilt $\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}$? Normgleichheit genügt nicht — verlangt ist Invarianz des zyklischen Spektralmaßes | `❓ [O]` NEU-221e, `[O-221-1c1a0]` |
| **Zyklisches Tripel** | $\lVert\Psi_N\rVert$, Nullmodusfreiheit, inverse Momente $k=0,1,2$ | `❓ [O]` NEU-221d, `[O-221-1c1b/c]` |
| **Adelische Quellkonstruktion** | Positive Momentfolge $(\mu_k)$ aus einer adelischen Quelle konstruieren (RH-stark) | `❓ [O]` NEU-220w |
| **Fourierladung $L_3^\circ$** | Explizites $\ell_{s_0,m_0}\neq 0$ konstruieren | `❓ [O]` NEU-161/162 |
| **Regulierte Spur im kritischen Streifen** | $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}})$ für $0<\Re\beta\le 1$ | `❓ [O]` NEU-141.D |
| **Singulärwert-Wachstum $J^-$** | $s_k(J^-\vert_{H^{\mathrm{eff}}_{\mathrm{rel}}})$ divergent oder akkumulierend? | `❓ [O]` NEU-57 |
| **Schur-Test exakt** | Nelson-Bedingung 1 exakt statt heuristisch | `❓ [O]` NEU-55 |
| **Rückrichtung RH** | $\operatorname{Spec}\subset\mathbb R \Rightarrow \mathrm{RH}$ | `❓ [O]` |

Vollständige Liste mit Verzweigungsbedingungen: [OFFENE_PROBLEME.md](OFFENE_PROBLEME.md).

---

## Lesepfade

**Erster Überblick (ca. 30 Minuten)**
[Minimalaxiome](00-grundlegung/objekt_x_minimalaxiome.md) → [Ebene XVI: Objekt X](00-grundlegung/ebene-XVI-objekt-x.md) → [Statusregister](STATUS.md) → [Offene Probleme](OFFENE_PROBLEME.md)

**Der analytische Hauptpfad**
NEU-44 (Primkanten) → NEU-42 (Fourier-Hebung) → NEU-63 (Weyl-Funktion) → NEU-136 (Selbstenergie) → NEU-141 (Mangoldt-Spur) → NEU-220k (Xi-Masterkontur) → NEU-220w (Hankel-Kriterium)

**Der kohomologische Pfad**
NEU-174 (Hochschild-Komplex) → NEU-176 (geladene $HH^4$-Klasse) → NEU-195 (Bewertungsderivationen) → NEU-216 ($\mathcal B^{\log}$) → NEU-218 (Cup-Aufstieg) → NEU-219u (No-Go)

**Wer nur die harten Ergebnisse sucht**
[STATUS.md](STATUS.md) listet gesicherte Sätze, No-Gos und konditionale Resultate ohne Zwischenschritte.

**Wer am Programm mitarbeiten will**
[EINSTIEGSPROMPT.md](EINSTIEGSPROMPT.md) fasst den vollständigen Arbeitskontext auf Stand NEU-221e
zusammen — Architektur, geschlossene Routen, aktuelle Sperren, Arbeitsregeln und den nächsten
konkreten Knoten. Gedacht als Einstiegstext für eine neue Arbeits- oder KI-Sitzung.

---

## Verwandte Repositories

| Repository | Inhalt |
|---|---|
| [riemann-hypothese-katalog](https://github.com/Waschtl904/riemann-hypothese-katalog) | Frühere Katalogfassung: BC-System, Koszul, HH-Kohomologie |
| [rh-maieutic-program](https://github.com/Waschtl904/rh-maieutic-program) | Maieutisches Forschungsprogramm — sokratische Herleitungsketten |
| [Riemann](https://github.com/Waschtl904/Riemann) | Numerische Experimente mit der Zetafunktion (Python) |
| [prolate-primes-paper](https://github.com/Waschtl904/prolate-primes-paper) | Koerzivität der prolaten Gram-Form auf Primzahl-Stützpunkten (TeX) |
| [pswf-coercivity-programme](https://github.com/Waschtl904/pswf-coercivity-programme) | Uniforme Koerzivität an Airy-reskalierten Primzahlen |
| [arith-spectral-bridge](https://github.com/Waschtl904/arith-spectral-bridge) | Modulare Arithmetik ↔ Spektraloperatoren (Jupyter) |
| [prime-quasicrystal-diffraction](https://github.com/Waschtl904/prime-quasicrystal-diffraction) | Beugungsspektren arithmetischer Punktmengen |

---

## Herkunft, Mitwirkung, Lizenz

Dieses Repository ist die **kuratierte öffentliche Fassung** eines privaten
Forschungsjournals. Die Dokumentinhalte sind unverändert übernommen; neu sind die
thematische Ordnung, die Navigationsebene und die vereinheitlichten Dateinamen.
Details zur Migration: [MITWIRKEN.md](MITWIRKEN.md).

Korrekturen, Gegenbeispiele und Verschärfungen sind ausdrücklich willkommen — negative
Befunde sind in diesem Programm gleichwertige Beiträge. Bitte über Issues.

Lizenz: [CC BY 4.0](LICENSE) · Zitierangaben: [CITATION.cff](CITATION.cff)
