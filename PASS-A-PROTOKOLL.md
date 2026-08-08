# Pass-A-Protokoll — SYN-Migrationsverfahren

**Erstellt:** 8. August 2026 | **Zuletzt aktualisiert:** 8. August 2026 (Gruppe F2: Eröffnungsmatrix NEU-151–173)

Dieses Dokument fixiert das verbindliche Verfahren für die Pass-A-Phase der SYN-Migration.

---

## Grundsatz

$$
\text{Knoten} + \text{vorhandene Audits} + \text{Patches} + \text{spätere Korrekturen}
\;\longrightarrow\;
\text{heute gültiger Endstand}
\;\longrightarrow\;
\text{SYN}
$$

Maximale Wiederverwendung des Auditbestands. Neuer mathematischer Aufwand nur wo:
- **Audit fehlt**, oder
- **Audit und heutiger Stand kollidieren**.

---

## Feste Pass-A-Regel: Auditsuche zuerst

Vor jedem Batch:
1. Vorhandene Audit-Dateien suchen (`ARCHIV-AUDIT-*`, `AUDITSTAND-*`, `ZWISCHENBILANZ-*`, `audits/`)
2. Spätere Korrekturknoten im Themenblock prüfen
3. Prüfart bestimmen
4. Nur bei `NEW-DIRECT-AUDIT` oder `TARGETED-REAUDIT` neuen mathematischen Aufwand anlegen

---

## Prüfart-Taxonomie

| Kürzel | Bedeutung | Aufwand |
|--------|-----------|----------|
| `AUDIT-REUSED` | Bestehender Audit übernommen; kein Widerspruch | Niedrig |
| `AUDIT-RECONCILED` | Mehrere Audits/Patches zu Endstand vereinigt | Mittel |
| `TARGETED-REAUDIT` | Widerspruch/Lücke isoliert; nur betroffene Aussage neu geprüft | Mittel |
| `NEW-DIRECT-AUDIT` | Kein brauchbarer Audit vorhanden; erstmals vollständig geprüft | Hoch |

---

## Gruppenregister

### Gruppe A — NEU-091–092

| Knoten | Prüfart | Endstatus |
|--------|----------|-----------|
| NEU-091 | `NEW-DIRECT-AUDIT` | INCORPORATED |
| NEU-092 | `NEW-DIRECT-AUDIT` | INCORPORATED |

---

### Gruppe B — NEU-093–100

| Knoten | Prüfart | Endstatus | Kernbefund |
|--------|----------|-----------|------------|
| NEU-093 | `AUDIT-REUSED` | INCORPORATED | Bochner-Lift; Mangoldt-Autokorrelation als positiv-definiter Kern |
| NEU-094 | `AUDIT-REUSED` | INCORPORATED | Bochner-Tor; logarithmische Korrelationskerne typisiert |
| NEU-095 | `AUDIT-REUSED` | INCORPORATED | Fensterregularisierung und Autokorrelationsdiagnose |
| NEU-096 | `AUDIT-REUSED` | INCORPORATED | Skalenanalyse Mangoldt; selbstduale Skala |
| NEU-097 | `AUDIT-REUSED` | INCORPORATED | Zwischenregime; selbstdualer Übergang |
| NEU-098 | `AUDIT-RECONCILED` | INCORPORATED + ✓[M]$_\rm neg$ | Hardy–Littlewood konditional; Singulärserien-Hauptterm ✓[M]; zwei lokale SUPERSEDED-Schritte |
| NEU-099 | `AUDIT-REUSED` | INCORPORATED | Singulärserien-Schicht; Shift-Feinstruktur |
| NEU-100 | `AUDIT-REUSED` | INCORPORATED | Restdichte $\Delta_N$; Übergang zum Shift-Spektrum |

---

### Gruppe C — NEU-101–110

**Abgeschlossen:** 8. August 2026 | **Commits:** Patches 1–5 (d5644669 → edc4fa53)

| Knoten | Prüfart | Endstatus | Kernbefund |
|--------|----------|-----------|-----------|
| NEU-101 | `AUDIT-RECONCILED` + `TARGETED-REAUDIT` | `SUPERSEDED(A,B,C)` + `OPEN(D)` | GM-Normierung $H\log(M/H)$; Transferlemma ?[O] |
| NEU-102 | `AUDIT-RECONCILED` | `SUPERSEDED(A)` + `INCORPORATED(B,F)` + `OPEN(D,E)` | $L^2$-Integrabilitätsfehler; No-Go (B) unabhängig gültig |
| NEU-103 | `AUDIT-REUSED` | `INCORPORATED` | Entfaltungskarte unabhängig von 101/102-Fehlern |
| NEU-104 | `AUDIT-RECONCILED` + `TARGETED-REAUDIT` | `INCORPORATED` ✓[M]$_\rm part$ | No-Go abstrakt korrekt; $\mathcal{S}_{N,H}$ SUPERSEDED |
| NEU-105 | `AUDIT-REUSED` | `INCORPORATED` | Binärer Falsifizierbarkeitssatz gültig |
| NEU-106 | `AUDIT-REUSED` | `INCORPORATED(1,2,5)` + `OPEN(heuristisch)` | Epistemische Trennung RH $\not\Rightarrow$ GUE |
| NEU-107 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | 107.2 Biimplikation → Einwegimplikation; 107.5 Normierung |
| NEU-108 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | 108.4 No-Go → Typisierungswarnung |
| NEU-109 | `AUDIT-REUSED` | `INCORPORATED(109.1,3)` + `OPEN(109.2,A,B)` | Wegabelung methodisch sauber |
| NEU-110 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | 110.2–3 $\times$[M]→?[O]; Ausgang A/B offen |

---

### Gruppe D — NEU-111–112

**Abgeschlossen:** 8. August 2026 | **Commits:** D-1/2 `43a0fa2b`, D-2/2 `4f12c65f`

| Knoten | Prüfart | Endstatus | Kernbefund |
|--------|----------|-----------|-----------|
| NEU-111 | `NEW-DIRECT-AUDIT` | `PATCH ANGEWENDET` | Ausgangs-B SUPERSEDED; signed-$\Gamma$+$m_\gamma$; $m_{\Omega,N}$ erst in 119 definiert; Jacobi-No-Go → Firewall |
| NEU-112 | `NEW-DIRECT-AUDIT` | `PATCH ANGEWENDET` / teilweise SUPERSEDED durch NEU-113 | $\mu_{\rm arith}=\sum m_\gamma\delta_\gamma$; Autokorrelationslift; Doppelzählung; 112.4 retypisiert |

---

### Gruppe E — NEU-113–120

**Abgeschlossen:** 8. August 2026 | **Commits:** E-1/6 `78b06719` → E-6/6 `904eb29b`

| Knoten | Prüfart | Endstatus | Kernbefund |
|--------|----------|-----------|-----------|
| NEU-113 | `AUDIT-RECONCILED` | `PATCH ANGEWENDET` / **SUPERSEDED BY P02** | Mellin-Zentrierung $x^{-1/2}$; Doppelzählung; $W_\xi^{\rm norm}=W_{\rm zeros}$ |
| NEU-114 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | $m_{\rm arith}=\Pi_\gamma(X)$ von ✓[M] auf ?[O] |
| NEU-115 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | Vierteilige Summe → $W_\xi^{\rm norm}=W_{\rm zeros}$; Interface-Firewall ✓[M] |
| NEU-116 | `AUDIT-REUSED` | `INCORPORATED`$_\rm part$ + **→ P10/P11** | $W_{\rm res}^{\rm top}\stackrel?=W_\xi^{\rm norm}$: ?[O]; lokale Faktoren → BC-Strang |
| NEU-117 | `AUDIT-REUSED` | `INCORPORATED`$_\rm part$ + **→ P10/P11** | $\operatorname{Aut}(\mathbb N,\cdot)\cong\operatorname{Sym}(\mathbb P)$: ✓[M]; globale Rigidität konditional |
| NEU-118 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` / teilweise SUPERSEDED durch NEU-119/P02 | $\mu_{\rm arith}$ (Maß) vs $m_{\rm arith}(z)$ (Funktion) Typfehler; Gamma-/Pol-Anteile $\times$[M] |
| NEU-119 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | Selbstadjungiertheit ?[O]; Eigenvektor-Cond. $\times$[M]; O3 Gamma $\times$[M] SUPERSEDED |
| NEU-120 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | 4$\times$ $\times$[M] gestrichen; Firewall ?[O]; vague Konvergenz eingebracht |

---

## $$\boxed{\text{NEU-091–120: PASS A COMPLETE}}$$

**Datum:** 8. August 2026

Alle 30 Knoten bereinigt. Methodennachweis: 30 Knoten + vorhandene Audits $\longrightarrow$ Pass-A ohne Vollneuaudit.

---

## P07 — SYN-Freigabe

**LaTeX-Fassung:** `papers/P07_Weil_Form_Statistics.tex`  
**Basis:** `papers/P07_Weil_Form_Statistics.md` — `SYN FINAL AUDITED`, Commit `6a162f92`; synchronisiert mit NEU-101 Patch 3, Commit `92d731d1`  
**Knotenbasis:** NEU-091–120 / `PASS A COMPLETE`  
**Prüfart:** LaTeX-SYN-Transferaudit; kein Vollneuaudit der 30 Forschungsknoten  
**Ergebnis:** `SYN FROZEN ✓[K/M]`

Geprüft wurden ausschließlich `.md` ↔ `.tex`, Formeltranskription,
Fourier-/Mellin-Konventionen, Satzstatus, Definition-vs.-Hypothese-vs.-Open-Problem,
Referenzen, Labels, Doppelzählungen, unzulässige Hochstufungen von
`OPEN/CONDITIONAL` und LaTeX-Kompilierbarkeit.

**Auditbefund:** kein neuer mathematischer Konflikt; kein NEU-Knoten wieder geöffnet.

---

## Nächste Batch-Reihenfolge

> **Wichtiger Hinweis zur Systematik:** Die Gruppen F, G, H, … folgen **nicht** der
> historischen NEU-Nummerierung, sondern der thematischen Abhängigkeitsreihenfolge
> gemäß `00-uebersicht/SYN_MIGRATIONSPROTOKOLL.md`. NEU-Nummern und Themenordner
> sind nicht mehr deckungsgleich; viele spätere Knoten gehören rückwirkend zu
> früheren Themen. Maximale Wiederverwendung vorhandener Audits gilt in jedem Batch.

| Gruppe | SYN-Ziel | Quellbestand | Reihenfolge |
|--------|----------|--------------|-------------|
| **F** | **P05** | `01-primkanten-werkzeuge/` + relevante Knoten aus `05-primkanal-fourierladung/` | **aktiv** |
| G | P06 | `02-jacobi-limes/` + zugehörige Jacobi-/Feshbach-Knoten | nach F |
| H | P08 | `04-grenzoperator-renormierung/` + zugehörige Renormierungs-/Grenzoperator-Knoten | nach G |
| I | P09 | `06-hochschild-bc-algebra/` + BC-relevante Quellen | nach H |
| … | P10/P11/P12 | repo-weite thematische Pakete | nach Abhängigkeiten |
| Abschluss | **P00** | `00-grundlegung/` + Gesamt-DAG + alle SYN-Endstände | **zuletzt** |

---

## Gruppe F — P05: Relative Primkanten und arithmetische Kantengeometrie

**Status:** aktiv | Bestandsaufnahme abgeschlossen | **F1 abgeschlossen** | **F2 eröffnet** | F3–F4 ausständig

### Hauptbefund der Bestandsaufnahme

Für P05 ist **kein neuer Vollaudit** erforderlich. Der Großteil des Quellbestands in
`01-primkanten-werkzeuge/` und `05-primkanal-fourierladung/` wurde im früheren
Gesamtdurchlauf bereits auditiert. Die neue Arbeit besteht überwiegend aus Reconciliation;
bei einer konkreten Kollision greift gezielt `TARGETED-REAUDIT`.

**Schlüsselbeobachtung Ordner 05:** Kein Grund für `NEW-DIRECT-AUDIT`.
Endanker sind NEU-170d (bereinigter DAG-Audit) und NEU-173 (abgeschlossener
Typquellenpfad, epistemische Korrektur C₂ → C_src-neg).

**Schlüsselbeobachtung Ordner 01:** Thematisch zu zerlegen.
Nur ein Teil gehört nach P05; NEU-010–25 → primär P09/P05-Referenz;
NEU-26–56 teils P06/P10; NEU-229–249 teils P09/P11.

### Paketstruktur Gruppe F

#### F1 — Historische Primkantenbasis — **ABGESCHLOSSEN** (Commit `07903f85`)

**Quellknoten:** NEU-039–045 + 44-Familie (44, 44X, 44X′, 44R)  
**Korrekturquellen:** NEU-151–155, NEU-226/227, Gegenlese-Commit `eae87a62`, NEU-250f Patch 1 (`1579a379`)  
**Prüfart:** überwiegend `AUDIT-RECONCILED`; ein neu entdeckter Typkonflikt → `TARGETED-REAUDIT` (NEU-250f)

| Knoten | Prüfart | Endstatus für P05 | Heute gültiger Kernbefund |
|--------|----------|-------------------|---------------------------|
| NEU-039 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Endlicher abstrakter Euler-Primoperator und $-\partial_\beta\log\det(1-\mathcal P_N)=\zeta_N'/\zeta_N$ algebraisch gültig; intrinsische `Wres`/$L_3^\circ$-Normalisierung nicht nachgewiesen |
| NEU-040 | `AUDIT-RECONCILED` | `INCORPORATED_part` + **→ P06** | Schur-Komplement-Identitäten formal gültig bei typisierten Blöcken; kanonischer `Wres`-Koppler und $z$–$\beta$-Intertwining offen |
| NEU-041 | `AUDIT-RECONCILED` | `INCORPORATED_part` + `OPEN` | Basisformel für $\widetilde\omega_2$ und Nullmodus-Obstruktion gültig; Kopplungsoperator nur relativ zu Hebungswahl; Hebungsabstieg/-unabhängigkeit offen; `C_pC_p^\#` nicht automatisch Projektor |
| NEU-042 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Resolvent/Laplace-Trennung ✓[M]; relativer Log-Zuwachs $\log(pm)-\log m=\log p$ ✓[M]; $L_3^\circ$-spezifische Kanalrealisierung nicht unbedingter Satz |
| NEU-043 | `AUDIT-RECONCILED` | `INCORPORATED_part` + `OPEN` | Edge-gelabelte $p$-Reinheit im ausdrücklich definierten Graphraum; Reinheit nach Kollaps nicht automatisch; induzierte `Wres`-Kantendiagonalität offen |
| NEU-044 (pq-Test) | `AUDIT-RECONCILED` | `INCORPORATED` + ✓[M]$_\rm neg$ | Kollaps löscht Primkantenlabel; keine automatische Kantendiagonalität/kein funktoriell eindeutiger relativer Clock im kollabierten Raum |
| NEU-044 (Normierungsblatt) | `AUDIT-RECONCILED` | `AUDIT-ONLY / DEFINITION` | Kanonische Quellenrekonstruktion und Normkonvention; ausdrücklich kein mathematisches Herkunftsresultat |
| NEU-044X | `AUDIT-RECONCILED` | `INCORPORATED_part` | Im gewählten eindimensionalen induzierten Modell Rang $\le1$; intrinsisches Nichtverschwinden $c_p\ne0$ nicht bewiesen |
| NEU-044X′ | `AUDIT-RECONCILED` | `CONDITIONAL` | Rangstabilität unter skalaren normkonvergenten Grenzwerten; uniformer endlicher Rang unter Gram-Triage nur plausibel/bedingt |
| NEU-044R | `AUDIT-RECONCILED` | `SUPERSEDED_part / CONDITIONAL` | Spurklassen-Rückbindung nur unter Rang-/Gewichtsannahmen; NEU-152/153 verhindern unbedingte Lesart |
| NEU-045 | `AUDIT-RECONCILED` | `INCORPORATED_part` + **→ P06** | Euler-Unterdeterminante gültig; Feshbach-Geometrie nicht intrinsisch gesichert; globale Überlappung und Spektralmaßform → NEU-226/227 |

**F1-Kernfirewalls für P05** (verbindlich für alle späteren F-Pakete):

1. $T_p \ne C_p^{[\widehat\varepsilon_p]} \ne C_p^{\rm rel}[\widehat\varepsilon_p]$ — drei Typen stets trennen.
2. $|c_p|^2$ ohne Hebungsabstieg/-unabhängigkeit kein intrinsisches Primgewicht.
3. Kantendiagonalität der quellseitig induzierten `Wres`-Paarung ist offen; definitorische Orthogonalität zählt nicht.
4. Primkanalbilder können sich überlappen; Off-Diagonalität folgt nicht automatisch.
5. Historische $D_{\rm rel}$-Eigenbasisformeln durch Spektralmaßform aus NEU-227 ersetzen.

**Neu entdeckter Konflikt:** NEU-250f Typfehler ($L_3\in C^4 \not\Rightarrow L_3^\circ\in F^3A$ ohne Realisierungsbrücke); unbedingter No-Go `SUPERSEDED`; korrigiert in Commit `1579a379`.

$$\boxed{\text{F1 PASS A COMPLETE}}$$

---

#### F2 — Fourier-/Rohkopplungsstrang (Ordner 05) — **ERÖFFNET**

**Quellknoten:** 33 Dateien, NEU-151 bis NEU-173 inkl. aller Unterknoten  
**Endanker:** NEU-170d (`AUDIT-REUSED`) + NEU-173 (`AUDIT-REUSED`)  
**Verbindliche Voraussetzung:** F1-Kernfirewalls gelten auch hier

##### Buchhaltungsbefund: DUPLICATE-ID NEU-166b

> **NEU-166b ist doppelt vergeben.** Im Repo existieren zwei inhaltlich verschiedene
> Dateien unter dieser Nummer:
>
> | Interne F2-Bezeichnung | Dateiname | Rolle |
> |------------------------|-----------|-------|
> | **166b-P** | `NEU-166b_Rollen_Provenienzentscheidung_Rp_Tp.md` | älteres methodisches Entscheidungs-/Provenienzblatt; friert zulässige Leserichtung ein; eigentliche Rollenentscheidung noch ?[O] |
> | **166b-T** | `NEU-166b_Typ_Domaenen_Deszentaudit_Tp_Fallverzweigung.md` | inhaltlich weiter entwickelt; Fall 2 ausgeschlossen; Fall 3a lokal/modenweise bestätigt; globale Entscheidung zwischen Fall 1, 3b, 4 offen |
>
> **Behandlung:** Keine historische Datei wird umbenannt. Für die SYN-Migration gilt:
> - **166b-T hat substanziellen Vorrang** für den mathematischen Endstand (präzisere Fallentscheidung).
> - **166b-P bleibt als Audit-/Provenienz-Firewall** erhalten (enthält weiterhin gültige Auditregeln, insbes. Verbot der nachträglichen Umdeklaration postulierter $R_{p,j}$ oder $T_p$ als Quellenkonstruktionen).
> - Kein SYN-Satz der Form „NEU-166b beweist …“ ist zulässig ohne Angabe, welche der beiden Dateien gemeint ist.
> - Status: `DUPLICATE-ID / 166b-T RECONCILED / 166b-P AUDIT-FIREWALL`

##### Prüfartmatrix NEU-151–173

| Knoten | Prüfart | Endstatus für P05 | Kernbefund / Firewall |
|--------|----------|-------------------|----------------------|
| NEU-151 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Normalisierungs-Typaudit Primkanaloperatoren; $T_p$-Typisierung gesichert; intrinsische Positivität nicht nachgewiesen |
| NEU-152 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Nichtentartung Primkanalgewichte: Kriterium gültig **konditional** auf Liftunabhängigkeit; Liftunabhängigkeit selbst offen |
| NEU-153 | `AUDIT-RECONCILED` | `CONDITIONAL` | Hebungsunabhängigkeit: behauptete intrinsische Liftunabhängigkeit zurückgenommen; Ergebnis nur unter Modellbedingungen gültig |
| NEU-154 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Pullback-Kern und Reichweite der Liftform; Strukturaussagen gültig; Rang-1-Anspruch an $T_p$ durch F1-Firewall 1 blockiert |
| NEU-155 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Rohkopplung $T_p$, Primkanalkompression, Rang-1-Erweiterung: drei Typen strikt getrennt (F1-Firewall 1 bestätigt) |
| NEU-156 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Verbundene Restspurform: Rekonstruktion und Eindeutigkeit gültig; globale Wres-Normierung offen |
| NEU-157 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Zulässigkeitsraum Rohkopplung; Nichttrivialität: Existenzaussage gültig; kanonische Zeugenroute durch 167b geschlossen |
| NEU-158 | `AUDIT-RECONCILED` | `INCORPORATED` | Invariante Formen, Rohkopplungsquotient, Symmetrieeindeutigkeit: ✓[M] ohne ausstehende Korrekturen |
| NEU-159 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Dualzeuge, Projektionsnichtvernichtung, Liftzulässigkeit: Dualzeuge-Existenz gültig; automatische Liftzulässigkeit nicht bewiesen |
| NEU-160 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Rohkopplungsquotient-Symmetrieabstieg: Abstieg im Quotientenraum gültig; globale Symmetriegruppe offen |
| NEU-161 | `AUDIT-RECONCILED` | `CONDITIONAL` | Nichttriviale Fourierladung $L_3^\circ$: Existenz nur im Testmodell; F1-Firewall ($L_3^\circ\in F^3A$ ?[O]) greifen hier direkt |
| NEU-162 | `AUDIT-RECONCILED` | `CONDITIONAL` | Quantorentest $L_3^\circ = e_1 V_1$: konditional im Einmodenmodell; globale Herkunft nicht gesichert (NEU-170d) |
| NEU-163 | `AUDIT-RECONCILED` | `CONDITIONAL` | Einmodenzeuge, Liftmitgliedschaft, Nichtnullkante: algebraisch rechenbar im Testmodell; Herkunft $[L_3]\mapsto L_3^\circ = e_1 V_1$ blockiert (NEU-170d) |
| NEU-164 | `AUDIT-RECONCILED` | `CONDITIONAL` | $R_p$-Test, kanonischer Zeuge, Entscheidungsknoten: konditional; Zielkanten-Nichtverschwinden nicht bewiesen (NEU-170d) |
| NEU-165 | `AUDIT-RECONCILED` | `INCORPORATED_part` | $R_p$-Wirkung, Matrixstruktur, Basisnullmengen, gemeinsamer Kern: Matrixstruktur gültig; Kernzeugenroute durch 167b geschlossen |
| NEU-165a | `AUDIT-REUSED` | `INCORPORATED` | Quellenregister $R_p$-Operatoren: Quellenlage bestätigt, kein Widerspruch |
| NEU-165b | `AUDIT-RECONCILED` | `INCORPORATED` | Konsistenzaudit $R_p$ vs. NEU-157: Konsistenz ✓[M]; falsche Kernzeugenroute ausgeschlossen |
| NEU-166 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Einmoden-/Zweimoden-Test, Zeugen: Test-Resultate gültig; Zeugenroute $k\in\ker C_p\setminus\ker T_p$ nicht typkorrekt geschlossen (durch 166a/b-T bestätigt) |
| NEU-166a | `AUDIT-RECONCILED` | `INCORPORATED` | Typ-Domänen-Deszentaudit $T_p$: Deszentstruktur ✓[M]; Auditregeln verbindlich |
| **NEU-166b-P** | `AUDIT-FIREWALL` | `METHODISCH ERHALTEN` | Rollen-/Provenienzentscheidung $R_p$/$T_p$: Leserichtung eingefroren; Verbot nachträglicher Umdeklaration als Quellenkonstruktion; Rollenentscheidung ?[O] |
| **NEU-166b-T** | `AUDIT-RECONCILED` | `INCORPORATED_part` | Typ-Domänen-Deszentaudit $T_p$ Fallverzweigung: Fall 2 ausgeschlossen ✓[M]; Fall 3a lokal/modenweise ✓[M]$_\rm part$; globale Entscheidung (Fall 1, 3b, 4) ?[O]; **substanzieller Vorrang** über 166b-P |
| NEU-167 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Lineare Kernbedingungen vs. Fourierladungsbedingung: Trennung gültig; alte Zeugenroute über Kernbedingungen durch 167b geschlossen |
| NEU-167b | `AUDIT-REUSED` | `INCORPORATED` | Abschluss O167-2: keine Kernbedingungen aus NEU-157/NEU-44 — maßgeblicher Endstand; Zeugenroute über $\ker C_p\setminus\ker T_p$ geschlossen ✓[M] |
| NEU-168 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Nichtverschwindensgeometrie, exakt zulässige Liftmenge: Geometrie gültig; keine falsche Kernzeugenroute; $L_3^\circ$-Trägervoraussetzung firewallen |
| NEU-169 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Kollisionssystem, Einzelmoden-Nichtverschwindung $B_p$: Kollisionssatz behalten; $L_3^\circ$-Trägervoraussetzung ausdrücklich firewallen (durch 250j verstärkt) |
| NEU-170 | `AUDIT-RECONCILED` | `SUPERSEDED_part` | Gew. Träger $L_3^\circ$, Quellenimport: durch 170a–d epistemisch überholt; Teilaussagen über Trägerdefinition erhalten |
| NEU-170a | `AUDIT-RECONCILED` | `SUPERSEDED_part` | Fouriergrad-Klasse $L_3$, Repräsentantenstatus: durch 170b/c/d präzisiert; frühere Repräsentantenannahmen zurückgenommen |
| NEU-170b | `AUDIT-RECONCILED` | `SUPERSEDED_part` | Ursprungsdefinition, Repräsentantenstatus $L_3$: durch 170c/d überholt; Quellendefinitionen aus NEU-20/28 relevant |
| NEU-170c | `AUDIT-RECONCILED` | `INCORPORATED_part` | Direktaudit $L_3$-Definition NEU-20/NEU-28: Quellendefinition geklärt; Repräsentantenstatus in NEU-28 bestätigt |
| NEU-170d | **`AUDIT-REUSED`** | **`INCORPORATED` — DAG-ENDANKER** | Bereinigter DAG-Audit NEU-28/NEU-162: Einmodenansatz algebraisch rechenbar; Herkunft $[L_3]\mapsto L_3^\circ = e_1 V_1$ blockiert; Zielkanten-Nichtverschwinden nicht bewiesen; maßgeblicher Endstand für gesamten $L_3^\circ$-Strang |
| NEU-171 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Typfundament $L_3$-Klasse, Kochainkomplex: Strukturaussagen gültig; durch 172/173 epistemisch fortgeschrieben |
| NEU-172 | `AUDIT-RECONCILED` | `INCORPORATED_part` | Direktaudit NEU-72/NEU-170b, Typfundament $L_3$: Fallbezeichnung durch 173 korrigiert (C₂ → C_src-neg); Teilresultate erhalten |
| NEU-173 | **`AUDIT-REUSED`** | **`INCORPORATED` — TYPQUELLEN-ENDANKER** | $\Delta$-Audit NEU-20/NEU-28, Typfundament, Quellenkegel: epistemische Korrektur C₂ → C_src-neg; alten Typquellen-Auditzyklus ausdrücklich abgeschlossen; mathematische Neukonstruktion bleibt davon getrennt offen; maßgeblicher Abschluss |

##### F2-Kernfirewalls (ergänzend zu F1)

6. NEU-166b ist eine Doppelnummer. In P05 stets zwischen 166b-P (Provenienz-Firewall) und 166b-T (Fallentscheidung, substanzieller Vorrang) unterscheiden.
7. Alle Aussagen über $L_3^\circ$ in NEU-161–169 sind konditional im Einmodenmodell. Der Endanker für diesen Strang ist NEU-170d, nicht die Einmodenrechnungen selbst.
8. Die Kernzeugenroute $k\in\ker C_p\setminus\ker T_p$ ist durch NEU-167b geschlossen; kein Resultat aus NEU-165/166/168 darf sie stillschweigend als offen behandeln.
9. NEU-169-Kollisionssatz bleibt erhalten, aber nur mit expliziter Firewall auf die $L_3^\circ$-Trägervoraussetzung — durch NEU-250j zusätzlich verstärkt.

---

#### F3 — Spätere Primfaser-Korrekturen

**Quellknoten:** NEU-225, NEU-227 sowie zugehörige Quellenaudits aus `01-primkanten-werkzeuge/`

| Behandlung |
|------------|
| Mit F1/F2-Endstand zusammenführen (`AUDIT-RECONCILED`) |
| Nicht-P05-Anteil (globale Kopplung, koh.) in P09/P11 weiterleiten |

---

#### F4 — Neuer Mangoldt-/Primzahlpotenzstrang

**Quellknoten:** NEU-250g, NEU-250i, NEU-250j (7. August 2026) + NEU-250f Patch 1 (`1579a379`)  
**Prüfart:** `TARGETED-REAUDIT` / RECONCILIATION

| Knoten | Inhalt | Offene Punkte / Firewall |
|--------|--------|--------------------------|
| NEU-250f + Patch 1 | Filtrations-No-Go nur **konditional** auf $L_{3,\rm alg}^\circ\in F^3A$ | Unbedingter alter No-Go `SUPERSEDED`; Realisierungsbrücke ?[O] |
| NEU-250g | Primitiver Faktor $\frac{\log p}{\sqrt p}$ algebraisch konstruiert | Hilbertraum-Fundierung $H_{\rm BC}$ offen; ⚠[M] |
| NEU-250i | $H_{\rm pr}=D_\Omega^{-1}H_{\rm BC}$; auf $n=p^m$: $\frac{\Lambda(p^m)}{p^{m/2}}=\frac{\log p}{p^{m/2}}$ | Firewall: $H_{\rm pr}\ne\Lambda$ auf allgemeinen zusammengesetzten $n$ |
| NEU-250j | Trägertrennung $\operatorname{supp}\Lambda\cap\operatorname{supp}(\text{Kreuzprimkollision})=\emptyset$ | Graphbasisüberlappung lebt nur auf $\Lambda=0$; Mediatorweg ?[O] |

---

### F-Roadmap

| Paket | Status | Nächster Schritt |
|-------|--------|------------------|
| F1 | **PASS A COMPLETE** (`07903f85`) | Endstand für P05 extrahiert |
| F2 | **ERÖFFNET** — Matrix steht | Reconciliation-Arbeit beginnen; keine neuen Dateien erforderlich |
| F3 | ausständig | NEU-225/226/227-Reconciliation final in P05-Scope ziehen |
| F4 | ausständig | NEU-250g/i/j gezielt re-auditieren; Patch 1 zu 250f verbindlich |
| P05-SYN | nach F1–F4 | `papers/P05_*.tex` + LaTeX-SYN-Transferaudit |

---

## Querverweise

- Verbindlicher Migrationsplan: `00-uebersicht/SYN_MIGRATIONSPROTOKOLL.md`
- Audit-Archive: `ARCHIV-AUDIT-2026-07.md`, `ARCHIV-AUDIT-NEU202-212.md` u. a.
- Zwischenbilanzen: `ZWISCHENBILANZ_2026-07-29.md` bis `2026-08-01.md`
- Auditstand HH-Strang: `AUDITSTAND-2026-08-03.md`
- Forschungsknoten (abgeschlossen): `03-weil-form-statistik/`
- Forschungsknoten (aktiv): `01-primkanten-werkzeuge/`, `05-primkanal-fourierladung/`
