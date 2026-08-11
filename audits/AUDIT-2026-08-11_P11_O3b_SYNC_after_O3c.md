# P11-O3b-SYNC — Synchronisation nach verifiziertem O3c

**Datum:** 2026-08-11  
**Knoten:** `[P11-O3b-SYNC]`  
**Vorgänger:** O3b, O3c  
**Modus:** `PASS-A ACTIVE`  
**Scope-Firewall:** kein O4, keine Residualroute, kein SYN, kein Seal.

---

## 0. Zweck

Dieser Synchronisationsknoten ändert **nicht** den Satz O3b.1 und ersetzt O3b nicht historisch. Er dokumentiert ausschließlich die durch O3c mathematisch notwendig gewordene Neuinterpretation der in O3b verwendeten Skalen.

O3c wurde adversarial gegengeprüft und bestand den vollständigen Gegencheck. Insbesondere wurden unabhängig bestätigt:

\[
\sup_T\|R_T\mathbf1_T\|^2<\infty,
\]

\[
\langle\mathbf1_T,A_T\mathbf1_T\rangle=2T+O(1),
\]

und für einen festen glatten ungeraden alten/source Testvektor `f_-` mit erstem nichtverschwindendem Boundary-Jet `m`:

\[
\sigma_T(J_{R,T}f_-)
\ge
c_m^2|\beta_R^{(m)}(f_-)|^2
\frac{e^T}{T^{2m+2}}
\bigl(1+O(T^{-1})\bigr).
\]

---

## 1. Was aus O3b unverändert gültig bleibt

O3b.1 beweist für jede primitive Dualzerlegung

\[
h_{T,f_-}=(R_T^{(1)})^*Y_T+Z_T
\]

mit erstem nichtverschwindendem Boundary-Jet `m`:

\[
\boxed{
\|Z_T\|_2^2
\ge
c_{R,f_-,m}
\frac{e^T}{T^{2m+2}}.
}
\tag{O3b-SYNC.1}
\]

Dieser Satz bleibt vollständig bestehen.

Sein Beweis benutzt nur

\[
R_T^{(1)}\mathbf1_T=0,
\]

\[
\langle Z_T,\mathbf1_T\rangle
=
\langle h_{T,f_-},\mathbf1_T\rangle,
\]

sowie die C4-Paarungsasymptotik

\[
|\langle h_{T,f_-},\mathbf1_T\rangle|^2
\asymp
\frac{e^T}{T^{2m+1}}.
\]

O3c verändert keinen dieser Inputs.

Status:

\[
\boxed{[O3b.1]\quad\checkmark[M]\ \text{unverändert}.}
\]

---

## 2. Was superseded ist

O3b verglich die primitive Zertifikatskosten-Untergrenze

\[
\frac{e^T}{T^{2m+2}}
\]

mit der damals committed C4-Untergrenze

\[
\frac{e^T}{T^{2m+3}}.
\]

Daraus entstand die Interpretation, die primitive C5d-artige Zertifikatsroute sei bereits aus Skalengründen um einen Faktor `T` zu grob für eine matching odd upper bound.

Diese Interpretation ist durch O3c superseded.

Denn O3c beweist den stärkeren Konstantenmode-Nenner

\[
\boxed{
\langle\mathbf1_T,A_T\mathbf1_T\rangle=2T+O(1)
}
\tag{O3b-SYNC.2}
\]

und damit die verschärfte echte Schurterm-Untergrenze

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\gtrsim
\frac{e^T}{T^{2m+2}}.
}
\tag{O3b-SYNC.3}
\]

Somit liegen nun

\[
\underbrace{\|Z_T\|^2}_{\text{primitive Zertifikatskosten-Untergrenze}}
\gtrsim
\frac{e^T}{T^{2m+2}}
\]

und

\[
\underbrace{\sigma_T(Jf_-)}_{\text{echtes Lower Certificate}}
\gtrsim
\frac{e^T}{T^{2m+2}}
\]

auf derselben Skala.

Daher sind insbesondere die in O3b verwendeten Aussagen

\[
\sigma_T(Jf_-)
\lesssim
\frac{e^T}{T^{2m+3}}
\]

als damaliger Zielmaßstab sowie die Schlussinterpretation

\[
\text{„primitive Route ist um Faktor }T\text{ zu grob“}
\]

**nicht mehr aktueller mathematischer Stand**.

Dies ist eine Scope-/Interpretationskorrektur, keine Widerlegung von Satz O3b.1.

---

## 3. Neuer aktueller Zielmaßstab

Der nächste scharfe odd Upper-Bound-Target lautet jetzt:

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\stackrel{?}{\lesssim}
C_{R,f_-}
\frac{e^T}{T^{2m+2}}.
}
\tag{O3b-SYNC.4}
\]

Eine solche Abschätzung würde zusammen mit O3c erstmals die Zwei-Seiten-Skala

\[
\boxed{
\sigma_T(J_{R,T}f_-)
\asymp
\frac{e^T}{T^{2m+2}}
}
\tag{O3b-SYNC.5}
\]

für feste glatte odd Richtungen liefern.

Dieser obere Bound ist **nicht** bewiesen.

Status:

\[
\boxed{?[O]_{\rm matching\ odd\ upper\ bound}.}
\]

---

## 4. Primitive Route: neue korrekte Interpretation

Aus O3b.1 und O3c folgt **nicht**, dass die primitive Route erfolgreich ist.

Es folgt nur:

\[
\boxed{
\text{Die primitive Route ist nicht mehr allein aus Skalengründen ausgeschlossen.}
}
\tag{O3b-SYNC.6}
\]

Offen bleibt, ob man tatsächlich eine primitive Dualzerlegung

\[
h_{T,f_-}=(R_T^{(1)})^*Y_T+Z_T
\]

konstruieren kann mit

\[
\|Y_T\|^2+\|Z_T\|^2
\lesssim
\frac{e^T}{T^{2m+2}}.
\tag{O3b-SYNC.7}
\]

Ebenso offen bleibt, ob dafür der volle Rest `R_T` benötigt wird.

---

## 5. Keine Konditionsfolgerung

Auch nach O3c und diesem Sync folgt noch nicht:

\[
\kappa(A_{R,-}^{T,U})\to\infty,
\]

noch

\[
\chi_{R,-}^{T,U}\to\infty,
\]

noch

\[
\chi_{R,-}^{T,U}\|\Theta_-^{T,U}\|\not\to0,
\]

noch eine Nichtkonvergenz von

\[
W_{R,S,-}^{[T]}.
\]

Der Grund ist unverändert: Für die odd Konditionszahl werden relative Wachstumsquotienten über alle odd Richtungen benötigt; ein Lower Certificate für jede feste Richtung genügt dafür nicht.

---

## 6. Statusmatrix

| Aussage | Status |
|---|---|
| O3b.1 primitive Zertifikatskosten-Untergrenze `e^T/T^{2m+2}` | `✓[M]` unverändert |
| O3c full-rest constant-mode bound | `✓[M]` |
| `\langle1_T,A_T1_T\rangle=2T+O(1)` | `✓[M]` |
| odd Lower Certificate `e^T/T^{2m+2}` | `✓[M]` |
| O3b Faktor-`T`-Interpretation | `SUPERSEDED` |
| primitive Route aus Skalengründen ausgeschlossen | `×[M]` als aktuelle Aussage |
| primitive matching upper bound | `?[O]` |
| full-rest matching upper bound | `?[O]` |
| odd Zwei-Seiten-Asymptotik | `?[O]` |
| odd Konditionszahl entschieden | `?[O]` |
| O4 / Residualroute / SYN / Seal | `BLOCKED` |

---

## 7. Nächster zulässiger Knoten

Der mathematisch scharfe nächste Schritt ist:

\[
\boxed{
[P11\text{-}O3d]\quad
\text{Matching-Odd-Upper-Bound-Audit auf der Skala }
\frac{e^T}{T^{2m+2}}.
}
\]

Dabei sind zwei Routen getrennt zu prüfen:

1. **primitive Dualroute:** Kann C5d-artige Observability für den geraden Hubvektor `h_{T,f_-}` so modifiziert werden, dass die Zertifikatskosten auf `e^T/T^{2m+2}` bleiben?
2. **full-rest Dualroute:** Können die nichtprimitiven Reststufen zusätzliche Approximation liefern, ohne die Kostenordnung zu verschlechtern?

Keine der beiden Routen ist durch diesen Sync entschieden.

---

## 8. Gesamtfirewall

\[
\boxed{
\texttt{O3b.1 VALID / O3b SCALE INTERPRETATION SUPERSEDED / O3d OPEN}
}
\]

und weiterhin

\[
\boxed{
\texttt{P11 PASS-A ACTIVE / ORIGINAL TRANSPORT OPEN / SYN BLOCKED}.
}
\]
