# NEU-219l — Exakter algebraischer Eckkern der adelischen Dilatation

**DAG-Position:** Nachfolger von NEU-219k (Commit 99af09b).  
**Geschlossen:** [O-219-5e1e-corner-core] ✓[K/M].  
**Negativer Quellenaudit:** „Die exakte algebraische Eckgleichheit folgt bereits aus Laca" ✓[M]$_{\mathrm{neg,Quelle}}$.  
**Neuer primärer Knoten:** [O-219-5e1f-orbit-directness].

---

## 0. Ergebnis

$$
\boxed{ e\,\widetilde{A}_{\mathrm{alg}}\,e = j_A(A_{\mathrm{alg}}). } \tag{0.1}
$$

Exakte Normalform für vollständig gekürztes $r = a/b$, $s = m/n$, $f \in B_{\mathrm{alg}}$, $L = \operatorname{lcm}(a,m)$, $q = L/m$, $N = bL/a$:

$$
\boxed{
e\,\gamma_{a/b}(\iota(f))\,U_{m/n}\,e
= j_A\!\left(\mu_m\,\rho_{L/m}\!\left(\sigma_{bL/a}(f)\right)\mu_n^*\right).
} \tag{0.2}
$$

Die Kompression ist genau dann nicht null, wenn $\sigma_{bL/a}(f) \neq 0$, äquivalent: $f|_{N\widehat{\mathbb{Z}}} \not\equiv 0$.

**Warnbeispiel.** Für $N > 1$ ist $f = 1 - E_N$ nichtnull, aber $\sigma_N(1-E_N) = 0$. Die Nichtnull-Bedingung ist nicht bloß $f \neq 0$.

$$\boxed{ [O\text{-}219\text{-}5e1e\text{-corner-core}] \quad \checkmark[K/M]. }$$

---

## 1. Konventionen

$$
(\gamma_r F)(x) = F(r^{-1}x), \qquad U_r F = \gamma_r(F) U_r, \qquad F U_r = U_r \gamma_{r^{-1}}(F). \tag{1.1}
$$

Für $f \in C(\widehat{\mathbb{Z}})$: $\iota(f)(x) = f(x)$ für $x \in \widehat{\mathbb{Z}}$, $0$ sonst; $e = \iota(1) = 1_{\widehat{\mathbb{Z}}}$.

Für $k \in \mathbb{N}^\times$:
$$
\gamma_k(\iota(f)) = \iota(\rho_k(f)), \tag{1.2}
$$
da beide Seiten auf $\widehat{\mathbb{Z}}$ den Wert $1_{k\widehat{\mathbb{Z}}}(x)f(x/k)$ haben und außerhalb verschwinden.

Für $r \in \mathbb{Q}_+^\times$: $\operatorname{supp}\,\gamma_r(\iota(f)) \subseteq r\widehat{\mathbb{Z}}$. $\tag{1.3}$

---

## 2. Rationaler Teilbarkeitsverband

Für $r, t \in \mathbb{Q}_+^\times$ definiere $r \vee t$ durch:
$$
v_p(r \vee t) = \max\{v_p(r), v_p(t)\} \quad \text{für jede Primzahl } p. \tag{2.1}
$$

Dann $r\widehat{\mathbb{Z}} \cap t\widehat{\mathbb{Z}} = (r \vee t)\widehat{\mathbb{Z}}$, und $(r \vee t)/r,\; (r \vee t)/t \in \mathbb{N}^\times$. $\tag{2.2}$

Für vollständig gekürztes $r = a/b$, $s = m/n$:
$$
1 \vee r \vee s = \operatorname{lcm}(a,m) \in \mathbb{N}^\times. \tag{2.4}
$$

*Beweis.* Die $p$-Komponente von $\widehat{\mathbb{Z}}$ erzwingt alle negativen Bewertungen auf null; übrig bleiben die positiven Primexponenten der gekürzten Zähler $a$ und $m$. $\square$

---

## 3. Exakte Produktformel

**Satz 3.1.** Für $r, t \in \mathbb{Q}_+^\times$, $f, h \in B_{\mathrm{alg}}$, $\ell = r \vee t$, $A = \ell/r$, $C = \ell/t$:
$$
\boxed{
\gamma_r(\iota(f))\,\gamma_t(\iota(h)) = \gamma_\ell\!\left(\iota\!\left(\sigma_A(f)\sigma_C(h)\right)\right).
} \tag{3.1}
$$

*Beweis.* Beide Seiten sind außerhalb $\ell\widehat{\mathbb{Z}}$ null. Für $x = \ell y$, $y \in \widehat{\mathbb{Z}}$: LHS$(x) = f(r^{-1}\ell y)h(t^{-1}\ell y) = f(Ay)h(Cy) = \sigma_A(f)(y)\sigma_C(h)(y)$ = RHS$(x)$. Da $B_{\mathrm{alg}}$ unter $\sigma_A$, $\sigma_C$ und Multiplikation stabil ist, liegt der Koeffizient in $B_{\mathrm{alg}}$. $\square$

**Korollar 3.2.** $\widetilde{B}_{\mathrm{alg}}$ ist eine $*$-Algebra, $\gamma$-stabil, und:
$$
\gamma_r(\iota(f))U_t \cdot \gamma_s(\iota(h))U_u = \gamma_{r \vee st}(\iota(\cdots))U_{su}, \tag{3.3}
$$
$$
(\gamma_r(\iota(f))U_s)^* = \gamma_{s^{-1}r}(\iota(f^*))U_{s^{-1}}. \tag{3.4}
$$

---

## 4. Allgemeine Eckkompression

Seien $r = a/b$, $s = m/n$ vollständig gekürzt. Setze:
$$
L = 1 \vee r \vee s = \operatorname{lcm}(a,m), \qquad N = \frac{L}{r} = \frac{bL}{a} \in \mathbb{N}^\times. \tag{4.1–4.2}
$$

**Satz 4.1.** Für jedes $f \in B_{\mathrm{alg}}$:
$$
\boxed{
e\,\gamma_r(\iota(f))\,U_s\,e = \gamma_L\!\left(\iota(\sigma_N(f))\right)U_s.
} \tag{4.3}
$$

*Beweis.* $U_s e = \gamma_s(e)U_s$, also $e\,\gamma_r(\iota(f))\,\gamma_s(e)\,U_s$. Die drei Diagonalfaktoren haben gemeinsamen Träger $(1 \vee r \vee s)\widehat{\mathbb{Z}} = L\widehat{\mathbb{Z}}$. Für $x = Ly$, $y \in \widehat{\mathbb{Z}}$: der Diagonalfaktor hat Wert $f(r^{-1}Ly) = f(Ny) = \sigma_N(f)(y)$, also $= \gamma_L(\iota(\sigma_N(f)))$. $\square$

**Korollar 4.2.** $e\,\gamma_r(\iota(f))\,U_s\,e \neq 0 \iff \sigma_N(f) \neq 0 \iff f|_{N\widehat{\mathbb{Z}}} \not\equiv 0$.

---

## 5. BC-Normalform

Setze $v_k := eU_ke$ für $k \in \mathbb{N}^\times$:
$$
v_k = U_ke = \gamma_k(e)U_k, \quad v_k^* = eU_{k^{-1}}, \quad v_k^*v_k = e, \quad v_kv_k^* = \gamma_k(e) = \iota(E_k). \tag{5.1–5.3}
$$

Eckeneinbettung: $j_A(f) = \iota(f)$, $j_A(\mu_k) = v_k$.

**Lemma 5.1.** Für $m, n \in \mathbb{N}^\times$, $k \in B_{\mathrm{alg}}$:
$$
\boxed{j_A(\mu_m k \mu_n^*) = \gamma_m(\iota(k))U_{m/n}.} \tag{5.5}
$$

**Satz 5.2 (Explizite BC-Normalform).** Mit $q = L/m \in \mathbb{N}^\times$:
$$
\boxed{
e\,\gamma_{a/b}(\iota(f))\,U_{m/n}\,e
= j_A\!\left(\mu_m\,\rho_q\!\left(\sigma_N(f)\right)\mu_n^*\right)
= j_A\!\left(\mu_m\,\rho_{L/m}\!\left(\sigma_{bL/a}(f)\right)\mu_n^*\right).
} \tag{5.7–5.8}
$$

*Beweis.* Da $L = mq$: $\gamma_L(\iota(\sigma_N(f))) = \gamma_m(\gamma_q(\iota(\sigma_N(f)))) = \gamma_m(\iota(\rho_q(\sigma_N(f))))$ via (1.2). Einsetzen in (4.3) und anwenden von Lemma 5.1 ergibt (5.7). $\square$

**Bemerkung 5.3.** $\rho_q(\sigma_N(f))$ liegt im Rangeideal $E_q B_{\mathrm{alg}}$; der Träger $L\widehat{\mathbb{Z}} = mq\widehat{\mathbb{Z}}$ wird exakt kodiert.

---

## 6. Beweis der Eckgleichheit

**Satz 6.1.** $e\,\widetilde{A}_{\mathrm{alg}}\,e = j_A(A_{\mathrm{alg}})$.

**Erste Inklusion** $j_A(A_{\mathrm{alg}}) \subseteq e\widetilde{A}_{\mathrm{alg}}e$: Nach Lemma 5.1 gilt $j_A(\mu_m f \mu_n^*) = \gamma_m(\iota(f))U_{m/n}$. Da $\operatorname{supp}\,\gamma_m(\iota(f)) \subseteq m\widehat{\mathbb{Z}} \subseteq \widehat{\mathbb{Z}}$, liegt dieser Ausdruck in der Ecke.

**Zweite Inklusion** $e\widetilde{A}_{\mathrm{alg}}e \subseteq j_A(A_{\mathrm{alg}})$: Jedes komprimierte Monom $e\,\gamma_r(\iota(f))U_s\,e$ besitzt nach Satz 5.2 die BC-Normalform $j_A(\mu_m\,\rho_{L/m}(\sigma_{bL/a}(f))\,\mu_n^*)$, liegt also in $j_A(A_{\mathrm{alg}})$. $\square$

---

## 7. Negativer Quellenaudit

Lacas Theorem 2.2.1 und Proposition 3.2.1 beweisen auf $C^*$-Ebene $A_{C^*} \cong e\widetilde{A}e$ (volle Ecke). Sie arbeiten mit $C^*$-Abschlüssen und normdichten Spannräumen.

Die exakte algebraische Kerngleichheit $e\widetilde{A}_{\mathrm{alg}}e = j_A(A_{\mathrm{alg}})$ hängt von der konkreten Definition $\widetilde{B}_{\mathrm{alg}} = \operatorname{span}_{\mathrm{fin}}\{\gamma_r(\iota(f))\}$ ab und wurde erst durch die Monomrechnung der Abschnitte 2–6 bewiesen.

$$
\boxed{ \text{„Laca allein beweist die exakte algebraische Eckidentität"} \quad \checkmark[M]_{\mathrm{neg,Quelle}}. }
$$

---

## 8. Algebraische Vollheit

**Satz 8.1.** $\widetilde{A}_{\mathrm{alg}}\,e\,\widetilde{A}_{\mathrm{alg}} = \widetilde{A}_{\mathrm{alg}}$.

*Beweis.* Für das spannendes Monom $x = \gamma_r(\iota(f))U_s$:
$$
(U_r e) \cdot e \cdot (\iota(f)U_{r^{-1}s}) = U_r\iota(f)U_{r^{-1}s} = \gamma_r(\iota(f))U_s = x. \tag{8.3}
$$
Kein Normdichteargument verwendet. $\square$

---

## 9. Lokale Einheiten

**Satz 9.1.** $\widetilde{A}_{\mathrm{alg}}$ besitzt zweiseitige lokale Einheiten aus Projektionen $p_t := \gamma_t(e) = 1_{t\widehat{\mathbb{Z}}}$, $t \in \mathbb{Q}_+^\times$.

*Beweis.* Für endlich viele Monome $x_i = F_i U_{s_i}$: Wähle $t$ so, dass $\operatorname{supp}(F_i) \subseteq t\widehat{\mathbb{Z}}$ und $s_i^{-1}\operatorname{supp}(F_i) \subseteq t\widehat{\mathbb{Z}}$ für alle $i$. Dann $p_t x_i = x_i = x_i p_t$. $\square$

---

## 10. Konkreter algebraischer Morita-Kontext

Setze $R := \widetilde{A}_{\mathrm{alg}}$, $B := eRe = j_A(A_{\mathrm{alg}})$, $P := Re$, $Q := eR$.

Die Morita-Paarungen:
$$
P \otimes_B Q \to R, \quad p \otimes q \mapsto pq \quad \text{(surjektiv wegen } ReR = R\text{)}, \tag{10.2}
$$
$$
Q \otimes_R P \to B, \quad q \otimes p \mapsto qp \quad \text{(surjektiv wegen } e \in eR,\, b = be \in Re\text{)}. \tag{10.3}
$$

Die konkreten Morita-Bimodule sind:
$$
\boxed{{}_R(\widetilde{A}_{\mathrm{alg}}\,e)_B} \qquad \text{und} \qquad \boxed{{}_B(e\,\widetilde{A}_{\mathrm{alg}})_R.}
$$

---

## 11. Orbit-induzierter Koeffizientenmodul

Für $\tau = \operatorname{Ad}(U_g) \circ \widetilde{\sigma}_\beta$ gilt $\tau(R) = R$. Setze $e_k = \tau^k(e)$, $A_k = \tau^k(B)$, $M_k = \tau^k(j_M(M))$.

Aus der Eckgleichheit folgt $A_k = e_k R e_k$ für jedes $k \in \mathbb{Z}$. Da $\tau$ Automorphismus und $e$ voll: $Re_kR = R$. $\tag{11.2–11.3}$

$$
\boxed{
\widetilde{M}_{\mathrm{orb}} = \bigoplus_{k \in \mathbb{Z}}^{\mathrm{alg}} \operatorname{Ind}_{e_k}(M_k),
\quad
\operatorname{Ind}_{e_k}(M_k) := Re_k \otimes_{A_k} M_k \otimes_{A_k} e_kR.
} \tag{11.5}
$$

Jeder Summand ist standardmäßig zweiseitig Morita-induziert aus der vollen Ecke $A_k \subseteq R$.

**11.1 Keine kanonische Reduktion auf einen Summanden.** Eine Reduktion würde zusätzliche $\tau$-Linearisierungsdaten benötigen, die eine semilineare Verschiebungsstruktur und eine Kozyklusbedingung erfüllen. Status: gesperrt, nicht widerlegt.

---

## 12. Schärfung der Multiplikationsrealisierung

Setze $N_k := RM_kR \subseteq \widetilde{\mathcal{A}}^{\log}$.

**Satz 12.1.** $\Pi_k: I_k \xrightarrow{\cong} N_k$ ist ein Isomorphismus von $R$-Bimodulen.

*Beweis.* Surjektivität: Definition. Für die Injektivität: $e_k N_k e_k = A_k M_k A_k = M_k$ (da $M_k$ unitaler $A_k$-Bimodul). Eckkompression: $e_k I_k e_k \cong M_k$. Unter dieser Identifikation ist $e_k \Pi_k e_k = \mathrm{id}_{M_k}$, also $\ker\Pi_k \cap e_k(\cdot)e_k = 0$. Da $e_k$ voll, für $\xi \in \ker\Pi_k$ mit lokaler Einheit $u = \sum_j a_j e_k b_j$: $\xi = u\xi u = 0$. $\square$

**Korollar 12.2.** Die globale Multiplikationsabbildung $\Pi: \bigoplus_k I_k \to \widetilde{\mathcal{A}}^{\log}$ ist injektiv genau dann, wenn:
$$
\boxed{
\Pi \text{ injektiv} \iff \sum_{k \in \mathbb{Z}} N_k \text{ ist algebraisch direkte Summe in } \widetilde{\mathcal{A}}^{\log}.
} \tag{12.8}
$$

Äquivalent: $\sum_{k \in F} x_k = 0$, $x_k \in N_k$, $F$ endlich $\Rightarrow x_k = 0\; \forall k$.

---

## 13. DAG-Status

**Geschlossen:**

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5e1e-corner-core] | $e\widetilde{A}_{\mathrm{alg}}e = j_A(A_{\mathrm{alg}})$, lcm-Normalform | ✓[K/M] |
| Algebraische Vollheit | $ReR = R$ direkt bewiesen | ✓[M] |
| Lokale Einheiten | $p_t = \gamma_t(e)$ zweiseitig | ✓[K/M] |
| Morita-Kontext | $Re$, $eR$ konkret | ✓[K/M] |
| $\Pi_k$ injektiv | jeder Orbit-Summand treu | ✓[K/M] |

**Negativer Quellenaudit:** „Laca allein beweist algebraische Eckgleichheit" ✓[M]$_{\mathrm{neg,Quelle}}$.

**Weiter offen:**

$$\boxed{ [O\text{-}219\text{-}5e1f\text{-orbit-directness}]: \quad \sum_{k \in \mathbb{Z}} N_k \stackrel{?}{=} \bigoplus_{k}^{\mathrm{alg}} N_k \text{ in } \widetilde{\mathcal{A}}^{\log}. }$$

---

## 14. Nächster atomarer Schritt: Orbit-Separatoren

Für eine endliche Relation $\sum_{k \in F} x_k = 0$, $x_k \in N_k$, ist ein Separator zu suchen, der den Orbitindex $k$ erkennt. Kandidaten (einzeln typzuprüfen):

- **Adelische Träger-/Bewertungsfiltrationen** der Ecken $e_k = \gamma_{g^k}(e)$
- **$\tau$-Spektral- oder Laurent-Grad** (nicht mit der $\mathbb{Q}_+^\times$-Gradierung verwechseln)
- **Eckkompressionen** $e_j(\cdot)e_j$: falls $e_j N_k e_j = 0$ für $j \neq k$, liefert das den Separator
- **KMS- oder modulare Gewichte**, sofern auf $N_k$ definiert
- **Überlappungszeuge** $0 \neq x \in N_k \cap \sum_{j \neq k} N_j$ als mögliche Gegenzeuge

Da $\tau$ die $\mathbb{Q}_+^\times$-Gruppenladung durch $g^\beta$-Streckung verändert, ist die Ladungsgradierung allein kein ausreichender Separator. Die Eckkompressionen $e_j(\cdot)e_j$ sind der vielversprechendste erste Kandidat.
