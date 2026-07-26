# NEU-170 — Gewichteter Träger von $L_3^\circ$ — Quellenimport für [O-169-1]

**Status:** Quellenaudit abgeschlossen. Befund B.3.  
**Vorgänger:** NEU-169 → NEU-170.  
**Gesperrt:** $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$ und algebraischer Rohzeuge bis zum positiven Befund in NEU-170a.  
**Nächster Knoten:** NEU-170a — Fouriergrad der ursprünglichen Klasse $[L_3]$.

---

## 170.A — Entscheidungsfrage

Zu entscheiden ist, ob die bisherige Quellenkette einen gewichteten Fourierkoeffizienten

$$\exists(s_0,m_0): s_0\ell_{s_0,m_0}\neq0$$

für

$$L_3^\circ = \sum_{s,m}\ell_{s,m}e_sV_m$$

liefert. Äquivalent ist zu prüfen:

$$\operatorname{supp}^{\times}(L_3^\circ) := \{(s,m): s\ell_{s,m}\neq0\} \neq\varnothing.$$

Dieser Befund ist nach NEU-169 notwendig, um aus der kollisionsfreien Einzelmodenstruktur auf $T_p^{pre}(e_uV_p)\neq0$ für $u\neq0$ zu schließen.

---

## 170.B — Audit von NEU-41

NEU-41 §4 schreibt $L_3^\circ$ formal als

$$\sum_{s,m}\ell_{s,m}e_sV_m$$

und definiert mit Gleichung (41.6):

$$\psi_p = -\sum_{u\neq0}\sum_{s,m} a_{p,u}\ell_{s,m}\,u\,s\log(p)\, e_{u+ps}V_{pm}. \tag{41.6}$$

Diese Formel beschreibt die Kopplung für beliebige vorhandene Koeffizienten. Sie beweist nicht, dass der konkrete Operator $L_3^\circ$ mindestens einen Koeffizienten mit $s\neq0$ besitzt.

NEU-41 verwendet im minimalen nichttrivialen Testfall eine Spezialisierung

$$L_3^\circ = \ell_{s,m}e_sV_m, \qquad s\neq0.$$

Dieser Abschnitt ist eine **bedingte Modellrechnung**:

$$s\neq0,\ \ell_{s,m}\neq0 \quad\Longrightarrow\quad \text{nichttrivialer Rohterm.}$$

Er ist kein Existenzbeweis für ein solches Paar $(s,m)$ im kanonischen $L_3^\circ$. NEU-41 setzt den gewählen gewichteten Modus im minimalen Test voraus, importiert oder konstruiert ihn aber nicht quellenfest.

$$\boxed{\text{NEU-41 liefert weder Befund B.1 noch B.2.}}$$

---

## 170.C — Audit der Normierung von $L_3^\circ$

Aus NEU-20/NEU-28 und dem Import in NEU-29 ist gesichert:

$$C_L = \operatorname{Tr}_{Hilbert}(L_3|_{\mathrm{diag}}) \neq0, \qquad L_3^\circ = C_L^{-1}L_3.$$

Daraus folgt:

$$L_3^\circ \neq 0.$$

Dieser Nichtverschwindensbefund kontrolliert jedoch **nicht** den Fourierindex. Insbesondere ist logisch möglich, dass

$$\ell_{s,m} = 0 \qquad\text{für alle }s\neq0,$$

während ein nichtverschwindender Anteil mit $s=0$ die diagonale Spur erzeugt. Da die lokale Kopplungsformel den Faktor $s$ enthält,

$$-u\,s\log(p)\,e_{u+ps}V_{pm},$$

tragen solche $s=0$-Terme nicht zu $T_p^{pre}$ bei. Somit impliziert $C_L\neq0$ nicht $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$.

$$\boxed{C_L\neq0 \text{ ist für [O-169-1] nicht ausreichend.}}$$

---

## 170.D — Audit von NEU-34

NEU-34 fixiert für die Analyse des rohen Fourier-Shifts modellhaft $s=1$, $m=1$ und definiert daraus einen gewichteten Shift:

$$\Theta_N E_{r,n} = -\gamma_N r\log(n)\, E_{r+n,n}.$$

Das Blatt identifiziert jedoch nicht $\gamma_N = \ell_{1,1}$ für den kanonischen Operator $L_3^\circ$ und beweist nicht $\ell_{1,1}\neq0$. Die Fixierung des Modus $(1,1)$ ist eine **Modellreduktion** der allgemeinen $\widetilde{\omega}_2$-Formel, kein quellenfester Koeffizientenimport.

$$\boxed{\text{NEU-34 liefert keinen quellenfesten B.1-Import.}}$$

---

## 170.E — Entscheidung nach Befundtypen

| Befundtyp | Inhalt | Status |
|---|---|---|
| B.1 | $\exists(s_0,m_0): s_0\ell_{s_0,m_0}\neq0$ explizit | $\boxed{\text{nicht gefunden}}$ |
| B.2 | Struktureller Satz: $L_3^\circ$ besitzt nichtkonstanten Fourieranteil | $\boxed{\text{nicht gefunden}}$ |
| B.3 | $L_3^\circ\neq0$ bzw. $C_L\neq0$, ohne $s=0$-Ausschluss | $\boxed{\checkmark[M]}$ |

---

## 170.F — Gesamtbefund

Die gegenwärtige Quellenkette beweist nicht $\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing$.

$$\boxed{[O\text{-}169\text{-}1] \quad ?[O].}$$

Ebenso bleibt der daraus folgende Einzelmoden-Rohzeuge bedingt:

$$\boxed{\operatorname{supp}^{\times}(L_3^\circ)\neq\varnothing \Longrightarrow T_p^{pre}(e_uV_p)\neq0,}$$

aber die Voraussetzung ist noch nicht quellenfest geschlossen.

---

## 170.G — Neuer atomarer Folgeauftrag

Der nächste Quellenauftrag ist nicht, NEU-41 erneut zu lesen, sondern die ursprüngliche Konstruktion der Klasse $[L_3]$ bzw. ihres Repräsentanten $L_3$ zu auditieren. Zu entscheiden ist:

$$\boxed{\text{Erzwingt die Definition oder Kohomologieklasse }[L_3]\text{ einen Anteil mit }s\neq0?}$$

Mögliche positive Schließungen wären:
- ein expliziter Koeffizient $\ell_{s_0,m_0}\neq0$, $s_0\neq0$;
- ein Beweis $L_3^\circ \notin \overline{\operatorname{span}}\{e_0V_m\}$;
- ein Kohomologie- oder Reinheitsargument, wonach ein rein ungechargter Repräsentant die Klasse $[L_3]$ nicht darstellen kann.

Bis zu einem solchen Befund bleibt der algebraische Rohzeuge gesperrt.

$$\boxed{\text{NEU-170a — Fouriergrad der ursprünglichen Klasse }[L_3].}$$

NEU-171 zur Normierungsquadrik wird erst dann zum kritischen Pfad, wenn NEU-170a einen positiven B.1- oder B.2-Befund liefert.

---

## Referenzverknüpfungen im DAG

| Blatt | Abhängigkeit |
|---|---|
| NEU-169 [O-169-1] | Primärer Auftrag dieses Blatts |
| NEU-41 Gl. (41.6) | Auditiert: kein B.1/B.2-Befund |
| NEU-20/28/29 | $C_L\neq0$ gesichert; für [O-169-1] nicht ausreichend |
| NEU-34 | Modellreduktion; kein quellenfester Koeffizientenimport |
| NEU-170a (nächster Knoten) | Fouriergrad von $[L_3]$ — [O-170-1/2/3] |
| NEU-171 (gesperrt bis NEU-170a) | Normierungsgeometrie Einzelmodus |
