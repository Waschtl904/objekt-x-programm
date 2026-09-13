# P11 / POS-DIL-2C — Exact exterior-shell gauge and positive `r_0` absorption

> **Stand:** 13. September 2026  
> **Rolle:** theorem-level interner Audit der exakten Außenkanal-Buchung und der positiven Absorption des elementaren archimedischen `R_0`-Blocks; keine Registry-Promotion, kein Abschluss von `R_1`, Skalarblock, Object X oder RH.  
> **Basis:** `main@6415bbf5a1a78974213c8b2222b0950e8a4dd070`.  
> **Scope:** lokalisierte Suzuki-/Weilform für `0<a<=1`, Testklasse `H_0^1(-a,a)` mit Nullfortsetzung.

## 0. Kurzurteil

Die bisher offene Shell-Buchungsfrage lässt sich exakt schließen.

Die kanonische lokalisierte Normalform lautet

```math
Q_{B_a}=G_a^+-N_a,
\qquad
N_a=c_aI+R_0+R_1.
```

Für jeden echten Außenkanal `c_n>a` gilt auf dem Fenster

```math
\|K_nv\|^2=2\|v\|^2.
```

Darum kann jede endliche Menge solcher Außenkanäle **exakt** in den positiven Featureblock aufgenommen werden, wenn dieselbe arithmetische Kanalmasse im skalaren Ledger gegengebucht wird. Die volle Weilform bleibt unverändert.

Für den geometrisch definierten ersten Außenshell

```math
\mathscr S_a^{out}=\{n=p^k:a<c_n\le2a\}
```

entsteht damit eine exakte Shell-Gauge-Normalform

```math
\boxed{
Q_{B_a}
=A_a^{out}-c_a^{out}I-R_0-R_1,
}
```

mit

```math
A_a^{out}=G_a^++H_a^{out},
```

```math
c_a^{out}=c_a+2B_a^{out}.
```

POS-DIL-2C-R hat zugleich für alle `0<a<=1` bewiesen

```math
A_a^{out}\succeq \mathcal E^*\mathcal E
```

im Form-Sinn.

Daraus folgt die **exakte positive Absorption von `R_0`**:

```math
\boxed{
P_a^{(0)}:=A_a^{out}-R_0\succeq0,
}
```

und die volle lokalisierte Weilform wird exakt zu

```math
\boxed{
Q_{B_a}
=P_a^{(0)}-c_a^{out}I-R_1.
}
```

Noch stärker besitzt der positive Block die explizite Zerlegung

```math
\boxed{
P_a^{(0)}
=D_a^{out}+L_+^*L_+,
}
```

wobei

```math
D_a^{out}:=A_a^{out}-\mathcal E^*\mathcal E\succeq0,
```

und

```math
L_+(v)=E_+(v)+E_-(v)
=2\int_{-a}^a\cosh(x/2)v(x)\,dx.
```

Damit ist `r_0` nicht mehr nur in einer Hilfs-Schurmatrix positiv eingebettet: Es ist **innerhalb einer exakten unveränderten Weil-Normalform vollständig in einen positiven gemeinsamen Prime-/archimedischen Block absorbiert**.

---

## 1. Importierte exakte Normalform

Aus der OX-GRAM-Konsolidierung:

```math
\boxed{
Q_{B_a}=G_a^+-N_a,
}
```

mit

```math
\boxed{
N_a=c_aI+C_a,
\qquad
C_a=R_0+R_1.
}
```

Also

```math
\boxed{
Q_{B_a}=G_a^+-c_aI-R_0-R_1.
}
```

Der skalare Koeffizient ist in der kanonischen lokalen Buchung

```math
c_a=A_a^{Zhu}+2A+1,
```

wobei `A_a^{Zhu}` die endliche Prime-Power-Masse des lokalen Überlappungscutoffs enthält.

Die genaue Herkunft dieser Normalform wird hier nicht neu bewiesen; sie ist Input aus dem bereits konsolidierten OX-GRAM-Audit.

---

## 2. Allgemeine Außenkanal-Gauge

Sei `J` eine endliche Menge von Prime Powers mit

```math
c_n=\frac12\log n>a
```

für jedes `n in J`.

Definiere

```math
H_{a,J}(v,w)
:=\sum_{n\in J}
\frac{\Lambda(n)}{\sqrt n}
\langle K_nv,K_nw\rangle,
```

und

```math
b_J:=2\sum_{n\in J}\frac{\Lambda(n)}{\sqrt n}.
```

Da die beiden verschobenen Fenster für `c_n>a` disjunkt sind,

```math
\|K_nv\|^2=2\|v\|^2.
```

Durch Polarisation folgt sogar als Formen

```math
\boxed{
H_{a,J}(v,w)=b_J\langle v,w\rangle_{L^2(-a,a)}.
}
```

Also

```math
\boxed{H_{a,J}=b_JI}
```

im Form-Sinn auf der Testklasse.

Damit gilt identisch

```math
\begin{aligned}
Q_{B_a}
&=G_a^+-c_aI-R_0-R_1\\
&=(G_a^++H_{a,J})-(c_a+b_J)I-R_0-R_1.
\end{aligned}
```

Also:

```math
\boxed{
Q_{B_a}
=G_{a,J}^+-c_{a,J}I-R_0-R_1,
}
```

mit

```math
G_{a,J}^+:=G_a^++H_{a,J},
\qquad
c_{a,J}:=c_a+b_J.
```

Dies ist die **exakte Außenkanal-Cutoff-Gauge-Invarianz**.

Keine Positivität von `Q_{B_a}` wurde verwendet.

---

## 3. Warum dies nicht die verbotene beliebige Diagonalergänzung ist

Algebraisch könnte man zu einer Differenz natürlich denselben beliebigen positiven Term auf beide Seiten addieren. Das wäre kein Object-X-Fortschritt.

Hier ist die zulässige Klasse enger und vorwärts definiert:

1. Die zusätzlichen Features sind die bereits vorhandenen echten Prime-Kanäle `K_n`.
2. Die Koeffizienten sind die kanonischen Weilgewichte
   ```math
   w_n=\frac{\Lambda(n)}{\sqrt n}.
   ```
3. Die Skalarmasse `b_JI` wird **nicht gewählt**, sondern folgt als Satz aus der Außenkanal-Identität
   ```math
   w_nK_n^*K_n=2w_nI
   ```
   auf dem Fenster.
4. Der erste Außenshell wird rein durch Shift-Geometrie ausgewählt, nicht durch Fit an eine benötigte Zahl.

Damit ist die Gauge selbst eine intrinsische Prime-Feature-Gauge, keine freie `tI`-Ergänzung.

**Firewall:** Die Tatsache, dass die volle Form unter dieser Gauge invariant ist, erzeugt allein noch keine zusätzliche Netto-Positivität von `Q_{B_a}`. Der Fortschritt liegt in der exakten gemeinsamen positiven Architektur und der anschließenden Absorption von `R_0`.

---

## 4. Erster Außenshell und arithmetischer Skalarinkrement

Für

```math
\mathscr S_a^{out}
=\{n=p^k:a<c_n\le2a\}
```

gilt äquivalent

```math
e^{2a}<n\le e^{4a}.
```

Definiere

```math
H_a^{out}:=H_{a,\mathscr S_a^{out}},
```

```math
B_a^{out}
=\sum_{e^{2a}<n\le e^{4a}}
\frac{\Lambda(n)}{\sqrt n}.
```

Dann

```math
\boxed{H_a^{out}=2B_a^{out}I.}
```

Setzt man wie in OX-GEN-A

```math
A_X:=2\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n},
```

so ist das Skalarinkrement exakt

```math
\boxed{
2B_a^{out}
=A_{e^{4a}}-A_{e^{2a}}.
}
```

Damit

```math
\boxed{
c_a^{out}
=c_a+A_{e^{4a}}-A_{e^{2a}}.}
```

Dies ist eine direkte exakte Brücke zwischen der POS-DIL-Shell-Gauge und dem bereits in OX-GEN-A auftretenden arithmetischen Skalar `A_X`.

---

## 5. Exakte Shell-Gauge-Normalform `✓[M]`

Setze

```math
A_a^{out}:=G_a^++H_a^{out}.
```

Dann folgt aus §2–4 ohne Approximation

```math
\boxed{
Q_{B_a}
=A_a^{out}-c_a^{out}I-R_0-R_1.
}
```

Diese Gleichheit gilt auf der gesamten dokumentierten lokalen Testklasse für jedes `0<a<=1`.

Die vorher offene Shell-Buchungsfrage ist damit im **Prime-cutoff-Gauge-Sinn exakt gelöst**.

---

## 6. Der Skalar `c_a` ist gaugeabhängig `✓[M]`

Aus der allgemeinen Außenkanal-Gauge folgt unmittelbar:

```math
c_a\longmapsto c_a+b_J
```

wenn die entsprechenden Außenkanäle in den positiven Featureblock aufgenommen werden.

Daher ist der isolierte numerische Wert von `c_a` innerhalb dieser äquivalenten Prime-Feature-Zerlegungen **nicht kanonisch**, solange der Prime-cutoff-Gauge nicht festgelegt wurde.

Kanonisch ist die vollständige Differenzform

```math
G_{a,J}^+-c_{a,J}I
```

und nicht einer ihrer beiden Summanden für sich.

Dies korrigiert die frühere operative Sprache „den Skalarblock `c_aI` erklären“:

> Gesucht werden muss entweder eine **Gauge-Fixierung** oder eine gaugeinvariante gemeinsame Geometrie des Skalarrestes, nicht die Erklärung eines isolierten gaugeabhängigen Zahlenwertes.

---

## 7. POS-DIL-2C-R liefert einen echten Defektraum

Der Radius-Audit bewies für jedes `0<a<=1`

```math
\boxed{
A_a^{out}(v,v)\ge\|\mathcal Ev\|^2.
}
```

Definiere die polarisierte Form

```math
D_a^{out}(v,w)
:=A_a^{out}(v,w)
-\langle\mathcal Ev,\mathcal Ew\rangle_{\mathbb C^2}.
```

Dann

```math
\boxed{D_a^{out}\succeq0.}
```

Wichtig: `D_a^{out}` wird nicht aus bekannter Weil-Positivität konstruiert. Seine Positivität folgt aus der expliziten elementaren Shell-Dominanz.

---

## 8. Exakte positive Absorption von R_0 `✓[M]`

Erinnerung:

```math
R_0(v,w)
=-E_+(v)\overline{E_-(w)}
-E_-(v)\overline{E_+(w)}.
```

Daher gilt polarisiert

```math
\begin{aligned}
&\langle\mathcal Ev,\mathcal Ew\rangle-R_0(v,w)\\
&=E_+(v)\overline{E_+(w)}
+E_-(v)\overline{E_-(w)}\\
&\quad+E_+(v)\overline{E_-(w)}
+E_-(v)\overline{E_+(w)}\\
&=\bigl(E_+(v)+E_-(v)\bigr)
\overline{\bigl(E_+(w)+E_-(w)\bigr)}.
\end{aligned}
```

Setze

```math
L_+(v):=E_+(v)+E_-(v).
```

Dann exakt

```math
\boxed{
\mathcal E^*\mathcal E-R_0=L_+^*L_+
}
```

als Formidentität.

Nun

```math
\begin{aligned}
A_a^{out}-R_0
&=(A_a^{out}-\mathcal E^*\mathcal E)
 +(\mathcal E^*\mathcal E-R_0)\\
&=D_a^{out}+L_+^*L_+.
\end{aligned}
```

Also

```math
\boxed{
P_a^{(0)}:=A_a^{out}-R_0
=D_a^{out}+L_+^*L_+
\succeq0.
}
```

Dies ist eine **explizite positive Prime-/archimedische Form**.

Der neue positive archimedische Kanal ist sogar konkret:

```math
\boxed{
L_+(v)
=2\int_{-a}^a\cosh(x/2)v(x)\,dx.
}
```

Er ist der gerade Exponentialmodus der bereits kanonischen OX-GEN-A-Repräsentation.

---

## 9. Exakte Weil-Normalform ohne R_0 im Defekt `✓[M]`

Aus §5 und §8:

```math
\begin{aligned}
Q_{B_a}
&=A_a^{out}-c_a^{out}I-R_0-R_1\\
&=(A_a^{out}-R_0)-c_a^{out}I-R_1.
\end{aligned}
```

Damit

```math
\boxed{
Q_{B_a}
=P_a^{(0)}-c_a^{out}I-R_1,
\qquad
P_a^{(0)}\succeq0,
\qquad0<a\le1.
}
```

Der elementare archimedische `R_0`-Block ist also **vollständig aus dem negativen/indefiniten Rest entfernt und in den positiven gemeinsamen Block absorbiert**.

Dies ist eine exakte Formidentität, keine Schur-Hilfsungleichung.

---

## 10. Bedeutung für Objekt X

Dies ist ein echter gemeinsamer Prime-/archimedischer positiver Baustein im lokalen `a<=1`-Scope:

- `P_a^{(0)}` enthält die vorhandenen positiven `G_a^+`-Features;
- echte äußere Prime-Kanäle liefern die zusätzliche positive Masse;
- `R_0` wird durch die gemeinsame Exponentialdarstellung exakt in einen positiven `L_+`-Kanal umgewandelt;
- die vollständige lokalisierte Weilform bleibt durch die Shell-Gauge exakt unverändert.

Damit ist die bisherige POS-DIL-Zielsetzung für den **elementaren archimedischen `r_0`-Layer** konstruktiv erfüllt.

**Aber:** Das ist noch nicht die volle Objekt-X-Realisierung, weil `c_a^{out}I+R_1` weiterhin als Rest verbleibt.

---

## 11. Neue Hauptfront — R_1 / gaugeinvarianter Skalarrest

Nach der exakten `R_0`-Absorption lautet die nächste echte Frage:

```math
\boxed{
Q_{B_a}
=P_a^{(0)}-\bigl(c_a^{out}I+R_1\bigr).
}
```

Gesucht ist jetzt eine intrinsische Behandlung des **verbleibenden Restes**.

Prioritäten:

1. `R_1` auf dieselbe Generator-/Featuregeometrie zurückführen oder eine natürliche Klassenobstruktion beweisen.
2. Wegen der Cutoff-Gauge nicht den isolierten Wert `c_a^{out}` erklären, sondern eine kanonische Gauge-Fixierung oder gaugeinvariante Skalar-Reststruktur finden.
3. Prüfen, ob `R_1` und der skalare Ledger gemeinsam statt getrennt behandelt werden müssen.
4. Keine erneute beliebige Diagonalaugmentation als Fortschritt verbuchen.

---

## 12. Harte Firewalls

Nicht bewiesen ist:

- `R_1`-Absorption;
- Positivität von `Q_{B_a}` aus der neuen Normalform;
- eine kanonische endgültige Wahl des Prime-cutoff-Gauge;
- eine Gleichsetzung von `c_a^{out}` mit einem intrinsischen Objekt-X-Skalar;
- eine globale Aussage für `a>1`;
- eine volle Weil-Gram-Identität auf der endgültigen Objekt-X-Testklasse;
- Object X oder RH.

Insbesondere darf die exakte Gauge-Invarianz nicht als „wir dürfen beliebig positive Masse hinzufügen“ missverstanden werden. Zulässig ist hier nur die vorab definierte Klasse **echter Außen-Prime-Kanäle mit ihren kanonischen Weilgewichten**.

---

## 13. Statusbuchung

```text
exterior Prime cutoff-gauge identity                  ✓[M]
first-shell scalar increment = A_{e^{4a}}-A_{e^{2a}} ✓[M]
cutoff-gauge dependence of isolated c_a               ✓[M]
positive defect form D_a^{out}                        ✓[M]
exact positive absorption A_a^{out}-R_0               ✓[M]
exact normal form Q=P_a^{(0)}-c_a^{out}I-R_1          ✓[M]
POS-DIL r_0-layer on 0<a<=1                           ✓[M]
OX-GEN-A2' overall                                     ✓[M]_part
R_1 / gauge-invariant scalar remainder                ?[O]
full Object-X realization / RH                        ?[O]
```

Keine Registry-Promotion aus diesem Audit allein.