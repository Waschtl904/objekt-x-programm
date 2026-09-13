# Abhängigkeitsgraph (DAG) — Objekt X / POS-DIL

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
OX-GEN / POS-DIL
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

Mit

```math
\mathcal Ev=(E_+(v),E_-(v)),
\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}),
```

und

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
D_n=\lambda_nS,
\qquad
S=\operatorname{diag}(-1,1),
```

gilt

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E.
```

Archimedischer Teil:

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
r_0(\log n)=-4\lambda_n^2.
```

Mit

```math
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad J=-P
```

gilt

```math
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle.
```

```text
2D translation representation rho
        |
        + --odd finite difference--> Prime channel K_n
        + --negative character-----> archimedean r_0''
        + --reflection pullback----> R_0 = E^* J E
```

Prime-only-A2 bleibt `×[M]` im engen Scope: die volle positive Prime-Gram-Form descendiert nicht durch `E`, und `{w_n,lambda_n}` allein fixieren die absolute `R_0`-Normierung nicht.

---

## 6. POS-DIL-1A — natürliche Companion-Klasse

Die zwei vorhandenen Involutionen sind

```math
P^2=S^2=I,
\qquad PSP=-S,
\qquad S=2\rho'(0).
```

Für eine positive Hermiteform `M` auf `C^2`:

```math
PMP=M,
\qquad SMS=M
```

zwingt

```math
M=tI.
```

Die zusätzliche Blockpositivität

```math
\begin{pmatrix}M&J\\J&M\end{pmatrix}\succeq0
```

ist genau für `t>=1` möglich. Somit:

```text
P- and S-symmetric positive companions
        |
        | --rigidity-->
        v
M=tI
        |
        | --minimal block positivity-->
        v
M_min=I  ✓[M]
```

Demgegenüber gilt für volle positive Translationinvarianz:

```math
\rho(t)^*M\rho(t)=M\ \forall t,\quad M\succeq0
\quad\Longrightarrow\quad
M=0.
```

```text
exact unitary Hilbertization of full rho on positive rank 2
        |
        v
×[M]  [enger Scope]
```

---

## 7. POS-DIL-1C — Prime-moment Hilbertisierung `✓[M]`

Für jede endliche nichtleere Prime-Power-Menge `N` setze

```math
\kappa_N=\sum_{n\in N}w_n\lambda_n^2,
```

und

```math
V_Nv=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}
\in\bigoplus_{n\in N}\mathbb C^2.
```

Dann

```math
\boxed{\|V_Nv\|^2=\|\mathcal Ev\|^2=|E_+(v)|^2+|E_-(v)|^2.}
```

Mit `\mathbb P_N=\oplus P` gilt gleichzeitig

```math
\boxed{R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.}
```

Für `n=p^k`, `q_p=p^{-1/2}`:

```math
\boxed{\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.}
```

Damit sitzt die Kanalindex-Amplitude exakt auf `flat minus AR(1)-root`.

```text
Prime channels K_n + Weil weights + E
        |
        | --normalized moment postcompression-->
        v
positive Hilbert target H_N
        |                         |
        | norm                    | target involution P_N
        v                         v
|E_+|^2+|E_-|^2  ✓[M]        R_0  ✓[M]
```

**Firewall:** Der volle positive Prime-Gramoperator descendiert weiterhin nicht durch `E`; `log|D|`, `r_1` und `c_aI` sind nicht integriert. Daher:

```text
OX-GEN-A2' overall  ✓[M]_part
```

---

## 8. Aktuelle Hauptfront — POS-DIL-2 / FEATURE-SHORTING

```text
POS-DIL-1 prime-moment Hilbertization  ✓[M]
        |
        | --requires contractive placement in existing positive features-->
        v
POS-DIL-2 / FEATURE-SHORTING ?[O]
        |
        +-------------------------------+
        |                               |
        | PASS                          | FAIL
        v                               v
contractive canonical shorting     class obstruction
inside G_a^+                       [POS-DIL-1 survives]
        |
        | --candidate-input only-->
        v
OX-GEN-B ?[O]
  incorporate r_1 and/or c_a I
```

Eine erste scharfe Testform ist

```math
\|\mathcal Ev\|^2\stackrel?\le G_a^+(v).
```

Nach Fixierung der positiven Featureabbildung `\mathcal F_a^+` lautet die typkorrekte Intertwinerform:

```math
C_a\mathcal F_a^+v=V_{N_a}v,
\qquad \|C_a\|\le1,
```

wobei `C_a` **vorwärts** aus vorhandenen Daten gebaut werden muss.

---

## 9. True Object-X path

```text
OX-GEN / POS-DIL partial geometry
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

Keine candidate-input-Kante ist eine Theoremimplikation.

---

## 10. Separate / parked routes

- **R37/G4c:** separat offen; Beziehung zu OX-GEN/Object X unresolved.
- **Historische R43-COND-/FD23-/Flagfragen:** eigene offene Quantoren, nicht aktuelle Voraussetzung.
- **PR #91:** Source-descent/Weil-separation Draft ohne übertragenes unabhängiges Exact-Head-GREEN.
- **PR #49 / SW1 salvage:** Candidate-only Nebenfront; kein stiller Merge.

---

## 11. Gate-Regel

Ein Falsifikationsgate zählt nur, wenn **beide Ausgänge vorher logisch möglich** waren. Reine Reformulierungen bekannter Positivität, gefittete Witness-Werte und post-hoc-Faktorisierungen sind kein Object-X-Fortschritt.

---

## Kanonische Einstiegspunkte

- [CURRENT-FRONT](../CURRENT-FRONT.md)
- [AKTUELLER_STAND](AKTUELLER_STAND.md)
- [FORSCHUNGS_ROADMAP_AKTUELL](FORSCHUNGS_ROADMAP_AKTUELL.md)
- [ACTIVE_THEOREM_REGISTRY](ACTIVE_THEOREM_REGISTRY.md)
- [OBJEKT_X_AKTUELLE_ARBEITSDEFINITION](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md)
