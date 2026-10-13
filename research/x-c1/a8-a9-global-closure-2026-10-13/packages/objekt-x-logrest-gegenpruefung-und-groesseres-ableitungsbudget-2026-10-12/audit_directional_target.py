"""Fixed rational joint log upper Gram and enlarged derivative target.

The target is stored exactly as alpha*T - beta*D - gamma*C^T G C.
No actual regularized derivative energy is computed here.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse, json, sys, zipfile, hashlib

def read(p):return json.loads(p.read_bytes())
def main(root,responses,review,out):
    sys.path.insert(0,str(root));import interval_helpers as h
    ld=h.ld
    gp=review/'data/LOG_TAIL_104.json';G=h.rat(read(gp)['full_tail_Gram_rational_upper']);Gi=h.inv(G)
    with zipfile.ZipFile(review/'inputs/Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11.zip') as z:
        gates=json.loads(z.read('Objekt-X-Zusammengesetzte-Aussenresiduen-und-Momentanschluss-2026-10-11/ATTACHMENT_GATES.json'))['cases']
    d104=F(11,10)+sum((F(1,n) for n in range(1,105)),F(0));Kfac=10920*d104
    rows=[]
    for p,label in enumerate(['EVEN','ODD']):
        r=read(responses/f'RESPONSES_{label}.json');m=read(root/f'COMPOSED_{label}_3072.json')
        rho=F(r['rho']);beta=F(r['beta']);K=h.rat(r['K12_new_rational']);Ki=h.inv(K)
        D=[[1-rho if i==j and i<191 else K[i-191][j-191] if i>=191 and j>=191 else F(0) for j in range(203)] for i in range(203)]
        MU=h.rat(r['M_upper_rational']);T=[[beta*(D[i][j]-MU[i][j]) for j in range(203)] for i in range(203)]
        cap=F(1,500) if p==0 else F(1,250);c8=F(1,5000) if p==0 else F(13,20000)
        C=[];rounderr=[]
        for row in m['C_three_log_rows_model']:
            bounds=[tuple(map(F,x)) for x in row]
            mid=[(lo+hi)/2 for lo,hi in bounds];rad=[(hi-lo)/2 for lo,hi in bounds]
            assert all(v>=0 for v in rad)
            error2=sum((v*v/(1-rho) for v in rad[:191]),F(0))+sum((rad[191+i]*abs(Ki[i][j])*rad[191+j] for i in range(12) for j in range(12)),F(0))
            C.append(mid);rounderr.append(h.sqrtup(error2))
        inherited=[F(1,10**8),F(1,10**10),F(1,10**60)]
        # Include the widths of all stored model intervals as well as the
        # analytic coefficient errors. None are placed in an H1 remainder.
        coefferr=[e+s for e,s in zip(inherited,rounderr)]
        elog=sum((h.sqrtup(G[i][i])*coefferr[i] for i in range(3)),F(0))
        tau=F(1,10**6)
        qC=(1+tau)/d104;qD=(1+1/tau)*elog**2/d104
        # Qbar=qC*C^T G C+qD*D <= cap*T. This is a fixed rational
        # matrix, with the three logarithms and all their crosses retained.
        top=[[(cap*T[i][j]-qD*D[i][j])/qC for j in range(203)] for i in range(203)]
        block=[[ld.point(top[i][j]) if i<203 and j<203 else ld.point(C[j-203][i]) if i<203 else ld.point(C[i-203][j]) if j<203 else ld.point(Gi[i-203][j-203]) for j in range(206)] for i in range(206)]
        proof=ld.positive(block)
        theta=F(21 if p==0 else 15)
        e=F(gates[p]['basis84_dual_contribution_relative_to_D_upper'])+F(1,10**300)
        aT=Kfac*theta/(1+theta)*(1-c8)
        bD=Kfac*theta/(1+theta)*e+Kfac*theta*qD
        gC=Kfac*theta*qC
        sigma=F(r['sufficient_complete_QR_normalized_budget'])
        uniform_floor=Kfac*theta/(1+theta)*((1-c8-(1+theta)*cap)*sigma-e)
        assert uniform_floor>0
        # Exact coefficient check for E_dir-E_uniform=Kfac*theta*(cap*T-Qbar).
        aU=Kfac*theta/(1+theta)*(1-c8-(1+theta)*cap)
        bU=Kfac*theta/(1+theta)*e
        assert aT-aU==Kfac*theta*cap
        assert bD-bU==Kfac*theta*qD and gC==Kfac*theta*qC
        rows.append({'parity':label.lower(),'coefficient_midpoints_3x203':[[str(x) for x in row] for row in C],
          'additional_midpoint_errors_D_dual':[str(x) for x in rounderr],
          'total_coefficient_errors_D_dual':[str(x) for x in coefferr],
          'weighted_joint_log_upper_coefficient_CtGC':str(qC),'weighted_joint_log_upper_coefficient_D':str(qD),
          'joint_log_upper_relative_to_T':str(cap),'fixed_joint_log_upper_proof':proof,
          'young_parameter':str(theta),'derivative_target_coefficient_T':str(aT),
          'derivative_target_subtracted_coefficient_D':str(bD),
          'derivative_target_subtracted_coefficient_CtGC':str(gC),
          'positive_uniform_target_lower_relative_to_D':str(uniform_floor),
          'target_formula':'E_dir = coefficient_T*T - coefficient_D*D - coefficient_CtGC*C.transpose()*G*C',
          'actual_regularized_derivative_Gram_computed':False,'full_remainder_certified':False})
        print(label,'PASS fixed rational joint log Gram and stronger directional derivative target; 206 pivots',flush=True)
    result={'status':'PASS_FIXED_RATIONAL_LOG_GRAM_AND_DIRECTIONAL_DERIVATIVE_TARGET',
        'full_log_tail_Gram_rational_upper_3x3':[[str(v) for v in row] for row in G],
        'full_log_tail_Gram_input_sha256':hashlib.sha256(gp.read_bytes()).hexdigest(),
        'cases':rows,'actual_regularized_derivative_Gram_computed':False,'full_remainder_certified':False}
    out.write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for k in ['input','responses','review','out']:ap.add_argument('--'+k,type=Path,required=True)
    x=ap.parse_args();assert __debug__;main(x.input,x.responses,x.review,x.out)
