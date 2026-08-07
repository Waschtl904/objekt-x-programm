# NEU-250e — Faltungszerlegung des Hebungskerns und L₃°-Zeugendesiderat

**Knoten:** \([O\text{-}221\text{-}1c1a0\text{-C1a/10}]\)

**Status:** \(\checkmark[M]_{\mathrm{part}}\)

**Datum:** 7. August 2026

> **Vorgänger:** NEU-250d — Der Hebungskern
> \[\ker B_p^{(1)} = \Bigl\{(a_u) : \sum_{u+ps=R}a_u\,u\,s\,\ell_{s,1}=0\ \forall R\Bigr\}\]
> wurde definiert. Offener Knoten \(/10\): \(\Delta_p^{\mathrm{adm}} \subseteq \ker B_p^{(1)}\)?  
> Die vorliegende Datei berechnet die Struktur von \(\ker B_p^{(1)}\) vollständig
> algebraisch — bedingt durch einen einzigen Zeugen \(\ell_{s_0,1} \neq 0\).

**Quellen:** NEU-250d (Definition \(\ker B_p^{(1)}\), Formel für \(P_1\widetilde T_p^{\mathrm{raw}}\)),
NEU-020 (Zeuge für \([L_3]\neq 0\) im \(m=6\)-Sektor, **nicht** im \(m=1\)-Sektor).

---

## 1. Restklassenzerlegung und Faltungsstruktur

### 1.1 Substitution

Schreibe \(R = r + pn\) mit \(r \in \mathbb{Z}/p\mathbb{Z}\), \(n \in \mathbb{Z}\),
und setze \(u = r + pk\), \(s = n-k\). Dann läuft die Summe

\[
(B_p^{(1)}a)_R = \sum_{u+ps=R} a_u\,u\,s\,\ell_{s,1}
\]

über \(k \in \mathbb{Z}\) und nimmt die Form an:

\[
(B_p^{(1)}a)_{r+pn}
= \sum_{k\in\mathbb{Z}} \underbrace{(r+pk)\,a_{r+pk}}_{=:\,x_k^{(r)}}
\cdot\underbrace{(n-k)\,\ell_{n-k,1}}_{=:\,q_{n-k}}.
\]

Das ist genau die diskrete Faltung \((x^{(r)} * q)_n\), also:

\[
\boxed{(B_p^{(1)}a)^{(r)} = x^{(r)} * q, \qquad q_s := s\,\ell_{s,1}.}
\]

### 1.2 Direkte Summenzerlegung

Die Indexmenge \(\mathbb{Z}\) zerfällt in \(p\) disjunkte Restklassen
\(r \in \{0, 1, \ldots, p-1\}\). Auf jeder Restklasse wirkt \(B_p^{(1)}\) als
**Faltungsoperator** mit demselben Filter \(q\):

\[
\boxed{B_p^{(1)} \cong \bigoplus_{r \in \mathbb{Z}/p\mathbb{Z}} C_q \circ M_u,}
\]

wobei \(C_q\) die Faltung mit \(q\) und \(M_u\) die Multiplikation mit dem
Fouriergewicht \(u = r+pk\) auf der \(r\)-Restklasse bezeichnet.

> **Strukturbemerkung.** Der Operator \(M_u\) auf der \(r\)-Restklasse
> wirkt als \(a_{r+pk} \mapsto (r+pk)\,a_{r+pk}\). Für \(r \neq 0\) gilt
> \(r+pk \neq 0\) für alle \(k\), also ist \(M_u\) auf der \(r\)-Restklasse
> **injektiv**. Für \(r = 0\) gilt \(0+p\cdot 0 = 0\), also hat \(M_u\) auf
> der \(0\)-Restklasse genau den Kern \(\{\delta_0\}\) (den Einheitsvektor
> bei \(k=0\), d.\,h.\ \(u = 0\)).

---

## 2. Zentraler konditionaler Satz (algebraisches Modell)

**Setup:** Sei \(\mathbb{C}[z, z^{-1}]\) der Laurentpolynomring (endlich getragene
Folgen). Schreibe

\[
X_r(z) := \sum_k x_k^{(r)} z^k = \sum_k (r+pk)a_{r+pk}\,z^k,
\qquad
Q(z) := \sum_s q_s z^s = \sum_s s\,\ell_{s,1}\,z^s.
\]

Dann gilt:

\[
(x^{(r)} * q)_n = [z^n]\bigl(X_r(z)\cdot Q(z)\bigr),
\]

d.\,h.\ \((B_p^{(1)}a)^{(r)} = 0\) genau dann, wenn \(X_r(z)\cdot Q(z) = 0\) in
\(\mathbb{C}[z,z^{-1}]\).

**Theorem (konditionaler Kernsatz — algebraisches Modell).**

*Hypothese:* \(Q \neq 0\) in \(\mathbb{C}[z,z^{-1}]\), d.\,h.\,
\(\exists\, s_0 \neq 0 : \ell_{s_0,1} \neq 0\).

*Schlussfolgerung:* Im endlich getragenen algebraischen Modell gilt:

\[
\boxed{Q \neq 0 \;\Longrightarrow\; \ker B_p^{(1)} = \operatorname{span}\{\delta_0\}.}
\]

**Beweis.**

*Schritt 1: Nullteilerfreiheit.*
\(\mathbb{C}[z,z^{-1}]\) ist ein nullteilerfreier Ring (jede Einheit ist eine
Laurenzeinheit \(\lambda z^k\); das Produkt zweier nichtnullwertiger
Laurentpolynome ist nichtnull). Aus \(Q \neq 0\) und \(X_r(z)Q(z) = 0\)
folgt daher \(X_r(z) = 0\).

*Schritt 2: Kern von \(M_u\) auf der \(r\)-Restklasse.*

- Für \(r \neq 0\): \(X_r = 0\) bedeutet \((r+pk)a_{r+pk} = 0\) für alle \(k\).
  Da \(r+pk \neq 0\) (weil \(r \not\equiv 0 \pmod{p}\)), folgt \(a_{r+pk} = 0\)
  für alle \(k\). Also \(a_u = 0\) für alle \(u \equiv r \pmod{p}\), \(r\neq 0\).
- Für \(r = 0\): \(X_0 = 0\) bedeutet \(pk\cdot a_{pk} = 0\) für alle \(k\),
  also \(a_{pk} = 0\) für alle \(k \neq 0\). Der Koeffizient \(a_0\) (\(k=0\),
  \(u = 0\)) ist **unsichtbar** für \(M_u\), da der Faktor \(u = 0\) ihn
  automatisch vernichtet.

*Schritt 3: Zusammenfassung.*
Für alle \(r\) und alle \(k\) mit \(r+pk \neq 0\) gilt \(a_{r+pk} = 0\).
Genau \(a_0\) (d.\,h.\ \(r=0, k=0\)) kann frei sein. Damit:

\[
\ker B_p^{(1)} = \operatorname{span}\{\delta_0\} \quad
\text{(im endlich getragenen algebraischen Modell)}. \quad \square
\]

**Konsequenz für den Hebungsabstieg:**

\[
Q \neq 0 \;\Longrightarrow\; \bigl(\Delta_p^{\mathrm{adm}} \subseteq \ker B_p^{(1)}
\iff \Delta_p^{\mathrm{adm}} \subseteq \operatorname{span}\{\delta_0\}\bigr).
\]

---

## 3. Firewall: algebraischer Satz vs.\ analytischer (\(\ell^2\)-)Satz

> **Diese Trennung ist verbindlich. Die Nullteilerfreiheit von
> \(\mathbb{C}[z,z^{-1}]\) darf nicht auf \(\ell^2\) übertragen werden.**

| Aspekt | Algebraisches Modell | \(\ell^2\)-Modell |
|---|---|---|
| Träger | endlich (Laurentpolynome) | \(\ell^2(\mathbb{Z})\) |
| Faltungsoperator | \(C_q\) auf \(\mathbb{C}[z,z^{-1}]\) | \(C_{\hat q} = M_{\hat q}\) im Fourierraum |
| Injectivität | aus Nullteilerfreiheit | abhängig von \(\hat q(\theta) \neq 0\) f.\,ü. |
| Kerncharakterisierung | \(X_r Q = 0 \Rightarrow X_r = 0\) | \(\ker C_q = \{f : \hat q\,\hat f = 0\}\) |
| Nullmengen | keine (Polynomring) | \(\{\theta : \hat q(\theta) = 0\}\) relevant |
| Status | \(\checkmark[M]\) (Theorem in \S2) | \(?[O]\) |

Für die \(\ell^2\)-Version ist die relevante Bedingung:

\[
\hat q(\theta) \neq 0 \quad \text{für fast alle } \theta \in [0, 2\pi),
\]

d.\,h.\ \(\hat q = \mathcal{F}(q)\) hat keine Nullmenge positiven Maßes.
Das ist eine **separate offene analytische Frage** \([O\text{-}250e\text{-ana}]\),
die von der Struktur der Koeffizienten \(\ell_{s,1}\) abhängt.

---

## 4. Verhältnis zu NEU-020: Was dort bewiesen ist und was nicht

NEU-020 beweist mit dem Zeugen \((n=2,m=3,r=4,s=1,t=-1,k=1)\):

\[
(R_3\Phi_3(e_4 V_2, e_1 V_3, e_{-1} V_1))_{6,6,0}
= -24\log(2)\log(6)/\mu \neq 0.
\]

Das liegt im \(V_6\)-Sektor (\(m=6\)), **nicht** im \(m=1\)-Sektor. Aus dem
NEU-020-Zeugen folgt:

\[
\ell_{s,6} \neq 0 \quad \text{für geeignetes } s
\qquad \Rightarrow \qquad [L_3] \neq 0 \text{ in } HH^4(F^3 A_{\mathrm{BC}}^{\mathrm{an}}).
\]

**Was NEU-020 nicht liefert:**
\(\ell_{s,1} \neq 0\) für irgendein \(s \neq 0\).

Die \(m=1\)-Scheibe von \(L_3^\circ\) und die \(m=6\)-Scheibe sind algebraisch
unabhängige Komponenten. Die Nichttrivialität der Gesamtklasse \([L_3] \neq 0\)
erzwingt keine nichttriviale \(m=1\)-Komponente.

> **Desiderat \([O\text{-}221\text{-}1c1a0\text{-C1a/10a}]\):**
> \[\exists\, s_0 \neq 0 : \ell_{s_0, 1} \neq 0 \quad ?\]
> Dieser Knoten kann **nicht** aus NEU-020 geschlossen werden.
> Er benötigt eine separate Betrachtung der \(m=1\)-Komponente von \(L_3^\circ\).

---

## 5. Vollständiger Pfad nach Klärung des Desiderats

```
NEU-250d
  └─> ker B_p^(1) definiert
        └─> NEU-250e (diese Datei)
              └─> Faltungszerlegung: B_p^(1) ≅ \bigoplus_r C_q M_u
                    └─> konditionaler Kernsatz: Q != 0 => ker B_p^(1) = span{delta_0}
                          |
                          └─> [O-221-1c1a0-C1a/10a]: Exists s_0 != 0 mit ell_{s_0,1} != 0?
                                |                        (NEU-162 / neue Berechnung)
                                |
                                ├─ JA:  Hebungsabstieg <=> Delta_p^adm \subseteq span{delta_0}
                                |         => [O-221-1c1a0-C1a/11]: Delta_p^adm-Klassifikation
                                |
                                └─ NEIN: Q = 0 => ker B_p^(1) = K_p (ganzer Kernraum)
                                          => Hebungsabstieg trivial erfüllbar
                                          => L_3^circ m=1-Schnitt ist 0
                                          => strukturelle Besonderheit
```

---

## 6. Statusbuchung

| Teilknoten | Aussage | Status |
|---|---|---|
| \([O\text{-}250e/1]\) | Faltungsreduktion \((B_p^{(1)}a)^{(r)} = x^{(r)} * q\) | \(\checkmark[M]\) |
| \([O\text{-}250e/2]\) | Direkte Summenzerlegung \(B_p^{(1)} \cong \bigoplus_r C_q M_u\) | \(\checkmark[M]\) |
| \([O\text{-}250e/3]\) | Konditionaler Kernsatz (algebraisch): \(Q\neq 0 \Rightarrow \ker B_p^{(1)} = \operatorname{span}\{\delta_0\}\) | \(\checkmark[M]\) |
| \([O\text{-}250e/4]\) | Firewall algebraisch vs.\ \(\ell^2\) dokumentiert | \(\checkmark[M]\) |
| \([O\text{-}250e/5]\) | NEU-020-Zeuge liegt im \(m=6\)-Sektor, nicht \(m=1\) | \(\checkmark[M]_{\mathrm{neg}}\) |
| **\([O\text{-}221\text{-}1c1a0\text{-C1a/10a}]\)** | **\(\exists\,s_0\neq 0: \ell_{s_0,1}\neq 0\)?** | **\(?[O]\)** |
| \([O\text{-}250e\text{-ana}]\) | \(\hat q(\theta)\neq 0\) f.\.\u.\ (analytische Ergänzung) | \(?[O]\) |

Gesamtstatus:
\[
\boxed{[O\text{-}221\text{-}1c1a0\text{-C1a/10}]:\ \checkmark[M]_{\mathrm{part}}
\text{ — algebraischer Mechanismus vollständig, Zeuge }\ell_{s_0,1}\neq 0\text{ offen.}}
\]

---

## 7. Nächster atomarer Knoten

\[
\boxed{[O\text{-}221\text{-}1c1a0\text{-C1a/10a}]:
\ \text{Zeige } \exists\,s_0\neq 0: \ell_{s_0,1}\neq 0.
\ \text{(Berechnung der }m=1\text{-Komponente von }L_3^\circ\text{)}}
\]

Dies entspricht dem alten Knoten NEU-162 in der jetzt operativ schärfer
gefassten Form: Nicht die gesamte Folge \((\ell_{s,1})_s\) wird benötigt,
sondern **ein einziger nichttrivialer Modus**.
