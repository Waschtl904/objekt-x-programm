# Audit-Kandidat: SW1-Δ-DESCENT — Stage 1/2: Rows bei 2d±s

> **Stand:** 29. August 2026  
> **Repo-Basis:** `main@83f07adf9136d416181d6f38779cd452eb6a4472`  
> **Status:** `?[O]` — Stage 1/2 hergeleitet, adversarialer Re-Review und Zertifikat noch ausstehend; keine Promotion.  
> **Scope:** ausschließlich die direkte 11-Wort-Ableitung und Hub-Auswertung bei (x=2dpm s) auf SW1.

---

## 0. Firewall

Dieses Audit beweist noch **keine** (Delta)-Rekurrenz und keine finite Terminierung.

Insbesondere kein:
- HT-RED;
- A0;
- (kerGamma_I={0});
- Full-Rest-Abschluss;
- Objekt X;
- RH.

Die historischen Scratch-Formeln für ((Ay)(2dpm s)) werden **nicht als Input** verwendet. Input sind nur HT.3/HT.4 aus
`audits/P11_R32_TAIL_FG_PIVOT_CANDIDATE.md`
sowie die bereits auf main verfügbaren SW1-2TP-/SW1-AWI-Strukturen erst **nach** Abschluss der direkten Row-Ableitung.

---

## 1. Setup

[
a=rac12log2,quad b=rac12log3,quad T=2a,
]
[
d=b-a,quad e=T-b,quad Delta=d-e=2d-a,
]
und
[
0<sigmale R<arepsilon,qquad R+arepsilon<Delta,qquad T_0=T+arepsilon.
	ag{DD.1}
]

Für
[
R<s<arepsilon
	ag{DD.2}
]
setzen wir
[
x_pm:=2dpm s=a+Deltapm s.
	ag{DD.3}
]

Die Vier-Echo-Formel lautet
[
egin{aligned}
(W_{delta,eta}^{(lambda)}y)(x)
={}&-chi_lambda(x-delta)widetilde y(x-delta-eta)
+chi_lambda(x-delta)widetilde y(x-delta+eta)\
&+chi_lambda(x+delta)widetilde y(x+delta-eta)
-chi_lambda(x+delta)widetilde y(x+delta+eta),
end{aligned}
	ag{DD.4}
]
mit
[
chi_lambda(u)=1_{{|u|le T_0-lambda}}.
]

---

## 2. Stage 1 — vollständiges 11-Wort-Ledger

### 2.1 Uniformes Gate-Muster

Für beide Rows (x=2dpm s) gilt auf ganz SW1:

- Wörter 1–6 und 11: linkes Gate (x-delta) offen;
- Wörter 7–10: linkes Gate geschlossen;
- für alle elf Wörter: rechtes Gate (x+delta) geschlossen.

Damit können nur (E_1,E_2) der Wörter 1–6 und 11 beitragen.

Die einzige nicht-uniforme **Source-Horizon**-Entscheidung tritt bei (x=2d-s) auf:
[
T+Delta-s<T_0
iff
s>Delta-arepsilon.
	ag{DD.5}
]

Definiere deshalb
[
J:=(Delta-arepsilon,arepsilon).
	ag{DD.6}
]
Ist (arepsilonleDelta/2), ist (J) leer (bis auf den L2-nulligen Berührfall bei Gleichheit). Ist (arepsilon>Delta/2), ist dies exakt der bereits durch SW1-AWI normalisierte Überlapp.

### 2.2 Row (x=2d+s)

| Wort | überlebender Beitrag |
|---:|---|
| 1 | (-c_1y(2e-s)+c_1y(2d+s)) |
| 2 | (-c_2y(T-Delta-s)) |
| 3 | (0) |
| 4 | (-c_4y(T-Delta-s)+c_4y(Delta+s)) |
| 5 | (+c_5y(2d+s)) |
| 6 | (0) |
| 7 | (0) |
| 8 | (0) |
| 9 | (0) |
| 10 | (0) |
| 11 | (-c_{11}y(T-s)+c_{11}y(2d+s)) |

Exakt acht Echo-Beiträge überleben.

### 2.3 Row (x=2d-s), außerhalb (J)

Für
[
s<Delta-arepsilon
	ag{DD.7}
]
gilt:

| Wort | überlebender Beitrag |
|---:|---|
| 1 | (-c_1y(2e+s)+c_1y(2d-s)) |
| 2 | (-c_2y(T-Delta+s)) |
| 3 | (0) |
| 4 | (-c_4y(T-Delta+s)+c_4y(Delta-s)) |
| 5 | (+c_5y(2d-s)) |
| 6 | (0) |
| 7 | (0) |
| 8 | (0) |
| 9 | (0) |
| 10 | (0) |
| 11 | (-c_{11}y(T+s)+c_{11}y(2d-s)) |

Wieder exakt acht Echo-Beiträge.

### 2.4 Row (x=2d-s), auf (J)

Für
[
s>Delta-arepsilon
	ag{DD.8}
]
überleben zusätzlich genau:
[
+c_2y(T+Delta-s)
]
aus Wort 2 und
[
+c_6y(T+Delta-s)
]
aus Wort 6.

Also insgesamt zehn Echo-Beiträge.

Da
[
c_2+c_6=eta_+,
	ag{DD.9}
]
ist die gesamte Umschaltung exakt
[
1_J(s),eta_+,y(T+Delta-s).
	ag{DD.10}
]

**Struktureller Punkt:** Für (sin J) ist
[
t:=Delta-sin Jsubset(R,arepsilon),
]
also
[
T+Delta-s=T+t
]
wieder eine echte SW1-Tail-Koordinate. Genau hier kann später SW1-2TP eingesetzt werden; dies wird in Stage 1 noch nicht benutzt.

---

## 3. Stage 2 — aggregierte A-Rows

Mit
[
alpha_b:=c_1+c_5+c_{11}>0,
	ag{DD.11}
]
[
eta_-:=-c_2-c_4,qquad
eta_+:=c_2+c_6,qquad
eta_b:=-c_{11},
	ag{DD.12}
]
und (c_4=c_2) folgt

[
oxed{
egin{aligned}
(Ay)(2d+s)
={}&-c_1y(2e-s)
+alpha_b y(2d+s)
+eta_-y(T-Delta-s)\
&+c_2y(Delta+s)
+eta_b y(T-s).
end{aligned}}
	ag{DD.13}
]

Für die gespiegelte Row:

[
oxed{
egin{aligned}
(Ay)(2d-s)
={}&-c_1y(2e+s)
+alpha_b y(2d-s)
+eta_-y(T-Delta+s)\
&+c_2y(Delta-s)
+eta_b y(T+s)
+1_J(s)eta_+y(T+Delta-s).
end{aligned}}
	ag{DD.14}
]

Die einzige Piecewise-Struktur ist damit exakt der bereits bekannte AWI-Bereich (J).

---

## 4. Stage 2 — Hub bei (2dpm s)

Für den Annulus-Hub
[
(HE_{mathcal A}w)(u)
=
p[w(u-a)-w(u+a)]
+r[w(u-b)-w(u+b)]
+q[w(u-T)-w(u+T)]
	ag{DD.15}
]
sind bei (u=2dpm s) sämtliche rechten Äste annulus-tot.

Da
[
2d-a=Delta,qquad
2d-b=-e,qquad
2d-T=-2e,
]
und (w) ungerade ist, folgt uniform auf SW1:

[
oxed{
(HE_{mathcal A}w)(2d+s)
=
p,w(Delta+s)-r,w(e-s)-q,w(2e-s),
}
	ag{DD.16}
]

[
oxed{
(HE_{mathcal A}w)(2d-s)
=
p,w(Delta-s)-r,w(e+s)-q,w(2e+s).
}
	ag{DD.17}
]

Alle sechs linken Argumentbeträge liegen strikt im Annulus:
[
R<Delta-s<Delta+s<T,
]
[
R<e-s<e+s<T,
]
[
R<2e-s<2e+s<T<S,
]
wobei für die knappen unteren Schranken (R+s<R+arepsilon<Delta<e) verwendet wird.

---

## 5. Augmentierte Rows

Aus
[
(I+A)y+HE_{mathcal A}w=0
]
folgt

[
oxed{
egin{aligned}
0={}&(1+alpha_b)y(2d+s)
+eta_-y(T-Delta-s)
+c_2y(Delta+s)
+eta_b y(T-s)
-c_1y(2e-s)\
&+p,w(Delta+s)-r,w(e-s)-q,w(2e-s),
end{aligned}}
	ag{DD.18}
]

und

[
oxed{
egin{aligned}
0={}&(1+alpha_b)y(2d-s)
+eta_-y(T-Delta+s)
+c_2y(Delta-s)
+eta_b y(T+s)\
&+1_J(s)eta_+y(T+Delta-s)
-c_1y(2e+s)\
&+p,w(Delta-s)-r,w(e+s)-q,w(2e+s).
end{aligned}}
	ag{DD.19}
]

Der direkte Diagonalpivot
[
1+alpha_b>1
	ag{DD.20}
]
ist strikt positiv. Das allein beweist noch keine (Delta)-Rekurrenz.

---

## 6. Nächste zu beweisende Stufe

Erst nach separatem Re-Review und Zertifizierung von (DD.13)–(DD.19):

1. ersetze die (Tpm s)-Kanäle mit dem zertifizierten SW1-2TP;
2. behandle auf (J) den zusätzlichen Tailwert (T+Delta-s) mit (t=Delta-s) und SW1-2TP/AWI;
3. identifiziere danach, ob die verbleibenden (Deltapm s)-Kanäle tatsächlich eine geschlossene Rekurrenz erzeugen;
4. beweise erst dann finite Terminierung.

Bis dahin:
[
oxed{mathrm{SW1!-!Delta DESCENT}:?[O].}
]
