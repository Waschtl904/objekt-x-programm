# P11-C1z-B2-C6b — Cross-Frame-Principal-Angles, whitened Jet-Tails und finite-window Cauchy-Kriterium

**Datum:** 10. August 2026  
**Knoten:** `[P11-C1z-B2-C6b]`  
**Direkte Voraussetzungen:** C1z-B2-C2, C1z-B2-C4, C1z-B2-C5, C1z-B2-C6, C1z-B2-C6a  
**Negativ-Firewalls, die ausdrücklich fortgelten:** C1y, C1z-B2-A, C1z-B2-B, C1z-B2-C4, C1z-B2-C6 Finite-Jet-Faktorisierungs-No-Go, C1z-B2-C6a Self-Gram-/Kompressions-No-Gos  
**Synthesis-Gate:** P11 bleibt `PASS-A ACTIVE`; kein SYN, kein Seal, kein `papers/P11`.

**Status:**

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6b]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,cross\text{-}frame\text{-}contraction}
+
\checkmark[M]_{\rm pos,principal\text{-}angle\text{-}defects}
+
\checkmark[M]_{\rm pos,domain\text{-}polar\text{-}factorization}
+
\checkmark[M]_{\rm pos,whitened\text{-}tail\text{-}criterion}
+
\checkmark[M]_{\rm pos,finite\text{-}window\text{-}Cauchy\text{-}reduction}
+
\checkmark[M]_{\rm neg,C2\text{-}flatness\text{-}alone}
}
\]

C6b korrigiert zunächst eine naheliegende, aber falsche Interpretation des C6a-Cross-Frame-Winkels und reduziert danach das volle finite-window Terminal-Cauchyproblem auf zwei dimensionslose Defekte.

1. Für zwei Isometrien `Q_T^E,Q_U^E:E->H` ist

   \[
   \Theta_{T,U}^E=(Q_T^E)^\dagger Q_U^E
   \]

   im Allgemeinen **keine unitäre Matrix**, sondern nur eine Kontraktion.
2. Der Betrag `|Theta|` misst die Principal-Angles der beiden terminalen Bildräume; ein eventueller polarer unitärer Faktor misst zusätzlich die interne Frame-Orientierung.
3. Der endliche Polarframe `Q_T^E` zerfällt exakt als

   \[
   Q_T^E=W_T\mathcal R_T^E,
   \]

   wobei `W_T` der volle Terminal-Gauge und `mathcal R_T^E` ein **domain-side polar frame** des Operators `M_{R,T}^{1/2}|_E` ist.
4. Der Unterschied zwischen dem diagnostischen Cross-Frame-Winkel `Theta` und der tatsächlichen Kompression des vollen Cross-Terminal-Kerns wird exakt durch die Abweichung von `mathcal R_T^E` von der festen Einbettung `E hookrightarrow H_R` kontrolliert.
5. Diese Abweichung wird wiederum durch zwei **whitened Jet-Tail-Defekte** kontrolliert: einen äußeren Tail und einen internen Funktionalkalkül-/Kompressionsdefekt.
6. Für jedes feste Jetfenster `E_{R,N}` ist daher ein konkretes hinreichendes Cauchy-Kriterium formuliert. `N` bleibt dabei fest; kein universeller endlicher Jetcutoff wird eingeführt.

Nicht bewiesen wird weiterhin

\[
\boxed{
W_{R,S,-}^{[T]}
\longrightarrow
W_{R,S,-}^{[\infty]}
\quad\text{stark}.
}
\]

Der neue offene Kern ist nun noch schärfer typisiert:

\[
\boxed{
\text{P11-spezifische Abschätzungen für whitened domain tails und Cross-Frame-Orientierungen.}
}
\]

---

# 0. Methodische Verkettung

C6b erbt nichts implizit.

## 0.1 Aus C2

Für `R<S<T` ist

\[
W_T:=W_{R,S,-}^{[T]}
\]

isometrisch:

\[
W_T^\dagger W_T=I.
\tag{C1zB2C6b.1}
\]

Für jedes **feste** Terminal `T` gilt der exakte finite-horizon Kokyklus über Zwischenlevel.

C2 enthält jedoch keine Gleichung, die zwei verschiedene Terminal-Gauges `W_T` und `W_U` direkt miteinander identifiziert.

## 0.2 Aus C6

Im Boundary-Profilbild gilt

\[
\widetilde W_T
=
M_{S,T}^{1/2}\iota_{R,S}M_{R,T}^{-1/2},
\tag{C1zB2C6b.2}
\]

und der volle Cross-Terminal-Kern ist

\[
\widetilde{\mathscr K}_{T,U}
:=
\widetilde W_T^\dagger\widetilde W_U.
\tag{C1zB2C6b.3}
\]

## 0.3 Aus C6a

Für das kanonische Jetfenster

\[
E:=E_{R,N}
=\operatorname{span}\{e_{R,0},\ldots,e_{R,N}\}
\subset\mathscr A_R^-
\]

ist

\[
M(E)=N.
\]

Die endliche terminale Frameabbildung lautet

\[
\Phi_T^E
:=
M_{S,T}^{1/2}\iota_{R,S}|_E.
\tag{C1zB2C6b.4}
\]

Ihre Selbst-Gramform ist

\[
C_T^E
:=(\Phi_T^E)^\dagger\Phi_T^E
=
P_E M_{R,T}|_E
>0.
\tag{C1zB2C6b.5}
\]

Der normalisierte Polarframe ist

\[
\boxed{
Q_T^E
:=
\Phi_T^E(C_T^E)^{-1/2}.
}
\tag{C1zB2C6b.6}
\]

Damit

\[
(Q_T^E)^\dagger Q_T^E=I_E.
\tag{C1zB2C6b.7}
\]

C6a definierte

\[
\Theta_{T,U}^E
:=(Q_T^E)^\dagger Q_U^E.
\tag{C1zB2C6b.8}
\]

---

# 1. Reconciliation — `Theta` ist im Allgemeinen keine unitäre Matrix

Die Form

\[
(Q_T^E)^\dagger Q_U^E
\]

ist ein Produkt des Adjungierten einer Isometrie mit einer zweiten Isometrie.

Daraus folgt **nicht** Unitarität.

Vielmehr gilt unmittelbar

\[
\|\Theta_{T,U}^E\|
\le
\|Q_T^E\|\,\|Q_U^E\|
=1.
\]

Also

\[
\boxed{
\Theta_{T,U}^E
\text{ ist stets eine Kontraktion auf }E.
}
\tag{C1zB2C6b.9}
\]

## Minimales Gegenbeispiel

C6a selbst enthält bereits das entscheidende Modell.

Sei

\[
E=\mathbb C,
\qquad H=\mathbb C^2,
\]

und

\[
Q_T z=ze_1,
\qquad
Q_U z=z(\cos\theta\,e_1+\sin\theta\,e_2).
\]

Dann sind `Q_T,Q_U` Isometrien, aber

\[
\boxed{
Q_T^\dagger Q_U
=\cos\theta.
}
\tag{C1zB2C6b.10}
\]

Für `0<theta<pi/2` ist dies weder unitär noch isometrisch.

Status:

\[
\boxed{\checkmark[M]_{\rm corr,cross\text{-}frame\text{-}contraction}.}
\]

### Konsequenz für die Interpretation

Die Aussage

\[
\text{„C2 fixiert den Betrag; offen ist nur eine Phase“}
\]

ist zu stark.

Korrekt ist:

\[
\boxed{
\text{Zwischen zwei Terminalframes können sowohl Bildraumwinkel als auch interne Orientierung variieren.}
}
\tag{C1zB2C6b.11}
\]

Der Cross-Frame-Operator `Theta` enthält beide Effekte.

---

# 2. Principal-Angle-Defekte

Setze

\[
P_T^E:=Q_T^E(Q_T^E)^\dagger,
\qquad
P_U^E:=Q_U^E(Q_U^E)^\dagger.
\tag{C1zB2C6b.12}
\]

Dies sind die orthogonalen Projektionen auf die terminalen Frame-Bildräume

\[
\operatorname{Ran}Q_T^E,
\qquad
\operatorname{Ran}Q_U^E.
\]

Dann

\[
\begin{aligned}
I_E-(\Theta_{T,U}^E)^\dagger\Theta_{T,U}^E
&=
I_E-(Q_U^E)^\dagger Q_T^E(Q_T^E)^\dagger Q_U^E\\
&=
(Q_U^E)^\dagger(I-P_T^E)Q_U^E.
\end{aligned}
\]

Also

\[
\boxed{
I-(\Theta_{T,U}^E)^\dagger\Theta_{T,U}^E
=
(Q_U^E)^\dagger(I-P_T^E)Q_U^E
\ge0.
}
\tag{C1zB2C6b.13}
\]

Symmetrisch

\[
\boxed{
I-\Theta_{T,U}^E(\Theta_{T,U}^E)^\dagger
=
(Q_T^E)^\dagger(I-P_U^E)Q_T^E
\ge0.
}
\tag{C1zB2C6b.14}
\]

Damit ist exakt sichtbar, warum `Theta` im Allgemeinen nicht unitär ist: seine Unitaritätsdefekte sind die transversal zu den jeweils anderen Frame-Bildräumen liegenden Komponenten.

Auf endlichdimensionalem `E` sind die Singularwerte von `Theta` die Kosinuswerte der Principal-Angles zwischen

\[
\operatorname{Ran}Q_T^E
\quad\text{und}\quad
\operatorname{Ran}Q_U^E.
\]

Insbesondere

\[
|\Theta_{T,U}^E|
:=
\bigl((\Theta_{T,U}^E)^\dagger\Theta_{T,U}^E\bigr)^{1/2}
\]

kodiert den Bildraumwinkelanteil.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,principal\text{-}angle\text{-}defects}.}
\]

---

# 3. Bildraumwinkel und interne Frame-Orientierung sind getrennte Obstruktionen

Angenommen `Theta_{T,U}^E` ist invertierbar. Das ist insbesondere der Fall, sobald die größte Principal-Angle strikt kleiner als `pi/2` ist.

Dann besitzt `Theta` die Polarzerlegung

\[
\boxed{
\Theta_{T,U}^E
=
V_{T,U}^E
|\Theta_{T,U}^E|,
}
\tag{C1zB2C6b.15}
\]

mit einem unitären Operator `V_{T,U}^E` auf `E`.

Damit sind zwei unabhängige Grenzfragen sichtbar:

1. **Subspace defect**

   \[
   |\Theta_{T,U}^E|\to I;
   \]

2. **internal orientation defect**

   \[
   V_{T,U}^E\to I.
   \]

Nur zusammen ergeben sie

\[
\Theta_{T,U}^E\to I.
\]

### Gleichbleibender Bildraum reicht nicht

Selbst wenn

\[
P_T^E=P_U^E,
\]

kann

\[
Q_U^E=Q_T^E V
\]

mit einem nichttrivialen unitären `V` gelten. Dann

\[
\Theta_{T,U}^E=V.
\]

Also ist reine Principal-Angle-Konvergenz noch nicht hinreichend.

### Reine Phase reicht ebenfalls nicht als Beschreibung

Umgekehrt kann `Theta` strikt kontraktiv sein, wenn sich die Bildräume unterscheiden. Dann existiert überhaupt kein rein unitärer Phasenparameter, der die gesamte Abweichung beschreibt.

Daher lautet die korrekte geometrische Sprache:

\[
\boxed{
\Theta
\text{ misst Principal-Angles plus interne Frame-Orientierung.}
}
\tag{C1zB2C6b.16}
\]

---

# 4. Exakte Cauchy-Identität für die endlichen Polarframes

Da `Q_T^E` und `Q_U^E` Isometrien sind,

\[
\begin{aligned}
(Q_T^E-Q_U^E)^\dagger(Q_T^E-Q_U^E)
&=
2I_E
-(Q_T^E)^\dagger Q_U^E
-(Q_U^E)^\dagger Q_T^E\\
&=
2I_E-\Theta_{T,U}^E-(\Theta_{T,U}^E)^\dagger.
\end{aligned}
\]

Also

\[
\boxed{
\|Q_T^E-Q_U^E\|^2
=
\|2I_E-\Theta_{T,U}^E-(\Theta_{T,U}^E)^\dagger\|.
}
\tag{C1zB2C6b.17}
\]

Daher sind auf festem endlichdimensionalem `E` äquivalent:

\[
Q_T^E-Q_U^E\to0,
\]

und

\[
\operatorname{Re}\Theta_{T,U}^E\to I_E
\quad\text{in Operatornorm}.
\]

Außerdem gilt wegen `||Theta||<=1` für jeden Einheitsvektor `x`:

\[
\begin{aligned}
\|(\Theta-I)x\|^2
&=
\|\Theta x\|^2+1-2\operatorname{Re}\langle\Theta x,x\rangle\\
&\le
2\bigl(1-\operatorname{Re}\langle\Theta x,x\rangle\bigr).
\end{aligned}
\]

Somit

\[
\boxed{
\|\Theta_{T,U}^E-I\|^2
\le
2\|I-\operatorname{Re}\Theta_{T,U}^E\|.
}
\tag{C1zB2C6b.18}
\]

Also ist auf endlichdimensionalen Fenstern sogar

\[
\boxed{
Q_T^E\text{ Cauchy}
\iff
\Theta_{T,U}^E\to I.
}
\tag{C1zB2C6b.19}
\]

für `T,U->infty`.

**Firewall:** Dies betrifft die endlichen Polarframes `Q_T^E`, noch nicht automatisch die Restriktion des vollen Terminal-Gauges `W_T|_E`. C6a hat genau vor dieser Verwechslung gewarnt.

---

# 5. Domain-side Polarframe — die fehlende Brücke zum vollen Gauge

Nun wird die C6a-Kompressionsfirewall exakt aufgelöst.

Sei

\[
i_E:E\hookrightarrow\mathscr A_R^-
\]

die feste isometrische Einbettung des Jetfensters in den `R`-Profilhilbertraum.

Definiere

\[
A_T^E
:=
M_{R,T}^{1/2}i_E
:
E\to\mathscr A_R^-.
\tag{C1zB2C6b.20}
\]

Dann

\[
(A_T^E)^\dagger A_T^E
=
P_E M_{R,T}|_E
=C_T^E.
\tag{C1zB2C6b.21}
\]

Der domain-side Polarframe ist daher

\[
\boxed{
\mathcal R_T^E
:=
A_T^E(C_T^E)^{-1/2}
=
M_{R,T}^{1/2}i_E(C_T^E)^{-1/2}.
}
\tag{C1zB2C6b.22}
\]

Er ist eine Isometrie:

\[
(\mathcal R_T^E)^\dagger\mathcal R_T^E=I_E.
\tag{C1zB2C6b.23}
\]

Nun benutzt man die exakte Gaugeformel

\[
\widetilde W_T
=
M_{S,T}^{1/2}\iota_{R,S}M_{R,T}^{-1/2}.
\]

Daraus folgt

\[
\widetilde W_T M_{R,T}^{1/2}i_E
=
M_{S,T}^{1/2}\iota_{R,S}i_E
=
\Phi_T^E.
\]

Nach Multiplikation mit `(C_T^E)^-1/2` erhält man

\[
\boxed{
Q_T^E
=
\widetilde W_T\mathcal R_T^E.
}
\tag{C1zB2C6b.24}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm pos,domain\text{-}polar\text{-}factorization}.}
\]

Dies ist die exakte fehlende Brücke zwischen dem endlichen diagnostischen Polarframe und dem vollen Terminal-Gauge.

---

# 6. Der diagnostische Winkel ist ein bewegter Cross-Terminal-Kern

Setze

\[
\mathscr K_{T,U}
:=
\widetilde W_T^\dagger\widetilde W_U
:
\mathscr A_R^-\to\mathscr A_R^-.
\tag{C1zB2C6b.25}
\]

Aus (C1zB2C6b.24) folgt exakt

\[
\boxed{
\Theta_{T,U}^E
=
(\mathcal R_T^E)^\dagger
\mathscr K_{T,U}
\mathcal R_U^E.
}
\tag{C1zB2C6b.26}
\]

Der in C6a untersuchte Cross-Frame-Winkel ist also **nicht** die feste Kompression

\[
i_E^\dagger\mathscr K_{T,U}i_E,
\]

sondern die Kompression des vollen Cross-Terminal-Kerns auf zwei terminalabhängig bewegte domain-side Polarframes.

Das ist die präzise Form der C6a-Kompressionsfirewall.

---

# 7. Domain-frame defect und Vergleich mit der festen Kompression

Definiere den dimensionslosen domain-frame defect

\[
\boxed{
\delta_T(E)
:=
\|\mathcal R_T^E-i_E\|.
}
\tag{C1zB2C6b.27}
\]

Da sowohl `widetilde W_T` als auch `widetilde W_U` Isometrien sind, gilt

\[
\|\mathscr K_{T,U}\|
\le1.
\tag{C1zB2C6b.28}
\]

Definiere die feste Fensterkompression des vollen Cross-Kerns

\[
\boxed{
\Omega_{T,U}^E
:=
i_E^\dagger\mathscr K_{T,U}i_E.
}
\tag{C1zB2C6b.29}
\]

Dann

\[
\begin{aligned}
\Theta_{T,U}^E-\Omega_{T,U}^E
={}&
(\mathcal R_T^E-i_E)^\dagger
\mathscr K_{T,U}\mathcal R_U^E\\
&+
i_E^\dagger\mathscr K_{T,U}
(\mathcal R_U^E-i_E).
\end{aligned}
\]

Somit

\[
\boxed{
\|\Theta_{T,U}^E-\Omega_{T,U}^E\|
\le
\delta_T(E)+\delta_U(E).
}
\tag{C1zB2C6b.30}
\]

Das ist die zentrale quantitative Brücke von C6b.

Insbesondere:

Wenn

\[
\delta_T(E)\to0
\]

und

\[
\Theta_{T,U}^E\to I_E,
\]

so folgt

\[
\boxed{
\Omega_{T,U}^E\to I_E.
}
\tag{C1zB2C6b.31}
\]

---

# 8. Exakter Cauchytest für die Restriktion des vollen Terminal-Gauges

Da

\[
\widetilde W_T i_E,
\qquad
\widetilde W_U i_E
\]

Isometrien von `E` nach `mathscr A_S^-` sind,

\[
\begin{aligned}
(\widetilde W_Ti_E-\widetilde W_Ui_E)^\dagger
(\widetilde W_Ti_E-\widetilde W_Ui_E)
=
2I_E-\Omega_{T,U}^E-(\Omega_{T,U}^E)^\dagger.
\end{aligned}
\]

Daher

\[
\boxed{
\|\widetilde W_T|_E-\widetilde W_U|_E\|^2
=
\|2I_E-\Omega_{T,U}^E-(\Omega_{T,U}^E)^\dagger\|.
}
\tag{C1zB2C6b.32}
\]

Kombiniert mit (C1zB2C6b.30) ergibt sich ein direktes hinreichendes Kriterium.

## Satz C1zB2C6b.1 — finite-window Zwei-Defekt-Cauchykriterium

Fixiere `R<S` und ein kanonisches Jetfenster

\[
E=E_{R,N}.
\]

Angenommen

\[
\boxed{
\delta_T(E)\to0
\qquad(T\to\infty)
}
\tag{C1zB2C6b.33}
\]

und

\[
\boxed{
\Theta_{T,U}^E\to I_E
\qquad(T,U\to\infty)
}
\tag{C1zB2C6b.34}
\]

in Operatornorm.

Dann ist

\[
\boxed{
\widetilde W_T|_E
\text{ Cauchy in Operatornorm}.
}
\tag{C1zB2C6b.35}
\]

### Beweis

Aus (C1zB2C6b.30):

\[
\|\Omega_{T,U}^E-I\|
\le
\|\Theta_{T,U}^E-I\|
+
\delta_T(E)+\delta_U(E)
\to0.
\]

Dann folgt (C1zB2C6b.35) aus (C1zB2C6b.32). `□`

Status:

\[
\boxed{\checkmark[M]_{\rm pos,finite\text{-}window\text{-}Cauchy\text{-}reduction}.}
\]

### Interpretation

Der endliche Odd-Cauchytest zerfällt in zwei Aufgaben:

1. **target cross-frame alignment:** `Theta -> I`;
2. **domain polar stabilization:** `delta_T(E) -> 0`.

C6a hatte beide Effekte noch unter dem Wort „Tailkontrolle“ zusammengefasst. C6b trennt sie exakt.

---

# 9. Whitened Jet-Tails — dimensionslose Kontrolle von `delta_T(E)`

Die rohe Größe

\[
Q_E M_{R,T}^{1/2}P_E
\]

ist wegen der absoluten Odd-Divergenz nicht sinnvollerweise ohne Normalisierung klein zu erwarten.

Die natürliche Normalisierung ist bereits durch die Selbst-Gramform

\[
C_T^E=P_E M_{R,T}|_E
\]

gegeben.

Schreibe

\[
P:=P_E,
\qquad Q:=I-P,
\qquad C_T:=C_T^E.
\]

Aus

\[
\mathcal R_T^E
=M_{R,T}^{1/2}i_EC_T^{-1/2}
\]

folgt die orthogonale Zerlegung

\[
\mathcal R_T^E-i_E
=
Q M_{R,T}^{1/2}i_EC_T^{-1/2}
+
\left(
P M_{R,T}^{1/2}i_EC_T^{-1/2}-i_E
\right).
\]

Definiere

\[
\boxed{
\tau_T(E)
:=
\|Q M_{R,T}^{1/2}i_EC_T^{-1/2}\|,
}
\tag{C1zB2C6b.36}
\]

und

\[
\boxed{
\kappa_T(E)
:=
\|P M_{R,T}^{1/2}i_EC_T^{-1/2}-i_E\|.
}
\tag{C1zB2C6b.37}
\]

Dann unmittelbar

\[
\boxed{
\delta_T(E)
\le
\tau_T(E)+\kappa_T(E).
}
\tag{C1zB2C6b.38}
\]

Die Größe `tau_T(E)` ist der **äußere whitened Jet-Tail**: Wie viel des polar normalisierten `M^{1/2}`-Bildes verlässt das feste Jetfenster?

Die Größe `kappa_T(E)` ist der **interne Funktionalkalkül-/Kompressionsdefekt**: Selbst innerhalb des Fensters muss

\[
P M^{1/2}P
\]

nicht mit

\[
(PMP)^{1/2}
\]

übereinstimmen.

C6a hat genau diese Nichtvertauschung durch ein `2x2`-Gegenmodell gesichert.

## Korollar C1zB2C6b.2

Wenn für festes `E=E_{R,N}`

\[
\boxed{
\tau_T(E)\to0,
\qquad
\kappa_T(E)\to0,
}
\tag{C1zB2C6b.39}
\]

so folgt

\[
\boxed{
\delta_T(E)\to0.
}
\tag{C1zB2C6b.40}
\]

Zusammen mit

\[
\Theta_{T,U}^E\to I
\]

liefert Satz C1zB2C6b.1 die Cauchy-Konvergenz des **vollen** Terminal-Gauges auf `E`.

Status:

\[
\boxed{\checkmark[M]_{\rm pos,whitened\text{-}tail\text{-}criterion}.}
\]

---

# 10. Warum die Normalisierung wesentlich ist

C6a beweist für jeden nichtzero ungeraden Vektor

\[
h_T(F,F)\to\infty.
\]

Daher divergiert auf jedem festen endlichen Jetfenster jede nichtzero quadratische Richtung der Selbst-Gramfamilie.

Das bedeutet gerade nicht, dass ein roher Off-Diagonalblock wie

\[
Q M_{R,T}^{1/2}P
\]

absolut gegen null gehen sollte.

Entscheidend ist seine Größe **relativ zur im Fenster selbst divergierenden Metrik**. Genau dies leistet der Faktor

\[
C_T^{-1/2}.
\]

Die korrekte asymptotische Frage lautet daher

\[
\boxed{
Q M_{R,T}^{1/2}P
(PM_{R,T}P)^{-1/2}
\to0\ ?
}
\tag{C1zB2C6b.41}
\]

und nicht

\[
Q M_{R,T}^{1/2}P\to0.
\]

Dies ist ein wichtiger Scope-Schutz gegen eine mit der totalen Odd-Divergenz unvereinbare absolute Tailforderung.

---

# 11. `Theta -> I` ist stärker als reine Principal-Angle-Kollapsierung

Aus (C1zB2C6b.13) folgt:

Wenn

\[
\Theta_{T,U}^E\to I,
\]

dann

\[
I-(\Theta_{T,U}^E)^\dagger\Theta_{T,U}^E\to0.
\]

Also kollabieren alle Principal-Angles gegen null.

Die Umkehrung gilt ohne zusätzliche Orientierungskontrolle nicht.

Denn

\[
|\Theta_{T,U}^E|\to I
\]

lässt einen nichttrivialen unitären Polaroperator `V_{T,U}^E` offen.

Damit zerfällt der target-side Nachweis logisch in

\[
\boxed{
|\Theta_{T,U}^E|\to I
\quad\text{und}\quad
V_{T,U}^E\to I.
}
\tag{C1zB2C6b.42}
\]

sobald `Theta` für große Terminale invertierbar ist.

Alternativ genügt direkt

\[
\operatorname{Re}\Theta_{T,U}^E\to I,
\]

weil (C1zB2C6b.18) dann `Theta->I` erzwingt.

Für praktische Schätzungen kann die Realteilform günstiger sein, da sie unmittelbar in die Cauchy-Identität (C1zB2C6b.17) eingeht.

---

# 12. C2-Flachheit ist keine Cross-Terminal-Konvergenzaussage

C2 beweist für jedes feste Terminal `T` eine exakte kohärente Isometrisierung über die Source-Level.

Das ist eine Aussage in der **horizontalen** Richtung

\[
R<S<U\le T.
\]

C6b untersucht dagegen die **terminale** Richtung

\[
T,U\to\infty
\]

bei festem `R<S`.

Diese beiden Richtungen dürfen nicht identifiziert werden.

## Abstraktes Metric-Cocycle-Gegenmodell

Wir zeigen, dass die formalen C2-Identitäten allein keinen terminalen Grenzwert erzwingen.

Sei jeder Levelraum

\[
H_t=\mathbb C^2.
\]

Wähle für jeden Level einen invertierbaren Operator `A_t` und definiere

\[
J_{r,s}:=A_sA_r^{-1}.
\]

Dann gilt automatisch

\[
J_{s,t}J_{r,s}=J_{r,t}.
\]

Die Zukunftsmetriken

\[
G_{r,t}=J_{r,t}^\dagger J_{r,t}
\]

besitzen den exakten Pullback-Kokyklus von C2.

Schreibe die Polarzerlegung

\[
J_{r,t}=U_{r,t}|J_{r,t}|.
\]

Eine direkte Rechnung liefert für die C2-Terminalgauge

\[
\boxed{
W_{r,s}^{[t]}
=U_{s,t}^\dagger U_{r,t}.
}
\tag{C1zB2C6b.43}
\]

Nun fixiere

\[
A_r=I,
\qquad
A_s=D:=\begin{pmatrix}2&0\\0&1\end{pmatrix}.
\]

Wähle eine Folge terminaler `A_t`, die zwischen

\[
D
\]

und einer positiv definiten Matrix

\[
P=R_\alpha D R_\alpha^\dagger
\]

mit `0<alpha<pi/2` alterniert.

Für `A_t=D` ist

\[
J_{s,t}=I,
\qquad
U_{s,t}=I,
\qquad
U_{r,t}=I,
\]

also

\[
W_{r,s}^{[t]}=I.
\]

Für `A_t=P` ist

\[
J_{r,t}=P
\]

positiv, also `U_{r,t}=I`, während

\[
J_{s,t}=PD^{-1}
\]

wegen `PD^{-1}\ne D^{-1}P` nicht selbstadjungiert positiv ist. Sein Polarunitär `U_{s,t}` ist daher nicht `I`.

Also

\[
W_{r,s}^{[t]}
=U_{s,t}^\dagger
\ne I.
\]

Durch Alternieren der beiden Terminaltypen entsteht eine nichtkonvergente Terminal-Gauge-Folge, obwohl an jedem einzelnen Terminal der vollständige C2-Kokyklus exakt gilt.

Damit ist bewiesen:

\[
\boxed{
\text{finite-horizon C2-Flachheit allein erzwingt keine Cross-Terminal-Konvergenz.}
}
\tag{C1zB2C6b.44}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm neg,C2\text{-}flatness\text{-}alone}.}
\]

### Scope-Firewall

Dieses Gegenmodell ist ein **abstraktes Modell der C2-Metrikkokyklusaxiome**. Es behauptet nicht, dass die konkrete P11-Nullfortsetzungs-/Feshbachgeometrie solche beliebigen terminalen Oszillationen realisiert.

Seine Aussage ist ausschließlich methodisch:

\[
\boxed{
\text{Ein positiver C6c-Satz muss zusätzliche P11-spezifische Struktur verwenden.}
}
\tag{C1zB2C6b.45}
\]

Ein Beweis nur aus „jedes `W_T` ist isometrisch“ und „für jedes `T` gilt der Kokyklus“ kann nicht genügen.

---

# 13. Kombination mit dem Dense-Core-Lifting aus C6a

Für jedes feste `N` setze

\[
E_N:=E_{R,N}.
\]

Angenommen, für jedes feste `N` gelten

\[
\tau_T(E_N)\to0,
\qquad
\kappa_T(E_N)\to0,
\tag{C1zB2C6b.46}
\]

und

\[
\Theta_{T,U}^{E_N}\to I_{E_N}
\qquad(T,U\to\infty).
\tag{C1zB2C6b.47}
\]

Dann liefert C6b zunächst Cauchy-Konvergenz von `W_T` auf jedem einzelnen `E_N`.

C6a liefert anschließend, weil

\[
\overline{\bigcup_N E_N}=\mathcal K_{X,R}^-
\]

und

\[
\|W_T\|=1,
\]

die starke Konvergenz auf dem gesamten ungeraden Hilbertraum.

Damit erhalten wir das folgende **bedingte Gesamt-Kriterium**.

## Satz C1zB2C6b.2 — bedingtes Odd-Gauge-Grenzkriterium

Wenn für jedes feste `N` die drei dimensionslosen Bedingungen

\[
\boxed{
\tau_T(E_{R,N})\to0,
}
\tag{C1zB2C6b.48}
\]

\[
\boxed{
\kappa_T(E_{R,N})\to0,
}
\tag{C1zB2C6b.49}
\]

und

\[
\boxed{
\Theta_{T,U}^{E_{R,N}}\to I
}
\tag{C1zB2C6b.50}
\]

gelten, dann existiert eine Isometrie

\[
W_{R,S,-}^{[\infty]}:
\mathcal K_{X,R}^-\to\mathcal K_{X,S}^-
\]

mit

\[
\boxed{
W_{R,S,-}^{[T]}
\xrightarrow[T\to\infty]{\rm strong}
W_{R,S,-}^{[\infty]}.
}
\tag{C1zB2C6b.51}
\]

**Status:** `✓[M]_{conditional}` — dies ist ein exaktes hinreichendes Kriterium, kein Nachweis seiner Hypothesen.

### Zentrale Firewall

Für jedes `N` wird zuerst

\[
T,U\to\infty
\]

untersucht.

Erst über das Dense-Core-Lifting wird anschließend der ganze Hilbertraum erreicht.

Es wird nirgends ein universelles endliches `N` oder `M(E)` verlangt.

---

# 14. Was C4 derzeit zu den neuen Defekten beiträgt

C4 liefert eine vollständige asymptotische Entwicklung der speziellen Boundary-Hubkopplung und daraus scharfe **Untergrenzen** nach dem ersten aktiven Jet.

Diese Informationen beweisen die totale Odd-Divergenz.

Sie liefern aber derzeit keine ausreichende obere oder Off-Diagonal-Kontrolle für

\[
\tau_T(E),
\qquad
\kappa_T(E),
\qquad
\Theta_{T,U}^E.
\]

Insbesondere folgt aus

\[
h_T(e_{R,m},e_{R,m})
\gtrsim
\frac{e^T}{T^{2m+3}}
\]

nicht, dass

\[
Q_E M_{R,T}^{1/2}P_E(P_EM_{R,T}P_E)^{-1/2}
\to0.
\]

Dafür müsste die **volle** Feshbach-/Profilmetrik relativ zur Jetflagge kontrolliert werden, nicht nur eine Variationsuntergrenze entlang der Konstantenmode.

Diese Firewall bleibt verbindlich.

---

# 15. No-Go-Persistenzmatrix

| Früherer Knoten | Gesiegelter Befund | Wirkung in C6b |
|---|---|---|
| C1y | translationsinvariante Operatorregulatoren lösen den Hub/Rest-Konflikt im C1y-Scope nicht | unverändert |
| B2-A | kein Schattenklassenabschluss durch Gamma-Präkonditionierung | unverändert |
| B2-B | naiver Haar-`L^2`-Grenzendpunkt reicht nicht | unverändert |
| C4 | unendliche Jet-Hierarchie; kein fixer endlicher Trunkat stabilisiert die rohe Metrik | unverändert; `N` bleibt fensterabhängig |
| C5/C6a | totale Odd-Divergenz | unverändert; motiviert gerade die **whitened** statt absolute Tailnorm |
| C6 | keine vollständige Faktorisierung durch festen endlichen Jetquotienten | unverändert |
| C6a | Selbst-Grams/Cholesky allein bestimmen Cross-Winkel nicht | unverändert; `Theta` bleibt eigene Hypothese |
| C6a | Kompression und Funktionalkalkül vertauschen nicht | präzisiert durch `delta`, `tau`, `kappa` |
| C2 | finite-horizon Terminal-Gauge ist exakt isometrisch/kohärent | bleibt; C6b zeigt zusätzlich, dass dies allein keine Terminalkonvergenz erzwingt |
| C5e | gerader Gamma-Gauge konvergiert stark | nur Vergleich; kein Import in den Odd-Kanal |

---

# 16. Was C6b supersediert — und was nicht

C6b supersediert ausschließlich die zu starke Interpretation

\[
\text{„Theta ist unitär; offen ist nur die Phase.“}
\]

Korrekt ist

\[
\boxed{
\Theta\text{ ist eine Kontraktion und enthält Bildraumwinkel plus interne Orientierung.}
}
\tag{C1zB2C6b.52}
\]

Nicht supersediert werden:

- die C6a-Definition von `Theta`;
- der Gram-angle No-Go;
- die Kompressionsfirewall;
- der Finite-Jet-No-Go;
- die totale Odd-Divergenz;
- die offene starke Terminal-Gauge-Konvergenz.

C6b ersetzt also keine gesiegelte positive Aussage, sondern korrigiert nur eine Interpretation und schärft den offenen Cauchytest.

---

# 17. Exakter nächster Arbeitsauftrag C6c

C6b zeigt, dass ein sinnvoller nächster Knoten nicht mehr allgemein nach „Tailkontrolle“ fragen sollte.

Er soll die drei dimensionslosen Größen auf einem festen kanonischen Jetfenster untersuchen:

\[
\boxed{
\tau_T(E_{R,N})
=
\|Q_{R,N}M_{R,T}^{1/2}i_{R,N}
(P_{R,N}M_{R,T}P_{R,N})^{-1/2}\|,
}
\tag{C1zB2C6b.53}
\]

\[
\boxed{
\kappa_T(E_{R,N})
=
\|P_{R,N}M_{R,T}^{1/2}i_{R,N}
(P_{R,N}M_{R,T}P_{R,N})^{-1/2}-i_{R,N}\|,
}
\tag{C1zB2C6b.54}
\]

und

\[
\boxed{
\Theta_{T,U}^{E_{R,N}}
=(Q_T^{E_{R,N}})^\dagger Q_U^{E_{R,N}}.
}
\tag{C1zB2C6b.55}
\]

Die erste konkrete Frage sollte sein:

\[
\boxed{
\text{Erzwingt die trianguläre Jetstruktur von }\iota_{R,T}
\text{ irgendeine quantitative Kontrolle von }\tau_T(E_{R,N})\text{ oder }\kappa_T(E_{R,N})?
}
\tag{C1zB2C6b.56}
\]

Falls nein, ist der nächste notwendige Input nicht mehr rein algebraisch, sondern eine neue **relative Feshbach-/Boundary-Asymptotik** für die Off-Diagonalblöcke der terminalen Metrik in der kanonischen Jet-ONB.

Für `Theta` sollte parallel geprüft werden, ob die konkrete positivity/polar structure des P11-Frames eine Orientierungskontrolle liefert, die im abstrakten C2-Gegenmodell fehlt.

**Firewall für C6c:** Kein Schluss aus Triangularität allein. Eine positive Tailaussage muss quantitative `T`-abhängige Schätzungen enthalten.

---

# 18. Endurteil

\[
\boxed{
[P11\text{-}C1z\text{-}B2\text{-}C6b]
\quad
\checkmark[K/M]_{\rm part}
+
\checkmark[M]_{\rm corr,cross\text{-}frame\text{-}contraction}
+
\checkmark[M]_{\rm pos,principal\text{-}angle\text{-}defects}
+
\checkmark[M]_{\rm pos,domain\text{-}polar\text{-}factorization}
+
\checkmark[M]_{\rm pos,whitened\text{-}tail\text{-}criterion}
+
\checkmark[M]_{\rm pos,finite\text{-}window\text{-}Cauchy\text{-}reduction}
+
\checkmark[M]_{\rm neg,C2\text{-}flatness\text{-}alone}
}
\]

C6b entscheidet den Odd-Grenzwert noch nicht. Der Fortschritt besteht darin, dass der verbleibende Grenzmechanismus jetzt in **drei dimensionslosen, fensterweisen Größen** zerlegt ist:

\[
\boxed{
(\tau_T,\kappa_T,\Theta_{T,U}).
}
\]

Damit ist erstmals präzise getrennt,

- was die divergente Selbstmetrik nur skaliert,
- was als domain-side Jet-Tail aus dem festen Fenster herausläuft,
- was aus Nichtvertauschung von Kompression und Quadratwurzel stammt,
- und was als echter Cross-Terminal-Principal-Angle/Orientierungsdefekt übrig bleibt.

Der nächste mathematische Durchbruch im ungeraden Kanal wäre ein P11-spezifischer Nachweis, dass diese Defekte auf jedem festen `E_{R,N}` verschwinden — oder ein Gegenbeispiel, dass mindestens einer davon persistiert.
