"""Export exact 100-decimal-grid proposals; confirm both precision solves agree."""
from pathlib import Path
import json,argparse
from fractions import Fraction as F
import eight_source_refined as m

def construct(bits):
    m.ctx.prec=bits;inp=m.ORIGINAL/'inputs';old=m.read(inp/'a8_model.json.gz');sol=m.read(inp/'SOLUTIONS.json');fun=m.read(inp/'FUNCTIONS.json')
    pol=m.legendre(544);out=[]
    for p,label in enumerate(['even','odd']):
        cells=[(m.box(c['lo']),m.box(c['hi'])) for c in fun['blocks'][p]['positive_cells']]
        base,sh,_,_,_,_=m.make_sources(p,cells,pol);gm=[]
        for j in range(4):
            mm=m.polynomial_moments(m.coeff(base[j]),m.arb(0),m.arb(1),544)
            for (l,h),ss in zip(cells,sh):mm=[v+w for v,w in zip(mm,m.polynomial_moments(m.coeff(ss[j]),l,h,544))]
            gm.append([m.pair(pol[n],mm,n) for n in range(p,384,2)])
        mom=old['raw_low_moments']
        cn=[m.af(F(2*n+1,2*p+1)).sqrt()*m.box(mom[n],10**100)/m.box(mom[p],10**100) for n in range(p+2,384,2)]
        cc=[[m.mid_decimal(gm[j][i+1]-cn[i]*gm[j][0]) for j in range(4)] for i in range(191)]
        C=m.arb_mat(cc);A=m.arb_mat([[m.af(sum(map(F,old['parities'][label]['A'][i][j]))/(2*10**100)) for j in range(191)] for i in range(191)])
        raw=A.solve(C);P=[]
        for i in range(191):P.append([sol['blocks'][p]['proposal'][i][j] if j<2 else str(F(int((raw[i,j].mid()*10**100).floor().unique_fmpz()),10**100)) for j in range(4)])
        out.append({'parity':label,'degrees':list(range(p+2,p+10,2)),'proposal':P})
    return out
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--primary',type=Path,required=True);ap.add_argument('--higher',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();assert not a.out.exists()
    x=construct(3072);y=construct(4096);assert x==y
    for path in [a.primary,a.higher]:
        r=m.read(path)
        for rr,xx in zip(r['blocks'],x):
            for row,prow in zip(rr['proposal'],xx['proposal']):
                assert all(F(v[0])<=F(q)<=F(v[1]) for v,q in zip(row,prow))
    out={'status':'PASS_EXACT_RATIONAL_PROPOSALS','grid_digits':100,'bits':[3072,4096],
         'coefficients_identical':1528,'previous_four_proposals_preserved':True,'blocks':x}
    a.out.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(out['status'])
if __name__=='__main__':main()
