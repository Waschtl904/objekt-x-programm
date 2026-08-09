# P07 Targeted-Reaudit — Externcheck GM-Skala und Nevanlinna-Konstante

**Datum:** 9. August 2026  
**Scope:** `papers/P07_Weil_Form_Statistics.md`, NEU-101, NEU-111, NEU-120  
**Prüfart:** `TARGETED-REAUDIT` nach externem KI-Gegencheck  

---

## 0. Ergebnis

Der externe Gegencheck enthielt zwei voneinander zu trennende Punkte:

1. einen behaupteten Fehler im Goldston–Montgomery-Korollar 3.2a;
2. einen strukturellen Hinweis zur Nevanlinna-Normalisierung $a_N$.

Endurteil:

- **GM-Korollar:** kein Gegenbefund gegen den aktuellen P07-Endstand; der externe Audit las fälschlich $H=M$ statt des live stehenden $H=\sqrt M$.
- **GM-Uniformitätsbereich auf der $H$-Seite:** der live stehende Bereich $1\le H\le M^{1-\varepsilon}$ bleibt bestehen. Die Untergrenze $M^\varepsilon$ gehört in der klassischen GM-Äquivalenz zur korrespondierenden Pair-Correlation-$T$-Seite, nicht als zusätzliche Untergrenze zur $H$-Seite.
- **Nevanlinna-Konstante:** neuer gültiger Schutzsatz: lokale gleichmäßige Konvergenz $\widetilde m_N^{\rm ren}\to m_{\rm arith}$ erzwingt $a_N\to0$.

P07 wird daher **nicht mathematisch zurückgerollt**. Es erhält nur eine lokale Symmetriepräzisierung.

---

## 1. GM-Gegencheck

P07 definiert

$$
\mathcal V(M,H)=\frac1M\int_M^{2M}(\psi(x+H)-\psi(x)-H)^2\,dx
$$

und führt konditional unter RH + SPC

$$
\mathcal V(M,H)\sim H\log(M/H)
$$

uniform im Bereich

$$
1\le H\le M^{1-\varepsilon}.
$$

Der aktuelle selbstduale Punkt ist

$$
\boxed{H=\sqrt M},
$$

nicht $H=M$. Daher

$$
\mathcal V(M,\sqrt M)
\sim \sqrt M\log(M/\sqrt M)
=\frac12\sqrt M\log M.
$$

Der behauptete $\log(M/M)=0$-Widerspruch trifft den Live-Stand nicht.

### Quellenpräzisierung

Eine spätere Fachzusammenfassung der Goldston–Montgomery-Äquivalenz formuliert die Bereiche getrennt:

- Pair-Correlation-Seite: $X^\varepsilon\le T\le X$;
- Kurzintervall-/Selberg-Integral-Seite: $1\le H\le X^{1-\varepsilon}$.

Damit ist ein Patch

$$
1\le H\le M^{1-\varepsilon}
\rightsquigarrow
M^\varepsilon\le H\le M^{1-\varepsilon}
$$

**nicht gerechtfertigt** und wird ausdrücklich nicht vorgenommen.

**Status:** `AUDIT-RECONCILED — kein Gegenbefund`.

---

## 2. Symmetrie von $m_{\rm arith}$

Im Repo ist

$$
\Xi(z)=\xi\!\left(\frac12+iz\right),
\qquad
m_{\rm arith}(z)=-\frac{\Xi'(z)}{\Xi(z)}.
$$

Aus der Funktionalgleichung $\xi(s)=\xi(1-s)$ folgt

$$
\Xi(-z)=\Xi(z).
$$

Also ist $\Xi'$ ungerade und damit

$$
\boxed{m_{\rm arith}(-z)=-m_{\rm arith}(z).}
$$

Aus der reellen Symmetrie folgt außerdem

$$
\Xi(\bar z)=\overline{\Xi(z)},
\qquad
m_{\rm arith}(\bar z)=\overline{m_{\rm arith}(z)}.
$$

Für $z=i$ ist $\bar i=-i$. Daher

$$
\overline{m_{\rm arith}(i)}
=m_{\rm arith}(-i)
=-m_{\rm arith}(i),
$$

also ist $m_{\rm arith}(i)$ rein imaginär und

$$
\boxed{\Re m_{\rm arith}(i)=0.}
$$

Für die in P07 verwendete Nevanlinna-Normalisierung ist somit die Zielkonstante

$$
\boxed{A=0.}
$$

**Status:** `✓[M]`.

---

## 3. Neuer notwendiger Konvergenztest für $a_N$

Die renormierten Approximanten lauten

$$
\widetilde m_N^{\rm ren}(z)
=a_N+\int_{\mathbb R}
\left(\frac1{t-z}-\frac{t}{1+t^2}\right)d\widetilde\mu_N(t),
\qquad a_N\in\mathbb R.
$$

Bei $z=i$ gilt exakt

$$
\frac1{t-i}-\frac{t}{1+t^2}
=\frac{t+i}{1+t^2}-\frac{t}{1+t^2}
=\frac{i}{1+t^2}.
$$

Der Integralterm ist daher rein imaginär. Folglich

$$
\boxed{\Re\widetilde m_N^{\rm ren}(i)=a_N.}
$$

Falls nun

$$
\widetilde m_N^{\rm ren}
\xrightarrow[N\to\infty]{\rm loc.unif.}
m_{\rm arith}
\quad\text{in }\mathbb C^+,
$$

so folgt insbesondere punktweise bei $i$:

$$
a_N
=\Re\widetilde m_N^{\rm ren}(i)
\longrightarrow
\Re m_{\rm arith}(i)
=0.
$$

Damit gilt der neue Schutzsatz

$$
\boxed{
\widetilde m_N^{\rm ren}\to m_{\rm arith}
\text{ lokal gleichmäßig}
\Longrightarrow a_N\to0.
}
$$

Dies ist **keine zusätzliche RH-Annahme**, sondern eine notwendige Konsequenz der bereits als offen markierten Konvergenz.

**Status:** `✓[M]` als notwendige Bedingung innerhalb der konditionalen Grenzarchitektur.

---

## 4. Konsequenz für P07

Zu ergänzen sind ausschließlich:

1. in §4 die Zentrierung $A=\Re m_{\rm arith}(i)=0$;
2. in §5 der notwendige Symmetrietest $a_N\to0$ unter lokaler gleichmäßiger Konvergenz;
3. in der Statusmatrix ein entsprechender Eintrag.

Nicht geändert werden:

- der GM-$H$-Bereich $1\le H\le M^{1-\varepsilon}$;
- der selbstduale Punkt $H=\sqrt M$;
- der CONDITIONAL-Status von GM;
- die Offenheit der eigentlichen Jacobi/Herglotz-Konvergenz;
- der Freeze-Status von P07.

---

## 5. Endurteil

$$
\boxed{
\text{P07 extern gegengeprüft: GM-Gegenbefund verworfen; }a_N\to0\text{-Firewall ergänzt.}
}
$$

**Endstatus:** `TARGETED-REAUDIT COMPLETE — P07 bleibt SYN FROZEN ✓[K/M]`.
