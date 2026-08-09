# SYN-Provenienzmatrix

**Stand:** 2026-08-09  
**Zweck:** Jeder migrierte Themenblock erhält einen eindeutigen aktuellen SYN-Zustand und eine nachvollziehbare Provenienz. Historische NEU-Dateien werden nicht gelöscht; `SUPERSEDED`, `NO-GO`, `OPEN` und `INCORPORATED` bleiben getrennt.

**Knotenstatuskategorien** (beschreiben den Zustand eines Forschungsknotens):
- `INCORPORATED` — gültige Mathematik, im SYN-Paper übernommen
- `NO-GO` — negatives Resultat, im SYN-Paper dokumentiert
- `SUPERSEDED` — durch späteren Knoten/Reaudit ersetzt
- `AUDIT-ONLY` — historischer Fehler-/Auditweg, kein eigenständiger positiver mathematischer Inhalt
- `OPEN` — aktive Forschungsfrage

**Dokumentstatus** (beschreiben den Zustand eines SYN-Papers/Blocks, getrennt von Knotenstatuskategorien):
- `FROZEN ✓[K/M]` — endgültig eingefroren; Wiederöffnung nur bei neuem konkretem mathematischem Gegenbefund
- `PASS-A SEALED` — Reconciliation/Auditbasis abgeschlossen; SYN-Migration freigegeben, aber Paper noch nicht eingefroren
- `CANDIDATE` — Freeze-Kandidat, letzter Cleanup ausstehend
- `ACTIVE` — in aktiver Revision

---

## Kanonische Definitionen (P02, §1–§6)

> Fourier-Konvention, $P_{\text{Haar}}$, $R_{\text{PW}}$, $C_{a,b}$, $g_{a,b}$, $h_{a,b}$, $\gamma_\infty$, $\Lambda_\Gamma$, $B_W$ — **kanonisch in P02 definiert**. Andere Papers verweisen auf P02 und geben höchstens Erinnerungen.

---

## Dokumentstatus — aktueller Freeze-/Migrationsstand

| Dokument | Patch / Auditanker | Dokumentstatus | Datum |
|---|---|---|---|
| P02 | Patch 3.5 | `FROZEN ✓[K/M]` | 2026-08-08 |
| P03 | Sync Patch 3 | `FROZEN ✓[K/M]` | 2026-08-08 |
| P05 | eingefrorener SYN-Endstand | `FROZEN ✓[K/M]` | 2026-08-09 |
| P06 | LaTeX-Transferaudit `1b1a7173`; G-T4/G-T5 bindend | `FROZEN ✓[K/M]` | 2026-08-09 |
| P07 | Patch 5 / P10-Reconciliation; Determinante auf `D_N->1` synchronisiert; LFF-Umkehrung OPEN | `FROZEN ✓[K/M]` | 2026-08-09 |
| P08 | Markdown `31c93d50`; LaTeX `d283c34c`; Transferaudit `3f12e0ef` | `FROZEN ✓[K/M]` | 2026-08-09 |
| P09 | Pass-A-Seal `28b5cba5`; Markdown `8346733e`; LaTeX `26f9d60e`; Transferaudit `e724b5a7` | `FROZEN ✓[K/M]` | 2026-08-09 |
| P10 | Pass-A FINAL SEAL `b8be0d6f`; Inventar final reconciliiert | `PASS-A SEALED` — SYN noch nicht geschrieben | 2026-08-09 |

**Freeze-Ausnahme P07:** P07 wurde nach seinem Freeze ausschließlich wegen eines neuen konkreten Cross-SYN-Gegenbefunds aus P06 G-T4/G-T5 eng begrenzt wieder geöffnet und danach in Markdown/LaTeX erneut synchron eingefroren. Dies entspricht der Migrationsregel; andere P05–P09-Blöcke wurden nicht pauschal wieder geöffnet.

---

## Block-Provenienz P05–P10

| Block | Primäre SYN-Rolle | Bindender Endstand | Provenienzstatus |
|---|---|---|---|
| P05 | relative Primkanäle, Lift-/Quell-/Gramgeometrie | gültige positive Resultate plus exakt gescopte Kanal-/Lift-No-Gos; Nichtentartung und globale Kopplung offen | `FROZEN / RECONCILED` |
| P06 | Jacobi–Feshbach, Divisorgraph, Transportgenerator | finite Identitäten und Modell-No-Gos; P06 G-T4/G-T5 korrigieren NEU-088–90 auf `D_N->1` | `FROZEN / RECONCILED` |
| P07 | Weil-Form-Statistik, Herglotz-Interface | Patch 5 bindend: `D_N->1` nur modell-/skalenspezifisch; `LFF=>Rampe` bewiesen, Umkehrung OPEN | `FROZEN / P10-RECONCILED` |
| P08 | Grenzoperator, Renormierung, Finite Part | modellrelative/conditionale Spur-/Mangoldt-Stränge; Primeclock-H1 ungewichtet No-Go; gewichteter Ersatz offen | `FROZEN / RECONCILED` |
| P09 | BC, Hochschild, geladene Kohomologie, Zyklizität | positiver geladener Hochschildpfad; kanonischer Rotations-No-Go mit expliziten Firewalls | `FROZEN / RECONCILED` |
| P10 | kondensierte No-Go-Sammlung | Pass-A-Inventar P05–P09, Gegencheck, Cross-SYN-Reaudit und FINAL SEAL abgeschlossen | `PASS-A SEALED / SYN-MIGRATION FREIGEGEBEN` |

---

## Knoten-Provenienz — kanonische Definitionsebene P02/P03

| NEU | SYN-Ziel | Abschnitt | Rolle | Status |
|---|---|---|---|---|
| NEU-220k | P02 | §1 | Fourier-Masterkonvention | `INCORPORATED` ✓[M] |
| NEU-220l | P03 | §1 | $B_W\ge0\Leftrightarrow$ RH | `INCORPORATED` ✓[M] |
| NEU-220b | P02, P07 | §5 | $\gamma_\infty$ Asymptotik | `INCORPORATED` ✓[M] |
| NEU-250n–r | P02 | §2–§4 | Port-Karte, $R_{\text{PW}}$, $g_{a,b}$ | `INCORPORATED` ✓[K/M] |
| NEU-252 (Patch) | P02 | §6 | Hermitesche Weilform $B_W$ | `INCORPORATED` ✓[K/M] |
| NEU-255 (Patch 2) | P03 | §2 | $H_0=L^2$, Koisometrie | `INCORPORATED` ✓[K/M] |
| NEU-256 (Patch) | P03 | §3 | $R_{\text{arith}}$; KLMN $\times[M]$ | `INCORPORATED` ✓[K/M] |
| NEU-257 (Patch 3) | P03 | §3–§5 | Closability-Firewall, explizite Folge | `INCORPORATED` ✓[K/M] |
| NEU-258 (Patch 1) | P02 | §6 (`thm:lit-id`) | Literaturidentifikation $B_{W,\text{NEU-252}}=B_{W,\text{Lit}}$ | `INCORPORATED` ✓[K/M] |
| NEU-259 | P03/P12? | — | RH-freie $\mathcal H_W$-Konstruktion | `OPEN` ?[O] |

> Diese Tabelle ist **keine erneute Einzelinventur aller historischen NEU-Dateien**. Für P05–P09 ist der jeweilige eingefrorene SYN-Endstand samt Pass-A-/Reaudit-Provenienz die bindende Blockreferenz. P10 führt die Negativ-/OPEN-Provenienz zusätzlich explizit in seiner Pass-A-Matrix.

---

## Offene Migrationspakete nach P10 Pass-A

Die früher hier aufgeführten P05–P09-Pakete sind inzwischen SYN-migriert und eingefroren. Offen sind nun:

| Block | Ziel | Status / Priorität |
|---|---|---|
| No-Go-Sammlung | P10 | **nächster Schritt:** SYN aus versiegeltem Pass-A-Inventar schreiben |
| Globale Kopplung + Objekt-X-Geometrie | P11 | danach; benötigt P05–P09 und darf P10-No-Gos nicht überdehnen |
| Finite-to-Infinite Weil-Geometrie | P12 | aktive Forschungsfront auf Basis P02/P04 |
| Survey + DAG | P00 | nach den vorigen Blöcken konsolidieren |

---

## SYN-Zielarchitektur

| ID | Arbeitstitel | Hauptsubstanz |
|---|---|---|
| P00 | Object X: Program, Architecture and Current Frontier | Survey, DAG, Status |
| P01 | BC Prime-Power Weights | bestehend |
| P02 | Adelic Weil Amplitude Port | **FROZEN** |
| P03 | Haar-$L^2$ Firewall | **FROZEN** |
| P04 | Finite Weil Geometry and Suzuki Extensions | bestehend |
| P05 | Relative Prime Channels and Arithmetic Edge Geometry | **FROZEN** |
| P06 | Jacobi–Feshbach and Divisor-Graph Approaches | **FROZEN** |
| P07 | Weil Form, Statistics and RH-Equivalent Positivity Criteria | **FROZEN / P10-RECONCILED** |
| P08 | Renormalized Prime Operators and Finite-Part Structures | **FROZEN** |
| P09 | Bost–Connes and Hochschild Structures | **FROZEN** |
| P10 | No-Go Theorems for Canonical Global Coupling | **PASS-A SEALED; SYN NEXT** |
| P11 | Global Coupling and the Object-X Candidate Geometry | $B_{pq}$, Objekt-X-Axiome |
| P12 | Finite-to-Infinite Weil Geometry | $J_{a,b}$, $a\to\infty$, aktive Forschungsfront |

---

## Migrationsregel

Ein NEU-/Themenblock gilt als **eingefroren**, sobald:
1. alle gültigen Aussagen im SYN-Paper erscheinen;
2. No-Go-, SUPERSEDED-, CONDITIONAL- und OPEN-Status sichtbar erhalten sind;
3. das SYN-Paper ein SYN-Direktaudit bestanden hat;
4. die Provenienzbuchung den Endstand abbildet.

Ein eingefrorener Block wird nur bei einem **neuen konkreten mathematischen Gegenbefund** eng begrenzt wieder geöffnet. Genau diese Ausnahme wurde bei P07 durch den späteren P06-G-T4/G-T5-Befund angewendet.

Danach muss der historische Block im normalen Forschungsalltag nicht vollständig neu gelesen werden.

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, 2026-08-09.*