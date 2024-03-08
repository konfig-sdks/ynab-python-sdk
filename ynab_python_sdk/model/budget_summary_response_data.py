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


class BudgetSummaryResponseData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "budgets",
        }
        
        class properties:
            
            
            class budgets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BudgetSummary']:
                        return BudgetSummary
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['BudgetSummary'], typing.List['BudgetSummary']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'budgets':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'BudgetSummary':
                    return super().__getitem__(i)
        
            @staticmethod
            def default_budget() -> typing.Type['BudgetSummary']:
                return BudgetSummary
            __annotations__ = {
                "budgets": budgets,
                "default_budget": default_budget,
            }
    
    budgets: MetaOapg.properties.budgets
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["budgets"]) -> MetaOapg.properties.budgets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_budget"]) -> 'BudgetSummary': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["budgets", "default_budget", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["budgets"]) -> MetaOapg.properties.budgets: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_budget"]) -> typing.Union['BudgetSummary', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["budgets", "default_budget", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        budgets: typing.Union[MetaOapg.properties.budgets, list, tuple, ],
        default_budget: typing.Union['BudgetSummary', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BudgetSummaryResponseData':
        return super().__new__(
            cls,
            *args,
            budgets=budgets,
            default_budget=default_budget,
            _configuration=_configuration,
            **kwargs,
        )

from ynab_python_sdk.model.budget_summary import BudgetSummary
