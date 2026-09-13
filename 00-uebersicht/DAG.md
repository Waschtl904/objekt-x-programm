# Abhängigkeitsgraph (DAG) — Objekt X / OX-GEN

> **Stand:** 13. September 2026; Registry unverändert.  
> **Rolle:** kompakte operative Abhängigkeits- und Firewall-Struktur.  
> **Keine Beweisautorität.** Status/Provenienz: [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md), aktuelle Front: [CURRENT-FRONT](../CURRENT-FRONT.md), Strategie: [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md).

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

```text
fixed-pair Strong Terminal / C6  [verfügbarer scoped result]
        |
        | --candidate-input only-->
        v
GENUINE X CANDIDATE ?[O]
```

Scope: jedes feste `0<R<S`, ungerader P11-Graphraum. Keine Radienuniformität, Operatornormkonvergenz oder Object-X-/RH-Folgerung.

---

## 3. Exakte Prime-Power-Struktur

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad
C_{kk}^{(p)}=(\log p)p^{-k/2},
```

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
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
OX-GEN
```

---

## 4. Endliche Suzuki-/OX-GRAM-Normalform

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

```text
finite OX-GRAM identity
        |
        | --shows only reformulation-->
        v
contractor existence [closed/vacuous as X-gate]
```

Offen bleibt eine **kanonische, vorwärts konstruierte** gemeinsame Geometrie.

---

## 5. OX-GEN-A — gemeinsamer Translation-/Reflexions-Generator `✓[M]`

Setze

```math
\mathcal Ev=(E_+(v),E_-(v)),
\qquad
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx.
```

Dann

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}).
```

Für Prime-Power-Kanäle

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

gilt

```math
\mathcal EK_n
=\lambda_n\operatorname{diag}(-1,1)\mathcal E.
```

Archimedischer Teil:

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
r_0(\log n)=-4\lambda_n^2.
```

Mit Austausch/Spiegelung

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix}
```

gilt

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Operative Bedeutung:

```text
Prime AR(1) / Weil-Tail
        |
        | --candidate-input-->
        v
2D translation representation rho
        |
        + --odd finite difference--> Prime channel K_n
        |
        + --negative character-----> archimedean r_0''
        |
        + --reflection pullback----> R_0 = E^*(-P)E
```

Dies ist eine exakte gemeinsame Prime-/Archimedean-Generatorstruktur, aber `-P` ist indefinit und daher noch keine positive Object-X-Realisierung.

---

## 6. Prime-only-A2 — enger Klassen-No-Go `×[M]`

Die positive Prime-Gram-Form

```math
\sum_n w_n\langle K_n\cdot,K_n\cdot\rangle
```

**descendiert nicht** durch `\mathcal E`, weil `ker \mathcal E` nicht in ihrem Radikal liegt.

Auf dem Quotienten erzwingt

```math
D_n^*HD_n=-\lambda_n^2H
```

nur

```math
H=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix};
```

der Maßstab `b` bleibt frei.

```text
{w_n, lambda_n} alone
        |
        | --insufficient to fix absolute R_0 normalization-->
        v
Prime-only A2  ×[M]  [eng definierter Scope]
```

Mit voller Translation-/Reflexionsstruktur ist die Form hingegen kanonisch: `R_0=E^*(-P)E`.

---

## 7. Aktuelle Hauptfront — POSITIVE-DILATION

```text
OX-GEN-A common generator plane  ✓[M]
        |
        | --requires positive embedding/dilation-->
        v
GENERATOR-CLASS / POSITIVE-DILATION-CLASS ?[O]
        |
        +-------------------------------+
        |                               |
        | explicit positive dilation    | class no-go
        v                               v
OX-GEN-A2' geometry piece ?[O]     obstruction ?[O]
        |
        | --candidate-input only-->
        v
OX-GEN-B ?[O]
  incorporate r_1 and/or c_a I
```

Eine positive Antwort auf A2' wäre der erste explizite gemeinsame Prime-/Archimedean-Baustein **mit positiver Umgebung**. Eine negative Antwort gilt nur für die vorher definierte natürliche Klasse.

---

## 8. True Object-X path

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
        v
RH
```

No candidate-input edge is a theorem implication.

---

## 9. Separate / parked routes

- **R37/G4c:** separat offen; Beziehung zu OX-GEN/Object X unresolved.
- **Historische R43-COND-/FD23-/Flagfragen:** eigene offene Quantoren, nicht aktuelle Voraussetzung.
- **PR #91:** Source-descent/Weil-separation Draft ohne übertragenes unabhängiges Exact-Head-GREEN.
- **PR #49 / SW1 salvage:** Candidate-only Nebenfront; kein stiller Merge.

---

## 10. Gate-Regel

Ein Falsifikationsgate zählt nur, wenn **beide Ausgänge vorher logisch möglich** waren. Reine Reformulierungen bekannter Positivität, gefittete Witness-Werte und post-hoc-Faktorisierungen sind kein Object-X-Fortschritt.

---

## Kanonische Einstiegspunkte

- [CURRENT-FRONT](../CURRENT-FRONT.md)
- [AKTUELLER_STAND](AKTUELLER_STAND.md)
- [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md)
- [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)
- [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)
