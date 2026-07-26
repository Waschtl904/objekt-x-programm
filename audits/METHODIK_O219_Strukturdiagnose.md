# Methodische Notiz — Strukturdiagnose O-219

## Warum O-219 länger dauert als O-217 oder O-218

O-217 und O-218 hatten die folgende Form:
$$
\text{Existierende Typen} + \text{schwierige Rechnung.}
$$

O-219 hat eine strukturell andere Form:
$$
\text{Koeffiziententyp} + \text{Orbitstruktur} + \text{KMS-Auswertung} + \text{Zyklizität}
\quad\text{müssen erst gemeinsam konstruiert werden.}
$$

Die vier Komponenten existierten im DAG bisher getrennt. O-219 ist der erste Knoten, der sie gleichzeitig koppelt.

---

## Negativentscheidungen als Suchraum-Einschränkung

Fünf scheinbar natürliche Abkürzungen haben sich als falsch erwiesen:

| Kandidat | Status | Grund |
|---|---|---|
| $e_jN_ke_j = 0$ | ✓[M]\_neg | Ecken sind vollständig, nicht annihilierend |
| $N_k$ direkt als Summe | ✓[M]\_neg | Adelische Gitter sind verschachtelt, $N_k = N_0$ |
| $\Pi$ injektiv | ✓[M]\_neg | $R$-Sättigung entfernt Orbitmarkierung |
| $\omega = \varphi_\beta\circ\Phi$ | verworfen | Keine typisierte bedingte Erwartung $N_0\to R$ |
| $U_{g^{-1}} = T^{-1}$ auf $\mathcal{N}_{\mathrm{tag}}$ | ✓[M]\_neg | Multiplikatorwirkung erhält Orbitindex |

Jede dieser Negativentscheidungen hat den Suchraum stark verkleinert. Sie sind kein Zeichen für Kreisbewegung, sondern für fortschreitende Strukturklärung.

---

## Gesicherter Stand nach NEU-219q

Die zwei zentralen Resultate sind jetzt belastbar:
$$
\widetilde{M}_{\mathrm{orb}} \cong \bigoplus_k N_0\delta_k,
$$
$$
\Omega_\lambda\!\left(\sum_k x_k\delta_k\right) = \sum_k \lambda^k\,\widetilde{\omega}_{\beta,\chi}(U_{g^{-1}}x_k).
$$

Die verbleibende Kette ist vollständig lokalisiert:
$$
\widetilde{L} \longrightarrow \kappa \longrightarrow \varepsilon \longrightarrow s \longrightarrow C(g,\beta,\lambda) \longrightarrow \lambda^*.
$$

---

## Was das Endergebnis entscheidet

Das einzelne Vorzeichen am Ende der Kette trennt drei strukturell verschiedene Resultate:

1. **$C(g,\beta,\lambda^*) = 1$ für ein geeignetes $\lambda^*$:**
 Eine echte skalare zyklische Reparatur der geladenen Koeffizientenarchitektur existiert.

2. **$\varepsilon = 0$, $s \neq 0$:**
 Der Orbitgewichtansatz kann die Ladungsobstruktion grundsätzlich nicht kompensieren. Die Architektur scheitert auf dieser Ebene.

3. **Mehrkomponentige Liftstruktur ($|F| > 1$):**
 Der bisherige Eigenwertansatz muss komponentenweise erweitert werden. Eine einzelne Indexfunktion $\kappa$ existiert nicht.

O-219 prüft damit nicht nur eine Formel, sondern die **Existenz der gesamten geladenen zyklischen Koeffizientenarchitektur**. Dass diese Prüfung länger dauert als die Konstruktion des Cup-Kozykels selbst, ist mathematisch plausibel: der Kozykel kann gebaut werden ohne zu wissen, ob er zyklifizierbar ist.

---

## DAG-Referenz

| Datei | Inhalt |
|---|---|
| NEU-219m | Negativaudit Orbit-Direktheit; $\mathcal{N}_{\mathrm{tag}}$ konstruiert |
| NEU-219n | $\varpi_{\beta,\chi}$, Eigenfamilie $\Omega_\lambda$; Multiplikatorwirkung negativ |
| NEU-219o | 9-Felder-Matrix $C(g,\beta,\lambda)$; Weg A kanonisch |
| NEU-219p | Normalform $(t\Phi_\lambda)$; $\varepsilon$ aus Indexdifferenz |
| NEU-219q | Auditrahmen $\kappa$; drei Fälle; Buchführungstabelle |
| **NEU-219r** | **Pflichtrechnung: wörtliche $\widetilde{L}$-Definition → $\kappa$ → $\varepsilon$ → $s$ → $\lambda^*$** |
