# NEU-36 — X.3.6: Determinantenkonvergenz der BC-Jacobi-Approximanten

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-30–35  
**Ziel:** Formuliere den Connes-Grenzschritt in BC-Sprache:

\[
\det_{Wres,N}(s-D_{X,N}^{geom,-}) \longrightarrow C\cdot \xi(s)
\]

ohne die Nullstellen von \(\xi\) in die Konstruktion einzubauen.

---

## 0. Ausgangslage

Aus NEU-34/35 steht der natürliche nicht-tautologische endliche Kandidat:

\[
D_{N}^{-}
:=
D_{X,N}^{geom,-}
=
\frac12 I+iA_N^{-},
\qquad
A_N^{-}:=H_N+\beta_NJ_N^{-}.
\]

Hierbei gilt:

- \(H_N\) ist der diagonale logarithmische/modulare Generator.
- \(J_N^{-}\) ist die \(Wres\)-kanonische schiefadjungierte Jacobi-Kopplung aus \(\widetilde\omega_2\).
- Der rohe Shift \(\Theta_N\) ist nicht normal.
- \(J_N^{+}\) ist zu stark selbstadjungiert und würde die kritische Gerade per Bau erzwingen.
- \(J_N^{-}\) ist der echte Testkandidat.

Die gewünschte Grenzbehauptung lautet daher nicht:

\[
\operatorname{Spec}(D_N^{-})\to Z(\xi)
\]

als primitive Annahme, sondern:

\[
\boxed{
\det_{Wres,N}(s-D_N^{-}) \longrightarrow C\cdot \xi(s)
}
\tag{36.1}
\]

als Konsequenz der BC-intrinsischen Konstruktion.

---

## 1. Warnung: Determinantenkonvergenz ist nicht Spektralkonvergenz

Für jedes endliche \(N\) ist \(D_N^{-}\) ein endlich-dimensionaler oder endlich-rangiger Operator auf dem trunkierten BC-Sektor \(B_{3,N}\). Daher existiert formal ein endliches charakteristisches Polynom.

Aber:

\[
\det(s-D_N^{-})
\]

ist nicht kanonisch genug. Es hängt von folgenden Daten ab:

1. Wahl der endlichen Trunkierung \(B_{3,N}\),
2. Wahl der \(Wres\)-Gram-Matrix,
3. Normierung der Spur,
4. eventueller Hadamard-/Weierstraß-Renormierung,
5. Behandlung von Randzuständen im Fourier-Orbit.

Daher ist die korrekte Größe nicht zuerst das Polynom, sondern seine logarithmische Ableitung.

---

## 2. Definition der endlichen \(Wres\)-Resolventspur

Fixiere die normalisierte Kopplung

\[
L_3^\circ:=C_L^{-1}L_3.
\]

Definiere für \(s\notin \operatorname{Spec}(D_N^{-})\):

\[
\boxed{
H_N^{-}(s)
:=
\operatorname{Tr}_{Wres,N}^{top}
\left((s-D_N^{-})^{-1}L_3^\circ\right).
}
\tag{36.2}
\]

Dies ist die endliche BC-Analogie zu

\[
H_\xi(s):=\frac{\xi'(s)}{\xi(s)}.
\]

Die Determinante wird nun nicht primär algebraisch definiert, sondern durch Integration der logarithmischen Ableitung.

Wähle einen Basispunkt \(s_0\) mit \(\xi(s_0)\ne0\), zum Beispiel \(s_0=2\). Setze:

\[
\boxed{
\mathcal D_N^{-}(s)
:=
\xi(s_0)\exp\left(
\int_{s_0}^{s} H_N^{-}(u)\,du
\right).
}
\tag{36.3}
\]

Die Integrale sind auf einfach zusammenhängenden Gebieten ohne Spektralpunkte von \(D_N^{-}\) zu verstehen. Global erhält man ein meromorph/entire reguliertes Objekt durch kanonische Hadamard-Fortsetzung.

Damit gilt per Definition:

\[
\partial_s\log \mathcal D_N^{-}(s)=H_N^{-}(s),
\qquad
\mathcal D_N^{-}(s_0)=\xi(s_0).
\tag{36.4}
\]

---

## 3. Hauptreduktion von NEU-36

### Satz 36.1 — Logarithmische Reduktion der Determinantenkonvergenz

Sei \(\Omega\subset\mathbb C\) ein einfach zusammenhängendes Gebiet, das keine Nullstelle von \(\xi\) enthält und für \(N\gg1\) keine Spektralpunkte von \(D_N^{-}\) enthält. Dann gilt:

\[
\mathcal D_N^{-}\to \xi
\quad\text{lokal gleichmäßig auf }\Omega
\]

genau dann, wenn

\[
H_N^{-}(s)\to \frac{\xi'(s)}{\xi(s)}
\quad\text{lokal gleichmäßig auf }\Omega
\]

und die Normierung

\[
\mathcal D_N^{-}(s_0)=\xi(s_0)
\]

festgehalten wird.

**Beweis.**

Aus lokaler gleichmäßiger Konvergenz der logarithmischen Ableitungen folgt für \(s\in\Omega\):

\[
\log\frac{\mathcal D_N^{-}(s)}{\xi(s)}
=
\int_{s_0}^{s}
\left(
H_N^{-}(u)-\frac{\xi'(u)}{\xi(u)}
\right)du.
\]

Die rechte Seite konvergiert lokal gleichmäßig gegen \(0\). Also:

\[
\frac{\mathcal D_N^{-}(s)}{\xi(s)}\to1.
\]

Die Umkehrung folgt durch Differentiation der lokal gleichmäßigen Konvergenz holomorpher nichtverschwindender Funktionen auf kompakten Teilgebieten, sofern keine Nullstellen oder Spektralpunkte getroffen werden.

\[
\boxed{\text{Damit ist der Connes-Grenzschritt ein Resolventspur-Grenzproblem.}}
\]

Status: ✓ [M]

---

## 4. Lokale Nullstellenfassung

Um Nullstellen einzuschließen, arbeite auf Konturen.

Sei \(\Gamma\) eine positiv orientierte glatte Kurve, die keine Nullstelle von \(\xi\) und für \(N\gg1\) keinen Spektralpunkt von \(D_N^{-}\) trifft.

Dann folgt aus

\[
H_N^{-}\to \xi'/\xi
\quad\text{lokal gleichmäßig auf }\Gamma
\]

die Konvergenz der Nullstellenzählfunktionen:

\[
\frac{1}{2\pi i}\int_\Gamma H_N^{-}(s)\,ds
\longrightarrow
\frac{1}{2\pi i}\int_\Gamma \frac{\xi'(s)}{\xi(s)}\,ds
=
\sum_{\rho\in \operatorname{int}(\Gamma)}m_\rho.
\tag{36.5}
\]

Stärker gilt für holomorphe Testfunktionen \(f\):

\[
\frac{1}{2\pi i}\int_\Gamma f(s)H_N^{-}(s)\,ds
\longrightarrow
\sum_{\rho\in \operatorname{int}(\Gamma)}m_\rho f(\rho).
\tag{36.6}
\]

Dies ist die einfache-Resolvent-Version der NEU-29-Spurformel.

Status: ✓ [M] relativ zur Resolventspur-Konvergenz.

---

## 5. Fehlerzerlegung

Definiere den Grenzfehler:

\[
E_N(s)
:=
H_N^{-}(s)-\frac{\xi'(s)}{\xi(s)}.
\tag{36.7}
\]

NEU-36 isoliert vier voneinander unabhängige Fehlerquellen:

\[
\boxed{
E_N
=
E_N^{prime}
+
E_N^{Jac}
+
E_N^{Wres}
+
E_N^{\Gamma}.
}
\tag{36.8}
\]

### 5.1 Primtrunkierungsfehler \(E_N^{prime}\)

Dieser misst den Unterschied zwischen endlichem BC-Primsektor und vollständigem Eulerprodukt.

Erwartete Form für \(\Re(s)>1\):

\[
E_N^{prime}(s)
\sim
-\sum_{p>N}\frac{\log p}{p^s-1}
\]

plus höhere modulare Korrekturen.

Status: ✓ [M] als formale Fehlerquelle, ⚠ [M] für exakte BC-Normabschätzung.

---

### 5.2 Jacobi-Kopplungsfehler \(E_N^{Jac}\)

Dieser misst, ob die \(J_N^{-}\)-Kopplung exakt die linearisierte \(\widetilde\omega_2\)-Dynamik erzeugt.

Zielbedingung:

\[
\operatorname{Tr}_{Wres,N}
\left((s-D_N^{-})^{-1}L_3^\circ\right)
=
-\sum_{n\in \langle p\le N\rangle}
\Lambda_N(n)n^{-s}
+\text{Gamma-/Randkorrektur}
\tag{36.9}
\]

mit einem effektiven von \(J_N^{-}\) erzeugten Mangoldt-Gewicht \(\Lambda_N\).

Status: ❓ [O]

---

### 5.3 \(Wres\)-Stetigkeitsfehler \(E_N^{Wres}\)

Dieser ist genau der alte OP-4.1a-Rest:

\[
\operatorname{Tr}_{Wres,N}\lim
=
\lim \operatorname{Tr}_{Wres,N}.
\]

Solange OP-4.1a nur intern gesichert ist, bleibt die globale Vertauschung von Grenzwert, Spur und Resolvent ein ⚠ [M]-Punkt.

Status: ⚠ [M]

---

### 5.4 Gamma-Faktor-Fehler \(E_N^\Gamma\)

NEU-28 hat bereits gezeigt, dass die \(\zeta\)-Seite zur \(\xi\)-Seite durch explizite Gamma-Korrektur gehoben werden muss.

Für die einfache logarithmische Ableitung lautet:

\[
\frac{\xi'}{\xi}(s)
=
\frac12\log\pi^{-1}
+
\frac12\frac{\Gamma'}{\Gamma}\left(\frac{s}{2}\right)
+
\frac{1}{s}
+
\frac{1}{s-1}
+
\frac{\zeta'}{\zeta}(s)
\]

je nach verwendeter Normalisierung von \(\xi\).

Der BC-Operator muss daher entweder:

1. den archimedischen Faktor als Zusatzsektor tragen, oder
2. \(E_N^\Gamma\) extern additiv korrigieren.

Status: ✓ [M] als notwendige Korrektur, ❓ [O] als intrinsische BC-Realisierung.

---

## 6. Der NEU-36-Leitsatz

### Leitsatz 36.2 — BC-Connes-Grenzproblem

Die Determinantenkonvergenz

\[
\boxed{
\mathcal D_N^{-}(s)\to \xi(s)
}
\tag{36.10}
\]

ist äquivalent zu den drei Aussagen:

1. **Resolventspur-Konvergenz**

   \[
   H_N^{-}(s)\to \xi'(s)/\xi(s)
   \]

   lokal gleichmäßig außerhalb der Nullstellen.

2. **Residuenkorrektheit**

   Für jede Nullstelle \(\rho\):

   \[
   \operatorname{Res}_{s=\rho} H_N^{-}(s)\to m_\rho.
   \]

3. **Normalisierung**

   \[
   \mathcal D_N^{-}(s_0)=\xi(s_0)
   \]

   für einen festen Basispunkt \(s_0\).

Status: ✓ [M]

---

## 7. RH-Folgerung aus endlicher Realitätsstruktur

Angenommen zusätzlich:

\[
\operatorname{Spec}(A_N^{-})\subset\mathbb R
\quad\text{für alle }N,
\tag{36.11}
\]

und

\[
\mathcal D_N^{-}\to \xi
\]

lokal gleichmäßig als Hadamard-regulierte Determinanten.

Dann liegen alle Grenznullstellen von \(\xi\) auf

\[
\Re(s)=\frac12.
\]

Denn die Nullstellen von \(\mathcal D_N^{-}\) liegen bei

\[
s=\frac12+i\lambda,
\qquad
\lambda\in\operatorname{Spec}(A_N^{-})\subset\mathbb R.
\]

Nach Hurwitz können nichtverschwindende Grenznullstellen nur Grenzpunkte solcher Nullstellen sein. Also:

\[
\boxed{RH.}
\]

Status: ✓ [M] unter Determinantenkonvergenz und Spektralrealität.

---

## 8. Umgekehrte Richtung

RH impliziert nicht automatisch:

\[
\operatorname{Spec}(A_N^{-})\subset\mathbb R
\]

für die konkreten BC-Approximanten.

Die Rückrichtung braucht eine Stabilitätsaussage:

\[
RH
\Longrightarrow
J_N^{-}\text{ erzeugt asymptotisch eine positive }Wres\text{-Hilbertisierung}
\Longrightarrow
\operatorname{dist}(\operatorname{Spec}(A_N^{-}),\mathbb R)\to0.
\]

Das ist derzeit nicht bewiesen.

Status: ❓ [O]

---

## 9. Konkrete nächste Aufgabe

NEU-36 reduziert den Grenzschritt auf die Berechnung von

\[
H_N^{-}(s)
=
\operatorname{Tr}_{Wres,N}^{top}
\left((s-\frac12I-iH_N-i\beta_NJ_N^{-})^{-1}L_3^\circ\right).
\tag{36.12}
\]

Die nächste Arbeit ist daher nicht mehr abstrakt, sondern rechnerisch:

\[
\boxed{
\text{NEU-37: Jacobi-Resolvent und effektives Mangoldt-Gewicht.}
}
\]

Zu zeigen wäre:

\[
H_N^{-}(s)
=
\frac{\xi_N'(s)}{\xi_N(s)}
+
\varepsilon_N(s),
\qquad
\varepsilon_N\to0,
\tag{36.13}
\]

wobei \(\xi_N\) ein BC-intrinsischer endlicher Euler-/Hadamard-Approximant ist.

---

## 10. Statusmatrix

| Aussage | Status |
|---|---:|
| Determinantenkonvergenz wird auf logarithmische Resolventspur reduziert | ✓ [M] |
| Cauchy-/Argumentprinzip-Version | ✓ [M] |
| Normierung durch Basispunkt \(s_0\) | ✓ [M] |
| RH-Folgerung aus Spektralrealität + Determinantenkonvergenz | ✓ [M] |
| exakte Berechnung von \(H_N^{-}\) | ❓ [O] |
| \(J_N^{-}\) erzeugt effektives Mangoldt-Gewicht | ❓ [O] |
| OP-4.1a-Grenzwert-Spur-Vertauschung | ⚠ [M] |
| intrinsische Gamma-Faktor-Realisierung | ❓ [O] |
| Rückrichtung RH ⇒ reale endliche Spektren | ❓ [O] |

---

## 11. Kurzfazit

NEU-36 beweist noch nicht die Determinantenkonvergenz.  
Es zeigt aber, dass der harte Connes-Grenzschritt exakt auf eine konkrete BC-Resolventrechnung reduziert ist:

\[
\operatorname{Tr}_{Wres,N}^{top}
\left((s-D_N^{-})^{-1}L_3^\circ\right)
\stackrel{?}{\longrightarrow}
\frac{\xi'(s)}{\xi(s)}.
\]

Damit ist der nächste Engpass klar:

\[
\boxed{
\text{Berechne den Jacobi-Resolventen von }A_N^{-}=H_N+\beta_NJ_N^{-}.
}
\]

Das ist NEU-37.
