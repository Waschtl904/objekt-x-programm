# NEU-188 — Erweiterungsobstruktion punktierter Gruppenkozykel auf die BC-Algebra (rev2)

## 188.0 — Ausgangslage

Aus NEU-187: $H^1(G, B_{\rho_d}) \neq 0$ für $d = n-m \neq 0$ ([O-187-2] ✓[M]),
repräsentiert durch ein singuläres Potential $H \in \operatorname{LC}(\widehat{\mathbb{Z}} \setminus \{0\})$,
nicht fortsetzbar zu einem Element von $B \cong \operatorname{LC}(\widehat{\mathbb{Z}})$.

Satz 187.3 liefert nur die Injektion $HH^1(A,A)_g \hookrightarrow HH^1(B,A)_g$.
Die Erweiterungsfrage:
$$[O\text{-}188]: \quad \text{Lässt sich } [c] \in H^1(B,A)_g \text{ zu } \delta \in \operatorname{Der}_g(A,A) \text{ fortsetzen?}$$

---

## 188.A — Korrektur: $m=2, n=1$ ist kein Test

Für jede **unitale** Derivation gilt notwendig:
$$y_1 = \delta(\mu_1) = \delta(1) = 0.$$

Die Gleichung $[e(s), y_1] = 0$ ist daher eine **redundante Folge** von $y_1 = 0$,
nicht eine unabhängige Bedingung. Selbst wenn man sie isoliert löst, zeigt sie nur
$y_1 \in C_A(B)$ (Kommutant von $B$), nicht $y_1 \in Z(A)$.

**Der erste sinnvolle Test muss $k > 1$ verwenden.**

| Knoten | Inhalt | Status |
|---|---|---|
| [O-188-alt] | $m=2,n=1$-Fall ist kein gültiger Test | ✓[K]\_neg — zurückgezogen |

---

## 188.B — Korrektur: (K2) ist keine Existenzobstruktion

Aus $z_n \mu_n + \mu_n^* y_n = 0$ folgt für **jedes** gegebene $y_n$ sofort eine Lösung:
$$z_n^{(0)} := -\mu_n^* y_n \mu_n^*.$$

*Nachweis:* $z_n^{(0)} \mu_n = -\mu_n^* y_n \mu_n^* \mu_n = -\mu_n^* y_n$ (via $\mu_n^*\mu_n=1$). $\checkmark$

Allgemeine Lösung: $z_n = z_n^{(0)} + w_n$ mit $w_n \mu_n = 0$.

(K2) allein ist **immer lösbar**. Die echte Obstruktion entsteht erst durch
Verträglichkeit mit den übrigen Relationen.

**Umbenennung:**
$$[O\text{-}188\text{-}2]: \quad \text{Verträglichkeit der aus (K2) gewonnenen } z_n \text{ mit (E5), (E3) und den Kreuzrelationen.}$$

---

## 188.C — Vollständigung des Constraint-Systems

### (E3): Projektionsrelation

Aus $\mu_n \mu_n^* = P_n := \frac{1}{n}\sum_{j=0}^{n-1} e(j/n)$ folgt durch Differentiation:

$$\boxed{y_n \mu_n^* + \mu_n z_n = \frac{1}{n}\sum_{j=0}^{n-1} x_{j/n}.} \tag{E3}$$

### (E7): Kreuzrelation (teilerfremder Fall)

Aus $\mu_m^* \mu_n = \mu_n \mu_m^*$ (für $\gcd(m,n)=1$) folgt:

$$\boxed{z_m \mu_n + \mu_m^* y_n = y_n \mu_m^* + \mu_n z_m.} \tag{E7}$$

### Neuer Vorknoten

$$[O\text{-}188\text{-}0]: \quad \text{Differenziere sämtliche Relationen (R1)–(R7) und bilde das vollständige Erweiterungssystem.}$$

(K1)–(K5) allein sind **nicht** ausreichend; (E3), (E7) und alle weiteren Kreuz- und
Projektionsrelationen müssen ebenfalls differenziert werden.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-188-0] | Vollständiges differenziertes Relationssystem (R1)–(R7) | ?[O] — (E3), (E7) hinzugefügt, weitere Kreuzrelationen ausstehend |

---

## 188.D — Eindeutigkeit der Erweiterung

**Lemma 188.1.** Für $g \neq 1_\Gamma$ besitzt (E4) höchstens eine Lösung $y_k$.

*Beweis.* Seien $y_k, y_k'$ zwei Lösungen, $w_k := y_k - y_k'$. Dann erfüllt $w_k$ die
homogene Gleichung $e(s) w_k = w_k e(ks)$ für alle $s$.
Schreibe $w_k = \sum_r c_r\, \mu_a e(r) \mu_b^*$ mit $a/b = gk$.
Linke Seite verschiebt den Koeffiziententräger um $as$, rechte um $bks$.
Nichtverschwindender endlicher Träger erfordert $a = bk$; zusammen mit $a/b = gk$
folgt $g = 1_\Gamma$ — Widerspruch. Also $w_k = 0$. $\square$

Analoges Argument liefert Eindeutigkeit von $z_k$ aus (E5).

| Knoten | Inhalt | Status |
|---|---|---|
| [O-188-uniq] | Eindeutigkeit von $y_k, z_k$ für $g \neq 1_\Gamma$ | ✓[M] — Lemma 188.1 |

---

## 188.E — Das $T_H$-Modell

Setze für $g = m/n$, $m \neq n$: $T_H := \mu_m H \mu_n^*$ (formal, mit $H$ aus NEU-187).
Bis auf Vorzeichenkonvention:
$$x_s = \operatorname{ad}(T_H)(e(s)).$$

### Formale Auswertung an $\mu_k$, $\mu_k^*$

Für $\gcd(k,n) = 1$:
$$\boxed{\operatorname{ad}(T_H)(\mu_k) = \mu_{mk}\bigl(\alpha_k(H) - H\bigr)\mu_n^*,} \qquad (\alpha_k H)(x) := H(kx).$$

Da die Lösung von (E4) eindeutig ist (Lemma 188.1):
$$\text{(E4) lösbar für dieses } k \iff \alpha_k(H) - H \in B.$$

Für $\gcd(k,m) = 1$ analog:
$$\operatorname{ad}(T_H)(\mu_k^*) = \mu_m\bigl(H - \alpha_k(H)\bigr)\mu_{nk}^*,$$
kontrolliert durch dieselbe Bedingung für (E5).

### Reduzierte Kernfrage

$$\boxed{\alpha_k(H) - H \in \operatorname{LC}(\widehat{\mathbb{Z}}) \quad \text{für alle relevanten } k?}$$

Für nicht teilerfremde Indizes treten zusätzlich Transferoperatoren der BC-Algebra auf.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-188-1] | $\alpha_k(H) - H \in B$ für alle teilerfremden Generatorindizes $k$ | ?[O] |
| [O-188-2] | Transferbedingungen im nicht teilerfremden Fall | ?[O] |
| [O-188-3] | Verträglichkeit mit (E3), (E7) und allen restlichen Relationen | ?[O] |

---

## 188.F — Automatische Äußerlichkeit

**Satz 188.2.** Ist $\delta_H := \operatorname{ad}(T_H)|_A$ eine wohldefinierte Derivation
$A \to A$ (d.h. alle Kommutatoren liegen in $A$), dann ist $\delta_H$ **nicht inner**.

*Beweis.* Wäre $\delta_H = \operatorname{ad}(u)$ für $u \in A_g$, so würde $T_H - u$ mit allen
$e(s)$ kommutieren. Im punktierten Fourier-Modell:
$$(\chi_{ms}(x) - \chi_{ns}(x))(H(x) - h(x)) = 0 \qquad \forall s.$$
Für $x \neq 0$ existiert wegen $m - n \neq 0$ ein $s$ mit $\chi_{(m-n)s}(x) \neq 1$,
also $H(x) = h(x)$ für $x \neq 0$. Da $h \in B = \operatorname{LC}(\widehat{\mathbb{Z}})$ bei $0$
lokal konstant fortsetzbar ist, wäre $H$ ebenfalls fortsetzbar — Widerspruch zur
Nichttrivialität der Klasse aus NEU-187. $\square$

**Konsequenz:** Jede erfolgreich erweiterte nichttriviale punktierte Klasse ist
automatisch äußerlich. [O-188-4] ist kein eigenständiger Engpass mehr.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-188-4] | Nicht-Innheit einer erfolgreichen Erweiterung | ✓[M] konditional — Satz 188.2, automatisch bei [O-188-1]–[O-188-3] positiv |

---

## 188.G — Zentrale offene Frage

$$\boxed{\exists\, H \notin \operatorname{LC}(\widehat{\mathbb{Z}}) \text{ auf } \widehat{\mathbb{Z}} \setminus \{0\}, \quad \alpha_k(H) - H \in \operatorname{LC}(\widehat{\mathbb{Z}}) \ \forall k\,?}$$

- **Positiver Kandidat** $\Rightarrow$ geladene äußere Derivation $\Rightarrow$ $HH^1(A,A)_g \neq 0$.
- **Regularitätssatz** (jedes solche $H$ ist über $0$ fortsetzbar) $\Rightarrow$ gesamte geladene $HH^1$-Route ausgeschlossen.

---

## 188.H — DAG-Stand nach NEU-188 rev2

```
[O-188-0]    ?[O]         Vollst. differenziertes Relationssystem (R1)-(R7), inkl. (E3),(E7)
[O-188-uniq] ✓[M]         Eindeutigkeit y_k, z_k fuer g != 1_Gamma (Lemma 188.1)
[O-188-1]    ?[O]         alpha_k(H) - H in B, teilerfremde k
[O-188-2]    ?[O]         Transferbedingungen, nicht teilerfremde k
[O-188-3]    ?[O]         Vertraeglichkeit (E3),(E7), Rest
[O-188-4]    ✓[M] kond.   Automatische Aeusserlichkeit (Satz 188.2)
[O-188]      ?[O]         HH^1(A,A)_g != 0?  <=  [O-188-1] & [O-188-2] & [O-188-3]
[O-186-0]    ?[O]         HH^4(A,A)_ch != 0?
```
