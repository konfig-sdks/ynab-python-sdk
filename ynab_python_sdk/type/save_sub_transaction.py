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


class RequiredSaveSubTransaction(TypedDict):
    # The subtransaction amount in milliunits format.
    amount: int

class OptionalSaveSubTransaction(TypedDict, total=False):
    # The payee for the subtransaction.
    payee_id: typing.Optional[str]

    # The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified on parent transaction) or (2) a payee with the same name or (3) creation of a new payee.
    payee_name: typing.Optional[str]

    # The category for the subtransaction.  Credit Card Payment categories are not permitted and will be ignored if supplied.
    category_id: typing.Optional[str]

    memo: typing.Optional[str]

class SaveSubTransaction(RequiredSaveSubTransaction, OptionalSaveSubTransaction):
    pass