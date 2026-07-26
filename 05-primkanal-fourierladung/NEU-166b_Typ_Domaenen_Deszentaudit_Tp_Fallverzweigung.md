# NEU-166b — Typ-, Domänen- und Deszentaudit von $T_p$: Fallverzweigung

**Status:** Audit- und Verzweigungsblatt — commitfähig.  
**Globale Fallentscheidung (Fall 1 / 3b / 4):** gesperrt bis [O-166b-1]–[O-166b-6] geschlossen.  
**Vorgänger:** NEU-166a (Architektur), NEU-165a (Quellenregister), NEU-165b (Zulässigkeitsklassifikation), NEU-157 rev.3, NEU-41.

---

## 166b.6 — Vorläufige Fallentscheidung nach NEU-41, NEU-157 rev.3, NEU-165a und NEU-165b

### Präprojektiver Rohterm (NEU-157)

Der präprojektive Rohterm ist in NEU-157 auf den geladenen Moden explizit definiert:

$$T_p^{\mathrm{pre}}(e_u V_p)
:= -\sum_{s,m} \ell_{s,m,u} \cdot s\log(p) \cdot e_{u+ps} V_{pm},
\qquad u \neq 0.$$

### Vor-Kopplung in NEU-41

NEU-41 verwendet auf einer Fourier-geladenen Hebung $\widehat\varepsilon_p$ dieselbe modale Formel als Vor-Kopplung

$$\widetilde\omega_2\!\bigl(\widehat\varepsilon_p,\,L_3^\circ\bigr)$$

und definiert anschließend

$$\Psi_p = \Pi_{J,N}\psi_p, \qquad C_p\varepsilon_p = \Psi_p.$$

### Lokale Rohfaktorisierung (modaler Bereich)

Auf demjenigen modalen Rohbereich, auf dem $T_p^{\mathrm{pre}}$ explizit definiert ist, gilt daher formelmäßig

$$C_p\varepsilon_p \sim \Pi_{J,N}\,T_p^{\mathrm{pre}}(\widehat\varepsilon_p).$$

**Wichtig:** Dies ist eine lokale, hebungsweise Bestätigung auf dem explizit kontrollierten modalen Bereich.  
Es ist **nicht** die typkorrekte globale Identität

$$C_p \circ \pi_{\mathrm{prim}} = \Pi_{J,N} \circ G_p \quad \text{auf } D_p^{\mathrm{wit}}.$$

Eine unmittelbare Gleichheit $C_p = \Pi_{J,N} \circ T_p^{\mathrm{pre}}$ wäre **typwidrig**, da $C_p$ auf dem Primärraum und $G_p$ auf Hebungen wirkt.

### Arbeitsnotation

Für NEU-166b wird eingeführt:

$$G_p^{\mathrm{raw}} := T_p^{\mathrm{pre}}.$$

Dies ist eine **Definition in NEU-166b** und keine aus NEU-165a oder NEU-165b importierte Operatoridentität.

### Noch nicht bestätigt

Die vorstehende modale Rohfaktorisierung bestätigt noch **keinen** globalen Operator

$$G_p^{\mathrm{wit}} \longrightarrow B_3$$

und insbesondere noch **nicht** die typkorrekte globale Identität

$$C_p \circ \pi_{\mathrm{prim}} = \Pi_{J,N} \circ G_p \quad \text{auf } D_p^{\mathrm{wit}}.$$

Hierfür fehlen weiterhin:
- eine wohldefinierte Verlängerung von $T_p^{\mathrm{pre}}$ auf $D_p^{\mathrm{wit}}$,
- die Kompatibilität mit der Primärprojektion,
- die erforderliche Hebungsunabhängigkeit,
- der Quotientenabstieg bezüglich $N_p$.

---

## Klassifikation der Zulässigkeitsbedingungen (nach NEU-165b)

### Bedingung (1) — Primärbedingung

$$\pi_{\mathrm{prim}}(\widehat\varepsilon_p) = \varepsilon_p$$

ist **affin-linear**. Nach Wahl eines zulässigen Basispunkts $\widehat\varepsilon_p^{\,0}$, d. h. $\widehat\varepsilon_p = \widehat\varepsilon_p^{\,0} + k$, liefert sie die homogene Variationsbedingung

$$\pi_{\mathrm{prim}}(k) = 0.$$

Bedingung (1) besitzt daher eine **homogene Linearisierung auf dem Variationsraum**; sie ist selbst nicht linear, sondern affin.

### Bedingung (2) — Fourierladungsbedingung

Ist bei präzisierter Koeffizientendarstellung **linear**. Ihre konkrete Ausformulierung als Familie homogen-linearer Operatoren

$$L_{p,a} \longrightarrow Y_{p,a}$$

steht jedoch noch aus ([O-166b-4]).

### Bedingung (3) — $W_{\mathrm{res}}$-Normierung

**Quadratisch.** Sie kann im Allgemeinen nicht als gemeinsamer Kern linearer Operatoren dargestellt werden. Die frühere Definition

$$\ker(\pi_{\mathrm{prim}}) \cap \bigcap_j \ker(R_{p,j})$$

kann die exakte Zulässigkeitsmenge deshalb **nicht** wiedergeben und wird **verworfen**.

### Bedingung (4) — Hebungsunabhängigkeit

Eine **Operatoridentität**. Ohne zusätzliche Struktur erzeugt sie keine automatische homogene Kernbedingung.

---

## Status des transversalen Detektors

Ein eigenständiger transversaler Detektor $\Theta_p$ ist in NEU-41, NEU-157 rev.3, NEU-165a oder NEU-165b **nicht konstruiert**.

Der Kandidat

$$\Theta_p^{\mathrm{cand}} := \Pi_{J,N}$$

ist ein natürlicher Kandidat in der schwachen Kompressionslesart. Nicht nachgewiesen ist, dass er:
- zulässige und unzulässige Richtungen transversal trennt,
- auf dem relevanten Quotienten wohldefiniert ist, oder
- die für den Zeugen benötigte Nichtverschwindung erkennt.

Zusätzlich ist der mögliche Verlust der Primkanteninformation nach NEU-44 zu berücksichtigen.

---

## Revidierte Fallverzweigung

### Fall 1

Die homogen-linearen Bedingungen $L_{p,a}$ lassen sich aus der Primärvariation und der Fourierladungsbedingung konstruieren.

**Status:** möglich; $[\text{O-157-R1/R2}]$ und $[\text{O-165b-1}]$ offen.

### Fall 2

Die frühere Familie $R_{p,j}$ und ein zweiter quellenfest definierter Operator liegen beide vor.

$$\boxed{\text{ausgeschlossen.}}$$

Die Operatoren $R_{p,j}$ sind nicht konstruiert.

### Fall 3a

Der Rohoperator wird auf dem expliziten modalen Bereich durch

$$G_p^{\mathrm{raw}} := T_p^{\mathrm{pre}}$$

gegeben und anschließend durch $\Pi_{J,N}$ komprimiert.

$$\boxed{\text{lokal und formelmäßig auf dem kontrollierten modalen Bereich bestätigt.}}$$

**Präzisierung:** „Fall 3a ist auf dem explizit definierten modalen Rohbereich formelmäßig bestätigt." Für eine beliebige Fourier-geladene Hebung gilt die Aussage erst, nachdem gezeigt wurde, dass ihre vollständige Entwicklung im Definitionsbereich von $T_p^{\mathrm{pre}}$ liegt und die Summe wohldefiniert ist.

### Fall 3b

Es existiert ein globaler Operator $G_p^{\mathrm{wit}} \to B_3$ zusammen mit einem hinreichenden transversalen Detektor $\Theta_p$, und die Konstruktion steigt auf den Quotienten ab.

**Status:** offen.

### Fall 4

Weder eine kanonische globale Verlängerung noch eine hinreichende Familie $L_{p,a}$ oder ein Deszendenznachweis ist verfügbar.

**Status:** weiterhin möglich.

---

## Gesamtbefund

$$\boxed{\text{Fall 2 ist ausgeschlossen.}}$$

$$\boxed{\text{Fall 3a ist lokal bzw. modenweise formelmäßig bestätigt.}}$$

$$\boxed{\text{Die globale Entscheidung zwischen Fall 1, Fall 3b und Fall 4 bleibt offen.}}$$

---

## Offene Punkte

**[O-166b-1]** Verlängerung von $T_p^{\mathrm{pre}}$ auf $D_p^{\mathrm{wit}}$ als globaler Operator $G_p^{\mathrm{wit}} \to B_3$.

**[O-166b-2]** Nachweis der typkorrekten Faktorisierung
$$C_p \circ \pi_{\mathrm{prim}} = \Pi_{J,N} \circ G_p \quad \text{auf } D_p^{\mathrm{wit}}.$$

**[O-166b-3]** Nachweis des Quotientenabstiegs
$$D_p^{\mathrm{wit}} \cap N_p \subseteq \ker\!\bigl(\Pi_{J,N} \circ G_p\bigr).$$

**[O-166b-4]** Konstruktion der konkret definierten homogen-linearen Operatoren $L_{p,a}$ aus der linearisierten Primärbedingung und der Fourierladungsbedingung.

**[O-166b-5]** Entscheidung, ob $\Pi_{J,N}$ lediglich eine Kompression oder ein hinreichender transversaler und quotientenverträglicher Detektor ist.

**[O-166b-6]** Bestimmung des vollständigen Definitionsbereichs von $T_p^{\mathrm{pre}}$, einschließlich Konvergenz bzw. Endlichkeit der modalen Summe für allgemeine Elemente von $D_p^{\mathrm{wit}}$.

---

## Commit-Status

NEU-166b kann in dieser Form als **Audit- und Verzweigungsblatt committed werden**.  
Der Commit beansprucht keine globale Entscheidung zwischen Fall 1, Fall 3b und Fall 4.

**Gesperrt** bleibt lediglich ein späterer globaler Entscheidungssatz, bis insbesondere die Struktur von $\Pi_{J,N}$, die Operatoren $L_{p,a}$ und der Quotientenabstieg geklärt sind.

---

## Referenzverknüpfungen im DAG

| Blatt | Abhängigkeit |
|---|---|
| NEU-166a | Architekturvorlage (Abschnitte 166a.A–H) |
| NEU-165a | Quellenregister $R_{p,j}$; [O-165a-2] offen |
| NEU-165b | Zulässigkeitsklassifikation (Bed. 1–4) |
| NEU-157 rev.3 | Definition $T_p^{\mathrm{pre}}$; Verortung §157.B.1 vs. §157.H zu prüfen |
| NEU-41 | Vor-Kopplung $\widetilde\omega_2$, Definition $C_p$, $\Psi_p$ |
| NEU-44 | Primkanteninformationsverlust bei $\Pi_{J,N}$ |
