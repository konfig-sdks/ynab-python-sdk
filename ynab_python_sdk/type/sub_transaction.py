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


class RequiredSubTransaction(TypedDict):
    id: str

    transaction_id: str

    # The subtransaction amount in milliunits format
    amount: int

    # Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests.
    deleted: bool

class OptionalSubTransaction(TypedDict, total=False):
    memo: typing.Optional[str]

    payee_id: typing.Optional[str]

    payee_name: typing.Optional[str]

    category_id: typing.Optional[str]

    category_name: typing.Optional[str]

    # If a transfer, the account_id which the subtransaction transfers to
    transfer_account_id: typing.Optional[str]

    # If a transfer, the id of transaction on the other side of the transfer
    transfer_transaction_id: typing.Optional[str]

class SubTransaction(RequiredSubTransaction, OptionalSubTransaction):
    pass
