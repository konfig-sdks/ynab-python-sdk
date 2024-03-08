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


class MonthSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "income",
            "deleted",
            "activity",
            "month",
            "to_be_budgeted",
            "budgeted",
        }
        
        class properties:
            month = schemas.DateSchema
            income = schemas.Int64Schema
            budgeted = schemas.Int64Schema
            activity = schemas.Int64Schema
            to_be_budgeted = schemas.Int64Schema
            deleted = schemas.BoolSchema
            
            
            class note(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'note':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class age_of_money(
                schemas.Int32Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int32'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'age_of_money':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "month": month,
                "income": income,
                "budgeted": budgeted,
                "activity": activity,
                "to_be_budgeted": to_be_budgeted,
                "deleted": deleted,
                "note": note,
                "age_of_money": age_of_money,
            }
    
    income: MetaOapg.properties.income
    deleted: MetaOapg.properties.deleted
    activity: MetaOapg.properties.activity
    month: MetaOapg.properties.month
    to_be_budgeted: MetaOapg.properties.to_be_budgeted
    budgeted: MetaOapg.properties.budgeted
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["income"]) -> MetaOapg.properties.income: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budgeted"]) -> MetaOapg.properties.budgeted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activity"]) -> MetaOapg.properties.activity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to_be_budgeted"]) -> MetaOapg.properties.to_be_budgeted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note"]) -> MetaOapg.properties.note: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["age_of_money"]) -> MetaOapg.properties.age_of_money: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["month", "income", "budgeted", "activity", "to_be_budgeted", "deleted", "note", "age_of_money", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["month"]) -> MetaOapg.properties.month: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["income"]) -> MetaOapg.properties.income: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budgeted"]) -> MetaOapg.properties.budgeted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activity"]) -> MetaOapg.properties.activity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to_be_budgeted"]) -> MetaOapg.properties.to_be_budgeted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note"]) -> typing.Union[MetaOapg.properties.note, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["age_of_money"]) -> typing.Union[MetaOapg.properties.age_of_money, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["month", "income", "budgeted", "activity", "to_be_budgeted", "deleted", "note", "age_of_money", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        income: typing.Union[MetaOapg.properties.income, decimal.Decimal, int, ],
        deleted: typing.Union[MetaOapg.properties.deleted, bool, ],
        activity: typing.Union[MetaOapg.properties.activity, decimal.Decimal, int, ],
        month: typing.Union[MetaOapg.properties.month, str, date, ],
        to_be_budgeted: typing.Union[MetaOapg.properties.to_be_budgeted, decimal.Decimal, int, ],
        budgeted: typing.Union[MetaOapg.properties.budgeted, decimal.Decimal, int, ],
        note: typing.Union[MetaOapg.properties.note, None, str, schemas.Unset] = schemas.unset,
        age_of_money: typing.Union[MetaOapg.properties.age_of_money, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MonthSummary':
        return super().__new__(
            cls,
            *args,
            income=income,
            deleted=deleted,
            activity=activity,
            month=month,
            to_be_budgeted=to_be_budgeted,
            budgeted=budgeted,
            note=note,
            age_of_money=age_of_money,
            _configuration=_configuration,
            **kwargs,
        )