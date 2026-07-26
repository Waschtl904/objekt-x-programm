# NEU-54 — X.3.24: Essentielle Selbstadjungiertheit via Nelson-Kommutator; Konfinement-Test

**Stand:** 29. Juni 2026  
**Programm:** Objekt X / X.3  
**Vorgänger:** NEU-53  
**Ziel:** Essentielle Selbstadjungiertheit von \(iJ^-\) auf \(\mathcal{D}_0\); Konfinement-Test für kompakte Resolvente; flache Achsen.

---

## 0. Strikte Trennung

\[
\text{essentielle Selbstadjungiertheit}
\neq
\text{kompakte Resolvente}
\neq
\text{diskretes Spektrum.}
\tag{54.SEP}
\]

Selbstadjungiertheit zuerst. Konfinement danach. Spektralart zuletzt.

---

## 1. Satz 54.1 — Symmetrie auf \(\mathcal{D}_0\)

\[
\mathcal{D}_0 = \operatorname{span}_{\mathrm{fin}}\{\eta_{p;m;r,u}\}.
\tag{54.1}
\]

Zu zeigen:

\[
\langle iJ^-x,y\rangle = \langle x,iJ^-y\rangle
\qquad (x,y\in\mathcal{D}_0).
\tag{54.2}
\]

Äquivalent auf Matrixebene:

\[
(J^-)_{ab} = -\overline{(J^-)_{ba}}.
\tag{54.3}
\]

Folgt direkt aus \((J_N^-)^* = -J_N^-\) (NEU-30 ff.), also \(iJ^-\) ist symmetrisch auf \(\mathcal{D}_0\).

Status: \(\checkmark\) [M]

---

## 2. Satz 54.2 — Nelson-Kommutator-Strategie (Hauptbeweis)

**Energieoperator:** Wähle \(L \ge 1\) diagonal in der \(\eta\)-Graphbasis:

\[
L\eta_{p;m;r,u} = \ell(p,m,r,u)\,\eta_{p;m;r,u},
\tag{54.4}
\]

mit

\[
\ell(p,m,r,u) \sim 1 + |r|\log(2+m) + |u|\log p + \Omega(m).
\tag{54.5}
\]

Hier ist \(\Omega(m)\) die Anzahl der Primteiler von \(m\) (mit Vielfachheit).

**Zwei Bedingungen für Nelson:**

\[
\|J^-x\| \le C\|Lx\|\qquad (x\in\mathcal{D}_0),
\tag{54.6}
\]

\[
|\langle J^-x,Lx\rangle - \langle Lx,J^-x\rangle| \le C\langle x,Lx\rangle\qquad (x\in\mathcal{D}_0).
\tag{54.7}
\]

Wenn (54.6) und (54.7) gelten, dann:

\[
\boxed{D_{\mathrm{rel}} = \overline{iJ^-}\text{ ist selbstadjungiert.}}
\tag{54.8}
\]

**Warum besser als analytische Vektoren:** Die Iterationen \((J^-)^n\) wachsen wegen der \(\gamma_N\log(n)\)-Gewichte sehr schnell; analytische Vektoren wären schwer direkt zu kontrollieren. Die Kommutator-Bedingung verlangt nur lineare Abschätzung.

Status: \(\:?\:\) [O] \(\to\) Nachweis von (54.6) und (54.7) ausständig.

---

## 3. Satz 54.3 — Defizit-Index-Alternative

Falls Nelson schwierig wird, alternative direkte Methode:

\[
((iJ^-)^* \pm i)f = 0, \qquad f\in\ell^2.
\tag{54.9}
\]

In Koeffizientenform:

\[
\sum_b (iJ^-)_{ab}\,f_b = \mp i\,f_a.
\tag{54.10}
\]

Ziel:

\[
\ker((iJ^-)^*-i) = 0,\qquad \ker((iJ^-)^*+i) = 0.
\tag{54.11}
\]

Beweis-Idee: Energie-Abschätzung zeigt, dass \(\ell^2\)-Lösungen von (54.10) exponentiell wachsen müssen \(\Rightarrow\) kein \(\ell^2\)-Element.

Status: \(\:?\:\) [O] \(\to\) Backup zu Nelson.

---

## 4. Satz 54.4 — Kato-Rellich (nur sekundär)

Kato-Rellich erfordert eine natürliche Zerlegung \(iJ^- = A + B\) mit \(A\) selbstadjungiert, \(\|Bx\|\le a\|Ax\|+b\|x\|\), \(a<1\). Da \(J^-\) primär ein gewichteter Off-Diagonal-Graphoperator ohne klaren dominanten diagonalen Teil ist, ist dieser Weg weniger natürlich.

Status: \(\warning\) [M] \(\to\) nur falls Nelson und Defizit-Index scheitern.

---

## 5. Satz 54.5 — Flache Achsen: r = 0 und n = 1

Aus der Kopplungsformel:

\[
\|\Theta_N(e_rV_n)\| = \gamma_N|r|\log(n)\,\|e_{r+n}V_n\|
\tag{54.12}
\]

folgt:

- \(r = 0\): Kopplung verschwindet, \(\Theta_N(e_0 V_n) = 0\).
- \(n = 1\): \(\log(1) = 0\), Kopplung verschwindet, \(\Theta_N(e_r V_1) = 0\).

Das sind **flache Achsen**: \(J^-\) wirkt dort wie \(0\). Sie sind nicht automatisch problematisch für Selbstadjungiertheit (der Operator kann dort trivial sein), aber für Konfinement sind sie problematisch.

**Drei Optionen:**

1. **Ausschluss:** \(\mathcal{D}_0 = \operatorname{span}_{\mathrm{fin}}\{\eta_{p;m;r,u}: r\neq 0, m>1\}\). Dann ist die flache Achse kein Teilraum der Domäne.
2. **Quotient:** Faktorisiere den Kern \(\ker(J^-)\) weg. Dann arbeitet man auf \(\mathcal{H}_{\mathrm{rel}}/\ker(J^-)\).
3. **Separat behandeln:** Zeige, dass der flache Teilraum \(\ker(J^-)\) mit \(D_{\mathrm{rel}} = 0\) selbstadjungiert ist und zerlege:

\[
\mathcal{H}_{\mathrm{rel}} = \ker(J^-)\oplus\ker(J^-)^\perp,\quad
D_{\mathrm{rel}} = 0\oplus D_{\mathrm{rel}}|_{\ker(J^-)^\perp}.
\tag{54.13}
\]

Status: \(\warning\) [M] \(\to\) Option 3 wahrscheinlich am saubersten, muss vor dem Konfinement-Satz fixiert werden.

---

## 6. Satz 54.6 — Konfinement und kompakte Resolvente

**Test:** Gilt

\[
\|\Theta_N(e_rV_n)\|\sim |r|\log n \to\infty
\tag{54.14}
\]

entlang der \(\eta\)-Basisflucht auf \(\ker(J^-)^\perp\)?

**Carleman-Kriterium** (für gewichtete Shift-/Jacobi-Operatoren entlang fester \(n\)-Fasern):

\[
\sum_r \frac{1}{|r|\log n} = \infty\qquad (n>1\text{ fest})
\tag{54.15}
\]

spricht für essentielle Selbstadjungiertheit entlang fester \(n\)-Fasern. Die globale \((p,m,u)\)-Kopplung muss zusätzlich kontrolliert werden.

**Kompakter Resolvent:** Hinreichend ist

\[
\boxed{
\|D_{\mathrm{rel}}x\|+\|x\| \ge c\|Lx\|\qquad (x\in\mathcal{D}_0),
}
\tag{54.16}
\]

mit \(L\) aus (54.4–54.5) und \(L^{-1}\) kompakt (da \(\ell(p,m,r,u)\to\infty\) entlang der Basis).

Dann:

\[
(D_{\mathrm{rel}}-i)^{-1}\in\mathcal{K}.
\tag{54.17}
\]

Erst dann darf NEU-53 Weg A (diskrete Eigenbasis) verwendet werden.

Status: \(\:?\:\) [O] \(\to\) Konfinement-Nachweis (54.16) ausständig.

---

## 7. Statusmatrix

| Aussage | Status |
|---|---|
| Symmetrie \(iJ^-\) auf \(\mathcal{D}_0\) (Satz 54.1) | \(\checkmark\) [M] |
| Nelson-Energieabschätzung (54.6–54.7) | \(\:?\:\) [O] Hauptbeweis |
| Defizit-Index-Alternative (54.11) | \(\:?\:\) [O] Backup |
| Flache Achsen \(r=0,n=1\): Option 3 | \(\warning\) [M] |
| Konfinement \(\|D_{\mathrm{rel}}x\|+\|x\|\ge c\|Lx\|\) (54.16) | \(\:?\:\) [O] |
| Kompakter Resolvent (54.17) | \(\:?\:\) [O] |

---

## 8. Nächster Schritt

\[
\boxed{
\text{NEU-55: Nachweis der Nelson-Bedingungen (54.6)–(54.7) für }iJ^-\text{ mit }L\text{ aus (54.4)–(54.5).}
}
\]

Teilfragen:
1. Berechne \(\|J^-\eta_{p;m;r,u}\|\) und vergleiche mit \(\ell(p,m,r,u)\) aus (54.5).
2. Berechne den Kommutator \([J^-,L]_{ab}\) auf \(\mathcal{D}_0\).
3. Prüfe: \(|[J^-,L]_{ab}| \le C\,\ell(a)\) pointwise?
4. Falls (54.6) scheitert: suche schwache Nelson-Version oder Defizit-Index.
