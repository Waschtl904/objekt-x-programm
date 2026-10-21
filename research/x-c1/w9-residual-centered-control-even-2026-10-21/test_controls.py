"""Fail-closed tests for the certificate's conditional scope and bindings."""
import copy
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

HERE=Path(__file__).resolve().parent


def load(name):
    spec=importlib.util.spec_from_file_location('residual_control_'+name,HERE/(name+'.py'))
    mod=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Controls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit=load('audit')
        cls.engine=load('engine')
        cls.result=json.loads((HERE/'RESULT.json').read_bytes())
        root=HERE.parents[2]
        spec=json.loads((HERE/'INPUT_BINDINGS.json').read_bytes())
        cls.old=json.loads((root/spec['files']['schur_result']['path']).read_bytes())
        cls.rest=json.loads((root/spec['files']['rest_result']['path']).read_bytes())

    def check_modified(self,key,value):
        r=copy.deepcopy(self.result);r[key]=value
        with self.assertRaises(RuntimeError):self.audit.check(r,self.old,self.rest)

    def test_actual_data_pass(self):
        self.assertEqual(self.audit.check(self.result,self.old,self.rest)['status'],
                         'PASS_INDEPENDENT_RATIONAL_SCALAR_AUDIT')

    def test_large_residual_target_is_rejected(self):
        self.check_modified('sufficient_whole_residual_Ldual_upper','1e-6')

    def test_finite_coordinates_cannot_be_promoted(self):
        self.check_modified('whole_residual_energy_computed',True)

    def test_conditional_pass_is_not_actual_pass(self):
        self.check_modified('whole_comparison_pass',True)

    def test_changed_old_price_is_rejected(self):
        self.check_modified('old_form_price_upper','0')

    def test_negative_norm_square_is_rejected(self):
        with self.assertRaises(RuntimeError):self.audit.sqrt_up('-1')

    def test_force_transport_cannot_close_residual_inventory(self):
        r=copy.deepcopy(self.result)
        r['whole_force_transport']['whole_residual_error_inventory_complete']=True
        with self.assertRaises(RuntimeError):self.audit.check(r,self.old,self.rest)

    def test_tampered_input_is_rejected(self):
        with tempfile.TemporaryDirectory()as td:
            root=Path(td).resolve();(root/'input').write_bytes(b'changed')
            spec={'source_commit':self.engine.BASE,'files':{'x':{'path':'input','sha256':'0'*64}}}
            with self.assertRaises(RuntimeError):self.engine.snapshot(root,json.dumps(spec).encode())

    def test_escaping_input_is_rejected_before_read(self):
        with tempfile.TemporaryDirectory()as td:
            spec={'source_commit':self.engine.BASE,'files':{'x':{'path':'../outside','sha256':'0'*64}}}
            with self.assertRaises(RuntimeError):self.engine.snapshot(Path(td).resolve(),json.dumps(spec).encode())


if __name__=='__main__':unittest.main()
