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


class MonthSummariesResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "server_knowledge",
            "months",
        }
        
        class properties:
            
            
            class months(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['MonthSummary']:
                        return MonthSummary
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['MonthSummary'], typing.List['MonthSummary']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'months':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'MonthSummary':
                    return super().__getitem__(i)
            server_knowledge = schemas.Int64Schema
            __annotations__ = {
                "months": months,
                "server_knowledge": server_knowledge,
            }
    
    server_knowledge: MetaOapg.properties.server_knowledge
    months: MetaOapg.properties.months
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["months"]) -> MetaOapg.properties.months: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["server_knowledge"]) -> MetaOapg.properties.server_knowledge: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["months", "server_knowledge", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["months"]) -> MetaOapg.properties.months: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["server_knowledge"]) -> MetaOapg.properties.server_knowledge: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["months", "server_knowledge", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        server_knowledge: typing.Union[MetaOapg.properties.server_knowledge, decimal.Decimal, int, ],
        months: typing.Union[MetaOapg.properties.months, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MonthSummariesResponseData':
        return super().__new__(
            cls,
            *args,
            server_knowledge=server_knowledge,
            months=months,
            _configuration=_configuration,
            **kwargs,
        )

from ynab_python_sdk.model.month_summary import MonthSummary
