# Aktueller Stand — Objekt X / POS-DIL

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](DAG.md), [Registry](ACTIVE_THEOREM_REGISTRY.md).

## 1. Basis

Fixed-pair Strong Terminal/C6 liegt im ungeraden P11-Graphraum vor. Die Prime-Power-Seite besitzt die exakte AR(1)/Weil-Tail-Struktur

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
\qquad T_q^*T_q+uu^*=R_q.
```

Für `a<=1`:

```math
Q_{B_a}=G_a^+-N_a,
\qquad N_a=c_aI+C_a.
```

## 2. OX-GEN-A / POS-DIL-1

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Die Prime-moment-Abbildung realisiert

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

## 3. POS-DIL-2A

Die unveränderte lokale Form `G_{1/2}^+` ist für unit-gain Shorting zu klein. Eine Plateaufolge liefert einen exakten positiven Massendefekt `delta_0>5/32`.

## 4. Erster äußerer Prime-Shell

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
\qquad c_n=\frac12\log n,
```

```math
H_a^{out}(v,w)=\sum_{n\in\mathscr S_a^{out}}
\frac{\Lambda(n)}{\sqrt n}\langle K_nv,K_nw\rangle.
```

Für jeden Shell-Kanal gilt

```math
\|K_nv\|^2=2\|v\|^2,
```

also

```math
H_a^{out}(v)=2B_a^{out}\|v\|^2.
```

Dies ist intrinsische Prime-Masse aus echten Kanälen.

## 5. POS-DIL-2C-R — vollständige Radiusfortsetzung `✓[M]`

Für `0<a<=1`:

```math
G_a^+(v)\ge(-\log a)\|v\|^2,
```

```math
\|\mathcal Ev\|^2\le4\sinh(a)\|v\|^2.
```

Eine siebenintervallige elementare Analyse der Prime-Power-Shellwechsel beweist

```math
-\log a+2B_a^{out}>4\sinh(a)
\qquad(0<a\le1).
```

Daher für **jeden** Radius im lokalen Scope:

```math
\boxed{
\|\mathcal Ev\|^2
\le G_a^+(v)+H_a^{out}(v),
\qquad0<a\le1.
}
```

und

```math
\boxed{
\begin{pmatrix}
G_a^++H_a^{out}&R_0\\
R_0&G_a^++H_a^{out}
\end{pmatrix}\succeq0.
}
```

Kanonische Quelle: `audits/P11_POS_DIL_2C_EXTERIOR_SHELL_RADIUS_0_1_2026-09-13.md`.

## 6. Neue einzige POS-DIL-Hauptfrage

**POS-DIL-2C-B / EXACT-SHELL-BOOKING `?[O]`**:

Wie kann die positive Außenkanalenergie in einer exakten gemeinsamen Prime-/Archimedean-Geometrie bilanziert werden, ohne die vollständige Weilform künstlich zu vergrößern?

Priorität:

1. Außenkanalmasse vor der Cutoff-Umschreibung rekonstruieren.
2. Shell-Differenzen/Teleskopierung untersuchen.
3. AR(1)-Root/Hub-Gegenbuchung prüfen.
4. Rolle von `1-u_k` prüfen.
5. Erst danach mögliche Verbindung zu `c_aI`.

Weiter offen: exakte Shell-Buchung, `r_1`, `c_aI`, genuine X candidate, volle Weil-Gram-Identität, Object X und RH.
