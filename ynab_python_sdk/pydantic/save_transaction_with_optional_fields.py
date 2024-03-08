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

from ynab_python_sdk.pydantic.save_sub_transaction import SaveSubTransaction
from ynab_python_sdk.pydantic.transaction_cleared_status import TransactionClearedStatus
from ynab_python_sdk.pydantic.transaction_flag_color import TransactionFlagColor

class SaveTransactionWithOptionalFields(BaseModel):
    account_id: typing.Optional[str] = Field(None, alias='account_id')

    # The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored.
    date: typing.Optional[date] = Field(None, alias='date')

    # The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored.
    amount: typing.Optional[int] = Field(None, alias='amount')

    # The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `tranfer_payee_id` on the account resource.
    payee_id: typing.Optional[typing.Optional[str]] = Field(None, alias='payee_id')

    # The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if `import_id` is also specified) or (2) a payee with the same name or (3) creation of a new payee.
    payee_name: typing.Optional[typing.Optional[str]] = Field(None, alias='payee_name')

    # The category for the transaction.  To configure a split transaction, you can specify null for `category_id` and provide a `subtransactions` array as part of the transaction object.  If an existing transaction is a split, the `category_id` cannot be changed.  Credit Card Payment categories are not permitted and will be ignored if supplied.
    category_id: typing.Optional[typing.Optional[str]] = Field(None, alias='category_id')

    memo: typing.Optional[typing.Optional[str]] = Field(None, alias='memo')

    cleared: typing.Optional[TransactionClearedStatus] = Field(None, alias='cleared')

    # Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default.
    approved: typing.Optional[bool] = Field(None, alias='approved')

    flag_color: typing.Optional[TransactionFlagColor] = Field(None, alias='flag_color')

    # An array of subtransactions to configure a transaction as a split. Updating `subtransactions` on an existing split transaction is not supported.
    subtransactions: typing.Optional[typing.List[SaveSubTransaction]] = Field(None, alias='subtransactions')
    class Config:
        arbitrary_types_allowed = True
