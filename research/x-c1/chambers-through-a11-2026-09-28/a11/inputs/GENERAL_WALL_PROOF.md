# Allgemeines Ein-Wand-Lemma für die gekoppelte C1a-Familie

27. September 2026 · **AUTHOR_DERIVED_LOCAL / EXTERNAL_REVIEW_OPEN**

## Ergebnis und Voraussetzungen

Der O10-Rohmechanismus gilt an jeder einzelnen Prime-Power-Wand der festen
C1a-Familie und lässt sich über jede **endliche Folge von Wänden**
zusammensetzen. Die Abschätzungen hängen ausdrücklich von den Wanddaten ab.
Die q=9-Wand ist eine zweite konkrete Instanz; siehe [Q9.md](Q9.md).

Fest bleiben die ursprünglichen beiden Mellinbedingungen, die physische
Nullfortsetzung, die unitäre Fourierkonvention mit `exp(−ixξ)` und die
volle Gammafunktion

$$
g(\xi)=\sum_{j\ge0}\frac{2\xi^2}{\lambda_j(\lambda_j^2+\xi^2)},
\qquad \lambda_j=2j+\tfrac12.
\tag{1}
$$

Die Voraussetzungen für eine einzelne Wand sind:

1. Eine endliche alte Familie positiver Gewichte `w_q` mit Verschiebungen
   `ℓ_q`, ein festes `κ>0` und ein neuer Kanal `(v,ℓ)` mit `v>0`, `ℓ>0`.
2. Die gekoppelten Symbole werden genau nach (2)–(3) aktualisiert.
3. Für die Formnaturality liegt der alte Träger in `[-A,A]` mit `2A≤ℓ`.
4. Für gleichzeitige Aussagen über ganze Quellenräume wird ein beliebiger
   endlicher maximaler Horizont L festgelegt.

Für Prime-Power-Kanäle gilt `ℓ=log(q*)`, `v=Λ(q*)/sqrt(q*)` und die strikte
Aktivierung `ℓ<2A`. Die Aussagen über die vollständigen Carrier verwenden (1),
nicht eine beliebige neu gewählte Gammafunktion. Positivität der gesamten
neuen Form ist **keine** Voraussetzung des Rohsatzes.

## 1. Gekoppelte Aktualisierung

Mit `ω=Σw_q`, `c(ξ)=Σw_q cos(ℓ_q ξ)` seien

$$
s=\kappa+2\omega,\quad h=g+s,\quad
m=g+\omega-c,\quad n=\kappa+\omega+c,\quad
t=m/\sqrt h,\quad d=n/\sqrt h.
\tag{2}
$$

Schreibe `z=cos(ℓξ)`. Dann ist die Aktualisierung

$$
m_+=m+v(1-z),\qquad n_+=n+v(1+z),\qquad h_+=h+2v.
\tag{3}
$$

Es gelten `m≥g`, `n≥κ`, `m+n=h`, `0≤m≤h` und `n≤s`.
Insbesondere entstehen die alten/neuen Kreuzterme durch das Quadrieren
derselben Zähler. Aus der Differenz der Quadrate folgt exakt

$$
t^2-d^2=w:=g-\kappa-2c,\qquad w_+-w=-2v\cos(\ell\xi).
\tag{4}
$$

## 2. Universelle Schranke für den kritischen Quotienten

Für **jedes** endliche `ℓ≥0` gilt

$$
0\le1-\cos(\ell\xi)\le C_\ell g_0(\xi)\le C_\ell g(\xi),
\quad C_\ell=\max\{1,\ell^2/16\},\quad
g_0(\xi)=\frac{4\xi^2}{1/4+\xi^2}.
\tag{5}
$$

Für `|ξ|≤1/2` benutzt man
`1−cos(ℓξ)≤ℓ²ξ²/2`, `g₀(ξ)≥8ξ²` und `8C_ℓ≥ℓ²/2`.
Für `|ξ|≥1/2` benutzt man `1−cos(ℓξ)≤2≤g₀(ξ)` und `C_ℓ≥1`.
Bei Null sind beide Seiten null. Der letzte Vergleich in (5) ist der
erste positive Summand der vollständigen Reihe (1).

Damit wird die Nullstelle `m(0)=0` durch eine Schranke auf einem ganzen
Frequenzbereich behandelt. Für fast alle ξ gelten

$$
1\le\frac{m_+}{m}\le1+vC_\ell,\qquad
1\le\frac{n_+}{n}\le1+\frac{2v}{\kappa},\qquad
\frac{s}{s+2v}\le\frac h{h+2v}\le1.
\tag{6}
$$

Folglich besitzen die **zwei getrennten** Wandmultiplikatoren

$$
a_T=\frac{m_+}{m}\sqrt{\frac h{h_+}},\qquad
a_D=\frac{n_+}{n}\sqrt{\frac h{h_+}}
\tag{7}
$$

die Grenzen

$$
\boxed{
\sqrt{\frac{s}{s+2v}}\le a_T\le1+vC_\ell,\qquad
\sqrt{\frac{s}{s+2v}}\le a_D\le1+\frac{2v}{\kappa}.}
\tag{8}
$$

Bei `ξ=0` wird `a_T=1` gesetzt. Diese Wahl ändert keinen L²-Operator.
Alle Multiplikatoren sind gerade, messbar, beschränkt und nach unten
beschränkt. Sie sind Isomorphismen der jeweiligen Umgebungs-L²-Räume;
die inversen Normen sind höchstens `sqrt((s+2v)/s)`.

Die angegebene Wahl liefert `C_ℓ=1` für `ℓ≤4`. Eine optimale Konstante wird
nicht behauptet; für größere Wände wächst die verwendete Majorante mit ℓ².

## 3. Vollständige Quellen auf jedem endlichen Horizont

Sei `𝒢` der Gamma-Formraum mit Norm `∫(1+g)|û|²`. Für `A>0` sei

$$
W_A=H^1_0((-A,A))\cap\ker E_+\cap\ker E_-,\quad
E_\pm u=\int u(x)e^{\pm x/2}\,dx,\quad
F_A=\overline{W_A}^{\mathcal G}.
\tag{9}
$$

Dabei werden die Quellen physisch auf der reellen Achse nullfortgesetzt.
Der bekannte obere Bound `g(ξ)≤(131/8)ξ²` sichert `W_A⊂𝒢`.
Für jeden endlichen A gilt tatsächlich

$$
F_A=\{u\in\mathcal G:\operatorname{supp}u\subset[-A,A],\ E_+u=E_-u=0\}.
\tag{10}
$$

Die rechte Seite ist unter der Gamma-Norm abgeschlossen. Für die umgekehrte
Inklusion verkleinere den Träger durch `u_r(x)=r^(−1/2)u(x/r)`, `r<1`.
Jeder Summand von (1) erfüllt `g(tξ)≤max(1,t²)g(ξ)` nach Summation.
Daher sind die Dilatationen nahe r=1 gleichmäßig auf 𝒢 beschränkt und
konvergieren stark gegen die Identität. Letzteres folgt zunächst für glatte
kompakt getragene Fourierfunktionen und dann durch Dichte im gewichteten L²-Raum.

Die beiden Momentfehler konvergieren wegen L²-Konvergenz auf festem Träger
gegen null. Zwei feste glatte Innenfunktionen mit invertierbarer Momentmatrix
korrigieren sie. Solche Funktionen existieren, weil `e^(x/2)` und `e^(−x/2)`
auf jedem Intervall positiver Länge linear unabhängig sind. Anschließendes
Glätten mit einem kleinen kompakten Mollifier erhält die Nullmomente:
`E_±(u*ρ)=E_±(u)E_±(ρ)`. Die Faltung konvergiert in 𝒢 und bleibt im Intervallinneren.
Für eine feste Parität kann die Korrektur innerhalb dieser Parität erfolgen.
So entstehen glatte H¹₀-Quellen; zusätzliche klassische Randspuren werden
für allgemeine Elemente von F_A nicht gefordert.

Fixiere nun `0<A≤L<∞` und die endlichen aktiven Familien
`Q_A={p^k: log(p^k)<2A}`. Wähle

$$
S_L\ge\max_{A\le L}s_A,\qquad \rho>S_L.
\tag{11}
$$

Zum Beispiel genügt `S_L=s_L`, einschließlich der strikten Endpunktkonvention,
und `ρ=S_L+1`. Mit `b_A=w_A+ρ` gilt

$$
g+\rho-S_L\le b_A\le g+\rho+S_L.
\tag{12}
$$

Somit ist `q_A+ρ||u||²` auf jedem F_A eine vollständige, zur Gamma-Norm
äquivalente Hilbertnorm. F_A selbst hängt nicht von L oder ρ ab.
Insbesondere wird die Zahl 17 nicht für beliebig große Horizonte festgehalten.

## 4. Physische Formnaturality

Für `A≤B` ist die physische Nullfortsetzung `J_(A,B)` auf W_A und danach
auf F_A die Inklusion derselben reellen Quelle. Sie erhält die beiden
Mellinbedingungen sowie Identität und Cocycle.

Jeder Kanal in `Q_B\Q_A` hat `ℓ_q≥2A`. Der Träger einer alten Quelle und
der um `+ℓ_q` oder `−ℓ_q` verschobene Träger einer anderen alten Quelle
überlappen daher höchstens in einer Nullmenge. Beide sesquilinearen
Translationspaarungen verschwinden. Mit (4) und Plancherel folgt

$$
q_B(Ju,Jv)=q_A(u,v),\qquad
\|Ju\|_{B,\rho}=\|u\|_{A,\rho}.
\tag{13}
$$

Dies gilt unmittelbar auf den vollständigen Räumen (10): Translation und
L²-Paarung sind stetig, und `|w_A|≤g+S_L` macht die Form auf 𝒢 stetig.
Am Aktivierungsendpunkt wird der einzelne Kontaktpunkt nicht als Überlapp
positiven Maßes behandelt. Neue Quellen mit größerem Träger müssen die
zusätzlichen Korrelationspaarungen dagegen nicht annullieren.

## 5. Beide Carrier und ihre Transporte

In zwei getrennten festen Kopien K_T und K_D von L² seien

$$
T_Au=t_A\widehat u,\quad D_Au=d_A\widehat u,\qquad
\mathcal H_A^T=\overline{T_AW_A},\quad
\mathcal H_A^D=\overline{D_AW_A}.
\tag{14}
$$

Wegen `d_A²≤s_A≤S_L` und
`b_A=t_A²+ρ−d_A²≥t_A²` sind beide Quelloperatoren auf F_A stetig.
Die beiden Regeln

$$
M^T_{A,B}T_Au=T_BJu,\qquad M^D_{A,B}D_Au=D_BJu
\tag{15}
$$

steigen jeweils unabhängig auf das betreffende Quellenbild ab, weil ihre
rechten Seiten durch den passenden beschränkten Multiplikator aus (7)
entstehen. Für konvergente Folgen von Quellenbildern liefert derselbe
Multiplikator einen Grenzwert im abgeschlossenen Zielcarrier. Somit sind
Mᵀ und Mᴰ auf den vollständigen Carriern definiert.

Die unteren Grenzen aus (8) zeigen Injektivität und abgeschlossenes Bild.
Die inversen Abbildungen werden auf diesen Bildern verwendet. Der
Umgebungs-Multiplikatorisomorphismus behauptet keine Surjektivität auf den
gesamten größeren Zielcarrier. Innerhalb einer Kammer sind beide Transporte
die wörtlichen isometrischen Inklusionen.

## 6. Endlich viele Wände: direktes Verhältnis und Cocycle

Für beliebige `0<A≤B≤L` definiere außerhalb von Null direkt

$$
a^T_{A,B}=\frac{m_B}{m_A}\sqrt{\frac{h_A}{h_B}},\qquad
a^D_{A,B}=\frac{n_B}{n_A}\sqrt{\frac{h_A}{h_B}}.
\tag{16}
$$

Setze `V_(A,B)=Σ_(Q_B\Q_A) w_q` und
`P_(A,B)=Σ_(Q_B\Q_A)w_q C_(ℓ_q)`. Die endlichen Summen ergeben

$$
\sqrt{\frac{s_A}{s_B}}\le a^T_{A,B}\le1+P_{A,B},\qquad
\sqrt{\frac{s_A}{s_B}}\le a^D_{A,B}\le1+\frac{2V_{A,B}}\kappa.
\tag{17}
$$

Damit folgt der ganze Carrier-Abstieg wie in §5. Für alle geordneten Tripel
`A≤B≤C≤L` kürzen sich die mittleren Zähler und positiven Wurzeln exakt:

$$
a^T_{B,C}a^T_{A,B}=a^T_{A,C},\quad
a^D_{B,C}a^D_{A,B}=a^D_{A,C}.
\tag{18}
$$

Am Nullpunkt kann für alle T-Verhältnisse konsistent 1 gewählt werden.
Die D-Verhältnisse sind dort regulär. Die Quellidentitäten sichern die
richtigen mittleren Carrier, daher gelten auf den gesamten Räumen

$$
M^T_{B,C}M^T_{A,B}=M^T_{A,C},\quad
M^D_{B,C}M^D_{A,B}=M^D_{A,C},\quad M^T_{A,A}=M^D_{A,A}=I.
\tag{19}
$$

Dies ist eine endliche algebraische Kürzung. Ein Grenzprodukt unendlich
vieler Wandoperatoren ist weder erforderlich noch hier nachgewiesen.
Bei einer Verlängerung des endlichen Maximalhorizonts L werden nur die
äquivalenten Hilbertnormen und Schranken neu gewählt; (16) und die Carrier
selbst bleiben dieselben. Die Rohfamilie ist somit für alle endlichen
Terminals konsistent definiert.

## 7. T-Isomorphismus und Defekt auf jedem endlichen Horizont

Für den konkreten Gamma-Kern gilt, zunächst auf W_A und dann auf F_A,

$$
\Gamma[u]=\int_0^\infty\frac{e^{-r/2}}{1-e^{-2r}}
\|\tau_ru-u\|^2dr\ge4e^{-A}\|u\|^2\ge\gamma_L\|u\|^2,
\quad\gamma_L=4e^{-L}>0.
\tag{20}
$$

Denn für `r>2A` ist das Normquadrat `2||u||²`; die Integration von
`2e^(−r/2)` liefert den angegebenen Boden. Die Identität folgt aus
Plancherel und der nichtnegativen Gamma-Reihe. Fourier-Grundlagen sind etwa
in [MIT, Chapter 4](https://math.mit.edu/~rbm/18-102-S18/Chapter4.pdf) dargestellt.

Die Funktion `f_S(x)=x²/(x+S)` ist wachsend und konvex auf `[0,∞)`:
`f'_S=1−S²/(x+S)²`, `f''_S=2S²/(x+S)³≥0`.
Jensen für `|û|²/||u||²`, `m_A≥g` und `s_A≤S_L` ergibt

$$
\|T_Au\|^2\ge\theta_L\|u\|^2,\qquad
\theta_L=\frac{\gamma_L^2}{\gamma_L+S_L}>0,\qquad
\|D_Au\|^2\le S_L\|u\|^2.
\tag{21}
$$

Der Gamma-Erwartungswert ist endlich; `f_S(g)≤g` legitimiert Jensen.
Mit (12)–(14) folgt

$$
\|T_Au\|^2\le\|u\|_{A,\rho}^2
\le(1+\rho/\theta_L)\|T_Au\|^2.
\tag{22}
$$

Das Bild von T_A ist daher abgeschlossen und nach (14) dicht im T-Carrier,
also gleich dem ganzen Carrier. T_A ist ein beschränkter Isomorphismus von
F_A auf dieses Bild. Für D wird keine beschränkte inverse Quellabbildung
benötigt. Es existiert eindeutig

$$
R_A:\mathcal H_A^T\to\mathcal H_A^D,\quad D_A=R_AT_A,
\qquad \|R_A\|^2\le S_L/\theta_L.
\tag{23}
$$

Aus (15) folgt zunächst auf dem dichten Quellenbild und dann überall

$$
R_BM^T_{A,B}=M^D_{A,B}R_A.
\tag{24}
$$

Mit `G_A=I−R_A*R_A`, (4) und der Formnaturality erhält man schließlich

$$
\boxed{(M^T_{A,B})^*G_BM^T_{A,B}=G_A.}
\tag{25}
$$

Diese Identität folgt auf den ganzen Carriern aus der Surjektivität von T_A.
Äquivalent ist die gekoppelte Gram-Bilanz

$$
(M^T)^*M^T-I=R_A^*((M^D)^*M^D-I)R_A.
\tag{26}
$$

Rohe Isometrie über eine Wand wird in keinem Schritt vorausgesetzt.

## 8. Genau welche Positivität der Rohsatz weiterträgt

Ist `G_A≥η_AI>0` und `||Mᵀ_(A,B)||≤K`, so gilt für
`y=Mᵀ_(A,B)x` auf dem abgeschlossenen alten Bild

$$
\langle y,G_By\rangle\ge\frac{\eta_A}{K^2}\|y\|^2.
\tag{27}
$$

Dies beweist keinen Boden auf dem ganzen neuen Carrier und keine Invarianz
des alten Bildes unter G_B. Schon `G_B=diag(η_A,−1)` mit der Einbettung
`x↦(x,0)` zeigt die logische Grenze der reinen Kompressionsidentität.

Ist ein alter **physischer** Boden `q_A≥c||.||²` bekannt, liefert (13)
zusätzlich auf dem alten transportierten Bild den Boden `c/(c+S_B)`:
`q_B[Ju]≥c||Ju||²` und `||D_BJu||²≤S_B||Ju||²`. Auch dieser Vergleich
kontrolliert ausschließlich das alte Bild.

Besitzen dagegen beide **vollständigen** Defekte Böden `G_A≥η_AI` und
`G_B≥η_BI` mit `η_A,η_B>0`, so sind
`Δ_A=G_A^(1/2)` und `Δ_B=G_B^(1/2)` beschränkt invertierbar. Dann definiert

$$
U^X_{A,B}=\Delta_BM^T_{A,B}\Delta_A^{-1}
\tag{28}
$$

eine isometrische Einbettung, denn ihr Gram ist nach (25) gleich I.
Für drei positive Terminals kürzen sich Δ_B⁻¹Δ_B und anschließend (19).
Damit gelten Cocycle und `U^X_(A,B)X_A=X_BJ_(A,B)` für `X_A=Δ_AT_A`.
Alle Symbolmultiplikatoren sind gerade, und die physische Inklusion
kommutiert mit Spiegelung. Somit gelten die Quell-, Transport- und
Defektidentitäten auch getrennt in beiden Paritäten; auf positiven
Carriern erhält der Funktionalkalkül für Δ diese Zerlegung ebenfalls.

Ein positiver physischer Terminalboden `q_B≥c||.||²` zieht durch (13)
denselben physischen Boden auf alle kleineren Horizonte zurück. Mit einer
gemeinsamen endlichen Schranke S_B folgt dort `G_A≥c/(c+S_B)I`.
So genügt pro neuer abgeschlossener Kammer ein vollständiger positiver
Terminalnachweis samt den angegebenen analytischen Bindungen.

## 9. Bedeutung der Iterierbarkeit

Der rohe Fortsetzungsmechanismus ist damit für die feste C1a-Familie auf
jedem endlichen Horizont bewiesen. Die positive Fortsetzung ist ein
bedingter Schritt: alter positiver Stand + neuer vollständiger
Terminalnachweis ergeben die nächste kompatible positive Familie.

Für jeden solchen endlichen Schritt genügt eine eigene strikt positive
Reserve. Eine einheitliche Reserve für alle Horizonte ist hier weder
bewiesen noch als Voraussetzung jedes Einzelschritts verlangt. Eine
kofinale positive Folge ist bisher nicht hergestellt. Globaler Readout,
globale Objekt-X-Konstruktion und RH erhalten dadurch keinen neuen Status.

## 10. Quellen und Prüfung

Die Formeln und abgeschlossenen Quellenmodelle stammen aus den in
`SOURCE_BINDINGS.json` gebundenen C1a-/O1–O7-Texten. Die lokale O10-Herleitung
und das lokale A9-Zertifikat bleiben unverändert. Neu sind der allgemeine
Frequenzbound (5), die endlichen Gesamtverhältnisse (16)–(19), die
horizontabhängigen vollständigen Quellschranken und ihre q=9-Instanz.

`verify_wall.py` kontrolliert exakte Algebra, skalare Majoranten, beide
Aktivierungsgrenzen, Mehr-Wand-Kürzung, rationale Quellproben und die
Dateibindungen. Er ersetzt nicht die analytischen Abschluss- und
Operatorargumente. Für A11 wird hier keine positive Terminalmatrix behauptet.
