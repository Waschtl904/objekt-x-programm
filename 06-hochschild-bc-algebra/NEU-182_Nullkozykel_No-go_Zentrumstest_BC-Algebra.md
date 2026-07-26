# NEU-182 — Nullkozykel-No-go und Zentrumstest in der BC-Algebra

## 182.0 — Zweck und epistemischer Status

NEU-182 untersucht zwei voneinander **unabhängige** Wege zur Erzeugung
eines geladenen Vier-Kozykels auf der algebraischen BC-Algebra:

1. **Verdrehte Faktorisierungsroute**

   $$u_\beta \smile \Omega_{\mathbf{p}} \in C^4(A_\mathbb{Q}^{\mathrm{alg}},\, {}_{\mathrm{id}}A_{\mathbb{Q},\sigma_\beta})$$

   wobei $u_\beta$ ein verdrehter Nullkozykel sein soll.

2. **Reguläre Faktorisierungsroute**

   $$u_g \smile \Omega_{\mathbf{p}} \in C^4(A_\mathbb{Q}^{\mathrm{alg}},\, A_\mathbb{Q}^{\mathrm{alg}})$$

   wobei $u_g \in Z(A_\mathbb{Q}^{\mathrm{alg}}) \cap A_g$, $g \neq 1$ gesucht wird.

Der erste Weg wird unter einer **präzisen Norm- und Isometrieannahme** ausgeschlossen.
Der zweite Weg bleibt einem Zentrumstest vorbehalten.

> **Ausdrücklicher Hinweis:** Der Ausschluss der verdrehten Nullkozykel impliziert nicht
> $$HH^4(A_\mathbb{Q}^{\mathrm{alg}},\, {}_{\mathrm{id}}A_{\mathbb{Q},\sigma_\beta})_{\mathrm{ch}} = 0.$$
> Er betrifft ausschließlich die Faktorisierung eines Vier-Kozykels durch einen verdrehten Nullkozykel.

---

## 182.A — Typkorrektes Nullkozykel-System

Sei $A := A_\mathbb{Q}^{\mathrm{alg}}$ und $M_{\sigma_\beta} := {}_{\mathrm{id}}A_{\sigma_\beta}$,
also $M_{\sigma_\beta} = A$ als Vektorraum mit den Wirkungen

$$a \cdot m = am, \qquad m \cdot a = m\,\sigma_\beta(a).$$

Für einen Nullkozykel $u \in C^0(A, M_{\sigma_\beta}) = M_{\sigma_\beta}$ gilt:

$$bu = 0 \iff au = u\,\sigma_\beta(a) \qquad \forall a \in A.$$

Unter
$$\sigma_\beta(e(r)) = e(r),\quad
\sigma_\beta(\mu_n) = n^{-\beta}\mu_n,\quad
\sigma_\beta(\mu_n^*) = n^\beta\mu_n^*$$

ergibt sich das vollständige **Generatorensystem**:

$$\boxed{\begin{aligned}
e(r)\,u &= u\,e(r), \\
\mu_n\,u &= n^{-\beta}\,u\,\mu_n, \\
\mu_n^*\,u &= n^{\beta}\,u\,\mu_n^*.
\end{aligned}}$$

Insbesondere ist $e(r)\,u = u\,e(r)$ eine **echte Zentralitätsbedingung**;
sie folgt nicht aus $\deg e(r) = 1$.

### Knotenstruktur 182.A

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-1] | $e(r)u = ue(r)$ ist nichttriviale Nullkozykelbedingung | ✓[M] — formale Konsequenz der Definition des verdrehten Hochschild-Kodifferentials und $\sigma_\beta(e(r))=e(r)$ |

---

## 182.B — Norm-No-go für verdrehte Nullkozykel

### 182.B.1 — Normativer Rahmen

Für das folgende Argument wird vorausgesetzt:

- Eine unitale $C^*$-Algebra $\overline{A}$ oder eine treue $C^*$-Darstellung von $A$,
  sodass $A \subseteq \overline{A}$ als Algebra eingebettet ist;
- die Generatorrelationen von $A$ gelten in $\overline{A}$;
- für mindestens ein $n > 1$ gilt $\mu_n^*\mu_n = 1$.

Die Abbildung $\sigma_\beta$ muss **nicht** zu einem beschränkten oder sternerhaltenden
Automorphismus von $\overline{A}$ fortsetzbar sein. Benötigt wird nur die algebraische
Intertwinerrelation $\mu_n u = n^{-\beta} u \mu_n$ für das betrachtete $u \in A \subseteq \overline{A}$.

**Offener Transferknoten:**

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-2N] | $A_\mathbb{Q}^{\mathrm{alg}}$ besitzt eine treue Einbettung in eine $C^*$-Realisierung | ?[O] — quellen- und präsentationsabhängig |

### 182.B.2 — Isometrierelation

Zu prüfen in der konkret verwendeten Präsentation:

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-2] | $\mu_n^*\mu_n = 1$ $(n \geq 1)$ | ?[O]_{Quelle} — wird nicht aus der Bezeichnung importiert |

### 182.B.3 — Isometrie der Linksmultiplikation

**Lemma 182.1.** Sei $\overline{A}$ eine $C^*$-Algebra und $v \in \overline{A}$ mit $v^*v = 1$.
Dann gilt für jedes $x \in \overline{A}$: $\|vx\| = \|x\|$.

*Beweis.*
$$\|vx\|^2 = \|(vx)^*(vx)\| = \|x^*v^*vx\| = \|x^*x\| = \|x\|^2. \quad \square$$

Auf $v = \mu_n$ angewandt folgt bei bestätigter Relation:
$$\boxed{\|\mu_n u\| = \|u\|.}$$

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-3] | $\|\mu_n u\| = \|u\|$ | ✓[M] konditional auf [O-182-2] und [O-182-2N] |

### 182.B.4 — No-go-Satz

**Satz 182.2 — Ausschluss kontraktiver Isometrie-Intertwiner.**
Seien $\overline{A}$ eine unitale $C^*$-Algebra, $v \in \overline{A}$ eine Isometrie
und $u \in \overline{A}$. Falls $vu = cuv$ für ein $c \in \mathbb{C}$ mit $|c| < 1$,
dann gilt $u = 0$.

*Beweis.* $\|u\| = \|vu\| = |c|\,\|uv\| \leq |c|\,\|u\|$. Da $|c| < 1$: $u = 0$. $\square$

**Korollar 182.3 — Verdrehte BC-Nullkozykel.**
Sei $n > 1$ und $\mu_n u = n^{-\beta} u \mu_n$.
Falls $\mu_n^*\mu_n = 1$ und $\operatorname{Re}\beta > 0$, dann $u = 0$.

Denn $|n^{-\beta}| = n^{-\operatorname{Re}\beta} < 1$.

> **Hinweis:** Für reelles $\beta > 0$ stimmt $\operatorname{Re}\beta = \beta$.
> Für komplexes $\beta$ mit $\operatorname{Re}\beta > 0$ gilt dasselbe.
> Für $\operatorname{Re}\beta = 0$ (rein imaginäres $\beta$) liefert der Satz keinen Ausschluss.

$$\boxed{Z^0(A, M_{\sigma_\beta}) = \{0\}, \qquad \operatorname{Re}\beta > 0}$$

(sofern Nullkozykel in der $C^*$-Realisierung liegen und Isometrierelation bestätigt ist)

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-4] | $Z^0(A, M_{\sigma_\beta}) = \{0\}$ für $\operatorname{Re}\beta > 0$ | ✓[M]_neg konditional auf [O-182-2] und [O-182-2N] |

### 182.B.5 — Exakte Reichweite

**Benötigt:**
- $\mu_n u = n^{-\beta} u \mu_n$ für ein einziges $n > 1$
- $\mu_n^*\mu_n = 1$
- eine $C^*$-Norm oder treue $C^*$-Darstellung
- $\operatorname{Re}\beta > 0$

**Nicht benötigt:** $e(r)u = ue(r)$, $\mu_n^* u = n^\beta u \mu_n^*$, oder die Nullkozykelrelationen für alle $n$.

**Nicht bewiesen:** $HH^4(A, M_{\sigma_\beta})_{\mathrm{ch}} = 0$.
Bewiesen ist nur: $Z^0(A, M_{\sigma_\beta}) = \{0\}$, womit die spezielle Route
$u \smile \Omega_{\mathbf{p}}$ mit nichttrivialem verdrehten Nullkozykel ausgeschlossen ist.

**Für $\operatorname{Re}\beta = 0$:** kein Ausschluss aus diesem Satz.

---

## 182.C — Test des regulären graduierten Zentrums

Für das reguläre Koeffizientenmodul gilt $Z^0(A, A) = Z(A)$.
Gesucht: $u_g \in A_g$, $g \neq 1$, mit $u_g \in Z(A)$.

### 182.C.1 — Generatorenkriterium

Falls $A$ erzeugt wird von $\{e(r)\}_{r \in \mathbb{Q}/\mathbb{Z}}$,
$\{\mu_n, \mu_n^*\}_{n \geq 1}$, ist $u_g \in Z(A)$ äquivalent zu:

$$\boxed{\begin{aligned}
e(r)\,u_g &= u_g\,e(r) &&\forall r, \\
\mu_n\,u_g &= u_g\,\mu_n &&\forall n, \\
\mu_n^*\,u_g &= u_g\,\mu_n^* &&\forall n.
\end{aligned}}$$

Die Prüfung nur einer oder zweier Generatorfamilien genügt nicht.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-5] | $u_g \in Z(A)$ ist an sämtlichen Generatorfamilien zu prüfen | ✓[M] als formales Generatorenkriterium — Existenz eines nichttrivialen $u_g$ bleibt offen |

### 182.C.2 — Erforderliche Normalform

Um $Z(A)_g := Z(A) \cap A_g$ zu bestimmen, wird eine lineare Normalform
der homogenen Komponente $A_g$ benötigt.

**Unterknoten:**

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-5a] | Bestimme eine linear unabhängige Normalform für $A_g$ | ?[O] |

Ein negativer Zentrumsbefund ist **ohne Normalform oder treue Darstellung nicht gerechtfertigt**.

Das Verfahren:
1. Schreibe $u_g = \sum_j c_j w_j$ in homogener Normalform
2. Berechne $[e(r), u_g]$ für allgemeines $r$
3. Nutze lineare Unabhängigkeit der Normalformmonome → Bedingungen an $c_j$
4. Prüfe $[\mu_n, u_g] = 0$ und $[\mu_n^*, u_g] = 0$

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-6] | $Z(A)_g = 0$ für alle $g \neq 1$? | ?[O] — weder positiver noch negativer Ausgang wird antizipiert |

---

## 182.D — Neutraler Vier-Kozykel aus Primderivationen

Seien $p_1, p_2, p_3, p_4$ paarweise verschiedene Primzahlen.
Unter der graduierten Zerlegung $A = \bigoplus_{g \in \Gamma} A_g$:

$$D_p(a_g) := v_p(g)\,a_g.$$

### 182.D.1 — Wohldefiniertheit auf dem Quotienten

Sei $A = F/I$ mit einem $\Gamma$-graduierten freien Algebraobjekt $F$.
Damit $D_p$ auf $A$ wohldefiniert ist, muss $I$ homogen sein: $D_p(I) \subseteq I$.

Für homogene $a_g, b_h$:
$$D_p(a_g b_h) = v_p(gh)\,a_g b_h = (v_p(g)+v_p(h))\,a_g b_h = D_p(a_g)b_h + a_g D_p(b_h).$$

Somit ist $D_p$ eine Derivation. Außerdem: $[D_p, D_q] = 0$.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-7a] | $I$ ist homogen | ?[O] — offener Auditknoten (identisch mit [O-181-3]) |
| [O-182-7b] | $D_p(I) \subseteq I$ | ✓[M] konditional auf [O-182-7a] |
| [O-182-7c] | $D_p$ ist eine Derivation auf $A$ | ✓[M] konditional auf [O-182-7a] |

### 182.D.2 — Definition des neutralen Vier-Kozykels

**Unnormalisierte Alternierung** (Konvention in diesem Programm):

$$\Omega_{\mathbf{p}} := \sum_{\pi \in S_4} \operatorname{sgn}(\pi)\;
D_{p_{\pi(1)}} \smile D_{p_{\pi(2)}} \smile D_{p_{\pi(3)}} \smile D_{p_{\pi(4)}}.$$

Mit der Cup-Leibnizregel und $bD_p = 0$ folgt:

$$\boxed{b\Omega_{\mathbf{p}} = 0.}$$

Die Kommutativität der Derivationen ist für den Kozykelbeweis **nicht erforderlich**.

### 182.D.3 — Nichtverschwindensauswertung

Aus $D_{p_i}(\mu_{p_j}) = \delta_{ij}\,\mu_{p_j}$ (da $p_j$ prim, $v_{p_i}(p_j) = \delta_{ij}$):

$$\Omega_{\mathbf{p}}(\mu_{p_1}, \mu_{p_2}, \mu_{p_3}, \mu_{p_4})
= \mu_{p_1}\mu_{p_2}\mu_{p_3}\mu_{p_4}
= \mu_{p_1 p_2 p_3 p_4} \neq 0.$$

> **Normierungshinweis:** Bei **unnormalisierter Alternierung** ist der Wert $\mu_{p_1 p_2 p_3 p_4}$
> (kein $1/4!$-Faktor). Ein Faktor $4!$ entsteht bei der Paarung mit einem
> antisymmetrisierten Vierzyklus oder bei explizit normalisierter Alt-Konvention.

Falls $\mu_n^*\mu_n = 1$, ist $\mu_N \neq 0$, daher $\Omega_{\mathbf{p}} \neq 0$.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-8] | $\Omega_{\mathbf{p}} \neq 0$ | ✓[M] konditional auf [O-182-7a/b/c] und $\mu_{p_1 p_2 p_3 p_4} \neq 0$ ([O-182-2]) |

### 182.D.4 — Kozykel versus Kohomologieklasse

Aus $\Omega_{\mathbf{p}} \neq 0$ folgt nur das Nichtverschwinden als Kochain.

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-9] | $\Omega_{\mathbf{p}} \notin bC^3(A, A)$? | ?[O] — erfordert Hochschild-Vierzyklus mit nichtverschwindender Paarung |

---

## 182.E — Rückwirkung auf den Cup-Knoten aus NEU-181

Sei $M$ entweder das reguläre Modul $A$ oder ein typkorrekt definiertes verdrehtes Modul $M_\sigma$.
Falls $u \in Z^0(A, M)$, $\Omega_{\mathbf{p}} \in Z^4(A, A)$, und die Cup-Abbildung
die Hochschild-Leibnizregel erfüllt:

$$b(u \smile \Omega_{\mathbf{p}}) = (bu) \smile \Omega_{\mathbf{p}} + u \smile b\Omega_{\mathbf{p}} = 0.$$

| Knoten | Inhalt | Status |
|---|---|---|
| [O-181-9a] | $b(u \smile \Omega_{\mathbf{p}}) = 0$ | ✓[M] konditional auf Cup-Leibnizregel aus NEU-181 |
| [O-181-9b] | $u \smile \Omega_{\mathbf{p}} \neq 0$ | ?[O] — folgt nicht aus $u \neq 0$ und $\Omega_{\mathbf{p}} \neq 0$ allein |

---

## 182.F — Ergebnisbilanz

### Mathematisch gesichert

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-1] | $e(r)u = ue(r)$ nichttriviale Bedingung | ✓[M] |
| [O-182-3] | $\|\mu_n u\| = \|u\|$ | ✓[M] \| [O-182-2] ∧ [O-182-2N] |
| [O-182-4] | $\operatorname{Re}\beta > 0 \Rightarrow Z^0 = \{0\}$ | ✓[M]_neg \| [O-182-2] ∧ [O-182-2N] |
| [O-181-9a] | $b(u \smile \Omega_{\mathbf{p}}) = 0$ | ✓[M] \| Cup-Leibnizregel NEU-181 |

### Quellen- und Transferfragen (offen)

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-2] | $\mu_n^*\mu_n = 1$ in verwendeter Präsentation | ?[O]_{Quelle} |
| [O-182-2N] | Treue $C^*$-Einbettung von $A_\mathbb{Q}^{\mathrm{alg}}$ | ?[O] |

### Offene mathematische Fragen

| Knoten | Inhalt | Status |
|---|---|---|
| [O-182-5a] | Normalform für $A_g$ | ?[O] |
| [O-182-6] | $Z(A)_g = 0$ für $g \neq 1$? | ?[O] |
| [O-182-7a] | $I$ homogenes Ideal (= [O-181-3]) | ?[O] |
| [O-182-8] | $\Omega_{\mathbf{p}} \neq 0$ | ✓[M] \| [O-182-7] ∧ [O-182-2] |
| [O-182-9] | $[\Omega_{\mathbf{p}}] \neq 0$ in $HH^4$? | ?[O] |
| [O-181-9b] | $u \smile \Omega_{\mathbf{p}} \neq 0$? | ?[O] |

---

## 182.G — Nächster atomarer Schritt

Der unmittelbar nächste Quellen-/Präsentationsaudit lokalisiert:

$$\mu_m \mu_n = \mu_{mn}, \qquad \mu_n^*\mu_n = 1,$$

sowie eine treue Einbettung $A_\mathbb{Q}^{\mathrm{alg}} \hookrightarrow A_\mathbb{Q}^{C^*}$.

Nach Abschluss dieses Audits können [O-182-2], [O-182-2N] und [O-182-4] endgültig eingetragen werden.

Parallel dazu wird für den Zentrumstest eine homogene Normalform der Räume $A_g$
importiert oder neu bewiesen. **Ohne diese Normalform bleibt [O-182-6] gesperrt.**

> **Struktureller Gewinn:** Die drei Aussagen sind vollständig entkoppelt:
> - Der verdrehte Nullkozykelweg ist unter der Isometrierelation ausgeschlossen.
> - Der reguläre Zentrumsweg bleibt offen.
> - Der neutrale Vier-Kozykel $\Omega_{\mathbf{p}}$ ist unabhängig davon bereits
>   als nichtverschwindende Kochain konstruierbar.
