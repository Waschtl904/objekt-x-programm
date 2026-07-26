# NEU-165b — Konsistenzaudit der $R_{p,j}$ in NEU-157

> Typ: **Konsistenzaudit** zu NEU-165a [O-165a-2].  
> Erstellt: 15. Juli 2026.  
> Grundlage: Direktes Lesen von NEU-157 §157.A (vollständiger Text).

---

## DAG-Position

```
NEU-41 §3  ──►  NEU-157 §157.A  ──►  NEU-165b (dieses Blatt)
                                         └──►  NEU-165 [O-165-1..6]
                                         └──►  mögliche Rückrevision NEU-157
```

---

## 165b.A — Auditbefund: Definitionsklasse

Nach dem direkten Lesen von NEU-157 §157.A (vollständiger Wortlaut) gilt:

$$\boxed{\text{Klasse 4: }R_{p,j}\text{ sind in NEU-157 nur postuliert, nicht konstruiert.}}$$

Die einzige Stelle, an der die $R_{p,j}$ in NEU-157 auftreten, ist Gleichung (157.A.1):

$$\mathcal{E}_p^{\mathrm{lin}} := \ker(\pi_{\mathrm{prim}}) \cap \bigcap_j\ker(R_{p,j}),\tag{157.A.1}$$

mit der Begleitnotiz:

> „wobei $R_{p,j}$ die relevanten linearen Regularitätsoperatoren aus NEU-41 §3 bezeichnet.“

Diese Notiz ist ein **Verweis**, keine Definition. NEU-157 führt weder eine Formel noch eine Konstruktion für einen der $R_{p,j}$ an.

---

## 165b.B — Vollständige Einzelklassifikation

Jede Erwähnung der Symbole $R_{p,j}$ in NEU-157 wird einzeln klassifiziert:

| Stelle | Wortlaut (Kurzform) | Klasse |
|---|---|---|
| (157.A.1) | Definition von $\mathcal{E}_p^{\mathrm{lin}}$ als Kern aller $R_{p,j}$ | **Klasse 4** |
| (157.A.2) | Skalarstabilität, bedingt auf Linearität aller $R_{p,j}$ | **Klasse 4** (Bedingung referenziert, nicht bewiesen) |
| Statusmarker 157.A | „expliziter Nachweis der Homogenität aller $R_{p,j}$ ausstehend“ | explizit offen |
| 157.E Tabelle | Homogenität aller $R_{p,j}$ → NEU-159 §159.A | offen, delegiert |

**Fazit:** Kein einziger Auftritt von $R_{p,j}$ in NEU-157 ist eine explizite Definition oder Konstruktion.

---

## 165b.C — Audit der vier Bedingungen aus NEU-41 §3

NEU-41 §3 enthält vier Zulässigkeitsbedingungen für die Hebung $\widehat\varepsilon_p$:

| Bedingung | Typ | Mögliche lineare Form | Befund |
|---|---|---|---|
| (1) Primärbedingung $\pi_{\mathrm{prim}}(\widehat\varepsilon_p)=\varepsilon_p$ | **affin/linear** | $\pi_{\mathrm{prim}}(k)=0$ für Liftveränderung $k$ | linear, wohldefiniert |
| (2) Fourierladung: $\widehat\varepsilon_p=\sum_{u\neq0}a_{p,u}e_uV_p+\cdots$ | **linear** (Koeffizientenbedingung) | Funktional $\ell_{u=0}(k)=0$ | linear, aber Struktur abhängig von Präzisierung |
| (3) $Wres$-Normierung: $\operatorname{Tr}_{Wres}^{conn}(\widehat\varepsilon_p^\#\widehat\varepsilon_p)=1$ | **quadratisch** | Variation: $2\operatorname{Re}\langle\widehat\varepsilon_p,k\rangle_{Wres}=0$ nur Tangentialbedingung | **nicht linear**, nur Tangentialraum |
| (4) Hebungsunabhängigkeit (41.4): $C_pC_p^\#=C_p'C_p'^\#$ im $Wres$-Quotienten | **Operatoridentität** | keine automatische Kernform | **kein einzelner Kern** |

### Besondere Warnung: $Wres$-Normierung

Die Bedingung

$$\langle\widehat\varepsilon_p,\widehat\varepsilon_p\rangle_{Wres}=1$$

definiert eine **Quadrik**, keinen linearen Unterraum. Für eine Liftveränderung $k$ gilt

$$\langle\widehat\varepsilon_p+k,\widehat\varepsilon_p+k\rangle_{Wres} - \langle\widehat\varepsilon_p,\widehat\varepsilon_p\rangle_{Wres} = 2\operatorname{Re}\langle\widehat\varepsilon_p,k\rangle_{Wres}+\langle k,k\rangle_{Wres}.$$

Nur der erste Term ist linear in $k$, der zweite ($\|k\|^2$-Term) ist es nicht. Die exakte Erhaltung der Normierungsbedingung ist daher **keine lineare Bedingung** an $k$. Ein linearer Operator $R_{p,\mathrm{norm}}$ mit $\ker(R_{p,\mathrm{norm}})=\{k:\|\widehat\varepsilon_p+k\|_{Wres}^2=1\}$ existiert nicht.

Damit ist der Abschnitt 157.A.2 von NEU-157, der $\mathcal{E}_p^{\mathrm{lin}}$ als Kernraum beschreibt, in Bezug auf die $Wres$-Normierungsbedingung **inkonsistent**: Die Normierung kann keinen linearen Kern erzeugen.

---

## 165b.D — Entscheidung: Welcher Fall liegt vor?

Nach dem vollständigen Audit:

$$\boxed{\text{Befund C: }R_{p,j}\text{ sind in NEU-157 nicht konstruiert, sondern nur postuliert.}}$$

Zusätzlich:

$$\boxed{\text{Teilbefund D: Die }Wres\text{-Normierung ist quadratisch und erzeugt keinen linearen Kern.}}$$

Die vier Fälle aus dem Audit-Schema:

| Fall | Zutreffen? |
|---|---|
| **A:** $R_{p,j}$ exakt und linear definiert | **nein** |
| **B:** basispunktabhängige Linearisierungen | **nicht nachgewiesen** |
| **C:** nur postuliert | **ja** |
| **D:** gemischt linear/nichtlinear | **ja** (Bedingung (3) nichtlinear) |

---

## 165b.E — Statuskorrektur für NEU-157

Aus dem Audit folgt eine notwendige Statuskorrektur:

### 165b.E.1 — $\mathcal{E}_p^{\mathrm{lin}}$ als Tangentialraum

Falls die $R_{p,j}$ als Linearisierungen der Zulässigkeitsbedingungen an einem Basislift $\widehat\varepsilon_p$ interpretiert werden, dann ist

$$\mathcal{E}_p^{\mathrm{lin}} = \ker(\pi_{\mathrm{prim}}) \cap \bigcap_j\ker(R_{p,j})$$

nur der **Tangentialraum der Zulässigkeitsmenge** am gewählten Lift, nicht der Raum tatsächlich zulässiger Liftveränderungen.

In diesem Fall wäre die Benennung $\mathcal{E}_p^{\mathrm{lin}}$ zu ersetzen durch:

$$\mathcal{T}_p(\widehat\varepsilon_p) := T_{\widehat\varepsilon_p}\mathcal{M}_p^{\mathrm{adm}},$$

den Tangentialraum der Zulässigkeitsmenge $\mathcal{M}_p^{\mathrm{adm}}$ am Basispunkt.

### 165b.E.2 — Zwei mögliche Korrekturen in NEU-157

**Option I** (Linearisierungsinterpretation):
Die Formel (157.A.1) ist korrekt, wenn jedes $R_{p,j}$ ausdrücklich als Fréchet-Ableitung einer Bedingung $F_{p,j}$ am Lift $\widehat\varepsilon_p$ definiert und die basispunktabhängigkeit explizit notiert wird.

**Option II** (exakter Zulässigkeitsraum):
Falls $\mathcal{E}_p^{\mathrm{lin}}$ den exakten Raum global zulässiger Liftveränderungen beschreiben soll, müssen die $R_{p,j}$ als vom Basispunkt **unabhängige** lineare Operatoren konstruiert werden. Das erfordert, dass alle Zulässigkeitsbedingungen global homogen-linear sind. Die $Wres$-Normierung erfüllt dies **nicht**.

---

## 165b.F — Konsequenz für NEU-165

Da die $R_{p,j}$ nicht explizit konstruiert sind, können in NEU-165 weder

$$\ker(R_{p,j})$$

noch

$$I_p^{\mathrm{adm}},\quad E_p^{\mathrm{adm}}$$

als bereits definierte mathematische Objekte verwendet werden.

Der Entscheidungsrahmen von NEU-165 bleibt gültig als **bedingter Rahmen**: Sobald die $R_{p,j}$ durch eine der zwei Optionen aus 165b.E.2 konstruiert werden, greift die Fallstruktur aus NEU-165 §165.J direkt.

**Die Sperrklausel für NEU-166 ist damit verschärft:** Nicht nur der Strukturtyp eines einzelnen Operators fehlt, sondern die Operatoren selbst sind noch nicht konstruiert.

---

## 165b.G — Revidierter Aufgabenstatus

$$\boxed{\text{[O-165b-1]}\ ?[O]}$$  
In NEU-157 und NEU-159 §159.A: Konstruiere jeden $R_{p,j}$ explizit als linearen Operator mit Definitionsbereich und Zielraum (Option I oder II aus 165b.E.2).

$$\boxed{\text{[O-165b-2]}\ ?[O]}$$  
Kläre, ob die $Wres$-Normierungsbedingung aus NEU-41 §3 überhaupt Bestandteil eines $R_{p,j}$ sein soll, oder ob sie als separate nichtlineare Bedingung außerhalb von $\mathcal{E}_p^{\mathrm{lin}}$ behandelt werden muss.

$$\boxed{\text{[O-165b-3]}\ ?[O]}$$  
Falls Linearisierungsinterpretation (Option I): Prüfe Basispunktabhängigkeit und benennen $\mathcal{E}_p^{\mathrm{lin}}$ entsprechend um in $\mathcal{T}_p(\widehat\varepsilon_p)$.

$$\boxed{\text{[O-165b-4]}\ ?[O]}$$  
Nach Konstruktion: Führe Wirkungsberechnung $R_{p,j}(e_uV_p)$ gemäß NEU-165 §165.H durch.

---

## 165b.H — Gesamtbefund

$$\boxed{
\begin{array}{l}
\text{Die }R_{p,j}\text{ sind in NEU-157 nicht konstruiert.}\\
\text{Die }Wres\text{-Normierung ist quadratisch und erzeugt keinen linearen Kern.}\\
\mathcal{E}_p^{\mathrm{lin}}\text{ ist entweder ein Tangentialraum oder benötigt eine}\\
\text{explizite Konstruktion der }R_{p,j}\text{ als voraussetzungsfreie lineare Operatoren.}
\end{array}
}$$
