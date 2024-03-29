# coding: utf-8

"""
    YNAB API Endpoints

    Our API uses a REST based design, leverages the JSON data format, and relies upon HTTPS for transport. We respond with meaningful HTTP response codes and if an error occurs, we include error details in the response body.  API Documentation is at https://api.ynab.com

    The version of the OpenAPI document: 1.68.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from ynab_python_sdk import schemas  # noqa: F401


class BudgetSettings(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "date_format",
            "currency_format",
        }
        
        class properties:
        
            @staticmethod
            def date_format() -> typing.Type['DateFormat']:
                return DateFormat
        
            @staticmethod
            def currency_format() -> typing.Type['CurrencyFormat']:
                return CurrencyFormat
            __annotations__ = {
                "date_format": date_format,
                "currency_format": currency_format,
            }
    
    date_format: 'DateFormat'
    currency_format: 'CurrencyFormat'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_format"]) -> 'DateFormat': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_format"]) -> 'CurrencyFormat': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["date_format", "currency_format", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_format"]) -> 'DateFormat': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_format"]) -> 'CurrencyFormat': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["date_format", "currency_format", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        date_format: 'DateFormat',
        currency_format: 'CurrencyFormat',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BudgetSettings':
        return super().__new__(
            cls,
            *args,
            date_format=date_format,
            currency_format=currency_format,
            _configuration=_configuration,
            **kwargs,
        )

from ynab_python_sdk.model.currency_format import CurrencyFormat
from ynab_python_sdk.model.date_format import DateFormat
