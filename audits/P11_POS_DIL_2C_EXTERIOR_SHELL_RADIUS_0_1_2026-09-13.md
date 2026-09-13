# P11 / POS-DIL-2C — Exterior prime-shell domination for every 0<a<=1

> **Stand:** 13. September 2026  
> **Rolle:** theorem-level interner Audit der Radiusfortsetzung des in POS-DIL-2B definierten ersten äußeren Prime-Shift-Shells; keine Registry-Promotion, keine exakte Shell-Buchung, keine volle Weil-Gram-Identität, kein Object-X-/RH-Abschluss.  
> **Basis:** `main@79c3eb8d9935b7d7fc45430af8b06c6b1cd43bd7`.  
> **Scope:** lokalisierte positive Featureform `G_a^+` für `0<a<=1`, Testklasse `H_0^1(-a,a)` mit Nullfortsetzung.

## 0. Kurzurteil

Der in POS-DIL-2B geometrisch definierte erste Außenshell

```math
\mathscr S_a^{\rm out}
=\left\{n=p^k:\ a<c_n\le2a\right\},
\qquad c_n=\frac12\log n,
```

mit

```math
H_a^{\rm out}(v,w)
=\sum_{n\in\mathscr S_a^{\rm out}}
\frac{\Lambda(n)}{\sqrt n}
\langle K_nv,K_nw\rangle
```

repariert den unit-gain-Massendefekt nicht nur bei `a=1/2`, sondern auf dem **gesamten lokalisierten Bereich**

```math
\boxed{0<a\le1.}
```

Genauer gilt für jede zulässige Testfunktion

```math
\boxed{
\|\mathcal Ev\|^2
\le
G_a^+(v)+H_a^{\rm out}(v),
\qquad 0<a\le1.
}
```

Für `v\ne0` ist die Ungleichung in der hier verwendeten Abschätzung sogar strikt.

Damit trägt

```math
A_a^{\rm out}:=G_a^++H_a^{\rm out}
```

den archimedischen Rang-2-Term auf jedem solchen Radius kontraktiv:

```math
\boxed{
\begin{pmatrix}
A_a^{\rm out}&R_0\\
R_0&A_a^{\rm out}
\end{pmatrix}\succeq0,
\qquad 0<a\le1.
}
```

Der Beweis ist vollständig algebraisch/elementar. Es werden keine numerischen Zertifikate benutzt.

**Firewall:** Die Radiusfrage ist damit geschlossen, die **Buchungsfrage nicht**. Es ist weiterhin offen, wie die äußere positive Prime-Energie in einer exakten unveränderten Weilform kanonisch gegengebucht/renormalisiert wird.

---

## 1. Zwei universelle Abschätzungen

### 1.1 Log-Multiplikator

Der positive Log-Multiplikator in `G_a^+` ist

```math
L_a(v)
=-\frac12\int_{-a}^a
\log(a^2-x^2)|v(x)|^2dx.
```

Für `0<a<=1` und `|x|<a` gilt

```math
a^2-x^2\le a^2,
```

also

```math
-\frac12\log(a^2-x^2)\ge-\log a.
```

Daher

```math
\boxed{G_a^+(v)\ge L_a(v)\ge(-\log a)\|v\|_2^2.}
```

Alle übrigen Komponenten von `G_a^+` werden im Radiusbeweis nur als nichtnegative Reserve benutzt.

### 1.2 Außenshell

POS-DIL-2B bewies für jeden Kanal mit `c_n>a`

```math
\|K_nv\|_2^2=2\|v\|_2^2.
```

Setze

```math
B_a^{\rm out}
=\sum_{n\in\mathscr S_a^{\rm out}}
\frac{\Lambda(n)}{\sqrt n}.
```

Dann exakt

```math
\boxed{H_a^{\rm out}(v)=2B_a^{\rm out}\|v\|_2^2.}
```

Somit

```math
\boxed{
A_a^{\rm out}(v)
\ge
\bigl(-\log a+2B_a^{\rm out}\bigr)\|v\|_2^2.
}
```

---

## 2. Universeller Moment-Upper-Bound

Durch Cauchy-Schwarz:

```math
|E_+(v)|^2
\le
\left(\int_{-a}^a e^x dx\right)\|v\|_2^2
=2\sinh(a)\|v\|_2^2,
```

und analog für `E_-`. Daher

```math
\boxed{
\|\mathcal Ev\|^2
\le4\sinh(a)\|v\|_2^2.
}
```

Es genügt also die skalare Ungleichung

```math
\boxed{
-\log a+2B_a^{\rm out}>4\sinh(a)
}
```

für `0<a<=1` zu beweisen.

---

## 3. Elementare Hilfsabschätzungen

### 3.1 Logarithmus von unten

Für `x>1` gilt

```math
\boxed{
\log x>\frac{2(x-1)}{x+1}.
}
```

Zum Beispiel folgt dies aus

```math
\log x
=2\left(t+\frac{t^3}{3}+\frac{t^5}{5}+\cdots\right),
\qquad t=\frac{x-1}{x+1}\in(0,1).
```

Insbesondere:

```math
\log2>\frac23,
\quad
\log3>1,
\quad
\log5>\frac43,
\quad
\log7>\frac32,
```

```math
\log11>\frac53,
\quad
\log13>\frac{12}{7},
\quad
\log17>\frac{16}{9},
\quad
\log19>\frac95.
```

### 3.2 Kleine Logarithmen von oben

Aus positiven Taylor-Teilsummen der Exponentialfunktion:

```math
\boxed{\log2<\frac34}
```

weil

```math
e^{3/4}>1+\frac34+\frac{(3/4)^2}{2}=\frac{65}{32}>2.
```

Weiter

```math
\boxed{\log3<\frac{10}{9}}
```

weil

```math
\sum_{j=0}^4\frac{(10/9)^j}{j!}
=\frac{59453}{19683}>3.
```

Ebenso

```math
\boxed{\log5<\frac53}
```

weil

```math
\sum_{j=0}^4\frac{(5/3)^j}{j!}
=\frac{10009}{1944}>5.
```

Und

```math
\boxed{\log7<2}
```

weil die Taylor-Summe von `e^2` bis zum Grad vier bereits `7` ist und weitere positive Terme folgen.

Für später brauchen wir außerdem

```math
\boxed{e^2<8.}
```

Denn

```math
e
=1+1+\frac12+\frac16+\sum_{k\ge4}\frac1{k!}
<\frac83+\frac{1/24}{1-1/5}
=\frac{87}{32}<\frac{11}{4},
```

also

```math
e^2<\frac{121}{16}<8.
```

### 3.3 Wurzeln

Die folgenden rationalen Schranken folgen jeweils unmittelbar durch Quadrieren:

```math
\frac75<\sqrt2<\frac32,
\qquad
\sqrt3<\frac74,
\qquad
\sqrt5<\frac94,
\qquad
\sqrt7<\frac83,
```

```math
\sqrt{11}<\frac{10}{3},
\qquad
\sqrt{13}<\frac{11}{3},
\qquad
\sqrt{17}<\frac{17}{4},
\qquad
\sqrt{19}<\frac{22}{5}.
```

### 3.4 `sinh` von oben

Für `0<x<=1` gilt

```math
\sinh x
=x+\frac{x^3}{6}+\frac{x^5}{120}+\cdots.
```

Ab dem Term `x^3/3!` ist das Verhältnis zweier aufeinanderfolgender Terme höchstens `x^2/20`. Daher

```math
\boxed{
\sinh x
<
x+\frac{x^3/6}{1-x^2/20}
=:U(x).
}
```

Wir verwenden die exakten Werte

```math
4U\!\left(\frac{3}{16}\right)=\frac{15423}{20444},
```

```math
4U\!\left(\frac38\right)=\frac{3903}{2542},
```

```math
4U\!\left(\frac59\right)=\frac{20140}{8613},
```

```math
4U\!\left(\frac34\right)=\frac{1023}{311},
```

```math
4U\!\left(\frac56\right)=\frac{4670}{1251},
```

```math
4U(1)=\frac{268}{57}.
```

---

## 4. Shell-Mitgliedschaft als Intervallproblem

Für ein Prime Power `n` setze

```math
\alpha_n=\frac14\log n,
\qquad
\beta_n=\frac12\log n=c_n.
```

Dann

```math
\boxed{
n\in\mathscr S_a^{\rm out}
\quad\Longleftrightarrow\quad
\alpha_n\le a<\beta_n.
}
```

Wir zerlegen `(0,1]` in sieben Intervalle:

```math
I_0=(0,\alpha_2),
```

```math
I_1=[\alpha_2,\beta_2),
```

```math
I_2=[\beta_2,\beta_3),
```

```math
I_3=[\beta_3,\beta_4),
```

```math
I_4=[\beta_4,\beta_5),
```

```math
I_5=[\beta_5,\beta_7),
```

```math
I_6=[\beta_7,1].
```

Auf jedem Intervall genügt eine feste kleine Teilmenge der tatsächlich vorhandenen Shell-Kanäle:

| Intervall | garantierte Shell-Prime-Powers |
|---|---|
| `I_0` | keine benötigt |
| `I_1` | `2` |
| `I_2` | `3,4` |
| `I_3` | `4,5,7,8` |
| `I_4` | `5,7,8,9,11` |
| `I_5` | `7,8,9,11,13,16,17` |
| `I_6` | `8,9,11,13,16,17,19` |

Die Mitgliedschaft folgt direkt aus `alpha_n<=a<beta_n`; die nötigen Ordnungsrelationen reduzieren sich auf elementare Integervergleiche. Für `I_6` garantiert `e^2<8`, dass bereits `beta_8>1`, also alle dort benutzten Kanäle bis `a=1` im Außenshell bleiben.

---

## 5. Sieben exakte Intervallabschätzungen

Wir schreiben

```math
C(a):=-\log a+2B_a^{\rm out}.
```

Auf jedem Intervall wird `C(a)` von unten durch eine rationale Zahl und `4sinh(a)` von oben durch eine kleinere rationale Zahl beschränkt.

### 5.1 Intervall I_0

Aus `log2<3/4` folgt

```math
\alpha_2<\frac{3}{16}.
```

Daher

```math
-\log a>\log\frac{16}{3}>\frac{26}{19}.
```

Andererseits

```math
4\sinh(a)<4U\!\left(\frac{3}{16}\right)
=\frac{15423}{20444}.
```

Und exakt

```math
\frac{26}{19}>\frac{15423}{20444}.
```

Also `C(a)>4sinh(a)` auf `I_0`.

### 5.2 Intervall I_1

Hier liegt `n=2` im Shell. Aus `log2<3/4` folgt `a<3/8`.

Ferner

```math
-\log a>\log\frac83>\frac{10}{11}.
```

Mit `sqrt2>7/5` und `log2>2/3`:

```math
2w_2=\sqrt2\log2>\frac{14}{15}.
```

Also

```math
C(a)>\frac{10}{11}+\frac{14}{15}
=\frac{304}{165}.
```

Dagegen

```math
4\sinh(a)<4U\!\left(\frac38\right)
=\frac{3903}{2542}.
```

Exakt

```math
\frac{304}{165}>\frac{3903}{2542}.
```

### 5.3 Intervall I_2

Hier liegen `3,4` im Shell. Aus `log3<10/9` folgt `a<5/9`.

```math
-\log a>\log\frac95>\frac47.
```

Mit `log3>1`, `sqrt3<7/4` und `log2>2/3`:

```math
2w_3>\frac87,
\qquad
2w_4=\log2>\frac23.
```

Somit

```math
C(a)>\frac47+\frac87+\frac23
=\frac{50}{21}.
```

Andererseits

```math
4\sinh(a)<4U\!\left(\frac59\right)
=\frac{20140}{8613},
```

und exakt

```math
\frac{50}{21}>\frac{20140}{8613}.
```

### 5.4 Intervall I_3

Hier liegen `4,5,7,8` im Shell. Da `a<beta_4=log2<3/4`:

```math
-\log a>\log\frac43>\frac27.
```

Die Gewichtsschranken lauten

```math
2w_4>\frac23,
\qquad
2w_5>\frac{32}{27},
```

```math
2w_7>\frac98,
\qquad
2w_8>\frac49.
```

Daher

```math
C(a)>
\frac27+\frac23+\frac{32}{27}+\frac98+\frac49
=\frac{5605}{1512}.
```

Dagegen

```math
4\sinh(a)<4U\!\left(\frac34\right)
=\frac{1023}{311},
```

und exakt

```math
\frac{5605}{1512}>\frac{1023}{311}.
```

### 5.5 Intervall I_4

Hier liegen `5,7,8,9,11` im Shell. Aus `log5<5/3` folgt `a<5/6`.

```math
-\log a>\log\frac65>\frac{2}{11}.
```

Weiter

```math
2w_5>\frac{32}{27},
\quad
2w_7>\frac98,
\quad
2w_8>\frac49,
```

```math
2w_9>\frac23,
\qquad
2w_{11}>1.
```

Also

```math
C(a)>
\frac{2}{11}+\frac{32}{27}+\frac98+\frac49+\frac23+1
=\frac{10937}{2376}.
```

Dagegen

```math
4\sinh(a)<4U\!\left(\frac56\right)
=\frac{4670}{1251},
```

und exakt

```math
\frac{10937}{2376}>\frac{4670}{1251}.
```

### 5.6 Intervall I_5

Hier liegen `7,8,9,11,13,16,17` im Shell. Da `a<beta_7<1`, ist `-log a>0`.

Die Gewichtsschranken ergeben

```math
2w_7>\frac98,
\quad
2w_8>\frac49,
\quad
2w_9>\frac23,
\quad
2w_{11}>1,
```

```math
2w_{13}>\frac{72}{77},
\quad
2w_{16}>\frac13,
\quad
2w_{17}>\frac{128}{153}.
```

Somit

```math
C(a)>
\frac98+\frac49+\frac23+1
+\frac{72}{77}+\frac13+\frac{128}{153}
=\frac{503389}{94248}.
```

Dagegen

```math
4\sinh(a)<4U(1)=\frac{268}{57},
```

und exakt

```math
\frac{503389}{94248}>\frac{268}{57}.
```

### 5.7 Intervall I_6

Hier liegen `8,9,11,13,16,17,19` im Shell. Der Logterm wird nur mit `-log a>=0` benutzt.

```math
2w_8>\frac49,
\quad
2w_9>\frac23,
\quad
2w_{11}>1,
```

```math
2w_{13}>\frac{72}{77},
\quad
2w_{16}>\frac13,
\quad
2w_{17}>\frac{128}{153},
\quad
2w_{19}>\frac9{11}.
```

Daher

```math
C(a)>
\frac49+\frac23+1+\frac{72}{77}+\frac13
+\frac{128}{153}+\frac9{11}
=\frac{59309}{11781}.
```

Und weiterhin

```math
4\sinh(a)\le4\sinh1<\frac{268}{57}.
```

Exakt

```math
\frac{59309}{11781}>\frac{268}{57}.
```

---

## 6. Theorem — vollständige Radiusfortsetzung `✓[M]`

Die sieben Intervalle überdecken `(0,1]`. Auf jedem gilt

```math
-\log a+2B_a^{\rm out}>4\sinh(a).
```

Daher für jedes `0<a<=1` und jedes nichttriviale zulässige `v`:

```math
\begin{aligned}
G_a^+(v)+H_a^{\rm out}(v)
&\ge
\bigl(-\log a+2B_a^{\rm out}\bigr)\|v\|_2^2\\
&>
4\sinh(a)\|v\|_2^2\\
&\ge
\|\mathcal Ev\|^2.
\end{aligned}
```

Also

```math
\boxed{
\|\mathcal Ev\|^2
\le
A_a^{\rm out}(v),
\qquad
A_a^{\rm out}:=G_a^++H_a^{\rm out},
\qquad
0<a\le1.
}
```

Status:

```text
\boxed{\checkmark[M]}
```

für die POS-DIL-2C-Radiusfrage auf dem gesamten dokumentierten `a<=1`-Scope.

---

## 7. R_0-Schurblock für jeden 0<a<=1 `✓[M]`

Da

```math
R_0(v,w)=\langle\mathcal Ev,J\mathcal Ew\rangle,
\qquad \|J\|=1,
```

folgt

```math
|R_0(v,w)|
\le\|\mathcal Ev\|\,\|\mathcal Ew\|
\le\sqrt{A_a^{\rm out}(v)A_a^{\rm out}(w)}.
```

Damit

```math
\boxed{
\begin{pmatrix}
A_a^{\rm out}&R_0\\
R_0&A_a^{\rm out}
\end{pmatrix}\succeq0,
\qquad 0<a\le1.
}
```

Ebenso faktorisiert die POS-DIL-1-Momentabbildung `V` kontraktiv durch jede Hilbert-Featureabbildung von `A_a^{out}`.

---

## 8. Was jetzt wirklich noch offen ist

Die **Positivitäts-/Radiusfrage** des ersten Außenshells ist im gesamten lokalen Scope `0<a<=1` geschlossen.

Offen bleibt die strukturell wichtigere Frage:

> Wie wird die positive Außenkanalenergie `H_a^{out}` in einer **exakten unveränderten Weil-Buchung** kanonisch gegengebucht oder renormalisiert?

Die lokale Suzuki-Normalform enthält nur den inneren endlichen Primeblock in `G_a^+`. Das additive Anhängen von `H_a^{out}` erzeugt zwar eine echte positive Geometrie aus echten Prime-Kanälen, aber noch keine Gleichheit mit der vollständigen Weilform.

Daher bleibt ausdrücklich offen:

- exakte Shell-Buchung/Renormalisierung;
- mögliche Teleskopierung über aufeinanderfolgende Shiftshells;
- Root/Hub-Gegenbuchung über `T_q^*T_q+uu^*=R_q`;
- Rolle der POS-DIL-1-Amplitude `1-u_k` in dieser Bilanz;
- `r_1`;
- `c_aI`;
- vollständige Weil-Gram-Identität;
- Object X und RH.

---

## 9. Neue operative Hauptfront — POS-DIL-2C-B / EXACT-SHELL-BOOKING

Nach Abschluss der Radiusfrage ist der nächste echte Gate:

> **Kann der geometrisch kanonische erste Außenshell in eine exakte gemeinsame Prime-/Archimedean-Geometrie eingebaut werden, ohne die Weilform zu verändern?**

Priorisierte algebraische Ansätze:

1. Rekonstruiere die Außenkanal-Identitätsmasse vor der lokalen Cutoff-Umschreibung.
2. Prüfe Differenzen benachbarter Shiftshells auf Teleskopierung.
3. Zerlege pro Primast die Shellenergie gegen AR(1)-Root/Hub:
   ```math
   T_q^*T_q+uu^*=R_q.
   ```
4. Prüfe, ob die gefundene Amplitude
   ```math
   1-u_k=1-q_p^k
   ```
   eine kanonische Gegenbuchung markiert.
5. Erst wenn eine exakte Bilanz vorliegt, darf eine Beziehung zum offenen Skalarblock `c_aI` untersucht werden.

Eine bloße weitere Positivitätsverstärkung zählt jetzt nicht mehr als Hauptfortschritt.

---

## 10. Statusbuchung

```text
POS-DIL-2A existing-G unit-gain no-go at a=1/2        ×[M]
first exterior shell pure-mass identity                ✓[M]
first exterior shell domination for every 0<a<=1      ✓[M]
contractive R_0 Schur block for every 0<a<=1           ✓[M]
POS-DIL-2C radius extension                            ✓[M]
OX-GEN-A2' overall                                     ✓[M]_part
POS-DIL-2C-B exact shell booking / renormalization     ?[O]
r_1 / c_aI / full Object-X realization / RH            ?[O]
```

Keine Registry-Promotion aus diesem Audit allein.