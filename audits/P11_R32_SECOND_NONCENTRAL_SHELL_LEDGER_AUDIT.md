# P11/R32 — zweite nichtzentrale Unsichtbarkeitsschale und vollständiges 11-Wort-Ledger

**Status:** Kandidat; keine Promotion.  
**P11:** FROZEN. **P12:** unverändert. **R14:** unverändert.  
**Basis:** SE-1/SE-2/CTX-1/NS-1 Kandidatenkette.  
**Ziel:** die nächste explizite Komponente des inneren Unsichtbarkeitsraums \(\mathcal K_R\) klassifizieren und von Anfang an alle elf Full-Rest-Wörter bilanzieren. Es wird hier **keine** Schur-Transversalität behauptet.

## 1. Setup

Im Drei-Shift-Fenster
\[
2a<T_0<c:=\tfrac12\log5,
\qquad a=\tfrac12\log2,
\quad b=\tfrac12\log3,
\quad T=2a,
\]
setze
\[
d:=b-a,
\qquad e:=T-b=2a-b,
\qquad \varepsilon:=T_0-T.
\]
Es gelten exakt
\[
d>e\qquad(9>8),
\]
\[
e>0\qquad(4>3),
\]
und
\[
e<\frac a2\qquad(8<9).
\]

Fixiere
\[
\boxed{\frac d2\le R<e}
\tag{SS.1}
\]
und
\[
\ell:=e-R>0.
\]
Aus \(2R\ge d>e\) folgt
\[
\boxed{0<\ell<R.}
\tag{SS.2}
\]
Ferner ist \(R<e<a/2\).

Setze
\[
I=(-R,R),
\qquad
\mathcal K_R:=\ker(E_I^*H|_{\mathscr H^+}),
\]
mit
\[
H=pD_{2a}+rD_{2b}+qD_{2T}.
\]

## 2. Zweite nichtzentrale Rand-Schale

Definiere auf der positiven Achse die zwei disjunkten Intervalle
\[
J_b:=(b,b+\ell)=(b,T-R),
\]
\[
J_T:=(T-\ell,T)=(b+R,T).
\tag{SS.3}
\]
Sie sind disjunkt, weil \(\ell<R\), also \(T-R<b+R\).

Definiere \(\mathcal S_{R,2}^+\) als den Raum aller geraden \(y\in L^2(-T_0,T_0)^+\), deren positiver Träger in \(J_b\cup J_T\) liegt und die für fast jedes \(0<u<\ell\) die gewichtete Paarbedingung
\[
\boxed{
q\,y(T-u)=r\,y(b+u)
}
\tag{SS.4}
\]
erfüllen.

Der Raum ist unendlichdimensional: ein beliebiges Profil \(f\in L^2(0,\ell)\) kann durch
\[
y(b+u)=f(u),
\qquad
y(T-u)=\frac rq f(u)
\]
und anschließend durch Geradheit fortgesetzt werden.

### Warnung: keine Mittelpunkt-Involution

Die stärkere, aber falsche Forderung
\[
q y(m-v)=r y(m+v)\quad\text{für alle }|v|<k,
\qquad m=(b+T)/2,
\]
würde nach \(v\mapsto-v\) zusammen mit der ursprünglichen Gleichung wegen \(r\ne q\) nur \(y=0\) erlauben. Die korrekte Geometrie besteht aus den zwei **getrennten Rand-Schalen** (SS.3), sodass nur eine Orientierung der Paarung innerhalb des beobachteten Fensters vorkommt.

## 3. Lemma SS-1a — Unsichtbarkeit

\[
\boxed{
\mathcal S_{R,2}^+\subset\mathcal K_R.
}
\tag{SS.5}
\]

### Beweis

Sei \(0<u<R\).

**a-Kanal.** Weil \(R<e<a/2\), gilt
\[
a+u<a+R<a+e=3a-b<b,
\]
letzteres äquivalent zu \(3a<2b\iff 8<9\). Somit liegen beide \(a\)-Äste unterhalb des positiven Trägers; der negative Träger liegt symmetrisch und liefert ebenfalls keinen Beitrag.

**b/T-Kanäle, Fall \(0<u<\ell\).** Dann
\[
b+u\in J_b,
\qquad T-u\in J_T,
\]
während \(b-u<b\) und \(T+u>T\) außerhalb des Trägers liegen. Daher
\[
(Hy)(u)=-r y(b+u)+q y(T-u)=0
\]
durch (SS.4).

**b/T-Kanäle, Fall \(\ell<u<R\).** Dann
\[
b+u\in(b+\ell,b+R)=(T-R,b+R),
\]
und
\[
T-u\in(T-R,T-\ell)=(T-R,b+R),
\]
also liegen beide Punkte im mittleren Supportloch zwischen \(J_b\) und \(J_T\). Die anderen Äste liegen weiterhin außerhalb.

Somit \(Hy=0\) fast überall auf \((0,R)\); wegen Parität gilt dasselbe auf \((-R,0)\). Damit folgt (SS.5).

## 4. Vollständige Pre-Adjoint-Supportbilanz

Verwende SE-2:
\[
\Phi_{20}=\alpha_1K_1+\alpha_2K_2+\alpha_3K_3,
\]
mit
\[
K_1=K_{\log2}^{tr},\quad K_2=K_{2\log2}^{tr},\quad K_3=K_{3\log2}^{tr},
\]
und Maskenradien
\[
\Omega_{20}: |u|<a+\varepsilon,
\quad
\Omega_{21}: |u|<\varepsilon,
\quad
\Omega_{30}: |u|<e+\varepsilon.
\]

Auf der positiven Achse besitzen die drei rechten \((2,0)\)-Outputs folgende Supportkomponenten.

### 4.1 \(M_{20}K_1y\)

Aus \(J_b\) entsteht
\[
(d,d+\ell),
\]
aus \(J_T\)
\[
(a-\ell,a).
\]
Beide liegen vollständig in \(\Omega_{20}\), also
\[
\boxed{M_{20}K_1|_{\mathcal S_{R,2}^+}\ne0.}
\tag{SS.6}
\]

### 4.2 \(M_{20}K_2y\)

Aus \(J_T\) entsteht
\[
(0,\ell),
\]
aus \(J_b\)
\[
(R,e).
\]
Beide liegen in \(\Omega_{20}\), also
\[
\boxed{M_{20}K_2|_{\mathcal S_{R,2}^+}\ne0.}
\tag{SS.7}
\]

### 4.3 \(M_{20}K_3y\)

Aus \(J_T\) entsteht unter anderem
\[
(a,a+\ell).
\]
Da \(\varepsilon>0\) und \(\ell>0\), schneidet dieses Intervall \((a,a+\varepsilon)\subset\Omega_{20}\) in positiver Länge. Daher
\[
\boxed{M_{20}K_3|_{\mathcal S_{R,2}^+}\ne0.}
\tag{SS.8}
\]

### 4.4 \((2,1)\)-Block

Der einzige rechte Term ist \(K_2\). Sein Output enthält \((0,\ell)\), welches jede Maske \(( -\varepsilon,\varepsilon)\) mit \(\varepsilon>0\) in positiver Länge schneidet. Also
\[
\boxed{M_{21}K_2|_{\mathcal S_{R,2}^+}\ne0.}
\tag{SS.9}
\]

### 4.5 \((3,0)\)-Block

Für \(K_b:=K_{\log3}^{tr}\) entstehen dieselben zentralen positiven Intervalle
\[
(0,\ell)\cup(R,e),
\]
die vollständig in \(|u|<e+\varepsilon\) liegen. Also
\[
\boxed{M_{30}K_b|_{\mathcal S_{R,2}^+}\ne0.}
\tag{SS.10}
\]

## 5. Exaktes 11-Wort-Ledger

Im \((2,0)\)-Block gibt es neun geordnete Wörter
\[
W_{\ell k}:=K_\ell^*M_{20}K_k,
\qquad \ell,k\in\{1,2,3\}.
\]
Da alle drei rechten Spalten nach Abschnitt 4 nichttrivial sind, bleiben zunächst alle neun Kandidaten erhalten. Der einzige zusätzliche Horizont-No-Go betrifft \(W_{32}\).

### 5.1 Warum \(W_{32}=0\)

Der maskierte rechte Output \(M_{20}K_2y\) ist in
\[
|u|<e
\]
getragen. Für \(|x|\le T_0\) liegen die Argumente von \(K_3^*\) mindestens im Abstand
\[
3a-T_0=a-\varepsilon
\]
vom Ursprung. Im Drei-Shift-Fenster gilt
\[
a-\varepsilon>a-E>e.
\]
Die letzte strikte Ungleichung folgt aus
\[
a-E-e=a+b-c>0
\iff 6>5.
\]
Damit kann \(K_3^*\) keinen in \((-e,e)\) getragenen Input innerhalb des Horizonts erreichen. Also
\[
\boxed{W_{32}|_{\mathcal S_{R,2}^+}=0.}
\tag{SS.11}
\]

### 5.2 Warum die übrigen acht \((2,0)\)-Wörter nicht identisch null sind

Für linke Zeilen \(K_1^*,K_2^*\) liegen die in Abschnitt 4 gefundenen maskierten Supports innerhalb ihrer erreichbaren Horizontbereiche, also sind
\[
W_{1k},W_{2k}\ne0\qquad(k=1,2,3)
\]
als Operatoren auf \(\mathcal S_{R,2}^+\).

Für \(K_3^*\) besitzen sowohl \(M_{20}K_1y\) als auch \(M_{20}K_3y\) Supportanteile beliebig nahe bzw. oberhalb von \(a\). Da die Erreichbarkeitsschwelle \(a-\varepsilon<a\) ist, sind auch
\[
W_{31}\ne0,\qquad W_{33}\ne0.
\]
Nur \(W_{32}\) ist durch (SS.11) ausgeschlossen.

Somit sind im \((2,0)\)-Block exakt
\[
\boxed{8\text{ von }9}
\]
Wörtern nicht identisch null auf der zweiten Schale.

Der \((2,1)\)-Selbstterm und der \((3,0)\)-Selbstterm sind nach (SS.9)–(SS.10) ebenfalls nicht identisch null. Insgesamt:
\[
\boxed{
8+1+1=10\text{ von }11
}
\tag{SS.12}
\]
Full-Rest-Wörtern sind auf \(\mathcal S_{R,2}^+\) als Operatoren potentiell aktiv.

## 6. Interpretation

Dies ist der erste explizite Unsichtbarkeitssektor, in dem die zuvor beobachtete starke Full-Rest-Sparsität praktisch verschwindet:

- erste nichtzentrale Schale NS-1: global nur 4 von 11 Wörtern aktiv;
- zweite nichtzentrale Rand-Schale SS-1a: 10 von 11 Wörtern aktiv.

Daher ist eine direkte Wiederholung des NS-1-Supportbeweises hier **nicht** gerechtfertigt. Der nächste Transversalitätsschritt muss entweder

1. die zehn Wörter in einer neuen Rohmatrix-/Orbitstruktur gemeinsam organisieren, oder
2. zusätzliche algebraische Beziehungen aus der gewichteten Paarbedingung (SS.4) ausnutzen.

## 7. Firewall und Kandidatenstatus

Bewiesen wird in diesem Audit nur als Kandidat:

- **SS-1a:** zweite nichtzentrale Rand-Schale ist ein unendlichdimensionaler Unterraum von \(\mathcal K_R\) für \(d/2\le R<e\);
- **SS-L:** auf dieser Schale sind exakt 10 von 11 Full-Rest-Wörtern als Operatoren nicht identisch null; nur \(W_{32}\) stirbt durch den Horizont.

Nicht bewiesen:

- irgendeine Schur-Transversalität dieser zweiten Schale;
- voller augmentierter Blockkern trivial;
- voller Schur-Crossblock injektiv;
- Closed Range / bounded below / uniforme Winkel;
- Polar Gauge, Strong Terminal Transport, Objekt X oder RH.

Bei unabhängigem GREEN wäre zulässig:

- **SS-1a:** `✓[M]`;
- **SS-L:** `✓[M]` als exakte Wort-/Supportklassifikation.

Keine Promotion ohne explizite Freigabe.
