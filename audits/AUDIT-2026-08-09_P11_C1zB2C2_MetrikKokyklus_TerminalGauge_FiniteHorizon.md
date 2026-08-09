# P11-C1z-B2-C2 — Kohärenzaudit des Metrik-Kokyklus: Terminal-Gauge und finite-horizon Trivialisierung

**Datum:** 9. August 2026  
**Knoten:** `[P11-C1z-B2-C2]`  
**Vorgänger:** C1z-B2-C1  
**Schnittstellen:** C1z-B2-B/C/C1; P03-Haar-L2-Firewall; P04 nur als spätere strukturelle Analogie

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C2]
\quad
\checkmark[K/M]_{\rm part}
}
\]

mit den neuen exakten Befunden

\[
\boxed{
\text{jeder endliche Source-Horizont besitzt eine kanonische kohärente isometrische Trivialisierung}
}
\]

und

\[
\boxed{
\Omega_{R,S,T}\text{ ist die Überlappung zweier verschiedener Metrik-Gauges, nicht bereits eine intrinsische endliche 2-Kokyklusklasse.}
}
\]

Der harte offene Punkt verschiebt sich damit von der **finite-level Kohärenz** zur **asymptotischen Terminalmetrik**

\[
G_{R,T},\qquad T\to\infty.
\]

---

# 0. Urteil

C1z-B2-C1 hatte die nativen Transitionen

\[
J_{R,S}:\mathcal K_{X,R}\to\mathcal K_{X,S}
\]

mit exaktem Kokyklus

\[
J_{S,T}J_{R,S}=J_{R,T}
\]

und die positiven invertierbaren Metrikoperatoren

\[
G_{R,S}:=J_{R,S}^*J_{R,S}
\]

konstruiert. Ferner gilt der exakte Pullback-Kokyklus

\[
\boxed{
G_{R,T}=J_{R,S}^*G_{S,T}J_{R,S}.
}
\tag{C1zB2C2.1}
\]

Die paarweisen Polar-Isometrien

\[
V_{R,S}:=J_{R,S}G_{R,S}^{-1/2}
\]

sind isometrisch, aber ihr Kokyklus war offen:

\[
V_{S,T}V_{R,S}\stackrel?=V_{R,T}.
\]

Der vorliegende Knoten zeigt, dass dies **nicht die richtige globale Form der Kohärenzfrage** ist.

Für jedes feste Terminallevel `T` existiert nämlich bereits eine exakte kohärente Isometrisierung aller früheren Level:

\[
\boxed{
W_{R,S}^{[T]}
:=G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2},
\qquad R<S\le T.
}
\tag{C1zB2C2.2}
\]

Diese Operatoren erfüllen gleichzeitig

\[
\boxed{(W_{R,S}^{[T]})^*W_{R,S}^{[T]}=I}
\tag{C1zB2C2.3}
\]

und

\[
\boxed{
W_{S,U}^{[T]}W_{R,S}^{[T]}
=W_{R,U}^{[T]},
\qquad R<S<U\le T.
}
\tag{C1zB2C2.4}
\]

Damit ist der Metrik-Kokyklus auf jedem endlichen Horizont **exakt trivialisiert**.

Die native Polar-Isometrie ist nur der Spezialfall, bei dem jede Kante ihren eigenen Zielhorizont als Gauge verwendet:

\[
\boxed{
V_{R,S}=W_{R,S}^{[S]}.
}
\tag{C1zB2C2.5}
\]

Der scheinbare Polar-Kokyklusfehler entsteht also dadurch, dass in

\[
V_{S,T}V_{R,S}
\]

die erste Kante `R->S` in der `S`-Gauge und die zweite Kante `S->T` in der `T`-Gauge normiert wird.

Das ist eine **Gauge-Inkohärenz**, keine bereits bewiesene intrinsische Krümmung des endlichen Systems.

Der wirkliche Objekt-X-Engpass lautet jetzt:

\[
\boxed{
\text{Existiert eine kanonische Terminal-Gauge für }T=\infty?
}
\]

also insbesondere: konvergieren die zurückgezogenen Zukunftsmetriken `G_{R,T}` für festes `R` in einer geeigneten Topologie?

---

# 1. Verbindliche Daten aus C1

Für `R<S`:

\[
J_{R,S}:=J_{R,S}^X
\]

ist ein beschränkter injektiver Operator zwischen den Hilberträumen

\[
\mathcal K_{X,R},\qquad \mathcal K_{X,S},
\]

mit geschlossenem Bild und exaktem Kokyklus

\[
\boxed{J_{S,T}J_{R,S}=J_{R,T}.}
\tag{C1zB2C2.6}
\]

Der Metrikoperator ist

\[
\boxed{G_{R,S}:=J_{R,S}^*J_{R,S}.}
\tag{C1zB2C2.7}
\]

C1 beweist die levelweise Untergrenze

\[
\boxed{
G_{R,S}
\ge
c_R I,
\qquad
c_R:=\frac1{1+\|H_R\|^2}>0,
}
\tag{C1zB2C2.8}
\]

für alle `S>R`.

Damit sind

\[
G_{R,S}^{\pm1/2}
\]

beschränkt und wohldefiniert.

Wir setzen der Notation halber

\[
\boxed{J_{R,R}:=I,\qquad G_{R,R}:=I.}
\tag{C1zB2C2.9}
\]

Dann gelten alle nachfolgenden Formeln auch an den Terminalrändern.

---

# 2. Exakter metrischer Pullback-Kokyklus

Aus (C1zB2C2.6):

\[
\begin{aligned}
G_{R,T}
&=J_{R,T}^*J_{R,T}\\
&=J_{R,S}^*J_{S,T}^*J_{S,T}J_{R,S}\\
&=J_{R,S}^*G_{S,T}J_{R,S}.
\end{aligned}
\]

Also erneut verbindlich:

\[
\boxed{
G_{R,T}
=J_{R,S}^*G_{S,T}J_{R,S}.
}
\tag{C1zB2C2.10}
\]

Dies ist stärker als eine bloße Größenvergleichsrelation. Es ist eine exakte Pullback-Identität positiver Metriken.

Für die quadratischen Formen:

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}
=
\langle G_{S,T}J_{R,S}f,J_{R,S}f\rangle_{X,S}.
}
\tag{C1zB2C2.11}
\]

Damit ist jede Zukunftsmetrik am Level `R` exakt die Rückziehung der entsprechenden Zukunftsmetrik am Level `S`.

---

# 3. Terminalmetrik auf einem festen endlichen Horizont

Fixiere nun ein Terminallevel

\[
T>0.
\]

Für jedes `R<T` definiere die `T`-Zukunftsmetrik auf `K_{X,R}` durch

\[
\boxed{
\langle f,g\rangle_{R}^{[T]}
:=
\langle G_{R,T}f,g\rangle_{X,R}.
}
\tag{C1zB2C2.12}
\]

Da `G_{R,T}` positiv und invertierbar ist, ist dies ein Hilbertskalarprodukt mit äquivalenter Norm

\[
\|f\|_{R,[T]}^2
=
\langle G_{R,T}f,f\rangle_{X,R}
=
\|J_{R,T}f\|_{X,T}^2.
\tag{C1zB2C2.13}
\]

Die letzte Identität zeigt unmittelbar:

\[
\boxed{
J_{R,T}:
(\mathcal K_{X,R},\|\cdot\|_{R,[T]})
\longrightarrow
\mathcal K_{X,T}
\text{ ist isometrisch auf sein Bild}.}
\tag{C1zB2C2.14}
\]

Wichtiger ist aber die Kompatibilität für alle Zwischenlevel.

---

# 4. Satz C2.1 — finite-horizon isometric system

Für jedes feste `T` und alle

\[
R<S\le T
\]

ist die native Transition

\[
J_{R,S}
\]

zwischen den `T`-Zukunftsmetriken isometrisch:

\[
\boxed{
\|J_{R,S}f\|_{S,[T]}
=
\|f\|_{R,[T]}.
}
\tag{C1zB2C2.15}
\]

### Beweis

Mit (C1zB2C2.10):

\[
\begin{aligned}
\|J_{R,S}f\|_{S,[T]}^2
&=\langle G_{S,T}J_{R,S}f,J_{R,S}f\rangle_{X,S}\\
&=\langle J_{R,S}^*G_{S,T}J_{R,S}f,f\rangle_{X,R}\\
&=\langle G_{R,T}f,f\rangle_{X,R}\\
&=\|f\|_{R,[T]}^2.
\end{aligned}
\]

`□`

Damit besitzt jedes endliche Intervall von Source-Leveln bereits einen **kohärenten isometrischen Hilbertapparat**, sobald alle Level mit derselben Terminalmetrik betrachtet werden.

Status:

\[
\boxed{\checkmark[M].}
\]

---

# 5. Dasselbe auf den nativen Hilberträumen: Terminal-Gauge-Operatoren

Statt die Skalarprodukte umzubenennen, kann man dieselbe Konstruktion als explizite Isometrien zwischen den nativen Graphräumen schreiben.

Definiere

\[
\boxed{
W_{R,S}^{[T]}
:=
G_{S,T}^{1/2}
J_{R,S}
G_{R,T}^{-1/2},
\qquad R<S\le T.
}
\tag{C1zB2C2.16}
\]

Dann

\[
\begin{aligned}
(W_{R,S}^{[T]})^*W_{R,S}^{[T]}
&=
G_{R,T}^{-1/2}
J_{R,S}^*
G_{S,T}
J_{R,S}
G_{R,T}^{-1/2}\\
&=
G_{R,T}^{-1/2}G_{R,T}G_{R,T}^{-1/2}\\
&=I.
\end{aligned}
\]

Also

\[
\boxed{
W_{R,S}^{[T]}:
\mathcal K_{X,R}\hookrightarrow\mathcal K_{X,S}
\text{ ist isometrisch}.}
\tag{C1zB2C2.17}
\]

Status: `✓[M]`.

---

# 6. Satz C2.2 — exakter Kokyklus der Terminal-Gauge-Isometrien

Für

\[
R<S<U\le T
\]

gilt exakt

\[
\boxed{
W_{S,U}^{[T]}W_{R,S}^{[T]}
=W_{R,U}^{[T]}.
}
\tag{C1zB2C2.18}
\]

### Beweis

\[
\begin{aligned}
W_{S,U}^{[T]}W_{R,S}^{[T]}
={}&
G_{U,T}^{1/2}J_{S,U}G_{S,T}^{-1/2}
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}\\
={}&
G_{U,T}^{1/2}J_{S,U}J_{R,S}G_{R,T}^{-1/2}\\
={}&
G_{U,T}^{1/2}J_{R,U}G_{R,T}^{-1/2}\\
={}&W_{R,U}^{[T]}.
\end{aligned}
\]

`□`

Damit:

\[
\boxed{
\{\mathcal K_{X,R},W_{R,S}^{[T]}\}_{R<S\le T}
}
\]

ist für jedes feste endliche `T` ein **echtes gerichtetes System mit isometrischen Transitionen**.

Dies ist der stärkste konstruktive Kohärenzbefund des C1z-Strangs bis hierher.

---

# 7. Die native Polar-Isometrie ist nur die Immediate-Target-Gauge

C1 definiert

\[
V_{R,S}:=J_{R,S}G_{R,S}^{-1/2}.
\]

Wegen

\[
G_{S,S}=I
\]

folgt aus (C1zB2C2.16) mit Terminallevel `T=S`:

\[
\boxed{
W_{R,S}^{[S]}
=J_{R,S}G_{R,S}^{-1/2}
=V_{R,S}.
}
\tag{C1zB2C2.19}
\]

Das ist die konzeptionelle Schlüsselidentität dieses Knotens.

Die Polar-Isometrisierung verwendet auf jeder einzelnen Kante die Metrik des **unmittelbaren Ziellevels**.

In einem Dreieck

\[
R<S<T
\]

werden daher in

\[
V_{S,T}V_{R,S}
\]

zwei verschiedene Terminal-Gauges gemischt:

- `V_{R,S}=W_{R,S}^{[S]}`;
- `V_{S,T}=W_{S,T}^{[T]}`.

Die kohärente `T`-Gauge wäre dagegen

\[
W_{S,T}^{[T]}W_{R,S}^{[T]}
=W_{R,T}^{[T]}.
\]

Damit ist klar:

\[
\boxed{
\text{Polar-Kokyklusfehler}
=\text{Mismatch verschiedener Terminal-Gauges}.}
\tag{C1zB2C2.20}
\]

Dies ist eine strukturelle Reinterpretation des C1-Engpasses.

---

# 8. Exakte Formel für den Obstruktionsoperator Omega

C1 definierte

\[
\Omega_{R,S,T}
:=V_{R,T}^*V_{S,T}V_{R,S}.
\]

Da

\[
V_{R,T}=W_{R,T}^{[T]},
\qquad
V_{S,T}=W_{S,T}^{[T]},
\]

und der Terminal-Kokyklus liefert

\[
W_{R,T}^{[T]}
=W_{S,T}^{[T]}W_{R,S}^{[T]},
\]

folgt

\[
\begin{aligned}
\Omega_{R,S,T}
&=(W_{R,T}^{[T]})^*W_{S,T}^{[T]}V_{R,S}\\
&=(W_{R,S}^{[T]})^*(W_{S,T}^{[T]})^*W_{S,T}^{[T]}V_{R,S}\\
&=(W_{R,S}^{[T]})^*V_{R,S}.
\end{aligned}
\]

Also

\[
\boxed{
\Omega_{R,S,T}
=(W_{R,S}^{[T]})^*W_{R,S}^{[S]}.
}
\tag{C1zB2C2.21}
\]

**Interpretation:** `Omega` ist die Überlappung zweier isometrischer Einbettungen derselben Source-Geometrie `K_{X,R}` nach `K_{X,S}`:

1. der kohärenten Zukunfts-/Terminal-`T`-Gauge;
2. der lokalen Immediate-Target-/Polar-`S`-Gauge.

Damit ist `Omega` eine **Gauge-Overlap-Matrix**, nicht bereits eine gauge-invariante endliche Krümmungsklasse.

---

# 9. Explizite positive Operatorformel für Omega

Aus

\[
W_{R,S}^{[T]}
=G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}
\]

folgt

\[
(W_{R,S}^{[T]})^*
=G_{R,T}^{-1/2}J_{R,S}^*G_{S,T}^{1/2}.
\]

Mit

\[
V_{R,S}=J_{R,S}G_{R,S}^{-1/2}
\]

ergibt sich

\[
\boxed{
\Omega_{R,S,T}
=
G_{R,T}^{-1/2}
J_{R,S}^*G_{S,T}^{1/2}J_{R,S}
G_{R,S}^{-1/2}.
}
\tag{C1zB2C2.22}
\]

Diese Formel ist exakt.

Sie zeigt auch unmittelbar, warum `Omega` im Allgemeinen weder positiv noch selbstadjungiert sein muss: die beteiligten positiven Quadratwurzeln müssen nicht kommutieren.

Status: `✓[M]`.

---

# 10. Omega ist immer eine Kontraktion — exakte Leakage-Faktorisierung

Setze

\[
A:=W_{R,S}^{[T]},
\qquad
B:=V_{R,S}=W_{R,S}^{[S]}.
\]

Beide sind Isometrien

\[
A,B:\mathcal K_{X,R}\to\mathcal K_{X,S}.
\]

Dann

\[
\Omega=A^*B.
\]

Also

\[
\boxed{\|\Omega\|\le1.}
\tag{C1zB2C2.23}
\]

Sei

\[
P_{R,S}^{[T]}:=AA^*
\]

die orthogonale Projektion auf

\[
\operatorname{Ran}W_{R,S}^{[T]}.
\]

Definiere den Gauge-Leakage-Operator

\[
\boxed{
L_{R,S,T}
:=(I-P_{R,S}^{[T]})V_{R,S}.
}
\tag{C1zB2C2.24}
\]

Dann gilt die orthogonale Zerlegung

\[
\boxed{
V_{R,S}
=W_{R,S}^{[T]}\Omega_{R,S,T}
+L_{R,S,T},
}
\tag{C1zB2C2.25}
\]

mit

\[
(W_{R,S}^{[T]})^*L_{R,S,T}=0.
\]

Folglich

\[
\boxed{
I-\Omega_{R,S,T}^*\Omega_{R,S,T}
=L_{R,S,T}^*L_{R,S,T}\ge0.
}
\tag{C1zB2C2.26}
\]

Dies ist eine exakte positive Defektfaktorisierung.

### Konsequenzen

1. `Omega` ist unitär nur dann, wenn zusätzlich der Co-Defekt verschwindet;
2. `Omega` ist isometrisch genau dann, wenn `L_{R,S,T}=0`, also

\[
\operatorname{Ran}V_{R,S}
\subseteq
\operatorname{Ran}W_{R,S}^{[T]};
\]

3. sind beide Bildräume gleich, ist `Omega` unitär;
4. `Omega=I` genau dann, wenn die beiden isometrischen Einbettungen selbst identisch sind:

\[
\boxed{
\Omega_{R,S,T}=I
\iff
V_{R,S}=W_{R,S}^{[T]}.
}
\tag{C1zB2C2.27}
\]

Über (C1zB2C2.19) ist dies exakt die Polar-Kokyklusbedingung aus C1.

---

# 11. Wichtige Statuskorrektur: Omega ist kein intrinsischer finite-horizon 2-Kokyklus

C1 hatte `Omega` bewusst als **Obstruktionsoperator** eingeführt. Diese Bezeichnung bleibt als Diagnoseoperator korrekt.

Nach dem vorliegenden Knoten muss aber eine stärkere Interpretation vermieden werden:

\[
\boxed{
\Omega\ne I
\text{ würde nicht bedeuten, dass der endliche Metrik-Kokyklus nicht trivialisiert werden kann.}
}
\tag{C1zB2C2.28}
\]

Denn (C1zB2C2.16)--(C1zB2C2.18) liefern für jedes feste `T` bereits eine exakte kohärente Trivialisierung.

Daher ist `Omega` präziser:

\[
\boxed{
\text{ein Associator / Gauge-Mismatch der kantenweisen Polar-Normalisierung.}
}
\tag{C1zB2C2.29}
\]

Es ist **nicht** bereits eine gauge-invariante Kohomologieklasse oder Krümmung.

Eine solche stärkere geometrische Interpretation würde zusätzliche Struktur erfordern, z.B. eine kanonisch ausgezeichnete Gaugeklasse oder einen asymptotischen Holonomiebegriff.

Status-Firewall: `✓[M]` für die finite-horizon Trivialisierung; keine Behauptung über einen unendlichen Horizont.

---

# 12. Gauge-Wechsel zwischen zwei Terminalhorizonten

Fixiere

\[
R<T<U.
\]

Definiere auf `K_{X,R}` den Horizon-Gauge-Wechsel

\[
\boxed{
C_R^{T\to U}
:=G_{R,U}^{1/2}G_{R,T}^{-1/2}.
}
\tag{C1zB2C2.30}
\]

Da beide Faktoren invertierbar sind, ist `C_R^{T->U}` ein beschränkter Automorphismus.

Für `R<S\le T<U` gilt dann exakt

\[
\boxed{
W_{R,S}^{[U]}
=
C_S^{T\to U}
W_{R,S}^{[T]}
(C_R^{T\to U})^{-1}.
}
\tag{C1zB2C2.31}
\]

### Beweis

\[
\begin{aligned}
C_S^{T\to U}W_{R,S}^{[T]}(C_R^{T\to U})^{-1}
={}&
G_{S,U}^{1/2}G_{S,T}^{-1/2}
G_{S,T}^{1/2}J_{R,S}G_{R,T}^{-1/2}
G_{R,T}^{1/2}G_{R,U}^{-1/2}\\
={}&
G_{S,U}^{1/2}J_{R,S}G_{R,U}^{-1/2}\\
={}&W_{R,S}^{[U]}.
\end{aligned}
\]

`□`

Damit sind alle finite-horizon isometrischen Systeme **exakt gauge-konjugiert**.

---

# 13. Horizon-Gauge-Wechsel selbst erfüllt einen exakten Kokyklus

Für

\[
T<U<V
\]

gilt auf jedem festen früheren Level `R<T`:

\[
\begin{aligned}
C_R^{U\to V}C_R^{T\to U}
&=
G_{R,V}^{1/2}G_{R,U}^{-1/2}
G_{R,U}^{1/2}G_{R,T}^{-1/2}\\
&=
G_{R,V}^{1/2}G_{R,T}^{-1/2}.
\end{aligned}
\]

Also

\[
\boxed{
C_R^{U\to V}C_R^{T\to U}
=C_R^{T\to V}.
}
\tag{C1zB2C2.32}
\]

Das ist ein weiterer exakter Kohärenzbefund.

Der Gauge-Wechsel ist im Allgemeinen nicht unitär. Seine positive metrische Größe ist

\[
\boxed{
(C_R^{T\to U})^*C_R^{T\to U}
=
G_{R,T}^{-1/2}G_{R,U}G_{R,T}^{-1/2}.
}
\tag{C1zB2C2.33}
\]

Dies ist der natürliche **relative Zukunftsmetrikoperator** zwischen den Horizonten `T` und `U`.

---

# 14. Was ein globaler Terminalhorizont leisten würde

Die finite-horizon Theorie legt jetzt einen sehr konkreten Grenzmechanismus nahe.

Angenommen, für jedes feste `R` existiert ein positiver beschränkter invertierbarer Operator

\[
G_{R,\infty}
\]

mit

\[
\boxed{
G_{R,T}\xrightarrow[T\to\infty]{\rm strong}G_{R,\infty}.
}
\tag{C1zB2C2.34}
\]

Dann folgt wegen der festen Untergrenze (C1zB2C2.8) und der Uniform-Boundedness-Principle:

- `G_{R,T}^{1/2}->G_{R,infty}^{1/2}` stark;
- `G_{R,T}^{-1/2}->G_{R,infty}^{-1/2}` stark.

Der Pullback-Kokyklus geht dann für `R<S` in den Grenzwert über:

\[
\boxed{
G_{R,\infty}
=J_{R,S}^*G_{S,\infty}J_{R,S}.
}
\tag{C1zB2C2.35}
\]

Man kann daher definieren

\[
\boxed{
W_{R,S}^{[\infty]}
:=
G_{S,\infty}^{1/2}
J_{R,S}
G_{R,\infty}^{-1/2}.
}
\tag{C1zB2C2.36}
\]

Dann gilt exakt

\[
\boxed{
(W_{R,S}^{[\infty]})^*W_{R,S}^{[\infty]}=I
}
\tag{C1zB2C2.37}
\]

und

\[
\boxed{
W_{S,T}^{[\infty]}W_{R,S}^{[\infty]}
=W_{R,T}^{[\infty]}.
}
\tag{C1zB2C2.38}
\]

Dies wäre unmittelbar ein **globaler isometrischer Hilbert-Induktivapparat**.

### Wichtig

(C1zB2C2.34) ist aktuell **nicht bewiesen**.

Der vorliegende Satz ist ein Konditionalsatz:

\[
\boxed{
\text{bounded strong convergence der Zukunftsmetriken}
\Longrightarrow
\text{kohärente globale isometrische Objekt-X-Gauge}.
}
\tag{C1zB2C2.39}
\]

---

# 15. Warum die Untergrenze für den Grenztest bereits günstig ist

Aus C1 gilt für festes `R` und alle `T>R`

\[
G_{R,T}\ge c_RI,
\qquad
c_R>0.
\]

Damit kann ein möglicher starker Grenzwert nicht durch Verlust der unteren Positivität degenerieren:

\[
G_{R,\infty}\ge c_RI.
\]

Der zentrale asymptotische Engpass ist also **nicht** die Invertierbarkeit von unten.

Er lautet vielmehr:

\[
\boxed{
\text{Sind }G_{R,T}\text{ für festes }R\text{ nach oben kontrolliert und stark Cauchy?}
}
\tag{C1zB2C2.40}
\]

C1z-B2-C hatte bereits gezeigt, dass keine einfache Monotonie in `T` vorausgesetzt werden darf, weil Hubwachstum und Feshbach-Screening gegeneinander arbeiten.

Daher ist weder monotone Formkonvergenz noch Divergenz aktuell gebucht.

---

# 16. Gleichwertige Form des asymptotischen Problems

Für festes `R` gilt

\[
\langle G_{R,T}f,f\rangle_{X,R}
=
\|J_{R,T}f\|_{X,T}^2.
\]

Da der Gammaanteil unter Nullfortsetzung exakt erhalten bleibt,

\[
q_{\Gamma,T}(J_{R,T}f)=q_{\Gamma,R}(f),
\]

ist

\[
\boxed{
\langle G_{R,T}f,f\rangle_{X,R}
=
q_{\Gamma,R}(f)+\sigma_T(J_{R,T}f).
}
\tag{C1zB2C2.41}
\]

während

\[
\|f\|_{X,R}^2
=q_{\Gamma,R}(f)+\sigma_R(f).
\]

Damit ist die gesamte Zukunftsmetrikdynamik exakt im Schurterm

\[
\boxed{
\sigma_T(J_{R,T}f)
=
\langle H_T^*J_{R,T}f,
(I+R_T^*R_T)^{-1}H_T^*J_{R,T}f\rangle.
}
\tag{C1zB2C2.42}
\]

konzentriert.

Der nächste Grenztest ist deshalb kein abstrakter Operatortrick, sondern die konkrete Frage:

\[
\boxed{
\sigma_T(J_{R,T}f)\stackrel?{\longrightarrow}\sigma_{R,\infty}(f)
\quad\text{für festen kompakten Source-Vektor }f.
}
\tag{C1zB2C2.43}
\]

---

# 17. Konsequenz für die Interpretation von Objekt X

Nach C2 ist die folgende Aussage jetzt präziser als die Formulierung aus C1:

Nicht

\[
\text{„Objekt X ist die Trivialisierung eines möglicherweise nichttrivialen endlichen 2-Kokyklus“},
\]

sondern

\[
\boxed{
\text{Objekt X könnte die stabile }T\to\infty\text{-Terminal-Gauge eines bereits finite-level flachen Metriksystems sein.}
}
\tag{C1zB2C2.44}
\]

Das ist konzeptionell ein erheblicher Unterschied.

Finite-level ist die Geometrie bereits flach im kategorialen Sinn, weil ein Terminalobjekt `T` die Pullbackmetriken kanonisch trivialisiert.

Die potenziell neue arithmetische Information liegt daher eher in

1. der asymptotischen Entwicklung `G_{R,T}`;
2. den Horizon-Gauge-Wechseln `C_R^{T->U}`;
3. einem möglichen Grenzoperator `G_{R,infty}`;
4. einer eventuell notwendigen Renormierung, falls `G_{R,T}` keinen bounded strong limit besitzt.

---

# 18. Beziehung zu Omega — präzise neue Rolle

`Omega` bleibt nützlich. Aus (C1zB2C2.21):

\[
\Omega_{R,S,T}
=(W_{R,S}^{[T]})^*W_{R,S}^{[S]}.
\]

Damit misst `Omega` für festes Dreieck `R<S<T`, wie stark sich die optimale isometrische Einbettung der Kante `R->S` ändert, wenn der Zukunftshorizont von `S` auf `T` verschoben wird.

Also:

\[
\boxed{
\Omega\text{ misst Horizon-Sensitivität der isometrischen Gauge.}
}
\tag{C1zB2C2.45}
\]

Dies kann durchaus arithmetisch relevante Information tragen.

Aber die richtige Frage ist dann nicht mehr nur

\[
\Omega\stackrel?=I,
\]

sondern asymptotisch etwa

\[
\boxed{
\Omega_{R,S,T}\stackrel?{\longrightarrow}\Omega_{R,S,\infty}
\quad(T\to\infty)
}
\tag{C1zB2C2.46}
\]

oder, stärker,

\[
\Omega_{R,S,T}\to I.
\]

Auch dies bleibt offen.

---

# 19. Firewalls

Aus C1z-B2-C2 folgt **nicht**:

1. dass der native Polar-Kokyklus `V_{S,T}V_{R,S}=V_{R,T}` gilt;
2. dass `Omega=I` gilt;
3. dass `Omega` für konkrete C1z-Level nichttrivial ist;
4. dass `G_{R,T}` für `T->infty` konvergiert;
5. dass `G_{R,T}` uniform nach oben beschränkt ist;
6. dass eine monotone Zukunftsmetrik existiert;
7. dass ein Grenzraum `K_X` bereits konstruiert ist;
8. dass der Grenzraum die exakte Weilform realisiert;
9. eine Identifikation mit `H_W` oder Suzuki/P04;
10. RH;
11. einen Abschluss von P10-O07;
12. P11-SYN oder P11-Seal.

Insbesondere bleibt P11 **ACTIVE**.

---

# 20. Statusmatrix

| Aussage | Status |
|---|---|
| nativer `J`-Kokyklus | `✓[K/M]` aus C/C1 |
| metrischer Pullback-Kokyklus | `✓[M]` aus C1 |
| `G_{R,T}>=c_R I` uniform in Zukunftshorizont | `✓[K/M]` |
| Terminalmetrik `q_R^[T]` positiv/invertierbar | `✓[M]` |
| `J_{R,S}` isometrisch zwischen gemeinsamen `T`-Terminalmetriken | `✓[M]` |
| `W_{R,S}^[T]` isometrisch auf nativen Graphräumen | `✓[M]` |
| exakter Kokyklus der `W^[T]` | `✓[M]` |
| native Polar-Isometrie `V_{R,S}=W_{R,S}^[S]` | `✓[M]` |
| `Omega=(W^[T])^*W^[S]` | `✓[M]` |
| `Omega` kontraktiv | `✓[M]` |
| positive Leakage-Faktorisierung `I-Omega*Omega=L*L` | `✓[M]` |
| Horizon-Gauge-Konjugation zwischen `W^[T]` und `W^[U]` | `✓[M]` |
| Gauge-Wechsel-Kokyklus `C^{U->V}C^{T->U}=C^{T->V}` | `✓[M]` |
| finite-horizon Metriksystem kohärent isometrisch trivialisiert | `✓[K/M]` |
| `Omega` intrinsische finite 2-Kokyklusklasse | `×` als Schlussfolgerung; nicht gerechtfertigt |
| bounded strong limit `G_{R,infty}` | `?[O]` |
| globaler `W^[infty]`-Kokyklus | `?[O]`, konditional auf `G_{R,infty}` |
| finaler Objekt-X-Hilbertlimes | `?[O]` |

---

# 21. Strukturelles Gesamtbild

Die C1z-Kette ist damit weiter geschärft:

\[
\boxed{
\begin{array}{c}
\text{finite-level Graphräume}\\
\downarrow\\
\text{bounded injective native Transitionen }J\\
\downarrow\\
\text{positive Pullbackmetriken }G_{R,S}\\
\downarrow\\
\text{paarweise Polar-Isometrien }V_{R,S}\\
\downarrow\\
\text{scheinbarer Polar-Kokyklusfehler }\Omega\\
\downarrow\\
\textbf{Terminal-Gauge-Reorganisation}\\
\downarrow\\
\text{für jedes endliche }T:\ \textbf{exakter isometrischer Kokyklus }W^{[T]}\\
\downarrow\\
\text{einziger verbleibender Kohärenzengpass: }T\to\infty.
\end{array}
}
\]

Der entscheidende Satz ist daher nicht mehr

\[
\Omega_{R,S,T}=I\ ?
\]

sondern

\[
\boxed{
G_{R,T}\xrightarrow[T\to\infty]{}G_{R,\infty}\ ?
}
\]

in einer Topologie, die Quadratwurzel, Inverse und Pullback verträgt.

---

# 22. Nächster atomarer Knoten

Der nächste Schritt ist nun eindeutig:

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C3]
\quad
\text{Asymptotikaudit der Zukunftsmetriken }G_{R,T}.
}
\]

Für festes `R` ist zu prüfen:

### C3-A — pointwise/form convergence

Für `f,g` in einem dichten Source-Kern:

\[
\langle G_{R,T}f,g\rangle_{X,R}
\stackrel?\longrightarrow
\mathfrak g_{R,\infty}(f,g).
\]

Wegen (C1zB2C2.41)--(C1zB2C2.42) reduziert sich dies auf den Schurterm

\[
\sigma_T(J_{R,T}f,J_{R,T}g).
\]

### C3-B — uniform boundedness / blow-up alternative

Entweder

\[
\sup_{T>R}\|G_{R,T}\|<\infty
\]

und starke Kompaktheits-/Cauchyargumente werden möglich,

oder es existiert ein konkreter Source-Vektor mit

\[
\|J_{R,T}f\|_{X,T}\to\infty,
\]

was eine notwendige Renormierung des Terminal-Gauges erzwingt.

### C3-C — renormalized horizon gauge

Falls unbeschränkter Drift vorliegt, ist zu testen, ob kanonische positive Skalierungen `A_T` existieren, sodass

\[
A_T^{-1/2}G_{R,T}A_T^{-1/2}
\]

bzw. die entsprechenden Pullbacks einen nichttrivialen Grenzwert besitzen.

**Leitfrage:**

\[
\boxed{
\text{Stabilisiert sich die bereits finite-level flache Metrik bei unendlichem Zukunftshorizont?}
}
\]
