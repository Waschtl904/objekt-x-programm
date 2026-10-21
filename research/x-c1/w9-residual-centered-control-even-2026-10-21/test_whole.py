"""Whole-residual safety checks and independent closed-form log controls."""
import ast,copy,importlib.util,json,unittest
from pathlib import Path
from unittest.mock import patch
from flint import arb,acb,ctx
HERE=Path(__file__).resolve().parent;WHOLE=HERE/'whole'

def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

class WholeControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit=load(WHOLE/'whole_audit.py','whole_audit_test')

    def changed(self,name,edit):
        target=WHOLE/name;original=Path.read_bytes
        modified=json.loads(original(target));edit(modified)
        def read(path):
            if path==target:return (json.dumps(modified,indent=2)+'\n').encode()
            return original(path)
        with patch.object(Path,'read_bytes',read):
            with self.assertRaises(RuntimeError):self.audit.audit(WHOLE)

    def test_actual_complete_data_pass(self):
        result=self.audit.audit(WHOLE)
        self.assertEqual(result['outcome'],'FIXED_EVEN_RESIDUAL_CENTERED_COMPARISON_PASS')
        self.assertFalse(result['N12_closed']);self.assertFalse(result['milestone_4_closed'])

    def test_incomplete_model_partition_fails(self):
        self.changed('taylor-model-panels-205/0205.json',lambda x:x.update(index=999))

    def test_large_operator_error_fails(self):
        self.changed('whole-error-ledger.json',lambda x:x['values'].update(proposed_Ldual_error=['0','1']))

    def test_uncontrolled_core_quadrature_fails(self):
        self.changed('core-quadrature-control-128.json',lambda x:x.update(total_outer_X_error_upper_expression=['0','1']))

    def test_wrong_endpoint_envelope_fails(self):
        self.changed('analytic-caps.json',lambda x:x['caps'].update(outer_endpoint_envelope='none'))

    def test_changed_model_hash_fails(self):
        self.changed('taylor-model-panels-205/BINDING.json',lambda x:x.update(cache='0'*64))

    def test_log_square_and_mixed_integrals(self):
        ctx.prec=256
        mod=load(WHOLE/'vendor/log_integrals.py','log_moment_test')
        m=mod.Moments({'zero':arb(0),'one':arb(1)},4)
        self.assertTrue(m.sequence('zero','one',('zero','zero'))[0].overlaps(arb(2)))
        self.assertTrue(m.sequence('zero','one',('zero','one'))[0].overlaps(2-arb.pi()**2/6))

    def test_cauchy_log_integral_known_value(self):
        ctx.prec=256
        tree=ast.parse((WHOLE/'whole_function_probe.py').read_text())
        function=next(v for v in tree.body if isinstance(v,ast.FunctionDef)and v.name=='ilog')
        ns={'arb':arb,'acb':acb}
        exec(compile(ast.Module(body=[function],type_ignores=[]),'bound_ilog_test','exec'),ns)
        # int_0^1 log(1-t)/(2-t) dt = -pi^2/12.
        self.assertTrue(ns['ilog'](arb(2),arb(1)).overlaps(-arb.pi()**2/12))

if __name__=='__main__':unittest.main()
