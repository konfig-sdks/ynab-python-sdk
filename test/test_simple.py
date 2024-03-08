# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from ynab_python_sdk import Ynab

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        ynab = Ynab(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(ynab)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
