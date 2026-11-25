"""Arb/rational replay of the signed odd high-space estimates."""
import argparse
import hashlib
import json
from pathlib import Path
from math import factorial

from flint import arb, ctx
from hochraum_jets import Q, cardinal, log_bounds, output_log_jets
from reflexion import reflected_tail, value

HERE = Path(__file__).resolve().parent
PIN = "36d6fec7966a802ee6a2084a66a8224f48247093"


def check_geometry():
    c, a, b = 3*arb(2).log()/2, arb(3).log(), arb(11).log()/2
    h, g = b-a, a-c
    r = 2*a-b
    center, delta = (c*c+r*r)/2, (c*c-r*r)/2
    R = value(".9")
    assert center-R > value(".09") and delta/R < value(".05")
    assert (R+delta)/(c+value(".3")) < value(".94")
    assert 2*value(".94")/g+1 < 34
    assert 2*(value(".94")+g)/h+1 < 34
    assert center/R < value("1.2") and c < value("1.05")
    assert h/a < value(".1") and h/g < value("12/7") and h/(2*g+h)<value(".47")
    assert 3000*69**95/value(".3") < value("1e185")
    assert value("1.05e185")*value(".05")**192/(1-value(".05")) < value("1e-63")
    assert value("1.05e185")*192*value("1.2")**191 < value("1e210")
    assert (a+b)/2-value(".09")-c > value(".018")
    assert h/2/value(".09")<value(".57")
    assert 200*value(".57")**4096/(1-value(".57")) < value("1e-990")
    rho=value("1.3")
    assert c*(rho+1/rho)/2 < a-value(".02")
    assert 400*rho**(-384)/(1-1/rho)<value("1e-39")
    assert 300*value(".47")**4000*value("5e91")<value("1e-100")
    assert arb(5)/factorial(380) < value("1e-800")


def report(energy_path, raw_dir):
    ctx.prec = 8192
    check_geometry()
    energy_bytes = energy_path.read_bytes()
    assert hashlib.sha256(energy_bytes).hexdigest() == "320e6fbbc102979d4817a3047347e7db16151e3092bfe675b6a23b03326c4731"
    energy=json.loads(energy_bytes)
    compact=json.loads((HERE/"JETDATEN.json").read_bytes())
    assert max(compact["polynomial_degrees"]) == 320
    jets=cardinal(compact["log_rows"], compact["X"])
    if raw_dir:
        full=output_log_jets(raw_dir/"FUNCTIONS12.json",raw_dir/"FROZEN_RESPONSE12.json")
        assert full == jets
        functions=json.loads((raw_dir/"FUNCTIONS12.json").read_bytes())["parities"]["odd"]["functions"]
        assert [f["F"]["log_ratio_multiplier"] for f in functions] == compact["log_rows"]
        assert [len(f["F"]["polynomial"])-1 for f in functions] == compact["polynomial_degrees"]
        assert json.loads((raw_dir/"FROZEN_RESPONSE12.json").read_bytes())["parities"]["odd"]["X"] == compact["X"]
    old_log, constant_log, amplitude=log_bounds(jets)
    assert old_log < Q("2.968e-37") and constant_log < Q("2.461e-80") and amplitude < Q("5e91")
    scale=2*arb(2).log()*arb(5).log()/(arb(10).sqrt()*value("1.84298"))
    rows={}
    bounds=[]
    for key, norm, cutoff, signed, direct, residual, price in [
        ("e","1","1.766810e-6","6.77e-7","5.2456104e-8","6.67944674e-12","1.23e-10"),
        ("s","9999.871371863025338",".000297270",".000114",".000008816611755","5.3240166456875e-7","9.1e-6")]:
        trial=energy["trial_"+key]
        assert sum(Q(t)**2 for t in trial["test"])<Q("2.7e8")**2
        tail=reflected_tail(trial["raw"],norm,4096)
        assert tail < value(cutoff)
        assert scale*tail+value("1e-14")<value(signed)
        coupling=value(signed)+value(direct)+value("2.183e-26")+(value("8.833")*value(residual)).sqrt()
        high=coupling**2/value(".58")
        assert high<value(price)
        rows[key]=dict(reflected_tail_upper=cutoff,signed_norm_upper=signed,old_residual_energy_upper=residual,
                       direct_remainder_upper=direct,schur_price_upper=price)
        bounds.append(value(price))
    he, hs=bounds
    det=(value("9.7719170086e-8")-he)*(value(".0018569778671088")-hs)-(value(".00001223973278951")+(he*hs).sqrt())**2
    assert det>value("2.97146e-11")
    return dict(parent=PIN,scope="odd fixed two-space plus Y_o, under inherited form and source contracts",
                estimates=rows,corrected_determinant_lower="2.97146e-11",external_review="OPEN",
                full_quotient_certified=False,physical_U11_constructed=False,point4_closed=False)


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("energy",type=Path)
    parser.add_argument("--full-inputs",type=Path)
    args=parser.parse_args()
    print(json.dumps(report(args.energy,args.full_inputs),indent=2))
