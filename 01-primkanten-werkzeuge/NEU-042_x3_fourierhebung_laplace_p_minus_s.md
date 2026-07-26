# NEU-42 — X.3.12: Fourier-geladene Primhebung und Padé-/Laplace-Realisierung von \(p^{-s}\)

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-39–41  
**Ziel:** Prüfe, ob die aus \(\widetilde\omega_2,L_3^\circ,Wres\) konstruierte Primkopplung \(C_p\) eine Jacobi-/Laplace-Realisierung des Faktors \(p^{-s}=e^{-s\log p}\) erzwingen kann.

---

## 0. Kernkorrektur

NEU-41 hatte die Zielbedingung

\[
M_{p,M}(s):=\langle\Psi_p,S_N(s,s)^{-1}\Psi_p\rangle_{Wres}\stackrel{?}{\longrightarrow}1-p^{-s}.
\]

NEU-42 zeigt: Diese Zielbedingung ist semantisch falsch.

\[
\boxed{
\text{Jacobi-Resolvent-Konvergenz zu }\delta_{\log p}\text{ liefert }(z-\log p)^{-1},\text{ nicht }p^{-s}.
}
\]

Der Exponentialfaktor kommt erst durch den Laplace-/Wärme-Funktionalkalkül.

Status: ✓ [M]

---

## 1. Drei verschiedene Funktionen

### 1.1 Cauchy-/Resolventtransformierte

\[
G_\mu(z)=\int\frac{d\mu(t)}{z-t}\quad\xrightarrow{\mu=\delta_{\log p}}\quad\frac1{z-\log p}.
\]

### 1.2 Laplace-Transformierte

\[
L_\mu(s)=\int e^{-st}\,d\mu(t)\quad\xrightarrow{\mu=\delta_{\log p}}\quad e^{-s\log p}=p^{-s}.
\]

### 1.3 Borel-/Funktionskalkülbrücke

\[
e^{-sT}=\frac{1}{2\pi i}\int_\Gamma e^{-sz}(z-T)^{-1}\,dz.
\]

\[
\boxed{
\text{Resolvent}\Rightarrow\text{Laplace}
}
\]

nur nach zusätzlichem Cauchy-/Borel-Funktionalkalkül, nicht direkt.

Status: ✓ [M]

---

## 2. Korrigierte Zielbedingungen

### 2.1 Resolvent-Ziel

\[
\boxed{
\langle\Psi_p^{(M)},(z-T_{p,M})^{-1}\Psi_p^{(M)}\rangle
\longrightarrow\frac{1}{z-\log p}.
}\tag{42.1}
\]

Äquivalent: \(\mu_{\Psi_p}^{(M)}\Rightarrow\delta_{\log p}\). \tag{42.2}

### 2.2 Laplace-Ziel

\[
\boxed{
\langle\Psi_p^{(M)},e^{-sT_{p,M}}\Psi_p^{(M)}\rangle
\longrightarrow p^{-s}.
}\tag{42.3}
\]

Erst (42.3) ist die arithmetische Exponentialschicht.

Status: ✓ [M]

---

## 3. Momentenkriterium

\[
\boxed{
\langle\Psi_p^{(M)},T_{p,M}^k\Psi_p^{(M)}\rangle\longrightarrow(\log p)^k.
}\tag{42.4}
\]

Für \(k=1,2\) speziell:

\[
\langle T_{p,M}\rangle\to\log p,
\qquad
\operatorname{Var}_{\Psi_p^{(M)}}(T_{p,M})\to0.
\]

Status: ✓ [M] im positiven GNS-Fall, ⚠ [M] im indefiniten \(Wres\)-Fall.

---

## 4. Tautologieproblem des KMS-Clocks

\[
T_{\log}E_{r,n}=\log(n)E_{r,n}
\quad\Rightarrow\quad
\langle\varepsilon_p,e^{-sT_{\log}}\varepsilon_p\rangle=p^{-s}.
\]

\[
\boxed{
T_{\log}\text{ realisiert }p^{-s}\text{ korrekt, aber tautologisch auf der KMS-Schicht.}
}
\]

Status: ✓ [M]

---

## 5. Was die Jacobi-Schicht leisten müsste

Nicht-tautologischer Wunsch:
\[
T_{p,M}^{Jac}=\log p\cdot I+R_{p,M},
\qquad
\langle\Psi_p,R_{p,M}^k\Psi_p\rangle\to0\text{ für alle }k\ge1.
\]

Status: ❓ [O]

---

## 6. Test am rohen Jacobi-Operator

NEU-37: \(A_N^-E_j=h(n)E_j+b_jE_{j+1}-b_{j-1}E_{j-1}\) mit \(b_j=(\beta_N\gamma_N/2)(a+jn)\log n\).

Der durch \(C_p\) erzeugte Vektor \(\Psi_p\) liegt im \(V_{pm}\)-Sektor. Mit \(h(n)=\log n\) ist

\[
h(pm)=\log p+\log m,
\]

nicht automatisch \(\log p\). Daher muss entweder \(L_3^\circ\) auf \(m=1\) projizieren, oder relativ normalisiert werden.

Status: ✓ [M]

---

## 7. Relativer logarithmischer Clock (positiver Befund)

\[
\boxed{
\Delta_p h(m):=h(pm)-h(m)=\log p.
}\tag{42.5}
\]

Formal auf dem \(V_m\to V_{pm}\)-Kanal:

\[
T_p^{rel}E_{r,pm}=(\log(pm)-\log m)E_{r,pm}=\log p\,E_{r,pm}.
\]

\[
\boxed{
e^{-sT_p^{rel}}=p^{-s}\text{ auf dem reinen }p\text{-Kopplungskanal.}
}
\]

\[
\boxed{
p^{-s}\text{ entsteht kanonisch als relativer modularer Log-Zuwachs }n\mapsto pn.
}
\]

Status: ✓ [M] formal, ❓ [O] für Realisierung auf dem vollständigen \(Wres\)-Jacobi-Quotienten.

---

## 8. Präzisierte Aufgabe der Fourier-geladenen Hebung

Die Fourier-geladene Hebung \(\widehat\varepsilon_p\) muss **nicht** selbst \(\log p\) erzeugen. Ihre Aufgabe:

1. Verhindern des \(\widetilde\omega_2\)-Verschwindens.
2. Wahl eines zyklischen Vektors \(\Psi_p\) im relativen \(p\)-Kopplungskanal.

Status: ✓ [M]

---

## 9. Revidierte Delta-Bedingung

\[
\boxed{
\mu_{\Psi_p}^{(M)}(T_p^{rel})\Rightarrow\delta_{\log p}.
}\tag{42.6}
\]

Reduziert sich auf Reinheit:

\[
\boxed{\Pi_{rel,p}\Psi_p\approx\Psi_p}\tag{42.7}
\]

im \(Wres\)-GNS-Sinn.

---

## 10. Minimaler Reinheitstest (✓ [M])

Für \(\widehat\varepsilon_p=e_uV_p,\ u\ne0\) und \(L_3^\circ=\ell_{s,m}e_sV_m,\ s\ne0\):

\[
\Psi_p=-us\log(p)\ell_{s,m}\Pi_{J,N}(e_{u+ps}V_{pm})\in V_{pm}\text{-Sektor}.
\]

Mit \(T_p^{rel}\) wirkt:

\[
T_p^{rel}\Psi_p=\log p\,\Psi_p.
\]

\[
\boxed{
\frac{\langle\Psi_p,e^{-sT_p^{rel}}\Psi_p\rangle}{\|\Psi_p\|_{Wres}^2}=p^{-s}.
}\tag{42.8}
\]

Status: ✓ [M] im reinen Einzelkanal.

---

## 11. Padé ist sekundär

\[
\boxed{
\text{Padé ist nur nötig, wenn man }p^{-s}\text{ direkt aus dem Jacobi-Resolventen erzwingen will.}
}
\]

Der natürliche BC-Weg: relative Monoid-Clock \(\Rightarrow e^{-sT_p^{rel}}=p^{-s}\).

Status: ✓ [M]

---

## 12. Drei-Operator-Architektur

| Operator | Wirkung |
|---|---|
| \(J_N^-\) | Fourier-Transfer innerhalb \(V_n\) |
| \(T_p^{rel}\) | Primzuwachs \(V_m\to V_{pm}\) |
| \(C_p\) | Brücke zwischen beiden |

Status: ✓ [M]

---

## 13. Revidierte Feshbach-Selbstenergie

\[
\Sigma_N(\beta)=\sum_{p\le N}\frac{C_pC_p^\#}{1-p^{-\beta}}
=\sum_{p\le N}\sum_{k\ge0}C_p e^{-\beta kT_p^{rel}}C_p^\#.
\]

Unterscheidung:
- \((1-\mathcal P)^{-1}\): geometrische Wiederkehrgewichte
- \(\log(1-\mathcal P)\): Euler-Kumulanten/Mangoldt

\[
\boxed{
-\partial_\beta\log(1-\mathcal P_p)\Rightarrow\frac{\log(p)p^{-\beta}}{1-p^{-\beta}}.
}
\]

Status: ✓ [M]

---

## 14. Sätze

### Satz 42.1 — Resolvent/Laplace-Trennung

Bei \(\mu_{\Psi_p}^{(M)}\Rightarrow\delta_{\log p}\):

\[
\langle\Psi_p^{(M)},(z-T_{p,M})^{-1}\Psi_p^{(M)}\rangle\to\frac1{z-\log p},
\quad
\langle\Psi_p^{(M)},e^{-sT_{p,M}}\Psi_p^{(M)}\rangle\to p^{-s}.
\]

Der zweite Schluss ist ein Laplace-/Funktionalkalkül-Schluss.  
Status: ✓ [M]

### Satz 42.2 — Relativer Primclock

Auf reinem \(V_m\to V_{pm}\)-Kanal: \(T_p^{rel}=\log p\). Daher \(e^{-sT_p^{rel}}=p^{-s}\).  
Status: ✓ [M]

### Satz 42.3 — Nichttautologische Rolle der Fourierhebung

\(\widehat\varepsilon_p\) erzeugt nicht \(\log p\), sondern den nichtverschwindenden zyklischen Vektor \(\Psi_p\) auf dem relativen \(p\)-Kanal.  
Status: ✓ [M]

---

## 15. Neuer offener Kern

\[
\boxed{
\Pi_{rel,p}\Psi_p=\Psi_p\quad\text{im }Wres\text{-GNS-Quotienten.}
}\tag{42.9}
\]

oder asymptotisch:

\[
\boxed{
\|\Psi_p-\Pi_{rel,p}\Psi_p\|_{Wres,GNS}\to0.
}\tag{42.10}
\]

Status: ❓ [O]

---

## 16. Statusmatrix

| Aussage | Status |
|---|---:|
| Resolventmaß \(\delta_{\log p}\) liefert \((z-\log p)^{-1}\), nicht \(p^{-s}\) | ✓ [M] |
| Laplace-/Wärmefunktionalkalkül liefert \(p^{-s}\) | ✓ [M] |
| Momentenkriterium für \(\mu\Rightarrow\delta_{\log p}\) | ✓ [M] / ⚠ indefinit |
| Relative Clock \(T_p^{rel}=\log(pm)-\log m=\log p\) | ✓ [M] |
| Reiner Einzelkanal liefert \(p^{-s}\) exakt nach Normierung | ✓ [M] |
| Padé ist sekundär | ✓ [M] |
| \(T_{\log}\) tautologisch auf KMS-Schicht | ✓ [M] |
| Reinheit \(\Pi_{rel,p}\Psi_p=\Psi_p\) im \(Wres\)-GNS | ❓ [O] → NEU-43 |
| Kanonische Fourierhebung im \(Wres\)-Quotienten | ❓ [O] → NEU-43 |
| Kopplung an vollständigen Feshbach-Determinanten | ❓ [O] |
| Gamma-Faktor-Intrinsifizierung | ❓ [O] |

---

## 17. Fazit

Der Faktor \(p^{-s}\) soll nicht direkt aus einer Jacobi-Weyl-Funktion erzwungen werden.
Er entsteht durch den relativen Primclock \(T_p^{rel}=\log p\) und den Laplace-Funktionalkalkül.

\[
\boxed{
\widehat\varepsilon_p\text{ muss einen nichtverschwindenden, reinen relativen }p\text{-Kanalvektor }\Psi_p\text{ erzeugen.}
}
\]

\[
\boxed{
\text{NEU-43: Reinheitslemma für }\Psi_p=\Pi_J\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)\text{ im relativen Primclock-Kanal.}
}
\]
