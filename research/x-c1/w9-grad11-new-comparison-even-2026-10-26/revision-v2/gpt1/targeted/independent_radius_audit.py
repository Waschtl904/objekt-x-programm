"""GPT1 exact audit of the corrected Gram-radius transport, without Arb."""
import sys, json, hashlib
from pathlib import Path
from fractions import Fraction as Q

if sys.flags.optimize or not __debug__:
    raise SystemExit('OPTIMIZED_PYTHON_REJECTED')
P=Path(__file__).resolve().parent
H=P/'merged/workspace/work/breakthrough-2026-10-25'
R=H/'revision_v2'
def need(value,message):
    if not value:raise RuntimeError(message)
def read(p):return json.loads(p.read_bytes())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def matrix(m):return [[Q(x) for x in row]for row in m]
def transpose(m):return list(map(list,zip(*m)))

data=read(R/'EXACT_GRAM_RADIUS_AUDIT_V2.json')
ledger=read(R/'SOURCE_BLOCK_LEDGER_V2.json')
old=read(H/'SOURCE_BLOCK_LEDGER_RESERVE.json')
need(data['source_ledger_sha256']==sha(R/'SOURCE_BLOCK_LEDGER_V2.json'),'Ledger binding')
need(old['young_parameters']==ledger['young_parameters'],'Changed lambda schedule')
need(set(data['grams'])=={'F','J','h','old96'},'Unexpected Gram blocks')
stats={};radii={}
for name,g in data['grams'].items():
    rm=matrix(g['raw_midpoint_exact']);rr=matrix(g['raw_entry_radius_exact'])
    m=matrix(g['midpoint_exact']);er=matrix(g['entry_radius_exact'])
    d=list(map(Q,g['radius_diagonal_exact']));n=len(m)
    need(n=={'F':12,'J':84,'h':12,'old96':96}[name],'Dimension')
    need(all(len(x)==n for a in [rm,rr,m,er]for x in a),'Nonsquare Gram')
    need(all(x>=0 for row in rr for x in row),'Negative raw radius')
    need(m==transpose(m) and er==transpose(er),'Symmetry')
    for i in range(n):
        for j in range(n):
            lo=max(rm[i][j]-rr[i][j],rm[j][i]-rr[j][i])
            hi=min(rm[i][j]+rr[i][j],rm[j][i]+rr[j][i])
            need(lo<=hi,'Empty intersection')
            need(m[i][j]==(rm[i][j]+rm[j][i])/2,'Symmetrized midpoint')
            need(er[i][j]==max(abs(lo-m[i][j]),abs(hi-m[i][j])),'Exact centered radius')
        need(d[i]>=sum(er[i],Q()),'Unpaid Gram row radius')
    radii[name]=d
    stats[name]={'dimension':n,'raw_midpoint_symmetric':rm==transpose(rm),'all_exact_row_bounds_pass':True,
                 'largest_radius_diagonal':str(max(d))}

delta=Q(data['delta_exact']);eb=Q(data['coupling_error_upper_exact']);tx=Q(data['inverse_metric_trace_upper_exact'])
need(delta==Q('1.84298') and eb>=0 and tx>0,'Invalid transport scalar')
need(data['original_error_component_count']==ledger['quadratic_radius_transport']['number_of_original_error_components']==11,'Changed number of error vectors')
lam={k:Q(v['lambda_exact'])for k,v in ledger['radius_cross_terms'].items()}
expected={'old96_high_linear','h_high_linear','F_h_physical','J_h_physical','F_old_B','J_old_B'}
need(set(lam)==expected and all(x>0 for x in lam.values()),'Unexpected/invalid Young factors')
for key,l in lam.items():
    lo,hi=map(Q,old['young_parameters'][key])
    need(lo<=l<=hi,'Lambda not in original enclosure')
prices={}
def embed(name,gram,weight,start):
    v=[Q()for _ in range(108)]
    for i,r in enumerate(radii[gram]):v[start+i]=weight*r
    prices[name]=v
embed('old96_high_linear','old96',lam['old96_high_linear']/delta,0)
embed('h_high_linear','h',lam['h_high_linear']/delta,96)
for g,offset in [('F',0),('J',12)]:
    embed(g+'_h_physical',g,2*lam[g+'_h_physical']/delta,offset)
    embed(g+'_old_B',g,eb**2/(delta**2*lam[g+'_old_B']),offset)
    embed(g+'_second_variation',g,11*tx*eb**2/delta**2,offset)
need(prices=={k:list(map(Q,v))for k,v in data['rational_formula_upper_diagonals'].items()},'Exact weighted prices disagree')
total=[sum((v[i]for v in prices.values()),Q())for i in range(108)]
need(total==list(map(Q,data['rational_formula_total_upper_diagonal'])),'Sum of weighted prices')
paid=ledger['matrices']['radius_added_upper']
need(all(list(map(Q,paid[i][j]))==[Q(),Q()]for i in range(108)for j in range(108)if i!=j),'Nonzero off-diagonal radius charge')
need(all(Q(paid[i][i][1])>=total[i]for i in range(108)),'Insufficient extra charge')
need(ledger['matrices']['v1_schedule_error_upper']==old['matrices']['error_upper'],'Preexisting ledger changed')

# Independent scalar regressions of both error mechanisms.
g=Q(11,10);e=Q(11,20);m=Q(1);r=Q(21,100);lam0=Q(1,2)
actual=(g+e)**2;oldprice=m+lam0*m+(1+1/lam0)*e**2+r
need(actual==Q(1089,400) and oldprice==Q(1047,400),'Original counterexample')
need(oldprice<actual and oldprice+lam0*r==actual,'lambda R not repaired')
oldinverse=Q(1,2)*4+Q(9,10)/Q(1,2)
need(oldinverse==Q(19,5)<4 and oldinverse+Q(1,10)/Q(1,2)==4,'R/lambda not repaired')

out={'status':'GPT1_SEVEN_RADIUS_CHARGES_EXACT_PASS','gram_blocks':stats,
     'seven_positions_eight_formula_rows':True,'all_108_coordinates_paid':True,
     'v1_ledger_component_unchanged':True,'original_young_schedule_unchanged':True,
     'quadratic_component_count':11,
     'counterexamples':{'lambda_R':{'actual':str(actual),'old':str(oldprice),'corrected':str(actual)},
                        'R_over_lambda':{'actual':'4','old':str(oldinverse),'corrected':'4'}},
     'source_raw_ball_binding':'Separately regenerated from unchanged v1 source fields by the fresh finite replay.',
     'rational_price_total_diagonal':list(map(str,total))}
(P/'INDEPENDENT_RADIUS_AUDIT.json').write_text(json.dumps(out,indent=2)+'\n')
print('GPT1_SEVEN_RADIUS_CHARGES_EXACT_PASS: 4 Grams, 108 coordinates, unchanged old charges and lambdas, both counterexamples repaired')
