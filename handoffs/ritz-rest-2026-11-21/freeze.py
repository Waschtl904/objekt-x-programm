"""Freeze one rational model Ritz representative from the November 19 stored data."""
from decimal import Decimal as D, localcontext, ROUND_HALF_EVEN
from fractions import Fraction as F
from pathlib import Path
import gzip,hashlib,json,sys

def get(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw.startswith(b'\x1f\x8b') else raw)

def decimal(x):
    return D(x.numerator)/D(x.denominator)

def mid(entry):
    mantissa, exponent, _, _ = entry["ball"]
    return F(mantissa)*F(2)**exponent

def run(cfg):
    b,first,second,vec=map(get,(cfg["bank"],cfg["first"],cfg["second"],cfg["vec"]))
    matrix=b["M_model_integer"]
    den=int(b["denominator"])
    w=[F(row[0]) for row in first["shell96"]+first["outer12_B_coordinates_z"]]
    lam=F(second["lambda_bar2"]["rational"])
    col=dict(json.loads(vec["payload"])["mapping"])["second"]["matrix"]
    n=len(col)
    w_rhs=[sum(x*y for x,y in zip(row[:n],w))/den for row in matrix[:n]]
    target=[mid(v[0])-lam*s for v,s in zip(col,w_rhs)]
    prec=120
    with localcontext() as ctx:
        ctx.prec=prec
        system=[[D(v)/den for v in row[:n]]+[decimal(target[i])] for i,row in enumerate(matrix[:n])]
        for j in range(n):
            pivot=system[j]
            if pivot[j]<=0: raise ValueError("bad model pivot")
            for i in range(j+1,n):
                row=system[i]
                factor=row[j]/pivot[j]
                for k in range(j+1,n+1):
                    row[k]-=factor*pivot[k]
        x=[D(0)]*n
        for i in reversed(range(n)):
            x[i]=(system[i][n]-sum(system[i][k]*x[k] for k in range(i+1,n)))/system[i][i]
        scale=10**30
        coeff=[int((v*scale).to_integral_value(rounding=ROUND_HALF_EVEN)) for v in x]
    z=[F(k,scale) for k in coeff]
    zz=[sum(at*bt for at,bt in zip(row[:n],z))/den for row in matrix[:n]]
    defect=max(abs(v-t) for v,t in zip(zz,target))
    print('max coef, model pairing, form, solve component defect',max(map(lambda t:float(abs(t)),z)),float(sum(v*t for v,t in zip(z,target))),float(sum(v*t for v,t in zip(z,zz))),float(defect))
    return {"basis":"F[12], J[84], outer in B coordinates[12]","denominator":str(scale),"numerators":[str(i) for i in coeff],"a":"1"}

if __name__=="__main__":
    config=json.loads(Path(sys.argv[1]).read_text(encoding="utf8"))
    result=run(config)
    Path(sys.argv[2]).write_text(json.dumps(result,indent=2)+"\n",encoding="utf8")
