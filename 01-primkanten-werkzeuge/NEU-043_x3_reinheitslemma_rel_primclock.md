# NEU-43 — X.3.13: Reinheitslemma für \(\Psi_p\) im relativen Primclock-Kanal

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-40–42  
**Ziel:** Prüfe die Reinheitsbedingung \(\Pi_{rel,p}\Psi_p=\Psi_p\) für \(\Psi_p=\Pi_J\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)\) im relativen Primclock-Kanal.

---

## 0. Kernresultat

NEU-43 zeigt:

1. Im **graph-erweiterten Korrespondenzraum** ist \(\widetilde\Psi_p\) automatisch relativ \(p\)-rein. ✓ [M]
2. Im **kollabierten Jacobi-Zielraum** ist Reinheit nicht automatisch: Derselbe Zielsektor \(V_n\) kann mehrere Primkanten besitzen (\(n=pm=qm'\)). ✗ [M]
3. Die exakte kollabierte Reinheit ist äquivalent zur \(Wres\)-Kantendiagonalität. ❓ [O]

---

## 1. Lokale Formel

\[
\widetilde\omega_2(e_uV_p,e_sV_m)=-us\log(p)\,e_{u+ps}V_{pm}.\tag{43.1}
\]

Jeder Summand trägt die relative Primkante \(m\xrightarrow{p}pm\). ✓ [M]

---

## 2. Fourier-geladene Primhebung

\[
\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)
=-\sum_{u\ne0}\sum_{s,m}a_{p,u}\ell_{s,m}\,u\,s\,\log(p)\,e_{u+ps}V_{pm}.\tag{43.2}
\]

Jeder Summand liegt in der Kante \(m\xrightarrow{p}pm\). ✓ [M]

---

## 3. Graph-erweiterter relativer Korrespondenzraum

\[
\boxed{
\mathcal H_{rel,N}:=\bigoplus_{p\le N}\bigoplus_{m\in S_N}\mathcal H_{m\xrightarrow{p}pm}.
}\tag{43.3}
\]

Basisvektor: \(E_{r;m\xrightarrow{p}pm}\).  
Kollapsabbildung \(\kappa:\mathcal H_{rel,N}\to\mathcal H_{J,N},\ E_{r;m\xrightarrow{p}pm}\mapsto E_{r,pm}\). ✓ [M]

---

## 4. Graph-reine Version \(\widetilde\Psi_p\)

\[
\boxed{
\widetilde\Psi_p:=\Pi_{rel,J}\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)
\in\bigoplus_m\mathcal H_{m\xrightarrow{p}pm}.
}\tag{43.5}
\]

\[
\boxed{\Pi_{rel,p}\widetilde\Psi_p=\widetilde\Psi_p.}\tag{43.7}
\]

Status: ✓ [M]

---

## 5. Relativer Primclock auf dem Graphraum

\[
T_{rel}E_{r;m\xrightarrow{p}pm}=\log(p)E_{r;m\xrightarrow{p}pm}.\tag{43.8}
\]

\[
e^{-sT_{rel}}\widetilde\Psi_p=p^{-s}\widetilde\Psi_p.\tag{43.9}
\]

\[
\boxed{
\frac{\langle\widetilde\Psi_p,e^{-sT_{rel}}\widetilde\Psi_p\rangle_{Wres,rel}}{\|\widetilde\Psi_p\|_{Wres,rel}^2}=p^{-s}.
}\tag{43.10}
\]

Status: ✓ [M] auf dem graph-erweiterten Raum.

---

## 6. Nichtverschwindungsbedingung

Hinreichend: \(\exists\, u\ne0,\, s\ne0,\, m\in S_N\) mit \(a_{p,u}\ell_{s,m}\ne0\) und \(\Pi_{rel,J}E_{u+ps;m\xrightarrow{p}pm}\ne0\) im \(Wres\)-GNS-Quotienten.

Status: ✓ [M] als Kriterium, ⚠ [M] für konkrete \(Wres\)-Auswertung.

---

## 7. pq-Kollision

Für \(n=pq\) kollabieren zwei verschiedene Primkanten in \(V_{pq}\):

\[
q\xrightarrow{p}pq,\qquad p\xrightarrow{q}pq.
\]

Sie tragen relative Clocks \(\log p\) bzw. \(\log q\).

Ohne Kantendiagonalität mischen sich diese nach \(\kappa\).

Status: ✓ [M]

---

## 8. Kollaps-Reinheit als Orthogonalitätsbedingung

\[
\boxed{
\left\langle E_{r;m\xrightarrow{p}n},E_{r';m'\xrightarrow{q}n}\right\rangle_{Wres,rel}=0
\quad\text{für }p\ne q.\tag{43.12}
}
\]

Äquivalent: \(\kappa^\#\kappa\) ist diagonal bezüglich Primkantenlabels. \tag{43.13}

Status: ❓ [O]

---

## Sätze

### Satz 43.1 — Graph-Reinheitslemma ✓ [M]

\(\widetilde\Psi_p=\Pi_{rel,J}\widetilde\omega_2(\widehat\varepsilon_p,L_3^\circ)\) liegt im graph-erweiterten relativen \(p\)-Kanal:
\[
\Pi_{rel,p}\widetilde\Psi_p=\widetilde\Psi_p,\qquad e^{-sT_{rel}}\widetilde\Psi_p=p^{-s}\widetilde\Psi_p.
\]

### Satz 43.2 — Kollaps-Reinheit unter \(Wres\)-Kantendiagonalität ⚠ [M]

Unter (43.12): \(\Pi_{rel,p}\Psi_p=\Psi_p\) im \(Wres\)-GNS-Quotienten; \(\langle\Psi_p,e^{-sT_p^{rel}}\Psi_p\rangle/\|\Psi_p\|^2=p^{-s}\).

### Satz 43.3 — Kollaps-Obstruktion ✗ [M]

Ohne (43.12) folgt aus \(\Psi_p\in V_{pm}\) nicht automatisch \(\Pi_{rel,p}\Psi_p=\Psi_p\).

---

## Architektonische Korrektur: Relative Feshbach-Version

\[
\boxed{
\mathbb F_N^{rel}(z,\beta)=
\begin{pmatrix}z-D_{rel,N}^- & -C_N^{rel}\\ (C_N^{rel})^\# & 1-\mathcal P_N(\beta)\end{pmatrix}.
}\tag{43.14}
\]

Der kollabierte Operator ist eine Projektion davon, nicht die primäre Struktur. ✓ [M]

---

## Statusmatrix

| Aussage | Status |
|---|---:|
| \(\widetilde\omega_2(e_uV_p,e_sV_m)\) liegt in \(V_{pm}\) | ✓ [M] |
| graph-erweiterter Raum \(\mathcal H_{rel,N}\) | ✓ [M] |
| graph-reine Aussage \(\Pi_{rel,p}\widetilde\Psi_p=\widetilde\Psi_p\) | ✓ [M] |
| \(e^{-sT_{rel}}\widetilde\Psi_p=p^{-s}\widetilde\Psi_p\) | ✓ [M] |
| Nichtverschwindungskriterium | ✓ [M] / konkrete Wres-Auswertung ⚠ |
| Kollaps erhält Reinheit automatisch | ✗ [M] |
| Kantendiagonalität der \(Wres\)-GNS-Paarung | ❓ [O] |
| erster Kollisionsfall \(q\xrightarrow{p}pq\) vs. \(p\xrightarrow{q}pq\) | ❓ [O] |
| relative Feshbach-Version \(\mathbb F_N^{rel}\) | ✓ [M] |

---

## Neuer offener Kern

\[
\boxed{\text{NEU-44: }Wres\text{-Kantendiagonalität und der }pq\text{-Kollisionstest.}}
\]

Minimaler Testfall: \(n=pq\),
\[
\left\langle E_{r;q\xrightarrow{p}pq},E_{r';p\xrightarrow{q}pq}\right\rangle_{Wres,rel}\stackrel{?}{=}0.\tag{43.17}
\]
