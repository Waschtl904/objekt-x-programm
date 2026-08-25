# P11/R32 — unabhängiges Review-Paket: zentraler Unsichtbarkeitsraum

**Status:** Review-Anforderung; keine Promotion.  
**Kandidat:** `19b81a82a32b7283b693b6b023d4fd21c38b5c80` — `audits/P11_R32_CENTRAL_INVISIBLE_SUBSPACE_AUDIT.md`.  
**P11 FROZEN; P12 unverändert; R14 unverändert.**

Bitte direkt aus dem konkreten Drei-Shift-Hub prüfen.

## A. Zentralraum

Im Fenster
\[
2a<T_0<\tfrac12\log5,
\quad a=\tfrac12\log2,
\quad b>a,
\quad T=2a>a,
\]
fixiere `0<R<a` und
\[
\mathcal C_R^+
=\{v\in L^2(-T_0,T_0)^+:
\operatorname{ess\,supp}v\subset[-(a-R),a-R]\}.
\]

Prüfen Sie für jedes aktive `tau in {a,b,T}` und fast jedes `|u|<R`:
\[
|u\pm\tau|>a-R,
\]
und damit
\[
D_{2\tau}v(u)=0.
\]

Verdict:

```text
CI-1 CENTRAL SUBSPACE INVISIBLE: GREEN / PARTIAL / FAIL
```

## B. Unendlichdimensionalität

Bestätigen Sie, dass `C_R^+` ein geschlossener unendlichdimensionaler Unterraum ist und daher
\[
\dim\ker(E_I^*H|_+)=\infty.
\]

```text
CI-1 INFINITE-DIMENSIONAL KERNEL: GREEN / PARTIAL / FAIL
```

## C. Firewall

Prüfen Sie adversarial, dass daraus **nicht** folgt
\[
\ker(E_I^*\Sigma E_A)\ne0.
\]
Dazu wäre zusätzlich erforderlich, dass für ein nichtzero `y in N_I`
\[
(I+R^*R)y\in\operatorname{Ran}(HE_A).
\]

Die qualitative Transversalitätsfrage bleibt also offen.

```text
CI-1 SCHUR-ANNIHILATOR FIREWALL: GREEN / PARTIAL / FAIL
```

## Gesamtverdict

```text
CI-1 CENTRAL SUBSPACE INVISIBLE:          GREEN / PARTIAL / FAIL
CI-1 INFINITE-DIMENSIONAL KERNEL:         GREEN / PARTIAL / FAIL
CI-1 SCHUR-ANNIHILATOR FIREWALL:          GREEN / PARTIAL / FAIL
CENTRAL INVISIBLE SUBSPACE OVERALL:       GREEN / PARTIAL / FAIL
```

Bei vollständigem GREEN darf CI-1 als `✓[M]` gebucht werden. Keine Schur-Kernel-, Polar-Gauge-, Strong-Terminal-, Objekt-X- oder RH-Promotion.
