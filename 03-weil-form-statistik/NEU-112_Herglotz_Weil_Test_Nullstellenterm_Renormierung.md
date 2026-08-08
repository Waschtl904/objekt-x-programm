# NEU-112 — Herglotz-Weil-Test: Nullstellenterm und Normierungsinterface

**Stand:** 1. Juli 2026 | **Patch:** 8. August 2026 (Pass-A Gruppe D, Patch D-2/2)
**Vorgänger:** NEU-111 (Herglotz-Weil-Brücke; \(m_{\rm arith}\) Herglotz \(\Leftrightarrow\) RH; signed-\(\Gamma\))
**Nächste Nummer:** NEU-113

> **Überblick (Patch):** NEU-112 versucht den Schritt von \(m_{\rm arith}\) zur quadratischen Weil-Form.
> Vier Punkte waren fehlerhaft; NEU-113 supersediert 112.2/3 mit der korrekten Behandlung.
> Der konzeptionelle Kern — **lineare \(\to\) quadratische Ebene** muss durch Autokorrelation gehoben werden — bleibt richtig und wichtig.

---

## ~~Satz NEU-112.1 (ursprünglich)~~ — Herglotz-Maß-Zerlegung — **×[M] SUPERSEDED**

> **Audit-Befund (Pass-A, 8. Aug. 2026):** Die ursprüngliche Zerlegung
> \(\mu_\xi = \sum_\gamma\delta_\gamma + \mu_{\Gamma,\rm ren}\)
> ist falsch. Gamma-, Pol- und Primbeiträge sind keine zusätzlichen Atome des Herglotz-Spektralmaßes;
> sie stammen aus der faktoriellen Zerlegung der expliziten Formel,
> nicht aus \(m_{\rm arith}=-\Xi'/\Xi\).

## Satz NEU-112.1 (korrigiert) — Herglotz-Spektralmaß von \(m_{\rm arith}\)

Unter RH ist das Herglotz-Spektralmaß von
\(m_{\rm arith}(z) = -\Xi'(z)/\Xi(z)\)
das **rein atomare Nullstellenmaß**:

$$
\boxed{\mu_{\rm arith} = \sum_{\gamma\in\Gamma} m_\gamma\,\delta_\gamma.}
$$

\(\Gamma = \{\gamma\in\mathbb{R} : \xi(\tfrac{1}{2}-i\gamma)=0\}\),
\(m_\gamma\geq 1\) die Nullstellenmultiplizität.

Gamma-, Pol- und Primbeiträge entstehen bei der arithmetischen Seite der **expliziten Formel** über
\(s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\) — sie sind keine zusätzlichen Spektralatome von \(m_{\rm arith}\).

**Status: \(\checkmark[M]\)** (unter RH)

---

## ~~Satz NEU-112.2 (ursprünglich)~~ — Stieltjes-Kern \(\to\) Quadratbetrag — **×[M] SUPERSEDED**

> **Audit-Befund:** Die ursprüngliche Fassung behauptete, die Stieltjes-Darstellung
> \(\sum_\gamma 1/(\gamma-z)\) wirke durch Residuen so, dass \(\sum_\gamma|\hat f(\gamma)|^2\) entsteht.
> Das ist ein **Typfehler**: eine lineare Auswertung liefert zunächst
> \(W_{\rm zeros}[\Phi] = \sum_\gamma m_\gamma\,\widehat\Phi(\gamma)\) — ein lineares Funktional.
> Der Quadratbetrag entsteht erst durch den Autokorrelationslift \(\Phi=\phi^**\phi\).
> **NEU-113.2–3 supersediert diese Fassung.**

## Satz NEU-112.2 (korrigiert) — Autokorrelationslift und Quadratform

**Schritt 1:** Lineare Weil-Auswertung:

$$
W_{\rm zeros}[\Phi] = \sum_{\gamma\in\Gamma} m_\gamma\,\widehat\Phi(\gamma).
$$

**Schritt 2:** Autokorrelationslift. Setze \(\Phi = \phi^* * \phi\), dann gilt \(\widehat\Phi(\gamma) = |\widehat\phi(\gamma)|^2\), und man erhält die Quadratform:

$$
\boxed{Q_{\rm zeros}[\phi]
:= W_{\rm zeros}[\phi^**\phi]
= \sum_{\gamma\in\Gamma} m_\gamma\,|\widehat\phi(\gamma)|^2.
\quad\checkmark[M]}
$$

Dies ist praktisch derselbe Typfix wie der spätere Kanonisierungsschritt
\(a \to g_{a,a} \to h_{a,a} \to B_W(a,a)\) in P02.

> **Literaturvergleich:** NEU-113.2–3 schreibt denselben Lift korrekt und supersediert
> die ursprüngliche Fassung dieses Satzes.

**Status: \(\checkmark[M]\)** (korrigierte Fassung; SUPERSEDED durch NEU-113)

---

## ~~Satz NEU-112.3 (ursprünglich)~~ — Vierfachsumme — **×[M] SUPERSEDED**

> **Audit-Befund:** Die ursprüngliche Gleichung
> \(Q_{\rm Weil} = Q_{\rm zeros} + Q_\Gamma + Q_{\rm poles} + Q_{\rm prime}\)
> doppelzählt alle Terme: NEU-113 stellt ausdrücklich fest,
> dass \(W_{\rm zeros} = W_{\rm pole/triv}+W_\Gamma+W_{\rm prime}\)
> und daher \(W_{\rm zeros}+W_\Gamma+W_{\rm prime}+W_{\rm pole/triv} = 2W_{\rm zeros}\).

## Satz NEU-112.3 (korrigiert) — Zero-side = arithmetic-side

Die normalisierte Weil-Distribution ist \(\underline{\rm entweder}\):

$$
W_\xi^{\rm norm} = W_{\rm zeros},
$$

\(\underline{\rm oder}\) äquivalent ausgedrückt als arithmetische Seite:

$$
W_\xi^{\rm norm} = W_{\rm pole/triv}+W_\Gamma+W_{\rm prime},
$$

aber **nicht** deren Summe. Der Schutzgedanke — \(m_{\rm arith}\) ist nicht dasselbe Objekt wie die quadratische Weilform — ist korrekt; die Begründung erfolgt über **linear vs.\ quadratisch / Testfunktionspaarung**, nicht über eine additive Zerlegung.

**Status: \(\checkmark[M]\)** (Doppelzählung beseitigt; NEU-113 supersediert)

---

## ~~Satz NEU-112.4 (ursprünglich)~~ — Typfehler Funktion vs.\ Funktional — **×[M] SUPERSEDED**

> **Audit-Befund:** Die ursprüngliche Gleichung verglich links eine Funktion von \(z\)
> (\(m_{\Gamma,\rm ren}(z)+\cdots\)) mit rechts Funktionalen/Quadratformen in \(f\)
> (\(Q_\Gamma[f]+\cdots\)). Das ist ein echter Typfehler.

## Satz NEU-112.4 (retypisiert) — Normierungsinterface als lineares Distributionsobjekt

Die korrekt gestellte Frage lautet: Für welche Fourierkonvention und welchen Testfunktionsraum gilt

$$
\boxed{W_\xi^{\rm norm}[\Phi] = E_{0,1}[\Phi] + G[\Phi] - P[\Phi] \quad ?[O]}
$$

wobei \(E_{0,1}\), \(G\), \(P\) die Standard-Weil-Terme (triviale Nullstellen, Gamma-Faktor, Pole) sind und alle drei auf demselben Testobjekt \(\Phi\) mit derselben Fourierkonvention ausgewertet werden. Diese Frage ist—in exakt dieser Form—von **NEU-113** korrekt aufgenommen und formuliert worden.

**Status: ?[O] / SUPERSEDED durch NEU-113**

---

## Strategische Notiz — Die zwei Ebenen der Migration

Gruppe D zeigt den konzeptionellen Fortschritt von P02:

| Alte Kette (NEU-111/112) | Neue Kette (P02/NEU-113ff.) |
|---|---|
| \(m_{\rm arith}\longrightarrow Q_{\rm Weil}\) (fast unmittelbar) | Zwei getrennte Ebenen |
| Ebene vermischt | **Lineare Weil-Distribution** \(W_\xi^{\rm norm}[\Phi]\) |
| Typfehler linear/quadratisch | **Autokorrelationslift** \(\Phi=\phi^**\phi\) |
| | **Hermitesche Weilform** \(B_W(a,b)\) |

$$
\boxed{
m_{\rm arith} \rightsquigarrow W_\xi^{\rm norm}
\quad\text{und getrennt}\quad
a\to g_{a,b}\to h_{a,b}\to B_W(a,b).
}
$$

---

## Statusübersicht (korrigiert)

| Punkt | Aussage | Status |
|-------|---------|--------|
| 112.1 | \(\mu_{\rm arith}=\sum_\gamma m_\gamma\delta_\gamma\) (kein Gamma/Pol/Prim-Anteil) | ✓[M] |
| 112.2 | Autokorrelationslift \(Q_{\rm zeros}[\phi]=\sum_\gamma m_\gamma|\hat\phi(\gamma)|^2\) | ✓[M] |
| 112.3 | Zero-side = arithmetic-side; keine Vierfachsumme | ✓[M] |
| 112.4 | Normierungsinterface \(W_\xi^{\rm norm}[\Phi]=E_{0,1}+G-P\) | ?[O] / → NEU-113 |

---

## Verweise

- **NEU-113 (Bombieri-Normalisierung):** Supersediert 112.2–3; Autokorrelationslift und korrekte Weil-Gleichung
- NEU-111 (Patch D-1/2): \(m_{\rm arith}\), signed-\(\Gamma\)
- **Bombieri:** *Remarks on Weil's quadratic functional in number theory* (2000)
- **Connes:** *Trace formula in noncommutative geometry* (1999)
- Weil: *Sur les formules explicites de la théorie des nombres premiers* (1952)
- NEU-119: \(m_{\Omega,N}\)-Definition (noch offen)
