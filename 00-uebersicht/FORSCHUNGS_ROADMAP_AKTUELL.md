# Objekt X — kanonische Forschungsroadmap v2.3

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

Der aktuelle `main`-Head wird live aus GitHub gelesen und nicht selbstreferenziell als SHA gespeichert.

---

## 1. Verfügbarer Meilenstein: fixed-pair Strong Terminal / C6

Der positive Wurzelanker plus R42.51 liefert für jedes feste `0<R<S`

```math
W_{R,S}^{[U]}\varepsilon_R\longrightarrow\varepsilon_S
```

im ungeraden P11-Graphraum.

Nicht enthalten: Radienuniformität, Operatornormkonvergenz, vollständiger gerader Sektor, Object-X-Realisierung oder RH.

---

## 2. Belastbare Prime-Power-Geometrie

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

Nach Weil-Diagonalnormalisierung:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2}.
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

Buchung: exakte Strukturinformation und theorem-ready Nebenprojekt; noch keine vollständige gemeinsame Prime-/Archimedean-Geometrie.

---

## 3. Endliche Suzuki-/OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad
N_a=c_aI+C_a.
```

`G_a^+` besteht aus positiven Prime-Kanal-, Log-Multiplikator- und logarithmischen `log|D|`-Formen.

Die Frage „existiert irgendein kontraktiver Faktor?“ ist **kein** Object-X-Gate. Bei bereits bekannter lokaler Positivität kann ein solcher Faktor zirkulär aus `Q_{B_a}` konstruiert werden.

Offen ist Kanonizität: Kann der Defekt aus derselben vorhandenen Geometrie **vorwärts** konstruiert werden?

---

## 4. Zertifikationsstand

PR #98 hat die endlichen Gate-1/Gate-2-Pfade gehärtet.

- Normalisierung: `a=0.5,0.8,1.0`, Realraum/Fourier, fail-closed Arb-Residualtests, explizite Bernoulli-/`sinc`-Restbälle, Arb-Cutoffs und Endpunktfehler.
- Gate 2: Arb 512 Bit, `N<=14`, drei Radien, beide Paritäten, **42/42** verschachtelte Blöcke mit strikt positiven Cholesky-Pivots.

Firewall: endliche Zertifikate, kein globaler Weil-Positivitäts- oder RH-Beweis.

---

## 5. OX-GEN-A — gemeinsamer Exponentialgenerator `✓[M]`

Definiere

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad
\mathcal Ev=(E_+(v),E_-(v)).
```

Für Translationen `(T_t v)(x)=v(x+t)` gilt

```math
\boxed{\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}).}
```

Für

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

folgt exakt und ohne Fensterrandterm

```math
\boxed{\mathcal EK_n
=\lambda_n\operatorname{diag}(-1,1)\mathcal E.}
```

Suzukis elementarer archimedischer Teil ist das negative Charakter derselben Darstellung:

```math
\boxed{r_0''(t)=-\operatorname{tr}\rho(t),}
```

sogar

```math
\boxed{r_0(t)=-4\bigl(\operatorname{tr}\rho(t)-2\bigr),
\qquad r_0(\log n)=-4\lambda_n^2.}
```

Mit Austauschoperator

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
```

gilt polarisiert

```math
\boxed{R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle_{\mathbb C^2}.}
```

Bedeutung: Prime-Kanäle und `r_0` sind zwei exakte Funktoren derselben zweidimensionalen Translation-/Reflexions-Geometrie. Dies ist die erste explizite gemeinsame Generatorstruktur des aktuellen Strangs.

Firewall: `-P` ist indefinit; dies ist noch keine positive Object-X-Realisierung.

---

## 6. Prime-only-A2 — enger No-Go `×[M]`

Die positive Prime-Gram-Form

```math
\mathfrak P_X(v,w)=\sum_{n\le X}w_n\langle K_nv,K_nw\rangle
```

steigt **nicht** durch `\mathcal E` auf den Rang-2-Quotienten ab. `ker \mathcal E` ist zwar kanal-invariant, aber nicht im Radikal der Prime-Gram-Form.

Auf dem Quotienten fixiert

```math
D_n^*HD_n=-\lambda_n^2H
```

nur

```math
H=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix};
```

der Maßstab `b` bleibt frei. Die diskreten Daten `{w_n,lambda_n}` allein bestimmen daher nicht den absoluten Koeffizienten der `R_0`-Form.

Mit voller Translation-/Spiegelstruktur ist die Form dagegen kanonisch: `R_0=\mathcal E^*(-P)\mathcal E`.

---

## 7. Aktuelle Default-Priorität: POSITIVE-DILATION

### Gate A — `GENERATOR-CLASS / POSITIVE-DILATION-CLASS`

Vor jedem No-Go eine natürliche, enge Klasse positiver Erweiterungen/Intertwiner festschreiben, die aus der bereits identifizierten Struktur

```text
(C^2, rho, P, E), Prime channels K_n, Prime AR(1), log|D|-geometry
```

gebaut werden darf.

Die Klasse muss positive Konstruktion und negativen Ausgang beide vorab zulassen.

### Gate B — `OX-GEN-A2' / POSITIVE-DILATION`

Frage:

> Kann die kanonische indefinite Rang-2-Geometrie `(C^2,rho,P,E)` intrinsisch in die positive Prime-/`log|D|`-Featuregeometrie eingebettet oder als Schur-/Defektterm einer positiven Erweiterung realisiert werden — ohne `Q_{B_a}`, RH oder eine rückwärts definierte Positivitätswurzel?

Positive Antwort: erster expliziter gemeinsamer Prime-/Archimedean-Baustein **mit positiver Umgebung**.

Negative Antwort: Klassen-No-Go nur für die vorher definierte natürliche Klasse.

### Gate C — `OX-GEN-B`

Erst nach A2': `r_1` und/oder den dominanten Skalar `c_aI` in dieselbe gemeinsame Geometrie einbeziehen.

### Parallel — Spur B

Prime-Power-AR(1)/Martingal-Faktorisierung als eigenständigen RH-unabhängigen Satz verschriftlichen; ausdrücklich nicht als Objekt X.

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

```text
OX-GEN partial geometry ?[O]
        |
        | --candidate-input only-->
        v
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

Keine `candidate-input`-Kante ist als logische Implikation zu lesen.

---

## 9. Separate Nebenfronten

### R37/G4c

Separat offen; Beziehung zur OX-GEN-/X-Route unresolved.

### Historische R43-COND-/FD23-/Flagfragen

Weiterhin in ihren eigenen Quantoren offen, aber keine Voraussetzungen des direct fixed-pair-C6-Abschlusses und keine Default-Priorität.

### PR #91

Analytischer Source-descent/Weil-separation-Draft. Kein unabhängiger Exact-Head-GREEN wird übertragen.

### SW1 salvage / PR #49

Candidate-only Nebenfront; kein stiller Merge.

---

## 10. Gesperrte Interpretationen

Nicht reaktivieren:

- PR91-Zeugenmatrix Rang 1;
- `3/4` als bloße Dämpfung;
- Vier-Boundary-Erklärung;
- cross-prime als Fensterrand;
- „Nichtunitarität = Hub“;
- matched cutoff als Objekt-X-Mechanismus;
- OX-REN/OX-REN' als Hauptfront;
- klassische `H^{1/2}`-/Douglas-Terminologie für `1/|x-y|`;
- globaler Kollaps von `||I-W^*W||`;
- `0.603` als Konstante;
- weitere reine OX-GRAM-Existenztests;
- Prime-only-Rang-2-Gram ohne zusätzliche Quotientenstruktur;
- Behauptung, die Rang-2-Generatorstruktur erkläre bereits `r_1` oder `c_aI`.

---

## 11. Falsifikations-/Rollback-Regeln

- **Gemeinsame Generatoridentitäten fallen:** OX-GEN-A und darauf beruhende Dilatationsfront neu auditieren; Prime-AR(1), C6 und Object-X-Ziel bleiben getrennt.
- **Eine definierte POSITIVE-DILATION-CLASS fällt:** nur diese Klasse ist ausgeschlossen.
- **Prime-AR(1)-Algebra fällt:** alle darauf gestützten OX-GEN-Interpretationen neu auditieren.
- **R37/G4c fällt:** R37-Pfad fällt; keine automatische Wirkung auf OX-GEN/C6.
- **PR91 fällt:** nur sein Kandidat fällt.
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
GENERATOR-CLASS / POSITIVE-DILATION-CLASS
OX-GEN-A2' / POSITIVE-DILATION
OX-GEN-B
r_1 / regular archimedean correction
scalar block c_a I in intrinsic geometry
genuine X candidate
exact full Weil-Gram identity
Object-X realization
Weil-criterion scope verification
RH
R37/G4c [separate]
```

Historische Nebenfragen bleiben über Audits, Git-Historie und Registry-/Problemprovenienz zugänglich; sie werden hier nicht zur Default-Priorität erhoben.
