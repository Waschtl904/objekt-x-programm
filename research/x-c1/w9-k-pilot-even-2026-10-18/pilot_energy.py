"""Frozen even witness: explicit K/P/weight update of the bound #238 assembler."""
import argparse
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path
from flint import arb,arb_mat,ctx
from common import Inputs,q,box,mat,ratmat,trace,norm,need,pad,enc,encode,HERE
from pilot_weights import build,sub


def quad(A,c):
    return (c.transpose()*A*c)[0,0]


def gram_norm_upper(x):
    """Norm upper bound from a known Gram identity, with no absolute-value repair."""
    need(x.upper()>=0,'Negative norm square upper endpoint')
    return x.upper().sqrt()


def load_pairs(path):
    raw=path.read_bytes()
    value=json.loads(gzip.decompress(raw) if raw[:2]==b'\x1f\x8b' else raw)
    value['_source_sha256']=hashlib.sha256(raw).hexdigest()
    return value


class Energy:
    def __init__(self,inp,data,K,P,pweight):
        self.inp=inp;self.data=data;self.par=data['parity'];p=int(self.par=='odd')
        self.pweight=pweight
        self.bounds,self.w=build(inp,self.par,K,P,pweight)
        c=inp.json('common')['cases'][p];raw=inp.json('old_sources')['cases'][p]
        C=self.w['C'];delta=self.w['delta'];rho=self.w['rho'];Ki=self.w['Ki'];a=self.w['a'];P=self.w['P']
        self.k=Ki*a
        self.ell=mat(data['Phi_star_h']);hc=mat(data['high_cross_models']);bare=mat(data['bare_F_J_pairs'])
        self.By=sub(hc,range(191),range(12));yf=sub(hc,range(191,203),range(12));yj=sub(hc,range(203,287),range(12))
        self.wh=C.transpose()*(self.ell-self.By/delta)/(1-rho).sqrt()
        self.wf=C.transpose()*(mat(raw['old_certificate']['source_c_model'])-mat(raw['old_certificate']['source_Bh_model'])/delta)/(1-rho).sqrt()
        self.wj=C.transpose()*(mat(raw['galerkin']['old_low_c_model'])-mat(raw['galerkin']['old_low_Bh_model'])/delta)/(1-rho).sqrt()
        bf=sub(bare,range(12),range(12));bj=sub(bare,range(12,96),range(12))
        self.v=bf-yf/delta-self.wf.transpose()*self.wh
        self.ws=self.wj-self.wf*self.k
        # Evaluate the composed difference first. No separate squaring of
        # Lambda J, gJ U8 or a_fin K^-1 v is performed.
        self.nu=(bj-self.k.transpose()*bf)-(yj-self.k.transpose()*yf)/delta-self.ws.transpose()*self.wh
        alternate=bj-yj/delta-self.wj.transpose()*self.wh-a.transpose()*Ki*self.v
        need(all(self.nu[i,j].overlaps(alternate[i,j])for i in range(84)for j in range(12)), 'Joint nu identity')
        self.components={'high_U8':mat(data['high_Gram'])/delta,
                         'finite_U8':self.wh.transpose()*self.wh,
                         'K_inverse_v':self.v.transpose()*Ki*self.v,
                         'P_upper_J_star_nu':self.pweight*self.nu.transpose()*P*self.nu}
        self.total=sum(self.components.values(),arb_mat(12,12))
        self.G=mat(data['G_W']);self.H=mat(data['H8_Gram']);self.eh=mat(data['e_h'])
        self.EF=mat(c['finite_feature_error_gram']);self.eJ=box(c['tail_feature_error_scalar']).sqrt()
        self.ELF=mat(raw['old_certificate']['joint_low_source_error_gram'])
        self.eLJ=self.w['gamma'].sqrt()*box(raw['galerkin']['source_model_error_norm'])
        self.a8=3*arb(2).log()/2;self.a=arb(3).log();self.b=arb(11).log()/2
        oldeps=self.bounds['old_QPhi_regular_kernel_uniform_error']
        self.eRawA=2*self.a8*oldeps*self.w['gamma'].sqrt()
        self.eLowA=8*self.a8*oldeps*self.w['gamma']
        neweps=self.bounds['old_FJ_regular_kernel_uniform_error']
        mu8=(self.a8*(1 if p==0 else -1)+self.a8.sinh())/2
        mu9=(self.a*(1 if p==0 else -1)+self.a.sinh())/2
        self.eBareF=(mu9/mu8).sqrt()*box(data['old_Y_coordinate_rounding_norm'])
        self.eBareJ=(mu9/mu8).sqrt()*box(data['old_J_coordinate_rounding_norm'])
        self.eRawF=2*self.a*neweps*16+1000*self.eBareF+q('1e-200')
        self.eRawJ=2*self.a*neweps*q('1.000502').sqrt()+1000*self.eBareJ+q('1e-200')
        # Degree-160 moment truncation, including its derivative, is much
        # smaller than the allocated whole-function 10^-200 error.
        tail=(self.a8/2).exp()*(self.a8/2)**160/arb.fac_ui(160)
        need(10**6*tail<q('1e-200'),'Moment Taylor tail budget')
        # The frozen coefficient discrepancy is priced as a full function.
        functions=inp.json('functions')['parities'][self.par]['functions']
        dnorm=[]
        for f in functions:
            sp=f['D']
            n=sum((abs(q(v))for v in sp['polynomial']),arb(0))
            n+=2*sum((abs(q(v))for v in sp['V_multiplier']),arb(0))
            n+=abs(q(sp['moment_multiplier']))*(self.a/2).exp()
            for shift in sp['shift_terms']:n+=sum((abs(q(v))for v in shift['polynomial']),arb(0))
            dnorm.append(n)
        Dnorm=sum((v*v for v in dnorm),arb(0)).sqrt()
        et=norm(mat(data['T_enclosure'])-mat(data['T']))*Dnorm
        ec=(48*self.a*(self.b-self.a)).sqrt()*self.bounds['new_regular_kernel_uniform_error']
        ed=q(inp.json('response')['parities'][self.par]['fixed_X']['whole_Hilbert_residual_model_error_upper'])
        self.residual_errors={'answer_model_Hilbert':ed,'new_Gamma_Hilbert':ec,'frozen_T_Hilbert':et}
        self.eResidual=sum(self.residual_errors.values(),arb(0))
        # Necessary independent sanity controls, never used as a quadrature proof.
        trHB=q(inp.json('high_response')[self.par]['tr_X_HB_exact_rational'])*(1-rho)
        controls=[]
        for j in range(12):
            yy=self.components['high_U8'][j,j]*delta
            need(yy>0,'Nonpositive complete high norm')
            cb=sub(C.transpose()*self.By,range(191),[j])
            gap=trHB*yy-(cb.transpose()*cb)[0,0]
            need(gap.upper()>-q('1e-15'),'B-high Cauchy bound violated')
            controls.append(gap)
        self.controls={'nu_identity_entries':1008,'C_B_high_Cauchy_gaps':controls}
        HF=mat(raw['old_certificate']['source_h_gram_model'])
        # H84_model retains the original 91/50 normalization; the renewed
        # U8 weight delta=18219/10000 must not replace that historical scale.
        HJ=mat(raw['galerkin']['H84_model'])*q('91/50')
        high_gaps=[]
        for source,gram in ((yf,HF),(yj,HJ)):
            for i in range(source.nrows()):
                for j in range(12):
                    gap=gram[i,i]*self.components['high_U8'][j,j]*delta-source[i,j]**2
                    need(gap.lower()>-q('1e-15'),'Whole high source Cauchy control')
                    high_gaps.append(gap)
        self.controls['high_source_Cauchy_entries']=len(high_gaps)
        self.controls['minimum_high_source_Cauchy_gap']=min(v.lower()for v in high_gaps)
        previous=inp.json('maps_'+self.par+'_512')
        previous_cp=arb_mat([[q(str(v))for v in row]for row in previous['feature_factor']])
        previous_bf=arb_mat([[q(str(v))for v in row]for row in previous['b_F']])
        cp_difference=norm(C.transpose()*self.ell-previous_cp)
        bf_difference=norm(bf-previous_bf)
        need(cp_difference<q('1e-7') and bf_difference<q('1e-7'),'Previous independently partitioned residual maps disagree')
        self.controls.update(previous_C_Phi_difference=cp_difference,previous_b_F_difference=bf_difference)
        psi=inp.json('psi')['data'][self.par]['directions']['lower_Pv']
        action=inp.json('finite_action')[self.par]['directions']['lower_Pv']
        t=arb_mat([[q(v)]for v in psi['t_exact']]);k0=arb_mat([[q(v)]for v in psi['k_model_exact']])
        cp=arb_mat([[box(v)]for v in action['c_model']])
        i0=(t.transpose()*bj-k0.transpose()*bf-cp.transpose()*self.ell)[0,0]/self.G[0,0].sqrt()
        previous_i0=box(inp.json('l00_'+self.par)['I0'])
        need(i0.overlaps(previous_i0),'Independent old z0 I0 reconstruction')
        self.controls['z0_I0_from_84_bare_pairings']=i0

    def certificate(self,coefficients,budget_upper,name):
        need(len(coefficients)==12,'Candidate dimension')
        c=arb_mat([[q(v)]for v in coefficients]);n2=quad(self.G,c)
        need(n2>0,'Positive candidate W norm')
        normalization=n2.sqrt();c/=normalization
        w=self.w;gamma=w['gamma'];delta=w['delta'];rho=w['rho'];C=w['C'];Ki=w['Ki'];P=w['P']
        # These are norms of the integrated functions. Intersecting an
        # enclosing interval with [0,infinity) uses that Gram identity; a
        # strictly negative upper endpoint is rejected, never absolutized.
        hn=gram_norm_upper(quad(self.H,c));eh=abs((self.eh*c)[0,0]).upper();en=norm(self.ell*c)
        fn=gram_norm_upper(quad(mat(self.data['H9_Gram']),c))
        crossfactor=hn+gamma*eh
        eBy=self.eRawA*crossfactor+self.eLowA*en
        eWh=norm(C)*eBy/(delta*(1-rho).sqrt())
        whn=norm(self.wh*c)
        fhigh=self.eRawF*trace(Ki).sqrt()*crossfactor+trace(Ki*self.ELF).sqrt()*en
        v_error=(self.eBareF*trace(Ki).sqrt()*fn+fhigh/delta+trace(Ki*self.wf.transpose()*self.wf).sqrt()*eWh+
                 trace(Ki*self.EF).sqrt()*(whn+eWh))
        kP=trace(P*self.k.transpose()*self.k).sqrt()
        rawS=self.eRawJ*trace(P).sqrt()+self.eRawF*kP
        lowS=self.eLJ*trace(P).sqrt()+trace(P*self.k.transpose()*self.ELF*self.k).sqrt()
        sourceS=self.eJ*trace(P).sqrt()+trace(P*self.k.transpose()*self.EF*self.k).sqrt()
        nu_error=((self.eBareJ*trace(P).sqrt()+self.eBareF*kP)*fn+(rawS*crossfactor+lowS*en)/delta+
                  trace(P*self.ws.transpose()*self.ws).sqrt()*eWh+sourceS*(whn+eWh))
        kv=Ki*self.v*c
        a_error=w['da']*trace(P*w['GJ']).sqrt()*(gram_norm_upper(quad(w['GF'],kv))+trace(Ki*w['GF']).sqrt()*v_error)
        nu_error+=a_error
        feature_errors={'high_U8_additional_old_source_error':arb(0),
                        'finite_U8':eWh,'K_inverse_v':v_error,
                        'P_upper_J_star_nu':self.pweight.sqrt()*nu_error}
        efeatures=sum((v*v for v in feature_errors.values()),arb(0)).sqrt()
        eres=w['w'].sqrt()*self.eResidual
        values={k:quad(A,c)for k,A in self.components.items()}
        model=sum(values.values(),arb(0));need(model.upper()>0,'Nonpositive partial energy')
        lo=max(arb(0),max(arb(0),model.lower()).sqrt()-efeatures.upper()-eres.upper())**2
        hi=(model.upper().sqrt()+efeatures.upper()+eres.upper())**2
        actual_interval=isinstance(budget_upper,list)
        K=box(budget_upper)if actual_interval else q(budget_upper)
        # Classify the actual outward-rounded rational endpoints which are
        # published, not a narrower internal ball before output rounding.
        interval=[enc(lo)[0],enc(hi)[1]];budget_interval=enc(K)
        if Fraction(interval[0])>Fraction(budget_interval[1]):outcome='PARTIAL_ENERGY_EXCLUDES_FOR_DIRECTION'
        elif actual_interval and Fraction(interval[1])<=Fraction(budget_interval[0]):outcome='PARTIAL_ENERGY_BELOW_ACTUAL_BUDGET_FOR_DIRECTION'
        elif actual_interval:outcome='INCONCLUSIVE_PARTIAL_ENERGY_FOR_DIRECTION'
        else:outcome='NO_EXCLUSION_WITH_THIS_BUDGET_UPPER'
        return {'name':name,'raw_coefficients':coefficients,'normalization':normalization,
                'pairs_sha256':self.data['_source_sha256'],
                'criterion':'FIXED_W9_COMPARISON_RULE_PARTIAL_LOWER_VS_K_P_UPPER',
                'component_model_energies':values,'partial_model_energy':model,
                'component_integration_and_arithmetic_radii':{k:v.rad()for k,v in values.items()},
                'feature_error_norms':feature_errors,'a_fin_common_error_contribution':a_error,
                'residual_model_error_norm':eres,'partial_actual_energy_interval':interval,
                'budget_interval_or_upper':budget_interval,'budget_kind':'ACTUAL_INTERVAL'if actual_interval else'UPPER_ONLY',
                'lower_energy_minus_budget_upper':q(interval[0])-q(budget_interval[1]),
                'outcome':outcome,'RL_computed':False,'full_energy_upper_claimed':False,'N12_closed':False}
