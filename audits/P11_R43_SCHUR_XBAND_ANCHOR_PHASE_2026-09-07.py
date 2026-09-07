#!/usr/bin/env python3
"""R43 finite anchor/complex-phase audit. Not an independent-review certificate.

Uses the exact #83 graph/source data through the adjacent hash-checked XBAND
script. Builds the graph by incidence matrices and transports by Cholesky solves.
Every scalar energy uses complex conjugation. Both anchors, both strips, and the
pair-endpoint symmetric splitting are tested. The latter is invariant under
endpoint exchange, not claimed canonical under all choices in the analytic model.
No canonical source, analytic Q, moving-window decay, Strong Terminal/C6 or RH.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy.linalg import cho_factor, cho_solve, eigh

HERE = Path(__file__).resolve().parent
BASE = HERE / "P11_R43_SCHUR_XBAND_COMM_2026-09-07.py"
EXPECTED_BASE_BLOB = "61e700872e0637dbc34145bf7039f0cac3f0b3f3"
ERRORS: dict[str, float] = {}


def check(label, a, b):
    """Scaled absolute/relative residual; protect zero targets without cancellation."""
    if label in ERRORS:
        raise ValueError(f"Repeated check label: {label}")
    a, b = np.asarray(a), np.asarray(b)
    error = float(np.linalg.norm(a-b) / max(1., np.linalg.norm(a), np.linalg.norm(b)))
    ERRORS[label] = error
    if not error < 5e-11:
        raise AssertionError((label, error))


def energy(x):
    return float(np.vdot(x, x).real)


def gram_energy(x, a):
    value = np.vdot(x, a @ x)
    if abs(value.imag) > 5e-11 * max(1., abs(value.real)) or value.real <= 0:
        raise ArithmeticError(f"Invalid Hermitian energy: {value}")
    return float(value.real)


def herm(a):
    return (a + a.conj().T) / 2


def root(a, exponent):
    d, u = eigh(herm(a))
    if d[0] <= 0:
        raise ArithmeticError("Expected SPD matrix")
    return herm((u * d**exponent) @ u.conj().T)


def graph(nodes, centers, weights):
    edges, ew = [], []
    for t, w in zip(centers, weights):
        for j, u in enumerate(nodes):
            if u-t >= nodes[0]:
                row = np.zeros(len(nodes)); row[j] = 1; row[j-t] = -1
                edges.append(row); ew.append(w)
    incidence = np.array(edges)
    return np.eye(len(nodes)) + incidence.T @ (np.array(ew)[:, None] * incidence)


def run():
    ERRORS.clear()
    data = BASE.read_bytes()
    actual = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    if actual != EXPECTED_BASE_BLOB:
        raise RuntimeError(f"Base blob mismatch: {actual}")
    spec = importlib.util.spec_from_file_location("xband_base", BASE)
    base = importlib.util.module_from_spec(spec); spec.loader.exec_module(base)
    p = base.load_parent("p83")
    bands = p.band_data(); weights = np.array([r[2] for r in bands])
    amps = np.array([r[3] for r in bands]); centers = p.CENTERS
    U, V = p.U, p.V
    nodes, big = np.arange(-U,U+1), np.arange(-V,V+1)
    n = len(nodes); ident = np.eye(n)
    embed = (big[:,None] == nodes[None,:]).astype(float)
    A, Av = graph(nodes,centers,weights), graph(big,centers,weights)
    check("independent_graph_U", A, p.build_resolvent_matrix(U,weights)[1])
    check("independent_graph_V", Av, p.build_resolvent_matrix(V,weights)[1])
    BU = herm(cho_solve(cho_factor(A,lower=True), ident))
    BT = herm(embed.T @ cho_solve(cho_factor(Av,lower=True),embed))
    bh, bi = root(BU,.5), root(BU,-.5)
    Q = herm(bh @ root(bi @ BT @ bi,.5) @ bh)
    check("Riccati", Q @ A @ Q, BT)
    ah, ai = root(A,.5), root(A,-.5)
    check("second_Q_construction", Q, ai @ root(ah @ BT @ ah,.5) @ ai)

    shifts = {h: base.shift(nodes,h) for h in (-7,-6,-5,-4,-2,2,4,5,6,7)}
    hub = -sum(a*(shifts[t//2]-shifts[-t//2]) for t,a in zip(centers,amps))
    rows, stars = [], []
    for z in big[np.abs(big)>U]:
        s = int(np.sign(z))
        active = [(i,int(z-s*t)+U) for i,t in enumerate(centers) if -U<=z-s*t<=U]
        W = sum(weights[i] for i,j in active)
        stars.append(active)
        for (i,j),(k,l) in combinations(active,2):
            rows.append((int(z),i,k,j,l,s*(centers[k]-centers[i]),np.sqrt(weights[i]*weights[k]/W)))
    incidence = np.zeros((len(rows),n))
    for k,(_,i,j,pos,target,h,rho) in enumerate(rows):
        incidence[k,target] = rho; incidence[k,pos] = -rho

    def direct_variance(x):
        value = 0.
        for active in stars:
            w = np.array([weights[i] for i,j in active]); values = np.array([x[j] for i,j in active])
            mu = np.dot(w,values)/sum(w)
            value += float(np.dot(w,abs(values-mu)**2))
        return value

    phase_factors = [1.,np.exp(1j*np.pi/4),1j,np.exp(.37j),np.exp(2.1j),2*np.exp(.73j)]
    rng = np.random.default_rng(20260907)
    real_results, subspaces, controls = [], [], []
    for name,B in (("BU",BU),("BT",BT),("Q",Q)):
        af,cf,ar,cr,anchor_rhs,omitted = [],[],[],[],[],[]
        for z,i,j,pos,target,h,rho in rows:
            T,Tm = shifts[h],shifts[-h]
            comm = T@B-B@T
            af.append(rho*(B@(T-ident))[pos]); cf.append(rho*comm[pos])
            ar.append(-rho*(B@(Tm-ident))[target]); cr.append(-rho*(Tm@B-B@Tm)[target])
            term = rho*(B@(T@Tm-ident))[pos]
            omitted.append(term)
            anchor_rhs.append(rho*(comm@(Tm-ident))[pos]+term)
        af,cf,ar,cr,anchor_rhs,omitted = map(np.array,(af,cf,ar,cr,anchor_rhs,omitted))
        R = incidence@B
        check(f"first_anchor_matrix_{name}",af+cf,R)
        check(f"second_anchor_matrix_{name}",ar+cr,R)
        check(f"anchor_change_full_matrix_{name}",af-ar,anchor_rhs)
        check(f"commutator_anchor_change_{name}",cf-cr,-(af-ar))
        assert np.linalg.norm(omitted)>1e-4  # Arbitrary boundary inputs need the defect term.
        a0,c0,g = (af+ar)/2,(cf+cr)/2,(af-ar)/2
        check(f"symmetric_matrix_{name}",a0+c0,R)
        controls.append([name,float(np.linalg.norm(omitted))])

        def quantities(v):
            x = B@v; G = gram_energy(x,A); out = []
            for a,c in ((af,cf),(ar,cr),(a0,c0)):
                aa,cc = a@v,c@v
                out.extend([energy(aa)/G,energy(cc)/G,2*float(np.vdot(aa,cc).real)/G,energy(aa+cc)/G])
            return np.array(out),G

        sources = []
        for X in (4,6,8):
            source = np.array([p.odd_bump(u,X) for u in nodes])
            v = hub@source
            check(f"parent_hub_{name}_{X}",v,np.array(list(p.raw_hub_values(X,amps).values())))
            q,G = quantities(v)
            real_results.append([X,name,*q.tolist(),energy(g@v)/G])
            sources.append((f"bump{X}",v))
            basis = np.array([[float(u==k)-float(u==-k) for k in range(1,X)] for u in nodes])
            vh = hub@basis
            check(f"anchor_defect_bulk_{name}_{X}",omitted@vh,np.zeros((len(rows),X-1)))
            coeff = rng.normal(size=X-1)+1j*rng.normal(size=X-1)
            sources.append((f"complex_odd{X}",vh@coeff))
            for anchor,a,c in (("first",af,cf),("second",ar,cr),("symmetric",a0,c0)):
                ra,rc,rd = a@vh,c@vh,R@vh
                ga,gc,gd = herm(ra.conj().T@ra),herm(rc.conj().T@rc),herm(rd.conj().T@rd)
                eps = float(np.sqrt(eigh(gc,ga,eigvals_only=True)[-1]))
                eratio = eigh(gd,ga,eigvals_only=True)
                assert np.isfinite(eps) and eps >= 0
                assert eratio[0] > 0
                subspaces.append([X,name,anchor,eps,float(eratio[0]),float(eratio[-1])])
        sources.append(("complex_arbitrary_old",rng.normal(size=n)+1j*rng.normal(size=n)))
        for label,v in sources:
            q,G = quantities(v)
            x = B@v
            check(f"complex_direct_ANOVA_{name}_{label}",q[3],direct_variance(x)/G)
            check(f"complex_anchor_total_{name}_{label}",q[[3,7,11]],np.full(3,q[3]))
            for k in (0,4,8):
                check(f"complex_square_{name}_{label}_{k}",q[k+3],sum(q[k:k+3]))
            g2=energy(g@v)/G
            check(f"anchor_average_A_{name}_{label}",(q[0]+q[4])/2,q[8]+g2)
            check(f"anchor_average_C_{name}_{label}",(q[1]+q[5])/2,q[9]+g2)
            check(f"anchor_average_I_{name}_{label}",(q[2]+q[6])/2,q[10]-2*g2)
            for j,phase in enumerate(phase_factors):
                qp,Gp = quantities(phase*v)
                check(f"phase_energy_{name}_{label}_{j}",Gp/G,abs(phase)**2)
                check(f"phase_all_terms_{name}_{label}_{j}",qp,q)
                xp = B@(phase*v)
                check(f"phase_direct_ANOVA_{name}_{label}_{j}",direct_variance(xp)/Gp,q[3])
                check(f"phase_global_L2_{name}_{label}_{j}",energy(xp)/Gp,energy(x)/G)
        # An omitted conjugate is detected by phase i on a nonzero real source.
        v = sources[0][1]; x=B@v; G=gram_energy(x,A)
        broken=float(((1j*x).T@A@(1j*x)).real/G)
        assert broken < -.99
        check(f"Hermitian_i_phase_{name}",gram_energy(1j*x,A)/G,1.)
        # Complex polarization, checked against direct sesquilinear pairing.
        v,w = sources[1][1],sources[3][1]
        for label,L in (("graph",root(A,.5)@B),("variance",R),("sym_main",a0),("sym_comm",c0)):
            x,y=L@v,L@w
            polar=(energy(x+y)-energy(x-y)-1j*(energy(x+1j*y)-energy(x-1j*y)))/4
            check(f"polarization_{name}_{label}",polar,np.vdot(x,y))

    return {"scope":"finite center graph only; self-check, not independent or interval certification",
            "base_script_blob":actual,
            "case_columns":["X","B","first_A2/G","first_C2/G","first_I/G","first_V/G",
                            "second_A2/G","second_C2/G","second_I/G","second_V/G",
                            "symmetric_A2/G","symmetric_C2/G","symmetric_I/G","symmetric_V/G","anchor_g2/G"],
            "cases":real_results,
            "subspace_columns":["X","B","anchor","epsilon_sup","min_V/A2","max_V/A2"],
            "subspaces_numerical_only":subspaces,
            "omitted_compression_defect_Frobenius":controls,
            "source_count_per_transport":7,"phase_factor_count":len(phase_factors),
            "unique_checks":len(ERRORS),"max_error":max(ERRORS.values()),
            "worst_check":max(ERRORS,key=ERRORS.get),"status":"PASS_PROXY_NOT_THEOREM"}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args(); result=run()
    text=json.dumps(result,indent=2,allow_nan=False)+"\n"
    if args.output:
        args.output.write_text(text,encoding="utf-8")
        print(f"PASS: {result['unique_checks']} anchor/phase checks, max error={result['max_error']:.3e}")
        print(*result["case_columns"],sep=" ")
        for row in result["cases"]:
            print(row[0],row[1],*(f"{x:.12g}" for x in row[2:]))
    else:
        print(text,end="")


if __name__=="__main__":
    main()
