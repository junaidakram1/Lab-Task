import unittest
from RulesOf6005 import RulesOf6005

class TestRulesOf6005(unittest.TestCase):
    
    def test_uncited_public_code(self):
        self.assertFalse(
            RulesOf6005.may_use_code_in_assignment(False, True, False, False, False),
            "Expected false: un-cited publicly-available code"
        )

    def test_self_written_code(self):
        self.assertTrue(
            RulesOf6005.may_use_code_in_assignment(True, False, True, True, True),
            "Expected true: self-written required code"
        )
        
    def test_self_written_not_available_not_cited(self):
        self.assertTrue(
            RulesOf6005.may_use_code_in_assignment(True, False, False, False, False),
            "Expected true: self-written code"
        )
        
    def test_not_self_written_but_available(self):
        self.assertTrue(
            RulesOf6005.may_use_code_in_assignment(False, True, True, True, True),
            "Expected true: publicly available, required code"
        )

if __name__ == "__main__":
    unittest.main()
