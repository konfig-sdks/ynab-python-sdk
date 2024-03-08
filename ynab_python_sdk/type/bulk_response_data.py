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

from ynab_python_sdk.type.bulk_response_data_bulk import BulkResponseDataBulk

class RequiredBulkResponseData(TypedDict):
    bulk: BulkResponseDataBulk

class OptionalBulkResponseData(TypedDict, total=False):
    pass

class BulkResponseData(RequiredBulkResponseData, OptionalBulkResponseData):
    pass
