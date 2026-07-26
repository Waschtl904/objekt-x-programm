# NEU-47 — X.3.17: Archimedische Separation und Hadamard-Divisor-Zuordnung

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-46  
**Ziel:** Entscheide, welche Terme der Zerlegung

\[
\frac{\zeta_N'}{\zeta_N}(s)
+\partial_s\log D_{\mathrm{Arch},N}(s)
+\partial_s\log D_{\mathrm{Spec},N}^{\mathrm{rel}}(s)
\longrightarrow
\frac{\xi'}{\xi}(s)
\tag{47.0}
\]

archimedisch sind, welche aus der relativen Spektralkopplung kommen.

---

## 0. Ausgangspunkt und Leitentscheidung

NEU-46 hat gesichert:

\[
D_{\mathrm{Fesh},N}^{\mathrm{rel}} = D_{\mathrm{Euler},N}^{\mathrm{conn}} \cdot D_{\mathrm{Spec},N}^{\mathrm{rel}}
\]

mit

\[
D_{\mathrm{Euler},N}^{\mathrm{conn}} = D_{\mathrm{prim},N},
\quad
D_{\mathrm{Spec},N}^{\mathrm{rel}} = D_{\mathrm{Jac},N} \cdot D_{\mathrm{scatt},N}.
\]

NEU-47 entscheidet:

\[
\boxed{
D_{\mathrm{Arch},N} \text{ trägt Gamma-/Pol-/Trivial-Nullstellen-Korrektur.}
}
\tag{47.A}
\]

\[
\boxed{
D_{\mathrm{Spec},N}^{\mathrm{rel}} \text{ trägt die relative Hadamard-/Nichttrivial-Nullstellen-Schicht.}
}
\tag{47.B}
\]

Keine Doppelzählung: Gamma liegt ausschließlich in \(D_{\mathrm{Arch}}\).

---

## 1. Archimedischer Normierungsfaktor \(D_{\infty}\)

Die kanonische archimedische Normierung ist der vollständige Faktor der \(\xi\)-Funktion:

\[
D_{\infty}(s) := \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2).
\tag{47.1}
\]

Seine logarithmische Ableitung ist:

\[
\partial_s \log D_{\infty}(s)
= \frac{1}{s} + \frac{1}{s-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi(s/2),
\tag{47.2}
\]

wobei \(\psi = \Gamma'/\Gamma\) die Digammafunktion ist.

Diese Terme tragen:
- **\(1/s\):** Pol bei \(s=0\) (triviale Nullstelle von \(\xi\), archimedisch)
- **\(1/(s-1)\):** Pol bei \(s=1\) (Pol von \(\zeta\))
- **\(-\tfrac{1}{2}\log\pi\):** geodätischer Renormierungsterm
- **\(\tfrac{1}{2}\psi(s/2)\):** Gamma-Pol-Kette bei \(s = -2k\), \(k \ge 1\)

**Satz 47.1 — Archimedische Separationsregel:**

\[
\boxed{
D_{\mathrm{Arch},N}(s) \longrightarrow D_{\infty}(s)
}
\tag{47.3}
\]

im logarithmischen Ableitungssinn \(N \to \infty\).
Insbesondere trägt \(D_{\mathrm{Arch},N}\) alle vier Terme aus (47.2) und keine Nichttrivial-Nullstellen.

Status: \(\checkmark/\warning\) [M] als Zielsatz (archimedischer Grenzwert extern).

---

## 2. Trivialnullstellen-Ausschluss für \(D_{\mathrm{Spec},N}^{\mathrm{rel}}\)

Bei \(s = -2k\) (\(k \ge 1\)) hat \(\zeta'/\zeta\) einen einfachen Pol mit Residuum \(+1\). Dieser Pol wird in \(\xi'/\xi\) durch \(\tfrac{1}{2}\psi(s/2)\) aufgehoben:

\[
\frac{\zeta'}{\zeta}(s) + \frac{1}{2}\psi(s/2) \text{ ist bei } s=-2k \text{ regulär.}
\tag{47.4}
\]

Folglich darf \(D_{\mathrm{Spec},N}^{\mathrm{rel}}\) dort keinen eigenen Grenzpol und keine eigene Nullstelle erzeugen.

**Satz 47.2 — Trivialnullstellen-Ausschluss:**

Für jede kleine Kontur \(\gamma_k\) um \(s = -2k\) ohne weitere Singularitäten:

\[
\boxed{
\lim_{N\to\infty}
\frac{1}{2\pi i}
\int_{\gamma_k}
\partial_s \log D_{\mathrm{Spec},N}^{\mathrm{rel}}(s)\,ds = 0.
}
\tag{47.5}
\]

Das bedeutet: \(D_{\mathrm{Spec},N}^{\mathrm{rel}}\) erzeugt keine trivialen Nullstellen.

Status: \(\checkmark/\warning\) [M] als Bedingung. Nachweis: \(\:?\:\) [O].

**Kommentar:** Satz 47.2 liefert den saubersten Beweis, dass \(D_{\mathrm{Spec}}\) nicht die Gamma-Terme tragen kann: Ein Gamma-Term in \(D_{\mathrm{Spec}}\) würde entweder (47.5) verletzen oder eine nicht-kanonische Kompensation erfordern.

---

## 3. Nichttrivialnullstellen-Kriterium (Hadamard-Test)

**Satz 47.3 — Nichttrivialnullstellen-Kriterium:**

Für eine kleine Kontur \(\gamma_\rho\) um eine nichttriviale Nullstelle \(\rho\) von \(\xi\), ohne weitere Nullstellen:

\[
\boxed{
\lim_{N\to\infty}
\frac{1}{2\pi i}
\int_{\gamma_\rho}
\partial_s \log D_{\mathrm{Spec},N}^{\mathrm{rel}}(s)\,ds = m_\rho,
}
\tag{47.6}
\]

falls \(\zeta_N\) auf \(\gamma_\rho\) keinen eigenen Divisor erzeugt.

Alternativ (kombinierter Test):

\[
\lim_{N\to\infty}
\frac{1}{2\pi i}
\int_{\gamma_\rho}
\left(
\frac{\zeta_N'}{\zeta_N}(s)
+ \partial_s\log D_{\mathrm{Spec},N}^{\mathrm{rel}}(s)
\right)ds = m_\rho.
\tag{47.7}
\]

Das ist der eigentliche Hadamard-Test: \(D_{\mathrm{Spec},N}^{\mathrm{rel}}\) muss die Divisorstruktur von \(\xi\) abzüglich des Eulerprodukt-Beitrags reproduzieren.

Status: \(\:?\:\) [O]

---

## 4. Residuentabelle

| Stelle \(s\) | Singularität von \(\xi'/\xi\) | Quelle | Erwartete Quelle in Zerlegung |
|---|---|---|---|
| \(s = 0\) | Pol Residuum \(+1\) | triviale Nullstelle \(\xi\) | \(D_{\mathrm{Arch}}\) via \(1/s\) |
| \(s = 1\) | Pol Residuum \(+1\) | Pol von \(\zeta\) | \(D_{\mathrm{Arch}}\) via \(1/(s-1)\) |
| \(s = -2k\), \(k\ge 1\) | Pol Residuum \(+1\) | triviale Nullstellen \(\zeta\), kompensiert durch \(\Gamma\) | **nur** \(D_{\mathrm{Arch}}\) via \(\tfrac{1}{2}\psi(s/2)\) |
| \(s = \rho\) (nichttrivial) | Pol Residuum \(m_\rho\) | Nullstellen von \(\xi\) | \(D_{\mathrm{scatt},N} \subset D_{\mathrm{Spec}}^{\mathrm{rel}}\) |

Status: \(\checkmark\) [M] als Erwartungsstruktur; Nachweis Zeilen 1–2 archimedisch extern.

---

## 5. Rolle von \(D_{\mathrm{Jac},N}\) und \(D_{\mathrm{scatt},N}\)

Die Faktorisierung \(D_{\mathrm{Spec},N}^{\mathrm{rel}} = D_{\mathrm{Jac},N} \cdot D_{\mathrm{scatt},N}\) trennt:

**\(D_{\mathrm{Jac},N}\):** Jacobi-Determinante der freien relativen Operatoren.

\[
D_{\mathrm{Jac},N}(z) = \prod_{p\le N} \det(z-D_{\mathrm{rel},p}^-).
\tag{47.8}
\]

Erwartung: Sie trägt reguläre Renormierungs-/Phasen-/Exponentialfaktoren, entspricht im Hadamard-Bild eher dem \(e^{a+bs}\)-Faktor. Kein eigener Divisor.

Status: \(\:?\:\) [O] (Divisorneutralität zu zeigen)

**\(D_{\mathrm{scatt},N}\):** Birman-Schwinger-/Streu-Determinante.

\[
D_{\mathrm{scatt},N}(z,\beta) = \prod_{p\le N}\left(1-\frac{M_p(z)}{1-p^{-\beta}}\right).
\tag{47.9}
\]

Erwartung: Trägt den Divisor. Im Hadamard-Bild entspricht \(D_{\mathrm{scatt},N}\) dem Produkt \(\prod_\rho E_1(s/\rho)\) nach geeigneter Regularisierung.

Status: \(\:?\:\) [O] (Hadamard-Konvergenz zu zeigen)

**Hatte-Arch-Bild:**

\[
\xi(s) = e^{a+bs} \prod_\rho E_1(s/\rho)
\]

projiziert auf:

| Hadamard-Faktor | Zerlegungskomponente |
|---|---|
| \(\tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\) | \(D_{\mathrm{Arch},N} \to D_{\infty}\) |
| \(e^{a+bs}\) | \(D_{\mathrm{Jac},N}\) (renormierend) |
| \(\prod_\rho E_1(s/\rho)\) | \(D_{\mathrm{scatt},N}\) (Divisor) |
| \(\zeta_N(s)^{-1}\) | \(D_{\mathrm{prim},N} = D_{\mathrm{Euler},N}^{\mathrm{conn}}\) |

---

## 6. Warnung: Konvergenztyp

Wichtige Bedingung für die Programmkonsistenz:

\[
\boxed{
D_{\mathrm{Spec},N}^{\mathrm{rel}} \not\to 1 \text{ als schlicht holomorph-normale Konvergenz für } \Re(s) > 1.
}
\tag{47.10}
\]

Risiko: Wenn \(D_{\mathrm{Spec},N}^{\mathrm{rel}} \to 1\) lokal gleichmäßig für \(\Re(s) > 1\), folgt per Identitätssatz auch \(D_{\mathrm{Spec}}^{\mathrm{rel}} \equiv 1\) im kritischen Streifen, also kein Divisor.

Die korrekte Konvergenz ist daher:
- **Relativ** (Quotient gegen endliche Approximanten),
- **Meromorph** (nicht holomorph — Polstellenverschiebungen erlaubt),
- **Konturweise** (nur auf Konturen, nicht offen-dicht), oder
- **Trace-formelartig** (als distributional/spurformartige Grenzaussage).

Status: \(\warning\) [M] als Warnung; genaue Konvergenzmode: \(\:?\:\) [O]

---

## 7. Prüfroute für NEU-48

Die abgeschlossene Prüfroute lautet:

1. **Residuentabelle** für \(s = 0, 1, -2, -4, \ldots, \rho\): Welcher Faktor liefert welches Residuum? \(\:?\:\) [O]
2. **Konturtest triviale Nullstellen:** \(D_{\mathrm{Spec},N}^{\mathrm{rel}}\) bei \(s = -2k\) neutral (Satz 47.2)? \(\:?\:\) [O]
3. **Konturtest nichttriviale Nullstellen:** \(D_{\mathrm{scatt},N}\) liefert \(m_\rho\) (Satz 47.3)? \(\:?\:\) [O]
4. **Divisorneutralität \(D_{\mathrm{Jac},N}\):** Nullstellenfrei? \(\:?\:\) [O]
5. **Konvergenztyp** \(D_{\mathrm{Spec},N}^{\mathrm{rel}}\): relativ-meromorph oder Trace-formelartig? \(\:?\:\) [O]

---

## 8. Statusmatrix

| Aussage | Status |
|---|---|
| \(D_{\mathrm{Arch},N} \to \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\) (Zielsatz) | \(\checkmark/\warning\) [M] |
| \(D_{\mathrm{Spec}}^{\mathrm{rel}}\) erzeugt keine trivialen Nullstellen (Satz 47.2) | Bedingung \(\checkmark\); Nachweis \(\:?\:\) [O] |
| \(D_{\mathrm{Spec}}^{\mathrm{rel}}\) trägt Divisor bei \(\rho\) (Satz 47.3) | \(\:?\:\) [O] |
| \(D_{\mathrm{Jac},N}\) divisorneutral | \(\:?\:\) [O] |
| \(D_{\mathrm{scatt},N}\) trägt Divisor (Hadamard) | \(\:?\:\) [O] |
| Konvergenztyp \(D_{\mathrm{Spec}}^{\mathrm{rel}}\) relativ-meromorph/trace-artig | \(\:?\:\) [O] |
| Residuentabelle vollständig | \(\:?\:\) [O] |
| Keine Doppelzählung Gamma/Divisor | \(\checkmark\) [M] als Designentscheidung |

---

## 9. Nochmaliges Fazit

NEU-47 ersetzt die Frage

\[
\text{Hadamard oder Gamma oder beides?}
\]

durch drei gesicherte Entscheidungen:

\[
\boxed{\text{Gamma gehört zu }D_{\mathrm{Arch}}.}\tag{47.D1}
\]

\[
\boxed{\text{Hadamard-Divisor gehört zu }D_{\mathrm{scatt}} \subset D_{\mathrm{Spec}}^{\mathrm{rel}}.}\tag{47.D2}
\]

\[
\boxed{D_{\mathrm{Jac}} \text{ kontrolliert die exponentielle/renormierende Hadamard-Freiheit.}}\tag{47.D3}
\]

Der Nachweis dieser drei Entscheidungen ist der Kern von NEU-48.

---

## 10. Nächster Schritt

\[
\boxed{\text{NEU-48: Konturtest für triviale und nichttriviale Nullstellen; Divisorneutralität von }D_{\mathrm{Jac},N}.}
\]
