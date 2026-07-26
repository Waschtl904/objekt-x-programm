# NEU-219a — KMS-Typaudit und Negativbefund für den BC-KMS-Kandidaten

**DAG-Position:** Korrekturaudit zu NEU-219, [O-219-1] und [O-219-5].  
**Commit-Referenz:** Nachfolger von 7efa47b (NEU-219).

---

## Ausgangslage

In der vorigen Analyse wurde vorgeschlagen, einen KMS-Zustand
$\omega_\beta: A_{C^*} \to \mathbb{C}$
als traciales Funktional mit $\omega_\beta(D_g(\mu_q)\mu_P) \neq 0$ zu verwenden.
Dieser Vorschlag wird hier vollständig ausgeschlossen.

Setze
$$
\eta_{q,P} := D_g(\mu_q)\mu_P \in M,
\qquad
C := [A_{\mathrm{alg}}, M].
$$

---

## [O-219-1a-alg] — Algebraische Äquivalenz

**Status:** ?[O] (identisch mit [O-219-1])

Rein algebraisch gilt:
$$
\boxed{
\eta_{q,P} \notin C
\iff
\exists\, \tau \in M^\vee:\quad \tau(C)=0,\quad \tau(\eta_{q,P})\neq0.
}
$$

Die Existenz eines solchen $\tau$ (ohne Stetigkeits- oder Positivitätsforderung) ist lediglich eine duale Umformulierung von $\overline{\eta}_{q,P} \neq 0$ in $M/C$. Es gilt:

$$
\boxed{ [O\text{-}219\text{-}1a\text{-alg}] \equiv [O\text{-}219\text{-}1]. }
$$

Als eigenständiger nachgelagerter Knoten bringt er keinen DAG-Fortschritt.

---

## [O-219-1a-KMS] — Negativbefund: BC-KMS-Zustand

**Status:** ✓[M]$_{\mathrm{neg}}$

### KMS-Gleichung und Zeitgewicht

Die Bost–Connes-Zeitentwicklung $\alpha_t$ (zu unterscheiden von den projektinternen $\sigma_k$) wirkt auf homogene Elemente durch
$$
\alpha_t(a_h) = h^{it} a_h,
\qquad
\alpha_{i\beta}(a_h) = h^{-\beta} a_h.
$$

Die KMS$_\beta$-Gleichung lautet auf analytischen Elementen:
$$
\omega_\beta(ab) = \omega_\beta\!\left( b\,\alpha_{i\beta}(a) \right).
$$

Dies ist eine **getwistete** Spuridentität, nicht $\omega_\beta(ab) = \omega_\beta(ba)$. Für ein homogenes $a_h \in A_h$ und $m \in M$ folgt:

$$
\boxed{ \omega_\beta(a_h m) = h^{-\beta}\,\omega_\beta(m a_h). } \tag{2.1}
$$

Insbesondere:
$$
\omega_\beta([\mu_n, m]) = (n^{-\beta}-1)\,\omega_\beta(m\mu_n),
$$
was im Allgemeinen **nicht** null ist. Der KMS-Zustand annihiliert den gewöhnlichen Modulkommutatorraum $[A_{\mathrm{alg}}, M]$ **nicht**.

### Gewichtsausschluss des Zielelements

Das Zielelement $\eta_{q,P}$ hat den homogenen Grad
$$
H = gqP = \frac{mqP}{n}.
$$

Wegen $q, p_1, p_2, p_3 \nmid mn$ gilt $H \neq 1$.

Setze in der KMS-Gleichung $a = \eta_{q,P}$, $b = 1$:
$$
\omega_\beta(\eta_{q,P}) = \omega_\beta(\alpha_{i\beta}(\eta_{q,P})) = H^{-\beta}\,\omega_\beta(\eta_{q,P}).
$$

Da $\beta > 0$ und $H \neq 1$, folgt $H^{-\beta} \neq 1$, also:

$$
\boxed{ \omega_\beta(D_g(\mu_q)\mu_P) = 0. } \tag{3.1}
$$

Dies gilt für alle $\beta > 0$, insbesondere bei $\beta = 1$ und bei $\beta > 1$.

$$
\boxed{ \text{„BC-KMS-Zustand als tracialer Detektor von }\eta_{q,P}\text{“} \quad \checkmark[M]_{\mathrm{neg}}. }
$$

Der Negativbefund beruht allein auf dem nichtneutralen Zeitgewicht $H \neq 1$, nicht auf Erweiterungsfragen.

### Kein Erweiterungsproblem

Da $M = \mathfrak{M}^{\log}_{\mathrm{glob}} \subseteq A_{C^*}$, ist $\omega_\beta|_M: M \to \mathbb{C}$ automatisch als beschränktes lineares Funktional definiert. Eine Konstruktion der Erweiterung ist nicht erforderlich. Die wirklichen Hindernisse sind:
- $\omega_\beta([A,M]) \neq 0$ im Allgemeinen (keine gewöhnliche Tracialität),
- $\omega_\beta(\eta_{q,P}) = 0$ (Gewichtsausschluss).

---

## [O-219-5a] — Getwisteter Quotient und KMS-Koeffiziententyp

**Status:** ✓[K/M]

Definiere den Twist auf analytischen Elementen durch:
$$
\theta_\beta := \alpha_{i\beta},
\qquad
\theta_\beta(a_h) = h^{-\beta} a_h.
$$

Dann gilt nach (2.1):
$$
\boxed{ \omega_\beta\bigl(am - m\theta_\beta(a)\bigr) = 0. } \tag{5.1}
$$

Der KMS-Zustand annihiliert also die **getwisteten** Modulkommutatoren. Der geeignete Quotient für den KMS-Pfad ist:

$$
\boxed{ M \Big/ [A,M]_{\theta_\beta}, }
$$

wobei
$$
[A,M]_{\theta_\beta} := \mathrm{span}_{\mathbb{C}}\{ am - m\theta_\beta(a) \mid a \in A_{\mathrm{alg}},\ m \in M \}.
$$

Dies ist ein eigenständiger Quotient; er ist im Allgemeinen größer als $[A,M]$. Der gewöhnliche Vollquotient [O-219-1] bleibt davon unberührt.

---

## [O-219-5b] — Total neutrale KMS-Fünffachform

**Status:** ?[O]

Da $\omega_\beta(\eta_{q,P}) = 0$, kann das Zielelement nicht direkt ausgewertet werden. Man benötigt einen kompensierenden Faktor $a_0$ mit
$$
\deg(a_0) \cdot H = 1 \quad\Longleftrightarrow\quad \deg(a_0) = H^{-1} = \frac{n}{mqP}.
$$

Die total neutrale KMS-Fünffachform lautet:
$$
\boxed{
\Phi_\beta(a_0, a_1, a_2, a_3, a_4)
:= \omega_\beta\!\left( a_0\, L^{\mathrm{cup}}_{g;\mathbf{p}}(a_1, a_2, a_3, a_4) \right),
}
$$
mit der Gradbedingung
$$
\deg(a_0)\cdot g \cdot \prod_{j=1}^4 \deg(a_j) = 1.
$$

Eine solche total neutrale Konfiguration kann unter $\omega_\beta$ nichtverschwindend sein. Danach sind separat zu prüfen:

1. **Getwisteter Hochschildrand:** $b_{\theta_\beta} \Phi_\beta = 0$
2. **Getwistete Zyklizität:** $(1 - \lambda_{\theta_\beta})\Phi_\beta = 0$ oder exakter Defekt
3. **Paarung:** $\langle L^{\mathrm{cup}}_{g;\mathbf{p}},\ z_{\varphi, \theta_\beta} \rangle \neq 0$

$$
\boxed{ [O\text{-}219\text{-}5b]: \quad \Phi_\beta \text{ und getwistete Randgleichung} \quad ?[O]. }
$$

---

## Revidierte Knotenstatustabelle (Zusätze zu NEU-219)

| Knoten | Inhalt | Status |
|--------|--------|--------|
| [O-219-1] | $\eta_{q,P} \notin [A,M]$ (voller Quotient) | ?[O] primär |
| [O-219-1a-alg] | Duale Umformulierung $\equiv$ [O-219-1] | ?[O] (kein Fortschritt) |
| [O-219-1a-KMS] | $\omega_\beta(\eta_{q,P}) = 0$ für $\beta > 0$ | ✓[M]$_{\mathrm{neg}}$ |
| [O-219-5a] | Getwisteter Quotient $[A,M]_{\theta_\beta}$, KMS-Typ | ✓[K/M] |
| [O-219-5b] | Total neutrale $\Phi_\beta$, getwisteter Rand | ?[O] |

---

## Konsequenz für den DAG

Der KMS-Zustand löst [O-219-1] nicht. Er eröffnet einen **separaten getwisteten Pfad** (Knoten [O-219-5a/5b]), der:
- den Quotient $M/[A,M]_{\theta_\beta}$ statt $M/[A,M]$ verwendet,
- eine total neutrale Fünffachform $\Phi_\beta$ mit Gradkompensation erfordert,
- getwisteten Rand und getwistete Zyklizität separat zu verifizieren hat.

Der gewöhnliche Vollquotient [O-219-1] muss weiterhin durch eine echte Struktur- oder Følner-Analyse entschieden werden.

```
[O-219-1]  eta_{q,P} not in [A,M]                     ?[O] primaer
    |
    +-- [O-219-1a-alg]: duale Umformulierung           ?[O] (==[O-219-1])
    +-- [O-219-1a-KMS]: omega_beta(eta)=0 wegen H!=1   [M]_neg
    |
[O-219-5a] getwisteter Quotient [A,M]_{theta_beta}     [K/M]
    |
[O-219-5b] total neutrale Phi_beta, getwisteter Rand   ?[O]
```

**Primärer nächster Schritt:** [O-219-1] via Struktur-/Følner-Analyse des vollen Kommutatorraums.
