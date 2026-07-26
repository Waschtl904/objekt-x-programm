# NEU-219y — Unit-Slot-Zeuge und Abschluss des kanonischen Basislift-Rotationspfads

## Knoten

`[O-219-5e1j-unit-slot-witness]`

## Ziel

Für
\[
\widetilde\omega_{\beta,\chi}\!\left(U_{g^{-1}}j_M(D_g(a_0)\mu_P)\right)
\]
ist ein explizites \(a_0 \in A_{\mathrm{alg}}\) mit \(W(a_0) \neq 0\) zu konstruieren oder ein strukturelles Vanishing nachzuweisen.

## 0. Quellenbefund und verbindliche Konventionen

Schreibe \(g = m/n\), \(m,n \in \mathbb{N}^\times\), \((m,n)=1\).

Verwendet werden ausschließlich die bestätigten NEU-211-Formeln:
\[
D_g(e(r))=0,
\]
\[
D_g(\mu_k) = \mu_{mk_0}G_{k_0,d}\mu_{n_0}^*, \qquad d=(n,k),\ n=dn_0,\ k=dk_0,
\]
\[
D_g(\mu_k^*) = -\mu_{m_0}G_{k_1,e}\mu_{nk_1}^*, \qquad e=(m,k),\ m=em_0,\ k=ek_1,
\]
mit \(G_{a,d} = \lim_N(\sigma_a(X_N)-\rho_d(X_N)) \in B^{\log}\).

Ferner: Nica-Relation \(\mu_A^*\mu_B = \mu_{B/d}\mu_{A/d}^*\), \(d=(A,B)\); \(f\mu_k=\mu_k\sigma_k(f)\), \(\sigma_k\rho_k=\mathrm{id}\); \(\gamma_k(\iota(f))=\iota(\rho_k(f))\).

**Negativer Primärquellenbefund:** Die Primärdateien NEU-219 bzw. NEU-219b lagen für diesen Audit nicht vollständig vor. Der zugängliche Übergabetext überliefert den früheren Zeugen und seine positive unrotierte Auswertung, aber nicht sämtliche dort ursprünglich genannten Nebenbedingungen an die Hilfsprimzahl \(q\). Für die überlieferte Normalform ist jedenfalls \((n,qP)=1\) notwendig, insbesondere \((n,q)=1\). Dieser Quellenrest berührt den neuen positiven Zeugen aus §5–§9 nicht und wird gesondert als Quellenvermerk geführt (siehe §13).

## 1. Exakter früher überlieferter Zeuge

\[
a_0^{\mathrm{neu}} = \mu_n\mu_{mqP}^*.
\]

Überliefert ist die unrotierte Identität
\[
a_0^{\mathrm{neu}} L^{\mathrm{cup}}(\mu_q,\mu_{p_1},\mu_{p_2},\mu_{p_3}) = \left(\prod_i \log p_i\right)\rho_n(\sigma_P(G_q)),
\]
sowie für \(\beta>1\) und jeden extremalen BC-KMS-Zustand \(\omega_{\beta,\chi}(\sigma_P(G_q))>0\).

Damit war \(a_0^{\mathrm{neu}}\) ein positiver Zeuge für die unrotierte Fünffachauswertung. Daraus folgt jedoch nichts über \(\widetilde\omega_{\beta,\chi}(U_{g^{-1}}j_M(D_g(a_0^{\mathrm{neu}})\mu_P))\), weil dort \(D_g\) auf \(a_0^{\mathrm{neu}}\) statt auf \(\mu_q\) wirkt.

## 2. Vollständige Rechnung für den früheren Zeugen

Aus \(d=(n,n)=n\): \(D_g(\mu_n)=\mu_mG_{1,n}\). Für \(k=mqP\): \(e=(m,mqP)=m\), also \(D_g(\mu_{mqP}^*)=-G_{qP,m}\mu_{nqP}^*\).

Leibnizregel liefert
\[
D_g(a_0^{\mathrm{neu}}) = \mu_mG_{1,n}\mu_{mqP}^* - \mu_nG_{qP,m}\mu_{nqP}^*.
\]

## 3. Rechtsmultiplikation mit \(\mu_P\) und Grad-Audit

Da \((mqP,P)=P\), \((nqP,P)=P\), liefert die Nica-Relation \(\mu_{mqP}^*\mu_P=\mu_{mq}^*\), \(\mu_{nqP}^*\mu_P=\mu_{nq}^*\). Somit
\[
D_g(a_0^{\mathrm{neu}})\mu_P = \mu_mG_{1,n}\mu_{mq}^* - \mu_nG_{qP,m}\mu_{nq}^* = F_q\mu_q^*,
\]
wobei \(F_q := \rho_m(G_{1,n}) - \rho_n(G_{qP,m}) \in B^{\log}\).

Globale Rechtsmodulstabilität zeigt \(D_g(a_0^{\mathrm{neu}})\mu_P \in \mathfrak{M}_{\mathrm{glob}}^{\log}\), aber die homogene Komponente ist
\[
D_g(a_0^{\mathrm{neu}})\mu_P \in \left(\mathfrak{M}_{\mathrm{glob}}^{\log}\right)_{q^{-1}},
\]
nicht die Grad-\(g\)-Komponente. Die im Arbeitsauftrag vorformulierte Behauptung \(D_g(a_0^{\mathrm{neu}})\mu_P \in M_g\) ist für diesen früheren Zeugen falsch.

## 4. Auswertung des früheren Zeugen

\[
j_M(F_q\mu_q^*) = \iota(F_q)U_{q^{-1}}, \qquad U_{g^{-1}}j_M(F_q\mu_q^*) = \gamma_{n/m}(\iota(F_q))U_{n/(mq)}.
\]

Dieser Ausdruck ist homogen vom Zeitgrad \(1/(gq)\). Jeder KMS-Zustand ist zeitinvariant; für homogenes \(x_r\) mit \(\widetilde\alpha_t(x_r)=r^{it}x_r\) folgt \(\widetilde\omega_{\beta,\chi}(x_r)=r^{it}\widetilde\omega_{\beta,\chi}(x_r)\), also \(=0\) falls \(r\neq1\).

Aus \((n,q)=1\) folgt \(gq\neq1\) (sonst \(q\mid n\)). Somit gilt unabhängig davon, ob \(F_q\) selbst null ist:
\[
W(a_0^{\mathrm{neu}})=0 \quad \text{für jeden zulässigen } \chi.
\]

**Status:** \(a_0^{\mathrm{neu}}\) als Unit-Slot-Zeuge — \(\checkmark[M]_{\mathrm{neg}}\). Dies revidiert nicht seine frühere positive unrotierte Verwendung.

## 5. Neuer kleinster gradkorrekter Zeuge

\[
a_0^\star := \mu_P^*.
\]

Grad \(P^{-1}\); da \(D_g\) den Grad mit \(g\) verschiebt, hat \(D_g(a_0^\star)\mu_P\) automatisch Grad \(g\) — exakt passend zur Gegenladung \(U_{g^{-1}}\).

Setze \(e=(m,P)\), \(m=em_0\), \(P=ek_1\); dann \((m_0,k_1)=1\) und wegen \((m,n)=1\) auch \((e,n)=1\). Adjungierte NEU-211-Formel:
\[
D_g(\mu_P^*) = -\mu_{m_0}G_{k_1,e}\mu_{nk_1}^*.
\]

## 6. Exakte nichtteilerfremde Normalform des neuen Zeugen

\((nk_1,ek_1)=k_1(n,e)=k_1\). Nica-Relation: \(\mu_{nk_1}^*\mu_{ek_1} = \mu_e\mu_n^*\). Somit
\[
D_g(\mu_P^*)\mu_P = -\mu_{m_0}G_{k_1,e}\mu_e\mu_n^* = -\mu_m\sigma_e(G_{P/e,e})\mu_n^*.
\]

Mit \(\sigma_e(G_{P/e,e}) = \sigma_e(\sigma_{P/e}(X)-\rho_e(X)) = \sigma_P(X)-\sigma_e\rho_e(X) = \sigma_P(X)-X = G_{P,1}\), und \(G_P := G_{P,1}\), folgt die von allen gcd-Fällen unabhängige Normalform:
\[
D_g(\mu_P^*)\mu_P = -\mu_mG_P\mu_n^*.
\]

Insbesondere \(D_g(\mu_P^*)\mu_P \in (\mathfrak{M}_{\mathrm{glob}}^{\log})_g\), weil \(G_P \in B^{\log}\), \((m,n)=1\) und der globale Modul unter der rechten \(A_{\mathrm{alg}}\)-Wirkung stabil ist. Es wird nicht behauptet, dass dieser Ausdruck in \(A_{\mathrm{alg}}\) liegt.

## 7. Vollständige adelische und KMS-Auswertung

\[
j_M(\mu_mG_P\mu_n^*) = \gamma_m(\iota(G_P))U_{m/n}.
\]
\[
U_{g^{-1}}j_M(D_g(\mu_P^*)\mu_P) = -U_{n/m}\gamma_m(\iota(G_P))U_{m/n} = -\gamma_n(\iota(G_P)) = -\iota(\rho_n(G_P)).
\]

Folglich \(W(\mu_P^*) = -\omega_{\beta,\chi}(\rho_n(G_P))\). Mit der inversen KMS-Identität \(\omega_{\beta,\chi}(\rho_n(f)) = n^{-\beta}\omega_{\beta,\chi}(f)\) folgt
\[
W(\mu_P^*) = -n^{-\beta}\omega_{\beta,\chi}(G_P).
\]

Verwendet wird die kanonische BC-Darstellung auf \(\ell^2(\mathbb{N}^\times)\), \(\mu_n\varepsilon_k=\varepsilon_{nk}\), \(H\varepsilon_k=\log(k)\varepsilon_k\), extremale Gibbs-Zustände für \(\beta>1\): \(\omega_{\beta,\chi}(f) = \frac{1}{\zeta(\beta)}\sum_{k\ge1}k^{-\beta}f(k\chi)\).

## 8. Strikte Positivität von \(\omega_{\beta,\chi}(G_P)\)

Faktorialtiefe \(\nu(x)=\max\{j : x \in (j+1)!\widehat{\mathbb{Z}}\}\); \(G_P(x)=c_{\nu(Px)}-c_{\nu(x)} \ge 0\) für \(x\neq0\), da Multiplikation mit \(P\) die Teilbarkeitstiefe nicht verkleinert.

Sei \(J=\min\{j\ge1 : P\mid(j+1)!\}\), \(r=(J+1)!/P\). Für jedes \(\chi \in \widehat{\mathbb{Z}}^{\,*}\): \(\nu(r\chi)<J\), \(\nu(Pr\chi)=J\), also \(G_P(r\chi)=c_J-c_{\nu(r\chi)}>0\).

Alle Gibbs-Summanden sind nichtnegativ, der \(r\)-te Summand strikt positiv. Somit \(\omega_{\beta,\chi}(G_P)>0\) für alle zulässigen extremalen \(\chi\) — nicht bloß generisch. Damit \(W(\mu_P^*)<0\).

## 9. Vollständige Vanishing-Analyse des positiven Zeugen

- \(G_P \neq 0\) (folgt aus \(G_P(r\chi)>0\)).
- \(D_g(\mu_P^*)\mu_P \neq 0\), insbesondere \(D_g(\mu_P^*) \neq 0\).
- \(\deg(D_g(\mu_P^*)\mu_P)=g\), \(\deg(U_{g^{-1}}j_M(\cdots))=1\) — keine Gradannihilation.
- Das KMS-Funktional löscht das neutrale positive Element nicht aus; Nichtverschwindung gilt für alle zulässigen extremalen \(\chi\).

## 10. Konsequenz für die Rotation

Mit \((a_0,a_1,a_2,a_3,a_4)=(\mu_P^*,\mu_{p_1},\mu_{p_2},\mu_{p_3},1)\):
\[
\Phi_0(\mathbf{a})=0, \qquad (t\Phi_0)(\mathbf{a}) = -\left(\prod_{i=1}^3\log p_i\right)n^{-\beta}\omega_{\beta,\chi}(G_P) \neq 0.
\]

Somit existiert kein \(C \in \mathbb{C}\) mit \(t\Phi_0=C\Phi_0\):
\[
\boxed{t\Phi_0 \neq C\Phi_0 \quad \forall C \in \mathbb{C}.}
\]

Diese Aussage benutzt weder die zurückgerollte Formel \(t\Phi_0=g^{-\beta}\Phi_0\) noch eine Vorabwahl \(s=-1\).

## 11. Revidierter DAG-Status

- \(a_0^{\mathrm{neu}} = \mu_n\mu_{mqP}^*\) im Unit-Slot-Test: \(\checkmark[M]_{\mathrm{neg}}\).
- \(a_0^\star = \mu_P^*\), \(W(a_0^\star)<0\): \(\checkmark[M]\).
- `[O-219-5e1j-unit-slot-witness]`: \(\checkmark[M]\).
- `[O-219-5e1j-explicit-cup-rotation]`: \(\checkmark[M]_{\mathrm{neg}}\).

Der kanonische skalare Basislift besitzt keine globale konstante Rotationseigenrelation. Der Weil-/Gammafaktorpfad und nichtkanonische Reparaturpfade werden dadurch nicht entschieden.

Da der Unit-Slot-Zeuge erfolgreich konstruiert wurde, wird kein neuer atomarer Reparaturknoten eröffnet.

## 12. Endstatus

\[
[O\text{-}219\text{-}5e1j\text{-unit-slot-witness}] \quad \checkmark[M],
\]
\[
[O\text{-}219\text{-}5e1j\text{-explicit-cup-rotation}] \quad \checkmark[M]_{\mathrm{neg}},
\]
mit dem zentralen Resultat
\[
\boxed{t\Phi_0 \neq C\Phi_0 \quad \forall C \in \mathbb{C}.}
\]

## 13. Quellenvermerk (kein DAG-Knoten)

\[
[Q\text{-}219y\text{-historische-}q\text{-Bedingungen}] \quad \text{offene Quellenlücke, ohne Einfluss auf den Abschluss.}
\]

Die vollständigen ursprünglichen Nebenbedingungen an die Hilfsprimzahl \(q\) aus den nicht auffindbaren Primärdateien NEU-219/NEU-219b sind nur partiell rekonstruiert (bekannt: \((n,qP)=1\), insbesondere \((n,q)=1\)). Dieser Vermerk ist rein dokumentarisch und berührt \(\checkmark[M]\) für `[O-219-5e1j-unit-slot-witness]` nicht.
