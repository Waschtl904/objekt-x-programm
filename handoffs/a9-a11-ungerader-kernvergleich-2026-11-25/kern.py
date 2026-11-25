"""Directed common A8 source, with an improved high floor and a shared low Schur matrix."""
import argparse
import json
import sys
from pathlib import Path
from fractions import Fraction
from bindungen import PAIRS, VARIATION, checked_pkg, git_blob

def run(root, tests, output, finite=None):
    from flint import arb, arb_mat, ctx
    pkg = checked_pkg(root)
    sys.path.insert(0, str(pkg))
    from common import Inputs, box, enc, mat, q, norm, trace, ratmat
    from assemble import Energy, load_pairs, quad
    from weights import sub
    ctx.prec = 1024
    inp = Inputs()
    pairs = load_pairs(pkg/"expected/PAIRS_odd.json.gz")
    frozen = json.loads(tests.read_bytes())
    assert git_blob(tests)==VARIATION
    assert frozen["pairs_sha256"] == pairs["_source_sha256"] == PAIRS
    e = Energy(inp, pairs)
    data = inp.json("common")["cases"][1]
    sources = inp.json("old_sources")["cases"][1]
    f, j = sources["old_certificate"], sources["galerkin"]
    vec = lambda row: arb_mat([[q(x)] for x in row])
    c,y,w = (vec(frozen[k]) for k in ("raw","test_y_rational","test_w_rational"))
    c /= quad(e.G,c).sqrt()
    yj = arb_mat([[y[i,0] if i<12 else w[i-12,0]] for i in range(96)])
    wh, wf, wj = e.wh*c,e.wf*y,e.wj*w
    delta, C, rho = e.w["delta"],e.w["C"],e.w["rho"]
    T = C.transpose()/(1-rho).sqrt()
    Hf,Hj,Hfj = mat(f["source_h_gram_model"]),mat(j["H84_model"])*q("1.82"),mat(j["complete_source_high_cross_model"])
    H96 = arb_mat([[Hf[i,k] if i<12 and k<12 else Hfj[i,k-12] if i<12 else Hfj[k,i-12] if k<12 else Hj[i-12,k-12] for k in range(96)] for i in range(96)])
    Hcross = sub(mat(pairs["high_cross_models"]),range(191,287),range(12))
    high = quad(mat(pairs["high_Gram"]),c) - 2*(yj.transpose()*Hcross*c)[0,0]+quad(H96,yj)
    low = T*(e.ell*c - mat(f["source_c_model"])*y - mat(j["old_low_c_model"])*w)
    t = wh-wf-wj
    Uerror = e.eResidual*e.bounds["U8_norm_upper"].sqrt()
    herror = (quad(mat(f["joint_high_source_error_gram"]),y).sqrt()+
              box(j["high_source_error_norm"])*norm(w)+e.w["gamma"].sqrt()*e.eResidual)
    cert = e.certificate(frozen["raw"],"10","outer")
    te = (cert["feature_error_norms"]["finite_U8"]+Uerror+
          quad(e.EF,y).sqrt()+e.eJ*norm(w))
    gamma=e.w["gamma"]
    # Norm of the map from physical sources to all raw low covector coordinates
    # is <= sqrt(gamma); bound the weighted low map by its Hilbert-Schmidt norm.
    le = norm(T)*(quad(e.ELF,y).sqrt()+e.eLJ*norm(w)+gamma.sqrt()*e.eResidual)
    def sqbounds(square,err):
        assert square>=0 and err>=0
        length=square.sqrt()
        return [max(arb(0),length.lower()-err.upper())**2,(length.upper()+err.upper())**2]
    hbounds=sqbounds(high,herror)
    tbounds=sqbounds((t.transpose()*t)[0,0],te)
    def endpoints(x):return [enc(x[0])[0],enc(x[1])[1]]
    def numeric(x): return [float(Fraction(v)) for v in x]
    old=[hbounds[i]/delta+tbounds[i] for i in range(2)]
    HB=arb_mat([[q(v)/q(data["HB_denominator"]) for v in row] for row in data["HB_integer_matrix"]])
    G=T*HB*T.transpose()
    I=arb_mat([[int(i==k) for k in range(191)] for i in range(191)])
    out=dict(high_norm_squared=endpoints(hbounds), old_high_energy=endpoints([s/delta for s in hbounds]),
             old_low_energy=endpoints(tbounds),old_energy=endpoints(old),errors={k: enc(v)[1] for k,v in dict(high=herror,complete_low=te,weighted_raw_low=le).items()})
    print("components",*[numeric(out[k]) for k in ("old_high_energy","old_low_energy","old_energy")], "errors",*[float(x) for x in (herror,te,le)],flush=True)
    for label,dd in (("inherited_high","1.84298"),):
        d=q(dd);alpha=delta/d;k=1/delta-1/d
        u=alpha*t+(1-alpha)*low
        P=I+k*G
        v=P.solve(u)
        n=(u.transpose()*v)[0,0]
        n12=sqbounds(n,alpha*te+(1-alpha)*le)
        energy=[hbounds[i]/d+n12[i] for i in range(2)]
        gain=[old[0]-energy[1],old[1]-energy[0]]
        out[label]=dict(delta=dd,energy=endpoints(energy),gain=endpoints(gain))
        print(label,"gain",numeric(endpoints(gain)),flush=True)
    # Physical low floor and bounded high block, with the actual common crossing B.
    # Enclose BB* separately, in normalized low coordinates.
    F8=arb_mat([[q(v)/q(data["F_denominator"]) for v in row] for row in data["F_integer_matrix"]])
    AL=F8+HB/delta
    eB=box(f["old_coupling_error_norm"]).upper()
    pad0=q(data["coupling_padding"])
    G0=arb_mat([[q(s[0]).union(q(s[1]))/q(10**100) for s in row] for row in sources["old_raw_coupling_gram"]])
    gg=T*G0*T.transpose()
    tt=T*T.transpose()
    tau=q("1e-16")
    ghi=(1+tau)*gg+(1+1/tau)*eB**2*tt
    glo=(1-tau)*gg-(1/tau-1)*eB**2*tt
    # For the lower preconditioned Schur floor, HB0 dominates G0,
    # since it is the row-padded upper bound at the older padding.
    loss=(1+1/tau)*eB**2*trace(tt)/delta
    assert tau < pad0 and loss < q(".01")
    al=T*AL*T.transpose()
    def eval_strong(d,upper):
        alpha=delta/d
        u=alpha*t+(1-alpha)*low
        K=al-(ghi if upper else glo)/d
        r=K.solve(u)
        v=(u.transpose()*r)[0,0]
        err=(alpha*te+(1-alpha)*le)/(1-loss).sqrt()
        i=int(upper)
        return hbounds[i]/d+sqbounds(v,err)[i]
    for label,dd in (("tight_low","1.8219"),("joint","1.84298")):
        d=q(dd)
        energy=[eval_strong(d,False),eval_strong(d,True)]
        gain=[old[0]-energy[1],old[1]-energy[0]]
        out[label]=dict(delta=dd,energy=endpoints(energy),gain=endpoints(gain))
        print(label,"gain",numeric(endpoints(gain)),flush=True)
    # Joint restriction to the 96 old shell coordinates. The middle system
    # only selects trials. Evaluate physical costs separately with signed errors.
    def cat(*mats):
        return arb_mat([[A[i,j] for A in mats for j in range(A.ncols())] for i in range(mats[0].nrows())])
    def mid(A):
        return arb_mat([[A[i,j].mid() for j in range(A.ncols())] for i in range(A.nrows())])
    def pack(A,B,D):
        n,m=A.nrows(),D.nrows()
        return arb_mat([[A[i,j] if i<n and j<n else B[i,j-n] if i<n else B[j,i-n] if j<n else D[i-n,j-n] for j in range(n+m)] for i in range(n+m)])
    Z0=cat(e.wf,e.wj,e.wh)
    rlow=T*cat(mat(f["source_c_model"]),mat(j["old_low_c_model"]),e.ell)
    Hfull=pack(H96,Hcross,mat(pairs["high_Gram"]))
    Dlo,Dup=mat(data["D96_lower_model"]),mat(data["D96_upper_model"])
    Dmid=(Dlo+Dup)/2
    bare=mat(pairs["bare_F_J_pairs"])
    d=q("1.84298")
    mixed=delta/d*Z0+(1-delta/d)*rlow
    Umodel=Hfull/d+mixed.transpose()*(al-gg/d).solve(mixed)
    ix,ex=range(96),range(96,108)
    old_restricted = Dmid-sub(Umodel,ix,ix)
    forces=bare-sub(Umodel,ix,ex)
    solutions = mid((old_restricted+old_restricted.transpose())/2).solve(mid(forces))
    E12=sub(Umodel,ex,ex)+forces.transpose()*solutions
    import mpmath as mp
    mp.mp.dps=55
    def mpb(A):
        return mp.matrix([[mp.mpf(str(A[i,j].mid().str(60,radius=False))) for j in range(A.ncols())] for i in range(A.nrows())])
    Kmodel=mp.matrix(inp.json("kp_model_odd")["K_P_model"])
    G12=mpb(e.G)
    L=mp.cholesky((G12+G12.T)/2)
    S=L**-1*(Kmodel-mpb(E12))*(L.T**-1)
    ev,dirs=mp.eigsy((S+S.T)/2)
    print("model normalized spectra:", [float(x) for x in ev], flush=True)
    print("original new candidate finite price",float(quad(E12,c)),flush=True)
    def freeze(x):
        fac=10**45
        z=Fraction(str(x.mid().fmpq()))*fac+Fraction(1,2)
        return str(Fraction(z.numerator//z.denominator,fac))
    rawmin=L.T**-1*dirs[:,0]
    scaled=[int(mp.nint(x*10**12)) for x in rawmin]
    cases={"s":frozen["raw"],"e":json.loads((pkg/"expected/CANDIDATE_odd.json").read_bytes())["raw_coefficients"],"min_model":scaled}
    trial_vectors={}
    for label,rawco in cases.items():
        cc=vec(rawco); cc/=quad(e.G,cc).sqrt()
        a0=solutions*cc
        ar=[freeze(a0[i,0]) for i in range(96)]
        aa=vec(ar);yy=sub(aa,range(12),[0]);ww=sub(aa,range(12,96),[0])
        xx=cat(aa.transpose()*(-1),cc.transpose()).transpose()
        sig=sqbounds(quad(Hfull,xx),quad(mat(f["joint_high_source_error_gram"]),yy).sqrt()+box(j["high_source_error_norm"])*norm(ww)+gamma.sqrt()*e.eResidual)
        et=e.certificate(rawco,"10","candidate")["feature_error_norms"]["finite_U8"]+Uerror+quad(e.EF,yy).sqrt()+e.eJ*norm(ww)
        el=norm(T)*(quad(e.ELF,yy).sqrt()+e.eLJ*norm(ww)+gamma.sqrt()*e.eResidual)
        vv=mixed*xx; ee=(delta/d*et+(1-delta/d)*el)/(1-loss).sqrt()
        vals=[]
        for ii,ggbound in enumerate((glo,ghi)):
            cv=(vv.transpose()*(al-ggbound/d).solve(vv))[0,0]
            vals.append(sig[ii]/d+sqbounds(cv,ee)[ii])
        bval=(aa.transpose()*bare*cc)[0,0]
        berror=(e.eBareF*norm(yy)+e.eBareJ*norm(ww))*quad(mat(pairs["H9_Gram"]),cc).sqrt() + (16*norm(yy)+q("1.000502").sqrt()*norm(ww))*e.eResidual
        vtest=[2*(bval.lower()-berror.upper())-quad(Dup,aa).upper()+vals[0],
               2*(bval.upper()+berror.upper())-quad(Dlo,aa).lower()+vals[1]]
        print(label, "trial price", numeric(endpoints(vtest)), "spectrum model budget",float((mpb(cc).T*Kmodel*mpb(cc))[0]),flush=True)
        out["trial_"+label]={"raw":rawco,"test":ar,"price":endpoints(vtest),"physical_core":endpoints(vals),"bare_error_upper":enc(berror)[1]}
        trial_vectors[label]=(cc,aa,et,el,quad(mat(f["joint_high_source_error_gram"]),yy).sqrt()+box(j["high_source_error_norm"])*norm(ww)+gamma.sqrt()*e.eResidual,berror)
    # Polarize the very same outer and inner tests. The two mixed bare errors
    # use the norm of the actual input rather than a model on the diagonal.
    k=512
    ep,sp=trial_vectors["e"],trial_vectors["s"]
    pol=[]
    for sign in (1,-1):
        cc=sp[0]+sign*k*ep[0]; aa=sp[1]+sign*k*ep[1]
        xx=cat(aa.transpose()*(-1),cc.transpose()).transpose()
        yy=sub(aa,range(12),[0]);ww=sub(aa,range(12,96),[0])
        sig=sqbounds(quad(Hfull,xx),sp[4]+k*ep[4])
        ee=(delta/d*(sp[2]+k*ep[2])+(1-delta/d)*(sp[3]+k*ep[3]))/(1-loss).sqrt()
        vv=mixed*xx
        bounds=[]
        for ii,ggbound in enumerate((glo,ghi)):
            cv=(vv.transpose()*(al-ggbound/d).solve(vv))[0,0]
            bounds.append(sig[ii]/d+sqbounds(cv,ee)[ii])
        barem=(aa.transpose()*bare*cc)[0,0]
        bareprice=(e.eBareF*norm(yy)+e.eBareJ*norm(ww))*quad(mat(pairs["H9_Gram"]),cc).sqrt()+(16*norm(yy)+q("1.000502").sqrt()*norm(ww))*e.eResidual*(1+k)
        pol.append([2*(barem.lower()-bareprice.upper())-quad(Dup,aa).upper()+bounds[0],
                    2*(barem.upper()+bareprice.upper())-quad(Dlo,aa).lower()+bounds[1]])
    cross=[(pol[0][0]-pol[1][1])/(4*k),(pol[0][1]-pol[1][0])/(4*k)]
    out["trial_mixed"]=dict(scale=k,price=endpoints(cross))
    print("mixed F",numeric(endpoints(cross)),flush=True)
    out["exploratory_spectrum"]=[float(x) for x in ev]
    if finite is not None:
        from restmerkmale import bound_features
        assert git_blob(finite)=="0cd7325cfed36fb357d6c44c0f2b7e14eeb491be"
        odd=json.loads(finite.read_bytes())
        out["residual_features"]=bound_features(e,sources,trial_vectors,pairs,delta,d,T,
                     al,glo,ghi,Umodel,Hfull,mixed,bare,Dmid,Dlo,Dup,loss,odd)
        for key in ("e","s"):
            row=out["residual_features"][key]
            print("physical finite residual",key,*[float(Fraction(row[k]["norm_upper"])) for k in ("F","J")],flush=True)
    output.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    for arg in ("root","tests","output"): parser.add_argument(arg,type=Path)
    parser.add_argument("--finite",type=Path)
    a=parser.parse_args();run(a.root.resolve(),a.tests,a.output,a.finite)
