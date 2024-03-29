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


class MonthSummary(BaseModel):
    month: date = Field(alias='month')

    # The total amount of transactions categorized to 'Inflow: Ready to Assign' in the month
    income: int = Field(alias='income')

    # The total amount budgeted in the month
    budgeted: int = Field(alias='budgeted')

    # The total amount of transactions in the month, excluding those categorized to 'Inflow: Ready to Assign'
    activity: int = Field(alias='activity')

    # The available amount for 'Ready to Assign'
    to_be_budgeted: int = Field(alias='to_be_budgeted')

    # Whether or not the month has been deleted.  Deleted months will only be included in delta requests.
    deleted: bool = Field(alias='deleted')

    note: typing.Optional[typing.Optional[str]] = Field(None, alias='note')

    # The Age of Money as of the month
    age_of_money: typing.Optional[typing.Optional[int]] = Field(None, alias='age_of_money')
    class Config:
        arbitrary_types_allowed = True
