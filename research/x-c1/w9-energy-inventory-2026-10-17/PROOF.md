# Vollständige W9-Energie: Dateninventar und gewichtete Fehlerkontrolle

17. Oktober 2026. **AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN** für die nachstehende
bedingte Herleitung. Die praktische Energiebilanz bleibt **OPEN**.
Dieses Paket berechnet keine neue Residualenergiematrix und entscheidet N12 nicht.
Es verändert weder die Antwortregel noch die abgeschlossenen Einzelrichtungen.

## 1. Fester Scope und Quellen

Basis ist #236, Commit `27dfebb03dc4bf10265797b575fcbe08a15eb500`.
Die 0.918952/0.863890 aus dessen §5 sind Maxima des **gesamten numerischen
Mittelpunktmodellraums**, keine bloßen Spitzen einer endlichen Suche.
Die zusätzliche gerade Modellmajorante 0.998543 erhält weiterhin keine
Beweiswertung. Keiner dieser Werte wird als gerichtete Eingabe benutzt.

Alle hier tatsächlich verwendeten Dateien und Archivmitglieder sind in
`INPUT_BINDINGS.json` mit Hash, Rolle und verwendeten Feldern aufgeführt.
Die arithmetische Formidentifikation, Domänen, vollständigen alten
Quellintegrationen, HB-Obermatrix und A9-Inversordnung bleiben geerbte
Voraussetzungen. Byteprüfung oder rationale Rechnung beweisen sie nicht erneut.
Insbesondere wird keine A11-Positivität oder A11-Inverse eingelesen oder benutzt.

Notation: H8 und H9 sind die physischen Mellin-Nullräume. Die **alte** Schale
(a8,a9) trägt W_X, die **neue** Schale (a9,a11) trägt W. J ist die alte
nichtorthonormale Basis84 in T. F_o bezeichnet die alten zwölf physischen
Quellen (vier z, acht Lambda Y). Davon verschieden sind die zwölf neuen
Antwortfunktionen Phi12 und D=A9 Phi12. Die feste Regel bleibt
T_new=X_fix Fhat und R=C-D T_new. Z bildet zwölf Koeffizienten auf die
Grad-11-Schalenpolynome ab; G_W=Z*WZ ist ihr physischer Gram.
Dhat=Pi9 Dtilde verwendet die **exakte** Momentprojektion.
Rhat=C-Dhat T_new und DeltaD=D-Dhat sind so auf H9 typisiert.

Die verbindlichen Quellen sind insbesondere A9-Inverserneuerung §6,
A9-Domänenherleitung §§4–5, Nstar-Funktionsanschluss §§3–6 und
Antwortgram-Herleitung §5. Historische Originale und ihre Statusfelder werden
nicht überschrieben. Die folgende obere W9-Norm ist eine **neue Folgerung**
aus diesen Voraussetzungen; sie war kein Resultat des alten Antwortgram-Pakets.

## 2. Vier Energieanteile, fünf gewichtete Features

Für f in H9 seien

\[
h=J_{old}^*f,\quad y=T_hh,\quad
v=F_o^*f-g_F^*U_8h,\quad
\nu=\Lambda_T^*f-g^*U_8h-a_{fin}^*K^{-1}v.
\]

K ist die feste alte rationale Untervergleichsmatrix K12_neu; sie wird nicht
gegen einen Mittelpunkt ausgetauscht. Mit C8 als alter Inverskongruenz gilt

\[
V_8=C_8^*(\Phi^*-B_8T_h/\delta),\qquad
U_8=\delta^{-1}T_h^*T_h+(1-\rho)^{-1}V_8^*V_8.
\]

Die ganze Majorante lautet

\[
\langle f,W_9f\rangle=
\langle h,U_8h\rangle+v^*K^{-1}v+
\frac{11}{10\beta}\langle\nu,R_L\nu\rangle+
\frac{11}{10}(J^*\nu)^*P_{upper}(J^*\nu).
\tag{1}
\]

Die erste Energie zerfällt in einen vollständigen hohen und einen endlichen
Anteil. Somit ist W9=Fcal*Fcal mit den fünf gemeinsamen Featureabbildungen

\[
\mathcal F f=\left(
\delta^{-1/2}T_hh,
(1-\rho)^{-1/2}V_8h,
K^{-1/2}v,
\sqrt{11/(10\beta)}R_L^{1/2}\nu,
\sqrt{11/10}P_{upper}^{1/2}J^*\nu\right).
\tag{2}
\]

Die Wurzeln bezeichnen positive Operatorwurzeln; eine Implementierung darf
äquivalente gewichtete Gram-Produkte verwenden. Alle T-Adjunkte benutzen W_X.
Die zwei unendlichen Anteile werden nicht durch 287 endliche Koordinaten ersetzt.

## 3. Bestand und genau fehlende Daten

Die Bestandsaufnahme prüft beide Paritäten und beide gespeicherten
Residualauflösungen (384/512). `INVENTORY.json` enthält alle tatsächlich
geprüften Dimensionen. Aussagen über fehlende Daten beziehen sich auf diesen
gebundenen Bestand und seine gespeicherten Maps, nicht auf unbekannte externe Pakete.

| Anteil | Vorhanden und wiederverwendbar | Für neue Residuen noch nötig |
|---|---|---|
| Feste Gewichte | delta, rho, C8 (191x191), K und K^-1 (12x12), P_upper (84x84), beta | keine neue Matrixauswahl; geerbte Fehler/Beweisanker erhalten |
| Hohe U8-Energie | ungerichteter H8-Gram und rekonstruierbares Phi*h; vollständige Projektionsdefinition | y_h*y_h bzw. fehlendes e_sigma-Moment, gerichtete Projektions-/Integrationsreste |
| Endliche U8-Energie | C8*Phi*h (191x12) | B8 y_h (191x12); erst die Differenz definiert V8 h |
| Zwölferenergie | F_o*f (12x12); alte niedrige/hohe g_F-Features und Fehlergrame | y_F*y_h (12x12), dann g_F*U8h und v gemeinsam |
| Basis84-Energie | alte gJ-Features, hohe F/J-Grame, a_fin J (12x84) mit Modellfehler, P_upper | (Lambda J)*f (84x12), y_J*y_h (84x12), dann alle 84 Komponenten J*nu |
| Vollständiger R_L-Dualterm | Operator-/Domänendefinition, L>=21/5 W_X, exakte Nebenbedingungen und alte Geometrie | ganze neue Funktionalabbildung nu und vollständiger Dualgram mit Rest |
| Direkte K_P-Seite | zwei numerische Grad-11-Grame aus #236; feste Antwort und gerichtete direkte Modellfehler | gerichtete Integrations-/Matrixreste bei späterer Zertifizierung |
| Modellfehler | ganze Hilbertnorm DeltaD und Antwortobergram G_T | brauchbarer gewichteter Fehlergram gemäß §4; grobe Ersatzlösung §5 reicht praktisch nicht |

Die alten Quellgrame betreffen g_F und gJ. Sie bestimmen nicht deren neue
Kreuzpaarungen mit h. Aus C8*Phi*h und einer h-Norm folgt B8 T_h h nicht.
Ein exaktes zweidimensionales Gegenmodell im Prüfer hat gleiche niedrige
Koordinate und gleiche Norm, aber entgegengesetztes hohes Vorzeichen und
unterschiedliche Energie nach dem gekoppelten V8-Feature.

**Hohe Projektion.** Für m_scaled, e=e_sigma, m_e=<m_scaled,e> und h in H8 gilt
mit der geerbten Skalierungsisometrie U

\[
\|T_hh\|^2=\|h\|^2+
\frac{\|m_{scaled}\|^2}{|m_e|^2}|\langle e,Uh\rangle|^2
-\|\Phi^*h\|^2.
\tag{3}
\]

Denn M*Uh=Uh-m_scaled<e,Uh>/m_e liegt in e^perp, und <m_scaled,Uh>=0.
Abzug der gesamten 191 niedrigen Koordinaten ergibt (3). Polarisation liefert
den gemeinsamen Gram. Die in #236 benutzte Matrix gamma_M H8-Phi*Phi
ist nur eine obere Modellmajorante, nicht die exakte linke Seite von (3).
Das bisher nicht gespeicherte e_sigma-Moment kann bei neuer Integration der
vorhandenen Residualfunktionen mitgeführt werden. Gamma-/Sprungzellen und
der logarithmische Rand bleiben dabei vollständig enthalten.

**Die beiden neuen Kreuzgrame.** Schreibe y_F=T_hg_F, y_J=T_hgJ,
V_F=V8 g_F, V_J=V8 gJ und V_h=V8 h. Dann

\[
g_F^*U_8h=\delta^{-1}y_F^*y_h+(1-\rho)^{-1}V_F^*V_h,
\]
\[
J^*g^*U_8h=\delta^{-1}y_J^*y_h+(1-\rho)^{-1}V_J^*V_h,
\]
\[
J^*\nu=(\Lambda J)^*f-J^*g^*U_8h-(a_{fin}J)^*K^{-1}v.
\tag{4}
\]

Alle Differenzen werden vor Quadrierung gebildet. Es genügt nicht, drei
separat große Normen zu addieren oder alte k-Fehler mehrfach zu bezahlen.
Die 191 B8*-Funktionen und alten Quellfunktionen sind analytisch konstruiert;
vorhandene Programme/Archive liefern Bausteine. Ihre neuen Paarungen sind
noch keine gespeicherten vollständigen Daten.

**R_L ist keine 84x84-Inverse.** Es ist die inverse L-Form auf dem gesamten
exakten T. Variational gilt

\[
\langle\nu,R_L\nu\rangle=
\sup_{t\in D(L)\cap T}\{2\Re\langle\nu,t\rangle_{W_X}-L[t]\}.
\tag{5}
\]

Ein Galerkinwert ist zunächst eine Untergrenze. Für einen tatsächlich
zulässigen t mit L_T t in T liefert r=nu-L_T t die exakte Identität

\[
\langle\nu,R_L\nu\rangle=
2\Re\langle\nu,t\rangle-L[t]+\langle r,R_Lr\rangle,
\qquad \langle r,R_Lr\rangle\le(5/21)\|r\|_{W_X}^2.
\tag{6}
\]

Für eine gemeinsame Zwölferspalte gilt die polarisierte Matrixidentität;
der vollständige Restgram muss eingeschlossen werden. Gerade die hohe
Funktionalwirkung und dieser Rest fehlen. Ein Abbruch bei Grad 95 ohne Rest
berechnet den vollständigen Term nicht.

## 4. Passende gewichtete Modellfehlerkontrolle

Setze E=DeltaD:C12->H9 und E_i=Fcal_i E, mit den fünf Zeilen aus (2).
Wenn gemeinsam gerichtete Obergrame Q_i>=E_i*E_i vorliegen, gilt

\[
Q_D:=\sum_{i=1}^5Q_i\succeq E^*W_9E.
\tag{7}
\]

Damit wird keine globale W9-Norm benötigt. Jeder Q_i muss alle zwölf
Fehlerspalten und ihre Linearkombinationen umfassen. Ein alter Preis für
<chi_p,E c> kontrolliert lediglich eine Rang-eins-Projektion und ersetzt
keinen dieser vollständigen Grame. Gemeinsame Quell-/k-Modellfehler werden
innerhalb der zusammengesetzten Features transportiert, nicht unabhängig
pro Auftreten erneut addiert.

Für T=T_new und R=Rhat-E T folgt

\[
(R-Rhat)^*W_9(R-Rhat)\preceq T^*Q_DT,
\qquad \|T^*Q_DT\|\le\operatorname{tr}(Q_DG_T).
\tag{8}
\]

Auf dem Grad-11-Raum sollte zunächst Z*T*Q_DTZ als Matrix behalten werden;
die Spur ist nur eine gröbere uniforme Alternative. Mit Hhat=Rhat*W9Rhat gilt
für theta>0 die obere Young-Hülle und für 0<theta<1 zusätzlich die untere:

\[
R^*W_9R\preceq(1+\theta)Hhat+(1+\theta^{-1})T^*Q_DT,
\tag{9}
\]
\[
R^*W_9R\succeq(1-\theta)Hhat-(\theta^{-1}-1)T^*Q_DT.
\tag{10}
\]

Für eine feste Richtung und eine gerichtete Einschließung e_lo<=Hhat[z]<=e_hi
sowie d_z>=z*T*Q_DTz gilt schärfer in Normform

\[
\bigl(\max(0,\sqrt{\max(0,e_{lo})}-\sqrt{d_z})\bigr)^2
\le\langle Rz,W_9Rz\rangle
\le(\sqrt{e_{hi}}+\sqrt{d_z})^2.
\tag{11}
\]

Numerische Approximationen der Features von Rhat erfordern ihre **eigenen**
Integrations-/Rundungsgrame zusätzlich zu (7). DeltaD ist der Fehler der
festen Antwortmodellierung, nicht der Name aller späteren Rechenfehler.
Eine negative Vergleichsrichtung ist erst bewiesen, wenn die gerichtete
Energie-Untergrenze die gerichtete K_P-Obergrenze übersteigt.
Eine positive finite Vergleichsmatrix bestätigt nur den untersuchten Raum;
der vollständige Schalenrest und der kompakte Gate einschließlich -Pi0 bleiben offen.

## 5. Bereits herleitbare, aber praktisch unbrauchbare obere Norm

Als Absicherung der Schnittstelle lässt sich aus den vorhandenen Daten eine
wirkliche obere Normschranke herleiten. Dies setzt weder einen unteren
Normzeugen als Obergrenze ein noch ersetzt es W9 durch die echte A9-Inverse.
Setze Xi=C8 C8*/(1-rho), gamma_M>=||M||² und HB>=B8 B8*.
Aus ||Phi||,||T_h||<=sqrt(gamma_M) und der Zweiterm-Ungleichung folgt

\[
\|U_8\|\le\gamma_M\left[\delta^{-1}+2\operatorname{tr}\Xi+
2\delta^{-2}\operatorname{tr}(\Xi H_B)\right]=:u_0.
\tag{12}
\]

Die Spur von Xi wird exakt aus den rationalen C8-Einträgen berechnet;
tr(Xi HB) und gamma_M sind gebundene gerichtete Eingaben. Es folgt u0<10^27
(gerade) bzw. <10^24 (ungerade). Diese groben Dezimaloberwerte heißen u.
Die Domänenherleitung liefert ||F_o||<16, ||g_F||<10^11,
||Q9^np F_o||<10^11 und ||g||<1000. Lambda_T ist in W_X isometrisch.
K>10^-16 I wird hier erneut mit zwölf exakten Pivots je Parität geprüft.
Daher sind

\[
v_*=16+10^{11}u,\quad a_*=10^{11}+10^{14}u,
\quad n_*=1+1000u+a_*10^{16}v_*
\]

gültige obere Normen für f->v, a_fin und N:f->nu. Für a_fin wird
q[F_o,Lambda .]-g_F*U8g verwendet, nicht die Kopplung der echten A8-Inverse.
Aus der alten Basisgeometrie folgt für die in (1) verwendete hohe Majorante

\[
h_*:=\frac{11}{10}\left[\frac5{21\beta}+1.000502\operatorname{tr}P_{upper}\right]
<65000\ \text{bzw.}\ <11000.
\]

Die rationale Spurprüfung wird wiederholt; die Positivität von P_upper bleibt
der geerbte vollständige 287-Pivot-Nachweis. Somit gilt tatsächlich

\[
\|W_9\|\le u+10^{16}v_*^2+h_{cap}n_*^2=:w_0<w.
\tag{13}
\]

| Nach außen vereinfachte Obergrenze | gerade | ungerade |
|---|---:|---:|
| w für die Norm von W9 | 10^195 | 10^183 |
| Gewählte skalare Obermatrix für DeltaD*W9 DeltaD | 10^121 I | 10^109 I |
| obere Fehlerenergie des ganzen R-Rhat auf der W-Einheitssphäre | 10^134 | 10^120 |

Die zweite Zeile bedeutet: **DeltaD*W9 DeltaD wird durch diese Matrix
majorisiert**; es ist keine obere Grenze für beliebige zulässige Q_D.
Diese Zahlen sind bloße verfügbare Oberpreise, keine Größenabschätzung des
wirklichen Fehlers und kein Nachweis einer notwendigen Verstärkung.
Sie sind für die aktuelle Entscheidung nicht brauchbar. Die kleine
Hilbertnorm des Modellfehlers rechtfertigt daher für sich allein weiterhin
keine Aussage „gewichteter Fehler vernachlässigbar“. Eine scharfe Q_D-Hülle
nach (7) oder ein wesentlich besserer globaler Normbeweis bleibt Arbeitsbedarf.

## 6. Konkreter nächster Rechenplan und Stopkriterium

1. Dieselben zwölf physischen Residualfunktionen reproduzierbar auswerten.
   Exakte Momentprojektionen, alle Gamma-Ränder und Prim-Schnittstellen erhalten.
   e_sigma-Momente, y_h*y_h, B8 y_h sowie y_F*y_h und y_J*y_h gemeinsam aufbauen.
2. Die 84 bloßen Paarungen (Lambda J)*f ergänzen. Daraus die U8-, Zwölfer- und
   Basis84-Energie nach (3),(4) bilden.
   Sie bleiben als Teilenergie beschriftet, solange der R_L-Block fehlt.
3. nu als vollständiges Funktional auf T konstruieren und R_L nach (5),(6)
   auswerten; Nebenbedingungen, Momentkorrekturen und unendlichen Rest bezahlen.
4. Parallel E=DeltaD mit den fünf gewichteten Features aus (7) einschließen.
   Ein ungerichteter Funktionswert oder ein alter chi_p-Preis ist kein Q_D.
5. Erst aus sämtlichen vier Energieanteilen eine vollständige numerische
   Vergleichsmatrix auf dem Grad-11-Raum bilden. Auflösungen, Modellfehler und
   Gram-Whitening kontrollieren; einen möglichen Kandidaten getrennt einfrieren.

Ein zertifizierter **positiver Teilenergiebeitrag** könnte schon zum Ausschluss
reichen, wenn seine Untergrenze K_P übersteigt. Das wäre ein zulässiger anderer
Ausschlussweg, aber keine Berechnung der vollständigen Energie. Für eine
obere Nichtausschluss-/Positivitätsaussage darf kein positiver Anteil fehlen.

Das aktuelle Freigabegate für die vollständige numerische Matrix lautet
`MISSING_NEW_RESIDUAL_FEATURES`. Es fehlt keine neue Bibliothek oder externe
Quelle, sondern es fehlen die benannten **neuen Funktionsintegrationen**.
Die vorhandenen Maps jetzt zu einer „vollen W9-Matrix“ zusammenzusetzen wäre
inhaltlich falsch. Dieses Inventarpaket startet diese nächste Großrechnung nicht.

## 7. Abnahme und Grenzen

Pflicht: alle Eigen-/Eingabebindungen, Dimensionen beider Paritäten/Auflösungen,
288 exakte K-Inverseinträge, 24 positive K-Bodenpivots, rationale Norm- und
Fehlerpreisrechnung, sechs nichtkommutierende Feature-Gram-Kontrollen und
24 Young-Matrixidentitäten, Gegenmodelle für ausgelassene Kreuzterme und
für die Verwechslung von Normunter- und -obergrenze. Frischer Archiv-Replay
muss `INVENTORY.json` bytegleich erzeugen. Registry-Validator, Ansichten und
zugehörige Tests sowie anwendbare CI gehören zur Integration.

Die Kontrollmodelle sind Algebra, keine Objekt-X-Energiedaten. Keine alte
Großintegration und kein alter 287-/574-Pivot-Lauf wird als frisch gerechnet
ausgegeben. Keine externe mathematische Prüfung, Regelbestätigung, N12-
Entscheidung, A9->A11-Fortsetzung, Objekt-X-Konstruktion oder RH-Folgerung.
