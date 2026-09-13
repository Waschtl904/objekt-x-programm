# Aktueller Stand — Objekt X / POS-DIL

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](DAG.md), [Registry](ACTIVE_THEOREM_REGISTRY.md), [Arbeitsdefinition](OBJEKT_X_AKTUELLE_ARBEITSDEFINITION.md).

## 1. Strong Terminal / C6

Für jedes feste `0<R<S` liegt Strong Terminal/C6 im ungeraden P11-Graphraum vor. Keine Radienuniformität, Operatornormkonvergenz, vollständige Object-X-Realisierung oder RH-Folgerung.

## 2. Prime-Power-/AR(1)-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad
T_q^*T_q+uu^*=R_q.
```

Die P11-Restseite besitzt die exakte Weil-Tail-Normalform. Cross-prime Root-Gram ist fensterloser Bulk.

## 3. OX-GRAM

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

Die bloße Existenz eines rückwärts aus `Q` definierten Kontraktors ist kein Object-X-Gate. CERT-HARDEN ist im dokumentierten endlichen Scope geschlossen.

## 4. OX-GEN-A `✓[M]`

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
r_0''(t)=-\operatorname{tr}\rho(t),
\qquad
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Prime-only-A2 aus `{w_n,lambda_n}` bleibt `×[M]` im engen Scope.

## 5. POS-DIL-1

Die natürliche Companion-Symmetrie erzwingt `M=tI`; minimale Blockpositivität liefert `M=I`. Volle positive `rho`-Invarianz erzwingt dagegen `M=0`.

Für jede endliche nichtleere Prime-Power-Menge `N`:

```math
V_Nv=\kappa_N^{-1/2}(\sqrt{w_n}\,\mathcal EK_nv)_{n\in N},
\qquad
\kappa_N=\sum_{n\in N}w_n\lambda_n^2.
```

Dann

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

`OX-GEN-A2'`: insgesamt `✓[M]_part`.

## 6. POS-DIL-2A — unit-gain bestehende Featureform `×[M]`

Bei `a=1/2` verletzt eine explizite gerade Plateaufolge

```math
\|\mathcal Ev\|^2\le G_{1/2}^+(v).
```

Grenzwerte:

```math
\|\mathcal Ev_\varepsilon\|^2
\to32\sinh^2\frac14,
\qquad
G_{1/2}^+(v_\varepsilon)
\to1+\sqrt2(\log2)^2,
```

mit

```math
32\sinh^2\frac14>2>1+\sqrt2(\log2)^2.
```

Notwendiger Zusatzmassendefekt:

```math
\delta_0
=32\sinh^2\frac14-1-\sqrt2(\log2)^2
>\frac5{32}.
```

## 7. POS-DIL-2B — erster äußerer Prime-Shell `✓[M]` bei `a=1/2`

Definiere

```math
\mathscr S_a^{\rm out}
=\{n=p^k: a<c_n\le2a\},
\qquad c_n=\tfrac12\log n,
```

und

```math
H_a^{\rm out}(v,w)
=\sum_{n\in\mathscr S_a^{\rm out}}
\frac{\Lambda(n)}{\sqrt n}
\langle K_nv,K_nw\rangle.
```

Für `c_n>a` sind die beiden verschobenen Fenster disjunkt, also exakt

```math
\boxed{\|K_nv\|_2^2=2\|v\|_2^2.}
```

Damit

```math
H_a^{\rm out}(v)
=2B_a^{\rm out}\|v\|_2^2.
```

Bei `a=1/2` enthält der Shell insbesondere `3,4,5`. Aus diesen echten Prime-Kanälen plus dem vorhandenen Log-Multiplikator folgt für jedes nichttriviale `v`

```math
G_{1/2}^+(v)+H_{1/2}^{\rm out}(v)
>\frac83\|v\|_2^2.
```

Andererseits

```math
\|\mathcal Ev\|^2
\le4\sinh\frac12\|v\|_2^2
<\frac83\|v\|_2^2.
```

Also uniform auf der ganzen Testklasse:

```math
\boxed{
\|\mathcal Ev\|^2
\le G_{1/2}^+(v)+H_{1/2}^{\rm out}(v).
}
```

Mit `A_{1/2}^{out}=G_{1/2}^++H_{1/2}^{out}` folgt

```math
\boxed{
\begin{pmatrix}
A_{1/2}^{\rm out}&R_0\\
R_0&A_{1/2}^{\rm out}
\end{pmatrix}\succeq0.
}
```

Kanonische Quelle: `audits/P11_POS_DIL_2B_FIRST_EXTERIOR_PRIME_SHELL_2026-09-13.md`.

## 8. Bedeutung und Firewall

Dies ist der erste positive Reparaturbaustein nach dem POS-DIL-2A-No-Go, dessen Zusatzmasse vorwärts aus **echten Prime-Kanälen mit den kanonischen Weilgewichten** entsteht.

Noch offen:

- Radiusfortsetzung auf andere `a`;
- exakte Buchung/Renormalisierung der äußeren Kanäle in einer vollen Weil-Identität;
- `r_1` und `c_aI`;
- genuine X candidate, volle Weil-Gram-Identität, Object X, RH.

Die Shellmasse wird ausdrücklich **nicht** mit `c_aI` identifiziert.

## 9. Nächste Arbeitsfolge

1. **POS-DIL-2C / SHELL-BOOKING:** klären, wie der positive äußere Shell in einer exakten gemeinsamen Prime-/Archimedean-Geometrie bilanziert werden kann, ohne künstliche Zusatzenergie.
2. **POS-DIL-2C / RADIUS:** danach bzw. parallel die Dominanz für andere `0<a<=1` beweisen oder den Radiusbereich exakt bestimmen.
3. Root/Hub-/AR(1)-Teleskopierung und Shell-Differenzen als mögliche Gegenbuchung untersuchen.
4. Erst danach `r_1`/`c_aI` einbeziehen, wenn ihre Rolle vorwärts motiviert ist.

Registry unverändert; keine automatische Promotion durch Merge oder CI.
