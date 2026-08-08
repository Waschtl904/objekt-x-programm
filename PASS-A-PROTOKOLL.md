# Pass-A-Protokoll — SYN-Migrationsverfahren

**Erstellt:** 8. August 2026 | **Status:** aktiv

Dieses Dokument fixiert das verbindliche Verfahren für die Pass-A-Phase der SYN-Migration.  
Es ersetzt kein mathematisches Dokument, sondern regelt den Prozess.

---

## Grundsatz

Das Ziel ist **nicht**, alle Knoten erneut vollständig zu auditieren. Das wäre ein neues Projekt von der Größenordnung der ursprünglichen Auditphase. Ziel ist vielmehr:

$$
\text{Knoten} + \text{vorhandene Audits} + \text{Patches} + \text{spätere Korrekturen}
\;\longrightarrow\;
\text{heute gültiger Endstand}
\;\longrightarrow\;
\text{SYN}
$$

Der bereits geleistete Auditbestand wird maximal wiederverwendet. Neue mathematische Arbeit wird nur dort investiert, wo:
- ein Audit fehlt, **oder**
- Audit und heutiger Stand kollidieren.

---

## Feste Pass-A-Regel: Auditsuche zuerst

Vor jedem neuen Batch:

1. Vorhandene Audit-Dateien für die Knoten des Batches suchen  
   (`ARCHIV-AUDIT-*`, `AUDITSTAND-*`, `ZWISCHENBILANZ-*`, `audits/`-Verzeichnis)
2. Spätere Korrekturknoten im selben Themenblock prüfen  
   (ein jüngerer Knoten, der eine frühere Aussage als falsch kennzeichnet, ist Audit-Material)
3. Prüfart bestimmen (siehe Taxonomie unten)
4. Nur dann neuen mathematischen Auditaufwand anlegen, wenn Prüfart `NEW-DIRECT-AUDIT` oder `TARGETED-REAUDIT`

---

## Prüfart-Taxonomie

| Kürzel | Bedeutung | Aufwand |
|--------|-----------|----------|
| `AUDIT-REUSED` | Bestehender Audit übernommen; gegen aktuellen Knotenstand und spätere Patches geprüft; kein Widerspruch gefunden | Niedrig |
| `AUDIT-RECONCILED` | Mehrere Audits/Patches/Zwischenbilanzen zu einem widerspruchsfreien Endstand vereinigt | Mittel |
| `TARGETED-REAUDIT` | Bestehender Audit vorhanden, aber Widerspruch oder Lücke beim SYN-Abgleich identifiziert; **nur** die betroffene Aussage neu geprüft | Mittel |
| `NEW-DIRECT-AUDIT` | Kein brauchbarer früherer Audit vorhanden; Knoten erstmals vollständig auditiert | Hoch |

---

## Gruppenregister

### Gruppe A — NEU-091–092

| Knoten | Prüfart | Endstatus |
|--------|----------|-----------|
| NEU-091 | `NEW-DIRECT-AUDIT` | INCORPORATED |
| NEU-092 | `NEW-DIRECT-AUDIT` | INCORPORATED |

---

### Gruppe B — NEU-093–100 *(Eintrag folgt)*

---

### Gruppe C — NEU-101–110

**Abgeschlossen:** 8. August 2026  
**Commits:** Patches 1–5 (d5644669 → edc4fa53)

| Knoten | Prüfart | Endstatus | Kernbefund |
|--------|----------|-----------|-----------|
| NEU-101 | `AUDIT-RECONCILED` + `TARGETED-REAUDIT` | `SUPERSEDED(A,B,C)` + `OPEN(D)` | GM-Normierung ×[M] korrigiert auf \(H\log(M/H)\); Transferlemma ?[O] |
| NEU-102 | `AUDIT-RECONCILED` | `SUPERSEDED(A)` + `INCORPORATED(B,F)` + `OPEN(D,E)` | \(L^2(\mathbb{R})\)-Integrabilitätsfehler; No-Go (B) unabhängig gültig |
| NEU-103 | `AUDIT-REUSED` | `INCORPORATED` | Entfaltungskarte unabhängig von 101/102-Fehlern |
| NEU-104 | `AUDIT-RECONCILED` + `TARGETED-REAUDIT` | `INCORPORATED` ✓[M]_part | No-Go abstrakt korrekt; \(\mathcal{S}_{N,H}\) SUPERSEDED; \(\mathcal{P}^{\rm unf}_{N,H}\) Ersatzobjekt |
| NEU-105 | `AUDIT-REUSED` | `INCORPORATED` | Binärer Falsifizierbarkeitssatz gültig |
| NEU-106 | `AUDIT-REUSED` | `INCORPORATED(1,2,5)` + `OPEN(heuristisch)` | Epistemische Trennung RH \(\not\Rightarrow\) GUE ✓[M] |
| NEU-107 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | 107.2 Biimplikation ×[M]→Einwegimplikation; 107.3 Hierarchie ×[M]→Typaussage; 107.5 Normierung korrigiert |
| NEU-108 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | 108.4 harter No-Go→Typisierungswarnung ✓[M]_part |
| NEU-109 | `AUDIT-REUSED` | `INCORPORATED(109.1,3)` + `OPEN(109.2,A,B)` | Wegabelung methodisch sauber |
| NEU-110 | `TARGETED-REAUDIT` | `PATCH ANGEWENDET` | 110.2 ×[M]→?[O]; 110.3 ×[M]→Typisierungsbedingung; Ausgang A/B offen |

---

### Gruppe D — NEU-111–112

**Abgeschlossen:** 8. August 2026  
**Commits:** Patches D-1/2, D-2/2 (43a0fa2b, 4f12c65f)

| Knoten | Prüfart | Endstatus | Kernbefund |
|--------|----------|-----------|-----------|
| NEU-111 | `NEW-DIRECT-AUDIT` | `PATCH ANGEWENDET` | Ausgangs-B-Begründung SUPERSEDED; signed-\(\Gamma\)+\(m_\gamma\); \(m_{\Omega,N}\) erst in NEU-119 definiert; Jacobi-No-Go→Typisierungs-Firewall |
| NEU-112 | `NEW-DIRECT-AUDIT` | `PATCH ANGEWENDET` / teilweise `SUPERSEDED` durch NEU-113 | Herglotzmaß \(\mu_{\rm arith}=\sum m_\gamma\delta_\gamma\) korrigiert; Autokorrelationslift; Doppelzählung gestrichen; 112.4 retypisiert |

**Strategischer Befund:** Die alte Kette \(m_{\rm arith}\to Q_{\rm Weil}\) (fast unmittelbar) wird durch die saubere P02-Kette ersetzt:

$$
m_{\rm arith}\rightsquigarrow W_\xi^{\rm norm}
\quad\text{und getrennt}\quad
a\to g_{a,b}\to h_{a,b}\to B_W(a,b).
$$

---

### Gruppe E — NEU-113–120 *(offen)*

**Bekannte Vorwarnungen (aus Gruppe-D-Audit):**

| Knoten | Verdacht | Quelle |
|--------|----------|--------|
| NEU-119 | Formulierung "\(m_{\rm arith}\) benötigt Gamma-Terme" — wahrscheinlich alte 112.1-Verwirrung | Gruppe-D-Direktaudit |
| NEU-120 | Kann NEU-119-Fehler als Voraussetzung importiert haben | Ableitung |

**Prüfregel für Gruppe E:** Zuerst `ARCHIV-AUDIT-*`-Dateien für NEU-113–120 suchen; dann gezielt die Gamma-Term-Frage als `TARGETED-REAUDIT` behandeln.

---

## Offene Batch-Reihenfolge

| Gruppe | Knoten | Priorität |
|--------|--------|-----------|
| E | NEU-113–120 | als nächstes |
| F | NEU-121–130 | nach E |
| … | … | … |

---

## Querverweise

- Audit-Archive: `ARCHIV-AUDIT-2026-07.md`, `ARCHIV-AUDIT-NEU202-212.md`, ...
- Zwischenbilanzen: `ZWISCHENBILANZ_2026-07-29.md` bis `2026-08-01.md`
- Aktueller Auditstand: `AUDITSTAND-2026-08-03.md`
- Alle Forschungsknoten: `03-weil-form-statistik/`
