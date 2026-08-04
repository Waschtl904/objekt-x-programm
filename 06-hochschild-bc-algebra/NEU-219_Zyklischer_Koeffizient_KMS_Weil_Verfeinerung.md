# NEU-219 — Zyklischer Koeffiziententyp und Weil-/KMS-Verfeinerung der geladenen Cup-Klasse

**DAG-Position:** Direkter Nachfolger von NEU-218 (Commit 9e1dd12).  
**Voraussetzung:** $[D_g^{\mathrm{corr}}] \smile [\Theta^\wedge_{p_1,p_2,p_3}] \neq 0 \in HH^4(A_{\mathrm{alg}}, \mathfrak{M}^{\log}_{\mathrm{glob}})_g$ — vollständig bewiesen.  
**Status gesamt:** $\checkmark[M]_{\mathrm{part}}$

> **AUDITKORREKTUR 2026-08-04** — Direktaudit NEU-219 (Ursprungsknoten).  
> Durchgehend ist $D_g^{\mathrm{corr}}$ statt $D_g$ zu verwenden.  
> Revidierter Gesamtstatus: $\checkmark[M]_{\mathrm{part}}$.

---

## 1. Ausgangslage

Setze:
$$
A = A_{\mathrm{alg}}, \qquad M = \mathfrak{M}^{\log}_{\mathrm{glob}}.
$$

Verbindlich ist die korrigierte geladene Derivation $D_g^{\mathrm{corr}}: A \to M$.

Für vier paarweise verschiedene Hilfsprimzahlen $q, p_1, p_2, p_3$ mit $P = p_1 p_2 p_3$ gilt:
$$
\eta_{q,P} := D_g^{\mathrm{corr}}(\mu_q)\mu_P = \mu_{mqP}\,\sigma_P(G_q)\,\mu_n^*.
$$

Der partielle Quotiententest aus NEU-218 beweist bereits:
$$
\eta_{q,P} \notin C_{H;R} := \sum_{r \in R}[\mu_r, M_{H/r}].
$$

Der volle Kommutatorquotient $M/[A,M]$ wird dadurch nicht entschieden. NEU-218 erklärt ihn ausdrücklich für offen und für den algebraischen $HH^4$-Beweis nicht erforderlich.

Bereits gesichert (Statuskorrektur gegenüber NEU-218-interner Vorsichtsformulierung):
$$
\boxed{[\mathrm{SO\text{-}Q}_{\mathrm{part}}] \quad \checkmark[M]}, \qquad
\boxed{[L^{\mathrm{cup}}_{g;\mathbf{p}}] \neq 0 \in HH^4(A,M)_g \quad \checkmark[M].}
$$

---

## 2. Wachstumskorrektur zu NEU-218

$$
\boxed{[O\text{-}219\text{-growth}] \quad \checkmark[M].}
$$

Bewiesen ist:
$$
\mathcal{F}_N(G_q)(x_N) \ge N^3\bigl(c_{J_N} - c_{K_N}\bigr), \qquad c_{J_N} - c_{K_N} \longrightarrow \infty.
$$

Mit $J_N \asymp N$, $K_N = O(\log N)$ folgt genauer:
$$
\mathcal{F}_N(G_q)(x_N) \gtrsim N^3 \log N.
$$

Das Wachstum ist **superkubisch**, nicht superpolynomial. Für den Widerspruchsbeweis genügt dies vollständig, da die Koinvariantenschranke nur $O(N^3)$ erlaubt.

---

## 3. Typbefund: Koeffizientenmodul

$M = \mathfrak{M}^{\log}_{\mathrm{glob}}$ ist zunächst nur ein $A_{\mathrm{alg}}$-Bimodul. Für einen allgemeinen Bimodul existiert **keine** kanonische Connes-$B$-Struktur auf den $M$-wertigen Hochschildkochains. Die Frage, ob $[L^{\mathrm{cup}}_{g;\mathbf{p}}]$ eine zyklische oder getwistete zyklische Verfeinerung besitzt, ist daher eigenständig zu untersuchen.

$$
\boxed{
HH^4\text{-Klasse} \;\longrightarrow\; \text{globaler zyklischer Koeffizient} \;\longrightarrow\; \text{KMS-/Weil-Paarung} \;\longrightarrow\; \text{Operatorrealisierung}.
}
$$

---

## 4. [O-219-0] — Zyklischer Koeffiziententyp

$$
\boxed{[O\text{-}219\text{-}0] \quad \checkmark[M]_{\mathrm{part}}.}
$$

Zu entscheiden: Welche zyklische Koeffiziententheorie ist auf $M$ anwendbar?

- **(A) Gewöhnlich zyklisch:** Es existiert $\tau: M \to \mathbb{C}$ mit
$$
\tau(am) = \tau(ma) \qquad \forall a \in A_{\mathrm{alg}},\ m \in M.
$$
Dann faktorisiert $\tau$ über $M/[A,M]$.

- **(B) KMS-getwistet:** Kein global traciales Funktional. Benötigt wird ein Twistautomorphismus $\theta_\beta := \alpha_{i\beta}$ mit
$$
\omega_\beta(am) = \omega_\beta\!\left(m\,\theta_\beta(a)\right).
$$

**Einschränkung (Auditkorrektur):** Die Alternative A/B ist nicht erschöpfend. Weitere Möglichkeiten umfassen: gewöhnliche zyklische Koeffizienten, getwistete zyklische Koeffizienten, Hopf-zyklische oder SAYD-Koeffizienten, Morita-induzierte oder markierte Module, andere nichttraciale Dualmodule. Außerdem ist der getwistete Pfad unabhängig von einer negativen Entscheidung des Vollquotienten untersuchbar. Der Satz „Die Entscheidung A versus B hängt direkt von O-219-1 ab" ist zu stark und wird gestrichen.

---

## 5. [O-219-1] — Voller Kommutatorquotient

$$
\boxed{[O\text{-}219\text{-}1]: \quad \eta_{q,P} \stackrel{?}{\notin} [A_{\mathrm{alg}}, M] \quad ?[O].}
$$

Dabei ist $[A,M] = \operatorname{span}_{\mathbb{C}}\{am - ma : a \in A,\ m \in M\}$.

Der partielle Quotient $C_{H;R}$ ist ein Unterraum:
$$
C_{H;R} \subseteq [A,M] \cap M_H.
$$

Aus $\eta_{q,P} \notin C_{H;R}$ folgt **nicht** $\eta_{q,P} \notin [A,M]$.

Rein algebraisch gilt die Äquivalenz:
$$
\boxed{[O\text{-}219\text{-}1a\text{-alg}] \equiv [O\text{-}219\text{-}1]: \quad ?[O].}
$$
Es existiert genau dann $\tau \in M^\vee$ mit $\tau([A,M]) = 0$ und $\tau(\eta_{q,P}) \neq 0$, wenn $\eta_{q,P} \notin [A,M]$.

---

## 6. KMS-Zustand als direkter Detektor — No-go

$$
\boxed{[O\text{-}219\text{-}1a\text{-KMS}] \quad \checkmark[M]_{\mathrm{neg}}.}
$$

Die BC-Zeitentwicklung wirkt auf homogenen Elementen durch $\alpha_t(a_h) = h^{it} a_h$. Für einen BC-KMS-Zustand $\omega_\beta$ gilt:
$$
\omega_\beta(ma) = h^{-\beta}\,\omega_\beta(am).
$$

Das Zielelement $\eta_{q,P}$ besitzt den homogenen Grad $H = gqP = mqP/n \neq 1$. Mit $b = 1$ folgt:
$$
\omega_\beta(\eta_{q,P}) = H^{-\beta}\,\omega_\beta(\eta_{q,P}).
$$

Für $\beta > 0$ und $H \neq 1$ ergibt sich:
$$
\boxed{\omega_\beta\!\left(D_g^{\mathrm{corr}}(\mu_q)\mu_P\right) = 0}
$$
für jeden BC-KMS-Zustand mit $\beta > 0$.

**Umfangsklausel:** Ausgeschlossen wird ein gewöhnlicher BC-KMS-Zustand als direktes nichtverschwindendes traciales Detektorfunktional für das nichtneutrale Zielelement $\eta_{q,P}$. Nicht ausgeschlossen sind total gradkompensierte KMS-Formen oder andere getwistete Koeffizientenarchitekturen.

---

## 7. [O-219-2] — Skalare Hochschildform $\Phi$

**Konditional auf $[O\text{-}219\text{-}1]$ positiv.**

**Auditkorrektur — Gradfehler:**

$$
\boxed{[O\text{-}219\text{-}2\text{-degree}] \quad \times[M].}
$$

Eine skalare zyklische $n$-Kochaine besitzt $n+1$ Argumente. Damit ist
$$
\Phi(a_0, \ldots, a_4)
$$
eine Kochaine vom Grad **4**, nicht vom Grad 5. Die frühere Behauptung $\Phi \in Z^5(A, \mathbb{C})$ ist falsch. Korrekt ist:
$$
\boxed{\Phi \in \operatorname{Hom}_{\mathbb{C}}(A^{\otimes 5}, \mathbb{C}),}
$$
also eine skalare Hochschild-/zyklische Kochaine vom Grad 4.

**Hochschildgeschlossenheit (konditional):**

$$
\boxed{[O\text{-}219\text{-}2\text{-closed}] \quad \checkmark[M] \text{ konditional auf } [O\text{-}219\text{-}1].}
$$

Sei $L = L^{\mathrm{cup}}_{g;\mathbf{p}} \in Z^4(A, M)$ und $\tau$ $A$-zentral. Dann:
$$
(b\Phi)(a_0, \ldots, a_5) = \tau\!\left(a_0\,(bL)(a_1, \ldots, a_5)\right) = 0.
$$
Beim äußeren Randterm wird genau die Tracialität $\tau(a_5 a_0 m) = \tau(a_0 m a_5)$ verwendet. Keine zusätzliche Hochschildrechnung erforderlich.

Bei $\tau(\eta_{q,P}) \neq 0$ liefert die Eingabe $(1, \mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3})$:
$$
\Phi(1, \mu_q, \mu_{p_1}, \mu_{p_2}, \mu_{p_3}) = \left(\prod_{i=1}^3 \log p_i\right)\tau(\eta_{q,P}) \neq 0.
$$

---

## 8. [O-219-3] — Zyklizitätstest

$$
\boxed{[O\text{-}219\text{-}3] \quad ?[O].}
$$

Die Zyklizitätsbedingung für eine skalare Kochaine vom Grad 4 lautet:
$$
\boxed{(\lambda\Phi)(a_0, a_1, a_2, a_3, a_4) = \Phi(a_4, a_0, a_1, a_2, a_3),}
$$
weil $(-1)^4 = 1$. Zu entscheiden: $\lambda\Phi = \Phi$.

**Auditkorrektur — Reparaturbehauptung gestrichen:**

Die frühere Behauptung „$(1-\lambda)\Phi \in \operatorname{im}(b)$ impliziert Zyklizität durch Korrekturterm" gilt **nicht** allgemein und wird gestrichen. Gesucht wäre eine Kochaine $\chi$ mit $(1-\lambda)(\Phi - b\chi) = 0$, was $(1-\lambda)\Phi = (1-\lambda)b\chi$ erfordert. Die bloße Existenz eines $\Psi$ mit $(1-\lambda)\Phi = b\Psi$ liefert keine solche $\chi$. Es sind zusätzliche Kompatibilitätsbedingungen im zyklischen Bikomplex erforderlich.

---

## 9. [O-219-4] — Connes-$B$-Operator

$$
\boxed{[O\text{-}219\text{-}4] \quad \warning[M].}
$$

**Auditkorrektur:** Im kozyklischen gemischten Komplex senkt $B$ den Kochaingrad:
$$
B: C^4 \longrightarrow C^3.
$$

$B\Phi$ ist daher **kein** „Kozykel höherer Ordnung", sondern eine Kochaine vom Grad 3.

Für eine normalisierte zyklische Kochaine gilt unter Standardkonvention bereits $B\Phi = 0$. Der eigentliche unabhängige Haupttest ist daher zunächst $\lambda\Phi = \Phi$. Anschließend ist die Einordnung in den zyklischen bzw. periodischen Komplex sauber anzugeben.

**Auditkorrektur — Zieltyp:** Die frühere Notation $HP^*(A)^\vee$ ist nicht korrekt begründet. Eine skalare periodisch-zyklische Kochaine definiert eine Klasse in $HP^{\mathrm{ev}}(A)$ bzw. im algebraischen periodisch-zyklischen Kohomologiekomplex, nicht automatisch im Dual eines bereits definierten $HP^*$.

---

## 10. [O-219-5] — Getwisteter KMS-Pfad

$$
\boxed{[O\text{-}219\text{-}5a] \quad \checkmark[K/M].}
$$
$$
\boxed{[O\text{-}219\text{-}5b] \quad ?[O].}
$$

Zur Vermeidung einer Kollision mit den arithmetischen Transporten $\sigma_k$ heißt der Twist:
$$
\boxed{\theta_\beta := \alpha_{i\beta}.}
$$

Für homogene Elemente: $\theta_\beta(a_h) = h^{-\beta} a_h$, mit Inversem $\theta_\beta^{-1}(a_h) = h^\beta a_h$.

Die KMS-Gleichung liefert:
$$
\omega_\beta\!\left(am - m\,\theta_\beta(a)\right) = 0.
$$

Der getwistete Modulkommutatorraum ist:
$$
[A,M]_{\theta_\beta} := \operatorname{span}\!\left\{am - m\,\theta_\beta(a)\right\}.
$$

Der KMS-Pfad benötigt anschließend:
- getwisteten Hochschildrand $b_{\theta_\beta}$;
- getwisteten Rotationsoperator $\lambda_{\theta_\beta}$;
- getwisteten Koeffizientenmodul;
- total neutralen Auswertungszyklus.

**Gradkompensation:**

$$
\boxed{[O\text{-}219\text{-}5b\text{-degree}] \quad \checkmark[M].}
$$

Da ein KMS-Zustand jedes nichtneutrale homogene Element annihiliert, muss eine skalare Fünffachform insgesamt Grad 1 besitzen. Für die konkrete Zieleingabe mit $\eta_{q,P}$ muss daher $a_0$ den Grad $n/(mqP)$ tragen.

**Getwistete Zyklizität und Nichtnullpaarung:**

$$
\boxed{[O\text{-}219\text{-}5b\text{-nonzero/cyclic}] \quad ?[O].}
$$

---

## 11. [O-219-6] — Weil-, Primzahlpotenz- und Gammafaktorpaarung

$$
\boxed{[O\text{-}219\text{-}6] \quad ?[O].}
$$

NEU-219 nennt: Weil-Distributionspaarung, Primzahlpotenzkopplung, Gammafaktorpaarung. Es werden jedoch keine der folgenden Daten definiert: $\mathcal{S}_{\mathrm{Weil}}$, $W: C^4_{\mathrm{cyc}}(A) \to \mathbb{C}$, $\Lambda_\infty: \mathcal{S}_\infty \to \mathbb{C}$, oder eine typisierte Abbildung, die $\Gamma'/\Gamma$ bzw. Primzahlpotenzterme erzeugt. Dieser Block ist ausschließlich ein Forschungsziel.

---

## 12. Buchungsposten

$$
\boxed{
\text{Die algebraische }HH^4\text{-Klasse ist gesichert;}\quad
\text{eine zyklische oder KMS-getwistete Verfeinerung noch nicht.}
}
$$

---

## 13. Revidierte Knotenstatustabelle

| Knoten | Revidierter Status | Befund |
|--------|-------------------|--------|
| Wachstumskorrektur | $\checkmark[M]$ | Superkubisch, genauer $\gtrsim N^3 \log N$ |
| Koeffizienten-Typbefund | $\checkmark[M]$ | Allgemeiner Bimodul besitzt keine kanonische zyklische Struktur |
| $[O\text{-}219\text{-}0]$ | $\checkmark[M]_{\mathrm{part}}$ | Gewöhnlich/getwistet korrekt getrennt, aber nicht erschöpfend |
| $[O\text{-}219\text{-}1]$ | $?[O]$ | Voller Kommutatorquotient |
| $[O\text{-}219\text{-}1a\text{-alg}]$ | $?[O]$ | Nur duale Umformulierung von O-219-1 |
| $[O\text{-}219\text{-}1a\text{-KMS}]$ | $\checkmark[M]_{\mathrm{neg}}$ | BC-KMS-Zustand annihiliert das nichtneutrale Zielelement |
| Existenz von $\tau$ aus positivem Vollquotient | $\checkmark[K/M]$ | Rein algebraische Separation |
| $\Phi \in Z^5(A,\mathbb{C})$ | $\times[M]$ | Fünf Argumente bedeuten Grad 4; korrekter Zieltyp $\operatorname{Hom}(A^{\otimes 5},\mathbb{C})$ |
| Hochschildgeschlossenheit von $\Phi$ | $\checkmark[M]$ konditional | Folgt automatisch aus $bL=0$ und Zentralität von $\tau$ |
| $[O\text{-}219\text{-}3]$ | $?[O]$ | Zyklizität nicht berechnet |
| „$b$-exakter Defekt automatisch reparierbar" | $\times[M]$ | Zusätzliche Kompatibilität erforderlich — gestrichen |
| $[O\text{-}219\text{-}4]$ | $\warning[M]$ | $B$ senkt Grad; periodischer Zieltyp falsch notiert |
| $[O\text{-}219\text{-}5a]$ | $\checkmark[K/M]$ | Getwisteter Quotient und Algebraautomorphismus |
| $[O\text{-}219\text{-}5b]$ | $?[O]$ | Getwisteter Rand, Zyklizität und Nichtnullpaarung |
| $[O\text{-}219\text{-}6]$ | $?[O]$ | Weil-/Primzahlpotenz-/Gammafaktorpfad |

---

## 14. Revidierter DAG

```
NEU-218
[L^cup] != 0 in HH^4(A,M)_g                              ✓[M]
        |
        v
[O-219-0] zyklischer Koeffiziententyp                     ✓[M]_part
        |
        +-- gewöhnlicher Pfad
        |       |
        |       +-- [O-219-1] eta notin [A,M]             ?[O]
        |       |
        |       +-- algebraisches zentrales tau            ✓[K/M] kond.
        |       |
        |       +-- skalare Grad-4-Form Phi                ✓[M] kond.
        |       |
        |       +-- bPhi=0                                  ✓[M] kond.
        |       |
        |       +-- lambda Phi = Phi                        ?[O]
        |       |
        |       +-- zyklische/periodische Einordnung        ?[O]
        |
        +-- BC-KMS-Zustand als direkter Detektor            ✓[M]_neg
        |
        +-- getwisteter Pfad
        |       |
        |       +-- theta_beta = alpha_{ibeta}              ✓[K/M]
        |       |
        |       +-- getwisteter Quotient                    ✓[K/M]
        |       |
        |       +-- Gradkompensation                        ✓[M]
        |       |
        |       +-- b_theta Phi_beta = 0                    ?[O]
        |       |
        |       +-- lambda_theta Phi_beta = Phi_beta         ?[O]
        |
        +-- Weil-/Primzahlpotenz-/Gammafaktorpaarung        ?[O]
```

---

**Commit-Referenz:** Auditkorrektur 2026-08-04, Nachfolger von 9e1dd12 (NEU-218).  
**Primärer nächster Audit:** `NEU-219a_KMS_Typaudit_Negativbefund.md`
