# Abhängigkeitsgraph (DAG)

> **Stand:** 6. September 2026  
> **Rolle:** kompakte operative Abhängigkeits- und Firewall-Struktur.  
> **Keine Beweisautorität.** Status/Provenienz stehen im [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md), volatile PR-/SHA-Daten in [ACTIVE_FRONT.yaml](ACTIVE_FRONT.yaml), die ausführliche Strategie in [FORSCHUNGS_ROADMAP_AKTUELL.md](FORSCHUNGS_ROADMAP_AKTUELL.md).

---

## 1. Kantenregel

Logische Kanten:

- `A ⇔ B` bewiesene Äquivalenz;
- `A ⇒ B` bewiesene Implikation;
- `A ?⇒ B` offene Implikation.

Forschungsabhängigkeiten (`uses`, `reduces-to`, `sufficient-route`, `candidate-input`) sind **keine** logischen Implikationen.

---

## 2. Operativer Strong-Terminal-Pfad

```text
R38 -> R39 -> R40 -> R41 -> R42
                         |
                         | reduces Strong Terminal
                         v
                 R43 fixed-normal gate ?[O]
```

R38–R42 bleiben gemäß ihrer exakten Provenienz frozen/reviewed; R43 bleibt OPEN.

---

## 3. R43 — zwei quantitative Wege

### 3.1 Strukturierter Direktweg

```text
R43-COND-SCHUR-NEGATIVE-PART-LEAKAGE-BOUND
        | provenance PR55
        v
R43-COND-GEOMETRIC-MEAN-RESOLVENT-FACTORIZATION
R43-COND-RESOLVENT-TRANSPORTED-LEAKAGE-BOUND
        | provenance PR57
        v
R43-COND-GOOD-NORMAL-COLLAR-PLUS-TAIL
R43-COND-TWO-HARD-DIAGONAL-NORMAL-CHANNELS
        | provenance PR58
        |
        +--> transported collar mass decay ?[O]
        +--> hard diagonal channels (1,1)+(2,2) saturated decay ?[O]
        |
        v
R43-COND-RESOLVENT-STRUCTURED-SATURATED-LEAKAGE-DECAY ?[O]
        |
        | OPEN direct quantitative composition bridge
        v
projected B-FLAGDYN / FD23-compatible control ?[O]
        |
        | sufficient route
        v
B-FLAGTIGHT ?[O]
```

**Firewall:** structured-vector control ist nicht automatisch operatorweite `B-METINC-COND`-Kontrolle.

### 3.2 Stärkerer Operator-/Spectral-Width-Weg

```text
B-METINC-COND ?[O]
B-METINC-GEO  ?[O]
B-METINC-NEW  ?[O]
        |
        v
B-METINC-WIDTH ?[O]
        |
        | sufficient route
        v
B-FLAGMOD ?[O]
```

Scheitert `B-METINC-WIDTH`, folgt daraus nicht das Scheitern von B-FLAGMOD oder Strong Terminal; eine direkt projizierte Route bleibt möglich.

---

## 4. Tightness / Sign / Strong Terminal

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

Schematisch:

```text
B-FLAGDYN / B-FLAGMOD + B-FLAGPHASE
                  |
                  | sufficient route
                  v
             B-FLAGTIGHT ?[O]
                  |
                  v
           B-SIGN / B-ORIENT ?[O]
                  |
                  v
           Strong Terminal / C6 ?[O]
```

---

## 5. Separater R37-Pfad

```text
R37 finite/algebraic certificate
        |
        v
G4c: real segment -> holomorphic annulus identity -> Laurent uniqueness ?[O]
```

**Firewall:** R38–R43 dürfen R37/G4c nicht rückwirkend promoten.

Die Abhängigkeit von R37/G4c zu einer späteren Object-X-Realisierung ist derzeit **unresolved**; daher keine prerequisite-Kante.

---

## 6. Finite-level / SW1

Die universelle positive finite-level Cross-Gram-/SW1-Route ist in ihrem gebuchten Scope negativ entschieden. Salvage-/Wedge-Fragen bleiben mögliche Nebenfronten.

Dieser Pfad beweist weder Strong Terminal noch dessen Negation und erzeugt kein Object-X-/RH-No-Go.

---

## 7. Objekt-X-Hauptarchitektur

Die aktuelle Arbeitsdefinition steht ausschließlich in [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).

```text
finite-level constraints -----+
                              |
Strong Terminal result -------+--> candidate-inputs --> genuine X candidate ?[O]
                              |                              |
R37 analytic information -----+                              | separate proof
                                                             v
                                                exact full Weil-Gram identity ?[O]
                                                             |
                                                             | + intrinsicity,
                                                             |   test class,
                                                             |   normalization
                                                             v
                                                Object-X realization ?[O]
                                                             |
                                                             | exact Weil-scope check
                                                             v
                                                Weil criterion / RH bridge
                                                             |
                                                             v
                                                            RH
```

Keine linke Front impliziert automatisch einen X-Kandidaten, Objekt X oder RH.

---

## 8. Aktuelle offene Forschungsfragen

```text
ROADMAP-HARD11                         research-subquestion
ROADMAP-HARD22                         research-subquestion
FD23-MINIMAL-CONDITION                 research-question
ROADMAP-BRIDGE-COND-DIRECT-FLAGDYN     open-bridge
ROADMAP-R37-G4C-DEPENDENCY              research-question
```

Diese ROADMAP-Labels sind keine kanonischen Theorem-IDs und erzeugen keinen Status.

---

## Kanonische Einstiegspunkte

- [CURRENT-FRONT](../CURRENT-FRONT.md)
- [ACTIVE_FRONT](ACTIVE_FRONT.yaml)
- [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md)
- [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)
- [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)
