# P11-O3 — Symmetrisierter Jensen-Kontraktor, gewichteter Cross-Gram und Konditions-Firewall

**Datum:** 2026-08-11  
**Programm:** P11 — `Global Coupling and the Object-X Candidate Geometry`  
**Knoten:** `[P11-O3]`  
**Vorgänger:** P11-O2 (`80a49495`), nach destruktivem Gegencheck `PASS` und GPT-Reconciliation  
**Modus:** `PASS-A ACTIVE`  
**Scope:** direkter Klasse-O-Audit des Modulus-Isometriewinkels; keine Residualroute, kein R3, kein SYN, kein Seal, kein `papers/P11`, kein automatischer O4.

---

# 0. Auditstatus und Kernurteil

O2 reduzierte den direkten Terminaldefekt auf zwei Isometriewinkel:

\[
\boxed{
W_U-W_T
=
\mathcal U_S(Q-W_T)\mathcal U_R^*
+
\mathscr P,
}
\tag{P11O3.1}
\]

wobei

\[
Q=A_S^{1/2}W_TA_R^{-1/2}
\]

selbst eine Isometrie ist.

O3 untersucht ausschließlich den ersten Winkel

\[
Q-W_T.
\]

Der neue Befund lautet:

Der Cross-Gram

\[
\mathscr C_{R,S}^{T,U}
:=W_T^*Q
\]

ist im nativen Source-Skalarprodukt im Allgemeinen nicht selbstadjungiert, aber er ist **ähnlich zu einem positiven Kontraktor**. Der Modulusblock besitzt daher keine unabhängige spektrale Phase. Seine endliche Nichttrivialität wird von einem dimensionslosen positiven Jensen-Kontraktionsdefekt getragen.

Definiere

\[
D:=W_T^*A_S^{1/2}W_T,
\qquad
\mathscr J:=A_R^{1/2}-D\ge0,
\]

und den symmetrisch normalisierten Jensen-Defekt

\[
\boxed{
\Theta_{R,S}^{T,U}
:=
A_R^{-1/4}\mathscr J A_R^{-1/4}.
}
\tag{P11O3.2}
\]

Dann gilt exakt

\[
\boxed{
0\le \Theta_{R,S}^{T,U}\le I.
}
\tag{P11O3.3}
\]

Außerdem ist

\[
\boxed{
B_{R,S}^{T,U}
:=I-\Theta_{R,S}^{T,U}
=A_R^{-1/4}DA_R^{-1/4}
}
\tag{P11O3.4}
\]

selbstadjungiert und ein positiver Kontraktor:

\[
\boxed{0\le B_{R,S}^{T,U}\le I.}
\tag{P11O3.5}
\]

Der native Cross-Gram ist hierzu ähnlich:

\[
\boxed{
\mathscr C_{R,S}^{T,U}
=A_R^{1/4}
B_{R,S}^{T,U}
A_R^{-1/4}.
}
\tag{P11O3.6}
\]

Daher

\[
\boxed{
\sigma(\mathscr C_{R,S}^{T,U})
\subseteq[0,1].
}
\tag{P11O3.7}
\]

Der Modulus-Cross-Gram trägt also keine nichttriviale Spektralphase. Seine mögliche Nichtnormalität entsteht ausschließlich aus der beweglichen Ähnlichkeit durch `A_R^{\pm1/4}`.

Im natürlichen gewichteten Source-Skalarprodukt mit Gewicht

\[
M_R^{T,U}:=A_R^{-1/2}
\]

ist `mathscr C` sogar selbstadjungiert und positiv kontraktiv.

Beim Rücktransport in die native Norm erscheint jedoch ein neuer asymptotischer Firewall-Faktor:

\[
\boxed{
\chi_R^{T,U}
:=
\|A_R^{1/4}\|\,
\|A_R^{-1/4}\|.
}
\tag{P11O3.8}
\]

O3 beweist den hinreichenden Normtransfer

\[
\boxed{
\|Q-W_T\|^2
\le
2\chi_R^{T,U}\,
\|\Theta_{R,S}^{T,U}\|.
}
\tag{P11O3.9}
\]

Damit ist

\[
\boxed{
\chi_R^{T,U}\|\Theta_{R,S}^{T,U}\|\to0
\Longrightarrow
\|Q-W_T\|\to0
}
\tag{P11O3.10}
\]

hinreichend.

**Aber:** Weder

\[
\Theta_{R,S}^{T,U}\to0
\]

noch eine uniforme Kontrolle von `chi_R^{T,U}` ist bewiesen. O3 schließt daher den Moduluswinkel nicht asymptotisch.

Auditstatus:

\[
\boxed{
\begin{aligned}
[P11\text{-}O3]
&\quad \checkmark[K/M]_{\rm part}\\
&+\checkmark[M]_{\rm pos,symmetric\text{-}Jensen\text{-}contraction}\\
&+\checkmark[M]_{\rm pos,cross\text{-}Gram\text{-}similarity}\\
&+\checkmark[M]_{\rm pos,weighted\text{-}selfadjointness}\\
&+\checkmark[M]_{\rm pos,spectrum\text{-}in\text{-}[0,1]}\\
&+\checkmark[M]_{\rm pos,normalized\text{-}leakage\text{-}decomposition}\\
&+\checkmark[M]_{\rm pos,conditioning\text{-}transfer\text{-}bound}\\
&+\checkmark[M]_{\rm corr,no\text{-}native\text{-}phase\text{-}elimination\text{-}without\text{-}conditioning}\\
&+?[O]_{\Theta\;\rm asymptotic}\\
&+?[O]_{\chi_R\;\rm control}\\
&+?[O]_{Q-W_T\;\rm asymptotic}\\
&+?[O]_{\rm polar\text{-}phase\text{-}alignment}\\
&+?[O]_{W_{R,S,-}^{[T]}\;\rm strong\;limit}.
\end{aligned}
}
\]

---

# 1. Verbindliche Daten aus O2

Fixiere

\[
0<R<S<T<U.
\]

Wir schreiben abkürzend

\[
W:=W_{R,S}^{[T]},
\qquad
A_R:=A_R^{T,U},
\qquad
A_S:=A_S^{T,U},
\qquad
Q:=Q_{R,S}^{T,U}.
\]

O1/O2 liefern:

\[
\boxed{W^*A_SW=A_R,}
\tag{P11O3.11}
\]

\[
\boxed{
Q=A_S^{1/2}WA_R^{-1/2},
}
\tag{P11O3.12}
\]

\[
\boxed{W^*W=Q^*Q=I.}
\tag{P11O3.13}
\]

Ferner

\[
D:=W^*A_S^{1/2}W
\tag{P11O3.14}
\]

und

\[
\boxed{
\mathscr J:=A_R^{1/2}-D\ge0.
}
\tag{P11O3.15}
\]

Die Jensen-Ungleichung aus O1 ist also exakt

\[
\boxed{
0\le D\le A_R^{1/2}.
}
\tag{P11O3.16}
\]

O2 identifizierte den Cross-Gram

\[
\boxed{
W^*Q
=DA_R^{-1/2}
=I-\mathscr J A_R^{-1/2}.
}
\tag{P11O3.17}
\]

und den Winkeloperator

\[
\boxed{
(Q-W)^*(Q-W)
=A_R^{-1/2}\mathscr J
+\mathscr J A_R^{-1/2}.
}
\tag{P11O3.18}
\]

---

# 2. Satz O3.1 — symmetrisch normalisierter Jensen-Kontraktor

Definiere

\[
\boxed{
B:=A_R^{-1/4}DA_R^{-1/4}.
}
\tag{P11O3.19}
\]

Aus `D>=0` folgt durch Kongruenz

\[
B\ge0.
\]

Aus

\[
D\le A_R^{1/2}
\]

folgt ebenfalls durch Kongruenz mit `A_R^{-1/4}`:

\[
B
\le
A_R^{-1/4}A_R^{1/2}A_R^{-1/4}
=I.
\]

Also

\[
\boxed{0\le B\le I.}
\tag{P11O3.20}
\]

Definiere nun

\[
\boxed{
\Theta:=I-B.
}
\tag{P11O3.21}
\]

Dann

\[
\boxed{0\le\Theta\le I.}
\tag{P11O3.22}
\]

Aus `D=A_R^{1/2}-mathscr J`:

\[
\begin{aligned}
B
&=A_R^{-1/4}
(A_R^{1/2}-\mathscr J)
A_R^{-1/4}\\
&=I-A_R^{-1/4}\mathscr J A_R^{-1/4}.
\end{aligned}
\]

Daher

\[
\boxed{
\Theta
=A_R^{-1/4}\mathscr J A_R^{-1/4}.
}
\tag{P11O3.23}
\]

Status:

\[
\boxed{\checkmark[M].}
\]

### Bedeutung

`mathscr J` ist positiv, aber dimensions- beziehungsweise gaugeabhängig. `Theta` ist seine symmetrische relative Normalisierung und erfüllt unabhängig von der Größe von `A_R` die endliche Schranke

\[
0\le\Theta\le I.
\]

Damit besitzt der O2-Jensenwinkel eine kanonische dimensionslose positive Repräsentation.

**Firewall:** Aus `0<=Theta<=I` folgt keinerlei asymptotische Kleinheit.

---

# 3. Satz O3.2 — Cross-Gram ist ähnlich zu einem positiven Kontraktor

Definiere

\[
\boxed{
\mathscr C:=W^*Q.
}
\tag{P11O3.24}
\]

Aus O2:

\[
\mathscr C=DA_R^{-1/2}.
\]

Setze `D=A_R^{1/4}BA_R^{1/4}` aus (P11O3.19). Dann

\[
\begin{aligned}
\mathscr C
&=A_R^{1/4}BA_R^{1/4}A_R^{-1/2}\\
&=A_R^{1/4}BA_R^{-1/4}.
\end{aligned}
\]

Also

\[
\boxed{
\mathscr C
=A_R^{1/4}BA_R^{-1/4}.
}
\tag{P11O3.25}
\]

Da `A_R^{1/4}` beschränkt invertierbar ist, sind `mathscr C` und `B` ähnlich.

Daher haben beide dasselbe Spektrum:

\[
\sigma(\mathscr C)=\sigma(B).
\]

Wegen

\[
0\le B\le I
\]

gilt

\[
\boxed{
\sigma(\mathscr C)\subseteq[0,1].
}
\tag{P11O3.26}
\]

Status:

\[
\boxed{\checkmark[M].}
\]

### Konsequenz

Der Cross-Gram zweier Isometrien kann abstrakt stark nichtnormal sein und komplexe Spektralstruktur besitzen. Im tatsächlichen O2-Modulusblock passiert das nicht auf Spektralebene:

\[
\boxed{
\text{Der Modulus-Cross-Gram besitzt nur reelles nichtnegatives Spektrum.}
}
\tag{P11O3.27}
\]

Seine Nichtselbstadjungiertheit im nativen Source-Skalarprodukt stammt ausschließlich aus der Ähnlichkeitstransformation durch `A_R^{1/4}`.

**Firewall:** Ähnlichkeit zu einem positiven Operator macht `mathscr C` im nativen Skalarprodukt nicht selbstadjungiert und nicht normal.

---

# 4. Gewichtete Selbstadjungiertheit

Setze

\[
\boxed{
M:=A_R^{-1/2}.
}
\tag{P11O3.28}
\]

Da `A_R` positiv invertierbar ist, ist `M` positiv invertierbar und definiert auf dem Source-Raum das äquivalente Skalarprodukt

\[
\boxed{
\langle f,g\rangle_M
:=\langle Mf,g\rangle.
}
\tag{P11O3.29}
\]

Nun

\[
\mathscr C=DA_R^{-1/2}=DM
\]

und

\[
\mathscr C^*=A_R^{-1/2}D=MD.
\]

Daher

\[
\boxed{
M\mathscr C
=MDM
=\mathscr C^*M.
}
\tag{P11O3.30}
\]

Dies ist exakt die Selbstadjungiertheitsbedingung von `mathscr C` bezüglich `langle.,.rangle_M`.

Außerdem

\[
M\mathscr C=MDM\ge0,
\]

weil `D>=0`.

Und aus `D<=A_R^{1/2}` folgt durch Kongruenz mit `M=A_R^{-1/2}`:

\[
MDM
\le
MA_R^{1/2}M
=A_R^{-1/2}
=M.
\]

Somit

\[
\boxed{
0\le_M\mathscr C\le_M I.
}
\tag{P11O3.31}
\]

Das heißt:

\[
\boxed{
\mathscr C
\text{ ist im }M\text{-Skalarprodukt ein positiver selbstadjungierter Kontraktor.}
}
\tag{P11O3.32}
\]

### Direkte unitäre Darstellung des gewichteten Operators

Setze

\[
S:=A_R^{-1/4}.
\]

Dann

\[
M=S^*S=S^2
\]

und

\[
S\mathscr C S^{-1}=B.
\]

Damit ist die gewichtete Geometrie exakt die native positive Geometrie des Kontraktors `B`.

---

# 5. Der dimensionslose Defekt und die native Ähnlichkeitsverstärkung

Aus

\[
B=I-\Theta
\]

und (P11O3.25):

\[
\begin{aligned}
\mathscr C
&=A_R^{1/4}(I-\Theta)A_R^{-1/4}\\
&=I-A_R^{1/4}\Theta A_R^{-1/4}.
\end{aligned}
\]

Also

\[
\boxed{
I-\mathscr C
=A_R^{1/4}\Theta A_R^{-1/4}.
}
\tag{P11O3.33}
\]

Adjungieren liefert

\[
\boxed{
I-\mathscr C^*
=A_R^{-1/4}\Theta A_R^{1/4}.
}
\tag{P11O3.34}
\]

O2s Isometriewinkel erfüllt allgemein

\[
(Q-W)^*(Q-W)
=2I-\mathscr C-\mathscr C^*.
\]

Daher exakt:

\[
\boxed{
(Q-W)^*(Q-W)
=
A_R^{1/4}\Theta A_R^{-1/4}
+
A_R^{-1/4}\Theta A_R^{1/4}.
}
\tag{P11O3.35}
\]

Diese Formel ist dieselbe Information wie O2s

\[
A_R^{-1/2}\mathscr J+\mathscr J A_R^{-1/2},
\]

aber jetzt in dimensionsloser symmetrischer Normalisierung.

---

# 6. Konditions-Firewall

Definiere die Viertelpotenz-Konditionsgröße

\[
\boxed{
\chi_R^{T,U}
:=
\|A_R^{1/4}\|
\|A_R^{-1/4}\|.
}
\tag{P11O3.36}
\]

Da `A_R` positiv invertierbar ist,

\[
\chi_R^{T,U}\ge1.
\]

Aus (P11O3.35):

\[
\begin{aligned}
\|(Q-W)^*(Q-W)\|
&\le
\|A_R^{1/4}\Theta A_R^{-1/4}\|
+
\|A_R^{-1/4}\Theta A_R^{1/4}\|\\
&\le
2\chi_R^{T,U}\|\Theta\|.
\end{aligned}
\]

Da

\[
\|Q-W\|^2
=
\|(Q-W)^*(Q-W)\|,
\]

folgt

\[
\boxed{
\|Q-W\|^2
\le
2\chi_R^{T,U}\|\Theta\|.
}
\tag{P11O3.37}
\]

Somit der direkte hinreichende Operatornorm-Zieltyp:

\[
\boxed{
\chi_R^{T,U}\|\Theta_{R,S}^{T,U}\|
\longrightarrow0
\quad\Longrightarrow\quad
\|Q_{R,S}^{T,U}-W_{R,S}^{[T]}\|
\longrightarrow0.
}
\tag{P11O3.38}
\]

Status:

\[
\boxed{\checkmark[M]_{\rm sufficient}.}
\]

### Warum dies nur ein Firewall-/Transferkriterium ist

O3 beweist weder

\[
\sup_{T<U}\chi_R^{T,U}<\infty
\]

noch

\[
\|\Theta_{R,S}^{T,U}\|\to0.
\]

Es ist daher unzulässig, aus der gewichteten Positivitätsstruktur allein auf nativen Winkelabschluss zu schließen.

Die korrekte neue Warnung lautet:

\[
\boxed{
\text{gewichtete Jensen-Kleinheit}
\not\Rightarrow
\text{native }Q/W\text{-Kleinheit}
\text{ ohne Kontrolle der beweglichen Ähnlichkeit}.}
\tag{P11O3.39}
\]

---

# 7. Umgekehrter endlicher Vergleich

Aus

\[
I-\mathscr C=W^*(W-Q)
\]

folgt

\[
\boxed{
\|I-\mathscr C\|
\le
\|Q-W\|.
}
\tag{P11O3.40}
\]

Aus (P11O3.33):

\[
\Theta
=A_R^{-1/4}(I-\mathscr C)A_R^{1/4}.
\]

Daher

\[
\boxed{
\|\Theta\|
\le
\chi_R^{T,U}\|I-\mathscr C\|
\le
\chi_R^{T,U}\|Q-W\|.
}
\tag{P11O3.41}
\]

Damit sind `Theta` und der native Isometriewinkel für jedes feste `T,U` weiterhin äquivalent, aber quantitative uniforme Asymptotik kann durch `chi_R^{T,U}` verzerrt werden.

**Firewall:** (P11O3.37) und (P11O3.41) ergeben keine asymptotische Äquivalenz, solange `chi_R^{T,U}` nicht kontrolliert ist.

---

# 8. Normalisiertes Range-Leakage

O1 definierte

\[
\mathscr L
=(I-P)A_S^{1/2}W,
\qquad
P:=WW^*.
\]

Definiere nun das dimensionslos normalisierte Leakage

\[
\boxed{
\mathscr N
:=(I-P)Q
=\mathscr L A_R^{-1/2}.
}
\tag{P11O3.42}
\]

Außerdem gilt

\[
PQ
=WW^*Q
=W\mathscr C.
\]

Daher die exakte orthogonale Zerlegung

\[
\boxed{
Q=W\mathscr C+\mathscr N,
\qquad
W^*\mathscr N=0.
}
\tag{P11O3.43}
\]

Da `Q` Isometrie ist:

\[
I=Q^*Q
=\mathscr C^*\mathscr C+\mathscr N^*\mathscr N.
\]

Also

\[
\boxed{
\mathscr N^*\mathscr N
=I-\mathscr C^*\mathscr C.
}
\tag{P11O3.44}
\]

Der Moduluswinkel selbst zerfällt orthogonal:

\[
Q-W
=W(\mathscr C-I)+\mathscr N.
\]

Damit

\[
\boxed{
(Q-W)^*(Q-W)
=(\mathscr C-I)^*(\mathscr C-I)
+\mathscr N^*\mathscr N.
}
\tag{P11O3.45}
\]

Setzt man (P11O3.44) ein, erhält man wieder

\[
2I-\mathscr C-\mathscr C^*.
\]

### Interpretation

Der O2-Moduluswinkel besitzt zwei geometrische Komponenten:

1. normiertes Herauslecken aus `Ran W` über `mathscr N`;
2. einen internen Cross-Gram-Defekt `mathscr C-I` innerhalb des alten Bildraums.

Diese sind jedoch nicht frei: `mathscr C` ist ähnlich zum positiven Kontraktor `B=I-Theta`.

Insbesondere ist `mathscr C-I` keine beliebige unitäre Phasenbewegung.

---

# 9. Exakte normierte Defektbalance

Setze

\[
\boxed{
\mathscr K:=I-\mathscr C.
}
\tag{P11O3.46}
\]

Dann

\[
Q-W=-W\mathscr K+\mathscr N.
\]

Aus

\[
\mathscr C=I-\mathscr K
\]

und (P11O3.44):

\[
\begin{aligned}
\mathscr N^*\mathscr N
&=I-(I-\mathscr K)^*(I-\mathscr K)\\
&=\mathscr K+\mathscr K^*-\mathscr K^*\mathscr K.
\end{aligned}
\]

Also

\[
\boxed{
\mathscr K+\mathscr K^*
=
\mathscr K^*\mathscr K
+
\mathscr N^*\mathscr N.
}
\tag{P11O3.47}
\]

Und wegen der orthogonalen Zerlegung:

\[
\boxed{
(Q-W)^*(Q-W)
=
\mathscr K^*\mathscr K
+
\mathscr N^*\mathscr N.
}
\tag{P11O3.48}
\]

Dies ist die vollständig normierte Pythagoras-Version von O2.

Da

\[
\mathscr K
=A_R^{1/4}\Theta A_R^{-1/4},
\]

ist auch der interne Defekt ähnlich zu einem positiven Kontraktionsdefekt.

---

# 10. Exakte Nulläquivalenzen

Für feste `T,U` gilt wegen Invertierbarkeit der Normalisierungen und O2:

\[
\boxed{
\Theta=0
\iff
\mathscr J=0
\iff
B=I
\iff
\mathscr C=I
\iff
Q=W
\iff
\mathscr N=0
\iff
\mathscr L=0.
}
\tag{P11O3.49}
\]

Beim Schritt `mathscr N=0 iff mathscr L=0` wird nur die Invertierbarkeit von `A_R^{-1/2}` verwendet.

Beim Schritt `mathscr L=0 iff mathscr J=0` gilt die in O2 bereits auditierte positive-Quadratwurzel-Argumentation.

**Wichtig:** Diese exakten endlichen Nulläquivalenzen sind keine uniforme asymptotische Äquivalenz.

---

# 11. Spektralphase versus Ähnlichkeitsnonnormalität

Aus (P11O3.26):

\[
\sigma(\mathscr C)\subseteq[0,1].
\]

Damit ist ausgeschlossen, dass der Modulus-Cross-Gram seine Nichttrivialität durch genuine komplexe Spektralrotation trägt.

Die verbleibende native Schwierigkeit ist vielmehr:

\[
\boxed{
\text{positive gewichtete Kontraktion}
\xrightarrow{\text{bewegliche Ähnlichkeit }A_R^{1/4}}
\text{möglicherweise nichtnormaler nativer Cross-Gram}.}
\tag{P11O3.50}
\]

Dies trennt den Modulusblock konzeptionell schärfer von der echten Gauge-Polarphase `mathcal U_H` aus O1/O2.

Die Polarphase `mathcal U_H` ist eine reale unitäre Phase des Gauge-Wechsels.

Der Modulus-Cross-Gram `mathscr C` besitzt dagegen nur eine **Ähnlichkeitsnonnormalität** über einen positiven Kontraktor.

---

# 12. Parität

O1/O2 bewiesen, dass

\[
A_R,
\quad
A_S,
\quad
W,
\quad
Q
\]

die Paritätssektoren respektieren beziehungsweise intertwinen.

Daher tun dies auch

\[
D,
\quad
\mathscr J,
\quad
B,
\quad
\Theta,
\quad
\mathscr C,
\quad
\mathscr K,
\quad
\mathscr N.
\]

Insbesondere zerfällt

\[
\Theta
=
\Theta_+\oplus\Theta_-,
\]

und die originale Klasse-O-Frage kann weiterhin separat auf dem ungeraden Sektor verfolgt werden.

O3 behauptet keine Aussage über die Asymptotik von `Theta_-`.

---

# 13. Asymptotische Konsequenztypen

Der exakte Originaltest bleibt

\[
W_{R,S,-}^{[T]}
\xrightarrow[T\to\infty]{\rm strong}?
W_{R,S,-}^{[\infty]}.
\]

O2 reduziert den direkten Defekt auf

\[
\mathcal U_S(Q-W_T)\mathcal U_R^*
+
\mathscr P.
\]

O3 liefert nun für den Modulusanteil mehrere **hinreichende**, aber nicht notwendige Zieltypen.

### O3-S1 — native Winkelkontrolle

Direkt:

\[
(Q-W_T)(\mathcal U_R)^*f\to0.
\]

Dies bleibt der schärfste Vektor-Zieltyp für den Modulusanteil.

### O3-S2 — Operatornormkontrolle

Stärker, aber moving-vector-sicher:

\[
\|Q-W_T\|\to0.
\]

### O3-S3 — symmetrischer Jensen plus Kondition

Hinreichend für S2:

\[
\boxed{
\chi_R^{T,U}\|\Theta_{R,S}^{T,U}\|\to0.
}
\tag{P11O3.51}
\]

### O3-S4 — getrennte normierte Leakage-/Cross-Gram-Kontrolle

Aus (P11O3.48) hinreichend:

\[
\|\mathscr K\|\to0,
\qquad
\|\mathscr N\|\to0.
\]

Aber dies ist nur eine weitere hinreichende Aufspaltung und kein notwendiger asymptotischer Satz.

---

# 14. Was O3 nicht löst

O3 beweist nicht:

1. `Theta -> 0`;
2. `chi_R` ist uniform beschränkt;
3. `Q-W_T -> 0` stark oder in Operatornorm;
4. `mathscr P -> 0`;
5. die moving-vector-Frage;
6. starke Konvergenz des odd Terminaltransports;
7. starke Nichtkonvergenz;
8. Monotonie `A_H^{T,U}>=I`;
9. Monotonie `G_{H,U}>=G_{H,T}`;
10. Residualäquivalenz;
11. R3;
12. `q_{r,T}`-Asymptotik;
13. `a_{R,T}^{(2)}\neq0`;
14. P11-Readiness;
15. SYN;
16. Seal;
17. Objekt-X-Existenz;
18. Weil-Positivität;
19. RH.

Der Originalstatus bleibt:

\[
\boxed{
W_{R,S,-}^{[T]}
\xrightarrow[T\to\infty]{\rm strong}?
W_{R,S,-}^{[\infty]}.
}
\tag{P11O3.52}
\]

---

# 15. Persistente O3-Firewalls

## O3-FW1 — positives ähnliches Modell ist nicht native Selbstadjungiertheit

\[
\mathscr C\sim B,
\qquad
0\le B\le I
\]

impliziert nicht, dass `mathscr C` im nativen Skalarprodukt selbstadjungiert oder normal ist.

## O3-FW2 — Spektrum in [0,1] ist kein Normabschluss

\[
\sigma(\mathscr C)\subseteq[0,1]
\]

impliziert nicht

\[
\mathscr C\to I.
\]

## O3-FW3 — Theta ist nur endlich beschränkt

\[
0\le\Theta\le I
\]

impliziert nicht

\[
\Theta\to0.
\]

## O3-FW4 — Konditionsverstärkung

Auch wenn `Theta` in einer gewichteten Geometrie klein wird, kann die bewegliche Ähnlichkeit über `A_R^{\pm1/4}` eine native Schlussfolgerung verhindern.

## O3-FW5 — keine uniforme Kondition erfunden

Es wird nicht behauptet

\[
\sup_{T<U}\chi_R^{T,U}<\infty.
\]

## O3-FW6 — Moving-vector bleibt

Ein bloßer starker fixed-vector Grenzwert von `Q-W_T` genügt für

\[
(Q-W_T)(\mathcal U_R^{T,U})^*f
\]

nicht automatisch.

## O3-FW7 — echte Polarphase bleibt separat

Die Ähnlichkeitsnonnormalität von `mathscr C` ist nicht mit der unitären Gauge-Polarphase `mathcal U_H` gleichzusetzen.

## O3-FW8 — keine Residualsubstitution

Kein `q_r`, `a^{(2)}` oder R3 wird in O3 importiert.

## O3-FW9 — kein automatischer O4

Nach O3 folgt zunächst destruktiver Gegencheck und GPT-Reconciliation.

---

# 16. Gegenprüfer-Checkliste

Der destruktive Gegencheck soll insbesondere prüfen:

1. Ist `B=A_R^{-1/4}DA_R^{-1/4}` positiv und `<=I`?
2. Ist `Theta=I-B=A_R^{-1/4}mathscr J A_R^{-1/4}` korrekt?
3. Ist `mathscr C=W^*Q=DA_R^{-1/2}` korrekt?
4. Ist `mathscr C=A_R^{1/4}BA_R^{-1/4}` exakt?
5. Folgt daraus wirklich `sigma(mathscr C) subset [0,1]`?
6. Ist `M=A_R^{-1/2}` das korrekte Gewicht für `M mathscr C = mathscr C^* M`?
7. Ist `0 <= M mathscr C <= M` korrekt?
8. Ist `I-mathscr C=A_R^{1/4}Theta A_R^{-1/4}` korrekt?
9. Ist die Winkelidentität (P11O3.35) korrekt?
10. Ist die Konditionsabschätzung (P11O3.37) korrekt?
11. Ist der umgekehrte Vergleich (P11O3.41) korrekt?
12. Ist `mathscr N=(I-P)Q=mathscr L A_R^{-1/2}` korrekt?
13. Ist `Q=W mathscr C+mathscr N` eine orthogonale Zerlegung?
14. Folgt `mathscr C^*mathscr C+mathscr N^*mathscr N=I`?
15. Ist die normierte Pythagoras-/Defektbalance korrekt?
16. Sind alle Nulläquivalenzen in (P11O3.49) zulässig?
17. Wird aus Similarity oder Spektrum nirgendwo native Normalität behauptet?
18. Wird keine asymptotische Konditionskontrolle erfunden?
19. Bleibt der odd Terminallimes offen?
20. Bleiben Polarphase und Residualroute getrennt?

---

# 17. Endurteil

O2 hatte den Modulusanteil des direkten Terminalproblems auf den Isometriewinkel

\[
Q-W_T
\]

reduziert.

O3 zeigt nun, dass auch dieser Winkel intern keine beliebige Isometriegeometrie besitzt.

Sein Cross-Gram

\[
\mathscr C=W_T^*Q
\]

ist ähnlich zu dem positiven Kontraktor

\[
B=I-\Theta,
\qquad
0\le\Theta\le I.
\]

Damit lautet die Modulusstruktur genauer:

\[
\boxed{
\text{positiver dimensionsloser Jensen-Winkel }\Theta
+
\text{bewegliche Ähnlichkeits-/Konditionsgeometrie }A_R^{\pm1/4}.
}
\tag{P11O3.53}
\]

Die echte unitäre Phase des gesamten Terminalproblems bleibt weiterhin ausschließlich im separaten Gauge-Polarphasenblock `mathscr P`.

Dies ist eine weitere direkte Schärfung von Klasse O, aber noch kein asymptotischer Abschluss.

Daher verbindlich:

\[
\boxed{
\texttt{P11-O3 = PARTIAL DIRECT REDUCTION, NOT TERMINAL CLOSURE}.
}
\]

Kein SYN, kein Seal, kein `papers/P11`, kein RH-Schluss und kein automatischer Folgeknoten.