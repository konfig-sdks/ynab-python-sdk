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


class BudgetSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "id",
        }
        
        class properties:
            id = schemas.UUIDSchema
            name = schemas.StrSchema
            last_modified_on = schemas.DateTimeSchema
            first_month = schemas.DateSchema
            last_month = schemas.DateSchema
        
            @staticmethod
            def date_format() -> typing.Type['DateFormat']:
                return DateFormat
        
            @staticmethod
            def currency_format() -> typing.Type['CurrencyFormat']:
                return CurrencyFormat
            
            
            class accounts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Account']:
                        return Account
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['Account'], typing.List['Account']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accounts':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Account':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "name": name,
                "last_modified_on": last_modified_on,
                "first_month": first_month,
                "last_month": last_month,
                "date_format": date_format,
                "currency_format": currency_format,
                "accounts": accounts,
            }
    
    name: MetaOapg.properties.name
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_modified_on"]) -> MetaOapg.properties.last_modified_on: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_month"]) -> MetaOapg.properties.first_month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_month"]) -> MetaOapg.properties.last_month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_format"]) -> 'DateFormat': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency_format"]) -> 'CurrencyFormat': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "name", "last_modified_on", "first_month", "last_month", "date_format", "currency_format", "accounts", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_modified_on"]) -> typing.Union[MetaOapg.properties.last_modified_on, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_month"]) -> typing.Union[MetaOapg.properties.first_month, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_month"]) -> typing.Union[MetaOapg.properties.last_month, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_format"]) -> typing.Union['DateFormat', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency_format"]) -> typing.Union['CurrencyFormat', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accounts"]) -> typing.Union[MetaOapg.properties.accounts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "name", "last_modified_on", "first_month", "last_month", "date_format", "currency_format", "accounts", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, ],
        last_modified_on: typing.Union[MetaOapg.properties.last_modified_on, str, datetime, schemas.Unset] = schemas.unset,
        first_month: typing.Union[MetaOapg.properties.first_month, str, date, schemas.Unset] = schemas.unset,
        last_month: typing.Union[MetaOapg.properties.last_month, str, date, schemas.Unset] = schemas.unset,
        date_format: typing.Union['DateFormat', schemas.Unset] = schemas.unset,
        currency_format: typing.Union['CurrencyFormat', schemas.Unset] = schemas.unset,
        accounts: typing.Union[MetaOapg.properties.accounts, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BudgetSummary':
        return super().__new__(
            cls,
            *args,
            name=name,
            id=id,
            last_modified_on=last_modified_on,
            first_month=first_month,
            last_month=last_month,
            date_format=date_format,
            currency_format=currency_format,
            accounts=accounts,
            _configuration=_configuration,
            **kwargs,
        )

from ynab_python_sdk.model.account import Account
from ynab_python_sdk.model.currency_format import CurrencyFormat
from ynab_python_sdk.model.date_format import DateFormat
