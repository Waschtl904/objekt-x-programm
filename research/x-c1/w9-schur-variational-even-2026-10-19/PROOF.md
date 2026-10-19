# Variationaler Schur-Untertest am verstärkten Untervergleich

19. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN**.
Basis: `a09f052a6c856f6a75f8b9942b9d78f8f6506ea1`.
Alle Aussagen gelten unter den gebundenen Operator-, Formdomänen-,
Quellenmodell- und Integrationsvoraussetzungen.

## 1. Ergebnis: Frage offen

**SCHUR_LOWER_TEST_OPEN.** Für den unveränderten geraden physischen Zeugen
und genau einen rational eingefrorenen 84er-Testvektor ergibt sich

\[
\langle f,Q_{\mathrm{lower},*}^{-1}f\rangle
\ge 45.58828752529\cdot10^{-6}.
\]

Das unveränderte tatsächliche Budget liegt im Intervall

\[
K_P\in[54.11716936070,54.11716937864]\cdot10^{-6}.
\]

Die veröffentlichte rationale Untergrenze minus Budgetobergrenze beträgt
ungefähr -8.52888185333e-6. **Das ist kein negativer Abstand der tatsächlichen
Inversenergie zum Budget.** Der einseitige Test liefert keinen Ausschluss,
keinen Teilpass und keine Dualreserve. Eine obere Einschließung der vollen
Inversenergie wird nicht berechnet.

Das numerische Modell des Testausdrucks ohne die zusätzlichen Modellfehler
liegt bei [56.02591582223,56.14860931250]e-6. Dieser Wert ist keine
zertifizierte Untergrenze. Die aktuelle Formfehlermajorante ist für die
Schwellenentscheidung zu grob; ihre Größe beweist keinen entsprechend
großen tatsächlichen Fehler.

Die Frage, ob alle Obermajoranten der Inverse genau dieser verstärkten
Unterform scheitern, bleibt damit offen. Meilenstein 4, N12 und externe
mathematische Prüfung bleiben offen. Die frühere Entscheidung gegen die
konkrete K-Pilot-Majorante wird weder zurückgenommen noch verallgemeinert.

## 2. Festgelegte Unterform und einseitiges Kriterium

Es gilt ausschließlich der [K-Pilot-Stand](../w9-k-pilot-even-2026-10-18/PROOF.md):

\[
K_*=K+\frac{13}{10^8}G_F,\quad
H_*^{\rm neu}=S-a_{low}^*((1-\rho)I)^{-1}a_{low}-a_{fin}^*K_*^{-1}a_{fin}.
\]

Seine volle Positivität folgt aus dem gebundenen K-/Schur-/Restnachweis.
Alle ursprünglichen Funktionen, U8, die Antwortmatrix X0, der physische
gerade Zeuge und das separate K_P-Zertifikat bleiben unverändert.
Die vollständige Vergleichsform lautet

\[
Q_{\rm lower,*}[w,z,r]
=\|U_8^{-1/2}(w+U_8G(z,r))\|^2
 +\|K_*^{1/2}(z+K_*^{-1}a_{fin}r)\|^2+H_*^{\rm neu}[r].
\]

Sie ist eine positive geschlossene Unterform von A9. Die vollständigen
Domänen- und Koordinatenaussagen werden aus der gebundenen
[Inversherleitung, Abschnitt 6](../a9-inverse-renewal-2026-10-13/original/HERLEITUNG.txt)
übernommen. Der K-Pilot begründet deren Änderung auf K_*; der alte
unverstärkte Untervergleich wird hier nicht still weiterverwendet.
Für die physische Residualquelle f setzen wir

\[
h=J_{old}^*f,\quad v=F^*f-g_F^*U_8h,\quad
\nu_*=\Lambda_T^*f-g^*U_8h-a_{fin}^*K_*^{-1}v,
\]
\[
E_b=\langle h,U_8h\rangle+v^*K_*^{-1}v.
\]

Dann gilt exakt

\[
\langle f,Q_{\rm lower,*}^{-1}f\rangle=E_b+
\langle\nu_*,(H_*^{\rm neu})^{-1}\nu_*\rangle.
\]

Für jeden festen rationalen Vektor t in R^84 ist Jt im Formbereich:
J besteht aus den unveränderten, korrekt momentprojizierten Polynomen bis
Grad 95. Das Variationsprinzip liefert

\[
\boxed{\quad E_b+2\operatorname{Re}\langle\nu_*,Jt\rangle-H_*^{\rm neu}[Jt]
\le\langle f,Q_{\rm lower,*}^{-1}f\rangle.\quad}
\tag{1}
\]

Eine gerichtete Untergrenze der linken Seite oberhalb K_P,upper würde
folglich jeden W mit Q_lower,*^-1 <= W am festen Zeugen ausschließen.
Dies beträfe nur die Inverse **dieser** Unterform, nicht jede Majorante
der tatsächlichen A9-Inverse. Umgekehrt lässt eine niedrigere linke Seite
die tatsächliche Inversenergie nach oben offen. Darum gibt es hier nur
`SCHUR_UNDERFORM_COMPARISON_EXCLUDED` oder `SCHUR_LOWER_TEST_OPEN`.

## 3. Einmalige Auswahl und unveränderlicher Testvektor

Vor dem gerichteten Auswertungslauf wird genau das 84er-Mittelpunktsystem

\[
H_0t=\ell_0,\qquad
H_0=(D_{mid}-U_0)_{JJ}-a_0^*K_*^{-1}a_0,\quad \ell_0=J^*\nu_{*,0},
\]

gelöst. Es gibt keine weiteren Starts, Skalierungen oder Kandidaten.
Die Lösung wird auf 50 Dezimalstellen rational gerundet. `CANDIDATE.json`
ist danach eine exakte Eingabe; die Abweichung vom numerischen Optimierer
braucht keinen Optimierungsfehlerpreis, weil (1) für jeden solchen t gilt.
Es wird keine globale oder gerichtete Optimalität beansprucht.

Der Vektor wurde vor dem Zertifikatslauf im lokalen Commit
`0a6fffd3792c90e310ab13ff8f0868acc4fb99a5` eingefroren. Sein SHA-256 lautet
`42bbf77a09f2e3f71b4c89cd3ad7c959a8f77fb507d049f3243568b53a2c612b`.
Seine euklidische Norm ist ungefähr 1.20614. Der gerichtete Test löst kein
neues Auswahlproblem. Ein Replay der Auswahl wird separat bytegleich
verglichen und verändert den anschließend geprüften festen Vektor nicht.

## 4. Gerichtete Formobergrenze: richtige Richtung

Schreibe B=D_direct-G*U8G und G=diag(G_F,G_J). Die vorhandenen gemeinsamen
Fehler geben mit d_a=d_D+d_U

\[
|t^*(B_{JJ}-B_{0,JJ})t|\le d_a\,t^*G_Jt,
\quad
\|K_*^{-1/2}(a_{fin}-a_0)t\|
\le d_a\sqrt{\operatorname{tr}(K_*^{-1}G_F)}\sqrt{t^*G_Jt}=e_a(t).
\]

d_U, d_D und d_a sind die unveränderten vollen 96-Quellen-/F-J-Fehler.
Der kleinere F-F-Fehler des K-Zulässigkeitsnachweises ersetzt keinen davon.
Mit z=a_0t und einer gerichteten unteren Schranke n_- für
sqrt(z*K_*^-1 z) folgt

\[
a_{fin}[t]^*K_*^{-1}a_{fin}[t]\ge(\max(0,n_--e_a(t)))^2.
\]

Aus der vollständigen Unterformherleitung gilt

\[
H_*^{\rm neu}[Jt]=t^*B_{JJ}t-a_{fin}[t]^*K_*^{-1}a_{fin}[t]-\eta q[Jt],
\quad q[Jt]\ge0.
\]

Daher ist die tatsächlich verwendete **obere** Schranke

\[
H_*^{\rm neu}[Jt]\le
(t^*B_{0,JJ}t)_{up}+d_a t^*G_Jt-(\max(0,n_--e_a(t)))^2=:H_{up}(t).
\tag{2}
\]

Das Weglassen des positiven eta-q-Gewinns macht (1) konservativer.
Es ändert nicht die festgelegte Zielunterform. Ein oberer Formwert ist
wegen des Minuszeichens in (1) die richtige Richtung.

Die numerische Aufschlüsselung erklärt den offenen Ausgang:

| Beitrag | Größe ungefähr |
|---|---:|
| Modellwert H0[t] | 4.05460499e-5 |
| gemeinsamer D/U-Formfehler | 6.35227558e-7 |
| a_fin-Fehler in K_*^-1/2-Norm | 1.65208807e-6 |
| daraus Verlust beim unteren a_fin-Quadrat | 9.76872333e-6 |
| verwendete obere Formschranke | 5.09500008e-5 |

Das kleine Fehlernormbudget wirkt auf einen Modellvektor mit
z*K_*^-1 z ungefähr 8.74077. Seine quadratische Fehlerwirkung ist deshalb
für den kleinen verbleibenden Schurwert entscheidend. Diese obere
Fehlermajorante ist keine gemessene Abweichung.

## 5. Paarungs- und ganze Residualfehler

Alle Paarungen stammen aus den gebundenen gemeinsamen #238-Integralen.
Die vom K-Piloten erneuerten Daten bilden

\[
\ell_0=J^*\nu_{*,0},\quad k=K_*^{-1}a_0
\]

als gemeinsame Differenz vor der Energieauswertung. Die zwei
algebraischen nu-Ausdrücke werden weiterhin in allen 1008 Einträgen
abgeglichen. Modellkoeffizienten, Gamma-Reste, hohe Paarungsfehler und
a_fin-Fehler werden behalten. Für den festen Vektor t ist der Preis
exakt die Rang-eins-Spezialisierung P=tt* der gebundenen
`pilot_energy.py`-Paarungsherleitung. Insbesondere enthält er einmal

\[
e_{a,pair}=d_a\sqrt{t^*G_Jt}
\left(\sqrt{(K_*^{-1}v_0)^*G_F(K_*^{-1}v_0)}
 +\sqrt{\operatorname{tr}(K_*^{-1}G_F)}\,e_v\right).
\]

Der entsprechende Preis in (2) betrifft einen anderen Ausdruck;
beide Abweichungen werden hier konservativ getrennt kontrolliert.
Die genauen Einzelpreise stehen in `RESULT.json`.

Für die ganze physische Residualmodellabweichung e_f wird eine eigene
richtungsabhängige Normobergrenze j_t berechnet. Mit

\[
s=(-kt,t),\quad d_k=d_a\sqrt{\operatorname{tr}(K_*^{-1}G_FK_*^{-1})}
\sqrt{t^*G_Jt},\quad U_{F,up}=U_{0,F}+d_U G_F,
\]
\[
u_t=\sqrt{s^*U_0s+d_U s^*Gs}+\sqrt{\operatorname{tr}(U_{F,up})}d_k,
\]
\[
j_t=\sqrt{1.000502}\,\|t\|+16(\|kt\|+d_k)+\sqrt{u}\,u_t,
\]

folgt |delta_f <nu_*,Jt>| <= j_t e_f. Hier sind u die vollständige
U8-Normmajorante, ||Lambda J||² <=1.000502 und ||F||<=16 gebunden.
Das ist die richtungsabhängige Fassung der alten Teilnormherleitung;
eine ungeprüfte alte Fehlernorm wird nicht übernommen.

Gerichtet ergibt sich die tatsächliche Paarung im Intervall
[4.05292112310,4.05628886225]e-5. Ihr a_fin-Fehler dominiert mit ungefähr
1.68373e-8; der zusätzliche ganze Residualpreis ist nur ungefähr 6.311e-13.
Auch dieses Paarungsintervall ist keine Energieobergrenze.

## 6. Basisenergie und Entscheidung

Die beiden vollständigen U8-Anteile und der K_*^-1-Anteil bilden E_b.
Die alten Integrationsradien bleiben in ihrem Modellintervall enthalten.
Zusätzliche Featurefehler werden über das Normdreieck bezahlt. Für die
ganze physische Residualabweichung wird die neu gebildete Basisnorm
u+v_*² benutzt, wobei v_* die gültige K_*^-1-Featureoperatorgrenze ist.
Das liefert E_b im Intervall ungefähr [1.54798658793,1.56025594020]e-5.
Die exakten äußeren rationalen Endpunkte stehen in `RESULT.json`.

Schließlich wird allein

\[
E_{test,lo}=E_{b,lo}+2\ell_{lo}-H_{up}
\]

nach unten rational gerundet und mit dem unveränderten K_P,upper verglichen.
Diese Untergrenze steht als `inverse_energy_lower` in `RESULT.json`.
Kein oberes Ende der vollen Inversenergie wird aus dem Modellwert erfunden.
Negative Normquadrate werden nicht durch Beträge repariert.

## 7. Abnahme und nächster Entscheidungspunkt

`INPUT_BINDINGS.json` bindet den K-Pilot, dessen geerbte Quellen und die
unveränderten Integrale. `MANIFEST.json` bindet das neue Paket.
`verify.py --check` rekonstruiert die einmalige Auswahl bytegleich und
prüft dann den bereits eingefrorenen Vektor vollständig. Der frische
vollständige Archiv-Replay, Hashes und lokale Pflichtchecks werden in
`ACCEPTANCE.json` dokumentiert. Historische Integrationen und der
unveränderte große K-Pilot-Schuraufbau werden nicht nochmals ausgeführt.

Abgeschlossen ist dieser kleine Diagnoseauftrag. Es gibt keinen
Ausschluss der ganzen Majorantenklasse und keinen Teilpass. Der nächste
begründete Entscheidungspunkt ist eine eng begrenzte Prüfung, ob der
dominierende a_fin-Formfehler am **gleichen** festen Vektor schärfer
kontrolliert werden kann. Das ist keine Zusage, dass eine Verengung
möglich oder ausreichend wäre. Eine neue Unterform oder Großintegration
wird durch den offenen Untertest weder erzwungen noch gestartet.
