# Pass-A-Protokoll — SYN-Migrationsverfahren

**Erstellt:** 8. August 2026 | **Zuletzt aktualisiert:** 8. August 2026 (F3 Primäraudit-Patch — doppelt geprüft)

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

**Status:** aktiv | **F1 COMPLETE** | **F2 eröffnet** | **F3 COMPLETE (doppelt geprüft)** | **F4 eröffnet** | P05-SYN ausständig

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

**Neu entdeckter Konflikt:** NEU-250f Typfehler; unbedingter No-Go `SUPERSEDED`; korrigiert in Commit `1579a379`.

$$\boxed{\text{F1 PASS A COMPLETE}}$$

---

#### F2 — Fourier-/Rohkopplungsstrang (Ordner 05) — **ERÖFFNET** (Commit `8ead5d52`)

**Quellknoten:** 33 Dateien, NEU-151 bis NEU-173 inkl. aller Unterknoten  
**Endanker:** NEU-170d + NEU-173 (`AUDIT-REUSED`)  
**Verbindliche Voraussetzung:** F1-Kernfirewalls gelten auch hier

##### Buchhaltungsbefund: DUPLICATE-ID NEU-166b

> | Interne F2-Bezeichnung | Dateiname | Rolle |
> |------------------------|-----------|-------|
> | **166b-P** | `NEU-166b_Rollen_Provenienzentscheidung_Rp_Tp.md` | Audit-Firewall; Rollenentscheidung ?[O] |
> | **166b-T** | `NEU-166b_Typ_Domaenen_Deszentaudit_Tp_Fallverzweigung.md` | substanzieller Vorrang; Fall 3a lokal ✓[M]_part; global ?[O] |
>
> Kein SYN-Satz der Form „NEU-166b beweist …“ ohne Angabe der Datei.
> Status: `DUPLICATE-ID / 166b-T RECONCILED / 166b-P AUDIT-FIREWALL`

*(Vollständige 33-Zeilen-Prüfartmatrix und F2-Kernfirewalls #6–9 im Commit `8ead5d52` festgehalten.)*

---

#### F3 — Spätere Primfaser-Korrekturen — **PASS A COMPLETE (doppelt geprüft)**

**Quellknoten:** NEU-225, NEU-226, NEU-227 (alle in `01-primkanten-werkzeuge/`)  
**Prüfart:** `AUDIT-RECONCILED` für alle drei  
**Verfahren:** Repo-/Konsistenzcheck Perplexity (Commit `193ee6d9`) + Primäraudit mathematisch (dieser Commit)  
**Abschlussdatum:** 8. August 2026

> **Primäraudit-Patch:** Vier epistemische Korrekturen gegenüber Commit `193ee6d9`:
> 1. **NEU-227 / $V\notin\mathcal S_2$:** Nicht „Notwendigkeitsbedingung für $V\in\mathcal S_4\setminus\mathcal S_2$ gesichert“, sondern: $V\notin\mathcal S_2$ ist notwendig damit der Nicht-$\mathcal S_1$-Zeuge überhaupt funktionieren kann. Der $\mathcal S_4$-Teil der Vermutung ist durch NEU-227 nicht gestützt und bleibt reine strukturelle Arbeitshypothese.
> 2. **NEU-226 / Kreuzterme:** Quellenaussage lautet „generisch $K_{pq}\ne0$“, nicht „für jedes $p\ne q$ unbedingt“. Formulierung korrigiert: Primkanalbilder können nichttrivial überlappen; Primblockdiagonalität ist nicht strukturell erzwungen.
> 3. **Firewall 10:** Nicht „jede $D_{\rm rel}$-Eigenbasisformel verboten“ (das würde den Spektralsatz treffen), sondern: die diskrete Eigenbasisdarstellung (51.3)/(51.4)/(51.7) aus NEU-51 ist SUPERSEDED und durch die projektionswertige Spektralmaßform (227.3)–(227.9) aus NEU-227 zu ersetzen.
> 4. **Weiterleitungskorrektur:** NEU-225 primär nach P06 (nicht P09); NEU-226/227 Feshbach-/Schattenklassen-/Spektralmaßanteile nach P06, nichtorthogonaler globaler Kopplungsmechanismus nach P11.

##### Prüfartmatrix NEU-225–227 (korrigierte Fassung)

| Knoten | Prüfart | Endstatus für P05 | Kernbefund |
|--------|----------|-------------------|------------|
| NEU-225 | `AUDIT-RECONCILED` | `INCORPORATED_part` + **→ P06** | $D_{\rm rel}\|_{\mathcal H_{p,a}}\cong 2ic_p\,d/dt$ auf $L^2(\mathbb R)$: Transportgenerator, rein absolutstetiges Spektrum, kein Kern in Primsektoren, kompakter Resolvent ausgeschlossen ✓[M]; Primfaserkette $c_p=\tfrac12\gamma_N p\log p$ verbindlich ✓[M]; Konvention $J_N^- = \tfrac12(\Theta_N-\Theta_N^\dagger)$, Option B ($\mathcal D_{\rm rel}=iJ_N^-$ selbstadjungiert) verbindlich ✓[M]; Domainenvorbehalt $\mathcal D_0$ separat geführt: ?[O] (`[O-225-1]`); Feshbach-Transfer als HP-Kandidat: Arbeitshypothese (`[O-225-2]`); $\eta$-Orthogonalitäts-Rollen**rollung in NEU-226 beschädigt die Primkettenrechnung nicht** (Primsektor: nur ein Sprung, $u$-Restklasse erhalten, durch NEU-227 bestätigt) |
| NEU-226 | `AUDIT-RECONCILED` | `INCORPORATED_part` + **→ P06/P11** | Kreuztermmechanismus: Primkanalbilder können nichttrivial überlappen ($\eta_{p;m;s,u}\sim e_{u+ps}V_{pm}$, verschiedene $(p,m)$ auf demselben $V_{pm}$); **generisch** $K_{pq}\ne0$ für $p\ne q$ ✓[M]; **Primblockdiagonalität nicht strukturell erzwungen** (keine unbedingte Gleichheit $\mathcal K_N=\bigoplus_p K_p$) ✓[M]; $K_N(z)$ bei festem $N$ nicht endlich-rangig: Rang-$\pi(N)$-Annahme widerlegt ✓[M]_neg; $\mathcal S_1$-Frage durch $u$-Regulator offen; NEU-77-Limes nur punktweise, Schattennormen nicht kontrolliert ✓[M]; $\eta$-Orthogonalität über Primkanäle zurückgerollt (nur innerhalb fester Kette gültig) ✓[M]; Blocker (51.3)/(51.4)/(51.7): Eigenbasisannahme verletzt NEU-52/225, durch Spektralmaßform zu ersetzen; Feshbach-/Schattenklassenanteil → P06; nichtorthogonale globale Kopplung → P11 |
| NEU-227 | `AUDIT-RECONCILED` | `INCORPORATED` + **→ P06/P11** | Koordinatenwörterbuch ✓[M]: $\eta_{p;m;s,u}\leftrightarrow e_R V_M$, $M=pm$, $R=u+ps$; $s\mapsto s+m$ und $r\mapsto r+n$ sind dieselbe Bewegung; im Primsektor vollständig gerechtfertigt ✓[M]; Spektralmaßform (227.3)–(227.9) SUPERSEDED die Eigenbasisform (51.3)/(51.4)/(51.7) vollständig ✓[K/M]; Polarzerlegungsargument nachgerechnet ✓[M]; **Nicht-$\mathcal S_1$-Zeuge erfordert $V\notin\mathcal S_2$** als Notwendigkeitsbedingung für den Zeugenmechanismus ✓[M] — der $\mathcal S_4$-Teil der Vermutung $V\in\mathcal S_4\setminus\mathcal S_2$ ist durch NEU-227 **nicht** gestützt und bleibt strukturelle Arbeitshypothese; Spektralmaßform → P06; $u$-Regulator/Quellhilbertraum/Gramoperator/$\det_2$ → P11 |

##### F3-Kernbefünde für P05 (korrigierte Fassung)

**Was gesichert ist und nach P05 geht:**

- $D_{\rm rel}$ ist ein Transportgenerator, kein Hilbert–Pólya-Operator; kompakter Resolvent ausgeschlossen. `✓[M]`
- Jede Primfaser $\mathcal H_{p,a}$ hat absolutstetiges Spektrum; kein Kern. `✓[M]`
- $D_{\rm rel}$ ist kanalerhaltend; **generisch** können Primkanalbilder überlappen und $K_{pq}\ne0$ für $p\ne q$ erzeugen; Primblockdiagonalität ist nicht strukturell erzwungen. `✓[M]`
- Spektralmaßform (227.3)–(227.9): verbindliche Schreibweise, ersetzt (51.3)/(51.4)/(51.7). Dies schärft F1-Firewall Nr. 5 zur konkreten SUPERSEDED-Ersetzungsregel. `✓[K/M]`
- Koordinatenwörterbuch (227.1)/(227.2): verbindlich auch für F4. `✓[M]`
- Primfaserkette $c_p = \tfrac12\gamma_N p\log p$: verbindliches Ergebnis für den Primsektor. `✓[M]`

**Was nach P06 weitergereicht wird:**

- Feshbach-Kollaps-Identität (NEU-77, endliches $N$): exakt gültig; globaler Limes nur punktweise. → P06
- Schattenklassenkriterien (227.6)–(227.9): Spurklasse/Hilbert-Schmidt-Entscheidung. → P06
- Sektoren $m$ nicht prim: Mehrfachsprünge mischen $u$-Klassen; `[O-225-3]` offen. → P06

**Was nach P11 weitergereicht wird:**

- Nichtorthogonaler globaler Kopplungsmechanismus: $u$-Regulator, Quellhilbertraum $\mathscr E$, Gramoperator, Orthonormalisierung der überlappenden Primkanalbilder. `[O-226-3]–[O-226-7]` offen. → P11
- $\det_2(I-K(z))$ gegen Weil-/$\Xi$-Schicht. → P11
- $V\notin\mathcal S_2$ als Notwendigkeitsbedingung für den Nicht-$\mathcal S_1$-Zeugenmechanismus gesichert; $V\in\mathcal S_4$ als strukturelle Arbeitshypothese (durch NEU-227 nicht bewiesen). → P11

**F3-Korrekturrollen für F4:**

Mit F3 steht fest:
1. Die Primkanalgeometrie ist ein Transportspektrum, kein Energiespektrum; $D_{\rm rel}$ liefert keine kompakte Schicht.
2. Generisch können Primkanalbilder überlappen; Primblockdiagonalität ist nicht strukturell erzwungen.
3. Das Koordinatenwörterbuch (227.1) ist verbindlich.

Damit kann F4 präzise fragen: Welche Teile dieser Geometrie tragen tatsächlich $\Lambda(p^m)/p^{m/2}$? Und warum können die generischen Kreuzterme $K_{pq}$ laut NEU-250j nicht zugleich auf $\mathrm{supp}\,\Lambda$ sitzen?

##### F3-Kernfirewall (korrigierte Fassung)

10. Die diskrete Eigenbasisdarstellung aus NEU-51 — (51.3), (51.4), (51.7) — ist **SUPERSEDED** und durch die projektionswertige Spektralmaßform (227.3)–(227.9) aus NEU-227 zu ersetzen. Dies betrifft die unzulässige Annahme einer diskreten Eigenbasis $D_{\rm rel}\eta_\alpha=\lambda_\alpha\eta_\alpha$; der Spektralsatz selbst ist nicht berührt. Diese Firewall ergänzt und schärft F1-Firewall Nr. 5.

$$\boxed{\text{F3 PASS A COMPLETE — doppelt geprüft: Repo-Check (193ee6d9) + Primäraudit-Patch (dieser Commit)}}$$

---

#### F4 — Neuer Mangoldt-/Primzahlpotenzstrang — **ERÖFFNET** (Arbeitshypothesen; TARGETED-REAUDIT ausständig)

**Quellknoten:** NEU-250g, NEU-250i, NEU-250j (7. August 2026) + NEU-250f Patch 1 (`1579a379`)  
**Prüfart:** `TARGETED-REAUDIT` / RECONCILIATION — **noch nicht durchgeführt**  
**Verbindliche Voraussetzung:** F1-Firewalls + F3-Koordinatenwörterbuch + F3-Spektralmaßform  
**Verfahren:** Primäraudit zuerst (mathematisch), danach Repo-/Konsistenzcheck; erst dann PASS A COMPLETE

> **Achtung:** Die Endstatuszeilen aus Commit `193ee6d9` (z. B. `INCORPORATED_part`, `SUPERSEDED_part`) sind **vorläufige Arbeitshypothesen** aus dem Repo-Check. Der vereinbarte TARGETED-REAUDIT von NEU-250g/i/j hat noch nicht stattgefunden. Kein F4-Status darf als PASS A COMPLETE gelesen werden.

##### Leitfrage F4 (aus F1–F3 gewonnen)

> F3 hat die Primkanalgeometrie als Transportspektrum gesichert und die BC-Überlappungsstruktur mit Koordinatenwörterbuch verankert. F4 fragt: Welche dieser Geometrie trägt tatsächlich den Mangoldt-Faktor $\Lambda(p^m)/p^{m/2}$? Und: Warum können die generischen Kreuzterme $K_{pq}$ ($p\ne q$) laut NEU-250j nicht zugleich auf $\mathrm{supp}\,\Lambda$ sitzen?

| Knoten | Prüfart | Vorläufiger Arbeitsstand (nicht geprüft) | Offen / Firewall |
|--------|----------|-------------------------------------------|------------------|
| NEU-250f + Patch 1 (`1579a379`) | `TARGETED-REAUDIT` | Filtrations-No-Go nur konditional auf $L_{3,\rm alg}^\circ\in F^3A$; unbedingter No-Go SUPERSEDED | Realisierungsbrücke ?[O] |
| NEU-250g | `AUDIT-RECONCILED` | Primitiver Faktor $\frac{\log p}{\sqrt p}$ algebraisch konstruiert | Hilbertraum-Fundierung $H_{\rm BC}$ offen; $\mathcal S_4$-Einordnung nicht aus F3 übertragbar |
| NEU-250i | `AUDIT-RECONCILED` | $H_{\rm pr}=D_\Omega^{-1}H_{\rm BC}$; $\Lambda(p^m)/p^{m/2}=\log p/p^{m/2}$ im Primsektor | **Firewall:** $H_{\rm pr}\ne\Lambda$ auf zusammengesetzten $n$ mit mehreren Primteilern |
| NEU-250j | `AUDIT-RECONCILED` | Trägertrennung $\mathrm{supp}\,\Lambda\cap\mathrm{supp}(K_{pq})=\emptyset$ für $p\ne q$ | Widerleg nicht nichtorthogonale Geometrie (F3-Firewall 11); Mediatorweg → P11 |

##### Verbindliche F4-Firewalls (aus F1–F3, gelten schon jetzt)

11. NEU-250j widerlegt **nicht** die in F3 gesicherten generischen Kreuzterme $K_{pq}\ne0$ aus NEU-226. Es zeigt nur die Trägertrennung $\mathrm{supp}\,K_{pq}\cap\mathrm{supp}\,\Lambda=\emptyset$ für $p\ne q$. Die nichtorthogonale Primkanalgeometrie bleibt bestehen.
12. Im Primsektor stimmt $\Lambda(p^m)/p^{m/2}=\log p/p^{m/2}$ mit dem primitiven Faktor aus NEU-250g überein; auf zusammengesetzten $n$ mit mehreren Primteilern ist $H_{\rm pr}\ne\Lambda$ eine harte Firewall.

---

### F-Roadmap

| Paket | Status | Nächster Schritt |
|-------|--------|------------------|
| F1 | **PASS A COMPLETE** (`07903f85`) | Endstand für P05 extrahiert |
| F2 | **ERÖFFNET** (`8ead5d52`) | Reconciliation-Arbeit; keine neuen Dateien erforderlich |
| F3 | **PASS A COMPLETE — doppelt geprüft** | Spektralmaßform und Koordinatenwörterbuch verbindlich verankert |
| F4 | **ERÖFFNET** (Vorläufiger Arbeitsstand) | Primäraudit NEU-250g/i/j zuerst; danach Repo-Check; dann PASS A COMPLETE |
| P05-SYN | nach F2+F4 | `papers/P05_*.tex` + LaTeX-SYN-Transferaudit |

---

## Querverweise

- Verbindlicher Migrationsplan: `00-uebersicht/SYN_MIGRATIONSPROTOKOLL.md`
- Audit-Archive: `ARCHIV-AUDIT-2026-07.md`, `ARCHIV-AUDIT-NEU202-212.md` u. a.
- Zwischenbilanzen: `ZWISCHENBILANZ_2026-07-29.md` bis `2026-08-01.md`
- Auditstand HH-Strang: `AUDITSTAND-2026-08-03.md`
- Forschungsknoten (abgeschlossen): `03-weil-form-statistik/`
- Forschungsknoten (aktiv): `01-primkanten-werkzeuge/`, `05-primkanal-fourierladung/`
