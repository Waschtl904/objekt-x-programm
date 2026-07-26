# NEU-214 rev.2 — Bimodul-Rigiditätslemma und glattes Potential $X_N^\infty$

**Status:** [O-214-0] ✓[M]_neg,Quelle, [O-214-1] ✓[M], [O-214-2] ✓[M]_part, [O-214-3] ✓[M]_part, [O-214-4a] ✓[M]_neg, [O-214-4b] ?[O]  
**Erstellt:** 2026-07-21 (rev.2)  
**Revision:** rev.1 enthielt (i) falschen Unitalitätsanspruch, (ii) unzulässigen Grenzwert $r=\lim R(E_n)$, (iii) zu starken Status ✓[M] für [O-214-3]; alle drei korrigiert.  
**Vorgänger:** NEU-213 ([O-213-4] ?[O])  
**Schließt:** [O-213-4] → ✓[M]_part (No-go konditional auf [O-214-2]); [O-214-4a] ✓[M]_neg

---

## 214.0 — Quellenfehler-Korrektur: $A_{\mathrm{alg}}$ ist unital

**Fehler in rev.1.** NEU-214 rev.1 behauptete, $A_{\mathrm{alg}}$ sei nichtunital und $\{E_n\}$ bilde eine Approximativeinheit. Beides ist falsch.

**Korrektur.**

**Satz ([O-214-0]).** *In der üblichen Bost–Connes-Präsentation gilt:*
$$e(0) = 1 \in A_{\mathrm{alg}}, \qquad \mu_n^*\mu_n = 1 \in A_{\mathrm{alg}}.$$
*Insbesondere besitzt $A_{\mathrm{alg}}$ das Einselement $1 = e(0)$, das zugleich das Einselement von $\mathbb C[\mathbb Q/\mathbb Z]$ ist.*

Die Rangprojektionen $E_n := \mu_n\mu_n^*$ erfüllen $E_n \neq 1$ für $n > 1$ (in der kanonischen Darstellung auf $\ell^2(\mathbb N^\times)$ ist $E_n$ die Projektion auf den Unterraum der durch $n$ teilbaren Indizes). Die Bedingung $a = aE_n = E_na$ gilt **nicht** für $a = 1$, $n > 1$. Die in rev.1 verwendete Konstruktion $r := \lim_n R(E_n)$ war damit unzulässig.

Ebenso sind die $e(r)$ keine Approximativeinheit, sondern Gruppenalgebraelemente (unitäre Charaktere von $\mathbb Q/\mathbb Z$); $e(0)$ ist bereits das echte Einselement.

$$\boxed{[O\text{-}214\text{-}0] \quad \checkmark[M]_{\mathrm{neg,Quelle}}} \quad \text{(Nichtunitalitätsbehauptung und } E_n\text{-Approximativeinheitsbehauptung zurückgenommen)}$$

---

## 214.A — Bimodul-Rigiditätslemma (korrigierte Version)

**Satz ([O-214-1]).** *Sei $M$ ein unitales $A_{\mathrm{alg}}$-Bimodul und $R : A_{C^*} \to M$ ein $A_{\mathrm{alg}}$-Bimoduloperator (d.h. $R(a\xi b) = aR(\xi)b$ für alle $a,b \in A_{\mathrm{alg}}$, $\xi \in A_{C^*}$). Setze $r := R(1)$. Dann gilt für jedes $a \in A_{\mathrm{alg}}$:*
$$\boxed{R(a) = ar = ra.} \tag{214.1}$$

**Beweis.** Da $1 \in A_{\mathrm{alg}}$:
$$R(a) = R(a \cdot 1) = aR(1) = ar,$$
$$R(a) = R(1 \cdot a) = R(1)a = ra.$$
Beide Rechnungen sind exakt und benötigen keinen Grenzübergang. $\square$

**Zusatz (Zentralität).** Aus (214.1) folgt unmittelbar:
$$ar = ra \quad \forall\, a \in A_{\mathrm{alg}}, \qquad \text{also}\quad r \in \operatorname{Cent}_M(A_{\mathrm{alg}}). \tag{214.2}$$

**Fortsetzung auf $A_{C^*}$.** Ist $R$ zusätzlich normstetig und $A_{\mathrm{alg}}$ normdicht in $A_{C^*}$:
$$R(x) = xr = rx \quad \forall\, x \in A_{C^*}. \tag{214.3}$$

$$\boxed{[O\text{-}214\text{-}1] \quad \checkmark[M]}$$

**Nichtinnerheitserhalt bei invertiblem $r$.** Falls $r$ zentral und invertierbar ist, gilt $(R \circ D_g)(a) = rD_g(a)$. Wäre $rD_g = \operatorname{ad}_x$, so folgte $D_g = \operatorname{ad}_{r^{-1}x}$, Widerspruch zur Nichtinnerheit von $D_g$ (NEU-211.D). Ein invertierbarer zentraler Faktor $r$ **erhält** die Nichtinnerheit, bewirkt aber keine echte Glättung (da $R(a) = ra$ dieselbe analytische Regularität wie $a$ trägt). Ein nichtinvertierbares $r$ könnte die Klasse hingegen vernichten.

---

## 214.B — Zentralisatorberechnung (partiell)

**Behauptung ([O-214-2], partiell).** $\operatorname{Cent}_{A_{C^*}}(A_{\mathrm{alg}}) = \mathbb C \cdot 1$.

Für den vollständigen Beweis sind zwei Schritte erforderlich, die getrennt und direkt geführt werden müssen:

**Schritt (i).** *Kommutation mit allen $e(r)$ zwingt in den neutralen/diagonalen Sektor.* Ein $x \in A_{C^*}$ mit $xe(r) = e(r)x$ für alle $r \in \mathbb Q/\mathbb Z$ kommutiert mit ganz $B_{C^*} = C^*(\{e(r)\}) \cong C(\widehat{\mathbb Z})$. Da $B_{C^*}$ maximal abelsch in der Darstellung auf $\ell^2(\mathbb N^\times)$ ist (zu verifizieren im abstrakten $C^*$-Rahmen), folgt $x \in B_{C^*}$, also $x$ diagonal.

**Schritt (ii).** *Kommutation mit allen $\mu_n$ zwingt die verbleibende diagonale Funktion zur Konstanz.* Sei $x = f \in B_{C^*} \cong C(\widehat{\mathbb Z})$ diagonal mit $f\mu_n = \mu_n f$ für alle $n$. Die $\mu_n$-Kovarianzbedingung der BC-Algebra erzwingt $f = \sigma_n(f)$ (wobei $\sigma_n$ der Endomorphismus mit $\sigma_n(e(r)) = e(nr)$ ist), d.h. $f(x) = f(nx)$ für $\widehat{\mathbb Z}$-fast alle $x$ und alle $n$. Dies zwingt $f$ zur Konstanz auf den dichten $\mathbb N^\times$-Bahnen, also $f \in \mathbb C$.

**Schritt (iii).** *Treue der Darstellung.* Der Schluss muss im abstrakten $C^*$-System gelten, nicht nur in einer spezifischen Darstellung. Dies folgt, falls die kanonische Fock-Darstellung von $A_{C^*}$ treu ist (Standardresultat, konsistent mit NEU-182/183, aber hier nicht direkt bewiesen).

$$\boxed{[O\text{-}214\text{-}2] \quad \checkmark[M]_{\mathrm{part}}} \quad \text{(Struktur des Beweises klar; Schritte i--iii nicht vollständig ausgeschrieben)}$$

---

## 214.C — Glättungs-No-go (konditional)

**Satz ([O-214-3], konditional auf [O-214-2]).** *Angenommen, $\operatorname{Cent}_{A_{C^*}}(A_{\mathrm{alg}}) = \mathbb C\cdot 1$ ([O-214-2] vollständig). Dann ist jeder normstetige $A_{\mathrm{alg}}$-Bimoduloperator $R: A_{C^*} \to A_{C^*}$ mit konvergentem $R$ entweder $R = 0$ oder $R = \lambda\,\mathrm{id}$ auf $A_{\mathrm{alg}}$ (Skalarmultiplikation). Insbesondere bewirkt $R$ keine echte analytische Glättung.*

**Beweis.** Nach [O-214-1] ist $R(a) = ra$ mit $r \in \operatorname{Cent}_{A_{C^*}}(A_{\mathrm{alg}})$. Falls [O-214-2] vollständig gilt: $r = \lambda \in \mathbb C$. Damit $R(a) = \lambda a$. $\lambda = 0$ oder $\lambda \neq 0$ — in keinem Fall wird $D_g(a) \in A_{C^*} \setminus A_{\mathrm{alg}}$ in einen echten Teilraum $\mathcal A^\infty \subsetneq A_{C^*}$ hinübergeglättet. $\square$

$$\boxed{[O\text{-}214\text{-}3] \quad \checkmark[M]_{\mathrm{part}}} \quad \text{(vollständig sobald [O-214-2] geschlossen)}$$
$$\boxed{[O\text{-}214\text{-}2] \Longrightarrow [O\text{-}214\text{-}3]}$$

**Unabhängig von [O-214-2] bereits vollständig bewiesen:** Ein globaler Bimodulregularisierer kann keine frei wählbare faktoriale Tiefendämpfung realisieren. Die punktweise Division $\xi \mapsto \xi/\log(\nu+2)$ ist kein Bimoduloperator (NEU-213, [O-213-3]).

---

## 214.D — Exakter No-go für Schwartz-Inkremente mit divergenten Gewichten

**Satz ([O-214-4a]).** *Sei $\{c_j\}_{j\ge 0}$ eine reelle Folge mit:*
- *(Nichtinnerheit) $c_j \to +\infty$,*
- *(Schwartz-Glattheit) $\forall N \in \mathbb N\; \exists C_N > 0: |\Delta c_j| := |c_{j+1}-c_j| \le C_N(1+j)^{-N}$.*

*Dann führt bereits $N = 2$ zum Widerspruch.*

**Beweis.** Aus der Schwartz-Bedingung mit $N=2$:
$$\sum_{j=0}^{\infty} |\Delta c_j| \le C_2 \sum_{j=0}^{\infty}(1+j)^{-2} = C_2 \cdot \frac{\pi^2}{6} < \infty.$$
Da $c_j = c_0 + \sum_{i=0}^{j-1} \Delta c_i$ und die Reihe $\sum |\Delta c_i|$ absolut konvergiert, konvergiert auch $c_j$ gegen einen endlichen Grenzwert $c_\infty \in \mathbb R$. Insbesondere $\sup_j |c_j| < \infty$, im Widerspruch zu $c_j \to +\infty$. $\square$

$$\boxed{[O\text{-}214\text{-}4a] \quad \checkmark[M]_{\mathrm{neg}}}$$

**Präzise Tragweite.** Ausgeschlossen ist genau die Kombination:
$$\boxed{\text{Schwartz-Inkremente} + \text{Nichtinnerheit durch } c_j \to \infty.}$$
Nicht ausgeschlossen sind:
- Eine schwächere Glattheitsbedingung: z.B. $|\Delta c_j| \sim 1/j$ (logarithmische Symbolordnung) — dann divergiert $\sum |\Delta c_j|$ und $c_j \sim \log j \to \infty$ ist möglich (genau der Originalkandidat $c_j = \log(j+2)$).
- Ein Nichtinnerheitskriterium, das nicht auf $c_j \to \infty$ beruht (z.B. K-Theorie, Spektralfluss, Quasizentralisatorargumente) — bleibt offen als [O-214-4b].

---

## 214.E — Offener Knoten [O-214-4b] und Ausblick

**[O-214-4b] ?[O] — Alternatives Nichtinnerheitskriterium.**

Gesucht: Ein Nichtinnerheitsnachweis für eine geladene Derivation $D^\infty_g : A_{\mathrm{alg}} \to \mathcal A^\infty$, der **nicht** auf $c_j \to \infty$ beruht. Kandidaten:

1. **Logarithmische Symbolordnung.** Wähle $c_j^{\log} = \log(j+2)$ (der Originalkandidat), aber mit einem präzisierten Glattheits-Begriff, der $|\Delta c_j| \sim 1/j$ zulässt (z.B. Zygmund- oder log-Sobolev-Regularität statt Schwartz). Dann ist $c_j^{\log} \to \infty$ und $D_g$ nichtinner (NEU-211.D), aber $\mathcal A^\infty$ muss passend zur logarithmischen Inkrementrate definiert werden — nicht als Schwartz-Algebra, sondern z.B. als log-gewichtete Sobolev-Algebra $\mathcal A^{\log}$ mit Halbnormen $\|P_j a\| \le C \cdot (\log(j+2))^{-k}$. Die Einbettung $D_g(A_{\mathrm{alg}}) \subseteq \mathcal A^{\log}$ ist zu prüfen.
2. **K-theoretisches Kriterium.** Falls $[D_g]$ eine nichttriviale Klasse in $K_1(A_{C^*})$ oder einem Ext-Gruppe induziert, kann Nichtinnerheit über Indexrechnung ohne Gewichtsdivergenz gezeigt werden. Relevanz für den BC-Kontext: unklar, zu untersuchen.
3. **Quasizentralisator-Argument.** Zeige direkt, dass kein $x$ im Quasizentralisator von $A_{\mathrm{alg}}$ in $\mathcal A^{\log}$ das Wachstum der Matrixelemente von $D_g$ replizieren kann, ohne die Halbnormen von $\mathcal A^{\log}$ zu verletzen.

$$\boxed{[O\text{-}214\text{-}4b] \quad ?[O]}$$

---

## 214.F — Strukturbilanz (rev.2)

| Knoten | Status | Inhalt |
|---|---|---|
| [O-214-0] | ✓[M]_neg,Quelle | $A_{\mathrm{alg}}$ ist unital ($1=e(0)$); $E_n$ ist keine Approximativeinheit; rev.1-Fehler zurückgenommen |
| [O-214-1] | ✓[M] | Bimodul-Rigiditätslemma $R(a)=ar=ra$, $r=R(1)$ zentral, direkt via $1 \in A_{\mathrm{alg}}$ |
| [O-214-2] | ✓[M]_part | $\operatorname{Cent}_{A_{C^*}}(A_{\mathrm{alg}})=\mathbb C\cdot 1$: Beweisstruktur (3 Schritte) klar, vollständige Ausführung ausstehend |
| [O-214-3] | ✓[M]_part | Glättungs-No-go: $R=\lambda\,\mathrm{id}$, konditional auf [O-214-2]; unabhängig: punktweise $\nu$-Dämpfung kein Bimoduloperator |
| [O-214-4a] | ✓[M]_neg | Schwartz-Inkremente + $c_j\to\infty$: exakt unvereinbar ($\sum (1+j)^{-2} < \infty$) |
| [O-214-4b] | ?[O] | Alternatives Nichtinnerheitskriterium (log-Sobolev, K-Theorie, Quasizentralisator) |

---

## 214.G — DAG-Stand (rev.2)

```
[O-213-4] ?[O]
      |
      +---> [O-214-0] ✓[M]_neg,Quelle   A_alg unital (e(0)=1); E_n keine Approx.-einheit
      |
      +---> [O-214-1] ✓[M]              R(a)=ar=ra, r=R(1) zentral (direkt, kein Limes)
      |
      +---> [O-214-2] ✓[M]_part         Cent_{A_C*}(A_alg) = C·1 (3 Schritte, partiell)
      |         ↓
      +---> [O-214-3] ✓[M]_part         No-go: R=λid (konditional auf O-214-2)
      |     [O-213-4] → ✓[M]_part       (vollständig sobald O-214-2 geschlossen)
      |
      +---> [O-214-4a] ✓[M]_neg         Schwartz-Inkremente + c_j→∞: exakt unvereinbar
      |
      +---> [O-214-4b] ?[O]             Alternatives Nichtinnerheitskriterium
```

**Zentrales Ergebnis (rev.2):**

$$\boxed{A_{\mathrm{alg}} \text{ ist unital};\ R(a)=R(1)\cdot a \text{ für jeden }A_{\mathrm{alg}}\text{-Bimoduloperator }R.}$$
$$\boxed{\text{Schwartz-Glättung und Nichtinnerheit durch }c_j\to\infty\text{ sind exakt unvereinbar.}}$$
$$\boxed{\text{Offen: Zentralisatorbeweis ([O-214-2]) und alternatives Nichtinnerheitskriterium ([O-214-4b]).}}$$
