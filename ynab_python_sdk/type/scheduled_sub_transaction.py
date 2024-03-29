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


class RequiredScheduledSubTransaction(TypedDict):
    id: str

    scheduled_transaction_id: str

    # The scheduled subtransaction amount in milliunits format
    amount: int

    # Whether or not the scheduled subtransaction has been deleted. Deleted scheduled subtransactions will only be included in delta requests.
    deleted: bool

class OptionalScheduledSubTransaction(TypedDict, total=False):
    memo: typing.Optional[str]

    payee_id: typing.Optional[str]

    category_id: typing.Optional[str]

    # If a transfer, the account_id which the scheduled subtransaction transfers to
    transfer_account_id: typing.Optional[str]

class ScheduledSubTransaction(RequiredScheduledSubTransaction, OptionalScheduledSubTransaction):
    pass
