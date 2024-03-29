# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel

from ynab_python_sdk.pydantic.account_type import AccountType
from ynab_python_sdk.pydantic.loan_account_periodic_value import LoanAccountPeriodicValue

class Account(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    type: AccountType = Field(alias='type')

    # Whether this account is on budget or not
    on_budget: bool = Field(alias='on_budget')

    # Whether this account is closed or not
    closed: bool = Field(alias='closed')

    # The current balance of the account in milliunits format
    balance: int = Field(alias='balance')

    # The current cleared balance of the account in milliunits format
    cleared_balance: int = Field(alias='cleared_balance')

    # The current uncleared balance of the account in milliunits format
    uncleared_balance: int = Field(alias='uncleared_balance')

    # The payee id which should be used when transferring to this account
    transfer_payee_id: typing.Optional[str] = Field(alias='transfer_payee_id')

    # Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests.
    deleted: bool = Field(alias='deleted')

    note: typing.Optional[typing.Optional[str]] = Field(None, alias='note')

    # Whether or not the account is linked to a financial institution for automatic transaction import.
    direct_import_linked: typing.Optional[bool] = Field(None, alias='direct_import_linked')

    # If an account linked to a financial institution (direct_import_linked=true) and the linked connection is not in a healthy state, this will be true.
    direct_import_in_error: typing.Optional[bool] = Field(None, alias='direct_import_in_error')

    # A date/time specifying when the account was last reconciled.
    last_reconciled_at: typing.Optional[typing.Optional[datetime]] = Field(None, alias='last_reconciled_at')

    # The original debt/loan account balance, specified in milliunits format.
    debt_original_balance: typing.Optional[typing.Optional[int]] = Field(None, alias='debt_original_balance')

    debt_interest_rates: typing.Optional[LoanAccountPeriodicValue] = Field(None, alias='debt_interest_rates')

    debt_minimum_payments: typing.Optional[LoanAccountPeriodicValue] = Field(None, alias='debt_minimum_payments')

    debt_escrow_amounts: typing.Optional[LoanAccountPeriodicValue] = Field(None, alias='debt_escrow_amounts')
    class Config:
        arbitrary_types_allowed = True
