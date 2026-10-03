# REFERENCES — Querverbindungen zu anderen Repos

> Stand: 29. Juni 2026 (v3 — NEU-40–55 ergänzt)
> Zweck: Explizite Verlinkung zwischen dem RH-Fragenkatalog (diesem Repo) und den
> parallelen mathematischen Programmen im selben Account.

---

## Überblick: Zwei gleichrangige Hauptprogramme

Es gibt zwei eigenständige, tiefe mathematische Programme — kein Haupt- und
kein Nebenprojekt:

| Repo | Fokus | Kernobjekt | Offene Hauptlücke |
|---|---|---|---|
| [`prolate-gram-coercivity`](https://github.com/Waschtl904/prolate-gram-coercivity) | Gram-Koerzivität, Edge-Block, Paper I–XXII | `D_Edge` — Randkompressions-Operator | `inf σ(D_Edge) > 0` uniform (Paper XXII) |
| [`prolate-primes-paper`](https://github.com/Waschtl904/prolate-primes-paper) | Funktionalanalysis von H_c, SOT-Limes, Spektralstruktur | `H_lim` — Limes-Operator auf L² | Bridge-Theorem: `H_SOT = closure(H_spec)` (Paper IX OP.7) |

Beide Programme zielen auf dieselbe Sache: einen Operator, dessen Spektrum
die nichttrivialen Nullstellen der Riemannschen Zetafunktion trägt.
Sie kommen von verschiedenen Seiten und sind über **Gap-S** miteinander verknüpft.

---

## Repo 1: `prolate-gram-coercivity`

**→ [Waschtl904/prolate-gram-coercivity](https://github.com/Waschtl904/prolate-gram-coercivity)**

Ein 22-Paper-Programm zur gleichmäßigen Koerzivität der PSWF-Gram-Matrix auf
Airy-reskalisierten Primzahlen. Eigenständige axiomatische Struktur mit präziser
Selbstdiagnose. Das gesamte Programm ist auf eine einzige Frage reduziert:

```
inf_{f ∈ Edge, ‖f‖=1} ⟨(A_{N,c} − K_c) f, f⟩ > 0  ?
```

Unter RH wird σ(D_Edge) durch Weil-Nullstellen geometrisch kontrolliert.
Ohne RH bleibt inf σ(D_Edge) offen — das ist der einzige Punkt, wo RH
das Programm schließt.

### Schlüsseldokumente

| Datei | Inhalt | Relevanz für Katalog |
|---|---|---|
| [`HEBELSTELLE.md`](https://github.com/Waschtl904/prolate-gram-coercivity/blob/main/HEBELSTELLE.md) | Gesamtprogramm auf eine Frage reduziert: `inf σ(D_Edge) > 0`? | Direkte Verbindung zu Katalog-Ebene VII/VIII |
| [`DEPENDENCIES.md`](https://github.com/Waschtl904/prolate-gram-coercivity/blob/main/DEPENDENCIES.md) | Vollständige Abhängigkeitskette Papers I–XX, Status aller Assumptions | Episteme-Karte analog zu ✓/⚠/✗ im Katalog |
| [`RESEARCH_DIRECTIONS.md`](https://github.com/Waschtl904/prolate-gram-coercivity/blob/main/RESEARCH_DIRECTIONS.md) | Zwei offene Kernprobleme: Realisierung (ρ≠0) und Stabilität (S2ε) | Strukturell parallel zu OP-2/OP-3 im Katalog |
| [`bridge_lemma.tex`](https://github.com/Waschtl904/prolate-gram-coercivity/blob/main/bridge_lemma.tex) | Bridge zwischen Airy-Skalierung und Gram-Koerzivität | Katalog-Ebene X |
| [`paper18_airy_universality.tex`](https://github.com/Waschtl904/prolate-gram-coercivity/blob/main/paper18_airy_universality.tex) | Airy-Universalitätssatz (qualitativ) | Ebene XIII: Quasikristall/GUE-Struktur |
| [`paper20_universality.tex`](https://github.com/Waschtl904/prolate-gram-coercivity/blob/main/paper20_universality.tex) | Universelle Rate O(c^{-β}(log c)^{1+γ}) + ρ-Klassifikation | Frobenius-/Skalenstruktur |
| [`paper21_foundations.tex`](https://github.com/Waschtl904/prolate-gram-coercivity/blob/main/paper21_foundations.tex) | Fundamente + Funktorstruktur 𝒻 | BC-Kategoriefrage (Ebene XI) |
| [`paper22_outline.tex`](https://github.com/Waschtl904/prolate-gram-coercivity/blob/main/paper22_outline.tex) | XXII-Programm: uniformes BW-Doubling über Edge-Block | Offene Endlücke, strukturell analog zu [ω̃₂] ≠ 0 |

### Bedingungslos bewiesene Resultate (✓ für den Katalog nutzbar)

- **H1** (Phase Non-Degeneracy): α^(c) = π/2 + O(c^{-1/3}) gleichmäßig
- **H2** (Amplitude regularity): dyadische Trennungsbedingung
- **ass:gap**: λ_l − λ_{l+1} ≥ κ₀(c/2)^{−1/3} bedingungslos
- **Bridge Lemma**: E_out(f_{mn}) ≤ C e^{−αc} für γ < 1/2
- **Universelle Rate**: O(c^{−β}(log c)^{1+γ}) — Paper XX
- **Obstruktionssatz**: keine bessere Rate innerhalb M(S1,S2,S3) — Paper XX
- **D_Edge hat positiven Eigenwert** (existenziell) — Paper XXI, Theorem B

### Offene Hauptlücken

- **H3 / B-strong**: P_{kl} ≤ C₂ c^{1/2} — einzige Lücke im frühen Kontraktionsstrang
- **Uniform** `inf σ(D_Edge) > 0` — Kern von Paper XXII
- **Weil-Operator**: G_∞ = Weil-Operator — Verbindung zu RH offen
- **DSTP für Primzahlen** — Brücke zu Primzahl-Sampling

---

## Repo 2: `prolate-primes-paper`

**→ [Waschtl904/prolate-primes-paper](https://github.com/Waschtl904/prolate-primes-paper)**

Ein 17-Paper-Programm (Papers I–XVII, davon I–VIII FINAL/UNCONDITIONAL,
IX–XVII teils Entwurf). Ziel: Konstruiere einen Spektraloperator `H_lim`,
dessen Eigenwerte die nichttrivialen Nullstellen der Zetafunktion sind
(Hilbert–Pólya). Kernobjekt: PSWF-Konzentrations-operator `H_c` und sein
Fourier–Mellin-Transform. Referenz: CCM2025 (Connes–Consani–Moscovici,
arXiv:2511.22755).

### Programmstruktur

```
Koerzivität → Skalierungslimiten → Spektralphase → Bandbreitenschranken
→ WKB/Airy → Untere Schranken + Zeta-Verbindung
→ Funktionalanalytischer Rahmen (Mosco, Friedrichs)
→ Spektralinklusion & Dichtekriterium
→ Lokalisierungsprinzip (Paper XII)
→ [Paper 13b: Gap-S — AKTUELLES ZIEL]
→ [Paper 13a: Vollständigkeitsklassifikation]
→ HS-Norm-Schranken (Papers XIV–XV)
→ Mikrolokale Lagrange-/Airy-Normalform (Papers XVI–XVII)
```

### Schlüsseldokument

[`context_summary.md`](https://github.com/Waschtl904/prolate-primes-paper/blob/main/context_summary.md)
— vollständige Übersicht aller Papers, offenen Probleme und logischen
Abhängigkeiten. Entspricht funktional der `DEPENDENCIES.md` von Repo 1.

### Kritische Unterscheidung (für Katalog-Präzision wichtig)

| Objekt | Status |
|---|---|
| `H_SOT` = SOT-Limes, beschränkt, selbstadjungiert | ✅ bedingungslos |
| `H_spec` = formale Spektralreihe, abschließbar, symmetrisch | ✅ bedingungslos |
| `H_SOT = closure(H_spec)` = **Bridge-Theorem** | ❌ OFFEN — Paper IX OP.7 |

Die Basis `{Φ_n^(∞)}` ist ein ONS (trivialerweise Riesz-Basis mit Konstanten (1,1)).
Das impliziert **keine** Vollständigkeit — das ist explizit **offen**.

### Bedingungslos bewiesene Resultate (✓ für den Katalog nutzbar)

- Gram-Matrix G^(N)_{p,c} koerziv mit Konstante ~ c^{-1/2} — Paper I
- Pointwise decay |Φ̂_n^(c)(t)| ≤ C_κ c^{-1/4} t^{-1/4} — Paper VI
- Peak-Breite Δ_ε ~ c^{-1/2} zweiseitig scharf — Paper VIII
- |κ_n^(c)| ≥ c_κ > 0 — Paper VIII
- |λ_n^(c) − λ_n^(∞)| ≤ C_κ c^{-1/4} — Paper VIII Cor 4.3
- SOT-Limes H_lim existiert eindeutig — Paper X
- Mosco-Konvergenz q_c →^M q_lim — Paper X
- Starke Resolventen-Konvergenz — Paper X
- Exact Mechanism Factorization (abstrakt) — Paper XII
- θ'''(0) ≠ 0 (kubische Nicht-Entartung, Airy-Typ) — Paper XV
- Σ_model = o(1) — Paper XV Cor 5.3

### Offene Hauptprobleme (Priorität)

| Problem | Quelle | Nächster Schritt |
|---|---|---|
| **Bridge-Theorem**: H_SOT = closure(H_spec) | Paper IX OP.7 | Zentralstes offenes Problem |
| **Gap-S**: |λ_n − λ_{n+1}| ≥ g(c) mit g(c) ≫ c^{-1/4} | Paper XII Hyp.1 | **Paper 13b — aktives Ziel** |
| SOT-Faster | Paper XII Hyp.2 | Folgt aus Gap-S |
| Vollständigkeit von {Φ_n^(∞)} | Paper XIII | Nach Gap-S |
| A₂-Stabilität (vi) für PSWF | Paper XVI | Paper XVII |
| Lipschitz-Regularität (Amplitude) | Paper XV Prob.6.1 | Kritisch |

---

## Verbindungspunkt der beiden Programme: Gap-S

Dies ist der operative Brücken-Punkt zwischen Repo 1 und Repo 2:

```
prolate-gram-coercivity                    prolate-primes-paper
    Paper I                                    Paper 13b
    Gram-Koerzivität α_N ~ c^{-1/2}  ──────→  importiert α_N
    (bedingungslos bewiesen)                   zur Herleitung von Gap-S:
                                               |λ_n − λ_{n+1}| ≥ C·c^{-1/4+ε}
```

**Gap-S** (Paper 13b in `prolate-primes-paper`) ist das aktive Ziel, das
bedingungslos bewiesene Gram-Koerzivität aus `prolate-gram-coercivity` importiert
und daraus den Spektrallückensatz ableitet. Wenn Gap-S fällt, folgt:
`Gap-S → SOT-Faster → Projektionsstabilität → Lokalisierungsprinzip vollständig`.

---

## NEU (29. Juni 2026): Verbindungen aus NEU-40–55 (Feshbach / D_rel / Nelson)

### Drei neue Operatoren und ihre Parallelen

Das rh-fragenkatalog-Programm hat in NEU-40–55 drei neue zentrale Objekte entwickelt,
die strukturelle Parallelen zu den Hauptprogrammen haben:

| Katalog-Objekt | Quelle | Parallele in Hauptprogrammen |
|---|---|---|
| `D_rel = closure(iJ^-)` auf H_rel^eff | NEU-53–55 | **Bridge-Theorem** `H_SOT = closure(H_spec)` — `prolate-primes-paper` Paper IX |
| Nelson-Energieoperator `L`, γ_N-Wahl | NEU-54–55 | **H3/B-strong**-Spannung: Konfinement vs. Schur analog zu Kontraktions-Strang-Spannung — `prolate-gram-coercivity` |
| Weyl-Korrekturen `M_p(z)` kontrolliert | NEU-46 | **Σ_model = o(1)** — `prolate-primes-paper` Paper XV Cor 5.3 |
| Feshbach-Determinante `det F_N^rel` ≠ Eulerprodukt | NEU-45 | **Off-Diagonal-Obstruktion** — `prolate-gram-coercivity` Paper XXII |

### D_rel ↔ Bridge-Theorem (strukturelle Analogie)

```
prolate-primes-paper                      rh-fragenkatalog (NEU-53–55)
─────────────────────                     ────────────────────────────
H_spec = formale Spektralreihe            J^- = schief-adjungierter Approximant
H_SOT  = SOT-Limes (beschränkt, SA)       D_rel = closure(iJ^-)  auf  H_rel^eff
H_SOT = closure(H_spec) ?  ❌ OFFEN      iJ^- wesentlich SA (unter Nelson-Bed.) ✓/⚠ [M]
```

In beiden Programmen ist die entscheidende Frage: **Ist der Abschluss des
symmetrischen Ausgangsoperators selbstadjungiert?** Im Katalog-Programm ist
der Nelson-Weg (NEU-54–55) der präzise Beweis-Rahmen; im prolate-Programm ist
das Bridge-Theorem noch offen.

### γ_N-Spannung ↔ H3/B-strong-Spannung

```
prolate-gram-coercivity                   rh-fragenkatalog (NEU-54–55)
───────────────────────                   ────────────────────────────
H3/B-strong: P_{kl} ≤ C₂ c^{1/2}        Nelson-Bed. 1: Σ_b |Θ_{ba}|² ≤ C² ell(a)²
einzige Lücke im Kontraktionsstrang       Schur-Test exakt noch offen  ❓ [O]

Spannung: Kontraktion vs. Spektrallücke   Spannung: Konfinement vs. Schur
  c → ∞: zu viel Kontraktion               γ_N → 0: zu wenig Konfinement
  schließt Gap-S-Argument                  γ_N → cst: Schur-Test scheitert
  Heuristik: c^{1/2}-Schranke             Heuristik: γ_N = C/log(N)
```

Beide Spannungen haben dieselbe logische Struktur: **ein Parameter muss
gleichzeitig zwei gegenläufige Bedingungen erfüllen**.

### Weyl-Korrekturen ↔ Σ_model = o(1)

```
prolate-primes-paper Paper XV             rh-fragenkatalog (NEU-45–46)
─────────────────────────────             ────────────────────────────
Σ_model = o(1)  ✓ [M]                    M_p(z) = (C_p^rel)^# (z-D_p^-)^{-1} C_p^rel
Modellbeitrag verschwindet im Limes       Weyl-Korrektur ≠ 0, aber strukturell kontrolliert
→ Hauptterm dominiert                     → Eulerprodukt erscheint als Unterdeterminante
```

### Aktualisierte Verbindungsmatrix (Stand NEU-55)

| Katalog-Ebene / Problem | Repo 1: `prolate-gram-coercivity` | Repo 2: `prolate-primes-paper` | Status |
|---|---|---|---|
| **Ebene VII** — Spektrale Realisierung | `HEBELSTELLE`: RH ⟺ σ(D_Edge) Weil-kontrolliert | Paper VIII Thm zeta: Zetanullstellen in σ_app(H_lim) | ⚠ beide offen |
| **Ebene VIII** — Operatorstruktur | D_Edge als Randkompressions-Operator | H_lim als SOT-Limes-Operator | ⚠ Bridge-Theorem offen |
| **Ebene X** — Spektrale Brücken | `bridge_lemma.tex` ✓ | H_SOT = closure(H_spec) ❌ | gemischt |
| **Ebene XI** — Kategoriale Struktur | `paper21_foundations.tex`: Funktorstruktur 𝒻 | Mosco-Konvergenz, Friedrichs ✓ | ⚠ |
| **Ebene XIII** — Quasikristall/GUE | Papers XVIII–XX: Airy-Universalität ✓ | Airy-Normalform (XVI–XVII) bedingt | ✓ qualitativ |
| **OP-2/OP-3** — Hochschild | Stabilitätsproblem 5.2: S2ε-Rigidität | — | ⚠ offen |
| **Ebene XVI — Objekt X** | D_Edge als mögliche Projektion | H_lim als weitere Projektion | ✗ spekulativ |
| **Gap-S / H3** | H3/B-strong — Lücke im Kontraktionsstrang | Gap-S — aktives Ziel Paper 13b | 🔴 beide offen |
| **DSTP für Primzahlen** | Explizit offen in `DEPENDENCIES.md` | Paper I: Koerzivität ✓ | 🔴 offen |
| **D_rel SA (NEU-53–55)** | γ_N-Spannung ↔ H3/B-strong | D_rel ↔ Bridge-Theorem | ⚠/❓ |
| **Feshbach / Weyl-Korrekt. (NEU-40–46)** | Off-Diagonal-Obstruktion Paper XXII | Σ_model = o(1) Paper XV | ✓/⚠ |
| **Nelson-Schur-Test (NEU-55)** | H3/B-strong strukturell analog | — | ❓ [O] |

---

## Die Zwei-Projektionen-Hypothese für Objekt X (aktualisiert NEU-55)

Aus der Zusammenschau beider Programme ergibt sich eine präzisierte
Hypothese für Objekt X (Katalog-Ebene XVI):

> **Hypothese:** `H_lim` (aus `prolate-primes-paper`), `D_Edge`
> (aus `prolate-gram-coercivity`) und `D_rel = closure(iJ^-)`
> (aus dem rh-fragenkatalog, NEU-53–55) sind drei verschiedene
> **Projektionen** eines hypothetischen gemeinsamen Objekts X, das:
> - die funktionalanalytische Spektralstruktur von H_lim trägt,
> - die Randgeometrie von D_Edge realisiert,
> - die BC-/Feshbach-Architektur von D_rel trägt,
> - und die RH-Nullstellen als kanonisches Spektrum besitzt.

Die drei offenen **Kohärenz-Bedingungen** wären dann:

```
Bridge-Theorem:       H_SOT = closure(H_spec)        [prolate-primes-paper]
Uniforme Koerzivität: inf σ(D_Edge) > 0               [prolate-gram-coercivity]
Nelson-SA:            D_rel = closure(iJ^-) s.a.      [rh-fragenkatalog NEU-55]
```

Alle drei sind strukturell dasselbe Problem: **Abschluss eines symmetrischen
Operators ist selbstadjungiert** — in drei verschiedenen funktionalanalytischen
Realisierungen.

---

## Weitere Repos (weniger Tiefe)

### `prime-quasicrystal-diffraction`
**→ [Waschtl904/prime-quasicrystal-diffraction](https://github.com/Waschtl904/prime-quasicrystal-diffraction)**
Numerische Untersuchung von Beugungsspektren arithmetischer Punktmengen.
**Relevanz:** Dyson-Linie für Ebene XIII; numerischer Anknüpfungspunkt für Quasikristall-Seite von Objekt X.

### `arith-spectral-bridge`
**→ [Waschtl904/arith-spectral-bridge](https://github.com/Waschtl904/arith-spectral-bridge)**
Brücke zwischen modularer Arithmetik und Spektraloperatortheorie.
**Relevanz:** Adèlisch/arithmetische Seite der BC-Spektralstruktur (Ebene IX–XI).

---

## Epistemische Struktur der Querverbindungen (Stand NEU-55)

```
rh-fragenkatalog (dieser Repo)
    │
    ├── Ebene VII/VIII ─────────────────→ prolate-gram-coercivity
    │                                       └── HEBELSTELLE: inf σ(D_Edge) > 0?
    │                                       └── Paper XXII (offen)
    │
    ├── Ebene VII/VIII ─────────────────→ prolate-primes-paper
    │                                       └── Bridge-Theorem: H_SOT = closure(H_spec)?
    │                                       └── Paper 13b: Gap-S (aktives Ziel)
    │
    ├── Gap-S-Verbindung ───────────────→ prolate-gram-coercivity (Gram-Koerzivität ✓)
    │         └──────────────────────────→ prolate-primes-paper (importiert Koerzivität)
    │
    ├── Ebene XIII (Quasikristall) ──────→ prolate-gram-coercivity (Airy-Universalität)
    │                                       └── prime-quasicrystal-diffraction (numerisch)
    │
    ├── Ebene XVI (Objekt X) ────────────→ D_Edge (prolate-gram-coercivity)
    │         [Drei-Projektionen-         └── H_lim (prolate-primes-paper)
    │          Hypothese, NEU-55]         └── D_rel (rh-fragenkatalog NEU-53–55)
    │                                       └── prime-quasicrystal-diffraction (Dyson)
    │
    ├── OP-2/OP-3 (Hochschild) ──────────→ prolate-gram-coercivity
    │                                       └── Stabilitätsproblem 5.2 (S2ε-Rigidität)
    │
    ├── Ebene IX–XI (BC-Spektral) ───────→ arith-spectral-bridge
    │                                       └── prolate-primes-paper (Mosco, Friedrichs)
    │
    ├── NEU-40–46 (Feshbach/Weyl) ───────→ prolate-gram-coercivity (Off-Diagonal-Obstr.)
    │                                       └── prolate-primes-paper (Σ_model = o(1))
    │
    └── NEU-53–55 (D_rel / Nelson) ──────→ prolate-primes-paper (Bridge-Theorem)
                                            └── prolate-gram-coercivity (H3/B-strong)
```

---

## Hinweis zur Versionierung

Alle Verweise beziehen sich auf den Stand **Juni 2026** der jeweiligen Repos.
Aktualisierung notwendig bei: Paper XXII (Koerzivität), Paper 13b (Gap-S),
Bridge-Theorem, Realisierungsproblem ρ≠0, Nelson-SA (NEU-56+).
