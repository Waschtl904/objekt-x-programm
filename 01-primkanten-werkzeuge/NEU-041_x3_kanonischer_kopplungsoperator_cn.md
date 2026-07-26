# NEU-41 — X.3.11: Kanonischer Kopplungsoperator \(C_N\) aus \(\widetilde\omega_2,L_3^\circ,Wres\)

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-35–40  
**Ziel:** Prüfe, ob der Feshbach-Kopplungsoperator

\[
C_N:\mathfrak p_N\longrightarrow \mathcal H_{J,N}
\]

kanonisch aus

\[
(B_3,[\widetilde\omega_2],[L_3],Wres_{BC}^{top})
\]

gewonnen werden kann, und ob er die Zielbedingung aus NEU-40,

\[
\operatorname{Tr}_{Wres}
\left(
S_N(s,s)^{-1}C_pC_p^\#
\right)
\approx
1-p^{-s},
\tag{41.0}
\]

erfüllen kann.

---

## 0. Ergebnisübersicht

NEU-41 liefert eine scharfe Diagnose.

1. **Der naive Kopplungsansatz ist nicht automatisch nichttrivial.**  
   Wird \(\varepsilon_p\) als ungechargter Monoidkanal \(V_p\) realisiert, dann verschwindet
   \(\widetilde\omega_2(\varepsilon_p,L_3^\circ)\) wegen des Fourierfaktors.

2. **Ein nichttriviales \(C_p\) braucht eine Fourier-geladene primitive Hebung**
   \(\widehat\varepsilon_p\in B_3\).

3. **Für endliche Jacobi-Trunkierungen ist die Feshbach-Zielgröße rational in \(s\).**
   Daher kann sie die exponentielle Funktion \(1-p^{-s}=1-e^{-s\log p}\) nicht exakt reproduzieren.

4. **Die korrekte Zielbedingung ist asymptotisch:**

\[
\operatorname{Tr}_{Wres}
\left(
S_N(s,s)^{-1}C_pC_p^\#
\right)
\longrightarrow
1-p^{-s}
\]

lokal gleichmäßig nach wachsender Fourier-/Jacobi-Trunkierung.

\[
\boxed{
\text{Exakte endliche Kopplung ist unmöglich; nötig ist eine asymptotische Padé-/Laplace-Realisierung.}
}
\]

---

## 1. Erinnerung: die \(\widetilde\omega_2\)-Formel

Für Basiselemente gilt

\[
\boxed{
\widetilde\omega_2(e_rV_n,e_sV_m)
=
-rs\log(n)\,e_{r+ns}V_{nm}.
}
\tag{41.1}
\]

Insbesondere gilt:

\[
r=0
\quad\text{oder}\quad
s=0
\quad\Longrightarrow\quad
\widetilde\omega_2(e_rV_n,e_sV_m)=0.
\tag{41.2}
\]

Status: ✓ [M]

---

## 2. Der naive Primkanal verschwindet

Wird \(\varepsilon_p = V_p = e_0V_p\) realisiert, dann ist \(r=0\) in (41.1), also:

\[
\boxed{
\widetilde\omega_2(V_p,L_3^\circ)=0
}
\tag{41.3}
\]

für jeden Term von \(L_3^\circ\). Damit \(C_p=0,\ \Sigma_N=0\): keine Feshbach-Kopplung.

\[
\boxed{
\text{Der primitive Primkanal muss Fourier-geladen gehoben werden.}
}
\]

Status: ✓ [M]

---

## 3. Fourier-geladene primitive Hebungen

Eine zulässige Hebung des primitiven Primkanals ist ein Element

\[
\widehat\varepsilon_p\in B_3
\]

mit:

1. \(\pi_{prim}(\widehat\varepsilon_p)=\varepsilon_p\)
2. Nichtverschwindende Fourierladung: \(\widehat\varepsilon_p = \sum_{u\ne0}a_{p,u}e_uV_p + \cdots\)
3. \(Wres\)-Normalisierung: \(\operatorname{Tr}_{Wres}^{conn}(\widehat\varepsilon_p^\#\widehat\varepsilon_p)=1\)
4. Wohlbestimmtheitsbedingung:

\[
\boxed{
\widehat\varepsilon_p\sim\widehat\varepsilon_p'
\quad\Longrightarrow\quad
C_pC_p^\#=C_p'C_p'^\#
\text{ im }Wres\text{-Quotienten.}
}
\tag{41.4}
\]

Status: ❓ [O]

---

## 4. Definition des Kandidaten \(C_p\)

Sei \(L_3^\circ=\sum_{s,m}\ell_{s,m}e_sV_m\). Die Vor-Kopplung ist

\[
\psi_p
:=
\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)
=
-\sum_{u\ne0}\sum_{s,m}
a_{p,u}\ell_{s,m}\,u\,s\,\log(p)\,
e_{u+ps}V_{pm}.
\tag{41.6}
\]

Projektion auf den Jacobi-Sektor: \(\Psi_p:=\Pi_{J,N}\psi_p\in\mathcal H_{J,N}\).

\[
\boxed{
C_p:\mathbb C\varepsilon_p\to\mathcal H_{J,N},
\qquad
C_p\varepsilon_p=\Psi_p.
}
\tag{41.7}
\]

\[
\boxed{
C_N=\bigoplus_{p\le N}C_p.
}
\tag{41.8}
\]

Status: ✓ [M] als kanonischer Kandidat relativ zur Hebung, ❓ [O] für Hebungsunabhängigkeit.

---

## 5. \(Wres\)-Adjungierte und Rang-eins-Form

\[
\boxed{
C_pC_p^\#x
=
\Psi_p\langle \Psi_p,x\rangle_{Wres}.
}
\tag{41.9}
\]

\(C_pC_p^\#\) ist der Rang-eins-Projektor auf den \(Wres\)-zyklischen Vektor \(\Psi_p\).

Status: ✓ [M] auf dem quotientierten nichtausgearteten Sektor.

---

## 6. Feshbach-Weyl-Funktion des Primkanals

\[
\boxed{
M_p(s)
:=
\operatorname{Tr}_{Wres}
\left(
S_N(s,s)^{-1}C_pC_p^\#
\right)
=
\langle \Psi_p,S_N(s,s)^{-1}\Psi_p\rangle_{Wres}.
}
\tag{41.10}
\]

Die NEU-40-Bedingung lautet:

\[
\boxed{
M_p(s)\stackrel{?}{\approx}1-p^{-s}.
}
\tag{41.11}
\]

Status: ✓ [M] als Reduktion.

---

## 7. Endliches No-Go: Rationalität vs. Exponentialfunktion

Für endliche Jacobi-Trunkierung ist \(M_p^{raw}(s) = \langle\Psi_p,(s-D_N^-)^{-1}\Psi_p\rangle\) rational in \(s\). Aber

\[
1-p^{-s}=1-e^{-s\log p}
\]

ist keine rationale Funktion. Daher:

\[
\boxed{
M_p^{raw}(s)=1-p^{-s}
\text{ kann für endliche Jacobi-Trunkierung keine holomorphe Identität sein.}
}
\tag{41.12}
\]

Auch mit endlicher Euler-Selbstenergie \(\Sigma_N(s) = \sum_{q\le N} C_qC_q^\#/(1-q^{-s})\) bleibt \(M_p(s)\) rational in \(s\) und \(\{q^{-s}:q\le N\}\).

Status: ✓ [M]

---

## 8. Korrektur der Zielbedingung (40.18)

Die korrekte asymptotische Form:

\[
\boxed{
M_{p,N,M}(s)
\longrightarrow
1-p^{-s}
}
\tag{41.13}
\]

lokal gleichmäßig, \(M\to\infty\) (Fourier-/Jacobi-Orbitlänge). Alternativ als Padé-Approximation:

\[
\boxed{
M_{p,N,M}(s)
=
[1-p^{-s}]_{\text{Padé},M}
+
o_M(1).
}
\tag{41.14}
\]

Status: ✓ [M] als notwendige Korrektur, ❓ [O] als Beweisziel.

---

## 9. Laplace-Realisierung des Exponentialterms

Eine natürliche Brücke: Wenn die Jacobi-Spektralmaße des zyklischen Vektors \(\Psi_p\) im Grenzwert gegen \(\delta_{\log p}\) konvergieren,

\[
\mu_{\Psi_p}^{(M)}
\Longrightarrow
\delta_{\log p},
\]

dann

\[
M_{p,M}(s)
\sim
\int\frac{d\mu_{\Psi_p}^{(M)}(\lambda)}{s-\lambda}
\longrightarrow
\frac{1}{s-\log p},
\]

und nach Borel-/Laplace-Transformation könnte \(e^{-s\log p} = p^{-s}\) entstehen.

\[
\boxed{
\text{Jacobi-Weyl-Funktion}
\longrightarrow
\text{Borel-Transform}
\longrightarrow
p^{-s}.
}
\]

Status: ❓ [O]

---

## 10. Kompatibilität: Primrichtung vs. Fourier-Orbit

| Dynamik | Wirkung |
|---|---|
| \(\widetilde\omega_2\)-Primkopplung | \(m\mapsto pm\) |
| \(J_N^-\)-Fourierorbit | \(r\mapsto r+n\) |

\(C_p\) ist genau der Übergang zwischen diesen Dynamiken.

Status: ✓ [M]

---

## 11. Selektionsregel für Matrixelemente

Ein Matrixelement \(\langle E_{r,n},C_p\varepsilon_p\rangle_{Wres}\) kann nur nicht verschwinden, wenn der \(Wres\)-Residuumskanal den Term \(e_{u+ps}V_{pm}\) mit \(E_{r,n}^\#\) paart:

\[
\boxed{
(r,n)\sim_{Wres}(u+ps,pm).
}
\tag{41.15}
\]

Status: ✓ [M] als Selektionsprinzip, ⚠ [M] für exakte Topologie.

---

## 12. Minimaler nichttrivialer Testfall

Nehme \(\widehat\varepsilon_p=e_uV_p,\ u\ne0\) und \(L_3^\circ=\ell_{s,m}e_sV_m,\ s\ne0\). Dann:

\[
\Psi_p
=
-u\,s\,\log(p)\,\ell_{s,m}
\Pi_{J,N}(e_{u+ps}V_{pm})
=:
\kappa_{p,u,s,m}E_{r,pm}.
\]

Mit NEU-37:

\[
M_p(s)
=
|\kappa_{p,u,s,m}|_{Wres}^2
\frac{
P_j^L(z_{pm}(s))P_{M-j}^R(z_{pm}(s))
}{
P_{M+1}^{(pm,a)}(z_{pm}(s))
}.
\tag{41.16}
\]

Dies ist explizit berechenbar; \(M_p(s) \approx 1-p^{-s}\) ist eine Approximationseigenschaft der Kontinuanten.

Status: ✓ [M]

---

## 13. Sätze

### Satz 41.1 — Kanonischer Kopplungskandidat

Nach Wahl einer Fourier-geladenen primitiven Hebung \(\widehat\varepsilon_p\) ist

\[
C_p\varepsilon_p = \Pi_{J,N}\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)
\]

der natürliche \(Wres\)-Frobenius-Kopplungskandidat.  
Status: ✓ [M] relativ zur Hebung.

### Satz 41.2 — Verschwindungsobstruktion

Für \(\widehat\varepsilon_p=V_p\) gilt \(C_p=0\). Jede nichttriviale Kopplung braucht Fourierladung.  
Status: ✓ [M]

### Satz 41.3 — Endliche Exponential-Obstruktion

Für endliche Jacobi-Trunkierungen ist \(\langle\Psi_p,(s-D_N^-)^{-1}\Psi_p\rangle\) rational in \(s\). Die Identität \(M_p(s)=1-p^{-s}\) kann nicht exakt auf einem Gebiet gelten.  
Status: ✓ [M]

---

## 14. Statusmatrix

| Aussage | Status |
|---|---:|
| Naive ungechargte Hebung \(V_p\) gibt \(C_p=0\) | ✓ [M] |
| Fourier-geladene Hebung notwendig | ✓ [M] |
| Kandidat \(C_p=\Pi_J\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)\) | ✓ [M] relativ zur Hebung |
| \(C_pC_p^\#\) zyklischer Rang-eins-Kanal | ✓ [M] |
| Zielgröße ist Weyl-Funktion \(M_p(s)\) | ✓ [M] |
| Exakte endliche Identität \(M_p=1-p^{-s}\) | ✗ [M] |
| Asymptotische Jacobi-/Padé-Realisierung | ❓ [O] |
| Hebungsunabhängigkeit im \(Wres\)-Quotienten | ❓ [O] |
| Exakte \(Wres\)-Selektionsregel | ⚠ [M] |
| Gamma-Faktor-Intrinsifizierung | ❓ [O] |

---

## 15. Fazit

\[
\boxed{
C_p\varepsilon_p
=
\Pi_{J,N}\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ).
}
\]

Zwei entscheidende Grenzen:

1. Ohne Fourierladung verschwindet \(C_p\).
2. Endlich kann \(C_p\) die Funktion \(1-p^{-s}\) nicht exakt erzeugen.

Neuer Kern des Programms:

\[
\boxed{
\text{Fourier-geladene Primhebung}
+
\text{Jacobi-Grenzapproximation}
\Longrightarrow
1-p^{-s}.
}
\]

\[
\boxed{
\text{NEU-42: Fourier-geladene Primhebung und Padé-/Laplace-Realisierung von }p^{-s}.
}
\]
