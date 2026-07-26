# NEU-167 — Lineare Kernbedingungen versus offene Fourierladungsbedingung

**Status:** Entscheidungsblatt zu [O-166b-4].  
**Vorgänger:** NEU-166b (offener Punkt [O-166b-4]), NEU-165b (Zulässigkeitsklassifikation), NEU-157 rev.3 §157.H Gl. (157.B.1), NEU-41.  
**Querverweis NEU-157:** Formel steht in Abschnitt §157.H „Präprojektive Nichtverschwindung", trägt Gleichungsnummer (157.B.1). Künftige Importe nennen beide Angaben.

---

## Ausgangslage

[O-166b-4] fragte, ob sich aus den Bedingungen (1) und (2) aus NEU-41 §3 eine Familie homogen-linearer Operatoren

$$L_{p,a}: D_p^{\mathrm{wit}} \longrightarrow Y_{p,a}, \qquad L_{p,a}(k)=0,$$

konstruieren lässt. Die folgende Analyse zeigt, dass die Antwort **nein** lautet — jedenfalls nicht in der bisher angenommenen direkten Form.

---

## 167.A — Primärbedingung erzeugt keinen neuen Operator

NEU-157 definiert

$$K_p := \ker(\pi_{\mathrm{prim}}).$$

Für Variationen $k \in K_p$ gilt $\pi_{\mathrm{prim}}(k) = 0$ bereits durch die Wahl des Grundraums. Der formal notierbare Operator

$$L_{p,\mathrm{prim}} := \pi_{\mathrm{prim}}\big|_{K_p}$$

ist auf $K_p$ identisch null. Er liefert keinen neuen, nichttrivialen Nebenbedingungsoperator.

$$\boxed{\text{Aus Bedingung (1) entsteht auf }K_p\text{ kein neuer nichttrivialer }L_{p,a}.}$$

---

## 167.B — Fourierladungsbedingung ist keine Kernbedingung

NEU-41 verlangt nichtverschwindende Fourierladung:

$$\widehat\varepsilon_p = \sum_{u \neq 0} a_{p,u}\,e_u V_p + \cdots, \qquad (a_{p,u})_{u \neq 0} \neq 0.$$

Die Koeffizientenabbildung

$$P_p^{\mathrm{ch}}: \widehat\varepsilon_p \longmapsto (a_{p,u})_{u \neq 0}$$

ist **linear**. Die eigentliche Zulässigkeitsbedingung lautet jedoch

$$P_p^{\mathrm{ch}}(\widehat\varepsilon_p) \neq 0,$$

also

$$\widehat\varepsilon_p \notin \ker(P_p^{\mathrm{ch}}).$$

Dies ist das **Komplement** eines linearen Kerns — keine Kernbedingung $L_{p,a}(k) = 0$.

$$\boxed{\text{Bedingung (2) liefert einen linearen Ladungsoperator, aber die geforderte Nichtverschwindung ist keine Kernbedingung.}}$$

### Abgrenzung

Falls zusätzlich verlangt wird, dass ungeladene Komponenten verschwinden, wäre

$$P_p^{(0)}(\widehat\varepsilon_p) = 0$$

eine echte homogen-lineare Bedingung. NEU-41 formuliert jedoch primär die Nichtverschwindensforderung, nicht eine Ausschlussbedingung dieser Art.

---

## 167.C — Strukturbefund: Was Bedingungen (1) und (2) zusammen erzeugen

Bedingungen (1) und (2) erzeugen allein **keine** nichttriviale Familie $\{L_{p,a}(\cdot) = 0\}_a$ im Sinne von [O-166b-4]. Sie erzeugen stattdessen eine Kombination aus:

1. **Grundraumfestlegung** — $K_p = \ker(\pi_{\mathrm{prim}})$ als Variationsraum,
2. **eventuellen linearen Ausschlussbedingungen** — sofern NEU-41 eine $P_p^{(0)}$-Bedingung enthält (noch zu prüfen: [O-167-1]),
3. **einer Nichtverschwindensbedingung** — $\widehat\varepsilon_p \notin \ker(P_p^{\mathrm{ch}})$, die als offene Zulassungsmenge, nicht als Kerngleichung, formuliert ist.

---

## 167.D — Konsequenz für Fall 1 der Fallverzweigung (NEU-166b)

Fall 1 in NEU-166b lautete:

> Die homogen-linearen Bedingungen $L_{p,a}$ lassen sich aus der Primärvariation und der Fourierladungsbedingung konstruieren.

Nach dem vorliegenden Befund ist Fall 1 **in seiner bisherigen Form leer oder nur formal**:

- Bedingung (1) liefert auf $K_p$ keinen nichttrivialen $L_{p,a}$.
- Bedingung (2) liefert zwar $P_p^{\mathrm{ch}}$ als linearen Operator, aber die Zulässigkeitsbedingung ist eine Nichtverschwindensforderung, kein Kern.

Fall 1 kann nur dann nicht-leer sein, wenn:
- NEU-41 zusätzliche lineare Ausschlussbedingungen enthält (z. B. $P_p^{(0)} = 0$), oder
- eine andere Quelle (NEU-157, NEU-44) lineare Kernbedingungen über $K_p$ beisteuert.

Beides ist derzeit offen ([O-167-1], [O-167-2]).

$$\boxed{\text{Fall 1 ist in der bisherigen Form nicht durch Bedingungen (1) und (2) allein befüllbar.}}$$

NEU-166b muss dadurch **nicht korrigiert** werden: Dort steht zu Recht, dass [O-166b-4] offen ist. Der Befund hier präzisiert nur, warum die Schließung von [O-166b-4] nichttrivial ist.

---

## Offene Punkte

**[O-167-1]** Enthält NEU-41 eine lineare Ausschlussbedingung $P_p^{(0)}(\widehat\varepsilon_p) = 0$ (Verschwinden ungeladener Komponenten), oder beschränkt sich NEU-41 auf die Nichtverschwindensforderung $P_p^{\mathrm{ch}} \neq 0$?

**[O-167-2]** Liefern NEU-157 §157.H Gl. (157.B.1) oder NEU-44 zusätzliche lineare Kernbedingungen über $K_p$, die Fall 1 nicht-leer machen könnten?

**[O-167-3]** Ist die Zulässigkeitsmenge $D_p^{\mathrm{adm}}$ als offene Teilmenge von $K_p$ (durch $\widehat\varepsilon_p \notin \ker(P_p^{\mathrm{ch}})$) ausreichend für die Zwecke von NEU-166b Fall 3a, oder wird eine Kerndarstellung zwingend benötigt?

---

## Commit-Status

NEU-167 ist als **Entscheidungsblatt zu [O-166b-4]** committed.  
Der Befund zu Fall 1 ist vorläufig; endgültige Entscheidung abhängig von [O-167-1] und [O-167-2].

---

## Referenzverknüpfungen im DAG

| Blatt | Abhängigkeit |
|---|---|
| NEU-166b [O-166b-4] | Primärer Auftrag dieses Blatts |
| NEU-157 rev.3 §157.H Gl. (157.B.1) | Definition $T_p^{\mathrm{pre}}$, Grundraumfestlegung |
| NEU-165b | Klassifikation Bedingungen (1)–(4) |
| NEU-41 §3 | Quelle der Fourierladungs- und Primärbedingung |
| NEU-44 | Potenzielle weitere Kernbedingungen |
