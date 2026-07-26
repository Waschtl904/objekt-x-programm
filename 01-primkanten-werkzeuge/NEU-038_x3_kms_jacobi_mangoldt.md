# NEU-38 — X.3.8: KMS-gewichteter Jacobi-Resolvent und Rückgewinnung von \(n^{-s}\)

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-28, NEU-35–37  
**Ziel:** Prüfe, ob der Kürzungsmechanismus aus NEU-28 mit der Jacobi-Kopplung \(J_N^-\) aus NEU-35/37 kompatibel ist.

---

## 0. Leitfrage

NEU-28 zeigte auf der direkten KMS-Seite:

\[
\lambda_{mod}(s)=\frac{C_L}{\zeta(s)}
\]

durch den Mechanismus:

\[
n^s \ \text{aus}\ \Delta_s^{-1}
\qquad\times\qquad
n^{-s}\ \text{aus}\ \phi_s
\qquad\Longrightarrow\qquad
1,
\]

wobei die verbleibende \(s\)-Abhängigkeit aus der KMS-Normierung

\[
Z(s)^{-1}=\zeta(s)^{-1}
\]

kommt.

NEU-37 zeigte dagegen:

\[
H_N^-(z)
=
\text{gewichtete Cauchy-Transformierte von Jacobi-Maßen}.
\]

Die Frage von NEU-38 lautet:

\[
\boxed{
\text{Ist der KMS-Kürzungsmechanismus mit dem Jacobi-Resolventen kompatibel?}
}
\]

Die Antwort ist zweigeteilt:

1. **Ja, formal:** \(J_N^-\) verändert den \(V_n\)-Sektor nicht. Daher ist die KMS-Gewichtung auf jeder Jacobi-Kette konstant und die Faktoren \(n^{\pm s}\) können wie in NEU-28 gekürzt werden.

2. **Nein, nicht ausreichend:** Diese Kürzung erzeugt noch keine Mangoldt-Gewichte. Sie liefert nur die richtige Dirichlet-/KMS-Basis und die inverse Zeta-Normierung. Die Mangoldt-Gewichte brauchen zusätzlich eine logarithmische/verbundene Spur- oder Momentenidentität.

Status: ✓ [M] als Kompatibilitätsdiagnose, ❓ [O] für die Mangoldt-Identität.

---

## 1. Zwei Parameter statt ein Parameter

Ein Notationsfehler droht, wenn man denselben Buchstaben \(s\) gleichzeitig für den KMS-Parameter und für den Resolventparameter verwendet.

Wir trennen daher:

- \(\beta\): KMS-/Dirichlet-Parameter,
- \(z\): Spektral-/Resolventparameter.

Der zweiparametrige Jacobi-KMS-Resolvent ist:

\[
\boxed{
\mathcal J_N(z;\beta)
:=
\operatorname{Tr}_{Wres,N}^{top}
\left(
\phi_{\beta,N}\bigl((z-D_N^-)^{-1}L_3^\circ\bigr)
\right).
}
\tag{38.1}
\]

Dabei ist

\[
D_N^-=\frac12I+i(H_N+\beta_NJ_N^-).
\]

Diese Trennung ist zwingend.  
Nur nach einer bewiesenen zweiparametrigen Identität darf man eine Diagonale \(z=z(\beta)\) einsetzen.

Status: ✓ [M]

---

## 2. KMS-Zerlegung nach \(V_n\)-Sektoren

Sei

\[
S_N:=\langle p\le N\rangle
\]

die von den Primzahlen \(p\le N\) erzeugte freie kommutative Halbgruppe.

Die KMS-Gewichtung hat auf dem \(V_n\)-Sektor die Form

\[
\phi_{\beta,N}|_{V_n}
=
Z_N(\beta)^{-1}n^{-\beta}\tau_n,
\]

mit

\[
Z_N(\beta)
=
\sum_{n\in S_N}n^{-\beta}
=
\prod_{p\le N}(1-p^{-\beta})^{-1}
=:\zeta_N(\beta).
\]

Also

\[
Z_N(\beta)^{-1}
=
\prod_{p\le N}(1-p^{-\beta})
=
\frac{1}{\zeta_N(\beta)}.
\]

Da \(J_N^-\) aus \(\widetilde\omega_2\) nur den Fourierindex verschiebt,

\[
r\mapsto r+n,
\]

aber \(n\) nicht verändert, gilt:

\[
[P_n,J_N^-]=0,
\qquad
[P_n,H_N]=0,
\qquad
[P_n,D_N^-]=0.
\]

Daher zerfällt der Resolvent sektoriell:

\[
(z-D_N^-)^{-1}
=
\bigoplus_{n\in S_N}
(z-D_{N,n}^-)^{-1}.
\]

Status: ✓ [M]

---

## 3. Reine KMS-Jacobi-Resolventreihe

Aus NEU-37 folgt für den \(n\)-Sektor:

\[
C_N(n;z)
:=
-i
\sum_{a,M}
\sum_{j=0}^{M}
\ell_j^{(n,a)}
\frac{
P_j^L(z_n)P_{M-j}^R(z_n)
}{
P_{M+1}^{(n,a)}(z_n)
},
\]

wobei

\[
z_n=-i(z-\tfrac12)-h(n)
\]

je nach gewählter \(z\)-Konvention.

Dann ist

\[
\boxed{
\mathcal J_N(z;\beta)
=
\frac{1}{\zeta_N(\beta)}
\sum_{n\in S_N}
C_N(n;z)n^{-\beta}.
}
\tag{38.2}
\]

Ohne KMS-Normierung wäre dies eine gewöhnliche endliche Dirichletreihe.  
Mit KMS-Normierung kommt der Faktor \(\zeta_N(\beta)^{-1}\) hinzu.

Status: ✓ [M]

---

## 4. Modulare Kürzungsvariante mit \(\Delta_\beta^{-1}\)

Der NEU-28-Mechanismus verwendet nicht nur \(\phi_\beta\), sondern auch einen modularen Faktor

\[
\Delta_\beta^{-1}|_{V_n}=n^\beta.
\]

Definiere daher den gekürzten Jacobi-KMS-Resolventen:

\[
\boxed{
\mathcal J_N^{mod}(z;\beta)
:=
\operatorname{Tr}_{Wres,N}^{top}
\left(
\phi_{\beta,N}
\bigl((z-D_N^-)^{-1}L_3^\circ\Delta_\beta^{-1}\bigr)
\right).
}
\tag{38.3}
\]

Dann kürzen sich im \(V_n\)-Sektor:

\[
n^{-\beta}\cdot n^\beta=1.
\]

Also:

\[
\boxed{
\mathcal J_N^{mod}(z;\beta)
=
\frac{1}{\zeta_N(\beta)}
\sum_{n\in S_N}C_N(n;z).
}
\tag{38.4}
\]

Damit ist der NEU-28-Kürzungsmechanismus mit dem Jacobi-Resolventen kompatibel.

Status: ✓ [M]

---

## 5. Vergleich mit NEU-28

NEU-28 ist der Spezialfall, in dem der gesamte \(n\)-Sektorbeitrag konstant summiert:

\[
\sum_{n\in S_N}C_N^{NEU28}(n)=C_L.
\]

Dann folgt:

\[
\lambda_{mod,N}(\beta)
=
\frac{C_L}{\zeta_N(\beta)}.
\]

Für den Jacobi-Resolventen erhalten wir dagegen:

\[
\mathcal J_N^{mod}(z;\beta)
=
\frac{S_N^{Jac}(z)}{\zeta_N(\beta)},
\]

mit

\[
S_N^{Jac}(z):=\sum_{n\in S_N}C_N(n;z).
\]

Daher ist die Kompatibilität mit NEU-28 äquivalent zu:

\[
\boxed{
S_N^{Jac}(z)=C_L
}
\tag{38.5}
\]

oder, nach Cauchy-Integration gegen eine Testfunktion \(F\),

\[
\boxed{
\frac{1}{2\pi i}\int_\Gamma F(z)S_N^{Jac}(z)\,dz=C_L(f)
}
\tag{38.6}
\]

für die passende Testfunktion \(f=F'\).

Status: ✓ [M] als Reduktion, ❓ [O] als konkrete Jacobi-Identität.

---

## 6. Wichtige Korrektur: inverse Zeta ist nicht Mangoldt

Aus

\[
\frac{1}{\zeta_N(\beta)}
\]

folgt nicht direkt das Mangoldt-Gewicht.

Denn

\[
\frac{1}{\zeta_N(\beta)}
=
\prod_{p\le N}(1-p^{-\beta})
=
\sum_{n\in S_N}\mu_N(n)n^{-\beta}.
\]

Die Koeffizienten sind Möbius-Koeffizienten \(\mu_N(n)\), nicht Mangoldt-Koeffizienten.

Mangoldt entsteht erst auf logarithmischer Ebene:

\[
\frac{\zeta_N'}{\zeta_N}(\beta)
=
-\sum_{n\in S_N}\Lambda_N(n)n^{-\beta}.
\]

Dagegen gilt:

\[
\partial_\beta\left(\frac{1}{\zeta_N(\beta)}\right)
=
-\frac{\zeta_N'(\beta)}{\zeta_N(\beta)^2}
=
-\sum_{n\in S_N}\mu_N(n)\log(n)n^{-\beta}.
\]

Also sind drei Koeffizientensysteme zu unterscheiden:

| Funktion | Koeffizienten |
|---|---|
| \(\zeta_N^{-1}\) | \(\mu_N(n)\) |
| \(\partial_\beta(\zeta_N^{-1})\) | \(-\mu_N(n)\log n\) |
| \(\zeta_N'/\zeta_N\) | \(-\Lambda_N(n)\) |

Diese Trennung ist mathematisch zwingend.

Status: ✓ [M]

---

## 7. Konsequenz für die Jacobi-Seite

Die reine KMS-Jacobi-Reihe

\[
\mathcal J_N(z;\beta)
=
\frac{1}{\zeta_N(\beta)}
\sum_n C_N(n;z)n^{-\beta}
\]

hat Koeffizienten

\[
(C_N(\cdot;z)*\mu_N)(m)
\]

im Dirichlet-Faltungsinn.

Die gekürzte modulare Variante

\[
\mathcal J_N^{mod}(z;\beta)
=
\frac{S_N^{Jac}(z)}{\zeta_N(\beta)}
\]

hat nur Möbius-Koeffizienten:

\[
S_N^{Jac}(z)\mu_N(m).
\]

Keine dieser beiden Formeln liefert automatisch

\[
-\Lambda_N(m).
\]

Daher ist die naive Behauptung

\[
\text{KMS-Kürzung}+\text{Jacobi-Resolvent}
\Longrightarrow
\Lambda_N
\]

falsch.

Korrekt ist:

\[
\boxed{
\text{KMS-Kürzung}+\text{Jacobi-Resolvent}
\Longrightarrow
\zeta_N^{-1}\text{-Normierung plus Jacobi-Koeffizienten}.
}
\]

Status: ✓ [M]

---

## 8. Die eigentliche Mangoldt-Bedingung

Um die logarithmische Determinantenspur zu erhalten, braucht man eine verbundene/logarithmische Operation.

Definiere formal eine Jacobi-Determinante

\[
\mathcal D_N^{Jac}(z;\beta)
\]

durch

\[
\partial_z\log \mathcal D_N^{Jac}(z;\beta)
=
\mathcal J_N(z;\beta).
\]

Das löst aber nur die \(z\)-Richtung.

Für die arithmetische logarithmische Ableitung braucht man zusätzlich:

\[
\boxed{
\partial_\beta\log \mathcal D_N^{arith}(\beta)
=
\frac{\zeta_N'}{\zeta_N}(\beta).
}
\tag{38.7}
\]

Auf Koeffizientenebene bedeutet dies:

\[
\boxed{
\operatorname{Conn}
\left(
C_N(\cdot;z),\mu_N
\right)
=
-\Lambda_N(\cdot).
}
\tag{38.8}
\]

Hier bezeichnet \(\operatorname{Conn}\) den verbundenen Dirichlet-/Euler-Kumulantenanteil.

Explizit müsste aus den Jacobi-Orbitbeiträgen eine Eulerfaktorisierung folgen:

\[
\mathcal D_N^{arith}(\beta)
=
\prod_{p\le N}
(1-p^{-\beta})
\]

oder, für den inversen Faktor,

\[
-\partial_\beta\log \mathcal D_N^{arith}(\beta)
=
\sum_{p^k\in S_N}\log(p)p^{-k\beta}.
\]

Status: ❓ [O]

---

## 9. Kompatibilitätssatz von NEU-38

### Satz 38.1 — KMS-Jacobi-Kompatibilität

Da \(J_N^-\) den \(V_n\)-Sektor invariant lässt, gilt:

\[
[P_n,D_N^-]=0
\]

und daher zerfällt der Jacobi-Resolvent sektoriell. Folglich besitzt der KMS-gewichtete Jacobi-Resolvent die Dirichletform

\[
\mathcal J_N(z;\beta)
=
\frac{1}{\zeta_N(\beta)}
\sum_{n\in S_N}C_N(n;z)n^{-\beta}.
\]

Mit zusätzlichem modularen Faktor \(\Delta_\beta^{-1}\) gilt die Kürzung

\[
\mathcal J_N^{mod}(z;\beta)
=
\frac{1}{\zeta_N(\beta)}
\sum_{n\in S_N}C_N(n;z).
\]

Status: ✓ [M]

---

### Satz 38.2 — Mangoldt-Obstruktion

Aus Satz 38.1 folgt nicht

\[
\mathcal J_N(z;\beta)
=
\frac{\zeta_N'}{\zeta_N}(\beta).
\]

Vielmehr ist eine zusätzliche verbundene Euler-/Dirichlet-Kumulantenidentität nötig, die aus den Jacobi-Koeffizienten \(C_N(n;z)\) die Mangoldt-Koeffizienten \(\Lambda_N(n)\) rekonstruiert.

Status: ✓ [M] als Obstruktion, ❓ [O] als Identität.

---

## 10. Verhältnis zu NEU-28

NEU-28 bleibt korrekt:

\[
\lambda_{mod,N}(\beta)
=
\frac{C_L}{\zeta_N(\beta)}.
\]

NEU-38 zeigt aber:

\[
\lambda_{mod,N}
\]

ist die inverse-Zeta-Schicht, nicht die Mangoldt-Schicht.

Die Mangoldt-Schicht entsteht erst durch den logarithmischen Übergang:

\[
\log\det
\quad\text{oder}\quad
\partial_\beta\log.
\]

Daher muss die X.3-Kette sauber getrennt werden:

\[
\boxed{
\text{KMS-Kürzung}
\Rightarrow
\zeta^{-1}
}
\]

\[
\boxed{
\text{verbundene/logarithmische Determinante}
\Rightarrow
\zeta'/\zeta
}
\]

\[
\boxed{
\text{Gamma-Korrektur}
\Rightarrow
\xi'/\xi.
}
\]

Status: ✓ [M]

---

## 11. Reparaturpfad: verbundene \(Wres\)-Spur

Der natürliche nächste Schritt ist nicht noch eine direkte Resolventrechnung, sondern die Konstruktion der verbundenen \(Wres\)-Spur:

\[
\operatorname{Tr}_{Wres}^{conn}
\]

mit der Eigenschaft:

\[
\operatorname{Tr}_{Wres}^{conn}
\left(
\log(1-\mathcal P_N)
\right)
=
\sum_{p\le N}\log(1-p^{-\beta}).
\]

Hier sollte \(\mathcal P_N\) der BC-intrinsische Primoperator sein, dessen Potenzen die \(p^k\)-Sektoren erzeugen.

Dann wäre:

\[
-\partial_\beta
\operatorname{Tr}_{Wres}^{conn}
\left(
\log(1-\mathcal P_N)
\right)
=
\sum_{p\le N}\sum_{k\ge1}\log(p)p^{-k\beta}
=
\sum_{n\in S_N}\Lambda_N(n)n^{-\beta}.
\]

Das ist exakt das Mangoldt-Gewicht.

Status: ❓ [O], aber nun präzise formuliert.

---

## 12. Neuer Engpass

Der neue zentrale offene Punkt ist:

\[
\boxed{
\text{Existiert ein BC-intrinsischer Primoperator }\mathcal P_N
\text{ auf }B_{3,N},
}
\]

sodass:

1. seine Potenzen die Primzahlpotenz-Sektoren \(p^k\) erzeugen,
2. \(Wres_{BC}^{top}\) auf \(\log(1-\mathcal P_N)\) eine verbundene Spur liefert,
3. der Jacobi-Kopplungsteil \(J_N^-\) mit dieser Primoperator-Struktur kompatibel ist,
4. daraus die Mangoldt-Koeffizienten folgen.

Dies ist stärker und präziser als die frühere Frage:

\[
J_N^- \stackrel{?}{\Rightarrow}\Lambda_N.
\]

Status: ❓ [O]

---

## 13. Statusmatrix

| Aussage | Status |
|---|---:|
| Trennung von KMS-Parameter \(\beta\) und Resolventparameter \(z\) | ✓ [M] |
| \(J_N^-\) erhält \(V_n\)-Sektoren | ✓ [M] |
| KMS-Jacobi-Resolvent ist endliche Dirichletreihe | ✓ [M] |
| modulare Kürzung mit \(\Delta_\beta^{-1}\) funktioniert | ✓ [M] |
| NEU-28-Kompatibilität auf inverser-Zeta-Schicht | ✓ [M] |
| inverse Zeta liefert Möbius, nicht Mangoldt | ✓ [M] |
| KMS+Jacobi erzeugt Mangoldt automatisch | ✗ [M] |
| verbundene Euler-/Dirichlet-Kumulantenidentität | ❓ [O] |
| BC-intrinsischer Primoperator \(\mathcal P_N\) | ❓ [O] |
| Gamma-Faktor-Intrinsifizierung | ❓ [O] |

---

## 14. Fazit

NEU-38 beantwortet die Kompatibilitätsfrage:

\[
\boxed{
\text{Ja: KMS-Kürzung und Jacobi-Resolvent sind sektoriell kompatibel.}
}
\]

Aber:

\[
\boxed{
\text{Nein: Diese Kompatibilität erzeugt noch nicht das Mangoldt-Gewicht.}
}
\]

Der Gewinn von NEU-38 ist die scharfe Trennung der drei Ebenen:

\[
\text{KMS-Normierung}
\quad\Rightarrow\quad
\zeta^{-1},
\]

\[
\text{logarithmisch/verbundene Spur}
\quad\Rightarrow\quad
\zeta'/\zeta,
\]

\[
\text{archimedische Gamma-Korrektur}
\quad\Rightarrow\quad
\xi'/\xi.
\]

Die nächste Aufgabe ist daher:

\[
\boxed{
\text{NEU-39: Verbundene }Wres\text{-Spur und Primoperator } \mathcal P_N.
}
\]

Dort muss die Mangoldt-Schicht erzeugt werden.
