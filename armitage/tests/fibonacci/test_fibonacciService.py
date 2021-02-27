import unittest

from flaskMathApp.fibonacci.service import fibonacciService

class FibonacciServiceTestCase(unittest.TestCase):
    def test_sanitize_inputs_success(self):
        result = fibonacciService.sanitizeAndCalculate(1)
        self.assertTrue(result != None)

    def test_sanitize_inputs_wrong_type(self):
        result = fibonacciService.sanitizeAndCalculate('test')
        self.assertTrue(result == None)
        
    def test_sanitize_inputs_negative(self):
        result = fibonacciService.sanitizeAndCalculate(-1)
        self.assertTrue(result == None)

    def test_right_calculation(self):
        result = fibonacciService.fib(4)
        self.assertEqual(result, 3)