"""Sixteen extra signed panels of the UNCHANGED original model, for diagnosis."""
from pathlib import Path
import json,time,hashlib
TASK=Path(__file__).resolve().parent
BOOT=TASK.parent/'pairing-check/run_pairs.py'
g={'__file__':str(BOOT),'__name__':'extra_panels_bootstrap'}
exec(compile(BOOT.read_text(encoding='utf-8').split('# Coarse signed quadrature')[0],str(BOOT),'exec'),g)
arb,arb_mat,arb_poly,ns,c=(g[k]for k in ['arb','arb_mat','arb_poly','ns','c'])
import taylor_model as tm
outdir=TASK/'extra-panels';outdir.mkdir(exist_ok=True)
oldir=g['WHOLE']/'taylor-model-panels-205'
manifest=json.loads((g['ORIGINAL']/'MANIFEST.json').read_bytes())
indices=list(range(32,40))+list(range(238,246))
a,b=ns['a'],ns['b'];cuts=[]
for edge in ns['edges']:
 for sh,wt in ns['channels']:
  cuts.extend(xx for xx in [edge+sh,edge-sh,sh-edge,-edge-sh]if a<xx<b)
cuts.extend(xx for xx in ns['res'].cuts if a<xx<b);cuts.sort(key=float)
oe=[a]
for xx in cuts:
 if not xx.overlaps(oe[-1]):oe.append(xx)
oe.append(b);assert len(oe)==4
pan=[(a+(oe[1]-a)*arb(2)**(-k-1),a+(oe[1]-a)*arb(2)**(-k))for k in range(205)]
pan += [(oe[1],oe[2])]
pan += [(b-(b-oe[2])*arb(2)**(-k),b-(b-oe[2])*arb(2)**(-k-1))for k in range(205)]
for count,index in enumerate(indices):
 target=outdir/f'{index:04}.json'
 if target.exists():continue
 raw=(oldir/f'{index:04}.json').read_bytes()
 assert hashlib.sha256(raw).hexdigest()==manifest[f'whole/taylor-model-panels-205/{index:04}.json']
 old=json.loads(raw);lo,hi=pan[index];width=hi-lo;tick=time.monotonic()
 assert lo.overlaps(c.box(old['lo'])) and hi.overlaps(c.box(old['hi']))
 order=((old['order']+31)//32)*32
 rec=tm.build(ns,lo,hi,order);poly=rec['polynomial'];err=rec['taylor_error']
 control=abs(poly(0)-ns['outer_value']((lo+hi)/2)).upper();assert control<c.q('1e-15')
 weights=arb_mat([[arb(2)/(j+k+1)if (j+k)%2==0 else arb(0)for k in range(len(poly))]for j in range(96)])
 ip=weights*arb_mat([[v]for v in poly]);affine=arb_poly([((lo+hi)/2-ns['mid'])/ns['half'],width/(2*ns['half'])])
 local=[ns['leg'][j](affine)*(arb(2*j+1)/(2*ns['hs'])).sqrt()for j in range(96)]
 transform=arb_mat([[p[k]for k in range(96)]for p in local]);moments=(transform*ip)*width
 r=c.encode({'index':index,'order':rec['order'],'lo':lo,'hi':hi,'moments':moments,'taylor_error_X_squared':2*width*err**2,'midpoint_control':control,'seconds':time.monotonic()-tick})
 target.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print('EXTRA_PANEL',count+1,16,index,'seconds',round(r['seconds'],2),flush=True)
print('EXTRA_DONE',round(time.monotonic()-g['start'],2),flush=True)
