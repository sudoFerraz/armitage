import os
import tempfile

import pytest
import unittest

from flaskMathApp import create_app


class AppInitializationTestCase(unittest.TestCase):

    def test_home(self):
        tester = create_app().test_client()
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Please refer to the endpoint documentation')

    def test_other(self):
        tester = create_app().test_client()
        response = tester.get('/a', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        tester = create_app().test_client()
        response = tester.post('/fibonacci', json={'fibonacciStep': 0})
        self.assertEqual(response.status_code, 200)
