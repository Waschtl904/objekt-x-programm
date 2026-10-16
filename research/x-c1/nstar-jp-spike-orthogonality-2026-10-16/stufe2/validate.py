import time, json
import mpmath as mp
from qnp_psi import *
g = setup(25)
a8,b9=g['a8'],g['b9']
# T1: Indikator 1_(-A,A) als "psi": H_Gamma = int_{A-x}^oo k + int_{A+x}^oo k
class Ind:
    def __init__(s,A): s.A=A
    def __call__(s,y): return mp.mpf(1) if abs(y)<s.A else mp.mpf(0)
for A in [a8,b9]:
    ind=Ind(A)
    for x in [mp.mpf('0.1'),mp.mpf('0.7'),a8*mp.mpf('0.999')]:
        if x>=A: continue
        exact=mp.quad(k_gamma,[A-x,mp.inf])+mp.quad(k_gamma,[A+x,mp.inf])
        # generische Routine erwartet Sprungstellen bei a8,b9 -> fuer A=b9 passt; fuer A=a8 ebenso (b9-Breakpoints harmlos)
        got=h_gamma(ind,x,g)
        print('T1 A=%s x=%s  |diff|=%s'%(mp.nstr(A,6),mp.nstr(x,6),mp.nstr(abs(got-exact),3)))
# T2: Fourier-Multiplikator auf Gauss u=exp(-x^2/2): g(xi)=Re psi(1/4+i xi/2)-psi(1/4)
u=lambda x: mp.exp(-x**2/2)
def hg_direct(x):
    f=lambda r: k_gamma(r)*(2*u(x)-u(x+r)-u(x-r))
    return mp.quad(f,[0,1,5,mp.inf])
def hg_fourier(x):
    gm=lambda xi: mp.re(mp.digamma(mp.mpf(1)/4+1j*xi/2))-mp.digamma(mp.mpf(1)/4)
    # u_hat(xi)=sqrt(2pi) e^{-xi^2/2}; H u(x) = (1/2pi) int g(xi) u_hat(xi) e^{i x xi} dxi = (1/sqrt(2pi)) int g(xi) e^{-xi^2/2} cos(x xi) dxi
    return mp.quad(lambda xi: gm(xi)*mp.exp(-xi**2/2)*mp.cos(x*xi),[-mp.inf,0,mp.inf])/mp.sqrt(2*mp.pi)
for x in [mp.mpf(0),mp.mpf('0.5'),mp.mpf('1.3')]:
    d,fou=hg_direct(x),hg_fourier(x)
    print('T2 x=%s direct=%s fourier=%s diff=%s'%(mp.nstr(x,3),mp.nstr(d,15),mp.nstr(fou,15),mp.nstr(abs(d-fou),3)))
# T3: 1/2 int_{-1}^1 [P_n(x)-P_n(y)]/|x-y| dy = H_n P_n(x)
for n in [0,1,2,5,8]:
    x=mp.mpf('0.37')
    val=mp.quad(lambda y: (mp.legendre(n,x)-mp.legendre(n,y))/abs(x-y),[-1,x,1])/2
    Hn=sum(mp.mpf(1)/j for j in range(1,n+1))
    print('T3 n=%d  diff=%s'%(n,mp.nstr(abs(val-Hn*mp.legendre(n,x)),3)))
# T4: Sprung und Log-Randterm fuer psi_v (gerade)
psi=Psi(g,'even','upper_v')
j=psi.shell_val(a8)-psi.core(a8)
print('T4 even Sprung j_v = psi(a8+)-psi(a8-) =',mp.nstr(j,12))
t0=time.time()
for e in [mp.mpf('1e-2'),mp.mpf('1e-4'),mp.mpf('1e-6'),mp.mpf('1e-8')]:
    x=a8-e
    val=q_raw(psi,x,g)
    print('   x=a8-%s: Q psi = %s ;  Q psi - (j/2) log(a8-x) = %s'%(mp.nstr(e,2),mp.nstr(val,10),mp.nstr(val-(j/2)*mp.log(e),10)))
print('   Zeit pro Auswertung ~%.2fs'%((time.time()-t0)/4))
print('T4 innere Breakpoints:',[mp.nstr(b,8) for b in interior_breakpoints(g)])
