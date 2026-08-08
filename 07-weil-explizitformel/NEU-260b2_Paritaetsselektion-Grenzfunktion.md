# NEU-260b.2 — Paritätsselektion durch Suzukis Grenzfunktion

**Katalog-ID:** NEU-260b.2  
**Ordner:** `07-weil-explizitformel`  
**Datum:** 2026-08-08  
**Auftrag:** $W(a,0;\cdot)$ ungerade, $W(a,\pi;\cdot)$ gerade; Zielausdruck $F(z)$ ungerade mit einfachem Nullpunkt bei $0$; Hurwitz/Rouché $\Rightarrow$ $\theta=\pi$-Zweig inkompatibel mit Suzukis Grenzrelation; $\varepsilon(a)=+1$ für hinreichend großes $a$ (konditional auf Grenzrelation).  
**RH-Firewall:** Das Ergebnis beweist weder die Grenzrelation noch RH.

---

## 0. Ausgangslage

Aus NEU-260b $\checkmark[K/M]$:
$$
T_av_+=e^x, \quad T_av_-=e^{-x}, \quad Pv_+=v_-. \qquad (0\text{-Base})
$$

Suzukis Parametrisierungsformel (Suzuki 2026, \S{}2):
$$
W(a,\theta;z) = (z-i)\int_{-a}^a v_+(x)e^{izx}\,dx + e^{i\theta}(z+i)\int_{-a}^a v_-(x)e^{izx}\,dx. \qquad (0\text{-W})
$$

---

## 1. Parität von $W(a,\theta;z)$

### 1.1 Hilfsgröße

Setze
$$
I_a(z) := \int_{-a}^a v_+(x)e^{izx}\,dx. \qquad (1\text{-Ia})
$$

Aus $v_-=Pv_+$, d.h. $v_-(x)=v_+(-x)$, folgt durch Substitution $x\mapsto-x$:
$$
\int_{-a}^a v_-(x)e^{izx}\,dx = \int_{-a}^a v_+(-x)e^{izx}\,dx = \int_{-a}^a v_+(x)e^{-izx}\,dx = I_a(-z). \qquad (1\text{-Im})
$$

### 1.2 Parität für $\theta=0$ ($+P$-Zweig)

$$
W(a,0;z) = (z-i)I_a(z) + (z+i)I_a(-z). \qquad (1\text{-W0})
$$

$$
W(a,0;-z) = (-z-i)I_a(-z) + (-z+i)I_a(z) = -(z+i)I_a(-z) - (z-i)I_a(z) = -W(a,0;z). \qquad (1\text{-W0odd})
$$

$$
\boxed{W(a,0;-z) = -W(a,0;z).\quad\checkmark[K/M]\quad\text{($+P$-Zweig ist ungerade)}} \qquad (1\text{-Odd})
$$

### 1.3 Parität für $\theta=\pi$ ($-P$-Zweig)

$$
W(a,\pi;z) = (z-i)I_a(z) - (z+i)I_a(-z). \qquad (1\text{-Wpi})
$$

$$
W(a,\pi;-z) = (-z-i)I_a(-z) - (-z+i)I_a(z) = -(z+i)I_a(-z) + (z-i)I_a(z) = W(a,\pi;z). \qquad (1\text{-Wpieven})
$$

$$
\boxed{W(a,\pi;-z) = +W(a,\pi;z).\quad\checkmark[K/M]\quad\text{($-P$-Zweig ist gerade)}} \qquad (1\text{-Even})
$$

---

## 2. Suzukis Zielausdruck $F(z)$ ist ungerade mit einfachem Nullpunkt bei $0$

### 2.1 Parität von $F$

Suzukis conjecturaler Zielausdruck:
$$
F(z) = z^2\frac{\xi(1/2-iz)}{\xi'(1/2-iz)}. \qquad (2\text{-F})
$$

Aus dem Funktionalgleichung $\xi(s)=\xi(1-s)$ folgt mit $s=1/2-iz$:
$$
\xi(1/2-iz) = \xi(1/2+iz). \qquad (2\text{-xi-sym})
$$

Differenzieren: $\xi'(1/2+iz)\cdot i = -\xi'(1/2-iz)\cdot(-i)$, also
$$
\xi'(1/2+iz) = -\xi'(1/2-iz). \qquad (2\text{-xip-antisym})
$$

Damit:
$$
F(-z) = (-z)^2\frac{\xi(1/2+iz)}{\xi'(1/2+iz)} = z^2\frac{\xi(1/2-iz)}{-\xi'(1/2-iz)} = -F(z). \qquad (2\text{-Fodd})
$$

$$
\boxed{F(-z) = -F(z).\quad\checkmark[K/M]} \qquad (2\text{-Odd})
$$

### 2.2 Einfacher Nullpunkt von $F$ bei $z=0$

Da $\xi(1/2)\neq 0$ (bekannt) und $\xi'(1/2)=0$ (da $\xi$ gerade um $s=1/2$),
hat $F$ bei $z=0$ einen Pol erster Ordnung im Nenner, aber den Faktor $z^2$ im Zähler:
- $z^2\to 0$ (Nullstelle zweiter Ordnung des Zählers),
- $\xi'(1/2-iz)\to 0$ (Nullstelle im Nenner bei $z=0$).

Taylor von $\xi$ um $s=1/2$: $\xi(1/2+w)=\xi(1/2)+\frac12\xi''(1/2)w^2+O(w^4)$ (nur gerade Terme), also
$$
\xi'(1/2-iz)=\frac{d}{dw}\xi(1/2+w)\big|_{w=-iz}=\xi''(1/2)\cdot(-iz)+O(z^3).
$$

Da $\xi''(1/2)>0$ (bekannt: positive Taylor-Koeffizienten):
$$
F(z) = z^2\frac{\xi(1/2)+O(z^2)}{\xi''(1/2)(-iz)+O(z^3)} = \frac{z^2\cdot\xi(1/2)}{-i\xi''(1/2)\cdot z}\cdot(1+O(z^2)) = \frac{i\xi(1/2)}{\xi''(1/2)}\cdot z + O(z^3). \qquad (2\text{-Taylor})
$$

$$
\boxed{F(z)=c\cdot z+O(z^3)\text{ mit }c=i\xi(1/2)/\xi''(1/2)\neq0.\quad\checkmark[K/M]\quad\text{($F$ hat einfachen Nullpunkt bei }z=0\text{)}} \qquad (2\text{-Simple})
$$

---

## 3. $\theta=\pi$ ist inkompatibel mit der Suzuki-Grenzrelation

### 3.1 Das Argument

Suzukis Grenzrelation (Vermutung, Suzuki 2026):
$$
e^{\phi(a,z)}W(a,\theta(a);z) \longrightarrow F(z), \quad a\to\infty, \text{ lokal gleichmäßig.} \qquad (3\text{-Limit})
$$

Der Faktor $e^{\phi(a,z)}$ ist nullstellenfrei (da $e^w\neq 0$ für alle $w\in\mathbb{C}$). Damit hat $e^{\phi(a,z)}W(a,\theta(a);z)$ dieselbe Nullstellenmenge wie $W(a,\theta(a);z)$.

Für $\theta(a)=\pi$: $W(a,\pi;\cdot)$ ist gerade (Abschnitt 1.3), also sind Nullstellen in Paaren $\pm z_0$, und jede Nullstelle bei $0$ hat gerade Multiplizität.

Der Grenzwert $F(z)$ hat bei $z=0$ einen einfachen (= ungeraden) Nullpunkt.

**Hurwitz/Rouché:** Lokal gleichmäßige Konvergenz holomorpher Funktionen preserviert Nullstellenordnungen im Limit. Für eine hinreichend kleine Kreisscheibe $D_r=\{|z|<r\}$ gilt: Für alle hinreichend großen $a$ hat $e^{\phi(a,z)}W(a,\theta(a);z)$ in $D_r$ genau eine Nullstelle (gezählt mit Vielfachheit), nämlich bei $z=0$ mit Ordnung 1.

Ein gerader Holomorphismus kann aber in einer Kreisscheibe um $0$ nur Nullstellen gerader Gesamtmultiplizität haben (weil $f(0)=0$, $f\text{ gerade }\Rightarrow f(z)=z^{2k}g(z)$ mit $g(0)\neq0$).

Daher: Wenn $\theta(a)=\pi$ für unendlich viele $a$, kann die lokal gleichmäßige Konvergenz zu $F$ nicht gelten.

$$
\boxed{\text{Eine Folge mit }\theta(a)=\pi\text{ kann Suzukis Grenzrelation nicht erfüllen.}\quad\checkmark[K/M]} \qquad (3\text{-Incomp})
$$

### 3.2 Schlussfolgerung

$$
\boxed{\text{Suzuki-Grenzrelation }(3\text{-Limit})\text{ gilt }\Rightarrow\varepsilon(a)=+1\text{ für alle hinreichend großen }a.\quad\checkmark[K/M]\text{ (konditional)}} \qquad (3\text{-Eps})
$$

Kein Stetigkeitsargument erforderlich. Das Argument nutzt nur: Nullstellenerhaltung unter lokaler gleichmäßiger Konvergenz + Paritätsstruktur + einfacher Nullpunkt von $F$ bei $0$.

---

## 4. RH-Firewall und Konditionalität

$$
\boxed{\text{NEU-260b.2 beweist weder die Grenzrelation }(3\text{-Limit})\text{ noch RH.}} \qquad (4\text{-Firewall})
$$

Die Grenzrelation ist der gewaltige offene Schritt; sie impliziert RH (Suzuki 2026, Hauptvermutung).

Was bewiesen ist:
$$
\boxed{\text{Falls Suzukis Grenzmechanismus der richtige ist, ist der }\mathbb{Z}_2\text{-Zweig nicht frei: }\varepsilon(a)=+1\text{ asymptotisch.}} \qquad (4\text{-Strong})
$$

Anschlussfrage: Kann die asymptotische $+P$-Auswahl über Stetigkeit (nach Konstruktion einer analytischen Familie) auf alle $a>0$ zurückpropagiert werden? $\to$ NEU-260b.3 (falls benötigt) oder direkt NEU-260c.

---

## 5. Statusbuchungen

$$W(a,0;-z)=-W(a,0;z)\quad\checkmark[K/M]\qquad(5\text{-a})$$
$$W(a,\pi;-z)=+W(a,\pi;z)\quad\checkmark[K/M]\qquad(5\text{-b})$$
$$F(-z)=-F(z)\quad\checkmark[K/M]\qquad(5\text{-c})$$
$$F(z)=cz+O(z^3),\;c\neq0\quad\checkmark[K/M]\text{ (einfacher Nullpunkt bei }0\text{)}\qquad(5\text{-d})$$
$$\theta(a)=\pi\text{ inkompatibel mit Suzuki-Grenzrelation}\quad\checkmark[K/M]\qquad(5\text{-e})$$
$$\varepsilon(a)=+1\text{ für hinreichend großes }a\text{ (konditional auf Grenzrelation)}\quad\checkmark[K/M]\text{ (konditional)}\qquad(5\text{-f})$$
$$\text{Grenzrelation und RH: nicht bewiesen}\quad?[O]\qquad(5\text{-g})$$
$$\varepsilon\equiv+1\text{ für alle }a>0\text{ (Propagation)}\quad?[O]\to\text{später}\qquad(5\text{-h})$$

---

## 6. Abhängigkeiten

| Referenz | SHA | Inhalt |
|---|---|---|
| NEU-260b (Patch) | e50ed1c | $Pv_+=v_-$, Parität $\checkmark$ |
| NEU-260b.1 (Patch) | dieser Commit | Stetigkeitsargument zurückgestuft |
| Suzuki 2026 | \S{}2 | $W(a,\theta;z)$-Formel, $e^\phi$-Normierung, Grenzkonjektur |
| Hurwitz/Rouché | — | Nullstellenerhaltung bei lokal gleichm. Konvergenz |

---

*Lizenz: CC BY 4.0 — Objekt-X-Programm.*  
*Erstellt 2026-08-08. Stärkstes bisheriges analytisches Resultat zur $\mathbb{Z}_2$-Selektion.*
