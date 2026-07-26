# NEU-49 — X.3.19: Birman-Schwinger-Indexsatz und Nichtüberzählung der Nullstellen

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-48  
**Ziel:**

\[
\operatorname{div} D_{\mathrm{scatt}} = \sum_\rho m_\rho[\rho],
\tag{49.0}
\]

in der schwachen Form:

\[
\partial_s\log D_{\mathrm{scatt},N}(s) \longrightarrow \sum_\rho m_\rho\left(\frac{1}{s-\rho}+\frac{1}{\rho}\right)
\tag{49.1}
\]

im konturweise-meromorphen Sinn.

---

## 0. Warnung: Nichtüberzählungsgefahr

Wenn \(D_{\mathrm{scatt},N} = \prod_{p\le N}\det(1-K_p(s))\) als echtes Primprodukt gelesen wird, dann gilt:

\[
\frac{1}{2\pi i}\int_{\gamma_\rho} \partial_s\log D_{\mathrm{scatt},N}\,ds
= \sum_{p\le N} \operatorname{Ind}_{\gamma_\rho}(1-K_p).
\tag{49.2}
\]

Da \(\operatorname{Ind}_{\gamma_\rho}(1-K_p) \in \mathbb{N}_0\), kann die Summe nur dann gegen \(m_\rho\) konvergieren, wenn:

| Mechanismus | Bedeutung |
|---|---|
| **Lokale Endlichkeit** | Nur endlich viele \(p\) tragen bei; Rest hat \(\operatorname{Ind}=0\) |
| **Zerlegung \(E_\rho = \bigoplus_p E_{\rho,p}\)** | Nullstellenmultiplizität zerlegt sich orthogonal über Primrichtungen |
| **Regularisierter/signierter Index** | Gegenbeiträge möglich |
| **Kollektive Determinante** | Kein echtes Primprodukt; \(\mathcal{K}_N = \bigoplus_p K_p\) als Ganzes |

Die naive Variante \(\operatorname{Ind}_{s=\rho}(1-K_p)=1\) für alle \(p\) wäre fatal: divergente Summe.

Status: Obstruktion gesichert. \(\times\) [M]

---

## 1. Satz 49.1 — Fredholm-Determinanten-Index

Sei \(K_p(s)\) auf \(\Omega\) trace-class-holomorph, \(\gamma \subset \Omega\) Kontur ohne Randnullstellen. Dann:

\[
\frac{1}{2\pi i}\int_\gamma \partial_s\log\det(1-K_p(s))\,ds
= \operatorname{ord}_\gamma\det(1-K_p)
= \sum_{s_0\in\mathrm{int}(\gamma)} \operatorname{Ind}_{s=s_0}(1-K_p).
\tag{49.3}
\]

Für einfache Eigenwertkreuzungen: \(\operatorname{Ind}_{s=\rho}(1-K_p) = \dim\ker(1-K_p(\rho))\).

Status: \(\checkmark/\warning\) [M] (je nach gesicherter Spurklasse-Eigenschaft).

---

## 2. Satz 49.2 — Additivität der Streudet-Schicht

Für das Primprodukt \(D_{\mathrm{scatt},N}=\prod_{p\le N}\det(1-K_p(s))\) und jede zulässige Kontur \(\gamma\):

\[
\frac{1}{2\pi i}\int_\gamma \partial_s\log D_{\mathrm{scatt},N}\,ds = \sum_{p\le N}\operatorname{Ind}_\gamma(1-K_p).
\tag{49.4}
\]

Formal korrekt, sobald Produktformel und Fredholm-Determinanten sauber definiert sind.

Status: \(\checkmark\) [M] (formal).

---

## 3. Satz 49.3 — Nichtüberzählung (Kern-Engpass)

Für jede nichttriviale Nullstelle \(\rho\):

\[
\boxed{
\sum_p \operatorname{Ind}_{s=\rho}(1-K_p) = m_\rho.
}
\tag{49.5}
\]

Dies verbietet insbesondere:

\[
\operatorname{Ind}_{s=\rho}(1-K_p) = 1 \quad\text{für alle oder unendlich viele }p.
\tag{49.6}
\]

Status: \(\:?\:\) [O] — Haupt-Engpass.

---

## 4. Architekturentscheidung: Primprodukt oder kollektive Determinante

### Variante 1 — Echtes Primprodukt

\[
D_{\mathrm{scatt},N}(s) = \prod_{p\le N}\det(1-K_p(s)).
\tag{49.7}
\]

Erfordert zwingend lokale Endlichkeit oder Zerlegung \(E_\rho = \bigoplus_p E_{\rho,p}\).

Status: \(\warning\) [M] — strukturell möglich, Nichtüberzählung nicht automatisch.

### Variante 2 — Kollektive Birman-Schwinger-Determinante (bevorzugt)

\[
\boxed{
D_{\mathrm{scatt},N}(s) = \det(1-\mathcal{K}_N(s)),
\quad
\mathcal{K}_N := \bigoplus_{p\le N} K_p.
}
\tag{49.8}
\]

Dann ist der Konturindex:

\[
\frac{1}{2\pi i}\int_{\gamma_\rho}\partial_s\log\det(1-\mathcal{K}_N(s))\,ds = \operatorname{Ind}_{\gamma_\rho}(1-\mathcal{K}_N),
\tag{49.9}
\]

ein einziger Index — kein Summe unabhängiger Primindizes.

**Vorteil:** Keine Nichtüberzählung per Konstruktion, wenn \(\ker(1-\mathcal{K}_\infty(\rho))\) die Nullstellenmultiplizität trägt.

Status: \(\checkmark\) [M] als strukturelle Präferenz.

---

## 5. Kern-Kernsatz von NEU-49

\[
\boxed{
D_{\mathrm{scatt}} \text{ ist nicht eine Sammlung lokaler Primdeterminanten,}
}
\tag{49.D1}
\]

\[
\boxed{
\text{sondern eine kollektive Birman-Schwinger-Determinante }\det(1-\mathcal{K}_N).}
\tag{49.D2}
\]

Der eigentliche Beweisengpass:

\[
\boxed{
\dim\ker(1-\mathcal{K}_\infty(\rho)) = m_\rho.
}
\tag{49.D3}
\]

Das ist stabiler als (49.5), weil es die Nullstelle nicht primweise mehrfach zählt.

---

## 6. Bewertung der drei Zugänge aus NEU-48

| Zugang | Kern | Bewertung |
|---|---|---|
| **A** Spurklasse | \(-\sum_p\mathrm{Tr}((1-K_p)^{-1}K_p')\to\sum_\rho m_\rho(\frac{1}{s-\rho}+\frac{1}{\rho})\) | Stark, Residuen automatisch. Erfordert Spurklasse-Konvergenz. \(\:?\:\) [O] |
| **B** Jacobi-Spektrum | \(\sum_p\dim\ker(1-K_p(\rho))\to m_\rho\) via \(E_\rho=\bigoplus_p E_{\rho,p}\) | Strukturell schön, aber Nichtüberzählung erfordert kanonische Zerlegung. \(\:?\:\) [O] |
| **C** Hadamard-Regularisierung | Globale Konvergenz verbessern, exponentiellen Anteil korrigieren | Löst Divisorfrage allein nicht. \(\times\) [M] als alleiniger Zugang. |

**Empfehlung:** Zugang A + kollektive Determinante (49.8) kombinieren.

---

## 7. Zusatzbedingung: Triviale Nullstellen bleiben neutral

Kompatibel mit NEU-48, Satz 48.2:

\[
\lim_{N\to\infty}\frac{1}{2\pi i}\int_{\gamma_{-2k}}\partial_s\log D_{\mathrm{scatt},N}(s)\,ds = 0.
\tag{49.10}
\]

Das bedeutet: \(\ker(1-\mathcal{K}_N(-2k)) = 0\) für alle \(k\ge1\). Die Birman-Schwinger-Eigenwertkurven dürfen bei \(s=-2k\) nicht durch \(1\) gehen.

Status: \(\warning\) [M].

---

## 8. Statusmatrix

| Aussage | Status |
|---|---|
| Fredholm-Determinanten-Index (Satz 49.1) | \(\checkmark/\warning\) [M] |
| Additivität Streudet (Satz 49.2) | \(\checkmark\) [M] formal |
| Nichtüberzählung (Satz 49.3) | \(\:?\:\) [O] Kern-Engpass |
| Obstruktion: Ind=1 für \(\infty\) viele \(p\) | \(\times\) [M] |
| Kollektive Determinante als bevorzugte Architektur | \(\checkmark\) [M] |
| \(\dim\ker(1-\mathcal{K}_\infty(\rho))=m_\rho\) | \(\:?\:\) [O] Haupt-Engpass |
| Triviale-Nullstellen-Neutralität bei \(s=-2k\) | \(\warning\) [M] |
| Hadamard-Regularisierung allein löst Divisorfrage | \(\times\) [M] |

---

## 9. Nächster Schritt

\[
\boxed{
\text{NEU-50: Konstruktion von }\mathcal{K}_\infty\text{ und Nachweis }\dim\ker(1-\mathcal{K}_\infty(\rho))=m_\rho.
}
\]

Drei Teilfragen:

1. Wie ist \(\mathcal{K}_\infty = \lim_{N\to\infty}\bigoplus_{p\le N}K_p\) im Operatorsinn definiert (SOT, Normkonvergenz, Tr-Norm)?
2. Warum kreuzen die Birman-Schwinger-Eigenwertkurven \(\mu_j(s)\) von \(\mathcal{K}_N\) bei \(s=\rho\) genau mit algebraischer Multiplizität \(m_\rho\) durch \(1\)?
3. Warum nicht bei \(s=-2k\)?
