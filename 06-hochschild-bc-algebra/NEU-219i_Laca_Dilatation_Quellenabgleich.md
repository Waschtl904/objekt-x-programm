# NEU-219i — Laca-Dilatation: Quellenabgleich und revidierter DAG

**DAG-Position:** Nachfolger von NEU-219h (Commit 9c8bdf3).  
**Durch Literatur geschlossen:** [O-219-5e1a]\_{C^\*}, [O-219-5e1b]\_{C^\*}, [O-219-5e1c]\_{\mathrm{alg.Dyn}}.  
**Primärer offener Knoten:** [O-219-5e1d] — adelischer Lift von $\mathfrak{M}^{\log}_{\mathrm{glob}}$.  
**Neuer struktureller Befund:** Konjugierter Twist $\tau = \gamma_g \circ \widetilde{\sigma}_\beta$ als Randautomorphie.

---

## 1. [O-219-5e1a]: Automorphe Dilatation — Laca-Konstruktion

Laca konstruiert für den BC-Endomorphismus $\rho_n(f)(x) = 1_{n\widehat{\mathbb{Z}}}(x)f(x/n)$ die minimale automorphe Dilatation explizit. Setze:
$$
\widetilde{B} = C_0(\mathbb{A}_f), \qquad \Gamma = \mathbb{Q}_+^\times.
$$

Die Gruppenwirkung:
$$
\boxed{(\gamma_r F)(a) = F(r^{-1}a), \qquad r \in \mathbb{Q}_+^\times.}
$$

Jedes $\gamma_r$ ist eine Automorphie von $C_0(\mathbb{A}_f)$. Die Einbettung
$$
\iota: C(\widehat{\mathbb{Z}}) \hookrightarrow C_0(\mathbb{A}_f), \qquad
\iota(f)(a) = \begin{cases} f(a), & a \in \widehat{\mathbb{Z}}, \\ 0, & a \notin \widehat{\mathbb{Z}}, \end{cases}
$$
erfüllt die exakte Intertwining-Gleichung (stärker als die in NEU-219h nur als Kandidat formulierte Kompressionsformel):
$$
\boxed{\gamma_n(\iota(f)) = \iota(\rho_n(f)).} \tag{1}
$$

$$\boxed{ [O\text{-}219\text{-}5e1a]_{C^*} \quad \checkmark[K/M]. }$$

---

## 2. Behandlung der Rangeprojektionen

Setze $e := 1_{\widehat{\mathbb{Z}}} \in C_0(\mathbb{A}_f)$. Aus der Wirkung folgt unmittelbar:
$$
\gamma_n(e) = 1_{n\widehat{\mathbb{Z}}} = \iota(E_n). \tag{2}
$$

Da $n\widehat{\mathbb{Z}} \subseteq \widehat{\mathbb{Z}}$, gilt $\gamma_n(e) \le e$ und daher:
$$
\boxed{e\,\gamma_n(e)\,e = \gamma_n(e) = \iota(E_n).} \tag{3}
$$

Der in NEU-219h als technischer Kern benannte Punkt ist auf $C^*$-Ebene exakt gelöst: Die Nichtunitalität von $\rho_n$ erscheint als Schrumpfung des Eckprojektors unter der automorphen Gruppenwirkung, nicht als Hindernis.

---

## 3. Minimalität

$$
\boxed{ \overline{\bigcup_{n\ge1} \gamma_{1/n}\bigl(\iota(C(\widehat{\mathbb{Z}}))\bigr)} = C_0(\mathbb{A}_f). } \tag{4}
$$

Geometrisch: $\mathbb{A}_f = \bigcup_{n\ge1} \frac{1}{n}\widehat{\mathbb{Z}}$. Die Dilatation ist eindeutig minimal; die drei in NEU-219h gleichrangig genannten Kandidatenansätze (Stacey, $\mathcal{O}_\infty$-Typ, Gruppenalgebra-Vervollständigung) müssen nicht mehr separat verfolgt werden — die adelische Laca-Konstruktion ist der autoritative Ausgangspunkt.

---

## 4. [O-219-5e1b]: Crossed-Product und Full-Corner

Setze $\widetilde{A} = C_0(\mathbb{A}_f) \rtimes_\gamma \mathbb{Q}_+^\times$. Lacas Full-Corner-Satz liefert:
$$
\boxed{A_{C^*} \cong e\widetilde{A}e,} \tag{5}
$$

wobei die Ecke voll ist. Die BC-Isometrie wird durch den komprimierten Gruppenimplementierer realisiert:
$$
\boxed{\mu_n \longleftrightarrow U_n e.} \tag{6}
$$

Die $U_r$ sind echte unitäre Gruppenimplementierer: $U_r U_s = U_{rs}$, $U_r F U_r^* = \gamma_r(F)$.

$$\boxed{ [O\text{-}219\text{-}5e1b]_{C^*} \quad \checkmark[K/M]. }$$

---

## 5. [O-219-5e1c]: Grad und Modulargewicht der Implementierer

Die BC-Zeitentwicklung setzt sich kanonisch fort durch $\widetilde{\alpha}_t(F) = F$ für $F \in C_0(\mathbb{A}_f)$ und:
$$
\boxed{\widetilde{\alpha}_t(U_r) = r^{it} U_r.} \tag{7}
$$

Dies respektiert die Crossed-Product-Relation, da $r \mapsto r^{it}$ ein Gruppencharakter ist. Für $\widetilde{\sigma}_\beta = \widetilde{\alpha}_{-i\beta}$:
$$
\boxed{\widetilde{\sigma}_\beta(U_r) = r^\beta U_r.} \tag{8}
$$

Die algebraische Gruppenladung:
$$
\boxed{\deg(U_r) = r, \qquad \deg(F) = 1.} \tag{9}
$$

Kontrolle: $\widetilde{\alpha}_t(\mu_n) = \widetilde{\alpha}_t(U_n e) = n^{it} U_n e = n^{it}\mu_n$ \checkmark.

**Nicht automatisch geschlossen:** Existenz eines geeigneten KMS-Zustands oder Gewichts auf der gesamten nichtunitalen Dilatationsalgebra $\widetilde{A}$; dies ist für [O-219-5e1d] relevant.

$$\boxed{ [O\text{-}219\text{-}5e1c]_{\mathrm{alg.Dyn}} \quad \checkmark[K/M]. }$$

---

## 6. Konjugierter Twist: der neue strukturelle Befund

Der echte invertierbare Gegenladungsträger ist vorhanden: $U_{g^{-1}} \in M(\widetilde{A})$ mit:
$$
\deg(U_{g^{-1}}) = g^{-1}, \qquad \widetilde{\sigma}_\beta(U_{g^{-1}}) = g^{-\beta} U_{g^{-1}}.
$$

Für einen Kandidaten der Form
$$
\widetilde{\Phi}(a_0,\ldots,a_4) = \widetilde{\omega}\bigl(U_{g^{-1}} a_0 L(a_1,\ldots,a_4)\bigr)
$$
verschiebt $U_{g^{-1}}$ beim KMS-Rand den Twist durch Konjugation. Aus
$$
U_{g^{-1}} \tau(a) = \widetilde{\sigma}_\beta(a) U_{g^{-1}}
$$
folgt als notwendiger Randtwist:
$$
\boxed{\tau = \operatorname{Ad}(U_g) \circ \widetilde{\sigma}_\beta = \gamma_g \circ \widetilde{\sigma}_\beta.} \tag{10}
$$

**Konsequenz:** Der richtige erweiterte zyklische Kandidat verwendet nicht unverändert $\widetilde{\sigma}_\beta$, sondern den konjugierten Twist $\tau$. Modulargewicht und algebraischer Grad von $U_r$ haben — wie in NEU-219h antizipiert — entgegengesetzte Kompensationsrollen:

| Eigenschaft | $U_{g^{-1}}$ | Wirkung auf $\widetilde{\Phi}$ |
|-------------|-------------|-------------------------------|
| $\deg(U_{g^{-1}})$ | $g^{-1}$ | Neutralisiert Gesamtladung $g^{-1}$ |
| $\widetilde{\sigma}_\beta(U_{g^{-1}})$ | $g^{-\beta} U_{g^{-1}}$ | Verschiebt Randtwist zu $\tau = \gamma_g \circ \widetilde{\sigma}_\beta$ |

---

## 7. Offene Knoten

### [O-219-5e1d]: Adelischer Lift des logarithmischen Koeffizientenmoduls

**Status: ?[O] primär**

Benötigt: $\widetilde{A}$-Bimodul $\widetilde{M}$ und typkorrekte Einbettung $j_M: \mathfrak{M}^{\log}_{\mathrm{glob}} \longrightarrow \widetilde{M}$. Zu prüfen:
$$
j_M(amb) = j_A(a)\,j_M(m)\,j_A(b), \qquad
\widetilde{\sigma}_\beta(j_M(m)) = j_M(\sigma_\beta(m)).
$$

Natürlicher Kandidat für $\widetilde{M}$:
$$
\widetilde{M} = \overline{\operatorname{span}_{\mathrm{fin}}\{x\,m\,y : x,y \in \widetilde{A}_{\mathrm{alg}},\ m \in M\}},
$$
doch Stabilität, logarithmischer Typ und geeignete Vervollständigung sind zu beweisen. Die Full-Corner-/Morita-Äquivalenz allein gibt nicht ohne Typaudit die gewünschte konkrete Kochainformel.

$$\boxed{ [O\text{-}219\text{-}5e1d] \quad ?[O]. }$$

### [O-219-5e1e]: Lift der Klasse $[L^{\mathrm{cup}}]$

**Status: gesperrt durch [O-219-5e1d]**

Induktion der Hochschildklasse in die Dilatation; der Nichttrivialitätserhalt unter Restriktion muss separat auditiert werden.

$$\boxed{ [O\text{-}219\text{-}5e1e] \quad \text{gesperrt durch }[O\text{-}219\text{-}5e1d]. }$$

### [O-219-5e2]: Zyklischer Rand, Rotation, Paarung

**Status: gesperrt durch [O-219-5e1e]**

$$
\boxed{ [O\text{-}219\text{-}5e2]: \quad b^\tau \widetilde{\Phi} = 0, \quad \lambda_\tau \widetilde{\Phi} = \widetilde{\Phi}, \quad \widetilde{\Phi} \neq 0. }
$$

---

## 8. Revidierter DAG

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5e1a]\_{C^\*} | Laca-Dilatation $(C_0(\mathbb{A}_f), \gamma, \iota, e)$ | ✓[K/M] |
| [O-219-5e1b]\_{C^\*} | $C_0(\mathbb{A}_f) \rtimes_\gamma \mathbb{Q}_+^\times$, Full-Corner | ✓[K/M] |
| [O-219-5e1c]\_{\mathrm{alg.Dyn}} | $\deg(U_r) = r$, $\widetilde{\sigma}_\beta(U_r) = r^\beta U_r$ | ✓[K/M] |
| **[O-219-5e1d]** | Lift $j_M$, $\widetilde{M}$, $\tau = \gamma_g \circ \widetilde{\sigma}_\beta$ | **?[O] primär** |
| [O-219-5e1e] | Lift $[L^{\mathrm{cup}}]$, Nichttrivialität | gesperrt |
| [O-219-5e2] | $b^\tau\widetilde{\Phi}=0$, $\lambda_\tau\widetilde{\Phi}=\widetilde{\Phi}$, Paarung | gesperrt |

```
[O-219-5e1a]  C_0(A_f), gamma_r(F)(a)=F(r^{-1}a), iota, e=1_{Z-hat}   [K/M]
      |
[O-219-5e1b]  A-tilde = C_0(A_f) x|_gamma Q+^x, Full-Corner           [K/M]
      |
[O-219-5e1c]  deg(U_r)=r, sigma-tilde_beta(U_r)=r^beta U_r             [K/M]
      |
      +--> tau = gamma_g circ sigma-tilde_beta  (neuer struktureller Befund)
      |
[O-219-5e1d]  j_M: M -> M-tilde, A-tilde-Bimodul, Lift L-cup           ?[O] PRIMAER
      |
[O-219-5e1e]  Induktion [L^cup], Nichttrivialitaet unter Restriktion    gesperrt
      |
[O-219-5e2]   b^tau Phi-tilde = 0, lambda_tau Phi-tilde = Phi-tilde     gesperrt
```

**Primaerer naechster Audit:** [O-219-5e1d] — adelischer Lift von $\mathfrak{M}^{\log}_{\mathrm{glob}}$ und Verträglichkeit mit dem konjugierten Twist $\tau = \gamma_g \circ \widetilde{\sigma}_\beta$.
