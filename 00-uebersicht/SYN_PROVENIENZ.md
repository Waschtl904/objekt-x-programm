# SYN-Provenienzmatrix

**Stand:** 2026-08-08  
**Zweck:** Jeder NEU-Knoten hat genau einen aktuellen Zustand und eine SYN-Zuweisung. Keine NEU-Datei wird gelöscht; diese Matrix ersetzt das manuelle Durchsuchen.

**Knotenstatuskategorien** (beschreiben den Zustand eines Forschungsknotens):
- `INCORPORATED` — gültige Mathematik, im SYN-Paper übernommen
- `NO-GO` — negatives Resultat, im SYN-Paper dokumentiert
- `SUPERSEDED` — durch späteren Knoten ersetzt (Nachfolger angegeben)
- `AUDIT-ONLY` — historischer Fehler-/Auditweg, kein mathematischer Inhalt
- `OPEN` — aktive Forschungsfrage

**Dokumentstatus** (beschreiben den Zustand eines SYN-Papers/Blocks, getrennt von Knotenstatuskategorien):
- `FROZEN ✓[K/M]` — endgültig eingefroren, kein weiterer mathematischer Re-Audit erforderlich
- `CANDIDATE` — Freeze-Kandidat, letzter Cleanup ausstehend
- `ACTIVE` — in aktiver Revision

---

## Kanonische Definitionen (alle in P02, §1–§6)

> Fourier-Konvention, $P_{\text{Haar}}$, $R_{\text{PW}}$, $C_{a,b}$, $g_{a,b}$, $h_{a,b}$, $\gamma_\infty$, $\Lambda_\Gamma$, $B_W$ — **alle kanonisch in P02 definiert** (§1–§6). Andere Papers verweisen auf P02 und geben höchstens Erinnerungen.

---

## Dokumentstatus

| Dokument | Patch | Dokumentstatus | Datum |
|---|---|---|---|
| P02 | Patch 3.5 | `FROZEN ✓[K/M]` | 2026-08-08 |
| P03 | Sync Patch 3 | `FROZEN ✓[K/M]` | 2026-08-08 |

---

## Provenienz-Tabelle

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
| NEU-258 (Patch 1) | P02 | §6 (\texttt{thm:lit-id}) | Literaturidentifikation $B_{W,\text{NEU-252}}=B_{W,\text{Lit}}$ | `INCORPORATED` ✓[K/M] |
| NEU-259 | P03/P12? | — | RH-freie $\mathcal{H}_W$-Konstruktion | `OPEN` ?[O] |

---

## Offene Migrationspakete (nach P02/P03 Freeze)

Diese Blöcke sind noch nicht SYN-migriert. Priorität nach Abhängigkeitstiefe:

| Block | Ordner | Geschätzter SYN-Ziel | Priorität |
|---|---|---|---|
| Weil-Form-Statistik | `03-weil-form-statistik` | P07 | hoch (abhängig von P02) |
| Weil-Explizitformel (Rest) | `07-weil-explizitformel` | P03/P07 | hoch |
| Primkanten-Werkzeuge | `01-primkanten-werkzeuge` | P05 | mittel |
| Jacobi-Limes | `02-jacobi-limes` | P06 | mittel |
| Grenzoperator-Renormierung | `04-grenzoperator-renormierung` | P08 | mittel |
| Primkanal-Fourierladung | `05-primkanal-fourierladung` | P05/P06 | mittel |
| Hochschild-BC-Algebra | `06-hochschild-bc-algebra` | P09 | niedrig |

---

## SYN-Zielarchitektur (Entwurf, ~13 Papers)

| ID | Arbeitstitel | Hauptsubstanz |
|---|---|---|
| P00 | Object X: Program, Architecture and Current Frontier | Survey, DAG, Status |
| P01 | BC Prime-Power Weights | bestehend |
| P02 | Adelic Weil Amplitude Port | **FROZEN** (Patch 3.5) |
| P03 | Haar-$L^2$ Firewall | **FROZEN** (Sync Patch 3) |
| P04 | Finite Weil Geometry and Suzuki Extensions | bestehend |
| P05 | Relative Prime Channels and Arithmetic Edge Geometry | Primkanten, Fourier-/Mangoldt-Gewichte |
| P06 | Jacobi–Feshbach and Divisor-Graph Approaches | Jacobi-Limes, Feshbach |
| P07 | Weil Form, Statistics and RH-Equivalent Positivity Criteria | Weilstatistik, RH-Äquivalenzen |
| P08 | Renormalized Prime Operators and Finite-Part Structures | Renormierung, Grenzoperatoren |
| P09 | Bost–Connes and Hochschild Structures | HH², BC-Strang |
| P10 | No-Go Theorems for Canonical Global Coupling | strukturelle Ausschlüsse gesammelt |
| P11 | Global Coupling and the Object-X Candidate Geometry | $B_{pq}$, Objekt-X-Axiome |
| P12 | Finite-to-Infinite Weil Geometry | $J_{a,b}$, $a\to\infty$, aktive Forschungsfront |

---

## Migrationsregel

Ein NEU-Block gilt als **eingefroren**, sobald:
1. Alle gültigen Aussagen in einem SYN-Paper erscheinen
2. Jeder Knoten in dieser Tabelle eine Status-Zeile hat
3. Das SYN-Paper ein SYN-Direktaudit bestanden hat

Danach muss der Block im normalen Forschungsalltag nicht mehr gelesen werden.

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, 2026-08-08.*