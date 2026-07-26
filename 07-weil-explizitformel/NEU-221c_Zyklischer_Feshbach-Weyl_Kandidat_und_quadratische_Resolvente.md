# NEU-221c — Zyklischer Feshbach-Weyl-Kandidat und quadratische Resolvente

**Katalog-ID:** NEU-221c
**Knoten:** [O-221-1c-relative-positive-Feshbach-sector]
**Vorgänger:** NEU-221 (Commit 9b6ba54) — Kandidateninventar, Normalisierungs-Firewall, Feshbach/Weyl als stärkster Ausgangspunkt
**Status:** ✓[K/M]_part (Konstruktionstyp fixiert) / ?[O] (quellseitige Extraktion aus NEU-46 und arithmetischer Momententest, RH-stark)

---

## 0. Typverschiebung gegenüber NEU-221

$$
\boxed{\text{Die Feshbach-/Weyl-Komponente liefert primär eine zyklische Resolventenmatrixstelle, nicht eine Spur.}}
$$

Die Spurformulierung \(\tau_X(T_X^{k+1})=\mu_k\) aus NEU-221 bleibt langfristiges Ziel. Für den ersten echten Kandidaten ist die Moment-GNS-Normalform aus NEU-220w jedoch natürlicher.

---

## 1. Zwei Zieltypen strikt unterschieden

### Semifiniter Spurtyp (langfristig)

$$
\tau_X(T_X^{k+1})=\mu_k.
$$

Muss später Atomizität und ganzzahlige Vielfachheiten reproduzieren — stark, aber für einen Feshbach-Vektor nicht unmittelbar natürlich.

### Zyklischer Weyl-Typ (Konstruktionsziel hier)

Gesucht: \(J_X\ge0\), \(\Omega_X\in\mathcal H_X\) mit

$$
\boxed{M_\Xi(w) = \left\langle \Omega_X,(I-wJ_X)^{-1}\Omega_X \right\rangle,} \qquad \boxed{\mu_k = \langle\Omega_X,J_X^k\Omega_X\rangle.}
$$

Genau solche skalaren Resolventenmatrixstellen liefern Weyl- und Feshbach-Funktionen. Die Spurversion kann später aus einem atomaren Modell gewonnen werden — sie sollte hier nicht vorzeitig erzwungen werden.

---

## 2. Kanonischer quadratischer Feshbach-Kandidat

Gegeben: \(\mathcal H_N^{\mathrm{rel}}\), \(D_N^{\mathrm{rel}}=(D_N^{\mathrm{rel}})^*\), \(\Psi_N\in\mathcal H_N^{\mathrm{rel}}\) (quellseitig vorgegebener Kopplungs-/zyklischer Vektor). Zu prüfen zuerst: \(0\in\rho(D_N^{\mathrm{rel}})\).

Dann ohne zusätzlichen Parameter:

$$
\boxed{J_{X,N} = (D_N^{\mathrm{rel}})^{-2}\ge0,} \qquad \boxed{\Omega_{X,N} = (D_N^{\mathrm{rel}})^{-1}\Psi_N.}
$$

Zugehörige Stieltjesfunktion:

$$
M_{X,N}(w) = \langle\Omega_{X,N},(I-wJ_{X,N})^{-1}\Omega_{X,N}\rangle = \boxed{\left\langle \Psi_N, \bigl((D_N^{\mathrm{rel}})^2-w\bigr)^{-1} \Psi_N \right\rangle.}
$$

Momente:

$$
\boxed{m_{k,N} = \langle\Omega_{X,N},J_{X,N}^k\Omega_{X,N}\rangle = \left\langle \Psi_N, (D_N^{\mathrm{rel}})^{-2k-2}\Psi_N \right\rangle.}
$$

Das ist der erste wirklich typgerechte \(X_\infty\)-Kandidat aus dem Feshbach-Sektor.

### Positivität ist automatisch

Für \(\operatorname{Im}w>0\):

$$
\operatorname{Im}M_{X,N}(w) = (\operatorname{Im}w) \left\| \bigl((D_N^{\mathrm{rel}})^2-w\bigr)^{-1} \Psi_N \right\|^2 >0
$$

sofern \(\Psi_N\neq0\). Damit ist \(M_{X,N}\) **ohne RH** eine Stieltjes-/Herglotzfunktion mit positivem Spektralmaß.

---

## 3. Erweiterte Normalisierungs-Firewall (auf den zyklischen Vektor)

Vor dem Momententest müssen unabhängig feststehen:

$$
\boxed{\mathcal H_N^{\mathrm{rel}}, \quad D_N^{\mathrm{rel}}, \quad \Psi_N, \quad \langle\cdot,\cdot\rangle_N.}
$$

Insbesondere verboten nach Kenntnis der Zielmomente: \(D_N^{\mathrm{rel}}\mapsto cD_N^{\mathrm{rel}}\), \(\Psi_N\mapsto d\Psi_N\), \(\langle\cdot,\cdot\rangle_N \mapsto e\langle\cdot,\cdot\rangle_N\). Denn \(D\mapsto cD\), \(\Psi\mapsto d\Psi\) verändert die Momente durch \(m_k\mapsto |d|^2c^{-2k-2}m_k\); schon zwei freie Skalierungen würden \(\mu_0,\mu_1\) wieder fittbar machen. Der Vektor \(\Psi_N\) muss aus der ursprünglichen Feshbach-Kopplung stammen und darf nicht nachträglich normiert werden.

---

## 4. Erster harter Kandidatentest: Nullmodus

Der erste Test ist nicht \(\mu_0\), sondern

$$
\boxed{0\in\rho(D_N^{\mathrm{rel}})?}
$$

Falls \(0\in\sigma(D_N^{\mathrm{rel}})\) und \(P_{\ker D_N^{\mathrm{rel}}}\Psi_N\neq0\), dann divergiert bereits \(m_{0,N} = \langle \Psi_N,(D_N^{\mathrm{rel}})^{-2}\Psi_N \rangle\) — der Kandidat wäre unmittelbar ausgeschlossen.

Falls ein Nullraum existiert, aber \(P_{\ker D_N^{\mathrm{rel}}}\Psi_N=0\), kann auf dem zyklischen Unterraum ein reduzierter inverser Operator verwendet werden — dies muss aber aus der Kopplungsgeometrie folgen; ein ad hoc Quotient ist unzulässig.

Da \(\Xi(0)\neq0\), muss ein gültiger Grenzkandidat letztlich einen spektralen Abstand von \(0\) im sichtbaren zyklischen Sektor besitzen.

---

## 5. Warum die Quadratisierung richtig ist

Die bisherigen lokalen Weyl-Funktionen haben die Form \(M_N^{\mathrm{lin}}(z) = \langle\Psi_N,(D_N^{\mathrm{rel}}-z)^{-1}\Psi_N\rangle\). Das Ziel \(M_\Xi\) lebt jedoch in der quadrierten Variablen \(w=\gamma^2\). Daher ist nicht \(M_N^{\mathrm{lin}}\) selbst zu vergleichen, sondern \(M_{X,N}(w) = \langle\Psi_N,((D_N^{\mathrm{rel}})^2-w)^{-1}\Psi_N\rangle\).

Die Quadratisierung:

- entfernt das Vorzeichen des symmetrischen Spektrums
- erzeugt einen positiven Operator
- führt direkt zur gewöhnlichen Stieltjesklasse
- vermeidet den \(\det_2\)-Formalismus
- liefert exakt die geraden inversen Momente

---

## 6. Verbot der orthogonalen direkten Summe der Primkanäle

Der Kandidat darf nicht bloß \(D_N^{\mathrm{rel}} = \bigoplus_{p\le N}D_p^{\mathrm{rel}}\) mit \(\Psi_N=\bigoplus_{p\le N}\Psi_p\) sein, wenn dadurch lediglich

$$
M_{X,N}(w) = \sum_{p\le N} \langle\Psi_p,((D_p^{\mathrm{rel}})^2-w)^{-1}\Psi_p\rangle
$$

entsteht. Eine solche Summe ist zwar positiv, enthält aber nur unabhängig addierte lokale Spektralmaße. Die vollständige Weil-Struktur entsteht durch nichttriviale Kopplung von Prim \(+\) \(\Gamma\) \(+\) Polrenormierung. Der relevante \(D_N^{\mathrm{rel}}\) muss ein gekoppelter Schur-/Feshbach-Operator sein; die Primkanäle dürfen erst nach der Kopplung als lokale Beiträge erscheinen.

**Autoritative Reihenfolge:**

$$
\boxed{\text{Euler-/Primkanäle} \longrightarrow \text{globale Feshbach-Kopplung} \longrightarrow \text{archimedischer Kanal} \longrightarrow D_N^{\mathrm{rel}} \longrightarrow (D_N^{\mathrm{rel}})^2.}
$$

**Nicht:** \(\bigoplus_p(D_p^{\mathrm{rel}})^2 \longrightarrow\) nachträgliche Addition von \(\Gamma\).

---

## 7. Berechnungsreihenfolge

$$
\boxed{m_{0,N} = \langle\Psi_N,D_N^{-2}\Psi_N\rangle,} \qquad \boxed{m_{1,N} = \langle\Psi_N,D_N^{-4}\Psi_N\rangle,} \qquad \boxed{m_{2,N} = \langle\Psi_N,D_N^{-6}\Psi_N\rangle.}
$$

Danach gilt automatisch für jeden positiven Kandidaten (Cauchy-Schwarz):

$$
m_{0,N}m_{2,N}-m_{1,N}^2 = \|\Omega_N\|^2 \|J_N\Omega_N\|^2 - |\langle\Omega_N,J_N\Omega_N\rangle|^2 \ge0.
$$

**Wichtige Präzisierung:** Der Hankeltest unterscheidet deshalb nicht zwischen positiven Feshbach-Kandidaten — Positivität ist durch die Konstruktion bereits eingebaut. Der echte Test ist ausschließlich die arithmetische Identität \(m_{k,N}\longrightarrow\mu_k\).

---

## 8. Erster echter Erfolgskatalog (FX-1 bis FX-7)

Ein Kandidat \(D_N^{\mathrm{rel}},\Psi_N\) gilt erst dann als Teil von Objekt \(X\), wenn bewiesen ist:

- **FX-1:** \(D_N^{\mathrm{rel}}=(D_N^{\mathrm{rel}})^*\)
- **FX-2:** \(0\in\rho(D_N^{\mathrm{rel}})\) im zyklischen Sektor
- **FX-3:** \(\Psi_N\) ist quellseitig kanonisch normiert
- **FX-4:** \(M_{X,N}(w) = \langle\Psi_N,(D_N^2-w)^{-1}\Psi_N\rangle\)
- **FX-5:** \(M_{X,N}\) besitzt eine unabhängige Euler-/Gamma-Berechnung
- **FX-6:** \(m_{k,N}\to\mu_k\) mindestens für \(k=0,1,2\)
- **FX-7:** der Grenzübergang verwendet keine Nullstellenlagen

**Nur FX-5 und FX-6 wären wirklicher Fortschritt gegen RH.** FX-1 bis FX-4 sind die notwendige Konstruktion.

---

## Revidierter Status

| Aussage | Status |
|---|---|
| Feshbach/Weyl als natürliche Quellregion | ✓[K/M]_part |
| Unmittelbare Spurform für lokalen Weyl-Vektor | verfrüht |
| Zyklische Stieltjes-Matrixstelle | ✓[K] |
| \(J_{X,N}=D_N^{-2}\), \(\Omega_N=D_N^{-1}\Psi_N\) | ✓[K] bei nachgewiesener Invertierbarkeit |
| \(M_{X,N}\) automatisch Stieltjes | ✓[M] |
| Kanonische Normierung von \(\Psi_N\) | ?[O] |
| Archimedisch gekoppelte globale Feshbach-Konstruktion | ?[O] |
| \(m_{k,N}\to\mu_k\) | ?[O], RH-stark |

```
[O-221-1c-relative-positive-Feshbach-sector]
  -> ✓[K/M]_part  (Konstruktionstyp und Positivität fixiert)
  -> ?[O]          (Extraktion von H_N^rel, D_N^rel, Psi_N aus NEU-46; Momententest m_k,N -> mu_k)
```

---

## Erster atomarer Auftrag

$$
\boxed{\text{Extrahiere aus NEU-46 exakt } (\mathcal H_N^{\mathrm{rel}},D_N^{\mathrm{rel}},\Psi_N) \text{ samt Skalarprodukt und Kopplungsnormalisierung.}}
$$

Erst danach darf \(J_{X,N}=(D_N^{\mathrm{rel}})^{-2}\) definiert und gegen die \(\Xi\)-Momente getestet werden.

Das ist wieder echte Objekt-\(X\)-Arbeit: nicht mehr eine weitere RH-Äquivalenz, sondern der Versuch, einen quellseitig positiven Stieltjesoperator aus der vorhandenen adelischen Feshbach-Geometrie zu bauen.

---

## Abhängigkeiten

| Referenz | Inhalt |
|---|---|
| NEU-221 (9b6ba54) | Kandidateninventar, Normalisierungs-Firewall (Basisversion), Zielwerte \(\mu_k\) |
| NEU-220w (f1bce0f) | Moment-GNS-Weyl-Modell, Zieltyp \(M_\Xi(w)=\langle\Omega,(I-wJ)^{-1}\Omega\rangle\) |
| NEU-46 | Relative Weyl-Funktionen \(M_p(z)\), Jacobi-/Feshbach-Sektor, Determinantenzerfall Euler/Jacobi/Streuung |
| NEU-42 | Relativer modularer Clock als arithmetischer Baustein |

---

*Erstellt im Rahmen des Akademisch-Fragenkatalogs, Waschtl904/rh-fragenkatalog.*
