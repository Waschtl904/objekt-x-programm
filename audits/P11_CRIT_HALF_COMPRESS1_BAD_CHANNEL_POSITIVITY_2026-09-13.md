# P11 Audit — CRIT-HALF-COMPRESS-1: bad-channel positivity at a=1/2

**Datum:** 13. September 2026  
**Basis:** Critical-half branch nach dem Prime-threshold bad-channel Audit.  
**Rolle:** theorem-level Teilabschluss des `a=1/2`, `p=2` Kompressionsgates.  
**Registry:** unveraendert.  
**Nonclaim:** noch kein Beweis der vollen NULLPOL-Positivitaet bei `a=1/2`; kein globaler NP-GAP-/RH-Abschluss.

---

## 0. Kurzurteil

Der exakt negative Prime-2-Kanal aus dem Threshold-Audit ist bei `a=1/2` **nicht** die verbleibende Obstruktion.

Sei

```math
h=\log2,
\qquad
w_2=\frac{\log2}{\sqrt2},
\qquad
b=\frac12-\frac h2=\frac{1-\log2}{2}.
```

Der negative Kanal ist die isometrische symmetrische Randkopie

```math
S_+:\mathscr D_{NP,b}\to
\mathscr D_{NP,1/2}\cap\operatorname{Ran}P_+.
```

Fuer jedes `g in D_{NP,b}` gilt auf diesem Kanal exakt

```math
Q_{1/2}(S_+g)
=Q_\infty(g)
-w_2\|g\|^2
-\sum_{m\ge1}e^{-\mu_mh}
\operatorname{Re}\bigl(E_{\mu_m,+}(g)\overline{E_{\mu_m,-}(g)}\bigr),
```

mit

```math
\mu_m=2m+\frac12,
\qquad
E_{\mu,+}(g)=\int e^{\mu x}g(x)dx,
\qquad
E_{\mu,-}(g)=\int e^{-\mu x}g(x)dx.
```

Der `m=0`-Cross-Term verschwindet **exakt** wegen NULLPOL.

Eine rein vorwaerts gerichtete elementare Abschaetzung liefert

```math
\boxed{
Q_{1/2}(S_+g)>\frac1{20}\|g\|^2.
}
```

Damit ist der komplette isolierte negative Prime-2-Eigenkanal strikt positiv kontrolliert.

Status:

```text
prime-2 bad-channel exact recursion                    ✓[M]
critical gamma-ground cross term killed by NULLPOL     ✓[M]
small-window archimedean source bound > 0.64 centered  ✓[M]
remaining higher-gamma cross defect < 0.09             ✓[M]
prime-2 bad-channel Q > 0.05                           ✓[M]
full a=1/2 NULLPOL Schur complement                    ?[O]
full NP-GAP / Object X / RH                            ?[O]
```

---

# 1. Der schlechte Prime-2-Kanal

Aus dem Threshold-Audit gilt fuer

```math
a=\frac12,
\qquad
h=\log2,
```

wegen

```math
\frac12<h<1
```

die nilpotente Randkanalzerlegung

```math
C_{2,1/2}
=-w_2P_+ + w_2P_-.
```

Der negative Kanal `Ran P_+` ist isometrisch zu

```math
I_b=(-b,b),
\qquad
b=\frac{1-h}{2}.
```

Explizit

```math
(S_+g)(y-h/2)=\frac{g(y)}{\sqrt2},
\qquad
(S_+g)(y+h/2)=\frac{g(y)}{\sqrt2}.
```

Die beiden Kopien sind disjunkt und

```math
\|S_+g\|=\|g\|.
```

Ferner

```math
E_\pm(S_+g)
=\sqrt2\cosh(h/4)E_\pm(g),
```

also

```math
S_+g\in\mathscr D_{NP,1/2}
\iff
g\in\mathscr D_{NP,b}.
```

Der Prime-2-Term ist auf diesem Kanal exakt

```math
\boxed{
\langle S_+g,C_{2,1/2}S_+g\rangle
=-w_2\|g\|^2.
}
```

---

# 2. Gamma-Moden in Realraumform

Die positive archimedische Featureform besitzt die Resolventenzerlegung

```math
\Phi_\infty(D)
=\sum_{m\ge0}A_m(D),
\qquad
A_m(D)=\frac2{\mu_m}\frac{D^2}{D^2+\mu_m^2},
\qquad
\mu_m=2m+\frac12.
```

Mit der Fourierkonvention des Projekts ist

```math
A_m
=\frac2{\mu_m}I-H_{\mu_m},
```

wobei `H_mu` der positive Faltungsoperator mit Kern

```math
e^{-\mu|x-y|}
```

ist.

Fuer zwei disjunkte Kopien von `g`, deren Mittelpunkte um `h` getrennt sind, verschwindet der Identitaets-Cross-Term. Der Green-Cross-Term faktorisiert dagegen exakt:

```math
\langle T_{-h/2}g,H_\mu T_{h/2}g\rangle
=e^{-\mu h}
E_{\mu,+}(g)\overline{E_{\mu,-}(g)}
```

(bis zur harmlosen Wahl, welcher Faktor konjugiert wird; in der quadratischen Form steht dessen Realteil).

Daher

```math
\boxed{
\langle S_+g,A_mS_+g\rangle
=
\langle g,A_mg\rangle
-e^{-\mu_mh}
\operatorname{Re}
\bigl(E_{\mu_m,+}(g)\overline{E_{\mu_m,-}(g)}\bigr).
}
```

Fuer den Grundmodus `mu_0=1/2` sind `E_{mu_0,±}` genau die NULLPOL-Momente. Also

```math
\boxed{
\text{der gesamte }m=0\text{-Cross-Term verschwindet auf }\mathscr D_{NP,b}.
}
```

Nach Summation und da die Norm unter `S_+` erhalten bleibt:

```math
\boxed{
Q_\infty(S_+g)
=Q_\infty(g)
-\sum_{m\ge1}e^{-\mu_mh}
\operatorname{Re}
\bigl(E_{\mu_m,+}(g)\overline{E_{\mu_m,-}(g)}\bigr).
}
```

Da auf `I_b` noch kein Prime-Power-Kanal aktiv ist, ist `Q_b(g)=Q_\infty(g)`.

---

# 3. Source-Lift auf dem kleineren Fenster

Da `g in D_{NP,b}`, liefert die Critical-half Range-Identitaet eindeutig

```math
\boxed{
g=L_{1/2}u,
\qquad
L_{1/2}=-\partial_x^2+\frac14,
\qquad
u\in C_c^\infty(-b,b).
}
```

Schreibe

```math
A=\|u''\|_2^2,
\qquad
B=\|u'\|_2^2,
\qquad
C=\|u\|_2^2.
```

Dann

```math
\boxed{
\|g\|^2=A+\frac12B+\frac1{16}C.
}
```

---

# 4. Scharfe Ableitungs-Poincare-Ungleichung

Weil `u in C_c^infty(-b,b)`, liegt `w=u'` in `H_0^1(-b,b)` und erfuellt zusaetzlich

```math
\int_{-b}^{b}w(x)dx=u(b)-u(-b)=0.
```

## Lemma 4.1

Fuer jedes `w in H_0^1(-b,b)` mit Integral null gilt

```math
\boxed{
\|w'\|_2^2\ge\left(\frac\pi b\right)^2\|w\|_2^2.
}
```

### Beweis-Skizze

Das variationale Problem zerfaellt in Paritaet. Im ungeraden Sektor ist der erste Dirichlet-Modus auf `(0,b)` bereits

```math
\sin(\pi x/b)
```

mit Eigenwert `(pi/b)^2` und Integral null. Im geraden Sektor fuehrt die Lagrange-Multiplikator-Gleichung fuer die zusaetzliche Integralbedingung auf

```math
\tan(kb)=kb;
```

der erste positive Root liegt strikt oberhalb `pi`, also ist der gerade constrained Eigenwert groesser. Damit ist `(pi/b)^2` die scharfe Unterkante.

Auf `u` angewandt:

```math
\boxed{
A\ge\Lambda B,
\qquad
\Lambda=\left(\frac\pi b\right)^2.
}
```

Aus der gewoehnlichen Dirichlet-Poincare-Ungleichung folgt ausserdem

```math
\boxed{
B\ge\lambda C,
\qquad
\lambda=\left(\frac\pi{2b}\right)^2=\frac\Lambda4.
}
```

---

# 5. Die ersten neun Gamma-Moden liefern bereits 6.02

Fuer `mu>0` setze

```math
R_\mu=(D^2+\mu^2)^{-1}.
```

Wie im vorherigen Schur-Audit gilt auf `I_b`

```math
\langle u,R_\mu u\rangle
\le\frac{1-e^{-\mu b}}{\mu^2}\|u\|^2.
```

Setze `c=1/2` und `d_mu=mu^2-c^2`. Polynomdivision liefert exakt

```math
\begin{aligned}
\langle L_cu,A_\mu L_cu\rangle
=\frac2\mu\Bigl[
&A+(2c^2-\mu^2)B+d_\mu^2C\\
&-\mu^2d_\mu^2\langle u,R_\mu u\rangle
\Bigr].
\end{aligned}
```

Daher insbesondere

```math
\boxed{
\langle g,A_\mu g\rangle
\ge
\frac2\mu\left[A+\left(\frac12-\mu^2\right)B\right],
}
```

weil der verbleibende `C`-Term nach dem Schur-Test gleich

```math
\frac2\mu d_\mu^2e^{-\mu b}C\ge0
```

ist und fuer eine Untergrenze verworfen werden darf.

Summiere nur die ersten neun Modi `m=0,...,8`. Setze

```math
\alpha
:=\sum_{m=0}^8\frac2{\mu_m}
=\sum_{m=0}^8\frac4{4m+1}
=\frac{710302388}{111035925},
```

```math
\beta
:=\sum_{m=0}^8\frac2{\mu_m}
\left(\frac12-\mu_m^2\right)
=-\frac{16633345331}{111035925}.
```

Dann

```math
\langle g,\Phi_\infty g\rangle
\ge\alpha A+\beta B.
```

Wir verwenden nur die sehr groben elementaren Schranken

```math
\log2>0.69,
\qquad
\pi>3.14.
```

Daraus

```math
b=\frac{1-\log2}{2}<\frac{31}{200},
```

und somit

```math
\Lambda
=\left(\frac\pi b\right)^2
>
\left(\frac{628}{31}\right)^2
=:\Lambda_0.
```

Mit

```math
r:=\frac{301}{50}=6.02
```

rechnet man rein rational nach:

```math
(\alpha-r)\Lambda_0+\beta-\frac r2>0,
```

und nach nochmaliger Verwendung `B>=Lambda_0 C/4` sogar

```math
\left[(\alpha-r)\Lambda_0+\beta-\frac r2\right]
\frac{\Lambda_0}{4}
-\frac r{16}>0.
```

Damit

```math
\alpha A+\beta B
-r\left(A+\frac12B+\frac1{16}C\right)>0
```

fuer jedes nichttriviale `u`. Also

```math
\boxed{
\langle g,\Phi_\infty g\rangle
>6.02\|g\|^2.
}
```

Alle Gamma-Moden `m>=9` wurden dabei einfach als positive Formen verworfen.

---

# 6. Zentrierte archimedische Reserve > 0.64

Die archimedische Schwelle ist

```math
\kappa_*
=\log(8\pi)+\gamma+\frac\pi2.
```

Mit den klassischen elementaren Schranken

```math
\pi<3.142,
\qquad
\gamma<0.578,
\qquad
\log(8\pi)<3.225
```

folgt

```math
\boxed{\kappa_*<5.38.}
```

(Die Log-Schranke folgt z.B. aus `8pi<25.136` und einer positiven Taylor-Untergrenze fuer `exp(3.225)>25.136`; die angezeigten Dezimalzahlen koennen durch die entsprechenden rationalen Zahlen `1571/500`, `289/500`, `129/40` ersetzt werden.)

Somit

```math
\boxed{
Q_\infty(g)
=\langle g,\Phi_\infty g\rangle-\kappa_*\|g\|^2
>0.64\|g\|^2.
}
```

---

# 7. Der hoehere Gamma-Cross-Defekt ist < 0.09

Cauchy-Schwarz auf `(-b,b)` liefert

```math
|E_{\mu,+}(g)|^2
\le\frac{\sinh(2\mu b)}{\mu}\|g\|^2,
```

und denselben Bound fuer `E_{mu,-}`. Also

```math
\left|
\operatorname{Re}
(E_{\mu,+}(g)\overline{E_{\mu,-}(g)})
\right|
\le
\frac{\sinh(2\mu b)}{\mu}\|g\|^2.
```

Daher ist der gesamte `m>=1`-Cross-Defekt hoechstens

```math
R
:=\sum_{m\ge1}
\frac{e^{-\mu_mh}\sinh(2\mu_mb)}{\mu_m}.
```

Im Spezialfall

```math
h=\log2,
\qquad
2b=1-\log2
```

wird

```math
\boxed{
R
=\frac12\sum_{m\ge1}
\frac{(e/4)^{\mu_m}-e^{-\mu_m}}{\mu_m}.
}
```

Wir brauchen nur eine sehr grobe rationale Majorante. Aus `e<2.72` folgen

```math
\frac e4<\frac{17}{25}=0.68,
\qquad
e^{-1}>\frac{367}{1000}=0.367.
```

Ferner

```math
\sqrt{17/25}<33/40,
\qquad
\sqrt{367/1000}>121/200.
```

Die ersten drei Summanden werden mit diesen rationalen Schranken direkt majorisiert; fuer den Rest verwendet man `1/(4m+1)<=1/17` und die geometrische Reihe in `(17/25)^2`. Der rein rationale Wert der so erhaltenen Majorante ist kleiner als `9/100`.

Somit

```math
\boxed{R<0.09.}
```

---

# 8. Der Prime-2-Verlust ist < 0.5

Mit

```math
\log2<0.7,
\qquad
\sqrt2>1.4
```

folgt sofort

```math
\boxed{
w_2=\frac{\log2}{\sqrt2}<\frac12.}
```

---

# 9. Bad-channel theorem

Kombiniere §§2, 6, 7, 8. Fuer jedes nichttriviale `g in D_{NP,b}` gilt

```math
\begin{aligned}
Q_{1/2}(S_+g)
&\ge
Q_\infty(g)-w_2\|g\|^2-R\|g\|^2\\
&>
(0.64-0.50-0.09)\|g\|^2.
\end{aligned}
```

Daher

```math
\boxed{
Q_{1/2}(S_+g)>\frac1{20}\|g\|^2.
}
```

Da `S_+` isometrisch ist:

```math
\boxed{
Q_{1/2}(v)>\frac1{20}\|v\|^2
\qquad
\forall\,0\ne v\in
\mathscr D_{NP,1/2}\cap\operatorname{Ran}P_+.
}
```

Dies ist ein echter theorem-level PASS fuer den **gesamten isolierten negativen Prime-2-Eigenkanal**.

---

# 10. Was noch offen bleibt

Die volle Form zerfaellt relativ zu

```math
\mathscr D_{NP,1/2}
=(P_+\mathscr D_{NP})\oplus
(P_+\mathscr D_{NP})^\perp
```

nicht orthogonal fuer die archimedische Form. Obwohl

- der Prime-Term auf `P_+` strikt negativ, aber jetzt kontrolliert ist,
- der Prime-Term auf `P_-` positiv ist,
- der Prime-Term auf dem mittleren Kanal null ist,

besitzt `Q_\infty` archimedische Kreuzblöcke zwischen diesen Unterraeumen.

Daher folgt aus der positiven Diagonalrestriktion auf `P_+` **noch nicht** die Positivitaet der vollen Matrix.

Der verbleibende Gate ist jetzt exakt ein Schur-/Shorting-Problem:

```math
\boxed{
\operatorname{Short}_{P_+}
\bigl(Q_\infty+w_2P_-\bigr)
\stackrel?\succeq
w_2P_+.
}
```

Dies ist wesentlich enger als der vorherige abstrakte `a=1/2`-Gate.

---

# 11. Strategische Konsequenz

Der bisher naheliegendste Verdacht war, dass der direkte negative Prime-2-Kanal selbst den `a=1/2`-Gate blockiert. Das ist nun ausgeschlossen.

Die verbleibende Schwierigkeit ist **nicht**

```text
negative prime diagonal mass,
```

sondern ausschliesslich

```text
archimedean off-diagonal coupling
between the localized bad channel and its complement.
```

Damit wird `CRIT-HALF-COMPRESS-1` zu einem echten, lokalisierten Schur-Komplementproblem. Der naechste Angriff soll genau den archimedischen Cross-Block mit der Gamma-Resolventen-/Green-Markov-Struktur kontrollieren.

---

# 12. Firewalls

Nicht behauptet wird:

- volle Positivitaet auf `D_{NP,1/2}` sei bewiesen;
- die archimedischen Kreuzblöcke seien klein oder positiv;
- externe bekannte Weil-Positivitaet bei `a=1/2` werde als Beweisinput verwendet;
- die angezeigte `1/20`-Reserve sei optimal;
- NP-GAP fuer alle Fenster, Object X oder RH seien geloest.
