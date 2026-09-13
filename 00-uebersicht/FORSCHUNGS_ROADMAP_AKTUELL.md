# Objekt X — kanonische Forschungsroadmap v3.2

> **Stand:** 13. September 2026; Registry unverändert.  
> **Keine Beweisautorität.** Operative Front: [CURRENT-FRONT](../CURRENT-FRONT.md).

## 1. Gesicherte Basis

Auf der Nullpolklasse

```math
D_{NP}=\ker M(0)\cap\ker M(1)
```

liefert COMMON-JUMP für jedes `a>0`

```math
Q_W|_{NP}=X_a^*X_a-\Gamma_aI.
```

Prime powers und archimedischer Gamma-Anteil werden von derselben Translation-Differenzfamilie

```math
K_t=T_{t/2}-T_{-t/2}
```

erzeugt. Status `✓[M]`.

## 2. Q0-Kanalstruktur `✓[M]`

Für

```math
A_\alpha=\int_0^\infty e^{-\alpha t}K_t^*K_tdt
```

gilt

```math
A_\alpha=\frac2\alpha L(L+\alpha^2)^{-1},
\qquad L=-\partial_x^2.
```

Mit `Q_0=L+1/4`:

```math
A_{1/2}Q_0=4L,
\qquad
Q_0:C_c^\infty(-a,a)\cong D_{NP}(a)
```

support-erhaltend.

Die höhere Kanalabschätzung

```math
A_\alpha\succeq\frac2\alpha e^{-\alpha a}I
```

ist durch einen expliziten Schur-Test geschlossen.

## 3. Short-window-Korrektur

Die Architektur liefert intern einen analytischen Kleinfenster-Bound. Dies ist **keine neue Kleinfensterpositivität in der Literatur**, da Suzuki Theorem 1.4 eine stärkere volle-Klasse-Aussage beweist.

```text
COMMON-JUMP/Q0 reproduction                ✓[M]_part
novel short-window Weil theorem            ×[M]
```

Der projektinterne Schwellenwert `a_*` wird durch einen Arb-Exact-Head-Gate zertifiziert; Zielbracket:

```math
0.1033784517534<a_*<0.1033784517535.
```

## 4. Neue kanonische Restform `✓[M]`

Setze

```math
\mathcal A(v)
=\int_0^\infty h(t)\|K_tv\|^2dt-\kappa_*\|v\|^2.
```

Dann auf Nullpol:

```math
\boxed{Q_W(v)=\mathcal A(v)-\mathcal O_a(v)}
```

mit

```math
\boxed{
\mathcal O_a(v)
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\operatorname{Re}\langle T_{\log n}v,v\rangle.
}
```

Die Prime-Diagonalmasse ist exakt wegzentriert. Nur überlappende Prime-Power-Shifts verbleiben.

## 5. Neue Default-Priorität — NP-OVERLAP

Der all-window Satz ist exakt

```math
\boxed{
(A_\infty-\kappa_*I)|_{D_{NP}(a)}
\succeq
\mathbf O_a|_{D_{NP}(a)}
\quad\forall a>0.
}
```

### Gate O1 — Spektrum des overlap operators

Bestimme positive Spektralmasse, Parität und Extremalrichtungen von

```math
\mathbf O_a
=2\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
\frac{T_{\log n}+T_{-\log n}}2
```

nach Kompression auf `D_NP(a)`.

### Gate O2 — Q0-Sobolev transport

Für `v=Q_0u` gilt

```math
\operatorname{Re}\langle T_tv,v\rangle
=\operatorname{Re}\langle T_tu'',u''\rangle
+\frac12\operatorname{Re}\langle T_tu',u'\rangle
+\frac1{16}\operatorname{Re}\langle T_tu,u\rangle.
```

Suche daraus scharfe supportabhängige Korrelationseinschränkungen.

### Gate O3 — Randüberlappung

Expliziere die Abhängigkeit vom Überlappungsradius

```math
\delta_n=2a-\log n.
```

Insbesondere muss die Methode die exakte Auslöschung für `delta_n<=0` und den Übergang `delta_n downarrow0` respektieren.

### Gate O4 — Prime-Power AR(1)

Prüfe, ob die bereits bewiesene Prime-Power-AR(1)/Weil-tail-Struktur den positiven Spektralteil von `O_a` kontrolliert. Dies ist jetzt die bevorzugte Rückkopplung an frühere Objekt-X-Arbeit.

## 6. Auxiliary: finite Gamma-null ladder

Für `alpha_m=2m+1/2` und `Q_m=-partial_x^2+alpha_m^2` entstehen Mellin-Nullstellen bei

```math
-2m,\qquad2m+1.
```

Endliche Mengen dieser Punkte sind nach Connes--Consani Proposition C.1 zulässig; die negativen geraden Punkte sind triviale Zeta-Nullstellen, während Proposition C.1 nur die nichttrivialen Nullstellen ausschließt.

Die Leiter ist mathematisch legitim, aber nicht Default-Priorität, solange sie den Prime-overlap nicht quantitativ verbessert.

## 7. Object-X-Pfad

```text
COMMON-JUMP common positive geometry ✓[M]
        |
        v
centered Prime-overlap form ✓[M]
        |
        v
NP-OVERLAP domination ?[O]
        |
        v
global null-pole Weil positivity
        |
        v
RH
```

Die Architektur ist konstruiert; der harte Rest ist jetzt eine explizite arithmetische Shift-Korrelationsungleichung.

## 8. Numerik-Firewall

Ritz-Minima in endlichen Nullpolräumen sind obere Schranken für das wahre Infimum. Nur zertifizierte Falsifikationen oder unabhängige Intervallbeweise dürfen theorematisch promoted werden.

## 9. Auxiliary / separate

OX-GEN-A, POS-DIL #101--#105, Prime-Power AR(1), PR #91, PR #49 und R37/G4c bleiben erhalten. Prime-Power AR(1) wird für Gate O4 ausdrücklich wieder als möglicher Input priorisiert.

## 10. Firewalls

- bekannte Kleinfensterpositivität nicht als Projektneuheit verkaufen;
- große Prime-Schwelle nicht mit dem zentrierten Restproblem verwechseln;
- finite Gamma-null ladder nicht als all-window coercivity ausgeben;
- kein fixed-`a` als RH-äquivalent behaupten;
- Registry/Arbeitsdefinition nicht automatisch promovieren;
- RH bleibt offen.