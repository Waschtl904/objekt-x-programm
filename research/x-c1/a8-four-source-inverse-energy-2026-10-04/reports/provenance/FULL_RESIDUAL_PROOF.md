# Vier vollständige A8-Funktionsresiduen und ihre Grame

4. Oktober 2026. AUTHOR_DERIVED / EXTERNAL_REVIEW_OPEN.

## 1. Gegenstand und unveränderte Voraussetzungen

Die vier rationalen Vorschläge aus `ObjektX_A8_Vier_Antworten_2026-10-04.zip` bleiben unverändert. Es werden keine neuen Galerkinlösungen gewählt. Die ursprüngliche Weil-Form-Identifikation, die vollständigen Formräume, die Mellinkorrektur und die zugehörige Referenzoperatoridentität sind übernommene Voraussetzungen. Sie werden hier nicht von Grund auf neu bewiesen. Die alte A8-Modellmatrix ist durch SHA-256 `5f8935d53f8518540ef25e6f2d511955bad688cf5905cb63e8d89f03aae2474b` gebunden.

Für a=3 log(2)/2, b=log(3), r=a/b und U_tu(x)=sqrt(2t)u(tx) gilt auf H=L²((-1,1),dx/2):

    rhat_j = Pihat_a [sqrt(r) (Qhat_b^ext f_(b,m_j))(r x) - Qhat_a^ext phat_j(x)].

Hier ist phat_j die festgelegte Kombination aller 191 momentkorrigierten alten Profile. Die neuen Grade sind 2,4 beziehungsweise 3,5. Physisch ist r_j=U_a^(-1)rhat_j. Die Normen in beiden Darstellungen stimmen überein. In einer festen Parität p ist die Mellinprojektion

    Pihat_a g = g - m_p <m_p,g>/mu_p,
    m_0(x)=cosh(a x/2), m_1(x)=sinh(a x/2), mu_p=||m_p||².

Dies ist die ursprüngliche Momentbedingung in dieser Parität, keine zusätzliche dritte Bedingung. Alle Daten sind reell; die Gram-Identitäten gelten durch komplexe Linearisierung mit Adjungierten.

## 2. Vollständige Funktionsdarstellung

Die Referenzwirkung ist

    Qhat_t^ext = D_H + V + q0(t) - K_t - S_t,
    V(x)=-log(1-x²)/2, q0(t)=-log(2 pi t)-EulerGamma.

Der alte harmonische Anteil bleibt bei Anwendung auf phat_j ein endliches Legendrepolynom. Der alte logarithmische Anteil V(x) phat_j(x) wird NICHT abgeschnitten oder durch Punktwerte ersetzt. Alle partiellen Translationen werden mit ihren tatsächlichen Überlappungsintervallen geführt. Die gemeinsame positive Hälfte besitzt zehn Integrationszellen; die andere Hälfte folgt exakt durch Parität. Der Kanal 8 wird nur auf der neuen Seite verwendet; seine Gewichte sind log(p)/sqrt(p^k).

Die regulären Kerne werden mit dem alten gebundenen Grad 160 und dem neuen Grad 128 modelliert. Ihre vollständigen uniformen Restmajoranten epsilon_a,epsilon_b bleiben enthalten. Es gilt

    ||K_t-K_t^P|| <= 2t epsilon_t.

Auf dem eingeschränkten neuen Intervall ist V(r x) glatt. Dafür verwenden wir ausschließlich als Rechenapproximation

    V_K(r x)=sum_(k=1)^K r^(2k) x^(2k)/(2k), K=640,
    0 <= V(r x)-V_K(r x) <= tau_V
      := r^(2K+2) / [2(K+1)(1-r²)].

Die uniforme Schranke beträgt ungefähr 1.57877324457746935e-33. Ihre volle L²-Wirkung wird bezahlt. Dies ist KEIN Abschneiden des alten hohen Quellenraums.

Die vor der Mellinprojektion stehenden Modellfunktionen besitzen damit auf jeder positiven Zelle die Form

    gtilde_j(x)=A_j(x)+B_j(x)V(x)+S_(j,cell)(x), B_j=-phat_j.

`FUNCTIONS.json` enthält gerichtete Koeffizienteneinschließungen, Zellgrenzen und die Mellinprojektionsdaten. Die höchsten alten Vorschlagsgrade bleiben 382/383; die glatte Potentialapproximation führt bis zum Grad 1285. Die wahre Residualfunktion wird nicht mit diesem endlichen Modell identifiziert. Vielmehr gilt

    rhat_j = Pihat_a gtilde_j + delta_j,
    ||delta_j|| <= d_j
      := 2a epsilon_a ||phat_j||
       + (2b epsilon_b+tau_V) ||f_(b,m_j)||.

Die Projektion und die physische Einschränkung sind Kontraktionen. Die tatsächlichen Profilnormen einschließlich Mellinkorrektur werden berechnet, nicht durch Koeffizientennormen ersetzt.

## 3. Kernwirkung ohne eine hohe Modentrunkierung

Für ein Polynom p definiere

    A_k(x)=integral_(-1)^1 |x-y|^k p(y) dy.

Es gilt A_1''=2p und A_k''=k(k-1)A_(k-2) für k>=2. Die beiden Integrationskonstanten werden durch vollständige Endpunktmomente bestimmt. Für Legendrepolynome ist

    integral_(-1)^1 (1-y)^k P_n(y)dy
      =(-1)^n 2^(k+1)(k!)²/[(k-n)!(k+n+1)!]  (n<=k),

sonst null. Diese Identität folgt aus Rodrigues und n-facher partieller Integration. Zusätzlich bleibt die exakte Parität erhalten. Der Faktor der Kernelwirkung ist t integral k_reg(t|x-y|)p(y)dy; die Halbmaßnormierung wird damit vollständig berücksichtigt.

Die Rekursion wird für 81 kleine Legendre-/Kernelpaare gegen unmittelbare rationale Monomialintegration geprüft. Ein endlicher Kernelpolynom-Support ist kein endlicher Support des logarithmischen oder Shiftanteils. Alle diese Anteile gehen über vollständige Integrale in den Gram ein.

## 4. Vollständige gewichtete Integrale

Für jede Zelle werden Polynomprodukte, Polynomprodukte mit V und der globale Anteil B_i B_j V² analytisch integriert. Für M_k(t)=integral_0^t x^k V(x)dx verwendet der Erzeuger die durch partielle Integration folgenden geschlossenen Formeln. Bei geradem k:

    M_k(t)=-[t^(k+1)log(1-t²)+2(atanh(t)-sum_(j=0)^(k/2)t^(2j+1)/(2j+1))]/[2(k+1)].

Bei ungeradem k:

    M_k(t)=[(1-t^(k+1))log(1-t²)/2
             +sum_(j=1)^((k+1)/2)t^(2j)/(2j)]/(k+1).

Die Endwerte bei t=1 werden getrennt über ihre Grenzwerte berechnet; log(0) wird nicht ausgewertet. Für k=2n:

    integral_0^1 x^(2n) V(x)²dx
      = [(sum_(j=0)^n 1/(2j+1)-log2)²
          +sum_(j=0)^n 1/(2j+1)²-pi²/12]/(2n+1).

Diese Formel folgt auch durch zweimaliges Ableiten des Beta-Integrals nach dem Exponenten von 1-x². Sämtliche logarithmischen Randbeiträge sind enthalten. 63 unabhängige positive Reihen-Einschließungen prüfen die partiellen einfachen Logmomente.

Der Gram auf H ist in fester Parität gleich dem Integral über [0,1]. Nach der Integration wird die ursprüngliche Mellinprojektion über

    Gtilde_ij=<gtilde_i,gtilde_j> - beta_i beta_j/mu_p,
    beta_j=<m_p,gtilde_j>

vollständig durchgeführt. Zur Berechnung der beta-Integrale wird m_p bis Grad 200 entwickelt. Sein gesamter exponentieller Rest erhält die geometrische Majorante

    tau_m <= (a/2)^201 / [201! (1-a/(2*202))].

Der Fehler im Moment wird mit ||gtilde_j|| tau_m bezahlt. Die Modell-Grame werden also nicht mit einem bloß polynomialen Ersatz der Mellinprojektion gleichgesetzt. Der separate Audit prüft mu_p zusätzlich durch

    mu_p=[sinh(a)/a+(-1)^p]/2

mit positiven Reihen und vollständigem Rest.

## 5. Vom Modell zum wahren gemeinsamen Residualgram

Mit ntilde_j als oberer Normgrenze des projizierten Modells gilt für jeden Eintrag

    |<r_i,r_j>-<rtilde_i,rtilde_j>|
      <= ntilde_i d_j + ntilde_j d_i + d_i d_j.

Dies bezahlt beide Gamma-Abbruchreste und die glatte Potentialapproximation einschließlich ihrer Kreuzprodukte. Alle Rundungen der Funktionskoeffizienten und Integrale sind bereits in den Modellintervallen enthalten. Beide vollständigen 2x2-Grame werden als gemeinsame symmetrische Intervallmatrizen geliefert; die Offdiagonalen werden nicht entfernt.

Aus Mittelpunkt M und symmetrischen Eintragsradien R ergeben sich zusätzlich gültige Loewner-Matrizen

    M-diag(row_sums(R)) <= G_full <= M+diag(row_sums(R)).

Dies folgt aus diagonaler Dominanz. Die positiven unteren Matrizen sind eine Aussage über die Linearunabhängigkeit dieser Residualfunktionen, NICHT über eine neue Weil- oder Schurpositivität.

## 6. Vollständige niedrige/hohe Trennung

Sei Z_a die alte Profilsynthese und G_a=Z_a*Z_a=I+cc*. Der physische L²-Orthogonalprojektor ist P_low=Z_a G_a^(-1) Z_a*. Für die Residualsynthese R gilt exakt

    G_full=R*R=E*G_a^(-1)E+R_perp*R_perp,
    E=Z_a*R, R_perp=(I-P_low)R.

Der neue Eingabeaudit hat bereits B_E,scharf mit E*E<=B_E,scharf geprüft. Daher

    0 <= G_low <= B_E,scharf,
    G_full^- - B_E,scharf <= G_high <= G_full^+.

Diese Schranken erfassen ALLE hohen alten L²-Richtungen nach der momentkorrigierten Profilprojektion. Sie sind keine endliche Liste zusätzlicher Residualkoeffizienten. G_low wird als obere/untere Matrixschranke ausgewiesen, nicht als bereits exakt bekannte Matrix. Der gemeinsame hohe Gram ist in beiden Paritäten strikt positiv eingeschlossen.

Die alte inverse Residualenergie R*Q_a^(-1)R wurde nicht berechnet. L²-Masse im hohen Profilkomplement darf nicht ohne Behandlung der alten Low/High-Kopplung unmittelbar durch einen einfachen hohen Energiegap dividiert werden.

## 7. Arithmetik und unabhängige Rechenwege

Verwendet werden 800 Dezimalgitterstellen in Integer-Intervallen, längere explizit kontrollierte Reihen für log, pi, EulerGamma und Mellinmomente sowie exakte rationale Koeffizienten. Das Euler-Restargument verwendet DLMF 5.11.2 und 5.11(ii): https://dlmf.nist.gov/5.11 .

Polynomkonvolutionen werden durch exakte Kronecker-Substitution beschleunigt: Die gewählte ganzzahlige Basis ist größer als jede mögliche nichtnegative Konvolutionsziffer. Die vorzeichenbehaftete Konvolution wird über konstante Verschiebungen und exakte Präfixsummen zurückgeführt. Ein gemeinsamer Koeffizientenradius bezahlt sämtliche Produkte der Eingaberadien. Es findet keine Gleitkomma-FFT statt. 20 ganzzahlige und 36 Intervalltests vergleichen die schnelle Methode mit direkter Multiplikation.

Der separate Audit benutzt für ||Q_a^P p||² die ursprüngliche vollständige Kopplungs-Grammatrix G0, nicht die neue Integration des logarithmischen Quadrats. Der rohe hohe Anteil ist P*G0P. Die niedrigen rohen Antworten werden aus A_mod P und dem separat integrierten Momentträger rekonstruiert. Zusammen ergibt das die vollständige alte Modellwirkungsnorm.

Ein weiterer Vergleich baut den vollständigen Residualgram aus der neuen Wirkungsnorm, dieser alten Wirkungsnorm und beiden neuen/alten Kreuzpaarungen auf. Die Mellinprojektion wird danach nochmals berechnet. Zusätzlich werden je Parität sechs ausgewählte niedrige Residualpaarungen aus den vollständigen Funktionen mit den originalen Galerkinbindungen verglichen.

Die Verfahren teilen Integer-Intervallarithmetik, Eingangsdaten und einige analytische Momentformeln. Die Prüfungen sind keine externe Begutachtung und keine unabhängige Rekonstruktion der ursprünglichen Weil-Form. Der komplette A8-Matrixgenerator und die 764 ursprünglichen Kreuzformintegrationen werden nicht nochmals ausgeführt.
