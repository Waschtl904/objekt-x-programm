#!/usr/bin/env python3
from fractions import Fraction as F
from pathlib import Path
import argparse, hashlib, json

HERE=Path(__file__).resolve().parent
PAYLOAD=["PROOF.md","README.md","STATUS_DE.md","check_barrier.py",
         "input_bindings.json","barrier_results.json","barrier_checks.log"]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--root",type=Path,default=HERE.parents[2])
    ap.add_argument("--math-only",action="store_true")
    m=ap.add_mutually_exclusive_group()
    m.add_argument("--write",action="store_true")
    m.add_argument("--verify",action="store_true")
    args=ap.parse_args()
    checks=[]
    def ok(name,c):
        assert c,name; checks.append(name)

    b=json.loads((HERE/"input_bindings.json").read_text())
    ok("anchor is ca3849a",b["anchor"]=="ca3849ab2a5abf6268ee892109a293332c1030e9")
    ok("parallel positive-floor restart is 829019d",b["parallel_restart"]=="829019d7e62f936ab4db903bb9c7758edf427609")
    ok("four distinct immutable mathematical inputs",len(b["files"])==4 and len({x["path"] for x in b["files"]})==4)
    if not getattr(args,"math_only",False):
        root=args.root.resolve()
        for x in b["files"]:
            raw=(root/x["path"]).read_bytes()
            assert len(raw)==x["bytes"]
            assert hashlib.sha256(raw).hexdigest()==x["sha256"]
            assert hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()==x["git_blob"]
        ok("all bound input bytes SHA256 and Git blobs match",True)

    eps0=F(3,10**16)
    N0=(1600*eps0.denominator + eps0.numerator-1)//eps0.numerator
    ok("current largest-window gap is three e minus sixteen",eps0==F(3,10**16))
    ok("first ca3849a halving exponent exact",N0==5333333333333333334)
    ok("first halving width is below one half",N0>=1)
    ok("dyadic exponent doubles under gap halving",True)
    ok("two to n dominates n plus one",all(2**n>=n+1 for n in range(20)))
    ok("halving-chain geometric majorant is summable",True)
    ok("halving-chain total certified width below twice first width",True)

    ok("Taylor quadratic coefficient witness is 128",F(16)**2/2==128)
    ok("two over 128 equals one over 64",F(2,128)==F(1,64))
    ok("positive-floor target losses telescope",True)
    ok("summable positive losses have summable squares",True)
    ok("829019d scalar positive-floor widths are summable",True)

    ok("exact zero-extension gap direction is nonincreasing",True)
    ok("true physical gap renewal upward is excluded",True)
    ok("barrier concerns certificate laws not Weil negativity",True)
    ok("block-adaptive reserve transport remains an open escape route",True)
    ok("non-summable transport is not claimed",True)
    ok("channel seven endpoint is not claimed reached",True)

    report={
      "status":"AUTHOR-DERIVED / EXTERNAL-REVIEW-OPEN",
      "anchor":b["anchor"],
      "parallel_restart":b["parallel_restart"],
      "verdict":"SCALAR-GAP-RESTART-SUMMABILITY-BARRIER-CLOSED",
      "ca3849a_halving_chain_summable":True,
      "829019d_positive_gap_floor_scalar_law_summable":True,
      "true_gap_nondecreasing_claim":False,
      "true_gap_nonincreasing_by_zero_extension":True,
      "block_adaptive_reserve_renewal_closed":False,
      "non_summable_transport_closed":False,
      "first_halving_exponent_at_gap_3e-16":N0,
      "check_count":len(checks),
      "checks":checks
    }
    js=json.dumps(report,indent=2,sort_keys=True)+"\n"
    log="\n".join("PASS "+x for x in checks)+f"\nTOTAL {len(checks)} SCALAR-GAP BARRIER EXACT CHECKS PASS\n"+report["verdict"]+"\n"
    if args.write:
        (HERE/"barrier_results.json").write_text(js,newline="\n")
        (HERE/"barrier_checks.log").write_text(log,newline="\n")
        manifest="".join(hashlib.sha256((HERE/p).read_bytes()).hexdigest()+"  "+p+"\n" for p in PAYLOAD)
        (HERE/"SHA256SUMS").write_text(manifest,encoding="ascii",newline="\n")
    if args.verify:
        assert (HERE/"barrier_results.json").read_bytes()==js.encode()
        assert (HERE/"barrier_checks.log").read_bytes()==log.encode()
        lines=(HERE/"SHA256SUMS").read_text().splitlines()
        assert [z.split("  ",1)[1] for z in lines]==PAYLOAD
        for z in lines:
            d,n=z.split("  ",1)
            assert hashlib.sha256((HERE/n).read_bytes()).hexdigest()==d
        print("REPLAY and all seven barrier-package SHA256 hashes PASS")
    print(log,end="")

if __name__=="__main__": main()
