# SYN-Migrationsprotokoll

**Stand:** 2026-08-09  
**Zweck:** Verbindliche Regel für die schrittweise Überführung von NEU-Knoten in SYN-Papers.

---

## Kernregel (unverhandelbar)

> **Kein Satz ins SYN, solange sein Audit-/Korrekturstatus nicht eindeutig ist.**

Das bedeutet konkret: Jede Aussage, die in ein SYN-Paper übernommen wird, muss einen der fünf Status-Tags aus `SYN_PROVENIENZ.md` tragen. Unklar = nicht migrieren.

---

## Was ein SYN-Block erfordert

Für jeden Themenblock werden gleichzeitig berücksichtigt:

1. Der ursprüngliche NEU-Knoten
2. Spätere Patches und Korrekturen
3. Die zugehörigen Direktaudits
4. Spätere Knoten, die eine Aussage widerlegt oder ersetzt haben
5. Aktuelle Statusbuchungen: `✓[M]`, `×[M]`, `✓[M]_neg`, `?[O]`
6. Die heute gültigen kanonischen Definitionen und Normierungen (Quelle: P02)

Erst aus dieser Zusammenschau entsteht der **gültige mathematische Endstand**, der ins SYN-Paper übernommen wird.

---

## Migrationsfluss

```text
NEU-Knoten
+ Audits
+ Patches
+ spätere Korrekturen
        ↓
gültiger mathematischer Endstand
        ↓
SYN-Paper (nur dieser Stand)
        ↓
SYN-Direktaudit
        ↓
Provenienzmatrix schließen
        ↓
Block eingefroren
```

Wenn beim SYN-Schreiben ein neuer Widerspruch entdeckt wird:

```text
Migration stoppen
    ↓
Fehler auditieren
    ↓
korrigieren / gezielt reconciliieren
    ↓
erst dann SYN freigeben
```

---

## Was mit fehlerhaften historischen Knoten passiert

Ein fehlerhafter historischer Knoten wird **nicht** umgeschrieben. Er bleibt als historischer Zustand im Laborbuch und erhält in der Provenienzmatrix den Tag `SUPERSEDED` oder `AUDIT-ONLY` mit Verweis auf den korrigierenden Patch/Reaudit.

**Beispiel aus der Praxis (2026-08-08):**

| Knoten | Alter Zustand | Urteil | Korrigierender Knoten |
|---|---|---|---|
| NEU-258 (vor Patch 1) | $B_\Gamma(a,a)=\int|\hat a|^2\operatorname{Re}\gamma_\infty\,dt$ (ohne $1/\pi$) | `SUPERSEDED` | NEU-258 Patch 1 |
| NEU-257 (vor Patch 3) | $\Gamma$ = positive Ordinaten | `SUPERSEDED` | NEU-257 Patch 3 |
| NEU-257 (vor Patch 2) | `(2-DiffOther)`: $1/n$-Vorfaktor falsch | `SUPERSEDED` | NEU-257 Patch 2 |

Das SYN-Paper übernimmt nur die korrigierten Fassungen.

---

## Warum kein blinder Mega-Durchlauf

Eine Aktion „300 Dateien → 10 Papers“ ohne Einzelkontrolle birgt drei Risiken:

- **Fehlerübernahme**: Ein alter `×[M]`-Knoten wird versehentlich als gültiges Resultat eingebaut.
- **Provenienzverlust**: Die Herkunft einer Aussage wird nicht eingetragen; später nicht mehr nachvollziehbar.
- **Konventionsdrift**: Zwei verschiedene Normierungen (z. B. $\gamma_\infty$ mit und ohne $1/2$-Faktor) werden gemischt.

Ein KI-Agent kann sehr viel mechanische Arbeit übernehmen (Dateien lesen, Querverweise einsammeln, LaTeX anlegen, Provenienz eintragen, Commits pushen). Die mathematische Entscheidung „Was ist gültig, was superseded, was No-Go, was offen?“ bleibt aber blockweise unter Kontrolle.

---

## Arbeitsgeschwindigkeit

Die SYN-Migration sollte **wesentlich schneller** gehen als die ursprünglichen Audits, weil:

- Bereits auditierte Blöcke müssen nicht mathematisch neu geprüft werden.
- Jeder Block liefert ein SYN-Direktaudit, kein Einzel-Audit pro Knoten.
- Die kanonischen Definitionen stehen bereits (P02).
- `SYN_PROVENIENZ.md` sorgt für Vollständigkeit ohne manuelles Durchsuchen.

Grobe Erwartung: 300–400 Knoten → 10–15 Blöcke → 10–15 SYN-Papers.

---

## Blockplan

| Reihenfolge | Block | Geschätzter SYN | Voraussetzung |
|---|---|---|---|
| 1 | P02 Re-Audit | P02 final | P02 Patch 3.2 |
| 2 | P03 eingefroren | P03 final | P03 Re-Audit Patch 1 |
| 3 | Weilstatistik / RH-Äquivalenzen | P07 | P02 final |
| 4 | Primkanten + Fourier-Ladung | P05 | unabhängig |
| 5 | Jacobi–Feshbach + Divisorgraph | P06 | unabhängig |
| 6 | Grenzoperator + Renormierung | P08 | P02, P05 |
| 7 | BC + Hochschild | P09 | P01 |
| 8 | No-Go-Sammlung | P10 | P05–P09 + eindeutige Negativ-/OPEN-Reconciliation |
| 9 | Globale Kopplung + Objekt-X | P11 | P05–P10 |
| 10 | Finite-to-Infinite Weil | P12 | P02, P04 |
| 11 | Survey + DAG | P00 | alle vorigen |

---

## Aktueller Migrationsstand — 9. August 2026

| SYN | Status | Bemerkung |
|---|---|---|
| P05 | `SYN FROZEN ✓[K/M]` | Primkanten + Fourier-Ladung abgeschlossen |
| P06 | `SYN FROZEN ✓[K/M]` | Jacobi–Feshbach + Divisorgraph abgeschlossen; LaTeX-Transferaudit `1b1a7173`; G-T4/G-T5 bindend |
| P07 | `SYN FROZEN ✓[K/M]` | Weil-Form Statistics abgeschlossen; nach P10-Cross-SYN-Reaudit eng begrenzt als Patch 5 synchronisiert und wieder eingefroren |
| P08 | `SYN FROZEN ✓[K/M]` | Grenzoperator + Renormierung abgeschlossen; Markdown-Finalcommit `31c93d50`, LaTeX `d283c34c`, Transferaudit `3f12e0ef` |
| P09 | `SYN FROZEN ✓[K/M]` | BC + Hochschild abgeschlossen; Pass-A-Seal `28b5cba5`, Markdown-Finalcommit `8346733e`, LaTeX `26f9d60e`, Transferaudit `e724b5a7` |
| **P10** | **`SYN FROZEN ✓[K/M]`** | Pass-A Seal `b8be0d6f`; Markdown `d307654c`; LaTeX `bc42bdff`; FINAL SEAL `449f361e` |
| **P11** | **NÄCHSTER AKTIVER BLOCK** | globale Kopplung + Objekt-X-Kandidatengeometrie; P10-Firewalls bindend |

P05–P10 werden nicht erneut geöffnet, sofern kein neuer konkreter mathematischer Gegenbefund gegen ihren eingefrorenen Endstand auftaucht. Die P07-Wiederöffnung im P10-Pass war genau eine solche eng begrenzte Ausnahme und ist abgeschlossen.

Verbindlicher nächster Arbeitsschritt ist damit **P11 — Global Coupling and the Object-X Candidate Geometry**.

Für P11 gelten insbesondere die aus P10 eingefrorenen Firewalls:

- lokale Primfaser-Realisierungen dürfen nicht als globaler Hilbert–Pólya-Endoperator ausgegeben werden;
- endliche Feshbachidentitäten dürfen nicht als globale Schatten-/Fredholm-Grenztheorie behandelt werden;
- der NEU-088–90-Determinantenkollaps `D_N->1` darf nicht auf andere Determinanten-/Fredholmarchitekturen ausgedehnt werden;
- `OPEN`/`CONDITIONAL` darf nicht als negatives Resultat umgedeutet werden;
- `P10-N15` bleibt retired und `P10-O29` OPEN;
- P09-Unit-Slot- und Standard-SAYD-No-Gos dürfen nicht auf nichtkanonische, andere Koeffizienten- oder Weil-/Gamma-korrigierte Konstruktionen ausgedehnt werden.

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, 2026-08-09.*