# Aktueller Stand — Objekt X / POS-DIL

> **Stand:** 13. September 2026; Registry unverändert.  
> Kurze operative Zusammenfassung. Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](DAG.md), [Registry](ACTIVE_THEOREM_REGISTRY.md), [Arbeitsdefinition](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).

## 1. Strong Terminal / C6

Der positive Wurzelanker plus R42.51 liefert Strong Terminal/C6 für jedes feste `0<R<S` im **ungeraden P11-Graphraum**.

Nicht enthalten: Radienuniformität, Operatornormkonvergenz, vollständiger gerader Sektor, Objekt-X-Realisierung oder RH.

## 2. Prime-Power-Struktur

Exakt gilt

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad C_{kk}^{(p)}=(\log p)p^{-k/2},
```

und nach Weil-Diagonalnormalisierung

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2}.
```

Mit `q=p^{-1/2}`:

```math
T_q^*T_q=R_q-uu^*,
\qquad T_q^*T_q+uu^*=R_q.
```

Die P11-Restseite besitzt die exakte Weil-Tail-Normalform. Cross-prime Root-Gram ist fensterloser Bulk, kein Boundaryterm.

## 3. Endliche OX-GRAM-Normalform

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

Die bloße Existenz eines kontraktiven Faktors ist kein nichtzirkulärer Object-X-Gate; bei bekannter lokaler Positivität kann er rückwärts aus `Q_{B_a}` definiert werden. Offen ist **Kanonizität**.

## 4. CERT-HARDEN

Die endlichen Gate-1/Gate-2-Checker sind gehärtet und auf demselben Exact Head GREEN. Gate 2: Arb 512 Bit, `N<=14`, drei Radien, beide Paritäten, **42/42** strikt positive Cholesky-Blöcke.

Das ist kein globaler Positivitäts- oder RH-Beweis.

## 5. OX-GEN-A — gemeinsame Generator-Ebene `✓[M]`

Definiere

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad \mathcal Ev=(E_+(v),E_-(v)).
```

Für

```math
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}),
\qquad
K_n=T_{\frac12\log n}-T_{-\frac12\log n}
```

gilt

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=\lambda_n\operatorname{diag}(-1,1)\mathcal E.
```

Suzukis elementarer archimedischer Teil erfüllt

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad r_0(\log n)=-4\lambda_n^2.
```

Mit `P(E_+,E_-)=(E_-,E_+)` und `J=-P`:

```math
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle.
```

## 6. Prime-only-A2 `×[M]` im engen Scope

Die volle positive Prime-Gram-Form descendiert nicht auf `v -> (E_+,E_-)`, weil `ker \mathcal E` nicht in ihrem Radikal liegt. Die reine Quotientenkovarianz fixiert außerdem nur die off-diagonale Formklasse, nicht ihren absoluten Maßstab.

## 7. POS-DIL-1 — positiver Quotientenbaustein

Setze

```math
S=\operatorname{diag}(-1,1)=D_n/\lambda_n=2\rho'(0).
```

### Companion-Rigidität `✓[M]`

Die minimale natürliche Symmetrieklasse

```math
PMP=M,
\qquad SMS=M
```

zwingt

```math
M=tI.
```

Die Blockpositivität

```math
\begin{pmatrix}M&J\\J&M\end{pmatrix}\succeq0
```

ist genau für `t>=1` möglich. Also ist

```math
\boxed{M_{\min}=I.}
```

### Vollständige positive `rho`-Invarianz `×[M]`

Aus

```math
\rho(t)^*M\rho(t)=M
```

für alle `t` und `M>=0` folgt `M=0`. Eine exakte unitäre Hilbertisierung der vollen Boost-Repräsentation auf demselben positiven Rang-2-Raum ist damit ausgeschlossen.

### Prime-moment Hilbertisierung `✓[M]`

Für eine endliche nichtleere Prime-Power-Menge `N` setze

```math
\kappa_N=\sum_{n\in N}w_n\lambda_n^2,
\qquad
V_Nv=\kappa_N^{-1/2}
\bigl(\sqrt{w_n}\,\mathcal EK_nv\bigr)_{n\in N}.
```

Dann exakt

```math
\boxed{\|V_Nv\|^2=|E_+(v)|^2+|E_-(v)|^2,}
```

und mit `\mathbb P_N=\oplus P`

```math
\boxed{R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.}
```

Damit entstehen minimale positive Companion-Masse und `R_0` aus derselben gewichteten Prime-moment-Featureabbildung.

Für `n=p^k`, `q_p=p^{-1/2}` gilt zusätzlich

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S,
```

also exakt `flat minus AR(1)-root` auf der Kanalindex-Ebene.

**Status:** OX-GEN-A2' insgesamt `✓[M]_part`, nicht vollständig geschlossen.

## 8. Nächste Arbeitsfolge

1. **POS-DIL-2 / FEATURE-SHORTING:** prüfen, ob die kanonische Momentabbildung kontraktiv in der vollständigen positiven Featuregeometrie sitzt, insbesondere
   ```math
   \|\mathcal Ev\|^2\stackrel?\le G_a^+(v).
   ```
2. **OX-GEN-B:** danach `r_1` und/oder `c_aI` einbeziehen.
3. Parallel: AR(1)/Martingal-Faktorisierung als eigenständigen RH-unabhängigen Satz verschriftlichen.

Weiter offen: genuine X candidate, volle Weil-Gram-Identität, Object-X-Realisierung, Weil-Kriterium-Scope und RH.

**Governance:** Merge ist keine Registry-Promotion. Historische R43-/R37-/NEU-Dokumente bleiben Provenienz, nicht operative Arbeitsanweisung.
