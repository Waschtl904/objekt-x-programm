# Abhängigkeitsgraph (DAG) — Objekt X / OX-GEN

> **Stand:** 13. September 2026; Registry unverändert.  
> **Rolle:** kompakte operative Abhängigkeits- und Firewall-Struktur.  
> **Keine Beweisautorität.** Status/Provenienz stehen im [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md), die aktuelle Front in [CURRENT-FRONT](../CURRENT-FRONT.md), die Strategie in [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md).

---

## 1. Kantenregel

Logische Kanten:

- `A ⇔ B` — bewiesene Äquivalenz;
- `A ⇒ B` — bewiesene Implikation;
- `A ?⇒ B` — offene Implikation.

Forschungs-/Beweisabhängigkeiten:

- `uses`
- `reduces-to`
- `candidate-input`
- `requires`
- `open-bridge`
- `sufficient-route`

Ein PR ist Provenienz/Container, kein mathematischer DAG-Knoten.

---

## 2. Verfügbarer Strong-Terminal-Baustein

Im ausgewiesenen Scope gilt für jedes feste `0<R<S` im ungeraden P11-Graphraum Strong Terminal/C6 aus positivem Wurzelanker plus R42.51.

```text
fixed-pair Strong Terminal / C6  [verfügbarer scoped result]
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]
```

**Firewall:** Es existiert kein Satz `Strong Terminal ⇒ Objekt X`, und Strong Terminal ist nicht als notwendige Bedingung jeder denkbaren X-Realisierung bewiesen.

Historische R43-COND-/FD23-/Flagfragen bleiben Nebenrouten in ihrem eigenen Scope; sie öffnen den fixed-pair-C6-Abschluss nicht automatisch wieder.

---

## 3. Exakte Prime-Power-Struktur

Für jeden Primast:

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

Mit `q_p=p^{-1/2}`:

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}q_p^{|j-k|}.
```

Tail-/Root-Struktur:

```math
T_q^*T_q=R_q-uu^*,
\qquad
T_q^*T_q+uu^*=R_q.
```

P11-Restseite:

```math
R_R^*R_R=\sum_{p,k}w_{p,k}Z_{p,k,R}^*Z_{p,k,R}.
```

```text
Prime-Power AR(1) / Weil-Tail structure  ✓[M] in documented scope
        |
        | --candidate-input-->
        v
OX-GEN ?[O]
```

**Firewall:** Diese exakte Struktur ist noch keine Objekt-X-Realisierung.

---

## 4. Endliche Suzuki-/OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad
N_a=c_aI+C_a.
```

Die bloße Existenz eines Kontraktors, der `N_a` relativ zu `G_a^+` faktorisiert, ist bei bereits bekannter lokaler Positivität zirkulär konstruierbar und deshalb **kein** Object-X-Gate.

```text
finite OX-GRAM identity
        |
        | --shows only reformulation-->
        v
contractor existence [closed/vacuous as X-gate]
```

Was offen bleibt, ist eine **kanonische, vorwärts konstruierte** gemeinsame Geometrie.

---

## 5. OX-GEN — aktuelle Hauptfront

Suzukis Rang-2-Teil:

```math
R_0(v,v)
=-2\left(\int\cosh\frac x2\,v\right)^2
+2\left(\int\sinh\frac x2\,v\right)^2.
```

Dieselbe Exponentialfamilie erscheint in

```math
p^{-1/2}=e^{-\log p/2},
\qquad
R_p(j,k)=p^{-|j-k|/2},
\qquad
w_{p,k}=\log p\,p^{-k/2}.
```

Operativer DAG:

```text
Prime AR(1) / Weil-Tail structure
        |
        | --candidate-input-->
        v
OX-GEN-A ?[O]
  isolate cosh/sinh moments at a=0.5
        |
        | --requires-->
        v
GENERATOR-CLASS ?[O]
  define natural noncircular class before no-go
        |
        +------------------------------+
        |                              |
        | positive construction        | class no-go
        v                              v
OX-GEN-B geometry piece ?[O]      generator-class obstruction ?[O]
```

A positive OX-GEN result would be a **partial geometric building block**, not yet a full X candidate. A negative result applies only to the generator class fixed in advance.

`R_1` and the scalar block `c_aI` remain separate open pieces.

---

## 6. True Object-X path

```text
OX-GEN partial geometry ?[O]
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]
        |
        | --requires separate exact proof-->
        v
EXACT FULL WEIL-GRAM IDENTITY ?[O]
        |
        | --component of realization with intrinsicity,
        |    test class and normalization-->
        v
OBJECT-X REALIZATION ?[O]
        |
        | ⇒ by Gram identity
        v
Q_W(f,f)=||T_Xf||^2 >= 0
        |
        | --requires exact criterion-scope verification-->
        v
WEIL-CRITERION-SCOPE ?[O]
        |
        | --unlocks classical criterion if scope matches-->
        v
RH
```

No candidate-input edge may be read as a theorem implication.

---

## 7. Separate / parked routes

### R37/G4c

```text
R37 finite/algebraic certificate
        |
        | --reduces-to within R37-->
        v
G4c ?[O]
```

Relation to OX-GEN/Object X: unresolved. No edge is asserted.

### Historical R43 quantitative routes

COND, FD23, global variation, BR39, hard channels and related flag routes remain valid historical/open questions in their scopes, but are not current prerequisites for fixed-pair C6 or OX-GEN.

### PR #91

Source-descent/Weil-separation Draft. No independent Exact-Head GREEN has been promoted or transferred by PR #98.

### SW1 salvage / PR #49

Candidate-only side route. No automatic merge or Object-X implication.

---

## 8. Gate rule

A falsification gate counts as a genuine narrowing of the Object-X search space only when **both outcomes were logically possible before the test**.

Pure reformulations of known positivity, fitted witness values, or post-hoc factorizations are not Object-X progress.

---

## Kanonische Einstiegspunkte

- [CURRENT-FRONT](../CURRENT-FRONT.md)
- [AKTUELLER_STAND](AKTUELLER_STAND.md)
- [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md)
- [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)
- [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)
