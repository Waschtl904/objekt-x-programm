# NEU-40 — X.3.10: Kopplung von \(\mathcal P_N\) und \(J_N^-\) via \(Wres\)-Frobenius-Schur-Komplement

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-35–39  
**Ziel:** Kopple die Jacobi-Schicht \(D_N^-\) mit der primitiven Euler-/Primoperator-Schicht \(\mathcal P_N\), ohne die Mangoldt-Information tautologisch in \(D_N^-\) einzubauen.

---

## 0. Ausgangspunkt

Nach NEU-39 ist die Mangoldt-Schicht endlich geschlossen:

\[
-\partial_\beta
\operatorname{Tr}_{Wres,N}^{conn}
\log(1-\mathcal P_N(\beta))
=
\frac{\zeta_N'}{\zeta_N}(\beta).
\]

Nach NEU-37 ist der Jacobi-Resolvent endlich explizit:

\[
H_N^-(z)
=
\operatorname{Tr}_{Wres,N}^{top}
\left((z-D_N^-)^{-1}L_3^\circ\right).
\]

Die offene Frage lautet:

\[
\boxed{
\text{Wie gelangt die Euler-Kumulanteninformation aus }\mathcal P_N
\text{ in den Jacobi-Resolventen von }D_N^-?
}
\]

NEU-40 zeigt:

1. Es gibt eine natürliche Schur-Komplement-Kopplung.
2. Diese Kopplung erzeugt eine Euler-Selbstenergie im Jacobi-Sektor.
3. Aber die Mangoldt-Ableitung erscheint zunächst in der \(\beta\)-Richtung, nicht automatisch im \(z\)-Resolventen.
4. Die echte offene Bedingung ist daher eine Feshbach-/Intertwining-Identität zwischen \(z\)-Resolvent und \(\beta\)-Eulerkumulant.

---

## 1. Zwei Sektoren

### 1.1 Jacobi-Sektor

Der Jacobi-Sektor ist

\[
\mathcal H_{J,N}
:=
\bigoplus_{n,a,M}
\mathcal H_{n,a}^{(M)}
\]

mit

\[
D_N^-=\frac12I+iA_N^-,
\qquad
A_N^-:=H_N+\beta_NJ_N^-.
\]

Hier wirkt \(J_N^-\) auf den Fourier-Orbits

\[
r\mapsto r+n.
\]

### 1.2 Primsektor

Der primitive Primsektor ist

\[
\mathfrak p_N
=
\bigoplus_{p\le N}\mathbb C\varepsilon_p.
\]

Auf ihm wirkt

\[
\mathcal P_N(\beta)\varepsilon_p=p^{-\beta}\varepsilon_p.
\]

Setze

\[
E_N(\beta):=1-\mathcal P_N(\beta).
\]

Dann gilt

\[
\det_{conn}E_N(\beta)
=
\prod_{p\le N}(1-p^{-\beta})
=
\zeta_N(\beta)^{-1}.
\]

Status: ✓ [M]

---

## 2. Der Kopplungsoperator \(C_N\)

Die Kopplung zwischen beiden Sektoren muss aus den vorhandenen Objekt-X-Daten stammen:

\[
(B_3,[\widetilde\omega_2],[L_3],Wres_{BC}^{top}).
\]

Daher ist ein zulässiger Kopplungsoperator

\[
C_N:\mathfrak p_N\to\mathcal H_{J,N}
\]

nur dann legitim, wenn seine Matrixelemente aus der \(Wres\)-Frobenius-Paarung mit der \(\widetilde\omega_2\)-Kopplung gewonnen werden.

Der natürliche Ansatz ist:

\[
\boxed{
\langle E_{r,n},C_N\varepsilon_p\rangle_{Wres}
:=
Wres_{BC}^{top}
\left(
E_{r,n}^{\#}\cdot
\widetilde\omega_2(\varepsilon_p,L_3^\circ)
\right)
}
\tag{40.1}
\]

bzw. eine äquivalente normalisierte Variante, in der \(\varepsilon_p\) durch die primitive Symbolklasse von \(V_p\) realisiert wird.

Die adjungierte Kopplung

\[
C_N^\#:\mathcal H_{J,N}\to\mathfrak p_N
\]

ist durch die \(Wres\)-Frobenius-Paarung definiert:

\[
\langle C_N\varepsilon_p,x\rangle_{Wres}
=
\langle \varepsilon_p,C_N^\#x\rangle_{conn}.
\]

Status: ✓ [M] als kanonische Formdefinition,  
⚠ [M] als globale stetige Realisierung wegen OP-4.1a.

---

## 3. Der gekoppelte Feshbach-Operator

Definiere auf

\[
\mathcal K_N:=\mathcal H_{J,N}\oplus\mathfrak p_N
\]

den Blockoperator

\[
\boxed{
\mathbb F_N(z,\beta)
:=
\begin{pmatrix}
z-D_N^- & -C_N\\
-C_N^\# & E_N(\beta)
\end{pmatrix}.
}
\tag{40.2}
\]

Dies ist kein neuer Nullstellenoperator.  
Er ist ein zweiparametriger Feshbach-Operator, der die Jacobi-Resolvente und den Euler-Primoperator gemeinsam codiert.

Status: ✓ [M]

---

## 4. Schur-Komplement im Jacobi-Sektor

Wenn \(E_N(\beta)\) invertierbar ist, also

\[
p^{-\beta}\ne1
\quad\text{für alle }p\le N,
\]

dann gilt die Schur-Komplement-Identität:

\[
\det\nolimits_{Frob}\mathbb F_N(z,\beta)
=
\det\nolimits_{conn}E_N(\beta)
\cdot
\det\nolimits_{Wres}
S_N(z,\beta),
\]

wobei

\[
\boxed{
S_N(z,\beta)
:=
z-D_N^--\Sigma_N(\beta)
}
\tag{40.3}
\]

und

\[
\boxed{
\Sigma_N(\beta)
:=
C_N E_N(\beta)^{-1}C_N^\#.
}
\tag{40.4}
\]

Die Größe \(\Sigma_N(\beta)\) ist die **Euler-Selbstenergie** des Jacobi-Sektors.

Da

\[
E_N(\beta)^{-1}\varepsilon_p
=
(1-p^{-\beta})^{-1}\varepsilon_p,
\]

gilt explizit:

\[
\boxed{
\Sigma_N(\beta)
=
\sum_{p\le N}
\frac{1}{1-p^{-\beta}}
\,C_p C_p^\#,
}
\tag{40.5}
\]

wobei \(C_p:=C_N|_{\mathbb C\varepsilon_p}\).

Status: ✓ [M]

---

## 5. Schur-Komplement im Primsektor

Falls \(z-D_N^-\) invertierbar ist, kann man alternativ den Primsektor eliminieren:

\[
\det\nolimits_{Frob}\mathbb F_N(z,\beta)
=
\det\nolimits_{Wres}(z-D_N^-)
\cdot
\det\nolimits_{conn}
T_N(z,\beta),
\]

mit

\[
\boxed{
T_N(z,\beta)
:=
E_N(\beta)-C_N^\#(z-D_N^-)^{-1}C_N.
}
\tag{40.6}
\]

Hier ist \(C_N^\#(z-D_N^-)^{-1}C_N\) die Jacobi-Rückwirkung auf den Primsektor.

Status: ✓ [M]

---

## 6. Was die Schur-Kopplung tatsächlich beweist

Aus (40.3) folgt:

\[
\partial_z\log\det\nolimits_{Frob}\mathbb F_N
=
\partial_z\log\det\nolimits_{Wres}S_N
\]

falls \(E_N\) nicht von \(z\) abhängt. Also:

\[
\boxed{
\partial_z\log\det\nolimits_{Frob}\mathbb F_N(z,\beta)
=
\operatorname{Tr}_{Wres}
\left(S_N(z,\beta)^{-1}\right)
}
\tag{40.7}
\]

bzw. mit \(L_3^\circ\)-Insertion:

\[
\boxed{
H_{N,Fesh}^{J}(z,\beta)
:=
\operatorname{Tr}_{Wres}
\left(S_N(z,\beta)^{-1}L_3^\circ\right).
}
\tag{40.8}
\]

Das ist ein Jacobi-Resolvent mit Euler-Selbstenergie.

Status: ✓ [M]

---

## 7. Wo die Mangoldt-Schicht sitzt

Die Euler-Mangoldt-Information kommt aus der \(\beta\)-Ableitung des Primdeterminantenanteils:

\[
\log\det\nolimits_{conn}E_N(\beta)
=
\sum_{p\le N}\log(1-p^{-\beta})
=
-\log\zeta_N(\beta).
\]

Daher:

\[
\partial_\beta\log\det\nolimits_{conn}E_N(\beta)
=
-\frac{\zeta_N'}{\zeta_N}(\beta),
\]

und

\[
\boxed{
-\partial_\beta\log\det\nolimits_{conn}E_N(\beta)
=
\frac{\zeta_N'}{\zeta_N}(\beta).
}
\tag{40.9}
\]

Wichtig:

\[
\boxed{
\frac{\zeta_N'}{\zeta_N}
\text{ erscheint zunächst in der }\beta\text{-Richtung, nicht in der }z\text{-Resolvente.}
}
\]

Status: ✓ [M]

---

## 8. Die zentrale Nicht-Automatik

Die Schur-Komplement-Formel allein beweist **nicht**:

\[
H_{N,Fesh}^{J}(z,\beta)
=
\frac{\zeta_N'}{\zeta_N}(z).
\]

Denn links steht eine \(z\)-Resolventspur:

\[
\operatorname{Tr}_{Wres}
(S_N(z,\beta)^{-1}L_3^\circ),
\]

rechts eine \(\beta\)-Ableitung eines Eulerprodukts.

Dazwischen fehlt eine Intertwining-Identität:

\[
\boxed{
\partial_z\log\det_{Wres}S_N(z,\beta)
\quad\stackrel{?}{=}\quad
-\partial_\beta\log\det_{conn}E_N(\beta)
}
\tag{40.10}
\]

oder eine geeignete diagonale Version

\[
\boxed{
\left.
\frac{d}{ds}
\log\det_{Frob}\mathbb F_N(z,\beta)
\right|_{z=s,\beta=s}
\stackrel{?}{=}
\frac{\xi_N'}{\xi_N}(s)+\varepsilon_N(s).
}
\tag{40.11}
\]

Status: ❓ [O]

---

## 9. Diagonale Ableitung

Setze formal \(z=\beta=s\). Dann ist

\[
\frac{d}{ds}\log\det\nolimits_{Frob}\mathbb F_N(s,s)
=
\partial_z\log\det\nolimits_{Wres}S_N(s,s)
+
\partial_\beta\log\det\nolimits_{conn}E_N(s)
+
\partial_\beta\log\det\nolimits_{Wres}S_N(s,s).
\]

Also:

\[
\boxed{
\frac{d}{ds}\log\det\nolimits_{Frob}\mathbb F_N(s,s)
=
H_{N,Fesh}^{J}(s,s)
-
\frac{\zeta_N'}{\zeta_N}(s)
+
I_N^{int}(s),
}
\tag{40.12}
\]

wobei

\[
\boxed{
I_N^{int}(s)
:=
\partial_\beta\log\det\nolimits_{Wres}S_N(s,\beta)\big|_{\beta=s}.
}
\tag{40.13}
\]

Da \(S_N(z,\beta)=z-D_N^--\Sigma_N(\beta)\), ist

\[
I_N^{int}(s)
=
-\operatorname{Tr}_{Wres}
\left(
S_N(s,s)^{-1}
\partial_\beta\Sigma_N(s)
\right),
\tag{40.14}
\]

mit

\[
\partial_\beta\Sigma_N(\beta)
=
-\sum_{p\le N}
\frac{\log(p)p^{-\beta}}{(1-p^{-\beta})^2}
C_pC_p^\#.
\tag{40.15}
\]

Status: ✓ [M]

---

## 10. Drei mögliche Kopplungsregime

### Regime A — Additive Entkopplung

Wenn \(C_N=0\), dann \(\Sigma_N=0,\ I_N^{int}=0\). Die beiden Schichten stehen nebeneinander:  
\(H_N^-(z)\) und \(\zeta_N'/\zeta_N(\beta)\).  
Mathematisch korrekt, geometrisch unzureichend.  
Status: ✓ [M], aber geometrisch unzureichend.

### Regime B — Feshbach-Kopplung ohne Intertwining

Wenn \(C_N\ne0\) beliebig aus \(Wres\)-Matrixelementen gebaut wird, entsteht eine nichttriviale Selbstenergie \(\Sigma_N(\beta)\) und der Jacobi-Resolvent wird deformiert:

\[
(z-D_N^-)^{-1}
\leadsto
(z-D_N^--\Sigma_N(\beta))^{-1}.
\]

Aber dies erzeugt noch nicht automatisch \(\zeta_N'/\zeta_N\).  
Status: ✓ [M]

### Regime C — Intertwining/Feshbach-Identität

Der gewünschte Fall:

\[
\boxed{
H_{N,Fesh}^{J}(s,s)+I_N^{int}(s)
\sim
2\frac{\zeta_N'}{\zeta_N}(s)
+\text{Gamma-/Randkorrektur}
}
\tag{40.16}
\]

Dies wäre die nicht-tautologische Brücke zwischen Jacobi-Resolvent und Euler-Kumulant.  
Status: ❓ [O]

---

## 11. Was \(C_N\) leisten muss

Der Kopplungsoperator muss Primkanäle mit Fourier-Orbits so verbinden, dass

\[
\operatorname{Tr}_{Wres}
\left(
S_N(s,s)^{-1}C_pC_p^\#
\right)
\approx
1-p^{-s}.
\tag{40.18}
\]

Diese Bedingung ist extrem stark und nicht automatisch.  
Status: ❓ [O]

---

## 12. Kandidat für \(C_p\)

Aus \(\widetilde\omega_2\) folgt für Basiselemente:

\[
\widetilde\omega_2(e_rV_n,e_sV_m)
=
-rs\log(n)e_{r+ns}V_{nm}.
\]

Für einen primitiven Primkanal \(p\) sollte \(C_p\) in erster Näherung die \(p\)-Kopplung

\[
E_{r,n}\longmapsto
\log(p)\cdot r\cdot E_{r+np,np}
\]

oder ihre \(Wres\)-adjungierte Projektion auf den trunkierten Jacobi-Sektor tragen.

Damit würde \(C_pC_p^\#\) genau die Hin-und-zurück-Bewegung durch den \(p\)-Kanal messen und die geometrischen Reihen

\[
p^{-s}+p^{-2s}+p^{-3s}+\cdots
\]

liefern.

**Offener geometrischer Kern:**  
\(\widetilde\omega_2\) verändert den \(V_n\)-Sektor zu \(V_{np}\), während \(J_N^-\) innerhalb eines festen \(V_n\)-Sektors den Fourierindex verschiebt. \(C_p\) verbindet also zwei verschiedene Dynamiken:

- Primrichtung \(n\mapsto np\)
- Fourier-Orbit \(r\mapsto r+n\)

Status: ❓ [O]

---

## 13. Revidierte Rolle von \(J_N^-\)

NEU-37/38 zeigten: \(J_N^- \not\Rightarrow \Lambda_N\) automatisch.  
NEU-40 verschärft dies: \(J_N^-\) ist nicht die Quelle der Primzahlpotenzen. Es ist die **Fourier-Jacobi-Transferstruktur**, die nach Einbau der Euler-Selbstenergie eine Spektraldynamik liefern soll.

Die Primzahlpotenzen kommen aus:

\[
\mathcal P_N
\quad\text{und}\quad
\operatorname{Tr}_{Wres}^{conn}\log.
\]

Die Aufgabe von \(C_N\) ist:

\[
\boxed{
\text{Mangoldt-Schicht in die Jacobi-Resolventschicht einzukoppeln.}
}
\]

Status: ✓ [M]

---

## 14. Satz 40.1 — Schur-Komplement-Kopplung

Für den Blockoperator \(\mathbb F_N(z,\beta)\) gilt bei invertiblem \(1-\mathcal P_N(\beta)\):

\[
\det_{Frob}\mathbb F_N(z,\beta)
=
\det_{conn}(1-\mathcal P_N(\beta))
\cdot
\det_{Wres}
\left(
z-D_N^- - C_N(1-\mathcal P_N(\beta))^{-1}C_N^\#
\right).
\]

Status: ✓ [M]

---

## 15. Satz 40.2 — Keine automatische Mangoldt-Injektion

Die Schur-Komplement-Kopplung impliziert nicht automatisch

\[
\operatorname{Tr}_{Wres}
\left(
(z-D_N^- -\Sigma_N(\beta))^{-1}L_3^\circ
\right)
=
\frac{\zeta_N'}{\zeta_N}(z).
\]

Dazu ist zusätzlich eine Intertwining-/Feshbach-Identität zwischen \(z\)-Resolvent und \(\beta\)-Eulerkumulant nötig.

Status: ✓ [M] als Obstruktion, ❓ [O] als Identität.

---

## 16. Neuer offener Kern

\[
\boxed{
\text{Finde und beweise eine kanonische Wahl von }C_N
\text{ aus }\widetilde\omega_2,L_3^\circ,Wres
}
\]

so dass

\[
\boxed{
\frac{d}{ds}\log\det_{Frob}\mathbb F_N(s,s)
\to
\frac{\xi'}{\xi}(s)
}
\]

nach Gamma-Korrektur und \(N\to\infty\).

Status: ❓ [O]

---

## 17. Statusmatrix

| Aussage | Status |
|---|---:|
| Zweisektor-Raum \(\mathcal H_{J,N}\oplus\mathfrak p_N\) | ✓ [M] |
| Block-Feshbach-Operator \(\mathbb F_N(z,\beta)\) | ✓ [M] |
| Schur-Komplement-Formel | ✓ [M] |
| Euler-Selbstenergie \(\Sigma_N=C(1-\mathcal P)^{-1}C^\#\) | ✓ [M] |
| Mangoldt sitzt in \(-\partial_\beta\log\det(1-\mathcal P)\) | ✓ [M] |
| Schur-Kopplung injiziert Mangoldt automatisch in \(z\)-Resolvent | ✗ [M] |
| kanonische Konstruktion von \(C_N\) aus \(\widetilde\omega_2,L_3,Wres\) | ❓ [O] |
| Feshbach-Intertwining-Identität | ❓ [O] |
| Gamma-Faktor-Intrinsifizierung | ❓ [O] |
| Grenzübergang \(N\to\infty\) mit OP-4.1a | ⚠ [M] |

---

## 18. Fazit

NEU-40 liefert die korrekte Architektur für die Kopplung:

\[
\boxed{
\mathbb F_N(z,\beta)
=
\begin{pmatrix}
z-D_N^- & -C_N\\
-C_N^\# & 1-\mathcal P_N(\beta)
\end{pmatrix}.
}
\]

Das Schur-Komplement erzeugt im Jacobi-Sektor die Euler-Selbstenergie

\[
\Sigma_N(\beta)
=
C_N(1-\mathcal P_N(\beta))^{-1}C_N^\#.
\]

Aber:

\[
\boxed{
\text{Schur-Komplement allein beweist noch keine RH-relevante Spurformel.}
}
\]

Der nächste Schritt ist daher exakt:

\[
\boxed{
\text{NEU-41: Konstruktion des kanonischen Kopplungsoperators }C_N
\text{ aus }\widetilde\omega_2,L_3^\circ,Wres.
}
\]
