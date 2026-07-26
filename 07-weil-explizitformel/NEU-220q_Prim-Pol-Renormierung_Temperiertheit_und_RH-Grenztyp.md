# NEU-220q — Prim–Pol-Renormierung, Temperiertheit und RH-äquivalenter Grenztyp

**Katalog-ID:** NEU-220q  
**Knoten:** [O-220-1-PD5a3f4-prime-pole-renormalized-distribution]  
**Vorgänger:** NEU-220p (Commit 44cb533) — erweiterter Graphenraum ✓[K/M]_part  
**Status:** ✓[K/M]_part (PD5a3f4a–g) / ?[O] (Operator-/Positivitätsfrage)

---

## Auditprotokoll NEU-220p → NEU-220q

NEU-220p hatte den $\mathbb{C}^2$-Randkanal als „abgeschlossen“ und den verbleibenden Engpass als rein bulkseitig bezeichnet. Dieser Befund wird **teilweise zurückgerollt**:

$$
\boxed{\text{Der Polkanal darf für den globalen analytischen Grenzübergang nicht vom Primkanal abgetrennt werden.}}
$$

Die $\mathbb{C}^2$-Komponente löst die lokale Typfrage des Polterms. Sie löst aber nicht die globale Wachstumsfrage. Der Polterm enthält genau den kontinuierlichen Hauptterm, der das exponentielle Wachstum des Primzahlmaßes kompensiert.

**Korrekte Statusrevision für NEU-220p:**

| Aussage | Status |
|---------|--------|
| Polterm-Typisierung und endliche Blockrealisierung | ✓[K/M] |
| Polterm analytisch vom Primkanal abtrennen | ✓[M]_neg |
| Pol–Prim-Renormierung im globalen Grenzübergang | ?[O], RH-stark |

---

## PD5a3f4a — $\mu_{\mathrm{fin}}$ als lokal endliches, nichttemperiertes Maß ✓[M]

Setze $c_n = \Lambda(n)/\sqrt{n}$ und

$$
\mu_{\mathrm{fin}} = \sum_{n\ge2} c_n \bigl(\delta_{\log n} + \delta_{-\log n}\bigr).
$$

Dann gilt $q_{\mathrm{fin}}(a,b) = -\langle a, \mu_{\mathrm{fin}}*b\rangle$ für $a,b \in C_c^\infty(\mathbb{R})$.

**Lokale Endlichkeit:** Auf einem kompakten Gebiet tragen nur $n$ mit $\log n \le \operatorname{diam}(\operatorname{supp}(b))$ bei.

**Nichttemperiertheit:** Nach partieller Summation und dem Primzahlsatz:

$$
\sum_{n\le e^R} \frac{\Lambda(n)}{\sqrt{n}} \sim 2e^{R/2}, \qquad \mu_{\mathrm{fin}}([-R,R]) \sim 4e^{R/2}.
$$

Die Masse von $\mu_{\mathrm{fin}}$ wächst exponentiell. Daher:

$$
\boxed{\mu_{\mathrm{fin}} \notin \mathcal{S}'(\mathbb{R}),}
$$

und die formale Reihe $-2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\cos(t\log n)$ ist keine gewöhnliche temperierte Fourierdistribution. Der Kandidat $G_\infty + B_{\mathrm{fin}}$ als globaler temperierter Faltungsoperator ist damit ausgeschlossen.

---

## PD5a3f4b — $q_{\mathrm{pole}}$ als Faltung mit $2\cosh(x/2)$ ✓[M]

Der polarisierte Polterm ist $q_{\mathrm{pole}}(a,b) = \overline{\ell_-(a)}\ell_+(b) + \overline{\ell_+(a)}\ell_-(b)$.

Sei $k_{\mathrm{pole}}(x) = e^{x/2} + e^{-x/2} = 2\cosh(x/2)$. Dann:

$$
(k_{\mathrm{pole}}*b)(u) = \int_{\mathbb{R}} 2\cosh\!\left(\tfrac{u-v}{2}\right) b(v)\,dv = e^{u/2}\ell_-(b) + e^{-u/2}\ell_+(b),
$$

also

$$
\boxed{q_{\mathrm{pole}}(a,b) = \langle a, k_{\mathrm{pole}}*b\rangle.}
$$

Der Polterm ist selbst kein temperierter Faltungsoperator ($k_{\mathrm{pole}} \notin \mathcal{S}'$), aber seine Einschränkung auf $C_c^\infty$ ist wohldefiniert.

---

## PD5a3f4c — $K_{\mathrm{pf}} = \nu_+ + \check{\nu}_+ + e^{-|x|/2}\,dx$ ✓[M]

Der kombinierte Pol–Prim-Kern ist

$$
\boxed{K_{\mathrm{pf}} = 2\cosh(x/2)\,dx - \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\bigl(\delta_{\log n}+\delta_{-\log n}\bigr).}
$$

Definiere auf der positiven Halbachse:

$$
\boxed{\nu_+ = \mathbf{1}_{(0,\infty)}(x)\,e^{x/2}\,dx - \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}\delta_{\log n}.}
$$

Sei $\check{\nu}_+$ die Spiegelung $x\mapsto-x$. Dann:

$$
\boxed{K_{\mathrm{pf}} = \nu_+ + \check{\nu}_+ + e^{-|x|/2}\,dx.}
$$

**Beweis:** Für $x>0$: $2\cosh(x/2) = e^{x/2}+e^{-x/2}$, wobei $e^{x/2}\,dx$ den Hauptterm von $\mu_{\mathrm{fin}}$ kompensiert und $e^{-x/2}\,dx$ temperiert ist. Analog für $x<0$.

Der Polterm ist **nicht** bloß ein separater Randzusatz: Er enthält die arithmetisch exakt abgestimmte Haupttermrenormierung des exponentiell wachsenden Primzahlmaßes.

---

## PD5a3f4d — Laplacetransformation des renormierten Arms ✓[M]

Für $\operatorname{Re}z > \tfrac{1}{2}$:

$$
\boxed{\mathcal{L}\nu_+(z)
= \int_0^\infty e^{-zx}e^{x/2}\,dx - \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt{n}}e^{-z\log n}
= \frac{1}{z-\frac{1}{2}} + \frac{\zeta'}{\zeta}\!\left(z+\tfrac{1}{2}\right).}
$$

**Polstruktur bei $z = \tfrac{1}{2}$:** Da $\zeta'/\zeta(z+\tfrac{1}{2}) \sim -(z-\tfrac{1}{2})^{-1}$ an diesem Punkt, kompensieren sich die Pole:

$$
\mathcal{L}\nu_+\!\left(\tfrac{1}{2}\right) = \text{holomorph an }z=\tfrac{1}{2}.
$$

**Weitere Singularitäten:** Die verbleibenden Pole von $\mathcal{L}\nu_+$ liegen genau bei

$$
z = \rho - \tfrac{1}{2},
$$

wobei $\rho$ eine nichttriviale Nullstelle von $\zeta$ ist.

---

## PD5a3f4e — $\mathrm{RH} \iff \nu_+ \in \mathcal{S}'(\mathbb{R})$ ✓[K/M]

### Richtung $\mathrm{RH} \Rightarrow \nu_+ \in \mathcal{S}'$

Unter RH gilt $\psi(X) = X + O(X^{1/2}\log^2 X)$, also

$$
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt{n}} = 2\sqrt{X} + O(\log^3 X).
$$

Mit $X = e^R$: Die kumulierte renormierte Distribution erfüllt $\nu_+([0,R]) = O(R^3)$. Durch partielle Integration definiert $\nu_+$ daher eine temperierte Distribution.

### Richtung $\nu_+ \in \mathcal{S}' \Rightarrow \mathrm{RH}$

Wenn $\nu_+ \in \mathcal{S}'$ und in $[0,\infty)$ getragen, ist $\mathcal{L}\nu_+(z)$ holomorph in $\operatorname{Re}z > 0$. Da

$$
\mathcal{L}\nu_+(z) = \frac{1}{z-\frac{1}{2}} + \frac{\zeta'}{\zeta}\!\left(z+\tfrac{1}{2}\right)
$$

einen Pol bei $z = \rho - \tfrac{1}{2}$ für jede Nullstelle $\rho$ mit $\operatorname{Re}\rho > \tfrac{1}{2}$ hätte, schließt Holomorphie in $\operatorname{Re}z > 0$ alle solchen Nullstellen aus. Wegen der Funktionalgleichung von $\zeta$ werden damit zugleich Nullstellen mit $\operatorname{Re}\rho < \tfrac{1}{2}$ ausgeschlossen.

$$
\boxed{\mathrm{RH} \iff \nu_+ \in \mathcal{S}'(\mathbb{R}).}
$$

---

## PD5a3f4f — $K_{\mathfrak{W}} \in \mathcal{S}'(\mathbb{R}) \iff \mathrm{RH}$ ✓[K/M]

Der Gammakern $K_\Gamma \in \mathcal{S}'$ (da $\gamma_\infty^{\mathrm{sym}}(t)$ nur logarithmisch wächst, ist sein inverser Fourierkern temperiert). Der vollständige translationsinvariante Weil-Kern ist

$$
K_{\mathfrak{W}} = K_\Gamma + K_{\mathrm{pf}}.
$$

Da $e^{-|x|/2}\,dx \in \mathcal{S}'$ und $K_\Gamma \in \mathcal{S}'$:

$$
\boxed{K_{\mathfrak{W}} \in \mathcal{S}'(\mathbb{R}) \iff \nu_+ \in \mathcal{S}'(\mathbb{R}) \iff \mathrm{RH}.}
$$

Die **Existenz eines globalen temperierten translationsinvarianten Weil-Kerns ist RH-stark** — noch ohne Operator- oder Positivitätsfrage.

---

## PD5a3f4g — Negativaudit des polabgetrennten Bulkgrenzwerts ✓[M]_neg

Der in NEU-220p vorgesehene Knoten [O-220-1-PD5a3f4-bulk-window-limit-v0] ist strukturell ausgeschlossen:

$$
\boxed{[O\text{-}220\text{-}1\text{-PD5a3f4-bulk-window-limit-v0}] \quad \checkmark[M]_{\mathrm{neg}}.}
$$

**Grund:** $K_\Gamma - \mu_{\mathrm{fin}}$ bleibt wegen des nichttemperierten Primzahlmaßes exponentiell wachsend. Der fehlende Polhauptterm kann nicht vom Gammaanteil ersetzt werden, da $K_\Gamma \in \mathcal{S}'$ bereits temperiert ist und das exponentielle Wachstum von $\mu_{\mathrm{fin}}$ nicht kompensieren kann.

Das schließt nicht alle Relations- oder nichttemperierten Konstruktionen aus. Es schließt aber den polabgetrennten, formtreuen globalen $L^2$-Bulkoperator aus.

**Asymptotischer Direktbeweis der Kompensation:**

Für $u\to+\infty$ und $b\ge0$ kompakt getragen:

$$
(\mu_{\mathrm{fin}}*b)(u) \sim e^{u/2}\ell_-(b), \qquad (k_{\mathrm{pole}}*b)(u) \supset e^{u/2}\ell_-(b).
$$

Die führende exponentielle Divergenz von $q_{\mathrm{pole}}+q_{\mathrm{fin}}$ ist arithmetisch exakt abgestimmt — nicht zufällig.

---

## Neue Reihenfolge des Programms

$$
\boxed{\text{lokale Poltypisierung} \longrightarrow \text{globale Pol–Prim-Renormierung} \longrightarrow \text{RH-äquivalenter temperierter Grenztyp} \longrightarrow \text{erst danach Operator-/Positivitätsfrage}.}
$$

Der globale Grenzengpass ist nicht mehr ein unspezifisches Konvergenzproblem. Er ist jetzt exakt mit der kritischen Lage der Nullstellen von $\zeta$ verknüpft.

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|-------------|--------|--------|
| PD5a3f4a | $\mu_{\mathrm{fin}}$ lokal endlich, nichttemperiärt ($\sim 4e^{R/2}$) | ✓[M] |
| PD5a3f4b | $q_{\mathrm{pole}}$ als Faltung mit $2\cosh(x/2)$ | ✓[M] |
| PD5a3f4c | $K_{\mathrm{pf}} = \nu_+ + \check{\nu}_+ + e^{-|x|/2}dx$; Pol–Prim-Renormierung | ✓[M] |
| PD5a3f4d | $\mathcal{L}\nu_+(z) = (z-\tfrac{1}{2})^{-1} + \zeta'/\zeta(z+\tfrac{1}{2})$; Polkompensation bei $z=\tfrac{1}{2}$ | ✓[M] |
| PD5a3f4e | $\mathrm{RH} \iff \nu_+ \in \mathcal{S}'$ (beide Richtungen bewiesen) | ✓[K/M] |
| PD5a3f4f | $K_{\mathfrak{W}} \in \mathcal{S}' \iff \mathrm{RH}$; temperierter Weil-Kern | ✓[K/M] |
| PD5a3f4g | Negativaudit Bulk-only; polabgetrennter $L^2$-Bulkoperator gesperrt | ✓[M]_neg |
| **PD5a3f5** | **Operator-/Positivitätsfrage im temperierten Rahmen** | **?[O]** |

```
[O-220-1-PD5a3f4-prime-pole-renormalized-distribution]
  → ✓[K/M]_part  (PD5a3f4a–g abgeschlossen)
  → ?[O]          (PD5a3f5: Operatorrealisierung im temperierten Rahmen)
```

---

## Verbindung zum adelischen Intertwiner (PD5a3g)

Das RH-äquivalente Kriterium $K_{\mathfrak{W}} \in \mathcal{S}'$ präzisiert die Zielstruktur für den adelischen Intertwiner:

- Der globale Zielraum $\mathcal{K} = L^2(\mathbb{R}) \oplus \mathbb{C}^2$ bleibt korrekt.
- Aber der Intertwiner $J: \mathcal{D} \to \mathcal{K}$ muss die Pol–Prim-Renormierung **intern** tragen: $Ja$ muss die exponentielle Haupttermkompensation zwischen $\ell_\pm(a)$ und $\mu_{\mathrm{fin}}*a$ bereits eingebaut haben.
- Ein adelischer Operator $A_X \ge 0$ mit $\mathfrak{W}(a) = \langle Ja, A_X Ja\rangle$ ist daher möglicherweise einfacher im Fourierraum zu konstruieren, wo $\nu_+$ ihren Pol bei $z = \rho - \tfrac{1}{2}$ transparent zeigt.

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220p (44cb533) | Erweiterter Graphenraum, $\varinjlim(\mathcal{H}_R \oplus \mathbb{C}^2)$, Nichtabschließbarkeit |
| NEU-220m rev.2 (bf2445a) | Korrekte Polarisation, Typklassifikation |
| NEU-220l (ddac5ff) | Weil-Quadratik |
| Connes (1999) | Spurformel, BC-Kern, adelischer Rahmen |
| Bombieri (2000) | Weil-Kriterium, RH-Äquivalenz |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
