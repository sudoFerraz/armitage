import os
import tempfile

import unittest

from flaskMathApp import create_app

class AckermannControllerTestCase(unittest.TestCase):

    def test_get_endpoint_succes(self):
        tester = create_app().test_client()
        response = tester.get('/ackermann/1/1', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_get_endpoint_fail(self):
        tester = create_app().test_client()
        response = tester.get('/ackermann/1/eijf', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_post_endpoint_succes(self):
        tester = create_app().test_client()
        response = tester.post('/ackermann', json={'m': 1, 'n': 1})
        self.assertEqual(response.status_code, 200)

    def test_post_endpoint_fail(self):
        tester = create_app().test_client()
        response = tester.post('/ackermann', json={'m': 'fiej', 'n': 1})
        self.assertEqual(response.status_code, 400)