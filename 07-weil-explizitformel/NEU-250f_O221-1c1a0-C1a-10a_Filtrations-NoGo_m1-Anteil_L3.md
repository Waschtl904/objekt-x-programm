# NEU-250f — Filtrations-No-Go: \(m=1\)-Anteil von \(L_3^\circ\)

**Knoten:** \([O\text{-}221\text{-}1c1a0\text{-C1a/10a}]\)

**Status:** \(\checkmark[M]_{\mathrm{neg,Quelle}}\)

**Datum:** 7. August 2026

> **Vorgänger:** NEU-250e — Offener Knoten \([O\text{-}221\text{-}1c1a0\text{-C1a/10a}]\):
> \(\exists\,s_0\neq 0: \ell_{s_0,1}\neq 0\,?\)
> Diese Datei schließt ihn negativ aus den vorhandenen Quellen.

**Quellen:** NEU-019 §2.1 (\(L_3 \in C^4(F^3 A_{\mathrm{BC}}^{\mathrm{an}}, F^3 A_{\mathrm{BC}}^{\mathrm{an}})\),
Definition der \(L_3\)-Konstruktion), NEU-025 (Filtrationsdefinition
\(F^q A_{\mathrm{BC}}^{\mathrm{an}}\)).

---

## 1. Filtrationsdefinition

Nach NEU-025 ist die Filtration auf \(A_{\mathrm{BC}}^{\mathrm{an}}\) durch den
Primfaktorgrad definiert:

\[
F^q A_{\mathrm{BC}}^{\mathrm{an}}
:= \overline{\operatorname{span}}\Bigl\{e_r V_n : \nu(n) \geq q\Bigr\},
\]

wobei \(\nu(n) := \Omega(n) = \sum_{p\mid n} v_p(n)\) die Anzahl der Primfaktoren
von \(n\) mit Vielfachheit bezeichnet. Insbesondere:

\[
\nu(1) = 0, \quad \nu(p) = 1, \quad \nu(pq) = 2, \quad \nu(pqr) \geq 3 \text{ (mit Vielfachheit)}.
\]

---

## 2. Filtrationszugehörigkeit von \(L_3^\circ\)

NEU-019 §2.1 definiert:

\[
L_3 \in C^4(F^3 A_{\mathrm{BC}}^{\mathrm{an}},\, F^3 A_{\mathrm{BC}}^{\mathrm{an}}).
\]

Insbesondere ist \(L_3^\circ\) (die konkrete Auswahl eines Kozyklus-Vertreters für
\([L_3]\)) ein Element von

\[
L_3^\circ \in F^3 A_{\mathrm{BC}}^{\mathrm{an}}.
\]

Nach der Filtrationsdefinition gilt für jeden Basisvektor \(e_r V_n\), der in
\(F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) liegt:

\[
\nu(n) \geq 3.
\]

Da \(\nu(1) = 0 < 3\), folgt:

\[
\boxed{e_r V_1 \notin F^3 A_{\mathrm{BC}}^{\mathrm{an}} \quad \forall\, r \in \mathbb{Z}.}
\]

Damit gilt für die Fourier-Monoidentwicklung
\(L_3^\circ = \sum_{s,m} \ell_{s,m}\, e_s V_m\):

\[
\boxed{\ell_{s,1} = 0 \quad \forall\, s \in \mathbb{Z}.}
\tag{250f.1}
\]

---

## 3. Konsequenz für den Faltungsfilter

Nach NEU-250e gilt \(q_s = s\,\ell_{s,1}\). Aus (250f.1):

\[
\boxed{Q(z) = \sum_s s\,\ell_{s,1}\,z^s \equiv 0.}
\tag{250f.2}
\]

Damit ist der Operator \(B_p^{(1)}\) aus NEU-250d identisch null:

\[
\boxed{B_p^{(1)} = 0.}
\tag{250f.3}
\]

Und der Hebungskern ist der gesamte algebraische Koeffizientenraum:

\[
\boxed{\ker B_p^{(1)} = K_p.}
\]

---

## 4. Konsequenz für den Hebungsabstieg

Nach NEU-221e (221e.1) lautet das Abstiegskriterium:

\[
\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}.
\]

Der primitive \(m=1\)-Anteil der Rohkopplung (NEU-221e §4):

\[
P_{m=1}\,\widetilde T_p^{\mathrm{raw}}(e_u V_p)
= -\log p \sum_s \ell_{s,1}\,u\,s\; E^{\mathrm{rel}}_{u+ps;\,1\to p}
\overset{(250f.1)}{=} 0.
\]

Daher:

\[
\boxed{P_{m=1}\,\widetilde T_p^{\mathrm{raw}} \equiv 0.}
\tag{250f.4}
\]

Die Inklusion \(P_{m=1}\,\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq
\mathcal N_{\mathrm{Wres,rel}}\) ist im primitiven \(1\to p\)-Kanal **trivial
erfüllt** — nicht wegen einer inhaltlichen Eigenschaft von \(\Delta_p^{\mathrm{adm}}\),
sondern weil die Rohkopplung auf diesen Sektor **strukturell nicht zugreift**.

---

## 5. Strukturelle Bedeutung

Der Befund hat eine klare Doppelbotschaft:

**Positives:**
- Die Frobenius-Residuenform \(h_p^{(1)}(E_R,E_{R'}) = \frac1p\delta_{R,R'}\)
 aus NEU-250c/d ist mathematisch wohldefiniert und positiv-definit.
- Hebungsunabhängigkeit im primitiven \(1\to p\)-Kanal ist trivial sichergestellt.
- \(\mathscr{H}_{\mathrm{rel},p}^{(1)} \cong \ell^2(\mathbb{Z})\) existiert.

**Negatives:**
- Der \(L_3^\circ\)-Mechanismus (Rohkopplung \(\widetilde T_p^{\mathrm{raw}}\))
 liefert im primitiven \(m=1\)-Sektor **keinen nichttrivialen Vektor**.
- Der positive Hilbertraum \(\mathscr{H}_{\mathrm{rel},p}^{(1)}\) erhält aus der
 bisherigen \(F^3\)/\(L_3\)-Kopplung **keinen Kopplungsoperator**.

\[
\boxed{
\text{Rohkopplung und primitiver Hilbertraum sind entkoppelt:}
\quad
T_p^{\mathrm{rel}}\bigl(\widehat{\mathcal E}_p^{\mathrm{adm}}\bigr)
\cap \mathscr{H}_{\mathrm{rel},p}^{(1)} = \{0\} \quad (\text{strukturell}).
}
\]

---

## 6. Neues Konstruktionsdesiderat

Der nächste Knoten ist **nicht** die Suche nach einem \(\ell_{s_0,1}\)-Zeugen —
dieser existiert nach (250f.1) nicht.

Vier mögliche Reaktionen:

| Route | Beschreibung | Status |
|---|---|---|
| **D1** | Neuen \(F^1\)-Partner \(L_1^\circ \in F^1 A_{\mathrm{BC}}^{\mathrm{an}}\) konstruieren, der den \(m=1\)-Sektor trägt | \(?[O]\) |
| **D2** | Frobenius-Gramraum auf \(\nu(m)\geq 1\)-Sektoren verallgemeinern (d.\,h.\ \(h_p^{(\nu\geq1)}\) statt nur \(m=1\)) | \(?[O]\) |
| **D3** | Direkten Kopplungsoperator aus dem \(F^1\)-Gramraum ohne \(L_3^\circ\) konstruieren | \(?[O]\) |
| **D4** | Den PSWF-Gramstrang als Primärpfad aktivieren (Ausgang C4 aus NEU-250a) | \(?[O]\) |

Der sofort zugänglichste Knoten ist **D2**: die Frobenius-Residuenform
\(h_p^{(1)}\) aus NEU-250c/d ist nur die \(m=1\)-Scheibe; die volle Form

\[
h_p^{(\nu)}(E_{r;m_1\to pm_1}, E_{r';m_2\to pm_2})
:= \operatorname*{Res}_{\beta=1}\varepsilon_\beta\bigl((j_{r,m_1}^{(p)})^*j_{r',m_2}^{(p)}\bigr)
\]

könnte auf \(\nu(m)\geq 1\)-Sektoren ausgedehnt werden und dort die
\(L_3^\circ\)-Rohkopplung empfangen.

---

## 7. Statusbuchung

| Teilknoten | Aussage | Status |
|---|---|---|
| \([O\text{-}221\text{-}1c1a0\text{-C1a/10a/1}]\) | \(L_3^\circ \in F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) (Quellenbeleg NEU-019) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a/10a/2}]\) | \(\nu(1) = 0 < 3 \Rightarrow e_r V_1 \notin F^3\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a/10a/3}]\) | \(\ell_{s,1} = 0\) für alle \(s\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a/10a/4}]\) | \(Q(z) \equiv 0\), \(B_p^{(1)} = 0\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a/10a/5}]\) | \(P_{m=1}\widetilde T_p^{\mathrm{raw}} \equiv 0\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a/10a}]\) | \(\exists s_0\neq 0: \ell_{s_0,1}\neq 0\)? | \(\checkmark[M]_{\mathrm{neg,Quelle}}\) |
| **\([O\text{-}221\text{-}1c1a0\text{-D}]\)** | **Kopplungsdesiderat: F\(^1\)-Gramraum an Quelle anschließen** | **\(?[O]\)** |

Gesamtstatus:
\[
\boxed{[O\text{-}221\text{-}1c1a0\text{-C1a/10a}]:\ \checkmark[M]_{\mathrm{neg,Quelle}}
\ \text{— strukturelles Filtrations-No-Go, kein Zeuge existiert.}}
\]

---

## 8. Konsequenz für NEU-250e (Korrekturhinweis)

Der in NEU-250e als \(?[O]\) markierte Knoten \([O\text{-}221\text{-}1c1a0\text{-C1a/10a}]\)
ist jetzt geschlossen:

\[
\text{NEU-250e, Knoten /10a: }\checkmark[M]_{\mathrm{neg,Quelle}} \quad
\text{(\(\ell_{s_0,1}\neq 0\) ist filtrations-strukturell ausgeschlossen).}
\]

Der konditionale Kernsatz in NEU-250e (\S2) gilt für den Fall \(Q\neq 0\) weiterhin
korrekt, aber seine Prämisse ist im Rahmen des \(L_3^\circ\)-Kopplungsstrangs nicht
erfüllbar. Das Theorem bleibt als algebraischer Satz gültig; seine Anwendungsdomäne
ist jetzt auf mögliche zukünftige \(F^1\)-Kopolyen (Route D1) beschränkt.
