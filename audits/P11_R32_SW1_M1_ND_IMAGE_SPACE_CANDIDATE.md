# P11/R32 — SW1 M1-ND Image-Space Reduction Candidate

> **Stand:** 31. August 2026  
> **Basis:** konstruiert auf `main@383e42f0643ad7ba3f8bec42faa988807a66ac9d`; gemergt mit PR #42 als `d117e4cb6e59a04ac0ae79b8176e4beaf114979e`; analytisch nachgehärtet nach Owner-Review am 31. August 2026.  
> **Status:** AI-GREEN candidate + independent GREEN (certificate, algebraic/mechanical scope) + owner analytic review **ACCEPTED**; keine `✓[M]`-Promotion.  
> **Ziel:** den echten C2/M1-Zustandsraum innerhalb des formalen \(12_H+12_W\)-Inputcovers explizit charakterisieren und M1-ND von 24 redundanten Slots auf sechs Basislift-Funktionen plus die exakte \(K\)-Nebenbedingung reduzieren.  
> **Firewall:** keine Injektivitätsaussage, kein Gegenvektor, kein HT-RED, kein Objekt-X- oder RH-Schluss.

---

## 0. Ausgangspunkt

Nach PR #40 gilt im dokumentierten Scope

\[
\boxed{
\ker\Gamma_I
\cong
\ker\mathscr C_R
\cong
\ker\widehat{\mathscr C}_R,
}
\tag{IMG.0}
\]

wobei M1-FULL den transportierten Operator als

\[
\boxed{
(\widehat{\mathscr C}_R F)(\theta)
=
\sum_{j=-3}^{3}
M_j(\theta)F(\theta+j\Delta)
}
\tag{IMG.1}
\]

auf einem formalen

\[
12_H+12_W
\]

Inputcover darstellt.

Dieser 24-Slot-Raum ist **nicht** der physische Definitionsraum. Beide 12er Blöcke sind redundante vier-Spezies-Cover geschlossener Bildunterräume.

Der erste M1-ND-Schritt ist daher nicht ein Matrixrangtest, sondern die exakte Beschreibung dieser Bildunterräume.

---

# Teil I — Vier-Spezies-Kovarianz

## 1. Sheet/Parity-Gruppe

Auf

\[
\mathbb T_L=\mathbb R/L\mathbb Z
\]

verwenden wir die vier bereits in C1C1/C2 definierten Kreismaps

\[
\rho_{P_0}(\theta)=\theta,
\]

\[
\rho_{P_1}(\theta)=\theta+\frac L2,
\]

\[
\rho_{\overline Q_0}(\theta)=4\Delta-\theta,
\]

\[
\rho_{\overline Q_1}(\theta)
=
4\Delta-\theta+\frac L2
\pmod L.
\tag{IMG.2}
\]

Sie bilden die Klein-Vierergruppe

\[
G=\{P_0,P_1,\overline Q_0,\overline Q_1\}.
\]

Alle vier \(\rho_g\) sind maßtreu.

---

## 2. Positive Liftmasken

Für die Horizontseite setze

\[
m_k(u)
=
\mathbf1_{\{0<u+kL<T_0\}},
\qquad
k=0,1,2.
\tag{IMG.3}
\]

Für den Annulus setze

\[
n_k(u)
=
\mathbf1_{\{R<u+kL<S\}},
\qquad
k=0,1,2.
\tag{IMG.4}
\]

Die speciesabhängigen Masken sind lediglich Pullbacks:

\[
m_{g,k}(\theta)
=
m_k(\rho_g(\theta)),
\qquad
n_{g,k}(\theta)
=
n_k(\rho_g(\theta)).
\tag{IMG.5}
\]

---

## 3. Symmetrischer Horizoncover

Für gerades

\[
y\in\mathscr H_+
\]

lautet die bereits korrigierte C1C1-Komponentenformel

\[
\boxed{
(\mathcal U_H y)_{g,k}(\theta)
=
\frac1{\sqrt2}\,
m_k(\rho_g(\theta))\,
y(\rho_g(\theta)+kL).
}
\tag{IMG.6}
\]

Damit gilt unmittelbar für jedes \(g\in G\):

\[
\boxed{
(\mathcal U_H y)_{g,k}(\theta)
=
(\mathcal U_H y)_{P_0,k}(\rho_g(\theta))
}
\tag{IMG.7}
\]

für fast jedes \(\theta\).

Die vier Species sind also **keine vier unabhängigen Funktionen**.

---

## 4. Symmetrischer Annuluscover

C2 vervierfacht den C1C1-Dreilift-Annuluscover redundant mit denselben vier Species.

Nach Odd-Faltung mit \(\sqrt2\) und Vierblatt-Normierung \(1/2\) lautet die Original-\(w\)-Komponentenform

\[
\boxed{
(\mathcal U_W^{(4)}w)_{g,k}(\theta)
=
\frac1{\sqrt2}\,
n_k(\rho_g(\theta))\,
w(\rho_g(\theta)+kL),
}
\tag{IMG.8}
\]

wobei rechts der positive Annuluswert von \(w\) verwendet wird.

Daher ebenfalls

\[
\boxed{
(\mathcal U_W^{(4)}w)_{g,k}(\theta)
=
(\mathcal U_W^{(4)}w)_{P_0,k}(\rho_g(\theta)).
}
\tag{IMG.9}
\]

Damit sind auch die zwölf formalen \(W\)-Slots nur vier redundante Darstellungen derselben drei Basisliftfunktionen.

---

# Teil II — Exakte Charakterisierung der Bildräume

## 5. Horizon-Bildraum ohne \(K\)-Restriktion

Definiere

\[
\mathscr R_H^{(4)}
\subset
L^2(\mathbb T_L;\mathbb C^{12})
\]

als die Menge aller \(F=(F_{g,k})\), die

### Support

\[
F_{P_0,k}
=
m_kF_{P_0,k}
\tag{IMG.10}
\]

und

### \(G\)-Kovarianz

\[
\boxed{
F_{g,k}
=
F_{P_0,k}\circ\rho_g
}
\tag{IMG.11}
\]

für alle \(g,k\) erfüllen.

Dann

\[
\boxed{
\operatorname{Ran}\mathcal U_H
=
\mathscr R_H^{(4)}.
}
\tag{IMG.12}
\]

### 5.1 Explizite Rückrekonstruktion

Sei

\[
F\in\mathscr R_H^{(4)}.
\]

Für

\[
x\in(0,T_0)
\]

gibt es eindeutig

\[
\theta=[x]_L\in[0,L),
\qquad
k\in\{0,1,2\},
\qquad
x=\theta+kL.
\]

Definiere

\[
\boxed{
y_F(x)
=
\sqrt2\,F_{P_0,k}(\theta)
}
\tag{IMG.13}
\]

auf der positiven Halbachse und erweitere gerade:

\[
y_F(-x)=y_F(x).
\]

Dann gilt

\[
\boxed{
\mathcal U_Hy_F=F.
}
\tag{IMG.14}
\]

Die Rückabbildung ist eindeutig.

---

## 6. Annulus-Bildraum

Definiere analog

\[
\mathscr R_W^{(4)}
\subset
L^2(\mathbb T_L;\mathbb C^{12})
\]

durch

\[
G_{P_0,k}
=
n_kG_{P_0,k}
\tag{IMG.15}
\]

und

\[
\boxed{
G_{g,k}
=
G_{P_0,k}\circ\rho_g.
}
\tag{IMG.16}
\]

Dann

\[
\boxed{
\operatorname{Ran}\mathcal U_W^{(4)}
=
\mathscr R_W^{(4)}.
}
\tag{IMG.17}
\]

Für \(G\in\mathscr R_W^{(4)}\) ist die positive Annulusrekonstruktion

\[
\boxed{
w_G(x)
=
\sqrt2\,G_{P_0,k}([x]_L),
\qquad
x=[x]_L+kL\in(R,S),
}
\tag{IMG.18}
\]

und die negative Seite wird ungerade ergänzt:

\[
w_G(-x)=-w_G(x).
\]

Damit

\[
\boxed{
\mathcal U_W^{(4)}w_G=G.
}
\tag{IMG.19}
\]

---

# Teil III — Der \(K\)-Bildraum

## 7. Innere Hubbedingung in Basislift-Koordinaten

Der echte Horizon-Input liegt nicht in ganz \(\mathscr H_+\), sondern in

\[
K
=
\ker(E_I^*H|_{\mathscr H_+}).
\]

A-FOLD/KNF liefert auf SW1 für fast jedes

\[
0<u<R
\]

die äquivalente positive Row

\[
\boxed{
\begin{aligned}
0={}&
p[y(a-u)-y(a+u)]\\
&+
r[y(b-u)-y(b+u)]\\
&+
q[y(T-u)-y(T+u)].
\end{aligned}
}
\tag{IMG.20}
\]

Alle sechs Argumente liegen auf SW1 im Horizont.

---

## 8. Basislift-Rekonstruktionsfunktion

Für einen Horizon-Basisliftvektor

\[
f=(f_0,f_1,f_2)
\]

mit

\[
f_k=m_kf_k
\]

definiere die positive rekonstruktierte Spur

\[
Y_f(x)
=
f_k([x]_L)
\qquad
\text{für }x=[x]_L+kL\in(0,T_0).
\tag{IMG.21}
\]

Der konstante Faktor \(\sqrt2\) aus IMG.13 cancelt in der homogenen Kernelrow.

Daher ist IMG.20 äquivalent zu

\[
\boxed{
\begin{aligned}
0={}&
p[Y_f(a-u)-Y_f(a+u)]\\
&+
r[Y_f(b-u)-Y_f(b+u)]\\
&+
q[Y_f(T-u)-Y_f(T+u)]
\end{aligned}
}
\tag{IMG.22}
\]

für fast jedes \(0<u<R\).

---

## 9. Exakter Basisraum für \(K\)

Definiere

\[
\boxed{
\mathscr B_K
:=
\left\{
f=(f_0,f_1,f_2):
f_k=m_kf_k
\text{ und IMG.22 gilt a.e.}
\right\}.
}
\tag{IMG.23}
\]

Definiere den Species-Extensionoperator

\[
(E_Hf)_{g,k}
=
f_k\circ\rho_g.
\tag{IMG.24}
\]

Dann gilt exakt

\[
\boxed{
\mathscr R_K^{(4)}
:=
\mathcal U_H(K)
=
E_H(\mathscr B_K).
}
\tag{IMG.25}
\]

Die Rückabbildung ist schlicht die \(P_0\)-Restriktion

\[
\boxed{
R_HF
=
(F_{P_0,0},F_{P_0,1},F_{P_0,2}).
}
\tag{IMG.26}
\]

Somit

\[
R_HE_H=I_{\mathscr B_K},
\qquad
E_HR_H=I_{\mathscr R_K^{(4)}}.
\tag{IMG.27}
\]

---

## 10. Exakter Basisraum für \(W\)

Definiere

\[
\boxed{
\mathscr B_W
:=
\left\{
g=(g_0,g_1,g_2):
g_k=n_kg_k
\right\}.
}
\tag{IMG.28}
\]

Mit

\[
(E_Wg)_{s,k}
=
g_k\circ\rho_s
\tag{IMG.29}
\]

und

\[
R_WG
=
(G_{P_0,0},G_{P_0,1},G_{P_0,2})
\tag{IMG.30}
\]

gilt

\[
\boxed{
E_W:
\mathscr B_W
\xrightarrow{\sim}
\mathscr R_W^{(4)}
}
\tag{IMG.31}
\]

mit

\[
R_WE_W=I_{\mathscr B_W},
\qquad
E_WR_W=I_{\mathscr R_W^{(4)}}.
\tag{IMG.32}
\]

---

# Teil IV — M1-ND als 6-Basislift-Problem

## 11. Zulässiger M1-Definitionsraum

Der tatsächliche M1-ND-Domain ist damit exakt

\[
\boxed{
\mathscr R_K^{(4)}
\oplus
\mathscr R_W^{(4)}
=
E_H(\mathscr B_K)
\oplus
E_W(\mathscr B_W).
}
\tag{IMG.33}
\]

Die 24 formalen Slotfunktionen sind also vollständig durch

\[
\boxed{
3_H+3_W
}
\]

Basisliftfunktionen bestimmt.

Dies bedeutet **nicht**, dass das Problem sechsdimensional ist. Jede Komponente bleibt ein \(L^2\)-Funktionskanal.

---

## 12. Nur \(P_0\)-Output genügt auf zulässigen Inputs

Für einen zulässigen Input entspricht M1-FULL exakt dem symmetrischen Cover des physischen even Outputs

\[
(I+A)y+HE_{\mathcal A}w.
\]

Daher liegt

\[
\widehat{\mathscr C}_R
\bigl(
\mathscr R_K^{(4)}\oplus\mathscr R_W^{(4)}
\bigr)
\subset
\mathscr R_H^{(4)}.
\tag{IMG.34}
\]

Ein Element von \(\mathscr R_H^{(4)}\) ist wegen IMG.11 genau dann null, wenn seine drei \(P_0\)-Komponenten null sind.

Definiere die \(P_0\)-Outputrestriktion

\[
R_0^{\rm out}:
\mathscr R_H^{(4)}
\to
\bigoplus_{k=0}^{2}L^2(\mathbb T_L).
\tag{IMG.35}
\]

Für den Horizon-Species-Extensionoperator \(E_H\) gilt auf dem zulässigen Outputbild explizit

\[
\boxed{
R_0^{\rm out}E_H
=
I
}
\tag{IMG.35a}
\]

auf dem dreifachen Basislift-Raum, und

\[
\boxed{
E_HR_0^{\rm out}
=
I_{\mathscr R_H^{(4)}}.
}
\tag{IMG.35b}
\]

Insbesondere ist

\[
\boxed{
R_0^{\rm out}\big|_{\mathscr R_H^{(4)}}
\text{ injektiv}.
}
\tag{IMG.35c}
\]

Damit gilt für jeden zulässigen Output \(Y\in\mathscr R_H^{(4)}\)

\[
\boxed{
R_0^{\rm out}Y=0
\iff
Y=0.
}
\tag{IMG.35d}
\]

Dies ist die explizite Output-Seite der Kernelreduktion und wird im IMG0-Zertifikat unabhängig vom Input-Rekonstruktionstest als eigene Assertion geprüft.

---

## 13. Effektiver M1-ND-Operator

Definiere

\[
\boxed{
\mathscr N_R
:=
R_0^{\rm out}
\widehat{\mathscr C}_R
(E_H\oplus E_W)
}
\tag{IMG.36}
\]

auf

\[
\mathscr B_K\oplus\mathscr B_W.
\]

Dann gilt die echte Kernelbijektion

\[
\boxed{
\ker\mathscr N_R
\xrightarrow[\ E_H\oplus E_W\ ]{\sim}
\ker\widehat{\mathscr C}_R
\Big|_{\mathscr R_K^{(4)}\oplus\mathscr R_W^{(4)}}.
}
\tag{IMG.37}
\]

Damit ist M1-ND äquivalent zu

\[
\boxed{
\ker\mathscr N_R=\{0\}.
}
\tag{IMG.38}
\]

Dies ist der erste zulässige **24→6-Reconciliation-Schritt**.

---

# Teil V — Was nach der Kovarianzsubstitution übrig bleibt

## 14. Effektive affine Basismaps für \(P_0\)-Output

Setzt man in die bereits zertifizierten FREE-/HUB-Speciesregeln

\[
F_{g,k}(\theta)
=
F_{P_0,k}(\rho_g(\theta))
\]

ein und behält nur die drei \(P_0\)-Outputrows, entstehen keine neuen affinen Phasen.

Die zehn freien physischen Source-Typen reduzieren modulo \(L\) auf neun verschiedene Basismaps:

\[
\boxed{
\theta,\ 
\theta\pm\Delta,\ 
\theta\pm2\Delta,\ 
-\theta+\Delta,\ 
-\theta+2\Delta,\ 
-\theta+3\Delta,\ 
-\theta+4\Delta.
}
\tag{IMG.39}
\]

Die neun Hubzweige erzeugen:

\[
\boxed{
-\theta+\Delta,\ 
-\theta+2\Delta,\ 
\theta\pm\Delta,\ 
\theta\pm2\Delta,
}
\]

sowie die drei \(B\)-Halbshiftmaps

\[
\boxed{
-\theta+\frac L2+2\Delta,\qquad
\theta+\frac L2-2\Delta,\qquad
\theta+\frac L2+2\Delta.
}
\tag{IMG.40}
\]

Insgesamt besitzt der \(P_0\)-reduzierte Operator exakt

\[
\boxed{12}
\]

verschiedene affine Basismap-Typen.

Diese sind:

- fünf reine Translationen
  \[
  \theta+k\Delta,\qquad k=-2,-1,0,1,2;
  \]
- vier Reflexionen
  \[
  -\theta+k\Delta,\qquad k=1,2,3,4;
  \]
- drei Halbshift-Typen aus IMG.40.

---

## 15. Bedeutung

Der 24-Slot-reine-\(\Delta\)-Cocycle und der 6-Basislift-Operator sind zwei Darstellungen desselben Problems:

### C2/M1

- 24 redundante Inputslots;
- nur reine Basisverschiebungen \(\theta\mapsto\theta+j\Delta\);
- Speciesinformation im Fiberindex.

### IMG-Reduktion

- sechs Basisliftfunktionen;
- Speciesredundanz vollständig entfernt;
- dafür erscheinen zusätzlich Reflexion und Halbshift als endliche Basispullbacks.

Die offene Nichtentartungsfrage wird dadurch nicht gelöst, aber der echte Zustandsraum ist nun explizit.

---


# Teil VI — Analytisches Post-Merge-Hardening

## 16. Warum die Bildraumcharakterisierung wirklich bijektiv ist

Die mechanische Kovarianzprüfung allein reicht nicht. Die benötigte analytische Aussage ist eine explizite Isomorphie zwischen drei Basislift-Funktionskanälen und dem zulässigen zwölf-Slot-Speciesbild.

Definiere zunächst

\[
\mathscr B_H^0
=
\bigoplus_{k=0}^{2}
m_kL^2(\mathbb T_L),
\qquad
f_k=m_kf_k.
\tag{IMG.41a}
\]

Der Species-Extensionoperator ist

\[
\boxed{
(E_Hf)_{g,k}(\theta)
=
f_k(\rho_g(\theta)).
}
\tag{IMG.41b}
\]

Da jede \(\rho_g\) maßtreu ist, ist \(f_k\circ\rho_g\in L^2\). Ferner folgt aus \(f_k=m_kf_k\)

\[
(E_Hf)_{g,k}(\theta)
=
m_k(\rho_g(\theta))
f_k(\rho_g(\theta)),
\]

also besitzt jede Species automatisch den korrekten Lift-Support.

Die \(P_0\)-Restriktion lautet

\[
\boxed{
R_HF
=
(F_{P_0,0},F_{P_0,1},F_{P_0,2}).
}
\tag{IMG.41c}
\]

Wegen \(\rho_{P_0}=\mathrm{id}\) gilt für jedes \(f\in\mathscr B_H^0\)

\[
\boxed{
R_HE_Hf=f.
}
\tag{IMG.41d}
\]

Umgekehrt sei \(F\in\mathscr R_H^{(4)}\). Dann ist definitionsgemäß

\[
F_{g,k}
=
F_{P_0,k}\circ\rho_g.
\]

Daher

\[
(E_HR_HF)_{g,k}
=
F_{P_0,k}\circ\rho_g
=
F_{g,k},
\]

also

\[
\boxed{
E_HR_H
=
I_{\mathscr R_H^{(4)}}.
}
\tag{IMG.41e}
\]

Damit

\[
\boxed{
E_H:
\mathscr B_H^0
\xrightarrow{\sim}
\mathscr R_H^{(4)},
\qquad
E_H^{-1}=R_H.
}
\tag{IMG.41f}
\]

Die Species sind Direktsummenkomponenten, keine Atlas-Charts. Treffen zwei Species dieselbe physische Basisstelle,

\[
\rho_g(\theta)=\rho_h(\eta),
\]

dann stimmen ihre Werte automatisch überein, weil beide aus derselben Basisfunktion \(f_k\) ausgewertet werden. Es entsteht keine zusätzliche Overlap-Konsistenzbedingung.

### 16.1 Rücktransport zu einem echten Horizonwert

Für \(x\in(0,T_0)\) existiert a.e. eindeutig

\[
x=\theta+kL,
\qquad
\theta=[x]_L\in[0,L),
\quad
k\in\{0,1,2\}.
\]

Setze

\[
\boxed{
y_f(x)
=
\sqrt2\,f_k(\theta)
}
\tag{IMG.41g}
\]

und erweitere gerade. Dann

\[
\begin{aligned}
(U_Hy_f)_{g,k}(\theta)
&=
\frac1{\sqrt2}
m_k(\rho_g(\theta))
y_f(\rho_g(\theta)+kL)\\
&=
m_k(\rho_g(\theta))
f_k(\rho_g(\theta))\\
&=
f_k(\rho_g(\theta)).
\end{aligned}
\]

Somit

\[
\boxed{
U_Hy_f=E_Hf.
}
\tag{IMG.41h}
\]

Die umgekehrte Basisliftformel ist

\[
f_k(\theta)
=
\frac1{\sqrt2}
m_k(\theta)y(\theta+kL).
\tag{IMG.41i}
\]

Damit ist nicht nur die Kovarianz notwendig, sondern

\[
\boxed{
\operatorname{Ran}U_H
=
\mathscr R_H^{(4)}
}
\]

auch surjektiv auf den definierten Kovarianzraum.

Für den \(K\)-Unterraum wird lediglich zusätzlich IMG.22 gefordert; daher bleibt

\[
\mathscr R_K^{(4)}
=
E_H(\mathscr B_K).
\]

### 16.2 Annulus

Mit

\[
\mathscr B_W
=
\bigoplus_{k=0}^{2}n_kL^2(\mathbb T_L),
\]

\[
(E_Wg)_{s,k}
=
g_k\circ\rho_s,
\qquad
R_WG=(G_{P_0,0},G_{P_0,1},G_{P_0,2}),
\]

gilt identisch

\[
\boxed{
R_WE_W=I_{\mathscr B_W},
\qquad
E_WR_W=I_{\mathscr R_W^{(4)}}.
}
\tag{IMG.41j}
\]

Die physische Annulusrekonstruktion ist

\[
w_g(x)
=
\sqrt2\,g_k([x]_L),
\qquad
x=[x]_L+kL\in(R,S),
\]

mit ungerader Fortsetzung.

---

## 17. Warum der Output im selben Horizon-Bildraum liegt

Die benötigte Aussage ist **nicht** eine bisher ungeprüfte Ambient-\(G\)-Äquivarianz des formalen \(12\times24\)-M1-Operators.

Auf dem zulässigen Definitionsraum gilt vielmehr die bereits in C1C1 definierte Faktorisierung

\[
\boxed{
\widehat{\mathscr C}_R
=
U_H\,
\widetilde{\mathscr C}_R\,
D,
}
\tag{IMG.42a}
\]

wobei

\[
D
=
(U_H|_K)^{-1}
\oplus
(U_W^{(4)})^{-1}
\]

auf dem echten Bildraum verstanden wird.

Sei

\[
X\in
\mathscr R_K^{(4)}
\oplus
\mathscr R_W^{(4)}.
\]

Setze

\[
(y,w)=DX.
\]

Der physische Output ist

\[
h
=
\widetilde{\mathscr C}_R(y,w)
=
(I+A)y+HE_{\mathcal A}w
\in\mathscr H_+.
\tag{IMG.42b}
\]

Somit

\[
\widehat{\mathscr C}_RX
=
U_Hh
\in
\operatorname{Ran}U_H
=
\mathscr R_H^{(4)}.
\]

Also

\[
\boxed{
\widehat{\mathscr C}_R
\bigl(
\mathscr R_K^{(4)}
\oplus
\mathscr R_W^{(4)}
\bigr)
\subset
\mathscr R_H^{(4)}.
}
\tag{IMG.42c}
\]

Die Output-Kovarianz folgt dann direkt aus der Komponentenformel von \(U_H\):

\[
Y_{g,k}(\theta)
=
\frac1{\sqrt2}
m_k(\rho_g(\theta))
h(\rho_g(\theta)+kL),
\]

während

\[
Y_{P_0,k}(\eta)
=
\frac1{\sqrt2}
m_k(\eta)h(\eta+kL).
\]

Mit \(\eta=\rho_g(\theta)\):

\[
\boxed{
Y_{g,k}(\theta)
=
Y_{P_0,k}(\rho_g(\theta)).
}
\tag{IMG.42d}
\]

**Wichtige Selbstbegrenzung:** IMG.42d wird nur für Outputs aus dem zulässigen physischen Bild behauptet. Es wird ausdrücklich **nicht** gebucht, dass der ambient definierte M1-Matrixoperator auf beliebigen 24-Slot-Funktionen mit der gesamten \(G\)-Aktion vertauscht.

M1-FULL wird hier ausschließlich als Identität der Matrixdarstellung mit demselben transportierten physischen Operator benutzt.

---

## 18. Vollständige Kernelbijektion der \(24\to6\)-Reduktion

Setze

\[
E:=E_H\oplus E_W,
\qquad
R:=R_H\oplus R_W.
\]

Auf den zulässigen Räumen gilt

\[
\boxed{
RE=I,
\qquad
ER=I.
}
\tag{IMG.43a}
\]

Ferner ist

\[
R_0^{\rm out}
\big|_{\mathscr R_H^{(4)}}
\]

injektiv, denn aus IMG.42d folgt

\[
R_0^{\rm out}Y=0
\Longrightarrow
Y_{g,k}=Y_{P_0,k}\circ\rho_g=0.
\tag{IMG.43b}
\]

Definiere wie zuvor

\[
\mathscr N_R
=
R_0^{\rm out}
\widehat{\mathscr C}_R
E.
\]

### Vorwärtsrichtung

Sei

\[
b\in\ker\mathscr N_R.
\]

Dann für

\[
Y:=\widehat{\mathscr C}_REb
\]

gilt

\[
R_0^{\rm out}Y=0.
\]

Nach IMG.42c liegt \(Y\in\mathscr R_H^{(4)}\), und wegen der Injektivität von \(R_0^{\rm out}\) auf diesem Raum folgt

\[
Y=0.
\]

Also

\[
Eb\in\ker\widehat{\mathscr C}_R.
\]

### Rückrichtung

Sei umgekehrt

\[
X\in
\ker\widehat{\mathscr C}_R
\cap
\bigl(
\mathscr R_K^{(4)}
\oplus
\mathscr R_W^{(4)}
\bigr).
\]

Setze

\[
b=RX.
\]

Dann

\[
Eb=ERX=X,
\]

und daher

\[
\mathscr N_Rb
=
R_0^{\rm out}
\widehat{\mathscr C}_RX
=
0.
\]

Somit sind die beiden Kernelabbildungen

\[
E:
\ker\mathscr N_R
\to
\ker\widehat{\mathscr C}_R
\]

und

\[
R:
\ker\widehat{\mathscr C}_R
\to
\ker\mathscr N_R
\]

beidseitig invers:

\[
\boxed{
\ker\mathscr N_R
\xrightarrow[\ E\ ]{\sim}
\ker\widehat{\mathscr C}_R
\Big|_{\mathscr R_K^{(4)}\oplus\mathscr R_W^{(4)}}.
}
\tag{IMG.43c}
\]

Zusammen mit PR #40:

\[
\boxed{
\ker\mathscr N_R
\cong
\ker\widehat{\mathscr C}_R
\cong
\ker\Gamma_I.
}
\tag{IMG.43d}
\]

---

## 19. Owner-Review vom 31. August 2026

Die vorstehenden beiden analytischen Hardening-Punkte wurden nach dem Merge von PR #42 zeilenweise durch den Projektinhaber geprüft.

Bestätigt wurden insbesondere:

1. \(R_HE_H=I\) und \(E_HR_H=I\) mit expliziter Extension/Restriction;
2. keine zusätzliche Atlas-Overlap-Bedingung, da die Species Direktsummenkomponenten sind;
3. der explizite Rücktransport \(f\leftrightarrow y_f\);
4. die Range-Aussage IMG.42c über die Faktorisierung durch \(U_H\);
5. die Kovarianz IMG.42d; zusätzlich im diskreten Kontrollmodell mit Fehler \(0\) überprüft;
6. die beidseitige Kernelreduktion IMG.43c;
7. die Selbstbegrenzung: keine Ambient-\(G\)-Äquivarianzbehauptung.

Verdict:

\[
\boxed{
\mathrm{IMG0\ analytic\ review}:\ \mathrm{ACCEPTED}.
}
\tag{IMG.44}
\]

Diese Abnahme ist **kein** independent GREEN (human) im Registry-Sinn, da dieser Status für externe menschliche Reviewer reserviert ist. Sie erzeugt ebenfalls keine \(\checkmark[M]\)-Promotion.

---

# Teil VII — Nächster zwingender Gate


## 20. M1-ND-IMG1

Der nächste Schritt ist nicht ein Determinantentest.

Aus dem vollständigen M1-FULL-Ledger muss nun direkt der effektive Operator IMG.36 assembliert werden:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!IMG1}:
\text{exakter }3\times6\text{-Funktionskanal-Ledger von }\mathscr N_R.
}
\tag{IMG.41}
\]

Dabei ist für jedes offene \(B_{96}\)-Atom zu prüfen:

1. welche der zwölf Basismaps IMG.39–IMG.40 aktiv sind;
2. welcher Inputlift \(k\in\{0,1,2\}\) getroffen wird;
3. welche A1-/Hubkoeffizienten aggregieren;
4. dass die \(P_0\)-Reduktion exakt dieselbe physische Outputrow ergibt;
5. dass keine künstliche Ambientlösung durch die Reduktion entsteht.

Erst danach ist eine Transfer-/Rekurrenzanalyse sinnvoll.

---

## 21. Status-Firewall

Dieser Kandidat beweist ausschließlich:

- die explizite \(G\)-Kovarianz der symmetrischen 12er Cover;
- die beidseitige Range-Rekonstruktion über \(P_0\);
- die zusätzliche \(K\)-Nebenbedingung als IMG.22;
- die Kernelreduktion des zulässigen M1-ND-Problems von 24 redundanten Slots auf sechs Basislift-Funktionskanäle;
- das endliche 12-Typ-Affinalphabet nach Specieselimination.

Er beweist **nicht**

\[
\ker\Gamma_I=\{0\},
\]

keine Injektivität von \(\mathscr N_R\), keine Closed-Range-Aussage und keinen Gegenvektor.

Aktueller Status:

\[
\boxed{
\mathrm{M1\!-\!ND\!-\!IMG0}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate, algebraic/mechanical scope)}
+
\text{owner analytic review ACCEPTED}
}
\]

Keine \(\checkmark[M]\)-Promotion. Der nächste freigegebene Arbeitsknoten ist M1-ND-IMG1.
