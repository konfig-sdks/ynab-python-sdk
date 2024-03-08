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


class Payee(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    # Whether or not the payee has been deleted.  Deleted payees will only be included in delta requests.
    deleted: bool = Field(alias='deleted')

    # If a transfer payee, the `account_id` to which this payee transfers to
    transfer_account_id: typing.Optional[typing.Optional[str]] = Field(None, alias='transfer_account_id')
    class Config:
        arbitrary_types_allowed = True