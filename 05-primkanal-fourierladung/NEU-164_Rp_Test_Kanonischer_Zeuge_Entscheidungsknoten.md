# NEU-164 — $R_{p,j}$-Test: Kanonischer Zeuge und Entscheidungsknoten

**Stand:** 15. Juli 2026 — rev.2  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-163 rev.2  
**Ziel:** Explizite Berechnung von $R_{p,j}(e_{1-p}V_p)$ und Klassifikation des Befunds; epistemisch korrekte Schlussform.

---

## Verbleibende Präzisierungen aus NEU-163

### Präzisierung 1 — Positivität der Kante

In 163.C wird
$$\langle E_{1,p},E_{1,p}\rangle_{W_{\mathrm{res}}} > 0$$
aus OP-4.1 (beiderseitige Nichtausgeartetheit, NEU-24) gefolgert. Dieser Schluss ist **korrekt, sofern** OP-4.1 tatsächlich **positive Definitheit** der $W_{\mathrm{res}}$-Hermiteform auf dem relevanten Unterraum liefert — nicht lediglich Links- und Rechtsnichtausgeartetheit.

Eine nichtausgeartete Hermiteform kann indefinit sein; aus bloßer Nichtausgeartetheit folgt $\langle E_{1,p},E_{1,p}\rangle_{W_{\mathrm{res}}} > 0$ nicht automatisch. Falls OP-4.1 nur Nichtausgeartetheit (nicht positive Definitheit) aussagt, muss 163.C diesen zusätzlichen **Positivitätsimport** explizit nennen und begründen.

> **Status:** $\checkmark[M]$ unter der Voraussetzung, dass OP-4.1 positive Definitheit enthält; andernfalls $?[O]$ mit Nachweispflicht.

### Präzisierung 2 — Cutoff-Abhängigkeit

Da der Raum als $H_{\mathrm{rel},N}$ bezeichnet wird, muss die Kante $1 \to p$ im jeweiligen Cutoff enthalten sein. Der uniforme Befund lautet:
$$\forall p\;\exists N \geq p:\quad E_{1;\,1\to p}^{\mathrm{rel}} \in H_{\mathrm{rel},N}.$$
An einem **festgehaltenen endlichen $N$** gilt die Aussage nur für Primzahlen $p \leq N$.

> **Status:** $\checkmark[M]$ uniform; bei festem $N$ nur für $p \leq N$.

---

## Notwendiger Import: Wirkung der $R_{p,j}$ auf Basisvektoren

Bevor irgendein Ausgang entschieden werden kann, müssen für jeden in NEU-159 auftretenden Operator $R_{p,j}$ folgende Punkte bestimmt werden:

| Prüfung | Zu bestimmen |
|---|---|
| Definitionsbereich | Liegt $e_uV_p$ überhaupt im Definitionsbereich von $R_{p,j}$? |
| Homogenität | Ist $R_{p,j}$ linear und homogen im Vektorargument? |
| Modenwirkung | Explizite Formel für $R_{p,j}(e_uV_p)$ in Abhängigkeit von $u$ |
| Nullmenge | Für welche $u$ verschwindet $R_{p,j}(e_uV_p)$? |
| Gemeinsamer Kern | Schnitt aller Nullmengen über alle $j$ |

**Wichtiger Vorbehalt:** $R_{p,j}$ ist linear im **Vektorargument** $e_uV_p$. Die Abbildung
$$u \longmapsto R_{p,j}(e_uV_p)$$
kann jedoch diagonal, polynomial, kombinatorisch oder völlig anders in $u$ sein. Erst ein Import der konkreten Formeln darf entscheiden, ob Gleichungen in $u$ linear, algebraisch oder anderer Natur sind.

---

## Zentrales Objekt: zulässige Indexmenge $\mathcal{U}_p^{\mathrm{adm}}$

Der entscheidende Gegenstand ist der **gemeinsame Kern aller Regularitätsbedingungen**:

$$\boxed{\mathcal{U}_p^{\mathrm{adm}} := \bigcap_j \left\{ u \neq 0 : R_{p,j}(e_uV_p) = 0 \right\}.}$$

Die freie Einmodenroute wird dann zur **Schnittfrage**:
$$\exists\, s_0, m_0, r_*:\quad u_0 = r_* - p\,s_0 \in \mathcal{U}_p^{\mathrm{adm}},$$
zusammen mit der Nichtnullbedingung der Zielkante. Dies ist zunächst eine **arithmetische Schnittfrage**, kein notwendigerweise lineares Gleichungssystem.

---

## 164.A — Kanonischer Zeuge

**Aufgabe:** Für jeden relevanten Regularitätsoperator $R_{p,j}$ berechne explizit $R_{p,j}(e_{1-p}V_p)$ und klassifiziere:

$$\begin{cases}
0 & \text{definitorisch oder durch Sektorregel},\\
0 & \text{nach konkreter Rechnung},\\
\neq 0 & \text{Obstruktion für den kanonischen Zeugen},\\
\text{unbestimmt} & \text{fehlende Definition oder Hypothese}.
\end{cases}$$

### Statusmatrix (nach Ausführung des Tests auszufüllen)

| Operator $R_{p,j}$ | Definitionsbereich | $R_{p,j}(e_{1-p}V_p)$ | Begründungstyp | Status |
|---|---|---|---|---|
| $j = 1$ | $?[O]$ | — | — | $?[O]$ |
| $j = 2$ | $?[O]$ | — | — | $?[O]$ |
| $\ldots$ | $?[O]$ | — | — | $?[O]$ |

---

## Drei Ausgänge nach Berechnung von $\mathcal{U}_p^{\mathrm{adm}}$

### Ausgang A — Kanonischer Zeuge zulässig

$$1-p \in \mathcal{U}_p^{\mathrm{adm}}.$$

Dann folgt, unter dem bereits isolierten Positivitäts- und Cutoff-Import:
$$T_p^{\mathrm{rel}}(e_{1-p}V_p) = (p-1)\log p\, E_{1;\,1\to p}^{\mathrm{rel}} \neq 0,$$
also unmittelbar:
$$\boxed{Q_p^{\mathrm{rel}} \neq 0.}$$

### Ausgang B — Kanonischer Zeuge scheitert, andere Moden bleiben

$$1-p \notin \mathcal{U}_p^{\mathrm{adm}}, \qquad \mathcal{U}_p^{\mathrm{adm}} \neq \varnothing.$$

Man sucht $u_0 \in \mathcal{U}_p^{\mathrm{adm}}$ und löst die Indexrelation
$$u_0 = r_* - p\,s_0$$
unter den zulässigen Bedingungen an $r_*, s_0, m_0$. Dies ist eine **arithmetische Schnittfrage**, nicht notwendigerweise ein lineares Gleichungssystem.

Epistemische Schlussform:
$$\text{kanonischer Zeuge scheitert} \quad\not\Longrightarrow\quad Q_p^{\mathrm{rel}} = 0.$$

### Ausgang C — Kein geladener Basisvektor zulässig

$$\mathcal{U}_p^{\mathrm{adm}} = \varnothing.$$

**Wichtiger Vorbehalt:** Auch dann folgt **nicht** sofort $Q_p^{\mathrm{rel}} = 0$. Eine Linearkombination
$$w = \sum_u a_u\, e_uV_p$$
könnte in allen Kernen liegen, obwohl kein einzelner Basisvektor $e_uV_p$ darin liegt.

Erst wenn zusätzlich nachgewiesen wird, dass die $R_{p,j}$ den Fouriersektor **diagonal** (koordinatenweise) testen, darf man aus $\mathcal{U}_p^{\mathrm{adm}} = \varnothing$ auf das Fehlen sämtlicher geladener Änderungen schließen. Dieser Nachweis ist ein gesonderter Import.

$$\boxed{\text{Kein Basiszeuge} \quad\not\Longrightarrow\quad \text{kein linear kombinierter Zeuge.}}$$

---

## Zielgröße nach vollständigem Import

Nach Offenlegung der konkreten Wirkung der $R_{p,j}$ ist entweder $Q_p^{\mathrm{rel}} \neq 0$ unmittelbar geschlossen (Ausgänge A oder B), oder die Zeugenfrage wird auf den exakt definierten Kern
$$\ker(\pi_{\mathrm{prim}}) \cap \bigcap_j \ker R_{p,j} \cap \mathcal{E}_p^{\mathrm{ch}}$$
zurückgeführt. Weitere abstrakte Architektur ist bis zu diesem Import nicht nötig.

---

## Statusmatrix NEU-164 rev.2

| Aussage | Status | Quelle |
|---|---|---|
| Präzisierung 1: Positivität via OP-4.1 (positive Definitheit) | $\checkmark[M]$ bedingt | NEU-163.C + OP-4.1 |
| Präzisierung 2: Cutoff-Uniformität $\forall p\,\exists N\geq p$ | $\checkmark[M]$ | NEU-163 rev.2 |
| Wirkungsformel $u\mapsto R_{p,j}(e_uV_p)$ importiert | $?[O]$ | NEU-159 / Import |
| $\mathcal{U}_p^{\mathrm{adm}}$ berechnet | $?[O]$ | abhängig von obigem |
| Ausgang A: $1-p\in\mathcal{U}_p^{\mathrm{adm}}\Rightarrow Q_p^{\mathrm{rel}}\neq 0$ | $\checkmark[M]$ bedingt | 164.A |
| Ausgang B: anderer $u_0\in\mathcal{U}_p^{\mathrm{adm}}$ (arithm. Schnittfrage) | $?[O]$ | 164.B |
| Ausgang C: $\mathcal{U}_p^{\mathrm{adm}}=\varnothing$; Diagonalität der $R_{p,j}$ nötig | $?[O]$ | 164.C |
| Schlussform: kanonischer Zeuge scheitert $\not\Rightarrow Q_p^{\mathrm{rel}}=0$ | $\checkmark[M]$ | 164.B |
| Schlussform: kein Basiszeuge $\not\Rightarrow$ kein komb. Zeuge | $\checkmark[M]$ | 164.C |

---

## Nächster Schritt

$$\boxed{\text{NEU-165 — Import: konkrete Wirkungsformeln }R_{p,j}(e_uV_p),\text{ Berechnung }\mathcal{U}_p^{\mathrm{adm}}.}$$
