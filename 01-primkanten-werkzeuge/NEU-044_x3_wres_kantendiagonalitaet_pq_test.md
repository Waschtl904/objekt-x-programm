# NEU-44 — X.3.14: \(Wres\)-Kantendiagonalität und der \(pq\)-Kollisionstest

**Stand:** 28. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-40–43  
**Ziel:** Entscheide, ob kollabierte Reinheit aus \(Wres_{BC}^{top}\) folgt oder ob \(\mathcal H_{rel,N}\) strukturell notwendig ist.

---

## 0. Kernentscheidung

\[
\boxed{
\text{Im kollabierten Jacobi-Sektor gibt es keine automatische }Wres\text{-Kantendiagonalität.}
}
\]

\[
\boxed{
\mathcal H_{rel,N}\text{ ist nicht optionale Hilfssprache, sondern notwendige Struktur für X.3.}
}
\]

---

## 1. Kollapsabbildung

\[
\kappa(E_{r;\,m\xrightarrow{p}pm})=E_{r,pm}.
\]

Für den \(pq\)-Test: \(\kappa(E_{r;\,q\xrightarrow{p}pq})=E_{r,pq}\) und \(\kappa(E_{r';\,p\xrightarrow{q}pq})=E_{r',pq}\). Die Kantenlabels sind nach \(\kappa\) verschwunden. ✓ [M]

---

## 2. Pullback-\(Wres\) ist nicht kantendiagonal (Satz 44.1)

\[
\left\langle E_{r;\,q\xrightarrow{p}pq},E_{r';\,p\xrightarrow{q}pq}\right\rangle_{\kappa}:=\langle E_{r,pq},E_{r',pq}\rangle_{Wres}.\tag{44.2}
\]

Die rechte Seite enthält keinen Faktor \(\delta_{p,q}^{edge}\). Aus OP-4.1 (nicht-ausgeartete Paarung) folgt: Im Allgemeinen nicht null.

\[
\boxed{\text{Der Pullback-}Wres\text{ ist nicht kantendiagonal.}}\quad\text{✓ [M]}
\]

---

## 3. Kollaps-Obstruktion (Satz 44.2)

Ein relativer Primclock \(T_{rel}\) auf \(\mathcal H_{J,N}\) müsste demselben Zielvektor \(E_{r,pq}\) gleichzeitig \(\log p\) und \(\log q\) zuweisen.

\[
\boxed{T_{rel}\text{ ist auf }\mathcal H_{J,N}\text{ ohne Kantenmarkierung nicht funktoriell wohldefiniert.}}\tag{44.4}
\]

Status: ✓ [M]

---

## 4. Variante A vs. Variante B

**Variante A (Pullback):** \(Wres_{rel}:=\kappa^*Wres\). Nicht kantendiagonal. ✓ [M]

**Variante B (kantendiagonale Hebung, Satz 44.3):**

\[
\boxed{
\left\langle E_{r;\,m\xrightarrow{p}pm},E_{r';\,m'\xrightarrow{q}qm'}\right\rangle_{Wres,rel}
:=\delta_{p,q}\,\delta_{m,m'}\,\langle E_{r,pm},E_{r',pm}\rangle_{Wres}.
}\tag{44.7}
\]

Kantendiagonal, Primclock wohldefiniert. ✓ [M] als Definition.  
Intrinsizität aus \(Wres_{BC}^{top}\): ❓ [O]

---

## 5. Revidiierter Feshbach-Operator

\[
\boxed{
\mathbb F_N^{rel}(z,\beta)=
\begin{pmatrix}z-D_{rel,N}^- & -C_N^{rel}\\ -(C_N^{rel})^\# & 1-\mathcal P_N(\beta)\end{pmatrix}
}\tag{44.8}
\]

auf \(\mathcal H_{rel,N}\oplus\mathfrak p_N\). \(C_p^{rel}\varepsilon_p=\widetilde\Psi_p\in\bigoplus_m\mathcal H_{m\xrightarrow{p}pm}\).

---

## 6. Relative Selbstenergie

\[
\Sigma_{rel,N}(\beta)=C_N^{rel}(1-\mathcal P_N(\beta))^{-1}(C_N^{rel})^\#
=\sum_{p\le N}\frac{C_p^{rel}(C_p^{rel})^\#}{1-p^{-\beta}}.\tag{44.10}
\]

\(p\)-Kanäle mischen sich nicht. ✓ [M]

---

## 7. Mangoldt-Schicht bleibt erhalten

\[
-\partial_s\operatorname{Tr}_{Wres,rel}^{conn}\log(1-\mathcal P_N(s))=\frac{\zeta_N'}{\zeta_N}(s).\quad\text{✓ [M]}
\]

Die relative Struktur verhindert Clockverlust durch \(pq\)-Kollision.

---

## 8. Bedeutung für Objekt X

Objekt X = \((A_{2D}^r,[\widetilde\omega_2],[L_3],Wres_{BC}^{top})\) benötigt eine fünfte Schicht:

\[
\boxed{\text{relative Primkanten }m\xrightarrow{p}pm,}
\]

die explizite Kategorifizierung dessen, was \(\widetilde\omega_2: V_p\times V_m\mapsto V_{pm}\) bereits strukturell leistet. ✓ [M]

---

## Statusmatrix

| Aussage | Status |
|---|---:|
| \(pq\)-Kollision im kollabierten Sektor \(V_{pq}\) | ✓ [M] |
| Pullback-\(Wres=\kappa^*Wres\) enthält kein Kantenlabel | ✓ [M] |
| Pullback-\(Wres\) ist kantendiagonal | ✗ [M] |
| relativer Primclock nach Kollaps wohldefiniert | ✗ [M] |
| Graphraum \(\mathcal H_{rel,N}\) strukturell notwendig | ✓ [M] |
| kantendiagonale Hebung \(Wres_{rel}\) | ✓ [M] als Definition |
| intrinsische Herleitung \(Wres_{rel}\) aus \(Wres_{BC}^{top}\) | ❓ [O] |
| relative Feshbach-Architektur \(\mathbb F_N^{rel}\) | ✓ [M] |
| globale Stetigkeit / OP-4.1a | ⚠ [M] |
| Gamma-Faktor-Intrinsifizierung | ❓ [O] |

---

## Neuer offener Kern

\[
\boxed{\text{NEU-45: Relative Feshbach-Determinante und Euler-Mangoldt-Spur im Graphraum.}}
\]

Priorititätstest: Kann \(\det_{Wres,rel}\mathbb F_N^{rel}\) so definiert werden, dass die Produktformel \(\prod_p(1-p^{-s})\) aus den \(p\)-Kanälen hervorgeht?
