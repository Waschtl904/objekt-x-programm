# Objekt X — kanonische Forschungsroadmap v2.2

> **Stand:** 13. September 2026; Registry unverändert.  
> **Rolle:** aktuelle Abhängigkeits- und Forschungsstrategiekarte.  
> **Keine Beweisautorität:** Diese Roadmap erzeugt keine `✓[M]`-Promotion, kein unabhängiges GREEN, keinen Freeze und keine Object-X-/RH-Folgerung.  
> **Operative Front:** [CURRENT-FRONT](../CURRENT-FRONT.md)  
> **Kurzstand:** [AKTUELLER_STAND](AKTUELLER_STAND.md)  
> **DAG:** [DAG](DAG.md)  
> **Objekt-X-Definition:** [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)  
> **Registry:** [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)

---

## 0. Autorität und Konfliktregel

Bei Konflikten gilt nach Zuständigkeit:

1. Arbeitsdefinition für die Identität von Objekt X;
2. Registry für gebuchten Theorem-/Reviewstatus;
3. kanonische Audit-/Beweisquelle für Mathematik im benannten Scope;
4. `CURRENT-FRONT.md` für aktuelle Priorität;
5. diese Roadmap für Strategie;
6. `ACTIVE_FRONT.yaml` für historische Stack-/PR-Provenienz.

Der aktuelle `main`-Head wird live aus GitHub gelesen und nicht selbstreferenziell als SHA in dieser Datei gespeichert.

---

## 1. Verfügbarer Meilenstein: fixed-pair Strong Terminal / C6

Der positive Wurzelanker plus R42.51 liefert für jedes feste `0<R<S`

```math
W_{R,S}^{[U]}\varepsilon_R\longrightarrow\varepsilon_S
```

im ungeraden P11-Graphraum.

**Nicht enthalten:** Radienuniformität, Operatornormkonvergenz, vollständiger gerader Sektor, Object-X-Realisierung oder RH.

Historische quantitative R43-COND-/FD23-/Flagfragen bleiben in ihrem eigenen Scope offen, sind aber keine Voraussetzungen des direkten fixed-pair-C6-Abschlusses.

---

## 2. Belastbare Prime-Power-Geometrie

Für einen Primast gilt exakt

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

Der Exponent `3/4` ist damit durch Martingalmultiplizität plus Weil-Diagonale erzwungen.

Nach Weil-Diagonalnormalisierung:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}\,p^{-|j-k|/2}.
```

Mit `q=p^{-1/2}`:

```math
T_q^*T_q=R_q-uu^*,
\qquad
T_q^*T_q+uu^*=R_q.
```

Die P11-Restseite besitzt die exakte Weil-Tail-Normalform

```math
R_R^*R_R=\sum_{p,k}w_{p,k}Z_{p,k,R}^*Z_{p,k,R}.
```

**Buchung:** exakte Strukturinformation und theorem-ready Nebenprojekt; noch keine vollständige gemeinsame Prime-/Archimedean-Geometrie.

---

## 3. Endliche Suzuki-/OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad
N_a=c_aI+C_a.
```

`G_a^+` besteht aus positiven Prime-Kanal-, Log-Multiplikator- und logarithmischen `log|D|`-Formen.

Die frühere Forschungsfrage

```text
existiert irgendein kontraktiver W_a ?
```

wird **nicht weiter als Object-X-Gate geführt**. Sobald lokale Positivität bereits bekannt ist, kann ein solcher Operator zirkulär aus `Q_{B_a}` konstruiert werden. Damit würde nur bekannte Positivität umgeschrieben.

**Offen ist Kanonizität:** Kann der Defekt aus derselben bereits vorhandenen Geometrie vorwärts konstruiert werden?

---

## 4. Zertifikationsstand

PR #98 hat die endlichen Gate-1/Gate-2-Pfade gehärtet.

### Normalisierung

Für `a=0.5,0.8,1.0` wurden Realraum und Fourierdarstellung mit fail-closed Arb-Residualtests verglichen. Explizit kontrolliert sind Bernoulli-Tail, `sinc`-Rest, Prime-Power-Cutoff und Endpunktfehler.

### Gate 2

Arb 512 Bit, Dirichletbasis `N<=14`, drei Radien und beide Paritäten: 42/42 verschachtelte Blöcke mit strikt positiven Cholesky-Pivots.

**Firewall:** Das sind endliche Zertifikate. Sie beweisen keine unendlichdimensionale lokale Positivität jenseits des bekannten Scopes und keine RH.

---

## 5. Aktuelle Hauptfront: OX-GEN

Suzukis Teilkern

```math
r_0''(t)=-2\cosh(t/2)
```

liefert exakt

```math
R_0(v,v)
=-2\left(\int\cosh\frac x2\,v\right)^2
+2\left(\int\sinh\frac x2\,v\right)^2.
```

Die Prime-Power-Geometrie verwendet dieselbe Exponentialfamilie:

```math
p^{-1/2}=e^{-\log p/2},
\qquad
R_p(j,k)=p^{-|j-k|/2},
\qquad
w_{p,k}=\log p\,p^{-k/2}.
```

### OX-GEN-Frage

Kann `R_0` als intrinsischer Rand-/Defektterm derselben Exponentialstruktur konstruiert werden, die die Prime-Power-Kanäle normiert, ohne `Q_{B_a}`, `B_a^{1/2}`, ein unbekanntes Forminfimum oder RH rückwärts zu verwenden?

Dies ist ein **Teilproblem**. `R_1` und der Skalarblock `c_aI` bleiben offen.

---

## 6. Nächste Gates

### OX-GEN-A — jetzt

Bei `a=0.5` die Funktionale

```math
v\mapsto\int\cosh(x/2)v(x)\,dx,
\qquad
v\mapsto\int\sinh(x/2)v(x)\,dx
```

innerhalb der vorhandenen Prime-/`log|D|`-Featuregeometrie isolieren.

Der Radius `a=0.5` wird zuerst benutzt, weil dort die endliche Extremalrichtung im Gate-2-Sweep deutlich stabiler war als bei `a>=0.8`. Diese Stabilität ist Diagnostik, kein Theorem.

### GENERATOR-CLASS

Vor jedem No-Go eine **natürliche und enge Generator-Klasse** definieren. Ein Gate zählt nur, wenn positive Konstruktion und negativer Ausgang vorab beide logisch möglich sind.

### OX-GEN-B

Danach entweder:

- expliziten nichtzirkulären Intertwiner/Defektmechanismus konstruieren, oder
- die vorher definierte Generator-Klasse ausschließen.

---

## 7. Spur B — eigenständige Mathematik

Parallel die Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständigen Satz verschriftlichen:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q.
```

Scope: fensterfrei, exakt, RH-unabhängig. Nicht als Objekt X vermarkten. Ein bisheriger Literaturbefund ist nur Neuheitsindikator, kein Prioritätsbeweis.

---

## 8. Vollständiger Object-X-Pfad

Ein echter X-Kandidat muss mindestens spezifizieren:

- intrinsische gemeinsame Geometrie,
- Hilbert-/Mediatorraum,
- kanonische Abbildung `T_X`,
- Prime-Power-Kanal,
- archimedischen Kanal,
- gemeinsame nichtorthogonale Kopplung,
- Testklasse und Normalisierung,
- Nicht-Zirkularität.

Danach separat:

```text
GENUINE X CANDIDATE ?[O]
        |
        | --requires separate proof-->
        v
EXACT FULL WEIL-GRAM IDENTITY ?[O]
        |
        v
OBJECT-X REALIZATION ?[O]
        |
        | ⇒ Q_W(f,f)>=0 on realized scope
        v
WEIL-CRITERION-SCOPE ?[O]
        |
        v
RH
```

Keine Forschungs-/candidate-input-Kante ist als logische Implikation zu lesen.

---

## 9. Separate Nebenfronten

### R37/G4c

Separat offen; Beziehung zur OX-GEN-/X-Route ist unresolved.

### Historische R43-COND-/FD23-/Flagfragen

Weiterhin in ihren eigenen Quantoren offen, aber nicht aktuelle Default-Aufgabe und keine Voraussetzung des direkten fixed-pair-C6-Abschlusses.

### PR #91

Analytischer Source-descent/Weil-separation-Draft. Kein unabhängiger Exact-Head-GREEN wird durch PR #98 übertragen.

### SW1 salvage / PR #49

Candidate-only Nebenfront; kein stiller Merge und keine unbewiesene Object-X-Kante.

---

## 10. Gesperrte Interpretationen

Nicht als aktive Strategie reaktivieren:

- PR91-Zeugenmatrix sei Rang 1;
- `3/4` sei bloße Dämpfung;
- Vier-Boundary-Erklärung der Interior/Baseline-Differenz;
- cross-prime sei Fensterrand;
- „Nichtunitarität = Hub“;
- matched cutoff als Objekt-X-Mechanismus;
- OX-REN/OX-REN' als Hauptfront;
- Radius-Swap im PR97-Checker durch bloßes Ersetzen von `R=1`;
- klassische `H^{1/2}`-/Douglas-Terminologie für den Kernel `1/|x-y|`;
- globaler Kollaps von `||I-W^*W||`;
- `0.603`-Koeffizientenratio als Konstante;
- weitere reine OX-GRAM-Existenztests ohne neuen Mechanismus.

---

## 11. Falsifikations-/Rollback-Regeln

- **OX-GEN-A scheitert:** Nur die aktuelle Generatorintuition fällt; Prime-AR(1), C6 und Object-X-Ziel bleiben unberührt.
- **Eine definierte GENERATOR-CLASS fällt:** Nur diese Klasse ist ausgeschlossen.
- **Prime-AR(1)-Algebra fällt im Exact-Head-Audit:** alle darauf gestützten OX-GEN-Interpretationen neu auditieren.
- **R37/G4c fällt:** R37-Pfad fällt; keine automatische Wirkung auf OX-GEN/C6.
- **PR91 fällt:** nur sein Source-descent/Weil-separation-Kandidat fällt.
- **Ein X-Kandidat fällt an der vollen Weil-Gram-Identität:** dieser Kandidat ist kein Objekt X; kein universelles No-Go.

---

## 12. Forschungsregel

Ein Schritt zählt als Object-X-Hauptfront-Fortschritt nur, wenn er

1. einen expliziten Teil gemeinsamer Gramgeometrie konstruiert,
2. eine vorab definierte Architekturklasse ausschließt,
3. eine notwendige Prime-/Archimedean-Generatorstruktur beweist oder
4. eine tatsächlich benötigte Domain-/Normalisierungs-/Konvergenzlücke schließt.

Bloße Umschreibungen, gefittete Witness-Werte und Positivitätsreproduktionen sind Nebenarbeit.

---

## 13. Explizit offen

```text
OX-GEN-A
GENERATOR-CLASS
OX-GEN-B
R_1 / regular archimedean correction
scalar block c_a I in intrinsic geometry
genuine X candidate
exact full Weil-Gram identity
Object-X realization
Weil-criterion scope verification
RH
R37/G4c [separate]
```

Historische Nebenfragen bleiben über Audits, Git-Historie und die Registry-/Problemprovenienz zugänglich; sie werden hier nicht zur aktuellen Default-Priorität erhoben.
