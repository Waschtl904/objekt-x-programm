# Abhängigkeitsgraph (DAG)

> **Stand (Governance):** 7. September 2026; mathematische Darstellung unverändert.<br>
> **Rolle:** kompakte operative Abhängigkeits- und Firewall-Struktur.  
> **Keine Beweisautorität.** Status/Provenienz stehen im [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md), volatile PR-/SHA-Daten in [ACTIVE_FRONT.yaml](ACTIVE_FRONT.yaml), die ausführliche Strategie in [FORSCHUNGS_ROADMAP_AKTUELL.md](FORSCHUNGS_ROADMAP_AKTUELL.md).

---

## 1. Kantenregel

Logische Kanten:

- `A ⇔ B` — bewiesene Äquivalenz;
- `A ⇒ B` — bewiesene Implikation;
- `A ?⇒ B` — offene Implikation.

Forschungs-/Beweisabhängigkeiten sind ausdrücklich beschriftet:

- `A --uses--> B` — A verwendet B;
- `A --reduces-to--> B` — A ist auf B zurückgeführt;
- `A --sufficient-route--> B` — A ist ein hinreichender Weg zu B;
- `A --candidate-input--> B` — A ist nur Kandidatenbaustein für B;
- `A --open-bridge--> B` — die Verbindung selbst ist offen.

Ein unbeschriftetes `->` wird in diesem DAG nicht verwendet.

---

## 2. Operativer Strong-Terminal-Pfad

R38–R42 werden hier nicht durch Pfeile als vermeintliche Theoremimplikationskette verbunden. Sie bilden die eingefrorene Forschungs-/Provenienzkette gemäß Registry.

```text
[R38, R39, R40, R41, R42]
        |
        | --reduces-to-->
        v
R43 FIXED-NORMAL STRONG-TERMINAL GATE ?[O]
```

Exakter Registry-Governance-String für R38–R42:

```text
FROZEN — independently verified AI-GREEN
```

Dieser String ist gemäß Registry eine projektinterne Reviewer-/Governance-Buchung und nicht automatisch ein formaler `independent GREEN (cross-model/certificate/human)`-Subtyp.

R43 bleibt OPEN.

---

## 3. R43 — strukturierter Direktweg

PR-Nummern sind nur Provenienz und deshalb **keine Knoten**.

### 3.1 Exakte Draft-source Resultate

```text
R43-COND-SCHUR-NEGATIVE-PART-LEAKAGE-BOUND
  source: active-stack base audit

R43-COND-GEOMETRIC-MEAN-RESOLVENT-FACTORIZATION
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND
  uses: R43-COND-SCHUR-NEGATIVE-PART-LEAKAGE-BOUND

R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL
R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS
R43-COND-NORMALIZED-GEOMETRIC-TRANSPORT-CONTRACTION
  uses: R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND
```

Die exakten PR-/Head-Zuordnungen und belegten GitHub-Mergestates stehen ausschließlich in `ACTIVE_FRONT.yaml`; `base` bewahrt die historische Review-Basis, `github_base` das separat gebuchte GitHub-Ziel und `merged_head_sha` den tatsächlich gemergten Head, getrennt von historischen Abhängigkeitspins. **Draft-source IDs** bleiben historische Quellbezeichnungen, keine aktuellen GitHub-Statusangaben. Die Registry bleibt bei diesem Governance-Abgleich unverändert; kein Merge erzeugt Registry-Promotion.

Die jüngsten XBAND-Audits sind in [CURRENT-FRONT, Abschnitt 2](../CURRENT-FRONT.md#2-r43-stack-und-integrationsstand) ausschließlich als lokale Diagnostik verlinkt; sie erzeugen hier keine neuen DAG-Knoten oder Kanten.

### 3.2 Offene quantitative Reduktion

```text
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
        |
        | --reduces-to-->
        +---------------- R43-COND-TRANSPORTED-COLLAR-MASS-DECAY ?[O]
        |
        +---------------- R43-COND-TWO-HARD-CHANNEL-SATURATED-DECAY ?[O]
```

Falls beide benötigten Zweige in der richtigen Quantorenform geschlossen werden, muss ihre exakte Komposition zum Leakage-Decay separat gebucht werden; die Roadmap nimmt diese Komposition nicht stillschweigend vorweg.

Danach bleibt die direkte Flag-Brücke ausdrücklich offen:

```text
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
        |
        | --open-bridge-->
        v
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN
        |
        | --sufficient-route-->
        v
projected B-FLAGDYN / FD23-compatible control ?[O]
        |
        | --sufficient-route-->
        v
B-FLAGTIGHT ?[O]
```

**Firewall:** structured-vector Kontrolle ist nicht automatisch operatorweite `B-METINC-COND`-Kontrolle.

---

## 4. R43 — stärkerer Operator-/Spectral-Width-Weg

```text
B-METINC-WIDTH ?[O]
  uses:
    - B-METINC-COND ?[O]
    - B-METINC-GEO  ?[O]
    - B-METINC-NEW  ?[O]

B-METINC-WIDTH ?[O]
        |
        | --sufficient-route-->
        v
B-FLAGMOD ?[O]
```

Scheitert `B-METINC-WIDTH`, folgt daraus nicht das Scheitern von B-FLAGMOD oder Strong Terminal; eine direkt projizierte Route bleibt möglich.

---

## 5. Tightness / Sign / Strong Terminal

Mit

\[
Q_{m,U}=W_U^*P_mW_U,
\qquad
q_m(U)=\langle\varepsilon_R,Q_{m,U}\varepsilon_R\rangle,
\]

gilt im gebuchten Scope

\[
\mathrm{B\!-\!FLAGTIGHT}\Longleftrightarrow\lim_m\limsup_U q_m(U)=0.
\]

Der aktuell verfolgte hinreichende Weg lautet:

```text
[B-FLAGDYN, B-FLAGMOD, B-FLAGPHASE]
        |
        | --sufficient-route-->
        v
B-FLAGTIGHT ?[O]
        |
        | --reduces-to-->
        v
B-SIGN / B-ORIENT ?[O]
        |
        | --open-bridge within current R43 route-->
        v
Strong Terminal / C6 ?[O]
```

Die letzte Darstellung ist eine Forschungsroute; nur ausdrücklich separat gebuchte Äquivalenzen/Implikationen dürfen logisch gelesen werden.

---

## 6. Separater R37-Pfad

```text
R37 finite/algebraic certificate
        |
        | --reduces-to within R37-->
        v
G4c: real segment → holomorphic annulus identity → Laurent uniqueness ?[O]
```

**Firewall:** R38–R43 dürfen R37/G4c nicht rückwirkend promoten.

Die Beziehung von R37/G4c zu einer späteren Object-X-Realisierung ist derzeit **unresolved**. Deshalb gibt es in diesem DAG **keine Kante** von R37/G4c zum X-Pfad.

---

## 7. Finite-level / SW1

Die universelle positive finite-level Cross-Gram-/SW1-Route ist in ihrem gebuchten Scope negativ entschieden. Salvage-/Wedge-Fragen bleiben mögliche Nebenfronten.

Dieser Pfad beweist weder Strong Terminal noch dessen Negation und erzeugt kein Object-X-/RH-No-Go.

---

## 8. Objekt-X-Hauptarchitektur

Die aktuelle Arbeitsdefinition steht ausschließlich in [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).

R37/G4c ist wegen ungeklärter Abhängigkeit **nicht** an diese Grafik angeschlossen.

```text
finite-level constraints
        |
        | --candidate-input-->
        v
GENUINE X CANDIDATE ?[O]

Strong Terminal result
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]

GENUINE X CANDIDATE ?[O]
        |
        | --requires separate proof-->
        v
EXACT FULL WEIL-GRAM IDENTITY ?[O]
        |
        | --component of realization together with
        |    intrinsicity + test class + normalization-->
        v
OBJECT-X REALIZATION ?[O]
        |
        | ⇒ by the Gram identity
        v
Q_W(f,f) = ||T_X f||² ≥ 0
        |
        | --requires exact Weil-scope verification-->
        v
E — WEIL-CRITERION-SCOPE-VERIFICATION ?[O]
        |
        | --unlocks exact classical criterion application-->
        v
RH
```

Keine linke Front impliziert automatisch einen X-Kandidaten, Objekt X oder RH.

---

## 9. Aktuelle offene Forschungsfragen

```text
ROADMAP-HARD11                          research-subquestion
ROADMAP-HARD22                          research-subquestion
FD23-MINIMAL-CONDITION                  research-question
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN      open-bridge
ROADMAP-R37-G4C-DEPENDENCY              research-question
```

Diese ROADMAP-Labels sind keine kanonischen Theorem-IDs und tragen daher keinen aus der Registry importierten `math_status`.

---

## Kanonische Einstiegspunkte

- [CURRENT-FRONT](../CURRENT-FRONT.md)
- [ACTIVE_FRONT](ACTIVE_FRONT.yaml)
- [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md)
- [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)
- [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)
