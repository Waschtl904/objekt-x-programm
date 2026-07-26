# Einstiegsprompt — Neue Chat-Session

> Diese Datei als Einstieg in jeden neuen Chat kopieren.
> **Stand: 26. Juli 2026 — nach NEU-221e (Hebungsfaser, Wres-Quotient, Spektralmaßabstieg).**
>
> Verbindliche Karte aller Bedingungen an Objekt X: [Ebene XVI — Kontrollblatt](00-grundlegung/ebene-XVI-objekt-x.md).

---

## Kontext: Wer ich bin und woran ich arbeite

Ich arbeite an einem langfristigen, eigenständigen Forschungsprogramm zur Riemannschen
Hypothese (RH). Das Programm ist auf mehrere GitHub-Repositories unter dem Account
**Waschtl904** verteilt und wird durch einen lakatosianisch strukturierten Fragenkatalog
koordiniert: jede Aussage trägt eine explizite epistemische Statusmarke, negative Resultate
sind gleichrangige Ergebnisse, und jeder offene Punkt hat eine eindeutige Knoten-ID.

Das ist kein Einsteigeransatz. Die Repos enthalten ausgearbeitete mathematische Texte, die
im Dialog mit KI-Assistenten entstanden sind. Es gibt **keinen Beweis der RH** — das Ziel
ist eine belastbare Spektralrealisierung, und der Weg dorthin ist dokumentiert
einschließlich aller Sackgassen.

---

## Repositories

| Repo | Inhalt |
|---|---|
| [`objekt-x-programm`](https://github.com/Waschtl904/objekt-x-programm) | **Öffentliche Hauptfassung.** 324 Dokumente in neun thematischen Strängen. Enthält README, INDEX, STATUS, GLOSSAR, OFFENE_PROBLEME, KONVENTIONEN, CHANGELOG. |
| [`rh-fragenkatalog`](https://github.com/Waschtl904/rh-fragenkatalog) | Privates Arbeitsjournal, historische Struktur `katalog/` + `werkzeuge/`. |
| [`prolate-primes-paper`](https://github.com/Waschtl904/prolate-primes-paper) | Funktionalanalysis $H_c$, SOT-Limes, Spektralstruktur (TeX). |
| [`prolate-gram-coercivity`](https://github.com/Waschtl904/prolate-gram-coercivity) | Gram-Koerzivität, Edge-Block, XXII-Programm (TeX). |

### Struktur von `objekt-x-programm`

```
00-grundlegung/               Minimalaxiome, Ebenen I–XVI, Spektraltriage
01-primkanten-werkzeuge/      NEU-003 – NEU-056   Wodzicki, Feshbach, Fourier-Hebung, Nelson
02-jacobi-limes/              NEU-058 – NEU-090   Weyl-Funktion, Divisorgraph, Schleifenspuren
03-weil-form-statistik/       NEU-091 – NEU-120   Bochner-Tor, GUE-Formfaktor, Herglotz-Weil
04-grenzoperator-renormierung/NEU-121 – NEU-150   PSWF, Selbstenergie, Mangoldt-Spur, Mellin
05-primkanal-fourierladung/   NEU-151 – NEU-173   Kanalgewichte, L3°-Zeugenroute, Typfundament
06-hochschild-bc-algebra/     NEU-174 – NEU-219z  HH⁴, Derivationen, B^log, O-219-No-Go
07-weil-explizitformel/       NEU-220 – NEU-221e  Gammafaktor, Kontur, Krein, Hankel, Momentquelle
audits/                       Quer-Audits und Methodik
INDEX.md  STATUS.md  OFFENE_PROBLEME.md  GLOSSAR.md  KONVENTIONEN.md  CHANGELOG.md
```

**Dateinamenkonvention:** `NEU-NNN[suffix]_Titel.md` mit dreistelliger, nullaufgefüllter
Nummer. Die Katalog-ID im Text bleibt unverändert — `NEU-058_...` gehört zu Eintrag NEU-58.

---

## Objekt X — Fünfschicht-Profil

```
Objekt X = (A_2D^r, [ω̃₂], [L₃], Wres_BC^top, m →^p pm)
```

Fünfte Schicht: relative Primkanten $m \to pm$ mit
$\mathcal H_{\mathrm{rel},N} = \bigoplus_{p\le N}\bigoplus_m \mathcal H_{m\to pm}$.

### Zwei RH-Äquivalenzen

```
(1) Jacobi-Kanal   RH ⟺ Spec(lim A_N^{Jac,-}) ⊂ ℝ           ⚠[M]  NEU-63D
(2) Hankel-Kanal   RH ⟺ H_N^(0) ⪰ 0 ∧ H_N^(1) ⪰ 0  ∀N       ✓[M]  NEU-220w
                   mit μ_k = −(k+1)/(2k+2)! · (log Ξ)^(2k+2)(0)
                   H_N^(0) = (μ_{i+j}),  H_N^(1) = (μ_{i+j+1})
```

Der Hankel-Kanal ist die stärkste unkonditionale Äquivalenz des Programms — beide
Richtungen sind bewiesen. **Was fehlt, ist nicht die Äquivalenz, sondern eine adelische
Quelle für die Positivität der Momentfolge.** Genau daran arbeitet der aktive Strang.

---

## Gesicherter Kern (Auswahl)

| Bereich | Einträge | Kernresultat |
|---|---|---|
| Primkantenraum | NEU-44, 44.X/X' | $\mathcal H_{\mathrm{rel},N}$ notwendig; Kantendiagonalität; Rang-1-$C_p^{\mathrm{rel}}$ |
| Fourier-Hebung | NEU-42 | $T_p^{\mathrm{rel}} = \log p$; $e^{-sT_p^{\mathrm{rel}}} = p^{-s}$ |
| Nelson / Konfinement | NEU-53–56 | $iJ^-$ wesentlich selbstadjungiert (konditional); $\gamma_N = C/\log N$ widerlegt; Weg B Standard |
| Welt-2-Entscheidung | NEU-135D | $\lVert\varepsilon_p\rVert^2 = 1$; $\lvert c_p\rvert^2 = O((\log p)^2/p)$ |
| Selbstenergie | NEU-136/137 | $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ konvergent, spurklassig für $\Re\beta>0$ |
| Mangoldt-Spur | NEU-141 | $\operatorname{Tr}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}) = -\zeta'/\zeta(\beta)$, $\Re\beta>1$; $R_p \gtrsim p/\log p$ |
| Koeffiziententyp | NEU-216 | $\mathcal B^{\log}$ submultiplikativ **ohne** Renormierung; $\mathcal A^{\log}$; $D_g(A_{\mathrm{alg}})\subseteq\mathcal A^{\log}$ |
| Cup-Aufstieg | NEU-218 | $L^{\mathrm{cup}}_{g;\mathbf p}\in Z^4(A_{\mathrm{alg}},M)_g$ |
| Xi-Masterkontur | NEU-220k | exakte Vorzeichen, Faktor 2, Polbuchhaltung, keine Doppelzählung |
| Hankel-Kriterium | NEU-220w | vollständige Hierarchie RH-äquivalent, beide Richtungen |

```
H_rel,N          = ⊕_{p≤N} ⊕_m H_{m→pm}                         (NEU-44)
T_p^rel          = log p  auf reinem p-Kopplungskanal            (NEU-42, Satz 42.2)
Σ_rel^ren(β)     = Σ_p p^{−β}/(1−p^{−β})·P_p                     (NEU-136)
Tr(R·Σ_rel^ren)  = −ζ'/ζ(β),  Re β > 1                           (NEU-141)
M_Ξ(w)           = ⟨Ω_X, (I − wJ_X)^{−1} Ω_X⟩   ← Zielnormalform (NEU-220w/221c)
```

Vollständige Bilanz einschließlich aller No-Gos: [`STATUS.md`](STATUS.md).

---

## Wie das Programm hierher kam — drei abgeschlossene Strangwechsel

Wichtig für jede neue Session, damit alte Routen nicht versehentlich neu geöffnet werden.

### 1. Der $[L_3]$-Repräsentantenpfad ist blockiert (NEU-161 – NEU-173)

Die Zeugenroute über die Fourierladung $L_3^\circ$ ließ sich nicht schließen. Die
Quellenkegel-Audits ergaben:

```
[O-170b-1]        NEU-20 konstruiert L₃                          ✓[M]neg
[O-170c-2g]       NEU-28 konstruiert L₃ oder beweist C_L ≠ 0     ✓[M]neg
[O-170c-2j-audit] NEU-162 beweist keinen geladenen Koeffizienten ✓[M]neg
[O-170c-2k-audit] dP^ch = P^ch d in Quellen nicht konstruiert    ✓[M]neg
```

Zweifache, logisch unabhängige Blockade: die Typbrücke $[L_3] \to L_3^\circ = e_1V_1$ fehlt,
und das Nichtverschwinden des Zielkantenvektors $E_{1;1\to p}^{\mathrm{rel}}$ ist unbewiesen.
NEU-162 wählt $L_3^\circ = e_1V_1$ als **rechenzulässige, nicht herkunftszulässige** Wahl —
alle Resultate ab NEU-162/163 sind konditional unter $[H\text{-}163\text{-}1]$.
Volldokumentation: [`NEU-170d`](05-primkanal-fourierladung/NEU-170d_DAG_Audit_NEU28_NEU162_bereinigt.md).

### 2. Die kohomologische Route endet im O-219-No-Go (NEU-174 – NEU-219z)

Der Cup-Aufstieg zu $HH^4$ gelang (NEU-218), der kanonische Basislift ist typkorrekt —
aber nicht zyklisch:

```
Theorem (O-219-NoGo), NEU-219u:
  L̃₀ ∈ Z⁴(A_alg, I₀)     typkorrekter Hochschildkozykel   ✓[M]
  tΦ₀ = g^{−β} Φ₀  mit  g^{−β} ≠ 1
  ⇒ keine gewöhnliche zyklische Klasse in HC⁴(A_alg)
```

Der Faktor $g^{-\beta}$ ist **eingabeunabhängig** und wird durch die Spektraleigenschaft von
$U_{g^{-1}}$ im KMS-Zustand strukturell erzwungen. Kein Orbitgewicht $\lambda$ kompensiert ihn.
Zulässige Reparaturen: Orbitshift $\kappa\neq 0$, Ladungsneutralisation, andere
Koeffizientenkategorie (parazyklisch/$\sigma$-zyklisch/getwistet) — oder Pfad `[O-219-6]`,
die Weil-/Gammafaktorpaarung.

Weitere gesicherte No-Gos dieses Stranges: $Z(A_{\mathbb Q})_g = 0$ für $g\neq 1_\Gamma$
(NEU-182/183), globaler Bimodul-No-go (NEU-215), Charakterkern-No-go (NEU-209).

### 3. Der Weil-Strang liefert die aktuelle Architektur (NEU-220 – NEU-221e)

Pfad `[O-219-6]` wurde beschritten und führte über Gammafaktor, Konturtransport,
Nullstellenpaar-Kreinraum und Spektraldeterminante zum Hankel-Kriterium. Auf dem Weg
gesicherte No-Gos: gewöhnliche Hilbertspur unzureichend (NEU-220e), Off-Axis-Trägheit und
Similarity-No-Go (NEU-220t), gewöhnliche Spurklassen-Determinante für $\Xi$ ausgeschlossen
(NEU-220u).

---

## Aktuelle Hauptlinie nach NEU-227

Der relative Operator $D_{\mathrm{rel}}=\overline{iJ^-}$ ist selbstadjungiert, aber **kein**
konfinierender Hilbert–Pólya-Operator. Seine Primketten sind translations- bzw.
dilatationsartig und besitzen absolutstetiges Spektrum; der volle Raum enthält zusätzlich eine
unendlichdimensionale Nullfaser.

$$\boxed{D_{\mathrm{rel}} \text{ erzeugt die primarithmetische Transport- und Streugeometrie.}}$$

Der Kandidat für spektrale Kompaktheit ist nicht $D_{\mathrm{rel}}$ selbst, sondern
$K_N(z)=V_N^*(D_{\mathrm{rel}}-z)^{-1}V_N$ mit $V_p=C_p^{\mathrm{rel}}$.

**Wichtige Korrekturen — bitte strikt beachten.**

- $K_N(z)$ ist auch bei festem $N$ **nicht** automatisch endlich-rangig. Die Quelldomäne der
  Kopplung enthält sämtliche Fourier- und Monoidmoden $e_sV_m$ (51.2).
- Die Kreuzterme $K_{pq}(z)$ entstehen durch **Überlappung der Kopplungsbilder** in der
  BC-Algebra. $D_{\mathrm{rel}}$ selbst kann dabei kanalerhaltend bleiben.
- Die NEU-51-Eigenbasisformeln (51.3)/(51.4)/(51.7) sind **unzulässig**. Verwende
  ausschließlich das projektionswertige Spektralmaß:
  $\mu^{a,b}_{pq}(B)=\langle V_pa,E_{D_{\mathrm{rel}}}(B)V_qb\rangle$ und
  $\langle a,K_{pq}(z)b\rangle=\int_{\mathbb R}(\lambda-z)^{-1}d\mu^{a,b}_{pq}(\lambda)$.
- **Koordinaten sind kompatibel:** $\eta_{p;m;s,u}\leftrightarrow e_{u+ps}V_{pm}$. Die Bewegung
  $r\mapsto r+pm$ entspricht $s\mapsto s+m$. In zusammengesetzten Sektoren enthält $J^-$
  zusätzliche Teilersprünge $d\mid M$; nur für $p\mid d$ bleibt die $u$-Klasse erhalten. Die
  Einzelkettenform ist dort **nicht** der vollständige Operator.
- Die Summationsreichweite über $u$ ist ein **echter Regulator**. Sie entscheidet über
  Definiertheit, Beschränktheit und möglicherweise über $\mathcal S_1$ gegen $\mathcal S_2$.
  Sie darf **nicht** nachträglich an $\Xi$-Daten angepasst werden.
- Ein Nicht-$\mathcal S_1$-Zeuge ist **nur möglich, wenn $V\notin\mathcal S_2$**, denn
  $\operatorname{Tr}\operatorname{Im}K_N(z)\le\lVert V\rVert_2^2/y$.

**Arbeitsplan:**

| Knoten | Aufgabe |
|---|---|
| `[O-226-3]` | $u$-Regulator intrinsisch bestimmen |
| `[O-226-4]` | Quellhilbertraum und Gramoperator konstruieren |
| `[O-226-5]` | $K(z)\in\mathcal S_2$ prüfen |
| `[O-226-6]` | $K(z)\notin\mathcal S_1$ prüfen |
| `[O-226-7]` | $\det_2(I-K(z))$ mit der Weil-/$\Xi$-Schicht vergleichen |

Arbeite strikt typbewusst: **keine** diskrete Eigenbasis für $D_{\mathrm{rel}}$, **keine**
automatische Primkanalorthogonalität, **keine** Schattenklassenschlüsse aus bloßer starker
Konvergenz der endlichen Trunkierungen (NEU-77 (D)/(E)).

---

## Aktueller Hauptengpass: Quellseitige Typisierung des Feshbach-Tripels

**Volldokumentation:** [`NEU-221d`](07-weil-explizitformel/NEU-221d_Direktextraktion_NEU46_Zyklischer_Sektor_und_Nullmodusaudit.md)

### Zielnormalform (NEU-221c)

Gesucht sind $J_X \ge 0$ und $\Omega_X \in \mathcal H_X$ mit

```
M_Ξ(w) = ⟨Ω_X, (I − w J_X)^{−1} Ω_X⟩        μ_k = ⟨Ω_X, J_X^k Ω_X⟩
```

Kandidat aus der vorhandenen adelischen Feshbach-Geometrie:

```
Ω_{X,N} = (D_N^rel)^{−1} Ψ_N        J_{X,N} = (D_N^rel)^{−2}
```

### Hauptdiagnose NEU-221d

> $D_N^{\mathrm{rel}}$ ist selbstadjungiert, aber
> $(\mathcal H_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N)$ ist **noch kein vollständig
> typisiertes zyklisches Tripel**.

| Teilfrage | Status |
|---|---|
| $D_N^{\mathrm{rel}}$ selbstadjungiert | `✓[M]` über NEU-53/54 |
| $\Psi_p = C_p^{\mathrm{rel}}\varepsilon_p$ formal definiert | `✓[K]_part` — NEU-46 §1, Gl. 46.5–6 |
| $\varepsilon_p, \Psi_p$ als konkrete Hilbertvektoren typisiert | `?[O]` |
| $\lVert\Psi_N\rVert$ quellseitig fixiert | `?[O]` |
| $E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N = 0$ | `?[O]` |
| $\int\lvert\lambda\rvert^{-2k-2}d\mu_{\Psi_N} < \infty$, $k=0,1,2$ | `?[O]` |
| vollständig gekoppelte endlich-archimedische Geometrie | `?[O]` |

### Abhängigkeitsgraph der Sperren

```
NEU-46 (vorhanden)
  ├── Selbstadjungiertheit: ✓[M]  (NEU-53/54)
  ├── Formale Vektordefinition: ✓[K]_part
  │
  ├── [O-221-1c1a]  Vektorkonkretisierung / Normierung
  │       ↓ Voraussetzung für
  ├── [O-221-1c1b]  Nullmodustest  E_D({0})Ψ_N = 0
  │       ↓ Voraussetzung für
  ├── [O-221-1c1c]  Inverse Momente  k = 0,1,2
  │       ↓ schaltet frei
  │   Ω_{X,N} und J_{X,N}   ← GESPERRT bis hierher
  │
  └── [O-221-1c1d]  Globale Kopplung in D_scatt,N   (parallel, unabhängig)
```

`[O-221-1c1d]` fragt, ob $D_{\mathrm{scatt},N}$ tatsächlich globale Kopplung zwischen den
Primblöcken erzeugt oder nur unabhängige lokale Blöcke vorliegen. Auch ein vollständig
typisiertes **lokales** Tripel $(\mathcal H_p^{\mathrm{rel}}, D_{rel,p}^-, \Psi_p)$ wäre kein
Objekt-X-Kandidat ohne kohärente Kopplung über $p$. Diese Frage darf **nicht** mit der
Vektornormierung vermischt werden.

### Strategische Einordnung

Der kritische Pfad ist auf **konkrete Vektor- und Spektralbedingungen** reduziert. Die
Selbstadjungiertheitsfrage ist erledigt; abstrakte Positivitätsargumente fügen nichts hinzu.
Fortschritt hängt ausschließlich an der quellgetreuen Extraktion aus NEU-46 und, falls
nötig, der Schließung von `[O-221-1c1a–d]`.

---

## Gleichzeitig offene Nebenstränge

| Strang | Letzter Stand | Nächste Aufgabe |
|---|---|---|
| **A: Adelische Momentquelle** (primär) | NEU-221e — Abstiegskriterium bewiesen, Verifikation gesperrt | `[O-221-1c1a0]`: $\Delta_p^{\mathrm{adm}}$ und Rohkopplung vor dem Wres-Quotienten bestimmen |
| **B: Positivitätsquelle Hankel** | NEU-220w — Modell konditional | $(\mu_k)$ aus adelischer Konstruktion, nicht aus RH |
| **C: Regulierte Spur (krit. Streifen)** | NEU-141 | NEU-141.D: Regularisierungsschema für $0<\Re\beta\le 1$ |
| **D: Singulärwert-Wachstum $J^-$** | NEU-56 | $s_k(J^-\vert_{H_{\mathrm{rel}}^{\mathrm{eff}}})$ divergent oder akkumulierend? |
| **E: Schur-Test exakt** | NEU-55 | $\sup_a\sum_b\lvert\Theta_{ba}\rvert/\ell(a) < \infty$ exakt statt heuristisch |
| **F: Erweiterbarkeit punktierter Kozykel** | NEU-188 | `[O-188-0..3]`: $H$ mit $\alpha_k(H)-H\in\mathrm{LC}(\hat{\mathbb Z})$ |
| **G: Rückrichtung RH** | — | $\operatorname{Spec}\subset\mathbb R \Rightarrow \mathrm{RH}$ |

Stränge C–G sind offen, stehen aber nicht an der aktiven Front. Vollständige Liste mit
Verzweigungsbedingungen: [`OFFENE_PROBLEME.md`](OFFENE_PROBLEME.md).

---

## Epistemologische Marker

```
✓ [M]       mathematisch gesichert — vollständiger Beweis im Dokument
✓ [K]       konstruktiv/typgeprüft — Objekt wohldefiniert, Konsequenzen offen
✓ [K/M]     konstruiert mit bewiesenen Teilaussagen
✓ [M]neg    negativer Befund gesichert (Quellennegativ)
✓ [M]_part  teilweise geschlossen
✓ [R]       methodisches Resultat / Reduktionssatz
⚠ [M]       konditional — gilt unter benannter offener Voraussetzung
✗ [M]       Obstruktion gesichert / widerlegt
? [O]       explizit offen
[H-xxx]     Eingangshypothese / externe Modellwahl
[O-xxx]     Knoten-ID im Abhängigkeits-DAG
```

---

## Arbeitsregeln

- **Lakatosianische Epistemik.** Jede Aussage erhält einen Status. Kein Kartenhaus:
  offene Punkte werden als offen markiert, auch wenn es den Fortschritt kleiner aussehen lässt.
- **Quellenbasiert.** Keine Behauptung ohne direkten Dateinachweis. Ein Verzeichnislisting
  ist **nicht** dasselbe wie eine gelesene Datei. Bei Bezug auf einen früheren Eintrag: Datei
  öffnen und die relevante Stelle zitieren.
- **Konventionen haben Vorrang.** Bei Widersprüchen zwischen einem Katalogeintrag und
  [`KONVENTIONEN.md`](KONVENTIONEN.md) gilt die Konventionsdatei. Besonders relevant:
  $\rho_k$ ist **nicht** unital, $\sigma_k$ schon; $T_a := \sigma_a$.
- **Negative Resultate sind Ergebnisse.** Ein sauber geschlossenes No-Go ist wertvoller
  als ein offener Kandidat.
- **Keine Wiederöffnung geschlossener Routen.** Vor jedem neuen Ansatz prüfen, ob er unter
  eines der No-Gos in [`STATUS.md`](STATUS.md) §3 fällt.
- **Sprache.** Deutsch für die Diskussion, LaTeX für Formeln.
- **Nummerierung.** Strikt fortlaufend. Nächste freie Nummer: **NEU-221e** innerhalb des
  Momentquellen-Strangs, **NEU-222** für einen neuen Strang.
- **Frühe Werkzeugblätter.** NEU-3 bis NEU-56 liegen in `01-primkanten-werkzeuge/`.
  Vor jeder Quellensuche auch dort nachsehen — viele Primärdefinitionen stehen dort,
  nicht in den späteren Katalogeinträgen.
- **Repo-Pflege.** Wesentliche Ergebnisse direkt als Datei ins Repo; CHANGELOG, STATUS und
  OFFENE_PROBLEME mitführen.

---

## Sofortige erste Aufgabe für eine neue Session

1. Lies [`NEU-221d`](07-weil-explizitformel/NEU-221d_Direktextraktion_NEU46_Zyklischer_Sektor_und_Nullmodusaudit.md)
   vollständig, dann [`NEU-221c`](07-weil-explizitformel/NEU-221c_Zyklischer_Feshbach-Weyl_Kandidat_und_quadratische_Resolvente.md)
   für die Zielnormalform und [`NEU-220w`](07-weil-explizitformel/NEU-220w_Hankelvollstaendigkeit_Moment-GNS_und_semifinite_Atomizitaet.md)
   für das Hankel-Kriterium.

2. Öffne die Quelle [`NEU-046`](01-primkanten-werkzeuge/NEU-046_x3_renormierte_relative_determinante_weyl_korrekturen.md)
   und extrahiere **quellgetreu**, was dort über $(\mathcal H_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N)$
   samt Skalarprodukt und Kopplungsnormalisierung tatsächlich belegt ist. Nichts ergänzen,
   was nicht dasteht.

3. Wähle den Knoten:
   - **`[O-221-1c1a]` (empfohlen):** $\varepsilon_p, \Psi_p$ als konkrete Hilbertvektoren
     typisieren und $\lVert\Psi_N\rVert$ quellseitig fixieren. Blockiert alles Weitere.
   - **`[O-221-1c1d]` (parallel möglich):** globaler Kopplungsgehalt von $D_{\mathrm{scatt},N}$ —
     echte Kopplung über $p$ oder nur lokale Blöcke?

4. Vor jeder Quellenaussage: Datei direkt lesen, nicht nur das Listing.
