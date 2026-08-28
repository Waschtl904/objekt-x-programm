# Audit-Kandidat: SW1-KNF — Disjoint-Window Kernel Normal Form

> **Stand:** 28. August 2026  
> **Repo-Basis dieses Audits:** `main@f2a5afcf98cef2ff2b73b2cf62cca329cc98ef33`  
> **Status:** `?[O]` — neuer Kandidat, noch kein adversariales GREEN, keine Promotion.  
> **Scope:** ausschließlich SW1, \(0<\sigma\le R<\varepsilon,\ R+\varepsilon<\Delta\).

---

## 0. Firewall (zuerst lesen)

Dieses Audit beweist — wenn es GREEN wird — **ausschließlich** eine sektorale Koordinaten-Normalform des inneren Kernels auf SW1. Es beweist **nicht**:

- kein globales FG-1;
- kein globales FG-TR1;
- kein A0 (volle freie-Koordinaten-Abdeckung);
- keine Trivialität von \(\mathcal K_R\) (der Raum rechts ist weiterhin unendlichdimensional);
- kein HT-RED (Full-Rest-/Schur-Elimination);
- keine Aussage über \(\ker\Gamma_I\);
- keine Mitpromotion von SW1-BL7, SW1-2TP oder SW1-AWI (separate, noch ungeprüfte Kandidaten).

\[
\boxed{\text{SW1-KNF ist eine sektorale Koordinaten-Normalform, kein Injektivitätssatz.}}
\]

---

## 1. Ausgangslage

Auf SW1 gilt per Definition
\[
0<\sigma\le R<\varepsilon,\qquad R+\varepsilon<\Delta.
\]

**Behauptung 1 (Skalenungleichung).**
\[
\boxed{2R<R+\varepsilon<\Delta<e<d.}
\]

*Beweisskizze (zu verifizieren):* \(R<\varepsilon\Rightarrow 2R<R+\varepsilon\). Die SW1-Bedingung liefert direkt \(R+\varepsilon<\Delta\). Die Ordnung \(\Delta<e<d\) folgt aus den globalen Parameterordnungsannahmen des Rahmens (Referenz auf die kanonische Konstantenordnung nachzutragen). **Zu prüfen im Review:** ob \(\Delta<e<d\) tatsächlich unabhängig von SW1 gilt oder selbst aus SW1 gefolgert werden muss.

---

## 2. Disjunktheit der drei Radius-\(R\)-Samplingfenster

Definiere
\[
I_a=(a-R,a+R),\qquad I_b=(b-R,b+R),\qquad I_T=(T-R,T+R).
\]

**Behauptung 2 (paarweise Disjunktheit).** Unter Behauptung 1 sind \(I_a,I_b,I_T\) paarweise disjunkt und liegen vollständig in \((0,T_0)\).

*Beweisskizze (zu verifizieren):*
- \(I_a\cap I_b=\emptyset\): erfordert \(a+R<b-R\), d.h. \(b-a>2R\). Zu prüfen gegen die konkrete Definition von \(b-a\) im Rahmen (vermutlich \(=\Delta\) oder ein Vielfaches).
- \(I_b\cap I_T=\emptyset\): analog mit \(T-b>2R\).
- \(I_a\cap I_T=\emptyset\): folgt aus den beiden vorigen, falls die Punkte in der Reihenfolge \(a<b<T\) liegen.
- Vollständige Enthaltenheit in \((0,T_0)\): insbesondere \(T+R<T_0=T+\varepsilon\), was aus \(R<\varepsilon\) folgt.

**Explizit zu prüfen:** keine versteckte physische Identifikation zwischen den sechs Randpunkten \(a-R,a+R,b-R,b+R,T-R,T+R\) und keiner anderen ausgezeichneten Stelle des Rahmens (z. B. \(2a\), \(2d\)) modulo der Sampling-Symmetrien.

---

## 3. Horizon-Legalität des \(T+u\)-Astes

**Behauptung 3.** Für alle \(0<u<R\) gilt \(T+u<T_0\), also ist der \(T+u\)-Ast vollständig horizon-legal.

*Beweisskizze:* \(u<R<\varepsilon\Rightarrow T+u<T+\varepsilon=T_0\). **Zu prüfen:** ob "horizon-legal" im Rahmen noch weitere Bedingungen verlangt (z. B. Nicht-Overlap mit einem separaten Horizon-Fenster), die hier nicht übersehen werden dürfen.

---

## 4. Reduzierte Kernelgleichung

**Behauptung 4.** Unter den Behauptungen 1–3 reduziert sich die Kernelgleichung \(E_I^*Hy=0\) für \(0<u<R\) exakt auf
\[
p\,[y(a-u)-y(a+u)] + r\,[y(b-u)-y(b+u)] + q\,[y(T-u)-y(T+u)] = 0.
\]

*Beweisskizze:* Da \(I_a,I_b,I_T\) paarweise disjunkt sind (Behauptung 2) und keine weiteren Branchpunkte in diese Fenster fallen (Behauptung 3), tragen keine anderen Terme zur Zeile bei. **Zu prüfen:** vollständiger Abgleich mit der Definition von \(E_I^*H\) im Rahmen — insbesondere, dass \(p,q,r\) tatsächlich genau diese drei Fenster gewichten und keine weiteren Terme (Annulus, w-Terme) hier auftreten.

---

## 5. Explizite Rekonstruktion

**Behauptung 5.** Da \(p>0\), lässt sich Behauptung 4 eindeutig nach \(y(a-u)\) auflösen:
\[
\boxed{
y(a-u) = y(a+u) -\frac rp\,[y(b-u)-y(b+u)] -\frac qp\,[y(T-u)-y(T+u)].
}
\]

*Beweisskizze:* triviale Umformung von Behauptung 4, vorausgesetzt \(p\neq0\) (hier \(p>0\), Referenz auf die kanonische Konstantendefinition nachzutragen). **Zu prüfen:** Vorzeichen und Werte von \(p,q,r\) exakt gegen die kanonische Quelle.

---

## 6. Parametrisierung durch fünf freie Branches

Definiere die fünf freien physischen Branches
\[
(a,a+R),\quad (b-R,b),\quad (b,b+R),\quad (T-R,T),\quad (T,T+R)
\]
und
\[
\boxed{\mathcal V_R^{SW1} = (a,a+R)\cup(b-R,b+R)\cup(T-R,T+R).}
\]

**Behauptung 6 (Blindbereich exakt).**
\[
\boxed{
\mathcal Z_{R,\mathrm{SW1}}^{\rm phys} = (0,a-R)\cup(a+R,b-R)\cup(b+R,T-R)\cup(T+R,T+\varepsilon).
}
\]

*Beweisskizze:* Komplement von \(I_a\cup I_b\cup I_T\) in \((0,T_0)\), unter Verwendung von Behauptung 2. **Zu prüfen:** dass dies exakt der Blindbereich ist — nicht nur eine Teilmenge — d. h. dass jeder Punkt in diesem Komplement tatsächlich ein direkter Blindwert ist (keine indirekte Kopplung über andere Zeilen).

---

## 7. Kandidatensatz (Isomorphismus)

**Kandidatenbehauptung (SW1-KNF).**
\[
\boxed{
\mathcal K_R \cong \mathcal Z_R^+ \oplus L^2(\mathcal V_R^{SW1}) \qquad\text{auf SW1},
}
\]
mit explizitem beschränktem Isomorphismus, dessen inverse Rekonstruktion durch die Formel in Behauptung 5 gegeben ist.

**Zu prüfen für GREEN (vollständige Liste, siehe Abschnitt 8):** Wohldefiniertheit, Surjektivität (jede Kernfunktion entsteht so), Injektivität der Parametrisierung (nicht zu verwechseln mit Injektivität von \(\Gamma_I\) oder \(\mathcal K_{I,A}\) — hier geht es nur um die Koordinatenabbildung selbst), Beschränktheit in beide Richtungen.

---

## 8. Adversarialer Review-Auftrag (vor GREEN einzeln zu prüfen)

1. \(2R<\Delta\) wirklich streng aus SW1 (Behauptung 1).
2. Alle drei Fenster \(I_a,I_b,I_T\) tatsächlich vollständig innerhalb \((0,T_0)\).
3. Paarweise Disjunktheit \(I_a,I_b,I_T\) (Behauptung 2).
4. Keine versteckte physische Identifikation zwischen den sechs Branchpunkten a.e.
5. \(T+u<T_0\) für alle \(0<u<R\) (Behauptung 3).
6. Die Rekonstruktionsformel (Behauptung 5) erfüllt die Row-Gleichung exakt.
7. Jede Kernfunktion entsteht tatsächlich so — Surjektivität der Parametrisierung.
8. Beschränktheit in beide Richtungen.
9. Blindbereich exakt, nicht nur als Teilmenge (Behauptung 6).
10. Scope-Firewall vollständig eingehalten (Abschnitt 0).

Kein GREEN ohne alle zehn Punkte einzeln bestanden. Keine Promotion, keine Registry-/Front-Änderung, solange dieser Status `?[O]` ist.

---

## 9. Erwarteter Nutzen bei GREEN

\[
\boxed{\text{Auf SW1 bräuchten wir für den inneren Kernel die globale Fiber-Graph-Theorie nicht mehr.}}
\]

Das wäre eine sauberere Grundlage für SW1-BL7 (siebter Blindwert \(2d+s\)) und SW1-2TP (simultaner \(T\pm s\)-Pivot), ändert aber für sich allein nichts an HT-RED, A0 oder \(\ker\Gamma_I\).
