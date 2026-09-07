#!/usr/bin/env python3
"""R43 XBAND: fresh reproduction, not the unavailable fe907714 patch.

Finite center-graph proxy ONLY; no canonical source, analytic Q, decay, C6 or RH.
Read provenance: PR83 4abccc2dd29d87f914440478c286dbc6edf11169 (blob
237bf3406debcc3d2ec757ce547d3759c55a1fc2), PR84
3e4e5a73679db9f88624869587c4bd3bc3fec266 (blob
bb0ccb9e788bb0949ab1ea01b80ad6f6ce5fef4d). Their definitions are reimplemented
here, not imported; existing files/registries are unchanged. Requires NumPy/SciPy.
All inner products conjugate the first argument. Run without Python -O.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import platform
from itertools import combinations
from math import exp, log, sqrt
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import cholesky, eigh, norm, solve, solve_sylvester

U, V = 30, 40
CENTERS = (10, 12, 14)
RADII = (4, 6, 8)
DELTAS = (.15, .10, .075, .05, .03, .02, .01, .005)
TOL = 5e-11
CHECKS: dict[str, float] = {}


def check(name, lhs, rhs=0.0):
    """Frobenius/vector residual, scaled by max(1, ||lhs||, ||rhs||)."""
    a, b = np.asarray(lhs), np.asarray(rhs)
    err = float(np.linalg.norm(a-b) / max(1., np.linalg.norm(a), np.linalg.norm(b)))
    CHECKS[name] = max(err, CHECKS.get(name, 0.))
    if not np.isfinite(err) or err >= TOL:
        raise AssertionError(f'{name}: scaled residual {err}')


def bands():
    m = int(exp(14.15)) + 16
    mark = bytearray(b'\x01') * (m+1)
    mark[:2] = b'\x00\x00'
    for p in range(2, int(sqrt(m))+1):
        if mark[p]:
            mark[p*p:m+1:p] = b'\x00' * (((m-p*p)//p)+1)
    primes = [p for p in range(2, m+1) if mark[p]]
    out, rows = [], []
    for t in CENTERS:
        ps = [p for p in primes if t-.15 <= log(p) <= t+.15]
        ww = [log(p)*(p-1)*p**-1.5 for p in ps]
        aa = [sqrt(log(p))*p**-.75 for p in ps]
        out.append([t, len(ps), sum(ww), sum(aa)])
        rows.append((np.log(np.array(ps, dtype=float)), np.array(ww), np.array(aa)))
    check('graph mass anchors', [r[2] for r in out],
          [44.59817706246725,120.89687763600345,329.1851915820806])
    check('hub mass anchors', [r[3] for r in out],
          [1.1572520185069353,1.7361325665411198,2.6546513413534485])
    return out, rows


def graph(T, weights):
    A = np.eye(2*T+1)
    for h, w in zip(CENTERS, weights):
        for a in range(h, 2*T+1):
            b = a-h
            A[a,a] += w
            A[b,b] += w
            A[a,b] -= w
            A[b,a] -= w
    return A


def shift(h, T=U):
    """(T_h x)(u)=x(u-h), zero extension; no periodic wrap."""
    out = np.zeros((2*T+1,2*T+1))
    for j, u in enumerate(range(-T,T+1)):
        if -T <= u-h <= T:
            out[j,u-h+T] = 1.
    return out


def power(A, p):
    check('power input Hermitian', A, A.conj().T)
    d, Z = eigh((A+A.conj().T)/2)
    if min(d) <= 0:
        raise AssertionError('non-SPD matrix in fractional power')
    return (Z*d**p) @ Z.conj().T


def geometric_mean(B, C):
    r, ri = power(B,.5), power(B,-.5)
    return r @ power(ri@C@ri,.5) @ r


def bump(t, X):
    a = np.asarray(t, dtype=float)
    out = np.zeros_like(a)
    mask = np.abs(a) < X
    out[mask] = a[mask]*np.exp(-1/(1-(a[mask]/X)**2))
    return out


def raw_hub(X, amps):
    u = np.arange(-U,U+1)
    return -sum(a*(bump(u-t/2,X)-bump(u+t/2,X))
                for t,a in zip(CENTERS,amps))


def geometry(weights, outer=V):
    """Separate strip sides, pairs and active TOTAL denominators."""
    rows, stars = [], []
    for z in list(range(-outer,-U))+list(range(U+1,outer+1)):
        s = 1 if z > 0 else -1
        active = [i for i,t in enumerate(CENTERS) if abs(z-s*t) <= U]
        W = sum(weights[i] for i in active)
        stars.append((z,s,active,W))
        for i,j in combinations(active,2):
            rows.append((z,i,j,z-s*CENTERS[i]+U,z-s*CENTERS[j]+U,
                         s*(CENTERS[j]-CENTERS[i]),weights[i]*weights[j]/W))
    return rows, stars


def direct_anova(x, weights, stars):
    total = 0.
    for z,s,active,W in stars:
        if not W:
            continue
        xs = np.array([x[z-s*CENTERS[i]+U] for i in active])
        ww = np.array([weights[i] for i in active])
        mu = np.sum(ww*xs)/W
        total += float(np.sum(ww*np.abs(xs-mu)**2))
    return total


def energy(x, A):
    val = np.vdot(x, A@x)
    check('energy real', val.imag)
    if val.real <= 0:
        raise AssertionError('nonpositive energy')
    return float(val.real)


def components(B, v, AU, rows, anchor):
    """All outputs have canonical sign d=x(u_i)-x(u_j)."""
    x = B@v
    G = energy(x,AU)
    cache = {}
    for h in {r[5] for r in rows} | {-r[5] for r in rows}:
        T = shift(h)
        a, c = B@((T-np.eye(len(v)))@v), (T@B-B@T)@v
        check('global Delta decomposition', (T-np.eye(len(v)))@x, a+c)
        cache[h] = (a,c)
    aa, cc, dd = [], [], []
    for z,i,j,ui,uj,h,k in rows:
        # tau_h-I at u_i is x(u_j)-x(u_i), hence the minus sign.
        q, hh, sign = (ui,h,-1) if anchor == 'lower' else (uj,-h,1)
        a,c = cache[hh]
        aa.append(sqrt(k/G)*sign*a[q])
        cc.append(sqrt(k/G)*sign*c[q])
        dd.append(sqrt(k/G)*(x[ui]-x[uj]))
    aa,cc,dd = map(np.asarray,(aa,cc,dd))
    check('sampled Delta decomposition',aa+cc,dd)
    return aa,cc,dd,G


def quadratic(a,c,d):
    out = np.array([np.vdot(a,a).real,np.vdot(c,c).real,
                    2*np.vdot(a,c).real,np.vdot(d,d).real],dtype=float)
    check('quadratic identity',out[0]+out[1]+out[2],out[3])
    return out


def resolved(X, delta, prime_rows, weights, amps, matrices, AU):
    """Independent vectorized replay of PR84 hybrid sampler, also with Q."""
    u = np.arange(-U,U+1)[:,None]
    v = np.zeros(2*U+1)
    micro = []
    for t,(lp,wp,ap),W,Amp in zip(CENTERS,prime_rows,weights,amps):
        mask = np.abs(lp-t) <= delta
        lp,wp,ap = lp[mask],wp[mask],ap[mask]
        wp,ap = wp*(W/sum(wp)),ap*(Amp/sum(ap))
        check('resolved mass',[sum(wp),sum(ap)],[W,Amp])
        v -= np.sum(ap*(bump(u-lp/2,X)-bump(u+lp/2,X)),axis=1)
        micro.append((lp,wp))
    check('resolved even hub',v,v[::-1])
    results = {}
    for name,B in matrices.items():
        x = B@v
        G = energy(x,AU)
        acc = np.zeros(3)
        for z in list(range(-V,-U))+list(range(U+1,V+1)):
            s = 1 if z > 0 else -1
            grouped = []
            for lp,wp in micro:
                q = z-s*lp
                mask = np.abs(q) <= U
                ww = wp[mask]
                if len(ww):
                    xx = np.interp(q[mask],np.arange(-U,U+1),x)
                    Wj = sum(ww)
                    mj = sum(ww*xx)/Wj
                    grouped.append((Wj,mj,float(sum(ww*np.abs(xx-mj)**2)),ww,xx))
            W = sum(g[0] for g in grouped)
            if W == 0:
                continue
            mu = sum(g[0]*g[1] for g in grouped)/W
            intra = sum(g[2] for g in grouped)
            inter = sum(g[0]*abs(g[1]-mu)**2 for g in grouped)
            total = sum(float(sum(g[3]*np.abs(g[4]-mu)**2)) for g in grouped)
            pair = sum(g[0]*h[0]/W*abs(g[1]-h[1])**2
                       for g,h in combinations(grouped,2))
            check('resolved ANOVA',total/G,(intra+inter)/G)
            check('resolved pair geometry',pair/G,inter/G)
            acc += np.array([intra,inter,total])/G
        results[name] = acc.tolist()
    return results


def main():
    if not __debug__:
        raise RuntimeError('run without -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('xband_recheck_results.json'))
    args = parser.parse_args()
    band_info, prime_rows = bands()
    weights,amps = [r[2] for r in band_info],[r[3] for r in band_info]
    AU,AV = graph(U,weights),graph(V,weights)
    I = np.eye(2*U+1)
    BU = solve(AU,I,assume_a='pos')
    BV = solve(AV,np.eye(2*V+1),assume_a='pos')
    old = np.arange(V-U,V+U+1)
    new = np.setdiff1d(np.arange(2*V+1),old)
    BT = BV[np.ix_(old,old)]
    Q = geometric_mean(BU,BT)
    check('Q reversed endpoints',Q,geometric_mean(BT,BU))
    L = cholesky(BU,lower=True)
    Li = solve(L,I)
    check('Q Cholesky route',Q,L@power(Li@BT@Li.T,.5)@L.T)
    check('Q Hermitian',Q,Q.T)
    check('Q Riccati',Q@AU@Q,BT)
    matrices = dict(BU=BU,BT=BT,Q=Q)
    specs = {}
    for name,B in dict(AU=AU,AV=AV,**matrices).items():
        d = eigh((B+B.T)/2,eigvals_only=True)
        if min(d)<=0:
            raise AssertionError('SPD failed')
        specs[name] = dict(min=float(d[0]),max=float(d[-1]),condition=float(d[-1]/d[0]))
    AoN,ANN = AV[np.ix_(old,new)],AV[np.ix_(new,new)]
    effective = AV[np.ix_(old,old)]-AoN@solve(ANN,AoN.T,assume_a='pos')
    K = effective-AU
    check('Schur inverse',effective@BT,I)
    if min(eigh((K+K.T)/2,eigvals_only=True)) < -TOL:
        raise AssertionError('Schur correction not PSD')
    degree = np.diag(2*sum(weights)-(np.diag(AU)-1))
    collar = np.flatnonzero(np.diag(degree)>1e-10)
    outside = np.setdiff1d(np.arange(len(I)),collar)
    check('Schur correction boundary rows',K[outside,:])
    check('Schur correction boundary columns',K[:,outside])
    Linf = AU-I+degree
    rootA = power(AU,.5)
    H = rootA@Q@rootA
    evH = eigh(H,eigvals_only=True)
    Lam = float(max(eigh(power(AU,-.5)@effective@power(AU,-.5),eigvals_only=True)))
    check('relative Schur stability',evH[0],1/sqrt(Lam))
    rows,stars = geometry(weights)
    rng = np.random.default_rng(430907)
    zcomplex = rng.normal(size=len(I))+1j*rng.normal(size=len(I))
    for outer in (40,44):
        rtest,stest = geometry(weights,outer)
        pair = sum(r[6]*abs(zcomplex[r[3]]-zcomplex[r[4]])**2 for r in rtest)
        direct = direct_anova(zcomplex,weights,stest)
        check('complex pair vs ANOVA',pair,direct)
        wrong = sum(weights[r[1]]*weights[r[2]]/(weights[r[1]]+weights[r[2]])
                    *abs(zcomplex[r[3]]-zcomplex[r[4]])**2 for r in rtest)
        if abs(wrong-direct)<1e-3:
            raise AssertionError('pairwise-denominator negative control failed')
    # Exact compression identities checked against a larger, safely padded space.
    E = np.zeros((201,len(I))); E[100-U:101+U,:] = I
    for h,k in ((2,4),(-2,2),(2,-2),(4,-2)):
        defect = shift(h)@shift(k)-shift(h+k)
        rhs = -E.T@shift(h,100)@(np.eye(201)-E@E.T)@shift(k,100)@E
        check('compression padded identity',defect,rhs)
    check('same-direction semigroup',shift(2)@shift(4),shift(6))
    defect = shift(-2)@shift(2)-I
    tail = np.zeros(len(I)); tail[-2:] = 1
    check('opposite-direction exact loss',defect,-np.diag(tail))
    controls = {}
    edge = np.zeros(len(I)); edge[-1]=1
    smooth = bump(np.arange(-U,U+1)-29,3)
    for name,v in dict(edge_impulse=edge,smooth_edge=smooth,bulk_hub=raw_hub(8,amps)).items():
        controls[name] = float(norm(defect@v)/norm(v))
    check('edge impulse full loss',controls['edge_impulse'],1.)
    check('bulk hub no loss',controls['bulk_hub'])
    if controls['smooth_edge']<=0:
        raise AssertionError('smooth boundary control failed')
    commutators = []
    for h in (-14,-12,-10,-4,-2,2,4,10,12,14):
        T = shift(h)
        F = AU@T-T@AU
        free = Linf@T-T@Linf
        deg = degree@T-T@degree
        check('boundary split',F,free-deg)
        interior = np.flatnonzero(np.abs(np.arange(-U,U+1))<=U-14-abs(h))
        for f in (F,free,deg):
            check('boundary localization rows',f[interior,:])
            check('boundary localization columns',f[:,interior])
        for name,B in matrices.items():
            D = T@B-B@T
            if name!='Q':
                A = AU if name=='BU' else effective
                check('endpoint inverse commutator',D,B@(A@T-T@A)@B)
            else:
                R = T@BT-BT@T-Q@(T@AU-AU@T)@Q
                check('Q Sylvester equation',Q@AU@D+D@AU@Q,R)
                Z = solve_sylvester(H,H,rootA@R@rootA)
                check('Q Sylvester reconstruction',Z,rootA@D@rootA)
                bound = norm(rootA@R@rootA,'fro')/(2*evH[0])
                if norm(Z,'fro')>bound+TOL:
                    raise AssertionError('weighted Sylvester bound failed')
            commutators.append(dict(transport=name,h=h,norm2=float(norm(D,2)),
                                    role='target' if abs(h) in (2,4) else 'large-shift control'))
    wrong_inverse = norm(shift(2)@BT-BT@shift(2)-BT@(AU@shift(2)-shift(2)@AU)@BT)
    if wrong_inverse<1e-6:
        raise AssertionError('wrong compressed inverse control failed')
    summaries,details = [],[]
    for X in RADII:
        v = raw_hub(X,amps)
        check('raw even parity',v,v[::-1])
        for name,B in matrices.items():
            data = {}
            for anchor in ('lower','upper'):
                a,c,d,G = components(B,v,AU,rows,anchor)
                q = quadratic(a,c,d)
                check('center pair vs ANOVA',q[3],direct_anova(B@v,weights,stars)/G)
                data[anchor] = a,c,d,G
                summaries.append(dict(X=X,transport=name,anchor=anchor,G=G,
                                      A2=q[0],C2=q[1],interference=q[2],variance=q[3]))
                for side in (-1,1):
                    for i,j in combinations(range(3),2):
                        mask=np.array([(r[0]*side>0 and r[1]==i and r[2]==j) for r in rows])
                        terms=quadratic(a[mask],c[mask],d[mask])
                        details.append(dict(X=X,transport=name,anchor=anchor,side=side,
                                            pair=f'{CENTERS[i]}:{CENTERS[j]}',h=CENTERS[j]-CENTERS[i],
                                            A2=terms[0],C2=terms[1],interference=terms[2],variance=terms[3]))
                for phase in (1j,np.exp(.37j),np.exp(1.9j)):
                    ap,cp,dp,Gp=components(B,phase*v,AU,rows,anchor)
                    check('global phase energy',Gp,G)
                    check('global phase terms',quadratic(ap,cp,dp),q)
            al,cl,d,G=data['lower']; ar,cr,dr,_=data['upper']
            check('anchors same oriented difference',d,dr)
            a,c,e=(al+ar)/2,(cl+cr)/2,(al-ar)/2
            check('anchor discrepancy cancellation',e,-(cl-cr)/2)
            qs=quadratic(a,c,d)
            E2=float(np.vdot(e,e).real)
            ql,qr=quadratic(al,cl,d),quadratic(ar,cr,d)
            check('symmetric source identity',(ql[0]+qr[0])/2,qs[0]+E2)
            check('symmetric commutator identity',(ql[1]+qr[1])/2,qs[1]+E2)
            check('symmetric interference identity',(ql[2]+qr[2])/2,qs[2]-2*E2)
            rho=sqrt(qs[1]/qs[0]); lower=max(0,sqrt(qs[0])-sqrt(qs[1]))**2
            if lower>qs[3]+TOL:
                raise AssertionError('reverse-triangle bound failed')
            summaries.append(dict(X=X,transport=name,anchor='symmetric',G=G,
                                  A2=qs[0],C2=qs[1],interference=qs[2],variance=qs[3],
                                  anchor_defect=E2,rho=rho,lower_bound=lower))
    for B in matrices.values():
        for anchor in ('lower','upper'):
            a,c,d,_=components(B,zcomplex,AU,rows,anchor)
            quadratic(a,c,d)
    # Every Schur sample is itself in the finite-range boundary collar.
    observed=sorted({r[3] for r in rows}|{r[4] for r in rows})
    if not set(observed).issubset(set(collar)):
        raise AssertionError('preimage collar claim failed')
    check('PR83 BU X8 anchor',[s['variance'] for s in summaries if s['X']==8 and s['transport']=='BU' and s['anchor']=='lower'][0],.07774575130993219)
    check('PR83 BT X8 anchor',[s['variance'] for s in summaries if s['X']==8 and s['transport']=='BT' and s['anchor']=='lower'][0],.04037469561856026)
    # Reproduce the whole PR84 sweep, without importing its real-only energy.
    sweep=[]
    for X in RADII:
        for delta in DELTAS:
            sweep.append(dict(X=X,delta=delta,results=resolved(X,delta,prime_rows,weights,amps,matrices,AU)))
    for X in RADII:
        for name in matrices:
            sub=[r for r in sweep if r['X']==X]
            intr=[r['results'][name][0] for r in sub]
            inter=[r['results'][name][1] for r in sub]
            slope=float(np.polyfit(np.log(DELTAS),np.log(intr),1)[0])
            if not (1.95<slope<2.05 and max(inter)/min(inter)<1.05 and intr[-1]<1e-4*inter[-1]):
                raise AssertionError('PR84 replay scaling failed')
    for delta,bu,bt in ((.15,[.00038831543026571983,.07612965713965107],
                        [.00020747116328667683,.03964722090973499]),
                       (.005,[4.227493739527122e-7,.07760182009854069],
                        [2.2547431633110823e-7,.040236080523582685])):
        rec=next(r for r in sweep if r['X']==8 and r['delta']==delta)
        check('PR84 BU anchors',rec['results']['BU'][:2],bu)
        check('PR84 BT anchors',rec['results']['BT'][:2],bt)
    # Exhaust the finite odd-source subspaces, not just the three smooth bumps.
    # Generalized eigenvalues are numerical, not directed-rounding certificates.
    Hfull=-sum(a*(shift(t//2)-shift(-t//2)) for t,a in zip(CENTERS,amps))
    subspaces=[]
    for X in RADII:
        F=np.zeros((len(I),X-1))
        for k in range(1,X):
            F[U+k,k-1]=1.; F[U-k,k-1]=-1.
        VV=Hfull@F
        for name,B in matrices.items():
            aa,cc,dd=[],[],[]
            for v in VV.T:
                al,cl,d,G=components(B,v,AU,rows,'lower')
                ar,cr,_,_=components(B,v,AU,rows,'upper')
                aa.append((al+ar)/2*sqrt(G))
                cc.append((cl+cr)/2*sqrt(G))
                dd.append(d*sqrt(G))
            As,Cs,Ds=np.array(aa).T,np.array(cc).T,np.array(dd).T
            GS,GC,GD=As.T@As,Cs.T@Cs,Ds.T@Ds
            GI=As.T@Cs+Cs.T@As
            GG=VV.T@B@AU@B@VV
            check('source Gram identity',GD,GS+GC+GI)
            if min(eigh(GS,eigvals_only=True))<=0:
                raise AssertionError('singular symmetric source Gram')
            eps=sqrt(float(max(eigh(GC,GS,eigvals_only=True))))
            ei,vi=eigh(GI,GS)
            ev=eigh(GD,GS,eigvals_only=True)
            eg=eigh(GD,GG,eigvals_only=True)
            subspaces.append(dict(X=X,transport=name,dimension=X-1,
                                  epsilon_sup=eps,source_Gram_condition=float(np.linalg.cond(GS)),
                                  interference_over_A2=[float(ei[0]),float(ei[-1])],
                                  variance_over_A2=[float(ev[0]),float(ev[-1])],
                                  variance_over_G=[float(eg[0]),float(eg[-1])],
                                  negative_interference_source_coefficients=vi[:,0].tolist(),
                                  positive_interference_source_coefficients=vi[:,-1].tolist()))
            for j in (0,-1):
                f=vi[:,j]
                check('subspace interference witness',float(f@GI@f),float(ei[j]))
                a,c,d,_=components(B,VV@f,AU,rows,'lower')
                quadratic(a,c,d)
    result=dict(scope='fresh finite proxy reproduction; no independent external review',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                bands=band_info,spectra=specs,compression=controls,
                stability=dict(H_min=float(evH[0]),H_max=float(evH[-1]),relative_Schur_Lambda=Lam,
                               weighted_inverse=1/(2*float(evH[0])),naive_Frobenius_bound=specs['AU']['condition']/(2*float(evH[0]))),
                geometry=dict(observed_nodes=[int(i-U) for i in observed],
                              boundary_nodes=[int(i-U) for i in collar],
                              wrong_compressed_inverse_residual=float(wrong_inverse)),
                commutators=commutators,summaries=summaries,pair_side_details=details,
                symmetric_source_subspaces=subspaces,
                prime_resolved_replay=sweep,checks=CHECKS,max_scaled_residual=max(CHECKS.values()))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    csvpath=args.output.with_suffix('.csv')
    with csvpath.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(details[0]));writer.writeheader();writer.writerows(details)
    print('PASS: finite proxy only; max scaled residual',result['max_scaled_residual'])
    for s in summaries:
        print(f"X={s['X']} {s['transport']:2} {s['anchor']:9} A2/G={s['A2']:.12g} C2/G={s['C2']:.12g} I/G={s['interference']:.12g} V/G={s['variance']:.12g}")
    print('Full output:',args.output,'; pair/side CSV:',csvpath)


if __name__=='__main__':
    main()
