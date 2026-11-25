"""Lower bound for the full inverse cost, evaluated on an admissible old test."""
import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

from budget import COEFFICIENTS, PACKAGE, PAIR_SHA256, check_package, git_blob

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("finite", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if git_blob(args.finite) != "0cd7325cfed36fb357d6c44c0f2b7e14eeb491be":
        raise ValueError("Published odd K input mismatch")
    finite = json.loads(args.finite.read_bytes())
    pkg = args.root.resolve() / PACKAGE
    check_package(pkg)
    sys.path.insert(0, str(pkg))
    from flint import arb, arb_mat, ctx, fmpq, fmpq_mat
    from common import Inputs, box, enc, mat, q, ratmat, trace
    from weights import sub
    from assemble import Energy, load_pairs, quad

    ctx.prec = 1024
    inputs = Inputs()
    pairs = load_pairs(pkg / "expected/PAIRS_odd.json.gz")
    assert pairs["_source_sha256"] == finite["pairing_file_sha256"] == PAIR_SHA256
    assert pairs["parity"] == "odd"
    inv = fmpq_mat([[fmpq(x) for x in row] for row in finite["K_rational"]]).inv()
    inverse_rows = [[str(inv[i,j]) for j in range(12)] for i in range(12)]

    class View:
        def __init__(self, output_gram=None):
            self.gram = output_gram

        def json(self, key):
            data = inputs.json(key)
            if key == "coherent":
                data["parities"]["odd"].update(
                    K_rational=finite["K_rational"], K_inverse_rational=inverse_rows)
            if key == "inverse_odd" and self.gram is not None:
                data["P_upper_rational"] = self.gram
            return data

    seed = Energy(View(), pairs)
    assert "odd" == seed.par
    case = inputs.json("common")["cases"][1]
    raw = inputs.json("old_sources")["cases"][1]
    F, J = range(12), range(12,96)
    U, DL, DU = [mat(case[k]) for k in ("U96_model","D96_lower_model","D96_upper_model")]
    Gf = ratmat([row[:12] for row in case["G96_rational"][:12]])
    Uff, Ujj = sub(U,F,F), sub(U,J,J)
    DD = (DU-DL)/2
    eps = q("1e-10")
    direct = sub((DL+DU)/2,J,J)
    B = direct-Ujj
    Kinv, amap = seed.w["Ki"], seed.w["a"]
    H = B - amap.transpose()*Kinv*amap - eps*direct
    coeff = [str(x) for x in COEFFICIENTS]
    c = arb_mat([[q(x)] for x in coeff])
    c = c / quad(seed.G,c).sqrt()
    def mid(A):
        return arb_mat([[A[i,j].mid() for j in range(A.ncols())] for i in range(A.nrows())])
    chosen = mid((H+H.transpose())/2).solve(mid(seed.nu*c))
    grid = 10**40
    def freeze(x):
        scaled = Fraction(str(x.mid().fmpq()))*grid + Fraction(1,2)
        return Fraction(scaled.numerator//scaled.denominator,grid)
    weights = [freeze(chosen[i,0]) for i in range(84)]
    w = arb_mat([[q(x)] for x in weights])
    # ww* gives the physical error of this one pairing in the inherited
    # feature estimates. It is never used as an inverse majorant.
    evaluator = Energy(View([[str(x*y) for y in weights] for x in weights]), pairs)
    cert = evaluator.certificate(coeff,"10","odd_variational_test")
    model = cert["component_model_energies"]
    errors = cert["feature_error_norms"]
    b0 = sum((model[k] for k in ("high_U8","finite_U8","K_inverse_v")),arb(0))
    b_err = (errors["finite_U8"]**2+errors["K_inverse_v"]**2).sqrt()
    b_err += evaluator.eResidual*(evaluator.bounds["U8_norm_upper"]+
                          evaluator.bounds["v_feature_operator_norm_upper"]**2).sqrt()
    core_lower = max(arb(0),b0.lower().sqrt()-b_err.upper())**2
    pair = (w.transpose()*evaluator.nu*c)[0,0]
    pair_error = (errors["P_upper_J_star_nu"]+
                  cert["residual_model_error_norm"])/q("1.1").sqrt()
    pair_lower = pair.lower()-pair_error.upper()

    EF = 2*(mat(case["finite_feature_error_gram"])+
            mat(raw["old_certificate"]["joint_high_source_error_gram"])/seed.w["delta"])
    EJ = 2*(box(case["tail_feature_error_scalar"])+
            box(raw["galerkin"]["high_source_error_norm"])**2/seed.w["delta"])
    v = Kinv*amap*w
    dw, uw, ew = quad(sub(DD,J,J),w),quad(Ujj,w),EJ*(w.transpose()*w)[0,0]
    df, uf, ef = quad(sub(DD,F,F),v),quad(Uff,v),quad(EF,v)
    assert all(x>=0 for x in (dw,uw,ew,df,uf,ef))
    bprice = dw + 2*(uw*ew).sqrt()+ew
    cross = 2*((df*dw).sqrt()+(uf*ew).sqrt()+(ef*uw).sqrt()+(ef*ew).sqrt())
    square_lower = max(arb(0),quad(Kinv,amap*w).lower()-cross.upper())
    eta_lower = eps*quad(sub(DL,J,J),w)
    F_lower = core_lower+2*pair_lower-quad(B,w).upper()-bprice.upper()+square_lower+eta_lower.lower()
    result = {"raw":COEFFICIENTS,"test_w_rational":[str(x) for x in weights],
              "pairs_sha256":pairs["_source_sha256"],"bits":ctx.prec,
              "base_lower":enc(core_lower)[0],"pair_lower":enc(pair_lower)[0],
              "base_error_upper":enc(b_err)[1],"pair_error_upper":enc(pair_error)[1],
              "B_model_upper":enc(quad(B,w))[1],"B_price_upper":enc(bprice)[1],
              "square_lower":enc(square_lower)[0],"square_cross_error_upper":enc(cross)[1],
              "eta_direct_lower":enc(eta_lower)[0],"F_lower":enc(F_lower)[0]}
    parameter = q(finite["epsilon"])
    v_error = errors["K_inverse_v"] + evaluator.bounds["v_feature_operator_norm_upper"]*evaluator.eResidual
    # Strongest physical F block with the frozen U8. The lower Young inequality
    # for the Gram gives an upper matrix for B_FF = D_FF - Psi_F*Psi_F.
    Ef_common = mat(case["finite_feature_error_gram"])
    assert 0 < parameter < 1
    shell_gap = (sub(DU,F,F) - (1-parameter)*Uff +
                 (1/parameter-1)*Ef_common - ratmat(finite["K_rational"]))
    t0 = Kinv*(seed.v*c-amap*w)
    finite_test = [freeze(t0[i,0]) for i in range(12)]
    y = arb_mat([[q(x)] for x in finite_test])
    rounding_sq = quad(ratmat(finite["K_rational"]), y-t0).upper()
    y_price = quad(shell_gap,y).upper()
    # Dual K norm of (a_actual - amap)w, from the joint direct and U sandwich.
    gw = quad(seed.w["GJ"],w)
    da_w = (seed.bounds["direct_energy_relative_error_upper"]*(trace(Kinv*Gf)*gw).sqrt()
            + (trace(Kinv*Uff)*ew).sqrt() + (trace(Kinv*EF)*uw).sqrt()
            + (trace(Kinv*EF)*ew).sqrt())
    assert rounding_sq>=0 and y_price >=0
    b_error = (v_error+da_w+rounding_sq.sqrt()).upper()
    restore_eta = eps*quad(sub(DU,J,J),w)
    result.update(test_y_rational=[str(x) for x in finite_test],
                  physical_F_directional_price=enc(y_price)[1],
                  physical_grouped_force_error=enc(b_error)[1],
                  restore_eta_upper=enc(restore_eta)[1])
    print("restored shell lower",float((F_lower-b_error**2-y_price-restore_eta.upper()).lower()),flush=True)
    args.output.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print("variational lower",float(Fraction(result["F_lower"])),flush=True)
    print("base, pairing, direct, square errors",*[float(x) for x in (b_err,pair_error,bprice,cross)],flush=True)

if __name__ == "__main__":
    run()
