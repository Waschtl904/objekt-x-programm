# NEU-184 — Zentrumstest: Koeffizientenaudit für $Z(A_\mathbb{Q})_g$ (rev2)

## 184.0 — Zweck und Abgrenzung

NEU-184 führt den **Koeffizientenaudit** des homogenen Zentrums durch:

$$[O\text{-}182\text{-}6]: \quad Z(A_\mathbb{Q}^{\mathrm{alg}})_g = 0 \quad \text{für alle } g \neq 1\,?$$

**Ausdrückliche Abgrenzung:** Dieser Knoten ist **unabhängig** von:
- $[O\text{-}182\text{-}9]$: $[\Omega_{\mathbf{p}}] \neq 0$ in $HH^4(A_\mathbb{Q}^{\mathrm{alg}}, A_\mathbb{Q}^{\mathrm{alg}})$
- $[O\text{-}181\text{-}9b]$: $u_g \smile \Omega_{\mathbf{p}} \neq 0$

Ein negativer Abschluss von [O-182-6] schließt **nur** die reguläre geladene
Nullkozykel-Faktorisierungsroute aus. Er impliziert weder $[\Omega_{\mathbf{p}}] = 0$
noch das Verschwinden von $HH^4(A_\mathbb{Q}^{\mathrm{alg}}, M_{\sigma_\beta})_{\mathrm{ch}}$.

---

## 184.1 — Eingangsbasis aus NEU-183

Gesichert (NEU-183):
- **Normalform:** $A_g = \operatorname{span}\{\mu_m\, e(r)\, \mu_n^*\}_{m/n = g}$
  mit $\gcd(m,n)=1$, $r \in \frac{1}{\mathrm{lcm}(m,n)}\mathbb{Z}/\mathbb{Z}$
- **Relationen (R1)–(R7)** der BC-Präsentation

Ein allgemeines homogenes Element fester Gradierung $g = m/n$ ($\gcd(m,n)=1$):

$$u_{m,n} = \sum_{r \in F} c_r\, \mu_m\, e(r)\, \mu_n^*, \qquad F \subset \mathbb{Q}/\mathbb{Z} \text{ endlich}.$$

---

## 184.2 — Kommutationstest mit $e(s)$

### Korrekte Auswertung der Relationen

Aus (R4): $\mu_m\, e(r) = e(r/m)\, \mu_m$, umgestellt: $e(s)\, \mu_m = \mu_m\, e(ms)$.

Aus (R5): $e(r)\, \mu_n^* = \mu_n^*\, e(nr)$, umgestellt: $\mu_n^*\, e(s) = e(s/n)^?\,\mu_n^*$.

> **Auditkorrektur:** Die direkte Umkehrung von (R5) ergibt **nicht** $\mu_n^* e(s) = e(s/n)\mu_n^*$,
> da Division durch $n$ in $\mathbb{Q}/\mathbb{Z}$ nicht eindeutig ist. Die korrekte Ableitung ist:
>
> Aus $e(r)\mu_n^* = \mu_n^* e(nr)$ setze $r' = nr$, also $e(r'/n)\mu_n^* = \mu_n^* e(r')$.
> Umgestellt: $\mu_n^*\, e(s) = e(s/n)\,\mu_n^*$ ist **nicht** wohldefiniert für beliebiges $s$.
>
> Stattdessen aus (R5) mit der rechten Seite: $\mu_n^*\, e(s) = ?$
> Aus $e(r)\mu_n^* = \mu_n^* e(nr)$ mit $r \mapsto s$:
> $$e(s)\mu_n^* = \mu_n^* e(ns).$$
> Daher: $\mu_n^* e(s) \neq e(s/n)\mu_n^*$ im Allgemeinen; stattdessen gilt (durch Adjungieren von R4):
> $\mu_n^* e(s) = e(ns)\mu_n^*$? Nein — das wäre die **adjungierte** Relation.

**Korrekte Auswertung via Adjungieren von (R4):**

Aus (R4): $\mu_n e(r) = e(r/n)\mu_n$. Adjungieren: $e(r/n)^*\mu_n^* = \mu_n^* e(r)^*$,
d.h. $e(-r/n)\mu_n^* = \mu_n^* e(-r)$, also:
$$\mu_n^*\, e(s) = e(ns)\, \mu_n^*. \qquad \text{[adjungiert aus (R4)]}$$

Damit:
$$\mu_m\, e(r)\, \mu_n^* \cdot e(s)
= \mu_m\, e(r)\, e(ns)\, \mu_n^*
= \mu_m\, e(r + ns)\, \mu_n^*.$$

Und (bereits aus 184.2 Linksseite):
$$e(s) \cdot \mu_m\, e(r)\, \mu_n^*
= \mu_m\, e(ms)\, e(r)\, \mu_n^*
= \mu_m\, e(r + ms)\, \mu_n^*.$$

### Kommutationsbedingung für ein einzelnes Monom

$$[e(s),\, \mu_m e(r) \mu_n^*] = 0
\iff \mu_m e(r+ms)\mu_n^* = \mu_m e(r+ns)\mu_n^*
\iff ms \equiv ns \pmod{\mathbb{Z}}
\iff (m-n)s \equiv 0 \pmod{\mathbb{Z}}.$$

Dies für **ein** einzelnes Monom und **alle** $s$ erzwingt $m = n$, also $g = m/n = 1$.
Der termweise Schluss ist aber für eine **Linearkombination** nicht direkt zulässig.

---

## 184.3 — Koeffizientenaudit: Linearkombination

Sei $u_{m,n} = \sum_{r \in F} c_r\, \mu_m e(r) \mu_n^*$ mit $F$ endlich.

Die Bedingung $[e(s), u_{m,n}] = 0$ lautet:

$$\sum_{r \in F} c_r\, \mu_m e(r+ms)\mu_n^* = \sum_{r \in F} c_r\, \mu_m e(r+ns)\mu_n^*.$$

Da die Monome $\{\mu_m e(t)\mu_n^*\}_{t \in \mathbb{Q}/\mathbb{Z}}$ linear unabhängig sind
(Normalform aus NEU-183), folgt koeffizientenweiser Vergleich:

$$c_{r - ms} = c_{r - ns} \qquad \forall r \in \mathbb{Q}/\mathbb{Z},\; \forall s \in \mathbb{Q}/\mathbb{Z}.$$

Nach Umindizierung $r \mapsto r + ms$:

$$c_{r+(m-n)s} = c_r \qquad \forall r, s \in \mathbb{Q}/\mathbb{Z}.$$

### Surjektivitätsargument

Ist $m \neq n$, so ist die Abbildung

$$\mathbb{Q}/\mathbb{Z} \longrightarrow \mathbb{Q}/\mathbb{Z}, \qquad s \longmapsto (m-n)s$$

**surjektiv** (da $m - n \in \mathbb{Z} \setminus \{0\}$ und Multiplikation mit
einer ganzen Zahl $\neq 0$ in $\mathbb{Q}/\mathbb{Z}$ surjektiv ist).

Daher ist $r \mapsto c_r$ invariant unter **allen** Translationen von $\mathbb{Q}/\mathbb{Z}$.

Eine Funktion $F \to \mathbb{C}$ mit **endlichem Träger** $F \subset \mathbb{Q}/\mathbb{Z}$,
die unter allen Translationen invariant ist, muss **identisch null** sein:
denn wäre $c_{r_0} \neq 0$ für ein $r_0 \in F$, so wäre $c_{r_0 + t} = c_{r_0} \neq 0$
für alle $t \in \mathbb{Q}/\mathbb{Z}$ — im Widerspruch zur Endlichkeit von $F$.

Also: $c_r = 0$ für alle $r$, d.h. $u_{m,n} = 0$.

### Satz 184.1 (korrigierte Fassung)

> **Satz 184.1.** Sei $u_{m,n} = \sum_{r \in F} c_r\, \mu_m e(r) \mu_n^*$
> ein homogenes Element mit $g = m/n \neq 1$ (d.h. $m \neq n$).
> Gilt $[e(s), u_{m,n}] = 0$ für alle $s \in \mathbb{Q}/\mathbb{Z}$, so ist $u_{m,n} = 0$.
>
> **Beweis:** (endlicher Träger) + (Surjektivität von $s \mapsto (m-n)s$) wie oben. $\square$

> **Korrekturhinweis zu rev1:** Die Vorgassung verwendete $\mu_n^* e(s) = e(s/n)\mu_n^*$
> (nicht wohldefiniert in $\mathbb{Q}/\mathbb{Z}$) und schloss termweise via „Dichte”.
> Die korrekte Relation ist $\mu_n^* e(s) = e(ns)\mu_n^*$ (adjungiert aus R4).
> Die Kommutationsbedingung lautet daher $(m-n)s \equiv 0$, nicht $mn = 1$.
> Das Ergebnis $Z(A_\mathbb{Q})_g = 0$ für $g \neq 1$ bleibt richtig;
> der Beweis beruht auf endlichem Träger + Surjektivität, nicht auf Dichte.

---

## 184.4 — Knotenabschluss

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-5] | Generatorentest $u_g \in Z(A)$ | ✓[M] — Kriterium alle drei Generatorfamilien |
| [O-182-6] | $Z(A_\mathbb{Q}^{\mathrm{alg}})_g = 0$ für $g \neq 1$ | ✓[M]\_neg — Satz 184.1 (rev2) |

**Epistemischer Status:**
$$[O\text{-}182\text{-}6] \quad \checkmark[M]_{\mathrm{neg}}$$

Verwendete Grundlagen: Normalform $A_g$ (✓[K], NEU-183); Relation (R4) und ihr Adjungiertes;
lineare Unabhängigkeit der Normalformmonome; Endlichkeit des Trägers; Surjektivität von
$s \mapsto (m-n)s$ auf $\mathbb{Q}/\mathbb{Z}$.

---

## 184.5 — Kanonischer DAG-Stand nach NEU-184

```
Verdrehte Route (Re β > 0)    ✓[M]_neg
Reguläre geladene Nullkozykelroute  ✓[M]_neg  ([O-182-6])
Ω_p als Kozykel, ≠ 0 als Kochain   ✓[K]
[Ω_p] ≠ 0 in HH⁴?                  ?[O]  → NEU-185
```

NEU-185 übernimmt ausschließlich [O-182-9] via Augmentations-Dualzyklus.
