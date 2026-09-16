# Objekt X — WHAT NOT TO REOPEN

**Stand:** 16. September 2026  
**Zweck:** Sackgassen-Firewall fuer neue Agenten und spaetere Forschungsrunden.  
**Regel:** Diese Klassen nur erneut oeffnen, wenn eine neue Hypothese den dokumentierten No-Go explizit umgeht. Nicht durch Umbenennung derselben Konstruktion reaktivieren.

> Diese Datei schliesst nur die angegebenen Klassen im angegebenen Scope. Sie ist kein universelles Object-X-No-Go.

---

## 1. Pointwise scattering positivity — GESPERRT `×[M]`

Nicht erneut versuchen:

```math
\tau_a(z)=|B_a(z)|^2
```

oder irgendeine Architektur, deren Positivitaet punktweise `tau_a(z)>=0` auf der ganzen reellen Achse verlangt.

Grund:

```math
\tau_a(0)<0,
\qquad
\tau_a(z)\to+\infty.
```

Primaerquelle: `audits/P11_SCATTERING_POINTWISE_POSITIVITY_NOGO_2026-09-13.md`.

Erlaubt bleibt: nichtlokale Paley-Wiener-/Boundary-/Storage-Kompression.

---

## 2. Direkte primeweise P11 -> COMMON-JUMP Kontraktion — GESPERRT `×[M]`

Nicht erneut versuchen, den P11-Innovationstail pro Primzahl direkt kontraktiv oder reverse-kontraktiv mit den nackten Jump-Kanaelen zu identifizieren.

Auf dem tatsaechlichen translation-generated Kanalbereich expandiert der P11-Tail niedrige Frequenzen und kontrahiert andere Richtungen. Es existiert keine einheitliche Ordnung in einer der beiden Richtungen.

Primaerquelle: `audits/P11_PRIMEWISE_INNOVATION_SHORTING_NOGO_2026-09-15.md`.

Erlaubt bleibt: covariance/precision duality und relative global coupling.

---

## 3. Scalar Hub repair — GESPERRT `×[M]`

Nicht erneut versuchen, den gestoppten Taildefekt nur durch einen skalar gewichteten Root-/Hub-Term zu reparieren.

Nach Stopp bleibt ein hoeher-/unendlich-rangiger Exterior-Defekt; ein Rang-1-Rootterm kann diesen universell nicht korrigieren.

Primaerquelle: `audits/P11_PRIMEWISE_INNOVATION_SHORTING_NOGO_2026-09-15.md`.

---

## 4. Common-depth OU embedding + ordinary orthogonal shorting — GESPERRT `×[M]`

Nicht Prime- und Riemann-R-Continuum-Zellen nur als Vektoren im selben `L^2(dt)` einbetten und anschliessend den Continuum-Block orthogonal herausschurten.

Die Continuum-Zellen sind bereits total im gemeinsamen Tiefenraum; das Shorting entfernt die diskrete arithmetische Seite vollstaendig.

Primaerquelle: `audits/P11_COMMON_DEPTH_SHORTING_TOTALITY_NOGO_2026-09-15.md`.

Erlaubt bleibt: Kopplungen, die die Skalenvariable `h`, Overlap-Cone-Inzidenz oder relative Boundary-Daten erhalten.

---

## 5. Ordinary passive cascade of normalized Euler cells — GESPERRT `×[M]`

Nicht die lokalen Schur-Zellen einfach ueber alle Primzahlen als gewoehnliche passive Kaskade multiplizieren.

Fuer festes reelles `s>0` kollabiert das Produkt auf null; der Cayley-Transfer wird trivial und verliert die Arithmetik.

Primaerquelle: `audits/P11_PASSIVE_EULER_CASCADE_COLLAPSE_NOGO_2026-09-15.md`.

Erlaubt bleibt: relative diskret/continuum Renormierung innerhalb eines groesseren konservativen Systems.

---

## 6. Local positive finite-part Hamiltonian by common scalar subtraction — GESPERRT `×[M]`

Nicht Prime- und Continuum-Hamiltonians lokal positiv addieren und danach nur einen gemeinsamen divergenten Skalar abziehen, um einen endlichen positiven kritischen Hamiltonian zu erhalten.

Der renormierte Eigenwert enthaelt `J_Delta(L)` und ist bereits bei `L=0` negativ:

```math
J_\Delta(0)=-\gamma<0.
```

Primaerquelle: `audits/P11_CRITICAL_RATE_LOCAL_RENORMALIZATION_NOGO_2026-09-15.md`.

Erlaubt bleibt: relative Rand-/Transfer-/Spektralverschiebung in einem unrenormiert positiven Elternsystem.

---

## 7. Static higher-Gamma frame repair — GESPERRT `×[M]`

Nicht argumentieren:

```text
P11 behaelt den OU-Grundmodus;
hoehere Gamma-Moden sind dicht;
also kontrollieren sie den verlorenen Tail uniform.
```

Die hoeheren Gamma-Exponentialmoden sind zwar total/dicht im passenden Tailkomplement, besitzen aber keine radiusuniforme untere Frame-Schranke. Nach aussen verschobene Einheitsvektoren haben verschwindende Gamma-Koeffizienten.

Primaerquelle: `audits/P11_GAMMA_TAIL_FRAME_NOGO_2026-09-15.md`.

---

## 8. Separate Critical-half amplification of Prime and Continuum — GESPERRT `×[M]`

Dies ist die wichtigste aktuelle Firewall.

Nicht zuerst den diskreten Root-Storage und den Continuum-Root-Storage getrennt von

```math
\Lambda(n)/n
```

auf

```math
\Lambda(n)/\sqrt n
```

anheben und erst danach subtrahieren.

Die notwendige Energieverstarkung ist `e^{L/2}` und auf dem plain Root-Storage unbeschraenkt. Fuer nichtverschwindende kompakte Sources wird der grosse-Tail nach der kritischen Verstarkung konstant statt integrierbar.

Primaerquelle: `audits/P11_ROOT_TRANSPORT_SAFE_TRANSFER_AND_CRITICAL_LIFT_FIREWALL_2026-09-16.md`.

Verbindliche Folgerung:

```text
CANCEL FIRST, CRITICAL-LIFT SECOND.
```

---

## 9. Fixed-window prolate as all-window strategy — DEMOTED

Die shorted Paley-Wiener-/Prolate-Reduktion und das Trace-minus-Ritz-Lemma bleiben korrekt und nuetzlich als fixed-window Zertifikationswerkzeug.

Nicht mehr als skalierbare globale Hauptstrategie behandeln: die relevante time-band-limiting Region waechst extrem stark mit dem Fenster und reproduziert eine bekannte lokale-Zertifikationsbarriere.

Primaerquellen:

- `audits/P11_NP_GAP_PROLATE_COMPRESSION_2026-09-13.md`
- `audits/P11_NP_PROLATE_TRACE_RITZ_CERTIFICATE_2026-09-13.md`
- `audits/P11_HARD_AUDIT_ERRATA_AND_PROLATE_BARRIER_2026-09-15.md`

---

## 10. Old orbit-chain exact formula — KORRIGIERT

Nicht mehr schreiben

```math
N(t)=\lfloor L/t\rfloor+1
```

als exakte wesentliche maximale Kettenlaenge an ganzzahligen Verhaeltnissen `L/t`.

Korrekt ist die wesentliche maximale Kettenlaenge

```math
N(t)=\lceil L/t\rceil
```

mit der ueblichen Randmengen-Firewall. Die alte daraus abgeleitete Lower-Bound war konservativ, aber die Exaktheitsbehauptung war falsch.

Primaerquelle: `audits/P11_HARD_AUDIT_ERRATA_AND_PROLATE_BARRIER_2026-09-15.md`.

---

## 11. Zeugen-Koinzidenzen nicht verallgemeinern

Nicht erneut aus einer einzigen Prime-2-Kalibration freie universelle Koeffizienten ableiten. Insbesondere die gefundene `1/4`-Hub-Korrektur am einzelnen Zeugen war eine Koinzidenz und scheitert als Operatorgesetz.

Regel:

```text
kein freier Koeffizient darf nach Sicht auf den Prime-2 witness angepasst werden.
```

---

## 12. Bekannte Theorie nicht als Projektneuheit verkaufen

Nicht als Neuheit beanspruchen:

- `xi'/xi` als Positive-Real/Herglotz RH-Kriterium;
- Lagarias-Positivitaet;
- Zeta-Transfer-/Kontrolltheorie allgemein;
- Eulerprodukt als Determinanten-/Resolventensprache;
- OU/AR(1), Green-, Poisson-, de-Branges-, Paley-Wiener-, Toeplitz-, Prolate- oder KYP-Theorie an sich;
- klassische PNT-Fehlerabschaetzungen.

Der moegliche Projektbeitrag kann nur in einer neuen, korrekt auditierten Glueung der konkreten P11-/Overlap-Cone-/Root-Transport-/Gamma-Komponenten liegen.

---

# Reopen-Protokoll

Eine gesperrte Klasse darf nur reaktiviert werden, wenn eine neue Konstruktion schriftlich beantwortet:

1. Welcher konkrete No-Go oben wird umgangen?
2. Welche neue Hypothese/Struktur war dort nicht enthalten?
3. Warum ist es nicht nur eine Umparametrisierung derselben gescheiterten Klasse?
4. Welcher vorab festgelegte destruktive Test kann die neue Variante falsifizieren?

Ohne diese vier Punkte: **nicht reopen**.
