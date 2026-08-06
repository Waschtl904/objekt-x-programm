# NEU-245e — Niedrigenergie-Spektralmassenaudit

**Kennung:** NEU-245e  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Vorgänger:** NEU-245d — Direktaudit [O-245c/1]: Kanonisierung, Nullmodus und Basismoment  
**Knoten:** \([O\text{-}245d/1]\)  
**Nachfolger:** \([O\text{-}245e/1]\) — Transportmittelwert- und Nullstellenaudit des tatsächlichen kanonischen \(\Psi_N\)

---

## 1 — Gegenstand

Zu prüfen sind für das zyklische Tripel

\[
\left(
\mathcal H_N^{\mathrm{rel}},
D_N^{\mathrm{rel}},
\Psi_N
\right)
\]

die Bedingungen

\[
\mu_{\Psi_N}^{D_N^{\mathrm{rel}}}(\{0\})=0,
\]

\[
\int_{\mathbb R}
|\lambda|^{-2}\,d\mu_{\Psi_N}(\lambda)<\infty,
\]

und gegebenenfalls die stärkere Forderung einer sichtbaren Spektrallücke um \(0\).

Ausgangspunkt ist der korrigierte Stand von NEU-245d:

- Symmetrie des Operators gesichert.
- Essentielle Selbstadjungiertheit offen.
- Intrinsischer Abstieg von \(\Psi_N\) offen.
- Nullmodusfreiheit offen.
- Inverse Momentintegrabilität quellenseitig nicht belegt.
- Richtige Potenzschwelle für \(m_{0,N}\): \(\alpha>2\).

---

## 2 — Gesamturteil

\[
\boxed{[O\text{-}245d/1] \quad \checkmark[M]_{\mathrm{part}}}
\]

Die Niedrigenergiefrage lässt sich strukturell stark reduzieren:

1. Auf jeder von NEU-225 diagonalisierten Primfaser besitzt \(D_{\mathrm{rel}}\) rein absolutstetiges Spektrum und keinen Eigenwert \(0\). Daher verschwindet dort der atomare Nullmodus für jeden Faservektor automatisch.
2. Die Basismomentbedingung ist exakt eine gewichtete Fourierbedingung:
\[
\int \frac{|\widehat\Psi(\xi)|^2}{\xi^2}\,d\xi<\infty.
\]
3. Bei hinreichend regulären Vektoren ist dafür notwendig, dass der transformierte Kopplungsvektor bei Frequenz \(0\) verschwindet:
\[
\widehat\Psi(0)=0.
\]
4. Eine Nullstelle erster Ordnung ist bereits hinreichend:
\[
\widehat\Psi(\xi)=O(\xi)
\quad\Longrightarrow\quad
F_N(\varepsilon)=O(\varepsilon^3)
\quad\Longrightarrow\quad
m_{0,N}<\infty.
\]
5. Die Feshbach-Architektur und die bloße Fourierladung der primitiven Hebung erzwingen diese Nullstelle nicht.
6. Der minimale Einmodenkandidat aus NEU-41 liefert einen expliziten zulässigen Testfall, in dem die Spektraldichte bei \(0\) nicht verschwindet und \(m_{0,N}\) divergiert.
7. Eine echte offene Spektrallücke ist für die endlichen Graphmodenkandidaten nicht zu erwarten und für \(m_{0,N}<\infty\) auch nicht notwendig.

**Neue Kernfrage:**

\[
\boxed{
\text{Erzeugt die kanonische adelische Kopplung eine
quellseitig erzwungene Nullstelle von }\widehat\Psi_N
\text{ bei }0?
}
\]

---

## 3 — Spektraldarstellung auf einer Primfaser

NEU-225 konstruiert auf jeder Primfaser \(\mathcal H_{p,a}\) eine unitäre Äquivalenz

\[
D_{\mathrm{rel}}\big|_{\mathcal H_{p,a}}
\cong
2ic_p\frac{d}{dt}
\]

auf zwei Kopien von \(L^2(\mathbb R)\). Das zunächst auftretende \(\operatorname{sech}t\)-Potential wird durch eine beschränkte unitäre Eichtransformation entfernt.

Fixiere die unitäre Fouriertransformation

\[
\widehat g(\xi)=\frac1{\sqrt{2\pi}}
\int_{\mathbb R}g(t)e^{-it\xi}\,dt.
\]

Dann gilt, bis auf ein für die folgenden Aussagen irrelevantes Vorzeichen,

\[
D_{\mathrm{rel}} \sim -2c_p\,M_\xi.
\]

Für einen Faservektor

\[
g=(g_+,g_-)
\in
L^2(\mathbb R)\oplus L^2(\mathbb R)
\]

lautet sein Spektralmaß daher:

\[
\boxed{
\mu_g(B)=
\int_{\mathbb R}
\mathbf 1_B(-2c_p\xi)
\left(
|\widehat g_+(\xi)|^2+
|\widehat g_-(\xi)|^2
\right)d\xi.
}
\]

Damit ist das Niedrigenergieproblem vollständig in Fourierkoordinaten übersetzt.

---

## 4 — Der atomare Nullmodus

Da das Spektralmaß bezüglich des Lebesguemaßes absolut stetig ist,

\[
\mu_g(\{0\})=0
\]

für jeden Faservektor \(g\). Äquivalent:

\[
E_{D_{\mathrm{rel}}}(\{0\})g=0.
\]

NEU-225 hält entsprechend fest, dass die Primfasern keine Eigenwerte und insbesondere keinen Kern besitzen.

Daher:

\[
\boxed{[O\text{-}245d/1\text{-prime-zero-atom}] \quad \checkmark[M]}
\]

unter der in NEU-225 konstruierten selbstadjungierten Transportrealisierung.

### Einschränkung

Dieser Befund gilt zunächst für die explizit diagonalisierten Primsektoren. Nicht vollständig bewiesen ist damit:

- der Abstieg auf den gesamten adelischen Quotienten,
- die Behandlung zusammengesetzter \(m\)-Sektoren,
- die Existenz einer einzigen globalen selbstadjungierten Realisierung mit der behaupteten gemeinsamen Kopplungsstruktur.

Daher bleibt:

\[
\boxed{[O\text{-}245d/1\text{-global-zero-atom}] \quad ?[O]}
\]

---

## 5 — Nullatom ist nicht inverse Integrabilität

Obwohl

\[
\mu_g(\{0\})=0,
\]

kann

\[
\int|\lambda|^{-2}\,d\mu_g(\lambda)
\]

divergieren. Aus der Spektraldarstellung folgt exakt:

\[
\boxed{
\int_{\mathbb R}|\lambda|^{-2}\,d\mu_g(\lambda)
=
\frac1{4c_p^2}
\int_{\mathbb R}
\frac{|\widehat g_+(\xi)|^2+|\widehat g_-(\xi)|^2}{\xi^2}\,d\xi.
}
\]

Somit:

\[
\boxed{
g\in\mathcal D(|D_{\mathrm{rel}}|^{-1})
\iff
\frac{\widehat g}{\xi}
\in
L^2(\mathbb R;\mathbb C^2).
}
\]

Der atomare Nullmodustest prüft nur, ob Masse genau bei \(0\) liegt. Das Basismoment prüft, wie schnell die kontinuierliche Spektralmasse in der Umgebung von \(0\) verschwindet.

---

## 6 — Exaktes Verteilungskriterium

Setze

\[
F_g(\varepsilon)=
\mu_g\bigl(( -\varepsilon,\varepsilon )\setminus\{0\}\bigr).
\]

Dann gilt für jedes \(\varepsilon_0>0\):

\[
\int_{0<|\lambda|\le\varepsilon_0}
|\lambda|^{-2}\,d\mu_g(\lambda)<\infty
\]

genau dann, wenn

\[
\boxed{
\int_0^{\varepsilon_0}
\frac{F_g(r)}{r^3}\,dr<\infty.
}
\]

Bei Endlichkeit gilt außerdem notwendig:

\[
\boxed{F_g(r)=o(r^2).}
\]

Eine hinreichende Potenzbedingung ist:

\[
F_g(r)=O(r^\alpha),
\qquad
\alpha>2.
\]

Damit bestätigt die Transportdarstellung die korrigierte Schwelle aus NEU-245d.

---

## 7 — Ordnung der spektralen Nullstelle

Angenommen, in der spektralen Darstellung gilt nahe \(0\):

\[
\widehat g(\xi)=O(|\xi|^\beta).
\]

Dann:

\[
F_g(\varepsilon)=O(\varepsilon^{2\beta+1}).
\]

Für das \(k\)-te inverse Moment

\[
\int|\lambda|^{-2k-2}\,d\mu_g(\lambda)
\]

gilt lokal:

\[
m_k(g)<\infty
\quad\Longleftarrow\quad
\beta>k+\frac12.
\]

Insbesondere:

\[
\boxed{m_0(g)<\infty \quad\Longleftarrow\quad \beta>\frac12.}
\]

Eine Nullstelle erster Ordnung liefert \(F_g(\varepsilon)=O(\varepsilon^3)\) und damit \(m_0(g)<\infty\).

Für die ersten drei Momente genügt:

\[
\begin{array}{c|c}
\text{Moment}&\text{hinreichende Nullstellenordnung}\\
\hline
m_0&\beta>\frac12\\
m_1&\beta>\frac32\\
m_2&\beta>\frac52
\end{array}
\]

---

## 8 — Konkretes Quellenkriterium: gewichtete Mittelwertfreiheit

Für einen regulären Faservektor \(g\in L^1\cap L^2\) gilt:

\[
\widehat g(0)=\frac1{\sqrt{2\pi}}\int_{\mathbb R}g(t)\,dt.
\]

Eine notwendige Niedrigenergiebedingung ist daher:

\[
\boxed{\int_{\mathbb R}g(t)\,dt=0.}
\]

Falls zusätzlich \(tg(t)\in L^1(\mathbb R)\), folgt aus der Mittelwertfreiheit:

\[
\widehat g(\xi)=O(\xi).
\]

Damit:

\[
\boxed{
\int g=0
\quad\text{und}\quad
tg\in L^1
\quad\Longrightarrow\quad
m_0(g)<\infty.
}
\]

---

## 9 — Form des Kriteriums in der Kreisvariable

**Vorzeichenkorrektur (NEU-245f §7):** Die ursprüngliche Fassung dieses Abschnitts verwendete \(e^{-i(2a/p-1)(\theta-\pi/2)}\). Unter der in NEU-225 gültigen Eichkonvention \(D_{\mathrm{pot}}=U^{-1}D_0U\), \(U=e^{i\phi}\) mit \(\phi(t)=(2\delta-1)\arctan(\sinh t)\), ist der freie Transportvektor \(g=Ug_0\), und das korrekte Mittelwertfunktional trägt daher den Faktor \(e^{+i\phi}\), nicht \(e^{-i\phi}\).

NEU-225 verwendet auf dem Halbkreis die Koordinate

\[
t=\log\tan\frac\theta2,
\qquad
\sin\theta=\operatorname{sech}t,
\]

sowie die Gewichtstransformation \(g_0(t)=\sqrt{\sin\theta}\,f(\theta)\) und die unitäre Eichtransformation \(g=e^{i\phi}g_0\) mit

\[
\phi(t)=(2\delta-1)\arctan(\sinh t)=(2a/p-1)(\theta-\pi/2).
\]

Die korrekte Mittelwertbedingung auf einer Halbkreisfaser lautet daher:

\[
\boxed{
\int_0^\pi
f(\theta)\,
 e^{+i(2a/p-1)(\theta-\pi/2)}
\frac{d\theta}{\sqrt{\sin\theta}}
=0.
}
\]

Für den vollständigen Vektor muss die entsprechende Bedingung in beiden Halbkreiskopien gelten.

---

## 10 — Warum die bisherige Quellenarchitektur die Bedingung nicht erzwingt

NEU-41 konstruiert den Kopplungsvektor aus einer Fourier-geladenen primitiven Hebung:

\[
\sum_{u\ne0}a_{p,u}e_uV_p+\cdots
\]

Die Fourierladung \(u\ne0\) verhindert lediglich das triviale Verschwinden der Kopplung. Weder die Faktoren \(u\), \(s\), \(\log p\) noch die Selektionsregel erzwingen automatisch \(\widehat\Psi_p(0)=0\). Die Quellen enthalten bislang keine entsprechende Koeffizientenidentität.

\[
\boxed{[O\text{-}245d/1\text{-automatic-integrability}] \quad \checkmark[M]_{\mathrm{neg}}}
\]

---

## 11 — Expliziter Gegenzeuge aus dem minimalen Einmodentest

Wähle \(p=2\), \(u=-1\), \(s=1\), \(m=1\). Dann \(u+ps=1\), \(pm=2\), Restklasse \(a=1\), \(\delta=\frac12\). Die Eichphase verschwindet. Unter der natürlichen Basisbrücke (konditional, vgl. NEU-245f §5/§14) ist der transformierte Halbkreisvektor proportional zu \(\sqrt{\operatorname{sech}t}\), dessen Fourierintegral bei \(0\) nicht verschwindet.

Folglich \(F_g(\varepsilon)\asymp\varepsilon\) und \(\int|\lambda|^{-2}d\mu_g=\infty\).

\[
\boxed{[O\text{-}245d/1\text{-minimal-mode}] \quad \checkmark[M]_{\mathrm{neg}}}
\]

Der Transport-Gegenzeuge trägt Status \(\checkmark[K/M]_{\mathrm{neg}}\) (konditional zur fehlenden Basisbrücke; vgl. NEU-245f).

---

## 12 — Die sichtbare Spektrallücke ist das falsche unmittelbare Ziel

Für nichtverschwindende endliche Graphmodenkandidaten ist eine offene Spektrallücke um \(0\) ausgeschlossen (Analytizitätsargument). Sie ist für \(m_0<\infty\) auch nicht erforderlich.

Die Zielhierarchie lautet:

\[
\boxed{
\text{Nullatomfreiheit}
\;<\;
\text{Nullstelle genügender Ordnung}
\;<\;
\text{Spektrallücke}.
}
\]

\[
\boxed{[O\text{-}245d/1\text{-finite-mode-gap}] \quad \checkmark[M]_{\mathrm{neg}}}
\]

---

## 13 — Globale spektrale Formulierung

Sei, konditional zur Selbstadjungiertheit, eine Spektraldarstellung \(D_N^{\mathrm{rel}}\cong M_\lambda\) auf \(\int^\oplus\mathfrak h_N(\lambda)\,d\lambda\) gegeben. Der intrinsische globale Zieltest ist:

\[
\boxed{\widehat\Psi_N(0)=0}
\]

zusammen mit \(\widehat\Psi_N(\lambda)=O(|\lambda|^\beta)\), \(\beta>\frac12\). Eine globale Auslöschung durch vektorielle Interferenz überlappender Primkanäle ist prinzipiell möglich, aber bislang nicht bewiesen.

---

## 14 — Revidierte Statusbuchung

| Teilknoten | Status | Befund |
|---|---|---|
| Primfaser besitzt atomaren Nullmodus | \(\checkmark[M]_{\mathrm{neg}}\) | Kein Eigenwert \(0\) |
| \(\mu_g(\{0\})=0\) auf Primfasern | \(\checkmark[M]\) | Absolutstetiges Spektrum |
| Globaler adelischer Nullmodustest | \(?[O]\) | Gesamtoperator und Quotient nicht vollständig kontrolliert |
| Exakte Fourierform von \(m_0\) | \(\checkmark[M]\) | Gewicht \(\xi^{-2}\) |
| Exaktes Verteilungskriterium | \(\checkmark[M]\) | \(\int F(r)r^{-3}dr<\infty\) |
| Mittelwertfreiheit als Quellenkriterium | \(\checkmark[M]\) | Mit erstem Moment hinreichend |
| Fourierladung erzwingt Mittelwertfreiheit | \(\checkmark[M]_{\mathrm{neg}}\) | Keine solche Identität vorhanden |
| Minimaler Einmodenkandidat | \(\checkmark[M]_{\mathrm{neg}}\) | Explizite Divergenz möglich |
| Offene Spektrallücke bei endlichen Modi | \(\checkmark[M]_{\mathrm{neg}}\) | Nur für Nullvektor möglich |
| Kanonische globale Nullstelle von \(\widehat\Psi_N\) | \(?[O]\) | Neue Kernfrage |
| \(m_{0,N}<\infty\) für den kanonischen Kandidaten | \(?[O]\) | Noch nicht freigeschaltet |
| \([O\text{-}245d/1]\) gesamt | \(\checkmark[M]_{\mathrm{part}}\) | Problem auf explizite Quellenidentität reduziert |

---

## 15 — Neuer atomarer Knoten

\[
\boxed{[O\text{-}245e/1] \quad \text{Transportmittelwert- und Nullstellenaudit von }\Psi_N.}
\]

Bearbeitet in: **NEU-245f** (Direktaudit \([O\text{-}245e/1]\)).

Nächster offener Knoten:

\[
\boxed{[O\text{-}245f/1] \quad \text{Relative-Ziel–Transport-Brücke}.}
\]

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
