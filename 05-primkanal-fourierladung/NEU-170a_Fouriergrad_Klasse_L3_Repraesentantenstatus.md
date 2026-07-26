# NEU-170a — Fouriergrad der Klasse $[L_3]$: Klasse, Repräsentant und Testmodus

**Status:** Klassen- und Repräsentantenaudit abgeschlossen. Negativer Quellenbefund.
**Vorgänger:** NEU-169 → NEU-170 → NEU-170a.
**Gesperrt:** $P^{ch}(L_3^\circ)\neq0$, $[L_3]_{ch}\neq0$, $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$, $T_p^{pre}(e_uV_p)\neq0$ bis zur Klärung in NEU-170b.
**Nächster Knoten:** NEU-170b — Ursprungsdefinition und Repräsentantenfreiheit von $L_3$.

---

## 170a.0 — DAG-Position und Auftrag

$$\text{NEU-169} \longrightarrow \text{NEU-170} \longrightarrow \boxed{\text{NEU-170a}}.$$

NEU-170 hat ergeben, dass die bisherige Quellenkette lediglich

$$L_3^\circ\neq0$$

beweist, jedoch nicht

$$\operatorname{supp}^{\times}(L_3^\circ) := \{(s,m): s\ell_{s,m}\neq0\} \neq\varnothing.$$

Der Auftrag von NEU-170a lautet:

$$\boxed{\text{Erzwingt die Definition, Kohomologieklasse oder Reinheitsstruktur von }[L_3]\text{ einen Fourieranteil mit }s\neq0?}$$

Dabei sind drei Ebenen strikt zu unterscheiden:
- die Kohomologieklasse $[L_3]$,
- ein gewählter Repräsentant $L_3$,
- eine modellhafte Spezialisierung auf einen einzelnen Fouriermodus.

---

## 170a.A — Die tatsächlich benötigte Aussage

Für den elementaren Einzelmoden-Rohzeugen aus NEU-169 wird die Repräsentantenaussage

$$\boxed{\exists(s_0,m_0): s_0\ell_{s_0,m_0}\neq0} \tag{170a.1}$$

benötigt. Dies ist äquivalent zu

$$P^{ch}(L_3^\circ)\neq0,$$

wobei formal

$$P^{ch}\!\left(\sum_{s,m}\ell_{s,m}e_sV_m\right) := \sum_{\substack{s\neq0\\m}}\ell_{s,m}e_sV_m$$

den geladenen Fourieranteil bezeichnet.

Die bloße Aussage $L_3^\circ\neq0$ reicht nicht, da ein nichtverschwindender Repräsentant vollständig im ungechargten Sektor $\operatorname{span}\{e_0V_m\}$ liegen kann.

---

## 170a.B — Audit von NEU-29

NEU-29 verwendet die Normierung

$$L_3^\circ = C_L^{-1}L_3, \qquad C_L = \operatorname{Tr}_{Hilbert}(L_3|_{\mathrm{diag}}) \neq0.$$

Daraus folgt quellenfest:

$$L_3\neq0, \qquad L_3^\circ\neq0.$$

Der Befund betrifft jedoch den diagonalen Spurkanal. NEU-29 enthält weder eine Fourierzerlegung des Leitoperators noch eine Aussage $P^{ch}(L_3^\circ)\neq0$. Insbesondere ist der Befund verträglich mit

$$L_3^\circ = \sum_m\ell_{0,m}e_0V_m.$$

Daher:

$$\boxed{\text{NEU-29 liefert keinen geladenen Fourieranteil von }L_3^\circ.} \tag{170a.2}$$

---

## 170a.C — Audit von NEU-34

NEU-34 stellt fest, dass die nichttriviale Kopplung aus der Fourierabhängigkeit der Hochschild-Kopplung

$$-rs\log(n)\,e_{r+ns}V_{nm}$$

stammen muss. Anschließend wird modellhaft der zweite Fouriermodus $s=1$, $m=1$ fixiert, um den gerichteten Shift $r\mapsto r+n$ und den Rohoperator $\Theta_N$ zu untersuchen.

Dieser Schritt beweist:

$$\boxed{\text{Falls ein entsprechender zweiter Fouriermodus eingesetzt wird, erzeugt }\widetilde\omega_2\text{ den gerichteten Shift.}}$$

Er beweist nicht $\ell_{1,1}\neq0$ für den kanonischen Repräsentanten $L_3^\circ$. Die Konstante $\gamma_N$ wird als Normierungs- bzw. Trunkierungskonstante eingeführt, nicht quellenfest mit dem Koeffizienten $\ell_{1,1}$ identifiziert.

Daher:

$$\boxed{\text{NEU-34 ist ein Modellaudit der Kopplung, kein Fourierimport für }L_3.} \tag{170a.3}$$

---

## 170a.D — Audit von NEU-41

NEU-41 schreibt den gewählten Repräsentanten formal als

$$L_3^\circ = \sum_{s,m}\ell_{s,m}e_sV_m$$

und erhält

$$\psi_p = -\sum_{u\neq0}\sum_{s,m} a_{p,u}\ell_{s,m}\,u\,s\log(p)\, e_{u+ps}V_{pm}. \tag{41.6}$$

Diese Formel ist eine bedingte Auswertung vorhandener Koeffizienten. Im minimalen Testfall wird angenommen:

$$L_3^\circ = \ell_{s,m}e_sV_m, \qquad s\neq0.$$

Dies liefert eine nichttriviale Kopplungsformel, sofern zusätzlich $\ell_{s,m}\neq0$ und die Zielprojektion nicht verschwindet. Die Testwahl ist jedoch kein Satz, dass der kanonische Repräsentant tatsächlich einen solchen Modus besitzt.

Daher:

$$\boxed{\text{NEU-41 setzt den benötigten geladenen Modus im Testfall voraus, konstruiert oder importiert ihn aber nicht.}} \tag{170a.4}$$

---

## 170a.E — Klasseninvarianz des Fouriergrades

Die Aussage $P^{ch}(L_3)\neq0$ ist zunächst eine Eigenschaft eines gewählten Repräsentanten. Um daraus eine Eigenschaft der Kohomologieklasse $[L_3]$ zu machen, muss gezeigt werden, dass die Fourierzerlegung mit dem relevanten Differential verträglich ist.

Benötigt wird mindestens eine Unterkomplexzerlegung

$$C^\bullet = C^\bullet_0 \oplus C^\bullet_{ch}$$

mit

$$d(C^\bullet_0)\subseteq C^{\bullet+1}_0, \qquad d(C^\bullet_{ch})\subseteq C^{\bullet+1}_{ch}. \tag{170a.5}$$

Erst dann folgt eine kohomologische Zerlegung

$$H^\bullet(C) \cong H^\bullet(C_0) \oplus H^\bullet(C_{ch})$$

oder zumindest eine wohldefinierte Projektion $[L_3] \mapsto [L_3]_{ch}$.

Ohne (170a.5) kann eine Änderung $L_3\mapsto L_3+dH$ den Fourierträger verändern; dann ist weder $P^{ch}(L_3)\neq0$ noch $P^{ch}(L_3)=0$ automatisch klasseninvariant.

**Quellenstatus:** Im auditierten Quellenkegel wurde weder $dP^{ch}=P^{ch}d$ noch eine entsprechende Fouriergradzerlegung der Kohomologie von $[L_3]$ gefunden.

$$\boxed{\text{„Geladener Fourieranteil von }[L_3]\text{" ist bislang keine quellenfest definierte Klasseninvariante.}} \tag{170a.6}$$

---

## 170a.F — Drei logisch verschiedene positive Schließungen

**Weg F.1 — Repräsentantenbefund**

Eine Quelle bestimmt den tatsächlich in NEU-41 verwendeten Repräsentanten $L_3^\circ$ und zeigt $P^{ch}(L_3^\circ)\neq0$. Dies reicht unmittelbar für den Rohzeugen, auch ohne Klasseninvarianz.

**Weg F.2 — Klassenbefund**

Die Fourierzerlegung steigt auf die Kohomologie ab und es gilt $[L_3]_{ch}\neq0$. Dann besitzt jeder Repräsentant, der die Gradzerlegung respektiert, einen nichttrivialen geladenen Anteil.

**Weg F.3 — Ausschluss eines ungechargten Repräsentanten**

Es wird bewiesen:

$$[L_3] \notin \operatorname{im}\!\left(H^\bullet(C_0)\to H^\bullet(C)\