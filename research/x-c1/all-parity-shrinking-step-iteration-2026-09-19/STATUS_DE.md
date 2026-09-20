# All-Parity-Restart und schrumpfende Iteration

**AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN**, 19. September 2026.

Der lokale All-Parity-Satz aus `a659047` ist nicht nur ein einmaliger
Shellschritt. Auf dem festen lokalen Band

`B=log(5)/2 <= a <= B+10^-2`

werden neue gerade und ungerade Momentprofile mit endpoint-uniformen
Konstanten konstruiert. Solange ein Endpunkt einen vollständigen
All-Parity-Gap `epsilon>0` besitzt, kann für jedes `0<gamma<epsilon` eine
explizit kleine rechte Shellbreite gewählt werden, auf der der neue Endpunkt
mindestens den Gap `gamma` behält.

Für den aktuellen Startpunkt `b0=B+10^-20` mit Gap `3e-15` wird die explizite
unendliche Kette

`N_n=4*10^16*2^n`, `h_n=2^(-N_n)`, `b_(n+1)=b_n+h_n`

zertifiziert. Die garantierten Gaps sind

`epsilon_n=10^-15*(1+2^(1-n))`,

also an jedem endlichen Schritt strikt größer als `10^-15`. Die Summe aller
neuen Schrittweiten ist kleiner als `10^-20`, daher bleibt die ganze Kette
im selben uniformen Prime-/Profilregime.

Damit ist **shrinking-step restartability / iteration** autorenseitig
geschlossen. Nicht geschlossen ist ein uniformer positiver Schritt
`h_n>=h_*>0`, ein nicht-summierbarer Transport zu einem vorgegebenen größeren
Fenster oder der Übergang über `log(7)/2`.

Dies ist kein Strong-Terminal-Satz, keine Connected Unit-Window Coercivity,
keine full C1-GEOM und keine Aussage zu Objekt X oder RH.
