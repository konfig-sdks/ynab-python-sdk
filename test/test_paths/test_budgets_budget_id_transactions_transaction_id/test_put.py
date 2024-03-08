# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import ynab_python_sdk
from ynab_python_sdk.paths.budgets_budget_id_transactions_transaction_id import put
from ynab_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestBudgetsBudgetIdTransactionsTransactionId(ApiTestMixin, unittest.TestCase):
    """
    BudgetsBudgetIdTransactionsTransactionId unit test stubs
        Updates an existing transaction
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
