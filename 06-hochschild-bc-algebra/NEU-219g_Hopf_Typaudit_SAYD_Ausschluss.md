# NEU-219g — Direktaudit des Hopf-zyklischen Pfades

**DAG-Position:** Nachfolger von NEU-219f (Commit 630e755).  
**Abgeschlossen:** [O-219-5d1a] ✓[K/M]; [O-219-5d1b] ✓[M]$_{\mathrm{neg}}$; [O-219-5d1c] ✓[K/M]; [O-219-5d2a] ✓[K/M]; [O-219-5d2b] ✓[M]$_{\mathrm{neg}}$.  
**Neuer offener Knoten:** [O-219-5d3] nichtstandardmäßiger $A$-relativer Hopf-Koeffizient.  
**Primärer nächster Pfad:** [O-219-5e1] Dilatationsalgebra.

---

## 1. Gesamturteil

$$
\boxed{
\text{Die }\mathbb{Q}_+^\times\text{-Gradierung von }A_{\mathrm{alg}}
\text{ definiert kanonisch eine }\mathcal{H}\text{-Koaktion, keine }\mathcal{H}\text{-Aktion.}
}
$$

Eine typkorrekte minimale Hopf-Aktion erhält man durch
$$
\boxed{\mathcal{H}_\beta := \mathbb{C}[t,t^{-1}] \cong \mathbb{C}[\mathbb{Z}],}
$$
wobei $t$ durch $\sigma_\beta = \alpha_{-i\beta}$ wirkt. Über $\mathcal{H}_\beta$ existieren eindimensionale SAYD-Module, aber es existiert **kein** SAYD-Koeffizient, der gleichzeitig den KMS-Twist $\sigma_\beta$ erzeugt und die Ladung $g^{-\beta}$ kompensiert. Der Ausschluss folgt aus der SAYD-Stabilität — dies ist die Hopf-algebraische Form der früheren Ladungsobstruktion.

$$\boxed{\text{Der Standard-Hopf-SAYD-Pfad reformuliert die Ladungsobstruktion, beseitigt sie aber nicht.}}$$

---

## 2. Natürliche Struktur aus der Gradierung: Komodulalgebra

Setze $\Gamma := \mathbb{Q}_+^\times$, $\mathcal{H}_\Gamma := \mathbb{C}[\Gamma]$ mit gruppenartigen Elementen $u_h$:
$$
\Delta(u_h) = u_h \otimes u_h, \quad \varepsilon(u_h) = 1, \quad S(u_h) = u_{h^{-1}}.
$$

Aus der BC-Gradierung $A_{\mathrm{alg}} = \bigoplus_{h\in\Gamma} A_h$ entsteht kanonisch die Rechtskoaktion:
$$
\boxed{
\delta_A: A_{\mathrm{alg}} \longrightarrow A_{\mathrm{alg}} \otimes \mathcal{H}_\Gamma,
\qquad \delta_A(a_h) = a_h \otimes u_h.
} \tag{2.1}
$$

Denn $\delta_A(a_h b_k) = a_h b_k \otimes u_{hk} = (a_h \otimes u_h)(b_k \otimes u_k)$. Ebenso für $M$. Für eine Gruppenalgebra ist eine Komodulstruktur genau eine Gruppengraduierung.

$$\boxed{ [O\text{-}219\text{-}5d1a]: \quad A_{\mathrm{alg}}, M \text{ als }\mathcal{H}_\Gamma\text{-Komodulstrukturen} \quad \checkmark[K/M]. }$$

---

## 3. Warum daraus keine Modulalgebra folgt

Eine linke $\mathcal{H}_\Gamma$-Modulalgebra erfordert $\gamma: \Gamma \to \mathrm{Aut}_{\mathrm{alg}}(A_{\mathrm{alg}})$. Die Gradierung gibt eine solche Wirkung nicht vor; sie kodiert lediglich Grade. Aus einem Charakter $\chi: \Gamma \to \mathbb{C}^\times$ erhält man $\gamma_\chi(a_h) = \chi(h)a_h$, aber die handelnde Gruppe ist die **Charaktergruppe** von $\Gamma$, nicht $\Gamma$ selbst.

Eine $\Gamma$-Wirkung auf die Gradkomponenten benötigt einen Bicharakter $B: \Gamma \times \Gamma \to \mathbb{C}^\times$ durch $u_r \triangleright a_h = B(r,h)a_h$ — zusätzliche Struktur, die nicht aus der BC-Gradierung folgt.

$$\boxed{ [O\text{-}219\text{-}5d1b] \quad \checkmark[M]_{\mathrm{neg}}. }$$

Dies ist kein Ausschluss aller künstlich gewählten $\mathbb{C}[\Gamma]$-Aktionen.

---

## 4. Minimaler reparierter Hopf-Typ: $\mathcal{H}_\beta = \mathbb{C}[\mathbb{Z}]$

Für den KMS-Pfad wird nur die einzelne Automorphie $\sigma_\beta$ benötigt. Definiere:
$$
\boxed{\mathcal{H}_\beta := \mathbb{C}[t,t^{-1}] \cong \mathbb{C}[\mathbb{Z}]} \tag{4.1}
$$
mit $\Delta(t) = t \otimes t$, $\varepsilon(t) = 1$, $S(t) = t^{-1}$, und Wirkung:
$$
\boxed{t^k \triangleright a_h := h^{k\beta} a_h = \sigma_\beta^k(a_h).} \tag{4.2}
$$

Verifikation der Modulalgebraeigenschaft:
$$
t^k \triangleright (a_h b_s) = (hs)^{k\beta} a_h b_s = (h^{k\beta} a_h)(s^{k\beta} b_s) = (t^k \triangleright a_h)(t^k \triangleright b_s), \qquad t^k \triangleright 1 = 1.
$$

$$\boxed{ [O\text{-}219\text{-}5d1c]: \quad A_{\mathrm{alg}} \text{ als }\mathcal{H}_\beta\text{-Modulalgebra} \quad \checkmark[K/M]. }$$

Der ursprüngliche Knoten [O-219-5d1] ist nur nach dem Hopf-Typwechsel $\mathbb{C}[\Gamma] \rightsquigarrow \mathbb{C}[\mathbb{Z}]$ positiv geschlossen.

---

## 5. Eindimensionale SAYD-Module über $\mathcal{H}_\beta$

Sei $E = \mathbb{C}\mathbf{e}$ mit Rechtsmodul- und Linkskomodulstruktur:
$$
\mathbf{e} \cdot t^k = c^k \mathbf{e} \quad (c \in \mathbb{C}^\times), \qquad
\lambda(\mathbf{e}) = t^r \otimes \mathbf{e} \quad (r \in \mathbb{Z}). \tag{5.1/5.2}
$$

Die SAYD-Stabilitätsbedingung (für Gruppenalgebra: $s$-Grad-Komponente, Wirkung von $s$ = Identität):
$$
\boxed{c^r = 1.} \tag{5.3}
$$

Abstrakt viele eindimensionale SAYD-Linien existieren ($r=0$, beliebiges $c$).
$$\boxed{ [O\text{-}219\text{-}5d2a]: \quad \text{abstrakte eindimensionale SAYD-Linien} \quad \checkmark[K/M]. }$$

---

## 6. Welche Koaktion den KMS-Twist erzeugt

Im Hopf-zyklischen Operator wirkt auf dem letzten Argument der Faktor $S^{-1}(\mathbf{e}_{(-1)})$. Für $\lambda(\mathbf{e}) = t^r \otimes \mathbf{e}$ ist dies $S^{-1}(t^r) = t^{-r}$. Der letzte Randterm soll $\sigma_\beta = t \triangleright (-)$ enthalten. Daher:
$$
t^{-r} = t \implies \boxed{r = -1.} \tag{6.1}
$$

Die benötigte SAYD-Koaktion ist:
$$
\boxed{\lambda(\mathbf{e}) = t^{-1} \otimes \mathbf{e}.} \tag{6.2}
$$

---

## 7. Welche Modulwirkung die Ladung kompensiert

Das Kandidatenfunktional $\widehat{\Phi}_{\beta,\chi}(\mathbf{e} \otimes a_0 \otimes \cdots \otimes a_4) := \Phi_{\beta,\chi}(a_0,\ldots,a_4)$ trägt auf dem Träger $h_0 h_1 h_2 h_3 h_4 = g^{-1}$ (wegen Ladung $g$ von $L$ und KMS-Gewichtsauslöschung). Hopf-Linearität verlangt, dass der diagonale Skalierungsfaktor $c \cdot (h_0 h_1 h_2 h_3 h_4)^{-\beta} = c \cdot g^\beta$ gleich $1$ ist. Also:
$$
\boxed{c = g^{-\beta}.} \tag{7.3}
$$

---

## 8. SAYD-Stabilität versus Ladungskompensation: Der Widerspruch

KMS-Randstruktur (Abschnitt 6) verlangt $r = -1$.

SAYD-Stabilität (5.3) verlangt dann $c^{-1} = 1$, also:
$$
\boxed{c = 1.} \tag{8.1}
$$

Ladungskompensation (Abschnitt 7) verlangt $c = g^{-\beta}$.

Beide Bedingungen gleichzeitig würden $g^{-\beta} = 1$ erzwingen — für $g \neq 1$, $\beta > 0$ unmöglich.

$$
\boxed{
\text{Es existiert kein eindimensionaler SAYD-Koeffizient,
der zugleich den KMS-Twist und die Ladung }g\neq1\text{ trägt.}
} \tag{8.2}
$$

$$\boxed{ [O\text{-}219\text{-}5d2b] \quad \checkmark[M]_{\mathrm{neg}}. }$$

---

## 9. Die beiden einzeln möglichen, aber unzureichenden Linien

### 9.1 Ladungslinie mit trivialer Koaktion ($r=0$, $c=g^{-\beta}$)

Gültiges SAYD-Modul, aber triviale Koaktion $\Rightarrow$ kein $\sigma_\beta$-Twist im letzten Randterm. Verbleibender Defekt im Hochschildrand:
$$
(b\Phi)(a_0,\ldots,a_5) = \omega_{\beta,\chi}(xa_5) - \omega_{\beta,\chi}(a_5 x)
= \omega_{\beta,\chi}(\sigma_\beta(a_5)x) - \omega_{\beta,\chi}(a_5 x) \neq 0.
$$

$$\boxed{\text{triviale Koaktion + Ladungscharakter} \quad \checkmark[M]_{\mathrm{neg}}.}$$

### 9.2 KMS-Twistlinie ohne Ladungscharakter ($r=-1$, $c=1$)

SAYD-Stabilität und KMS-Twist kompatibel, aber Hopf-Equivarianz scheitert auf dem geladenen Träger: diagonaler Skalar $g^\beta \neq 1$.

$$\boxed{\text{KMS-Koaktion + trivialer Charakter} \quad \checkmark[M]_{\mathrm{neg}}.}$$

---

## 10. Der Ausschluss ist nicht blou00df eindimensional

Für $\mathbb{C}[\mathbb{Z}]$ ist ein SAYD-Modul $\mathbb{Z}$-graduiert. Auf einem homogenen Vektor vom Grad $s$ erzwingt Stabilität $s \cdot \mathbf{e} = \mathbf{e}$. Um $\sigma_\beta$ im letzten Randterm zu erzeugen, muss der Koeffizientenvektor homogen vom Grad $t^{-1}$ sein, was $t^{-1} \cdot \mathbf{e} = \mathbf{e}$ und damit $t \cdot \mathbf{e} = \mathbf{e}$ erzwingt. Dies widerspricht $t \cdot \mathbf{e} = g^{-\beta}\mathbf{e}$ für $g \neq 1$.

$$
\boxed{
\text{Kein homogener SAYD-Koeffizientenvektor kann gleichzeitig
den reinen KMS-Twist und die nichttriviale Ladung kompensieren.}
} \tag{10.1}
$$

Höherdimensionale SAYD-Module würden im zyklischen Operator eine Summe verschiedener Twists erzeugen, nicht den einzelnen bereits bewiesenen Rand $b^{\sigma_\beta}\Phi = 0$.

---

## 11. Revidierter DAG-Status

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-5d1a] | $\mathcal{H}_\Gamma$-Komodulstruktur aus Gradierung | ✓[K/M] |
| [O-219-5d1b] | Kanonische $\mathcal{H}_\Gamma$-Modulalgebra | ✓[M]$_{\mathrm{neg}}$ |
| [O-219-5d1c] | $\mathcal{H}_\beta = \mathbb{C}[\mathbb{Z}]$ wirkt durch $\sigma_\beta$ | ✓[K/M] |
| [O-219-5d2a] | Abstrakte eindimensionale SAYD-Linien | ✓[K/M] |
| **[O-219-5d2b]** | SAYD-Linie mit KMS-Twist **und** Ladung $g$ | **✓[M]$_{\mathrm{neg}}$** |
| **[O-219-5d3]** | Nichtstandardmäßiger $A$-relativer Hopf-Koeffizient | **?[O]** |
| **[O-219-5e1]** | Dilatationsalgebra mit invertierbarem $u_g$ | **?[O] primär** |

```
[O-219-5d1c]  H_beta = C[Z] Modulalgebra                  [K/M]
      |
[O-219-5d2a]  abstrakte SAYD-Linien                       [K/M]
      |
[O-219-5d2b]  SAYD: KMS-Twist + Ladung g gleichzeitig     [M]_neg
      |        (SAYD-Stabilitaet = Ladungsobstruktion)
      |
      +-- [O-219-5d3]  A-relativer Hopf-Koeffizient        ?[O]
      |
[O-219-5e1]   Dilatationsalgebra, u_g invertierbar         ?[O] PRIMAER
      |
[O-219-5e2]   zyklische Klasse erweiterter Kochain         gesperrt
```

---

## 12. Strukturelle Konsequenz

Die SAYD-Stabilitätsbedingung ist nicht zufällig ein neues Hindernis. Sie ist genau die Hopf-algebraische Form der früheren Periodizitätsbedingung $T = 1$. Der Versuch, die Ladung durch den SAYD-Modulcharakter zu kompensieren, kollidiert mit der Stabilität, sobald dieselbe Koeffizientenkoaktion den KMS-Twist erzeugen soll:

$$
\boxed{
\text{Der Standard-Hopf-SAYD-Pfad reformuliert die Ladungsobstruktion, beseitigt sie aber nicht.}
}
$$

Die frühere Empfehlung „kein strukturelles Hindernis im Hopf-Pfad bekannt“ (NEU-219f) ist damit **revidiert**. Der konstruktiv starkste verbleibende Pfad ist die Dilatations-/Crossed-Product-Erweiterung [O-219-5e1], in der ein tatsächlicher invertierbarer Ladungsträger $u_g$ die Gesamtladung innerhalb der Algebra neutralisiert. Alternativ müsste für [O-219-5d3] eine genuine relative Koeffiziententheorie entwickelt werden.
