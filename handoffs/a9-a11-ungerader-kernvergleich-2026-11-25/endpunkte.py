"""Exact checks of the new core comparison and the two-direction residual budget."""
import argparse
import json
from fractions import Fraction as F
from pathlib import Path
from bindungen import git_blob

HERE=Path(__file__).resolve().parent
def read(path):
    return json.loads(path.read_bytes())

def check(data, previous_s, previous_e):
    assert git_blob(previous_s)=="07c844ec5d5d2406c72449362e6a1bb91da965ed"
    assert git_blob(previous_e)=="0cd7325cfed36fb357d6c44c0f2b7e14eeb491be"
    energy=read(data/"ENERGIE.json")
    ke=F(read(previous_e)["K_P"][0])
    ks=F(read(previous_s)["K_P_interval"][0])
    assert list(map(int,energy["trial_s"]["raw"]))==list(map(int,read(previous_s)["raw_coefficients"]))
    def interval(case,field):
        lo,hi=map(F,energy[case][field])
        assert lo<=hi
        return lo,hi
    gmin,gmax=interval("joint","gain")
    assert F("0.00558833")<gmin<=gmax<F("0.00563432")
    assert interval("inherited_high","gain")[1]<F(".000088")
    assert interval("tight_low","gain")[0]>F(".00558785")
    a=ke-interval("trial_e","price")[1]
    b=ks-interval("trial_s","price")[1]
    k0,k1=map(F,read(data/"MISCHBUDGET.json")["mixed"])
    f0,f1=interval("trial_mixed","price")
    c=max(abs(k0-f1),abs(k1-f0))
    assert a>F("9.77258e-8") and b>F(".00185751") and c<F(".000012238")
    assert a*b-c*c>F("3.17618e-11")
    re,rs=F("1e-9"),F("1e-4")
    # An upper rational square root for the mixed residual error.
    cross=F("3.17e-7")
    assert cross**2>=re*rs and a>re and b>rs
    assert (a-re)*(b-rs)-(c+cross)**2>F("1.23724e-11")
    lo,hi=map(F,read(data/"KANDIDAT.json")["K_P_interval"])
    flo,fhi=interval("trial_min_model","price")
    assert lo-fhi<0<hi-flo
    print("PASS: core gain, positive trial budget matrix, conditional residual gate.")
    print("Full residual energies required: e <= 1e-9 and s <= 1e-4.")
    print("The physical residuals and full two-source decision are checked in abschluss.py.")

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--data",type=Path,default=HERE)
    parser.add_argument("--previous-s",type=Path,required=True)
    parser.add_argument("--previous-e",type=Path,required=True)
    args=parser.parse_args()
    check(args.data,args.previous_s,args.previous_e)
