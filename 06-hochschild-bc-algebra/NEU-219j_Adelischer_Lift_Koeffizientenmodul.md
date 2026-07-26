# NEU-219j — Adelischer Lift des logarithmischen Koeffizientenmoduls

**DAG-Position:** Nachfolger von NEU-219i (Commit ea69712).  
**Teilweise geschlossen:** [O-219-5e1d-corner], [O-219-5e1d1], [O-219-5e1d2] ✓[K/M].  
**Offen:** [O-219-5e1d3] konkrete $C^*$-Realisierung; [O-219-5e1d4] logarithmische Vervollständigung.  
**Freigegeben:** [O-219-5e1e-alg] algebraische Corner-Induktion von $L^{\mathrm{cup}}$.  
**Neuer Knoten:** [O-219-5e2-mult] Multiplikatorinsertion und Definitionsbereich des Gewichts.

---

## 1. Algebraischer adelischer Kern

Setze $\Gamma := \mathbb{Q}_+^\times$, $\widetilde{B} := C_0(\mathbb{A}_f)$, $(\gamma_r F)(x) = F(r^{-1}x)$.

$$
\boxed{
\widetilde{B}_{\mathrm{alg}} :=
\operatorname{span}_{\mathrm{fin}}\bigl\{\gamma_r(\iota(f)) : r\in\Gamma,\ f\in B_{\mathrm{alg}}\bigr\}.
} \tag{1.1}
$$

### Produktstabilität

Für $F = \gamma_r(\iota(f))$, $G = \gamma_s(\iota(g))$ mit Trägern $\subseteq r\widehat{\mathbb{Z}}$ bzw. $\subseteq s\widehat{\mathbb{Z}}$: Setze $t$ durch $v_p(t) = \max\{v_p(r), v_p(s)\}$, dann $k := t/r \in \mathbb{N}$, $\ell := t/s \in \mathbb{N}$, und:
$$
FG = \gamma_t\bigl(\iota(\sigma_k(f)\sigma_\ell(g))\bigr). \tag{1.2}
$$

Da $B_{\mathrm{alg}}$ unter allen $\sigma_n$ stabil ist, ist $\widetilde{B}_{\mathrm{alg}}$ eine $*$-Algebra, $\gamma$-stabil nach Konstruktion.

$$
\boxed{
\widetilde{A}_{\mathrm{alg}} := \widetilde{B}_{\mathrm{alg}} \rtimes_{\gamma,\mathrm{alg}} \Gamma.
} \tag{1.3}
$$

$$\boxed{ [O\text{-}219\text{-}5e1d0] \quad \checkmark[K/M]. }$$

---

## 2. Adelischer logarithmischer Koeffizientenkern

$$
\boxed{
\widetilde{B}^{\log} :=
\operatorname{span}_{\mathrm{fin}}\bigl\{\gamma_r(\iota(F)) : r\in\Gamma,\ F\in B^{\log}\bigr\}
\subseteq C_c(\mathbb{A}_f).
} \tag{2.1}
$$

Die Produktrechnung (1.2) gilt unverändert. Da $\sigma_k(B^{\log}) \subseteq B^{\log}$ und $B^{\log}$ eine Banach-$*$-Algebra ist:

$$
\boxed{\widetilde{B}^{\log} \text{ ist eine }\gamma\text{-stabile algebraische }*\text{-Algebra.}} \tag{2.2}
$$

$$
\boxed{\widetilde{\mathcal{A}}^{\log} := \widetilde{B}^{\log} \rtimes_{\gamma,\mathrm{alg}} \Gamma.} \tag{2.3}
$$

Elemente sind endliche Summen $\sum_r F_r U_r$ mit $F_r \in \widetilde{B}^{\log}$. Da $C_0(\mathbb{A}_f)$ nicht unital ist, sind nackte $U_r$ Multiplikatoren; Produkte $F_r U_r$ liegen im Crossed-Product selbst.

$$\boxed{ [O\text{-}219\text{-}5e1d1] \quad \checkmark[K/M]. }$$

---

## 3. Eckeneinbettung des bisherigen Moduls

Sei $e = 1_{\widehat{\mathbb{Z}}}$. Die Laca-Einbettung:
$$
j_A(f) = \iota(f), \qquad j_A(\mu_n) = U_n e.
$$

Da $M = \mathfrak{M}^{\log}_{\mathrm{glob}} \subseteq \mathcal{A}^{\log} \subseteq A_{C^*}$, liefert die Corner-Einbettung:
$$
\boxed{j_M: M \hookrightarrow e\widetilde{\mathcal{A}}^{\log}e.} \tag{3.1}
$$

Für $a,b \in A_{\mathrm{alg}}$, $m \in M$:
$$
\boxed{j_M(amb) = j_A(a)\,j_M(m)\,j_A(b).} \tag{3.2}
$$

Injektivität folgt aus der Full-Corner-Realisierung. Dies schließt die schwächste Bedeutung eines adelischen Lifts:

$$\boxed{ [O\text{-}219\text{-}5e1d\text{-corner}] \quad \checkmark[K/M]. }$$

Noch ist damit kein $\widetilde{A}_{\mathrm{alg}}$-Bimodul konstruiert, sondern nur ein $A_{\mathrm{alg}}$-Bimodul in der Ecke.

---

## 4. Warum die bloße Bimodulhülle nicht genügt

Die erste Bimodulhülle $\widetilde{M}_0 := \operatorname{span}_{\mathrm{fin}}\{x\,j_M(m)\,y : x,y \in \widetilde{A}_{\mathrm{alg}},\ m \in M\}$ ist ein $\widetilde{A}_{\mathrm{alg}}$-Bimodul.

Für den konjugierten Twist $\tau = \gamma_g \circ \widetilde{\sigma}_\beta$ gilt jedoch $\tau(e) = \gamma_g(e)$, und im geladenen Fall:
$$
\gamma_g(e) \neq e \qquad (g \neq 1).
$$

Somit verschiebt $\tau$ die Ausgangsecke: $e\widetilde{A}e \to \tau(e)\widetilde{A}\tau(e)$. Es folgt nicht automatisch $\tau(\widetilde{M}_0) = \widetilde{M}_0$. Die bloße Bimodulhülle ist kein $\tau$-äquivariantes Koeffizientenobjekt.

---

## 5. Orbit-induzierter $\tau$-äquivarianter Bimodul

Für $k \in \mathbb{Z}$ setze $e_k := \tau^k(e)$, $A_k := \tau^k(j_A(A_{\mathrm{alg}}))$, $M_k := \tau^k(j_M(M))$. Dann ist $M_k$ ein $A_k$-Bimodul. Definiere:

$$
\boxed{I_k := \widetilde{A}_{\mathrm{alg}}\,e_k \otimes_{A_k} M_k \otimes_{A_k} e_k\widetilde{A}_{\mathrm{alg}}.} \tag{5.1}
$$

$$
\boxed{\widetilde{M}_{\mathrm{orb}} := \bigoplus_{k\in\mathbb{Z}}^{\mathrm{alg}} I_k.} \tag{5.2}
$$

### $\tau$-Wirkung

$$
\widetilde{\tau}: I_k \longrightarrow I_{k+1}, \qquad
xe_k \otimes m \otimes e_k y \longmapsto \tau(x)e_{k+1} \otimes \tau(m) \otimes e_{k+1}\tau(y). \tag{5.3}
$$

Wohldefiniert auf dem balancierten Tensorprodukt, da $\tau(A_k) = A_{k+1}$, $\tau(M_k) = M_{k+1}$. Invertierbar, und:
$$
\boxed{\widetilde{\tau}(x\,\xi\,y) = \tau(x)\,\widetilde{\tau}(\xi)\,\tau(y).} \tag{5.4}
$$

Damit ist $(\widetilde{M}_{\mathrm{orb}}, \widetilde{\tau})$ ein typkorrektes $\tau$-äquivariantes $\widetilde{A}_{\mathrm{alg}}$-Bimodul.

### Rückgewinnung des ursprünglichen Moduls

Im $k=0$-Summanden: $\widetilde{A}_{\mathrm{alg}}\,e \otimes_{A_{\mathrm{alg}}} M \otimes_{A_{\mathrm{alg}}} e\,\widetilde{A}_{\mathrm{alg}} \supseteq e \otimes M \otimes e \cong M$. Einbettung:
$$
\boxed{m \longmapsto e \otimes j_M(m) \otimes e.} \tag{5.5}
$$

Injektiv. Abstrakter algebraischer $\tau$-äquivarianter Lift vollständig konstruiert:

$$\boxed{ [O\text{-}219\text{-}5e1d2] \quad \checkmark[K/M]. }$$

---

## 6. Was dadurch noch nicht erreicht ist

Der orbit-induzierte Modul ist ein abstraktes balanciertes Tensorprodukt. Noch nicht bewiesen:

**Injektivität der Gesamtrealisierung:** Die natürliche Multiplikationsabbildung
$$
\Pi_k: I_k \to \widetilde{A}_{C^*}, \qquad xe_k \otimes m \otimes e_k y \mapsto xmy, \tag{6.1}
$$
ist in ihrer Injektivität nicht formal garantiert. Ebenso ist $\Pi_k(I_k) \cap \Pi_\ell(I_\ell) \neq \{0\}$ für $k \neq \ell$ nicht ausgeschlossen.

$$\boxed{ [O\text{-}219\text{-}5e1d3]: \quad \Pi = \bigoplus_k \Pi_k \text{ injektiv?} \quad ?[O]. }$$

**Logarithmische Vervollständigung:** Eine adelische logarithmische Norm bzw. geeignete Vervollständigung ist noch nicht definiert.

$$\boxed{ [O\text{-}219\text{-}5e1d4]: \quad \text{konkreter vollständiger logarithmischer Modultyp} \quad ?[O]. }$$

---

## 7. Revidierter Gesamtstatus von [O-219-5e1d]

| Unterknoten | Inhalt | Status |
|-------------|--------|--------|
| [O-219-5e1d-corner] | Eckeneinbettung $j_M: M \hookrightarrow e\widetilde{\mathcal{A}}^{\log}e$ | ✓[K/M] |
| [O-219-5e1d1] | Adelischer log. Koeffizientenkern $\widetilde{\mathcal{A}}^{\log}$ | ✓[K/M] |
| [O-219-5e1d2] | Abstrakter $\tau$-äquivarianter Bimodul $\widetilde{M}_{\mathrm{orb}}$ | ✓[K/M] |
| **[O-219-5e1d3]** | Injektivität $\Pi: \widetilde{M}_{\mathrm{orb}} \to \widetilde{A}_{C^*}$ | **?[O]** |
| **[O-219-5e1d4]** | Logarithmische Vervollständigung | **?[O]** |

$$\boxed{ [O\text{-}219\text{-}5e1d] \quad \checkmark[M]_{\mathrm{part}}. }$$

Der algebraische Lift ist vorhanden; der konkrete analytische Lift bleibt offen.

---

## 8. Freigabe von [O-219-5e1e-alg]

Der abstrakte Modul hebt die algebraische Sperre. Freigegeben:

$$
\boxed{
[O\text{-}219\text{-}5e1e\text{-alg}]:\quad
\text{Konstruiere eine explizite Hochschild-Kettenabbildung,
die }L^{\mathrm{cup}}\text{ aus der vollen Ecke in }C^4(\widetilde{A}_{\mathrm{alg}}, \widetilde{M}_{\mathrm{orb}})\text{ überführt.}
} \quad ?[O].
$$

Separat zu prüfen:
- $b^\tau \widetilde{L} = 0$
- $\widetilde{L}|_{e(\cdot)e} = j_M \circ L^{\mathrm{cup}}$ (Corner-Kompatibilität)
- $[\widetilde{L}] \neq 0$ in $H^4(\widetilde{A}_{\mathrm{alg}}, \widetilde{M}_{\mathrm{orb}})$

Die Full-Corner-Morita-Äquivalenz liefert nicht automatisch eine konkrete Kochainformel; explizite Kettenabbildungen zwischen den Hochschildkomplexen der Ecke und der Dilatationsalgebra müssen konstruiert werden.

Gesperrt bleibt:
$$\boxed{ [O\text{-}219\text{-}5e1e\text{-conc}] \quad \text{gesperrt durch }[O\text{-}219\text{-}5e1d3/4]. }$$

---

## 9. Multiplikatorwarnung: neuer Knoten

Da $C_0(\mathbb{A}_f)$ nicht unital ist, liegt $U_{g^{-1}}$ im Allgemeinen in $M(\widetilde{A})$, nicht in $\widetilde{A}$ selbst. Die Formel
$$
\widetilde{\Phi}(a_0,\ldots,a_4) = \widetilde{\omega}\bigl(U_{g^{-1}}\,a_0\,\widetilde{L}(a_1,\ldots,a_4)\bigr)
$$
ist nur typkorrekt, wenn:
1. $a_0\,\widetilde{L}(a_1,\ldots,a_4) \in \widetilde{A}$ (Multiplikatorwirkung liefert Element von $\widetilde{A}$), und
2. $\widetilde{\omega}$ auf diesem Element definiert ist.

$$
\boxed{
[O\text{-}219\text{-}5e2\text{-mult}]:\quad
\text{Multiplikatorinsertion und Definitionsbereich des Gewichts}\quad ?[O].
}
$$

---

## 10. Revidierter DAG

| Knoten | Status |
|--------|--------|
| [O-219-5e1d-corner] | ✓[K/M] |
| [O-219-5e1d1] | ✓[K/M] |
| [O-219-5e1d2] | ✓[K/M] |
| **[O-219-5e1d3]** $\Pi$ injektiv | **?[O]** |
| **[O-219-5e1d4]** log. Vervollständigung | **?[O]** |
| **[O-219-5e1e-alg]** Corner-Induktion $L^{\mathrm{cup}}$ | **?[O] freigegeben** |
| [O-219-5e1e-conc] konkreter Lift | gesperrt durch d3/d4 |
| **[O-219-5e2-mult]** Multiplikatorinsertion | **?[O] neu** |
| [O-219-5e2] $b^\tau\widetilde{\Phi}=0$, $\lambda_\tau\widetilde{\Phi}=\widetilde{\Phi}$ | gesperrt |

```
[O-219-5e1d2]  M-orb tau-aequivariant algebraisch              [K/M]
      |
      +-- [O-219-5e1d3]  Pi injektiv?                          ?[O]
      +-- [O-219-5e1d4]  log. Vervollstaendigung               ?[O]
      |
[O-219-5e1e-alg]  Kettenabbildung L^cup -> C^4(A-tilde, M-orb) ?[O] FREIGEGEBEN
      |
      +-- Corner-Kompatibilitaet, b^tau L-tilde = 0, [L-tilde] != 0
      |
[O-219-5e2-mult]  U_{g^{-1}} Multiplikator, Def.-bereich omega  ?[O] NEU
      |
[O-219-5e2]    b^tau Phi-tilde=0, lambda_tau Phi-tilde=Phi-tilde gesperrt
```

**Naechster atomarer Schritt:** [O-219-5e1e-alg] — explizite Hochschild-Kettenabbildung aus der Ecke in $C^4(\widetilde{A}_{\mathrm{alg}}, \widetilde{M}_{\mathrm{orb}})$, parallel zu [O-219-5e2-mult].
