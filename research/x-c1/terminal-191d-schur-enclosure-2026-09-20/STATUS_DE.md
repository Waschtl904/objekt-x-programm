# Terminaler 191D-Schurtest

20.09.2026. **AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**.

Der feste Horizont `a=1` ist auf zwei tats�chliche 191x191-Schurmatrizen
reduziert, eine f�r Even und eine f�r Odd. Die vollst�ndige hohe Antwort
bleibt in den Matrixintervallen enthalten; kein hoher Modus wird durch eine
endliche Stichprobe ersetzt.

Die Rechnung verwendet exakte rationale Legendre- und Mellinmomente,
gerichtete Arb-B�lle mit 2048 Bit, f�nf Prime-Kan�le und eine explizite
Gamma-Restschranke. Nach Abzug des rationalen High-Response-Budgets wird
eine rationale Dreiecks-Vorconditionierung eingesetzt. Beide vorconditionierten
Matrizen haben Zeilenreserve gr��er als `9/10` und 191 positive gerichtete
LDL*-Pivots. Damit ist eine strikte terminale Schurreserve im angegebenen
festen Scope autorenseitig zertifiziert.

Die Aussage bleibt ein eingereichtes Paket und ist nicht in den verifizierten
mathematischen Snapshot promoviert. Der operative Gate
`TERMINAL-191D-DEFECT-SCHUR-A1` bleibt deshalb offen, bis eine unabh�ngige
Pr�fung die Eingangsidentit�ten, Richtungen der Intervalle, die vollst�ndige
High-Antwort und die LDL*-Schritte best�tigt.

Nicht behauptet werden Positivit�t au�erhalb des festen Horizonts, ein
globaler C1-Abschluss, Objekt X, globale Weil-Positivit�t oder RH. Ein
gescheiterter Vergleich der unvorconditionierten unteren Rohmatrix w�re
keine negative vollst�ndige Weil-Quelle; die ver�ffentlichte Zertifizierung
st�tzt sich ausschlie�lich auf die gerichtete vorconditionierte Untere.
