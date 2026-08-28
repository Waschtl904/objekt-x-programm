# Audit-Kandidat: SW1-BL7 — Siebter direkter Blindwert \(2d+s\)

> **Stand:** 28. August 2026  
> **Repo-Basis dieses Audits:** `main@242f1c2684a982067d45633c2b559cd149557396`  
> **Status:** `?[O]` — self-contained Beweis vorliegend, adversariales GREEN noch ausstehend, keine Promotion.  
> **Scope:** ausschließlich SW1, \(0<\sigma\le R<\varepsilon,\ R+\varepsilon<\Delta\); ausschließlich der siebte Blindwert \(2d+s\).

---

## 0. Firewall (zuerst lesen)

Dieses Audit beweist — wenn es GREEN wird — **ausschließlich**, dass \(2d+s\) für \(s\in(R,\varepsilon)\) auf SW1 direkt blind ist. Es beweist **nicht**:

- kein SW1-2TP (simultaner \(T\pm s\)-2×2-Pivot);
- keine SW1-AWI (A-Wall-Involution \(s\leftrightarrow\Delta-s\));
- keinen \(\Delta\)-Descent;
- kein HT-RED (Full-Rest-/Schur-Elimination);
- kein A0;
- keine Aussage über \(\ker\Gamma_I\);
- keine Erweiterung oder Modifikation von SW1-KNF (`audits/P11_R32_SW1_KNF_CANDIDATE.md`, bereits GREEN, PR #15) — dieses Audit **verwendet** SW1-KNF nur als Referenzrahmen für den Blindbereich, ändert es aber nicht.

\[
\boxed{\text{SW1-BL7 ist ausschließlich ein zusätzlicher Blindwert-Nachweis, kein Pivot- oder Injektivitätssatz.}}
\]

---

## 1. Kandidatensatz

\[
\boxed{
s\in(R,\varepsilon)\quad\Longrightarrow\quad 2d+s\in(a+R,\,b-R)\subset\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}
}
\]

wobei \(\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}\) der in SW1-KNF exakt bestimmte Blindbereich ist:
\[
\mathcal Z_{R,\mathrm{SW1}}^{\rm phys} = (0,a-R)\cup(a+R,b-R)\cup(b+R,T-R)\cup(T+R,T+\varepsilon).
\]

Die Aussage gilt **für jedes** \(s\in(R,\varepsilon)\), nicht nur a.e. Das "a.e." wird erst relevant, sobald man daraus eine Aussage über \(L^2\)-Funktionswerte wie \(y(2d+s)=z(2d+s)\) macht.

---

## 2. Beweis

**Konstantenidentitäten** (kanonischer Rahmen):
\[
2d-a=\Delta,\qquad b-2d=e,\qquad T-2d=2e.
\]

**Untere Schranke.** Für \(s\in(R,\varepsilon)\), also insbesondere \(s>R\):
\[
(2d+s)-(a+R) = (2d-a)+s-R = \Delta+s-R > 0,
\]
da \(\Delta>0\) und \(s>R\). Also \(2d+s>a+R\).

**Obere Schranke.** Für \(s\in(R,\varepsilon)\) gilt zunächst \(R+s<R+\varepsilon\), und auf SW1 gilt \(R+\varepsilon<\Delta<e\) (letzteres aus der Skalenkette in SW1-KNF, Behauptung 1). Also
\[
R+s<\Delta<e.
\]
Daraus
\[
(b-R)-(2d+s) = (b-2d)-(R+s) = e-(R+s) > 0,
\]
also \(2d+s<b-R\).

**Zusammen:**
\[
\boxed{a+R<2d+s<b-R.}
\]

Damit liegt \(2d+s\) im offenen Intervall \((a+R,b-R)\subset\mathcal Z_{R,\mathrm{SW1}}^{\rm phys}\); insbesondere ist der Abstand zu \(a\) und zu \(b\) strikt größer als \(R\), ohne zusätzliche Rahmenannahme außer der SW1-Bedingung selbst.

**Folgeabschätzungen (automatisch aus der Doppelungleichung).**
\[
b-(2d+s)=e-s>e-\varepsilon>R\quad\text{(da }R+s<\Delta<e\text{ mit }s<\varepsilon\text{ liefert }e-s>e-\varepsilon\text{, und }e-\varepsilon>R\text{ folgt aus derselben Kette)},
\]
\[
T-(2d+s)=(T-2d)-s=2e-s>e-s>R.
\]

**Horizon-Legalität.** Aus \(2d+s<b-R<b<T<T_0\) folgt sofort \(2d+s\in(0,T_0)\); eine separate Abschätzung ist nicht nötig.

---

## 3. Neuheit gegenüber den sechs promoteten Blindwerten

Der promotete Satz (`audits/P11_R32_HT_A4B_SW1_M_PROMOTION.md`, \(\checkmark[M]\)) listet
\[
s,\ a-s,\ a+s,\ T-s,\ 2d-s,\ T+s.
\]

Elementarer Ausschluss jeder Identität mit \(2d+s\) (für \(s\in(R,\varepsilon)\), also \(s\neq0\)):

\[
\begin{aligned}
2d+s=s &\Rightarrow d=0,\\
2d+s=a-s &\Rightarrow 2s=a-2d=-\Delta<0 \quad(\text{Widerspruch, da }s>0),\\
2d+s=a+s &\Rightarrow 2d=a \Rightarrow \Delta=0,\\
2d+s=T-s &\Rightarrow s=\tfrac{T-2d}{2}=e,\quad\text{aber }s<\varepsilon<\Delta<e,\\
2d+s=2d-s &\Rightarrow s=0,\\
2d+s=T+s &\Rightarrow 2d=T \Rightarrow e=0.
\end{aligned}
\]

Alle sechs Fälle widersprechen entweder \(d,\Delta,e>0\) oder \(s\in(R,\varepsilon)\) mit \(R>0\). Also ist \(2d+s\) für jedes \(s\in(R,\varepsilon)\) verschieden von allen sechs promoteten Werten.

---

## 4. Adversarialer Review-Checkpunkte

1. \(2d-a=\Delta\), \(b-2d=e\), \(T-2d=2e\) exakt gegen kanonische Quelle.
2. Untere Schranke \(2d+s>a+R\) (folgt direkt aus \(s>R\)).
3. Obere Schranke \(2d+s<b-R\) (folgt aus \(R+\varepsilon<\Delta<e\), SW1-KNF Skalenkette).
4. Folgeabschätzungen \(b-(2d+s)>R\) und \(T-(2d+s)>R\) korrekt aus der Doppelungleichung abgeleitet.
5. Horizon-Legalität \(2d+s<T_0\) korrekt als Folge, keine separate Annahme nötig.
6. Alle sechs Neuheits-Ausschlüsse in Abschnitt 3 einzeln korrekt.
7. Aussage gilt für jedes \(s\in(R,\varepsilon)\) (nicht nur a.e.); a.e.-Vorbehalt korrekt auf die spätere \(L^2\)-Anwendung verschoben.
8. Scope-Firewall vollständig eingehalten (Abschnitt 0).

Kein GREEN ohne alle acht Punkte einzeln bestanden. Keine Promotion, keine Registry-/Front-Änderung, solange dieser Status `?[O]` ist.

---

## 5. Erwarteter Nutzen bei GREEN

Mit SW1-BL7 stünde ein siebter direkter Blindwert zur Verfügung, relevant für die Auswertung der Row bei \(2d\pm s\) im Rahmen des \(\Delta\)-Descent-Ansatzes. Dies allein ändert nichts an HT-RED, A0 oder \(\ker\Gamma_I\) und ist kein Ersatz für SW1-2TP oder SW1-AWI.
