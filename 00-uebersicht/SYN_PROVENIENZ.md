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
| P10 | Pass-A Seal `b8be0d6f`; Markdown `d307654c`; LaTeX `bc42bdff`; FINAL SEAL `449f361e` | `FROZEN ✓[K/M]` | 2026-08-09 |
| P11 | globale Kopplung + Objekt-X-Kandidatengeometrie | `ACTIVE` — nächster verbindlicher Block | 2026-08-09 |

**Freeze-Ausnahme P07:** P07 wurde nach seinem Freeze ausschließlich wegen eines neuen konkreten Cross-SYN-Gegenbefunds aus P06 G-T4/G-T5 eng begrenzt wieder geöffnet und danach in Markdown/LaTeX erneut synchron eingefroren. Dies entspricht der Migrationsregel; andere P05–P09-Blöcke wurden nicht pauschal wieder geöffnet.

---

## Block-Provenienz P05–P11

| Block | Primäre SYN-Rolle | Bindender Endstand | Provenienzstatus |
|---|---|---|---|
| P05 | relative Primkanäle, Lift-/Quell-/Gramgeometrie | gültige positive Resultate plus exakt gescopte Kanal-/Lift-No-Gos; Nichtentartung und globale Kopplung offen | `FROZEN / RECONCILED` |
| P06 | Jacobi–Feshbach, Divisorgraph, Transportgenerator | finite Identitäten und Modell-No-Gos; P06 G-T4/G-T5 korrigieren NEU-088–90 auf `D_N->1` | `FROZEN / RECONCILED` |
| P07 | Weil-Form-Statistik, Herglotz-Interface | Patch 5 bindend: `D_N->1` nur modell-/skalenspezifisch; `LFF=>Rampe` bewiesen, Umkehrung OPEN | `FROZEN / P10-RECONCILED` |
| P08 | Grenzoperator, Renormierung, Finite Part | modellrelative/conditionale Spur-/Mangoldt-Stränge; Primeclock-H1 ungewichtet No-Go; gewichteter Ersatz offen | `FROZEN / RECONCILED` |
| P09 | BC, Hochschild, geladene Kohomologie, Zyklizität | positiver geladener Hochschildpfad; kanonischer Rotations-No-Go mit expliziten Firewalls | `FROZEN / RECONCILED` |
| P10 | kondensierte No-Go-Sammlung | N01–N54 reconciliiert, N15 retired, O01–O29 offen sichtbar; Markdown/LaTeX transferauditiert | `FROZEN ✓[K/M]` |
| P11 | globale Kopplung und Objekt-X-Kandidatengeometrie | nächster aktiver Block; muss alle P10-Scope-Firewalls respektieren | `ACTIVE` |

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
| NEU-259 | P04 → P12 | finite Ebene / Grenzfront | RH-freie finite Suzuki-Operatorstruktur; globaler $a\to\infty$-Träger offen | finite Teile `INCORPORATED`, Grenzteil `OPEN` |

> Diese Tabelle ist **keine erneute Einzelinventur aller historischen NEU-Dateien**. Für P05–P10 ist der jeweilige eingefrorene SYN-Endstand samt Pass-A-/Reaudit-/Transferprovenienz die bindende Blockreferenz. P10 führt seine Negativ-/OPEN-Provenienz zusätzlich explizit in der final reconciliierten Pass-A-Matrix.

---

## Vollsynthese NEU-252–260 — PRE-C1z-Reconciliation

**Auditanker:** `audits/AUDIT-2026-08-09_P11_PRE-C1z_Vollsynthese_NEU252-260.md`, Commit `7b865770`.  
**Status:** `✓[K/M] PASS — MATHEMATICAL SYNTHESIS COMPLETE / PRE-C1z RELEASED`.

| Knoten | Bindender heutiger Befund | Provenienzstatus | SYN-Ziel |
|---|---|---|---|
| NEU-252 | vollständige hermitesche Polarisation von $B_W$; keine Positivitätsbehauptung | `INCORPORATED` ✓[K/M] | P02 |
| NEU-253 | M4-Geometrieagenda; Radikal statt isotroper Kegel als Quotientenkern | `INCORPORATED / FRAMEWORK` | P03 / P11-Firewall |
| NEU-254 | positive Hintergrundkandidaten; $R_{\rm PW}$ nur surjektiv, kanonische Sektion statt Inverser | `INCORPORATED / REFINED` | P03 |
| NEU-255 | Haar-Koisometrie, $H_0=L^2$ als Hintergrund; $B_W$ dort unbeschränkt | `INCORPORATED` ✓[K/M] | P03 |
| NEU-256 | Dilation/Kompensationsdiagnostik; isolierter Primblock nicht separat als voller No-Go verwendbar | gültige Diagnostik `INCORPORATED`; KLMN-Hoffnung `SUPERSEDED` | P03 |
| NEU-257 | $L^2$-Semibeschränktheit iff RH; unter RH $B_W$ auf Haar-$L^2$ nicht closable | `INCORPORATED` ✓[K/M], bindende Firewall | P03 FROZEN |
| NEU-258 | $B_{W,\rm NEU-252}=B_{W,\rm Lit}$; kein Normierungs-Ausweg aus 257 | `INCORPORATED` ✓[K/M] | P02/P03 |
| NEU-259 | endliche Suzuki-Ebene RH-frei konstruiert; globaler Grenzübergang offen | finite Teile `INCORPORATED`, global `OPEN` | P04 → P12 |
| NEU-260 | Arbeitsauftrag $\lambda$, $\theta/U_a$, $\phi(a,z)$, $J_{a,b}$ | `OPEN / PARTIALLY DISCHARGED` | P04/P12 |
| NEU-260a | positive Arbeitsnormalisierung; $\lambda$ topologisch gauge-artig, Spektralinvarianz nicht bewiesen | `INCORPORATED` finite Ebene / Rest `OPEN` | P04/P12 |
| NEU-260b | intrinsisches Datum ist $U_a$, nicht eine basisabhängige Winkelkoordinate; keine typisierte KMS/Frobenius-Selektion | `INCORPORATED / OPEN selection` | P04/P12 |
| NEU-260b.1 | Parität reduziert $U(1)$ auf $\{+P,-P\}\cong\mathbb Z_2$ | `INCORPORATED` ✓[K/M] | P04 |
| NEU-260b.2 | Suzuki-Grenzrelation impliziert konditional den $+P$-Zweig | `CONDITIONAL`; P04/P12-Sync offen | P12 / P04-sync |
| NEU-260c | keine physische Datei; $\phi(a,z)$-Problem nur geplant | `OPEN / PLANNED` | P12 |
| NEU-260d | keine physische Datei; $J_{a,b}$-Problem nur geplant | `OPEN / PLANNED` | P12 |

**Bindende Interpretation für P11:** P03 entscheidet den Haar-$L^2$-Endpunkt negativ, nicht die Existenz stärkerer adèlischer/relativer Geometrien. P11-C1z darf daher eine source-kanonische Geometrie vor dem vollständigen Haar-Kollaps untersuchen. Die Suzuki-Grenzfragen bleiben P12-Scope.

---

## Inventar-/ID-Sonderfälle — repo-weit verifiziert

Diese Flags betreffen die **Dokumentidentität/Provenienz**, nicht automatisch den mathematischen Status des jeweiligen Inhalts.

1. **NEU-242 — `DUPLICATE-ID`:** Unter derselben Nummer existieren zwei verschiedene Dokumente in unterschiedlichen Ordnern/Titeln. Historische Zitate müssen daher mindestens `NEU-ID + Dateipfad/Titel` angeben.
2. **NEU-251 — `UNALLOCATED / NO PHYSICAL NODE VERIFIED`:** Auf aktuellem `main` existiert keine physische NEU-251-Datei. Daraus wird kein mathematischer No-Go abgeleitet.
3. **NEU-260c,d — `PLANNED / DEFERRED → P12`:** keine physischen Dateien; nur als offene Folgeknoten in NEU-260/P04 bezeichnet.
4. **Cross-folder nodes NEU-246–250x:** Mehrere Knoten dieses Nummernbereichs liegen thematisch/physisch über `01-primkanten-werkzeuge` und `07-weil-explizitformel` verteilt. Insbesondere sind NEU-246, NEU-247, NEU-247a/b, NEU-248, NEU-249 sowie NEU-250g/i/j als cross-folder-Provenienzfälle zu behandeln. Bei solchen IDs ist der Dateipfad Teil der eindeutigen Provenienzidentität.

**Provenienzregel für Duplicate-/Cross-folder-Fälle:**

\[
\boxed{\text{NEU-ID allein ist nicht immer ein eindeutiger Dokumentbezeichner.}}
\]

---

## Offene Migrationspakete nach P10 Freeze

P05–P10 sind SYN-migriert und eingefroren. Offen sind nun:

| Block | Ziel | Status / Priorität |
|---|---|---|
| Globale Kopplung + Objekt-X-Geometrie | P11 | **nächster aktiver Block**; P10-Firewalls bindend |
| Finite-to-Infinite Weil-Geometrie | P12 | aktive Forschungsfront auf Basis P02/P04; NEU-260b.2/260c/260d zu synchronisieren |
| Survey + DAG | P00 | nach den vorigen Blöcken konsolidieren |

---

## SYN-Zielarchitektur

| ID | Arbeitstitel | Hauptsubstanz |
|---|---|---|
| P00 | Object X: Program, Architecture and Current Frontier | Survey, DAG, Status |
| P01 | BC Prime-Power Weights | bestehend |
| P02 | Adelic Weil Amplitude Port | **FROZEN** |
| P03 | Haar-$L^2$ Firewall | **FROZEN** |
| P04 | Finite Weil Geometry and Suzuki Extensions | bestehend; NEU-260b.2-Sync offen |
| P05 | Relative Prime Channels and Arithmetic Edge Geometry | **FROZEN** |
| P06 | Jacobi–Feshbach and Divisor-Graph Approaches | **FROZEN** |
| P07 | Weil Form, Statistics and RH-Equivalent Positivity Criteria | **FROZEN / P10-RECONCILED** |
| P08 | Renormalized Prime Operators and Finite-Part Structures | **FROZEN** |
| P09 | Bost–Connes and Hochschild Structures | **FROZEN** |
| P10 | No-Go Theorems for Canonical Global Coupling | **FROZEN** |
| P11 | Global Coupling and the Object-X Candidate Geometry | **ACTIVE NEXT** — $B_{pq}$, globale Gramkopplung, Objekt-X-Axiome |
| P12 | Finite-to-Infinite Weil Geometry | $J_{a,b}$, $\phi(a,z)$, $a\to\infty$, NEU-260b.2 conditional selection |

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