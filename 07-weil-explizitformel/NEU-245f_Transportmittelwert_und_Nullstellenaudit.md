# NEU-245f — Transportmittelwert- und Nullstellenaudit

**Kennung:** NEU-245f  
**Ordner:** `07-weil-explizitformel/`  
**Datum:** 2026-08-06  
**Vorgänger:** NEU-245e — Niedrigenergie-Spektralmassenaudit  
**Knoten:** \([O\text{-}245e/1]\)  
**Nachfolger:** \([O\text{-}245f/1]\) — Relative-Ziel–Transport-Brücke

---

## 1 — Prüffrage

Zu entscheiden ist, ob der aus

\[
\sum_{u\ne0}a_{p,u}e_uV_p+\cdots
\]

und

\[
\sum_{s,m}\ell_{s,m}e_sV_m
\]

gebildete Kopplungsvektor

\[
T_p^{\mathrm{rel}}(\widehat\varepsilon_p)
\]

in der Transportdarstellung notwendig die Nullstellenbedingung

\[
\widehat\Psi_p(0)=0
\]

erfüllt. Für das Basismoment wäre anschließend erforderlich:

\[
\widehat\Psi_p(\xi)=O(|\xi|^\beta),
\qquad
\beta>\frac12.
\]

---

## 2 — Gesamturteil

\[
\boxed{[O\text{-}245e/1] \quad \checkmark[M]_{\mathrm{part}}}
\]

Der Audit liefert vier Ergebnisse:

1. Für einen fest typisierten endlichen Primfaser-Vektor kann die Transportmittelwertfunktion exakt als lineares Funktional seiner Kettenkoeffizienten berechnet werden.
2. Dieses Funktional verschwindet auf keinem einzelnen Fourier-Kettenmodus. Mittelwertfreiheit ist daher eine echte lineare Auslöschungsbedingung zwischen mehreren Modi.
3. Die bisherige Fourierladung, Wres-Normierung und Feshbach-Kopplungsformel erzwingen diese Auslöschung nicht.
4. Für den tatsächlich behaupteten kanonischen Vektor \(\Psi_N\) kann die Bedingung noch nicht abschließend geprüft werden, weil:
   - die Menge exakt zulässiger Hebungen nicht vollständig definiert ist;
   - der intrinsische Quotientabstieg offen ist;
   - die Brücke vom relativen Zielbasisvektor \(E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}\) zur Transportbasis \(\eta_{p;m;r,\nu}\) nicht explizit konstruiert wurde.

Die verbindliche Antwort lautet:

\[
\boxed{\text{Die Mittelwertidentität ist nicht automatisch erzwungen.}}
\]

Aber:

\[
\boxed{\text{Ob der noch nicht konstruierte kanonische Vektor sie erfüllt, bleibt offen.}}
\]

---

## 3 — Quellseitige Kopplungsformel

NEU-41 beziehungsweise NEU-221e geben auf Basiselementen:

\[
\widetilde\omega_2(e_uV_p,\,e_sV_m)
=
-us\log p\;e_{u+ps}V_{pm}.
\]

Damit lautet die relative Rohkopplung für festes \(u\ne0\):

\[
\boxed{
T_p^{\mathrm{raw}}(e_uV_p)
=
-\sum_{s,m}
\ell_{s,m}\,us\log p\;
E^{\mathrm{rel}}_{u+ps;\,m\xrightarrow p pm}.
}
\]

Für eine allgemeine Fourier-geladene Hebung:

\[
\boxed{
T_p^{\mathrm{raw}}(\widehat\varepsilon_p)
=
-\sum_{u\ne0}\sum_{s,m}
a_{p,u}\ell_{s,m}\,us\log p\;
E^{\mathrm{rel}}_{u+ps;\,m\xrightarrow p pm}.
}
\]

Diese Kopplung ist linear in den Hebungskoeffizienten \(a_{p,u}\). Sie ist jedoch nur relativ zur gewählten Hebung definiert; der intrinsische Abstieg durch den Wres-Quotienten ist weiterhin offen.

---

## 4 — Erste Typbeschränkung: NEU-225 behandelt nur den Sektor \(m=p\)

Die exakte Transportdiagonalisierung aus NEU-225 wurde im Primsektor

\[
m=p
\]

durchgeführt. Dort ist der einzige nichttriviale Teiler von \(m\) gerade \(p\), und die Kette zerfällt nach

\[
r\bmod p.
\]

NEU-225 hält ausdrücklich fest, dass zusammengesetzte Fasern mit mehreren Teilersprüngen noch offen sind.

Ein Rohkopplungsterm aus NEU-41 landet jedoch in der Faser:

\[
m_{\mathrm{Ziel}}=pm.
\]

Damit fällt er genau dann in den von NEU-225 diagonalisierten Sektor \(m_{\mathrm{Ziel}}=p\), wenn:

\[
\boxed{m=1.}
\]

Folglich ist der gegenwärtige Transportmittelwertaudit unmittelbar nur auf den Teil

\[
\sum_s\ell_{s,1}e_sV_1
\]

anwendbar. Alle Beiträge mit \(m>1\) landen in zusammengesetzten Zielsektoren \(pm\), deren Transport- und Spektraltyp durch NEU-225 nicht erfasst ist.

\[
\boxed{[O\text{-}245e/1\text{-prime-sector-scope}] \quad \checkmark[M]}
\]

\[
\boxed{[O\text{-}245e/1\text{-composite-targets}] \quad ?[O]}
\]

---

## 5 — Zweite Typbeschränkung: Fehlende Basisbrücke

NEU-221e definiert den relativen Rohzielraum durch Basisvektoren:

\[
E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}.
\]

NEU-225 arbeitet dagegen mit der orthonormalen Hilbertbasis:

\[
\eta_{p;m;r,\nu}.
\]

Dabei bezeichnet der vierte Index \(\nu\) in NEU-225 einen Bewertungs- beziehungsweise Faserindex, während \(u\) in NEU-41 bereits als Fourierladung der Hebung verwendet wird. Diese beiden Verwendungen dürfen nicht identifiziert werden.

Im Quellenbestand fehlt eine explizite Abbildung:

\[
\boxed{
\iota_{p,N}:
E^{\mathrm{rel}}_{r;\,1\xrightarrow p p}
\longrightarrow
\eta_{p;p;r,\nu}
}
\]

beziehungsweise eine entsprechende Linearkombination über \(\nu\).

Ohne diese Brücke ist nicht vollständig bestimmt:

- welche Transportkette ein Rohkopplungsterm besetzt;
- mit welcher Multiplizität er dort erscheint;
- ob verschiedene Rohkanten im selben Transportkanal kollidieren;
- und welche Koeffizienten nach dem Wres-Quotienten tatsächlich verbleiben.

Daher ist der in NEU-245e verwendete Übergang

\[
E_{r,p}
\longmapsto
e_k
\longmapsto
\sqrt{\operatorname{sech}t}\,e^{ik\theta(t)}
\]

bislang nur die natürliche Modellidentifikation, aber noch kein quellenseitig bewiesener Isomorphismus.

\[
\boxed{[O\text{-}245e/1\text{-target-transport-bridge}] \quad ?[O]}
\]

---

## 6 — Konditionale Berechnung auf einer festen Primkette

Nun sei die natürliche Basisbrücke für einen festen Primsektor vorausgesetzt. Fixiere:

\[
a\in\{0,\ldots,p-1\},
\qquad
\delta=\frac ap,
\]

und schreibe \(e_k=\eta_{a+kp}\). NEU-225 verwendet die Kreis-Fouriertransformation:

\[
e_k
\longmapsto
\frac{e^{ik\theta}}{\sqrt{2\pi}}.
\]

Anschließend:

\[
t=\log\tan\frac\theta2,
\qquad
\sin\theta=\operatorname{sech}t,
\]

und:

\[
g_0(t)=\sqrt{\sin\theta}\,f(\theta).
\]

Der Operator besitzt danach das Potential

\[
-c_p(2\delta-1)\operatorname{sech}t.
\]

Mit

\[
U=e^{i\phi(t)},
\qquad
\phi(t)=(2\delta-1)\arctan(\sinh t),
\]

gilt

\[
D_{\mathrm{pot}}=U^{-1}\Bigl(2ic_p\frac d{dt}\Bigr)U.
\]

Die Abbildung in die freie Transportdarstellung ist daher:

\[
g=Ug_0=e^{i\phi(t)}g_0(t).
\]

Dies folgt direkt aus der Eichrelation in NEU-225.

---

## 7 — Vorzeichenkorrektur in NEU-245e

Auf \((0<\theta<\pi)\) gilt:

\[
\arctan(\sinh t)=\theta-\frac\pi2.
\]

Damit lautet der Transportmittelwert:

\[
\boxed{
\mathcal M_{p,a}^+(f)
=
\int_0^\pi
f(\theta)\,
e^{+i(2a/p-1)(\theta-\pi/2)}
\frac{d\theta}{\sqrt{\sin\theta}}.
}
\]

In NEU-245e §9 steht dagegen der Faktor \(e^{-i(2a/p-1)(\theta-\pi/2)}\). Dieser entspricht nicht der dort zugleich verwendeten Relation \(D_{\mathrm{pot}}=U^{-1}D_0U\), \(U=e^{i\phi}\). Verbindlich ist unter dieser Konvention das **positive** Vorzeichen im Exponenten.

\[
\boxed{\warning[M]}
\]

Die Vorzeichenkorrektur ändert nicht die Aussage, dass Mittelwertfreiheit eine zusätzliche lineare Bedingung ist. Sie ändert aber die exakte Koeffizientenformel.

---

## 8 — Exakte Mittelwertkoeffizienten

Sei auf dem oberen Halbkreis:

\[
f(\theta)=\frac1{\sqrt{2\pi}}\sum_{k\in\mathbb Z}c_k e^{ik\theta}
\]

eine endliche Fourierkombination. Setze:

\[
\alpha_{p,a}=\frac{2a}{p}-1.
\]

Dann:

\[
\mathcal M_{p,a}^+(f)=\sum_k c_k\,\mathfrak m_{p,a,k},
\]

wobei:

\[
\boxed{
\mathfrak m_{p,a,k}
=
\frac{
\pi\,e^{i\pi k/2}
}{
\Gamma\!\left(
\frac34+\frac{k+\alpha_{p,a}}2
\right)
\Gamma\!\left(
\frac34-\frac{k+\alpha_{p,a}}2
\right)
}.
}
\]

Somit lautet die obere Mittelwertbedingung exakt:

\[
\boxed{
\sum_{k\in\mathbb Z}
c_k\,
\frac{
e^{i\pi k/2}
}{
\Gamma\!\left(
\frac34+\frac{k+2a/p-1}{2}
\right)
\Gamma\!\left(
\frac34-\frac{k+2a/p-1}{2}
\right)
}
=0.
}
\]

Für die zweite Halbkreiskopie entsteht ein analoges, separat zu fixierendes lineares Funktional. Da die beiden Kopien in der Primfaser orthogonal auftreten, muss die notwendige Niedrigenergieauslöschung grundsätzlich in beiden Komponenten erfüllt sein.

---

## 9 — Kein einzelner Kettenmodus hat Mittelwert null

Ein Koeffizient \(\mathfrak m_{p,a,k}\) könnte nur verschwinden, wenn einer der Gammafaktoren einen Pol besitzt:

\[
\frac{k+\alpha_{p,a}}{2}=\pm\left(\frac32+2n\right),
\qquad n\in\mathbb N_0.
\]

Dies ist für Primzahlen \(p\) unmöglich:

- **Fall \(p=2\):** \(\alpha_{2,a}\in\{-1,0\}\), also \(k+\alpha_{2,a}\in\mathbb Z\), während die rechte Seite eine Halbzahl ist.
- **Fall \(p\) ungerade:** Aus einer solchen Gleichung würde \(4a\equiv0\pmod p\) folgen, also \(a=0\). Dann ist \(k+\alpha_{p,0}=k-1\in\mathbb Z\), erneut keine Halbzahl.

Daher:

\[
\boxed{
\mathfrak m_{p,a,k}\neq0
\qquad
\text{für alle Primzahlen }p,\ a,\ k.
}
\]

Folglich besitzt kein einzelner Fourier-Kettenmodus die benötigte Nullstelle:

\[
\boxed{\mathcal M_{p,a}^+(e_k)\neq0.}
\]

\[
\boxed{[O\text{-}245e/1\text{-single-chain-mode}] \quad \checkmark[M]_{\mathrm{neg}}}
\]

konditional zur natürlichen Basisbrücke aus §5. Dies verallgemeinert den in NEU-245e betrachteten \(p=2\)-Einmodentest: Nicht nur dieser spezielle Modus, sondern jeder einzelne Modus scheitert am Mittelwerttest.

---

## 10 — Mittelwertfreiheit ist eine Kodimension-eins-Bedingung

Auf jeder endlichen oberen Primkette ist \(\mathcal M_{p,a}^+\) ein nichtverschwindendes lineares Funktional. Daher besitzt sein Kern Kodimension eins:

\[
\boxed{
\ker\mathcal M_{p,a}^+
\subset
\operatorname{span}\{e_k\}
\text{ hat Kodimension }1.
}
\]

Die Mittelwertfreiheit ist also erreichbar, aber nur durch eine präzise Auslöschung zwischen mindestens zwei Modi. Für die zwei Halbkreiskopien entstehen im Allgemeinen zwei Bedingungen. Der zulässige Niedrigenergieraum hat daher typischerweise mindestens Kodimension zwei innerhalb einer endlichen Primfaser.

Die Feshbach-Konstruktion erzeugt diese Bedingungen nicht allein dadurch, dass \(u\ne0\). Fourierladung garantiert Nichttrivialität der Rohkopplung, nicht ihre Orthogonalität zur Nullfrequenz.

---

## 11 — Einsetzen der Rohkopplungskoeffizienten

Im von NEU-225 erfassten Sektor muss \(m=1\) gelten. Dann \(r=u+ps\). Die Restklasse ist:

\[
a\equiv r\equiv u\pmod p.
\]

Schreibe \(u=a+jp\). Dann \(r=a+(j+s)p\), \(k=j+s\). Der Kettenkoeffizient zum Modus \(k\) ist daher formal:

\[
\boxed{
c_k^{(p,a)}
=
-\log p
\sum_{\substack{u\ne0,\ s\\ u\equiv a\;(\mathrm{mod}\,p)\\ (u-a)/p+s=k}}
a_{p,u}\,\ell_{s,1}\,us
}
\]

vor Anwendung von Wres-Quotient, Multiplizitätsabbildung und möglicher Kantenkollision.

Damit wird der Mittelwerttest zu der expliziten bilinearen Bedingung:

\[
\boxed{
\sum_k
\left(
\sum_{\substack{u\ne0,\ s\\ u\equiv a\,(p)\\ (u-a)/p+s=k}}
a_{p,u}\ell_{s,1}us
\right)
\cdot
\frac{e^{i\pi k/2}}{\Gamma(\tfrac34+\tfrac{k+\alpha}{2})\Gamma(\tfrac34-\tfrac{k+\alpha}{2})}
=0.
}
\]

Diese Gleichung steht in den bisherigen Quellen nicht. NEU-41 verlangt lediglich: nichtverschwindende Fourierladung, primitive Projektion, Wres-Normierung und eine bislang offene Hebungsunabhängigkeit des Rang-eins-Kanals. Keine dieser Bedingungen ist identisch mit der obigen gewichteten Mittelwertgleichung.

\[
\boxed{[O\text{-}245e/1\text{-source-forcing}] \quad \checkmark[M]_{\mathrm{neg,Quelle}}}
\]

---

## 12 — Die Hebungsfrage verschärft den Befund

NEU-221e zeigt:

\[
\widehat\varepsilon_p=\widehat\varepsilon_p^{\,0}+K_p.
\]

Die Wres-Normierung schneidet darin eine quadratische Menge aus. Die vollständige Menge exakt zulässiger Hebungen ist aber noch nicht abschließend definiert. Insbesondere ist nicht bewiesen, dass der Kopplungsvektor oder sein Spektralmaß unabhängig von der Hebungswahl ist.

Damit gibt es drei logisch verschiedene Anforderungen:

- **A.** Mittelwertfreiheit einer gewählten Hebung: \(\mathcal M_{p,a}(\Psi[\widehat\varepsilon_p])=0\)
- **B.** Hebungsunabhängigkeit des Mittelwerts: \(\mathcal M_{p,a}(\Psi[k])=0\) für alle \(k\in K_p\)
- **C.** Kanonischer Nullwert: \(\mathcal M_{p,a}(\Psi[\widehat\varepsilon_p^{\,0}])=0\)

Die bisherige Quotientabstiegsbedingung

\[
\widetilde T_p^{\mathrm{raw}}(\Delta_p^{\mathrm{adm}})\subseteq\mathcal N_{\mathrm{Wres,rel}}
\]

würde nur dann automatisch B implizieren, wenn das Transportmittelwertfunktional das Wres-Radikal annihiliert und damit auf dem Quotienten wohldefiniert ist. Auch dies ist nicht bewiesen:

\[
\boxed{\mathcal N_{\mathrm{Wres,rel}}\subseteq\ker\mathcal M_{p,a} \quad ?[O]}
\]

Damit ist die Mittelwertfrage nicht nur eine Koeffizientenfrage, sondern zugleich eine neue Quotientverträglichkeitsfrage.

---

## 13 — Regularität nach erfolgter Auslöschung

Für eine endliche Fourierkombination ist \(f(\theta)\) beschränkt. Nach Gewichtung und Eichung gilt:

\[
g(t)=e^{i\phi(t)}\sqrt{\operatorname{sech}t}\,f(\theta(t)).
\]

Daher \(|g(t)|\le C e^{-|t|/2}\), und somit:

\[
g\in L^1\cap L^2,
\qquad
t\,g(t)\in L^1.
\]

Für endliche Primfaser-Vektoren folgt deshalb:

\[
\mathcal M_{p,a}(f)=0
\quad\Longrightarrow\quad
\widehat g(\xi)=O(\xi),
\]

und damit \(m_0(g)<\infty\).

\[
\boxed{[O\text{-}245e/1\text{-finite-regularity}] \quad \checkmark[M]}
\]

Für einen unendlichen Grenzvektor ist dagegen eine einheitliche Abschätzung \(\int(1+|t|)|g_N(t)|\,dt<\infty\) erforderlich. Eine solche Grenzkontrolle ist nicht vorhanden.

\[
\boxed{[O\text{-}245e/1\text{-limit-regularity}] \quad ?[O]}
\]

---

## 14 — Korrektur des Einmoden-Gegenzeugen aus NEU-245e

NEU-245e bucht den speziellen Test

\[
p=2,\quad u=-1,\quad s=1,\quad m=1
\]

als vollständigen Gegenzeugen. Algebraisch landet dieser Term tatsächlich bei \(r=1\), \(pm=2\), also im passenden Primsektor. Die Schlussfolgerung \(g(t)\propto\sqrt{\operatorname{sech}t}\) setzt jedoch zusätzlich voraus, dass der relative Rohbasisvektor exakt auf einen einzelnen Transportbasisvektor mit \(a=1\), \(k=0\) abgebildet wird. Diese Basisbrücke ist, wie in §5 gezeigt, nicht explizit belegt.

Daher ist die korrekte Buchung:

\[
\boxed{\text{algebraischer Einmodentest} \quad \checkmark[M]}
\]

\[
\boxed{\text{Transport-Gegenzeugen} \quad \checkmark[K/M]_{\mathrm{neg}}}
\]

Der allgemeinere Satz aus §9 besitzt dieselbe Konditionalität zur fehlenden Ziel–Transport-Brücke.

---

## 15 — Antwort auf \([O\text{-}245e/1]\)

Die Frage

\[
\text{Erzwingt die adelische Kopplung }\widehat\Psi_N(0)=0?
\]

wird wie folgt beantwortet:

\[
\boxed{\text{Nein, nicht durch die bislang dokumentierten Bedingungen.}}
\]

Quellenseitig existiert keine Identität, welche die gewichtete Koeffizientensumme zum Verschwinden bringt. Für den noch zu konstruierenden kanonischen Quotientenvektor bleibt dagegen offen:

\[
\boxed{\widehat\Psi_N(0)=0 \quad ?[O]}
\]

Ein negativer Abschluss des gesamten Feshbach-Weyl-Kandidaten wäre erst gerechtfertigt, wenn:

- der kanonische Lift beziehungsweise das intrinsische Spektralmaß konstruiert ist; und
- dessen Transportmittelwert nachweislich ungleich null ist.

---

## 16 — Revidierte Statusbuchung

| Teilknoten | Status | Befund |
|---|---|---|
| Rohkopplungskoeffizienten | \(\checkmark[M]\) | Explizit aus NEU-41/221e |
| Beschränkung auf \(m=1\) für NEU-225-Primsektor | \(\checkmark[M]\) | Sonst zusammengesetzter Zielsektor |
| Zusammengesetzte Zielsektoren \(pm\) | \(?[O]\) | Nicht diagonalisiert |
| Relative Ziel–Transport-Brücke | \(?[O]\) | \(E^{\mathrm{rel}}\to\eta\) fehlt |
| Vorzeichen des Eichfaktors in NEU-245e | \(\warning[M]\) | Unter NEU-225-Konvention ist \(e^{+i\phi}\) korrekt |
| Exaktes Mittelwertfunktional auf fester Kette | \(\checkmark[M]\) | Gamma-Koeffizientenformel |
| Einzelmodus mit Mittelwert null | \(\checkmark[M]_{\mathrm{neg}}\) | Kein einzelner Modus genügt |
| Mittelwertfreiheit durch Modenauslöschung | \(\checkmark[K/M]\) | Kodimension eins pro Halbkomponente |
| Fourierladung erzwingt Mittelwertfreiheit | \(\checkmark[M]_{\mathrm{neg,Quelle}}\) | Keine Quellenidentität |
| Mittelwertabstieg durch Wres-Quotient | \(?[O]\) | Radikalverträglichkeit ungeprüft |
| Endliche Regularität nach Auslöschung | \(\checkmark[M]\) | \(tg\in L^1\) |
| Grenzregularität | \(?[O]\) | Keine einheitliche Abschätzung |
| Kanonischer Vektor erfüllt Nullstelle | \(?[O]\) | Vektor selbst noch nicht intrinsisch |
| \([O\text{-}245e/1]\) gesamt | \(\checkmark[M]_{\mathrm{part}}\) | Automatik negativ, kanonischer Fall offen |

---

## 17 — Nächster atomarer Knoten

Vor einem weiteren Moment- oder Numerikaudit muss die fehlende Typbrücke geschlossen werden:

\[
\boxed{[O\text{-}245f/1] \quad \text{Relative-Ziel–Transport-Brücke}.}
\]

### Arbeitsauftrag

Konstruiere eine explizite Abbildung:

\[
\boxed{
\iota_{p,N}:
\mathscr V_{\mathrm{rel},p,N}^{\mathrm{pre}}
\longrightarrow
\bigoplus_{m,a,\nu}
\ell^2(\mathbb Z)
}
\]

mit:

\[
E^{\mathrm{rel}}_{r;\,m\xrightarrow p pm}
\longmapsto
\sum_\nu
b_{p,m,r,\nu}\,
\eta_{p;pm;r,\nu}.
\]

Zu prüfen sind:

1. Übereinstimmung der Indizes \(p,m,r,\nu\);
2. Kompatibilität mit dem Wres-Radikal;
3. Abstieg auf den positiven relativen Hilbertraum;
4. Intertwining: \(D_{\mathrm{transport}}\iota_{p,N}=\iota_{p,N}D_{\mathrm{rel}}\);
5. Behandlung der zusammengesetzten Zielsektoren \(pm\);
6. Definition des Mittelwertfunktionals auf dem Quotienten.

Erst danach kann für den tatsächlichen Kopplungsvektor die Koeffizientenidentität \(\widehat\Psi_N(0)=0\) ohne Modellannahme geprüft werden.

---

## 18 — Repository-Korrekturblock

```text
AUDIT [O-245e/1]

Quellkopplung:
  T_p^raw(e_u V_p)
  = -sum_{s,m} ell_{s,m} u s log(p)
      E_rel_{u+ps; m -> pm}.

Geltungsbereich der NEU-225-Transportdarstellung:
  direkter Audit nur fuer Zielsektor pm=p,
  also fuer m=1.

Offene Typbruecke:
  E_rel_{r;1->p}
  --> eta_{p;p;r,nu}
  ist nicht explizit konstruiert.

Eichkonvention:
  D_pot = U^{-1} D_free U,
  U=e^{i phi}.
  Daher ist der freie Transportvektor U g_0
  und der Mittelwertfaktor e^{+i phi},
  nicht e^{-i phi}.
  NEU-245e §9 muss korrigiert werden.

Oberes Primfaser-Mittelwertfunktional:
  alpha = 2a/p - 1,

  M_{p,a}(f)
  = integral_0^pi
      f(theta)
      exp(+i alpha(theta-pi/2))
      dtheta/sqrt(sin theta).

Fuer e_k(theta)=exp(ik theta)/sqrt(2pi):
  m_{p,a,k}
  = pi exp(i pi k/2) /
    [Gamma(3/4+(k+alpha)/2)
     Gamma(3/4-(k+alpha)/2)].

Fuer Primzahlen p gilt:
  m_{p,a,k} != 0
  fuer alle a,k.

Folgerung:
  Kein einzelner Kettenmodus besitzt Transportmittelwert null.
  Ausloeschung ist eine echte lineare Kodimension-eins-Bedingung.

Quellenbefund:
  Fourierladung, Wres-Normierung und Feshbach-Formel
  erzwingen diese Bedingung nicht.

Status:
  [O-245e/1]                          checkmark[M]_part
  [O-245e/1-prime-sector-scope]       checkmark[M]
  [O-245e/1-composite-targets]        ?[O]
  [O-245e/1-target-transport-bridge]  ?[O]
  [O-245e/1-source-forcing]           checkmark[M]_neg,Quelle
  [O-245e/1-finite-regularity]        checkmark[M]
  [O-245e/1-limit-regularity]         ?[O]

Naechster Knoten:
  [O-245f/1]
  Relative-Ziel-Transport-Bruecke.
```

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm, öffentliche Fassung des RH-Forschungsjournals*
