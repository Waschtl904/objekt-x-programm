# NEU-220r — Nullstellenmaß, Nichtabschließbares Sampling und bedingtes Spektralmodell

**Katalog-ID:** NEU-220r  
**Knoten:** [O-220-1-PD5a3f5-zero-measure-sampling-and-selfadjointness]  
**Vorgänger:** NEU-220q (Commit ed81836) — Prim–Pol-Renormierung ✓[K/M]_part  
**Status:** ✓[K/M]_part (PD5a3f5a–g) / ?[O] (adelisch erzeugter Spektralraum)

---

## Auditprotokoll NEU-220q → NEU-220r

NEU-220q hatte $K_{\mathfrak{W}} \in \mathcal{S}' \iff \mathrm{RH}$ bewiesen und den Weg zur Operatorrealisierung als nächsten Schritt bezeichnet. Das folgende Audit ergibt:

$$
\boxed{\nu_+\in\mathcal{S}' \text{ genügt für einen symmetrischen Rigged-Space-Operator }\mathcal{S}\to\mathcal{S}', \text{ aber nicht für einen selbstadjungierten Operator auf }L^2(\mathbb{R})\oplus\mathbb{C}^2.}
$$

Die Temperiertheit löst das globale Distributionstypproblem. Sie löst weder die $L^2$-Abschließbarkeit noch die Operatorrealisierung.

---

## PD5a3f5a — $K_{\mathfrak{W}} \in \mathcal{S}' \Rightarrow T_{\mathfrak{W}}: \mathcal{S} \to \mathcal{S}'$ ✓[K/M]

Ist $K_{\mathfrak{W}} \in \mathcal{S}'(\mathbb{R})$, dann ist

$$
\boxed{T_{\mathfrak{W}} b = K_{\mathfrak{W}} * b}
$$

ein wohldefinierter stetiger Operator $T_{\mathfrak{W}}: \mathcal{S}(\mathbb{R}) \to \mathcal{S}'(\mathbb{R})$.

Ist $K_{\mathfrak{W}}$ reell und gerade (was aus der Hermitizität von $\mathfrak{W}$ folgt), gilt im distributionstheoretischen Sinn $\langle a, T_{\mathfrak{W}}b\rangle = \overline{\langle b, T_{\mathfrak{W}}a\rangle}$. Damit erhält man einen **symmetrischen Operator im Rigging** $\mathcal{S} \subset L^2 \subset \mathcal{S}'$. Das ist ein echter Fortschritt, aber noch kein abgeschlossener oder selbstadjungierter $L^2$-Operator.

---

## PD5a3f5b — $\mathcal{F}K_{\mathfrak{W}} = \sqrt{2\pi}\,\mu_Z$ unter RH – konditionaler Befund ✓[M]

Verwende die unitäre Fouriertransformation $(\mathcal{F}a)(t) = \frac{1}{\sqrt{2\pi}}\int a(u)e^{itu}\,du$ und setze $A_a(t) = \sqrt{2\pi}\,(\mathcal{F}a)(t)$.

Unter RH hat jede nichttriviale Nullstelle die Form $\rho = \tfrac{1}{2}+i\gamma_\rho$. Die mit Vielfachheiten gewichtete Summe in der expliziten Formel liefert:

$$
\mathfrak{W}(a,b) = \sum_\rho m_\rho \overline{A_a(\gamma_\rho)} A_b(\gamma_\rho)
= 2\pi\int_{\mathbb{R}} \overline{(\mathcal{F}a)(t)}\,(\mathcal{F}b)(t)\,d\mu_Z(t),
$$

wobei $\mu_Z = \sum_\rho m_\rho \delta_{\gamma_\rho}$ das Nullstellenmaß ist. Mit $\mathcal{F}(K*b) = \sqrt{2\pi}\,(\mathcal{F}K)(\mathcal{F}b)$ folgt:

$$
\boxed{\mathcal{F}K_{\mathfrak{W}} = \sqrt{2\pi}\,\mu_Z \qquad \text{unter RH}.}
$$

**Spektralbefund:** Die Fouriertransformierte des vollständigen Weil-Kerns ist unter RH kein gewöhnliches Symbol, sondern ein **positives reines Punktmaß**. Der Pol–Prim-Renormierungsmechanismus (NEU-220q, PD5a3f4c–d) wandelt die exponentiellen Divergenzen beider Terme durch Randwert-Kompensation in atomare Spektralkanäle um: An jeder Nullstellenordinate $\gamma_\rho$ heben sich die imaginären Hauptwertanteile der beiden Arme auf, während die Dirac-Anteile addiert werden.

---

## PD5a3f5c — Negativaudit: Kein selbstadjungierter Lebesgue-$L^2$-Multiplikator ✓[M]_neg

Ein translationsinvarianter selbstadjungierter Operator auf $L^2(\mathbb{R},dt)$ erscheint nach Fouriertransformation als Multiplikation mit einer reellen messbaren Funktion $m(t)$. Ein allgemeines Element von $\mathcal{S}'$ ist jedoch keine messbare Funktion; insbesondere können Dirac-Maße und deren Ableitungen nicht punktweise mit $L^2(dt)$-Äquivalenzklassen multipliziert werden.

Da $\mu_Z$ singulär bezüglich des Lebesgue-Maßes ist, existiert kein messbares $m(t)$ mit $m(t)\,dt = d\mu_Z(t)$. Folglich:

$$
\boxed{\text{Temperiertheit} \not\Rightarrow \text{Fouriermultiplikator auf }L^2(\mathbb{R},dt).}
$$

Der selbstadjungierte translationsinvariante Weil-Operator auf $L^2(\mathbb{R},dt)$ ist damit auch unter RH ausgeschlossen. Das widerspricht nicht dem Hilbert–Pólya-Programm; es zeigt, dass der gesuchte Hilbertraum nicht das naive Lebesgue-$L^2$ sein kann.

---

## PD5a3f5d — Samplingoperator $J_Z: C_c^\infty \to \mathcal{H}_Z$ ✓[M]

Unter RH definiere auf $\mathcal{D} = C_c^\infty(\mathbb{R})$ den Nullstellen-Samplingoperator

$$
J_Z a = \bigl(A_a(\gamma_\rho)\bigr)_\rho \in \mathcal{H}_Z := L^2(\mathbb{R},\mu_Z) \cong \ell^2(\{\gamma_\rho\}, m_\rho).
$$

Wegen des schnellen Abfalls $|A_a(\gamma)| = O(|\gamma|^{-N})$ für alle $N$ (da $a \in \mathcal{S}$) und der klassischen Nullstellendichte $\sim (T\log T)/(2\pi)$ bis Höhe $T$ ist $J_Za \in \mathcal{H}_Z$ wohldefiniert. Es gilt:

$$
\boxed{\mathfrak{W}(a,b) = \langle J_Za, J_Zb\rangle_{\mathcal{H}_Z} \qquad \text{(unter RH)}.}
$$

In der Faktorisierungssprache: $A_X = I_{\mathcal{H}_Z}$. Diese Konstruktion setzt RH bereits voraus (reelle $\gamma_\rho$, positive Form, positives $\mu_Z$). Sie ist daher kein RH-Beweis, sondern ein **konditionales Spektralmodell**.

---

## PD5a3f5e — Nichtabschließbarkeit von $J_Z$ auf ungewichtetem $L^2$ ✓[M]_neg

Das ist das unendlichdimensionale Analogon der nichtabschließbaren Randspur $L_\partial$ (NEU-220p, PD5a3f3d).

Wähle eine Nullstellenordinate $\gamma_0$ und $\varphi \in C_c^\infty(\mathbb{R})$ mit $\int \varphi(v)\,dv = 1$. Setze

$$
a_R(u) = \frac{1}{R}\varphi\!\left(\frac{u}{R}\right)e^{-i\gamma_0 u}.
$$

Dann $\|a_R\|_2 = R^{-1/2}\|\varphi\|_2 \to 0$, aber $A_{a_R}(\gamma_0) = \int \varphi(v)\,dv = 1$. Für $\gamma \ne \gamma_0$ gilt $A_{a_R}(\gamma) = \int \varphi(v)e^{iR(\gamma-\gamma_0)v}\,dv \to 0$ (Riemann–Lebesgue). Der schnelle Abfall zusammen mit der Nullstellendichte liefert Konvergenz in $\mathcal{H}_Z$ gegen den Basisvektor $e_{\gamma_0}$:

$$
\boxed{a_R \to 0 \text{ in }L^2, \qquad J_Z a_R \to e_{\gamma_0} \ne 0 \in \mathcal{H}_Z.}
$$

$$
\boxed{J_Z: C_c^\infty \subset L^2(\mathbb{R}) \longrightarrow \mathcal{H}_Z \text{ ist nicht abschließbar.}}
$$

---

## PD5a3f5f — $\mathcal{H}_Z = L^2(\mu_Z)$ als konditionales Spektralmodell ✓[K/M] (konditional)

Auf $\mathcal{H}_Z$ ist der Multiplikationsoperator

$$
(M_\gamma c)(\gamma) = \gamma\, c(\gamma), \qquad
\mathcal{D}(M_\gamma) = \left\{c \in \mathcal{H}_Z : \sum_\rho m_\rho \gamma_\rho^2 |c(\gamma_\rho)|^2 < \infty\right\}
$$

selbstadjungiert (reeller Multiplikator auf einem gewichteten $\ell^2$). Da $\mathfrak{W}(a,b) = \langle J_Za, J_Zb\rangle_{\mathcal{H}_Z}$ unter RH, entspricht der Weil-Form im Sinn des Hilbert–Pólya-Programms: $M_\gamma$ hat reelles Spektrum $\{\gamma_\rho\}$, also Nullstellen auf der kritischen Linie.

**Konditionaler Status:** Das Modell ist exakt, setzt aber RH voraus. Es ist kein Beweis, sondern beschreibt präzise, wie ein RH-freier Beweis aussehen müsste: Man bräuchte $\mathcal{H}_Z$ und $M_\gamma$ ohne Vorannahme über die $\gamma_\rho$.

---

## PD5a3f5g — Anforderungen an einen nichttautologischen adelischen Spektralraum ?[O]

Der eigentliche Durchbruch wäre nicht, $\mu_Z$ als Spektralraum nachträglich zu verwenden, sondern es **aus der adelischen Architektur als positives Spektralmaß herzuleiten**, ohne zuvor RH einzusetzen.

### Warum $L^2(\mathbb{R}) \oplus \mathbb{C}^2$ nicht genügt

Nach globaler Pol–Prim-Renormierung erscheinen zusätzlich unendlich viele atomare Kanäle $\delta_{\gamma_\rho}$. Der natürliche bedingte erweiterte Raum ist schematisch

$$
\boxed{L^2(\mathbb{R}) \oplus \mathbb{C}^2 \oplus L^2(\mu_Z),}
$$

wobei $L^2(\mu_Z)$ nicht durch einen abschließbaren Samplingoperator aus dem Bulk-$L^2$ erreichbar ist. Eine abstrakte unitäre Identifikation von $L^2(\mu_Z)$ mit einem Teilraum von $L^2(\mathbb{R})$ wäre möglich (beide separabel), aber nicht kanonisch und ohne arithmetischen Gehalt.

### Anforderungsprofil

Ein nichttautologischer adelischer Spektralraum $\mathcal{H}_X$ mügssste:

1. **RH-frei konstruiert** sein: keine Vorannahme über die Lage der Nullstellen.
2. **Einen natürlichen Operator $A_X$** tragen mit $\mathfrak{W}(a) = \langle Ja, A_X Ja\rangle_{\mathcal{H}_X}$ für einen RH-frei definierten Intertwiner $J$.
3. **Positivität von $A_X$** aus der adelischen/arithmetischen Struktur folgen, nicht aus der Spektrallage.
4. **Die atomaren Nullstellen-Spektralkanäle** natürlich als Teil der Architektur tragen, nicht als nachträglichen Zusatz.
5. **Mit dem BC-Kern von Connes kompatibel** sein (PD5a3g).

---

## Knotentabelle

| Teilaufgabe | Inhalt | Status |
|-------------|--------|--------|
| PD5a3f5a | $K_{\mathfrak{W}} \in \mathcal{S}' \Rightarrow T_{\mathfrak{W}}: \mathcal{S}\to\mathcal{S}'$ symmetrisch | ✓[K/M] |
| PD5a3f5b | $\mathcal{F}K_{\mathfrak{W}} = \sqrt{2\pi}\mu_Z$ unter RH; atomare Spektralkanäle | ✓[M], konditional |
| PD5a3f5c | Lebesgue-$L^2$-Multiplikator ausgeschlossen; $\mu_Z \perp dt$ | ✓[M]_neg |
| PD5a3f5d | $J_Z: C_c^\infty \to \mathcal{H}_Z$ wohldefiniert unter RH | ✓[M], konditional |
| PD5a3f5e | $J_Z$ nicht abschließbar auf ungewichtetem $L^2$; Analogon zu $L_\partial$ | ✓[M]_neg |
| PD5a3f5f | $\mathcal{H}_Z = L^2(\mu_Z)$, $M_\gamma$ selbstadjungiert; konditionales Hilbert–Pólya-Modell | ✓[K/M], konditional |
| PD5a3f5g | Anforderungen an nichttautologischen adelischen Spektralraum; $L^2\oplus\mathbb{C}^2\oplus L^2(\mu_Z)$ | ?[O], RH-stark |

```
[O-220-1-PD5a3f5-zero-measure-sampling-and-selfadjointness]
  → ✓[K/M]_part  (PD5a3f5a–g abgeschlossen)
  → ?[O]          (PD5a3f5g: adelischer Spektralraum ohne RH-Vorannahme)
```

---

## Strukturelle Gesamtbilanz (NEU-220m bis NEU-220r)

| Schicht | Inhalt | Status |
|---------|--------|--------|
| Testfunktionsform | $\mathfrak{W}: \mathcal{D}\times\mathcal{D}\to\mathbb{C}$ hermitesch | ✓[K/M] |
| Pol–Prim-Renormierung | $K_{\mathrm{pf}} = \nu_+ + \check{\nu}_+ + e^{-|x|/2}dx$ | ✓[M] |
| Temperiertes Kriterium | $K_{\mathfrak{W}} \in \mathcal{S}' \iff \mathrm{RH}$ | ✓[K/M] |
| Rigged-Space-Operator | $T_{\mathfrak{W}}: \mathcal{S}\to\mathcal{S}'$ symmetrisch | ✓[K/M] |
| Bedingtes Spektralmodell | $\mathcal{H}_Z = L^2(\mu_Z)$ unter RH | ✓[K/M], konditional |
| Selbstadjungierter $L^2$-Operator | Auf Lebesgue-$L^2$ ausgeschlossen | ✓[M]_neg |
| Adelischer Spektralraum RH-frei | Offenes Durchbruchsziel | ?[O], RH-stark |

$$
\boxed{\text{Temperiertheit liefert den globalen distributionstheoretischen Kern;}
\quad\text{Selbstadjungigkeit verlangt einen neuen Spektralhilbertraum, nicht bloß }L^2\text{-Bulk plus }\mathbb{C}^2.}
$$

---

## Abhängigkeiten

| Referenz | Inhalt |
|----------|--------|
| NEU-220q (ed81836) | $K_{\mathfrak{W}} \in \mathcal{S}' \iff \mathrm{RH}$, $\mathcal{L}\nu_+$ Polstruktur |
| NEU-220p (44cb533) | $L_\partial$ nicht abschließbar, $\varinjlim(\mathcal{H}_R\oplus\mathbb{C}^2)$ |
| NEU-220n (6bbfd22) | Fensteroperatoren $(\mathcal{H}_R, W_R)$ |
| Connes (1999) | Spurformel, BC-Kern, Hilbert–Pólya |
| Bombieri (2000) | Weil-Kriterium, explizite Formel |
| Davenport, Multiplicative Number Theory | Nullstellendichte, Primzahlsatz unter RH |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
