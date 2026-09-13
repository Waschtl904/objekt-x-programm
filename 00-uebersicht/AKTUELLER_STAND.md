# Aktueller Stand — Objekt X / NULLPOL-COMMON

> **Stand:** 13. September 2026; Registry unverändert.  
> Details: [CURRENT-FRONT](../CURRENT-FRONT.md), [Common-Jump-Audit](../audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md), [Roadmap](FORSCHUNGS_ROADMAP_AKTUELL.md), [DAG](DAG.md).

## 1. Nullpol-Scope

```math
E_-(v)=M(v)(0),\qquad E_+(v)=M(v)(1).
```

Auf `D_NP=ker M(0) cap ker M(1)` verschwinden `R_0` und `E`. Die globale Weil-Vorzeichenbedingung bleibt dort nach Connes–Consani Proposition C.1 RH-äquivalent.

## 2. Gemeinsame Jump-Geometrie `✓[M]`

Für

```math
K_t=T_{t/2}-T_{-t/2}
```

gilt

```math
K_t^*K_t=2I-T_t-T_{-t}.
```

Archimedes und Primzahlpotenzen benutzen exakt diese eine Familie:

```math
\mu_a
=
\frac{e^{-t/2}}{1-e^{-2t}}dt
+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}.
```

Die zugehörige positive Featureabbildung `X_a` erfüllt

```math
\langle X_av,X_aw\rangle
=
\int_0^\infty\frac{e^{-t/2}}{1-e^{-2t}}
\langle K_tv,K_tw\rangle dt
+
\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
\langle K_{\log n}v,K_{\log n}w\rangle.
```

## 3. Exakte Schwelle

```math
\kappa_*
=\log\pi-\psi(1/4)
=\log(8\pi)+\gamma+\frac\pi2,
```

```math
\Gamma_a
=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}+\kappa_*.
```

## 4. Exakte Weil-Normalform für alle `a>0`

Für `supp(v),supp(w) subset [-a,a]`:

```math
\boxed{
Q_W(v,w)
=
\langle Ev,PEw\rangle
+
\langle X_av,X_aw\rangle
-
\Gamma_a\langle v,w\rangle.
}
```

Auf Nullpol:

```math
\boxed{
Q_W(v,w)
=
\langle X_av,X_aw\rangle
-
\Gamma_a\langle v,w\rangle.
}
```

Dies ist eine vorwärts konstruierte gemeinsame Prime-/archimedische Hilbert-Geometrie. Keine RH-Annahme geht in die Identität ein.

## 5. Was dadurch geschlossen wird

```text
NP-R1 separate generator search          geschlossen/subsumiert ✓[M]
NP-COMMON common feature geometry        ✓[M]
NP-SCALAR cutoff-gauge covariance        ✓[M]
```

`log|D|`, `R_1`, Prime shifts und die Exterior-shell-Buchung sind verschiedene Darstellungen derselben zentrierten Jump-Gram-Struktur.

## 6. Neuer Hauptengpass — NP-GAP

```math
\lambda_{NP}(a)
=
\inf_{0\ne v\in C_c^\infty(-a,a)\cap D_{NP}}
\frac{\|X_av\|^2}{\|v\|_2^2}.
```

Offen ist genau

```math
\boxed{\lambda_{NP}(a)\ge\Gamma_a\quad\text{für alle }a>0.}
```

Für die Familie aller Fenster ist dies die verbleibende RH-äquivalente Spektralgap-/Frame-Frage. Ein einzelnes fixes `a` wird nicht als RH-äquivalent behauptet.

## 7. Status

```text
common jump-Gram architecture               ✓[M]
exact all-a normal form                      ✓[M]
forward Object-X candidate architecture      ✓[M]_part
sharp NP-GAP                                 ?[O]
full positive Object-X / RH                  ?[O]
publication novelty                          ?[O]
```

OX-GEN-A bleibt exakte Polschicht; POS-DIL #101--#105 bleibt auxiliary full-class geometry.