# NEU-55 — X.3.25: Matrixabschätzungsblatt — Nelson-Bedingungen für \(iJ^-\)

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-54  
**Ziel:** Explizite Matrix-Abschätzungen der zwei Nelson-Bedingungen via \(\Theta_N\)-Matrixstruktur; vollständige Satzstruktur bis zur essentiellen Selbstadjungiertheit.

---

## 0. Vorab-Präzisierung: \(\ker(J^-)\) und effektiver Raum

Für Selbstadjungiertheit stellt \(\ker(J^-)\) kein Problem dar (\(D_{\mathrm{rel}}=0\) dort ist selbstadjungiert). Für **kompakte Resolvente** jedoch gilt:

\[
\boxed{\ker(J^-)\text{ mit unendlicher Multiplizität verhindert kompakten Resolventen.}}
\tag{55.PRE}
\]

Daher definiere den effektiven Spektralraum:

\[
\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}} := \overline{\operatorname{Ran}(J^-)} = \ker(J^-)^\perp.
\tag{55.0}
\]

Alle folgenden Abschätzungen gelten auf \(\mathcal{D}_0^{\mathrm{eff}} := \mathcal{D}_0 \cap \mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}\), d.h. es wird \(r\neq 0\) und \(m>1\) vorausgesetzt.

Zusätzlich sollte gelten: \(V_N^*\ker(J^-)=0\), damit die Streudet-Schicht den trivialen Kern nicht sieht.

---

## 1. Setup: Matrixform

\[
a=(p,m,r,u),\quad \eta_a=\eta_{p;m;r,u},\quad
J^-\eta_a = \sum_b \Theta_{ba}\,\eta_b,
\tag{55.1}
\]

\[
L\eta_a = \ell(a)\,\eta_a,\quad
\ell(p,m,r,u) \sim 1+|r|\log(2+m)+|u|\log p+\Omega(m).
\tag{55.2}
\]

Aus \(\Theta_N(e_rV_n)=-\gamma_N r\log(n)\,e_{r+n}V_n\) (NEU-30) folgt:

\[
\Theta_{ba}\neq 0 \quad\text{nur für }b=(p',m',r+n,u')\text{ mit } m'=m,\; n|m.
\tag{55.3}
\]

Das bedeutet: **\(\Theta_N\) ist lokal endlich** \(\to\) jeder Basisvektor hat endlich viele Nachbarn pro \(N\) (nach oben unbegrenzt für \(N\to\infty\), aber bei festem \(N\) kontrolliert).

---

## 2. Satz 55.1 — Lokale Normabschätzung (Nelson-Bedingung 1)

**Matrixform:**

\[
\|J^-\eta_a\|^2 = \sum_b |\Theta_{ba}|^2.
\tag{55.4}
\]

**Zu zeigen:**

\[
\boxed{\sum_b|\Theta_{ba}|^2 \le C^2\ell(a)^2.}
\tag{55.5}
\]

**Heuristische Rechnung:** Aus (55.3) sind die nichtverschwindenden \(\Theta_{ba}\) von der Form

\[
|\Theta_{ba}| \sim \gamma_N |r|\log n,
\tag{55.6}
\]

mit \(n|m\) und \(b=(p',m,r+n,u')\). Der Energieoperator enthält \(|r|\log(2+m)\). Für \(n\le m\) gilt \(\log n\le\log m\le\log(2+m)\), also

\[
|\Theta_{ba}| \lesssim \gamma_N\,\ell(a).
\tag{55.7}
\]

Bei endlicher Nachbarzahl (lokale Endlichkeit bei festem \(N\)) folgt dann (55.5) sofort:

\[
\sum_b|\Theta_{ba}|^2 \lesssim (\text{Nachbarzahl})\cdot\gamma_N^2\,\ell(a)^2.
\tag{55.8}
\]

**Schur-Test-Variante** (robuster, kein Endlichkeitsargument nötig):

\[
\boxed{
\sup_a \sum_b \frac{|\Theta_{ba}|}{\ell(a)} < \infty,\qquad
\sup_b \sum_a \frac{|\Theta_{ba}|}{\ell(a)} < \infty.
}
\tag{55.9}
\]

Dann \(J^-L^{-1}\in\mathcal{B}(\mathcal{H})\), also \(\|J^-x\|\le C\|Lx\|\). \(\checkmark/\warning\) [M]

---

## 3. Satz 55.2 — Expliziter Kommutator (formal \(\checkmark\) [M])

\[
\boxed{[J^-,L]_{ba} = (\ell(a)-\ell(b))\,\Theta_{ba}.}
\tag{55.10}
\]

**Herleitung:** \([J^-,L]\eta_a = J^-(\ell(a)\eta_a)-LJ^-\eta_a = \sum_b(\ell(a)-\ell(b))\Theta_{ba}\eta_b\).

Status: \(\checkmark\) [M]

---

## 4. Satz 55.3 — Kommutator-Schur-Test (Nelson-Bedingung 2)

Nelson verlangt:

\[
|\langle J^-x,Lx\rangle - \langle Lx,J^-x\rangle| \le C\langle x,Lx\rangle.
\tag{55.11}
\]

Hinreichende **Schur-Bedingung** (zeilenweise):

\[
\boxed{\sum_b|\ell(a)-\ell(b)|\,|\Theta_{ba}| \le C\ell(a).}
\tag{55.12}
\]

**Zu zeigen:** \(|\ell(a)-\ell(b)|\) für eine \(\Theta_N\)-Kante \(a\to b\) ist kontrollierbar. Mit \(b=(p',m,r+n,u')\) und \(\Theta_{ba}\sim\gamma_N r\log n\):

\[
\ell(b)-\ell(a)
\sim |r+n|\log(2+m)-|r|\log(2+m)
= n\cdot\operatorname{sgn}(r+n)\cdot\log(2+m),
\tag{55.13}
\]

also (für \(r,n>0\)):

\[
|\ell(b)-\ell(a)| \sim n\log(2+m) \lesssim m\log(2+m).
\tag{55.14}
\]

Dann:

\[
|\ell(b)-\ell(a)|\,|\Theta_{ba}|
\lesssim n\log m\cdot\gamma_N r\log n
\lesssim \gamma_N m(\log m)^2 r.
\tag{55.15}
\]

Vgl. mit \(\ell(a) \sim |r|\log m\). Damit (55.12):

\[
\frac{|\ell(b)-\ell(a)|\,|\Theta_{ba}|}{\ell(a)}
\lesssim \frac{\gamma_N m(\log m)^2 r}{|r|\log m}
= \gamma_N m\log m.
\tag{55.16}
\]

**Warnung:** Der Ausdruck \(\gamma_N m\log m\) wächst mit \(m\). Bei Summation über Kanten \(a\to b\) darf man nicht summieren, ohne die Trunkierung \(N\) zu berücksichtigen. Bei festem \(N\) und endlichen \(m\le N\) ist (55.16) beschränkt. Im Grenzübergang \(N\to\infty\) muss die Konvergenzrate \(\gamma_N\to 0\) schnell genug gewählt werden.

**Präzisierter Status:** \(\checkmark\) [M] für endliches \(N\). Für \(N\to\infty\): abhängig von \(\gamma_N\). \(\warning\) [M]

---

## 5. Satz 55.4 — Essentielle Selbstadjungiertheit

Aus Satz 55.1 (Nelson-Bed. 1) und Satz 55.3 (Nelson-Bed. 2) folgt via Nelsons Kommutator-Theorem:

\[
\boxed{iJ^-\text{ ist wesentlich selbstadjungiert auf }\mathcal{D}_0^{\mathrm{eff}}.}
\tag{55.17}
\]

Daher:

\[
D_{\mathrm{rel}} = \overline{iJ^-}\text{ ist kanonisch selbstadjungiert auf }\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}.
\tag{55.18}
\]

Die Resolvente \((D_{\mathrm{rel}}-s)^{-1}\) ist für \(s\notin\mathbb{R}\) wohldefiniert.

Status: \(\checkmark\) [M] unter Bedingungen (55.5)/(55.9) und (55.12). Expliziter Beweis der Bedingungen: \(\:?\:\) [O]

---

## 6. Konfinement und \(\gamma_N\)-Rolle

\(\gamma_N\) erfüllt eine doppelte Funktion:

| Rolle | Anforderung |
|---|---|
| Konfinement \(\|J^-\eta_a\|\sim\gamma_N|r|\log n\to\infty\) | \(\gamma_N\) nicht zu schnell \(\to 0\) |
| Kommutator-Schur-Test: \(\gamma_N m\log m\) beschränkt | \(\gamma_N\to 0\) schnell genug |

Diese Spannung muss in NEU-56 aufgelöst werden.

Heuristische Auflösung: Nehme \(\gamma_N = C/\log N\). Dann:
- \(\gamma_N\cdot m\log m \lesssim m/N\) für \(m\le N\): beschränkt für festes \(N\).
- \(\gamma_N|r|\log n\to\infty\) entlang \(|r|\to\infty\) oder \(n\to\infty\) bei festem \(N\): Konfinement bleibt erhalten.

Status: \(\warning\) [M]

---

## 7. Statusmatrix

| Aussage | Status |
|---|---|
| Effektiver Raum \(\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}\) (55.0) | \(\checkmark\) [M] |
| Matrixform \(\|J^-\eta_a\|^2=\sum_b|\Theta_{ba}|^2\) (55.4) | \(\checkmark\) [M] |
| Nelson-Bed. 1: \(\sum_b|\Theta_{ba}|^2\le C^2\ell(a)^2\) (55.5) | \(\checkmark/\warning\) [M] heuristisch |
| Schur-Test (55.9) | \(\:?\:\) [O] |
| Kommutator \([J^-,L]_{ba}\) (55.10) | \(\checkmark\) [M] |
| Kommutator-Schur (55.12) | \(\checkmark\) [M] für endl. \(N\); \(\warning\) [M] Grenzfall |
| Essentielle Selbstadjungiertheit (55.17–55.18) | \(\checkmark\) [M] unter Bed. |
| \(\gamma_N\)-Spannung Konfinement/Schur | \(\warning\) [M] |

---

## 8. Nächster Schritt

\[
\boxed{
\text{NEU-56: Wahl von }\gamma_N\text{; Konfinement-Beweis auf }\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}\text{; kompakter Resolvent vs. Spektralmaß-Form.}
}
\]

Teilfragen:
1. Optimale Wahl \(\gamma_N\) (z.B. \(\gamma_N=C/\log N\))?
2. Gilt \(\|D_{\mathrm{rel}}x\|+\|x\|\ge c\|Lx\|\) auf \(\mathcal{H}_{\mathrm{rel}}^{\mathrm{eff}}\)?
3. Falls ja: kompakter Resolvent, diskretes Spektrum, Weg A (NEU-53).
4. Falls nein: Spektralmaß-Form bleibt Standard (Weg B).
