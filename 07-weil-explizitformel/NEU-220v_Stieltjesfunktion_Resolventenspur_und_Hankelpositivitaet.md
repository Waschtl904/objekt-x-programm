# NEU-220v — Stieltjesfunktion, Resolventenspur und Hankelpositivität (rev.2)

**Katalog-ID:** NEU-220v (rev.2)
**Knoten:** [O-220-1-PD5a3f9-Stieltjes-Weyl-resolvent-criterion]
**Vorgänger:** NEU-220u (Commit d7c4f16) — Spektraldeterminante, Schattenklasse ✓[K/M]_part, konditional
**Status:** ✓[K/M]_part (PD5a3f9a–f) / ?[O] (PD5a3f9g, RH-stark)
**Revision:** korrigiert PD5a3f9d (algebraischer Fehler in der Rückrichtung) und fixiert die Residuenkonvention. Nachfolger: NEU-220w.

---

## Präzisierung der Schattenaussage aus NEU-220u

$$
A_+^{-1}\in\bigcap_{p>1}\mathcal{S}_p, \qquad A_+^{-1}\notin\mathcal{S}_1.
$$

Für \(B_+ := A_+^2\) gilt dagegen

$$
\boxed{B_+^{-1}=A_+^{-2}\in\mathcal{S}_1.}
$$

Damit lässt sich das RH-starke Operatorziel vollständig in der quadrierten Spektralvariablen formulieren, ohne den \(\det_2\)-Formalismus: Es reduziert sich auf eine skalare Stieltjes-/Herglotz-Eigenschaft.

---

## PD5a3f9a — \(\Phi(w)\) branchfrei aus der geraden \(\Xi\) ✓[K/M]

Da \(\Xi(z)=\xi(1/2+iz)\) gerade ist, existiert eine eindeutig bestimmte ganze Funktion \(\Phi(w)\) mit \(\Phi(z^2) = \Xi(z)/\Xi(0)\), \(\Phi(0)=1\). Die Schreibweise \(\Phi(w) = \Xi(\sqrt{w})/\Xi(0)\) ist nur Kurzform; die Definition über die gerade Potenzreihe von \(\Xi\) ist branchfrei und wohldefiniert auf ganz \(\mathbb{C}\).

---

## PD5a3f9b — \(M_\Xi(w) = -\Phi'(w)/\Phi(w)\) ✓[K/M]

$$
\boxed{M_\Xi(w) := -\frac{\Phi'(w)}{\Phi(w)}.}
$$

Außerhalb \(w=0\):

$$
\boxed{M_\Xi(w) = -\frac{i}{2\sqrt{w}}\frac{\xi'}{\xi}\left(\frac12+i\sqrt{w}\right),}
$$

wobei der scheinbare Singularitätspunkt \(w=0\) wegen der Geradheit von \(\Xi\) hebbar ist.

### Residuenkonvention (neu, korrigiert)

Bei einer Nullstelle \(\lambda\) von \(\Phi\) der Vielfachheit \(m\) gilt

$$
M_\Xi(w) = -\frac{\Phi'(w)}{\Phi(w)} \sim -\frac{m}{w-\lambda} = \frac{m}{\lambda-w}.
$$

Daher ist der komplexanalytische Residuenwert

$$
\boxed{\operatorname{Res}_{w=\lambda}M_\Xi=-m.}
$$

Die positive Masse des Stieltjes-Maßes ist also

$$
\boxed{\mu(\{\lambda\}) = -\operatorname{Res}_{w=\lambda}M_\Xi = m>0.}
$$

Dieses Vorzeichen ist autoritativ für alle späteren Spur- und Spektralprojektionsformeln (siehe NEU-220w).

---

## PD5a3f9c — RH \(\Rightarrow\) Stieltjes-Darstellung ✓[M]

Unter RH: \(\Phi(w) = \prod_{\gamma>0}(1-w/\gamma^2)^{m_\gamma}\), also

$$
\boxed{M_\Xi(w) = \sum_{\gamma>0}\frac{m_\gamma}{\gamma^2-w}.}
$$

Die Summe konvergiert lokal gleichmäßig außerhalb der positiven Pole (\(\sum m_\gamma/\gamma^2 < \infty\)). Für \(w=x+iy\), \(y>0\): \(\operatorname{Im}\,1/(\gamma^2-w) = y/((\gamma^2-x)^2+y^2)>0\), und für \(x<0\): \(M_\Xi(x)>0\). Damit ist \(M_\Xi\) unter RH eine meromorphe Stieltjesfunktion.

---

## PD5a3f9d — Stieltjes-Eigenschaft \(\Rightarrow\) RH ✓[M] (KORRIGIERT)

**Fehler in rev.1:** Der Zwischensatz „\(z_0^2\in[0,\infty)\Rightarrow z_0\) reell oder rein imaginär“ war falsch, und das anschließende Argument über \(\zeta(s)<0\) für \(0<s<1\) war zur Ausschließung rein imaginärer Nullstellen unnötig eingeführt worden.

**Korrektur:** Aus der Stieltjes-Eigenschaft folgt, dass sämtliche Pole von \(M_\Xi\), also sämtliche Nullstellen \(w_0\) von \(\Phi\), in \([0,\infty)\) liegen. Ist \(z_0\) eine Nullstelle von \(\Xi\), so ist \(w_0=z_0^2\), und

$$
\boxed{z_0^2\in[0,\infty) \;\Longrightarrow\; z_0\in\mathbb R,}
$$

**nicht** „\(z_0\) reell oder rein imaginär“. Für \(z_0=iy\neq0\) wäre \(z_0^2=-y^2<0\), also gar nicht in \([0,\infty)\) — der Fall rein imaginärer Nullstellen wird durch die Bedingung \(z_0^2\ge0\) bereits ausgeschlossen, ohne dass \(\zeta(s)<0\) auf \(0<s<1\) herangezogen werden muss. Dieses zusätzliche Argument ist für diese Rückrichtung überflüssig (es bleibt als eigenständiger, klassischer Fakt richtig, wird hier aber nicht benötigt).

Damit ist jedes \(z_0\) reell, äquivalent zu \(\operatorname{Re}\rho = 1/2\) über die Substitution \(z=(\rho-1/2)/i\).

### Exakte RH-Äquivalenz ✓[K/M]

$$
\boxed{\mathrm{RH} \iff M_\Xi \text{ ist eine meromorphe Stieltjesfunktion mit Träger in } [0,\infty).}
$$

---

## PD5a3f9e — \(B_X \ge 0\), \(B_X^{-1} \in \mathcal{S}_1\) als Zieloperator ✓[K/M]

Sei \(B_X\) positiv selbstadjungiert mit kompaktem Resolventen und \(B_X^{-1} \in \mathcal{S}_1\). Dann ist \(M_X(w) = \operatorname{Tr}((B_X-w)^{-1})\) eine Stieltjesfunktion. Schon die Identität

$$
\boxed{\operatorname{Tr}\bigl((B_X-w)^{-1}\bigr) = M_\Xi(w)}
$$

zusammen mit Normierung bei \(w=0\) liefert \(\det(I-wB_X^{-1}) = \Phi(w)\). Strategisch einfacher: zuerst \(B_X \ge 0\) konstruieren statt direkt einen symmetrischen Operator \(H_X\).

### Semifinite Version (adelische Zielarchitektur)

Gesucht: \((\mathcal{N}_X,\tau_X)\), \(B_X \ge 0\) affiliiert an \(\mathcal{N}_X\), mit \(B_X^{-1} \in L^1(\mathcal{N}_X,\tau_X)\), sodass

$$
\boxed{\tau_X\bigl((B_X-w)^{-1}\bigr) = M_\Xi(w).}
$$

---

## PD5a3f9f — Moment- und Hankelpositivität ✓[M]_part, unter RH (STATUS PRÄZISIERT)

Taylorentwicklung bei \(w=0\): \(M_\Xi(w) = \sum_{k\ge0}\mu_k w^k\), mit

$$
\boxed{\mu_k = \operatorname{Tr}(B_X^{-k-1}) = \operatorname{Tr}(A_+^{-2k-2}) = -\frac{k+1}{(2k+2)!}(\log\Xi)^{(2k+2)}(0).}
$$

Hankelmatrizen \(H_N^{(0)} = (\mu_{i+j})\), \(H_N^{(1)} = (\mu_{i+j+1})\) müssen \(\succeq 0\) sein. **Revidierte Aussage (siehe NEU-220w für den vollen Beweis):** Die endlichen Hankeltests sind einzeln nur notwendig; die vollständige unendliche doppelte Hankelhierarchie ist jedoch RH-äquivalent (hinreichend und notwendig), nicht nur notwendig, wie in rev.1 formuliert.

---

## PD5a3f9g — Export zur semifiniten BC-/KMS-Resolventenspur ?[O], RH-stark

Unverändert gegenüber rev.1. Siehe NEU-220w für die Moment-GNS-Realisierung und die Audit der semifiniten Spurvariante (Atomizität, ganzzahlige Spurgewichte).

---

## Revidierter Status

| Aussage | Status |
|---|---|
| \(z_0^2\in[0,\infty)\Rightarrow z_0\) reell oder imaginär | ✓[M]_neg (verworfen, fehlerhaft) |
| \(z_0^2\in[0,\infty)\Rightarrow z_0\in\mathbb R\) | ✓[M] (korrigiert) |
| \(\zeta(s)<0\)-Argument für PD5a3f9d | nicht erforderlich (entfernt aus dieser Rückrichtung) |
| Einzelne endliche Hankeltests | ✓[M]_part (nur notwendig) |
| Vollständige doppelte Hankelhierarchie \(\iff\) RH | siehe NEU-220w |

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-220u (d7c4f16) | Schattenklassenzwang, \(\det_2\)-Normalformen |
| NEU-220t (7b02a03) | Metrikblock-Klassifikation |
| NEU-220w | Vollständiger Hankel-RH-Beweis, Moment-GNS-Weyl-Modell, semifinite Atomizität |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog. Revision 2.*
