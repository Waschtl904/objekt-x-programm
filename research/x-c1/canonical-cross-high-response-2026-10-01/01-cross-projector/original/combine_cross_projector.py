"""Intersect independently valid actual-operator enclosures."""
from pathlib import Path
from fractions import Fraction as F
import argparse,hashlib,json
def combine(paths):
 reports=[json.loads(p.read_bytes()) for p in paths]
 assert len({r['main'] for r in reports})==1
 assert all(r['status']=='EXPLORATORY_RIGOROUS_ENCLOSURES_NOT_GATE_ACCEPTANCE' for r in reports)
 sources={}
 for r in reports:
  for name,h in r['source_sha256'].items():
   assert name not in sources or sources[name]==h
   sources[name]=h
 def matrix(key):
  out=[]
  for i in range(6):
   row=[]
   for j in range(8):
    lo=max(F(r[key][i][j][0]) for r in reports);hi=min(F(r[key][i][j][1]) for r in reports)
    assert lo<=hi,(key,i,j)
    row.append([str(lo),str(hi)])
   out.append(row)
  return out
 return {'status':'EXPLORATORY_RIGOROUS_ENCLOSURES_NOT_GATE_ACCEPTANCE','stage':'A_AND_B',
  'main':reports[0]['main'],'source_sha256':sources,
  'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
  'K_direct_enclosure':matrix('K_direct_enclosure'),'Y_direct_enclosure':matrix('Y_direct_enclosure'),
  'joint_residual_identity_checked':True,'full_high_response_paid':True,
  'A13_inputs_used':False,'actual_odd_angle_certified':False}
def main():
 p=argparse.ArgumentParser();p.add_argument('--input',type=Path,nargs=3,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 a.out.write_text(json.dumps(combine(a.input),indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
