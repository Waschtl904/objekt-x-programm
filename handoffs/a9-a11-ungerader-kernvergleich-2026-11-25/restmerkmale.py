"""Bound both finite observations of the physical residual after exact core elimination."""
from flint import arb, arb_mat
from common import box, enc, mat, norm, q, ratmat, trace
from assemble import quad
from weights import sub

def bound_features(e, sources, tests, pairs, delta, d, T,
                   al, glo, ghi, Umodel, Hfull, mixed, bare, Dmid, Dlo, Dup, loss,
                   odd):
    """Return weighted prices on F12 and J84 for the two fixed physical residuals."""
    F,J=range(12),range(12,96)
    ix,ext=range(96),range(96,108)
    Dwidth=(Dup-Dlo)/2
    model_force=bare-sub(Umodel,ix,ext)
    model_form=Dmid-sub(Umodel,ix,ix)
    fm,jm=sources["old_certificate"],sources["galerkin"]
    alpha=delta/d
    Nspan=(al-ghi/d).inv()-(al-glo/d).inv()
    Ki=ratmat(odd["K_rational"]).inv()
    P=e.w["P"]
    def scalar_upper(value):
        assert value.is_finite()
        return enc(value)[1]
    fhigh=mat(fm["joint_high_source_error_gram"])
    jhigh=box(jm["high_source_error_norm"])
    results={}
    for label in ("s","e"):
        cc,aa,et,el,eh,_=tests[label]
        xx=arb_mat([[-aa[i,0]] if i<96 else [cc[i-96,0]] for i in range(108)])
        hmod=quad(Hfull,xx).sqrt()
        ux=mixed*xx
        lxerr=alpha*et+(1-alpha)*el
        physical_f=quad(mat(pairs["H9_Gram"]),cc).sqrt()
        model_r=model_force*cc-model_form*aa
        out={}
        for key,ids,M in (("F",F,Ki),("J",J,P)):
            row=sub(mixed,range(191),ids)
            trM=trace(M).sqrt()
            hierr=trace(M*fhigh).sqrt() if key=="F" else trM*jhigh
            loerr=trace(M*e.EF).sqrt() if key=="F" else trM*e.eJ
            rawerr=trace(M*e.ELF).sqrt() if key=="F" else trM*e.eLJ
            scaled_low=alpha*loerr+(1-alpha)*norm(T)*rawerr
            herm=trace(M*sub(Hfull,ids,ids)).sqrt()
            high=(hierr*(hmod+eh)+herm*eh)/d
            # The actual normalized Schur inverse is <= I. The two numerical
            # envelopes are also positive and bounded by I/(1-loss).
            low=(scaled_low*(norm(ux)+lxerr)+trace(M*row.transpose()*row).sqrt()*lxerr)/(1-loss)
            # The midpoint Gram G0 lies between glo and ghi. The difference
            # of either inverse to the model is bracketed by +/- Nspan.
            inv=trace(M*row.transpose()*Nspan*row).sqrt()*quad(Nspan,ux).sqrt()
            direct=trace(M*sub(Dwidth,ids,ids)).sqrt()*quad(Dwidth,aa).sqrt()
            if key=="F":
                bare_err=(e.eBareF*physical_f+16*e.eResidual)*trM
            else:
                bare_err=(e.eBareJ*physical_f+q("1.000502").sqrt()*e.eResidual)*trM
            squared=quad(M,sub(model_r,ids,[0])).upper()
            assert squared>=0
            nominal=squared.sqrt()
            parts=dict(model=nominal,high_error=high,low_error=low,
                       inverse_error=inv,direct_error=direct,bare_error=bare_err)
            assert all(v>=0 and v.is_finite() for v in parts.values())
            out[key]={k:scalar_upper(v) for k,v in parts.items()}
            out[key]["norm_upper"]=scalar_upper(sum(parts.values(),arb(0)))
        results[label]=out
    results["P_operator_upper"]=scalar_upper(max(sum(abs(P[i,j]).upper() for j in range(84)) for i in range(84)))
    return results
