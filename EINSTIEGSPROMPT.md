# Einstiegsprompt — Neue Chat-Session

> **Aktueller Stand: 30. August 2026.**
> Für eine neue Session soll **nur der folgende aktuelle Einstieg** als operative Arbeitsgrundlage verwendet werden.
> Der frühere NEU-250a/Wres-Prompt bleibt darunter ausschließlich als historische Provenienz erhalten.

## Aktueller Einstieg — kopierbarer Arbeitskontext

Ich arbeite am Forschungsprogramm **Objekt X** zur Riemannschen Hypothese im Repository
`Waschtl904/objekt-x-programm`. Arbeite als strenger mathematischer Auditor und
Research Assistant. Prüfe bei jeder neuen Aufgabe zuerst den aktuellen `main`-Stand und
verwende aktive mathematische Quellen vor älteren Navigationsdokumenten.

### Kanonische operative Quellen

1. `CURRENT-FRONT.md` — aktuelle Forschungsfront und nächster Schritt.
2. `00-uebersicht/ACTIVE_THEOREM_REGISTRY.md` — Status, Scope, Provenienz.
3. `00-uebersicht/P11_R32_STATUS_2026-08-25.md` — Post-Freeze-Statusaddendum, Update 2026-08-30.
4. `00-uebersicht/FORSCHUNGS_ROADMAP_2026-08-26.md` — strategische Roadmap.
5. `00-uebersicht/OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md` — Definition von Objekt X.

### Aktueller mathematischer Stand

- PR #34 ist nach `main` gemergt; mathematische Merge-Basis:
  `6ac0141b2de3a0b2af98fff6d11c403fe3b379b6`.
- C1B2A-CHIRO: `✓[M]` plus reproduzierbares Certificate.
- C1B2A-TRANSFER: `✓[M]`.
- M1-RAW und M1-FULL(7/2): kanonische reproduzierbare Certificate-Ergebnisse.
- Daraus folgt M1-FULL((r)) für jedes (3<r<4) auf offenen Parameterkammern und offenen Kreisatomen.
- Die CI-geprüften Byte-Provenienzen bleiben die Script-Blobs
  `b92f7778...` (AFF-CHIRO), `18f992d1...` (GATE1R) und
  `d73993a3...` (M1-FULL), GitHub Actions Run `33328052407`.
- Daraus folgt **keine** Cross-Gram-Injektivität, kein HT-RED, kein Objekt-X-Abschluss und keine RH-Aussage.

### Aktive Frage

[
\boxed{\ker\Gamma_I=\{0\}\ ?[O]}
]

bzw. die äquivalente Preimage-/augmentierte-System-Form auf SW1.

### Nächste Arbeitsfolge aus Roadmap A

1. Odd/even-Faltung exakt festlegen.
2. Hub-Shifts (a,b,T) einsetzen.
3. Rest-Martingaleblöcke einsetzen.
4. Alle elf (K^*M_\Omega K)-Wörter nach Cutoff-Wänden zerlegen.
5. A0 vollständig prüfen, inklusive Schwanz- und Randklassen.
6. Rohsystem auf dem ersten globalen P12-Stratum aufbauen.
7. Invertierbare Rohmatrix oder exakten Gegenvektor suchen.
8. Erst danach über Promotion oder No-Go entscheiden.

Statusmarker strikt verwenden: `✓[M]`, `✓[K/M]`, `✓[M]_part`,
`✓[M]_neg`, `×[M]`, `?[O]`. Keine stärkere Aussage buchen als durch
Beweis/Certificate und exakte Provenienz gedeckt.

---

## Historischer Alt-Prompt — nicht als aktuelle Front verwenden

> **Historischer Stand:** 6. August 2026 — nach NEU-250a / Ausgang B / damaliger nächster Knoten [O-221-1c1a0-C].
> Die folgenden Abschnitte bleiben nur als Forschungsprovenienz erhalten.

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
| [`objekt-x-programm`](https://github.com/Waschtl904/objekt-x-programm) | **Öffentliche Hauptfassung.** Primäres aktives Repo. Enthält README, INDEX, STATUS, GLOSSAR, OFFENE_PROBLEME, KONVENTIONEN, CHANGELOG, **KARTE.md** (Großschreibung!). |
| [`rh-fragenkatalog`](https://github.com/Waschtl904/rh-fragenkatalog) | Privates Archivrepo (älter, nicht mehr aktiv). |
| [`prolate-primes-paper`](https://github.com/Waschtl904/prolate-primes-paper) | Funktionalanalysis $H_c$, SOT-Limes, Spektralstruktur (TeX). |
| [`prolate-gram-coercivity`](https://github.com/Waschtl904/prolate-gram-coercivity) | Gram-Koerzivität, Edge-Block, XXII-Programm (TeX). |

### Struktur von `objekt-x-programm`

```
00-grundlegung/               Minimalaxiome, Ebenen I–XVI, Spektraltriage
01-primkanten-werkzeuge/      NEU-003 – NEU-056, NEU-223 – NEU-249   Wodzicki, Feshbach, Fourier-Hebung, Nelson, Dirichletresiduumsform
02-jacobi-limes/              NEU-058 – NEU-090   Weyl-Funktion, Divisorgraph, Schleifenspuren
03-weil-form-statistik/       NEU-091 – NEU-120   Bochner-Tor, GUE-Formfaktor, Herglotz-Weil
04-grenzoperator-renormierung/NEU-121 – NEU-150   PSWF, Selbstenergie, Mangoldt-Spur, Mellin
05-primkanal-fourierladung/   NEU-151 – NEU-173   Kanalgewichte, L3°-Zeugenroute, Typfundament
06-hochschild-bc-algebra/     NEU-174 – NEU-222   HH⁴, Derivationen, B^log, O-219-No-Go
07-weil-explizitformel/       NEU-220 – NEU-250a  Gammafaktor, Kontur, Krein, Hankel, Momentquelle, Wres-Typaudit
audits/                       Quer-Audits und Methodik
INDEX.md  STATUS.md  OFFENE_PROBLEME.md  GLOSSAR.md  KONVENTIONEN.md  CHANGELOG.md  KARTE.md
```

**Dateinamenkonvention:** `NEU-NNN[suffix]_Titel.md` mit dreistelliger, nullaufgefüllter
Nummer. Die Katalog-ID im Text bleibt unverändert.

**Wichtige Korrekturen gegenüber früheren Sessions:**
- Das primäre aktive Repo ist **`objekt-x-programm`**, nicht `rh-fragenkatalog`.
- Die Karte heißt **`KARTE.md`** (Großschreibung) im Root des Repos.
- Höchste vergebene Nummer: **NEU-250a** (in `07-weil-explizitformel/`).
- Nächste freie Nummer: **NEU-251**.
- NEU-057 ist eine ältere Lücke in 01 — nicht die nächste aktive Nummer.
- Im Strang 07 geht die Nummerierung bis NEU-250a; NEU-245d, NEU-245e/f ebenfalls vorhanden.
- NEU-246 existiert doppelt (in 01 und 07) — Klärung ausstehend.

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
Quelle für die Positivität der Momentfolge.**

---

## Gesicherter Kern (Auswahl)

| Bereich | Einträge | Kernresultat |
|---|---|---|
| Primkantenraum | NEU-44, 44.X/X' | $\mathcal H_{\mathrm{rel},N}$ notwendig; Kantendiagonalität; Rang-1-$C_p^{\mathrm{rel}}$ |
| Fourier-Hebung | NEU-42 | $T_p^{\mathrm{rel}} = \log p$; $e^{-sT_p^{\mathrm{rel}}} = p^{-s}$ |
| Nelson / Konfinement | NEU-53–56 | $iJ^-$ wesentlich selbstadjungiert (konditional); $\gamma_N = C/\log N$ widerlegt; Weg B Standard |
| Welt-2-Entscheidung | NEU-135D | $\lVert\varepsilon_p\rVert^2 = 1$; $\lvert c_p\rvert^2 = O((\log p)^2/p)$ |
| Selbstenergie | NEU-136/137 | $\Sigma_{\mathrm{rel}}^{\mathrm{ren}}(\beta)$ konvergent, spurklassig für $\Re\beta>0$ |
| Mangoldt-Spur | NEU-141 | $\operatorname{Tr}(R\Sigma_{\mathrm{rel}}^{\mathrm{ren}}) = -\zeta'/\zeta(\beta)$, $\Re\beta>1$ |
| Koeffiziententyp | NEU-216 | $\mathcal B^{\log}$ submultiplikativ **ohne** Renormierung |
| Cup-Aufstieg | NEU-218 | $L^{\mathrm{cup}}_{g;\mathbf p}\in Z^4(A_{\mathrm{alg}},M)_g$ |
| Xi-Masterkontur | NEU-220k | exakte Vorzeichen, Faktor 2, Polbuchhaltung |
| Hankel-Kriterium | NEU-220w | vollständige Hierarchie RH-äquivalent, beide Richtungen |
| BC-Residuenarchitektur | NEU-15–25 | Dirichlet-/Laurent-Residuenstruktur auf $F^3A_{\mathrm{BC}}^{\mathrm{an}}$ vorhanden |

---

## Wie das Programm hierher kam — drei abgeschlossene Strangwechsel

### 1. Der $[L_3]$-Repräsentantenpfad ist blockiert (NEU-161 – NEU-173)

Zweifache, logisch unabhängige Blockade: die Typbrücke $[L_3] \to L_3^\circ = e_1V_1$ fehlt,
und das Nichtverschwinden des Zielkantenvektors $E_{1;1\to p}^{\mathrm{rel}}$ ist unbewiesen.
Volldokumentation: [`NEU-170d`](05-primkanal-fourierladung/NEU-170d_DAG_Audit_NEU28_NEU162_bereinigt.md).

### 2. Die kohomologische Route endet im O-219-No-Go (NEU-174 – NEU-219z)

Der Cup-Aufstieg zu $HH^4$ gelang (NEU-218), aber der Faktor $g^{-\beta}$ ist
**eingabeunabhängig** und blockiert die zyklische Klasse in $HC^4(A_{\mathrm{alg}})$.

### 3. Der Weil-Strang liefert die aktuelle Architektur (NEU-220 – NEU-250a)

Pfad `[O-219-6]` führte über Gammafaktor, Konturtransport, Nullstellenpaar-Kreinraum und
Spektraldeterminante zum Hankel-Kriterium (NEU-220w). Der Wres-Typaudit-Strang
(NEU-246–NEU-250a) hat die tiefste gemeinsame Lücke identifiziert.

---

## Aktueller Stand (nach Session vom 6. August 2026 — NEU-250a)

### Abgeschlossene Kette dieser Session

```
NEU-246   Typ-Grad-Kerninvarianzaudit Koszul-Kandidat          ✓[M]
NEU-247   Tensor-Lift Typbrücke                                 ✓[M]
NEU-247a  Präzisierungen Typbrücke                              ✓[M]
NEU-247b  Domänenpräzisierung P5, Auditplan c2b2a               ✓[M]
NEU-248   Wohldefiniertheit Tensoroperator                      ✓[M]
NEU-249   Präzisierungen Notation/Konstruktion/Stabilität       ✓[M]
NEU-250   Wres-Minimalblock Kleinfallprüfung                    ✓[M]  → Ausgang E
NEU-250a  Typisierung Dirichletresiduumsform, rel. Primkantenraum ✓[M]_part → Ausgang B
```

### Endentscheidung B (NEU-250a) — ✓[M]_neg, Quelle

> Die Dateien NEU-015 bis NEU-025 liefern eine eigenständige arithmetische
> Dirichlet-/Laurent-Residuenarchitektur auf der BC-Seite. Sie definieren jedoch keine
> Repräsentationsabbildung
> $j_{p,N}: \mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}} \to F^3 A_{\mathrm{BC}}^{\mathrm{an}}$
> vom relativen Primkantenraum in den Definitionsbereich dieser Funktionale. Die bisherige
> relative Wres-Paarung $\langle E_a, E_b\rangle_{\mathrm{Wres,rel}}$ ist kein konstruiertes
> mathematisches Objekt.

### Tiefste gemeinsame Lücke (deepest gap)

```
fehlende Repräsentation  j_{p,N} : V^pre_rel → F³ A_BC^an
```

Alle abhängigen offenen Fragen — `[O-221-1c1a0]`, `[O-246/0corr-2]`, Bestimmung
von $\mathcal N_{\mathrm{Wres,rel}}$, Hebungsunabhängigkeit von $J_{p,b}$ — setzen diese
Abbildung voraus. Korrigierter DAG:

```
BC-Residuenarchitektur
  ⟶ [Repräsentation j_{p,N}]   ← fehlt  →  [O-221-1c1a0-C]  ← aktiver Knoten
      ⟶ relative Paarung h_{p,N}
          ⟶ Grammatrix
              ⟶ Radikal
                  ⟶ Hebungsabstieg  →  [O-221-1c1a0]
```

### Nächster atomarer Knoten

```
[O-221-1c1a0-C]  BC-Repräsentation eines primitiven relativen Primkantenvektors
```

Für $p=2$: ein explizites BC-Element
$j_{2,N}(E_{R;1\to 2}^{\mathrm{rel}}) \in F^3 A_{\mathrm{BC}}^{\mathrm{an}}$ konstruieren,
das sechs Bedingungen erfüllt (NEU-250a §12):

| Nr. | Bedingung |
|---|---|
| 1 | Typkorrektheit: $j_{2,N}(E_R)\in F^3A_{\mathrm{BC}}^{\mathrm{an}}$ |
| 2 | Linearität |
| 3 | Indexverträglichkeit |
| 4 | Involutionsverträglichkeit: $j_{2,N}(E_R)^*$ explizit |
| 5 | Residuenfähigkeit: $\lambda_\beta^{\mathrm{mod}}(R_3(\cdots))$ bei $\beta=1$ auswertbar |
| 6 | Nichttautologie |

---

## Repository-Korrekturen (ausstehend)

| Datei | Korrektur |
|---|---|
| NEU-044 (alle Varianten) | Relative Wres-Paarung als symbolischen Kandidaten kennzeichnen; Hinweis auf fehlende $j_{p,N}$ |
| NEU-221e | Vor Definition des Wres-Radikals: Formalitätsvermerk |
| NEU-246 bis NEU-249 | Vorläufer-Rückbindung an `[O-221-1c1a0-C]` |

**Terminologie (strikt einhalten):**
- `Wres_BC^(q,ℓ)` — tatsächlich definiertes BC-Dirichletresiduum
- `h_Wres,rel` — erst zu konstruierende relative Paarung  
Diese beiden Objekte sind **nicht identisch** und dürfen nicht identisch benannt werden.

---

## Bekannte Dubletten / offene Klärungen

| Eintrag | Status |
|---|---|
| NEU-246 | Existiert doppelt (in 01 und 07) — Klärung ausstehend |
| NEU-219u | Doppelt in 06 |
| NEU-219y | Doppelt in 06 |
| NEU-057 | Lücke in 01 — ältere, nicht mehr aktive Lücke; keine Priorität |

---

## Erste Aufgaben für die neue Session

1. Lies **`KARTE.md`** vollständig (Großschreibung, Root des Repos) — sie ist die
   verlässlichste Übersicht des aktuellen Standes.

2. Lies **`NEU-250a`** in `07-weil-explizitformel/` — dort stehen alle sechs Konstruktions-
   bedingungen für $j_{2,N}$ sowie die Deepest-Gap-Box.

3. Lade NEU-046, NEU-015, NEU-016, NEU-019, NEU-020 aus `01-primkanten-werkzeuge/` und
   prüfe, ob dort ein Ansatz für $j_{2,N}$ erkennbar ist.

4. Eröffne Knoten **`[O-221-1c1a0-C]`** als neue Datei
   `07-weil-explizitformel/NEU-251_O221-1c1a0-C_BC-Repraesentation_primitiver_Primkantenvektor.md`.

5. Schau auch in NEU-221e (in 07) — dein Knoten schließt inhaltlich direkt daran an
   (Wres-Quotient, affine Hebungsfaser).

---

## Gleichzeitig offene Nebenstränge

| Strang | Letzter Stand | Nächste Aufgabe |
|---|---|---|
| **A: Wres-Repräsentation** (aktive Front) | NEU-250a — Ausgang B | `[O-221-1c1a0-C]`: $j_{2,N}$ konstruieren |
| **B: Adelische Momentquelle** | NEU-245c/d — Kanonisierung $\Psi_N$ | NEU-245d abschließen; `[O-245c/2]` |
| **C: Positivitätsquelle Hankel** | NEU-220w — Modell konditional | $(\mu_k)$ aus adelischer Konstruktion |
| **D: Regulierte Spur (krit. Streifen)** | NEU-141 | NEU-141.D: Schema für $0<\Re\beta\le 1$ |
| **E: Singulärwert-Wachstum $J^-$** | NEU-56 | $s_k(J^-)$ divergent oder akkumulierend? |
| **F: Erweiterbarkeit punktierter Kozykel** | NEU-188 | `[O-188-0..3]` |
| **G: Rückrichtung RH** | — | $\operatorname{Spec}\subset\mathbb R \Rightarrow \mathrm{RH}$ |

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

- **Lakatosianische Epistemik.** Jede Aussage erhält einen Status. Kein Kartenhaus.
- **Quellenbasiert.** Keine Behauptung ohne direkten Dateinachweis. Ein Verzeichnislisting
  ist **nicht** dasselbe wie eine gelesene Datei.
- **Konventionen haben Vorrang.** Bei Widersprüchen gilt [`KONVENTIONEN.md`](KONVENTIONEN.md).
  Besonders: $\rho_k$ ist **nicht** unital, $\sigma_k$ schon; $T_a := \sigma_a$.
- **Negative Resultate sind Ergebnisse.** Ein sauber geschlossenes No-Go ist wertvoller
  als ein offener Kandidat.
- **Keine Wiederöffnung geschlossener Routen.** Vor jedem neuen Ansatz [`STATUS.md`](STATUS.md) §3 prüfen.
- **Sprache.** Deutsch für die Diskussion, LaTeX für Formeln.
- **Nummerierung.** Nächste freie Nummer: **NEU-251**.
- **KARTE.md lesen vor jeder Session** — nicht nur das Listing, sondern den vollen Inhalt.
- **Frühe Werkzeugblätter.** NEU-3 bis NEU-56 in `01-primkanten-werkzeuge/`. Dort stehen
  viele Primärdefinitionen — vor jeder Quellensuche nachsehen.
- **Repo-Pflege.** Wesentliche Ergebnisse direkt als Datei ins Repo; CHANGELOG, STATUS und
  OFFENE_PROBLEME mitführen.
- **Erfolgsmeldungen verifizieren.** Nach jedem Commit den Diff auf GitHub prüfen —
  nicht allein der Zusammenfassung des Assistenten vertrauen.
