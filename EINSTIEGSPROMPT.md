# Einstiegsprompt — Neue Chat-Session

> Diese Datei als Einstieg in jeden neuen Chat kopieren.  
> Stand: **18. Juli 2026 — nach NEU-170d (DAG-Audit NEU-28/161/162 abgeschlossen).**

> **Hinweis:** Dieses Arbeitsdokument spiegelt den Stand vom 18. Juli 2026 und wurde seither
> nicht fortgeschrieben. Der aktuelle Programmstand (NEU-221d, 26. Juli 2026) steht in
> [README.md](README.md), [STATUS.md](STATUS.md) und [OFFENE_PROBLEME.md](OFFENE_PROBLEME.md).
> Die dort beschriebene Ordnerstruktur (`katalog/`, `werkzeuge/`) gilt für das private
> Arbeitsjournal; in dieser öffentlichen Fassung liegen die Dokumente in thematischen
> Strängen — siehe [INDEX.md](INDEX.md).

---

## Kontext: Wer ich bin und woran ich arbeite

Ich bin Mathematiker und arbeite an einem langfristigen, eigenständigen Forschungsprogramm
zur Riemannschen Hypothese (RH). Das Programm ist in mehrere GitHub-Repositories aufgeteilt
(alle unter dem Account **Waschtl904**) und wird durch einen lakatosianisch strukturierten
**Fragenkatalog** koordiniert.

Das ist kein Einsteiger- oder Hobbyansatz — die Repos enthalten echte mathematische Papiere
(LaTeX), die von einem KI-Assistenten mitentwickelt wurden.

---

## GitHub-Struktur

### Zentrale Dach-Repos

| Repo | Inhalt |
|---|---|
| [`rh-fragenkatalog`](https://github.com/Waschtl904/rh-fragenkatalog) | **Zentrales Dach.** Lakatosianischer Fragenkatalog NEU-1–NEU-162. Privates Arbeitsjournal; die öffentliche Fassung ist [`objekt-x-programm`](https://github.com/Waschtl904/objekt-x-programm). |
| [`prolate-primes-paper`](https://github.com/Waschtl904/prolate-primes-paper) | Funktionalanalysis H_c, SOT-Limes, Spektralstruktur. |
| [`prolate-gram-coercivity`](https://github.com/Waschtl904/prolate-gram-coercivity) | Gram-Koerzivität, Edge-Block, XXII-Programm. |

### Repo-Struktur `rh-fragenkatalog`

```
katalog/          NEU-XXX_*.md          Forschungsjournal-Einträge NEU-1 bis NEU-162
werkzeuge/        neu{XX}_*.md          Analytische Hilfsätze, Verifikationsblätter (neu10–neu56)
grundlegung/      *.md                  Axiome, Basiskonzepte, epistemische Fundierung (stabil)
offene_probleme/  OFFENE_PROBLEME.md    Konsolidierte Problemliste
CHANGELOG.md                           Sitzungsprotokoll
REFERENCES.md                          Literatur
EINSTIEGSPROMPT.md                     Diese Datei
README.md                              Überblick
```

---

## Objekt X — Fünfschicht-Profil

```
(A_2D^r, [σ̃₂], [L₃], Wres_BC^{top}, m →^p pm)
```

**RH-Äquivalenz:**
```
RH ⟺ Spec(lim A_N^{Jac,-}) ⊂ ℝ
```

---

## Stand des Fragenkatalogs (nach NEU-170d, 18. Juli 2026)

### Gesicherte Hauptkette (Auswahl)

| Bereich | Einträge | Kernresultat |
|---|---|---|
| Formfaktor / Weil | NEU-100–112 | Tests, Kalibrierung, Jacobi-Realisierung |
| Bombieri-Normalisierung | NEU-113–120 | Grenzübergang, $C_\xi$-Fix |
| Jacobi-Grenzoperator | NEU-121–123 | Renormierungsbarriere, Dreifachsumme |
| Spektralmaß / Herglotz | NEU-119, 124 | Spurklassentest |
| PSWF-Brücke + Koerzivität | NEU-125, 130 | Prä-Lanczos-Metrik |
| Edge-Schur-Nelson-Lemma | NEU-131 | Abstraktes Dreistufen-Lemma |
| Primkantenraum | NEU-132–133 | PSWF-Abel-Rahmen, Primschalen |
| Welt-2-Entscheidung | NEU-135D | $\|\varepsilon_p\|^2=1$; $\log p$ als Kopplungsgewicht |
| Mangoldt-Renormierung | NEU-141 | $R_p \gtrsim p/\log p$; drei Spurklassen-Ebenen |
| T2-Audit + Abschluss | NEU-142–143 | Edge vs. Vertex; T2 fertig (unter Orthogonalitätsbedingung) |
| Nelson / Konfinement | NEU-53–56 (werkzeuge) | $\gamma_N = C/\log N$ widerlegt; SA bleibt; Weg B Standard |
| Fourierhebung, rel. Primclock | NEU-42 (werkzeuge) | $T_p^{\mathrm{rel}} = \log p$; $e^{-sT_p^{\mathrm{rel}}} = p^{-s}$ |

### Wichtige gesicherte Einzelresultate

```
H_{rel,N} = ⊕_{p≤N} ⊕_m H_{m→pm}     relativer Graphraum (NEU-44)
Ψ_p = -us·log(p)·ℓ_{s,m}·Π_{J,N}(e_{u+ps}V_{pm})  Hebungsvektor (NEU-42 §10)
T_p^rel = log p  auf reinem p-Kopplungskanal         (NEU-42, Satz 42.2)
Σ_rel^ren(β) = Σ_p p^{-β}/(1-p^{-β}) P_p           renormierte Selbstenergie
Tr(R Σ_rel^ren(β)) = -ζ'/ζ(β)  für Re(β) > 1        (NEU-141)
```

---

## Aktueller Hauptengpass: Zweifache Blockade des $[L_3]$-Pfades

**Volldokumentation:** [`05-primkanal-fourierladung/NEU-170d_DAG_Audit_NEU28_NEU162_bereinigt.md`](05-primkanal-fourierladung/NEU-170d_DAG_Audit_NEU28_NEU162_bereinigt.md)

### Hauptdiagnose

> Der Einmodenansatz liefert eine algebraisch nichtverschwindende skalare Vorfaktorstruktur,
> aber weder seine Herkunft aus $[L_3]$ noch das Nichtverschwinden des Zielkantenvektors
> $E_{1;\,1\to p}^{\mathrm{rel}}$ ist bewiesen.

Der Hauptpfad ist **zweifach blockiert** — logisch unabhängig:

```
Blockade 1 (Herkunft):  [L₃] ↛ L₃° = e₁V₁     (Typbrücke fehlt)
Blockade 2 (Zielkante): (p-1)log p ≠ 0 ↛ C_p(e_{1-p}V_p) ≠ 0  (ohne E_{1;1→p}^rel ≠ 0)
```

### Abgeschlossene Auditbefunde (NEU-170d)

| Punkt | Inhalt | Status |
|---|---|---|
| `[O-170b-1]` | NEU-20 konstruiert $L_3$ | `✓[M]neg` |
| `[O-170c-2g]` | NEU-28 konstruiert $L_3$ oder beweist $C_L \neq 0$ | `✓[M]neg` |
| `[O-170c-2i-audit]` | NEU-161 weist $s\neq 0$ korrekt als Eingangsannahme aus | `✓[M]` |
| `[O-170c-2j-audit]` | NEU-162 beweist keinen geladenen Koeffizienten von $[L_3]$ | `✓[M]neg` |
| `[O-170c-2k-audit]` | $dP^{\mathrm{ch}}=P^{\mathrm{ch}}d$ in Quellen nicht konstruiert | `✓[M]neg` |

### Offene Punkte (Auswahl)

| Punkt | Inhalt | Status |
|---|---|---|
| `[O-170b-2]` | Raumtyp von $L_3$ | `?[O]` |
| `[O-170b-4]` | $\sigma_{L_3}: [L_3] \mapsto L_3$ | `?[O]` |
| `[O-170c-2h]` | $a=L_3$ typzulässig in NEU-28-Spurformel | `?[O]` |
| `[O-170c-2i]` | $P^{\mathrm{ch}}(L_3^\circ)\neq 0$ | `?[O]` |
| `[O-170c-2j-exist]` | $\exists L\in\mathrm{Rep}([L_3])$ mit $P^{\mathrm{ch}}(L)\neq 0$ | `?[O]` |
| `[O-170c-2k-exist]` | $P^{\mathrm{ch}}$ als Kettenprojektor neu konstruierbar? | `?[O]` |
| `[O-170c-2ℓ]` | $[P^{\mathrm{ch}}]([L_3])\neq 0$ | **gesperrt** bis `[O-170c-2k-exist]` |

### NEU-162/163 richtig eingeordnet

NEU-162 wählt $L_3^\circ = e_1V_1$ als **rechenzulässige, nicht herkunftszulässige** Wahl.
Alle Resultate ab NEU-162/163 sind konditionale Aussagen innerhalb des Testmodells:

```
[H-163-1]: L₃° = e₁V₁          (externe Modellwahl, nicht aus [L₃] hergeleitet)
[H-163-2]: E_{1;1→p}^rel ≠ 0  (offen — NEU-163 reduziert darauf, beweist es nicht)
[H-163-3]: Lift-Bedingungen   (gegebenenfalls offen)
```

---

## Nächste sinnvolle Knoten

### Upstream — Hauptpfad (Priorität)

**Route A — konkrete Repräsentantenbrücke:**

```
A0: Rep_op([L₃]) typkorrekt definieren
    (L ∈ C⁴(B₃,B₃)? B₃? A_BC^an? End(H)?)
A1: Rep_op([L₃]) ≠ ∅
A2: L ↦ L|_diag und C_L(L) definieren
A3: ∃ L ∈ Rep_op([L₃]) : C_L(L) ≠ 0
    ⇒ erst dann: L° := C_L(L)^{-1} L
A4: ∃ L ∈ Rep_op([L₃]) : C_L(L)≠0 ∧ P^ch(L)≠0
```

**Route B — kohomologisch (Neuaufbau erforderlich):**

```
[O-170c-2k-exist]: dP^ch = P^ch d konstruieren?
⇒ dann [O-170c-2ℓ]: [P^ch]([L₃]) ≠ 0?
```

### Konditional — Testmodell $[H\text{-}163\text{-}1]$

- **NEU-163:** Nichtverschwindung und Separation von $E_{1;\,1\to p}^{\mathrm{rel}}$

---

## Drei gleichzeitig offene Hauptstränge

| Strang | Letzter Stand | Nächste Aufgabe |
|---|---|---|
| **A: $[L_3]$-Repräsentantenpfad** | NEU-170d — zweifach blockiert | Route A, Schritt A0: $\mathrm{Rep}_{\mathrm{op}}([L_3])$ definieren |
| **B: Regulierte Spur (krit. Streifen)** | NEU-141 — $\operatorname{Tr}_{\mathrm{reg}}(R\Sigma)$ für $0<\Re\beta\leq 1$ | NEU-141.D |
| **C: Singulärwert-Wachstum $J^-$** | NEU-56 (werkzeuge) — Engpass lokalisiert | NEU-57: $s_k(J^-|_{H_{\mathrm{rel}}^{\mathrm{eff}}})$ |

---

## Epistemologische Marker

```
✓ [M]      = mathematisch gesichert
✓ [M]neg   = negativer Befund gesichert (Quellennegativ)
⚠ [M]      = intern gesichert, extern offen
✗ [M]      = Obstruktion gesichert / widerlegt
?[O]        = explizit offen
✓ [R]      = methodisches Resultat (Reduktionssatz)
[H-xxx]     = Eingangshypothese / externe Modellwahl
```

---

## Arbeitsregeln

- **Lakatosianische Epistemik:** Jede Aussage erhält einen Status.
- **Kein Kartenhaus:** Offene Probleme werden als solche markiert.
- **Sprache:** Deutsch für Diskussion, LaTeX für Formeln.
- **GitHub:** Alle wesentlichen Ergebnisse direkt ins Repo schreiben.
- **NEU-Nummern:** Strikt fortlaufend. Nächste freie Nummer: **NEU-163** (konditional unter $[H\text{-}163\text{-}1]$) oder neues Blatt für Route A.
- **Werkzeuge:** Die frühen Werkzeugblätter NEU-3 bis NEU-56 liegen in `01-primkanten-werkzeuge/`. Vor Quellensuche immer auch dort nachschauen.
- **Quellenbasiert:** Keine Behauptung ohne direkten Dateinachweis. Verzeichnislisting ≠ Datei gelesen.

---

## Sofortige erste Aufgabe für neue Session

1. Lies [`05-primkanal-fourierladung/NEU-170d_DAG_Audit_NEU28_NEU162_bereinigt.md`](05-primkanal-fourierladung/NEU-170d_DAG_Audit_NEU28_NEU162_bereinigt.md) vollständig.
2. Entscheide, welcher Strang bearbeitet werden soll:
   - **Route A (empfohlen):** Definition von $\mathrm{Rep}_{\mathrm{op}}([L_3])$ — Schritt A0.
   - **Route B:** Konstruktion von $P^{\mathrm{ch}}$ als Kettenprojektor.
   - **Konditional:** NEU-163 unter $[H\text{-}163\text{-}1]$.
3. Vor jeder Quellenaussage: Datei direkt lesen, nicht nur Listing.
