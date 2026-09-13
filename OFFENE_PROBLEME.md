# Offene Probleme — NP-OVERLAP-AR1

> **Stand:** 13. September 2026.  
> Operative Quellen: [CURRENT-FRONT](CURRENT-FRONT.md), [Prime-overlap AR(1)](audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md), [Review correction](audits/P11_NP_GAP_REVIEW_CORRECTION_PRIME_OVERLAP_2026-09-13.md).

## Neu geschlossen

### Einzelshift-Geometrie `✓[M]`

```math
\|S_t\|
=\cos\frac{\pi}{\lceil2a/t\rceil+1}
```

für `0<t<2a`, und `S_t=0` für `t>=2a`.

### Einzelshift-Nullpolverbesserung `×[M]`

Dieselbe Top-Norm wird bereits auf `D_NP(a)` erreicht. Zwei Nullpolmomente beseitigen die unendlichdimensionale Top-Eigensphäre nicht.

**Konsequenz:** eine Summe unabhängiger Einzelshift-Normschranken kann die Nullpolstruktur nicht ausnutzen und ist als Hauptstrategie ausgeschieden.

### Vollständiger p-Block `✓[M]`

Für `q=p^{-1/2}`:

```math
\boxed{
O_{p,a}^{(N)}=(\log p)(R_q^{(N)}-I_N),
\qquad R_q^{(N)}=(q^{|j-k|}).
}
```

Der positive Sektor ist

```math
|theta|<arccos(q).
```

Damit ist die alte Prime-Power-AR(1)-Struktur exakt die Fasergeometrie des neuen Overlap-Problems.

---

## Priorität 0 — `[MULTIPRIME-AR1]` `?[O]`

Zu quantifizieren ist die gleichzeitige positive Energie derselben Funktion in den AR(1)-Blöcken vieler Primzahlen.

Da

```math
log p/log r notin Q
```

für `p!=r`, liegen die gefährlichen Niedrigfrequenzsektoren auf inkommensurablen Gittern.

### Pflichtfragen

1. Gibt es eine quantitative Uncertainty-/Frame-Ungleichung zwischen zwei oder mehreren `log p`-Faserungen?
2. Kann eine Funktion gleichzeitig nahe am positiven Topsektor von `R_{p^{-1/2}}-I` für viele `p` liegen?
3. Liefert die bekannte AR(1)-Inverse/Markov-Struktur eine gemeinsame Kontraktion?
4. Wie verändert der Q0-Sobolevtransport diese simultaneous-low-frequency-Frage?
5. Kann die Überlappungsbreite `delta_n=2a-log n` eine zusätzliche Randstrafe liefern?

---

## Priorität 1 — `[AR1-RECONNECT]`

Verbinde die exakte Faserform systematisch mit den bereits bewiesenen Prime-Power-Sätzen des Programms, insbesondere

```math
C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2}
```

und den Markov-/Weil-tail-Faktorisierungen.

Gesucht ist eine echte Ungleichung für `sum_p O_{p,a}`, nicht nur eine weitere Identifikation der Matrixklasse.

---

## Priorität 2 — `[ARCH-COUPLING]`

Der Zieloperator bleibt

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\sum_p O_{p,a}|_{D_{NP}(a)}.
}
```

Die archimedische Seite darf nicht getrennt von der kollektiven Prime-Seite optimiert werden, wenn dadurch nur mehr Einzelkanalmasse entsteht.

---

## Auxiliary

- finite Gamma-null ladder: strukturell zulässig, aber ohne Prime-overlap-Kontrolle Nebenfront;
- short-window Coercivity: intern `✓[M]_part`, Neuheitsclaim `×[M]`;
- Arb-`a_*`-Gate: numerisches Seitengate;
- finite Ritzwerte: nur Diagnostik/Falsifikationshilfe.

## Endziel

```text
collective multi-prime AR1 suppression
        |
        v
all-a NP-OVERLAP
        |
        v
global null-pole Weil positivity
        |
        v
RH
```

## Firewalls

Nicht behaupten:

- Einzelshift-No-Go widerlege kollektive Mechanismen;
- Inkommensurabilität allein liefere bereits einen quantitativen Bound;
- bekannte Kleinfensterpositivität sei neu;
- ein fixes Fenster sei RH-äquivalent;
- Object X oder RH seien bewiesen.
