# Objekt X — kanonische Forschungsroadmap v3.4

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Operative Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Gesicherte Basis

- COMMON-JUMP gemeinsame Prime-/archimedische Featurefamilie `✓[M]`;
- `Q_0` support-erhaltende Nullpolparametrisierung `✓[M]`;
- zentrierter Prime-overlap `✓[M]`;
- exakte per-prime AR(1)-Fasern `✓[M]`.

Auf Nullpol:

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v).
```

## 2. Gate D0 — methodische No-Gos

### Independent shift/block norm sum

Für `a<log n<2a` gilt `||S_{log n}||=1/2`. Deshalb wächst der unabhängige Normbudget-Term mindestens wie

```math
2e^a(1+o(1)).
```

Eine rein skalare archimedische Untergrenze kann auf den wachsenden Nullpolräumen nicht entsprechend wachsen. Diese Beweisklasse ist `×[M]`.

### Raw Prolate factor

Ein `a`-unabhängiger Konzentrationsfaktor gegen die rohe Prime-Multiplikatoramplitude `~4e^a` ändert die Skala nicht. Prolate bleibt nur nach arithmetischer Zentrierung als möglicher Hilfsmechanismus zulässig.

## 3. Gate D1 — Nullpol correlation gauge `✓[M]`

Für

```math
C_v(t)=\langle T_tv,v\rangle
```

gilt auf `D_NP(a)`

```math
\boxed{
\int_0^{2a}2\cosh(t/2)\operatorname{Re}C_v(t)dt=0.
}
```

Damit kann die Prime-Power-Maßseite exakt um `2 cosh(t/2)dt` zentriert werden.

## 4. Gate D2 — pole-cleared Prime discrepancy `✓[M]`

```math
d\mathfrak D(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dt)
-2\cosh(t/2)dt.
```

Dann

```math
\boxed{
\mathcal O_a(v)
=2\int\operatorname{Re}C_v(t)d\mathfrak D(t)
=-2\int_0^{2a}\mathfrak D(t)
\frac{d}{dt}\operatorname{Re}C_v(t)dt.
}
```

Der PNT-Hauptterm ist herauszentriert:

```math
\mathfrak D(T)=o(e^{T/2}).
```

## 5. Gate D3 — analytic fingerprint `✓[M]`

Für `Re(s)>1/2`:

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=-\frac{d}{ds}\log\left[(s^2-1/4)\zeta(s+1/2)\right].
}
```

Damit entfernt die Nullpolzentrierung exakt die beiden Pole `z=0,1` der endlichen Stelle. In `xi`-Notation ist derselbe Ausdruck der zero-bearing logarithmic derivative plus der bekannte Gamma-Korrektor.

## 6. Gate D4 — NP-CORR `?[O]`

Nicht gesucht ist eine absolute Majorante von `D(T)`: polynomialer Wuchs von `D` ist bereits RH-hart.

Gesucht ist eine **Korrelationsungleichung** für die spezielle Testklasse

```text
positive-definite autocorrelations
compact support [-2a,2a]
null-pole cosh moment = 0
Q0-parametrizable origin
```

gegen das signierte Maß `dD`.

Vorab zulässige Mechanismen:

1. Signwechsel/Oszillation von `D`;
2. positive-definite constraints on `C_v`;
3. `Q_0`-Transport von `C_v'`;
4. per-prime AR(1) als lokale Faserung von `dnu`;
5. centered Toeplitz/Paley-Wiener/Prolate estimates;
6. explizite Falsifikationszeugen, falls die Korrelationsroute scheitert.

## 7. Rolle der AR(1)-Struktur

Die Identität

```math
O_{p,a}^{(N)}=(\log p)(R_{p^{-1/2}}^{(N)}-I)
```

bleibt wichtig, aber nicht als separat zu normierender Block. Sie soll die lokale Vorzeichen-/Markov-Struktur von `dD` erklären und mit der bereits bewiesenen Prime-Power-AR(1)/Weil-tail-Faktorisierung reconnecten.

## 8. Object-X-Pfad

```text
COMMON-JUMP ✓[M]
   |
centered Prime overlap ✓[M]
   |
null-pole cosh gauge ✓[M]
   |
pole-cleared discrepancy ✓[M]
   |
NP-CORR anti-correlation ?[O]
   |
all-a NP-GAP ?[O]
   |
RH
```

## 9. Firewalls

- polynomial absolute control of `D` is already RH-hard;
- no return to independent shift/block norm summation;
- raw Prolate constant-factor concentration is not a sufficient main mechanism;
- AR(1) identification alone is not yet the collective inequality;
- Registry/Arbeitsdefinition unverändert.
