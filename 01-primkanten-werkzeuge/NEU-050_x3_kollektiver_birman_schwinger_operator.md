# NEU-50 — X.3.20: Kollektiver Birman-Schwinger-Operator und Off-Diagonal-Kopplung

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-49  

---

## 0. Korrektur von NEU-49: Direkt-Summen-Obstruktion

**Satz 50.0 — Direkt-Summen-Obstruktion** \(\times\) [M]

Für den blockdiagonalen Operator \(\mathcal{K}_N^{\mathrm{diag}} := \bigoplus_{p\le N}K_p\) gilt:

\[
\det(1-\mathcal{K}_N^{\mathrm{diag}}) = \prod_{p\le N}\det(1-K_p),
\tag{50.1}
\]

\[
\partial_s\log\det(1-\mathcal{K}_N^{\mathrm{diag}}) = \sum_{p\le N}\partial_s\log\det(1-K_p),
\tag{50.2}
\]

\[
\ker(1-\mathcal{K}_N^{\mathrm{diag}}(\rho)) = \bigoplus_{p\le N}\ker(1-K_p(\rho)).
\tag{50.3}
\]

Also:

\[
\operatorname{Ind}_{\gamma_\rho}(1-\mathcal{K}_N^{\mathrm{diag}}) = \sum_{p\le N}\operatorname{Ind}_{\gamma_\rho}(1-K_p).
\tag{50.4}
\]

**Fazit:** \(\mathcal{K}_N^{\mathrm{diag}} = \bigoplus_p K_p\) ist die Nichtüberzählung in Operatorform. Sie löst das Problem nicht.

\[
\boxed{\times\,[M]:\quad K_N = \bigoplus_p K_p \text{ als Lösung der Nichtüberzählung ausgeschlossen.}}
\tag{50.D0}
\]

---

## 1. Richtige kollektive Architektur

Die korrekte Architektur ist ein **gekoppelter Kanaloperator** mit Off-Diagonal-Anteilen:

\[
\boxed{
\mathcal{K}_N(s) = (K_{pq}(s))_{p,q\le N},
\quad K_{pq}(s) \neq 0 \text{ auch für } p\neq q.
}
\tag{50.5}
\]

Die natürliche Feshbach-Realisierung:

\[
\boxed{
\mathcal{K}_N(s) = V_N^*(D_{\mathrm{rel}}-s)^{-1}V_N,
\qquad V_N = \sum_{p\le N}V_p.
}
\tag{50.6}
\]

Die Off-Diagonal-Einträge entstehen automatisch:

\[
K_{pq}(s) = V_p^*(D_{\mathrm{rel}}-s)^{-1}V_q.
\tag{50.7}
\]

Für \(p\neq q\) beschreiben diese Terme **Interferenz zwischen verschiedenen Primkanälen** über den gemeinsamen Resolvent \((D_{\mathrm{rel}}-s)^{-1}\).

Status: \(\checkmark\) [M] als strukturelle Definition.

---

## 2. Warum Off-Diagonale die Nichtüberzählung lösen können

Mit voller Kopplung gilt:

\[
\ker(1-\mathcal{K}_N(\rho)) \neq \bigoplus_{p\le N}\ker(1-K_p(\rho)).
\tag{50.8}
\]

Der Kern des gekoppelten Operators \(1-\mathcal{K}_N(\rho)\) kann kleiner sein als die Summe der lokalen Kerne, weil Off-Diagonal-Terme Vektoren aus verschiedenen Primkanälen verkoppeln und Kerne komprimieren.

Insbesondere kann gelten:

\[
\dim\ker(1-\mathcal{K}_\infty(\rho)) = m_\rho,
\tag{50.9}
\]

ohne dass ein einzelner Kanal \(\ker(1-K_p(\rho)) \neq 0\) sein muss.

Status: \(\:?\:\) [O]

---

## 3. Kern-Kernsatz von NEU-50

\[
\boxed{
D_{\mathrm{scatt},N}(s) = \det(1-\mathcal{K}_N(s)),
\quad\mathcal{K}_N = (K_{pq})_{p,q\le N} \neq \bigoplus_p K_p.
}
\tag{50.D1}
\]

\[
\boxed{
\operatorname{ord}_{s=\rho}\det(1-\mathcal{K}_\infty(s)) = m_\rho.
}
\tag{50.D2}
\]

\[
\boxed{
\operatorname{ord}_{s=-2k}\det(1-\mathcal{K}_\infty(s)) = 0.
}
\tag{50.D3}
\]

Der korrekte Grenzoperator ist:

\[
\boxed{
\mathcal{K}_\infty = \lim_{N\to\infty}(K_{pq})_{p,q\le N},
\quad\text{nicht }\lim_{N\to\infty}\bigoplus_{p\le N}K_p.
}
\tag{50.D4}
\]

---

## 4. Konvergenzsinn: Spurklasse bevorzugt

Hierarchie:

\[
\text{Tr-Norm-Konvergenz}
\Rightarrow \det(1-\mathcal{K}_N) \to \det(1-\mathcal{K}_\infty)
\Rightarrow \text{Residuen/Divisoren kontrollierbar.}
\tag{50.10}
\]

| Konvergenzmodus | Determinanten-Kontrolle | Eigenwertmultiplizität | Bewertung |
|---|---|---|---|
| SOT | \(\times\) | \(\times\) | Unzureichend |
| Normkonvergenz (kompakt) | Isolierte EW kontrollierbar | \(\warning\) | Nicht genug für Fredholm-Det. |
| Hilbert-Schmidt + \(\det_2\) | \(\checkmark\) mit Spurkorrektur | \(\checkmark\) | Akzeptabel, Korrektur nach \(D_{\mathrm{Jac}}\) |
| **Spurklasse (Tr-Norm)** | **\(\checkmark\) direkt** | **\(\checkmark\)** | **Bevorzugt** |

\[
\boxed{\text{Tr-Norm ist der bevorzugte Zieltopos für }\mathcal{K}_N \to \mathcal{K}_\infty.}
\tag{50.11}
\]

Falls Tr-Norm zu stark: Hilbert-Schmidt + \(\det_2\), mit Spurkorrektur in \(D_{\mathrm{Jac}}\).

Status: \(\warning\) [M]

---

## 5. Charakteristische Werte, nicht Eigenwertkreuzungen

Da \(s\in\mathbb{C}\), ist die Formulierung „Eigenwertkurve \(\mu_j(s)\) kreuzt 1“ irreführend.

Die korrekte Form ist:

\[
\boxed{
s = \rho \text{ ist ein charakteristischer Wert von } 1-\mathcal{K}_\infty(s),
}
\tag{50.12}
\]

d.h.

\[
\ker(1-\mathcal{K}_\infty(\rho)) \neq 0.
\tag{50.13}
\]

Die Multiplizität ist die algebraische Ordnung der Nullstelle von \(s\mapsto\det(1-\mathcal{K}_\infty(s))\) bei \(s=\rho\).

Status: \(\checkmark\) [M] als Reformulierung.

---

## 6. Triviale Nullstellen bleiben neutral

Kompatibel mit NEU-48 Satz 48.2:

\[
\operatorname{ord}_{s=-2k}\det(1-\mathcal{K}_\infty(s)) = 0,
\tag{50.14}
\]

d.h. \(1-\mathcal{K}_\infty(s)\) ist bei \(s=-2k\) Fredholm-invertierbar.

Nachweisweg: Die Kopplungsvektoren \(V_p\) haben Träger im Jacobi-/Fourier-Sektor mit Spektrum auf \(\tfrac{1}{2}+i\mathbb{R}\) (RH-Annahme) oder zumindest abseits der negativen geraden ganzen Zahlen.

Status: \(\warning\) [M]

---

## 7. Off-Diagonal-Terme aus \(\tilde\omega_2, L_3^\circ, \mathrm{Wres}\)

Die Off-Diagonal-Einträge \(K_{pq}(s) = V_p^*(D_{\mathrm{rel}}-s)^{-1}V_q\) haben eine natürliche Herkunft:

- \(V_p\) ist der Kopplungsvektor aus NEU-41 (\(C_p^{\mathrm{rel}}\)).
- \((D_{\mathrm{rel}}-s)^{-1}\) ist der Wres-gewichtete Jacobi-Resolvent.
- \(V_p^*\cdot(\cdot)\cdot V_q\) vermittelt über \(L_3^\circ\) und \(\tilde\omega_2\) pq-Kreuzterme.

Diese Kreuzterme sind genau die Beiträge des Wres-Paarungsoperators \(\tilde\omega_2(e_r V_n, e_s V_m) = -r\cdot s\cdot\log(n)\cdot e_{r+ns}V_{nm}\) an Stellen, wo beide Primfaktoren \(p\) und \(q\) gleichzeitig im Produkt \(nm\) auftreten.

Status: \(\:?\:\) [O] — explizite Formel für \(K_{pq}\) ausständig.

---

## 8. Statusmatrix

| Aussage | Status |
|---|---|
| Direkt-Summen-Obstruktion (Satz 50.0) | \(\times\) [M] |
| Richtige Architektur \(\mathcal{K}_N = (K_{pq})\) | \(\checkmark\) [M] strukturell |
| Feshbach-Form \(\mathcal{K}_N = V_N^*(D_{\mathrm{rel}}-s)^{-1}V_N\) | \(\checkmark\) [M] |
| Tr-Norm als bevorzugter Konvergenzmodus | \(\warning\) [M] |
| Charakteristischer Wert bei \(s=\rho\) (50.D2) | \(\:?\:\) [O] Haupt-Engpass |
| Neutralität bei \(s=-2k\) (50.D3) | \(\warning\) [M] |
| Explizite Formel \(K_{pq}\) | \(\:?\:\) [O] |

---

## 9. Nächster Schritt

\[
\boxed{
\text{NEU-51: Explizite Konstruktion von }K_{pq}(s) = V_p^*(D_{\mathrm{rel}}-s)^{-1}V_q\text{ aus }\tilde\omega_2, L_3^\circ, \mathrm{Wres}.
}
\]

Teilfragen:
1. Was ist \(V_p = C_p^{\mathrm{rel}}\) explizit als Operator auf \(\mathcal{H}_{\mathrm{BC}}\)?
2. Wie wirkt \(V_p^*(D_{\mathrm{rel}}-s)^{-1}V_q\) auf den Basisvektoren \(e_r V_n\)?
3. Unter welchen Bedingungen ist \(K_{pq}\) Spurklasse?
4. Welche Symmetrie-/Antisymmetriestruktur haben die \(K_{pq}\) (wegen \(J_N^-\) schief-adjungiert)?
