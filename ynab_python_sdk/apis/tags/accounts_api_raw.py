# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by: https://konfigthis.com
"""

from ynab_python_sdk.paths.budgets_budget_id_accounts.post import CreateNewAccountRaw
from ynab_python_sdk.paths.budgets_budget_id_accounts_account_id.get import GetSingleAccountRaw
from ynab_python_sdk.paths.budgets_budget_id_accounts.get import ListAllRaw


class AccountsApiRaw(
    CreateNewAccountRaw,
    GetSingleAccountRaw,
    ListAllRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
