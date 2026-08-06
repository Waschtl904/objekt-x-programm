# NEU-245c — Audit des Feshbach-Weyl-Kandidaten gegen [O-245b/1]

**Journalnummer:** NEU-245c  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-06  
**Anschlussknotenpunkt:** NEU-245b ([O-220-1f₀] Mindestarchitektur), NEU-221c/d/e (Feshbach-Weyl-Tripel)  
**Status:** ✓[M]_part — Teilabschluss, Folgefragen [O-245c/1] und [O-245c/2] offen

---

## Prüffrage

**[O-245b/1]:** Reicht die Mindestbedingung M3 — ein gemeinsames Quellenbild über
\(\mathcal{S}_{\mathrm{adel}}\) — aus, um die Hankel-Positivitätshierarchie aus NEU-220v/w
im Grenzübergang zu reproduzieren, oder ist eine zusätzliche M1-kompatible Kopplung
erforderlich?

---

## Gesamturteil

\[
\boxed{[O\text{-}245b/1] \quad \checkmark[M]_{\mathrm{part}}}
\]

Die Entscheidung lautet:

\[
\boxed{\text{M3 allein reicht nicht aus.}}
\]

Aber ebenso gilt:

\[
\boxed{\text{Es darf kein zusätzlicher additiver Kreuzterm zur Weil-Form eingeführt werden.}}
\]

Die fehlende Kopplung muss innerhalb des quellseitig konstruierten Feshbach-Tripels
\(\left(\mathcal{H}_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N\right)\)
liegen — also bereits in \(D_N^{\mathrm{rel}}\), im Streu-/Schurblock und im kanonischen
Vektor \(\Psi_N\) enthalten sein, bevor
\[
J_{X,N} = (D_N^{\mathrm{rel}})^{-2}
\]
gebildet wird.

---

## 1. Was NEU-221c tatsächlich leistet

Unter den Voraussetzungen
\[
(D_N^{\mathrm{rel}})^* = D_N^{\mathrm{rel}}, \qquad 0 \in \rho(D_N^{\mathrm{rel}}), \qquad \Psi_N \in \mathcal{H}_N^{\mathrm{rel}},
\]
setzt NEU-221c:

- \((D_N^{\mathrm{rel}})^{-2} \ge 0\),
- \((D_N^{\mathrm{rel}})^{-1} \Psi_N\) wohldefiniert,
- die Resolventenmatrixstelle
\[
\left\langle \Psi_N, \bigl((D_N^{\mathrm{rel}})^2 - w\bigr)^{-1} \Psi_N \right\rangle.
\]

Die Momente lauten:
\[
m_{k,N} = \left\langle \Psi_N, (D_N^{\mathrm{rel}})^{-2k-2} \Psi_N \right\rangle.
\]

Für jedes bereits wohldefinierte positive \(J_{X,N}\) sind die zugehörigen Hankelmatrizen
automatisch positiv. NEU-221c sagt deshalb selbst ausdrücklich, dass der Hankeltest positive
Feshbach-Kandidaten nicht unterscheidet; der echte Test ist die arithmetische Identität
\[
m_{k,N} \longrightarrow \mu_k.
\]

Damit konstruiert NEU-221c einen positiven Zieltyp, aber noch keine Identifikation mit den
\(\Xi\)-Momenten.

---

## 2. Abgleich mit M1 — Blockseparation

NEU-221c ist mit M1 in seiner Zielrichtung kompatibel. Die Datei verbietet ausdrücklich
\[
\bigoplus_{p \le N} D_p^{\mathrm{rel}}
\]
als bloße orthogonale Summe unabhängiger Primkanäle. Sie verlangt stattdessen die Reihenfolge:
\[
\text{Primkanäle} \longrightarrow \text{globale Feshbach-Kopplung} \longrightarrow \text{archimedischer Kanal} \longrightarrow D_N^{\mathrm{rel}} \longrightarrow (D_N^{\mathrm{rel}})^2.
\]

Die Kopplung wird damit nicht als nachträglicher additiver Kreuzterm verstanden, sondern als
Bestandteil des globalen Operators vor der Quadratisierung.

Nicht bewiesen ist jedoch, dass der in den älteren Quellen auftretende Streu- bzw. Feshbachblock
tatsächlich eine nichttriviale globale Kopplung zwischen verschiedenen Primkanälen erzeugt.
NEU-221d führt genau dies als offenen Knoten \([O\text{-}221\text{-}1c1d]\).

\[
\boxed{\text{M1-Kompatibilität des Konstruktionstyps} \quad \checkmark[K/M]}
\]
\[
\boxed{\text{M1-Verifikation des konkreten Quelloperators} \quad ?[O]}
\]

---

## 3. Abgleich mit M2 — Typ-Homogenität

Sobald das Tripel vollständig definiert ist, ist der Feshbach-Weyl-Typ homogen:
\[
\Psi_N \in \mathcal{H}_N^{\mathrm{rel}}, \qquad D_N^{\mathrm{rel}} : \mathcal{D}(D_N^{\mathrm{rel}}) \to \mathcal{H}_N^{\mathrm{rel}}, \qquad J_{X,N} : \mathcal{H}_N^{\mathrm{rel}} \to \mathcal{H}_N^{\mathrm{rel}}.
\]

Die Resolventenmatrixstelle ist dann skalar und die Momente liegen alle im selben positiven
zyklischen Modell.

Der Quellenbestand stellt dieses Tripel aber noch nicht vollständig bereit. NEU-221d verbucht
als offen:

- \(\Psi_N\) als konkreter Hilbertvektor,
- \(\|\Psi_N\|\) mit quellseitig fester Normierung,
- \(E_{D_N^{\mathrm{rel}}}(\{0\})\Psi_N = 0\),
- Integrierbarkeit der inversen Momente \(\int |\lambda|^{-2k-2} \, d\mu_{\Psi_N}(\lambda)\).

Ohne diese Bedingungen sind \(D_N^{-1}\Psi_N\), \(J_{X,N}\) im sichtbaren zyklischen Sektor
und die Momente noch nicht freigeschaltet.

NEU-221e verschärft die Normierungsfrage: Verschiedene gleich normierte Hebungen können
verschiedene Weyl-Funktionen, Spektralmaße und inverse Momente erzeugen. Der Abstieg durch
die Liftfaser bzw. den Wres-Quotienten ist bislang nur durch ein Kriterium typisiert, nicht
positiv verifiziert.

\[
\boxed{\text{M2 als abstrakter Zieltyp} \quad \checkmark[K/M]}
\]
\[
\boxed{\text{M2 für das konkrete quellseitige Tripel} \quad ?[O]}
\]

---

## 4. Abgleich mit M3 — gemeinsames Quellenbild

M3 verlangt, dass archimedische, primarithmetische und Feshbach-Daten aus derselben adelischen
Quelle entstehen.

NEU-221c setzt das Tripel \((\mathcal{H}_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N)\)
voraus, definiert aber keine vollständige Abbildung
\[
\mathcal{S}_{\mathrm{adel}} \longrightarrow (\mathcal{H}_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N).
\]

NEU-221d extrahiert nur: die Selbstadjungiertheit von \(D_N^{\mathrm{rel}}\), eine formale
lokale Vektordefinition, eine dokumentierte Feshbach-/Streuzerlegung. Die konkrete
Vektorrealisierung, ihre Normierung, der Nullmodustest und der globale Kopplungsgehalt
bleiben offen.

\[
\boxed{\text{M3 ist in NEU-221c gefordert, aber nicht konstruiert.}}
\]
\[
\boxed{\text{M3-Verifikation} \quad ?[O]}
\]

---

## 5. Warum M3 allein nicht genügt

Selbst eine perfekte gemeinsame Quellenabbildung würde zunächst nur garantieren, dass alle
Daten aus demselben \(f \in \mathcal{S}_{\mathrm{adel}}\) stammen. Daraus folgt noch nicht:
\[
m_{k,N} \to \mu_k.
\]

Denn die Positivität der Kandidatenmomente ist automatisch:
\[
\left| \sum_i c_i J_{X,N}^i \Omega_{X,N} \right|^2 \ge 0.
\]

Dasselbe gilt für die verschobene Hankelfamilie, weil \(J_{X,N} \ge 0\). Diese Positivität
sagt jedoch nicht, dass die Grenzfolge mit
\[
-\frac{1}{(2k+2)!} (\log \Xi)^{(2k+2)}(0)
\]
übereinstimmt.

NEU-220v/w zeigen, dass die vollständige doppelte Hankelhierarchie der festen Zielmomente
\(\mu_k\) RH-äquivalent ist. Ein beliebiger positiver Feshbach-Kandidat besitzt zwar seine
eigene positive Hankelhierarchie, reproduziert damit aber nicht automatisch diejenige von
\(M_\Xi\).

\[
\boxed{\text{M3 erzeugt gemeinsame Herkunft, aber keine Momentidentität.}}
\]

---

## 6. Die tatsächlich fehlende Bedingung M4

Neben M1–M3 ist eine weitere notwendige Bedingung einzuführen:

\[
\boxed{\textbf{M4 — Resolventen- und Momentidentifikation}}
\]

Es muss quellseitig — ohne Nullstellendaten und ohne nachträgliche Normierung — bewiesen
werden, dass
\[
\left\langle \Psi_N, \bigl((D_N^{\mathrm{rel}})^2 - w\bigr)^{-1} \Psi_N \right\rangle
\]
gegen \(M_\Xi(w)\) konvergiert. Eine hinreichende Zielform wäre lokale gleichmäßige
Konvergenz:
\[
\boxed{M_{X,N}(w) \longrightarrow M_\Xi(w)}
\]
in einer festen Umgebung von \(w = 0\). Dann folgen automatisch \(m_{k,N} \to \mu_k\)
für alle \(k\).

Die bloße Prüfung von \(k = 0, 1, 2\) ist ein sinnvoller Pilot, aber keine Reproduktion
der vollständigen Hankelhierarchie.

M4 zerfällt mindestens in:
\[
\begin{aligned}
\text{M4a: } & \Psi_N \text{ kanonisch und liftunabhängig}, \\
\text{M4b: } & E_{D_N}(\{0\})\Psi_N = 0 \text{ und inverse Momente endlich}, \\
\text{M4c: } & D_{\mathrm{scatt},N} \text{ enthält echte globale Kopplung}, \\
\text{M4d: } & M_{X,N} \to M_\Xi \text{ bzw. } m_{k,N} \to \mu_k.
\end{aligned}
\]

---

## 7. Antwort auf [O-245b/1]

Die ursprüngliche Alternative „M3 genügt" oder „zusätzlicher Kopplungsterm nötig" ist zu grob.
Die korrekte Entscheidung lautet:

\[
\boxed{\text{M3 allein genügt nicht.}}
\]
\[
\boxed{\text{Ein zusätzlicher additiver Kopplungsterm ist weder notwendig noch zulässig.}}
\]
\[
\boxed{\text{Erforderlich: eine M1-konforme interne globale Kopplung in } D_N^{\mathrm{rel}} \text{ und } \Psi_N,}
\]
zusammen mit M4, der arithmetischen Resolventen- bzw. Momentidentifikation.

---

## 8. Revidierte Statustabelle

| Teilfrage | Status |
|---|---|
| Feshbach-Weyl-Zieltyp | ✓[K/M] |
| Positivität von \(J_{X,N} = D_N^{-2}\) | ✓[M], konditional zur Invertierbarkeit |
| Automatische Hankelpositivität der Kandidatenmomente | ✓[M] |
| M1-konforme Zielarchitektur | ✓[K/M] |
| Konkrete globale Kopplung in \(D_{\mathrm{scatt},N}\) | ?[O] |
| Konkrete Typisierung und Normierung von \(\Psi_N\) | ?[O] |
| Nullmodusfreiheit und inverse Momente | ?[O] |
| M3: gemeinsames adelisches Quellenbild | ?[O] |
| M3 allein reproduziert die Zielhierarchie | ✓[M]_neg |
| Zusätzlicher additiver Kreuzterm | ✓[M]_neg |
| M4: \(M_{X,N} \to M_\Xi\) | ?[O], RH-stark |
| **[O-245b/1] gesamt** | **✓[M]_part** |

---

## 9. Nächste atomare Knoten

**[O-245c/1]:** Extrahiere aus dem bestehenden Feshbach-/Streusektor eine kanonische,
M1–M3-kompatible Familie \((\mathcal{H}_N^{\mathrm{rel}}, D_N^{\mathrm{rel}}, \Psi_N)\)
und prüfe zuerst:
\[
E_{D_N}(\{0\})\Psi_N = 0, \qquad \int |\lambda|^{-2} \, d\mu_{\Psi_N} < \infty.
\]
Erst wenn der Basismoment \(m_{0,N}\) existiert, ist ein Vergleich mit \(\mu_0\) sinnvoll.

**[O-245c/2]:** Der anschließende entscheidende Knoten:
\[
\boxed{M_{X,N}(w) \longrightarrow M_\Xi(w)?}
\]
Dies ist die erste Stelle, an der der Feshbach-Kandidat mehr leisten muss als automatisch
positive Momente zu erzeugen. Die richtige Fortsetzung ist kein neuer Positivitätsbeweis,
sondern ein Identitätsaudit:

\[
\boxed{\text{positiver Feshbach-Kandidat} \;\stackrel{?}{=}\; \text{arithmetische } \Xi\text{-Momentquelle.}}
\]

---

## Querverweise

- NEU-220j: Analytischer Weil-Testfunktionsraum und Konturtransport
- NEU-220l: Weil-Quadratik, Autokorrelation und positiver Kegel
- NEU-220t: Metrikblock-Klassifikation, OffAxis-Trägheit und Similarity-NoGo
- NEU-220v/w: Stieltjesfunktion/Hankelvollständigkeit, Resolventenspur, Hankelpositivität
- NEU-221: Adelische Momentquelle für den positiven Weil-Operator
- NEU-221c: Zyklischer Feshbach-Weyl-Kandidat und quadratische Resolvente
- NEU-221d: Direktextraktion NEU-46, Zyklischer Sektor und Nullmodusaudit
- NEU-221e: Affine Hebungsfaser, Wres-Quotient und Spektralmassabstieg Ψ_p
- NEU-245: [c.2a] Operatortypaudit NEU-195/NEU-216, Koszul-Kandidat
- NEU-245b: Typaudit [O-220-1f₀], Mindestarchitektur, globale Archimedes-Prim-Kopplung
- NEU-195: Bewertungsderivationen, Reduktion HH¹
- NEU-216: Log-Koeffiziententyp B-log
