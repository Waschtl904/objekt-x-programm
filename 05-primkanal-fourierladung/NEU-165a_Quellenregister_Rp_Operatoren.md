# NEU-165a — Quellenregister der $R_{p,j}$-Operatoren

> Typ: **Quellenprotokoll** zu NEU-165 [O-165-1].  
> Erstellt: 15. Juli 2026.  
> Revision: Direkter Import aus NEU-41 und Namenskonventionsdiagnose.  
> Zweck: Vor jeder Wirkungsberechnung ist für jeden Operator $R_{p,j}$ die exakte Definitionsquelle, der Definitionsbereich und der Zielraum festzuhalten. Der direkte Abgleich mit NEU-41 liefert bereits einen expliziten, aber zunächst nur verwandten Operator $C_p$; zugleich bleibt die Brücke zu den in NEU-157 genannten $R_{p,j}$ offen.

---

## DAG-Position

```
NEU-41 §1/§3/§4  ──►  NEU-157 (157.A.1)  ──►  NEU-165a  ──►  NEU-165 [O-165-2]
                                                        └──►  NEU-165 [O-165-3..6]
```

---

## 165a.A — Gesicherter Befund aus NEU-157

Aus NEU-157 §157.A.1, Gleichung (157.A.1), ist gesichert:

$$\mathcal{E}_p^{\mathrm{lin}} := \ker(\pi_{\mathrm{prim}}) \cap \bigcap_j \ker(R_{p,j}),\tag{157.A.1}$$

wobei die $R_{p,j}$ als **„die relevanten linearen Regularitätsoperatoren aus NEU-41 §3“** bezeichnet werden.

Dieser Satz ist als Verweisformel gesichert; offen bleibt jedoch, **wo** in NEU-41 die Familie $R_{p,j}$ tatsächlich benannt oder explizit definiert wird.

**Quellenstatus:**

| Aussage | Quelle | Status |
|---|---|---|
| Existenz und Bezeichnung der $R_{p,j}$ in NEU-157 | NEU-157 (157.A.1), Rückverw. auf NEU-41 §3 | ✅[M] |
| Wörtliche Definition einer Familie $R_{p,j}$ in NEU-41 | direkter Leseabgleich NEU-41 | ✗[M] |
| Explizite Formel $R_{p,j}(e_uV_p)$ | **ausstehend** | ❓[O] |
| Brücke zwischen Bedingungen aus NEU-41 §3 und $R_{p,j}$ aus NEU-157 | **ausstehend** | ❓[O] |

---

## 165a.B.0 — Ergebnis des direkten Leseauftrags

Der direkte Abgleich mit NEU-41 ergibt:

- NEU-41 definiert **keinen** Operator mit der Bezeichnung $R_{p,j}$.
- Der dort ausdrücklich definierte Operator ist der Kopplungsoperator
  $$C_p,$$
  der aus der mit festem zweitem Argument ausgewerteten Hochschildform $\widetilde\omega_2$ und der anschließenden Projektion $\Pi_{J,N}$ hervorgeht.

Damit ist die bisherige Quellenangabe

$$\text{„Die }R_{p,j}\text{ sind in NEU-41 §3 definiert“}$$

in dieser **wörtlichen Form nicht bestätigt**.

NEU-41 §3 enthält vielmehr die **inhaltlichen Zulässigkeits- beziehungsweise Regularitätsbedingungen** der Hebung, aus denen die später in NEU-157 verwendeten $R_{p,j}$ möglicherweise gewonnen, abstrahiert oder linearisiert wurden.

Es ist daher künftig zu unterscheiden zwischen

$$\boxed{\text{Ursprung der Nebenbedingungen: NEU-41 §3}}$$

und

$$\boxed{\text{Definition beziehungsweise Benennung der }R_{p,j}:\ \text{noch zu identifizieren}.}$$

---

## 165a.B.1 — Explizit definierter Kopplungsoperator $C_p$

NEU-41 §1 enthält die Formel

$$\widetilde\omega_2(e_rV_n,e_sV_m)=-rs\log(n)\,e_{r+ns}V_{nm}.\tag{41.1}$$

Für

$$L_3^\circ=\sum_{s,m}\ell_{s,m}e_sV_m$$

und den Eingangsvektor

$$e_uV_p,\qquad u\neq 0,$$

ergibt sich gemäß NEU-41 §4:

$$C_p(e_uV_p)=\Pi_{J,N}\left(-\sum_{s,m}\ell_{s,m}\,u\,s\,\log(p)\,e_{u+ps}V_{pm}\right).\tag{165a.1}$$

Da die Terme mit $s=0$ nach (41.1) verschwinden, kann äquivalent über $s\neq0$ summiert werden.

---

## 165a.B.2 — Operatorstrukturelle Form

Definiere formal den Indexoperator

$$D_p(e_uV_p):=u\,e_uV_p$$

und für jedes Paar $(s,m)$ den Verschiebungsoperator

$$W_{p;s,m}(e_uV_p):=e_{u+ps}V_{pm}.$$

Dann besitzt $C_p$ formal die Darstellung

$$C_p=-\log(p)\,\Pi_{J,N}\sum_{s,m}s\,\ell_{s,m}\,W_{p;s,m}D_p.\tag{165a.2}$$

Damit ist $C_p$ im Allgemeinen eine

$$\boxed{\text{Summe gewichteter Verschiebungsoperatoren}.}$$

Die Bezeichnung „diagonal im Eingangsindex $u$“ ist zu vermeiden. Zwar tritt $u$ als multiplikativer Faktor auf, zugleich wird aber der Ausgangsindex durch

$$u\longmapsto u+ps$$

verschoben. Der Zielvektor hängt somit wesentlich von $u$ ab.

---

## 165a.B.3 — Rohspaltenträger vor der Projektion

Vor Anwendung von $\Pi_{J,N}$ lautet der Rohspaltenträger:

$$S_p^{\mathrm{raw}}(u):=\{(u+ps,pm): s\neq0,\ \ell_{s,m}\neq0\}.\tag{165a.3}$$

Für festes $u$ ist die Abbildung

$$ (s,m)\longmapsto(u+ps,pm) $$

auf der formal bezeichneten Basis injektiv, sofern verschiedene Paare $(r,n)$ tatsächlich verschiedene Basisvektoren $e_rV_n$ bestimmen. Daher können vor der Projektion keine zwei verschiedenen Paare $(s,m)$ innerhalb derselben Spalte denselben Zielbasisvektor erzeugen.

---

## 165a.B.4 — Tatsächlicher Spaltenträger nach der Projektion

Der tatsächliche Spaltenträger ist nicht ohne Kenntnis von $\Pi_{J,N}$ mit $S_p^{\mathrm{raw}}(u)$ identisch.

Falls $\Pi_{J,N}$ eine koordinatenweise Projektion auf eine Teilmenge der Basisvektoren ist, gilt:

$$S_p(u)=\{(u+ps,pm)\in S_p^{\mathrm{raw}}(u): \Pi_{J,N}(e_{u+ps}V_{pm})\neq0\}.\tag{165a.4}$$

Falls $\Pi_{J,N}$ Basisvektoren mischt, muss der tatsächliche Matrixeintrag stattdessen aus

$$r_p((a,b),u)=-u\log(p)\sum_{s,m}s\,\ell_{s,m}\,\big\langle e_aV_b,\Pi_{J,N}(e_{u+ps}V_{pm})\big\rangle\tag{165a.5}$$

bestimmt werden. Dann ist

$$S_p(u)=\{(a,b):r_p((a,b),u)\neq0\}.$$

Ohne explizite Struktur der Projektion darf daher nur der **Rohspaltenträger** als gesichert angegeben werden.

---

## 165a.B.5 — Strukturklassifikation

### Allgemeiner Fall

Enthält $L_3^\circ$ mehrere nichtverschwindende Koeffizienten $\ell_{s,m}$, so erzeugt ein einzelner Eingangsvektor im Allgemeinen mehrere verschobene Zielkomponenten. Damit liegt vor der Projektion eine echte Mehrtermstruktur vor:

$$\boxed{\text{gewichtete Shiftmischung}.}$$

Sie ist weder diagonal noch allgemein projektiv beziehungsweise rang eins.

### Eintermfall

Sei

$$L_3^\circ=\ell_{s_0,m_0}e_{s_0}V_{m_0},\qquad s_0\neq0.$$

Dann gilt

$$C_p(e_uV_p)=\kappa_{p,u}\,\Pi_{J,N}(e_{u+ps_0}V_{pm_0}),\tag{165a.6}$$

mit

$$\kappa_{p,u}=-u\,s_0\log(p)\,\ell_{s_0,m_0}.$$

Dies ist auf dem von den $e_uV_p$ erzeugten Raum ein

$$\boxed{\text{gewichteter partieller Verschiebungsoperator}}$$

beziehungsweise eine einspaltig besetzte Matrixstruktur vor der Projektion.

Der Operator ist **nicht** allein deshalb rang eins, weil jede einzelne Spalte nur einen Zielbasisvektor enthält. Rang eins wäre erst dann bewiesen, wenn

$$\dim\operatorname{span}\{\Pi_{J,N}(e_{u+ps_0}V_{pm_0}):u\in I_p\}\leq1.\tag{165a.7}$$

Ohne diese Kollinearitätsaussage ist die Bezeichnung „rang-eins-artig“ zu vermeiden.

---

## 165a.B.6 — Mögliche Überlappungen verschiedener Eingangsspalten

Auch wenn die Zielterme innerhalb einer festen Spalte vor der Projektion verschieden sind, können die Zielträger verschiedener Eingangsindizes überlappen. Eine Überlappung ist möglich, wenn

$$(u+ps,pm)=(u'+ps',pm').$$

Dies verlangt

$$m=m'$$

und

$$u'-u=p(s-s').$$

Daher sind Auslöschungen zwischen verschiedenen Eingangsvektoren nicht allein durch die Rohspaltenform ausgeschlossen. Die Formel für $C_p$ beweist somit noch **keine** gemeinsame Diagonalität im Sinn von NEU-165.G.

---

## 165a.B.7 — Linearitätsstatus von $C_p$

Sofern $\widetilde\omega_2$ im ersten Argument linear ist, $L_3^\circ$ festgehalten wird und $\Pi_{J,N}$ linear ist, ist

$$x\longmapsto \Pi_{J,N}(\widetilde\omega_2(x,L_3^\circ))$$

ein linearer Operator.

Dies schließt jedoch **nicht** die offene Linearitätsfrage der $R_{p,j}$, weil gegenwärtig nicht bewiesen ist, dass die $R_{p,j}$ mit $C_p$, seinen Komponenten oder linearen Funktionalen von $C_p$ identisch sind.

---

## 165a.C — Namenskonventionsdiagnose

Der Quellenabgleich führt zu folgender korrigierter Tabelle:

| Objekt | Direkte Quelle | Befund |
|---|---|---|
| $\widetilde\omega_2$ | NEU-41 §1 | explizite bilineare Formel |
| $C_p$ | NEU-41 §4 | expliziter projizierter Kopplungsoperator |
| Zulässigkeitsbedingungen der Hebung | NEU-41 §3 | inhaltliche Bedingungen vorhanden |
| $R_{p,j}$ als benannte Operatorfamilie | nicht in NEU-41 gefunden | Brücke zu NEU-157 offen |
| abstrakte Verwendung der $R_{p,j}$ | NEU-157 §157.A | direkt zu überprüfen |

Die Tabelle 165a.B für die $R_{p,j}$ darf daher **nicht** durch eine Zeile ersetzt werden, in der $C_p$ stillschweigend als eines der $R_{p,j}$ behandelt wird. Stattdessen ist $C_p$ als verwandter, explizit importierter Operator in einer **separaten Tabelle** zu führen.

---

## 165a.D — Offene Brücke zwischen NEU-41 und NEU-157

Der nächste Leseauftrag lautet nicht mehr lediglich:

$$\text{„Lies NEU-41 §3.“}$$

Vielmehr ist direkt in NEU-157 §157.A festzustellen:

1. Wo werden die Symbole $R_{p,j}$ erstmals eingeführt?
2. Werden sie dort explizit definiert oder nur vorausgesetzt?
3. Entstehen sie aus Funktionalen der Form
   $$F_{p,j}(\widehat\varepsilon_p)=0?$$
4. Wird eine lineare Übergangsformel
   $$F_{p,j}(\widehat\varepsilon_p+k)-F_{p,j}(\widehat\varepsilon_p)=R_{p,j}(k)\tag{165a.8}$$
   bewiesen?
5. Handelt es sich um exakte lineare Differenzen, um Ableitungen beziehungsweise Linearisierungen oder lediglich um abstrakte Nebenbedingungen?

Insbesondere darf aus einer Normierungsbedingung nicht automatisch ein linearer Operator gewonnen werden. Eine Bedingung der Form

$$\|x\|^2=c$$

ist quadratisch. Ihre Nullstellenmenge oder ihre Variation ist ohne zusätzliche Argumente kein Kern eines linearen Operators.

---

## 165a.E — Revidierter Aufgabenstatus

Der bisherige Auftrag [O-165a-1] ist in drei Teilbefunde zu zerlegen.

$$\boxed{\text{[O-165a-1a]}\ \checkmark[M]}$$  
Direkter Import von $C_p$: Die Formel für $C_p(e_uV_p)$ wurde aus NEU-41 importiert.

$$\boxed{\text{[O-165a-1b]}\ \checkmark[M]\ \text{— negativer Befund}}$$  
In NEU-41 wurde keine ausdrücklich so bezeichnete Operatorfamilie $R_{p,j}$ gefunden.

$$\boxed{\text{[O-165a-2]}\ ?[O]}$$  
Es ist zu bestimmen, wie die Bedingungen aus NEU-41 §3 in NEU-157 zu den Operatoren $R_{p,j}$ werden.

$$\boxed{\text{[O-165a-3]}\ ?[O]}$$  
Es ist zu prüfen, ob $\Pi_{J,N}$
- eine koordinatenweise Basisprojektion ist,
- Basisvektoren mischt,
- oder zusätzliche Identifikationen erzeugt.

Erst danach kann der tatsächliche Spaltenträger von $C_p$ berechnet werden.

---

## 165a.F — Konsequenz für NEU-166

Die Sperrklausel bleibt bestehen. Der Import von $C_p$ genügt noch nicht zur Eröffnung eines Kernblatts über die $R_{p,j}$, weil die Identifikation

$$R_{p,j}\stackrel{?}{=}\text{Komponente, Funktional oder Linearisierung von }C_p$$

weiter offen ist.

Ein NEU-166 darf erst eröffnet werden, wenn mindestens einer der folgenden Befunde vorliegt:

- ein **explizit definierter Operator**,
- eine **explizit bewiesene homogene Variation einer Bedingung**,
- oder eine Darstellung der Form
  $$R_{p,j}=\Lambda_{p,j}\circ C_p$$
  für ein ausdrücklich definiertes lineares Funktional beziehungsweise eine ausdrücklich definierte Projektion $\Lambda_{p,j}$.

---

## 165a.G — Aktueller Gesamtbefund

Der direkte Import aus NEU-41 liefert einen echten mathematischen Fortschritt:

$$\boxed{C_p\text{ ist eine projizierte Summe gewichteter Verschiebungen.}}$$

Er liefert aber **noch keinen** Import der $R_{p,j}$.

Der neue Engpass lautet daher:

$$\boxed{\text{Wie werden die Zulässigkeitsbedingungen aus NEU-41 §3 in NEU-157 zu den }R_{p,j}\text{?}}$$

Bis diese Brücke identifiziert ist, bleiben

$$I_p^{\mathrm{adm}}\qquad\text{und}\qquad E_p^{\mathrm{adm}}$$

hinsichtlich der $R_{p,j}$-Nebenbedingungen unberechnet.
