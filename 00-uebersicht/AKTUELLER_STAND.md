# Aktueller Stand — Objekt X / OX-GEN

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

## 5. OX-GEN-A — gemeinsam erzeugte Rang-2-Geometrie `✓[M]`

Definiere

```math
E_\pm(v)=\int e^{\pm x/2}v(x)\,dx,
\qquad \mathcal Ev=(E_+(v),E_-(v)).
```

Für Translationen `(T_t v)(x)=v(x+t)` gilt

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\rho(t)=\operatorname{diag}(e^{-t/2},e^{t/2}).
```

Mit

```math
K_n=T_{\frac12\log n}-T_{-\frac12\log n},
\qquad
\lambda_n=n^{1/4}-n^{-1/4}
```

folgt **ohne Fensterrandterm**

```math
E_\pm(K_nv)=\mp\lambda_nE_\pm(v).
```

Suzukis elementarer archimedischer Teil ist zugleich das negative Charakter derselben Darstellung:

```math
\boxed{r_0''(t)=-\operatorname{tr}\rho(t),
\qquad r_0(\log n)=-4\lambda_n^2.}
```

Mit dem Austauschoperator `P(E_+,E_-)=(E_-,E_+)` gilt

```math
\boxed{R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle_{\mathbb C^2}.}
```

Prime-Kanäle und `r_0` sind damit zwei exakte Funktoren derselben zweidimensionalen Translation-/Reflexions-Geometrie.

## 6. Prime-only-A2 aus `{w_n,lambda_n}` `×[M]` im engen Scope

Die volle positive Prime-Gram-Form descendiert nicht auf `v -> (E_+,E_-)`, weil `ker \mathcal E` nicht in ihrem Radikal liegt.

Die Quotientenkovarianz

```math
D_n^*HD_n=-\lambda_n^2H
```

fixiert nur

```math
H=\begin{pmatrix}0&b\\\bar b&0\end{pmatrix};
```

der Maßstab `b` bleibt frei. Die diskreten Daten `{w_n,lambda_n}` allein bestimmen den absoluten Koeffizienten der `R_0`-Form daher nicht.

Mit voller Translation-/Spiegelstruktur ist die Form hingegen kanonisch: `R_0=\mathcal E^*(-P)\mathcal E`.

## 7. Nächste Arbeitsfolge

1. **GENERATOR-CLASS / POSITIVE-DILATION-CLASS:** natürliche positive Erweiterungs-/Intertwinerklasse für `(C^2,rho,P,E)` festschreiben.
2. **OX-GEN-A2' / POSITIVE-DILATION:** die kanonische indefinite Rang-2-Geometrie in die positive Prime-/`log|D|`-Featuregeometrie einbetten oder die definierte Klasse ausschließen.
3. **OX-GEN-B:** danach `r_1` und/oder `c_aI` in dieselbe gemeinsame Geometrie einbeziehen.
4. Parallel: AR(1)/Martingal-Faktorisierung als eigenständigen RH-unabhängigen Satz verschriftlichen.

Weiter offen: genuine X candidate, volle Weil-Gram-Identität, Object-X-Realisierung, Weil-Kriterium-Scope und RH.

**Governance:** Merge ist keine Registry-Promotion. Historische R43-/R37-/NEU-Dokumente bleiben Provenienz, nicht operative Arbeitsanweisung.
