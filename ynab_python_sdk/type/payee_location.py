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


class RequiredPayeeLocation(TypedDict):
    id: str

    payee_id: str

    latitude: str

    longitude: str

    # Whether or not the payee location has been deleted.  Deleted payee locations will only be included in delta requests.
    deleted: bool

class OptionalPayeeLocation(TypedDict, total=False):
    pass

class PayeeLocation(RequiredPayeeLocation, OptionalPayeeLocation):
    pass
