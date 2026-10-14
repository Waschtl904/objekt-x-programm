"""Construct the finite inverse-renewal correction with directed Arb.

This constructs a candidate rational upper bound. The independent
standard-library auditor checks its whole 287-dimensional Schur block.
No new operator integration and no finite truncation of a high tail.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, hashlib, io, json, sys, time, zipfile
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path[:0]=[str(ROOT/'work/compute-deps'),str(ROOT/'work/new-responses84-2026-10-11')]
from flint import arb,arb_mat,fmpq,ctx
from safe_serial import serial
from audit import member

def af(s):
    v=F(s);return arb(fmpq(v.numerator,v.denominator))

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=1024)
    ap.add_argument('--suffix',default='')
    ap.add_argument('--schur-package',type=Path)
    ap.add_argument('--responses-dir',type=Path,default=ROOT/'work/new-responses84-2026-10-11')
    ap.add_argument('--output-dir',type=Path,default=HERE)
    args=ap.parse_args();ctx.prec=args.bits
    args.output_dir.mkdir(parents=True,exist_ok=True)
    source_bytes={}
    if args.schur_package:
        raw=args.schur_package.read_bytes()
        assert hashlib.sha256(raw).hexdigest()=='65085974657257bd447d93342c5001d29e797b2fa70d876d53d36b587b16c2ba'
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            binding=json.loads(member(z,'INPUT_BINDINGS.json'))['responses']
            rb=member(z,binding['filename'])
            assert hashlib.sha256(rb).hexdigest()==binding['sha256']
            with zipfile.ZipFile(io.BytesIO(rb)) as rz:
                for label in ['EVEN','ODD']:source_bytes[label]=member(rz,f'RESPONSES_{label}.json')
    for label in ['EVEN','ODD']:
        t=time.time()
        raw=source_bytes[label] if source_bytes else (args.responses_dir/f'RESPONSES_{label}.json').read_bytes()
        r=json.loads(raw)
        K=[[F(v) for v in row] for row in r['K12_new_rational']]
        rho=F(r['rho']);M=[[F(v) for v in row] for row in r['M_upper_rational']]
        E=[[((1-rho) if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0))-M[i][j]
             for j in range(203)] for i in range(203)]
        X=[[F(v) for v in row] for row in r['X84x203_rational']]
        Ea=arb_mat([[af(v) for v in row] for row in E])
        Xa=arb_mat([[af(v) for v in row] for row in X])
        print(label,'directed 203-dimensional solve',flush=True)
        P=Xa*Ea.inv()*Xa.transpose();P=(P+P.transpose())/2
        boxes=serial(P,60)
        mid=[[(F(v[0])+F(v[1]))/2 for v in row] for row in boxes]
        up=[row[:] for row in mid]
        for i in range(84):
            rad=sum((F(v[1])-F(v[0]))/2 for v in boxes[i])
            up[i][i]+=rad+F(1,10**40)
        rowcap=max(sum(abs(v) for v in row) for row in up)
        trace=sum(up[i][i] for i in range(84))
        record={'status':'CANDIDATE_FINITE_CORRECTION_AWAITING_INDEPENDENT_RATIONAL_BLOCK_CHECK',
          'parity':label.lower(),'bits':args.bits,'response_source_sha256':hashlib.sha256(raw).hexdigest(),
          'E_definition':'D203-M_upper_rational','E_rational':[[str(v) for v in row] for row in E],
          'X84x203_rational':r['X84x203_rational'],
          'P_definition':'X E^-1 X*','P_upper_rational':[[str(v) for v in row] for row in up],
          'candidate_P_upper_row_norm':str(rowcap),'candidate_P_upper_trace':str(trace),
          'strict_diagonal_padding':'1e-40','beta':r['beta'],
          'residual_cap':['1/250','71/10000'][label=='ODD'],
          'scalar_M_upper_relative_D':r['M_actual_normalized_upper_scalar'],
          'elapsed_seconds':time.time()-t}
        dest=args.output_dir/f'INVERSE_{label}{args.suffix}.json'
        dest.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
        print(label,'row norm upper',float(rowcap),'trace upper',float(trace),'seconds',time.time()-t,flush=True)

if __name__=='__main__':main()
