import os
import tempfile

import unittest

from flaskMathApp.ackermann.service import ackermannService

class AckermannServiceTestCase(unittest.TestCase):

    def test_sanitize_inputs_success(self):
        result = ackermannService.sanitizeAndCalculate(1, 1)
        self.assertTrue(result != None)

    def test_sanitize_inputs_wrong_type(self):
        result = ackermannService.sanitizeAndCalculate(1, 'test')
        self.assertEqual(result, None)

    def test_correct_calculation(self):
        result = ackermannService.ackermann(1, 1)
        self.assertEqual(result, 3)
    