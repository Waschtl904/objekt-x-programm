# P11-C1d — Archimedisch–primarithmetische gemeinsame Inzidenzgeometrie

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1d]`  
**Vorgänger:** P11-C1c  
**Primärbasis:** P02 (vollständige hermitesche Weilform), NEU-220c (auditierte Reihenform von `A_\infty` und Polterm), P05 (Prime-Power-Gewichte)  

**Urteil:**

\[
\boxed{[P11-C1d]\quad\checkmark[K/M]_{\rm part}}
\]

Der Primzahlpotenzblock und der archimedische Gamma-Block besitzen RH-frei eine **gemeinsame zentrierte Translations-Inzidenzstruktur**. Beide werden durch dieselbe Operatorfamilie

\[
D_s:=U_{s/2}-U_{-s/2}
\]

erzeugt. Der Primblock erscheint als diskrete kompensierte Inzidenzsumme, der Gamma-Block als kontinuierliche positive Inzidenzenergie plus ein negativer skalarer Grundterm. Der Polterm ist exakt die Differenz zweier Rang-eins-Randkanäle.

Dies ist eine neue gemeinsame Geometriesprache, aber noch keine positive Objekt-X-Vervollständigung und kein RH-Beweis.

---

## 1. Gemeinsamer analytischer Kantenoperator

Auf

\[
\mathcal A_{\rm PW}=C_c^\infty(\mathbb R;\mathbb C)
\subset L^2(\mathbb R,du)
\]

wirkt der kanonische Translationsfluss

\[
(U_sa)(u)=a(u+s).
\]

Für jede Kantenlänge `s>0` definiere

\[
\boxed{D_s:=U_{s/2}-U_{-s/2}.}
\]

Mit der P02-Konvention gilt

\[
\boxed{
\langle D_sa,D_sb\rangle
=2\langle a,b\rangle
-\langle U_sa,b\rangle
-\langle U_{-s}a,b\rangle
=2\langle a,b\rangle-2g_{a,b}(s).
}
\]

Dies ist der gemeinsame Inzidenzbaustein für alle folgenden Sektoren.

---

## 2. Prime-Power-Sektor: diskrete kompensierte Inzidenz

Für

\[
\alpha=(p,m),\qquad
\ell_\alpha=m\log p,
\qquad
w_\alpha=\frac{\log p}{p^{m/2}}>0
\]

liefert P02

\[
B_{\rm fin}(a,b)
=-2\sum_\alpha w_\alpha g_{a,b}(\ell_\alpha).
\]

Mit der Inzidenzidentität folgt **global auf `\mathcal A_{PW}`**, ohne getrennt divergente Summen zu definieren:

\[
\boxed{
B_{\rm fin}(a,b)
=
\sum_\alpha w_\alpha
\Bigl(
\langle D_{\ell_\alpha}a,D_{\ell_\alpha}b\rangle
-2\langle a,b\rangle
\Bigr).
}
\]

Warum diese kompensierte Summe wohldefiniert ist: Der Klammerausdruck ist exakt

\[
-2g_{a,b}(\ell_\alpha).
\]

Da `g_{a,b}\in C_c^\infty(\mathbb R)`, tragen für feste `a,b` nur endlich viele Prime-Power-Zeiten `\ell_\alpha` bei.

**Firewall:** Die beiden Teile

\[
\sum_\alpha w_\alpha\langle D_{\ell_\alpha}a,D_{\ell_\alpha}b\rangle,
\qquad
2\sum_\alpha w_\alpha\langle a,b\rangle
\]

sind einzeln im Allgemeinen divergent und dürfen global nicht voneinander getrennt werden.

Status: `✓[K/M]`.

---

## 3. Gamma-Sektor: Herleitung direkt aus der auditierten NEU-220c-Reihe

NEU-220c fixiert

\[
A_\infty(t)
=
-\gamma-\log\pi
+
\sum_{k=0}^\infty
\left[
\frac1{k+1}
-
\frac{k+\tfrac14}{(k+\tfrac14)^2+t^2/4}
\right].
\]

Setze

\[
a_k:=k+\frac14.
\]

Dann

\[
A_\infty(t)-A_\infty(0)
=
\sum_{k=0}^\infty
\left[
\frac1{a_k}
-
\frac{a_k}{a_k^2+t^2/4}
\right].
\]

Für `a>0` und `b\in\mathbb R` gilt elementar

\[
\int_0^\infty e^{-ax}(1-\cos bx)\,dx
=
\frac1a-\frac{a}{a^2+b^2}.
\]

Daher, mit `b=t/2`, und wegen positiver Summanden/Tonelli:

\[
\begin{aligned}
A_\infty(t)-A_\infty(0)
&=
\int_0^\infty
\left(\sum_{k=0}^\infty e^{-(k+1/4)x}\right)
(1-\cos(tx/2))\,dx\\
&=
\boxed{
\int_0^\infty
\frac{e^{-x/4}}{1-e^{-x}}
(1-\cos(tx/2))\,dx.
}
\end{aligned}
\]

Dies ist aus der bereits auditierten Reihenform abgeleitet; es wird keine RH-Annahme verwendet.

Außerdem ist aus NEU-220c

\[
\boxed{
A_\infty(0)
=
-\gamma-\frac\pi2-3\log2-\log\pi
\approx -5.37218341922566558<0.
}
\]

---

## 4. Archimedische Kantenmaßdichte

Setze `x=2s`. Dann

\[
A_\infty(t)
=
A_\infty(0)
+
2\int_0^\infty
\omega_\infty(s)(1-\cos ts)\,ds,
\]

mit

\[
\boxed{
\omega_\infty(s)
:=
\frac{e^{-s/2}}{1-e^{-2s}}>0.
}
\]

Damit besitzt der archimedische Multiplikator eine Lévy-/Dirichlet-artige Darstellung über **dieselben realen Kantenlängen `s`**, auf denen die Prime-Power-Zeiten liegen.

---

## 5. Gamma-Block als positive kontinuierliche Inzidenzenergie plus Grundterm

NEU-220c/P02 liefern

\[
B_\Gamma(a,b)
=
\frac1{2\pi}
\int_{\mathbb R}
A_\infty(t)
\widehat a(t)\overline{\widehat b(t)}\,dt.
\]

Für den zentrierten Kantenoperator gilt per Plancherel

\[
\langle D_sa,D_sb\rangle
=
\frac1{2\pi}
\int_{\mathbb R}
2(1-\cos ts)
\widehat a(t)\overline{\widehat b(t)}\,dt.
\]

Einsetzen der Darstellung aus §4 ergibt

\[
\boxed{
B_\Gamma(a,b)
=
A_\infty(0)\langle a,b\rangle
+
\int_0^\infty
\omega_\infty(s)
\langle D_sa,D_sb\rangle\,ds.
}
\]

Die Integralform ist positiv im Energieanteil:

\[
\boxed{
\mathcal E_\infty(a,a)
:=
\int_0^\infty
\omega_\infty(s)\|D_sa\|_2^2\,ds
\ge0.
}
\]

Konvergenz:

- für `s\downarrow0` gilt `\omega_\infty(s)\sim(2s)^{-1}` und `\|D_sa\|_2=O(s)`, also Integrand `O(s)`;
- für `s\to\infty` fällt `\omega_\infty(s)=O(e^{-s/2})`, während `\|D_sa\|\le2\|a\|`.

Status: `✓[K/M]`.

---

## 6. Polterm als Differenz zweier Rang-eins-Randkanäle

Definiere

\[
L_+(a):=\widehat a(i/2),
\qquad
L_-(a):=\widehat a(-i/2),
\]

und die symmetrischen/antisymmetrischen Randamplituden

\[
P_+(a):=\frac{L_+(a)+L_-(a)}{\sqrt2},
\qquad
P_-(a):=\frac{L_+(a)-L_-(a)}{\sqrt2}.
\]

NEU-220c gibt

\[
B_{\rm pole}(a,b)
=
L_+(a)\overline{L_-(b)}
+
L_-(a)\overline{L_+(b)}.
\]

Direkte Expansion liefert

\[
\boxed{
B_{\rm pole}(a,b)
=
P_+(a)\overline{P_+(b)}
-
P_-(a)\overline{P_-(b)}.
}
\]

Damit ist auch der Polsektor exakt als Rang-eins-plus minus Rang-eins typisiert.

Status: `✓[M]`.

---

## 7. Exakte gemeinsame Inzidenzform der vollständigen Weilform

Zusammen ergibt sich auf `\mathcal A_{PW}`:

\[
\boxed{
\begin{aligned}
B_W(a,b)
={}&
\int_0^\infty
\omega_\infty(s)
\langle D_sa,D_sb\rangle\,ds\\
&+
\sum_{p}\sum_{m\ge1}
\frac{\log p}{p^{m/2}}
\Bigl[
\langle D_{m\log p}a,D_{m\log p}b\rangle
-2\langle a,b\rangle
\Bigr]\\
&+
A_\infty(0)\langle a,b\rangle\\
&+
P_+(a)\overline{P_+(b)}
-
P_-(a)\overline{P_-(b)}.
\end{aligned}
}
\]

Die Prime-Power-Summe ist **als kompensierte Summe** zu lesen; für feste `a,b` ist sie effektiv endlich.

Dies ist keine neue Definition von `B_W`, sondern eine algebraisch äquivalente Reorganisation der bereits in P02 eingefrorenen Form.

---

## 8. Einheitliche Kantenlängenachse

Die beiden unendlichen Sektoren werden nun von derselben Inzidenzfamilie `D_s` auf der Achse

\[
s\in(0,\infty)
\]

gesteuert.

### Archimedischer Anteil

Kontinuierliches positives Kantenmaß

\[
\boxed{
d\nu_\infty(s)
=
\frac{e^{-s/2}}{1-e^{-2s}}\,ds.
}
\]

### Arithmetischer Anteil

Diskrete Prime-Power-Maße

\[
\boxed{
\nu_{\rm pr}
=
\sum_p\sum_{m\ge1}
\frac{\log p}{p^{m/2}}
\delta_{m\log p}.
}
\]

Damit besitzen Prim- und Archimedeskanal erstmals im P11-Strang denselben geometrischen Grundtyp:

\[
\boxed{
\text{Kantenlänge }s
\quad\mapsto\quad
D_s=U_{s/2}-U_{-s/2}.
}
\]

Sie unterscheiden sich durch ihr Maß und durch die notwendige arithmetische Kompensation.

---

## 9. Finite Cutoffs: positive Energie minus expliziter Defekt

Für eine endliche Prime-Power-Menge `F` setze

\[
W_F:=\sum_{\alpha\in F}w_\alpha,
\]

\[
\mathcal E_F(a,b)
:=
\sum_{\alpha\in F}
w_\alpha
\langle D_{\ell_\alpha}a,D_{\ell_\alpha}b\rangle,
\]

und

\[
\mathcal E_\infty(a,b)
:=
\int_0^\infty
\omega_\infty(s)
\langle D_sa,D_sb\rangle ds.
\]

Dann gilt für den prime-getrunkten Weilblock

\[
\boxed{
\begin{aligned}
B_W^F(a,b)
={}&
\mathcal E_\infty(a,b)
+\mathcal E_F(a,b)
+P_+(a)\overline{P_+(b)}\\
&-
\Bigl[
(2W_F-A_\infty(0))\langle a,b\rangle
+P_-(a)\overline{P_-(b)}
\Bigr].
\end{aligned}
}
\]

Da `A_\infty(0)<0`, ist

\[
2W_F-A_\infty(0)>0.
\]

Somit besitzt jedes endliche Modell eine explizite **positive-Energie-minus-positive-Defekt**-Darstellung.

**Wichtig:** Mit wachsendem `F` divergieren `W_F` und im Allgemeinen `\mathcal E_F` getrennt; nur ihre kompensierte Differenz ist auf dem Testkern stabil. Daraus folgt noch keine positive Grenzform und keine closable Operatorrealisierung.

---

## 10. Neue geometrische Lesart

P11-C1d liefert folgende gemeinsame Vorstruktur:

\[
\boxed{
\text{Objekt-X-Vorgeometrie}
\supset
\text{diskret-kontinuierlicher Kantenlängenraum}
\times
\text{zentrierte Translationsinzidenz }D_s.
}
\]

Der positive Teil der endlichen Modelle wird durch

- kontinuierliche archimedische Kanten,
- diskrete Prime-Power-Kanten,
- einen positiven Randkanal

erzeugt.

Der Defekt besteht aus

- einem cutoff-abhängigen skalaren Hintergrundkanal,
- einem negativen Rang-eins-Randkanal.

Das Problem der globalen Positivität wird dadurch **nicht gelöst**, aber auf eine neue konkrete Form reduziert.

---

## 11. Beziehung zum Prime–Prime-Gramkern aus C1c

C1c definierte zusätzlich den vollständigen latenten Kreuzkern

\[
G_{s,t}(a,b):=\langle D_sa,D_tb\rangle.
\]

Die eingefrorene Weilform benutzt in der Darstellung aus §7 zunächst nur die **Diagonalwerte** `G_{s,s}` gegen `\nu_\infty` bzw. `\nu_{\rm pr}`.

Die Off-Diagonalwerte

\[
G_{s,t},\qquad s\neq t,
\]

sind daher eine natürliche, positive Gramgeometrie, aber **noch keine zusätzlichen Weil-Summanden**.

Damit ist die P11-Hauptfrage jetzt präzise:

\[
\boxed{
\text{Gibt es eine kanonische nichtorthogonale Faktorisierung/Kompression, die die latenten }G_{s,t}\text{-Kreuzblöcke nutzt,}\
\text{den expliziten Defekt kontrolliert und trotzdem exakt dieselbe }B_W\text{ komprimiert?}
}
\]

---

## 12. Scope-Firewalls

Aus C1d folgt **nicht**:

1. `B_W\ge0`;
2. RH;
3. eine globale positive Vervollständigung;
4. Closability auf Haar-`L^2` — P03 schließt diesen Weg im relevanten Scope aus;
5. dass die Off-Diagonalwerte `G_{s,t}` beliebig zu `B_W` addiert werden dürfen;
6. dass getrennte positive/negative Teile einen konvergenten unendlichen Grenzwert besitzen;
7. dass der cutoff-abhängige Defekt durch eine endlichrangige Korrektur beherrscht wird.

Insbesondere bleibt die NEU-250-/P10-Firewall gegen additive Kreuzterme vollständig intakt.

---

## 13. Statusmatrix

| Aussage | Status |
|---|---|
| gemeinsame Inzidenzfamilie `D_s` für Prim und Gamma | `✓[K/M]` |
| Gamma-Lévy-Darstellung aus NEU-220c-Reihe | `✓[M]` |
| positive kontinuierliche Gamma-Inzidenzenergie | `✓[K/M]` |
| globale kompensierte Prime-Power-Inzidenzform | `✓[K/M]` |
| Polterm = positiver Rang-1-Kanal minus negativer Rang-1-Kanal | `✓[M]` |
| exakte gemeinsame Inzidenzform von `B_W` | `✓[K/M]` |
| finite positive-Energie-minus-Defekt-Darstellung | `✓[K/M]` |
| getrennte unendliche positive Prime-Energie | `×[M]` ohne Renormierung |
| positive Objekt-X-Vervollständigung | `?[O]` |
| kanonische Nutzung der latenten `G_{s,t}`, `s\neq t` | `?[O]` |
| exakte nichtorthogonale Faktorisierung mit Defektkontrolle | `?[O]` |

---

## 14. Nächster Knoten

\[
\boxed{[P11\text{-}C1e]\quad\text{Defektkontrollproblem auf dem diskret-kontinuierlichen Kantenraum}.}
\]

Zu prüfen ist **nicht**, ob man den negativen Defekt frei wegoptimieren kann. Zu prüfen ist, ob die gemeinsame Quellenstruktur eine kanonische lineare Relation/Kompression zwischen

\[
\{D_sa\}_{s>0},
\qquad
\{D_{m\log p}a\}_{p,m},
\qquad
\langle a,\cdot\rangle,
\qquad
P_-(a)
\]

erzeugt, aus der eine positive Gramform folgt.

Ein möglicher mathematischer Prüfstein ist eine **source-induced Poincaré-/frameartige Ungleichung** auf endlichen Cutoffs:

\[
\mathcal E_\infty(a,a)+\mathcal E_F(a,a)+|P_+(a)|^2
\stackrel{?}{\ge}
(2W_F-A_\infty(0))\|a\|_2^2+|P_-(a)|^2,
\]

aber diese Ungleichung darf nicht als Annahme eingeführt werden: im passenden globalen Grenzregime ist sie unmittelbar mit der Weil-Positivitätsfrage verknüpft. Gesucht ist eine **arithmetische Struktur, die sie erzwingt**, nicht ein neuer äquivalenter Positivitätstest.
