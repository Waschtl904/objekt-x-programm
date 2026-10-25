"""Independent exact endpoint recombination; no numerical-library dependency."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,zipfile
H=Path(__file__).resolve().parent
d=json.loads((H/'DIRECTED-DIAGNOSTIC.json').read_bytes());f=d['F']
def need(ok,msg):
    if not ok:raise RuntimeError(msg)
def pair(v):
    a,b=map(Q,v);need(a<=b,'Reversed interval');return a,b
B=pair(f['base_interval']);P=pair(f['pair_interval']);HH=pair(f['H_interval'])
F=pair(f['F_interval']);K=pair(d['K']['K_P_interval'])
need(F==(B[0]+2*P[0]-HH[1],B[1]+2*P[1]-HH[0]),'F recombination')
gap=F[0]-K[1]
need(gap==Q(d['F_lower_minus_K_upper']),'Gap recombination')
need(gap>Q('1.0476e-6'),'Strict diagnostic separation')
need(pair(d['K_minus_F_interval'])==(K[0]-F[1],K[1]-F[0]),'Gap interval')
# Conservative displayed bounds are checked against exact rational endpoints.
Kdisplay=(Q('0.0327864990425293'),Q('0.0327864990425388'))
Fdisplay=(Q('0.0327875467274905'),Q('0.0327881384890562'))
need(Kdisplay[0]<=K[0] and K[1]<=Kdisplay[1],'K display')
need(Fdisplay[0]<=F[0] and F[1]<=Fdisplay[1],'F display')
src=json.loads((H/'DIAGNOSTIC-DIRECTION.json').read_bytes())
need(hashlib.sha256((H/'DIAGNOSTIC-DIRECTION.json').read_bytes()).hexdigest()==d['diagnostic_direction_sha256'],'Frozen direction binding')
archive=H.parent/'inherited/Objekt-X-Zweiraum-Ganzrest-und-Matrixvergleich-2026-10-24.zip'
with zipfile.ZipFile(archive)as z:directions=json.loads(z.read('two-direction-2026-10-24/DIRECTIONS.json'))
v=list(map(Q,directions['v1_rational']));q=list(map(Q,src['raw_coefficients']))
remaining=[q[j]-q[1]*v[j]/v[1]for j in range(2,12)]
need(any(x!=0 for x in remaining),'New direction must be outside old two-space')
prices={k:pair(x)[1]for k,x in f['pair_prices'].items()}
need(all(x>=0 for x in prices.values()),'Nonnegative error prices')
halfwidth=lambda x:(x[1]-x[0])/2
parts={'base_interval_radius':halfwidth(B),'twice_pairing_interval_radius':2*halfwidth(P),'H_interval_radius':halfwidth(HH)}
need(sum(parts.values(),Q(0))==halfwidth(F),'Total F radius')
out={'status':'PASS_EXACT_ENDPOINT_RECOMBINATION','scope':'Internal rational arithmetic and binding audit, not independent analytic review or a second numerical quadrature.',
     'F_lower_minus_K_upper':str(gap),'strict_display_floor':'1.0476e-6',
     'K_display_outward':list(map(str,Kdisplay)),'F_display_outward':list(map(str,Fdisplay)),
     'direction_outside_old_two_space':True,'raw_kernel_remainder':list(map(str,remaining)),
     'F_error_radius_decomposition':{k:str(v)for k,v in parts.items()},
     'pair_error_components_descending':[(k,str(v))for k,v in sorted(prices.items(),key=lambda kv:kv[1],reverse=True)],
     'negative_control_sign_reversal_rejected':not(-gap>Q('1.0476e-6')),
     'negative_control_missing_double_pair_radius_rejected':sum(parts.values(),Q(0))-halfwidth(P)!=halfwidth(F),
     'inputs_sha256':{n:hashlib.sha256((H/n).read_bytes()).hexdigest()for n in ['DIRECTED-DIAGNOSTIC.json','DIAGNOSTIC-DIRECTION.json']}}
(H/'ENDPOINT-AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':out['status'],'strict_gap':float(gap),'outside_old_two_space':True,'error_radii':{k:float(v)for k,v in parts.items()}},indent=2))
