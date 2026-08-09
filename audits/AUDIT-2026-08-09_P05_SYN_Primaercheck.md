# P05-SYN-Primärcheck — Relative Prime Channels and Arithmetic Edge Geometry

**Datum:** 9. August 2026  
**Geprüfte SYN-Quelle:** `papers/P05_Relative_Prime_Channels_and_Arithmetic_Edge_Geometry.md`  
**SYN-Stand:** `SYN DRAFT 4`, Commit `f85aa6cd9aec98f47d7429b5a7524b1f27e7344d`  
**Pass-A-Basis:** Gruppe F `PASS A COMPLETE`, `PASS-A-PROTOKOLL.md`, Commit `9c23fc49`  
**Prüfart:** SYN-Inhaltsaudit; kein erneuter Vollaudit der historischen NEU-Knoten  
**Status:** `P05 SYN PRIMARY CONTENT CHECK COMPLETE / unabhängiger Inhaltsgegencheck ausständig`

---

## 1. Prüfprinzip

Der P05-SYN-Primärcheck prüft ausschließlich den Transfer

\[
\text{F1--F4 gültiger Endstand}
\longrightarrow
\text{P05 Markdown-SYN}.
\]

Er eröffnet keine bereits geschlossenen historischen Audits erneut. Geprüft werden:

1. Typen und Quantoren,
2. Statusmarker und epistemische Reichweite,
3. Symbolkollisionen,
4. lokale versus globale Scope-Grenzen,
5. Weiterleitungen nach P06/P09/P11.

Ein SYN-Text darf eine historische Aussage umbenennen oder typologisch disambiguieren, aber ihren mathematischen Status nicht verändern.

---

## 2. Ergebnis nach Themenblöcken

| P05-Block | Primärbefund | Status |
|---|---|---|
| §1 Typisierte Primkanalarchitektur | $T_p$, $C_p^{[\widehat\varepsilon_p]}$, $C_p^{\rm rel}[\widehat\varepsilon_p]$ korrekt getrennt; Rang-$\le1$ nur auf induzierter Ebene; intrinsisches $c_p\neq0$ nicht behauptet | `OK` |
| §2 Liftgeometrie | quadratische Normierung korrekt; keine erfundene lineare Kernfamilie; exakter Nichtnullzeuge bleibt offen | `OK` |
| §3 feste-$p$-Kollision | Injektivität und Restklassen-/Faltungsrelation korrekt; konditionale $L_3^\circ$-Voraussetzung erhalten | `OK` |
| §4 $L_3^\circ$-Herkunft | NEU-162 nur rechenzulässig; NEU-170d/173 als Endanker; Quellennegativität nicht zur mathematischen Unmöglichkeit hochgestuft | `OK` |
| §5 Quotient/Symmetrie | abstrakte Sätze von konkreter Nichttrivialität/Unitärität/Irreduzibilität getrennt | `OK` |
| §6 Primfasertransport | Transportnormalform auf $L^2(\mathbb R)\oplus L^2(\mathbb R)$ korrekt; zusammengesetzte Sektoren bleiben `[O-225-3]` offen | `OK` |
| §7 Nichtorthogonalität | generische Überlappung nicht zu universellem $K_{pq}\neq0$ hochgestuft; Nichtorthogonalität nicht als Primmischung von $D_{\rm rel}$ beschrieben | `OK` |
| §8 Primzahlpotenzen | primitiver $p$-Faktor und arithmetische $\Lambda(p^m)$-Identität getrennt; all-$n$-BC-Halbgewicht und Operatorrealisierung bleiben `CONDITIONAL` | `OK` |
| §9 Mangoldt-Träger | direkte Kreuzprimkollision korrekt vom festen-$p$-Kollisionssatz unterschieden; kein Orthogonalitäts-No-Go daraus abgeleitet | `OK` |
| §10 Routing | P06/P09/P11-Grenzen entsprechen dem Pass-A-Endstand | `OK` |
| §11 Statusmatrix | keine erkannte Hochstufung von `?[O]`/`CONDITIONAL`; negative Quellenbefunde als solche markiert | `OK` |

---

## 3. Im Primärcheck gefundene und bereits eingearbeitete Redaktionskorrekturen

### 3.1 Transportkoeffizient versus Primkanal-Amplitude

Historisch verwenden zwei Stränge das Symbol $c_p$ für verschiedene Objekte:

- F1/F2: hebungsabhängige Kanal-Amplitude $c_p$ in $P_p=|c_p|^2\Pi_p^{(1)}$;
- NEU-225/F3: Transportkoeffizient $\frac12\gamma_Np\log p$.

P05 setzt daher

\[
\boxed{\kappa_p^{\rm tr}:=\frac12\gamma_Np\log p}
\]

und schreibt

\[
D_{\rm rel}|_{\mathcal H_{p,a}}
\cong
2i\kappa_p^{\rm tr}\frac d{dt}.
\]

**Befund:** reine SYN-Disambiguierung; keine mathematische Änderung.

### 3.2 Liftkern versus Prim-/Feshbachblöcke

F2 verwendet historisch $K_p=\ker\pi_{\rm prim}$, während F3 $K_p,K_{pq}$ in der Prim-/Feshbachblockarchitektur verwendet. P05 setzt für den Liftkern

\[
\boxed{\mathscr K_p^{\rm lift}:=\ker\pi_{\rm prim}}.
\]

### 3.3 Quotientenraum versus lokaler Weil-Beitrag

NEU-159/160 verwenden $Q_p$ für den Rohkopplungsquotienten; im Gesamtprogramm bezeichnet $Q_p$ zugleich den lokalen Weil-Beitrag. P05 setzt

\[
\boxed{\mathscr Q_p^{\rm quot}:=Q_p^{(\mathrm{NEU\text{-}159/160)}}.
\]

### 3.4 Rang-eins-Projektion versus Symmetriedarstellung

Historisch wird $\pi_p$ sowohl als Rang-eins-Projektion als auch als unitäre Symmetriedarstellung verwendet. P05 trennt:

\[
\Pi_p^{(1)}:=|e_1^{(p)}\rangle\langle e_1^{(p)}|,
\qquad
\pi_p^{\rm sym}:G_p\to\mathcal U(\mathscr Q_p^{\rm quot}).
\]

### 3.5 Verbundene Liftform versus BC-Halbgewicht

Zur Vermeidung einer Verwechslung des historischen Lift-$h_p$ mit $h_p^{\rm bal}$ aus F4 verwendet P05

\[
\boxed{h_p^{\rm conn}}
\]

für die verbundene Liftform.

Alle fünf Änderungen sind ausschließlich redaktionelle Kanonisierungsschritte.

---

## 4. Kritische Statusfirewalls im SYN-Text

Der Primärcheck bestätigt, dass P05 insbesondere **nicht** behauptet:

- intrinsisches $c_p\neq0$ oder hebungsunabhängige Nichtentartung;
- Existenz eines exakt zulässigen Nichtnullzeugen;
- einen aus $[L_3]$ hergeleiteten geladenen Repräsentanten $L_3^\circ=e_1V_1$;
- konkrete Nichttrivialität/Irreduzibilität der F2-Quotientendarstellung;
- globale Operatorverlängerung oder Quotientendeszent von $T_p^{\rm pre}$;
- globale Eigenwertfreiheit von $D_{\rm rel}$ in zusammengesetzten Sektoren;
- strukturelle Primblockdiagonalität;
- allgemeines $h_n^{\rm bal}=n^{-1/2}I$ für alle $n$;
- vollständige operatorische Primzahlpotenzrealisierung;
- Primorthogonalität aus der Mangoldt-Trägertrennung;
- eine bereits konstruierte globale positive Gramkopplung oder einen Hilbert--Pólya-Operator.

Damit bleiben die entscheidenden F1--F4-Firewalls erhalten.

---

## 5. Statusmatrix des Primärchecks

| Aussage | P05-Status | Primärcheck |
|---|---|---|
| Typtrennung Roh-/induzierter/relativer Kanaloperator | `✓[K/M]` | bestätigt |
| Nullmodusobstruktion auf kontrolliertem modalen Bereich | `✓[M]` | bestätigt |
| Lift-Nichtentartung/Hebungsunabhängigkeit | `?[O]` | bestätigt |
| exakter Liftzeuge | `?[O]` | bestätigt |
| feste-$p$-Kollisionsstruktur | `✓[M]` | bestätigt |
| geladener $L_3^\circ$ aus der Klasse | `?[O]` | bestätigt |
| abstrakte Quotienten-/Kommutantensätze | `✓[M]` | bestätigt |
| konkrete Quotientenrealisierung | `?[O]` / `CONDITIONAL` | bestätigt |
| Transportnormalform im Primsektor | `✓[M]` | bestätigt |
| zusammengesetzte Spektralsektoren | `?[O]` | bestätigt |
| nichtorthogonale Primkanalbilder | `✓[M]` | bestätigt |
| primitiver Halbgewichtsfaktor | `✓[M]_{part}` | bestätigt |
| arithmetische Primzahlpotenzidentität | `✓[M]` | bestätigt |
| all-$n$-BC-Halbgewicht | `CONDITIONAL` / Beweis nicht gefunden | bestätigt |
| Kreuzprimkollision vs. Mangoldt-Träger | `✓[M]` | bestätigt |

---

## 6. Primärurteil

\[
\boxed{\text{P05 SYN PRIMARY CONTENT CHECK COMPLETE}}
\]

Für `SYN FINAL AUDITED` fehlt noch ein unabhängiger **pfadgebundener SYN-Inhaltsgegencheck** gegen:

1. `papers/P05_Relative_Prime_Channels_and_Arithmetic_Edge_Geometry.md`,
2. `PASS-A-PROTOKOLL.md` — Gruppe F,
3. F2-Primäraudit/Zweitcheck,
4. F3-Endstand,
5. F4-Primäraudit/Zweitcheck.

Der Gegencheck soll keine neuen NEU-Audits eröffnen, sondern ausschließlich nach ausgelassenen F-Endbefunden, Statushochstellungen, Typ-/Symbolkollisionen und falschen P06/P09/P11-Weiterleitungen suchen.
