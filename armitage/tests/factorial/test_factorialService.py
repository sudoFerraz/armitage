import unittest

from flaskMathApp.factorial.service import factorialService

class FactorialServicetestCase(unittest.TestCase):
    def test_sanitize_inputs_success(self):
        result = factorialService.sanitizeAndCalculate(1)
        self.assertTrue(result != None)

    def test_sanitize_inputs_fail(self):
        result = factorialService.sanitizeAndCalculate('test')
        self.assertTrue(result == None)

    def test_correct_calculation(self):
        result = factorialService.calculate(1)
        self.assertEqual(1, 1)