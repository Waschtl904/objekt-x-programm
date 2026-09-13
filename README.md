# Objekt-X-Programm

*Ein lakatosianisches Forschungsjournal zur Riemannschen Hypothese.*

Gesucht wird eine gemeinsame arithmetisch-analytische Hilbert-/Gram-Geometrie für Primzahlpotenzen und archimedischen Beitrag der Weil-Form. Arbeitsname: **Objekt X**.

> **Stand: 13. September 2026.**  
> COMMON-JUMP liefert eine gemeinsame positive Featurearchitektur. Nach Prime-Zentrierung und Nullpol-Autokorrelationszentrierung ist der harte arithmetische Rest eine pole-cleared Prime-Diskrepanz, die gegen eine stark eingeschränkte Autokorrelationsklasse gepaart wird. RH bleibt offen.

## Hier beginnen

1. [CURRENT-FRONT](CURRENT-FRONT.md)
2. [Pole-cleared Prime discrepancy](audits/P11_NP_DISCREPANCY_POLE_CLEARED_CORRELATION_2026-09-13.md)
3. [Prime-overlap AR(1)](audits/P11_NP_OVERLAP_AR1_FIBERIZATION_2026-09-13.md)
4. [COMMON-JUMP](audits/P11_NP_COMMON_JUMP_GRAM_2026-09-13.md)
5. [Roadmap](00-uebersicht/FORSCHUNGS_ROADMAP_AKTUELL.md)

## 1. Gemeinsame Geometrie

Auf der Nullpolklasse

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

reduziert COMMON-JUMP die Weilform auf

```math
Q_W(v)=\mathcal A(v)-\mathcal O_a(v),
```

```math
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
```

Der erste Gamma-Kanal wird durch `Q_0=-partial_x^2+1/4` support-erhaltend lokalisiert; vollständige Blöcke einer Primzahl sind exakt zentrierte AR(1)-Matrizen.

## 2. Zwei Methoden sind ausgeschieden

### Unabhängige Shift-/Blocknormsummation

Für `a<log n<2a` ist die scharfe komprimierte Shift-Norm `1/2`. Damit wächst der separate Normbudget-Term mindestens wie

```math
2e^a(1+o(1)).
```

Diese all-window-Beweisklasse ist `×[M]`.

### Raw-amplitude Prolate

Ein konstanter Zeit-Frequenz-Konzentrationsfaktor gegen einen rohen Prime-Multiplikator mit Amplitude `~e^a` ändert die Skala nicht. Prolate ist nur nach arithmetischer Zentrierung ein zulässiger Hilfsmechanismus.

## 3. Nullpol liefert eine exakte Korrelations-Gauge

Setze

```math
C_v(t)=\langle T_tv,v\rangle.
```

Aus `E_+=E_-=0` folgt

```math
\boxed{
\int_0^{2a}2\cosh(t/2)\operatorname{Re}C_v(t)dt=0.
}
```

Damit kann aus dem Prime-Power-Maß exakt der glatte Anteil `2 cosh(t/2)dt` entfernt werden, ohne den quadratischen Wert auf `D_NP(a)` zu ändern.

## 4. Pole-cleared Prime discrepancy

Definiere

```math
\boxed{
d\mathfrak D(t)
=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(dt)
-2\cosh(t/2)dt.
}
```

Dann

```math
\boxed{
\mathcal O_a(v)
=2\int_0^\infty\operatorname{Re}C_v(t)d\mathfrak D(t).
}
```

Kumulativ:

```math
\boxed{
\mathfrak D(T)
=\sum_{\log n\le T}\frac{\Lambda(n)}{\sqrt n}
-4\sinh(T/2).
}
```

Der PNT-Hauptterm `~2e^{T/2}` cancelt. Die rohe exponentielle Prime-Masse ist also **nicht** der kanonische Rest auf Nullpol.

## 5. Der Zeta-Fingerabdruck ist exakt

Für `Re(s)>1/2`:

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=-\frac{\zeta'}{\zeta}\left(s+\frac12\right)
-\frac1{s-1/2}-\frac1{s+1/2}.
}
```

Also

```math
\boxed{
\mathcal L[d\mathfrak D](s)
=-\frac{d}{ds}\log[(s^2-1/4)\zeta(s+1/2)].
}
```

Die Nullpol-Zentrierung entfernt auf der Prime-Seite genau die beiden Polfaktoren `z=0,1`.

## 6. Exakte Korrelationsform

Mit Stieltjes-Integration gilt

```math
\boxed{
\mathcal O_a(v)
=-2\int_0^{2a}\mathfrak D(t)
\frac{d}{dt}\operatorname{Re}C_v(t)dt.
}
```

Damit lautet die Hauptfrage nicht mehr „wie groß ist die Prime-Summe?“, sondern:

> Wie koppelt die **pole-cleared arithmetische Diskrepanz** an Ableitungen kompakt getragener positiver-definiter Autokorrelationen mit Nullpol-Zwang?

## 7. Warum das Problem trotzdem RH-hart bleibt

Unter RH folgt aus dem klassischen Chebyshev-Fehlerterm

```math
\mathfrak D(T)=O(T^3).
```

Umgekehrt würde bereits ein polynomialer Absolutbound `D(T)=O(T^K)` für ein fixes `K` RH implizieren. Deshalb ist das nächste Ziel **keine** absolute Diskrepanzmajorante, sondern eine signed anti-correlation inequality für die spezielle Testklasse.

## 8. Neue Hauptfront

```text
COMMON-JUMP / Q0                         ✓[M]
per-prime AR(1) fibers                  ✓[M]
null-pole autocorrelation gauge         ✓[M]
pole-cleared Prime discrepancy          ✓[M]
independent norm-sum route              ×[M]
raw-amplitude constant-Prolate route    ×[M]
NP-DISCREPANCY / anti-correlation       ?[O]
forward Object-X architecture           ✓[M]_part
full positive Object-X / RH             ?[O]
```

Die bevorzugte Route kombiniert Signstruktur von `D(t)`, positive Definitheit der Autokorrelation, `Q_0`-Transport und die lokalen AR(1)-Fasern. Prolate/Toeplitz ist nur auf der **zentrierten** Diskrepanz weiterzulassen.

## Firewalls

- polynomialer Absolutbound für `D` wäre bereits RH-hart;
- AR(1)-Identifikation allein ist noch keine globale Antikorrelation;
- bekannte Kleinfensterpositivität wird nicht als Neuheit beansprucht;
- Registry und Objekt-X-Arbeitsdefinition bleiben ohne separate Promotion unverändert.

Lizenz: [CC BY 4.0](LICENSE).