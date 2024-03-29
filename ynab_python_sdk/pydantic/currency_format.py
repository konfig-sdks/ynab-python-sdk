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


class CurrencyFormat(BaseModel):
    iso_code: str = Field(alias='iso_code')

    example_format: str = Field(alias='example_format')

    decimal_digits: int = Field(alias='decimal_digits')

    decimal_separator: str = Field(alias='decimal_separator')

    symbol_first: bool = Field(alias='symbol_first')

    group_separator: str = Field(alias='group_separator')

    currency_symbol: str = Field(alias='currency_symbol')

    display_symbol: bool = Field(alias='display_symbol')
    class Config:
        arbitrary_types_allowed = True
