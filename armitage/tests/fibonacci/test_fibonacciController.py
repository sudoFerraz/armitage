import os
import tempfile

import unittest

from flaskMathApp import create_app

class FibonacciControllerTestCase(unittest.TestCase):

    def test_get_endpoint_success(self):
        tester = create_app().test_client()
        response = tester.get('/fibonacci/0', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_endpoint_fail(self):
        tester = create_app().test_client()
        response = tester.get('/fibonacci/test', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_post_endpoint_success(self):
        tester = create_app().test_client()
        response = tester.post('/fibonacci', json={'fibonacciStep': 0})
        self.assertEqual(response.status_code, 200)

    def test_post_enpoint_fail(self):
        tester = create_app().test_client()
        response = tester.post('/fibonacci', json={'fibonacciStep': 'test'})
        self.assertEqual(response.status_code, 400)

    