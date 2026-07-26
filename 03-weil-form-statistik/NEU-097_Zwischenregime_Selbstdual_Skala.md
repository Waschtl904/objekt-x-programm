# NEU-97 — Zwischenregime und Selbstdual-Skala

**Stand:** 1. Juli 2026  
**Vorgänger:** NEU-96 (Skalentriage; kanonischer Bereich \(1 \ll T \ll M_N\); Linearisierungspflicht)  
**Nächste Nummer:** NEU-98

---

## Ausgangspunkt

NEU-96 identifiziert das Zwischenregime \(1 \ll T(N) \ll M_N\) als einzigen nichttrivialen Kandidatenbereich. NEU-97 strukturiert dieses Regime durch eine Potenzleiter und markiert zwei ausgezeichnete Punkte: eine analytisch kontrollierbare Einstiegsskala und eine strukturell kanonische Selbstdual-Skala.

---

## Definition NEU-97.1 — Skalenleiter und Paarbreite

Setze

$$
T(N) = M_N^\theta, \qquad 0 < \theta < 1,
$$

und definiere die **Mangoldt-Paarbreite**

$$
H_N := \frac{M_N}{T(N)} = M_N^{1-\theta}.
$$

Der Fensterfaktor \(\widehat{\eta}(T \log(n/m))\) lokalisiert auf Paare mit

$$
|m - n| \lesssim H_N.
$$

Damit ist \(T(N)\) äquivalent zur Wahl einer Paarbreite \(H_N\). Die Skalenleiter läuft von:

$$
\underbrace{\theta \to 0}_{H_N = M_N \text{ (global)}} \quad\longrightarrow\quad \underbrace{\theta = \tfrac12}_{H_N = \sqrt{M_N} \text{ (selbstdual)}} \quad\longrightarrow\quad \underbrace{\theta \to 1}_{H_N = 1 \text{ (diagonal)}}.
$$

Beide Extreme sind No-Go (NEU-96).

**Status: \(\checkmark[M]\)**

---

## Definition NEU-97.2 — Selbstdual-Skala

Der geometrische Mittelpunkt der Leiter ist

$$
\theta = \frac12 \quad\Longrightarrow\quad T_c(N) = \sqrt{M_N}, \qquad H_N = \sqrt{M_N}.
$$

Diese Skala ist **selbstdual**: Frequenzbreite und Primseitenfenster sind gleich groß:

$$
T_c \cdot H_N = M_N, \qquad T_c = H_N = \sqrt{M_N}.
$$

Eigenschaften:
- Vermeidet Diagonal-Kollaps (\(T_c \ll M_N\)) und Rang-eins-Kollaps (\(T_c \gg 1\))
- Echte Kreuzterme \(\Lambda(m)\Lambda(n)\) mit \(|m-n| \lesssim \sqrt{M_N}\) bleiben erhalten
- Fenster lokal auf der Log-Achse: \(|\log(n/m)| \lesssim M_N^{-1/2}\)

$$
\boxed{T_c = \sqrt{M_N} \text{ ist strukturell kanonisch, aber analytisch schwer.}}
$$

**Analytische Last:** Kontrolle von Paarstatistiken \(\sum_{|m-n| \lesssim \sqrt{M_N}} \Lambda(m)\Lambda(n)\) ist tief (Hardy\u2013Littlewood/Goldston\u2013Y\u0131ld\u0131r\u0131m-Niveau).

**Status: \(\warning[M]\) / \(?[O]\)**

---

## Definition NEU-97.3 — Kontrollskala

Für analytische Erstkontrolle wähle die logarithmische Einstiegsskala:

$$
T_0(N) = \log^2 M_N, \qquad H_N = \frac{M_N}{\log^2 M_N}.
$$

Eigenschaften:
- \(H_N \to \infty\): echte Kreuzterme
- \(H_N / M_N = 1/\log^2 M_N \to 0\): kein globaler Rang-eins-Kollaps
- Breit genug für PNT-/Selberg-/Goldston\u2013Y\u0131ld\u0131r\u0131m-Mittelwertmethoden

$$
\boxed{T_0 = \log^2 M_N \text{ ist die kontrollierbare Einstiegsskala.}}
$$

**Risiko:** Zu grobe Mittelung kann Weil-kompatible Feinstruktur verwischen. \(T_0\) eignet sich zum Nachweis von Nicht-Kollaps, nicht zum Nachweis von Weil-Kompatibilität.

**Status: \(\checkmark[M]\) / \(\warning[M]\)**

---

## Tabelle: Drei ausgezeichnete Skalen

| Skala | \(T(N)\) | \(H_N\) | Kreuzterme | Analytische Kontrolle | Weil-Tauglichkeit |
|---|---|---|---|---|---|
| Kontrollskala | \(\log^2 M_N\) | \(M_N/\log^2 M_N\) | \(\checkmark\) | \(\checkmark\) (PNT-Niveau) | \(\warning\) |
| Selbstdual-Skala | \(\sqrt{M_N}\) | \(\sqrt{M_N}\) | \(\checkmark\) | \(?\) (Hardy\u2013Littlewood) | \(?\) |
| Diagonal | \(\gg M_N\) | \(\leq 1\) | \(\times\) | \(\checkmark\) (trivial) | \(\times\) |

---

## Epistemische Trennung

$$
\boxed{\text{Strukturell kanonisch} \neq \text{analytisch bewiesen kontrollierbar.}}
$$

- \(T_c = \sqrt{M_N}\) ist **strukturell** der richtige Testpunkt (Selbstdualität, keine Kollapse, maximale Kreuztermdichte).
- \(T_0 = \log^2 M_N\) ist **analytisch** der nächste erreichbare Punkt.
- NEU-97 setzt \(T_c\) als Zieltest, nicht als bewiesene Skala.

---

## Neue Leitfrage für NEU-98

$$
\boxed{\text{Bleibt }B_{N,T}^{\mathrm{arith}}\text{ beim Ubergang }T_0 \to T^\theta \to T_c\text{ stabil, oder tritt ein neuer Kollaps auf?}}
$$

Konkrete Prüfpunkte:
1. Ist \(B_{N,T_0}^{\mathrm{arith}}\) nicht-kollabiert und trägt echte Kreuzterme?
2. Gibt es einen kritischen \(\theta^*\), bei dem der Kern seinen Charakter ändert?
3. Wie verhält sich die Korrelationsdichte \(\sum_{|m-n| \leq H_N} \Lambda(m)\Lambda(n)/mn\) als Funktion von \(\theta\)?

---

## Statusübersicht

| Punkt | Aussage | Status |
|-------|---------|--------|
| (A) | Skalenleiter \(T = M_N^\theta\), \(H_N = M_N^{1-\theta}\) | \(\checkmark[M]\) |
| (B) | Selbstdual-Skala \(T_c = \sqrt{M_N}\): strukturell kanonisch | \(\warning[M]\) |
| (C) | Kontrollskala \(T_0 = \log^2 M_N\): analytisch zugänglich | \(\checkmark[M]\) / \(\warning\) |
| (D) | \(T_c\) ist Zieltest, nicht bewiesene Skala | \(\checkmark[M]\) |
| (E) | Stabilität entlang Leiter \(T_0 \to T_c\) | \(?[O]\) |

---

## Verweise

- NEU-96: Skalentriage; drei Regime; Linearisierungspflicht
- NEU-95: Fensterpflicht; Autokorrelationsexpansion
- NEU-84: Skalentrennung \(M_N^{\mathrm{path}}/M_N^{\mathrm{op}}\) (strukturelle Analogie)
- Goldston & Y\u0131ld\u0131r\u0131m: *Higher correlations of divisor sums* (Paarstatistik in kurzen Intervallen)
- Selberg: *Lectures on sieves* (logarithmische Mittelwerts\u00e4tze)
- Montgomery: *The pair correlation of zeros* (1973)
- Heath-Brown: *The distribution of integers with a divisor in a given interval* (Fensterstatistik)
