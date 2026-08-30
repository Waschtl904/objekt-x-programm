# P11/R32 — SW1 A-FOLD Reconciliation Audit

> **Stand:** 30. August 2026  
> **Basis:** `main@2b7c54edada3e00f4bc61e1ce67b30c0e05ba0f3`  
> **Status:** Kandidat; keine Promotion. Ziel ist eine exakte unitäre Brücke zwischen dem Vollraum-Blocksystem, der Odd/even-Halbachsenfaltung und dem bereits vorhandenen SW1-A0/A1-Rohsystem.  
> **Scope-Firewall:** keine neue Injektivitätsaussage, kein HT-RED, kein Objekt-X- oder RH-Schluss.

---

## 0. Warum dieses Lemma noch gebraucht wird

Die Einzelbausteine existieren bereits:

- RB.5--RB.9 in `P11_P12_R32_RUECKBINDUNG_AUDIT.md` geben die unitäre Odd-Faltung des Annulus-Hubs;
- KNF.10 in `P11_R32_SW1_KNF_CANDIDATE.md` gibt die positive Row der zweiten augmentierten Gleichung;
- A0 deckt die freien (z/h)-Koordinaten auf SW1 exhaustiv ab;
- A1 gibt das vollständige positive finite-cell Rohsystem der ersten augmentierten Gleichung;
- SE.15--SE.16 geben (A=R^*R) als Summe von genau elf endlichen (K^*M_\Omega K)-Wörtern.

Was bisher fehlt, ist eine einzige explizite Äquivalenzkette

[
\boxed{
\text{Vollraum-Blocksystem}
\iff
\text{unitär gefaltetes Halbachsensystem}
\iff
\text{A0/A1-Rohsystem}.
}
]

A-FOLD schließt ausschließlich diese Brücke.

---

## 1. Räume und unitäre Faltungen

Setze

[
\mathscr H:=L^2(-T_0,T_0),\qquad
\mathscr H^\pm:=L^2(-T_0,T_0)^\pm.
]

Definiere

[
F_+:L^2(0,T_0)\to\mathscr H^+,
\qquad
(F_+f)(x)=2^{-1/2}f(|x|),
\tag{AF.1}
]

und

[
F_-:L^2(0,T_0)\to\mathscr H^-,
\qquad
(F_-g)(x)=2^{-1/2}\operatorname{sgn}(x)g(|x|).
\tag{AF.2}
]

Für (x=0) ist der Wert irrelevant. Direkt gilt

[
\|F_+f\|_{L^2(-T_0,T_0)}^2
=
2\cdot\frac12\|f\|_{L^2(0,T_0)}^2
=
\|f\|^2,
\tag{AF.3}
]

und ebenso für (F_-). Beide Abbildungen sind surjektiv auf die jeweiligen Paritätssektoren; daher unitär. Auf der positiven Halbachse lauten die Inversen

[
(F_+^{-1}y)(t)=\sqrt2,y(t),\qquad
(F_-^{-1}v)(t)=\sqrt2,v(t).
\tag{AF.4}
]

Für den Annulus und das innere Intervall benutzen wir die analogen unitarisierten Odd-Extensions

[
\mathcal O_{R,S}:L^2(R,S)\xrightarrow{\sim}\mathscr H_{\mathcal A}^-,
\qquad
\mathcal O_{0,R}:L^2(0,R)\xrightarrow{\sim}\mathscr H_I^-,
\tag{AF.5}
]

wobei (\mathcal O_{R,S}) exakt RB.5 ist.

---

## 2. A-FOLD-1 — Faltung der inneren Hubrow

Im Drei-Shift-Fenster ist

[
H
=
P_{T_0}
\bigl(
pD_{2a}+rD_{2b}+qD_{2T}
\bigr)
E_{T_0},
\qquad
D_{2\tau}=U_\tau-U_{-\tau}.
\tag{AF.6}
]

Für gerades (F_+f) und (u>0) ergibt direkte Substitution

[
\begin{aligned}
(F_-^{-1}HF_+f)(u)
={}&p\,[f(|u-a|)-f(u+a)]\\
&+r\,[f(|u-b|)-f(u+b)]\\
&+q\,[f(|u-T|)-f(u+T)],
\end{aligned}
\tag{AF.7}
]

jeweils mit den ursprünglichen Horizon-Cuts.

Auf SW1 gilt

[
0<u<R<\varepsilon,
\qquad
2R<R+\varepsilon<\Delta<e<d<a<T,
\tag{AF.8}
]

also (u<a,b,T), und KNF.9 garantiert, dass alle sechs Branchwerte im Horizont liegen. Daher wird AF.7 zu

[
\boxed{
\begin{aligned}
(\mathcal O_{0,R}^{-1}E_I^*HF_+f)(u)
={}&p[f(a-u)-f(a+u)]\\
&+r[f(b-u)-f(b+u)]\\
&+q[f(T-u)-f(T+u)]
\end{aligned}}
\tag{AF.9}
]

für fast jedes (0<u<R).

Dies ist exakt die unitär normalisierte Form von KNF.10. Wenn (y=F_+f), dann (f=\sqrt2,y|_{(0,T_0)}); deshalb ist AF.9 genau (\sqrt2) mal die unnormalisierte positive KNF-Row. Der Nullraum ist identisch.

---

## 3. A-FOLD-2 — Faltung des Annulus-Hubs

RB.5--RB.8 beweisen bereits

[
\boxed{
F_+^{-1}HE_{\mathcal A}\mathcal O_{R,S}
=
L_{R,S,T_0}^{\{a,b,2a\}}.
}
\tag{AF.10}
]

Damit ist die erste augmentierte Hubquelle unter der unitären Faltung exakt der kanonische P12-Rohoperator; es gibt keinen zusätzlichen Normierungsfaktor.

Für die spätere A1-Firewall ist insbesondere der rechte (T)-Ast wichtig. Schreibe

[
S=T+\sigma.
\tag{AF.11}
]

Für (x>0) ist

[
S-(T+x)=\sigma-x.
\tag{AF.12}
]

Auf SW1 gilt (T>R), also ist die untere Annulusgrenze für (T+x) automatisch erfüllt. Folglich ist der rechte (T)-Ast genau für

[
0<x<\sigma
\tag{AF.13}
]

aktiv und trägt aus (D_{2T}=U_T-U_{-T}) den Koeffizienten

[
\boxed{-q,w(T+x).}
\tag{AF.14}
]

Für (x>\sigma) gilt (T+x>S), also ist dieser Ast tot. Ferner

[
T_0-(T+x)=\varepsilon-x,
\tag{AF.15}
]

und wegen (x<\sigma\le R<\varepsilon) ist der aktive Ast automatisch horizon-legal. Damit ist die in A1.16 verwendete Schwelle **exakt (\sigma)**.

---

## 4. A-FOLD-3 — Faltung von (A=R^*R) ohne Faktor-2-Drift

Die Full-Rest-Faktorisierung liefert im Drei-Shift-Fenster

[
A
=
(\log2)\Phi_{2,0}^*M_{\Omega_{2,0}}\Phi_{2,0}
+
2(\log2)\Phi_{2,1}^*M_{\Omega_{2,1}}\Phi_{2,1}
+
2(\log3)\Phi_{3,0}^*M_{\Omega_{3,0}}\Phi_{3,0},
\tag{AF.16}
]

und nach Expansion genau (9+1+1=11) endliche (K^*M_\Omega K)-Wörter.

Jedes (K_s^{\rm tr}) enthält eine Differenztranslation und wechselt daher die Parität. Definiere

[
\widehat K_s
:=
F_-^{-1}K_s^{\rm tr}F_+.
\tag{AF.17}
]

Die Cutoffs (M_\Omega) sind gerade, weil alle (Omega) symmetrische Intervalle um (0) sind. Daher

[
F_-^{-1}M_\Omega F_-
=
M_{\Omega^+},
\qquad
\Omega^+:=\Omega\cap(0,T_0).
\tag{AF.18}
]

Aus der Unitarität von (F_\pm) folgt für jedes Wort exakt

[
\boxed{
F_+^{-1}
(K_s^{\rm tr})^*
M_\Omega
K_t^{\rm tr}
F_+
=
\widehat K_s^*
M_{\Omega^+}
\widehat K_t.
}
\tag{AF.19}
]

Insbesondere ändern sich weder Wortgewicht noch Vorzeichen noch Wortanzahl. Es entsteht **kein Faktor 2**.

Setze

[
\widehat A:=F_+^{-1}AF_+.
\tag{AF.20}
]

Dann ist (\widehat A) exakt der gerade positive Halbachsenoperator aus denselben elf Wörtern. Für (y=F_+f) gilt punktweise auf der positiven Halbachse

[
f=\sqrt2,y,
\qquad
F_+^{-1}Ay=\sqrt2,(Ay)|_{(0,T_0)}.
\tag{AF.21}
]

Da jede A1-Row linear homogen in den (y)-Werten ist, canceln die beiden (\sqrt2)-Faktoren termweise. Damit bleiben sämtliche Koeffizienten in A1.3--A1.13 exakt unverändert.

---

## 5. A-FOLD-4 — unitäre Blockoperator-Äquivalenz

Definiere die Domain- und Codomain-Unitaries

[
U
:=
F_+\oplus\mathcal O_{R,S},
\tag{AF.22}
]

[
V
:=
F_+\oplus\mathcal O_{0,R}.
\tag{AF.23}
]

Für den augmentierten Vollraumoperator SE.3

[
\mathcal K_{I,A}
\binom yw
=
\binom{(I+A)y+HE_{\mathcal A}w}{E_I^*Hy}
\tag{AF.24}
]

setze

[
\boxed{
\widehat{\mathcal K}_{I,A}
:=
V^{-1}\mathcal K_{I,A}U.
}
\tag{AF.25}
]

Dann

[
\boxed{
\widehat{\mathcal K}_{I,A}
\binom fg
=
\binom{(I+\widehat A)f+\widehat H_{\mathcal A}g}
{\widehat H_I f},
}
\tag{AF.26}
]

mit

[
\widehat H_{\mathcal A}
=
F_+^{-1}HE_{\mathcal A}\mathcal O_{R,S},
\qquad
\widehat H_I
=
\mathcal O_{0,R}^{-1}E_I^*HF_+.
\tag{AF.27}
]

Da (U,V) unitär und insbesondere bijektiv sind,

[
\boxed{
\ker\widehat{\mathcal K}_{I,A}
=
U^{-1}(\ker\mathcal K_{I,A}).
}
\tag{AF.28}
]

Somit gilt die echte Bijektivitätsaussage

[
\boxed{
\ker\mathcal K_{I,A}=\{0\}
\iff
\ker\widehat{\mathcal K}_{I,A}=\{0\}.
}
\tag{AF.29}
]

Es gibt weder verlorene noch zusätzliche Lösungen.

---

## 6. A-FOLD-5 — Reconciliation mit A0/A1

A0 zerlegt den freien geraden Quellenraum auf SW1 über den positiven physischen Support. Die unitäre Skalierung

[
f=\sqrt2,y|_{(0,T_0)}
\tag{AF.30}
]

ändert weder wesentlichen Support noch Zellgrenzen. Daher bleiben sämtliche A0-Zellen, einschließlich

[
(T+R,T_0)
\tag{AF.31}
]

und die Randlagen

[
\sigma=R,
\qquad
\varepsilon=\Delta/2,
\tag{AF.32}
]

unverändert.

A1 wertet auf denselben positiven Zellen die erste Vollraumgleichung aus. Nach AF.19--AF.21 ist ihre 11-Wort-Seite exakt (\widehat A); nach AF.10 ist ihre Hubseite exakt (\widehat H_{\mathcal A}). Somit ist A1.23/A1.24 in den normierten Variablen nichts anderes als die erste Zeile von AF.26.

Die KNF-Rekonstruktion der zweiten Zeile ist durch AF.9 exakt dieselbe Nullbedingung.

Damit gilt a.e. auf SW1 die Kette

[
\boxed{
\mathcal K_{I,A}(y,w)=0
\iff
\widehat{\mathcal K}_{I,A}(f,g)=0
\iff
\text{A0/A1-Rohsystem in den gefalteten Koordinaten}=0,
}
\tag{AF.33}
]

mit ((y,w)=U(f,g)).

---

## 7. A-FOLD-PARAM — unveränderte SW1-Parameter-Firewall

Die Faltungen (F_\pm,\mathcal O_{R,S},\mathcal O_{0,R}) wirken ausschließlich auf der Raumvariablen und auf der Parität. Sie ändern keine der Parameterdefinitionen

[
S=T+\sigma,
\qquad
T_0=T+\varepsilon.
\tag{AF.34}
]

Insbesondere bleibt die SW1-Bedingung wortgleich

[
\boxed{
0<\sigma\le R<\varepsilon,
\qquad
R+\varepsilon<\Delta.
}
\tag{AF.35}
]

Die beiden für die kritische (T)-Tail-Umschaltung relevanten exakten Identitäten sind

[
S-(T+x)=\sigma-x,
\tag{AF.36}
]

[
(T+R)-S=R-\sigma.
\tag{AF.37}
]

Damit kann keine Faltungs- oder Wortsubstitution aus (\sigma\le R) einen Fall (\sigma>R) erzeugen. Jede spätere Hilfsvariable ist gegen AF.34 zurückzuschreiben; nur die ursprünglichen (\sigma,R,\varepsilon) dürfen die P12-RT-Firewall steuern.

---

## 8. Status und Firewall

Wenn das algebraisch/mechanische Zertifikat und ein unabhängiger Audit dieses Dokument bestätigen, ist der angemessene Status

[
\boxed{
\mathrm{SW1!-!A!-!FOLD}:
\text{AI-GREEN candidate}
+
\text{independent GREEN (certificate)}
}
]

ohne formale Promotion.

A-FOLD beweist ausdrücklich **nicht**

- die Injektivität des A1-Rohsystems;
- (\ker\Gamma_I=\{0\});
- HT-RED;
- Closed Range / bounded below;
- Objekt X;
- RH.

Der nächste mathematische Schritt nach A-FOLD ist nicht ein Neuaufbau von A0/A1, sondern die Reconciliation des bestehenden A2--A10-Stacks mit AF.33 und anschließend der eigentliche Nichtentartungstest.
