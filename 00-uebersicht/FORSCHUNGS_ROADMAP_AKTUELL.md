# Objekt X — kanonische Forschungsroadmap v3.3

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Operative Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Gesicherte Architektur

COMMON-JUMP liefert auf Nullpol

```math
Q_W|_{NP}=X_a^*X_a-\Gamma_aI
```

mit gemeinsamer Translation-Differenzfamilie `K_t`. Q0 lokalisiert den ersten Gamma-Kanal exakt, und die höheren Kanäle besitzen den rigorosen `e^{-alpha a}`-Schur-Bound.

Die Kleinfenster-Coercivity ist eine interne Reproduktion bekannter Positivität, kein neuer Literatur-Satz.

## 2. Zentriertes all-window Problem

Exakt:

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
```

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
Re\langle T_{\log n}v,v\rangle.
```

Die Prime-Diagonalmasse ist wegzentriert. Ziel:

```math
(A_\infty-\kappa_*I)|_{D_{NP}(a)}\succeq O_a|_{D_{NP}(a)}.
```

## 3. Gate O1 — Einzelshift abgeschlossen `✓[M] / ×[M]`

Faserung modulo `t` gibt

```math
\|S_t\|=\cos\frac{\pi}{\lceil2a/t\rceil+1}.
```

Dieselbe scharfe Norm wird auf `D_NP(a)` erreicht. Daher ist eine Nullpol-Verbesserung einzelner Shiftkanäle ausgeschlossen:

```text
single-shift null-pole norm improvement  ×[M]
```

Unabhängige Einzelshift-Normabschätzungen sind nicht mehr Default-Strategie.

## 4. Gate O2 — vollständiger Block einer Primzahl `✓[M]`

Für

```math
ell_p=log p,
q_p=p^{-1/2}
```

ist die `N`-Punkt-Faser des vollständigen `p`-Blocks

```math
\boxed{
O_{p,a}^{(N)}=(\log p)(R_{q_p}^{(N)}-I),
\qquad R_q^{(N)}=(q^{|j-k|}).
}
```

Der positive Sektor des AR(1)-Symbols ist

```math
|theta|<arccos(q_p).
```

Damit ist die frühere Prime-Power-AR(1)-Struktur exakt in der neuen Hauptfront wiedergefunden.

## 5. Gate O3 — kollektive Multi-Prime-Interferenz `?[O]`

Für `p!=r` gilt

```math
log p/log r notin Q.
```

Die gefährlichen Niedrigfrequenzsektoren liegen also auf inkommensurablen logarithmischen Gittern.

Zu quantifizieren:

1. Wie groß kann die simultane positive AR(1)-Energie für viele Primzahlen sein?
2. Gibt es eine Frame-/uncertainty-Ungleichung zwischen den `log p`-Faserungen?
3. Kann die alte AR(1)/Markov-/Weil-tail-Faktorisierung eine gemeinsame Kontraktion liefern?
4. Welche Rolle spielen Parität und die Overlap-Breite `delta_n=2a-log n`?
5. Wie koppelt der Q0-Sobolevtransport diese Prime-Energien an den archimedischen Überschuss?

## 6. Gate O4 — Prime-Power AR(1) reconnect

Vergleiche die neue exakte Faseridentität systematisch mit den bereits bewiesenen Projektresultaten

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2}
```

und der Markov-/AR(1)-Faktorisierung. Ziel ist kein bloßer Strukturvergleich, sondern eine quantitative Mehrprimzahl-Ungleichung.

## 7. Auxiliary

Die finite Gamma-null ladder `{-2m,2m+1}` bleibt Connes--Consani-kompatibel, aber ohne Kontrolle des Prime-overlap nur Nebenfront.

## 8. Object-X-Pfad

```text
COMMON-JUMP ✓[M]
   |
centered Prime-overlap ✓[M]
   |
per-prime AR(1) fibers ✓[M]
   |
collective multi-prime suppression ?[O]
   |
all-a NP-OVERLAP ?[O]
   |
global null-pole Weil positivity
   |
RH
```

## 9. Numerik / Firewalls

- Ritz-Minima sind obere Schranken für das wahre Infimum.
- Der Arb-Gate für `a_*` ist nur ein short-window-Seitengate.
- Bekannte Kleinfensterpositivität nicht als Neuheit beanspruchen.
- Einzelshift-No-Go nicht zu einem No-Go für kollektive Multi-Prime-Mechanismen überdehnen.
- Registry/Arbeitsdefinition unverändert.
