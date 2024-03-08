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


class BudgetDetail(
    schemas.ComposedSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    
                    
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
                    
                    
                    class payees(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Payee']:
                                return Payee
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Payee'], typing.List['Payee']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'payees':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Payee':
                            return super().__getitem__(i)
                    
                    
                    class payee_locations(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['PayeeLocation']:
                                return PayeeLocation
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['PayeeLocation'], typing.List['PayeeLocation']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'payee_locations':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'PayeeLocation':
                            return super().__getitem__(i)
                    
                    
                    class category_groups(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['CategoryGroup']:
                                return CategoryGroup
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['CategoryGroup'], typing.List['CategoryGroup']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'category_groups':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'CategoryGroup':
                            return super().__getitem__(i)
                    
                    
                    class categories(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Category']:
                                return Category
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Category'], typing.List['Category']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'categories':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Category':
                            return super().__getitem__(i)
                    
                    
                    class months(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['MonthDetail']:
                                return MonthDetail
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['MonthDetail'], typing.List['MonthDetail']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'months':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'MonthDetail':
                            return super().__getitem__(i)
                    
                    
                    class transactions(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['TransactionSummary']:
                                return TransactionSummary
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['TransactionSummary'], typing.List['TransactionSummary']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'transactions':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'TransactionSummary':
                            return super().__getitem__(i)
                    
                    
                    class subtransactions(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['SubTransaction']:
                                return SubTransaction
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['SubTransaction'], typing.List['SubTransaction']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'subtransactions':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'SubTransaction':
                            return super().__getitem__(i)
                    
                    
                    class scheduled_transactions(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ScheduledTransactionSummary']:
                                return ScheduledTransactionSummary
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['ScheduledTransactionSummary'], typing.List['ScheduledTransactionSummary']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'scheduled_transactions':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ScheduledTransactionSummary':
                            return super().__getitem__(i)
                    
                    
                    class scheduled_subtransactions(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['ScheduledSubTransaction']:
                                return ScheduledSubTransaction
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['ScheduledSubTransaction'], typing.List['ScheduledSubTransaction']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'scheduled_subtransactions':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'ScheduledSubTransaction':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "accounts": accounts,
                        "payees": payees,
                        "payee_locations": payee_locations,
                        "category_groups": category_groups,
                        "categories": categories,
                        "months": months,
                        "transactions": transactions,
                        "subtransactions": subtransactions,
                        "scheduled_transactions": scheduled_transactions,
                        "scheduled_subtransactions": scheduled_subtransactions,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["accounts"]) -> MetaOapg.properties.accounts: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["payees"]) -> MetaOapg.properties.payees: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["payee_locations"]) -> MetaOapg.properties.payee_locations: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["category_groups"]) -> MetaOapg.properties.category_groups: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["categories"]) -> MetaOapg.properties.categories: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["months"]) -> MetaOapg.properties.months: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["subtransactions"]) -> MetaOapg.properties.subtransactions: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["scheduled_transactions"]) -> MetaOapg.properties.scheduled_transactions: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["scheduled_subtransactions"]) -> MetaOapg.properties.scheduled_subtransactions: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["accounts", "payees", "payee_locations", "category_groups", "categories", "months", "transactions", "subtransactions", "scheduled_transactions", "scheduled_subtransactions", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["accounts"]) -> typing.Union[MetaOapg.properties.accounts, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["payees"]) -> typing.Union[MetaOapg.properties.payees, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["payee_locations"]) -> typing.Union[MetaOapg.properties.payee_locations, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["category_groups"]) -> typing.Union[MetaOapg.properties.category_groups, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["categories"]) -> typing.Union[MetaOapg.properties.categories, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["months"]) -> typing.Union[MetaOapg.properties.months, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> typing.Union[MetaOapg.properties.transactions, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["subtransactions"]) -> typing.Union[MetaOapg.properties.subtransactions, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["scheduled_transactions"]) -> typing.Union[MetaOapg.properties.scheduled_transactions, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["scheduled_subtransactions"]) -> typing.Union[MetaOapg.properties.scheduled_subtransactions, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accounts", "payees", "payee_locations", "category_groups", "categories", "months", "transactions", "subtransactions", "scheduled_transactions", "scheduled_subtransactions", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                accounts: typing.Union[MetaOapg.properties.accounts, list, tuple, schemas.Unset] = schemas.unset,
                payees: typing.Union[MetaOapg.properties.payees, list, tuple, schemas.Unset] = schemas.unset,
                payee_locations: typing.Union[MetaOapg.properties.payee_locations, list, tuple, schemas.Unset] = schemas.unset,
                category_groups: typing.Union[MetaOapg.properties.category_groups, list, tuple, schemas.Unset] = schemas.unset,
                categories: typing.Union[MetaOapg.properties.categories, list, tuple, schemas.Unset] = schemas.unset,
                months: typing.Union[MetaOapg.properties.months, list, tuple, schemas.Unset] = schemas.unset,
                transactions: typing.Union[MetaOapg.properties.transactions, list, tuple, schemas.Unset] = schemas.unset,
                subtransactions: typing.Union[MetaOapg.properties.subtransactions, list, tuple, schemas.Unset] = schemas.unset,
                scheduled_transactions: typing.Union[MetaOapg.properties.scheduled_transactions, list, tuple, schemas.Unset] = schemas.unset,
                scheduled_subtransactions: typing.Union[MetaOapg.properties.scheduled_subtransactions, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    accounts=accounts,
                    payees=payees,
                    payee_locations=payee_locations,
                    category_groups=category_groups,
                    categories=categories,
                    months=months,
                    transactions=transactions,
                    subtransactions=subtransactions,
                    scheduled_transactions=scheduled_transactions,
                    scheduled_subtransactions=scheduled_subtransactions,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                BudgetSummary,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BudgetDetail':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from ynab_python_sdk.model.account import Account
from ynab_python_sdk.model.budget_summary import BudgetSummary
from ynab_python_sdk.model.category import Category
from ynab_python_sdk.model.category_group import CategoryGroup
from ynab_python_sdk.model.month_detail import MonthDetail
from ynab_python_sdk.model.payee import Payee
from ynab_python_sdk.model.payee_location import PayeeLocation
from ynab_python_sdk.model.scheduled_sub_transaction import ScheduledSubTransaction
from ynab_python_sdk.model.scheduled_transaction_summary import ScheduledTransactionSummary
from ynab_python_sdk.model.sub_transaction import SubTransaction
from ynab_python_sdk.model.transaction_summary import TransactionSummary