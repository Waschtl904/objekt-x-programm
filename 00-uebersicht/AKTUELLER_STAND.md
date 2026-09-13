# Aktueller Stand — Objekt X / OX-GEN

> **Stand:** 13. September 2026; Registry unverändert.
> Diese Datei ist die kurze operative Zusammenfassung. Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](DAG.md), [Registry](ACTIVE_THEOREM_REGISTRY.md), [Arbeitsdefinition](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).

## 1. Strong Terminal / C6

Der positive Wurzelanker plus R42.51 liefert Strong Terminal/C6 für jedes feste `0<R<S` im **ungeraden P11-Graphraum**.

Nicht enthalten: Radienuniformität, Operatornormkonvergenz, vollständiger gerader Sektor, Objekt-X-Realisierung oder RH. Historische R43-COND-/FD23-Fragen und R37/G4c bleiben getrennte Nebenfragen.

## 2. Prime-Power-Struktur

Exakt gilt

```math
C_{jk}^{(p)}=(\log p)p^{\min(j,k)}p^{-3(j+k)/4},
\qquad C_{kk}^{(p)}=(\log p)p^{-k/2}.
```

Mit `q_p=p^{-1/2}` folgt die Weil-dekorierte AR(1)-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}q_p^{|j-k|},
\qquad T_q^*T_q+uu^*=R_q.
```

Die P11-Restseite besitzt die exakte Weil-Tail-Normalform. Cross-prime Root-Gram ist fensterloser Bulk, kein Boundaryterm.

## 3. Endliche OX-GRAM-Normalform

Für `a<=1` liegt

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a
```

vor. `G_a^+` besteht aus positiven Prime-Kanal-, Log-Multiplikator- und logarithmischen `log|D|`-Formen.

Die bloße Existenz eines kontraktiven Faktors ist kein nichtzirkulärer Objekt-X-Gate: Bei bereits bekannter lokaler Positivität kann er rückwärts aus `Q_{B_a}` definiert werden. Offen ist **Kanonizität**, nicht Existenz.

## 4. CERT-HARDEN geschlossen

Vor Merge von PR #98 waren auf demselben Exact Head GREEN:

- gehärteter Normalisierungsvergleich Realraum/Fourier für `a=0.5,0.8,1.0` mit expliziten Bernoulli-/sinc-Restbällen, Arb-Cutoffs und fail-closed Residualtests;
- Gate 2 mit Arb 512 Bit, Dirichletbasis `N<=14`, drei Radien, beiden Paritäten und **42/42** strikt positiven Cholesky-Blöcken.

Das sind endliche Zertifikate, kein unendlichdimensionaler Positivitäts- oder RH-Beweis.

## 5. Aktuelle Hauptfront OX-GEN

Suzukis Kernteil liefert exakt

```math
R_0(v,v)
=-2\left(\int\cosh\frac x2\,v\right)^2
+2\left(\int\sinh\frac x2\,v\right)^2.
```

Dieselbe Exponentialfamilie erscheint in `p^{-1/2}=e^{-\log p/2}`, der AR(1)-Korrelation und den Weilgewichten.

**OX-GEN:** Kann der archimedische Rang-2-Defekt als intrinsischer Rand-/Defektterm derselben Exponentialstruktur konstruiert werden, die die Prime-Power-Geometrie normiert, ohne die fertige Weilform oder RH rückwärts zu verwenden?

`R_1` und der Skalarblock `c_aI` bleiben offen.

## 6. Nächste Arbeitsfolge

1. **OX-GEN-A:** bei `a=0.5` die `cosh/sinh`-Momentfunktionale in der Prime-/`log|D|`-Featuregeometrie isolieren.
2. **GENERATOR-CLASS:** natürliche Generator-Klasse vor einem No-Go festschreiben.
3. **OX-GEN-B:** expliziten Intertwiner oder Klassen-No-Go suchen.
4. Parallel: AR(1)/Martingal-Faktorisierung als eigenständigen RH-unabhängigen Satz verschriftlichen.

Weiter offen bleiben genuine X candidate, exakte volle Weil-Gram-Identität, Object-X-Realisierung, Weil-Kriterium-Scope und RH.

**Governance:** Merge ist keine Registry-Promotion. `ACTIVE_FRONT.yaml` bleibt historisches Stackledger; `STATUS.md`, `INDEX.md` und ältere NEU-/R43-Fronten sind Provenienz, nicht operative Arbeitsanweisung.
