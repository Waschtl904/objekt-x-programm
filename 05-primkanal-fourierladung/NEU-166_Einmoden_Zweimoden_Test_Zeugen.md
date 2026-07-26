# NEU-166 — Ein- und Zweimoden-Test für exakt zulässige Liftänderungen

> Typ: **Zeugen-Konstruktion**.  
> Erstellt: 15. Juli 2026. Revision rev.2: 16. Juli 2026.  
> Vorgänger: NEU-157 rev.3, NEU-165a, NEU-165b.  
> Ziel: Den kleinsten mathematisch ehrlichen Existenzbeweis für
> $$\ker(C_p)\cap\ker(T_p)^{\,c}\cap\mathcal{Q}_p(\widehat\varepsilon_p^{\,0})\neq\varnothing.$$

---

## DAG-Position

```
NEU-157 rev.3  ──►  NEU-166  ──►  NEU-159 (vollständiger Zeuge)
      NEU-165a  ──►  NEU-166
      NEU-165b  ──►  NEU-166
```

---

## Statusbereinigung: $R_{p,j}$-Symbole entfernt

Die postulierte Symbolfamilie $R_{p,j}$ ist aus dem Hauptpfad entfernt. Auftrag [O-165b-1] (explizite Konstruktion der $R_{p,j}$) ist **geschlossen**. Es werden nur Operatoren $L_{p,a}$ eingeführt, die aus konkret homogen-linearen Bedingungen hervorgehen.

| Blatt | Rolle |
|---|---|
| NEU-157 rev.3 | primäre exakte Zulässigkeitstheorie |
| NEU-165 | abstrakter Rahmen für tatsächlich vorhandene lineare Nebenbedingungen |
| NEU-165a | expliziter Import und Shiftstruktur von $C_p$ |
| NEU-165b | Audit und Nachweis der Definitionslücke |
| **NEU-166** | **Ein-/Zweimoden-Test: konkreter Zeuge** |

---

## 166.A — Das verbliebene Existenzproblem

Das exakte Existenzproblem lautet:

$$\boxed{\exists\,k\in K_p^{\mathrm{hom}}\cap\ker(C_p)\cap\ker(T_p)^{\,c}\cap\mathcal{Q}_p(\widehat\varepsilon_p^{\,0}).}$$

Drei Teilbedingungen: (i) $C_p(k)=0$, (ii) $T_p(k)\neq0$, (iii) $2\operatorname{Re}h_p(\widehat\varepsilon_p^{\,0},k)+h_p(k,k)=0$.

---

## 166.B — Rohbild-Zerlegung und Vergleichsdiagramm

Definiere den **unprojizierten Kopplungsoperator**

$$G_p(e_uV_p):=-u\log(p)\sum_{s,m}s\,\ell_{s,m}\,e_{u+ps}V_{pm}.\tag{166.B.1}$$

Dann gilt

$$C_p = \Pi_{J,N}\circ G_p.$$

Falls auch $T_p = \Theta_p\circ G_p$ für eine Abbildung $\Theta_p$ gilt, entsteht das Vergleichsdiagramm:

$$\begin{array}{ccccccc}
K_p & \xrightarrow{\;G_p\;} & Y_p^{\mathrm{raw}} & \quad & K_p & \xrightarrow{\;G_p\;} & Y_p^{\mathrm{raw}}\\
& \searrow^{C_p} & \downarrow^{\Pi_{J,N}} & \quad & & \searrow^{T_p} & \downarrow^{\Theta_p}\\
& & Y_p^C & \quad & & & Y_p^T
\end{array}$$

Das Einmoden-Kriterium lautet dann präzise:

$$G_p(e_uV_p)\in\ker(\Pi_{J,N})\setminus\ker(\Theta_p).\tag{*}$$

**Offene Aufgabe [O-166-0]:** Exakte Definition von $T_p$, sein Definitions- und Zielraum, explizite Formel $T_p(e_uV_p)$, und seine Relation zu $G_p$ und $C_p$. Insbesondere: Gilt $T_p=\Theta_p\circ G_p$?

**Statusmarker:** ❓[O]

---

## 166.C — Faktorisierungsdiagnose (entscheidend)

Nicht die Verschiedenheit der Zielräume, sondern die **Faktorisierungsrelation** entscheidet über Existenz oder Ausschluss eines Zeugen.

### 166.C.1 — Ausschlussfall

Falls ein Operator $A_p$ existiert mit

$$T_p = A_p\circ C_p,$$

dann gilt automatisch $\ker(C_p)\subseteq\ker(T_p)$. Ein Zeuge mit $C_p(k)=0$, $T_p(k)\neq0$ ist dann **unmöglich**.

$$\boxed{T_p=A_p\circ C_p \implies \text{Einmoden-Zeuge unmöglich.}}$$

### 166.C.2 — Möglicher Zeugenfall

Falls $C_p=B_p\circ T_p$, kann ein Zeuge existieren: nämlich wenn $T_p(k)\in\ker(B_p)\setminus\{0\}$.

### 166.C.3 — Komplementäre Projektionen (Hauptfall)

Falls $C_p=\Pi_p G_p$ und $T_p=\Theta_p G_p$ mit voneinander **unabhängigen** Projektionen, muss gezeigt werden:

$$\operatorname{ran}(G_p)\cap(\ker\Pi_p\setminus\ker\Theta_p)\neq\varnothing.$$

Das ist der **eigentliche geometrische Engpass**.

**Wichtig:** Auch bei identischem Zielraum können $C_p(k)=0$ und $T_p(k)\neq0$ gleichzeitig gelten, sofern die Operatoren unabhängig sind. Umgekehrt können verschiedene Zielräume durch eine Faktorisierung verbunden sein und den Zeugen ausschließen.

**Die korrekte primmäre Frage ist:**

$$\boxed{\ker(C_p)\not\subseteq\ker(T_p)?}$$

**Statusmarker:** ❓[O] — erfordert explizite Definition von $T_p$ [O-166-0].

---

## 166.D — Einmoden-Ansatz

Setze $v_{p,u}:=e_uV_p$, $k=t\,v_{p,u}$, $t\in\mathbb{C}$. Definiere

$$a_{p,u}:=h_p(\widehat\varepsilon_p^{\,0},v_{p,u}),\qquad b_{p,u}:=h_p(v_{p,u},v_{p,u}).$$

Normierungsbedingung:

$$2\operatorname{Re}(t\,a_{p,u})+|t|^2b_{p,u}=0.\tag{166.1}$$

**Einmoden-Kriterium:**

$$\boxed{C_p(e_uV_p)=0,\quad a_{p,u}\neq0,\quad T_p(e_uV_p)\neq0.}\tag{166.2}$$

Bei positiver Definitheit ($b_{p,u}>0$, $v_{p,u}\neq0$) besitzt (166.1) für $t\neq0$ genau dann eine Lösung, wenn $a_{p,u}\neq0$. Die explizite Lösung ist:

$$t_0 = \frac{2|a_{p,u}|}{b_{p,u}}\,e^{i(\pi-\phi)},\qquad\phi=\arg(a_{p,u}).$$

**Statusmarker:** ✅[M] als Satz; ❓[O] Existenz eines $u$ mit (166.2).

---

## 166.E — Primkandidat $u=1-p$

Der bevorzugte Testkandidat ist $u=1-p$:

- $u=1-p\neq0$ für $p\geq2$.
- Für $s=1$: Zielindex $r=1+p(s-1)=1$, d.h. Terme $e_1V_{pm}$.

Die entscheidende Rohbildfrage:

$$G_p(e_{1-p}V_p)\in\ker(\Pi_{J,N})\setminus\ker(\Theta_p)?\tag{166.3}$$

Diese Frage kann erst beantwortet werden, wenn $\Theta_p$ und die Struktur von $\Pi_{J,N}$ explizit bekannt sind [O-166-0, O-165a-3].

**Statusmarker:** ❓[O]

---

## 166.F — Zweimoden-Ansatz

Setze $v_u=e_uV_p$, $v_{u'}=e_{u'}V_p$, $w=a\,v_u+b\,v_{u'}$.

### 166.F.1 — Kernbedingung: vollständige Spaltenproportionalität

$w\in\ker(C_p)$ genau dann, wenn

$$a\,C_p(v_u)+b\,C_p(v_{u'})=0.$$

Sind beide Spalten ungleich null, ist dies äquivalent zu:

$$\boxed{C_p(v_u)\text{ und }C_p(v_{u'})\text{ sind linear abhängig.}}\tag{**}$$

### 166.F.2 — Arithmetische Supportbedingung (notwendig, nicht hinreichend)

Vor der Projektion treffen Terme der beiden Spalten zusammen, wenn

$$(u+ps,pm)=(u'+ps',pm'),$$

d.h. $m=m'$ und

$$u-u'=p(s'-s).\tag{166.4}$$

Dies ist die **arithmetische Überlappungsbedingung**. Bei einer einzelnen überlappenden Zielkomponente und Mehrtermfall ergibt das Verhältnis

$$\frac{b}{a}=-\frac{u\,s\,\ell_{s,m}}{u'\,s'\,\ell_{s',m}}\tag{166.5}$$

**noch keine** vollständige Annihilierung. Dieselbe Proportion muss **alle** projizierten Zielkoordinaten annihilieren:

$$a\,r_p(v,u)+b\,r_p(v,u')=0\quad\text{für jeden Zielindex }v.$$

Bei koordinatenweiser Projektion verlangt dies:

$$\operatorname{supp}C_p(v_u)=\operatorname{supp}C_p(v_{u'})$$

und koordinatenweise dasselbe Koeffizientenverhältnis. Andernfalls bleibt mindestens eine ungepaarte Zielkomponente stehen.

**Zweimoden-Triage:**

$$\text{arithmetische Supportüberlappung}\longrightarrow\text{vollständige Spaltenproportionalität}\longrightarrow w\in\ker(C_p).$$

**Statusmarker:** ✅[M] als Triage-Schema; ❓[O] ob ein Paar $(u,u')$ vollständige Proportionalität erfüllt.

### 166.F.3 — Normierungsschritt nach Kernrichtung

Sobald eine feste Kernrichtung $w\in\ker(C_p)$, $w\neq0$, gefunden ist, setze $k=\tau w$. Mit

$$A_w:=h_p(\widehat\varepsilon_p^{\,0},w),\qquad B_w:=h_p(w,w)$$

lautet die Normierungsbedingung:

$$2\operatorname{Re}h_p(\widehat\varepsilon_p^{\,0},\tau w)+|\tau|^2B_w=0.$$

Bei $B_w>0$ (positiv definit) existiert $\tau\neq0$ genau dann, wenn $A_w\neq0$. Das Kriterium ist konventionsunabhängig vom Argument der Sesquilinearität.

Da $T_p(\tau w)=\tau T_p(w)$, ändert eine nichtverschwindende Normierungsskalierung den Status $T_p(w)\neq0$ nicht.

**Statusmarker:** ✅[M] als Satz; ❓[O] ob $A_w\neq0$ für gefundenes $w$.

### 166.F.4 — $T_p(w)\neq0$ für Zweimoden-Kandidaten

Nach Fixierung von $b/a$:

$$T_p(w)=a\,T_p(v_u)+b\,T_p(v_{u'})\stackrel{?}{\neq}0.\tag{166.6}$$

Das Verhältnis $b/a$ aus (166.5) muss vermieden werden, dass auch $T_p(v_u)$ und $T_p(v_{u'})$ exakt in diesem Verhältnis stehen.

**Statusmarker:** ❓[O]

---

## 166.G — Arbeitskette

**Einmodus:**
$$C_p(e_uV_p)=0 \longrightarrow a_{p,u}\neq0 \longrightarrow T_p(e_uV_p)\neq0 \longrightarrow \text{Zeuge }k=t_0 e_uV_p.$$

**Zweimodus:**
$$\text{Arithm. Überlappung (166.4)} \longrightarrow \text{Spaltenproportionalität (**)} \longrightarrow A_w\neq0 \longrightarrow T_p(w)\neq0 \longrightarrow \text{Zeuge }k=\tau w.$$

---

## 166.H — Statusmatrix

| Aussage | Status |
|---|---|
| Rohbild-Zerlegung $C_p=\Pi_{J,N}\circ G_p$ | ✅[M] |
| Einmoden-Kriterium (166.2) als Satz | ✅[M] |
| Normierungslemma für feste Kernrichtung (166.F.3) | ✅[M] |
| Zweimoden-Triage-Schema | ✅[M] |
| Arithmetische Überlappungsbedingung (166.4) | ✅[M] |
| Koeffizientenverhältnis (166.5) als notwendige Bedingung | ✅[M] |
| Exakte Definition von $T_p$ und $\Theta_p$ | ❓[O] → [O-166-0] |
| $T_p=\Theta_p\circ G_p$? Faktorisierungsdiagnose | ❓[O] → [O-166-0] |
| $\ker(C_p)\not\subseteq\ker(T_p)$? | ❓[O] → [O-166-0] |
| Primkandidat $u=1-p$: (166.3) erfüllt? | ❓[O] → [O-166-0], [O-165a-3] |
| Vollständige Spaltenproportionalität für ein Paar $(u,u')$ | ❓[O] → [O-166-1] |
| $A_w\neq0$ für gefundene Kernrichtung | ❓[O] → [O-166-2] |
| $T_p(w)\neq0$ für Zweimoden-Kandidaten | ❓[O] → [O-166-3] |

---

## Offene Aufgaben

$$\boxed{\text{[O-166-0]}}\quad\text{\textbf{primär}}$$  
Exakte Definition von $T_p$: Definitionsbereich, Zielraum, Formel $T_p(e_uV_p)$, Relation zu $G_p$ und $C_p$. Bestimme $\Theta_p$ und entscheide die Faktorisierungsdiagnose (166.C).

$$\boxed{\text{[O-166-1]}}$$  
Nach [O-166-0]: Primkandidat $u=1-p$ testen via (166.3). Bei Scheitern: kleinste Paare $(u,u')$ mit arithmetischer Überlappung (166.4) bestimmen und vollständige Spaltenproportionalität (**) nachweisen.

$$\boxed{\text{[O-166-2]}}$$  
Für gefundene Kernrichtung $w$: $A_w=h_p(\widehat\varepsilon_p^{\,0},w)\neq0$ prüfen.

$$\boxed{\text{[O-166-3]}}$$  
$T_p(w)\neq0$ nachweisen. Da Skalierung erhalten bleibt, genügt $T_p(w)\neq0$ für die unnormierte Kernrichtung.

---

## Verweise

NEU-41 §1/§4, NEU-157 rev.3 (§157.B–G), NEU-159, NEU-165a (165a.1/165a.2), NEU-165b.
