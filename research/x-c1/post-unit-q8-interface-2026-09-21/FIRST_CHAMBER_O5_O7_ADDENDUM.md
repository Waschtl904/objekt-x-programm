# Erste geschlossene Kammer: Nachtrag zu O5–O7

2026-09-22. Gemeinsamer lokaler Ergebnisstand mit dem Basisdokument:
**FIRST-CHAMBER RAW T/D COCYCLE, O1–O7 — AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Dieser Nachtrag ändert für sich allein keinen globalen Registry-Status.

Ergänzung zu [FIRST_CHAMBER_RAW_TD_O1_O4.md](FIRST_CHAMBER_RAW_TD_O1_O4.md).
Das Basisdokument enthält O1–O4; dieser Nachtrag ergänzt O5 und O6 samt
uniformer Kontrolle für O7. Beide Texte verwenden denselben Scope
\[
1\le A\le B\le C\le A_8=\frac12\log8.
\]

## 1. Bereits konstruierte Daten

Es gelten die dort definierten Quellen \(W_A\), die explizite Fortsetzung
\(F_A\), die abgeschlossenen Carrier \(\mathcal H_A^T,\mathcal H_A^D\), die
isometrischen Inklusionen \(M^T,M^D\) und die beiden Cocycle-Gesetze.

Die Multiplikatoren sind kammerweit dieselben:
\[
h=g+s,\quad m=g+\omega-c,\quad n=\kappa+\omega+c,\quad
t=\frac m{\sqrt h},\quad d=\frac n{\sqrt h},
\]
\[
m\ge g\ge0,\quad \kappa\le n\le s<12,\quad t^2-d^2=w=g-\kappa-2c.
\]
Die exakte Eingabe
\[
10<s<\frac{23}{2}<12
\]
ist C1a, Gleichung (5), Commit
\`5557d94d048dc05e7c3b4534a5a2d1711bdc71dc\`.

## 2. Uniformer Gamma-Floor

Für \(u\in W_A\) ist
\[
\Gamma[u]=\int_0^\infty k(r)\|\tau_ru-u\|_2^2\,dr,\qquad
k(r)=\frac{e^{-r/2}}{1-e^{-2r}}.
\]
Für \(r>2A\) sind die Träger disjunkt bis auf Nullmengen, also
\[
\|\tau_ru-u\|_2^2=2\|u\|_2^2.
\]
Für \(u\ne0\) folgt
\[
\Gamma[u]\ge2\|u\|_2^2\int_{2A}^\infty k(r)\,dr
>4e^{-A}\|u\|_2^2.
\]
Da \(A\le A_8\),
\[
4e^{-A}\ge4e^{-A_8}=\sqrt2>\frac43.
\]
Damit
\[
\boxed{\Gamma[u]>\frac43\|u\|_2^2\quad(u\ne0),}
\]
und für alle \(u\in W_A\) die nichtstrikte Fassung
\[
\Gamma[u]\ge\frac43\|u\|_2^2.
\]

## 3. Jensen-Schritt und untere T-Schranke

Für \(u\ne0\) setze
\[
d\mu=\frac{|\widehat u(\xi)|^2}{\|u\|_2^2}\,d\xi.
\]
Mit
\[
f_s(x)=\frac{x^2}{x+s},\qquad f_s''(x)=\frac{2s^2}{(x+s)^3}>0
\]
und \(m\ge g\) ergibt Jensen
\[
\frac{\|T_Au\|^2}{\|u\|_2^2}
\ge \int f_s(g)\,d\mu
\ge f_s\!\left(\frac{\Gamma[u]}{\|u\|_2^2}\right)
> f_{12}(4/3)=\frac2{15}.
\]
Somit
\[
\boxed{\|T_Au\|^2>\frac2{15}\|u\|_2^2\quad(u\ne0),}
\qquad
\boxed{\|D_Au\|^2\le s\|u\|_2^2.}
\]
Für alle Quellen gilt nichtstrikt
\[
\|T_Au\|^2\ge\frac2{15}\|u\|_2^2,\qquad
\|D_Au\|^2\le12\|u\|_2^2.
\]

## 4. O5: Defektoperator und Intertwining

Auf dem dichten Rohbild definiere
\[
R_A^0(T_Au)=D_Au.
\]
Die untere T-Schranke liefert Wohldefiniertheit. Ferner
\[
\|D_Au\|^2
\le\frac{15s}{2}\|T_Au\|^2
\le90\|T_Au\|^2.
\]
Daher besitzt \(R_A^0\) die eindeutige beschränkte Fortsetzung
\[
\boxed{
R_A:\mathcal H_A^T\to\mathcal H_A^D,\qquad
\|R_A\|\le\sqrt{90}.}
\]
Auf \(T_A(W_A)\) gilt
\[
\begin{aligned}
R_BM^T_{A,B}T_Au
&=R_BT_BJ_{A,B}u\\
&=D_BJ_{A,B}u\\
&=M^D_{A,B}D_Au\\
&=M^D_{A,B}R_AT_Au.
\end{aligned}
\]
Durch Dichte und Beschränktheit:
\[
\boxed{R_BM^T_{A,B}=M^D_{A,B}R_A.}
\]

## 5. Normäquivalenz der Quellenvervollständigung

Für die explizite Kammervervollständigung
\[
\|u\|_{A,17}^2=q_A[u]+17\|u\|_2^2
=\|T_Au\|^2+17\|u\|_2^2-\|D_Au\|^2
\]
gilt
\[
\boxed{
\|T_Au\|^2\le\|u\|_{A,17}^2
\le\frac{257}{2}\|T_Au\|^2.}
\]
Links wird \(d^2\le s<12<17\) verwendet; rechts die untere T-Schranke.
Damit ist
\[
T_A:F_A\xrightarrow{\cong}\mathcal H_A^T
\]
ein beschränkter Hilbertraumisomorphismus auf den Carrier.

## 6. O6: Formnaturality

Auf der Kammer ist
\[
w=g-\kappa-2c,\qquad b=w+17\ge g+17-s>g+5.
\]
Punktweise gilt
\[
|w|\le g+s\le \frac{12}{5}\,b.
\]
Daher
\[
|q_A(u,v)|
\le\frac{12}{5}\|u\|_{A,17}\|v\|_{A,17}.
\]
Für \(u,v\in W_A\) liefert physische Nullfortsetzung
\[
\begin{aligned}
q_B(J_{A,B}u,J_{A,B}v)
&=\int w\,
\overline{\widehat{Z_BJ_{A,B}u}}
\widehat{Z_BJ_{A,B}v}\,d\xi\\
&=\int w\,
\overline{\widehat{Z_Au}}\widehat{Z_Av}\,d\xi\\
&=q_A(u,v).
\end{aligned}
\]
Stetigkeit und Dichte ergeben
\[
\boxed{
q_B(J_{A,B}u,J_{A,B}v)=q_A(u,v)
\quad(u,v\in F_A).}
\]

## 7. O7-Scope und Firewall

Zusammen mit dem Basisbeweis sind auf der gesamten ersten geschlossenen Kammer
O1–O7 autorenseitig geschlossen:

- Quellen und explizite C0-Fortsetzung \(F_A\);
- zwei getrennte Rohtransporte \(M^T,M^D\);
- Identitäts- und Cocycle-Gesetze;
- Defektoperatoren \(R_A\) mit \(\|R_A\|\le\sqrt{90}\);
- typkorrektes R-Intertwining;
- Formnaturality auf \(F_A\);
- uniforme Normkontrollen.

Status:
**FIRST-CHAMBER RAW T/D COCYCLE, O1–O7 — AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.

Dies schließt weder den unbeschränkten \`TERMINAL-HORIZON-C1-COCYCLE\` noch
O8. Insbesondere folgt aus \(\|R_A\|\le\sqrt{90}\) keine Kontraktion und keine
Positivität von \(I-R_A^*R_A\). Nicht behauptet werden ein gemeinsames \(V\),
signierte Operatorkongruenz, positive korrigierte Transporte, Positivität für
neue Terminals, q=8-Wall-Crossing, kofinale C1-Geometrie, globales Objekt X,
globale Weil-Positivität oder RH.
