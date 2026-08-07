# NEU-250i — Primzahlpotenzsektor, Grad-normalisierte BC-Energie und vollständiger von-Mangoldt-Faktor

**Katalog-ID:** NEU-250i 
Vorgänger: NEU-250g (Modulare Halbgewichtung), NEU-250h (Quellenabbildung)
**Status:** ✓[M] für I1–I5, Firewall für allg. $n$ gesetzt

---

## 0. Ausgangslage und Obstruktion für $m > 1$

NEU-250g hat gezeigt: Auf dem balancierten $p$-Kanal ($n = p$, $m = 1$) gilt
$$
h_p^{\mathrm{bal}}\bigl(\mathsf H_{\rm BC}^{1/2}E_R, \mathsf H_{\rm BC}^{1/2}E_{R'}\bigr) = \frac{\log p}{\sqrt p}\,\delta_{RR'}.
$$

Der Versuch, dies naiv auf allgemeine $n = p^m$ zu verallgemeinern, erzeugt sofort eine Obstruktion: Da $\mathsf H_{\rm BC}j_{R,p^m} = \log(p^m)\,j_{R,p^m} = m\log p\,j_{R,p^m}$, liefert die naive Halbgewichtung
$$
h_{p^m}^{\mathrm{bal}}\bigl(\mathsf H_{\rm BC}^{1/2}E_R, \mathsf H_{\rm BC}^{1/2}E_{R'}\bigr) = \frac{m\log p}{p^{m/2}}\,\delta_{RR'},
$$
was für $m > 1$ einen **überschußigen Faktor $m$** gegenüber dem korrekten von-Mangoldt-Koeffizienten $\Lambda(p^m)/\sqrt{p^m} = \log p/p^{m/2}$ trägt. Für $m = 1$ war dieser Unterschied unsichtbar.

---

## I1 — Allgemeine Halbmodularisierung

Aus NEU-250g, Schritt G1 (gültig für alle $n \geq 1$):
$$
\boxed{h_n^{\mathrm{bal}} = n^{-1/2}\,I.} \qquad (1)
$$

Der KMS-Halbgewichtungsfaktor hängt nur von $n$ ab und liefert exakt $p^{-m/2}$ für $n = p^m$. Kein offener Punkt.

Status: ✓[M], direkt aus NEU-250g.

---

## I2 — No-Go der naiven BC-Energie auf $p^m$ (Obstruktion ✓[M]$_{\mathrm{neg}}$)

Für den allgemeinen BC-Zeitentwicklungs-Generator gilt (KONVENTIONEN.md Abschnitt 3):
$$
[\mathsf H_{\rm BC}, V_n] = +\log(n)\,V_n, \qquad \mathsf H_{\rm BC}j_{R,n} = \log(n)\,j_{R,n}. \qquad (2)
$$

Für $n = p^m$:
$$
\mathsf H_{\rm BC}\,j_{R,p^m} = \log(p^m)\,j_{R,p^m} = m\log p\,j_{R,p^m}. \qquad (3)
$$

Naive Anwendung von I1 und G2 aus NEU-250g ergibt:
$$
h_{p^m}^{\mathrm{bal}}\bigl(\mathsf H_{\rm BC}^{1/2}E_R, \mathsf H_{\rm BC}^{1/2}E_{R'}\bigr)
= \frac{m\log p}{p^{m/2}}\,\delta_{RR'}. \qquad (4)
$$

Da $\Lambda(p^m)/\sqrt{p^m} = \log p/p^{m/2}$, ist (4) für $m > 1$ um den Faktor $m$ zu groß.

$$
\boxed{\text{Naives G2 auf } p^m \text{ liefert Faktor }m\text{ zuviel. Obstruktion gesetzt.}} \qquad (\checkmark[M]_{\mathrm{neg}})
$$

---

## I3 — Vorhandener Monoiddgrad $\mathsf D_\Omega$ aus NEU-025

NEU-025 (Spaltbarkeit, `01-primkanten-werkzeuge/NEU-025_op4_1top_spaltbarkeit.md`) definiert die intrinsische Gradfunktion des Monoids
$$
\nu(n) = \Omega(n) \qquad (\text{Anzahl der Primfaktoren mit Vielfachheit}), \qquad (5)
$$
also $\Omega(p) = 1$, $\Omega(p^m) = m$, $\Omega(mn) = \Omega(m)+\Omega(n)$. Daraus stammt die Symbolfiltration
$$
F^qA_{\rm BC}^{\rm an} = \Bigl\{\sum_{\Omega(n) \geq q}f_{r,n}\,e_r V_n\Bigr\}. \qquad (6)
$$

Der zugehörige Multiplikationsoperator auf dem BC-Faserraum ist
$$
\mathsf D_\Omega\,j_{R,n} := \Omega(n)\,j_{R,n}, \qquad \mathsf D_\Omega\,j_{R,p^m} = m\,j_{R,p^m}. \qquad (7)
$$

$\mathsf D_\Omega$ ist eine **unabhängige arithmetische BC-Größe**: sie stammt aus der Monoidstruktur, nicht aus dem KMS-Gewicht oder dem Weil-Match.

Status: ✓[M], zitiert aus NEU-025 ohne neue Konstruktion.

---

## I4 — Primitive Energie auf dem Primzahlpotenzsektor

Die **Grad-normalisierte BC-Energie** ist
$$
\boxed{\mathsf H_{\rm pr} := \mathsf D_\Omega^{-1}\,\mathsf H_{\rm BC},} \qquad (8)
$$
wobei $\mathsf D_\Omega^{-1}$ auf $\{j_{R,n} : \Omega(n) \geq 1\}$ wohldefiniert ist (Einschränkung auf den Primzahlpotenzsektor, $n \neq 1$). Auf $j_{R,1}$ ($\Omega(1) = 0$) ist der Ausdruck singulär; er wird dort nicht benötigt, da $\Lambda(1) = 0$.

Evaluation auf $n = p^m$:
$$
\mathsf H_{\rm pr}\,j_{R,p^m}
= \frac{\log(p^m)}{\Omega(p^m)}\,j_{R,p^m}
= \frac{m\log p}{m}\,j_{R,p^m}
= \log p \cdot j_{R,p^m}. \qquad (9)
$$

$$
\boxed{\mathsf H_{\rm pr}\,j_{R,p^m} = \log p\,\cdot\,j_{R,p^m}.} \qquad (10)
$$

Beide Faktoren in (8) sind unabhängig von der Zielgröße $\Lambda(n)/\sqrt{n}$ und bereits im Repository verankert:
$$
p^{-m/2} \leftarrow \text{KMS-Halbgewichtung (NEU-250g, I1)}, \qquad
\log p = \frac{\log(p^m)}{\Omega(p^m)} \leftarrow \text{BC-Energie / Monoidgrad (NEU-025, I3).}
$$

Status: ✓[M], keine rückwärts konstruierten Faktoren.

---

## I5 — Vollständiger lokaler von-Mangoldt-Koeffizient

**Satz (vollständiger primitiver Koeffizient):** Für alle $n = p^m$ ($p$ prim, $m \geq 1$) gilt
$$
\boxed{h_{p^m}^{\mathrm{bal}}\Bigl(\mathsf H_{\rm pr}^{1/2}E_R,\,\mathsf H_{\rm pr}^{1/2}E_{R'}\Bigr)
= \frac{\log p}{p^{m/2}}\,\delta_{RR'}
= \frac{\Lambda(p^m)}{\sqrt{p^m}}\,\delta_{RR'}.} \qquad (11)
$$

*Beweis (für festes $n = p^m$):*

Aus (1): $h_{p^m}^{\mathrm{bal}} = p^{-m/2}\,I$.

Aus (10): $\mathsf H_{\rm pr}^{1/2}\,j_{R,p^m} = (\log p)^{1/2}\,j_{R,p^m}$.

Daher:
$$
h_{p^m}^{\mathrm{bal}}\bigl(\mathsf H_{\rm pr}^{1/2}E_R,\,\mathsf H_{\rm pr}^{1/2}E_{R'}\bigr)
= \bigl\langle p^{-m/2}\,\mathsf H_{\rm pr}^{1/2}E_R,\,\mathsf H_{\rm pr}^{1/2}E_{R'}\bigr\rangle
= p^{-m/2}\,(\log p)\,\delta_{RR'}
= \frac{\log p}{p^{m/2}}\,\delta_{RR'}. \quad\square
$$

Da $\Lambda(p^m) = \log p$ für alle $m \geq 1$ (Definition der von-Mangoldt-Funktion), ist dies exakt der Weilkoeffizient.

---

## Anschluss an NEU-250h

NEU-250h (H2) liefert ohne neue Quadratwurzel:
$$
g_a(m\log p) = \operatorname{Re}\langle a, U_{m\log p}\,a\rangle. \qquad (12)
$$

Mit (11) und (12) hat man damit erstmals alle Primzahlpotenzterme lokal in der korrekten Form:
$$
\boxed{\frac{\log p}{p^{m/2}}\,\operatorname{Re}\langle a, U_{m\log p}\,a\rangle
= \frac{\Lambda(p^m)}{\sqrt{p^m}}\,g_a(m\log p).} \qquad (13)
$$

Das reproduziert exakt den primitiven Summanden der Masterform (NEU-220l, PD5a2d) für beliebiges $m \geq 1$ und beliebige Primzahl $p$.

---

## Firewall: $\mathsf H_{\rm pr} \neq \Lambda$ auf allgemeinem Monoid

$$
\boxed{\mathsf H_{\rm pr}\,j_{R,n} = \frac{\log n}{\Omega(n)}\,j_{R,n} \neq \Lambda(n)\,j_{R,n}
\text{ für allgemeines } n.} \qquad (\text{Firewall})
$$

Gegenbeispiel: $n = 6 = 2\cdot3$, $\Omega(6) = 2$:
$$
\frac{\log 6}{\Omega(6)} = \frac{\log 6}{2} \neq 0 = \Lambda(6).
$$

Auf zusammengesetzten Zahlen mit mehreren verschiedenen Primfaktoren versagt $\mathsf H_{\rm pr}$ als $\Lambda$-Operator vollständig. Dies ist kein Defekt: $\Lambda(n) = 0$ für solche $n$, und diese Terme tragen gar nicht zur Weil-Masterform (NEU-220l, (6)) bei. Der Satz I5 ist deshalb auf dem vollen Träger von $\Lambda$ korrekt — genau auf $\mathcal P = \{p^m : p\text{ prim}, m \geq 1\}$.

---

## Offene Frage: Primfaserkopplungen bei $m > 1$ vs. $m = 1$

Die Faserarchitektur aus KONVENTIONEN.md / NEU-225 behandelt für $M = pm$ den $p^m$-Sektor mit Indexverschiebungen $s \mapsto s+m$; nur im Primsektor $M = p$ entfällt der Fall $d = 1$ (da $\log 1 = 0$) automatisch, und die Einzelkettenrechnung ist dort vollständig. Für $M = p^m$ mit $m > 1$ treten dieselben Fasern wie bei $p^1 \cdot p^{m-1}$ auf; die Frage, ob der $p^m$-Kanal einen eigenständigen Knoten NEU-250j braucht oder ob er sich direkt aus dem $p$-Kanal durch $m$-fache Iteration ergibt, bleibt offen.

---

## Knotentabelle

| Schritt | Inhalt | Status |
|---------|--------|--------|
| I1 | $h_n^{\mathrm{bal}} = n^{-1/2}I$ (allgemein) | ✓[M] |
| I2 | Naives G2 auf $p^m$: Faktor $m$ zuviel | ✓[M]$_{\mathrm{neg}}$ |
| I3 | $\mathsf D_\Omega\,j_{R,n} = \Omega(n)\,j_{R,n}$ aus NEU-025 | ✓[M] |
| I4 | $\mathsf H_{\rm pr} = \mathsf D_\Omega^{-1}\mathsf H_{\rm BC}$, Eigenvektor $\log p$ | ✓[M] |
| I5 | $h_{p^m}^{\mathrm{bal}}(\mathsf H_{\rm pr}^{1/2}E_R,\mathsf H_{\rm pr}^{1/2}E_{R'}) = \Lambda(p^m)/\sqrt{p^m}\,\delta_{RR'}$ | ✓[M] |
| Firewall | $\mathsf H_{\rm pr} \neq \Lambda$ auf allg. $n$; explizites Gegenbeispiel $n=6$ | ✓[M]$_{\mathrm{neg}}$ |

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-250g (33df3ee) | $h_n^{\mathrm{bal}} = n^{-1/2}I$, G1/G2 für $m=1$ |
| NEU-250h (0abda0b) | $g_a(m\log p) = \operatorname{Re}\langle a,U_{m\log p}a\rangle$, Realteil zwingend |
| NEU-025 (c0d87d7) | $\nu(n)=\Omega(n)$, Symbolfiltration $F^qA_{\rm BC}^{\rm an}$ |
| NEU-220l (1dc07b3) | Masterform $\mathfrak W(a)$, $\Lambda(n)/\sqrt n$-Koeffizient für alle $n\geq 2$ |
| KONVENTIONEN.md | $[\mathsf H_{\rm BC},V_n]=+\log(n)V_n$; Primfaserarchitektur für $M=pm$ |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/objekt-x-programm.*
