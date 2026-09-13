# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie für Primzahlpotenzen und archimedischen Beitrag der Weil-Form. Arbeitsname: **Objekt X**.

> **Stand: 13. September 2026.**  
> COMMON-JUMP liefert eine gemeinsame positive Featurearchitektur. Nach exakter Zentrierung ist der verbleibende harte arithmetische Rest ein Prime-Power-Überlappungsoperator, dessen vollständige Blöcke pro Primzahl exakt AR(1)-Matrizen sind. RH bleibt offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [Prime-overlap AR(1)](audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md)
3. [Review correction / Prime overlap](audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md)
4. [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)
5. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## 1. Gemeinsame Geometrie

Für

```math
K_t=T_{t/2}-T_{-t/2}
```

entstehen Prime-Power- und archimedische Beiträge aus derselben positiven Jump-Familie. Auf der Nullpolklasse `D_NP` gilt exakt

```math
Q_W(v)=\|X_av\|^2-\Gamma_a\|v\|^2.
```

Der erste Gamma-Kanal wird durch

```math
Q_0=-\partial_x^2+1/4
```

support-erhaltend lokalisiert:

```math
A_{1/2}Q_0=-4\partial_x^2,
\qquad
Q_0:C_c^\infty(-a,a)\cong D_{NP}(a).
```

## 2. Korrekte Kleinfensterbuchung

Die eigene Architektur reproduziert analytisch Kleinfenster-Coercivity. Kleinfensterpositivität selbst ist jedoch nicht neu: Suzuki Theorem 1.4 beweist bereits eine stärkere volle-Klasse-Aussage.

```text
COMMON-JUMP/Q0 internal reproduction      ✓[M]_part
short-window positivity as new theorem    ×[M]
```

Ein eigener Arb-Gate prüft nur den expliziten projektinternen Schwellenwert `a_*`.

## 3. Exakte zentrierte Restform

Nach Cancellation der Prime-Diagonalmasse gilt

```math
\boxed{Q_W(v)=\mathcal A(v)-\mathcal O_a(v)}
```

mit

```math
\boxed{
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
Re\langle T_{\log n}v,v\rangle.
}
```

Die Wand ist damit nicht der nackte Skalar `Gamma_a`, sondern die kollektive Überlappung der inneren Prime-Power-Shifts.

## 4. Einzelshift: exakte Geometrie und No-Go

Für

```math
S_t=(T_t+T_{-t})/2
```

auf `L^2(-a,a)` liefert Faserung modulo `t`

```math
\boxed{
\|S_t\|=\cos\frac{\pi}{\lceil2a/t\rceil+1}
}
```

für `0<t<2a`. Dieselbe scharfe Norm ist bereits auf der Nullpolklasse erreichbar.

Daher:

```text
single-shift null-pole norm improvement   ×[M]
```

Ein Beweis kann also nicht aus unabhängigen besseren Einzelshift-Normen entstehen.

## 5. Vollständiger Block einer Primzahl ist exakt AR(1)

Für eine Primzahl `p` setze

```math
ell_p=log p,
q_p=p^{-1/2}.
```

Gruppiert man **alle** Potenzen `p^k` und fasert modulo `ell_p`, erhält man auf einer `N`-Punkt-Faser

```math
\boxed{
O_{p,a}^{(N)}=(\log p)(R_{q_p}^{(N)}-I_N),
\qquad
R_q^{(N)}=(q^{|j-k|})_{j,k}.
}
```

Das ist genau die Kac--Murdock--Szegő-/AR(1)-Korrelationsmatrix, die im früheren Prime-Power-Strang des Programms bereits unabhängig gefunden wurde.

Ihr zentrierter Symbolfaktor ist

```math
P_q(theta)-1
=\frac{2q(\cos theta-q)}{1-2q\cos theta+q^2},
```

also positiv genau im Niedrigfrequenzsektor

```math
|theta|<arccos(q).
```

## 6. Neue Hauptfrage: kollektive Prime-Interferenz

Für verschiedene Primzahlen `p!=r` ist

```math
log p/log r notin Q.
```

Die gefährlichen positiven AR(1)-Sektoren leben daher auf inkommensurablen logarithmischen Gittern.

Die neue Hauptfrage lautet:

> Wie stark kann dieselbe Funktion gleichzeitig in den positiven Niedrigfrequenzsektoren vieler verschiedener Prime-Gitter konzentriert sein?

Formal bleibt

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\sum_pO_{p,a}|_{D_{NP}(a)}
\quad\forall a>0
}
```

zu beweisen.

Die bevorzugte Route verbindet diese exakte Faserform mit der bereits bewiesenen Prime-Power-AR(1)/Markov-/Weil-tail-Geometrie.

## Status

```text
COMMON-JUMP common geometry                  ✓[M]
Q0 first-channel / support map               ✓[M]
centered Prime-overlap                       ✓[M]
exact single-shift fibers                    ✓[M]
single-shift null-pole improvement           ×[M]
exact per-prime AR(1) fibers                 ✓[M]
collective multi-prime suppression           ?[O]
forward Object-X candidate architecture      ✓[M]_part
full positive Object-X / RH                  ?[O]
```

## Firewalls

- Inkommensurabilität allein ist noch keine quantitative Ungleichung.
- Der Einzelshift-No-Go gilt nicht gegen kollektive Multi-Prime-Mechanismen.
- Bekannte Kleinfensterpositivität wird nicht als Neuheit beansprucht.
- Endliche Ritz-Minima beweisen keinen globalen Gap.
- Registry und Objekt-X-Arbeitsdefinition bleiben ohne separate Promotion unverändert.

Lizenz: [CC BY 4.0](LICENSE).