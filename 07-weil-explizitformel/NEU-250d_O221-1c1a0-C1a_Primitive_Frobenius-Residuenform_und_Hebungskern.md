# NEU-250d — Primitive Frobenius-Residuenform und expliziter Hebungskern

**Knoten:** \([O\text{-}221\text{-}1c1a0\text{-C1a}]\)

**Status:** \(\checkmark[M]_{\mathrm{part}}\)

**Datum:** 7. August 2026

> **Vorgänger:** NEU-250c — Für \(p=2\) wurde berechnet:
> \(G^L_{R,R'}(\beta) = \delta_{R,R'}\cdot 2^{-\beta}\zeta(\beta)\),
> Residuum \(\frac12\delta_{R,R'} > 0\). Offen blieb \([O\text{-}221\text{-}1c1a0\text{-C1a}]\):
> Gilt das für allgemeines \(p\), und ist die \(F^1\)-Gramform für die Hebungskern-
> Konstruktion verwendbar?

**Quellen:** NEU-015 §3.1 (Matrixkoeffizienten, Involution), NEU-221e §4 (Fourierregel,
\(\widetilde T_p^{\mathrm{raw}}\), \(\Delta_p^{\mathrm{adm}}\), \(\mathcal N_{\mathrm{Wres,rel}}\)).

---

## 1. Notation und Konventionen

Sei \(p\) eine beliebige Primzahl. Setze

\[
j_R^{(p)} := e_R V_p \in A_{\mathrm{BC}}^{\mathrm{an}}, \qquad R \in \mathbb Z.
\]

Die Frobenius-Residuenform des Primsektors \(p\) ist

\[
h_p^{(1)}(E_R, E_{R'}) := \operatorname*{Res}_{\beta=1}\, \varepsilon_\beta\bigl((j_R^{(p)})^* j_{R'}^{(p)}\bigr).
\]

Die neue Notation \(h_p^{(1)}\) oder \(h^{\mathrm{Frob}}_{\mathrm{rel},p}\) ist bewusst
verschieden von \(h_{\mathrm{Wres,rel}}\) gewählt: sie bezeichnet eine \(F^1\)-Frobenius-
Residualform, nicht die \(F^3/L_3\)-Wres-Doppelpol-Form.

---

## 2. Allgemeiner Primsektor: Matrixrechnung

Nach NEU-015 §3.1:

\[
(e_R V_p)_{m,k,r'} = \delta_{k,pm}\,\delta_{r',R}, \qquad
(V_p^* e_{-R})_{m,k,r'} = \delta_{m,pk}\,\delta_{r',-R}.
\]

### 2.1 Produkt \((j_R^{(p)})^* j_{R'}^{(p)}\)

\[
\bigl((j_R^{(p)})^* j_{R'}^{(p)}\bigr)_{m,\ell,r''}
= \sum_k (V_p^* e_{-R})_{m,k,-R}\cdot(e_{R'} V_p)_{k,\ell,R'}
= \sum_k \delta_{m,pk}\,\delta_{\ell,pk}\cdot\delta_{r'',R'-R}.
\]

Die \(k\)-Summe: es existiert \(k\) mit \(m = pk\) und \(\ell = pk\) genau dann, wenn
\(p\mid m\) und \(\ell = m\). Damit:

\[
\boxed{
\bigl((j_R^{(p)})^* j_{R'}^{(p)}\bigr)_{m,\ell,r''}
= \delta_{\ell,m}\,\delta_{r'',R'-R}\,\mathbf{1}_{[p\mid m]}.
}
\]

Diagonal, getragen auf \(p\mathbb{N}\), Ladung \(R'-R\).

### 2.2 Linke Gramform

\[
G^{L,p}_{R,R'}(\beta)
= \varepsilon_\beta\bigl((j_R^{(p)})^* j_{R'}^{(p)}\bigr)
= \sum_m m^{-\beta}\,\delta_{0,R'-R}\,\mathbf{1}_{[p\mid m]}.
\]

Für \(R' \neq R\): Null. Für \(R' = R\):

\[
G^{L,p}_{R,R}(\beta)
= \sum_{n=1}^\infty (pn)^{-\beta}
= p^{-\beta}\,\zeta(\beta).
\]

\[
\boxed{G^{L,p}_{R,R'}(\beta) = \delta_{R,R'}\cdot p^{-\beta}\,\zeta(\beta).}
\]

### 2.3 Rechte Gramform

\[
\bigl(j_{R'}^{(p)} (j_R^{(p)})^*\bigr)_{m,\ell,r''}
= \sum_k \delta_{k,pm}\,\delta_{k,p\ell}\cdot\delta_{r'',R'-R}
= \delta_{\ell,m}\,\delta_{r'',R'-R}.
\]

Kein \(p\mid m\)-Filter. Damit:

\[
\boxed{G^{R,p}_{R,R'}(\beta) = \delta_{R,R'}\cdot\zeta(\beta).}
\]

### 2.4 KMS-Konsistenz

Unter \(\sigma_t(V_p) = p^{it}V_p\) gilt \(\sigma_{i\beta}(j_R^{(p)}) = p^{-\beta}j_R^{(p)}\). Daher:

\[
\varepsilon_\beta\bigl((j_R^{(p)})^* j_R^{(p)}\bigr)
\overset{\mathrm{KMS}}{=} p^{-\beta}\,\varepsilon_\beta\bigl(j_R^{(p)}(j_R^{(p)})^*\bigr)
= p^{-\beta}\,\zeta(\beta). \quad \checkmark[M]
\]

---

## 3. Hauptsatz 1 — Allgemeiner Primsektor

\[
\boxed{h_p^{(1)}(E_R,E_{R'}) := \operatorname*{Res}_{\beta=1} G^{L,p}_{R,R'}(\beta)
= \frac1p\,\delta_{R,R'}.}
\]

**Beweis.** Aus §2.2: \(G^{L,p}_{R,R'}(\beta) = \delta_{R,R'}\cdot p^{-\beta}\zeta(\beta)\).
Wegen \(\operatorname{Res}_{\beta=1}\zeta(\beta) = 1\) und \(p^{-\beta}\) stetig bei \(\beta=1\):
\(\operatorname{Res}_{\beta=1}G^{L,p}_{R,R'}(\beta) = \delta_{R,R'}\cdot p^{-1}\). \(\square\)

**Skalierung zwischen Primsektoren:**

| \(p\) | \(h_p^{(1)}(E_R,E_R)\) |
|---|---|
| 2 | \(1/2\) |
| 3 | \(1/3\) |
| 5 | \(1/5\) |
| \(p\) | \(1/p\) |

---

## 4. Hauptsatz 2 — Positivität und triviales Radikal

**Satz.** \(h_p^{(1)} > 0\) und \(\operatorname{Rad}h_p^{(1)} = \{0\}\).

**Beweis.** Sei \(x = \sum_R c_R E_R\) mit endlichem Träger. Dann:

\[
h_p^{(1)}(x,x)
= \sum_{R,R'} \overline{c_R}\,c_{R'}\,h_p^{(1)}(E_R,E_{R'})
= \sum_R |c_R|^2\cdot\frac1p
= \frac1p\|x\|_{\ell^2}^2.
\]

Damit:
- \(h_p^{(1)}(x,x) \geq 0\) für alle \(x\);
- \(h_p^{(1)}(x,x) = 0 \iff x = 0\).

\[
\boxed{h_p^{(1)} > 0, \qquad \operatorname{Rad}h_p^{(1)} = \{0\}.} \quad \square
\]

---

## 5. Hauptsatz 3 — Positive primitive Hilbertisierung

**Korollar.** Die Vervollständigung
\(\mathscr H_{\mathrm{rel},p}^{(1)} := \overline{\mathscr V_{\mathrm{rel},2,N}^{\mathrm{pre}}}^{h_p^{(1)}}\)
ist ein Hilbertraum mit ONB \(\{\sqrt{p}\,E_R\}_{R\in\mathbb Z}\) und

\[
\boxed{\mathscr H_{\mathrm{rel},p}^{(1)} \cong \ell^2(\mathbb Z), \qquad \|E_R\|^2 = \frac1p.}
\]

**Frobenius-Residuenbrücke:** Die isometrische Einbettung

\[
\iota_p : \mathscr H_{\mathrm{rel},p}^{(1)} \longrightarrow \ell^2(\mathbb Z),
\qquad E_R \longmapsto \frac{1}{\sqrt p}\,\eta_R
\]

mit \(\{\eta_R\}\) orthonormal ist eine Isometrie:

\[
\left\|\frac{1}{\sqrt p}\eta_R\right\|^2 = \frac1p = \|E_R\|_{h_p^{(1)}}^2. \quad \checkmark[M]
\]

> **Verhältnis zu NEU-246.** NEU-246 hatte postuliert \(E_R \mapsto \sqrt{w_R}\eta_R\)
mit einer nicht quellseitig begründeten Gewichtsfunktion \(w_R\). Die hier konstruierte
Brücke liefert **dasselbe Bild** mit \(w_R = 1/p\), aber auf einer vollständig
nachgewiesenen Grundlage: die Frobenius-Residualform aus den BC-Matrixrelationen.
NEU-246 war in der **Wres-Begründung** fehlerhaft; die \(F^1\)-Frobenius-Brücke ist
eine **neue, unabhängige** Konstruktion, die zu denselben Gewichten führt.

---

## 6. Hauptsatz 4 — Expliziter Hebungskern

**Setup.** Sei \(\delta = \sum_u a_u e_u V_p \in K_p\) eine Liftänderung. Nach
NEU-221e §4 (Fourierregel aus NEU-42 §10):

\[
\widetilde T_p^{\mathrm{raw}}(e_u V_p)
= -\sum_{s,m} \ell_{s,m}\,u\,s\,\log p\; E^{\mathrm{rel}}_{u+ps;\,m\to pm}.
\]

Der **primitive Kanal** \(m=1\) liefert:

\[
P_1\widetilde T_p^{\mathrm{raw}}(e_u V_p)
= -\log p\sum_s \ell_{s,1}\,u\,s\; E^{\mathrm{rel}}_{u+ps;\,1\to p}.
\]

Für allgemeines \(\delta = \sum_u a_u e_u V_p\):

\[
P_1\widetilde T_p^{\mathrm{raw}}(\delta)
= -\log p\sum_R \Bigl(\sum_{\substack{u,s\in\mathbb Z\\u+ps=R}} a_u\,u\,s\,\ell_{s,1}\Bigr)\,E_R.
\]

**Norm unter \(h_p^{(1)}\):**

Da \(h_p^{(1)}(E_R,E_{R'}) = \frac1p\delta_{R,R'}\):

\[
\boxed{
\bigl\|P_1\widetilde T_p^{\mathrm{raw}}(\delta)\bigr\|_{h_p^{(1)}}^2
= \frac{(\log p)^2}{p}\sum_R \Bigl|\sum_{u+ps=R} a_u\,u\,s\,\ell_{s,1}\Bigr|^2.
}
\]

**Exaktes Abstiegskriterium** im primitiven Kanal:

\[
\boxed{
P_1\widetilde T_p^{\mathrm{raw}}(\delta) = 0
\iff
\sum_{u+ps=R} a_u\,u\,s\,\ell_{s,1} = 0 \quad \forall R.
}
\]

**Definition des primitiven Hebungskerns:**

\[
\boxed{
\ker B_p^{(1)} := \Bigl\{(a_u)_{u\in\mathbb Z} \;:\; \sum_{u+ps=R} a_u\,u\,s\,\ell_{s,1} = 0\ \forall R\Bigr\}.
}
\]

> **Typhinweis.** \(\ker B_p^{(1)}\) ist ein linearer Teilraum von \(K_p\). Er hängt von den
> Koeffizienten \(\ell_{s,1}\) von \(L_3^\circ\) im Primrang-1-Sektor ab. Diese Koeffizienten
> sind durch \(L_3^\circ\) bestimmt, sobald \(L_3^\circ\) explizit gegeben ist.

---

## 7. Die offene Hauptfrage

Der Abstieg \(\Delta_p^{\mathrm{adm}} \subseteq \mathcal N_{\mathrm{Wres,rel}}\) aus
NEU-221e (221e.1) wird — nach Substitution der neuen Gramform — zur Frage:

\[
\boxed{\Delta_p^{\mathrm{adm}} \subseteq \ker B_p^{(1)} \;?}
\tag{250d.\star}
\]

Dies ist das ursprüngliche Hebungsproblem in konkret berechenbarer Form.

### 7.1 Zwei Klärungsstufen

**Stufe 1 (symbolisch).** Falls \(L_3^\circ\) nur endlich viele nichtverschwindende
\(\ell_{s,1}\) besitzt, ist \(\ker B_p^{(1)}\) ein endlicher Kodimensionsraum und (250d.\(\star\))
ist ein endlichdimensionales lineares Gleichungssystem.

**Stufe 2 (kanonisch).** Der entscheidende Test nach NEU-221e §2.2 ist äquivalent zum
Test auf \(\mathcal A_p^{\mathrm{adm}}\) (falls \(0 \in \mathcal A_p^{\mathrm{adm}}\)). Die
Frage reduziert sich auf:

> Liegen die explizit zulässigen Lifterzeuger \(k \in \mathcal A_p^{\mathrm{adm}}\) in \(\ker B_p^{(1)}\)?

---

## 8. Verhältnis zu \(\mathcal N_{\mathrm{Wres,rel}}\) (neue vs.\ alte Form)

| Eigenschaft | \(\mathcal N_{\mathrm{Wres,rel}}\) (\(F^3\)/Wres) | \(\ker B_p^{(1)}\) (\(F^1\)/Frobenius) |
|---|---|---|
| Polordnung | Doppelpol (\(\zeta^2\)-Typ) | einfacher Pol (\(\zeta\)-Typ) |
| Filtrationsstufe | \(F^3 A_{\mathrm{BC}}^{\mathrm{an}}\) | \(F^1 A_{\mathrm{BC}}^{\mathrm{an}}\) |
| Grammatrix | \(\mathrm{Wres}_{\mathrm{BC}}^{(2,0)}\) | \(h_p^{(1)} = \frac1p\delta_{R,R'}\) (explizit) |
| Positivität | offen (\(?[O]\)) | bewiesen (\(\checkmark[M]\)) |
| Radikal | unbestimmt | \(\{0\}\) bewiesen |
| Abstiegskriterium | \(\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}}) \subseteq \mathcal N_{\mathrm{Wres,rel}}\) | \(\Delta_p^{\mathrm{adm}} \subseteq \ker B_p^{(1)}\) |

Da \(\ker B_p^{(1)} = P_1^{-1}(0)\) unter der primitiven Projektion, ist
\(\ker B_p^{(1)} \subseteq K_p\) ein echter Teilraum. Falls \(\mathcal N_{\mathrm{Wres,rel}} \cap K_p = K_p\)
(Wres radikal enthält den ganzen Kernraum), gilt:

\[
\ker B_p^{(1)} \subseteq \mathcal N_{\mathrm{Wres,rel}} \cap K_p,
\]

und das Kriterium (250d.\(\star\)) wäre hinreichend für (221e.1). Das ist derzeit \(?[O]\).

---

## 9. Statusbuchung

| Teilknoten | Aussage | Status |
|---|---|---|
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/1]\) | \(G^{L,p}_{R,R'}(\beta) = \delta_{R,R'}\cdot p^{-\beta}\zeta(\beta)\) für alle \(p\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/2]\) | \(G^{R,p}_{R,R'}(\beta) = \delta_{R,R'}\cdot\zeta(\beta)\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/3]\) | KMS-Konsistenz für allgemeines \(p\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/4]\) | \(h_p^{(1)}(E_R,E_{R'}) = \frac1p\delta_{R,R'}\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/5]\) | \(h_p^{(1)} > 0\), \(\operatorname{Rad}h_p^{(1)} = \{0\}\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/6]\) | \(\mathscr H_{\mathrm{rel},p}^{(1)} \cong \ell^2(\mathbb Z)\) mit \(\|E_R\|^2 = 1/p\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/7]\) | \(\|P_1\widetilde T_p^{\mathrm{raw}}(\delta)\|^2 = \frac{(\log p)^2}{p}\sum_R|\sum_{u+ps=R}a_uus\ell_{s,1}|^2\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/8]\) | Definition \(\ker B_p^{(1)}\) | \(\checkmark[M]\) |
| \([O\text{-}221\text{-}1c1a0\text{-C1a}/9]\) | Frobenius-Residuenbrücke \(E_R \mapsto \frac1{\sqrt p}\eta_R\) unabhängig von NEU-246 | \(\checkmark[M]\) |
| **\([O\text{-}221\text{-}1c1a0\text{-C1a}/10]\)** | **\(\Delta_p^{\mathrm{adm}} \subseteq \ker B_p^{(1)}\)?** | **\(?[O]\)** |
| **\([O\text{-}221\text{-}1c1a0\text{-C1a}/11]\)** | **\(\ker B_p^{(1)} \subseteq \mathcal N_{\mathrm{Wres,rel}}\)?** (Brücke zur alten Form) | **\(?[O]\)** |

Gesamtstatus:
\[
\boxed{[O\text{-}221\text{-}1c1a0\text{-C1a}]:\ \checkmark[M]_{\mathrm{part}}
\text{ — vier Hauptsätze bewiesen, Knoten 10 offen.}}
\]

---

## 10. Nächster atomarer Knoten

\[
\boxed{[O\text{-}221\text{-}1c1a0\text{-C1a}\text{/10}]:
\ \text{Bestimme } \ell_{s,1}\text{-Koeffizienten von }L_3^\circ
\ \text{und prüfe }\Delta_p^{\mathrm{adm}} \subseteq \ker B_p^{(1)}.}
\]
