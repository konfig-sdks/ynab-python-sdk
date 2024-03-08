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


class SubTransaction(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "transaction_id",
            "amount",
            "deleted",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            transaction_id = schemas.StrSchema
            amount = schemas.Int64Schema
            deleted = schemas.BoolSchema
            
            
            class memo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'memo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class payee_id(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payee_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class payee_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payee_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class category_id(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'category_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class category_name(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'category_name':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class transfer_account_id(
                schemas.UUIDBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'uuid'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, uuid.UUID, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transfer_account_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class transfer_transaction_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transfer_transaction_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "transaction_id": transaction_id,
                "amount": amount,
                "deleted": deleted,
                "memo": memo,
                "payee_id": payee_id,
                "payee_name": payee_name,
                "category_id": category_id,
                "category_name": category_name,
                "transfer_account_id": transfer_account_id,
                "transfer_transaction_id": transfer_transaction_id,
            }
    
    transaction_id: MetaOapg.properties.transaction_id
    amount: MetaOapg.properties.amount
    deleted: MetaOapg.properties.deleted
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transaction_id"]) -> MetaOapg.properties.transaction_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["memo"]) -> MetaOapg.properties.memo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payee_id"]) -> MetaOapg.properties.payee_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payee_name"]) -> MetaOapg.properties.payee_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_id"]) -> MetaOapg.properties.category_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category_name"]) -> MetaOapg.properties.category_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_account_id"]) -> MetaOapg.properties.transfer_account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transfer_transaction_id"]) -> MetaOapg.properties.transfer_transaction_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "transaction_id", "amount", "deleted", "memo", "payee_id", "payee_name", "category_id", "category_name", "transfer_account_id", "transfer_transaction_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transaction_id"]) -> MetaOapg.properties.transaction_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleted"]) -> MetaOapg.properties.deleted: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["memo"]) -> typing.Union[MetaOapg.properties.memo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payee_id"]) -> typing.Union[MetaOapg.properties.payee_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payee_name"]) -> typing.Union[MetaOapg.properties.payee_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_id"]) -> typing.Union[MetaOapg.properties.category_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category_name"]) -> typing.Union[MetaOapg.properties.category_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_account_id"]) -> typing.Union[MetaOapg.properties.transfer_account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transfer_transaction_id"]) -> typing.Union[MetaOapg.properties.transfer_transaction_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "transaction_id", "amount", "deleted", "memo", "payee_id", "payee_name", "category_id", "category_name", "transfer_account_id", "transfer_transaction_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        transaction_id: typing.Union[MetaOapg.properties.transaction_id, str, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        deleted: typing.Union[MetaOapg.properties.deleted, bool, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        memo: typing.Union[MetaOapg.properties.memo, None, str, schemas.Unset] = schemas.unset,
        payee_id: typing.Union[MetaOapg.properties.payee_id, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        payee_name: typing.Union[MetaOapg.properties.payee_name, None, str, schemas.Unset] = schemas.unset,
        category_id: typing.Union[MetaOapg.properties.category_id, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        category_name: typing.Union[MetaOapg.properties.category_name, None, str, schemas.Unset] = schemas.unset,
        transfer_account_id: typing.Union[MetaOapg.properties.transfer_account_id, None, str, uuid.UUID, schemas.Unset] = schemas.unset,
        transfer_transaction_id: typing.Union[MetaOapg.properties.transfer_transaction_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SubTransaction':
        return super().__new__(
            cls,
            *args,
            transaction_id=transaction_id,
            amount=amount,
            deleted=deleted,
            id=id,
            memo=memo,
            payee_id=payee_id,
            payee_name=payee_name,
            category_id=category_id,
            category_name=category_name,
            transfer_account_id=transfer_account_id,
            transfer_transaction_id=transfer_transaction_id,
            _configuration=_configuration,
            **kwargs,
        )