# Objekt X — kanonische Forschungsroadmap v2.7

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Operative Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Verfügbare Basis

- fixed-pair Strong Terminal/C6 im ungeraden P11-Graphraum;
- Prime-Power-AR(1)/Weil-Tail:
  ```math
  C_{jk}^{(p)}=\sqrt{w_{p,j}w_{p,k}}p^{-|j-k|/2},
  \qquad T_q^*T_q+uu^*=R_q;
  ```
- lokalisierte Normalform
  ```math
  Q_{B_a}=G_a^+-N_a,
  \qquad N_a=c_aI+C_a.
  ```

Arbiträre rückwärts definierte Kontraktorexistenz bleibt kein Object-X-Gate.

## 2. OX-GEN-A / POS-DIL-1

Die gemeinsame Generator-Ebene erfüllt

```math
\mathcal ET_t=\rho(t)\mathcal E,
\qquad
\mathcal EK_n=D_n\mathcal E,
```

```math
R_0(v,w)=\langle\mathcal Ev,-P\mathcal Ew\rangle.
```

Die Prime-moment-Hilbertisierung liefert

```math
\|V_Nv\|^2=\|\mathcal Ev\|^2,
\qquad
R_0(v,w)=\langle V_Nv,\mathbb P_NV_Nw\rangle.
```

AR(1)-Brücke:

```math
\sqrt{w_{p,k}}D_{p^k}=\sqrt{\log p}(1-q_p^k)S.
```

## 3. POS-DIL-2A — lokale bestehende G-Masse allein fällt

Bei `a=1/2` ist unit-gain Shorting in der unveränderten `G_{1/2}^+`-Norm unmöglich. Notwendiger Massendefekt:

```math
\delta_0>\frac5{32}.
```

## 4. POS-DIL-2B/2C-R — äußerer Prime-Shell löst die Positivitätsfrage auf 0<a<=1

Geometrisch:

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\},
\qquad c_n=\frac12\log n.
```

```math
H_a^{out}(v,w)=\sum_{n\in\mathscr S_a^{out}}
\frac{\Lambda(n)}{\sqrt n}\langle K_nv,K_nw\rangle.
```

Jeder äußere Kanal ist auf dem Fenster reine lokale Masse:

```math
\|K_nv\|^2=2\|v\|^2.
```

Damit

```math
H_a^{out}(v)=2B_a^{out}\|v\|^2.
```

Für alle `0<a<=1` liefert der vorhandene Log-Multiplikator

```math
G_a^+(v)\ge(-\log a)\|v\|^2,
```

während

```math
\|\mathcal Ev\|^2\le4\sinh(a)\|v\|^2.
```

Eine endliche siebenintervallige Prime-Power-Analyse beweist

```math
\boxed{-\log a+2B_a^{out}>4\sinh(a)}
```

für den gesamten Bereich `0<a<=1`. Daher

```math
\boxed{
\|\mathcal Ev\|^2
\le G_a^+(v)+H_a^{out}(v)
\qquad(0<a\le1),
}
```

und folglich

```math
\boxed{
\begin{pmatrix}
G_a^++H_a^{out}&R_0\\
R_0&G_a^++H_a^{out}
\end{pmatrix}\succeq0.
}
```

**Radiusfrage geschlossen `✓[M]`.**

## 5. Aktuelle Default-Priorität: POS-DIL-2C-B / EXACT-SHELL-BOOKING

Die positive Geometrie ist nun auf dem gesamten lokalen Radiusbereich stark genug. Der Engpass ist ausschließlich die exakte Bilanz:

> Kann `H_a^{out}` in die gemeinsame Prime-/Archimedean-Geometrie eingebaut werden, ohne die vollständige Weilform durch zusätzliche Energie zu verändern?

Priorisierte Reihenfolge:

### 5.1 Vor-Cutoff-Rekonstruktion

Rekonstruiere exakt, wo die Identitätsmasse der Kanäle `c_n>a` vor der lokalisierten Cutoff-/Normalform-Umschreibung sitzt.

### 5.2 Shell-Differenzen / Teleskopierung

Prüfe aufeinanderfolgende Shift-Shells auf eine kanonische Differenzzerlegung, bei der äußere positive Masse und Gegenmasse exakt bilanzieren.

### 5.3 AR(1)-Root/Hub

Prüfe pro Primast

```math
T_q^*T_q+uu^*=R_q
```

als mögliche Gegenbuchungsgeometrie. Insbesondere ist die bereits gefundene Quotientenamplitude

```math
1-u_k=1-q_p^k
```

auf eine Buchungsrolle zu testen.

### 5.4 Erst danach c_a / r_1

Eine Verbindung des Shell-Skalars mit `c_aI` oder dem regulären `r_1`-Block darf erst nach einer exakten Bilanz untersucht werden. Keine stille Identifikation.

## 6. Danach: vollständiger Object-X-Pfad

```text
exact shell booking ?[O]
        |
        | --candidate-input only-->
        v
OX-GEN-B / genuine X candidate ?[O]
        |
        v
exact full Weil-Gram identity ?[O]
        |
        v
Object-X realization ?[O]
        |
        v
Weil-criterion scope ?[O]
        |
        v
RH
```

## 7. Firewalls

- Radiuspositivität ist nicht exakte Weil-Buchung.
- Außenshellmasse ist nicht bereits `c_aI`.
- POS-DIL-2A war nur ein No-Go gegen die unveränderte `G^+`-Norm.
- Keine Registry-Promotion durch Merge/CI.
- PR #91, PR #49 und R37/G4c bleiben separat.

## 8. Explizit offen

```text
POS-DIL-2C-B exact shell booking / renormalization
OX-GEN-B
r_1
c_a I in intrinsic geometry
genuine X candidate
exact full Weil-Gram identity
Object-X realization
Weil-criterion scope
RH
```
