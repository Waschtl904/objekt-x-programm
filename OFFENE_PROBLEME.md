# Offene Probleme — A1-FINITE-1212

> **Stand:** 13. September 2026.  
> Operative Audits: [A1 Omega1551](audits/P11_A1_OMEGA1551_REDUCTION_2026-09-13.md) · [A1 bounded Schur remainder](audits/P11_A1_SCHUR_BOUNDED_REMAINDER_2026-09-13.md).

## Neu geschlossen

### `[A1-OMEGA1551]` `✓[K/M]`

```math
\boxed{m_1(\xi)>0.1\quad(|\xi|\ge1551).}
```

Der Beweis ist ein Exact-Head-Arb-Zertifikat mit rigorosem Digamma-Bound, Ableitungsschranke, rationalem Gitter und far-field Monotonie.

### `[A1-REDUCED-BAND]` `✓[K/M]`

Mit

```math
c=0.1,
\qquad
r=(m_1-c)\mathbf1_{[-1551,1551]}
```

ist `||r||<12` zertifiziert.

### `[A1-CROSS-1210]` `✓[K/M]`

KRD plus Arb liefert

```math
\lambda_{1210}(1551)<1.5\times10^{-42},
```

```math
\tau_{1210}>0.099,
```

und

```math
\boxed{\text{Schur penalty}<2.2\times10^{-39}.}
```

Damit sind Infinite Tail und Crossblock quantitativ absorbiert.

---

## Priorität 0 — `[A1-RESOLVED-3E39]` `?[O]`

Es bleibt **nur noch** die finite Aussage

```math
\boxed{
(L_1)_{RR}\succeq3\times10^{-39}I.
}
```

auf dem moment-augmentierten resolved PSWF-Raum

```text
N = 1210 PSWF modes
+ at most 2 moment directions
= at most 1212 dimensions
= at most 606 even + 606 odd.
```

Pflichten:

1. rigorose Darstellung des augmented PSWF-Raums;
2. interval-zertifizierte finite Matrix von `L_1`;
3. parity-getrennte Inertia/PSD;
4. lower eigenvalue bound `>=3e-39`.

`3e-39` ist ein **vorab deklarierter sufficient threshold**, kein beobachteter Eigenwert.

---

## Danach — `[A1-CERT]` `?[O]`

Der resolved lower bound plus der bereits zertifizierte Schur-Penalty ergibt die volle kanonische Completion bei `a=1`.

---

## Firewalls

- Der ältere `2300/1680`-Gate bleibt korrekt, ist aber gröber.
- Resolved lower bound ist weiterhin offen.
- Frühere Dirichlet-Ritzwerte bleiben Diagnostik.
- Fixed-window `a=1` ist noch nicht bewiesen.
- All-a NP-GAP, Object X und RH bleiben offen.
