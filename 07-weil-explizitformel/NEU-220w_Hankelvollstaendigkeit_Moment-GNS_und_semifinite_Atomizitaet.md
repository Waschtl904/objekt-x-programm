# NEU-220w — Hankelvollständigkeit, Moment-GNS-Weyl-Modell und semifinite Atomizität

**Katalog-ID:** NEU-220w
**Knoten:** [O-220-1-PD5a3f10-Hankel-completeness-moment-GNS]
**Vorgänger:** NEU-220v rev.2 (Commit e18da4f) — Stieltjes-Kriterium, korrigierte Rückrichtung, Residuenkonvention
**Status:** ✓[K/M]_part (PD5a3f10a–f abgeschlossen, konditional zur Positivitätsvoraussetzung) / ?[O] (adelische Quellkonstruktion, RH-stark)

---

## 1. Verstärkung: die vollständige Hankel-Hierarchie ist RH-äquivalent

In NEU-220v wurden endliche Hankeltests als notwendige Bedingungen beschrieben. Die vollständige unendliche Hierarchie ist darüber hinaus **hinreichend**, also RH-äquivalent.

Schreibe in einer Umgebung von \(w=0\)

$$
M_\Xi(w) = \sum_{k=0}^\infty \mu_k w^k, \qquad \boxed{\mu_k = -\frac{k+1}{(2k+2)!}(\log\Xi)^{(2k+2)}(0).}
$$

Definiere \(H_N^{(0)} = (\mu_{i+j})_{i,j=0}^N\), \(H_N^{(1)} = (\mu_{i+j+1})_{i,j=0}^N\). Dann gilt:

$$
\boxed{\mathrm{RH} \iff H_N^{(0)}\succeq0 \text{ und } H_N^{(1)}\succeq0 \quad \forall N\ge0.}
$$

### Hinrichtung

Unter RH: \(\mu_k = \sum_{\gamma>0} m_\gamma/\gamma^{2k+2}\). Mit \(\nu_\Xi = \sum_{\gamma>0}(m_\gamma/\gamma^2)\delta_{\gamma^{-2}}\) gilt \(\mu_k = \int_{[0,\infty)} x^k\,d\nu_\Xi(x)\). Damit sind \((\mu_k)\) und die verschobene Folge \((\mu_{k+1})\) positiv definit — genau die beiden Hankelbedingungen.

### Rückrichtung

Seien \(H_N^{(0)}, H_N^{(1)} \succeq 0\) für alle \(N\). Nach dem Stieltjes-Momentsatz existiert ein positives Radonmaß \(\nu\) auf \([0,\infty)\) mit \(\mu_k = \int x^k\,d\nu(x)\); die Positivität beider Hankelfamilien ist dafür notwendig und hinreichend.

Da \(M_\Xi\) bei \(0\) analytisch ist, erfüllen die Koeffizienten eine exponentielle Schranke \(|\mu_k|\le CR^{-k}\) für ein \(R>0\). Da \(\mu_k\ge0\), zwingt dies jedes darstellende Maß auf ein kompaktes Intervall: \(\operatorname{supp}\nu\subseteq[0,L]\) für ein endliches \(L\) (sonst würde Masse oberhalb \(L+\varepsilon\) schnelleres Momentwachstum erzwingen).

Damit ist \(F_\nu(w) = \int_{[0,L]} d\nu(x)/(1-wx)\) in einer Umgebung von \(0\) analytisch mit derselben Taylorreihe wie \(M_\Xi\), also \(F_\nu(w)=M_\Xi(w)\) — zunächst lokal, dann durch analytische Fortsetzung.

Die Cauchytransformierte \(G_\nu(z) = \tfrac1z M_\Xi(1/z) = \int_{[0,L]} d\nu(x)/(z-x)\) ist meromorph. Durch die Stieltjes-Inversionsformel wird das Maß eindeutig aus der Cauchytransformierten zurückgewonnen; eine meromorphe Cauchytransformierte besitzt daher nur atomare Masse an ihren reellen Polen, mit Massen gleich den negativen Residuen.

Folglich besitzt \(M_\Xi\) nur Pole auf der positiven reellen Achse. Also liegen sämtliche Nullstellen von \(\Phi\) in \((0,\infty)\), und damit sämtliche Nullstellen von \(\Xi\) sind reell — das ist RH.

---

## 2. Moment-GNS statt sofortiger semifiniter Spur

Definiere auf \(\mathbb{C}[x]\), mit \(x^*=x\), das lineare Funktional \(\mathcal L_\Xi(x^k)=\mu_k\). Die vollständigen Hankelbedingungen sind äquivalent zu

$$
\boxed{\mathcal L_\Xi(p^*p)\ge0} \qquad\text{und}\qquad \boxed{\mathcal L_\Xi(xp^*p)\ge0}
$$

für alle Polynome \(p\).

Die erste Bedingung erzeugt via GNS einen Hilbertraum \(\mathcal H_\Xi^{\mathrm{mom}}\), einen zyklischen Vektor \(\Omega_\Xi\) und einen symmetrischen Multiplikationsoperator \(J_\Xi\). Die zweite erzwingt \(J_\Xi\ge0\). Wegen des exponentiell beschränkten Momentwachstums ist das darstellende Maß kompakt getragen, also ist \(J_\Xi\) sogar beschränkt. Es gilt dann

$$
\boxed{M_\Xi(w) = \left\langle \Omega_\Xi, (I-wJ_\Xi)^{-1} \Omega_\Xi \right\rangle.}
$$

Unter RH ist das Spektralmaß von \(J_\Xi\) bezüglich \(\Omega_\Xi\)

$$
\boxed{\nu_\Xi = \sum_{\gamma>0} \frac{m_\gamma}{\gamma^2} \delta_{\gamma^{-2}}.}
$$

Damit entsteht ein konkreter Weyl-/GNS-Operator \(J_\Xi\) aus den Zentralableitungen von \(\Xi\), nicht aus einer vorgegebenen Nullstellenliste. Das ist noch kein RH-Beweis, weil die Positivität von \(\mathcal L_\Xi\) gerade RH-äquivalent ist. Es ist aber ein deutlich konkreterer Zieltyp:

$$
\boxed{\text{Konstruiere eine positive BC-/KMS-Funktionalität, deren Momente } \mu_k \text{ sind.}}
$$

Sobald das gelingt, liefert GNS automatisch den positiven Operator und die Stieltjesfunktion.

---

## 3. Audit der semifiniten Spurvariante

Angenommen, es existieren \((\mathcal N_X,\tau_X)\), \(B_X\ge0\), \(B_X^{-1}\in L^1(\mathcal N_X,\tau_X)\) mit \(\tau_X((B_X-w)^{-1})=M_\Xi(w)\). Die Spektraltheorie liefert das positive Maß \(\nu_B(E) = \tau_X(E_{B_X}(E))\) mit

$$
\tau_X((B_X-w)^{-1}) = \int_{(0,\infty)} \frac{d\nu_B(\lambda)}{\lambda-w}.
$$

Da \(M_\Xi\) meromorph ist, muss \(\nu_B\) rein atomar sein — ein kontinuierlicher Anteil würde über die Stieltjes-Inversionsformel einen nichtmeromorphen Randbeitrag erzeugen. Außerdem gilt an jedem Pol (mit der in NEU-220v rev.2 fixierten Residuenkonvention):

$$
\boxed{\tau_X(E_{B_X}(\{\lambda\})) = -\operatorname{Res}_{w=\lambda}M_\Xi(w).}
$$

Für die Xi-Funktion:

$$
\boxed{\tau_X(E_{B_X}(\{\gamma^2\})) = m_\gamma \in\mathbb N.}
$$

Damit erzwingt die Identität nicht nur Positivität, sondern auch: rein atomaren \(\tau_X\)-sichtbaren Spektraltyp, keine kontinuierliche Spektralkomponente, ganzzahlige Spurgewichte, und exakt die Nullstellenvielfachheiten. Die semifinite Umgebung umgeht das diskrete Spektralproblem also nicht — sie muss eine integer-quantisierte atomare Spur hervorbringen.

---

## Revidierter Status

| Aussage | Status |
|---|---|
| \(z_0^2\in[0,\infty)\Rightarrow z_0\) reell oder imaginär | ✓[M]_neg (verworfen, siehe NEU-220v rev.2) |
| \(z_0^2\in[0,\infty)\Rightarrow z_0\in\mathbb R\) | ✓[M] |
| Einzelne endliche Hankeltests | ✓[M]_part |
| Vollständige doppelte Hankelhierarchie \(\iff\) RH | ✓[K/M] |
| Moment-GNS-/Weyl-Realisierung | ✓[K/M] konditional zur Positivität von \(\mathcal L_\Xi\) |
| Adelische Herleitung der Momentpositivität | ?[O], RH-stark |
| Semifinite Spuridentität \(\tau_X((B_X-w)^{-1})=M_\Xi(w)\) | ?[O], RH-stark |
| Atomizität und ganzzahlige Spurgewichte bei Identität | ✓[M] |

```
[O-220-1-PD5a3f10-Hankel-completeness-moment-GNS]
  -> ✓[K/M]_part  (vollständiger Hankel-RH-Beweis, Moment-GNS-Modell)
  -> ?[O]          (adelische Quellkonstruktion von L_Xi bzw. (N_X, tau_X, B_X), RH-stark)
```

---

## Strategische Standortbestimmung: Rückkehr zu Objekt X

Die Kette NEU-220a–w hat den Zieltyp von \(X_\infty\) aus Fehlern und No-go-Sätzen zunehmend schärfer destilliert:

$$
\text{Gammafaktor} + \text{Primzahlpotenzen} + \text{Polrenormierung} \longrightarrow \text{Weil-Form} \longrightarrow \text{positive adelische Resolventenspur} = M_\Xi(w).
$$

Weitere RH-äquivalente Reformulierungen führen allein kaum noch näher an eine Konstruktion. Der nächste Hauptblock kehrt daher bewusst zur Quellseite zurück, nicht mehr als Unterfrage von PD5a3, sondern als eigenständiger Knoten:

**NEU-221 — Adelische Momentquelle für den positiven Weil-Operator**

Leitfrage: Welches bereits vorhandene BC-/KMS-Objekt kann als \(B_X^{-1}\) dienen und die ersten Xi-Momente erzeugen? Erster konkreter Konstruktionstest (statt sofort der vollen Identität für alle \(w\)):

$$
\tau_X(B_X^{-1})=\mu_0, \qquad \tau_X(B_X^{-2})=\mu_1,
$$

mit quellseitig definiertem \(B_X\), ohne Verwendung von Nullstellen.

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-220v rev.2 (e18da4f) | Korrigiertes Stieltjes-Kriterium, Residuenkonvention |
| NEU-220u (d7c4f16) | Schattenklassenzwang, \(\det_2\)-Normalformen |
| Stieltjes (1894) / Akhiezer (1965) | Momentproblem, Hankelmatrizen, Inversionsformel |
| Connes (1999) | BC-Kern, adelischer Rahmen, KMS-Zustände |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog. Folgeknoten: NEU-221.*
