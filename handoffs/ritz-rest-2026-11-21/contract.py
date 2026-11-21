"""Evaluate the full 109-bank contract for one rational vector; all bounds use rational arithmetic."""
from fractions import Fraction as F
from math import isqrt,lcm
from pathlib import Path
import gzip,json,hashlib,sys
def get(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)
def up_root(q):
    if q<0: raise ValueError("negative squared error")
    scale=10**60
    k=isqrt((q.numerator*scale**2)//q.denominator)
    return F(k + (k*k*q.denominator < q.numerator*scale**2), scale)
def common(v):
    den=lcm(*(t.denominator for t in v))
    return [t.numerator*(den//t.denominator) for t in v],den
def bilinear_int(M,md,x,y):
    X,xd=common(x);Y,yd=common(y)
    return F(sum(xi*sum(t*j for t,j in zip(row,Y)) for xi,row in zip(X,M) if xi),md*xd*yd)
def enclose(q,places=36):
    s=10**places
    return [str(F((q*s).__floor__(),s)),str(F((q*s).__ceil__(),s))]
def main(cfg, witness):
    b,first,second,vec,di,fix=map(get,[cfg[k] for k in ('bank','first','second','vec','direct','projection')])
    scale=int(witness["denominator"])
    z=[F(int(k),scale) for k in witness["numerators"]]+[F(0)]
    assert len(z)==109
    w=[F(row[0]) for row in first['shell96']+first['outer12_B_coordinates_z']]+[F(0)]
    l1,l2=[F(v['rational']) for v in fix['lambda_bar']]
    assert l2==F(second['lambda_bar2']['rational'])
    e=[-l1*x for x in w];e[-1]=F(1)
    den=int(b['denominator']); mat=b['M_model_integer']; err=b['E_upper_integer']
    old=[F(x) for x in di["old_row_majorant"]]
    radii=[[F(v) for v in row] for row in di['radii']]
    assert all(len(row)==109 for row in radii)
    radii=[[max(radii[i][j],radii[j][i]) for j in range(109)] for i in range(109)]
    def restnorm(x):
        return bilinear_int(err,den,x,x)-sum(t*a*a for t,a in zip(old,x))
    def direct(x,y):
        return sum(abs(xi)*sum(r*abs(yj) for r,yj in zip(row,y) if yj) for xi,row in zip(x,radii) if xi)
    n0=bilinear_int(mat,den,z,z); ne=restnorm(z)+direct(z,z); 
    p10=bilinear_int(mat,den,z,e)
    p1e=up_root(restnorm(z)*restnorm(e))+direct(z,e)
    cells=dict(json.loads(vec['payload'])['mapping'])['second']['matrix']
    mid=[F(v[0]['ball'][0])*F(2)**v[0]['ball'][1] for v in cells]
    p20=sum(t*k for t,k in zip(mid,z))-l2*bilinear_int(mat,den,z,w)
    values={"norm_model":n0,"norm_radius":ne,"norm_lower":n0-ne,"norm_upper":n0+ne,
            "raw_109_norm_radius":bilinear_int(err,den,z,z),
            "p1_model":p10,"p1_radius":p1e,"p1_lower":p10-p1e,"p1_upper":p10+p1e,
            "p2_model":p20,"p2_squared_over_nominal_norm":p20*p20/n0,
            "p1p2_over_nominal_norm":p10*p20/n0,
            "p2_positive_limit_using_norm_lower":up_root(F('0.089')*(n0-ne)) if n0>ne else F(0)}
    y = [zi + l2*wi for zi, wi in zip(z, w)]
    finite_bank_error = up_root(restnorm(z)*restnorm(y)) + direct(z, y)
    p2_shift_error = abs(l2)*(up_root(restnorm(z)*restnorm(w)) + direct(z, w))
    u, c = F("0.0000035227"), F("0.00020740")
    d_cap = F("0.0109")
    p1_lower = p10 - p1e
    cross_lower = p1_lower - up_root(u*d_cap)
    delta_limit = (F("0.1") - n0 - ne - d_cap)/2
    delta_model = p20-n0
    signed_cap = F("0.00014")
    scalar_headroom = delta_limit - delta_model - finite_bank_error
    n_lower = n0-ne
    assert n_lower > 0 and cross_lower > -c and c + p1_lower > 0
    values.update({
        "ell_z_model": delta_model,
        "ell_z_bank_error_other_than_t2": finite_bank_error,
        "p2_bank_error_other_than_t2": p2_shift_error,
        "abs_normalized_first_upper": up_root(max(abs(p10-p1e),abs(p10+p1e))**2/n_lower),
        "conditional_D_cap": d_cap, "conditional_Q_cap": d_cap*F(21,25),
        "conditional_R12_lower": cross_lower,
        "conditional_D_cross_limit": (c+p1_lower)**2/u,
        "conditional_ell_z_upper_allowed": delta_limit,
        "conditional_p2_upper_allowed": (F("0.1") + n_lower - d_cap)/2,
        "unknown_signed_t2_error_allowed": scalar_headroom,
        "R22_upper_if_signed_error_at_most_00014_and_D_paid":
            n0+ne+2*(delta_model+finite_bank_error+signed_cap)+d_cap,
    })
    for key,val in values.items():print(key,float(val))
    return {k:enclose(v) for k,v in values.items()}
if __name__=="__main__":
    cfg=get(sys.argv[1]);z=get(sys.argv[2])
    Path(sys.argv[3]).write_text(json.dumps(main(cfg,z),indent=2)+"\n",encoding='utf8')
