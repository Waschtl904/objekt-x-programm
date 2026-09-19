# Die vollständige Shellantwort der Near-Null-Richtung bleibt positiv

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 19. September 2026.

Für B=log(5)/2 und das ganze Intervall 0<b-B<=10^-20 ist der verlangte
gerichtete Test geschlossen. Untersucht wird die bereits festgelegte
Grad-62-Quelle v_B und ihre L2-Projektion w_v=v_B-c_v psi. Ihre physische
Norm wird beibehalten; sie wird nicht nachträglich auf eins normiert.

Die gerichtete Rechnung liefert:

| Größe | Ergebnis, hier verkürzt dargestellt |
|---|---:|
| c_v | 0,298651520175487… > 0 |
| q_B[psi] | 0,145813467002544… |
| a_0[w_v] | 0,0130055059199525… |
| d[c_v e] | 0,0130055012660849… |
| c_0(w_v,c_v e) | -0,0130055035927460… |
| Trace-Probequotient rho_e | 0,999999999958101835… |
| Gesamtes zusätzliches Shellresiduum | < 5 × 10^-18 |
| Vollständiger gerichteter Schurrest r_v | > 5,449 × 10^-13 |

Die exakten rationalen Intervalle stehen in `direction_results.json`.
Die Rekonstruktionsidentität ist symbolisch exakt überprüft; die drei
Formwerte summieren sich einschließlich des doppelten Kreuzterms zur
ursprünglichen Quellenenergie von ungefähr 5,45323 × 10^-13.

Entscheidend ist die vollständige Shellkontrolle. Für
y_N=q_B(w_v,psi)/q_B[psi] · e wird die Trace-Komponente der Riesz-Gleichung
exakt erfüllt. Das verbleibende Funktional ist die Kopplung der
A-orthogonalen Hilfsrichtung v_B-q_B(v_B,psi)/q_B[psi] · psi an das gesamte
Shellprofil. Der bereits bewiesene Boden 70 ||s||² kontrolliert dessen
vollständige duale Norm. Es wird kein unendlicher Tail weggelassen.

Damit gilt auf dem gesamten genannten Intervall:

\[
0.999999999958101835247772515802
\le \eta_v(b)
\le 0.999999999958102151489693134390 < 1,
\]

\[
5.44902716834069532\,10^{-13}
\le r_v(b)\le
5.44906829720240261\,10^{-13}.
\]

Das ist ein positiver Befund für eine Core-Richtung mit **beliebiger
vollständiger Shellantwort**. Der gesamte reduzierte Core, sein Komplement
und die Odd-Fortsetzung bleiben offen. Ein All-Source-Satz rechts von B
folgt daraus noch nicht. Der Rest r_v ist außerdem kein Rayleighquotient:
||v_B||² beträgt etwa 0,16543536 und ||w_v||² etwa 0,11751291.

Eine Aussage des eingereichten Reviews wird korrigiert: Weil
K=C_0* D^-1 C_0 hier beschränkt und positiv ist, folgt für ein festes b aus
R_0>=sigma I tatsächlich Theta_0<=M/(M+sigma)<1, sobald K<=M I.
Zusammen mit der bekannten Umkehrung sind die Gates unter diesen
Voraussetzungen äquivalent. Für eine uniforme Aussage müssen sigma und M
uniform kontrolliert sein. Das ersetzt keinen Nachweis dieser Konstanten.

Der Checker besteht 31 neue Prüfungen und reproduziert die 28 Prüfungen
des Quotientensatzes sowie dessen 43 Shell-Pivot-Prüfungen. Alle 41
gebundenen Eingaben, Ergebnisdateien und SHA-256-Einträge werden geprüft.
Analytische Beweise stehen ausdrücklich getrennt vom endlichen Checker.
Keine Quadratur als Beweis, keine dritte Mellinbedingung, kein A1.

Das Paket wird ausschließlich ergänzend auf der Forschungsbranch abgelegt.
main und der Merge von PR #137 bleiben unverändert. Der epistemische
Status bleibt AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN.
