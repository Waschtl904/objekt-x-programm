# NEU-51 — X.3.21: Resolventen-Matrixelement \(K_{pq}\), Spurklasse-Kriterium, Symmetrieform

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-50  
**Ziel:** Explizite Basisformel für \(K_{pq}(s)\) aus \(V_p = C_p^{\mathrm{rel}}\), Klasse \(\mathcal{S}_1\) vs. \(\mathcal{S}_2\), Symmetrie.

---

## 0. Ausgangspunkt

Aus NEU-50:

\[
\mathcal{K}_N(s) = V_N^*(D_{\mathrm{rel}}-s)^{-1}V_N,
\quad V_N = \sum_{p\le N}V_p,
\tag{51.0}
\]

also

\[
\mathcal{K}_N(s) = \sum_{p,q\le N} K_{pq}(s),
\quad K_{pq}(s) := V_p^*(D_{\mathrm{rel}}-s)^{-1}V_q.
\tag{51.1}
\]

Ziel: \(K_{pq}(s)_{(r,n),(t,m)}\) explizit.

---

## 1. Satz 51.1 — Relative Kopplungsform

Aus \(\tilde\omega_2(e_u V_p, e_s V_m) = -u\,s\,\log(p)\,e_{u+ps}V_{pm}\) (NEU-43/44) folgt:

\[
\boxed{
V_p(e_s V_m) = \sum_u (-u\,s\,\log p)\, \eta_{p;m;s,u},
\quad \eta_{p;m;s,u} \sim e_{u+ps}V_{pm}.
}
\tag{51.2}
\]

Die Summationsreichweite über \(u\) ist noch nicht fixiert (Regulierung). Zulässige Optionen:
- \(u\in\mathbb{Z}\) mit Gewichtsabschneidung,
- \(u\) durch den \(p\)-Kanal-Projektor fixiert,
- endliche Fourierprojektion \(|u|\le U_p\).

Diese Wahl entscheidet später über \(\mathcal{S}_1\) vs. \(\mathcal{S}_2\).

Status: \(\checkmark/\warning\) [M] — abhängig von Regulierungswahl.

---

## 2. Satz 51.2 — Resolventenformel für \(K_{pq}\)

Sei \(D_{\mathrm{rel}}\eta_\alpha = \lambda_\alpha\eta_\alpha\) eine Spektralzerlegung. Dann:

\[
\boxed{
K_{pq}(s)_{(r,n),(t,m)}
= r\,t\,\log p\,\log q
\sum_{u,v} u\,v\;
R_{\mathrm{rel}}(s)\bigl[(p;n;r,u),(q;m;t,v)\bigr],
}
\tag{51.3}
\]

mit dem Resolventen-Matrixelement:

\[
R_{\mathrm{rel}}(s)\bigl[(p;n;r,u),(q;m;t,v)\bigr]
:=
\sum_\alpha
\frac{
\overline{\langle\eta_\alpha,\eta_{p;n;r,u}\rangle}\,
\langle\eta_\alpha,\eta_{q;m;t,v}\rangle
}{
\lambda_\alpha - s
}.
\tag{51.4}
\]

Diese Form zeigt:
- \(p = q\): Diagonal-Kanalbeitrag (kein Priminterferenz-Term).
- \(p\neq q\): echte Priminterferenz durch gemeinsamen Resolventen \((D_{\mathrm{rel}}-s)^{-1}\). ✓ [M]

Status: \(\checkmark\) [M] formal, sobald \(V_p\) gemäß Satz 51.1 fixiert.

---

## 3. Satz 51.3 — Off-Diagonal-Notwendigkeit

Für \(p\neq q\) ist \(K_{pq}(s)\neq 0\) generisch, weil \(D_{\mathrm{rel}}\) auf dem gemeinsamen Graphraum operiert und die \(\eta_{p;n;r,u}\) keine kanaldiagonale Basis erzwingen.

\[
\boxed{\mathcal{K}_N \neq \bigoplus_{p\le N}K_p.}
\tag{51.5}
\]

Ausnahme: Falls \(D_{\mathrm{rel}}\) kantendiagonal ist, fallen Off-Diagonale weg — aber dann wäre \(R_{\mathrm{rel}}(s)[(p;n;r,u),(q;m;t,v)] = 0\) für \(p\neq q\), was eine explizite Eigenschaft der Basis ist, nicht der allgemeinen Situation. ✗ [M] als Standardfall.

---

## 4. Satz 51.4 — Spurklasse-Kriterium

**Hinreichende Bedingung für \(K_N \in \mathcal{S}_1\):**

\[
\boxed{
(D_{\mathrm{rel}}-s)^{-1/2}V_N \in \mathcal{S}_2
}
\tag{51.6}
\]

Dann ist \(K_N(s) = ((D_{\mathrm{rel}}-s)^{-1/2}V_N)^*(D_{\mathrm{rel}}-s)^{-1/2}V_N \in \mathcal{S}_1\).

Explizite Bedingung in Basisform:

\[
\boxed{
\sum_p (\log p)^2 \sum_{n,r,u} \frac{u^2 r^2}{|\lambda_{p;n;r,u}-s|} < \infty.
}
\tag{51.7}
\]

**Falls (51.7) divergiert:**

\(K_N \in \mathcal{S}_2\) (Hilbert-Schmidt) kann noch gelten, dann ist

\[
D_{\mathrm{scatt},N}(s) = \det_2(1-K_N(s))
\tag{51.8}
\]

die regularisierte Fredholm-Determinante. Die fehlende Spurkorrektur

\[
\exp(\mathrm{Tr}\,K_N(s))
\tag{51.9}
\]

gehört dann zu \(D_{\mathrm{Jac},N}\).

Status: \(\:?\:\) [O] — Konvergenz von (51.7) ausständig.

---

## 5. Satz 51.5 — Symmetrieform

**Normalisierungsentscheidung (vor Divisorargument festzulegen):**

### Option A: \(D_{\mathrm{rel}} = J_N^-\) schief-adjungiert (\((J_N^-)^* = -J_N^-\))

\[
\bigl((D_{\mathrm{rel}}-s)^{-1}\bigr)^* = -(D_{\mathrm{rel}}+\bar s)^{-1}.
\tag{51.10}
\]

Daher:

\[
\boxed{K_{pq}(s)^* = -K_{qp}(-\bar s).}
\tag{51.11}
\]

### Option B: \(\mathcal{D}_{\mathrm{rel}} = iJ_N^-\) selbstadjungiert (\(\mathcal{D}_{\mathrm{rel}}^* = \mathcal{D}_{\mathrm{rel}}\))

\[
\bigl((\mathcal{D}_{\mathrm{rel}}-s)^{-1}\bigr)^* = (\mathcal{D}_{\mathrm{rel}}-\bar s)^{-1}.
\tag{51.12}
\]

Daher:

\[
\boxed{K_{pq}(s)^* = K_{qp}(\bar s).}
\tag{51.13}
\]

**Empfehlung:** Option B (\(\mathcal{D}_{\mathrm{rel}} = iJ_N^-\)), damit \(\mathcal{K}_N(\bar s)^* = \mathcal{K}_N(s)\) und die Fredholm-Determinante reellwertige Null\-stellen im richtigen Sinn erzeugen kann.

Status: \(\warning\) [M] — Entscheidung vor NEU-52 zu treffen.

---

## 6. Zusammenfassung: Der erste konkrete Test

Die Kernrechnung ist:

\[
\boxed{
\sum_{u,v} u\,v\;R_{\mathrm{rel}}(s)\bigl[(p;n;r,u),(q;m;t,v)\bigr]
}
\tag{51.14}
\]

muss explizit oder abschätzbar werden. Daraus folgen:

1. \(K_{pq}\in\mathcal{S}_1\) oder \(\mathcal{S}_2\) (Spurklasse-Entscheidung)
2. Off-Diagonal-Stärke für \(p\neq q\)
3. Erst danach ist sinnvoll zu fragen: \(\operatorname{ord}_{s=\rho}\det(1-\mathcal{K}_\infty(s))=m_\rho\)

---

## 7. Statusmatrix

| Aussage | Status |
|---|---|
| Kopplungsform \(V_p\) (Satz 51.1) | \(\checkmark/\warning\) [M] (Regulierung offen) |
| Resolventenformel \(K_{pq}\) (Satz 51.2) | \(\checkmark\) [M] formal |
| Off-Diagonal-Notwendigkeit (Satz 51.3) | \(\checkmark\) [M] |
| Spurklasse \(\mathcal{S}_1\): Bedingung (51.7) | \(\:?\:\) [O] |
| Hilbert-Schmidt \(\mathcal{S}_2\) + \(\det_2\) | \(\:?\:\) [O] |
| Symmetrieform Opt. A vs. B | \(\warning\) [M] Entscheidung ausständig |
| Summe (51.14) explizit/abschätzbar | \(\:?\:\) [O] Kern-Engpass |

---

## 8. Nächster Schritt

\[
\boxed{
\text{NEU-52: Explizite Auswertung von }R_{\mathrm{rel}}(s)[(p;n;r,u),(q;m;t,v)]\text{ und Spurklasse-Entscheidung.}
}
\]

Teilfragen:
1. Welche Basisstruktur hat \(D_{\mathrm{rel}}\) auf \(\eta_{p;m;s,u}\)?
2. Sind die \(\eta_{p;m;s,u}\) eine Eigenbasis oder eine dichte Teilmenge?
3. Für welches \((\lambda_{p;n;r,u})\) konvergiert (51.7)?
